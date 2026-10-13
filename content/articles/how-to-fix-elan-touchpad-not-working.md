---
title: "How to Fix an ELAN Touchpad Not Working"
slug: how-to-fix-elan-touchpad-not-working
date: 2026-09-14
categories: ["drivers"]
tags: ["elan", "touchpad", "not working", "windows 11"]
description: "ELAN touchpad dead after a Windows update? Fix driver, settings, and BIOS issues with this ELAN-specific troubleshooting guide."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working after a Windows update?"
    a: "Windows Update frequently replaces the ELAN driver with a generic Microsoft PS/2 mouse driver that lacks the ELAN functionality, or installs an incompatible ELAN version. The touchpad may move the cursor but lose gestures, or stop entirely. Reinstalling the ELAN driver from your laptop manufacturer's support page restores full function in most cases."
  - q: "What is the difference between ELAN and Synaptics touchpads?"
    a: "They are competing touchpad hardware and driver platforms used by different laptop manufacturers — ELAN (Elan Microelectronics) and Synaptics each make the controller chip and its driver. The troubleshooting is similar, but you must install the correct manufacturer's driver: an ELAN driver will not work on Synaptics hardware and vice versa."
  - q: "My ELAN touchpad works but gestures don't — why?"
    a: "Basic cursor movement works through the generic PS/2 mouse driver, but multi-finger gestures, scrolling, and tapping require the full ELAN driver and its control panel. Installing the proper ELAN driver from the laptop maker and enabling gestures in Settings > Bluetooth & devices > Touchpad restores the advanced features."
  - q: "Can a BIOS setting disable my ELAN touchpad?"
    a: "Yes. Many laptops have a BIOS option for the touchpad (often under Advanced or Device Configuration) that can be set to disabled, and BIOS updates occasionally reset it. There is also commonly an Fn-key toggle (like Fn+F5) that disables the touchpad at the hardware level — check both before assuming a driver problem."
---

ELAN touchpads are everywhere — ASUS, Lenovo, Acer, MSI, and many others use Elan Microelectronics controller chips — and they have a well-earned reputation for breaking after Windows updates. The pattern is so consistent it is almost a tradition: update installs, touchpad dies or loses its gestures, and the fix is reinstalling the correct ELAN driver. But updates are not the only cause, and this guide covers the full ELAN-specific checklist: the Fn-key trap, the BIOS setting, the driver dance, and the settings that silently disable the pad.

One ELAN quirk worth knowing upfront: Windows loves replacing the ELAN driver with its generic PS/2 mouse driver. The touchpad then "works" just enough to move the cursor, which convinces people the driver is fine while gestures, scrolling, and tap-to-click stay dead. If your cursor moves but nothing else works, you are almost certainly running the generic driver. For the Synaptics equivalent, see our [Synaptics touchpad fix guide](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/), and for brand-agnostic touchpad troubleshooting, the [general touchpad guide](/articles/touchpad-not-working-troubleshooting/).

## Why this happens

- **Windows replaced the ELAN driver.** Updates install the generic Microsoft PS/2 driver, killing ELAN-specific functions.
- **Fn-key touchpad toggle.** An accidental Fn+F-key press disables the touchpad at the hardware level.
- **Touchpad disabled in BIOS.** A BIOS setting or a reset after an update can turn the touchpad off in firmware.
- **Touchpad disabled in Settings.** Windows Settings has its own touchpad toggle that updates and accidental clicks can flip.
- **Corrupted ELAN driver installation.** Partial updates leave the driver in a broken state.
- **Palm rejection too aggressive.** Overzealous palm detection can make the touchpad seem dead while typing or with certain hand positions.
- **Hardware failure.** The ribbon cable connecting the touchpad can loosen, particularly after drops or repairs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the Fn-key toggle and Settings switch

The two fastest checks, and embarrassingly common culprits.

1. Look for a touchpad icon on your function keys (often **F5**, **F6**, **F7**, or **F9**) and press **Fn + that key** to toggle the touchpad. Try it twice to make sure you end in the enabled state.
2. Open **Settings > Bluetooth & devices > Touchpad** and confirm the **Touchpad** toggle is **On**.
3. While there, check **Cursor speed** is not set to minimum (which can feel like a dead pad) and that **Taps** settings match your expectations.
4. If the touchpad settings page is missing entirely, Windows is using the generic driver — skip to Fix 3.

