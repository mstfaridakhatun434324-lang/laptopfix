---
title: "Laptop Keyboard Not Working? Fixes That Actually Work"
slug: how-to-fix-keyboard-not-working-on-laptop-reddit
date: 2026-09-28
categories: ["drivers"]
tags: ["keyboard", "laptop keyboard", "drivers", "troubleshooting", "windows"]
description: "Laptop keyboard dead or typing wrong characters? Real fixes that work — from filter keys and driver resets to ribbon cables and external keyboard tests."
thumbnail: "/images/thumbs/how-to-fix-keyboard-not-working-on-laptop-reddit.webp"
faqs:
  - q: "Why did my laptop keyboard suddenly stop working?"
    a: "Sudden total failure is usually software: a Windows update broke the keyboard driver, Filter Keys got enabled accidentally, or the driver binding corrupted. Gradual failure — a few keys dying over weeks — points at hardware like liquid damage or a failing ribbon cable. The pattern of failure tells you which you're dealing with."
  - q: "What is Filter Keys and why does it break typing?"
    a: "Filter Keys is an accessibility feature that ignores brief or repeated keystrokes. It's easily enabled by accident — holding the right Shift key for eight seconds triggers the prompt. With it on, typing feels broken: keys seem dead or repeat strangely. Turning it off in Settings > Accessibility > Keyboard instantly restores normal typing."
  - q: "Can I fix a laptop keyboard without replacing it?"
    a: "If the cause is software — drivers, Filter Keys, or a stuck key — yes, completely. If it's hardware like a damaged ribbon cable or liquid damage, a temporary fix is using an external USB keyboard while you arrange a proper keyboard replacement, which is inexpensive on most laptop models."
  - q: "Why do some keys work but others don't?"
    a: "Partial failure usually means hardware: a damaged keyboard matrix, debris under specific keys, or liquid damage affecting certain rows. Software problems tend to kill the whole keyboard at once. Try an external keyboard — if all keys work there, your laptop's keyboard hardware is the problem."
---

Few things are as immediately crippling as a dead laptop keyboard. No password entry, no shortcuts, no work. The forums are full of this problem, and the advice ranges from useful to superstitious. Here's the distilled version: keyboard failures split cleanly into software causes (fixable in minutes) and hardware causes (fixable with parts), and there's a simple test that tells you which camp you're in within thirty seconds.

That test is an external USB keyboard. If the external keyboard works fine, Windows' input system is healthy and the problem is your laptop's keyboard hardware or its driver. If the external keyboard *also* fails, it's system-wide software. Start there, then follow the matching path below.

One more reassurance before you start: a completely dead laptop keyboard is rarely a motherboard problem. The keyboard is a separate, inexpensive part connected by a ribbon cable, and the driver is pure software. That means nearly every outcome here is good news — either a settings toggle, a driver reinstall, or a cheap part. The expensive, unfixable scenarios are the rarest ones.

## Why this happens

- **Filter Keys enabled:** accessibility feature silently swallowing keystrokes.
- **Corrupt keyboard driver:** the PS/2 or HID keyboard driver binding broke.
- **Windows update regression:** an update damaged the keyboard driver stack.
- **Stuck or debris-blocked keys:** physical obstruction under keycaps.
- **Loose ribbon cable:** the keyboard's internal connector worked free.
- **Liquid damage:** spills corrode the keyboard matrix over days or weeks.
- **BIOS-level failure:** keyboard dead even in BIOS means hardware, period.
- **Third-party software interference:** macro tools or keyboard remappers hijacking input.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: The 30-second external keyboard test

1. Plug in any USB keyboard (borrow one if needed).
2. If it types normally, your laptop's keyboard hardware or driver is the problem — continue below.
3. If the USB keyboard also fails, it's system-wide: jump to Fix 4 (drivers) and Fix 7 (software interference).
4. Use the on-screen keyboard (**Win + Ctrl + O**) as a stopgap for passwords and urgent typing.
5. This single test saves enormous time by splitting hardware from software immediately.

### Fix 2: Turn off Filter Keys and Sticky Keys

