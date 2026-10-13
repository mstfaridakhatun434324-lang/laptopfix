---
title: "How to Fix an Elan Touchpad Not Working on an HP Laptop"
slug: how-to-fix-elan-touchpad-not-working-on-hp-laptop
date: 2026-09-11
categories: ["drivers"]
tags: ["elan touchpad", "hp laptop", "touchpad not working", "windows drivers"]
description: "Fix an Elan touchpad not working on an HP laptop: re-enable the touchpad, repair the Elan driver, and stop Windows from disabling it after updates."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why did my HP touchpad stop working after a Windows update?"
    a: "Windows updates sometimes replace the vendor Elan driver with a generic Microsoft one or reset touchpad settings during the upgrade. The generic driver may fail to initialize the Elan hardware, leaving the cursor frozen. Reinstalling the HP-specific Elan driver and re-enabling the device in Settings usually restores it."
  - q: "How do I know if my HP laptop uses an Elan or Synaptics touchpad?"
    a: "Open Device Manager, expand Human Interface Devices or Mice and other pointing devices, and look for ELAN or Synaptics in the device name. Alternatively, check Settings, Bluetooth and devices, Touchpad, where many HP models show the touchpad type. This matters because each vendor needs its own driver package."
  - q: "The touchpad works in BIOS but not in Windows. What does that mean?"
    a: "That is a software problem, not dead hardware. If the cursor moves in the BIOS setup screen, the touchpad and its ribbon connection are fine. The fault lies with the Windows driver, a disabled setting, or a conflicting update. Focus on driver repair and Windows settings rather than hardware replacement."
  - q: "Should I use the HP driver or the generic Windows driver for my touchpad?"
    a: "Use the HP driver. HP customizes power and gesture behavior for its hardware, and the generic Microsoft PS/2 driver often lacks multi-touch support or fails to wake the Elan chip properly. Download the Elan driver from your model's support page for the most reliable result."
---

An Elan touchpad that suddenly stops working on an HP laptop is one of those failures that feels catastrophic — no cursor, no clicks, and no obvious reason. The good news is that this is almost always a software problem. The touchpad hardware rarely dies; what usually breaks is the driver, a setting Windows flipped during an update, or a power-management rule that puts the Elan chip to sleep and never wakes it.

HP ships a huge range of laptops with Elan touchpads, from budget Pavilion models to Envy and EliteBook machines, and the troubleshooting path is consistent across them. Work through this guide methodically, starting with the two-minute checks that solve most cases, and only move to driver surgery if the simple steps fail. You will not need to open the laptop for anything here.

## Why this happens

- **Disabled in Settings:** Windows lets the touchpad be toggled off entirely, and a shortcut key or an update can flip it without warning.
- **Wrong or corrupted driver:** A Windows update may install a generic driver over HP's Elan package, or the driver files may corrupt after a failed update.
- **Device disabled in Device Manager:** The Elan input device can be disabled at the driver level, which a Settings toggle will not undo.
- **Function-key disable:** Many HP laptops have a dedicated touchpad toggle (often Fn + a key, or a double-tap corner on the pad itself) that gets pressed accidentally.
- **USB power management conflict:** Aggressive power saving can suspend the touchpad's internal USB interface, and it fails to resume.
- **Conflicting external mouse software:** Some mouse utilities register a "disable touchpad when mouse is attached" rule that sticks even after the mouse is unplugged.
- **BIOS-level disable:** On business-class HP models, the touchpad can be turned off in BIOS, which overrides every Windows setting.
- **Stuck driver state after sleep:** A known Elan quirk — resuming from sleep sometimes leaves the driver in a hung state until it is restarted.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the touchpad toggle and Settings

1. Press the touchpad toggle key on your keyboard — on most HP laptops it is a function key with a touchpad icon, or double-tap the small lighted dot in the top-left corner of the pad.
2. Open **Settings → Bluetooth & devices → Touchpad** and confirm the Touchpad switch is **On**.
3. On that same page, uncheck **"Leave touchpad on when a mouse is connected"** issues — actually, toggle it the other way: if a mouse is plugged in, turn this setting **On** so the pad stays active.
4. Test the cursor. If it moves now, the fix was a toggle — the most common cause by far.

