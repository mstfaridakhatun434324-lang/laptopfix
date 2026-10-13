---
title: "How to Fix IRQL Not Less or Equal on Windows 10"
slug: how-to-fix-irql-not-less-or-equal-on-windows-10
date: 2026-10-13
categories: ["windows-errors"]
tags: ["irql not less or equal", "windows 10", "bsod"]
description: "IRQL_NOT_LESS_OR_EQUAL blue screen on Windows 10? Find the faulty driver or memory issue behind it with this ordered fix guide."
thumbnail: "/images/thumbs/how-to-fix-irql-not-less-or-equal-on-windows-10.webp"
faqs:
  - q: "What does IRQL_NOT_LESS_OR_EQUAL mean on Windows 10?"
    a: "It means a driver or system process tried to access memory it shouldn't have — either a bad address or at the wrong interrupt level. On Windows 10 the usual causes are faulty drivers (network and graphics lead), corrupted system files, and defective RAM."
  - q: "How do I find which driver caused it?"
    a: "Open the latest minidump in C:\\Windows\\Minidump with WinDbg Preview (free from the Microsoft Store) and run `!analyze -v`. The IMAGE_NAME line names the driver. The simpler BlueScreenView tool shows the same information with the suspect driver highlighted."
  - q: "Is this error more likely drivers or RAM?"
    a: "Drivers, roughly three times out of four. Suspect RAM when the dump blames a different driver every crash, when crashes happen at random idle moments, or when driver fixes change nothing. Consistent blame on one driver means a driver problem."
  - q: "Can Windows 10 updates cause this error?"
    a: "Yes — updates frequently replace working drivers with problematic ones, particularly network and audio drivers. If crashes started within a day of Patch Tuesday, roll back the suspect driver or uninstall the update before doing deeper troubleshooting."
---
IRQL_NOT_LESS_OR_EQUAL is Windows 10's way of saying something touched memory it had no business touching. The "something" is usually a driver reaching for an invalid address or accessing memory at the wrong interrupt priority level. It's one of the most common Windows 10 blue screens, and also one of the most fixable — because the minidump almost always points at the offender.

The Windows 10 repair path is well-trodden: identify the driver from the dump, replace it properly, then check memory and system files. Let's walk it.

## Why this happens

- **A faulty driver accessed invalid memory.** Network, graphics, and audio drivers are the usual suspects on Windows 10.
- **A Windows 10 update replaced a good driver.** Patch Tuesday driver swaps are a notorious trigger.
- **Corrupted system files.** Damaged kernel or networking components cause faults in otherwise fine drivers.
- **Defective RAM.** Bad memory corrupts driver operations, producing IRQL faults with shifting blame.
- **Overclocked memory (XMP).** Unstable RAM clocks corrupt data the same way faulty RAM does.
- **Antivirus filter drivers.** Kernel-level security software mishandling memory access.

## How to fix it

Work through these in order — diagnose your specific driver before changing anything.

### Fix 1: Identify the driver from the minidump

Targeted fixes beat shotgun fixes every time.

