---
title: "Laptop Keyboard Not Working? Step-by-Step Fix for Windows"
slug: "how-to-fix-keyboard-not-working-on-laptop-step-by-step"
date: "2026-09-14"
categories: ["drivers"]
tags: ["keyboard not working", "laptop keyboard", "keyboard driver", "windows 11", "input device"]
description: "Laptop keyboard dead or typing wrong characters? Step-by-step fixes for driver issues, filter keys, BIOS settings, and hardware checks to restore typing."
thumbnail: "/images/thumbs/how-to-fix-keyboard-not-working-on-laptop-step-by-step.webp"
faqs:
  - q: "Why did my laptop keyboard suddenly stop working?"
    a: "The most common sudden causes are an accidentally enabled accessibility feature like Filter Keys, a keyboard driver crash after a Windows update, or the keyboard being disabled in Device Manager. Liquid spills and ribbon-cable issues cause physical failures, but software is the culprit more often than people expect. Checking Filter Keys and reinstalling the keyboard driver resolves the majority of sudden failures."
  - q: "How do I type if my laptop keyboard is completely dead?"
    a: "Use the On-Screen Keyboard: press Win + Ctrl + O to open it, or go to Settings > Accessibility > Keyboard and enable it. A USB keyboard also works immediately with no setup. These let you log in, navigate Device Manager, and run driver fixes while the built-in keyboard is down. The on-screen keyboard is also useful for entering your password at the login screen."
  - q: "Can a Windows update break the laptop keyboard?"
    a: "Yes. Updates sometimes install an incompatible keyboard or chipset driver, enable Filter Keys unexpectedly, or change the keyboard layout so keys produce wrong characters. If the keyboard failed right after an update, check the keyboard layout in Settings, turn off Filter Keys, and roll back or reinstall the keyboard driver in Device Manager."
  - q: "How can I tell if it's a driver problem or a broken keyboard?"
    a: "Test the keyboard in the BIOS setup or at the boot menu: if keys work there but not in Windows, it is a software or driver problem. If keys fail in the BIOS too, or an external USB keyboard works fine while the built-in one does not, the built-in keyboard hardware or its ribbon cable is the likely fault. Driver reinstalls only help the software case."
---

A non-working laptop keyboard ranges from mildly annoying (a few dead keys) to completely paralyzing (no input at all, including at the login screen). Before assuming the hardware is dead, work through this guide — keyboard failures are caused by accessibility settings, driver glitches, and disabled devices far more often than by broken hardware, and the software fixes take only minutes.

First, get yourself a way to type: press Win + Ctrl + O for the On-Screen Keyboard, or plug in any USB keyboard. You will need input for the driver steps below, and the on-screen keyboard works even at the Windows login screen.

## Why this happens

- **Filter Keys enabled:** This accessibility feature ignores brief keystrokes and is the single most common cause of "keyboard stopped working."
- **Wrong keyboard layout:** An update can switch the layout, making keys type the wrong characters rather than nothing at all.
- **Corrupted keyboard driver:** The standard PS/2 or HID keyboard driver can fail after a Windows update, killing all input.
- **Keyboard disabled in Device Manager:** The device can end up disabled by troubleshooting software or a failed update.
- **Sticky Keys or other accessibility interference:** Related accessibility features can change how keystrokes register.
- **BIOS-level disable:** Some laptops can disable the internal keyboard in firmware, hiding it from Windows.
- **Fast Startup preserving a bad state:** The hibernation snapshot can lock in a broken keyboard driver state across reboots.
- **Physical failure:** Liquid damage, a loose ribbon cable, or worn-out key switches — the hardware causes, checked last.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off Filter Keys and Sticky Keys

This thirty-second check resolves a huge number of keyboard "failures."

1. Open Settings > Accessibility > Keyboard.
2. Turn off Sticky Keys, Filter Keys, and Toggle Keys.
3. Under Filter Keys, make sure it is not set to turn on via the Shift key shortcut.
4. Test typing in Notepad immediately — Filter Keys causes exactly the symptom of keys needing long presses.
5. If keys now work but feel slow, the problem was Filter Keys all along.

### Fix 2: Check the keyboard layout and language

If keys produce wrong characters rather than nothing, the layout changed.

