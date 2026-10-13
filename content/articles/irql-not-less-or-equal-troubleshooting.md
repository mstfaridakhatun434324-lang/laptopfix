---
title: "Troubleshooting IRQL_NOT_LESS_OR_EQUAL on Windows 11 Laptops"
slug: irql-not-less-or-equal-troubleshooting
date: 2026-09-03
categories: ["windows-errors"]
tags: ["irql not less or equal", "bsod", "driver error", "stop code 0x0a", "windows 11"]
description: "IRQL_NOT_LESS_OR_EQUAL blue screen on Windows 11? Understand stop code 0x0A and troubleshoot it with 7 proven driver and hardware fixes."
thumbnail: "/images/thumbs/irql-not-less-or-equal-troubleshooting.webp"
faqs:
  - q: "What does IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "Stop code 0x0A means a driver tried to access memory at an improper interrupt request level — it touched pageable memory while running at a priority where paging is not allowed. In practice, this is a driver bug: the driver referenced a bad address or mishandled its interrupt level. The blue screen often names the offending .sys file."
  - q: "Is IRQL_NOT_LESS_OR_EQUAL caused by RAM?"
    a: "It can be. Faulty RAM corrupts the addresses drivers work with, producing 0x0A crashes that name different drivers each time. If the blamed .sys file keeps changing, or driver fixes do nothing, run the Windows Memory Diagnostic — inconsistent blame is the signature of a hardware memory problem."
  - q: "Which drivers cause IRQL_NOT_LESS_OR_EQUAL most often?"
    a: "Network drivers (ndis.sys and vendor Wi-Fi drivers), graphics drivers, and storage drivers top the list, followed by antivirus filter drivers. On laptops, the Wi-Fi driver is the single most common offender — especially older Intel, Realtek, or MediaTek wireless drivers on new Windows 11 builds."
  - q: "Can Windows Update cause this blue screen?"
    a: "Yes. Updates can install a new driver revision with a bug, or change kernel behavior an old driver depended on. If crashes started within a day of an update, roll back the most recently updated driver first, and check the update history for driver updates you did not explicitly approve."
---

IRQL_NOT_LESS_OR_EQUAL — stop code 0x0A — is the most frequently seen blue screen in Windows 11, and also one of the most diagnosable. "IRQL" is the Interrupt Request Level, a priority scheme Windows uses to manage what code can run when; drivers must follow strict rules about which memory they touch at each level. When a driver breaks those rules — accessing paged memory at a level where paging is forbidden, or simply dereferencing a bad pointer — Windows crashes with 0x0A rather than let the corruption spread.

For laptop owners, the practical translation is simple: this is a driver problem until proven otherwise, with the Wi-Fi driver as suspect number one. The stop screen frequently names the guilty `.sys` file, which turns a scary crash into a targeted repair job. Work the sequence below and you'll usually have it fixed before lunch.

## Why this happens

- **Buggy network/Wi-Fi drivers.** The single most common 0x0A trigger on laptops — wireless drivers mishandling interrupt levels.
- **Outdated graphics drivers.** GPU drivers operate at high IRQL; bugs here crash hard and often.
- **Corrupted driver installations.** Partially installed or mixed-version driver files break IRQL discipline.
- **Faulty RAM.** Bad memory corrupts driver addresses, producing 0x0A crashes with shifting blame.
- **Incompatible antivirus filters.** Kernel-level security drivers that violate IRQL rules.
- **Overclocked or unstable hardware.** Timing violations surface as driver-level memory faults.
- **Corrupted system files.** Damage to ntoskrnl.exe or hal.dll breaks the IRQL machinery itself.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify and fix the named driver

Use the clue on the blue screen.

1. Note the `.sys` filename in parentheses on the stop screen (disable auto-restart via `sysdm.cpl` if it vanishes too fast).
2. Common mappings: `ndis.sys` or `Netwtw10.sys` = network, `nvlddmkm.sys` = NVIDIA graphics, `rtwlane.sys` = Realtek Wi-Fi, `mtkwl6ex.sys` = MediaTek Wi-Fi.
3. Open **Device Manager**, locate the device, and check the driver date on **Properties > Driver**.
4. If the crash followed an update, use **Roll Back Driver**; otherwise **Update driver > Search automatically**.
5. For Wi-Fi specifically, download the newest driver from your laptop maker's support page rather than trusting the generic Windows driver.

