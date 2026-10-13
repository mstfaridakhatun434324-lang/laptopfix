---
title: "Feature Experience Pack Failed to Install? 7 Fixes for Windows Update"
slug: troubleshoot-feature-experience-pack-failed-to-install
date: 2026-09-21
categories: ["windows-update"]
tags: ["feature experience pack", "windows update", "install failed", "windows 11", "troubleshooting"]
description: "The Windows Feature Experience Pack keeps failing to install? These 7 fixes clear the blockers — from cache resets to manual installation — so the pack finally lands."
thumbnail: "/images/thumbs/troubleshoot-feature-experience-pack-failed-to-install.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "The Windows Feature Experience Pack is a small Microsoft package that updates select shell and UI features — things like the Snipping Tool, input components, and Start menu elements — independently of full OS builds. It lets Microsoft ship feature improvements through Windows Update without waiting for a feature release. It is not critical to system stability, but its failure often signals a broader update problem worth fixing."
  - q: "Why does the Feature Experience Pack fail to install?"
    a: "The usual causes mirror other small-package failures: a corrupted update cache delivering a damaged download, a damaged component store, third-party antivirus interfering with the install, or a pending restart from a previous update blocking new installs. Occasionally the pack itself has a bad release, in which case waiting for the revised version is the fix."
  - q: "Can I ignore the Feature Experience Pack failure?"
    a: "You can survive without it — it delivers minor features, not security fixes. But ignoring it is unwise if the failure indicates a sick update pipeline, because the same corruption will eventually block security updates too. Fix the underlying issue using this guide, and the pack will install as a side effect."
  - q: "How is the Feature Experience Pack different from a feature update?"
    a: "A feature update (like 24H2) is a full OS build upgrade — gigabytes, long install, new build number. The Feature Experience Pack is a tiny package (tens of megabytes) that updates individual Windows features through the regular cumulative update channel. It installs in minutes and never changes your build number."
---

The Windows Feature Experience Pack is one of those updates you never asked for and barely notice — until it starts failing. Then it sits in your update history with a red "failed to install" badge, retries on every update check, and fails again, each time with an unhelpful error code. It is a small package delivering minor shell and feature improvements, so the failure is not an emergency — but it is a symptom. The same corruption that blocks this little pack will eventually block the security updates that actually matter.

The failure causes are the familiar ones in miniature: a corrupted download in the update cache, a damaged component store, antivirus interference, or a pending restart holding the installer hostage. Because the pack is small, the fixes are quick — most people resolve it in under half an hour. Work through the seven below in order, and the pack will install as a side effect of a healthier update pipeline.

## Why this happens

- **Corrupted update cache.** A damaged download of the pack fails verification on every retry.
- **Damaged component store.** The installer cannot stage the pack's files against a broken store.
- **Pending restart.** A previous update awaiting reboot blocks new package installs.
- **Antivirus interference.** Third-party security software blocking the pack's installer.
- **Corrupted system files.** Broader file damage affecting the installer components.
- **Bad pack release.** Occasionally Microsoft ships a pack version with a defect, later revised.
- **Metered connection or paused updates.** Network policies interrupting the small download mid-stream.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and retry — clear the pending state

The simplest cause is the most common: a pending restart from another update is blocking the pack.

1. Save your work and do a full **Restart** (not shutdown — restart clears pending states that shutdown with fast startup preserves).
2. After rebooting, go to **Settings > Windows Update** and click **Check for updates**.
3. Let the Feature Experience Pack attempt its install.
4. If it succeeds, you are done — the blocker was a pending operation. If it fails again with the same code, continue; the problem is in the package or the pipeline.

### Fix 2: Run the Windows Update troubleshooter

Let the automated tool clear the surface-level issues first.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and apply any fixes.
3. Restart the laptop and check for updates again.
4. The troubleshooter handles corrupted download states and stuck service configurations — the easy wins. If it reports it fixed something but the pack still fails, the cache itself likely needs the manual reset in Fix 4.

### Fix 3: Check for a revised pack version

Sometimes the problem is the package, not your machine. Microsoft occasionally revises a bad pack release.

1. In **Settings > Windows Update > Update history**, note the exact KB number and version of the failing pack.
2. Search that KB on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) to see if a newer revision exists.
3. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for any advisory about the pack version.
4. If a newer revision exists, the catalog download (Fix 6) gets it directly; if the pack was pulled entirely, hiding the update and waiting a week is the correct move — not fighting a withdrawn package.

### Fix 4: Reset the update cache manually

A corrupted cached copy of the pack fails identically on every retry. Force Windows to download it fresh.

1. Open Command Prompt as administrator.
2. Stop the services:
   ```
   net stop wuauserv
   net stop bits
   net stop cryptsvc
   ```
3. Rename the caches:
   ```
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   ```
4. Restart the services and check for updates. For small packages like the Experience Pack, a fresh download usually installs on the first try. This same reset is the core of our [update database error repair guide](/articles/how-to-fix-windows-update-database-error-on-windows-11/).

### Fix 5: Temporarily disable third-party antivirus

Small packages with shell components are exactly what heuristic antivirus engines sometimes flag mid-install.

1. Disable **real-time protection** in your third-party antivirus temporarily.
2. Run the update check and let the pack install.
3. Re-enable protection immediately afterward.
4. If this was the blocker, add the Windows Update working directories to your antivirus exclusions — or consider whether Windows Security alone meets your needs, since it never conflicts with updates.

### Fix 6: Install the pack manually from the Update Catalog

Bypass Windows Update entirely with the standalone package.

1. Find the pack's KB number in your update history.
2. Search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and download the x64 `.msu` (or `.cab`) for your build.
3. Run the installer as administrator and let it complete.
4. Restart and verify in update history. A successful manual install proves the package is fine and the automated pipeline was the problem — the cache reset in Fix 4 usually keeps it healthy going forward.

### Fix 7: Repair the component store and system files

If the pack fails even manually, the installation machinery itself is damaged.

1. In an elevated prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` (15–30 minutes).
2. Follow with `sfc /scannow` to full completion.
3. Restart and retry the update check — first the automated way, then manually if needed.
4. After the pack installs, run one more update check to confirm the pipeline is healthy: if the pack was the canary, the mine is now clear. For persistent pipeline issues beyond this, our [troubleshooter repair guide](/articles/troubleshoot-windows-update-troubleshooter-not-working/) covers the diagnostic infrastructure.

## Closing

A failing Feature Experience Pack is rarely about the pack — it is the canary in your update pipeline, and its failure points at cache corruption, a damaged component store, or antivirus interference. The cache reset and manual catalog install resolve nearly every case, and fixing the underlying issue protects the security updates that actually matter. Small package, useful warning, quick fix.
