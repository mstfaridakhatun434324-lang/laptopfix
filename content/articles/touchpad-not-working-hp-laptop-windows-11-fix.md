---
title: "Touchpad Not Working on an HP Laptop (Windows 11): 7 Fixes"
slug: touchpad-not-working-hp-laptop-windows-11-fix
date: 2026-10-05
categories: ["drivers"]
tags: ["touchpad", "hp laptop", "drivers", "windows 11"]
description: "HP laptop touchpad not working on Windows 11? Try these 7 fixes — function-key toggle, driver reinstall, and BIOS checks — to get it moving again."
thumbnail: "/images/thumbs/touchpad-not-working-hp-laptop-windows-11-fix.webp"
faqs:
  - q: "Why did my HP laptop touchpad suddenly stop working?"
    a: "The most common causes are accidentally pressing the touchpad toggle key, the touchpad being disabled in Windows settings, or a driver problem after a Windows or BIOS update. HP laptops use both Synaptics and ELAN touchpads, and either driver's installation can be corrupted. Hardware failure is possible but much less common than these software causes."
  - q: "How do I enable the touchpad on an HP laptop?"
    a: "Press the touchpad toggle key (usually Fn plus a function key with a touchpad icon) and check Settings > Bluetooth & devices > Touchpad to make sure the switch is on. Also check the BIOS under Advanced > Built-In Device Options, where the touchpad can be disabled at the hardware level. Re-enable it in all three places if needed."
  - q: "Should I use HP Support Assistant to update the touchpad driver?"
    a: "Yes. HP Support Assistant pulls drivers validated for your exact model, which are more reliable than the generic versions Windows Update installs. Open HP Support Assistant, check for updates, and install any listed touchpad or chipset drivers. Restart the laptop afterward so the new driver loads."
  - q: "What if the touchpad works in BIOS but not in Windows?"
    a: "That points squarely at a Windows driver or settings problem, not hardware failure. Reinstall the HID-compliant touchpad driver in Device Manager and check for a conflicting mouse or USB input device. If the cursor still will not move, try a different driver version from HP's support site for your exact model."
---

You are typing on your HP laptop and the cursor will not move. The touchpad feels dead — no taps, no two-finger scroll, no clicks — even though the keyboard works fine. On HP laptops this is a frequent complaint after Windows 11 updates, but it also happens out of the blue on perfectly healthy machines.

Before assuming the hardware is broken, know that most touchpad failures on HP laptops are software problems: a disabled setting, a toggle key pressed by accident, or a driver that needs a fresh install. The seven fixes below start with the simplest checks and end with the deeper diagnostics.

## Why this happens

- **The touchpad toggle key was pressed accidentally** — most HP laptops have an Fn shortcut that disables the touchpad with one keystroke.
- **The touchpad is disabled in Windows Settings** — updates or cleanup tools can flip the Touchpad switch off.
- **The touchpad driver is corrupted or outdated** — a bad driver install leaves the device present but non-responsive.
- **The touchpad is disabled in BIOS** — HP's Built-In Device Options can turn it off at the hardware level, where Windows cannot override it.
- **A conflicting input device or service** — external mice, docking stations, or stuck input services can suppress the touchpad.

## How to fix it

Work through these in order — the first two fixes take seconds and resolve most cases.

### Fix 1: Press the touchpad toggle key

HP laptops include a function key that enables or disables the touchpad. It is easy to hit by accident, so this is always worth checking first.

1. Look at the top row of your keyboard for a key with a touchpad icon (often F5, F11, or F12 on HP models).
2. Hold **Fn** and press that key (some HP models toggle with the key alone).
3. Test the touchpad. A small indicator light near the touchpad may change state when it is enabled.

### Fix 2: Enable the touchpad in Windows Settings

Windows 11 keeps its own touchpad switch, independent of the function key. Make sure it is on and configured.

1. Open **Settings > Bluetooth & devices > Touchpad**.
2. Make sure the **Touchpad** toggle is set to **On**.
3. Expand the settings below to confirm gestures and taps are enabled, then test the cursor again.

### Fix 3: Reinstall the HID-compliant touchpad driver

A fresh driver install clears corrupted files that keep the touchpad from responding. Device Manager handles this in a few clicks.

1. Right-click **Start** and choose **Device Manager**.
2. Expand **Human Interface Devices** (or **Mice and other pointing devices**) and find **HID-compliant touch pad** — HP models may also show a "Synaptics" or "ELAN" touchpad entry.
3. Right-click it, choose **Uninstall device**, and confirm.
4. Restart the laptop — Windows reinstalls the driver automatically on boot.

### Fix 4: Update the driver with HP Support Assistant

HP validates drivers for your exact model, so their version is more reliable than the generic one Windows installs on its own.

1. Open **HP Support Assistant** from the Start menu (install it from the Microsoft Store if it is missing).
2. Click **Check for updates** and let it scan.
3. Install any touchpad, chipset, or input driver updates it lists, then restart the laptop.

You can also download drivers manually from [HP's official support site](https://support.hp.com/us-en) by entering your model number.

### Fix 5: Check the touchpad in BIOS

If a BIOS update or settings change disabled the touchpad at the hardware level, no Windows fix will help — you must re-enable it before Windows boots.

1. Restart the laptop and press **Esc** repeatedly, then **F10** to enter BIOS setup.
2. Navigate to **Advanced > Built-In Device Options**.
3. Make sure **Touchpad** (or "Internal Pointing Device") is enabled.
4. Save and exit, then let Windows start and test the touchpad.

### Fix 6: Test with an external mouse and disconnect extras

Plugging in a USB mouse tells you whether Windows is registering input devices at all, and removing docks and hubs rules out conflicts.

1. Connect a USB or Bluetooth mouse and confirm the cursor moves with it.
2. Unplug USB hubs, docking stations, and any extra input devices.
3. Restart the laptop with only the mouse connected, then unplug the mouse and test the touchpad alone.

### Fix 7: Run Windows Update and update chipset drivers

Missing chipset or input drivers can keep the touchpad driver from loading. A final update pass catches stragglers. Driver problems after updates affect more than touchpads — if your Wi-Fi also broke after a Windows 11 update, our [Wi-Fi fix guide](/articles/wifi-not-working-after-windows-11-update-fix/) walks through that repair.

1. Open **Settings > Windows Update** and click **Check for updates**.
2. Install all updates, then click **Advanced options > Optional updates** and install any driver updates listed.
3. Restart the laptop and test. If the update process itself stalls, see our guide on [Windows Update stuck at 100%](/articles/windows-update-stuck-at-100-percent-fix/).

Nine times out of ten, an HP touchpad that stops working is a settings or driver problem, not dead hardware — Fix 1 through Fix 3 alone revive most of them. If the touchpad works in BIOS but refuses to move in Windows, stay focused on drivers; if nothing responds even in BIOS, it is time to contact HP support. And remember that updates can knock out several devices at once, so check our [Wi-Fi repair guide](/articles/wifi-not-working-after-windows-11-update-fix/) if your wireless dropped at the same time. As a temporary workaround while you troubleshoot, a basic USB mouse keeps you productive, and HP's built-in hardware diagnostics (press Esc during startup, then F2) can confirm whether the touchpad itself is healthy. If diagnostics pass but Windows still ignores the touchpad after every fix above, a clean reinstall of the chipset and serial I/O drivers from HP's support site is the deepest software reset available short of a Windows refresh. Give each driver change a full restart before judging the result, since input drivers only reload at boot.
