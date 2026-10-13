---
title: "How to Fix Touchpad Not Working on ASUS Laptop"
slug: how-to-fix-touchpad-not-working-on-asus-laptop
date: 2026-10-03
categories: ["drivers"]
tags: ["asus touchpad not working", "asus laptop touchpad", "touchpad driver asus", "precision touchpad"]
description: "Touchpad dead on your ASUS laptop? Fix it with the ASUS Precision Touchpad driver, function-key toggles, and BIOS checks — model-specific steps inside."
thumbnail: "/images/thumbs/how-to-fix-touchpad-not-working-on-asus-laptop.webp"
faqs:
  - q: "Which key turns the touchpad on and off on ASUS laptops?"
    a: "On most ASUS laptops it is Fn + F9, though some models use F6 or a dedicated touchpad key — look for the touchpad icon on the function row. Pressing it accidentally is the number one cause of a suddenly dead touchpad. If the toggle does nothing, the ASUS Precision Touchpad driver is likely missing, which also disables the hotkey."
  - q: "Why did my ASUS touchpad stop working after a Windows update?"
    a: "Windows Update frequently replaces the ASUS Precision Touchpad driver with a generic Microsoft driver that lacks ASUS-specific features, or it installs a version mismatch with the ATK Package hotkey software. Reinstalling the Precision Touchpad driver from ASUS support for your exact model, plus the ATK Package, restores full function."
  - q: "Should I use the ASUS driver or the Microsoft precision driver?"
    a: "Use the ASUS Precision Touchpad driver from ASUS support for your exact model. It is built on Microsoft's precision driver stack but adds the model-specific configuration ASUS laptops need. The generic driver from Windows Update works for basic movement on some models but often breaks gestures and the Fn toggle."
  - q: "Does a BIOS update fix ASUS touchpad problems?"
    a: "Rarely, but it matters when the touchpad is not detected at all in Device Manager. Some ASUS BIOS versions include touchpad firmware settings, and a few updates fixed I2C touchpad detection. Check the BIOS changelog for touchpad mentions before updating, and confirm the touchpad is enabled in the BIOS first."
---

ASUS laptops use precision touchpads driven by a model-specific ASUS driver layered on Microsoft's precision stack, plus the ATK Package that handles the Fn hotkeys. When the touchpad dies on an ASUS, it is usually one of three things: the Fn toggle got hit by accident, Windows Update swapped in the wrong driver, or the I2C device the touchpad hangs off stopped responding.

The good news is that ASUS documents this well and provides every driver you need on its support site. The fixes below start with the instant checks — the toggle key and Settings — then move to driver surgery, and finish with the BIOS and hardware checks for the cases where the touchpad is not detected at all.

## Why this happens

- **The Fn touchpad toggle was pressed accidentally.** Fn + F9 (or F6) disables the touchpad instantly with no on-screen warning on many models.
- **Windows Update replaced the ASUS Precision Touchpad driver** with a generic version that breaks gestures or the whole device.
- **ATK Package / hotkey driver missing or outdated**, which disables the Fn toggle and some touchpad features.
- **Touchpad disabled in Windows Settings** under Bluetooth & devices > Touchpad, sometimes flipped by an update.
- **I2C HID device error in Device Manager** — the touchpad's bus interface failing to start, shown as a yellow warning.
- **Touchpad disabled in the BIOS** on models that expose the setting, or a BIOS bug affecting I2C detection.
- **Loose ribbon cable or failed touchpad hardware**, typically after a drop or a battery swelling underneath the palm rest.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Press the touchpad toggle key

Before anything else, try Fn + F9 — the ASUS touchpad toggle. On some models it is F6 or a dedicated key; check the function row for a touchpad icon. Press it once, wait a few seconds, and test. If an on-screen indicator appears saying the touchpad is on but nothing moves, the toggle works and the problem is the driver — move to Fix 3.

1. Locate the touchpad icon on the function row (usually F9).
2. Press Fn + the key once and wait five seconds.
3. Test the touchpad. Repeat once in case the first press only woke the keyboard.
4. If nothing changes, continue to the Settings check.

### Fix 2: Re-enable the touchpad in Windows Settings

