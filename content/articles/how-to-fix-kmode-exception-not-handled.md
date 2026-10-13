---
title: "KMODE_EXCEPTION_NOT_HANDLED: Causes and Fixes for Windows Laptops"
slug: how-to-fix-kmode-exception-not-handled
date: 2026-09-01
categories: ["windows-errors"]
tags: ["kmode exception not handled", "bsod", "kernel mode", "driver error", "stop code 0x1e"]
description: "KMODE_EXCEPTION_NOT_HANDLED blue screen on your laptop? Learn what stop code 0x1E means and fix it with 7 driver-focused troubleshooting steps."
thumbnail: "/images/thumbs/how-to-fix-kmode-exception-not-handled.webp"
faqs:
  - q: "What does KMODE_EXCEPTION_NOT_HANDLED mean?"
    a: "Stop code 0x1E means a kernel-mode program threw an exception the error handler could not catch — essentially, a driver or core Windows component crashed in a way Windows cannot recover from. The blue screen usually names the offending .sys file in parentheses, which is your biggest clue. Nine times out of ten, that file belongs to a driver."
  - q: "Which driver causes KMODE_EXCEPTION_NOT_HANDLED?"
    a: "There is no single culprit; the stop screen names the specific file, such as ndis.sys (network), ntfs.sys (storage), or a vendor driver like e1d65x64.sys (Intel network). Note the exact filename, identify its owner with a web search, then update, roll back, or reinstall that driver first."
  - q: "Can RAM cause KMODE_EXCEPTION_NOT_HANDLED?"
    a: "Yes, though it is less common than a driver cause. Faulty RAM corrupts kernel-mode data structures, which can surface as unhandled kernel exceptions. If driver fixes fail and the named .sys file changes between crashes, run the Windows Memory Diagnostic to check the hardware."
  - q: "Should I update or roll back the driver?"
    a: "It depends on timing. If crashes started right after a driver or Windows update, roll the driver back. If nothing changed recently and the driver is old, update it. The rule is simple: undo the most recent change first, then move forward to newer versions."
---

KMODE_EXCEPTION_NOT_HANDLED — stop code 0x1E — is Windows' way of saying a kernel-mode component hit an error it had no handler for. Kernel mode is where drivers and the core OS live, with full access to hardware and memory; when something goes wrong down there, there's no safety net, so Windows crashes the whole system. The saving grace of this stop code is that the blue screen almost always names the failing module — a `.sys` file in parentheses — which hands you the investigation on a plate.

On laptops, the usual offenders are network drivers, graphics drivers, storage drivers, and the occasional overzealous antivirus filter driver. The fix sequence below starts with identifying the named driver, then works through the standard driver-repair ladder, with system-file and hardware checks for the stubborn cases.

## Why this happens

- **A buggy or corrupted driver.** The named `.sys` file on the stop screen is the prime suspect in the majority of 0x1E crashes.
- **Driver conflicts after updates.** A new Windows build can break an older driver that previously worked fine.
- **Overclocked or unstable hardware.** Aggressive CPU/GPU/RAM settings cause kernel-mode exceptions under load.
- **Corrupted system files.** Damage to kernel components makes even healthy drivers throw unhandled exceptions.
- **Faulty RAM.** Bad memory corrupts kernel data, producing 0x1E crashes that name different files each time.
- **Incompatible antivirus or firewall drivers.** Kernel-level security filters are a classic source of unhandled exceptions.
- **Overheating components.** Thermal instability under load manifests as kernel exceptions during gaming or heavy work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the named driver and update or roll it back

The stop screen gives you the answer — use it.

1. Note the `.sys` filename shown on the blue screen (photograph it if the system restarts too fast).
2. To stop the auto-restart, boot into Safe Mode and uncheck **Automatically restart** under `sysdm.cpl > Advanced > Startup and Recovery`.
3. Identify the driver's owner: `ntoskrnl.exe` points at core Windows or RAM, `ndis.sys` at networking, `dxgkrnl.sys` at graphics; vendor files like `rtwlanu.sys` belong to specific hardware.
4. In **Device Manager**, find the device, open **Properties > Driver**: use **Roll Back Driver** if the crash followed an update, otherwise **Update driver**.
5. For graphics, do a clean install from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) rather than relying on Windows Update.

