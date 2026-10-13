---
title: "Keyboard Not Working on Your Laptop? What to Do"
slug: what-to-do-if-keyboard-not-working-on-laptop
date: 2026-09-27
categories: ["drivers"]
tags: ["keyboard not working", "laptop keyboard", "keys not typing", "keyboard driver"]
description: "Laptop keyboard not typing? Learn what to do when keys stop working — from filter keys and driver fixes to external keyboard tests."
thumbnail: "/images/thumbs/what-to-do-if-keyboard-not-working-on-laptop.webp"
faqs:
  - q: "What should I do first when my laptop keyboard stops working?"
    a: "First, determine the scope: do no keys work, or only some? Then plug in a USB keyboard — if it works, Windows is healthy and the fault is the laptop's keyboard or its driver. Check Filter Keys in Accessibility settings, which silently swallows keystrokes, and reboot. Those three steps (scope, USB test, Filter Keys) diagnose most cases in minutes."
  - q: "Why do some keys work but others do not?"
    a: "Partial failure usually means hardware: a damaged keyboard matrix row, debris under specific keys, or liquid damage to one zone. Software (drivers, Filter Keys) tends to affect the whole keyboard or specific functions, not random individual keys. If the same keys fail in the BIOS and a Linux live USB, the keyboard hardware is at fault — pop off a keycap and look for debris or corrosion."
  - q: "Can a driver update break the laptop keyboard?"
    a: "Yes, though it is less common than with touchpads or WiFi. A corrupted keyboard filter driver (often from third-party utilities) or a failed chipset update can stop keystrokes reaching Windows. Reinstalling the keyboard device and the chipset driver in Device Manager resolves the software side. If an external USB keyboard works fine, the OS input stack is healthy."
  - q: "What are Filter Keys and why do they break typing?"
    a: "Filter Keys is an accessibility feature that ignores brief or repeated keystrokes, designed for users with tremors. When enabled accidentally (holding Shift for 8 seconds triggers the prompt), typing feels broken — keys seem dead or repeat oddly. Turning it off in Settings > Accessibility > Keyboard instantly restores normal typing. It is one of the most common 'keyboard broken' false alarms."
---

A keyboard that will not type is uniquely paralyzing — every fix seems to need the keyboard you do not have. But the diagnosis does not: the on-screen keyboard (Win+Ctrl+O) covers input needs, and the fault splits cleanly into scope questions. All keys dead points at drivers, settings, or the whole keyboard; some keys dead points at the keyboard matrix or debris; USB keyboard works points away from Windows entirely.

This guide runs that diagnosis first, then the fixes in order: the settings traps, the driver layer, the BIOS, and finally the hardware. Keep the on-screen keyboard handy and work top to bottom.

## Why this happens

- **Filter Keys enabled accidentally**, swallowing keystrokes.
- **Keyboard driver corrupted** or blocked by a bad filter driver.
- **Chipset driver failed**, breaking the keyboard's bus interface.
- **Keyboard disabled in Device Manager** or by a utility.
- **Liquid damage or debris** killing individual keys or zones.
- **Ribbon cable loose** after drops or battery swelling.
- **Third-party keyboard utilities** intercepting all input.
- **BIOS-level failure** where even firmware setup gets no keys.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Scope the fault with a USB keyboard

Plug in a USB keyboard (or open the on-screen keyboard with Win+Ctrl+O for navigation). If the USB keyboard types fine, Windows' input stack is healthy and the fault is the laptop's keyboard hardware or its driver — continue with this guide. If the USB keyboard also fails, the problem is OS-level: jump to the driver and settings fixes. Also note exactly which keys fail on the laptop keyboard: everything dead versus a dead zone tells hardware from software later. The [keyboard troubleshooting hub](/articles/keyboard-not-working-on-laptop-troubleshooting/) organizes these branches.

1. Plug in a USB keyboard and test typing.
2. USB works = laptop keyboard/driver fault; continue here.
3. USB fails too = OS-level fault; focus on drivers/settings.
4. Note whether all keys or only some keys fail.

### Fix 2: Turn off Filter Keys and Sticky Keys

Open Settings > Accessibility > Keyboard (navigate with the on-screen keyboard or USB keyboard) and turn off Filter Keys, Sticky Keys, and Toggle Keys. Filter Keys is the notorious one — holding the right Shift for eight seconds enables it via a popup, and then keystrokes feel dead or delayed. This single settings page resolves a remarkable number of 'keyboard stopped working' reports with zero driver involvement. Also dismiss any stuck Ease of Access prompts that may be intercepting input. Microsoft's keyboard guidance is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Settings > Accessibility > Keyboard.
2. Turn off Filter Keys, Sticky Keys, and Toggle Keys.
3. Dismiss any accessibility popups intercepting keys.
4. Test typing immediately.

