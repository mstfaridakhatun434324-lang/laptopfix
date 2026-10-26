---
title: "AI Laptop USB Ports Not Working? How to Fix It on Windows 11"
slug: ai-laptop-usb-ports-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags: ["usb ports", "ai laptop", "windows 11", "usb not working", "hardware fix"]
description: "USB ports not working on your AI laptop? Fix dead ports, unrecognised devices, and power issues on Windows 11 with clear, safe steps and get connected again."
thumbnail: "/images/thumbs/ai-laptop-usb-ports-not-working.webp"
faqs:
  - q: "Why do some USB ports work but others do not?"
    a: >
      Different ports may use different controllers, hubs, or power limits, so one faulty driver, disabled hub, or power-saving setting can affect only some ports. Testing each port with the same device helps you tell a single-port fault from a system-wide driver problem.
  - q: "Why does Windows say USB device not recognised?"
    a: >
      That message usually means the device descriptor failed, the driver is missing or corrupted, or the port cannot supply enough power. Trying another port and cable, updating the USB controller driver, and removing ghost devices in Device Manager usually resolves it.
  - q: "Can a USB hub cause ports to stop working?"
    a: >
      Yes. An unpowered hub, a faulty hub, or too many power-hungry devices on one hub can overload the port and cause disconnects. Connect the device directly to the laptop to test, and use a powered hub for drives, docks, and multiple accessories.
  - q: "Should I update the BIOS if USB ports fail?"
    a: >
      Only after driver and power fixes fail. A BIOS or firmware update can fix USB controller bugs, but it carries risk if power is lost during the update, so keep the laptop plugged in, back up data, and use only the maker's official update.
---

USB ports are the workhorses of a laptop: they connect mice, keyboards, drives, docks, printers, and phones. When they stop working, work stalls quickly. A drive may not appear, a mouse may freeze, Windows may report a device as unrecognised, or an entire side of ports may go dead. On a thin AI laptop with only a few ports, losing even one feels like losing a lot.

Most USB failures on Windows 11 are not permanent hardware damage. Drivers can corrupt, hubs can be disabled by power saving, ghost devices can block new connections, and a single bad cable or hub can make every port look faulty. Sorting out which of those is happening is the key to a fast fix.

This guide takes you through that diagnosis in order. You will test ports and cables properly, reset the USB stack, fix power and driver problems, and know when a port genuinely needs professional repair.

## Why this happens

- **Power saving disabled hubs:** Windows may switch off USB root hubs to save battery, and some hubs fail to wake cleanly, leaving ports dead until restart.
- **Corrupted USB controller driver:** A failed update or conflicting driver can break an entire controller, affecting every port attached to it at once.
- **Ghost or conflicting devices:** Old, hidden device entries can conflict with a newly connected device, causing unrecognised-device errors.
- **Faulty cable, hub, or device:** A damaged cable or overloaded unpowered hub is the most common cause, yet it is often mistaken for a laptop fault.
- **Insufficient power:** External drives, docks, and multiple accessories can draw more power than a single port or hub can supply.
- **Fast Startup sleep state:** Fast Startup can leave USB controllers in a half-powered state after shutdown, so ports misbehave until a full restart.
- **Physical port damage:** Bent pins, debris, or a loose port from repeated plugging can cause intermittent contact that software fixes cannot repair.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test ports, cables, and devices properly

Never assume the laptop is at fault until you have isolated the variables. A proper test takes only a few minutes and prevents hours of driver work for a bad cable. Use a device you know works, test every port, and remove hubs from the chain for the first test.

1. Shut down the laptop fully, disconnect all USB devices and hubs, then power on again with nothing attached.
2. Connect one known-good device, such as a wired mouse, directly to each port in turn, without a hub or extension cable.
3. Try a different cable with the same device, since USB-C and micro-USB cables vary in data and power capability.
4. Test the same device on another computer if possible, to confirm the device itself is healthy.

### Fix 2: Restart the USB stack and remove ghost devices

Windows keeps a history of every USB device ever connected, and stale entries can block new ones. Removing ghost devices and restarting the USB controllers forces Windows to rediscover ports cleanly. This is safe: Windows reinstalls controllers automatically on restart, and your files are untouched.

1. Open Device Manager, click View, then Show hidden devices to reveal greyed-out USB entries.
2. Expand Universal Serial Bus controllers, and uninstall any greyed-out or duplicate entries for devices no longer connected.
3. Right-click each USB Root Hub and USB Host Controller, choose Uninstall device, but do not tick Delete driver software for controllers.
4. Restart the laptop and let Windows reinstall the controllers automatically, then test your device again.

For official Windows help, see [Windows support](https://support.microsoft.com/en-us/windows). Laptop makers also publish USB and chipset drivers that can help when Windows generic drivers fail.

### Fix 3: Stop power saving from switching ports off

Power management is a leading cause of ports that work after a restart but fail after sleep or idle time. Windows may power down root hubs, and some AI laptops aggressively cut USB power to extend battery life. Disabling that behaviour for hubs removes random disconnects and dead-after-sleep ports.

1. Open Device Manager, expand Universal Serial Bus controllers, and open Properties for each USB Root Hub.
2. Go to the Power Management tab and uncheck Allow the computer to turn off this device to save power.
3. Repeat for every root hub and for USB devices listed under Universal Serial Bus devices if they offer the option.
4. Open power plan advanced settings and set USB selective suspend setting to Disabled for the plugged-in profile.

### Fix 4: Fix power delivery and hub problems

Many USB failures are really power failures. An external drive that spins up, a dock with several devices, or a long passive extension can exceed what a port supplies. When Windows reports insufficient power, a device keeps disconnecting, or a drive clicks and vanishes, the power chain is the first suspect — a pattern also seen when companion features fail for power or service reasons, as in the [copilot-actions-not-working](/articles/copilot-actions-not-working/) and [cocreator-prompt-no-image](/articles/cocreator-prompt-no-image/) guides.

1. Connect power-hungry devices directly to the laptop, bypassing hubs, docks, and extension cables for testing.
2. Use a powered USB hub with its own mains adapter for multiple devices, especially external drives and docks.
3. Use the cable supplied with the device, or a short, high-quality cable rated for data and the required power level.
4. Disconnect other USB devices temporarily to test whether total power draw was causing the failure.

### Fix 5: Do a full power reset and check for hardware damage

When software fixes fail, a full power reset clears the controller state that survives normal restarts, especially with Fast Startup enabled. This step also gives you a clean moment to inspect ports physically. If a port is damaged, no driver fix will help, and continued forcing of connectors can worsen the damage. Note that a missing feature after an update is sometimes a software issue instead, as with the [copilot-app-missing-start-menu-search](/articles/copilot-app-missing-start-menu-search/) case, so keep your driver and test notes for support.

1. Shut down the laptop fully, unplug the charger, and disconnect all USB devices.
2. Hold the power button for fifteen to twenty seconds to drain residual power, if your laptop maker allows this procedure.
3. Reconnect the charger, power on, and test a known-good device in each port before reattaching hubs.
4. Inspect each port with a torch for bent pins, debris, or a loose tongue, and clean dust gently with compressed air only.

## Closing

USB port failures on AI laptops look alarming but are usually caused by a cable, hub, power setting, or driver that you can fix in under an hour. Test methodically, remove hubs for diagnosis, update chipset drivers, disable hub power saving, and do a full power reset before assuming hardware failure. If a single port stays dead after all of that, or shows physical damage, professional repair is the safe next step — and your test notes will help the technician fix it faster.
