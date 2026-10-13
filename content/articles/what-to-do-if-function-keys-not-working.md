---
title: "What to Do When Function Keys Stop Working on Your Laptop"
slug: "what-to-do-if-function-keys-not-working"
date: "2026-09-16"
categories: ["drivers"]
tags: ["function keys", "fn key", "keyboard", "bios", "windows 11"]
description: "Function keys dead on your laptop? Learn how Fn lock, BIOS action-key settings, and missing OEM utilities cause the problem, and fix them step by step."
thumbnail: "/images/thumbs/what-to-do-if-function-keys-not-working.webp"
faqs:
  - q: "Why did my F1 to F12 keys suddenly stop working?"
    a: "The usual causes are Fn lock being toggled on, a BIOS setting that swapped the keys to media functions, a Windows update that broke the keyboard driver, or a missing manufacturer utility. Press Fn + Esc to toggle Fn lock first. If that fails, check the BIOS for an Action Keys or Function Key Behavior option."
  - q: "What is Fn lock and how do I turn it off?"
    a: "Fn lock swaps whether the F1 to F12 keys perform their standard functions or the printed media actions like volume and brightness. On most laptops, Fn + Esc toggles it, sometimes with an on-screen indicator or a light on the Esc key. Some brands use Fn + Caps Lock or a dedicated Fn lock key instead."
  - q: "Can a BIOS setting disable my function keys?"
    a: "Yes. Most laptops have a BIOS option called Action Keys Mode, Function Key Behavior, or Hotkey Mode that decides whether F1 to F12 act as standard function keys or media keys by default. Changing this in the BIOS is the permanent fix if Fn lock keeps resetting after every reboot."
  - q: "Do I need manufacturer software for function keys to work?"
    a: "Often yes. The special Fn combinations for brightness, airplane mode, and keyboard backlight are handled by utilities like Lenovo Vantage, HP Hotkey Support, Dell QuickSet, or ASUS Armoury Crate. If those utilities are missing or broken after a Windows reinstall, the Fn combinations stop working even though the basic keys are fine."
---

You press F5 to refresh a page and instead the keyboard backlight dims. Or you press Fn + F5 and nothing happens at all. Function key problems are rarely about broken hardware; they are about layers of settings that decide what those twelve keys actually do.

Those layers are: Fn lock state, a BIOS option that sets the default behavior, the keyboard driver, and the manufacturer's utility software that handles the special combinations. A change in any one of them, often triggered by a Windows update, can silently remap your entire top row. For keys that do nothing at all, also see our [keyboard troubleshooting guide](/articles/how-to-fix-keyboard-not-working-on-laptop-in-windows-11-24h2/).

The fixes below start with the instant Fn lock toggle and move down through the BIOS and software layers. Most people are fixed by step two.

## Why this happens

- **Fn lock is toggled on:** The keys are sending media commands instead of F1 to F12, or the reverse, depending on the lock state.
- **The BIOS action-keys setting flipped:** A BIOS update or reset can change whether F1 to F12 default to standard or media functions.
- **The manufacturer utility is missing or broken:** Fn combinations for brightness and backlight depend on OEM software that Windows updates can remove.
- **A corrupted keyboard driver:** The standard PS/2 or HID keyboard driver can break after major Windows updates.
- **Filter Keys or Sticky Keys interference:** Accessibility features can change how key combinations register.
- **A stuck Fn key:** A physically stuck Fn key inverts every function key press until it is released.
- **Fast Startup holding a bad state:** Windows Fast Startup can preserve a broken keyboard state across reboots.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle Fn lock with the keyboard shortcut

This is the fix for the majority of cases. Fn lock determines whether the top row sends F1 to F12 codes or the printed media actions, and it is easy to trigger accidentally.

1. Press Fn + Esc together and watch for an on-screen Fn lock indicator.
2. Test the F1 to F12 keys in an application that uses them, such as F5 in a browser.
3. If Fn + Esc does nothing, try Fn + Caps Lock or look for a dedicated Fn lock key.
4. Check whether the Esc key has a small lock light that changes state.
5. If the toggle works but resets after reboot, move on to the BIOS fix below.

