---
title: "How to Fix the Feature Experience Pack Failed to Install on Windows 11"
slug: "how-to-fix-feature-experience-pack-failed-to-install-on-windows-11"
date: 2026-09-08
categories: ["windows-update"]
tags: ["feature experience pack", "windows update", "windows 11", "failed to install"]
description: "Feature Experience Pack failed to install on Windows 11? Six fixes for prerequisites, cache corruption, disabled services, and manual Catalog installs."
thumbnail: "/images/thumbs/how-to-fix-feature-experience-pack-failed-to-install-on-windows-11.webp"
faqs:
  - q: "What is the Feature Experience Pack on Windows 11?"
    a: "The Windows Feature Experience Pack updates select Windows shell and feature components outside the full OS upgrade cycle. On Windows 11 it arrives via Windows Update as a small package. Its contents are incremental experience refinements rather than security fixes, which is why a failed install is best treated as a diagnostic signal about your update pipeline’s health, not as a critical missing update."
  - q: "Is the pack required for security?"
    a: "Not for security — security arrives through cumulative updates, which are independent of the pack. But do not ignore it either: the same cache corruption, disabled services, or servicing damage blocking the pack will block the next cumulative update. Fix the underlying pipeline using the steps here, and both the pack and future updates install normally."
  - q: "Does the pack need a prerequisite update?"
    a: "Sometimes. The pack’s installer can require a minimum servicing stack or cumulative update level. If your Windows 11 is behind on updates, install the latest cumulative update first — automatically or manually from the Microsoft Update Catalog — then retry the pack. Skipping the prerequisite is a common hidden cause of repeated pack failures."
  - q: "Where can I see the failed pack in update history?"
    a: "Open Settings, then Windows Update, then Update history, and look under the relevant category for the failed Feature Experience Pack entry with its error code. If the entry is missing, simply run Check for updates — once the pipeline is repaired, Windows re-offers the pack automatically and the new attempt appears in the history."
---

On Windows 11 the Feature Experience Pack is a small, quiet package — and when it fails to install, it fails quietly too, reappearing in Windows Update day after day. The pack’s actual contents are minor shell refinements, so the real cost of the failure is what it signals: something in the update pipeline is wrong, and bigger updates will trip over the same problem soon.

The Windows 10 version of this failure behaves slightly differently and is covered in the [Windows 10 pack guide](/articles/how-to-fix-feature-experience-pack-failed-to-install-on-windows-10/). On Windows 11, the fix path runs through servicing prerequisites, cache resets, and the services that deliver the pack.

## Why this happens

- **Pack delivered through a jammed update queue:** On Windows 11 the pack flows through the normal update pipeline; a stuck queue blocks it like any other payload.
- **Corrupted update cache metadata:** Damaged metadata makes the small pack fail integrity checks despite its tiny download size.
- **Missing prerequisite servicing updates:** The pack can require a minimum servicing stack or cumulative level; without it, the installer refuses the package.
- **Disabled update services:** Tweaking tools that disable wuauserv or BITS break the pack’s delivery while Windows otherwise looks healthy.
- **Metered connection deferral:** As non-critical content, the pack waits indefinitely on metered connections.
- **Shell component corruption:** The pack updates shell-adjacent components; damaged base files cause apply-time failures.
- **Staging permission damage:** ACL damage on staging folders produces access-denied failures for the pack installer.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Update the servicing base first

The pack builds against a recent servicing baseline. An outdated stack or cumulative level fails its prerequisite check silently. Updating the base first is the prerequisite most people skip — and the fix for the most stubborn pack failures.

1. Install all pending updates in Settings > Windows Update, especially any servicing stack or cumulative updates.
2. Restart when prompted.
3. Run Check for updates again and look for the Feature Experience Pack.
4. Install it on the current base.

### Fix 2: Reset the update cache

A handful of corrupt metadata bytes can block this small package indefinitely. The standard reset clears the corruption in minutes and is the highest-yield fix for pack failures on otherwise healthy systems.

1. Elevated Terminal: net stop wuauserv, net stop bits, net stop cryptSvc.
2. Rename: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
3. Restart services: net start wuauserv, net start bits, net start cryptSvc.
4. Check for updates; the pack reappears with fresh metadata.

### Fix 3: Repair system files with DISM and SFC

Because the pack applies to shell components, damage in the underlying files fails the install at apply time. DISM repairs the store, SFC repairs the files — the standard repair pair for apply-time package failures.

1. Open an elevated Terminal.
2. Run: DISM /Online /Cleanup-Image /RestoreHealth.
3. Run: sfc /scannow.
4. Restart, then retry the pack.

### Fix 4: Re-enable disabled update services

Debloat scripts commonly disable these services, breaking the pack’s delivery channel while everything else seems fine. The pack cannot arrive with its transport switched off.

1. Open services.msc and check Windows Update and Background Intelligent Transfer Service.
2. If Disabled, set to Manual (Trigger Start) and start them.
3. Check the [Windows Update support hub](https://support.microsoft.com/en-us/windows) if services refuse to stay running.
4. Retry the pack install.

### Fix 5: Rule out metered deferral

Non-critical payloads are metering’s first victims. If cumulative updates succeed while only the pack fails, a metered flag is the likely discriminator.

1. Check the metered toggle: Settings > Network & internet > Wi-Fi > your network.
2. Switch Metered connection off, or enable “Download updates over metered connections” under Windows Update > Advanced options.
3. Retry the pack.
4. Details: the [Windows 11 metered-connection guide](/articles/how-to-fix-metered-connection-blocking-windows-update-on-windows-11/).

### Fix 6: Install the pack manually from the Catalog

The Catalog’s standalone package bypasses the Windows Update client entirely. Success here proves the system is healthy and isolates the fault to the client pipeline — which the earlier fixes repair.

1. Find the pack’s KB in Update history.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Install the package manually and restart.
4. Confirm the entry shows installed, then verify automatic updates work next cycle.

### Fix 7: Decode the pack’s error code instead of retrying blindly

The Feature Experience Pack’s failure always leaves an error code in Update history, and that code names the actual problem — yet most users retry without reading it. Common codes: 0x80070002 means the package files never staged (reset the cache), 0x80070005 means the installer was denied access (check antivirus and permissions), and 0x800f081f means the component store cannot supply the files (run DISM). Reading the code first converts the pack failure from a mystery into a fifteen-minute targeted repair, and the same code-reading habit speeds up every other Windows Update failure you will ever meet. Keep a note of the code and the fix that worked; if the pack fails again next cycle with the same code, you will know the underlying issue was never truly resolved.

1. Open Settings > Windows Update > Update history and find the failed Feature Experience Pack entry.
2. Write down the exact error code (for example, 0x80070002).
3. Match it: 0x80070002 → re-download via cache reset; 0x80070005 → permissions/antivirus; 0x800f081f/0x80073712 → DISM store repair.
4. Apply the matching fix from this guide’s earlier sections.
5. Retry the pack and confirm the history entry flips to installed.
6. Document the code and fix — recurring identical codes mean a deeper issue worth investigating.

## Closing

On Windows 11 the Feature Experience Pack is a canary: its failure rarely matters for its own sake, but it reliably signals pipeline trouble that the next cumulative update will hit too. Update the servicing base, reset the cache, re-enable the services, and the pack — and everything after it — installs cleanly.
