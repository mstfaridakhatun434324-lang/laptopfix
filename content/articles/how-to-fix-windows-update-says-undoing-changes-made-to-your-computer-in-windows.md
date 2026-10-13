---
title: "Fix 'Undoing Changes Made to Your Computer' in Windows 11 24H2"
slug: how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-in-windows
date: 2026-10-07
categories: ["windows-update"]
tags: ["undoing changes made to your computer", "windows 11 24h2", "update failed", "windows update stuck", "undoing changes"]
description: "Stuck on 'Undoing changes made to your computer' in Windows 11 24H2? Here is how to break the loop and get updates installing."
thumbnail: "/images/thumbs/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-in-windows.webp"
faqs:
  - q: "What does 'Undoing changes made to your computer' actually mean?"
    a: "It means a Windows update failed to install completely, so Windows is rolling the system back to its pre-update state. The rollback itself is normal and protective — the problem is only when it loops repeatedly or takes hours. One occurrence is Windows doing its job; a loop is Windows failing at it."
  - q: "How long should the 'Undoing changes' screen take?"
    a: "Typically 15 minutes to an hour depending on drive speed and update size. Beyond two to three hours with no progress, the rollback itself is likely stuck. Do not power off during the first hour — interrupting a rollback mid-write is how systems end up unbootable. Patience first, intervention after."
  - q: "Will I lose my files when Windows undoes the changes?"
    a: "No. The rollback reverses system files and update components only; your documents, photos, and personal files are untouched. In thousands of these cases, personal data survives intact. Still, if you can boot, back up critical files before attempting repairs — not because the rollback threatens them, but because any OS-level repair deserves a backup."
  - q: "Why does this keep happening with every update?"
    a: "Recurring rollbacks point at a persistent blocker: corrupted update components, a driver that fails to migrate, insufficient disk space, or third-party software (especially antivirus or disk encryption) interfering with the install. Fixing the trigger once — rather than retrying the same update — is what breaks the cycle."
---

Your laptop restarted for updates and now it says **"Undoing changes made to your computer"** — and it has said that for a very long time. On **Windows 11 24H2** this screen has become a familiar dread: an update failed partway, Windows is rolling back, and sometimes the rollback itself stalls or the same failure repeats with every Patch Tuesday.

The good news is that this is one of the most diagnosable Windows problems. The failure leaves traces — error codes in update history, stuck services, corrupted caches — and each trace points at a specific fix. This guide is ordered for 24H2 specifically, accounting for that release update-engine quirks and driver-migration issues.

First rule: if the screen has been up less than an hour, wait. Rollbacks on slow drives legitimately take a while, and interrupting one is the fastest route to an unbootable system. If it has been hours, or if this is the third Tuesday in a row, start below. For the general stuck-rollback case, the [undoing changes stuck guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/) covers non-24H2 specifics.

## Why this happens

- **Failed driver migration during the update:** A driver that cannot migrate to the new build aborts the install and triggers rollback.
- **Corrupted update cache:** Damaged downloaded update files failing integrity checks mid-install.
- **Insufficient disk space for the rollback:** The update needs room for both install and rollback data; tight drives fail both.
- **Third-party antivirus interference:** Real-time protection blocking update file operations at the critical moment.
- **Corrupted servicing stack:** Damaged component store making every update attempt fail identically.
- **24H2-specific driver incompatibilities:** Older drivers (especially storage and biometric) that 24H2 update engine rejects.
- **Interrupted previous update:** A half-applied earlier update leaving the system in a state the next update cannot build on.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait it out — then force your way to the desktop

If the rollback screen has been up under two hours, give it time with the laptop plugged in. Past three hours with zero change, hold the power button to force off, wait 30 seconds, and power on — Windows usually completes the rollback on the next boot or lands you at the desktop with the update marked failed. If it boots normally, you are now in repair position; do not simply retry the update yet.

1. Wait at least two hours on the rollback screen, plugged in.
2. No progress after three hours: force power off, wait 30 seconds.
3. Power on and let Windows finish booting (it may resume the rollback).
4. At the desktop: note the failed update in Settings → Windows Update → Update history.