Brand-specific walkthroughs exist too — see [KMODE_EXCEPTION_NOT_HANDLED on Dell laptops](/articles/how-to-fix-kmode-exception-not-handled-on-dell-laptop/) and [on Lenovo laptops](/articles/how-to-fix-kmode-exception-not-handled-on-lenovo-laptop/).

### Fix 2: Run the Windows Memory Diagnostic

Rule out RAM, especially if the named file varies between crashes.

1. Press **Windows + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
3. If errors appear, test sticks individually (if removable) or contact support for soldered RAM.
4. Also reset any overclocking: enter BIOS/UEFI and load **Optimized Defaults**.
5. Retest under the load that used to crash — memory faults often need heat and pressure to show.

### Fix 3: Update all drivers via your manufacturer

Get the driver stack consistent in one pass.

1. Find your exact model on Dell, HP, or Lenovo support and download the latest drivers.
2. Download and install the latest **chipset**, **network**, **graphics**, and **storage** drivers.
3. On Intel systems, also run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Restart after each major driver group, not just at the end.
5. Skip third-party "driver updater" tools — they cause more 0x1E crashes than they fix.

### Fix 4: Repair system files with DISM and SFC

Fix damage to the kernel components themselves.

1. Open **Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow`, then restart.
3. Check **Settings > Windows Update** and install all pending updates — cumulative updates frequently contain kernel fixes.
4. If the named file was `ntoskrnl.exe` and SFC found corruption it repaired, that's a strong sign this was the cause.
5. Persistent `ntoskrnl.exe` crashes after clean SFC point back at RAM or drivers calling into the kernel badly.

### Fix 5: Remove or update security software

Kernel filters from security products are a known 0x1E source.

1. Uninstall third-party antivirus via **Settings > Apps > Installed apps** (use the vendor's removal tool if offered).
2. Test on Microsoft Defender alone for a few days.
3. If crashes stop, reinstall the latest version of the security product — old filter drivers are usually the problem, not the product itself.
4. Do the same test for VPN clients and disk-encryption tools, which install similar kernel drivers.
5. Never run two real-time antivirus products simultaneously; their drivers fight in kernel mode.

### Fix 6: Check thermals and disable fast startup

Heat and hibernation-state corruption both produce kernel exceptions.

1. Monitor CPU/GPU temperatures under load; sustained readings above 95°C on a laptop warrant cleaning vents and checking fans.
2. Disable **Fast Startup**: **Control Panel > Power Options > Choose what the power buttons do > Change settings > uncheck Turn on fast startup**.
3. Fast Startup's hibernation file can carry corrupted kernel state across boots — a full shutdown clears it.
4. Update the BIOS from your manufacturer's support page; thermal and power-management fixes are common.
5. Test with the laptop on a hard, flat surface (or a cooling pad) to rule out heat-soak crashes.

### Fix 7: Analyze the minidump for the exact culprit

When the stop screen isn't enough, read the crash dump.

1. Confirm dumps are enabled: `sysdm.cpl > Advanced > Startup and Recovery > Write debugging information` should be **Small memory dump**.
2. After the next crash, find `C:\Windows\Minidump\*.dmp`.
3. Open it with WinDbg Preview (free from the Microsoft Store) and run `!analyze -v`.
4. The `IMAGE_NAME` and `MODULE_NAME` lines identify the failing driver precisely.
5. Take that filename to the device's vendor for the newest driver, or remove the owning software entirely.

## Closing

KMODE_EXCEPTION_NOT_HANDLED is one of the friendlier blue screens because it names its suspect. Write down that `.sys` filename, work the driver angle — roll back what's new, update what's old, clean-install the graphics stack — and most cases resolve without ever touching hardware diagnostics. The traps are skipping the minidump analysis when the named file keeps changing (that's RAM or thermals talking) and letting a third-party "driver fixer" loose on the system. Follow the evidence the stop screen gives you, and stop code 0x1E is a solvable puzzle, not a curse.
