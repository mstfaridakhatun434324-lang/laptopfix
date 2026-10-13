---
title: "ELAN Touchpad Not Working on Windows 10? 7 Driver Fixes"
slug: how-to-fix-elan-touchpad-not-working-on-windows-10
date: 2026-09-18
categories: ["drivers"]
tags: ["elan touchpad", "touchpad not working", "windows 10", "i2c driver"]
description: "ELAN touchpad dead on Windows 10? Restore it with these 7 driver fixes — enable the device, reinstall the ELAN driver, and fix I2C HID conflicts."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working-on-windows-10.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working on Windows 10?"
    a: "The most common cause is a Windows 10 update replacing the ELAN driver with an incompatible version or disabling the I2C HID device the touchpad depends on. Accidentally toggling the touchpad off with Fn + F-key is also frequent, as is the touchpad being disabled in BIOS. Less commonly, the ELAN driver files corrupt, or a conflicting Windows Precision driver tries to manage the same hardware. The fixes below address each cause in order."
  - q: "Where is the ELAN touchpad in Device Manager?"
    a: "ELAN touchpads appear in two places: under Human Interface Devices as I2C HID Device or ELAN Input Device, and under Mice and other pointing devices as ELAN PS/2 Port Input Device or similar. If either entry shows a yellow warning or is disabled, that's your problem. If both are missing, enable Show hidden devices — a greyed-out entry means Windows disabled it after a failed start."
  - q: "Should I use the ELAN driver or the Windows Precision driver?"
    a: "Use whichever your laptop manufacturer provides for your model. ELAN touchpads with manufacturer ELAN drivers offer the vendor's gesture suite; some newer ELAN hardware runs on Microsoft's Precision drivers instead. Don't mix them — installing a Precision driver over an ELAN-managed device (or vice versa) causes exactly the dead-touchpad symptom. Get the driver from your laptop maker's support site for your exact model."
  - q: "Can I fix the ELAN touchpad without a mouse?"
    a: "Yes — Windows 10 is fully keyboard-navigable. Press Win + X then M for Device Manager, use Tab and arrow keys to navigate, the Menu key (or Shift + F10) for right-click, and Enter to activate. Enable Mouse Keys as a backup: press Left Alt + Left Shift + Num Lock, then use the number pad to move the pointer. The [general touchpad guide](/articles/best-way-to-fix-touchpad-not-working/) has more keyboard-only navigation tips."
---

The cursor won't move. Taps do nothing, gestures are gone, and you're stuck navigating with a keyboard or a borrowed USB mouse. ELAN touchpads — common in ASUS, Lenovo, Acer, and MSI laptops — are particularly prone to driver failures on Windows 10, where updates love to replace the working ELAN driver with something incompatible.

ELAN touchpads talk to Windows through two channels: the ELAN driver itself and the I2C HID device underneath it. Either one failing kills the touchpad. This guide repairs both, starting with the instant checks.

## Why this happens

- **Touchpad toggled off via Fn key:** Most laptops have an **Fn + F-key** touchpad toggle that's easy to hit accidentally.
- **Windows Update replaced the ELAN driver:** A pushed driver incompatible with your ELAN hardware revision.
- **I2C HID device failed or disabled:** The underlying bus device the ELAN driver depends on stops working.
- **Touchpad disabled in BIOS:** Firmware-level disable invisible to Windows.
- **Corrupt ELAN driver files:** Partial updates leave the driver unable to start.
- **Conflicting Precision driver:** Windows trying to manage ELAN hardware with Microsoft's Precision driver stack.
- **Touchpad disabled in Settings:** Windows 10's touchpad toggle turned off, sometimes by update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle the touchpad back on (keyboard and Settings)

The most common cause is also the fastest fix.

1. Press the touchpad toggle key — usually **Fn + F5**, **Fn + F7**, or **Fn + F9** (look for the touchpad icon on your function keys).
2. Go to **Settings > Devices > Touchpad** and make sure the **Touchpad** toggle is **On**.
3. Untick **Leave touchpad on when a mouse is connected** temporarily if a USB mouse is plugged in — this setting auto-disables the touchpad.
4. Unplug any USB mouse and test the touchpad.

If the Fn toggle doesn't respond, the ELAN driver isn't running — which confirms a driver problem and points you to the fixes below.

### Fix 2: Re-enable the ELAN device in Device Manager

Windows may have disabled the device after a failed start.

