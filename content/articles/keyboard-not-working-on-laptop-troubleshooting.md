---
title: "Keyboard Not Working on Laptop: Full Troubleshooting Guide"
slug: keyboard-not-working-on-laptop-troubleshooting
date: 2026-09-22
categories: ["drivers"]
tags: ["keyboard not working", "laptop keyboard", "keyboard driver", "keys not responding", "filter keys"]
description: "Laptop keyboard not typing? Check Filter Keys, reinstall the keyboard driver, test in BIOS, and isolate hardware failure with this complete guide."
thumbnail: "/images/thumbs/keyboard-not-working-on-laptop-troubleshooting.webp"
faqs:
  - q: "Why did my laptop keyboard suddenly stop working?"
    a: "The most common sudden causes are Filter Keys getting enabled accidentally, which makes the keyboard ignore brief key presses, and a driver glitch after a Windows update. Liquid spills and ribbon cable issues cause physical failures. Check Filter Keys first since it takes ten seconds, then test the keyboard in the BIOS to separate software from hardware problems."
  - q: "What are Filter Keys and how do I turn them off?"
    a: "Filter Keys is a Windows accessibility feature that ignores brief or repeated keystrokes, making a working keyboard appear dead. Holding the right Shift key for eight seconds can enable it accidentally. Turn it off in Settings, Accessibility, Keyboard, under Sticky, Filter, and Toggle keys, and uncheck the shortcut that enables it."
  - q: "My keyboard works in BIOS but not in Windows — what is wrong?"
    a: "That proves the keyboard hardware is fine and the problem is software: a corrupted keyboard driver, Filter Keys, a conflicting third-party program, or malware intercepting keystrokes. Reinstall the keyboard driver in Device Manager, disable Filter Keys, and run a malware scan. Safe Mode testing narrows it further."
  - q: "Can I use my laptop if the keyboard is physically broken?"
    a: "Yes. Enable the On-Screen Keyboard in Settings, Accessibility, Keyboard, or press Win plus Ctrl plus O. A USB keyboard also works immediately with no setup. These workarounds keep you productive while you decide between a keyboard replacement, which is feasible on many models, and professional repair."
---

A laptop keyboard that stops responding ranges from mildly annoying (a few dead keys) to work-stopping (nothing types at all). Before assuming the worst, know this: a large share of "dead keyboard" cases are software — an accidentally enabled accessibility feature, a driver hiccup, or a stuck state that a reset clears. The physical keyboard is actually quite robust.

The diagnostic approach is simple and decisive. First rule out the software traps that mimic hardware failure, then test the keyboard outside Windows (in the BIOS), which instantly tells you whether you're dealing with software or hardware. Only then do you consider physical causes.

## Why this happens

- **Filter Keys enabled accidentally:** Holding right Shift for 8 seconds enables this accessibility feature, which then ignores normal keystrokes — the keyboard looks dead but isn't.
- **Corrupted keyboard driver:** The standard PS/2 keyboard driver can corrupt after updates, producing total or partial key failure.
- **Stuck modifier or power state:** A crashed embedded controller can leave the keyboard unresponsive until the power is fully drained.
- **Third-party software intercepting keys:** Keyboard remappers, macro tools, and some "gaming" utilities hook keystrokes and can block them entirely.
- **Liquid damage:** Even small spills corrode the keyboard membrane over hours or days, causing spreading key failure.
- **Loose ribbon cable:** The keyboard connects via a fragile ribbon cable; drops or prior disassembly can partially unseat it.
- **BIOS-level disable:** Some BIOS versions have keyboard or internal-device toggles that can disable the built-in keyboard.
- **Malware keyloggers:** Malicious software intercepting keystrokes can make typing behave erratically or appear broken in certain applications.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Filter Keys — the ten-second trap

1. Open **Settings → Accessibility → Keyboard**.
2. Turn **Filter keys** OFF if it's on.
3. Uncheck **"Allow the shortcut key to start Filter Keys"** so holding Shift can't re-enable it silently.
4. Also verify **Sticky keys** and **Toggle keys** are off while you're here.
5. Test typing immediately. If keys now respond, that was the entire problem — one of the most common [keyboard failure patterns](/articles/best-way-to-fix-keyboard-not-working-on-laptop/) in support forums.

### Fix 2: Test the keyboard in the BIOS

