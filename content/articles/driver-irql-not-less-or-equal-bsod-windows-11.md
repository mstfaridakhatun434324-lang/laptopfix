---
title: "Driver IRQL Not Less or Equal: Fixing This Windows 11 BSOD"
slug: driver-irql-not-less-or-equal-bsod-windows-11
date: 2026-09-02
categories: ["windows-errors"]
tags: ["blue screen", "driver error", "IRQL"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL on Windows 11 is almost always a driver problem. Learn to identify the bad driver and fix it for good."
thumbnail: "/images/thumbs/driver-irql-not-less-or-equal-bsod-windows-11.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "A driver tried to access memory at an invalid address while running at a raised interrupt level (IRQL). In plain terms, a driver reached for memory it was not allowed to touch. The blue screen usually names the offending file, like ndis.sys for network drivers or nvlddmkm.sys for NVIDIA graphics."
  - q: "Which driver usually causes it on Windows 11?"
    a: "Network drivers (especially Wi-Fi), graphics drivers, and storage drivers top the list. Third-party antivirus filter drivers are another classic. The filename on the blue screen is your best clue — search it to identify which device it belongs to."
  - q: "Can Windows Update cause this error?"
    a: "Yes. Windows Update sometimes installs a generic or mismatched driver over a working manufacturer driver, particularly for Wi-Fi and Bluetooth. If the crashes started right after an update, rolling back that driver in Device Manager is the first thing to try."
  - q: "Is it ever a hardware problem?"
    a: "Occasionally. Failing RAM or an overheating GPU can corrupt driver operations and produce this stop code. But software causes dominate — always exhaust driver fixes and a memory test before suspecting hardware."
---
**DRIVER_IRQL_NOT_LESS_OR_EQUAL** is one of the most common blue screens on Windows 11, and it has a reassuring trait: the blue screen usually tells you exactly which driver crashed. A filename like `rtwlanu.sys`, `nvlddmkm.sys`, or `ndis.sys` right under the stop code is a signed confession.

The underlying mechanics are simple enough. Windows drivers run at different "interrupt request levels," and at higher levels a driver may only touch certain memory. When a driver reaches for paged or invalid memory at the wrong level, Windows stops the system. Your job is to find that driver and replace, roll back, or remove it.

## Why this happens

- **Corrupt or outdated device drivers:** The overwhelmingly common cause — a driver with a bug in its memory handling.
- **Windows Update driver replacements:** A generic driver pushed by Windows Update can conflict with laptop-specific hardware.
- **Conflicting software:** Two programs fighting over the same device (two VPN clients, antivirus plus firewall suites) can destabilize a driver.
- **Overclocked hardware:** Unstable CPU, RAM, or GPU overclocks corrupt driver memory operations.
- **Failing RAM:** Bad memory cells corrupt the data drivers work with, producing identical symptoms to a driver bug.
- **Damaged system files:** Corruption in shared driver frameworks (like `ndis.sys`) breaks every driver built on them.
- **Newly installed hardware:** A new USB device, dock, or Wi-Fi card with immature drivers can trigger it immediately.

## How to fix it

Work through these in order. In most cases you will be done by Fix 3.

### Fix 1: Read the filename on the blue screen

Before changing anything, identify the culprit — it saves hours.

1. The next time the blue screen appears, look below the stop code for a filename ending in `.sys`. Take a photo with your phone.
2. Common ones: `ndis.sys` (network stack), `rtwlanu.sys` / `Netwtw10.sys` (Realtek/Intel Wi-Fi), `nvlddmkm.sys` (NVIDIA), `atikmdag.sys` (AMD), `storahci.sys` (storage).
3. Search the filename to find its device. If the screen flashes too fast to read, disable automatic restart: **Settings > System > About > Advanced system settings > Startup and Recovery > Settings**, and uncheck **Automatically restart**. With auto-restart off, the blue screen stays visible indefinitely, giving you time to photograph the filename and the full stop-code parameters for your notes.

### Fix 2: Update the offending driver from the manufacturer

Once you know the device, get the correct driver.

1. Open **Device Manager** (**Win + X > Device Manager**), find the device, right-click it, and choose **Update driver > Search automatically for drivers**.
2. Better: download the latest driver from your laptop manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) — these are tested against your exact hardware.
3. For graphics, you can also go straight to NVIDIA's driver download or AMD's driver page. For Intel Wi-Fi and chipset, the Intel Driver & Support Assistant is reliable.
4. Install, reboot, and test under the conditions that used to crash.

### Fix 3: Roll back a driver that just updated

If the crashes started after a Windows or driver update, undo it.

1. In **Device Manager**, right-click the suspect device and open **Properties > Driver**.
2. Click **Roll Back Driver**, choose a reason, and confirm.
3. Reboot and test. To stop Windows Update from reinstalling the bad version, you can pause updates for a few weeks under **Settings > Windows Update**, or use the "Show or hide updates" troubleshooter from Microsoft Support.

### Fix 4: Uninstall conflicting software

Filter drivers from security and VPN software are frequent IRQL offenders.

1. If you run third-party antivirus, temporarily uninstall it (Windows Security takes over automatically) and test for a day or two.
2. Remove or update VPN clients, virtual-drive tools, and "driver updater" utilities — the last category causes more IRQL crashes than it fixes.
3. Open **Settings > Apps > Installed apps** and remove anything installed just before the crashes began. For a broader take on driver-related stop codes, see our guide to [driver-power-state-failure-windows-11-fix](/articles/driver-power-state-failure-windows-11-fix/).

### Fix 5: Run Windows Memory Diagnostic

Rule out bad RAM, which mimics driver bugs.

1. Press **Win + R**, type `mdsched.exe`, press **Enter**, and choose **Restart now and check for problems**.
2. Check the results in **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
3. If errors appear, reseat or replace the faulty stick. If you have also seen other memory-flavored crashes, our [memory-management-bsod-windows-11-fix](/articles/memory-management-bsod-windows-11-fix/) article walks through the full memory troubleshooting path.

### Fix 6: Repair system files

A damaged network or driver framework file breaks every driver using it.

1. Open an elevated **Command Prompt** and run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`, then run `sfc /scannow` once more.
3. Reboot and retest. If you want the full DISM procedure spelled out, see [how to run DISM RestoreHealth on Windows 11](/articles/how-to-run-dism-restore-health-on-windows-11/).

### Fix 7: Reset the network stack (for ndis.sys crashes)

If the named file is network-related, reset the whole stack cleanly.

1. In an elevated Command Prompt, run these in order:
   - `netsh winsock reset`
   - `netsh int ip reset`
   - `ipconfig /flushdns`
2. Reboot. This clears corrupt socket and TCP/IP state that can destabilize network drivers at high IRQL.

### Fix 8: Disable overclocking and test hardware

If software fixes fail, remove hardware instability from the picture.

1. Reset BIOS to **Optimized Defaults** and disable XMP memory profiles temporarily.
2. Remove recently added USB devices, docks, and SD cards.
3. If crashes persist only under load, monitor temperatures — an overheating GPU corrupts its driver's memory operations.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL is Windows pointing a finger at a driver — read the filename, update or roll back that driver from the manufacturer's site, and clear out conflicting software. Nine times out of ten the fix is a driver, not hardware, and the blue screen itself tells you where to look.
