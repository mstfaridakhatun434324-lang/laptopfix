---
title: "USB Ports Not Working on Your ASUS Laptop? Fix Them"
slug: how-to-fix-usb-ports-not-working-on-asus-laptop
date: 2026-10-13
categories: ["drivers"]
tags: ["usb ports", "asus laptop", "usb fix", "device manager", "windows 11"]
description: "USB ports dead on your ASUS laptop? Diagnose power, driver, and hardware causes and restore every port with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-usb-ports-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why did all my USB ports stop working at once?"
    a: "All ports failing simultaneously points to a system-level cause, not individual port damage: the USB host controller driver crashed, USB selective suspend parked the controllers, or a Windows update broke USB enumeration. A full shutdown (not restart) plus a controller driver reset fixes most all-at-once failures. Individual port failures, by contrast, suggest physical damage."
  - q: "How do I reset the USB controllers on my ASUS laptop?"
    a: "Open Device Manager, expand Universal Serial Bus controllers, and uninstall every USB Root Hub and host controller entry (don't tick driver deletion). Then restart — Windows redetects and reinstalls all USB controllers fresh at boot. This clears corrupted controller states that survive normal restarts and is the highest-yield fix for dead ports."
  - q: "Can a BIOS setting disable USB ports?"
    a: "Yes. ASUS BIOS includes USB configuration options — legacy USB support, xHCI mode, and per-port enables — that can disable ports if misconfigured. If USB devices don't work even in the BIOS or during boot, firmware settings are suspect. Loading optimized defaults in the BIOS restores sane USB configuration."
  - q: "Why do my USB ports work in BIOS but not in Windows?"
    a: "That split proves the hardware and firmware are fine — the problem is purely Windows-side: the USB driver stack, selective suspend, or a corrupted controller driver. Focus on Device Manager's USB controllers, disable selective suspend, and reinstall the chipset driver from ASUS. Don't waste time on hardware theories when the BIOS test passes."
---

Every USB port dead at once. Or one port that only works if you wiggle the plug. Or ports that work for a mouse but not for an external drive. USB failures on ASUS laptops span the full range from trivial to terminal, but they diagnose cleanly because USB is a layered system: physical port, controller hardware, controller driver, power management, and the device itself. Find which layer broke and the fix is usually straightforward.

The single most useful diagnostic question is scope: all ports or one port? All ports dead means software or controller-level trouble — very fixable. One dead port while others work means physical damage — much less fixable. This guide handles both, starting with the resets that fix the common cases in minutes.

## Why this happens

- **USB controller driver corrupted:** The host controller driver that manages all ports can corrupt (often after a Windows update), killing every port at once.
- **USB selective suspend:** Windows' power feature suspends "idle" USB devices and controllers; on some ASUS models they never wake properly.
- **Fast Startup preserving broken state:** The hibernated USB driver state survives restarts, keeping ports dead until a true shutdown clears it.
- **Physical port damage:** Bent pins, cracked solder joints from cable stress, or debris in the port kill individual ports permanently.
- **Power delivery limits:** An underpowered port (or too many bus-powered devices) causes dropouts and detection failures, especially with external drives.
- **BIOS USB misconfiguration:** Disabled xHCI, legacy USB settings, or a bad BIOS update can disable ports at firmware level.
- **Chipset driver outdated:** The chipset driver underpins USB controllers; an outdated or corrupted one produces flaky USB behavior across all ports.
- **Static discharge damage:** A static shock to a port can fry its controller channel — rare, but it happens, and it kills that port for good.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do a true shutdown and power-drain

1. Hold **Shift** and click **Shut down** (not Restart) — this clears Fast Startup's preserved USB driver state.
2. Unplug the charger and all USB devices. Hold the power button for **15 seconds** to drain residual power.
3. Reconnect only the charger, boot up, and test each USB port with a simple device like a mouse. This alone revives a large share of "all ports dead" cases.

### Fix 2: Test scope — one port or all ports

1. Try the same known-good USB device (a basic mouse is ideal) in every port on the laptop.
2. If all ports fail, it's system-level — continue with the driver fixes. If only one port fails, inspect it with a flashlight for bent pins or debris, and skip to Fix 7's hardware assessment.
3. Test both USB-A and USB-C ports separately; they use different controllers and fail independently.

### Fix 3: Reinstall the USB controllers

1. Open Device Manager (**Win+X > Device Manager**) and expand **Universal Serial Bus controllers**.
2. Right-click each **USB Root Hub** and host controller entry and choose **Uninstall device** (do NOT tick driver deletion — you want Windows to reinstall its own drivers).
3. Restart the laptop. Windows redetects every USB controller fresh at boot.
4. Test all ports again. This is the definitive fix for corrupted controller states.

### Fix 4: Disable USB selective suspend

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set it to **Disabled** for both On battery and Plugged in.
3. In Device Manager, for each **USB Root Hub** under Universal Serial Bus controllers, open **Properties > Power Management** and uncheck **Allow the computer to turn off this device to save power**.
4. Restart and test — this fixes ports that die after sleep or idle periods. The [selective suspend guide](/articles/how-to-turn-off-usb-selective-suspend-on-windows-11/) covers this setting's full implications.

### Fix 5: Update the chipset driver from ASUS

1. Find your ASUS model number (sticker on the bottom or **Fn+Esc**... on ASUS it's usually just the sticker or `msinfo32`).
2. Download the latest **chipset driver** from ASUS support for your model and install it, then restart.
3. The chipset driver owns the USB controllers' low-level behavior; updating it fixes flakiness that controller reinstalls don't touch. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) also documents USB troubleshooting steps worth trying.

### Fix 6: Check the BIOS USB settings

1. Restart and press **F2** (or **Del**) at the ASUS logo to enter the BIOS.
2. Find USB configuration and confirm **xHCI** / USB ports are enabled. Try **Load Optimized Defaults** if anything looks odd.
3. Test a USB keyboard in the BIOS itself — if it works here but not in Windows, the problem is definitively Windows-side and the driver fixes above are the answer.
4. Check for a BIOS update on ASUS support mentioning USB fixes, and install it with the charger connected.

### Fix 7: Assess physical port damage

1. Inspect the dead port with a flashlight: bent pins inside USB-A, lint packed in USB-C, or a loose, wobbly connector all mean physical damage.
2. Clean debris gently with a wooden toothpick (never metal) while the laptop is fully off.
3. A single physically damaged port on an otherwise healthy laptop is best worked around — use the remaining ports or a USB hub on a good port. Board-level port repair is possible but rarely economical; the [24H2 USB troubleshooting guide](/articles/how-to-fix-usb-ports-not-working-in-windows-11-24h2/) has more on distinguishing hardware from software failures.

## Closing

USB port failures look catastrophic but are usually a driver-state problem wearing a hardware costume: true-shutdown, controller reinstall, selective suspend off, chipset driver update — in that order — revives the great majority of dead ports. The scope test (all ports vs one port) is the key diagnostic that keeps you from reinstalling drivers for a bent pin or mourning a port that just needed its controller reset. Work the layers, and your ports will be back in business.