1. Restart and enter BIOS/UEFI setup (**F2**, **Del**, or **Esc** depending on brand).
2. Try typing in any BIOS text field, or just navigate menus with arrow keys.
3. If the keyboard works in BIOS, the hardware is fine — your problem is 100% Windows software. Continue with the driver fixes.
4. If keys fail in BIOS too, skip to the hardware fixes (Fix 7 and 8) — no Windows reinstall will help.
5. This single test saves enormous wasted effort and is the most important diagnostic step in keyboard troubleshooting.

### Fix 3: Reinstall the keyboard driver

1. Press **Win + X** and open **Device Manager** (use the On-Screen Keyboard, **Win + Ctrl + O**, if needed).
2. Expand **Keyboards**, right-click **Standard PS/2 Keyboard**, and choose **Uninstall device**.
3. Restart the laptop — Windows reinstalls the keyboard driver automatically at boot.
4. Test all keys, including function keys and the number row.
5. If Device Manager shows a yellow warning on the keyboard entry, note the error code before uninstalling; Code 19 or 39 confirm driver corruption. Verifying the [driver version](/articles/best-way-to-check-driver-version-in-device-manager/) afterward confirms a clean reinstall.

### Fix 4: Power-drain to reset the embedded controller

1. Shut down fully and unplug the charger.
2. If the battery is removable, take it out; otherwise just leave it unplugged.
3. Hold the power button for **30 seconds** to drain residual power and reset the embedded controller that manages the keyboard.
4. Reconnect power and boot normally.
5. Test the keyboard at the login screen. This clears the stuck-controller state that survives ordinary restarts and causes keyboards to stay dead for no visible reason.

### Fix 5: Boot into Safe Mode to isolate software conflicts

1. Hold **Shift** while clicking **Restart**, then go to **Troubleshoot → Advanced options → Startup Settings → Restart**, and press **4** for Safe Mode.
2. Test the keyboard in Safe Mode's minimal driver environment.
3. If it works in Safe Mode, a startup program or third-party driver is intercepting keystrokes — open **msconfig**, disable startup items in halves, and bisect to find the culprit.
4. Suspect keyboard remappers, macro software, and recently installed "system optimizer" tools first.
5. Uninstall the offending program completely rather than just disabling it, since hooks can persist.

### Fix 6: Run a malware scan

1. Open **Windows Security → Virus & threat protection** and run a **Full scan**.
2. Keyloggers and some info-stealers hook the keyboard at a low level and can cause missed, doubled, or blocked keystrokes.
3. If Windows Security finds nothing but suspicion remains, run the **Microsoft Safety Scanner** from [Microsoft Support](https://support.microsoft.com/en-us/windows) as a second opinion.
4. After cleaning any detections, reinstall the keyboard driver (Fix 3) since malware-damaged driver stacks don't always recover on their own.
5. Change important passwords from a clean device if a keylogger was found — assume keystrokes were captured.

### Fix 7: Check for physical damage and reseat the cable

1. Inspect the keyboard for signs of liquid: sticky keys, discoloration, or a spill you remember. Spill damage spreads as corrosion advances — act quickly by powering off and drying.
2. Blow out debris under keys with compressed air held upright.
3. For partial failures (a row or cluster of dead keys), the membrane or ribbon cable is the likely fault. On models with a removable keyboard, reseating the ribbon cable (following the service manual) can restore contact.
4. Test with an external USB keyboard — if it types perfectly, the OS side is fine and the built-in keyboard hardware is the fault.
5. Individual dead keys on an otherwise working keyboard almost always mean membrane damage, not software.

### Fix 8: Replace or work around a dead keyboard

1. Look up your model's keyboard replacement difficulty — many business laptops have field-replaceable keyboards secured by screws; ultrabooks often require full disassembly.
2. Replacement keyboards are inexpensive for common models; follow a video guide for your exact model if you're comfortable opening the machine.
3. If the laptop is under warranty, contact the manufacturer instead — keyboard replacement is typically covered.
4. As an interim or permanent workaround, a compact USB or Bluetooth keyboard works with zero configuration.
5. Enable the **On-Screen Keyboard** (**Settings → Accessibility → Keyboard**) for password fields and short typing sessions.

## Closing

Keyboard failure diagnosis hinges on one test: does it work in the BIOS? Yes means software — Filter Keys, drivers, or conflicting programs, all fixable in minutes. No means hardware — cable, membrane, or controller. Work the list in order, and you'll know which world you're in before spending money or opening the machine.
