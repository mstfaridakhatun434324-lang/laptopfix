---
title: "Touchpad Not Working? A Step-by-Step Fix Guide"
slug: how-to-fix-touchpad-not-working-step-by-step
date: 2026-09-10
categories: ["drivers"]
tags: ["touchpad not working", "laptop touchpad", "touchpad driver", "precision touchpad"]
description: "Touchpad completely dead? Follow this step-by-step guide to diagnose and fix touchpad failures, from the Fn toggle to driver and BIOS repairs."
thumbnail: "/images/thumbs/how-to-fix-touchpad-not-working-step-by-step.webp"
faqs:
  - q: "Why did my touchpad stop working suddenly?"
    a: "The most common sudden cause is the Fn touchpad toggle being pressed accidentally — one keystroke disables the device. The next most common is a Windows update replacing the touchpad driver with a generic version. Both are software states, which is why the touchpad usually returns without any hardware repair once the toggle or driver is corrected."
  - q: "How do I know if my touchpad problem is hardware or software?"
    a: "Check Device Manager with hidden devices shown: if the touchpad appears, even flagged, the hardware is communicating and the problem is software. If it is entirely absent and the BIOS shows no pointing device either, suspect the ribbon cable or the pad itself. A Linux live USB is the tiebreaker — a working pad there proves Windows is at fault."
  - q: "What is the difference between a precision touchpad and a vendor touchpad?"
    a: "Precision touchpads use Microsoft's standardized driver built into Windows, with gestures handled by the OS. Vendor touchpads (Synaptics, ELAN) need the maker's driver for full function. Windows 11 prefers precision mode; a vendor pad running on the generic fallback moves the cursor but loses gestures. Installing the maker's driver restores the full feature set."
  - q: "Can a swollen battery kill the touchpad?"
    a: "Yes, and it is more common than people expect. The battery sits directly under the palm rest on many laptops, and a swelling battery presses upward on the touchpad, first causing erratic clicks then total failure. If the palm rest feels raised or the touchpad clicks on its own, stop using the laptop and have the battery replaced — swollen batteries are a safety issue."
---

A dead touchpad turns a laptop into a desktop that you cannot move. No cursor, no clicks, no gestures — and the cause ranges from a single accidental keypress to a failed driver to a swollen battery pressing up from below. The symptom looks the same in all cases, which is why guessing wastes time and a step-by-step diagnosis does not.

This guide is ordered the way a technician works: the instant checks first (toggle, settings), then the driver layer, then the bus and BIOS, then hardware. Each step has a pass/fail test, so you always know whether to keep going or stop. Follow it top to bottom and you will find the failed layer.

## Why this happens

- **Fn touchpad toggle pressed accidentally**, disabling the device instantly.
- **Touchpad switched off in Windows Settings** or by a mouse-connected policy.
- **Windows Update replaced the touchpad driver** with a generic fallback.
- **Touchpad disabled in the BIOS** or set to the wrong bus mode.
- **I2C/SMBus bus driver failed**, so the pad's interface cannot start.
- **Power management suspending the pad** and failing to wake it.
- **Corrupted precision touchpad driver stack** after an update.
- **Ribbon cable loose, or swollen battery** pressing on the pad from below.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Press the touchpad toggle and check Settings

Look at the function row for a touchpad icon and press that Fn combination once. Many laptops show an on-screen indicator when the pad toggles. Then open Settings > Bluetooth & devices > Touchpad and confirm the master switch is on, and tick 'Leave touchpad on when a mouse is connected' — the auto-disable-on-mouse feature strands people constantly. Test movement immediately. If the cursor moves, the whole problem was the toggle, and you are done in under a minute.

1. Press the touchpad Fn toggle and watch for an indicator.
2. Open Settings > Bluetooth & devices > Touchpad and enable it.
3. Tick 'Leave touchpad on when a mouse is connected'.
4. Test movement, clicks, and two-finger scroll.

### Fix 2: Reinstall the touchpad driver from the laptop maker

If the toggle does not help, the driver is the next suspect. Download the touchpad driver from the laptop maker's support page for your exact model. In Device Manager, uninstall the touchpad entry (under Human Interface Devices or Mice and other pointing devices), ticking 'Delete the driver software'. Install the maker's package and reboot. This is the highest-yield repair for pads that vanished after updates. Synaptics-specific variants are covered in the [Synaptics deep dive](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/).

