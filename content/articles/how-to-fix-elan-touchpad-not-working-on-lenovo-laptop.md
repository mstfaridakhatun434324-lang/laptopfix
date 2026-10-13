---
title: "ELAN Touchpad Not Working on a Lenovo Laptop? 7 Fixes That Work"
slug: how-to-fix-elan-touchpad-not-working-on-lenovo-laptop
date: 2026-10-07
categories: ["drivers"]
tags: ["touchpad", "elan", "lenovo", "mouse", "drivers"]
description: "ELAN touchpad dead on your Lenovo laptop after an update? 7 fixes — from function-key toggles to clean ELAN driver reinstalls."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working after a Windows update?"
    a: "Windows Update frequently replaces Lenovo's ELAN touchpad driver with a generic Microsoft precision touchpad driver or a mismatched ELAN version. The new driver either fails to initialize the ELAN hardware or misidentifies it, so the touchpad goes dead. This is a driver mismatch, not hardware damage, and reinstalling Lenovo's ELAN driver for your exact model restores it."
  - q: "How do I know if my Lenovo uses an ELAN or Synaptics touchpad?"
    a: "Open Device Manager and expand 'Human Interface Devices' or 'Mice and other pointing devices' — the touchpad entry will say ELAN or Synaptics in its name. Alternatively, check Settings > Bluetooth & devices > Touchpad; ELAN models often show an ELAN tab or branding. Lenovo's support page for your exact model also lists which touchpad hardware it shipped with."
  - q: "The touchpad works in BIOS but not in Windows. What does that mean?"
    a: "That's excellent diagnostic news — it means the touchpad hardware is fine and the problem is purely the Windows driver. If the cursor moves in the BIOS setup screens but not in Windows, skip the hardware checks and go straight to the driver fixes. A clean reinstall of the ELAN driver almost always resolves this specific symptom."
  - q: "Can I use my Lenovo without the touchpad while I fix it?"
    a: "Yes. Plug in any USB mouse and it will work immediately — Windows treats it as a separate device. You can also enable Mouse Keys (Settings > Accessibility > Mouse) to control the cursor with the number pad in a pinch. These workarounds don't interfere with the driver fixes, so use them freely while you work through the steps."
---

The cursor won't budge. Taps do nothing, two-finger scroll is gone, and the touchpad feels like a dead slab of glass. If your Lenovo uses an ELAN touchpad — and many IdeaPads, ThinkPads, and Legion models do — this failure almost always follows a Windows update that swapped your ELAN driver for something incompatible. The hardware is fine; the software handshake broke.

Before diving into drivers, rule out the embarrassingly simple causes: Lenovo laptops have a function key that disables the touchpad, and Windows has a setting that turns it off when a mouse is connected. The seven fixes below start there and escalate to the clean ELAN driver reinstall that permanently solves most cases. For Synaptics-based Lenovos, our [Synaptics touchpad guide](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/) covers the equivalent steps.

## Why this happens

- **Windows Update replaced the ELAN driver** — a generic precision touchpad driver or wrong ELAN version can't drive the hardware.
- **The touchpad is disabled via function key** — Lenovo's Fn-key toggle turns the touchpad off at firmware level.
- **"Leave touchpad on when a mouse is connected" got flipped** — the update enabled the setting that disables the touchpad with a USB mouse plugged in.
- **The ELAN driver is corrupted** — interrupted updates leave driver files that fail to initialize the device.
- **The touchpad is disabled in BIOS** — some Lenovo BIOS setups have an internal pointing device toggle.
- **Fast Startup cached a dead device state** — the touchpad never reinitializes properly across hybrid shutdowns.
- **A second pointing driver is conflicting** — leftover Synaptics components or a USB mouse driver can fight the ELAN driver.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle the touchpad function key

Lenovo laptops map touchpad on/off to a function key — usually **F6** or **F8**, marked with a touchpad icon. It's remarkably easy to hit accidentally, and Windows updates sometimes leave it in the off state. Press **Fn + the touchpad key** (or just the key if your Fn lock is on) and test immediately. Watch for an on-screen notification confirming the touchpad state changed.

1. Locate the touchpad icon on your function keys (commonly F6 or F8).
2. Press **Fn + that key** and wait a few seconds.
3. Try moving the cursor — test taps and two-finger scroll too.
4. If nothing changes, press the combination once more; some models toggle through states.

### Fix 2: Check the touchpad settings in Windows

