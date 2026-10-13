---
title: "Fix a Laptop Keyboard That Has Stopped Typing"
slug: how-to-fix-keyboard-not-working-on-laptop
date: 2026-09-24
categories: ["drivers"]
tags: ["laptop keyboard", "keyboard not working", "driver fix", "windows 11", "troubleshooting"]
description: "A dead laptop keyboard is usually a driver, filter, or ribbon-cable issue. Follow this technician-grade flow to diagnose and fix a keyboard that won't type."
thumbnail: "/images/thumbs/how-to-fix-keyboard-not-working-on-laptop.webp"
faqs:
  - q: "Why did my laptop keyboard suddenly stop working?"
    a: "The most common triggers are a failed keyboard driver update, the filter-keys accessibility setting silently turning on, a stuck Fn lock, or the internal ribbon cable working loose. Software causes account for the majority of cases and can be ruled out in minutes before you suspect hardware."
  - q: "Should I use an external keyboard as a test?"
    a: "Yes. If a USB keyboard types normally while the built-in one is dead, the operating system and its input stack are fine, which narrows the fault to the built-in keyboard's driver or hardware. If neither works, suspect a Windows-level input problem instead."
  - q: "Can a Windows update break the keyboard?"
    a: "Absolutely. Keyboard drivers ship through Windows Update, and a bad or mismatched driver package can disable the built-in keyboard overnight. Rolling back the driver in Device Manager is the fastest fix, and it works in the majority of update-related cases."
  - q: "When is it time to replace the keyboard?"
    a: "When the keyboard fails in BIOS or UEFI setup too, no software fix will help because the hardware itself is unreachable. If the ribbon cable is seated correctly and external keyboards work, the keyboard assembly needs replacement. Replacement keyboards are model-specific and usually inexpensive — just confirm the BIOS failure first, since no new keyboard will fix a driver problem."
---

A laptop keyboard that stops typing mid-sentence feels like a catastrophe, but the cause is rarely as dramatic as it seems. In most cases I see, the hardware is perfectly fine — a Windows update, a flipped accessibility setting, or a corrupted keyboard driver has simply cut the connection between the keys and the operating system. The good news is that software causes can be eliminated in about fifteen minutes, and even some hardware causes are fixable without a repair shop.

Work through this guide like a technician: start with the zero-effort checks, move to driver-level repairs, and only open the chassis if everything else points at a physical fault. Each step tells you something, so don't skip ahead.

## Why this happens

- **Corrupted keyboard driver:** The PS/2 or HID keyboard driver can fail after a Windows update, a failed driver install, or a power glitch during boot.
- **Filter Keys silently enabled:** Holding the right Shift key for eight seconds can turn on Filter Keys, which makes the keyboard ignore brief keystrokes and look dead.
- **Fn lock or language layout change:** Some keys may appear broken when the keyboard layout switched (for example, to a different language) or when Fn lock remaps the top row.
- **Fast Startup holding a bad state:** Windows Fast Startup saves driver states between boots, so a one-time driver failure can persist across restarts.
- **Loose internal ribbon cable:** The keyboard connects to the motherboard through a thin ribbon cable that can creep loose from heat cycles, drops, or past servicing.
- **Liquid or debris under keys:** Even a few drops of liquid can bridge traces on the keyboard membrane; crumbs can wedge keys physically down.
- **BIOS-level hardware failure:** A failed keyboard controller or damaged membrane won't work even in BIOS setup, which rules out every software fix.
- **USB power or hub conflicts:** On some models, an overloading USB device or a docking station can interfere with the internal keyboard's power rail during boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out the quick toggles

1. Press and hold **Shift** for eight seconds. If you hear a beep or see a Filter Keys prompt, turn **Filter Keys off** in **Settings → Accessibility → Keyboard**.
2. Check the taskbar language indicator (ENG or similar). If it changed, press **Windows + Space** to cycle back to your layout.
3. Try **Fn + Esc** (or the dedicated Fn-lock key on your model) to release any stuck function lock.
4. Test typing in Notepad. If some keys now work, the keyboard itself is alive and you have a settings problem.

### Fix 2: Test with an external keyboard

1. Plug in any USB keyboard and type for a minute.
2. If the external keyboard works perfectly, your Windows input stack is healthy — the fault is isolated to the built-in keyboard's driver or hardware.
3. If neither keyboard works, suspect a Windows-level issue (Fix 4 and Fix 5) rather than the laptop keyboard itself.
4. Keep the USB keyboard handy: you'll need it to navigate while the built-in keyboard is down.

### Fix 3: Restart the keyboard driver without rebooting

1. Press **Windows + X** and open **Device Manager**.
2. Expand **Keyboards**, right-click the built-in keyboard (usually "Standard PS/2 Keyboard" or "HID Keyboard Device"), and choose **Uninstall device**.
3. Restart the laptop. Windows reinstalls a clean copy of the keyboard driver during boot.
4. This single step resolves the largest share of post-update keyboard failures because it discards the corrupted driver state entirely. For related peripheral driver recovery, see our guide on [fixing function keys](/articles/how-to-fix-function-keys-not-working-on-windows-11/).

### Fix 4: Roll back a bad driver update

1. In **Device Manager → Keyboards**, right-click the keyboard and open **Properties → Driver**.
2. If **Roll Back Driver** is clickable, select it and choose a reason — this restores the previous working version.
3. If the button is greyed out, the driver was replaced rather than updated; use **Update driver → Browse my computer → Let me pick** and choose an older listed version.
4. Restart and test before letting Windows Update touch the driver again.

### Fix 5: Disable Fast Startup to clear the stuck state

1. Open **Control Panel → Power Options → Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully (not restart), wait ten seconds, and power on.
4. A true cold boot reloads every driver from scratch, which clears faults that Fast Startup's hibernated state keeps alive.

### Fix 6: Boot into BIOS to separate hardware from software

1. Restart and press the BIOS key for your brand (F2, F10, Del, or Esc) during the logo screen.
2. Try the arrow keys and Enter inside BIOS setup.
3. If the keyboard works in BIOS but not in Windows, the hardware is fine — focus entirely on driver and OS fixes.
4. If it fails in BIOS too, no Windows repair will help: skip to Fix 7 or plan for replacement.

### Fix 7: Reseat the keyboard ribbon cable (advanced)

1. Power off, unplug, and remove the battery if it is removable.
2. Follow your model's service manual to remove the bottom cover and locate the keyboard ribbon connector.
3. Flip up the connector's locking latch, slide the cable fully out, blow out any dust, reinsert it squarely, and lock the latch.
4. Reassemble and test. This resolves keyboards that died after a drop or a previous repair, and it takes about twenty minutes with the right screwdriver. For a broader walkthrough of keyboard-side failures beyond the ribbon cable, see our [keyboard troubleshooting guide](/articles/keyboard-not-working-on-laptop-troubleshooting/).

### Fix 8: Block Windows from reinstalling the bad driver

1. After you have a working driver, open **Settings → Windows Update → Advanced options → Optional updates** and uncheck any keyboard driver offers.
2. For persistent cases, use the **Show or hide updates** troubleshooter to hide the offending driver package.
3. Microsoft documents current known input issues on the [Windows support site](https://support.microsoft.com/en-us/windows), which is worth checking before each monthly update cycle.

## Closing

Keyboard failures look frightening but surrender quickly to methodical diagnosis: external keyboard test, driver reinstall, rollback, cold boot, BIOS check, and only then the ribbon cable. Most keyboards come back at Fix 3 or Fix 4. If yours works in BIOS but not in Windows, you will win this fight — it's just a matter of finding which driver state is stuck.
