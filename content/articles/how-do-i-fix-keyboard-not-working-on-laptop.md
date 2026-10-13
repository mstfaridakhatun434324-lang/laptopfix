---
title: "Laptop Keyboard Not Working? How to Fix It (Windows 10/11)"
slug: how-do-i-fix-keyboard-not-working-on-laptop
date: "2026-10-12"
categories: ["drivers"]
tags: ["laptop keyboard", "keys not typing", "keyboard driver", "filter keys", "keyboard troubleshooting"]
description: "Laptop keyboard not typing or some keys dead? Learn how to fix a non-working laptop keyboard on Windows 10 and 11, from filter keys to driver and hardware checks."
thumbnail: "/images/thumbs/how-do-i-fix-keyboard-not-working-on-laptop.webp"
faqs:
- q: "Why did my laptop keyboard suddenly stop working?"
  a: "The most common causes are Filter Keys being accidentally enabled, a corrupted keyboard driver after a Windows update, or the keyboard being disabled by a stuck Fn-lock state. Physical causes like a loose ribbon cable or liquid damage are less common but possible. A quick test: if the keyboard works in BIOS setup, the hardware is fine and the problem is Windows software, which is fixable without repair."
- q: "How do I turn off Filter Keys on Windows 11?"
  a: "Open Settings, go to Accessibility, then Keyboard, and turn off Filter Keys. This feature ignores brief or repeated keystrokes and is easily enabled by holding the right Shift key for eight seconds. When active, typing feels broken — keys seem dead or repeat strangely. Disabling it restores normal typing instantly, and you can also disable the shortcut that turns it on."
- q: "Can a Windows update break my laptop keyboard?"
  a: "Yes. Updates sometimes install an incompatible keyboard or chipset driver, or they enable accessibility features like Filter Keys during the upgrade. If the keyboard died immediately after an update, check Filter Keys first, then reinstall the keyboard driver from Device Manager. Rolling back the recent update is a further option if the timing lines up exactly."
- q: "What should I do if only some keys are not working?"
  a: "A few dead keys usually indicate a hardware problem — debris under the keycaps, a damaged keyboard membrane, or a partially seated ribbon cable — rather than software, since software failures typically kill the whole keyboard. Try compressed air under the affected keys and test with an external USB keyboard. If the external keyboard works fully, the internal keyboard likely needs cleaning or replacement."
---

You open your laptop, type your password, and nothing appears. Or half the keys work and the rest are dead. Or every keypress produces the wrong character. A non-working keyboard turns a laptop into a very expensive paperweight, and the panic it causes makes careful diagnosis feel impossible — but the fix is usually simpler than the fear suggests.

Keyboards fail in two distinct ways: all at once (almost always software — a setting, a driver, or an update) or partially (usually hardware — debris, a damaged membrane, or a loose cable). Knowing which pattern you have cuts the suspect list in half immediately. A keyboard that works in BIOS but not in Windows, for example, is a software problem by definition, and software problems do not require a repair shop.

This guide separates the two patterns fast, then walks through the software fixes in order — settings, drivers, and system state — before covering the hardware checks. Grab a USB keyboard if you have one; it makes the software steps far easier.

## Why this happens

- **Filter Keys accidentally enabled**: Holding right Shift for eight seconds enables this accessibility feature, which makes keys seem dead.
- **Corrupted keyboard driver**: Updates can replace the working driver with one that fails to initialize the keyboard.
- **Wrong keyboard layout selected**: A layout change makes keys produce unexpected characters rather than nothing.
- **Stuck Fn-lock or Num Lock state**: Laptops remap keys under Fn-lock; a latched state scrambles input.
- **Debris or damage under keys**: Crumbs and dust physically prevent key switches from registering.
- **Loose internal ribbon cable**: The keyboard connects via a fragile ribbon that works loose with drops or heat cycles.
- **Liquid damage**: Even small spills corrode the keyboard membrane, typically killing clusters of keys.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and test in BIOS

The single most informative test takes two minutes: restart, enter BIOS/UEFI setup, and try typing there. BIOS talks to the keyboard without any Windows driver, setting, or accessibility feature involved. If keys work in BIOS, your hardware is fine and the fault is 100% Windows software — keep going through the fixes below with confidence.

1. Restart the laptop and enter BIOS/UEFI setup (usually F2 or Del).
2. Try typing in any text field, or just press keys and watch for responses.
3. If keys work in BIOS, exit without saving and continue with Fix 2.
4. If keys are dead in BIOS too, skip to the hardware checks in Fix 6.
5. Note the pattern: all keys dead suggests software or cable; some keys dead suggests physical damage.

### Fix 2: Turn off Filter Keys and Sticky Keys

