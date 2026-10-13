---
title: "Windows 11 'Undoing Changes Made to Your Computer': Complete Fix Guide"
slug: how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-windows
date: 2026-10-11
categories: ["windows-update"]
tags: ["undoing changes made to your computer", "windows 11", "update rollback", "windows update failed", "undoing changes"]
description: "The complete guide to fixing 'Undoing changes made to your computer' on Windows 11 — from the stuck screen to permanent repair."
thumbnail: "/images/thumbs/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-windows.webp"
faqs:
  - q: "Is it safe to turn off my PC while it says 'Undoing changes'?"
    a: "Not during the first hour — interrupting a rollback mid-write can leave the system unbootable. After two to three hours with genuinely no progress (no disk activity, no screen change), a forced shutdown becomes the reasonable move; Windows usually resumes or completes the rollback on the next boot. Patience first, force second, and never as the opening move."
  - q: "Will the rollback uninstall my programs?"
    a: "No. Rollback reverses the update system files only — your installed programs, settings, and personal files remain. In rare cases a program installed between the update start and the rollback can behave oddly, but a reinstall fixes that. Your data and applications are not the rollback target."
  - q: "How do I stop Windows from retrying the same failing update?"
    a: "Use 'Pause updates' in Settings → Windows Update for up to five weeks while you fix the root cause — pausing is better than letting it fail monthly. For a specific bad driver delivered via update, the 'Show or hide updates' troubleshooter can hide it. But pausing is a delaying tactic; the goal is fixing the blocker, then unpausing."
  - q: "When should I give up and reinstall Windows?"
    a: "When you have cleared the cache, repaired servicing with DISM/SFC, updated all drivers, tested without third-party interference, tried a manual install, and run an in-place upgrade — and the same update still rolls back. At that point a clean install (with backups) is faster than further diagnosis. Most users never reach this step; the in-place upgrade resolves nearly everything."
---

It is the most deflating screen in Windows: after a long update, your PC announces it is **"Undoing changes made to your computer"** — and then takes its time doing it. On **Windows 11** this loop has a well-mapped anatomy: the update fails for a specific reason, the rollback protects you from the half-installed state, and the same failure repeats until the underlying trigger is fixed.

This is the complete guide: what the screen means, how long to wait, how to escape a stuck rollback, and — most importantly — how to fix the trigger so it never comes back. It is written for Windows 11 generally, with the version-specific and brand-specific variants linked where they matter.

The single most important habit: read the error code in Update history before doing anything else. Everything in this guide branches from that code. For the 24H2-specific quirks of this failure, see the [24H2 undoing-changes guide](/articles/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-in-windows/).

## Why this happens

- **Driver migration failures:** The top cause: a driver the new build cannot migrate, aborting the install.
- **Corrupted servicing stack:** Damaged component store failing every update identically.
- **Bad update downloads:** Corrupted files in the update cache failing integrity checks.
- **Disk space exhaustion:** Too little room for install plus rollback data.
- **Third-party software blocking:** Antivirus, encryption, or utilities intercepting update operations.
- **Firmware compatibility gates:** BIOS/TPM/secure-boot checks failing silently before install.
- **Stuck update services:** Windows Update or BITS wedged, poisoning every attempt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Escape the stuck screen safely

Under two hours on the rollback screen: wait, plugged in, doing nothing — most rollbacks finish. Past three hours with no disk activity and no screen change: force power off, wait 30 seconds, power on. Windows typically resumes the rollback or boots to the desktop with the update marked failed. Once at the desktop, open Update history and write down the failed KB and its error code before touching anything else.

1. Wait at least two hours on the rollback screen, plugged in.
2. Truly stuck (3+ hours, no activity): force off, wait, power on.
3. Let Windows finish booting or resume the rollback.
4. Record the failed KB number and error code from Update history.

### Fix 2: Classify the error code

The code chooses your fix: 0xC1900101 family → drivers; 0x800F0922 / 0x80073712 → servicing corruption; 0x80070070 → disk space; 0x80070002 / 0x80070003 → corrupted download; 0x80240034 or service errors → stuck services. Write the code down and jump to its fix — this classification is the difference between a twenty-minute repair and a weekend of guessing. The [error-code repair guide](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-after-windows-11-upd/) expands each family.

1. Expand the failed update in Update history; copy the full code.
2. Match it to driver / servicing / space / download / service family.
3. Go directly to the matching fix below.
4. Unlisted code: search the exact string, then try the cache clear.

### Fix 3: Clear the update cache and restart the services

The universal first repair regardless of family: run the Windows Update troubleshooter, then stop the Windows Update and BITS services, delete the contents of `C:\Windows\SoftwareDistribution\Download`, and restart the services. Corrupted downloads and wedged service states cause an enormous share of rollbacks, and this reset is harmless. Check for updates afterward to force a clean re-download.

1. Run Settings → System → Troubleshoot → Windows Update.
2. Stop Windows Update and BITS services.
3. Delete the SoftwareDistribution\Download contents.
4. Restart services; check for updates.

### Fix 4: Fix the driver family: update everything that migrates

For driver codes, update chipset, storage, display, network, audio, and biometric drivers from your laptop maker support page — not just Windows Update. Uninstall any driver the error names, disconnect external USB devices, and retry once. Driver migration failures are the most common rollback cause on laptops precisely because of the deep OEM driver stack; the maker-validated versions exist for this reason.

1. Update all maker-validated drivers, especially chipset/storage.
2. Uninstall drivers named in the error; disconnect USB extras.
3. Retry the update exactly once.
4. Still failing: note whether the code changed — progress matters.

### Fix 5: Repair servicing and free space

For servicing codes: elevated `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`, restart. For space codes: Disk Cleanup as administrator with system files, targeting old Windows installations — secure 20 GB+ free. These two repairs address the "fails identically every time" pattern: corruption and space do not fix themselves between attempts, so every retry without them is another scheduled rollback.

1. Run DISM restore-health and SFC; restart.
2. Free 20 GB+ with elevated Disk Cleanup.
3. Confirm repairs reported clean.
4. Retry the update once.

### Fix 6: Remove interference and install manually

Temporarily disable third-party antivirus and pause encryption, then retry — interference failures mimic other codes. If it still fails, install manually: download the KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and run the .msu. Manual installs bypass pipeline failures and give clearer errors. Document each attempt result; the pattern of what changed is diagnostic gold. Microsoft documents the manual process in [Windows support](https://support.microsoft.com/en-us/windows).

1. Disable AV and pause encryption; retry once.
2. Still failing: download the KB from the Update Catalog.
3. Install the .msu manually; record the exact outcome.
4. Same code again: system-state repair is next.

### Fix 7: In-place upgrade: the definitive repair

Back up, then run the Windows 11 installer from [Microsoft software download](https://www.microsoft.com/en-us/software-download/windows11): Upgrade → keep files and apps. This rebuilds the update engine, servicing stack, and driver base while preserving your data — it resolves chronic rollback loops that survive every targeted fix. Afterward, install the previously failing update promptly to confirm the loop is broken, then unpause updates.

1. Back up personal files.
2. Run the installer → Upgrade → keep files and apps (plugged in).
3. Install the previously failing update; confirm success.
4. Unpause updates and monitor the next Patch Tuesday.

## Closing

The "Undoing changes" loop ends when its trigger is fixed, not when the update is retried: escape the stuck screen safely, read the error code, clear the cache, fix the driver or servicing family it points to, remove interference, install manually, and repair in place as the final answer. Worked once, properly, Patch Tuesday goes back to being uneventful.
