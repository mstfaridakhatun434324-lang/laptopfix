---
title: "Keyboard Not Working on Your Laptop in Windows 11? Diagnose and Fix It"
slug: how-to-fix-keyboard-not-working-on-laptop-on-windows-11
date: 2026-09-09
categories: ["drivers"]
tags: ["laptop keyboard", "windows 11", "keyboard driver", "keys not working"]
description: "Your laptop keyboard stopped typing in Windows 11? Rule out filter keys and driver faults first, then work through hardware checks with this technician's guide."
thumbnail: "/images/thumbs/how-to-fix-keyboard-not-working-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why did my laptop keyboard stop working suddenly?"
    a: "Sudden total keyboard failure is usually software: Filter Keys got enabled accidentally, the keyboard driver corrupted after an update, or the keyboard device is disabled in Device Manager. Hardware failure tends to kill individual keys first, not the whole keyboard at once. Check the software causes before assuming the keyboard is dead."
  - q: "What are Filter Keys and how do I turn them off?"
    a: "Filter Keys is an accessibility feature that ignores brief or repeated keystrokes — holding Shift for eight seconds enables it accidentally, making the keyboard seem dead. Turn it off in Settings, then Accessibility, then Keyboard, by disabling Filter Keys. It is the single most common cause of a suddenly unresponsive laptop keyboard."
  - q: "Can I test whether it's hardware or software?"
    a: "Yes. Restart and try the keyboard in the BIOS or UEFI setup — if keys work there but not in Windows, the problem is software (drivers or settings). If keys fail in the BIOS too, it is hardware. The on-screen keyboard (Windows key plus Ctrl plus O) also lets you keep working while you diagnose."
  - q: "Will an external USB keyboard work as a workaround?"
    a: "Almost always yes. USB keyboards use a completely separate driver path from the internal keyboard, so they keep working when the laptop keyboard fails. Keep one handy during troubleshooting — you will need it to type commands and navigate Device Manager while the internal keyboard is down."
---

Every key dead at once. You open the laptop, type your password — nothing. The touchpad moves the cursor, the screen is fine, but the keyboard might as well be a picture of a keyboard. Before panic sets in: total keyboard failure on a laptop is usually software, and software can be fixed.

The diagnostic question is simple — do the keys work outside Windows? If yes, you are fighting a driver or settings problem. If no, it is the keyboard hardware or its ribbon cable. Either way there is a path forward, and a cheap USB keyboard keeps you productive while you work it. (On Windows 10, the screens differ slightly — see our [Windows 10 keyboard guide](/articles/how-to-fix-keyboard-not-working-on-laptop-on-windows-10/) for that version.)

## Why this happens

- **Filter Keys enabled accidentally.** Holding Shift for eight seconds turns on this accessibility feature, which swallows keystrokes.
- **Keyboard driver corrupted.** A Windows update damaged the standard PS/2 keyboard driver.
- **Keyboard disabled in Device Manager.** The device got disabled during troubleshooting or by an update.
- **Wrong input language selected.** The keyboard types, but produces unexpected characters — a language bar issue, not dead keys.
- **Fast Startup holding bad state.** Hybrid shutdown preserves a corrupted keyboard driver state across reboots.
- **BIOS keyboard setting changed.** Rare, but firmware updates can toggle the internal keyboard.
- **Ribbon cable loosened.** Drops and thermal cycling unseat the keyboard's internal connector.
- **Liquid damage or key matrix failure.** Spills kill rows or columns of keys; full-board failure follows severe damage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out Filter Keys

Press and hold the right **Shift** key for eight seconds — if you hear a beep and see a Filter Keys dialog, that was your problem. Go to **Settings > Accessibility > Keyboard** and make sure **Filter Keys** is off. Also check **Sticky Keys** while you are there. Filter Keys makes the keyboard ignore brief keystrokes, which feels exactly like a dead keyboard, and it gets enabled accidentally more often than anyone admits. Test typing in Notepad after disabling it.

### Fix 2: Test the keyboard outside Windows

Restart and press **F2**, **Del**, or your brand's BIOS key repeatedly during boot. If you can navigate the BIOS menus with the arrow keys, the keyboard hardware works and Windows is the problem — continue with the software fixes. If the BIOS does not respond to keys either, skip to the hardware fixes (Fix 6 and 7). Also try the **Windows recovery environment**: hold **Shift** while clicking Restart, and test keys in the recovery menus. This two-minute test tells you which half of the guide applies to you.

### Fix 3: Reinstall the keyboard driver

Open **Device Manager** (right-click Start — or use the on-screen keyboard with **Windows + Ctrl + O** to navigate), expand **Keyboards**, right-click **Standard PS/2 Keyboard**, and choose **Uninstall device**. Do not check any driver-deletion box. Restart — Windows reinstalls the keyboard driver during boot. If the device shows a yellow warning instead, the driver is corrupted and this reinstall is exactly the fix. If the keyboard is missing from Device Manager entirely, click **Action > Scan for hardware changes**. Microsoft's driver troubleshooting guidance is at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 4: Disable Fast Startup

Fast Startup preserves driver state across shutdowns, which means a corrupted keyboard driver state survives every "restart." Go to **Control Panel > Power Options > Choose what the power buttons do**, click **Change settings that are currently unavailable**, and uncheck **Turn on fast startup**. Then do a full **Shut down** (not restart), wait ten seconds, and power on. This forces Windows to initialize the keyboard driver completely fresh. If the keyboard works after this but failed before, Fast Startup was preserving the broken state.

### Fix 5: Check language, layout, and run the troubleshooter

If keys type but produce wrong characters, click the language indicator in the taskbar and switch back to your layout — Windows 11's **Windows + Space** shortcut changes layouts accidentally. Then run the keyboard troubleshooter: **Settings > System > Troubleshoot > Other troubleshooters > Keyboard**. It checks the driver binding and common misconfigurations automatically. Also test in Safe Mode (hold Shift while restarting, then Troubleshoot > Startup Settings) — if the keyboard works in Safe Mode but not normally, a startup program or third-party driver is interfering.

### Fix 6: Reseat the keyboard ribbon cable

If the BIOS test failed, the problem is hardware. For laptops with removable keyboards or accessible internals (and out of warranty): power off, disconnect the charger and battery, remove the bottom panel, and locate the keyboard's ribbon cable where it meets the motherboard. Flip up the locking tab, slide the cable out, inspect for damage, slide it firmly back in, and lock the tab. Ribbon cables loosened by drops or heat are a classic cause of sudden total keyboard death. Reassemble and test.

### Fix 7: Replace the keyboard or use external options

If reseating does not help and the BIOS test failed, the keyboard assembly itself has failed — liquid damage, a cracked matrix, or controller failure. Replacement keyboards for most laptops cost modestly and are model-specific; order by exact model number from the manufacturer or a reputable parts supplier. Power-related input failures are a separate category worth ruling out — our guide on [driver power state failures](/articles/driver-power-state-failure-windows-11-fix/) covers those. Meanwhile, a USB keyboard works indefinitely as a stopgap, and the on-screen keyboard (**Windows + Ctrl + O**) covers emergencies.

## Closing

A dead laptop keyboard is a software problem until the BIOS test says otherwise. Check Filter Keys, reinstall the driver, kill Fast Startup — those three fix the large majority of cases. If the hardware test fails, reseat the ribbon cable before ordering parts. And keep a ten-dollar USB keyboard in a drawer; it turns a crisis into an inconvenience. Document which fix worked so the next failure takes minutes, not hours. A short note in your phone — "keyboard died, Fix 4, Fast Startup off" — is worth more than any amount of re-diagnosis.