Windows has its own touchpad master switch that updates occasionally flip. Open Settings > Bluetooth & devices > Touchpad and make sure the toggle is on. Also check the 'Leave touchpad on when a mouse is connected' option — with some ASUS models and docks, Windows disables the touchpad the moment any USB mouse is detected, which looks exactly like a dead touchpad.

1. Open Settings > Bluetooth & devices > Touchpad.
2. Turn the Touchpad toggle on.
3. Enable 'Leave touchpad on when a mouse is connected'.
4. Test gestures like two-finger scroll to confirm full function.

### Fix 3: Reinstall the ASUS Precision Touchpad driver

This is the core fix. Download the Precision Touchpad driver from ASUS support for your exact model — not a generic driver, and not whatever Windows Update offers. Uninstall the current driver first with its software removed so the broken version cannot come back. For background on how these drivers differ across models, see [fixing the Synaptics touchpad on ASUS](/articles/how-to-fix-synaptics-touchpad-not-working-on-asus-laptop/) models that use the older stack.

1. On ASUS support, enter your exact model and download the Touchpad / Precision Touchpad driver.
2. In Device Manager, uninstall the touchpad device, ticking 'delete the driver software'.
3. Install the downloaded ASUS driver and reboot.
4. Verify gestures and the Fn toggle work again.

### Fix 4: Reinstall the ATK Package

The ATK Package (ATKACPI driver and hotkey utilities) is what makes Fn + F9 actually toggle the touchpad on ASUS machines. If the toggle key does nothing at all — no indicator, no effect — the ATK software is missing or broken. Download the ATK Package from ASUS support for your model, install it, and reboot before testing the hotkey again. Microsoft documents the precision touchpad driver model in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Download the ATK Package from ASUS support for your exact model.
2. Uninstall any existing ATK entries in Settings > Apps first.
3. Install the fresh ATK Package and reboot.
4. Press Fn + F9 and confirm the on-screen touchpad indicator appears.

### Fix 5: Fix the I2C HID device error

Many ASUS touchpads connect over I2C, and Device Manager may show 'I2C HID Device' with a yellow warning instead of a touchpad entry. Uninstall that device with its driver deleted, then scan for hardware changes. If it reinstalls cleanly, the touchpad comes back; if the warning returns immediately, the bus itself is failing — try the BIOS reset in Fix 6.

1. In Device Manager, expand Human Interface Devices.
2. Right-click the flagged I2C HID Device and uninstall it, deleting the driver.
3. Click Action > Scan for hardware changes.
4. If the warning persists, shut down, unplug for 60 seconds, then boot and recheck.

### Fix 6: Check the touchpad in the BIOS

Reboot into the BIOS (F2 on most ASUS laptops) and look for a touchpad or internal pointing device option — enable it if present. Some ASUS BIOS versions also let you switch the touchpad between Advanced and Basic modes; Advanced is the correct setting for the precision driver. While you are there, note whether the touchpad works in the BIOS menus on models that support mouse input there.

1. Reboot and press F2 to enter the BIOS.
2. Find the touchpad / internal pointing device setting and enable it.
3. Set the mode to Advanced if the option exists.
4. Save, exit, and test in Windows.

### Fix 7: Test for hardware failure

If the touchpad is absent from Device Manager even with hidden devices shown, and the BIOS has no trace of it, suspect the ribbon cable or the touchpad itself. A swollen battery pressing up under the palm rest is a classic ASUS failure that kills the touchpad — if the palm rest feels raised or the touchpad clicks oddly, stop using the battery and get it replaced. Otherwise, ASUS service can replace the touchpad module; the part is model-specific.

1. Show hidden devices in Device Manager and look for any touchpad entry.
2. Check for a swollen battery pushing up the palm rest.
3. Boot a Linux live USB — no touchpad there means hardware.
4. Contact ASUS support for a touchpad or cable replacement.

## Closing

On ASUS laptops the fix is almost always software: the Fn toggle, the Settings switch, or the Precision Touchpad driver from ASUS support for your exact model. The ATK Package restores the hotkey when the toggle itself is dead, and the I2C reinstall handles the yellow-warning cases. Only when the device is invisible everywhere — Device Manager, BIOS, and a live Linux USB — should you treat it as a hardware repair. If a Windows update keeps swapping the driver back, the [Windows 11 Synaptics driver guide](/articles/how-to-fix-synaptics-touchpad-not-working-on-windows-11/) explains how to lock in the right version.
