---
title: "Best Way to Fix USB Ports Not Working on a Windows 11 Laptop"
slug: best-way-to-fix-usb-ports-not-working
date: 2026-10-01
categories: ["drivers"]
tags: ["usb ports not working", "fix usb ports", "usb controller driver", "usb power drain", "windows 11"]
description: "The best way to fix USB ports not working: a ranked repair sequence — power drain, controller reinstall, power-management fixes, and hardware checks."
thumbnail: "/images/thumbs/best-way-to-fix-usb-ports-not-working.webp"
faqs:
  - q: "What is the single best fix for dead USB ports?"
    a: "The full power drain: shut down completely, unplug everything including the AC adapter, hold the power button for 30 seconds, then boot with only AC connected. This resets the embedded controller that manages USB power and resolves the majority of all-ports-dead cases in about a minute. If that fails, reinstalling the USB controllers in Device Manager is the next best step."
  - q: "Why do USB ports fail after Windows updates?"
    a: "Windows Update replaces USB host controller and chipset drivers with versions that are sometimes incompatible with your specific hardware, or it resets USB selective suspend settings. The pattern — everything worked yesterday, dead today — is the signature. Rolling back the USB controller driver or reinstalling the chipset driver from the laptop maker's site fixes it."
  - q: "Should I disable USB selective suspend permanently?"
    a: "If your ports have a history of dying after idle or sleep, yes — disabling it costs a negligible amount of battery and eliminates an entire class of failures. Set it to Disabled in the advanced power plan settings for both battery and plugged-in states. It is one of the highest-value preventive tweaks for USB reliability on laptops."
  - q: "How do I know if a USB port is physically broken?"
    a: "Physical damage affects one port while the others work fine. Look inside with a flashlight for bent pins, a loose or wobbly connector housing, or debris. A port that works only when you hold the cable at an angle has a cracked solder joint or worn pins. Single-port failures with visible damage are hardware — no driver fix will help."
---

Not all USB fixes are equal, and trying them in random order wastes the afternoon. This guide ranks the repairs by effectiveness — the fixes that resolve the most cases with the least effort come first, and each step includes the diagnostic read that tells you whether to continue or stop. The ranking comes from the failure pattern data: controller lockups and driver corruption cause the overwhelming majority of USB port deaths, physical damage is a distant third, and true motherboard failure is rare.

Before starting, note your pattern: all ports dead, one port dead, or ports dying after idle. That single observation determines which fixes matter for you.

## Why this happens

- **Embedded-controller lockup.** The power-management chip hangs; a drain resets it — most common all-ports cause.
- **USB controller driver corruption.** Usually triggered by Windows Update replacing a working driver.
- **USB selective suspend.** Power-saving that disables idle ports and sometimes never re-enables them.
- **Overcurrent protection tripped.** A faulty peripheral shorting the bus and shutting ports down.
- **BIOS USB settings changed.** Firmware updates occasionally resetting USB configuration.
- **Physically damaged port.** Bent pins or broken solder — single-port failures.
- **Motherboard controller failure.** Rare — diagnosed only by eliminating everything else.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: The full power drain (best first step)

Highest success rate per minute spent of any USB fix.

1. Shut down **completely** — hold Shift while clicking Shut down to bypass fast startup.
2. Unplug the AC adapter, **every** USB device, and any dock.
3. Press and hold the power button for a full **30 seconds**.
4. Connect only the AC adapter and power on.
5. Test with a simple USB device (wired mouse) in each port.
6. If ports return, reconnect peripherals **one at a time** — the one that kills them again is shorted and is your real culprit.

The pattern-reading approach here mirrors the systematic method in [USB ports not working troubleshooting](/articles/usb-ports-not-working-troubleshooting/).

### Fix 2: Reinstall the entire USB controller stack

The best driver-level fix — rebuilds what updates break.

1. **Device Manager > Universal Serial Bus controllers** — note any yellow warnings first.
2. Right-click each **USB Root Hub** and **USB Host Controller** → **Uninstall device**. Do all of them.
3. If your keyboard/mouse are USB, they'll die mid-process — that's expected; use the laptop's built-in keyboard/trackpad.
4. **Restart.** Windows redetects the hardware and rebuilds the USB stack from scratch.
5. Test every port with a known-good device.
6. This is the definitive fix for "worked yesterday, dead after an update" cases.

### Fix 3: Kill USB selective suspend permanently

The best preventive fix for ports that die after idle.

1. Control Panel → Power Options → Change plan settings → **Change advanced power settings**.
2. Expand **USB settings** → **USB selective suspend setting** → set to **Disabled** for both On battery and Plugged in.
3. In Device Manager, for each **USB Root Hub** → Properties → **Power Management** → uncheck "Allow the computer to turn off this device to save power."
4. Disable **fast startup** (Power Options → Choose what the power buttons do) so bad USB power states don't survive shutdowns.
5. The battery cost of these changes is negligible; the reliability gain is substantial.

### Fix 4: Roll back or refresh the chipset driver

For update-caused failures that a reinstall doesn't fix.

1. In Device Manager, open the **USB Host Controller** → Driver tab → **Roll Back Driver** if the option is available.
2. Download the **chipset driver** from your laptop maker's support page — USB controllers are part of the chipset package.
3. Install it over the current driver and restart.
4. Intel users can also run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to refresh chipset components.
5. After stabilizing, consider [blocking automatic driver updates](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) so Windows doesn't reinstall the broken version.

### Fix 5: Hunt the shorted peripheral

When ports die the moment something is plugged in.

1. With all ports working (after Fix 1 or 2), plug devices back **one at a time**, testing ports after each.
2. The device that kills the ports has an internal short — inspect its cable for fraying, especially near connectors.
3. Check Device Manager for **Unknown USB Device (Port Reset Failed)** — it names the offending port.
4. Look inside each port with a flashlight for bent pins, staples, or debris causing shorts.
5. Retire or repair the faulty peripheral — repeatedly tripping overcurrent protection stresses the controller.

Related device-level detection issues are covered in [how to fix a USB device not recognized after a Windows 11 update](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/).

### Fix 6: Reset BIOS USB configuration

For ports dead even in BIOS, or after firmware updates.

1. Enter **BIOS/UEFI** and find **USB Configuration**.
2. Ensure USB ports, USB controller, and legacy USB support are all **Enabled**.
3. Choose **Load Optimized Defaults**, save, and exit — this clears corrupted USB firmware settings.
4. Update the **BIOS** from the manufacturer's support page if a newer version lists USB fixes.
5. Recheck ports in BIOS with a USB keyboard before booting Windows — working here but not in Windows means the OS stack (Fix 2), not firmware.

### Fix 7: Judge the hardware honestly

The final assessment.

1. **One dead port, others fine, visible damage** → physical repair or a hub workaround; no software fix applies.
2. **Port works only at an angle** → cracked solder joint or worn pins — a shop can resolder it.
3. **All ports dead in BIOS after drain + defaults** → controller or motherboard failure — professional diagnosis.
4. Workaround that lasts: a **powered USB hub** on any working port, or a Thunderbolt dock if those ports are alive.
5. If the laptop is under warranty and multiple ports are dead without visible damage, file a claim — that's a board-level defect.

## Closing

Ranked by results, USB repair is: power drain first (a minute, fixes most), controller-stack reinstall second (fixes update damage), selective-suspend disable third (prevents recurrence), then the peripheral hunt and BIOS reset. Physical damage announces itself by affecting one port while its neighbors work — everything else is software or power state, and software loses to the sequence above. Do the drain before anything else; it's the highest-yield sixty seconds in laptop troubleshooting.
