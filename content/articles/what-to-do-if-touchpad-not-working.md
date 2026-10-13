---
title: "Touchpad Not Working? What to Do First on Your Laptop"
slug: what-to-do-if-touchpad-not-working
date: 2026-09-12
categories: ["drivers"]
tags: ["touchpad", "trackpad", "synaptics", "precision touchpad"]
description: "Touchpad dead on your Windows laptop? Start with these first-response steps — function-key toggles, settings, and driver checks — before deeper diagnosis."
thumbnail: "/images/thumbs/what-to-do-if-touchpad-not-working.webp"
faqs:
  - q: "Why did my touchpad suddenly stop working?"
    a: "The most common sudden cause is accidentally pressing the touchpad toggle key (usually Fn + F7/F9 or similar), which disables the touchpad instantly with no on-screen warning. Next most common: a Windows Update replaced your touchpad driver, or a palm-rejection/sensitivity setting got reset. Hardware failure is actually the least likely cause of a sudden stoppage."
  - q: "How do I turn my touchpad back on with the keyboard?"
    a: "First try the function-key combo — look for a touchpad icon on your F-keys and press it, with Fn if required. Then press Win + I to open Settings, navigate to Bluetooth & devices > Touchpad with Tab and arrows, and make sure the Touchpad toggle is On. If the Touchpad page is missing entirely from Settings, Windows isn't detecting the device at all, which points to a driver or BIOS-level problem."
  - q: "Can a Windows update disable my touchpad?"
    a: "Yes — Windows Update frequently replaces manufacturer touchpad drivers (Synaptics, ELAN) with generic versions that either malfunction or lose the Settings page integration. If your touchpad died right after an update, roll the driver back in Device Manager or reinstall the touchpad driver from your laptop maker's support page, which is the version actually validated for your model."
  - q: "Touchpad works in BIOS but not in Windows — what does that mean?"
    a: "That's actually good news: it proves the hardware is fine and the problem is purely software. A touchpad that moves the cursor in BIOS/UEFI setup but not in Windows means the Windows driver is missing, corrupt, or disabled. Focus entirely on Device Manager — reinstall or roll back the touchpad driver — and skip any hardware troubleshooting."
---

A dead touchpad turns a laptop into a desktop with commitment issues — you're suddenly hunting for a mouse just to click anything. Before you assume hardware failure, know this: the overwhelming majority of touchpad stoppages are software, and most are fixed in under five minutes. The classic culprits are the accidental function-key toggle, a driver swapped by Windows Update, or the touchpad simply switched off in Settings.

Your first-response order: check the toggle key, check Settings, check Device Manager, then test in BIOS to separate hardware from software. For the deeper driver-level diagnosis — dump analysis of the touchpad stack, precision driver conversion — see our [touchpad troubleshooting guide](/articles/troubleshoot-touchpad-not-working/). For Synaptics-specific breakage after updates, there's also [fixing the Synaptics touchpad](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/).

## Why this happens

- **Accidental function-key toggle**: Most laptops have a touchpad on/off key (Fn + F5/F7/F9) that's trivially easy to hit while typing.
- **Windows Update replaced the driver**: Generic Microsoft drivers often replace Synaptics/ELAN drivers and break gestures or the whole pad.
- **Touchpad disabled in Settings**: The Settings toggle can be flipped by updates, manufacturer utilities, or an external mouse's "disable when mouse present" option.
- **Driver corruption**: A partial update or interrupted install leaves the touchpad driver in a half-working state.
- **Touchpad disabled in BIOS/UEFI**: Some BIOS setups have an "Internal Pointing Device" option that can be off — common after BIOS updates reset settings.
- **External mouse auto-disable**: Manufacturer utilities (and Windows itself) can disable the touchpad whenever a USB/Bluetooth mouse is connected.
- **Hardware failure**: Loose ribbon cable or a dead pad — genuinely rare for sudden failures, more plausible after drops or liquid exposure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Press the touchpad toggle key

The five-second fix that solves an embarrassing number of cases.

1. Look at your function keys (F1–F12) for a touchpad icon — a rectangle with a finger, or a rectangle with a line through it.
2. Press that key. On most laptops you must hold **Fn** at the same time; on some, the F-keys default to media/function mode — try it both with and without Fn.
3. Watch for an on-screen indicator showing the touchpad enabled/disabled state.
4. Test the touchpad immediately after each press. If it springs to life, you found it — consider disabling the hotkey in your manufacturer's utility if you keep hitting it accidentally.
5. No touchpad icon on any F-key? Check your manual — some laptops bury the toggle in a manufacturer app instead.

