---
title: "ELAN Touchpad Not Working on ASUS Laptop? Fix It Now"
slug: "how-to-fix-elan-touchpad-not-working-on-asus-laptop"
date: 2026-09-06
categories: ["drivers"]
tags: ["elan touchpad", "asus laptop", "touchpad not working", "precision touchpad", "mouse not working"]
description: "Touchpad dead on your ASUS laptop? Fix the ELAN touchpad driver with function-key checks, clean driver reinstalls, and BIOS settings."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why did my ASUS touchpad stop working suddenly?"
    a: "The most common sudden cause is accidentally pressing the touchpad disable hotkey, usually Fn plus F9 on ASUS laptops, which toggles the touchpad off with no on-screen warning. The next most common causes are a Windows update replacing the ELAN driver and the touchpad being disabled in Windows settings. Check the hotkey and the settings toggle first; both take seconds and resolve a large share of sudden failures."
  - q: "Should I install the ELAN driver or use Microsoft precision drivers?"
    a: "Use whichever your ASUS model was designed for, which is usually the ELAN driver from ASUS support. Some newer ASUS models use Microsoft Precision drivers natively and work best with those. Check what Device Manager shows under Human Interface Devices: an ELAN entry means install the ASUS ELAN package, while an I2C HID device often means the Precision driver path is correct."
  - q: "The touchpad works in BIOS but not in Windows. What does that mean?"
    a: "That is actually good news: it proves the touchpad hardware is fine and the problem is purely software inside Windows. Test by entering the BIOS or a boot menu and moving the cursor. If it moves there, focus entirely on Windows drivers, settings, and services. A clean reinstall of the ELAN or Precision driver in Windows resolves nearly all of these cases."
  - q: "Two-finger scroll stopped working but the cursor moves. How do I fix it?"
    a: "Partial gesture failure with a working cursor points to driver or settings rather than hardware. Open touchpad settings and confirm gestures are enabled, then check the ELAN or Precision control panel for per-gesture toggles. If settings look right, reinstall the touchpad driver from ASUS support, since gesture handling is the first thing to break when the driver installation degrades."
---

A dead touchpad on an ASUS laptop turns the machine into a desktop that cannot leave the desk. The cursor does not move, taps do nothing, and gestures are gone. Sometimes it fails completely, sometimes only scrolling or tapping breaks while the cursor still moves. Either way, the cause is rarely a dead touchpad; ASUS touchpad failures are overwhelmingly about the hotkey toggle, the driver, or a Windows setting.

ASUS uses ELAN touchpad hardware on many models, with the driver delivered through ASUS support pages. Windows Update has a long history of replacing that driver with something incompatible, which is why touchpads so often die right after an update. The fix sequence is short and reliable once you know it.

Start with the instant checks, then move to the driver work that fixes the persistent cases. If your machine uses a [Dell ELAN touchpad](/articles/how-to-fix-elan-touchpad-not-working-on-dell-laptop/) instead, the same logic applies with Dell's driver source.

## Why this happens

- **Touchpad disabled by hotkey:** Fn plus F9 on most ASUS laptops toggles the touchpad with no obvious indicator.
- **Disabled in Windows settings:** the touchpad toggle in Settings can be switched off, sometimes by updates.
- **Driver replaced by Windows Update:** an incompatible driver gets installed over the ASUS ELAN package.
- **Corrupted ELAN driver:** failed installs leave gesture and cursor handling broken.
- **Touchpad disabled in BIOS:** a BIOS reset can turn the internal pointing device off at the firmware level.
- **Conflicting external mouse software:** settings that disable the touchpad when a mouse is connected can stick.
- **I2C controller driver issue:** the ELAN touchpad talks over I2C, and a broken I2C HID driver breaks communication.
- **Hardware failure:** a loose ribbon cable or dead sensor, uncommon but possible after drops.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Press the touchpad toggle hotkey

This is the number-one cause and the fastest fix. ASUS maps touchpad toggle to Fn plus F9 on most models, and it is easy to hit accidentally. Try it before anything else.

1. Press Fn + F9 together and wait three seconds.
2. Try moving the touchpad and watch for any response.
3. Some models use Fn + F6 or a dedicated touchpad key; check your keyboard icons.
4. Look for an on-screen notification confirming the touchpad state.
5. If the hotkey does nothing, continue to the settings check.

### Fix 2: Enable the touchpad in Windows settings

Windows has its own touchpad master switch, and updates occasionally flip it. Confirming it is on takes seconds and also exposes cursor speed and gesture settings.

1. Open Settings and go to Bluetooth and devices, then Touchpad.
2. Make sure the Touchpad toggle at the top is switched On.
3. Uncheck Leave touchpad on when a mouse is connected for testing.
4. Verify taps and scroll gestures are enabled in the gestures sections.
5. Test the touchpad immediately after each change.

### Fix 3: Check Device Manager for the ELAN device

Device Manager shows whether Windows sees the touchpad hardware and whether its driver is healthy. A missing or error-flagged device directs the rest of the repair.

1. Press Windows + X and open Device Manager.
2. Expand Human Interface Devices and Mice and other pointing devices.
3. Look for ELAN Input Device or I2C HID Device entries.
4. If one shows a yellow warning, note the error code.
5. If nothing touchpad-related appears, click Action, then Scan for hardware changes.

### Fix 4: Re-enable or restart the touchpad device

A device that is present but disabled or hung can often be revived in place without reinstalling anything. This is the software equivalent of turning it off and on again.

1. Right-click the ELAN or I2C HID device in Device Manager.
2. Choose Disable device, wait five seconds, then choose Enable device.
3. If the driver tab offers Roll Back Driver, use it when the failure followed an update.
4. Restart the laptop after re-enabling.
5. Test cursor movement, tapping, and two-finger scroll.

### Fix 5: Clean-reinstall the ASUS ELAN driver

The definitive software fix. Remove the broken driver completely and install the touchpad driver ASUS published for your exact model, which restores full gesture support.

1. Find your exact ASUS model number on the bottom sticker.
2. In Device Manager, uninstall the ELAN or touchpad device with driver removal checked.
3. Restart the laptop.
4. Download the Touchpad driver from the ASUS support page for your model.
5. Install it, restart again, and verify all gestures work.

### Fix 6: Check the BIOS pointing-device setting

If the touchpad is invisible even in Device Manager, the BIOS may have it disabled. This happens after BIOS resets and on some models after firmware updates.

1. Restart and press F2 or Del to enter the BIOS.
2. Look under Advanced for Internal Pointing Device or Touchpad.
3. Set it to Enabled if it is disabled.
4. Save changes and exit the BIOS.
5. Boot into Windows and check Device Manager for the touchpad.

### Fix 7: Test hardware and check official guidance

When software steps fail, confirm the hardware. A touchpad that works in BIOS but not Windows is software; one dead everywhere after these steps is likely hardware.

1. Enter the BIOS and test whether the cursor moves there.
2. Boot a Linux live USB to test the touchpad outside Windows.
3. If dead everywhere, the ribbon cable or sensor may need service.
4. Review ASUS-specific touchpad articles on the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).
5. Contact ASUS support with your serial number if hardware service is needed.

## Closing

ASUS touchpad failures are almost never mysterious: the hotkey turned it off, Windows disabled it, or the driver needs reinstalling. Run the checks in this order and the touchpad comes back quickly. Keep the ASUS ELAN driver installed and be wary after major Windows updates. For related symptoms, see our guide on [ASUS function key issues](/articles/how-to-fix-function-keys-not-working-on-asus-laptop/).