1. Look at the taskbar language indicator (near the clock) and confirm it shows your expected language.
2. Press Win + Space to cycle layouts and test after each switch.
3. Go to Settings > Time & language > Language & region and remove any keyboard layouts you do not use.
4. Make sure the preferred layout is at the top of the list.
5. Restart the laptop so the layout choice sticks across the login screen too.

### Fix 3: Reinstall the keyboard driver

A clean driver reset fixes corruption from updates and failed installs.

1. Press Win + X and open Device Manager (use the on-screen keyboard if needed).
2. Expand Keyboards and right-click "Standard PS/2 Keyboard" or the HID keyboard entry.
3. Choose Uninstall device — do not worry, Windows reinstalls it on restart.
4. Click Action > Scan for hardware changes, or simply restart the laptop.
5. Test every key after reboot, including function keys and the number row.
6. If some keys remain dead while most work, note which ones — a pattern (like a whole row) suggests hardware.
7. For the [Windows 11-specific variant](/articles/how-to-fix-keyboard-not-working-on-laptop-on-windows-11/), the same reinstall sequence applies with the newer Settings paths.

### Fix 4: Update the chipset driver

The keyboard connects through the chipset, and an outdated chipset driver can break input.

1. Visit your laptop maker's support site and download the latest chipset driver for your exact model.
2. Install it and restart when prompted.
3. Return to Device Manager and confirm the keyboard entry shows no warning icon.
4. Test the keyboard, including after a sleep-wake cycle, which is when chipset issues usually resurface.
5. Microsoft's [Windows support documentation](https://support.microsoft.com/en-us/windows) covers input-device troubleshooting if you need the official reference.

### Fix 5: Boot into Safe Mode to isolate software conflicts

Safe Mode loads a minimal driver set — if the keyboard works there, a third-party program is interfering.

1. Hold Shift while clicking Restart, then go to Troubleshoot > Advanced options > Startup Settings > Restart.
2. Press 4 for Safe Mode and test the keyboard at the login screen and desktop.
3. If it works in Safe Mode, think about recently installed software — keyboard macro tools, gaming overlays, and some antivirus products hook keystrokes.
4. Uninstall suspects one at a time from Safe Mode or normal mode and retest.
5. A clean boot (via `msconfig`, disabling all non-Microsoft services) is the systematic way to find the culprit.

### Fix 6: Disable Fast Startup and reset power state

Fast Startup can preserve a broken keyboard driver state indefinitely.

1. Open Control Panel > Power Options > Choose what the power buttons do.
2. Click "Change settings that are currently unavailable" and uncheck "Turn on fast startup".
3. Shut down fully, unplug the laptop, and hold the power button for 15 seconds to drain residual power.
4. Power on and test the keyboard immediately at the login screen.
5. This full power drain also resets the embedded controller, which manages the keyboard on many laptops.

### Fix 7: Check the BIOS and test outside Windows

Determine definitively whether this is software or hardware.

1. Restart and enter the BIOS setup — try typing in any text field there.
2. If the keyboard works in BIOS but not Windows, the problem is 100% software-side: reinstall or repair Windows.
3. If it fails in BIOS too, check whether the BIOS has an internal keyboard toggle and make sure it is enabled.
4. Boot a Linux live USB as a second opinion outside of Windows entirely.
5. A keyboard dead in BIOS, Linux, and Windows is a hardware fault — ribbon cable or keyboard module.

### Fix 8: Reseat the keyboard cable or arrange service

Only attempt this if you have confirmed a hardware fault and are comfortable opening the laptop.

1. Check your warranty status first — opening the laptop can void it.
2. Power off, unplug, and remove the battery if it is removable.
3. Following your model's service manual, access the keyboard's ribbon cable connector on the motherboard.
4. Release the locking tab, reseat the ribbon cable fully and squarely, and relock it.
5. Reassemble and test. If keys are still dead, the keyboard module itself needs replacement — a common, inexpensive part on most models.
6. For a companion input-device guide, see [fixing a dead touchpad](/articles/how-to-fix-synaptics-touchpad-not-working-on-windows-11/), which shares the driver-diagnosis approach.

## Closing

Laptop keyboard failures follow a clear hierarchy: accessibility settings first, then layout, then drivers, then deeper software conflicts, and hardware last. The BIOS test in Fix 7 is the definitive fork in the road — it tells you in sixty seconds whether to keep troubleshooting Windows or start looking at the keyboard module itself.
