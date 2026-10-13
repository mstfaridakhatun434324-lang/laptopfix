---
title: "USB Ports Not Working on Windows 11? Fix Them Step by Step"
slug: how-to-fix-usb-ports-not-working-on-windows-11
date: 2026-10-05
categories: ["drivers"]
tags: ["usb ports not working", "windows 11 usb", "usb device not recognized", "usb driver fix"]
description: "USB ports dead on Windows 11? Work through power settings, USB controller drivers, and selective suspend fixes to bring every port back."
thumbnail: "/images/thumbs/how-to-fix-usb-ports-not-working-on-windows-11.webp"
faqs:
  - q: "Why do my USB ports work in the BIOS but not in Windows?"
    a: "That pattern points squarely at a Windows driver or power-management problem, not hardware. The USB controllers and ports are electrically fine — Windows is failing to drive them. Reinstalling the USB controller drivers and disabling USB selective suspend are the two fixes that resolve this in most cases."
  - q: "What is USB selective suspend and should I disable it?"
    a: "USB selective suspend lets Windows power down individual USB ports to save battery. On many laptops it misbehaves, leaving ports unresponsive until a reboot. Disabling it in the power plan is safe — it slightly increases idle power draw but eliminates an entire class of flaky-port behavior, and it is reversible."
  - q: "Why does only one USB port fail while the others work?"
    a: "Individual port failures usually mean a damaged port, a bent pin inside it, or debris — especially on frequently used ports. Try the same device in every port: if it works elsewhere, the port itself is the problem. Check inside the dead port with a flashlight for bent pins before assuming the controller is at fault."
  - q: "Can a Windows update break all USB ports at once?"
    a: "Yes. Updates sometimes replace USB 3.x controller drivers with versions that do not initialize correctly, or corrupt the driver stack. Uninstalling the USB controllers in Device Manager and letting Windows redetect them on reboot fixes this, because it forces a clean driver enumeration."
---

When every USB port on a Windows 11 laptop stops responding — no mice, no drives, no phones charging — the machine feels broken. But total USB failure is rarely a hardware problem. Windows 11 manages USB through a stack of controller drivers and aggressive power-saving features, and when any layer of that stack glitches, all the ports go dark together.

The pattern matters for diagnosis. All ports dead at once points to drivers or power management. One dead port points to physical damage. Devices that connect and instantly disconnect point to power delivery. The fixes below are ordered to match: fast software resets first, then driver work, then the per-port and hardware checks.

## Why this happens

- **USB selective suspend** powered the ports down and failed to wake them — the most common cause of ports that die after sleep.
- **Corrupted USB controller drivers**, often after a Windows update replaced the working version.
- **Power management on USB root hubs** allowing Windows to switch ports off to save power.
- **Overloaded port power budget** — too many bus-powered devices drawing more than the port can supply.
- **Fast Startup holding a bad device state** across reboots, so the problem survives restarts.
- **Physically damaged port** — bent pins, debris, or a cracked solder joint on one or more ports.
- **BIOS USB settings** (xHCI mode, USB power in sleep) misconfigured after a firmware update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do a full power drain

A full power drain clears the USB controller state that Fast Startup preserves across reboots. Shut down completely, unplug everything including the charger, hold the power button for 15 seconds, then reconnect and boot. This alone revives ports that died after sleep or hibernation, because it forces every controller to re-enumerate from scratch.

1. Shut the laptop down completely — not sleep, not hibernate.
2. Unplug the charger and every USB device.
3. Hold the power button for 15 seconds, then release.
4. Reconnect the charger, boot, and test the USB ports.

### Fix 2: Disable USB selective suspend

Selective suspend is the top software suspect. Turning it off stops Windows from parking individual ports, which eliminates the wake-failure behavior. The cost is a small increase in idle power draw — negligible on a laptop that spends most of its time plugged in, and worth it for reliable ports.

1. Open Power Options > Change plan settings > Change advanced power settings.
2. Expand USB settings > USB selective suspend setting.
3. Set it to Disabled for both On battery and Plugged in.
4. Click OK and test the ports after sleep and wake.

### Fix 3: Stop Windows powering off the USB root hubs

Each USB root hub has its own power-management toggle that lets Windows switch it off. When several hubs get parked, every port they serve dies. Untick the option on all of them — it takes a minute and prevents Windows from ever putting a hub to sleep behind your back. Microsoft covers these power settings in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Device Manager and expand Universal Serial Bus controllers.
2. Right-click each USB Root Hub, open Properties > Power Management.
3. Untick 'Allow the computer to turn off this device to save power'.
4. Repeat for every root hub entry, then reboot.

### Fix 4: Reinstall the USB controller drivers

Uninstalling the USB controllers forces Windows to redetect and reinstall the entire USB stack with clean drivers. Do this from Device Manager — your mouse and keyboard will stop working mid-process if they are USB, so have the laptop's touchpad or keyboard ready. For 'device not recognized' errors on specific peripherals rather than dead ports, the [USB device not recognized guide](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) goes deeper.

1. Open Device Manager and expand Universal Serial Bus controllers.
2. Right-click each USB controller/host entry and choose Uninstall device.
3. When all are uninstalled, restart the laptop.
4. Windows reinstalls the controllers automatically — test every port.

### Fix 5: Turn off Fast Startup

Fast Startup saves a snapshot of device states at shutdown, which means a corrupted USB controller state gets reloaded on every boot. Disabling it forces a true cold boot every time. This is a prime suspect when USB ports fail after every restart but work after a full power drain.

1. Open Power Options > Choose what the power buttons do.
2. Click 'Change settings that are currently unavailable'.
3. Untick 'Turn on fast startup' and save changes.
4. Shut down fully, boot, and test the ports.

### Fix 6: Test ports individually and inspect for damage

If only some ports fail, the problem is physical. Test the same known-good device — a simple USB flash drive is ideal — in every port. Shine a flashlight into any dead port and look for bent pins or debris; a bent pin can short the port and take its controller channel down. Do not probe inside with metal tools while powered.

1. Test one known-good USB device in every port.
2. Note which ports fail — a single dead port means physical damage.
3. Inspect dead ports with a flashlight for bent pins or debris.
4. Blow out debris with compressed air; bent pins need professional repair.

### Fix 7: Check BIOS USB settings

Enter the BIOS and verify USB controllers are enabled and xHCI mode is on — some firmware updates reset these. Also check any 'USB power in sleep' or 'always-on USB' options. If ports work in the BIOS menus but not in Windows after all the above, reinstall Windows' chipset driver from the laptop maker, since the USB controllers depend on it.

1. Reboot into the BIOS and confirm USB controllers are enabled.
2. Ensure xHCI / USB 3 mode is enabled, not disabled or Auto-failing.
3. Save, boot into Windows, and retest.
4. Install the latest chipset driver from the laptop maker if issues persist.

## Closing

Dead USB ports on Windows 11 are a software problem far more often than a hardware one: the power drain, selective suspend, and controller reinstall in this guide resolve the great majority of cases. Reserve the hardware suspicion for single dead ports with visible damage. And once the ports are back, leave selective suspend off — the tiny battery cost buys you ports that work every time you plug something in. If individual devices fail to enumerate while the ports themselves are alive, work through [USB device not recognized fixes](/articles/how-to-fix-usb-device-not-recognized-in-windows-11-24h2/).
