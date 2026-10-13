---
title: "Function Keys Not Working? Diagnose and Repair Them"
slug: troubleshoot-function-keys-not-working
date: 2026-09-06
categories: ["drivers"]
tags: ["function keys not working", "fn key", "hotkeys", "keyboard driver"]
description: "Laptop function keys dead or doing the wrong thing? Diagnose Fn lock, driver, and BIOS causes and restore your hotkeys on Windows 11."
thumbnail: "/images/thumbs/troubleshoot-function-keys-not-working.webp"
faqs:
  - q: "Why do my function keys do media controls instead of F1-F12?"
    a: "Your laptop is in media-key mode, where the top row defaults to brightness and volume instead of F1 through F12. Press Fn + Esc (the Fn Lock toggle on most brands) to switch back, or change the default in BIOS under Function Key Behavior. This is a mode setting, not a malfunction."
  - q: "What is Fn Lock and how do I toggle it?"
    a: "Fn Lock switches the top row between standard F1-F12 functions and the printed media/hotkey functions. On most laptops, Fn + Esc toggles it, sometimes with an on-screen indicator or a lock light on the Esc key. Some brands use Fn + Caps Lock or a BIOS setting instead — check your manual for the exact combo."
  - q: "Why do only some function keys work?"
    a: "Partial failure usually means the hotkey driver or utility is missing while basic keyboard input works. Volume and brightness keys often depend on the manufacturer's hotkey software, while F1-F12 themselves are handled by the BIOS. Reinstalling the maker's hotkey/ATK package typically restores the dead keys."
  - q: "Can a Windows update break function keys?"
    a: "Yes. Updates can replace the manufacturer's hotkey driver with a generic keyboard driver that doesn't implement the Fn combinations, or reset the BIOS-adjacent settings the keys depend on. Reinstalling the hotkey utility from the laptop maker's support page is the standard fix after an update breaks them."
---

Function keys misbehaving usually means one of two things: they're doing the "wrong" action (media controls instead of F1-F12), or some of them do nothing at all. The first is a mode setting. The second is a driver or utility problem. Both are fixable without opening the laptop, and this guide separates the two cases so you apply the right fix.

Start by pressing a top-row key alone, then with Fn held. If the key works with Fn but not without it, you're in media-key mode — that's Fix 1 and you're done in ten seconds. If keys do nothing in either combination, continue through the driver fixes. Our companion guide covers [function keys that refuse to respond](/articles/how-do-i-fix-function-keys-not-working/) with a fix-first approach.

## Why this happens

- **Media-key mode active:** The top row defaults to brightness/volume functions instead of F1-F12.
- **Fn Lock toggled accidentally:** Fn + Esc (or similar) was pressed unknowingly, flipping the row's behavior.
- **Missing hotkey driver:** The manufacturer's hotkey/ATK utility isn't installed, so Fn combinations do nothing.
- **Windows Update replaced the driver:** A generic keyboard driver overwrote the maker's hotkey implementation.
- **BIOS function-key behavior setting:** The BIOS default for the top row was changed, often by a BIOS update.
- **Third-party keyboard software conflicts:** Remapping tools or gaming software intercept the function row.
- **Fast Startup stale state:** A corrupted keyboard driver state persists across hybrid shutdowns.
- **Hardware failure of the row:** Liquid damage or a damaged keyboard ribbon affects the top row specifically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle Fn Lock and check the mode

Press Fn + Esc and watch for an on-screen indicator or a light change on the Esc key — this toggles Fn Lock on most Dell, HP, and Lenovo laptops. Test the top row after toggling. On some ASUS models the combo is Fn + F-something specific, and on Lenovos there's often a dedicated FnLk key. If toggling switches behavior between F1-F12 and media keys, the keys were never broken — just in the other mode. Decide which mode you prefer and leave it there.

1. Press Fn + Esc and watch for an indicator.
2. Test the top row keys alone afterward.
3. Try Fn + the key to confirm both modes work.
4. Check your manual if Fn + Esc does nothing.
5. Leave the row in whichever mode you prefer.

### Fix 2: Set the default behavior in BIOS

Restart into BIOS setup and look for "Function Key Behavior," "Action Keys Mode," or similar under Advanced or System Configuration. Set it to "Function Key" if you want F1-F12 as the default, or "Multimedia Key" if you prefer brightness/volume without Fn. Save and exit. This sets the hardware-level default that applies before Windows even loads, so it's the most durable fix for mode confusion — it survives driver changes and updates.

