---
title: "Fixing the Reference by Pointer BSOD"
slug: how-to-fix-reference-by-pointer-bsod-youtube
date: 2026-09-11
categories: ["windows-errors"]
tags: ["blue screen", "reference by pointer", "stop code 0x18"]
description: "REFERENCE_BY_POINTER blue screens mean a driver mishandled an object count. Here's how to find the bad driver and end the crashes."
thumbnail: "/images/thumbs/how-to-fix-reference-by-pointer-bsod-youtube.webp"
faqs:
  - q: "What does REFERENCE_BY_POINTER mean?"
    a: "Windows tracks how many parts of the system are using each internal object with a reference count. If a driver decrements that count incorrectly — freeing an object still in use, or corrupting the count — Windows bug-checks with stop code 0x18. It is a driver bug essentially every time."
  - q: "Which drivers cause this most often?"
    a: "Antivirus filter drivers, VPN clients, virtual-drive software, and storage filter drivers top the list, because they all manipulate object references heavily. Outdated network and USB drivers are also common. The minidump usually names the offender."
  - q: "Can I fix it without technical tools?"
    a: "Yes. Updating all drivers from the manufacturer and removing recently installed security, VPN, or virtual-drive software resolves most cases with no debugging needed. The dump-analysis steps are only for stubborn cases where the obvious fixes fail."
  - q: "Is my hardware failing?"
    a: "Very unlikely. This stop code is one of the most purely software-caused blue screens in Windows — it describes a driver logic error, not a hardware fault. Only consider RAM testing after all driver avenues are exhausted."
---
**REFERENCE_BY_POINTER** (stop code `0x18`) is Windows catching a driver in a bookkeeping error. Every object in the kernel — files, devices, processes — carries a reference count of how many components are using it. When a driver decrements that count wrongly, the count goes inconsistent, and Windows halts rather than let a freed-while-in-use object corrupt the system.

The practical upshot is encouraging: this is a driver bug essentially every time, not failing hardware. Your task is to find which driver miscounted and replace or remove it.

## Why this happens

- **Buggy filter drivers:** Antivirus, VPN, disk-encryption, and virtual-drive filter drivers manipulate object references constantly — and bugs here are the top cause.
- **Outdated storage or USB drivers:** Drivers that mishandle device-object lifetimes during plug/unplug or sleep/wake cycles.
- **Conflicting security products:** Two products hooking the same objects, each decrementing counts the other expects to own.
- **Corrupt driver installations:** Half-updated drivers with mismatched components miscounting references.
- **Beta or unsigned drivers:** Untested drivers that never went through Microsoft's validation.
- **Windows Update driver swaps:** A generic driver replacing a manufacturer driver that handled references correctly.
- **Sleep/wake driver bugs:** Drivers that mishandle device power transitions corrupt reference counts when the laptop sleeps and wakes — if crashes cluster around closing and opening the lid, suspect this pattern.
- **Rarely, bad RAM:** Memory corruption can scramble a reference count, but this is the exception.

## How to fix it

Work through these in order. Most cases end at Fix 2 or 3.

### Fix 1: Remove recently installed filter-driver software

Think about what changed just before the crashes started — that is your prime suspect.

1. Open **Settings > Apps > Installed apps** and sort by install date. Anything installed in the days before the first crash — VPN clients, antivirus trials, virtual-drive tools, disk utilities — is suspect.
2. Uninstall the most recent additions one at a time, testing stability between each.
3. Pay special attention to "driver updater" utilities and free antivirus trials bundled with other software. These are disproportionately represented in 0x18 crashes.

### Fix 2: Update all drivers from the manufacturer

Replace every suspect driver with a tested version in one pass. This is worth doing comprehensively rather than one driver at a time: REFERENCE_BY_POINTER is often caused by the interaction of a filter driver with the driver beneath it, so updating the whole storage, USB, and network stack together eliminates the interaction as well as the individual bugs. Download everything first, then install and reboot between major drivers.

1. Go to your manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)), enter your serial number, and install the latest **chipset**, **storage**, **USB**, and **network** drivers.
2. If you use third-party antivirus, update it to the latest version or switch to Windows Security temporarily — antivirus filter drivers are the single most common 0x18 culprit.
3. Reboot and use the machine normally for a day. If crashes persist, the next steps get more targeted.

### Fix 3: Identify the driver from the minidump

Let the crash evidence name the driver instead of guessing. This step takes ten minutes and routinely saves hours: a precise driver name turns a blind driver-update sweep into a single targeted replacement, and it protects you from "fixing" drivers that were never broken.

1. Install **WinDbg Preview** from the Microsoft Store and open the newest file in `C:\Windows\Minidump`.
2. Run `!analyze -v` and note the **IMAGE_NAME** — that driver mishandled the reference count.
3. Update, roll back, or uninstall that specific driver. Our full dump-reading tutorial is [how to analyze BSOD dump files on Windows 10](/articles/how-to-analyze-bsod-dump-files-on-windows-10/).

### Fix 4: Use Driver Verifier on the suspect

Confirm the diagnosis before committing to a fix.

1. Press **Win + R**, type `verifier.exe`, press **Enter**, and choose **Create custom settings** with all checks except **Low resources simulation**.
2. Choose **Select driver names from a list** and tick only your suspect driver.
3. Reboot and reproduce the crash. Verifier will catch the reference-counting violation immediately and name it.
4. Run `verifier /reset` from an elevated prompt afterward and reboot.

### Fix 5: Repair system files

Corrupt shared driver components can cause reference-counting errors in otherwise fine drivers.

1. Open an elevated **Command Prompt** and run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Reboot and retest. This is quick and eliminates an entire class of causes.

### Fix 6: Check for Windows Update driver conflicts

A generic driver from Windows Update may have replaced a working one.

1. In **Device Manager**, check the devices related to your crashes (network, storage, USB) — open **Properties > Driver** and note the date.
2. If a driver date matches the start of your crashes, use **Roll Back Driver**.
3. To prevent recurrence, pause updates temporarily or hide that specific driver update via the troubleshooter documented on Microsoft Support.

### Fix 7: Test memory as a last resort

Only reach for this after driver causes are exhausted — but do not skip it if crashes blame different drivers each time.

1. Run `mdsched.exe` and choose **Restart now and check for problems**.
2. Check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
3. Replace faulty RAM. For the complete memory troubleshooting sequence, see [memory-management-bsod-windows-11-fix](/articles/memory-management-bsod-windows-11-fix/).

## Closing

REFERENCE_BY_POINTER is Windows catching a driver's bookkeeping mistake — so the fix is finding that driver. Remove recently added filter-driver software, update everything from the manufacturer, and use the minidump to name the culprit if it hides. Hardware is almost never the story here, which makes this one of the more satisfying blue screens to fix. One last tip: if the crashes started the same week you installed a new VPN, antivirus, or disk tool, uninstall that program first before touching any driver — in real-world cases, the newest filter driver is the offender more often than not.