### Fix 2: Re-enable the touchpad in Settings

Keyboard-only navigation to the rescue.

1. Press **Win + I** to open Settings.
2. Use **Tab** and arrow keys to navigate to **Bluetooth & devices** > **Touchpad** (or type "touchpad" in the Settings search box and press Enter).
3. Make sure the main **Touchpad** toggle is **On**.
4. If the entire Touchpad page is missing, Windows isn't detecting a precision touchpad at all — skip to Fix 4 (driver/BIOS territory).
5. While here, check **"Leave touchpad on when a mouse is connected"** is checked if you use an external mouse — the auto-disable feature is a silent culprit.

### Fix 3: Adjust cursor speed and sensitivity

Sometimes the pad "works" but is unusable — pointer barely moves or jumps.

1. In **Settings** > **Bluetooth & devices** > **Touchpad**, drag **Cursor speed** to the middle or higher.
2. Under **Taps** and **Scroll and zoom**, re-enable the gestures you use — updates sometimes reset these.
3. Expand **Touchpad sensitivity** (under **More touchpad settings** or similar) and set it to **Medium** or **High sensitivity** — low sensitivity with palm rejection can make the pad feel dead.
4. If you wear gloves or have dry skin, higher sensitivity genuinely helps capacitive pads register.
5. Test two-finger scroll and tap-to-click specifically — individual gestures can break while basic movement works.

### Fix 4: Check Device Manager for the touchpad device

Find out whether Windows sees the hardware.

1. Press **Win + X** > **Device Manager** and expand **Human Interface Devices** and **Mice and other pointing devices**.
2. Look for entries like "Synaptics TouchPad," "ELAN Input Device," or "HID-compliant touch pad." A yellow warning icon means driver trouble — right-click > **Update driver** or **Uninstall device**, then restart.
3. If the touchpad entry is missing entirely, click **View** > **Show hidden devices** — a greyed-out entry means it's disabled; right-click > **Enable device**.
4. Still nothing? The device may be disabled at BIOS level (Fix 5) or the driver stack is badly corrupted (Fix 6).
5. If you recently updated Windows, try **Roll Back Driver** on the touchpad device first — this is the fastest fix for update-caused deaths.

### Fix 5: Enable the touchpad in BIOS/UEFI

When Windows can't see the device at all.

1. Restart and press your BIOS key during boot (**F2**, **Del**, or **F10** — varies by maker; Lenovo often uses **F1** or the Novo button).
2. Navigate with the keyboard to the **Advanced** or **Devices** tab and look for **Internal Pointing Device** or **Touchpad**.
3. Make sure it's set to **Enabled**, save (**F10**), and exit.
4. Boot into Windows and recheck Device Manager — the device should now appear.
5. If the BIOS has no such option, that's fine — it means the pad is always enabled at firmware level, and the problem is Windows-side.

### Fix 6: Reinstall the manufacturer's touchpad driver

The definitive software fix when the driver is the problem.

1. Identify your touchpad brand from Device Manager (Synaptics, ELAN, or Microsoft precision).
2. Download the touchpad driver from your manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — matched to your exact model.
3. In Device Manager, right-click the touchpad > **Uninstall device**, checking **Attempt to remove the driver** if offered.
4. Restart, then install the downloaded manufacturer driver and restart again.
5. Verify in Settings that the Touchpad page is back with full gesture options — manufacturer drivers restore features generic ones drop.

### Fix 7: Test in BIOS and consider hardware

The final separation of software from hardware.

1. Reboot into BIOS/UEFI setup — most BIOS screens respond to the touchpad for navigation.
2. If the touchpad moves the cursor in BIOS but not in Windows, the hardware is 100% fine — repeat Fix 6 with a different driver version, or try an older driver from the manufacturer's archive.
3. If the touchpad is dead in BIOS too, you're looking at hardware: a disconnected ribbon cable (common after drops or bottom-panel removals) or a failed pad.
4. For cable issues, reseating requires opening the laptop — only attempt if you're comfortable; otherwise it's a repair-shop job, usually inexpensive.
5. As a workaround either way, any USB or Bluetooth mouse restores full usability immediately.

## Closing

Touchpad failures are almost never the emergency they feel like: check the toggle key, check Settings, check the driver — in that order — and you'll resolve the vast majority without opening the laptop or spending a cent. The BIOS test is your ground truth; everything before it is just ruling out the easy stuff.
