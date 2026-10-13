---
title: "Synaptics Touchpad Not Working: Troubleshooting Walkthrough"
slug: synaptics-touchpad-not-working-troubleshooting
date: 2026-10-13
categories: ["drivers"]
tags: ["synaptics", "touchpad", "precision touchpad", "driver"]
description: "Synaptics touchpad dead after an update or fresh install? A full troubleshooting walkthrough from driver stack to hardware."
thumbnail: "/images/thumbs/synaptics-touchpad-not-working-troubleshooting.webp"
faqs:
  - q: "Why did my Synaptics touchpad stop working after a Windows update?"
    a: "Windows Update frequently replaces the manufacturer's Synaptics driver with a generic Microsoft precision-touchpad driver or vice versa, and the two stacks don't interoperate. The touchpad then shows as working in Device Manager while producing no cursor movement. Reinstalling the exact Synaptics package from your laptop maker restores the correct stack."
  - q: "Should I use the Synaptics driver or the Windows precision driver?"
    a: "Use whichever your laptop shipped with. If your model came with Synaptics software and its control panel, keep the Synaptics stack. If it shipped as a precision touchpad, keep Microsoft's driver. Mixing them — installing Synaptics software over a precision driver — is a top cause of dead cursors and missing settings."
  - q: "My touchpad works in BIOS but not in Windows. What does that mean?"
    a: "A touchpad that moves the cursor in BIOS or a live Linux USB but not in Windows is always a driver or OS configuration problem, never a hardware fault. Focus entirely on the driver stack and Windows settings."
  - q: "Can I fix a Synaptics touchpad without an external mouse?"
    a: "Yes. Windows is fully keyboard-navigable: Win + X opens the power-user menu, arrow keys move, Enter selects, and Tab cycles controls. You can open Device Manager, uninstall and reinstall drivers, and toggle touchpad settings in the Settings app without ever touching a mouse. A phone-as-mouse app over USB is another fallback."
---

The cursor won't move. Or it moves but gestures are gone, or the touchpad settings page in Windows has vanished entirely, leaving you with a laptop that's technically working and practically unusable. Synaptics touchpads fail in a particularly confusing way because there are two competing driver stacks — Synaptics' own and Microsoft's precision touchpad — and Windows updates love to swap one for the other without asking.

This matters because the two stacks are not interchangeable. A laptop that shipped with the Synaptics driver expects Synaptics' software; force-feeding it the precision driver (or the reverse) produces the classic symptom: Device Manager shows a happy, working device while the cursor sits frozen. The walkthrough below untangles exactly which stack you have, puts the right one back, and then works through the settings, power, and hardware layers that account for everything else.

One quick triage before you start: does the cursor move in BIOS/UEFI or on a Linux live USB? If yes, your hardware is fine and this is purely software — skip straight to the driver fixes with confidence. There's also a focused [Synaptics fix for Windows 11 24H2](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/) if your failure lines up with that update.

## Why this happens

- **Windows Update swapped the driver stack.** The most common cause, full stop: a Synaptics laptop gets the generic precision driver (or vice versa), and the touchpad goes silent while Device Manager reports success.
- **The Synaptics driver installation corrupted.** Interrupted OEM updates or conflicting remnants of both stacks leave the device in a limping state — present, "working," motionless.
- **The touchpad is disabled at the FN-key or BIOS level.** Many laptops have an **Fn + F-key** touchpad toggle that's easy to hit accidentally; some BIOSes expose a separate disable.
- **Windows' own touchpad setting got turned off.** An update or a misclick under **Settings > Bluetooth & devices > Touchpad** can simply switch the device off in software.
- **Power management suspended the touchpad.** On some models the touchpad rides an internal bus that Windows aggressively power-manages, killing it after sleep until reboot.
- **Palm-rejection or sensitivity settings went extreme.** Not truly "not working" — the cursor moves but feels dead because sensitivity dropped to minimum or palm detection rejects every touch.
- **The ribbon cable loosened.** After drops or palm-rest flex, the touchpad's internal connector can walk loose — suspect this only if software is fully ruled out and the failure is intermittent.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the hardware toggle and Windows setting

The two-second fixes that embarrass everyone. Get them out of the way first.

1. Press your laptop's touchpad toggle — usually **Fn + F5/F7/F9** (look for the touchpad icon on the function keys). Press it once, wait three seconds, and test.
2. Go to **Settings > Bluetooth & devices > Touchpad** and confirm the master **Touchpad** toggle is **On**.
3. On that same page, check **Touchpad sensitivity** isn't set to *Low sensitivity* and that *Leave touchpad on when a mouse is connected* matches your situation — with it off and a mouse receiver plugged in, the touchpad correctly disables itself.
4. If the entire Touchpad settings page is missing, Windows doesn't see a compatible touchpad at all — that's a driver-stack problem, continue to Fix 2.