The focused Windows 11 repair path is at [IRQL_NOT_LESS_OR_EQUAL Windows 11 fix](/articles/irql-not-less-or-equal-windows-11-fix/), and the driver-specific variant is covered in [how to fix DRIVER_IRQL_NOT_LESS_OR_EQUAL on Windows 11](/articles/how-to-fix-driver-irql-not-less-or-equal-on-windows-11/).

### Fix 2: Update the Wi-Fi driver manually

Since wireless drivers cause most laptop 0x0A crashes, give yours special attention.

1. In **Device Manager**, expand **Network adapters** and note your exact Wi-Fi chip (Intel AX201/AX211, Realtek 8852, MediaTek MT7921, etc.).
2. Download the latest driver for your exact model from Dell, HP, or Lenovo support — model-specific builds beat generic ones.
3. For Intel wireless, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) reliably finds the newest Wi-Fi and Bluetooth drivers.
4. In Device Manager, choose **Uninstall device** (checking **delete the driver software**), then install the downloaded driver fresh.
5. Restart and test on both 2.4 GHz and 5 GHz networks — some driver bugs only trigger on one band.

### Fix 3: Clean-install the graphics driver

GPU drivers are the second-biggest 0x0A source.

1. Download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) for your exact GPU.
2. During installation, choose **Custom > Perform a clean installation** (NVIDIA) or **Factory Reset** (AMD).
3. For stubborn cases, use Display Driver Uninstaller (DDU) in Safe Mode to strip the old driver completely before reinstalling.
4. Avoid installing the manufacturer's "game ready" beta drivers if stability matters more than day-one game support.
5. Retest with the workload that crashed — graphics 0x0A faults usually need 3D load to trigger.

### Fix 4: Test your RAM

Shifting blame between crashes means hardware.

1. Run `mdsched.exe`, choose **Restart now and check for problems**.
2. Check **Event Viewer > Windows Logs > System > MemoryDiagnostics-Results** after reboot.
3. If the blue screen names a different `.sys` file every time, treat RAM as the prime suspect even before testing.
4. Test sticks individually if removable; run MemTest86 overnight for intermittent faults.
5. Also load BIOS defaults to clear any unstable memory timings.

### Fix 5: Repair system files and update Windows

Fix the OS layer the drivers run on.

1. In **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. Install all pending updates in **Settings > Windows Update**, including optional driver updates.
3. If a specific update coincides with the crashes, check the Microsoft Update Catalog for a revised version.
4. When `ntoskrnl.exe` is the named file and SFC repairs corruption, the OS itself was likely the problem.
5. Persistent `ntoskrnl.exe` blame with clean SFC points back to a driver calling the kernel incorrectly — return to Fix 1 with minidump analysis.

### Fix 6: Remove problematic security and utility software

Kernel filters from third-party tools break IRQL rules.

1. Uninstall third-party antivirus temporarily; test on Microsoft Defender.
2. Remove VPN clients, firewall utilities, and "system optimizer" tools one at a time, testing between each.
3. Check for multiple security products running real-time protection simultaneously — pick one.
4. Update motherboard utility software (RGB, fan control) — old versions install filter drivers with known 0x0A bugs.
5. Reinstall only the latest versions of tools you actually need.

### Fix 7: Analyze the minidump to confirm the culprit

Get certainty when the pattern is unclear.

1. Verify dumps are on: `sysdm.cpl > Advanced > Startup and Recovery > Small memory dump`.
2. After the next crash, open `C:\Windows\Minidump\*.dmp` in WinDbg Preview and run `!analyze -v`.
3. Read `IMAGE_NAME` — that's your culprit in most cases.
4. If the analysis names Windows core files with no third-party driver in the stack, suspect RAM or run Driver Verifier (carefully — it intentionally crashes bad drivers).
5. Take the confirmed filename to the vendor's support page for the newest driver, or remove the owning software.

## Closing

IRQL_NOT_LESS_OR_EQUAL earns its reputation as the most common blue screen, but it's also among the most solvable: the stop screen usually names the driver, and the repair is a targeted update, rollback, or clean reinstall away. Start with the Wi-Fi driver on laptops — it's the offender more often than all other drivers combined — then work the graphics stack, memory, and system files. The only real trap is treating every 0x0A as a Windows problem and reinstalling the OS while a two-year-old wireless driver keeps crashing the kernel. Fix the driver, and the most feared blue screen becomes a fifteen-minute job.
