---
title: "USB Device Not Recognized on Windows 10? 7 Fixes to Try"
slug: how-to-fix-usb-device-not-recognized-on-windows-10
date: 2026-09-27
categories: ["drivers"]
tags: ["usb not recognized", "windows 10", "usb driver", "device manager"]
description: "'USB device not recognized' on Windows 10? Fix it with these 7 steps — port testing, USB driver reinstalls, power management, and selective suspend tweaks."
thumbnail: "/images/thumbs/how-to-fix-usb-device-not-recognized-on-windows-10.webp"
faqs:
  - q: "What does 'USB device not recognized' mean on Windows 10?"
    a: "It means Windows detected something plugged into the USB port but couldn't identify it — the device descriptor request failed. This happens when the USB drivers are corrupt, the device isn't getting enough power, the cable is charge-only or damaged, USB selective suspend is interfering, or the device itself is faulty. The error is Windows telling you the handshake failed, and the fixes below repair each stage of that handshake."
  - q: "Why does my USB device work on another computer but not mine?"
    a: "That result clears the device and cable — the problem is your computer's USB stack: corrupt USB controller drivers, aggressive USB power management, or a damaged port. Reinstall the USB controllers in Device Manager, disable USB selective suspend, and test every port on the laptop. If it fails on all ports but works elsewhere, the USB driver stack is the culprit; if it fails on one port only, that port is likely damaged."
  - q: "Can a Windows 10 update cause USB recognition failures?"
    a: "Yes. Updates sometimes replace working USB 3.0 controller drivers with incompatible versions, or reset USB power management settings. If USB devices stopped being recognized right after an update, check Device Manager for warnings under Universal Serial Bus controllers, roll back the controller driver if the option exists, or reinstall the chipset driver from your laptop maker's site. Pausing updates prevents the bad driver from returning."
  - q: "Is USB selective suspend safe to disable?"
    a: "Completely safe. Selective suspend lets Windows power down idle USB devices to save battery; disabling it only means USB devices stay powered — costing a tiny amount of battery life. For desktops it's irrelevant; for laptops the impact is minimal. Disabling it is a standard troubleshooting step for recognition issues, and the [selective suspend guide](/articles/best-way-to-turn-off-usb-selective-suspend/) shows every method."
---

You plug in a flash drive, phone, or printer, and Windows 10 pops up: "USB device not recognized. The last USB device you connected malfunctioned." Device Manager shows "Unknown USB Device (Device Descriptor Request Failed)." The device works fine on other computers. Something in your USB chain is refusing the handshake.

USB recognition involves the port, the cable, the USB controller driver, power delivery, and the device's firmware — in that order of likelihood. This guide works that chain methodically, with a verification step after each fix so you know exactly which one solved it.

## Why this happens

- **Corrupt USB controller drivers:** The USB 3.0/extensible host controller driver failing device enumeration.
- **Insufficient power:** The port not delivering enough current, especially for drives and phones.
- **Charge-only or damaged cable:** Cables without data wires can't complete the handshake.
- **USB selective suspend:** Power saving cutting the device mid-enumeration.
- **Port-specific damage:** A physically damaged port failing on some devices.
- **Fast Startup USB state:** Cached USB state confusing re-enumeration.
- **Device firmware issue:** The peripheral's firmware failing to present its descriptor.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the port, cable, and device triangle

Isolate the faulty component with swap tests.

1. Plug the device into a **different USB port** — try both USB 2.0 (black) and USB 3.0 (blue) ports; some devices enumerate better on 2.0.
2. Try a **different cable** — use one proven to transfer data, not just charge.
3. Test the device on **another computer** to confirm it works.
4. Test a **different device** in the suspect port to check the port itself.

Record results: device fails everywhere = device fault; fails on one port = port fault; fails on your laptop only = driver/power fault (continue below).

### Fix 2: Reinstall the USB controllers

Corrupt controller drivers are the top software cause.

1. Open Device Manager (**Win + X**) and expand **Universal Serial Bus controllers**.
2. Right-click each **USB Root Hub**, **USB Host Controller**, and **USB 3.0 Extensible Host Controller** and choose **Uninstall device**. (Your USB mouse may freeze — use the trackpad; everything reinstalls on reboot.)
3. After uninstalling all, click **Action > Scan for hardware changes** — or just restart.
4. Windows rebuilds the entire USB stack fresh.
5. Plug the device in and test.

This clears corrupt controller state without touching your files or settings. It's safe and surprisingly effective. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the same controller-reinstall procedure for persistent USB errors.

### Fix 3: Disable USB selective suspend

Power saving interrupting enumeration is a classic.

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set it to **Disabled** for both battery and plugged in.
3. In Device Manager, for each **USB Root Hub** under USB controllers: **Properties > Power Management** > untick **Allow the computer to turn off this device to save power**.
4. Restart and test the device.

The [selective suspend deep-dive](/articles/best-way-to-turn-off-usb-selective-suspend/) covers registry-level disabling if the settings don't stick.

### Fix 4: Update the chipset driver

The USB controllers are part of the chipset — its driver governs them.

1. Download the latest **chipset driver** for your exact laptop model from the manufacturer's support site.
2. Install it and restart.
3. Recheck Device Manager's USB controllers for warning icons.
4. Test the device again.

OEM chipset drivers include USB controller fixes that Windows' generic drivers lack. This is especially important on AMD-based laptops, where chipset drivers significantly affect USB stability.

### Fix 5: Remove the Unknown USB Device ghost entries

Stale failed-enumeration entries can block fresh attempts.

1. In Device Manager, enable **View > Show hidden devices**.
2. Expand **Universal Serial Bus controllers** and uninstall every greyed-out **Unknown USB Device** entry.
3. Unplug the device, restart, then plug it into a different port.
4. If it enumerates correctly now, the ghost entry was blocking it.

Also check **Disk Management** for storage devices that enumerate as disks but don't get letters — assign a letter if needed.

### Fix 6: Disable Fast Startup and test with full power

Cached USB state and power limits both interfere.

1. **Control Panel > Power Options > Choose what the power buttons do** > untick **Turn on fast startup**.
2. For power-hungry devices (external HDDs, phones), use a **powered USB hub** or a **Y-cable** — laptop ports sometimes can't supply enough current.
3. Keep the laptop on **AC power** while testing — battery saver modes limit USB power.
4. Shut down fully, wait 30 seconds, boot, and test.

If the device works through a powered hub but not directly, the laptop's port power delivery is marginal for that device — the hub is the permanent fix.

### Fix 7: Check for port damage and update the device firmware

When software is exhausted, inspect hardware.

1. Shine a light into the USB port — bent pins, debris, or a loose tongue indicate physical damage.
2. Clean debris carefully with compressed air and a wooden toothpick (power off first).
3. Check the device manufacturer's site for **firmware updates** for the peripheral itself.
4. For phones: try a different USB mode on the phone (File Transfer/MTP vs Charging) — the mode dialog appears in the phone's notification shade.
5. Test in a Linux live USB — working there confirms a Windows driver issue; failing there confirms hardware.

A single damaged port doesn't condemn the laptop — USB hubs are cheap. But multiple failing ports suggest chipset trouble, which needs professional diagnosis. For broader port failures, the [USB ports guide](/articles/best-way-to-fix-usb-ports-not-working/) covers controller-level repair.

## Closing

"USB device not recognized" is a handshake failure, and handshakes fail at specific points: cable, port, power, driver. The swap test identifies which point in two minutes; the controller reinstall and selective-suspend fixes handle the software side. Once the device enumerates cleanly, it stays recognized — USB doesn't forget a working handshake.
