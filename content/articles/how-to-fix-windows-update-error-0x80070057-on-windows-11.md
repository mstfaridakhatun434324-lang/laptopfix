---
title: "Fix Windows Update Error 0x80070057 on Windows 11: The Parameter Is Incorrect"
slug: how-to-fix-windows-update-error-0x80070057-on-windows-11
date: 2026-10-10
categories: ["windows-update"]
tags: ["windows 11", "windows update", "error 0x80070057", "parameter incorrect", "troubleshooting"]
description: "Error 0x80070057 ('the parameter is incorrect') blocks Windows 11 updates. Learn what corrupts the update parameters and how to fix each cause."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070057-on-windows-11.webp"
faqs:
  - q: "What does error 0x80070057 mean?"
    a: "It means 'the parameter is incorrect' — Windows Update passed invalid or corrupted data to one of its components. In practice, this points to corrupted update metadata, a damaged registry entry under the Windows Update keys, or a corrupted system file that the update engine depends on."
  - q: "Why does 0x80070057 often appear with large updates?"
    a: "Large updates pass more parameters — file manifests, component lists, driver migration instructions — so there are more chances for one corrupted value to derail the process. Cumulative and feature updates therefore trigger this error far more often than small patches, which is why the error seems to appear out of nowhere on Patch Tuesday."
  - q: "Can 0x80070057 mean my Windows installation is corrupted beyond repair?"
    a: "Rarely. It usually means the update subsystem's data is corrupted, not Windows itself. The standard sequence of cache reset, DISM, and SFC fixes it in most cases. Only if DISM cannot repair the component store would you consider an in-place upgrade."
  - q: "Does 0x80070057 affect upgrades to new Windows 11 versions?"
    a: "Yes, it is a common feature-update blocker. If a monthly cumulative update installs fine but the annual feature update fails with 0x80070057, the cause is usually corrupted migration data or a damaged component store that only the bigger update's parameter set exposes."
---

Error 0x80070057 translates to "the parameter is incorrect," which is Windows' way of saying that the update engine handed one of its components bad data. On Windows 11, this error loves to appear at the worst moments: during large cumulative updates, during feature updates, and sometimes during the final reboot phase when you thought everything was fine. The laptop is not broken — but the update subsystem's bookkeeping is, and it needs to be rebuilt.

Think of it this way: every update is a set of instructions with parameters — which files to replace, which registry keys to touch, which drivers to migrate. If any of those parameters are corrupted in the download, in the cache, or in the registry, the component receiving them rejects the whole operation with 0x80070057. Your job is to find where the bad parameter lives and replace it with clean data. The steps below hunt it down in the most likely places first.

## Why this happens

- **Corrupted update metadata:** The downloaded update's manifest files are damaged, so the parameters describing what to install are invalid.
- **Damaged Windows Update registry keys:** Corrupted values under the update-related registry hives feed bad parameters to the engine.
- **Corrupted component store:** WinSxS damage means the baseline data the update compares against is wrong, producing invalid computed parameters.
- **Decimal symbol locale bug:** A classic cause — if the system's decimal symbol is not a period (.), some update components misparse version numbers and fail with 0x80070057.
- **Corrupted system files:** Damaged protected files that the update engine loads can cause parameter validation to fail.
- **Third-party antivirus hooks:** Security software intercepting update API calls can corrupt the parameters in transit.
- **Failed System Reserved partition operations:** Updates that need to write to the System Reserved partition fail with this error when that partition is full or corrupted.
- **Damaged user profile for the update service:** Rare, but a corrupted system profile can cause parameter-passing failures in the update services.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the decimal symbol setting

This sounds bizarre, but it is a documented cause: update components expect the decimal symbol to be a period. If yours is a comma, version parsing fails.

1. Open **Control Panel > Clock and Region > Region**.
2. Click **Additional settings** and check the **Decimal symbol** field — it must be `.` (period).
3. If it is a comma or anything else, change it to a period and click OK.
4. Restart and retry the update. This single setting has fixed 0x80070057 for countless users.

### Fix 2: Run the Windows Update troubleshooter

The troubleshooter resets update components and clears corrupted metadata automatically.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Apply all fixes, restart, and check for updates.

### Fix 3: Reset the update cache

Corrupted metadata in the cache is the most common source of bad parameters. Rebuild it.

1. Open **Terminal (Admin)**.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Restart and check for updates.

### Fix 4: Repair the component store and system files

Bad baseline data in WinSxS produces bad computed parameters. DISM and SFC fix the baseline.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`.
3. Restart and retry. This pair also resolves the closely related [0x80070002 missing-file failures](/articles/how-to-fix-windows-update-error-0x80070002-on-windows-11/), which share the same repair path.

### Fix 5: Free space on the System Reserved partition

Updates that touch boot files fail with 0x80070057 when the System Reserved partition is full.

1. Open **Disk Management** (right-click Start).
2. Find the **System Reserved** partition and check its free space — it needs at least 15–30 MB free.
3. If it is full, the safest cleanup is to delete old font files: assign it a drive letter in Disk Management, open it in File Explorer, go to `EFI\Microsoft\Boot\Fonts`, and delete non-English font files (keep the English ones).
4. Remove the drive letter afterward, restart, and retry the update.

### Fix 6: Temporarily disable third-party antivirus

Security hooks intercepting update operations can corrupt parameters in transit.

1. Disable real-time protection temporarily in your antivirus settings.
2. Retry the update immediately while protection is off.
3. Re-enable protection as soon as the update completes.
4. If this fixes it, add Windows Update exclusions or switch to Microsoft Defender to avoid a repeat.

### Fix 7: Perform an in-place upgrade repair

If the parameter corruption is in the registry or servicing stack beyond what DISM can fix, an in-place upgrade reinstalls Windows 11 while keeping files and apps. Download the installer from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), run setup, choose **Keep personal files and apps**, and let it complete. Afterward, run Windows Update once more — with fresh servicing components, 0x80070057 should be gone. For context on keeping the pipeline healthy afterward, the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) has current guidance.

It is worth understanding where 0x80070057 bites hardest: feature updates. A monthly cumulative update replaces hundreds of files, but a feature update migrates thousands — drivers, boot files, user profiles — and every one of those operations passes parameters that must validate. That is why this error often appears for the first time during the annual update even on machines whose monthly updates were flawless. If you are on Windows 10 rather than 11, the [Windows 10 version of this fix](/articles/how-to-fix-windows-update-error-0x80070057-on-windows-10/) covers the same causes with Windows 10's menus. Either way, the decimal-symbol check remains the highest-value thirty seconds in this entire guide — do not skip it.

## Closing

Error 0x80070057 looks cryptic, but its causes are concrete: bad metadata, bad registry data, a wrong decimal symbol, or a full System Reserved partition. The decimal-symbol check alone resolves a surprising number of cases, and the cache reset plus DISM/SFC handles most of the rest. Work the list in order, and the "parameter is incorrect" message becomes a solved problem rather than a recurring mystery.
