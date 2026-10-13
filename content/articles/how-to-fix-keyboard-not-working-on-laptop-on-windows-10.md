---
title: "Keyboard Not Working on Windows 10 Laptop? Work Through These Fixes"
slug: how-to-fix-keyboard-not-working-on-laptop-on-windows-10
date: 2026-09-11
categories: ["drivers"]
tags: ["laptop keyboard", "windows 10", "keyboard driver", "filter keys"]
description: "Laptop keyboard dead on Windows 10? From Filter Keys to driver reinstalls to ribbon-cable reseats, this guide walks you through every fix in the right order."
thumbnail: "/images/thumbs/how-to-fix-keyboard-not-working-on-laptop-on-windows-10.webp"
faqs:
  - q: "Why would the whole keyboard die at once on Windows 10?"
    a: "Whole-keyboard failure is almost always software on Windows 10: Filter Keys enabled by accident, a corrupted PS/2 keyboard driver after an update, or the device disabled in Device Manager. Hardware failures usually kill individual keys or rows first. The BIOS test — keys working in setup but not Windows — confirms software within two minutes."
  - q: "How do I type if the keyboard doesn't work at all?"
    a: "Use the on-screen keyboard: press Windows key plus Ctrl plus O, or go to Settings, then Ease of Access, then Keyboard, and turn on the on-screen keyboard. A USB keyboard is the better workaround — it uses a separate driver path and works even when the internal keyboard is completely dead."
  - q: "What is Filter Keys and why does it kill my keyboard?"
    a: "Filter Keys is an Ease of Access feature that tells Windows to ignore brief or repeated keystrokes. Holding the right Shift key for eight seconds enables it, and suddenly every keypress seems ignored. Disable it in Settings, then Ease of Access, then Keyboard. It is the most common cause of a suddenly dead laptop keyboard."
  - q: "Can a Windows 10 update break the keyboard driver?"
    a: "Yes. Feature and cumulative updates can corrupt the Standard PS/2 Keyboard driver or leave it in a bad state preserved by Fast Startup. Uninstalling the keyboard in Device Manager and restarting forces a clean reinstall, and disabling Fast Startup prevents the corrupted state from surviving reboots."
---

You press the power button, the Windows 10 login screen appears, and the keyboard does nothing. No password entry, no response in any app. The touchpad works, an external mouse works — but the built-in keyboard is completely inert.

On Windows 10 this is a well-trodden problem with a well-trodden fix order. Total failure points to software — Filter Keys, the PS/2 keyboard driver, or Fast Startup preserving a corrupted driver state — far more often than to hardware. The two-minute BIOS test splits the problem cleanly: keys work in BIOS setup means Windows is at fault; keys dead in BIOS means hardware. (On Windows 11 the same logic applies with slightly different screens — see our [Windows 11 keyboard guide](/articles/how-to-fix-keyboard-not-working-on-laptop-on-windows-11/).)

## Why this happens

- **Filter Keys enabled accidentally.** Eight seconds on the Shift key enables it and keystrokes get swallowed.
- **Corrupted PS/2 keyboard driver.** A Windows 10 update damaged the standard keyboard driver.
- **Fast Startup preserving bad state.** Hybrid shutdown carries the corrupted driver state across every reboot.
- **Keyboard disabled in Device Manager.** Disabled during troubleshooting or by an update and never re-enabled.
- **Sticky Keys interfering.** Another Ease of Access feature changing how keypresses register.
- **Third-party keyboard software conflicting.** Remapping or macro utilities hooking the keyboard stack.
- **Ribbon cable loosened.** Physical connector between keyboard and motherboard unseated by impact or heat.
- **Liquid damage.** Spills corrode the key matrix; severe damage kills the whole board.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off Filter Keys and Sticky Keys

