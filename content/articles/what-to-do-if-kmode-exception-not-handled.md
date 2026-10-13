---
title: "What to Do When You Get KMODE Exception Not Handled"
slug: what-to-do-if-kmode-exception-not-handled
date: 2026-09-16
categories: ["windows-errors"]
tags: ["KMODE exception", "BSOD", "driver error"]
description: "KMODE Exception Not Handled means a driver crashed the Windows kernel. Identify the faulty driver and fix this blue screen step by step."
thumbnail: "/images/thumbs/what-to-do-if-kmode-exception-not-handled.webp"
faqs:
  - q: "What does KMODE Exception Not Handled mean?"
    a: "It means a kernel-mode program — almost always a driver — generated an exception (an error condition) that the Windows error handler could not catch, so the system crashed. The blue screen often names the offending driver file, like ntfs.sys or a .sys file from your graphics or network driver. It is a driver problem in the vast majority of cases, not a hardware failure."
  - q: "How do I find which driver caused it?"
    a: "Check the blue screen itself — Windows often displays the driver filename in parentheses after the stop code. If you missed it, open the minidump in C:\\Windows\\Minidump with WinDbg or BlueScreenView; the analysis names the faulting module. The Event Viewer System log around the crash time also frequently identifies the driver."
  - q: "Can RAM cause KMODE Exception Not Handled?"
    a: "Rarely as the primary cause, but faulty RAM can corrupt driver code as it loads, producing this stop code as a secondary symptom. If driver updates and rollbacks do not help, run Windows Memory Diagnostic or MemTest86 to rule memory out. In practice, though, nine times out of ten the fix is updating, rolling back, or removing the named driver."
  - q: "Should I use Driver Verifier to diagnose it?"
    a: "Driver Verifier is powerful but risky — it intentionally crashes the system when a driver misbehaves, which can create boot loops if you verify the wrong drivers. Only use it if the minidump does not identify the culprit, verify only third-party drivers, and know how to boot into Safe Mode to run verifier /reset if the system will not start."
---

KMODE Exception Not Handled is Windows telling you that a driver crashed so badly the kernel could not recover. Unlike some cryptic stop codes, this one is often helpful: the blue screen frequently names the actual driver file responsible, right there in parentheses. Something like `KMODE_EXCEPTION_NOT_HANDLED (Netwtw10.sys)` is practically a signed confession.

Your job is to identify that driver and deal with it — update it, roll it back, or remove it. The fixes below start with reading the clue Windows left you, then work through the driver fixes in order of likelihood. Most cases resolve within the first three steps.

## Why this happens

- **Corrupted or outdated driver.** The named .sys file is damaged or incompatible with your Windows build.
- **Driver updated just before crashes started.** New driver versions sometimes ship with kernel bugs.
- **Conflicting drivers.** Two drivers fighting over the same hardware or memory region.
- **Corrupted system files.** Damage to Windows' own kernel-mode components.
- **Faulty RAM corrupting drivers.** Bad memory altering driver code as it loads (uncommon but real).
- **Overclocking instability.** Unstable CPU/RAM causing kernel-mode exceptions under load.

## How to fix it

Work through these in order, noting the driver name from the blue screen if shown.

### Fix 1: Note the driver name and update it

The blue screen's parenthetical filename is your prime suspect.

1. The next time it crashes (or from memory), note the .sys filename shown with the stop code.
2. Open **Device Manager** (`Win + X`) and find the related device — common ones: network adapters (Netwtw**, rtwlane.sys), graphics (nvlddmkm.sys, atikmdag.sys), storage (stornvme.sys, iaStorAC.sys).
3. Download the latest driver from the manufacturer, not Windows Update: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or your laptop maker ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
4. Install it, restart, and test.

### Fix 2: Roll back the driver if crashes started after an update

A fresh driver with a kernel bug is a classic cause.

1. In **Device Manager**, right-click the suspect device and open **Properties**.
2. Go to the **Driver** tab and click **Roll Back Driver** if available; choose a reason and confirm.
3. If rollback is grayed out, choose **Uninstall device** (check **Attempt to remove the driver** if offered), restart, and let Windows install its inbox driver.
4. Test stability before installing any newer version.

### Fix 3: Boot into Safe Mode and remove the offender

If the driver crashes on every boot, remove it from Safe Mode.

1. Force WinRE with three interrupted boots, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4** for Safe Mode.
2. In Safe Mode, open **Device Manager** and uninstall or roll back the suspect driver.
3. Also check **Settings > Apps** for recently installed driver utilities and remove them.
4. Restart normally.

### Fix 4: Run SFC and DISM

Repair Windows' own kernel components in case they are the damaged party.

1. Open **Terminal (Admin)** from `Win + X`.
2. Run `sfc /scannow`.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart.

### Fix 5: Analyze the minidump for confirmation

Verify you are chasing the right driver.

1. Install **WinDbg Preview** from the Microsoft Store.
2. Open the latest .dmp in `C:\Windows\Minidump`.
3. Run `!analyze -v` and read **MODULE_NAME** / **IMAGE_NAME**.
4. If it names a different driver than you suspected, redirect your update/rollback efforts there.

Our full walkthrough on [reading minidump files](/articles/how-to-check-minidump-files-on-windows-11/) covers this process step by step.

### Fix 6: Test the RAM

Rule out memory corrupting the drivers.

1. Press `Win + R`, type `mdsched.exe`, and run the memory diagnostic.
2. For a thorough check, run MemTest86 from a bootable USB for two passes.
3. Replace any failing module; on soldered-RAM ultrabooks, this means manufacturer service.

Related kernel crashes include [System Thread Exception Not Handled](/articles/system-thread-exception-not-handled-blue-screen-error-fix/) and the Lenovo-specific [KMODE exception guide](/articles/how-to-fix-kmode-exception-not-handled-on-lenovo-laptop/).

### Fix 7: Disable overclocking and Fast Startup

Eliminate instability sources.

1. Enter the BIOS and load optimized defaults, disabling any XMP or CPU overclock.
2. In Windows: **Control Panel > Power Options > Choose what the power buttons do > Change settings that are currently unavailable**, uncheck **Turn on fast startup**.
3. Shut down fully once, then power on and test.

### Fix 8: Use Driver Verifier to catch the culprit (carefully)

When the dump does not name the driver, Verifier forces the guilty one to crash identifiably.

1. First, create a system restore point: search **Create a restore point**, select C:, and click **Create**.
2. Press `Win + R`, type `verifier`, and press Enter.
3. Choose **Create custom settings**, enable **Special pool**, **Force IRQL checking**, and **Pool tracking**; then select **Select driver names from a list** and check only third-party drivers (never verify all drivers).
4. Restart — if a driver misbehaves, the system will blue-screen naming it directly.
5. Once identified, boot into Safe Mode, run `verifier /reset` in an admin Command Prompt to turn Verifier off, then update or remove the named driver.
6. Never leave Verifier running longer than needed; it intentionally degrades performance and stability.

## Closing

KMODE Exception Not Handled is one of the more honest blue screens — it usually tells you exactly which driver crashed. Trust that clue: update or roll back the named driver from the manufacturer's site, and the crashes typically stop immediately. Keep the minidump analysis in reserve for cases where the screen flashes by too fast, and test the RAM if drivers do not explain it. Driver-caused does not mean driver-doomed; this is among the most fixable stop codes there is, and most people resolve it the same day it starts. Keep a note of the driver version that caused it, in case Windows Update tries to reinstall it.
