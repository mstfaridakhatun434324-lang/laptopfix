---
title: "Touchpad Not Working in Windows 11 24H2? 7 Fixes to Restore It"
slug: how-to-fix-touchpad-not-working-in-windows-11-24h2
date: 2026-09-28
categories: ["drivers"]
tags: ["touchpad not working", "windows 11 24h2", "precision touchpad", "i2c hid"]
description: "Touchpad dead after Windows 11 24H2? Bring it back with these 7 fixes — I2C HID repair, Precision driver reinstall, and 24H2-specific update blocks."
thumbnail: "/images/thumbs/how-to-fix-touchpad-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did the 24H2 update break my touchpad?"
    a: "Windows 11 24H2 has a documented pattern of breaking touchpads: it replaces working I2C HID or manufacturer touchpad drivers with incompatible versions, and in some cases disables the touchpad device entirely. ELAN, Synaptics, and Precision touchpads are all affected on different models. The repair is to uninstall the broken driver with driver deletion, reinstall the manufacturer's version, and block Windows from replacing it again — exactly what the fixes below do."
  - q: "How do I use my laptop with no touchpad and no mouse?"
    a: "Windows 11 is fully keyboard-operable. Press Win + X for the quick menu, use Tab and arrow keys to navigate, Enter to select, and Shift + F10 (or the Menu key) for right-click. Enable Mouse Keys as a pointer substitute: Settings then Accessibility then Mouse, turn on Mouse keys, and drive the pointer with the number pad. An inexpensive USB mouse also works instantly — Windows installs it without needing the touchpad."
  - q: "What is the I2C HID device and why does it matter?"
    a: "I2C HID Device is the bus driver that modern precision touchpads use to communicate with Windows — the touchpad hardware talks I2C, and this driver translates it into pointer input. If the I2C HID device fails (yellow warning in Device Manager under Human Interface Devices), the touchpad above it can't work no matter what touchpad driver is installed. Reinstalling the I2C HID device is often the actual fix when touchpad driver reinstalls fail."
  - q: "Should I roll back Windows 11 24H2 to fix the touchpad?"
    a: "Only as a last resort. The driver-level fixes below resolve 24H2 touchpad failures without the disruption of a full build rollback — and rollback is only available for 10 days after the update anyway. If you're within the window and nothing works, Settings then System then Recovery then Go back is the path. But first try the driver repair and blocking steps; they fix the root cause rather than retreating from the update. The general [touchpad guide](/articles/touchpad-not-working-troubleshooting/) covers non-24H2 causes."
---

The 24H2 update finished, the laptop rebooted, and the touchpad is dead. No cursor movement, no taps, nothing — while an external USB mouse works perfectly. If this timeline matches yours, you're dealing with one of Windows 11 24H2's signature driver breakages, and it's fixable without rolling back the update.

24H2 breaks touchpads in a specific way: it swaps the I2C HID bus driver or the touchpad driver for an incompatible version. The repair targets exactly that. All fixes below are keyboard-navigable — you don't need a mouse.

## Why this happens

- **24H2 replaced the I2C HID driver:** The bus driver the touchpad depends on got swapped for a broken version.
- **Manufacturer touchpad driver overwritten:** ELAN/Synaptics/Precision drivers replaced by incompatible inbox versions.
- **Touchpad device disabled by the update:** Windows disabled the device after a failed start during upgrade.
- **Fn touchpad toggle state lost:** The toggle state desynced during the update.
- **BIOS touchpad setting reset:** Rare, but major updates can coincide with firmware resets.
- **Corrupt driver migration:** The update's driver migration left half-migrated driver state.
- **Conflicting duplicate drivers:** Old and new driver versions both present, fighting over the device.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle the touchpad on (Fn key + Settings)

Rule out the simple state issue first — updates desync the toggle.

1. Press the touchpad toggle: **Fn +** the touchpad-icon function key (varies by brand — F5, F7, or F9 usually).
2. Press **Win + I** for Settings, navigate to **Bluetooth & devices > Touchpad** (Tab/arrows/Enter).
3. Make sure the **Touchpad** toggle is **On**.
4. If a USB mouse is connected, check that Windows isn't auto-disabling the touchpad: disconnect the USB mouse and test, since the "leave touchpad on when a mouse is connected" behavior can desync after the update.

If the Fn key produces no on-screen indicator, the hotkey driver may also be broken — but focus on the touchpad driver first.

### Fix 2: Re-enable the touchpad in Device Manager

