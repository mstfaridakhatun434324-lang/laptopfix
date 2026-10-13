---
title: "Touchpad Not Working on Windows 10? Fix It Step by Step"
slug: how-to-fix-touchpad-not-working-on-windows-10
date: 2026-09-07
categories: ["drivers"]
tags: ["touchpad", "windows 10", "cursor", "driver"]
description: "Touchpad dead on Windows 10? Step-by-step fixes from the toggle key to the driver stack, in the order that works."
thumbnail: "/images/thumbs/how-to-fix-touchpad-not-working-on-windows-10.webp"
faqs:
  - q: "Why did my touchpad stop working after a Windows 10 update?"
    a: "Windows 10 updates regularly replace the manufacturer's touchpad driver with a generic one, or flip the touchpad's enabled state. The update process can also reset the 'leave touchpad on when mouse is connected' behavior. Reinstalling the OEM touchpad driver and re-checking the Settings toggles resolves the large majority of post-update touchpad deaths."
  - q: "My touchpad toggle key doesn't do anything. Is the touchpad broken?"
    a: "Not necessarily — the Fn-key toggle depends on the manufacturer's hotkey software, which may itself be broken or uninstalled. Use Settings > Devices > Touchpad to toggle it in software instead. If the software toggle works but the key doesn't, reinstall the hotkey utility from the laptop maker; the touchpad hardware is fine."
  - q: "Should I update to the latest touchpad driver or roll back?"
    a: "Roll back first if the touchpad worked recently — the newest driver isn't always the best one for older hardware. Only seek a newer driver from the laptop manufacturer's site if the current one is corrupted or missing. Avoid generic driver-updater tools; they frequently install the wrong touchpad stack and make things worse."
  - q: "Touchpad works for moving but not for scrolling or gestures. What's wrong?"
    a: "The basic cursor driver is loaded but the advanced gesture stack isn't — usually because a generic driver replaced the manufacturer's full package. Installing the OEM touchpad driver restores two-finger scroll, pinch zoom, and multi-finger gestures. Also check that gestures are enabled under Settings > Devices > Touchpad, since updates sometimes reset them."
---

Windows 10 and touchpads have a long, troubled history together. The OS means well — it tries to keep drivers current — but its updates have a habit of swapping your laptop's carefully tuned touchpad driver for a generic one, flipping the touchpad off in Settings, or breaking the hotkey software that drives the Fn toggle. The result is always the same: a cursor that won't move on a machine that's otherwise fine.

The fix sequence below is ordered by how often each step works, not by how technical it is. It starts with the two-minute checks (the toggle key, the Settings switch, the mouse-connected behavior) because those embarrassingly account for a large share of "dead" touchpads, then moves into the driver stack where the real update damage lives, and ends with the hardware verdict.

Windows 11 users should follow our [Windows 11 touchpad fix](/articles/how-to-fix-touchpad-not-working-on-windows-11/) instead — the Settings paths differ. For the Synaptics-specific deep dive, there's the [Synaptics troubleshooting walkthrough](/articles/synaptics-touchpad-not-working-troubleshooting/).

## Why this happens

- **A Windows 10 update replaced the touchpad driver.** The classic: the manufacturer's driver gets swapped for a generic Microsoft one that moves the cursor — or doesn't — while gestures and settings vanish.
- **The touchpad got toggled off.** The Fn-key toggle is easy to hit accidentally, and updates sometimes flip the software switch in Settings without asking.
- **"Leave touchpad on when a mouse is connected" is off.** With a wireless mouse receiver plugged in, Windows helpfully disables the touchpad — and people forget the receiver is there.
- **The hotkey/function-key software broke.** The Fn toggle depends on the OEM's hotkey utility; if that utility is broken or missing, the key does nothing and the touchpad can get stuck off.
- **The driver installation corrupted.** Half-applied updates leave the touchpad device present but non-functional — Device Manager looks happy, the cursor doesn't move.
- **Power management suspended the touchpad bus.** On some models the touchpad shares an internal bus that Windows powers down aggressively, killing it after sleep.
- **BIOS disabled the pointing device.** Some BIOSes have an internal-pointing-device toggle; firmware updates can flip it, making the touchpad invisible to Windows entirely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Try the toggle key and the Settings switch

Two minutes, highest embarrassment-to-success ratio in all of troubleshooting.

1. Press your touchpad toggle — usually **Fn + F5**, **F7**, or **F9** (look for the touchpad icon). Wait a few seconds and test. Try it twice — the on/off state isn't always obvious.
2. Go to **Settings > Devices > Touchpad** and make sure the **Touchpad** toggle is **On**.
3. On the same page, check **Leave touchpad on when a mouse is connected** — if you use a wireless mouse (even occasionally), leave this checked while troubleshooting.
4. Adjust **Touchpad sensitivity** to *Medium* or higher — at *Low sensitivity*, light touches genuinely don't register, which feels like a dead pad.