1. Download the touchpad driver from the laptop maker's support page.
2. Uninstall the touchpad device in Device Manager, deleting the driver.
3. Install the maker's driver package and reboot.
4. Verify movement, scrolling, and gestures.

### Fix 3: Repair the I2C/SMBus bus driver

Modern touchpads communicate over I2C or SMBus, and a flagged 'I2C HID Device' in Device Manager means the bus failed, not the pad. Uninstall the flagged bus device (deleting its driver), then choose 'Scan for hardware changes'. If it returns flagged, reinstall the chipset driver from the laptop maker — the bus controller lives in the chipset package. Microsoft's driver guidance is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Find the flagged I2C HID or SMBus device in Device Manager.
2. Uninstall it, deleting the driver software.
3. Scan for hardware changes and check the flag.
4. Install the maker's chipset driver and reboot if still flagged.

### Fix 4: Disable power management on the touchpad

A pad that works after boot but dies after sleep is being power-managed to death. In Device Manager, open the touchpad's Properties > Power Management and untick 'Allow the computer to turn off this device to save power'. In the advanced power plan settings, set USB selective suspend to Disabled if the pad is USB-attached. Then test across a full sleep/wake cycle — not just a reboot — because the failure only triggers on the sleep transition.

1. Untick power saving on the touchpad's Power Management tab.
2. Disable USB selective suspend in the power plan.
3. Put the laptop to sleep, wake it, and test the pad.
4. Leave the setting off permanently if it fixes the issue.

### Fix 5: Check the BIOS pointing-device setting

Reboot into the BIOS and confirm the internal pointing device is enabled. Some BIOS versions offer a touchpad mode (Basic/Advanced, PS/2/I2C) — set it to Advanced or I2C for modern drivers. If the BIOS shows no pointing device at all, note that: combined with an absent Device Manager entry, it points at hardware. The [Windows 11 touchpad guide](/articles/how-to-fix-touchpad-not-working-in-windows-11-24h2/) documents the BIOS paths per brand.

1. Enter the BIOS setup on boot.
2. Enable the internal pointing device.
3. Set the touchpad mode to Advanced/I2C if offered.
4. Save, boot, and reinstall the driver if needed.

### Fix 6: Test in Safe Mode and with a live USB

Boot into Safe Mode: if the touchpad works there, a third-party driver or startup program is interfering — clean-boot to find it. If Safe Mode is also dead, boot a Linux live USB. A working pad in Linux proves the hardware is fine and Windows is at fault (return to driver fixes). A dead pad in Linux confirms hardware. This two-boot test is the definitive software/hardware split and takes about ten minutes.

1. Boot into Safe Mode and test the touchpad.
2. If it works in Safe Mode, clean-boot Windows to find the conflict.
3. Boot a Linux live USB and test again.
4. Dead in Linux too means hardware — move to the next fix.

### Fix 7: Inspect for swollen battery and cable failure

Power down and check whether the palm rest is raised or the touchpad area feels domed — a swelling battery underneath kills touchpads mechanically and is a fire risk, so treat it urgently and do not puncture or bend it. If the chassis is flat, the ribbon cable connecting the pad may have worked loose, especially after a drop; reseating it requires opening the bottom cover. Touchpad modules are inexpensive model-specific parts, and a shop can replace one quickly.

1. Check for a raised palm rest or domed touchpad area.
2. If swollen, stop using the laptop and replace the battery promptly.
3. Otherwise, open the cover and reseat the touchpad ribbon cable.
4. Replace the touchpad module or get a repair quote.

## Closing

Touchpad failures follow a strict hierarchy, and this guide walks it from top to bottom: the toggle you pressed by accident, the setting that disabled it, the driver Windows Update swapped, the bus beneath the driver, the BIOS above it, and finally the hardware itself. Most cases end in the first three steps — the embarrassing Fn toggle is the single most common 'repair' in laptop history. The habit worth keeping is the diagnostic discipline: test after every step, and let the pass/fail result tell you which layer failed. A touchpad that moves is a solved problem; a touchpad that does not, tested methodically, always tells you exactly what is wrong.
