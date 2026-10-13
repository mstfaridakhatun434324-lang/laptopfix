---
title: "How to Fix USB Device Not Recognized After a Windows 11 Update"
slug: how-to-fix-usb-device-not-recognized-after-windows-11-update
date: 2026-09-29
categories: ["drivers"]
tags: ["usb device not recognized", "usb malfunctioned", "usb driver", "windows 11 update"]
description: "USB device not recognized after a Windows 11 update? Six fixes for the 'USB device malfunctioned' error, from hub power resets to chipset driver repair."
thumbnail: "/images/thumbs/how-to-fix-usb-device-not-recognized-after-windows-11-update.webp"
faqs:
  - q: "What does 'USB device not recognized' / 'the last USB device you connected malfunctioned' mean?"
    a: "It means the USB device announced itself on the bus but the enumeration handshake failed — Windows couldn't read its descriptors or match a driver, so it gave up and flagged the port. The device might be fine; the failure is in the handshake. Common triggers after an update: a replaced USB host controller driver, power management cutting the port mid-handshake, or a corrupted driver for that specific device class."
  - q: "The device works on another computer. Does that rule out the device?"
    a: "Mostly yes — it proves the device's hardware and firmware are functional, which points the finger at your laptop's USB stack: the host controller driver, hub power delivery, or the device's Windows driver. The one exception is power-hungry devices that work on a desktop's beefier ports but fail on a laptop's power-limited ones — in that case a powered hub is the fix, not a driver."
  - q: "Can a Windows update break just one USB port?"
    a: "It can appear that way: updates can change power management per-port or break the driver for a specific hub while others keep working. But true single-port failure is more often hardware — a damaged port or its power delivery. Test the device in every port: if it fails everywhere, it's the stack; if it fails in one port only, inspect that port for physical damage and suspect hardware."
  - q: "Should I uninstall all USB controllers in Device Manager?"
    a: "It's a legitimate last-resort fix — Windows rebuilds the entire USB stack on reboot — but do it carefully: uninstall the USB host controllers (not the keyboard/mouse if they're USB, or you'll lose input until reboot). Save your work first, since you'll need to restart immediately. Try the gentler fixes in this guide first; the full-stack rebuild is for when individual hub resets haven't worked."
---

You plug in the flash drive, phone, or peripheral, and Windows 11 pops up "USB device not recognized" — or the device appears in Device Manager as "Unknown USB Device (Device Descriptor Request Failed)." It worked before the update. The device works on other computers. So the problem is your laptop's USB stack, and on Windows 11 24H2 that stack has several update-sensitive layers: the host controller driver, hub power management, and the device-class driver.

The error message is actually informative if you read it technically: "device descriptor request failed" means the handshake died at step one — Windows asked the device "who are you?" and got garbage or silence. That points at power, the controller driver, or the cable — not at the device's function driver, which never even got involved. We'll work from the port up through the stack. Thunderbolt/USB4 devices have their own additional layer — if that's your device, the [Thunderbolt fix guide](/articles/how-to-fix-thunderbolt-not-working-on-laptop-in-windows-11-24h2/) covers it.

## Why this happens

- **The USB host controller driver broke in the update.** The 24H2 upgrade replaced the xHCI controller driver with a build that mishandles enumeration on your chipset.
- **USB selective suspend starves the handshake.** Power management cuts power to the port mid-enumeration, so the descriptor request fails.
- **The hub needs a power reset.** The USB hub's internal state wedged during the update; it needs a full power cycle, not just a reboot.
- **The device's own driver is corrupt or mismatched.** The update replaced the function driver (for the printer, phone, audio interface) with a broken build.
- **Fast Startup preserved the broken USB state.** Hibernation-style shutdowns carry the wedged controller state across reboots.
- **The cable or port can't deliver stable power.** Marginal cables and worn ports cause exactly the intermittent descriptor failures this error describes.
- **Too many bus-powered devices.** The port's power budget is exceeded, and the new device can't complete enumeration on the available current.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Power-cycle the USB hardware properly

Clear the wedged hub state that reboots don't touch.

1. Unplug ALL USB devices from the laptop (every single one).
2. Shut down fully — hold **Shift** while clicking **Shut down** to bypass Fast Startup.
3. Unplug the charger, hold the power button for 30 seconds, then reconnect the charger and boot.
4. Plug in only the problem device, directly (no hub), and test. This resolves a large share of post-update USB failures.

### Fix 2: Disable USB selective suspend

Stop power management from killing the handshake.

1. **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings**.
2. Expand **USB settings** > **USB selective suspend setting** > set to **Disabled** for both On battery and Plugged in.
3. In Device Manager > **Universal Serial Bus controllers**, right-click each **USB Root Hub** > **Properties** > **Power Management** tab — uncheck **Allow the computer to turn off this device to save power**.
4. Restart and test the device.

### Fix 3: Uninstall the failed device entry and rescan

Force a clean re-enumeration.

1. With the device plugged in, open Device Manager and find the **Unknown USB Device (Device Descriptor Request Failed)** entry.
2. Right-click > **Uninstall device**, then unplug the device.
3. Click **Action** > **Scan for hardware changes**, then plug the device into a *different* port.
4. If it enumerates correctly now, the original port's state was the problem — avoid that port until you've done Fix 5.

### Fix 4: Reinstall the device's function driver

Fix the driver layer above the USB handshake.

1. Identify the device class (storage, printer, phone, audio) and download its current Windows 11 driver from the maker.
2. In Device Manager, uninstall the device's entry (**Attempt to remove the driver** checked) with the device unplugged.
3. Install the maker's driver package first, *then* plug in the device when the installer asks (order matters for many peripherals).
4. For phones, ensure the correct USB mode is selected on the phone itself (File Transfer/MTP, not Charging only) — the most common "unrecognized phone" cause.

### Fix 5: Update the chipset and USB controller drivers

Repair the host side of the handshake.

1. Download the **chipset driver package** from your laptop vendor: [Dell Support](https://www.dell.com/support), HP's support site, or [Lenovo Support](https://support.lenovo.com/us/en/) — USB host controllers are chipset components.
2. Install it and restart.
3. In Device Manager > **Universal Serial Bus controllers**, check the **USB xHCI Compliant Host Controller** for warning icons — update its driver if flagged.
4. Intel users can also check the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for newer chipset/USB drivers.

### Fix 6: Rebuild the USB stack and test power delivery

The deep reset plus the power question.

1. In Device Manager > **Universal Serial Bus controllers**, uninstall every **USB Host Controller** entry (leave keyboards/mice for last if they're USB — you'll lose input until reboot, so save work and use the power button to restart).
2. Restart — Windows rebuilds the entire USB stack from scratch on boot.
3. Test the device directly in each port. If it works in some ports but not others, the failing ports may have hardware damage — inspect for bent pins or debris.
4. For power-hungry devices (external HDDs, audio interfaces), test through a **powered** USB hub — if the hub fixes it, the laptop's port power budget was the limiter, not the driver. If the device identifies as unknown even after enumeration succeeds, the [unknown device guide](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) picks up the driver-identification work.

## Closing

"USB device not recognized" is a handshake failure, and handshakes fail for concrete reasons: wedged hub state, power management cutting the port, a broken controller driver, or the device's own driver. Power-cycle properly, disable selective suspend, force clean re-enumeration, and repair the chipset drivers — in that order — and the device that "malfunctioned" will be recognized for what it actually is.