Filter Keys is the classic "my keyboard broke overnight" culprit. It tells Windows to ignore brief keystrokes, so normal typing produces nothing or sporadic characters. It activates via an eight-second Shift hold that people trigger accidentally. Sticky Keys causes similar confusion with modifier keys. Both live in Accessibility settings and disable instantly.

1. Open Settings, go to Accessibility, then Keyboard.
2. Turn off Filter Keys, Sticky Keys, and Toggle Keys.
3. Click the Filter Keys section and disable the "hold Shift for eight seconds" shortcut.
4. Test typing in Notepad immediately.
5. If typing works, the mystery is solved — no driver work needed.

### Fix 3: Reinstall the keyboard driver

When the keyboard is dead across all of Windows but works in BIOS, the driver translating keypresses is the prime suspect. Device Manager lists laptop keyboards under a standard entry that is easy to reinstall; Windows redetects the hardware on reboot and rebuilds the driver binding. This fixes corruption from updates in the large majority of software cases.

1. Press Win + X and open Device Manager (use an external keyboard or the on-screen keyboard: Win + Ctrl + O).
2. Expand "Keyboards," right-click the internal keyboard entry, and choose "Uninstall device."
3. Restart the laptop — Windows will redetect the keyboard and reinstall the driver.
4. Test typing at the login screen.
5. If it still fails, download the chipset driver from your laptop maker's support page, since the keyboard routes through the chipset.

### Fix 4: Check the keyboard layout and language

If keys produce the wrong characters rather than nothing — @ and " swapped, or accents appearing unasked — the layout changed, not the hardware. Windows switches layouts with Win + Space, which people hit accidentally. This is not a failure at all, just a setting, and it reverses in seconds.

1. Look at the taskbar language indicator (e.g., ENG US vs ENG UK).
2. Press Win + Space to cycle back to your correct layout.
3. Open Settings, Time and language, Language and region, and remove layouts you never use.
4. Test the previously wrong keys.
5. If characters are still wrong, continue — but layout issues never cause fully dead keys.

### Fix 5: Boot into Safe Mode and try a clean boot

Third-party software — keyboard remappers, macro tools, some antivirus suites — can intercept keystrokes before applications see them. Safe Mode loads only Microsoft drivers and services, so a keyboard that works there is being blocked by something installed. A clean boot then identifies the offender by elimination.

1. Hold Shift while clicking Restart, then navigate to Troubleshoot, Advanced options, Startup Settings, and boot into Safe Mode.
2. Test the keyboard in Safe Mode (Notepad works fine there).
3. If it works, the cause is third-party software — return to normal mode.
4. Use `msconfig` to perform a clean boot, re-enabling startup items in halves to isolate the culprit.
5. Uninstall or reconfigure the offending program once found.

### Fix 6: Inspect for physical problems

If the keyboard is dead in BIOS too, or only some keys fail, the problem is physical. Before paying for repair, check the simple things: debris under keys, a battery pressing on the keyboard from below (swollen batteries push upward), and the external-keyboard test that confirms the rest of the system is fine. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) cover software troubleshooting, but hardware needs hands-on checks.

1. Turn the laptop off, tilt it, and tap gently to dislodge debris; use compressed air under problem keys.
2. Remove the back panel (if comfortable) and check whether the battery looks swollen — a bulging battery needs replacement, not keyboard repair.
3. Test with a USB keyboard: full function there confirms the system is fine and only the internal keyboard is at fault.
4. If you recently had the laptop serviced, the keyboard ribbon cable may not be fully seated — a technician can reseat it in minutes.
5. For liquid damage, power off immediately, do not try to dry-and-hope; corrosion spreads while powered.

### Fix 7: Restore the system to when typing worked

When software is clearly at fault but no individual fix lands — the keyboard died after an update and driver reinstalls do not stick — roll the whole system back. System Restore reverts drivers, settings, and updates to a chosen date while leaving personal files alone. It is the broadest software fix available short of reinstalling Windows.

1. Search for "Create a restore point" and open System Protection.
2. Click "System Restore" and choose a date before the keyboard failed.
3. Complete the wizard and let the laptop restart.
4. Test typing at the login screen.
5. If no restore point exists, consider a Windows reset with the keep-my-files option as the final software step.

Touchpad failures often accompany keyboard issues after the same updates — if your cursor is frozen too, see the [Synaptics touchpad troubleshooting guide](/articles/troubleshoot-synaptics-touchpad-not-working/). A keyboard showing as an [unknown device](/articles/how-to-fix-unknown-device-in-device-manager/) in Device Manager needs the driver-identification approach instead.

## Closing

A dead laptop keyboard is a software problem more often than people expect — Filter Keys, a corrupted driver, or an update side effect. Test in BIOS first to split hardware from software, then work the settings and driver fixes. When keys die in clusters or after a spill, though, believe the hardware evidence and get the keyboard serviced.
