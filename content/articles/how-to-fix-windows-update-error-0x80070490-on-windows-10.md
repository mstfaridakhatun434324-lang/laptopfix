---
title: "Fix Windows Update Error 0x80070490 on Windows 10: Element Not Found"
slug: how-to-fix-windows-update-error-0x80070490-on-windows-10
date: 2026-09-02
categories: ["windows-update"]
tags: ["windows 10", "windows update", "error 0x80070490", "element not found", "dism"]
description: "Error 0x80070490 on Windows 10 means a component is missing from the store. Repair it with these Windows 10-specific DISM and cache steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070490-on-windows-10.webp"
faqs:
  - q: "What does 0x80070490 mean on Windows 10?"
    a: "It means 'element not found.' The servicing engine looked for a component, package, or manifest in the component store and could not find it. On Windows 10 this most often indicates WinSxS corruption, sometimes caused by interrupted updates or aggressive system-cleaner tools."
  - q: "Why does 0x80070490 hit driver updates on Windows 10 so often?"
    a: "Windows 10 pushes many driver updates through Windows Update, and each one stages packages in the driver store. If a staged package is corrupted or references a missing component, that specific driver update fails with 0x80070490 while everything else installs normally."
  - q: "How long does DISM RestoreHealth take on Windows 10?"
    a: "Typically 15 to 30 minutes on an SSD, longer on a spinning hard drive. It downloads healthy replacements from Windows Update, so a working internet connection speeds it up considerably. Let it finish uninterrupted — stopping DISM midway can leave the component store in a worse state than it started in."
  - q: "Should I avoid system cleaner tools after fixing this?"
    a: "Yes — at least the aggressive ones. Tools that purge 'unused' WinSxS or servicing files are a documented cause of 0x80070490. Windows 10's built-in Disk Cleanup with Windows Update Cleanup is safe; third-party deep cleaners are not worth the risk."
---

Windows 10's take on error 0x80070490 is the same "element not found" complaint: the update engine reached into the component store for something that was not there. Windows 10 laptops encounter this most often on driver updates pushed through Windows Update and on cumulative updates after an interrupted install. The repair path centers on DISM — the tool built specifically for component store repair — framed in Windows 10's menus and command prompts.

Because Windows 10 has been in service for years, its component stores have had more time to accumulate damage from interrupted updates, cleaner tools, and aging drives. Work the sequence below in order; the DISM step does the heavy lifting, and everything around it prepares the ground or handles the cases DISM cannot.

## Why this happens

- **WinSxS corruption:** The component store index and contents disagree after years of updates, interruptions, and cleanups.
- **Aggressive cleaner tools:** Third-party utilities deleting servicing files create genuinely missing components.
- **Interrupted cumulative updates:** Power loss or forced shutdowns mid-install leave half-registered components.
- **Corrupted driver store packages:** Damaged staged drivers fail with this error on driver updates specifically.
- **Damaged servicing registry keys:** Corrupted servicing hives misdirect component resolution.
- **Failing hard drive:** Bad sectors under the component store on older spinning drives.
- **Broken servicing stack update:** A failed SSU leaves the servicing engine unable to resolve components.
- **Corrupted update manifests:** Damaged manifests in the download cache describe nonexistent components.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter

Windows 10's troubleshooter repairs servicing registrations automatically.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Select **Windows Update**, click **Run the troubleshooter**, and apply all fixes.
3. Restart and check for updates.

### Fix 2: Reset the update cache

Clear corrupted manifests and partial component packages.

1. Open **Command Prompt (Admin)** from the Start right-click menu.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Restart and retry the update.

### Fix 3: Repair the component store with DISM

The core repair for "element not found." Let it run to completion.

1. In **Command Prompt (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait — on a hard drive this can take 30+ minutes. Ensure the laptop stays powered and connected.
3. When it reports success, restart immediately and check for updates.
4. If DISM reports it could not repair, proceed to Fix 6 for the offline approach.

### Fix 4: Run SFC against the repaired store

With the store fixed, let SFC repair protected files from it.

1. In **Command Prompt (Admin)**, run `sfc /scannow`.
2. Wait for 100% verification.
3. Restart and retry. This DISM-then-SFC order also fixes [0x80070003 path errors](/articles/how-to-fix-windows-update-error-0x80070003-on-windows-10/) that stem from the same store damage.

### Fix 5: Repair the driver store for driver-specific failures

When only driver updates fail with 0x80070490, target the driver store directly.

1. Run `pnputil /enum-drivers` in an elevated prompt and identify packages for the failing device.
2. Delete bad packages with `pnputil /delete-driver oemXX.inf /uninstall`.
3. Uninstall the device in **Device Manager** (tick driver removal), restart, and install the manufacturer's driver fresh.
4. Retry Windows Update — the driver entry should now install or disappear.

### Fix 6: Run DISM offline from Windows Recovery

For stores too damaged for online repair, work offline where nothing is locked.

1. Boot to WinRE: hold Shift while clicking **Restart** from the Start menu, then **Troubleshoot > Advanced options > Command Prompt**.
2. Confirm the Windows drive letter, then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
3. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
4. Exit and boot normally, then check for updates.

### Fix 7: In-place upgrade repair install

The last resort that always works for store corruption: reinstall Windows 10 over itself. Mount an official Windows 10 ISO, run setup, choose **Keep personal files and apps**. The process rebuilds WinSxS completely. Afterward, update drivers from your manufacturer's site before heavy Windows Update use, and stick to Disk Cleanup rather than third-party cleaners — guidance echoed on the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows).

Because Windows 10 machines are often older, two environmental factors deserve emphasis. First, spinning hard drives: DISM's RestoreHealth on a 5400 RPM laptop drive can take well over an hour, and interrupting it out of impatience is one of the ways component stores get damaged in the first place. Start it when you can leave the machine alone — plugged in, lid set to do nothing when closed — and let it finish. Second, third-party cleaners: the longer a Windows 10 installation has been running, the more likely someone ran an aggressive PC optimizer that purged servicing files. If the timeline fits, say so to yourself plainly: the tool caused this, DISM is the fix, and the tool should not be run again. The [Windows 11 version of this repair](/articles/how-to-fix-windows-update-error-0x80070490-on-windows-11/) follows the same logic with Windows 11's interface. After recovery, schedule a monthly Disk Cleanup with Windows Update Cleanup selected — it keeps the store lean without breaking it.

One more diagnostic worth running on older Windows 10 laptops: check the drive's SMART health before assuming software is the whole story. Open an elevated Command Prompt and run wmic diskdrive get status — a result of anything other than OK means the drive is reporting hardware problems, and no amount of DISM will fix a store that lives on failing sectors. In that case, clone the drive to a new SSD first, then repair the store on healthy hardware. Component store corruption that keeps returning after successful DISM repairs is the classic signature of a dying drive wearing a software disguise.

## Closing

On Windows 10, 0x80070490 is component store damage until proven otherwise, and DISM is the proven fix. The troubleshooter and cache reset clear the decks, DISM plus SFC rebuilds the store and files, the driver-store cleanup handles driver-specific cases, and offline DISM or a repair install covers the rest. Avoid aggressive cleaner tools going forward, and the "element not found" error stays in the past where it belongs.