24H2 disables devices that fail during the upgrade.

1. Press **Win + X**, then **M** (Device Manager).
2. Navigate with arrow keys to **Human Interface Devices** and expand it (Right arrow).
3. Look for **I2C HID Device** — if greyed out, press the Menu key (**Shift + F10**), choose **Enable device**.
4. Expand **Mice and other pointing devices** and enable any greyed touchpad entries (ELAN, Synaptics, HID-compliant mouse).
5. Test the touchpad.

Enable everything touchpad-related that's disabled — Windows sometimes disables both the bus device and the touchpad itself.

### Fix 3: Reinstall the I2C HID device (the 24H2 signature fix)

This is the repair that specifically addresses 24H2's breakage pattern.

1. In Device Manager, under **Human Interface Devices**, select **I2C HID Device**.
2. Open its context menu (**Shift + F10**) and choose **Uninstall device**. If asked about deleting the driver, tick it.
3. If multiple I2C HID devices exist, uninstall them one at a time — the touchpad's is usually the one with the warning, if any.
4. **Restart** the laptop (**Alt + F4** on desktop, choose Restart).
5. After reboot, Windows redetects the I2C bus and installs a fresh driver — test the touchpad.

This single fix resolves a large share of post-24H2 touchpad deaths because the I2C bus driver is what 24H2 most commonly breaks.

### Fix 4: Install the manufacturer's touchpad driver

Don't trust 24H2's driver choice — install the validated one.

1. On another device (or with a USB mouse), go to your laptop maker's support site.
2. Download the **touchpad / I/O driver** for your exact model — get both the touchpad driver and the **chipset/serial IO driver** (the I2C controller driver).
3. Install the Serial IO/chipset driver first, then the touchpad driver, restarting between.
4. Test the touchpad.

The Serial IO driver is the piece most people miss — the I2C controller itself needs its driver for the bus device to work. For ELAN-specific hardware, the [ELAN guide](/articles/best-way-to-fix-elan-touchpad-not-working/) has revision-matching details.

### Fix 5: Roll back the driver and block 24H2's replacement

If the touchpad worked minutes before 24H2, the old driver was fine.

1. In Device Manager, open the touchpad device's **Properties > Driver** tab and click **Roll Back Driver** if available.
2. Do the same for the **I2C HID Device** if it has a Driver tab with rollback.
3. Go to **Settings > Windows Update** and pause updates.
4. Use the **Show or hide updates** troubleshooter to hide the touchpad/I2C driver updates.
5. Restart and verify the touchpad survives.

Blocking is essential — without it, Windows reinstalls the 24H2 driver and the touchpad dies again overnight.

### Fix 6: Clean out duplicate and ghost touchpad drivers

The update can leave old and new drivers fighting.

1. In Device Manager, enable **View > Show hidden devices**.
2. Under **Mice and other pointing devices** and **Human Interface Devices**, uninstall every greyed-out touchpad, mouse, and I2C entry.
3. In **Settings > Apps**, uninstall duplicate touchpad software (two ELAN versions, for example).
4. Restart and install only the manufacturer's current driver set.

Ghost devices from the pre-24H2 driver stack can intercept the hardware before the new driver loads — clearing them removes the conflict.

### Fix 7: Check BIOS and test hardware independence

Final verification that it's software, not hardware.

1. Restart into BIOS/UEFI — if the touchpad works in a mouse-driven BIOS, the hardware is fine.
2. Check for a **Touchpad** / **Internal Pointing Device** toggle under Advanced/Devices and ensure it's **Enabled**.
3. Check for a BIOS update from the manufacturer — some 24H2-era updates fix I2C initialization.
4. Boot a Linux live USB: working touchpad there definitively proves Windows is the problem.

Touchpad working in BIOS/Linux but dead in Windows after all driver work means a deep Windows issue — a repair install keeps files while rebuilding the driver stack. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the Device Manager steps used throughout this guide. Dead everywhere means hardware: the ribbon cable or the touchpad module itself. The [Precision touchpad reference](/articles/best-way-to-fix-touchpad-not-working/) covers hardware diagnosis further.

## Closing

24H2's touchpad breakage looks catastrophic — a totally dead touchpad — but it's a driver swap, and driver swaps are reversible. The I2C HID reinstall is the signature fix; the manufacturer's driver plus update-blocking is the permanent one. Once the right drivers are pinned, 24H2 runs fine with a working touchpad.
