---
title: "Synaptics Touchpad Not Working? Step-by-Step Fix for Windows Laptops"
slug: "how-to-fix-synaptics-touchpad-not-working-step-by-step"
date: "2026-09-10"
categories: ["drivers"]
tags: ["synaptics touchpad", "touchpad driver", "windows 11", "mouse not working", "precision touchpad"]
description: "Synaptics touchpad dead on your laptop? Follow this step-by-step guide covering function keys, driver reinstalls, I2C conflicts, and BIOS settings to restore your touchpad."
thumbnail: "/images/thumbs/how-to-fix-synaptics-touchpad-not-working-step-by-step.webp"
faqs:
  - q: "Why does my Synaptics touchpad stop working after a Windows update?"
    a: "Windows Update often replaces the manufacturer's Synaptics driver with a generic Microsoft precision touchpad driver, or installs a Synaptics version that does not match your laptop's firmware. The result is a dead or erratic touchpad. Reinstalling the original driver from your laptop maker's support page, or rolling back to the previous driver version in Device Manager, usually restores full function within minutes."
  - q: "My touchpad works but gestures do not. Is that a driver issue?"
    a: "Yes, almost always. Basic cursor movement can work with a fallback PS/2-compatible driver while multi-finger gestures, scrolling, and tap settings require the full Synaptics driver plus its control panel. Reinstall the manufacturer's touchpad driver package and check the Synaptics or precision touchpad settings in Windows Settings to re-enable gestures."
  - q: "Can a BIOS setting disable the touchpad?"
    a: "On many business laptops, the BIOS includes an option to disable the internal pointing device, sometimes with a mode that turns it off when an external mouse is present. Enter the BIOS setup, look under Advanced or Devices for the touchpad or internal pointing device setting, make sure it is enabled, then save and exit. This is worth checking if the touchpad never appears in Device Manager."
  - q: "What if the touchpad is missing from Device Manager entirely?"
    a: "First enable hidden devices in Device Manager, then look under Human Interface Devices and Mice for Synaptics or I2C HID entries. If nothing appears, check the BIOS to confirm the touchpad is enabled, then scan for hardware changes. A touchpad that is invisible in both Windows and the BIOS, across a clean OS install, usually indicates a disconnected ribbon cable or a failed touchpad module."
---

A dead Synaptics touchpad turns a laptop into a desk-bound machine. Whether yours stopped responding entirely, moves erratically, lost its gestures, or vanished from Device Manager, the cause is usually a driver conflict, a toggled setting, or a power-state glitch — all fixable without opening the laptop. This guide walks through every fix in order, from the thirty-second checks to the deeper driver surgery, so follow it top to bottom.

Before diving in, grab a USB mouse if you have one. Most of these steps are much easier with a working pointer, though every one of them can also be done with keyboard navigation (Tab, arrow keys, and Enter) if you are stuck without a mouse.

## Why this happens

- **Driver replaced by Windows Update:** Windows frequently swaps the manufacturer's Synaptics driver for a generic one that does not match the touchpad firmware.
- **Touchpad disabled by function key:** Most laptops have an Fn + F-key combination that toggles the touchpad, and it is easy to hit accidentally.
- **I2C HID driver conflict:** Modern touchpads communicate over the I2C bus; a failed I2C HID device entry can block the Synaptics driver from loading.
- **Corrupted Synaptics driver install:** Partial updates or failed installs leave the driver in a half-working state with gestures missing.
- **Touchpad disabled in Windows Settings:** The touchpad toggle can be switched off by an update, a policy, or a previous troubleshooting session.
- **BIOS pointing-device setting:** Some laptops disable the touchpad at firmware level, making it invisible to Windows entirely.
- **Power management suspending the device:** Aggressive power saving can put the touchpad's I2C interface to sleep and never wake it.
- **Loose ribbon cable or hardware failure:** A disconnected internal cable — common after drops or repairs — kills the touchpad physically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the touchpad toggle key and Settings

Rule out the simple stuff first — this fix takes under a minute.

1. Look for a touchpad icon on your function keys (often F5, F7, or F9) and press Fn plus that key to toggle the touchpad on.
2. Open Settings > Bluetooth & devices > Touchpad and confirm the Touchpad switch is On.
3. In the same page, check "Leave touchpad on when a mouse is connected" if you use both.
4. Expand Taps and Scroll and zoom to confirm your gestures are enabled.
5. Test the touchpad after each change — if it springs to life, you are done.

### Fix 2: Run the hardware troubleshooter

Windows still ships a hardware troubleshooter that can detect disabled or misconfigured input devices.

