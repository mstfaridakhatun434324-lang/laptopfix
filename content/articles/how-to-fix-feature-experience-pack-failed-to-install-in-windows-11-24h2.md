---
title: "Windows Feature Experience Pack Failed to Install on 24H2? Here's the Fix"
slug: how-to-fix-feature-experience-pack-failed-to-install-in-windows-11-24h2
date: 2026-09-30
categories: ["windows-update"]
tags: ["feature experience pack", "windows 11 24h2", "update failed", "0x800f081f"]
description: "The Windows Feature Experience Pack keeps failing to install on Windows 11 24H2? Understand what it is, why it fails, and how to get it installed."
thumbnail: "/images/thumbs/how-to-fix-feature-experience-pack-failed-to-install-in-windows-11-24h2.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "It's a small Microsoft package that delivers improvements to Windows features outside the normal update cycle — things like the Snipping Tool, touch keyboard, and shell components. It installs through Windows Update like any other update, and when it fails you'll see it listed separately in your update history with its own error code."
  - q: "Can I safely ignore a failed Feature Experience Pack?"
    a: "Mostly yes — it's not a security update, so skipping it won't leave you vulnerable. But repeated failures often signal deeper servicing-stack problems that will eventually block important cumulative updates too. It's worth fixing the underlying cause rather than ignoring the symptom."
  - q: "Why does it fail with error 0x800F081F?"
    a: "Error 0x800F081F means Windows couldn't find the source files it needs, usually because the component store is corrupt or a required manifest is missing. Running DISM with the RestoreHealth switch rebuilds the component store from known-good copies and is the standard fix for this specific error."
  - q: "Does the Feature Experience Pack require a restart?"
    a: "Usually not a full restart — most versions apply silently in the background. If Windows Update shows it as 'pending restart,' though, let the restart happen; the pack finalizes shell components that can't be swapped while Explorer is running, and skipping it can leave the install half-applied."
---

Of all the things Windows Update can fail on, the Feature Experience Pack is the most baffling. It's small — often under 100 MB. It's not a security patch, not a driver, not a feature update. It's a bundle of minor improvements to built-in Windows features, and yet it can fail repeatedly with cryptic errors while everything else installs fine. You retry, it downloads, it churns for a while, and then: "Failed to install." No useful explanation, just a hex code if you're lucky.

The reason it's worth fixing — despite being non-critical — is what the failure tells you. The Feature Experience Pack exercises the same servicing machinery (the component store, the package manager, the manifest system) as every other update. When it fails, that machinery is damaged, and it's only a matter of time before a cumulative security update fails the same way. On Windows 11 24H2, where Microsoft delivers more through these packs than before, the fixes below restore the whole pipeline.

## Why this happens

- **Corrupt component store**: The WinSxS store that holds package manifests is damaged, so the installer can't verify the pack's files.
- **Missing source files (0x800F081F)**: Windows can't locate the payload it needs, usually after a cleanup tool aggressively purged the store.
- **Stuck pending operations**: A previous update left "pending.xml" operations that block any new package from installing.
- **Corrupt SoftwareDistribution cache**: The downloaded pack itself is damaged and fails hash verification on every retry.
- **Servicing stack out of date**: The underlying servicing stack update (SSU) that the pack depends on never installed properly.
- **Third-party "debloater" tools**: Scripts that strip Windows components often remove manifests the Experience Pack expects to update.
- **Insufficient reserved storage**: The pack needs working space in the system reserved areas; a nearly full drive blocks it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the actual error code first

Don't treat all failures the same. The error code in Update history tells you which fix to prioritize and saves you from doing all seven.

1. Go to **Settings > Windows Update > Update history**.
2. Expand **Other updates** or **Quality updates** and find the Feature Experience Pack entry.
3. Note the exact error code (common ones: 0x800F081F, 0x80073701, 0x8024002E).
4. 0x800F081F points to component store damage (Fix 3). 0x8024002E means the update service is blocked (see our [update service guide](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/)).
5. 0x80073701 indicates a missing referenced assembly — also a DISM job.

### Fix 2: Clear the download cache and retry cleanly