Open **Settings > Ease of Access > Keyboard** and make sure both **Filter Keys** and **Sticky Keys** are off. Filter Keys is the classic culprit — it ignores brief keystrokes, which reads as a dead keyboard. If holding Shift for eight seconds previously triggered the Filter Keys prompt, that confirms the diagnosis. Test in Notepad immediately after disabling. Also uncheck "allow the shortcut key to start Filter Keys" to prevent it from happening again.

### Fix 2: Test in the BIOS

Restart and tap **F2**, **Del**, **F1**, or your brand's key during boot to enter BIOS/UEFI setup. Try the arrow keys and Enter. Working keys here means the hardware is fine and Windows 10 is the problem — proceed with the software fixes. Dead keys here means hardware — jump to Fix 6. This test takes two minutes and prevents hours of wasted driver troubleshooting on a physically broken keyboard. If the touchpad is misbehaving too, our [Synaptics touchpad repair guide](/articles/how-to-fix-synaptics-touchpad-not-working-on-windows-10/) covers that hardware — many laptops share one internal cable assembly for keyboard and touchpad, so dual failures point at the cable.

### Fix 3: Reinstall the keyboard driver

Open **Device Manager** (press **Windows + X**, then M — or use the on-screen keyboard via **Windows + Ctrl + O**), expand **Keyboards**, right-click **Standard PS/2 Keyboard**, and choose **Uninstall device**. Restart the laptop; Windows reinstalls the driver during boot. If the keyboard entry showed a yellow warning icon, this reinstall is very likely the fix. Microsoft's official driver troubleshooting steps are documented at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows). If the keyboard section is empty, click **Action > Scan for hardware changes** first — the device may simply need redetection.

### Fix 4: Disable Fast Startup and do a full shutdown

Fast Startup is the reason corrupted keyboard driver state survives reboots on Windows 10. Go to **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**, click **Change settings that are currently unavailable**, and uncheck **Turn on fast startup (recommended)**. Then **Shut down** fully (not Restart), wait ten seconds, and power on. This cold boot forces complete driver reinitialization. If the keyboard returns after this, Fast Startup was preserving the broken state — leave it off.

### Fix 5: Clean boot to find software conflicts

Press **Windows + R**, type `msconfig`, and press Enter. On the **Services** tab, check **Hide all Microsoft services**, then **Disable all**. On the **Startup** tab, open Task Manager and disable all startup items. Restart. If the keyboard works in this clean state, re-enable items in halves to find the conflicting program — keyboard remappers, macro tools, and some "gaming" utilities hook the keyboard stack and can wedge it. Safe Mode loads only Microsoft's own drivers, so a keyboard that works there but not in normal mode proves a third-party driver or startup program is the culprit rather than Windows itself. Uninstall or update the culprit once identified.

### Fix 6: Reseat the keyboard ribbon cable

For a BIOS-dead keyboard, the ribbon cable is the next suspect. Power off, unplug, remove the battery if possible, and open the bottom panel (only if out of warranty and you are comfortable). Find the wide flat ribbon cable from the keyboard to the motherboard, release its locking tab, slide it out, inspect the contacts, reseat it firmly, and lock the tab. Reassemble and test. A cable loosened by a drop is a common cause of sudden total failure, and reseating costs nothing.

### Fix 7: Replace the keyboard assembly

If reseating fails and the BIOS test was negative, the keyboard hardware has failed. Order a replacement keyboard by exact laptop model — they are model-specific and inexpensive for most machines. Some laptops have easily swapped keyboards (screws under the battery or bezel); others rivet the keyboard into the top case, making replacement a shop job. Meanwhile, a USB keyboard is a complete workaround — it uses a separate driver stack and is unaffected by the internal keyboard's failure. For driver-level issues that persist, a Windows 10 in-place repair install rebuilds the input stack as a final software step.

## Closing

Windows 10 keyboard death is a software problem until the BIOS test proves otherwise — Filter Keys, driver reinstall, and Fast Startup cover the vast majority of cases. If the BIOS test fails, reseat the ribbon cable before spending money on parts. Either way, a USB keyboard in the drawer turns this from an emergency into a scheduled repair.