1. Press Win + R, type `msdt.exe -id DeviceDiagnostic`, and press Enter.
2. Click Next and let the troubleshooter scan for hardware problems.
3. Apply any fix it recommends, especially ones mentioning the pointing device.
4. Restart the laptop even if it claims nothing was wrong — the scan can reset device state.
5. If the touchpad remains dead, continue to Device Manager.

### Fix 3: Enable and reinstall the driver in Device Manager

This is the fix that resolves most Synaptics problems — a proper driver reset.

1. Press Win + X, open Device Manager, and expand "Mice and other pointing devices" and "Human Interface Devices".
2. Look for Synaptics, "Synaptics SMBus TouchPad", or "I2C HID Device" entries.
3. If an entry has a down arrow, right-click it and choose Enable device.
4. If it has a yellow warning, right-click, choose Uninstall device, and tick "Attempt to remove the driver for this device".
5. Click Action > Scan for hardware changes and let Windows redetect the touchpad.
6. Restart the laptop and test the touchpad and its gestures.
7. If Windows installs only a basic driver with no gestures, move on to the manufacturer's package below.

### Fix 4: Install the manufacturer's Synaptics driver

The generic driver gives you a cursor; the manufacturer's package gives you the full touchpad.

1. Visit your laptop maker's support site — for example [Dell's official support](https://www.dell.com/support) — enter your model, and download the latest touchpad or input driver.
2. If the maker offers a Synaptics-specific package, prefer it over the generic "precision touchpad" one.
3. Run the installer, accept the defaults, and restart when prompted.
4. Open Settings > Bluetooth & devices > Touchpad and configure gestures to your liking.
5. Look for a Synaptics control panel entry in the system tray or Settings for advanced options like palm rejection and sensitivity.
6. If the manufacturer's driver is old, check whether your model supports Microsoft's precision touchpad driver instead — some newer Synaptics touchpads work better with it.

### Fix 5: Fix the I2C HID device conflict

When the touchpad communicates over I2C, a broken I2C HID entry blocks everything.

1. In Device Manager, expand Human Interface Devices.
2. Find "I2C HID Device" — if it shows a yellow warning with Code 10, this is your culprit.
3. Right-click it, choose Uninstall device, and do NOT tick driver removal (keep the driver, just reset the device).
4. Click Action > Scan for hardware changes.
5. If the warning returns, update the chipset driver from your laptop maker's support site — the I2C controller belongs to the chipset.
6. Restart and verify the touchpad responds; for the [Windows 11 variant of this issue](/articles/how-to-fix-synaptics-touchpad-not-working-on-windows-11/), the same chipset-driver approach applies.

### Fix 6: Check BIOS settings for the pointing device

If the touchpad never appears in Device Manager at all, the BIOS may be hiding it.

1. Restart the laptop and press the BIOS key (F2, F10, or Del depending on brand) during boot.
2. Navigate to Advanced, Devices, or a similar section and find the touchpad or internal pointing device option.
3. Set it to Enabled (avoid "Auto" modes that disable it when a USB mouse is plugged in, at least while testing).
4. Save and exit, boot into Windows, and check Device Manager again.
5. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the OS-side touchpad settings if you need to reconfigure them afterward.

### Fix 7: Disable power management on the touchpad

Power saving can suspend the touchpad's interface and fail to wake it.

1. In Device Manager, find the Synaptics or I2C HID entry, right-click, and choose Properties.
2. On the Power Management tab, uncheck "Allow the computer to turn off this device to save power".
3. Open Control Panel > Power Options > Change advanced power settings.
4. Expand USB settings > USB selective suspend setting and set it to Disabled (some touchpads enumerate over internal USB).
5. Restart and test the touchpad after a sleep-wake cycle, which is when this bug usually strikes.

### Fix 8: Test in BIOS and consider hardware service

If no software fix has worked, determine whether the touchpad is physically alive.

1. Restart into the BIOS setup — if the touchpad works there (some BIOS menus support it), the hardware is fine and the problem is purely Windows-side.
2. Boot from a Linux live USB and test the touchpad there as a second opinion.
3. If it is dead in BIOS, Linux, and Windows, the ribbon cable is likely loose or the module has failed.
4. Reseating the cable requires opening the laptop — check your warranty first, since this can void it on some models.
5. For a related input-device failure pattern, see our guide on [keyboards not working on laptops](/articles/how-to-fix-keyboard-not-working-on-laptop-on-windows-11/), which shares several diagnostic steps.

## Closing

Synaptics touchpad failures are overwhelmingly software problems — a toggled key, a driver swap, or an I2C conflict — and the sequence above catches every common variant. Once it is working again, keep the manufacturer's touchpad driver installed and be cautious with third-party driver updaters, which are the most frequent cause of the "worked yesterday, dead today" touchpad mystery.