### Fix 2: Unplug the mouse and check for interference

Isolate the touchpad from competing input devices.

1. Unplug any USB mouse or wireless receiver, and turn off Bluetooth mice temporarily.
2. Test the touchpad with no other pointing device active. If it springs to life, the "disable when mouse connected" logic (or a faulty mouse sending phantom input) was the culprit.
3. If you need the mouse connected, keep **Leave touchpad on when a mouse is connected** checked permanently.
4. Also disconnect USB docks and hubs for the test — a malfunctioning hub can flood the input subsystem and freeze the cursor.

### Fix 3: Reinstall the manufacturer's touchpad driver

The anchor fix for update-broken touchpads.

1. Open **Device Manager** (**Win + X** > Device Manager) and expand **Mice and other pointing devices** and **Human Interface Devices** — note the touchpad's current name and driver version.
2. Download the **touchpad driver** for your exact model from the laptop maker's support site. Dell, HP, and Lenovo each publish model-specific packages — don't use a generic download.
3. Right-click the touchpad device > **Uninstall device**, checking *Attempt to remove the driver for this device* to clear the wrong driver fully.
4. Run the manufacturer's installer as administrator and reboot. Verify gestures (two-finger scroll, pinch) work — their return confirms the correct stack is in place.

### Fix 4: Roll back the driver Windows Update installed

Faster than a reinstall when the old driver is still on disk.

1. In **Device Manager**, right-click the touchpad > **Properties** > **Driver** tab.
2. If **Roll Back Driver** is clickable, use it — select *A previous version of the driver worked better*.
3. Reboot and test. If the touchpad works, stop Windows from "fixing" it again: prefer the OEM's update utility over Windows Update for drivers. Microsoft documents the input-device repair path on the [official Windows support site](https://support.microsoft.com/en-us/windows).
4. If Roll Back is grayed out, the old driver is gone — proceed with the full reinstall in Fix 3.

### Fix 5: Repair the function-key/hotkey software

When the toggle key does nothing, the key's software — not the touchpad — is broken.

1. Check **Settings > Apps** for your manufacturer's hotkey utility (e.g., Dell's QuickSet, Lenovo's Hotkeys, HP's Hotkey Support) — if it's missing, that's the problem.
2. Download and reinstall the **hotkey/function-key utility** from the maker's support site, then reboot.
3. Test the Fn touchpad toggle again. Even if you prefer the Settings toggle, a working hotkey utility prevents the touchpad from getting stuck off.
4. While you're there, check the maker's site for a **BIOS update** only if the release notes mention touchpad or input fixes — don't flash BIOS speculatively.

### Fix 6: Check BIOS and power settings

Look below the OS when the device is missing or dies after sleep.

1. Enter **BIOS/UEFI** and find the internal pointing device entry — ensure it's **Enabled**.
2. In **Device Manager**, expand **System devices** and check **Intel Serial IO** / SMBus controllers for warnings — the touchpad depends on these buses. Reinstall chipset drivers from the manufacturer if needed.
3. Do a **full shutdown** (hold **Shift** while clicking Shut down) to clear Fast Startup's preserved driver state, then power on fresh.
4. For sleep-related deaths: in Device Manager, find the touchpad's parent bus device and disable *Allow the computer to turn off this device to save power* on the **Power Management** tab.

### Fix 7: Confirm hardware with an external test

The final verdict, proven rather than assumed.

1. Boot a **Linux live USB** — if the touchpad works there, the hardware is definitively fine; the problem is 100% Windows software, and a clean driver-stack rebuild (Fix 3, possibly with a driver-store cleanup) will fix it.
2. If it's dead in Linux and in BIOS, suspect the touchpad ribbon cable or the module itself — especially after a drop or palm-rest service.
3. Check **Device Manager > View > Show hidden devices** for the touchpad appearing grayed out — that indicates Windows saw it once and lost it, which leans hardware/connection rather than driver.
4. Interim usability: enable **Mouse Keys** (**Settings > Ease of Access > Mouse**) to drive the cursor from the keyboard, or use a USB mouse while arranging repair.

## Closing

Windows 10 touchpad failures are overwhelmingly a software story: the toggle nobody meant to press, the update that swapped the driver, the hotkey utility that quietly broke. Work the two-minute checks first, reinstall the manufacturer's driver as the anchor fix, and keep Windows Update from re-breaking it. The cursor comes back — it almost always does.
