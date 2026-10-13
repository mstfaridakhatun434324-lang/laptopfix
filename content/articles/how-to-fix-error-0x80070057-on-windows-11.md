---
title: "How to Fix Error 0x80070057 on Windows 11"
slug: how-to-fix-error-0x80070057-on-windows-11
date: 2026-09-22
categories: ["windows-errors"]
tags: ["error-0x80070057", "windows-11", "windows-update"]
description: "Error 0x80070057 on Windows 11? Fix the parameter-is-incorrect update error with these proven repair steps."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070057-on-windows-11.webp"
faqs:
  - q: "What does error 0x80070057 mean?"
    a: "It means 'the parameter is incorrect' — Windows Update or a setup process received an unexpected value. Common triggers include corrupted update cache files, a wrong decimal symbol in regional settings, damaged system files, or a full system reserved partition during upgrades."
  - q: "Why does 0x80070057 appear during Windows Update?"
    a: "Usually because the SoftwareDistribution cache is corrupted or the update components are in a bad state. Resetting the Windows Update components and clearing the cache fixes the majority of update-related cases."
  - q: "Can the decimal symbol really cause this error?"
    a: "Yes, surprisingly. If the decimal symbol in your regional settings is not a period, some Windows processes fail parameter validation. Changing it back to a period has fixed this error for many users."
  - q: "Will I lose files fixing 0x80070057?"
    a: "No. All the standard fixes — resetting update components, SFC/DISM, changing regional settings — leave your files untouched. Only a full Windows reinstall would affect data, and that's rarely needed here."
---
# How to Fix Error 0x80070057 on Windows 11

**Error 0x80070057** — "the parameter is incorrect" — usually pops up when Windows Update fails, when you're backing up files, or during an upgrade. It's a frustratingly vague code, but the underlying causes are well understood, and the fixes below handle nearly every scenario.

This error is almost never serious. It typically means some cached data or setting got mangled, and once you clear it, updates flow normally again. It shows up in three main situations: Windows Update refusing to install, File History or system backup failing midway, and Windows setup aborting during an upgrade — the fixes below cover all three, so start with the one matching where you see the error.

If you're hitting a different update error instead, our [error code 0x80070057 fix](/articles/error-code-0x80070057-fix/) covers a closely related variant, and the [black screen after update guide](/articles/windows-11-black-screen-after-update-fix/) helps if a bad update left your system unstable.

## Why this happens

- **Corrupted Windows Update cache:** Damaged files in the SoftwareDistribution folder make updates fail parameter checks.
- **Wrong decimal symbol in regional settings:** A comma or other character as the decimal separator breaks validation in some Windows processes.
- **Damaged system files:** Corrupted servicing-stack or component-store files cause update installs to reject parameters.
- **Full System Reserved partition:** During upgrades, a reserved partition with no free space fails with this exact code.
- **Third-party antivirus interference:** Overzealous real-time scanning can lock update files mid-write.
- **Faulty backup target:** When it appears during File History or backup, the destination drive or its file system is usually the problem.

## How to fix it

Work through these in order. For update failures, Fix 1 alone solves it most of the time.

### Fix 1: Reset Windows Update components

Clearing the corrupted cache is the single most effective fix for this error.

1. Open **Terminal (Admin)** from the **Win + X** menu.
2. Stop the update services:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
3. Rename the cache folders so Windows rebuilds them:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services:
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
   `net start msiserver`
5. Open **Settings > Windows Update** and check for updates again.
6. Once updates install successfully, you can delete the `SoftwareDistribution.old` and `catroot2.old` folders to reclaim disk space — Windows has already built fresh replacements.

If the error appears during File History backups rather than updates, also check that the destination drive has free space and is formatted NTFS; FAT32 drives and nearly-full targets trigger the same code for a completely different reason.

### Fix 2: Check the decimal symbol setting

This odd-sounding fix is a documented cause of 0x80070057.

1. Open **Settings > Time & language > Language & region**.
2. Click **Administrative language settings**, then the **Formats** tab, and click **Additional settings**.
3. Make sure **Decimal symbol** is a period (`.`). If it's a comma or anything else, change it.
4. Click **OK**, restart the laptop, and retry the failed operation.

### Fix 3: Run the Windows Update troubleshooter

The built-in troubleshooter automatically repairs common servicing problems.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Apply any fixes it suggests and restart when prompted.
4. Try the update again. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the latest version of these steps if the menus move.

### Fix 4: Repair system files with SFC and DISM

Damaged servicing files need repairing before updates can succeed. This two-tool combination fixes the component store that Windows Update depends on.

1. Open an admin Terminal and run `sfc /scannow`.
2. When it finishes, run `DISM /Online /Cleanup-Image /StartComponentCleanup` to clear out superseded update components that sometimes confuse the installer.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` for the full repair.
3. If DISM fails to find source files, download the Windows 11 ISO from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, and run:
   `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:D:\Sources\Install.wim:1 /LimitAccess`
   (replace `D:` with the mounted ISO's drive letter)
4. Restart and retry the update.

### Fix 5: Free space on the System Reserved partition (upgrade errors)

If 0x80070057 appears during a Windows upgrade, the reserved partition is probably full.

1. Press **Win + R**, type `diskmgmt.msc`, and press **Enter**.
2. Note the small (usually 100–500 MB) System Reserved partition.
3. Assign it a drive letter: right-click it, choose **Change Drive Letter and Paths**, and add one.
4. Open an admin Command Prompt, switch to that drive, and delete unneeded font or log files — but only files, never folders you don't recognize.
5. Remove the drive letter afterward and retry the upgrade.

### Fix 6: Temporarily disable third-party antivirus

Security software locking update files mid-write is a real, if uncommon, trigger.

1. Open your antivirus settings and disable real-time protection temporarily.
2. Retry the update or backup.
3. Re-enable protection immediately afterward — don't browse unprotected.
4. If this fixed it, check the vendor's site for an updated version before the next Patch Tuesday.

### Fix 7: Install the update manually

When automatic update keeps failing, the standalone installer often sails through.

1. Note the KB number of the failing update in **Settings > Windows Update > Update history**.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and run the `.msu` file.
3. If the manual install also fails with 0x80070057, back up your data and run an in-place upgrade: mount the Windows 11 ISO, run `setup.exe`, choose **Keep personal files and apps**, and let it reinstall Windows over itself. This replaces every system component while preserving your data and programs, and it clears stubborn servicing corruption that SFC and DISM can't reach.

## Closing

Error 0x80070057 looks cryptic but it's usually just a corrupted update cache or a quirky regional setting. Reset the update components, check that decimal symbol, repair system files, and you'll have updates installing cleanly again — no reinstall required in the vast majority of cases.