### Fix 2: Re-enable the device in Device Manager

1. Press **Win + X** and choose **Device Manager**.
2. Expand **Human Interface Devices** and look for **ELAN Input Device** (it may also appear under **Mice and other pointing devices** as **ELAN PS/2 Port Smart-Pad**).
3. If you see a small down-arrow on the icon, right-click it and choose **Enable device**.
4. If there is no down-arrow, right-click and choose **Disable device**, wait ten seconds, then right-click and choose **Enable device** again. This restarts the driver cleanly.

### Fix 3: Roll back or reinstall the Elan driver

1. In Device Manager, right-click the Elan device and choose **Properties → Driver**.
2. If **Roll Back Driver** is clickable, use it — this undoes a bad driver update. Restart and test.
3. If rollback is unavailable, choose **Uninstall device**, check **"Attempt to remove the driver for this device"** if offered, then restart.
4. Windows will reinstall a driver on boot. If the touchpad works but gestures are missing, the generic driver loaded — continue to the next fix for the proper HP driver.

### Fix 4: Install the official HP Elan driver

1. Go to [HP's support site](https://support.hp.com/us-en), enter your exact model number, and open the driver list for your Windows version.
2. Download the **Elan Touchpad driver** (sometimes listed under Driver-Keyboard, Mouse and Input Devices).
3. Run the installer as administrator and restart when prompted.
4. Verify in Device Manager that the driver provider now reads **ELAN Microelectronics**, not Microsoft. For background on why vendor drivers matter, see how [driver updates can fail in Windows Update](/articles/how-to-fix-driver-updates-keep-failing-windows-update-on-windows-10/) — the same mismatch causes many touchpad failures.

### Fix 5: Stop Windows from replacing the driver

1. Open **Settings → System → About → Advanced system settings → Hardware → Device Installation Settings**.
2. Choose **No** for automatic driver downloads. This prevents Windows Update from swapping your working Elan driver for a generic one again.
3. Alternatively, after a working driver is installed, use the **Show or hide updates** troubleshooter from [Microsoft support](https://support.microsoft.com/en-us/windows) to block the specific bad driver update.

### Fix 6: Disable USB power management for the touchpad

1. In Device Manager, expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub**, right-click → **Properties → Power Management**, and uncheck **"Allow the computer to turn off this device to save power"**.
3. Do the same for the Elan device itself if it shows a Power Management tab.
4. Restart. This fixes touchpads that die after the laptop sleeps or idles, a classic Elan power-state bug similar to [driver power state failures](/articles/driver-power-state-failure-bsod-windows-11/) seen elsewhere.

### Fix 7: Check for the touchpad in BIOS

1. Restart and press **F10** repeatedly to enter BIOS setup on your HP laptop.
2. Navigate to **Advanced → Device Options** (wording varies by model) and look for an **Internal Pointing Device** or **Touchpad** entry.
3. Make sure it is **Enabled**, then save and exit.
4. If the touchpad works in BIOS but not Windows, that confirms a Windows-side problem — return to the driver fixes above rather than suspecting hardware.

### Fix 8: Run a final conflict check

1. Disconnect all USB mice, receivers, and docks, then restart.
2. Boot into **Safe Mode** (Settings → Recovery → Advanced startup) and test the touchpad there. If it works in Safe Mode, a third-party program — often mouse or security software — is interfering.
3. Use a clean boot (msconfig, disable all non-Microsoft services) to isolate the culprit, then remove or update it.

## Closing

An Elan touchpad failure on an HP laptop is frustrating but rarely terminal: a flipped toggle, a disabled device, or a driver Windows replaced without asking accounts for the overwhelming majority of cases. The driver you want is the one HP built for your exact model, and once it is installed and protected from automatic replacement, the problem usually stays fixed for good.