Windows has its own touchpad master switch, and updates do flip it. Go to **Settings > Bluetooth & devices > Touchpad** and confirm the touchpad toggle is On. While there, uncheck "Leave touchpad on when a mouse is connected" is actually the opposite of what you want — make sure the touchpad stays enabled regardless. Also verify the cursor speed isn't set to zero, which mimics a dead touchpad.

1. Open **Settings > Bluetooth & devices > Touchpad**.
2. Make sure the main **Touchpad** toggle is set to **On**.
3. Unplug any USB mouse temporarily — retest with it disconnected.
4. Reset touchpad settings to defaults using the **Reset** button if one is present.

### Fix 3: Enable the ELAN device in Device Manager

The ELAN touchpad may be present in Device Manager but disabled — showing a small down-arrow icon. Expand both **Human Interface Devices** and **Mice and other pointing devices** and look for anything with ELAN in the name. If it's disabled, enabling it brings the touchpad straight back. This takes thirty seconds and catches the cases where an update disabled the device rather than replacing its driver.

1. Open **Device Manager** and check **Human Interface Devices** for an ELAN entry.
2. If you see a down-arrow icon on it, right-click and choose **Enable device**.
3. Also check **Mice and other pointing devices** for a disabled ELAN or PS/2 mouse entry.
4. Test the touchpad immediately after enabling.

### Fix 4: Do a full shutdown to reset the device state

Fast Startup's hybrid shutdown can leave the ELAN controller in a wedged state that survives normal restarts. A full shutdown forces the embedded controller to reinitialize the touchpad hardware from scratch on the next boot. This is particularly effective when the touchpad died suddenly without any update — a sign of a stuck hardware state rather than a driver problem.

1. Hold **Shift** while clicking **Start > Power > Shut down** for a full shutdown.
2. Unplug the AC adapter and wait 60 seconds.
3. Press and hold the power button for 30 seconds to drain residual power.
4. Reconnect, boot up, and test the touchpad before opening any programs.

### Fix 5: Clean-reinstall the ELAN driver from Lenovo

This is the definitive fix for update-caused failures. Download the touchpad driver for your exact model from [Lenovo's support site](https://support.lenovo.com/us/en/) — make sure it's the ELAN version, not Synaptics. Uninstall the current driver with the "delete driver software" option so Windows can't reinstall the same broken one, then install Lenovo's package fresh. Our [ELAN on Windows 11 24H2 guide](/articles/how-to-fix-elan-touchpad-not-working-in-windows-11-24h2/) has model-specific notes if you get stuck.

1. Download the ELAN touchpad driver for your exact Lenovo model from Lenovo support.
2. In **Device Manager**, right-click the ELAN device and choose **Uninstall device**.
3. Check **Attempt to remove the driver for this device** and confirm.
4. Restart, run the Lenovo ELAN installer, restart again, and test thoroughly.

### Fix 6: Check the BIOS internal pointing device setting

Some Lenovo BIOS setups include a toggle for the internal pointing device. If it's off, no Windows driver will ever bring the touchpad back. Restart, press **F2** (or **Fn + F2**) at the Lenovo logo to enter BIOS setup, and look under the **Config** or **Devices** tab for "Internal Pointing Device" or "TrackPad." Enable it, save with **F10**, and boot into Windows.

1. Restart and press **F2** at the Lenovo logo to enter BIOS setup.
2. Navigate to the **Config** or **Devices** tab.
3. Find **Internal Pointing Device** (or TrackPad) and set it to **Enabled**.
4. Press **F10** to save and exit, then test the touchpad in Windows.

### Fix 7: Block Windows Update from replacing the driver again

A clean reinstall is temporary if Windows Update overwrites the ELAN driver again next month. After confirming the touchpad works, use Microsoft's "Show or hide updates" troubleshooter to hide the touchpad driver update. Microsoft documents update management at [Windows support](https://support.microsoft.com/en-us/windows) — the troubleshooter remains the most reliable way to block a specific driver.

1. Download Microsoft's **Show or hide updates** troubleshooter.
2. Run it, choose **Hide updates**, and select the ELAN/touchpad driver update.
3. Confirm the update is hidden so it won't reinstall on the next Patch Tuesday.
4. Keep the Lenovo ELAN installer saved on your drive for quick recovery.

## Closing

A dead ELAN touchpad on a Lenovo is a driver mismatch wearing a hardware costume — the quickest proof is that it usually works in BIOS. The function-key toggle and Windows settings catch the simple cases; the clean reinstall of Lenovo's ELAN driver plus blocking the bad update ends the cycle permanently. Your touchpad isn't broken — Windows just forgot how to talk to it.
