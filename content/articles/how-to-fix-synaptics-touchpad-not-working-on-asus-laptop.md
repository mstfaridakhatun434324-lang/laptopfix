---
title: "Synaptics Touchpad Not Working on ASUS Laptop: Complete Fix Guide"
slug: how-to-fix-synaptics-touchpad-not-working-on-asus-laptop
date: 2026-09-19
categories: ["drivers"]
tags: ["synaptics touchpad", "asus laptop", "touchpad not working", "windows 11", "driver fix"]
description: "Your ASUS laptop touchpad stopped responding? This guide walks through the exact driver, BIOS, and Windows settings fixes that bring a dead Synaptics touchpad back to life."
thumbnail: "/images/thumbs/how-to-fix-synaptics-touchpad-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why does my ASUS touchpad suddenly stop working after a Windows update?"
    a: "Windows updates often replace the ASUS-tuned Synaptics driver with a generic Microsoft HID driver, or flag the old driver as incompatible and disable the device. On many ASUS models the update also resets the touchpad enable state in firmware. Reinstalling the Synaptics driver from ASUS support and re-enabling the device in Device Manager restores full gesture and cursor control in most cases."
  - q: "How do I know whether my ASUS laptop uses a Synaptics or ELAN touchpad?"
    a: "Open Device Manager, expand Human Interface Devices or Mice and other pointing devices, and look for an entry containing Synaptics or ELAN. If neither appears, enable hidden devices and check again. Knowing the exact vendor matters because installing the wrong manufacturer's driver can leave the touchpad completely dead, so confirm before downloading anything."
  - q: "The touchpad toggle is missing from Windows Settings. What does that mean?"
    a: "A missing touchpad toggle in Settings under Bluetooth and devices almost always means Windows cannot see the touchpad hardware at all. The driver is either missing, disabled, or the device was switched off at the firmware level. Work through driver reinstallation and check for a hardware disable key combination, since the setting cannot appear until Windows detects the device."
  - q: "Can a BIOS update fix a dead Synaptics touchpad on an ASUS laptop?"
    a: "Yes, in some cases. ASUS BIOS updates sometimes include embedded controller fixes that re-enable touchpad communication over the I2C bus, especially on Vivobook and Zenbook models. Check the ASUS support page for your exact model for a BIOS newer than the one installed. Flash it on AC power with nothing else running, and test the touchpad after the reboot."
---

A dead touchpad turns a perfectly good ASUS laptop into a machine that needs a desk, a mouse, and patience. If your cursor froze, gestures vanished, or the touchpad toggle disappeared from Settings after a Windows update, you are dealing with one of the most common ASUS driver problems. The good news is that it is almost never hardware damage — it is a driver, firmware, or settings mismatch that you can fix yourself in under half an hour.

ASUS uses Synaptics touchpads on a huge share of its Vivobook, Zenbook, and older ROG models. These touchpads talk to Windows over the I2C bus, and they depend on a precisely matched driver. When Windows Update pushes a generic driver, when the ASUS Smart Gesture utility gets removed, or when a function-key press disables the pad by accident, the whole input stack goes quiet. This guide covers every proven fix in the right order, starting with the checks that take ten seconds. For a version of this problem that is not tied to a specific brand, see our general [Synaptics touchpad repair walkthrough](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/), and if you are auditing other hardware while you are at it, our guide on [checking driver versions in Device Manager](/articles/how-to-check-driver-version-in-device-manager-on-laptop/) will help.

## Why this happens

- **Windows Update replaced the Synaptics driver** with a generic Microsoft HID-compliant mouse driver that does not support the I2C touchpad interface, so the pad stops responding entirely.
- **The touchpad was disabled by the Fn key shortcut** — on most ASUS laptops Fn + F9 toggles the touchpad, and a single accidental press during typing can switch it off without any on-screen warning.
- **The device is disabled in Device Manager**, sometimes automatically after a driver conflict, leaving the hardware present but switched off at the driver level.
- **ASUS Smart Gesture or the precision touchpad driver was uninstalled**, removing the software layer that translates touch input into cursor movement and gestures.
- **The touchpad is disabled in the BIOS/UEFI firmware** under Advanced settings, which makes Windows unable to detect it no matter which driver you install.
- **Corrupted driver files after a failed update** leave the Synaptics device showing a yellow warning icon with error code 10, 24, or 43.
- **A fast startup or hibernation glitch** leaves the embedded controller in a bad state, so the touchpad is not initialized during boot even though everything is configured correctly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the Fn + F9 touchpad toggle