A corrupt download is the simplest cause and the fastest to rule out. Windows will re-download the pack from scratch.

1. Open **Command Prompt as administrator**.
2. Run `net stop wuauserv` and `net stop bits`.
3. Open File Explorer and delete everything inside `C:\Windows\SoftwareDistribution\Download`.
4. Run `net start wuauserv` and `net start bits`.
5. Go to **Settings > Windows Update** and click **Check for updates**.
6. If the pack fails again with the same code, the download wasn't the problem — continue.

### Fix 3: Repair the component store with DISM

This is the core fix for Feature Experience Pack failures. DISM rebuilds the WinSxS component store that the pack's installer depends on.

1. Open **Command Prompt as administrator**.
2. Run `DISM /Online /Cleanup-Image /ScanHealth` to assess the damage.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` — this takes 10–30 minutes and needs internet access.
4. Follow with `sfc /scannow` to repair any protected system files.
5. Restart the laptop.
6. Retry the Feature Experience Pack from Windows Update.
7. If DISM itself fails with 0x800F081F, you need an offline source: mount a Windows 11 24H2 ISO and run `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\Sources\install.wim:1` (adjust the drive letter). ISOs are available from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

### Fix 4: Install the latest servicing stack update manually

The pack depends on the servicing stack — the low-level engine that installs packages. If the SSU is outdated or damaged, everything built on it fails.

1. Check your installed SSU version in **Settings > Windows Update > Update history** — look for "Servicing Stack" entries.
2. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search "servicing stack update Windows 11 24H2".
3. Download the latest SSU for your architecture (x64 for most laptops).
4. Install the `.msu` file and restart when prompted.
5. Retry the Feature Experience Pack — with a healthy servicing stack it usually goes through.

### Fix 5: Clear pending operations blocking the installer

A stuck `pending.xml` from an interrupted earlier update will block every subsequent package install with assembly errors.

1. Open **Command Prompt as administrator**.
2. Run `dism /online /cleanup-image /startcomponentcleanup` to clear superseded components.
3. Check `C:\Windows\WinSxS\pending.xml` — if it exists and is old, the pending operations are stale.
4. Run `DISM /Online /Cleanup-Image /RestoreHealth` again to reconcile the store.
5. Restart and retry the pack installation.
6. Avoid force-restarting during future updates — that's how pending.xml gets stuck in the first place.

### Fix 6: Undo damage from debloater scripts

If you (or a "tweaking" guide) ran a script that removed Windows components, the Experience Pack may be trying to update files that no longer exist. This is depressingly common.

1. Think back: did you run any debloating, "privacy," or component-removal script? Tools like these often strip the shell components the pack updates.
2. The reliable fix is an **in-place upgrade**: mount a Windows 11 24H2 ISO and run `setup.exe`, choosing **Keep personal files and apps**.
3. This reinstalls all system components — including the ones the script removed — without touching your data.
4. After the in-place upgrade completes, the Feature Experience Pack installs normally.
5. Avoid re-running the debloater afterward, or you'll be back here next month. For related post-reinstall update issues, see our guide to [update errors after a clean install](/articles/how-to-fix-windows-update-error-after-clean-install-in-windows-11-24h2/).

### Fix 7: Free space and install the pack standalone

If the drive is nearly full, the pack can't stage its files. And as a final fallback, the standalone installer bypasses Windows Update entirely.

1. Free at least 10 GB: run **Settings > System > Storage > Temporary files** and clear categories you don't need.
2. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for "Feature Experience Pack" plus your build number.
3. Download the matching `.msu` and install it directly.
4. Check **Settings > System > About** afterward — the Experience Pack version should reflect the new install.
5. If even the standalone installer fails, the in-place upgrade from Fix 6 is the definitive repair.

## Closing

The Feature Experience Pack is small, but its failures are a canary in the coal mine for your servicing stack. DISM's RestoreHealth fixes the overwhelming majority of cases by rebuilding the component store the pack depends on. Get it installing cleanly and you've also hardened the pipeline for the cumulative updates that actually matter — the ones carrying security fixes you can't afford to miss.