### Fix 2: Run the Windows Update troubleshooter and clear the cache

The built-in troubleshooter (Settings → System → Troubleshoot → Other troubleshooters → Windows Update) fixes the common stuck states automatically. Then clear the corrupted cache manually: stop the Windows Update and BITS services, delete the contents of `C:\Windows\SoftwareDistribution\Download`, restart the services. This forces a clean re-download and resolves the largest single category of repeat rollbacks.

1. Run the Windows Update troubleshooter and apply its fixes.
2. Stop the Windows Update and Background Intelligent Transfer services.
3. Delete everything in `C:\Windows\SoftwareDistribution\Download`.
4. Restart the services and check for updates again.

### Fix 3: Free disk space and repair the servicing stack

Updates need generous free space — aim for 20 GB+ free before retrying. Run Disk Cleanup as administrator including system files. Then repair the component store that every update builds on: elevated `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`. A corrupted servicing stack makes every update fail identically, so this repair breaks the "fails every month" pattern at its root.

1. Ensure at least 20 GB free on C: (Disk Cleanup as admin).
2. Run elevated DISM restore-health, then `sfc /scannow`.
3. Restart the laptop.
4. Retry the update only after both complete cleanly.

### Fix 4: Update or remove the blocking driver

Check update history for the error code — 0x800F0922, 0x80070002/03, and 0xC1900101 families each hint at driver migration failures. Update chipset, storage, and biometric drivers from your laptop maker support page before retrying. If a specific driver is named in the failure, uninstall it temporarily, run the update, then reinstall fresh. For the 24H2-specific driver angle, see the [24H2 update-failure guide](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-in-windows-11-24h2/).

1. Note the exact error code in Update history.
2. Update chipset, storage, and biometric drivers from the maker.
3. Temporarily uninstall any driver named in the failure.
4. Retry the update with current drivers in place.

### Fix 5: Temporarily disable third-party antivirus and encryption

Third-party antivirus and full-disk encryption tools are classic rollback triggers — they intercept file operations the update engine needs. Temporarily disable real-time protection (or uninstall the AV as a test), pause encryption if the tool allows, run the update, then re-enable everything. If the update succeeds with protection off, you have found your blocker and can plan around it (update the AV, whitelist the process). Microsoft documents update troubleshooting in [Windows support](https://support.microsoft.com/en-us/windows).

1. Disable third-party antivirus real-time protection temporarily.
2. Pause third-party disk encryption if applicable.
3. Run the Windows update with protections lowered.
4. Re-enable everything immediately after, success or failure.

### Fix 6: Install the update manually from the catalog

Bypass the broken automatic path: find the KB number in update history, download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), and install the .msu by hand. Manual installs skip several automatic-pipeline failure points and give clearer error messages when they fail. If the manual install also rolls back with the same code, the problem is definitively in your system state, not the delivery — proceed to the repair install.

1. Find the failing KB number in Update history.
2. Download it from the Microsoft Update Catalog.
3. Install the .msu manually and note any error.
4. Same failure: the system state needs repair (next fix).

### Fix 7: Repair with an in-place upgrade

When rollbacks recur despite clean caches, repaired servicing, and current drivers, the OS needs rebuilding: run the Windows 11 24H2 installer from [Microsoft software download](https://www.microsoft.com/en-us/software-download/windows11) choosing "Keep personal files and apps". This reinstalls the update engine and servicing stack around your data. It is the definitive fix for chronic rollback loops and succeeds where repeated retries never will.

1. Back up personal files first.
2. Run the 24H2 installer → Upgrade → keep files and apps.
3. Let it complete (1–2 hours, plugged in).
4. Verify the previously failing update now installs.

## Closing

The "Undoing changes" screen is Windows protecting you from a bad update — the loop afterward is the part that needs fixing. Wait out the rollback, clear the update cache, repair the servicing stack, update the blocking drivers, and install manually or repair in place if it persists. Break the trigger once and Patch Tuesday goes back to being boring.