Before touching any software, rule out the simplest cause. On the vast majority of ASUS laptops, Fn + F9 enables or disables the touchpad. Look for a touchpad icon on the F9 key itself. Press Fn + F9 once, wait three seconds, and test the cursor. Some newer Zenbook models use Fn + F6 instead, so check your function row for the icon. If you see a brief on-screen indicator, the pad was simply switched off. This single key combination resolves the problem more often than any other step.

1. Locate the touchpad icon on your function keys (usually F9, sometimes F6).
2. Press and hold Fn, then tap that key once.
3. Wait three seconds and move your finger across the pad.
4. If an on-screen prompt appears, press the key combination once more to confirm the enabled state.

### Fix 2: Verify the touchpad is enabled in Windows Settings

Windows 11 has its own touchpad master switch, independent of the Fn key. If it got flipped during an update, the pad will stay dead even with a perfect driver installed.

1. Open Settings with Win + I and go to Bluetooth and devices, then Touchpad.
2. Confirm the Touchpad toggle at the top is set to On.
3. Expand the toggle section and check that cursor speed and gestures are configured.
4. If the entire Touchpad page is missing, skip to Fix 4 — Windows cannot see the device at all.

### Fix 3: Re-enable the device in Device Manager

A disabled device is invisible to Windows but fully present in hardware. This takes under a minute and fixes cases where the driver is fine but the device was switched off.

1. Press Win + X and select Device Manager.
2. Expand Human Interface Devices and look for a Synaptics entry, or check Mice and other pointing devices.
3. If you see a downward arrow on the icon, right-click it and choose Enable device.
4. If no Synaptics entry exists, go to View, select Show hidden devices, and look again.

### Fix 4: Reinstall the Synaptics driver from ASUS support

This is the fix that resolves the majority of persistent cases. The correct driver is the one ASUS built for your exact model, not the generic one Windows Update installed. Download it from the ASUS support site for your model, and you can confirm what is currently installed through the [Windows support documentation](https://support.microsoft.com/en-us/windows) and the steps in our [driver version guide](/articles/how-to-check-driver-version-in-device-manager-on-laptop/).

1. Find your exact model number on the sticker under the laptop or in MyASUS.
2. Visit the ASUS support site, enter the model, and open the Driver and Utility section for your Windows version.
3. Download the Touchpad or Synaptics driver package listed for your model.
4. In Device Manager, right-click the Synaptics device, choose Uninstall device, and tick Delete the driver software if offered.
5. Restart the laptop, then run the ASUS installer you downloaded and reboot once more.

### Fix 5: Roll back the driver to the previous version

If the touchpad died immediately after a Windows update, the previous driver was working and the new one is the problem. Windows keeps the old driver around specifically for this.

1. In Device Manager, right-click the Synaptics touchpad and open Properties.
2. Go to the Driver tab and click Roll Back Driver if the button is active.
3. Choose "Previous version of the driver performed better" and confirm.
4. Restart and test. If the button is greyed out, the old driver is gone — continue to Fix 6.

### Fix 6: Update the BIOS and the embedded controller firmware

On several Vivobook and Zenbook generations, ASUS fixed touchpad initialization bugs through BIOS updates. This is worth doing when the pad is dead even in the BIOS setup screen or during Windows installation.

1. In MyASUS or on the ASUS support page, compare your BIOS version against the latest for your model.
2. Download the BIOS update and run it with the charger connected and no other programs open.
3. Do not touch the laptop during the flash — an interruption can brick the board.
4. After the automatic reboot, enter the BIOS and check under Advanced that the internal pointing device is enabled.

### Fix 7: Reset the embedded controller with a hard power drain

When fast startup leaves the embedded controller in a bad state, no driver change helps because the hardware never initializes. A full power drain resets the controller.

1. Shut the laptop down completely and unplug the charger.
2. If the battery is removable, take it out; otherwise hold the power button for a full 40 seconds.
3. Reconnect the charger (and battery) and power on normally.
4. Test the touchpad on the login screen before signing in — if it works there, the problem was the controller state.

## Closing

Nine times out of ten, a dead Synaptics touchpad on an ASUS laptop comes down to the Fn toggle, a disabled device, or a driver that Windows Update replaced with the wrong one. Work the fixes in order and stop at the first one that restores the cursor — there is no need to flash the BIOS if a driver reinstall already did the job. If the pad is still dead after every step, including in the BIOS setup screen, the ribbon cable may have come loose, and that is a job for a service center.
