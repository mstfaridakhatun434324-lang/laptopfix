---
title: "DRIVER_IRQL_NOT_LESS_OR_EQUAL on Windows 10: Fix It Like a Tech"
slug: how-to-fix-driver-irql-not-less-or-equal-on-windows-10
date: 2026-10-02
categories: ["windows-errors"]
tags: ["bsod", "stop code", "windows 10", "drivers"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen on Windows 10? A driver touched memory it shouldn't. Here's the technician's fix order."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal-on-windows-10.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean in plain English?"
    a: "A driver tried to access a memory address at the wrong privilege level — essentially reaching into memory it had no business touching. Windows crashes immediately. The blue screen often names the driver file, which tells you exactly who the offender is."
  - q: "Which driver usually causes it?"
    a: "Network drivers (Wi-Fi and Ethernet) are the most common, followed by graphics drivers and storage controller drivers. The filename on the blue screen — like ndis.sys, nvlddmkm.sys, or storport.sys — identifies it directly."
  - q: "Can Windows Update cause this error?"
    a: "Yes. Windows Update frequently replaces manufacturer drivers with generic Microsoft versions that misbehave on specific laptop hardware. If the crash started right after an update, rolling back the driver is often the entire fix."
  - q: "Is this a RAM problem?"
    a: "Usually not — this stop code is specifically about a driver accessing memory improperly, not about memory being faulty. But if the named driver changes with every crash, test your RAM, because bad memory can make innocent drivers look guilty."
---

`DRIVER_IRQL_NOT_LESS_OR_EQUAL` is the classic driver blue screen. The name is jargon for a simple violation: a driver tried to touch memory at an interrupt level where that memory wasn't accessible. Windows doesn't negotiate with drivers that break memory rules — it crashes on the spot.

The reason technicians like this stop code is that it usually names names. The blue screen frequently shows the offending driver file in parentheses, and that turns a mysterious crash into a ten-minute fix. Here's the order a tech would work it.

## Why this happens

- **A buggy or outdated device driver**: The direct cause in most cases. Network drivers lead the pack on laptops, with graphics and storage drivers close behind.
- **Windows Update replaced a good driver with a generic one**: Microsoft's generic drivers don't always respect OEM hardware quirks, and the mismatch produces exactly this violation.
- **Corrupted driver files**: Disk errors or interrupted installations damage driver binaries so they misbehave at runtime.
- **Conflicting drivers from similar devices**: Two drivers fighting over the same hardware (common with USB Wi-Fi adapters alongside built-in Wi-Fi, or after motherboard swaps) cause access violations.
- **Overclocking or unstable RAM**: Makes drivers read garbage from memory, which looks like an illegal access even when the driver code is correct.
- **Antivirus or VPN filter drivers**: These sit in the network stack at high privilege; buggy filters are a classic source of this exact stop code.

## How to fix it

Work through these in order — identify the driver first, then act.

### Fix 1: Note the driver name on the blue screen

Don't let the next crash go to waste.

1. When it blue-screens, look for a filename after the stop code, e.g. `DRIVER_IRQL_NOT_LESS_OR_EQUAL (ndis.sys)`.
2. Quick decoder: `ndis.sys`/`Netwtw10.sys`/`rtwlanu.sys` = network drivers; `nvlddmkm.sys` = NVIDIA; `atikmdag.sys` = AMD; `storport.sys`/`stornvme.sys` = storage; `usbport.sys` = USB.
3. If you missed it, check **Event Viewer** > **Windows Logs** > **System** for BugCheck entries, or run the free BlueScreenView against `C:\Windows\Minidump`.
4. If every crash names a *different* driver, skip to Fix 6 (RAM test) — that's the telltale sign of bad memory framing innocent drivers.

### Fix 2: Update the culprit driver from the manufacturer

Get the real driver, not Windows' generic guess.

1. Open **Device Manager** (**Win + X** > **Device Manager**) and find the device matching your culprit.
2. For network drivers, download from your laptop maker's support site (OEM Wi-Fi drivers are heavily customized) or the chip vendor (Intel/Realtek/Qualcomm).
3. For NVIDIA graphics: [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx) with a **clean install**. For AMD: [AMD's driver page](https://www.amd.com/en/support/download/drivers.html). For Intel: the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Install, restart, and give it a few days of normal use — this crash can be intermittent.

The broader [IRQL_NOT_LESS_OR_EQUAL guide](/articles/irql-not-less-or-equal-windows-11-fix/) covers additional scenarios if the manufacturer's driver doesn't end it.

### Fix 3: Roll back if a recent update caused it

The fastest fix when the timeline is obvious.

1. In **Device Manager**, right-click the suspect device > **Properties** > **Driver** tab > **Roll Back Driver**.
2. If the button is grayed out, uninstall the device (check **Delete the driver software for this device**), then install the previous version from the manufacturer's driver archive.
3. If a Windows update is the suspect: **Settings** > **Update & Security** > **Windows Update** > **View update history** > **Uninstall updates**, and remove the recent one.
4. Pause Windows updates for a week (**Settings** > **Update & Security** > **Windows Update** > **Pause updates**) so it doesn't immediately reinstall the bad driver.

### Fix 4: Remove or update filter drivers (antivirus, VPN)

Network-stack filters are repeat offenders for this stop code.

1. Update your VPN client and antivirus to the latest versions.
2. If crashes continue, uninstall the VPN client temporarily and test for several days.
3. Temporarily replace third-party antivirus with Windows Defender as a test (**Settings** > **Apps** > uninstall the AV).
4. Reinstall the latest versions afterward if the test clears them — fresh installs get clean filter drivers.

For post-update variants of this crash, see the [DRIVER_IRQL after Windows 11 update guide](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/).

### Fix 5: Check for conflicting or duplicate devices

Two drivers claiming the same hardware cause access violations.

1. Open **Device Manager** > **View** > **Show hidden devices**.
2. Look for grayed-out duplicates of network adapters, USB devices, or storage controllers — remnants of old hardware or dongles.
3. Right-click each phantom device and **Uninstall device**.
4. If you use a USB Wi-Fi adapter alongside built-in Wi-Fi, disable the built-in adapter in Device Manager (or vice versa) so only one driver owns wireless.

### Fix 6: Test your RAM

When the blamed driver keeps changing, the memory is lying to the drivers.

1. Press **Win + R**, type `mdsched.exe`, press Enter > **Restart now and check for problems**.
2. Any error means bad RAM — replace the faulty stick (test one at a time if you have two).
3. For a conclusive test, run MemTest86 overnight from USB.

### Fix 7: Repair system files and reset network stack

Corrupted system components and a tangled network stack are the last software suspects.

1. Open an elevated Command Prompt (**Win + X** > **Command Prompt (Admin)**).
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Reset the network stack completely:
   - `netsh winsock reset`
   - `netsh int ip reset`
   - `ipconfig /flushdns`
4. Restart. These commands rebuild the network components that `ndis.sys`-related crashes implicate.
5. If crashes persist after all of this with clean memory tests, the fault is likely motherboard-level — time for professional diagnosis.

The [24H2 IRQL_NOT_LESS_OR_EQUAL walkthrough](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/) covers the same crash on newer Windows builds.

## Closing

`DRIVER_IRQL_NOT_LESS_OR_EQUAL` is one of the most fixable blue screens because it usually tells you exactly which driver misbehaved. Read the filename, get that driver's proper manufacturer version (or roll it back), and the crash typically ends there. The tech's secret isn't any exotic tool — it's refusing to guess when the blue screen already gave you the answer.