1. Open the newest `.dmp` file in `C:\Windows\Minidump\` with **WinDbg Preview** and run `!analyze -v`.
2. Note **IMAGE_NAME** — the driver file. Write it down exactly.
3. Check the blue screen itself too — Windows 10 often prints the driver filename right on the crash screen.
4. If every crash names a different driver, skip to the RAM test — scattered blame means memory.

### Fix 2: Clean-reinstall the named driver

Remove the offender completely and install the right version.

1. Boot into **Safe Mode** if needed: **Shift + Restart > Troubleshoot > Advanced options > Startup Settings**, press **4**.
2. Open **Device Manager** (**Win + X**), right-click the device, choose **Uninstall device**, and tick **Delete the driver software for this device** if shown.
3. Restart, then install the correct driver: chipset and network from your laptop maker's site, graphics from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html), Intel components via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Block Windows Update from reinstalling a bad version using Microsoft's show/hide updates troubleshooter. The same clean-replacement method fixes [DRIVER_IRQL_NOT_LESS_OR_EQUAL](/articles/how-to-fix-driver-irql-not-less-or-equal-reddit/) crashes, its close cousin.

### Fix 3: Roll back recent driver or Windows updates

If the timeline matches an update, reverse it.

1. In **Device Manager**, open the device's **Driver** tab and click **Roll Back Driver** if available.
2. Otherwise go to **Settings > Update & Security > Windows Update > View update history > Uninstall updates** and remove the recent update.
3. Pause updates for a couple of weeks (**Settings > Update & Security > Windows Update > Pause updates**) while the fixed driver situation stabilizes.
4. Reinstall updates selectively afterward, watching for the return of crashes.

### Fix 4: Repair system files

Damaged Windows components cause IRQL faults that look like driver bugs.

1. Open an elevated **Command Prompt** — right-click the Start button and choose **Command Prompt (Admin)**.
2. Run `sfc /scannow` and let it finish.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and test. On Windows 10 these two tools resolve a large share of stop codes with no clear driver blame.

### Fix 5: Test the RAM

Memory is the second suspect, and the test is conclusive.

1. Search for **Windows Memory Diagnostic**, open it, and choose **Restart now and check for problems**.
2. For a deeper test, run **MemTest86** from a bootable USB — at least one full pass.
3. Disable **XMP** in the BIOS as part of testing — unstable memory overclocks cause identical symptoms to bad RAM.
4. Replace faulty modules. RAM faults also produce [MEMORY_MANAGEMENT](/articles/memory-management-bsod-windows-11-fix/) crashes, so mixed stop codes reinforce the diagnosis.

### Fix 6: Remove kernel-level third-party software

Antivirus and "optimizer" tools operating at kernel level are frequent IRQL offenders.

1. Uninstall third-party antivirus, firewall, and system utility software from **Settings > Apps**.
2. Use vendor removal tools to clear leftover drivers.
3. Run on Windows Defender for a few days and monitor.
4. If crashes stop, replace the removed software with a current version or leave Defender in place — it's genuinely competent on Windows 10.

### Fix 7: Update the BIOS and verify stability

Finish with firmware and a proper soak test.

1. Update the BIOS from your laptop maker's support page with the charger connected.
2. After all fixes, stress the system for several days — the workloads that crashed before, plus general use.
3. If one driver keeps failing after clean reinstalls from the vendor, run the manufacturer's diagnostics on the underlying hardware.
4. Document what fixed it — if the error ever returns, you'll know exactly where to look. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) covers recovery options if crashes damaged the installation along the way.

### Fix 8: Run Driver Verifier on the suspect driver

When the dump names a driver but reinstalls don't resolve it, stress that driver deliberately to confirm.

1. Open an elevated **Command Prompt** and run `verifier /standard /driver suspect.sys`, using the exact filename from your minidump analysis.
2. Restart and use the laptop — Verifier will crash Windows quickly if that driver is genuinely faulty, producing a clear stop code.
3. After confirmation, boot into **Safe Mode**, open Command Prompt, and run `verifier /reset` to disable it.
4. Replace the confirmed driver following Fix 2. Keep Verifier sessions short and always reset it afterward — the crashes it produces are intentional diagnostics, and the full process is detailed in the [Driver Verifier violation guide](/articles/what-to-do-if-driver-verifier-detected-violation/).

## Closing

IRQL_NOT_LESS_OR_EQUAL on Windows 10 is a solvable problem with a clear method: read the dump, replace the named driver cleanly, roll back bad updates, verify memory. The stop code sounds technical, but the workflow is the same one technicians use daily — diagnose first, fix specifically, verify thoroughly. Keep the good driver pinned, the bad update blocked, and XMP stable, and this blue screen becomes a story you tell, not a problem you have.