### Fix 2: Change the function key behavior in the BIOS

The BIOS setting is the permanent version of Fn lock. Setting it to Function Key first makes F1 to F12 behave as standard function keys without holding Fn, which is what most desktop converts expect.

1. Restart the laptop and enter the BIOS with F2, F10, Delete, or Esc.
2. Find Advanced, Configuration, or System Setup, then locate Action Keys Mode, Function Key Behavior, or Hotkey Mode.
3. Set it to Disabled or Function Key first for standard F1 to F12 behavior.
4. Save and exit, usually with F10.
5. Boot into Windows and confirm the keys behave as expected without holding Fn.

### Fix 3: Reinstall the keyboard driver

If the keys register the wrong codes or nothing at all, the keyboard driver may be corrupt. Reinstalling it takes two minutes and fixes driver-level remapping issues.

1. Open Device Manager and expand Keyboards.
2. Right-click the Standard PS/2 Keyboard or HID Keyboard Device and choose Uninstall device.
3. Restart the laptop; Windows will reinstall the driver automatically.
4. Test all twelve function keys plus several Fn combinations.
5. If problems persist, check Windows Update for an optional keyboard driver from your manufacturer.

### Fix 4: Install or repair the manufacturer's utility software

The Fn combinations for brightness, volume, airplane mode, and backlight are not standard keyboard functions; they are handled by OEM utilities. After a clean Windows install or a major update, these utilities are often missing.

1. Identify your brand's utility: Lenovo Vantage, HP Hotkey Support, Dell QuickSet or Dell Peripheral Manager, ASUS Armoury Crate, or Acer Quick Access.
2. Download it from the official support page, such as https://support.lenovo.com/us/en/ for Lenovo systems.
3. Install the utility and restart the laptop.
4. Open the utility and check its keyboard or hotkey settings for anything disabled.
5. Test the Fn combinations for brightness, volume, and backlight control.

### Fix 5: Check accessibility settings for interference

Sticky Keys and Filter Keys change how the keyboard interprets presses and modifier combinations. They are sometimes enabled accidentally through repeated Shift presses.

1. Open Settings, then Accessibility, then Keyboard.
2. Turn off Sticky Keys, Filter Keys, and Toggle Keys.
3. If a shortcut prompt appears when pressing Shift five times, decline it.
4. Test the function keys again with all three features disabled.
5. Microsoft documents these features at https://support.microsoft.com/en-us/windows if you need them for accessibility and want to configure exceptions.

### Fix 6: Disable Fast Startup to clear a stuck keyboard state

Fast Startup saves the kernel and driver state to disk instead of fully shutting down. If the keyboard driver entered a bad state, Fast Startup will faithfully restore that bad state on every boot.

1. Open Control Panel, go to Power Options, and click Choose what the power buttons do.
2. Click Change settings that are currently unavailable.
3. Uncheck Turn on fast startup and save the changes.
4. Shut down the laptop completely, wait ten seconds, and power it on.
5. Test the function keys on the fresh boot. You can re-enable Fast Startup later if you prefer.

### Fix 7: Rule out a physically stuck Fn key

It sounds too simple, but a Fn key stuck in the pressed position inverts every function key and can even interfere with other shortcuts. Crumbs and debris are the usual culprits.

1. Press the Fn key several times firmly to unstick it.
2. Inspect around the key for crumbs or debris and clean with compressed air.
3. Open the on-screen keyboard (Windows + Ctrl + O) and watch whether Fn appears highlighted without being touched.
4. If the key is physically damaged, an external USB keyboard is a practical workaround.
5. For persistent hardware faults, follow our general advice on [keeping drivers current](/articles/how-to-update-drivers-on-windows-11-laptop/) and contact the manufacturer's repair service.

## Closing

Function key issues are settings problems wearing a hardware disguise. The Fn + Esc toggle and the BIOS action-keys option resolve the overwhelming majority of cases, with the manufacturer utility covering the special Fn combinations. Only when keys register nothing at all across every layer should you start suspecting the keyboard hardware itself.