### Fix 3: Reinstall the keyboard and chipset drivers

In Device Manager, uninstall the keyboard device (Standard PS/2 Keyboard or HID Keyboard Device) and reboot — Windows rediscovers it. If that fails, the deeper fix is the chipset driver: the keyboard's controller lives on the platform bus, so reinstall the chipset driver from the laptop maker's support page for your exact model. Also check Human Interface Devices for flagged entries from keyboard utilities and uninstall those. Function-key-specific failures have their own diagnostics in the [function-key guide](/articles/how-to-fix-function-keys-not-working-in-windows-11-24h2/).

1. Uninstall the keyboard device in Device Manager and reboot.
2. Reinstall the chipset driver from the laptop maker.
3. Clear flagged HID entries from keyboard utilities.
4. Test the laptop keyboard after each step.

### Fix 4: Remove interfering keyboard software

Third-party tools that hook the keyboard — AutoHotkey scripts, PowerToys Keyboard Manager, gaming macro software, some VPN clients' filters — can swallow all input when they malfunction. Boot into Safe Mode: if the keyboard works there, a startup program is the culprit. Use msconfig to clean-boot, re-enabling items in halves until the keyboard dies again — the last enabled half contains the offender. Uninstall or update it. This binary search takes twenty minutes and definitively identifies software interference.

1. Boot into Safe Mode and test the keyboard.
2. If it works there, clean-boot with msconfig.
3. Re-enable startup items in halves to find the offender.
4. Uninstall or update the interfering software.

### Fix 5: Test in the BIOS

Reboot and try the keyboard in the BIOS/UEFI setup — navigate menus, change a harmless setting. Keys working in the BIOS but not Windows convicts the Windows driver stack: return to Fix 3 and also try System Restore to before the failure. Keys dead in the BIOS too means the fault is at or below the firmware: the keyboard hardware, its cable, or the embedded controller. No Windows reinstall fixes a keyboard the BIOS cannot see, so this test decides whether software effort continues.

1. Reboot into the BIOS/UEFI setup.
2. Test navigation keys in the BIOS menus.
3. Works in BIOS = Windows software fault; revisit drivers.
4. Dead in BIOS = hardware or embedded-controller fault.

### Fix 6: Clean under the keys and check for damage

For partial failures — specific dead keys or a dead zone — power down and inspect. Pop off a suspect keycap gently and look for debris, crumbs, or corrosion; clean with compressed air and a dry swab. Consider liquid history honestly: even a small spill months ago corrodes the matrix traces progressively. If a whole row or column is dead, the matrix trace for that line is broken — sometimes repairable by cleaning the ribbon connector, usually requiring keyboard replacement. The [step-by-step keyboard guide](/articles/how-to-fix-keyboard-not-working-on-laptop-step-by-step/) details keycap removal per type.

1. Power down and pop off a suspect keycap carefully.
2. Clear debris and clean contacts with dry air/swab.
3. Note row/column patterns indicating matrix damage.
4. Consider any liquid-spill history.

### Fix 7: Reseat the cable or replace the keyboard

For a fully dead laptop keyboard that fails the BIOS test, the ribbon cable connecting it to the board is the next check — drops and battery swelling loosen it. Opening the bottom cover to reseat the cable is moderate difficulty; HP, Lenovo, and Dell publish service manuals per model. If reseating fails, the keyboard itself is bad: replacement keyboards are model-specific and inexpensive, though some ultrabooks fuse the keyboard into the top case (making it a bigger job). Get a quote before ordering — a shop replaces most laptop keyboards in under an hour.

1. Open the bottom cover per the model's service manual.
2. Reseat the keyboard ribbon cable firmly.
3. Test before reassembling fully.
4. Replace the keyboard or get a repair quote.

## Closing

Keyboard failures reward the scope-first diagnosis: the USB keyboard test splits Windows from hardware in seconds, the BIOS test splits drivers from the keyboard itself, and the all-keys versus some-keys question splits settings from matrix damage. Most 'dead keyboard' cases are Filter Keys, a wedged driver, or a meddling utility — all software, all fixable without parts. The hardware cases announce themselves clearly (dead in BIOS, dead zones, spill history) and have a fixed remedy in the cable or the replacement keyboard. Keep the on-screen keyboard shortcut (Win+Ctrl+O) memorized; it turns a keyboard emergency from a crisis into a methodical repair.