### Fix 2: Identify which driver stack you should have

Installing the wrong stack is worse than installing nothing. Determine yours first.

1. Check your laptop maker's spec page or the original driver list: if they publish a **Synaptics TouchPad driver** (often with a Synaptics control panel), you're on the Synaptics stack.
2. In **Device Manager > Human Interface Devices** or **Mice and other pointing devices**, note what's installed: *Synaptics TouchPad* / *Synaptics SMBus* means Synaptics stack; *HID-compliant touch pad* with precision settings in the Settings app means Microsoft precision.
3. If Device Manager shows one thing and the manufacturer's site ships the other, trust the manufacturer — that's the stack your firmware was validated against.
4. Write down the current driver version (**Properties > Driver**) as your baseline before changing anything.

### Fix 3: Reinstall the correct manufacturer driver

The anchor fix for most Synaptics failures.

1. Download the touchpad driver for your exact model from the laptop maker's support site — not from Synaptics' generic page, not from Windows Update.
2. In **Device Manager**, right-click the touchpad device > **Uninstall device**, checking *Attempt to remove the driver for this device* to clear the wrong stack completely.
3. Run the manufacturer's installer as administrator and reboot — even if it doesn't ask. Touchpad drivers often need the reboot to bind to the SMBus or I²C controller.
4. Verify in **Settings > Bluetooth & devices > Touchpad** that the full settings page (with your expected options) is back, and test multi-finger gestures.

### Fix 4: Roll back a driver that an update replaced

For "worked yesterday" failures, the update's driver is the suspect.

1. In **Device Manager**, open the touchpad device **Properties > Driver** tab.
2. If **Roll Back Driver** is available, use it and choose *A previous version of the driver seemed to work better*.
3. Then stop Windows from re-applying the wrong one: use your OEM's update utility for drivers, and see our guide on [disabling automatic driver updates](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) to keep the correct stack in place.
4. Microsoft documents touchpad and input troubleshooting on the [official Windows support site](https://support.microsoft.com/en-us/windows) if you need the platform-level steps.

### Fix 5: Check BIOS and the internal bus

When Device Manager shows no touchpad device at all, look below the OS.

1. Enter **BIOS/UEFI** and look for a touchpad entry (often under **Advanced** or **Main**) — ensure it's Enabled, not Disabled or "Auto" behaving badly.
2. Back in Windows, expand **Device Manager > System devices** and check the **Intel Serial IO** / **SMBus** controllers for warning icons — the touchpad depends on these buses, and a broken bus driver takes the touchpad with it. Reinstall chipset drivers from the manufacturer if you see warnings.
3. Try a **full shutdown** (not restart): power off, unplug, hold the power button 20 seconds, then boot. This resets embedded-controller state that a warm reboot preserves.
4. If an external USB mouse works fine throughout, the USB stack is healthy and the fault is isolated to the touchpad's own bus or driver.

### Fix 6: Rule out software conflicts

Something else can be holding the touchpad hostage.

1. Boot into **Safe Mode** — if the touchpad works there, a startup program or filter driver is interfering. Common culprits: old mouse utilities, remote-desktop input hooks, and third-party "touchpad enhancer" tools.
2. Use **msconfig** to disable startup items in halves until the offender is found, or check **Device Manager > View > Show hidden devices** for ghost mouse/touchpad entries from previously installed software and uninstall them.
3. Third-party antivirus with "input protection" features has been known to block touchpad input — test with it temporarily disabled.
4. If you recently installed any mouse or gesture software, remove it before reinstalling the Synaptics driver — install order matters, and the Synaptics stack should go in clean.

### Fix 7: Confirm hardware with an outside-OS test

The final verdict: hardware or software, proven rather than guessed.

1. Boot a **Linux live USB** (Ubuntu works) — if the touchpad moves the cursor there, the hardware is definitively fine and the problem is 100% Windows software. Revisit Fixes 2–4 with that certainty.
2. If it's dead in Linux and in BIOS too, the touchpad hardware, its ribbon cable, or the motherboard connector is at fault.
3. For out-of-warranty laptops, a replacement touchpad module is usually a $15–30 part and a moderate DIY job (palm rest removal); in-warranty, this is a manufacturer repair.
4. As an interim measure, enable **Mouse Keys** (**Settings > Accessibility > Mouse**) so the numeric keypad can drive the cursor — it keeps the laptop usable while you arrange the repair.

## Closing

Synaptics touchpad failures are driver-stack failures far more often than hardware failures: the wrong stack installed by an update, a corrupted OEM package, or a toggle nobody remembers pressing. Identify the stack your laptop shipped with, reinstall it cleanly from the manufacturer, and keep Windows Update from swapping it again. The cursor that wouldn't move almost always comes back.