1. Go to **Settings > Accessibility > Keyboard**.
2. Turn **off** Sticky Keys, Filter Keys, and Toggle Keys.
3. Uncheck "Allow the shortcut key to start Filter Keys" to prevent accidental re-enabling via the Shift-hold shortcut.
4. Test typing immediately — Filter Keys is the #1 "my keyboard is broken" false alarm.
5. Also check **Settings > Time & language > Typing** for anything odd like aggressive autocorrect interfering.

### Fix 3: Test the keyboard in BIOS

1. Restart and enter BIOS/UEFI (F2/Del) — try typing in any BIOS text field or navigating menus.
2. Keyboard works in BIOS but not Windows: 100% a Windows driver/software problem. Skip hardware fixes.
3. Keyboard dead in BIOS too: hardware problem — ribbon cable, keyboard unit, or motherboard connector.
4. This test is definitive because BIOS doesn't use Windows drivers at all.
5. Note the result; it determines whether the remaining steps are software or hardware.

### Fix 4: Reinstall the keyboard driver

1. Open Device Manager, expand **Keyboards**.
2. Right-click the internal keyboard (usually "Standard PS/2 Keyboard") and choose **Uninstall device**.
3. Restart — Windows reinstalls the driver automatically at boot.
4. If the keyboard is missing from Device Manager entirely, click **Action > Scan for hardware changes**, and check **View > Show hidden devices**.
5. Also update chipset drivers from your laptop manufacturer's support page — the internal keyboard connects through the chipset.
6. Touchpad issues often share the same driver root; see [Synaptics touchpad fixes](/articles/how-to-fix-synaptics-touchpad-not-working-reddit/) if both input devices misbehave.
7. If the keyboard works in Safe Mode but not normally, a startup program is intercepting input — clean-boot to find it.

### Fix 5: Clean under the keys and check for stuck keys

1. Turn the laptop off, tilt it, and shake gently — crumbs fall out surprisingly often.
2. Use compressed air at an angle under the keycaps, not straight down.
3. Look for physically stuck keys: a key held down (even slightly) can block the entire keyboard's input.
4. Press every key firmly once to unstick any that are lodged.
5. For liquid spills: power off immediately, disconnect power, and let it dry for 48 hours — corrosion continues while wet.

### Fix 6: Reseat the keyboard ribbon cable

1. This requires opening the laptop — only attempt if you're comfortable and the warranty allows.
2. Power off, disconnect the charger, and remove the bottom panel (check a teardown video for your exact model).
3. Find the keyboard's flat ribbon cable connecting to the motherboard; flip up the locking tab, reseat the cable fully, and lock it.
4. Ribbon cables work loose from heat cycling and drops — reseating fixes many "died suddenly" cases.
5. If you're not comfortable opening the laptop, this is a quick, cheap service-center job — describe it as a suspected loose keyboard cable.

### Fix 7: Eliminate software interference

1. Uninstall or disable keyboard macro tools, remappers (AutoHotkey scripts, SharpKeys), and "gaming" keyboard utilities.
2. Perform a clean boot (msconfig > hide Microsoft services > disable all) and test typing.
3. Check for malware — keyloggers and some malware families interfere with keyboard input.
4. Run `sfc /scannow` to repair corrupted Windows input components.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has additional hardware troubleshooter steps if the problem persists.
6. If a clean boot fixes it, re-enable startup items in halves to identify the interfering program.

## Closing

Keyboard failure looks catastrophic but diagnoses fast: external keyboard test, BIOS test, Filter Keys check — three steps that take five minutes and pinpoint the cause with near certainty. Software causes (Filter Keys, drivers) fix in minutes; hardware causes (ribbon cable, keyboard unit) are among the cheapest laptop repairs there is. The mistake is assuming the worst before testing. Test first, then fix the thing that's actually broken, and keep a cheap USB keyboard in a drawer — it's the fastest diagnostic tool you own. If an external keyboard stutters too, the issue is system-wide input handling rather than the laptop keyboard — [keyboard fixes for Windows 11](/articles/how-to-fix-keyboard-not-working-on-laptop-on-windows-11/) approach it from that angle.