1. Press **Win + X**, then **M** to open Device Manager.
2. Expand **Human Interface Devices** and look for **I2C HID Device** and any **ELAN** entries.
3. Expand **Mice and other pointing devices** and look for **ELAN PS/2 Port Input Device** or **ELAN Input Device**.
4. If any entry is greyed out or has a down arrow, right-click (Menu key or **Shift + F10**) and choose **Enable device**.
5. If entries show a yellow warning, note the error code — Code 10 and Code 24 are the common ones here.

Enable everything ELAN/I2C-related, then test. If the touchpad springs to life, a failed start had left it disabled.

### Fix 3: Update the ELAN driver from the manufacturer

Get the driver built for your exact ELAN hardware revision.

1. In Device Manager, note the exact ELAN device name under **Mice and other pointing devices**.
2. Go to your laptop maker's support site (ASUS, Lenovo, Acer, MSI) and download the **touchpad/ELAN driver** for your exact model.
3. Install it and restart.
4. Check **Settings > Devices > Touchpad** — the ELAN tab or additional settings should reappear.

Avoid generic ELAN drivers from third-party sites; ELAN hardware revisions differ, and the wrong revision driver installs but doesn't work. The [ELAN-specific reference](/articles/how-do-i-fix-elan-touchpad-not-working/) covers revision matching. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the Device Manager update and rollback steps used here if you need screenshots.

### Fix 4: Reinstall the I2C HID device

The ELAN driver sits on top of the I2C bus — if the bus device is broken, the touchpad can't work.

1. In Device Manager, under **Human Interface Devices**, right-click **I2C HID Device** and choose **Uninstall device**.
2. If there are multiple I2C HID entries, uninstall the one corresponding to the touchpad (trial and error is safe — they reinstall on reboot).
3. **Restart** the laptop — Windows redetects the I2C bus and reinstalls the driver.
4. Test the touchpad after reboot.

Do not uninstall every I2C device at once blindly; do them one at a time with a restart between if you're unsure which is the touchpad.

### Fix 5: Roll back the driver

If the touchpad died right after a Windows 10 update, revert it.

1. In Device Manager, right-click the ELAN device under **Mice and other pointing devices** and choose **Properties**.
2. Go to the **Driver** tab and click **Roll Back Driver** if available.
3. Restart and test.
4. Pause Windows updates (**Settings > Update & Security > Windows Update > Pause updates**) to prevent the bad driver returning.
5. If rollback is unavailable, manually install the previous driver version from the manufacturer's site.

This is the highest-success fix for update-triggered ELAN failures.

### Fix 6: Check the BIOS touchpad setting

A firmware-disabled touchpad ignores every Windows fix.

1. Restart and enter BIOS/UEFI (**F2**, **Del**, or **F10** — varies by brand).
2. Look under **Advanced** or **Devices** for **Internal Pointing Device** or **Touchpad**.
3. Set it to **Enabled**.
4. Save and exit, then test in Windows.

While in the BIOS, also check for a BIOS update on the manufacturer's site — some updates fix ELAN initialization bugs. If the touchpad works in the BIOS menus (on models with mouse-driven BIOS), the hardware is fine.

### Fix 7: Remove conflicting drivers and test hardware

Clear out driver conflicts and verify the hardware itself.

1. In Device Manager, **View > Show hidden devices**, and uninstall any duplicate or greyed-out ELAN/mouse entries.
2. Check **Settings > Apps** for multiple touchpad utilities (ELAN Smart-Pad plus another vendor's tool) and remove the ones you don't need.
3. Run `sfc /scannow` in an admin Command Prompt to repair system files.
4. Test the touchpad in the BIOS or a Linux live USB — working there means Windows is the problem; dead everywhere means the touchpad hardware or its ribbon cable failed.

Hardware failure usually follows physical damage or liquid exposure. The ribbon cable connecting the touchpad can also work loose — reseating it requires opening the laptop. For Synaptics-based touchpads with similar symptoms, see the [Synaptics guide](/articles/best-way-to-fix-synaptics-touchpad-not-working/).

## Closing

ELAN touchpad failures on Windows 10 follow a familiar script: an update breaks the driver, the I2C device fails underneath it, or the Fn toggle got hit. The re-enable, reinstall, and rollback sequence covers nearly every case — and once the manufacturer's ELAN driver is in place with updates paused, the touchpad stays working.
