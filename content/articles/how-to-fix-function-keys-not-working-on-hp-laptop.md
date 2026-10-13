---
title: "HP Laptop Function Keys Not Working? How to Fix Them"
slug: how-to-fix-function-keys-not-working-on-hp-laptop
date: 2026-10-11
categories: ["drivers"]
tags: ["function keys", "hp laptop", "fn key", "keyboard driver", "action keys"]
description: "Function keys not working on your HP laptop? Fix them by toggling Action Keys mode in BIOS, reinstalling the keyboard driver, and checking HP utilities."
thumbnail: "/images/thumbs/how-to-fix-function-keys-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why do my function keys do the wrong thing on my HP laptop?"
    a: "HP's Action Keys mode swaps the default behavior: with it on, F1-F12 perform their printed actions (volume, brightness) without Fn, and you need Fn for classic F-key functions. If the behavior feels inverted, the mode is simply set opposite to what you expect — toggle it in BIOS or with Fn + Esc."
  - q: "What does Fn + Esc do on an HP laptop?"
    a: "It toggles Action Keys mode on most HP models. A lock icon with 'fn' appears on the Esc key. Pressing Fn + Esc switches whether F1-F12 act as function keys or action keys by default. It is the fastest fix when the keys seem backwards."
  - q: "Can a driver update break the function keys?"
    a: "Yes. The HP System Event Utility and the keyboard driver translate Fn combinations into actions. If Windows Update replaced these with generic versions, special keys stop responding. Reinstalling the HP System Event Utility and chipset drivers from HP support restores them."
  - q: "Do function keys work in BIOS if Windows is the problem?"
    a: "They should. The BIOS setup screen uses raw keyboard input independent of Windows drivers. If F-keys work in BIOS but not in Windows, the problem is software — drivers or utilities. If they fail in BIOS too, you likely have a hardware keyboard issue."
---

Press F5 to refresh a page and your HP laptop mutes the speakers instead. Or you hammer Fn + F11 for brightness and nothing happens at all. Function key problems on HP laptops are rarely hardware failures — they are almost always a mode setting, a missing utility, or a driver that Windows replaced.

HP handles function keys differently from most brands. A firmware feature called Action Keys mode decides whether F1 through F12 behave as classic function keys or as media and system shortcuts by default, and the Fn key flips whichever behavior is active. Layered on top is the HP System Event Utility, a background program that translates those key presses into on-screen actions.

This guide fixes HP function keys in the right order: the instant Fn + Esc toggle, the BIOS Action Keys setting, the HP utilities and drivers, and finally hardware checks. Most people are fixed by step two.

## Why this happens


- **Action Keys mode set opposite to expectation:** The firmware default makes F-keys act as media keys; users expecting classic F-key behavior think the keys are broken.
- **HP System Event Utility missing or broken:** This background utility translates Fn combinations. Without it, special keys do nothing even though the keyboard works.
- **Generic keyboard driver after an update:** Windows Update can replace HP's keyboard driver with a generic HID driver that lacks Fn-combination support.
- **Fn lock stuck in one state:** The Fn lock toggle can get stuck, inverting every F-key press until toggled back.
- **BIOS update resetting Action Keys:** Firmware updates occasionally restore factory defaults, flipping Action Keys mode without warning.
- **Filter Keys intercepting presses:** Windows accessibility's Filter Keys can swallow repeated or brief key presses, making function keys feel dead.
- **Third-party keyboard managers conflicting:** Remapping tools and some gaming overlays intercept function keys before HP's utility sees them.
- **Hardware keyboard fault:** Liquid damage or a failing keyboard ribbon cable can kill specific rows — but this is the least common cause by far.

## How to fix it


Work through these in order — diagnose first, then act.

### Fix 1: Try the Fn + Esc toggle first


This single keystroke fixes the majority of 'my function keys do the wrong thing' reports on HP laptops. It flips Action Keys mode instantly with no restart required.

1. Locate the Esc key — on most HP laptops it carries a small 'fn' lock icon.
2. Press Fn + Esc together.
3. Look for an on-screen notification confirming Function key lock on or off.
4. Test F1-F12 both with and without holding Fn.
5. If the keys now behave as you expect, you are done — this was a mode issue, not a fault.

### Fix 2: Set Action Keys mode in BIOS


If the toggle does not stick or you want the permanent default changed, the BIOS setting is the authoritative control. This is also the fix when Fn + Esc does nothing at all.

1. Restart the laptop and press F10 repeatedly during boot to enter BIOS Setup.
2. Go to the Advanced tab, then Device Options or System Configuration (varies by model).
3. Find Action Keys Mode.
4. Set it to Enabled if you want F1-F12 to act as media/action keys by default, or Disabled for classic function-key behavior.
5. Press F10 to save and exit, then test in Windows.

### Fix 3: Reinstall HP System Event Utility


When Fn combinations produce no on-screen response — no volume overlay, no brightness change — the System Event Utility is usually missing or crashed. This HP-specific program is what turns those key presses into actions.

1. Open Settings, Apps, Installed apps and look for HP System Event Utility.
2. If present, uninstall it, then restart.
3. Visit [HP support](https://support.hp.com/us-en), enter your exact model, and download the HP System Event Utility plus the chipset driver.
4. Install the chipset driver first, restart, then install the System Event Utility.
5. Test Fn + F-key combinations and confirm the on-screen overlays appear.

### Fix 4: Fix the keyboard driver in Device Manager


A generic driver can handle typing fine while dropping all Fn combinations. Reinstalling the proper keyboard driver restores the full key map.

1. Press Windows + X and open Device Manager.
2. Expand Keyboards, right-click your keyboard device, and choose Uninstall device (do not check driver removal unless reinstalling from HP).
3. Restart — Windows reinstalls the keyboard driver automatically.
4. If Fn keys still fail, right-click the keyboard, choose Update driver, then Search automatically for drivers.
5. For stubborn cases, download the keyboard/input driver from HP support for your exact model and install it manually.

### Fix 5: Check Filter Keys and Sticky Keys


Windows accessibility features can silently eat function key presses. Filter Keys in particular ignores brief or repeated keystrokes, which makes F-keys feel intermittently dead.

1. Open Settings, Accessibility, Keyboard.
2. Turn off Sticky Keys, Filter Keys, and Toggle Keys.
3. Also check that Use Fn key behavior or similar vendor options are not conflicting.
4. Test the function keys again immediately — this fix is instant, no restart needed.

### Fix 6: Test in BIOS and try an external keyboard


This is the hardware verdict. If function keys work in BIOS setup but not Windows, the problem is 100% software. If an external USB keyboard's F-keys work fine, your built-in keyboard may have a hardware fault.

1. Restart, enter BIOS with F10, and confirm navigation keys respond there.
2. Plug in any USB keyboard and test its F1-F12 keys in Windows.
3. If the USB keyboard works but the built-in one does not, back up your data and contact HP support about a keyboard replacement.
4. If neither works in Windows but BIOS is fine, perform a clean boot (msconfig, disable non-Microsoft services) to find conflicting software.
5. Related key and input issues are covered in our [Lenovo function keys guide](/articles/how-to-fix-function-keys-not-working-on-lenovo-laptop/) and [Dell function keys guide](/articles/how-to-fix-function-keys-not-working-on-dell-laptop/).

## Closing


HP function key problems are configuration problems wearing a hardware disguise. The Fn + Esc toggle and the BIOS Action Keys setting resolve the vast majority of cases in under two minutes; the System Event Utility covers most of the rest. Only when keys fail in BIOS too should you start thinking about a replacement keyboard.