1. Restart into BIOS setup.
2. Find Function Key Behavior or Action Keys Mode.
3. Choose Function Key or Multimedia Key as your default.
4. Save with F10 and boot into Windows.
5. Verify the top row behaves as configured.

### Fix 3: Reinstall the manufacturer's hotkey utility

The Fn combinations for brightness, volume, airplane mode, and similar are implemented by maker software (ASUS ATK Package, Lenovo Hotkeys, Dell QuickSet, HP Hotkey Support). Download the latest version for your exact model from the maker's support site — [Lenovo's support site](https://support.lenovo.com/us/en/) or [Dell's support portal](https://www.dell.com/support). Uninstall the old version first, reboot, install fresh, reboot again. This restores keys that do nothing at all, including update-related breakage like [function keys failing after a Windows 11 update](/articles/how-to-fix-function-keys-not-working-in-windows-11-24h2/).

1. Identify your maker's hotkey utility name.
2. Download the latest version for your exact model.
3. Uninstall the old version in Settings, Apps.
4. Reboot, install the fresh package, reboot again.
5. Test every Fn combination.

### Fix 4: Check the keyboard driver in Device Manager

Open Device Manager, expand Keyboards, and check the entries. If you see a warning icon, uninstall the keyboard device and reboot — Windows reinstalls the standard driver. If the keyboard uses a maker-specific driver, reinstall it from the support page. Also check Human Interface Devices for hotkey-related entries with errors. Avoid installing random "keyboard driver updater" tools; the standard Windows driver plus the maker's hotkey utility is the correct stack, and Microsoft's support pages cover the keyboard troubleshooting basics.

1. Open Device Manager and expand Keyboards.
2. Uninstall any keyboard entry showing a warning.
3. Reboot and let Windows reinstall the driver.
4. Check Human Interface Devices for hotkey errors.
5. Reinstall the maker's keyboard driver if one exists.

### Fix 5: Remove conflicting keyboard software

Keyboard remappers (SharpKeys, PowerToys Keyboard Manager), gaming peripheral software (Razer Synapse, Logitech G Hub), and macro tools can intercept the function row. Temporarily disable or uninstall them and test the keys. If function returns, re-add your customizations carefully, excluding the top row. Also check for "gaming mode" toggles in peripheral software that disable Windows-key and function-key combinations. Test with a clean boot if you're unsure which program is responsible.

1. Disable keyboard remapping and macro tools temporarily.
2. Check gaming software for gaming-mode key blocking.
3. Uninstall or reconfigure the conflicting program.
4. Use a clean boot to isolate unknown culprits.
5. Retest the full function row.

### Fix 6: Disable Fast Startup and test in BIOS

A corrupted keyboard driver state can survive hybrid shutdowns. Disable Fast Startup in Power Options (uncheck "Turn on fast startup"), then shut down fully and cold-boot. Separately, test the function keys inside the BIOS setup itself — most BIOS screens respond to F-keys for navigation. If function keys work in BIOS but not in Windows, the fault is 100% software (drivers/utilities). If they fail in BIOS too, you're looking at hardware.

1. Disable Fast Startup in Power Options.
2. Shut down fully and cold-boot.
3. Enter BIOS setup and test F-keys for navigation.
4. Working in BIOS but not Windows means software fault.
5. Failing in BIOS too means hardware fault — see Fix 7.

### Fix 7: Rule out hardware damage

If the top row fails even in BIOS, inspect for liquid damage — spills love the top keyboard row — and check whether an external USB keyboard's function keys work (they should, proving Windows itself is fine). A damaged internal keyboard ribbon or membrane requires keyboard replacement; on many laptops the keyboard is a replaceable module, on others it's riveted to the palm rest and the repair is bigger. Get a quote before assuming the worst — but believe the BIOS test.

1. Test function keys in BIOS to confirm hardware fault.
2. Verify an external USB keyboard's function row works.
3. Inspect for liquid damage around the top row.
4. Check the service manual for keyboard replacement difficulty.
5. Get a repair quote for the keyboard module.

## Closing

Function key problems are mode settings or missing utilities far more often than broken keyboards. The Fn + Esc toggle and the BIOS behavior setting resolve the "wrong action" cases instantly; the maker's hotkey utility reinstall fixes the "dead key" cases. Only when keys fail inside the BIOS itself should you start thinking about hardware — everything else is software, and software can be fixed.