### Fix 2: Verify the touchpad is enabled in BIOS

Firmware-level disable overrides everything in Windows.

1. Restart and enter the BIOS (**F2**, **Delete**, or **Esc** depending on brand).
2. Look under **Advanced**, **Devices**, or **Main** for **Touchpad**, **Internal Pointing Device**, or **PS/2 Mouse** — set it to **Enabled**.
3. Save and exit, then test in Windows. If the BIOS shows it enabled already, the problem is in Windows — continue below.

### Fix 3: Reinstall the correct ELAN driver

The core fix for most ELAN failures.

1. Open Device Manager, expand **Mice and other pointing devices** (or **Human Interface Devices**), and check what driver is listed. **PS/2 Compatible Mouse** means the generic driver is in use — that is your problem.
2. Download the **ELAN touchpad driver** for your exact model from your laptop manufacturer's official support page — for Dell, HP, or Lenovo machines start at [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
3. Uninstall the current pointing device driver in Device Manager (check **Attempt to remove the driver**), restart, then install the downloaded ELAN package.
4. After installation, verify **ELAN** or **ELAN Input Device** appears in Device Manager and that the full **Touchpad** settings page with gesture options appears in Windows Settings.

### Fix 4: Roll back a bad driver update

If the touchpad died right after an update, undo it.

1. In Device Manager, right-click the touchpad device, choose **Properties > Driver tab**, and click **Roll Back Driver** if available.
2. If rollback is greyed out, manually install the previous ELAN version from the manufacturer's driver archive.
3. After recovery, consider pausing driver updates (**Settings > Windows Update > Advanced options**) until you have a known-good ELAN version installed.
4. Note the working driver version somewhere — ELAN regressions recur, and knowing your good version saves time next update.

### Fix 5: Adjust palm rejection and sensitivity

For touchpads that work intermittently or seem dead while typing.

1. Open **Settings > Bluetooth & devices > Touchpad** and set **Touchpad sensitivity** to **High sensitivity** or **Most sensitive** as a test.
2. If your ELAN control panel is available (often in **Control Panel > Mouse > ELAN** tab), reduce **PalmTracking** or palm rejection sensitivity.
3. Test typing while touching the pad — if the pad only dies while typing, palm rejection was the cause, and you can tune it to a middle ground rather than disabling it.
4. Also check the ELAN tab for a **Disable when external USB mouse is plugged in** option — uncheck it if you use both.

### Fix 6: Check for conflicting software

Something else may be grabbing the touchpad.

1. Uninstall or disable any third-party touchpad utilities you installed (some "touchpad blocker" apps conflict with the ELAN driver).
2. Boot into **Safe Mode** and test the touchpad. If it works in Safe Mode, a startup program is interfering — use **msconfig** to disable startup items selectively.
3. Check **Task Manager > Startup** for mouse/touchpad-related utilities from other manufacturers and disable them.

### Fix 7: Inspect the hardware connection

The last resort for a pad that survives no software fix.

1. If the touchpad is not detected in Device Manager at all (even as an unknown device) and the BIOS shows it enabled, the ribbon cable may have loosened.
2. On out-of-warranty laptops you are comfortable opening, reseat the touchpad's ribbon cable on the motherboard — these are fragile ZIF connectors, so research your model's disassembly first.
3. If reseating does not help, the touchpad module itself may have failed — replacement modules are model-specific and usually inexpensive, but installation difficulty varies widely.

## Closing

ELAN touchpad failures follow a script: check the Fn key, check the Settings toggle, then reinstall the proper ELAN driver from the laptop maker — that sequence resolves the overwhelming majority of cases, including the classic post-update death. The generic PS/2 driver masquerading as a working touchpad is the trap to watch for: cursor movement without gestures means the real driver is missing. Only when Device Manager cannot see the device at all, across drivers and BIOS checks, should you suspect the ribbon cable or the hardware itself.
