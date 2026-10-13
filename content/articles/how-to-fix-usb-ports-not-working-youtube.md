---
title: "USB Ports Not Working on a Laptop? Video-Guide Style Walkthrough"
slug: how-to-fix-usb-ports-not-working-youtube
date: 2026-09-20
categories: ["drivers"]
tags: ["usb ports", "usb not working", "device not recognized", "usb driver", "troubleshooting"]
description: "Dead USB ports on your laptop? Follow this visual-style walkthrough: power reset, driver reinstall, power management, and hardware checks."
thumbnail: "/images/thumbs/how-to-fix-usb-ports-not-working-youtube.webp"
faqs:
  - q: "Why did all my USB ports stop working at once?"
    a: "When every USB port dies simultaneously, the cause is almost never the individual ports — it's something they share: the USB host controller driver, a system-wide power management glitch, or a BIOS setting. A single dead port suggests physical damage; all ports dead points to driver or controller issues, which are very fixable."
  - q: "Can a Windows update break USB ports?"
    a: "Yes. USB host controller driver updates bundled with Windows updates occasionally break port enumeration, particularly on AMD platforms and older Intel chipsets. If all ports died right after an update, rolling back the USB controller driver or reinstalling the chipset driver package usually restores them immediately."
  - q: "Why does my USB device work on one port but not another?"
    a: "Individual ports can fail from physical wear — the internal contacts loosen or break after thousands of insertions. USB 3 ports (blue) and USB 2 ports (black) also run on different controllers, so a controller issue can kill one type while the other works. Try every port and note the pattern before concluding anything."
  - q: "Should I disable USB selective suspend?"
    a: "For troubleshooting, yes — it's a fast test that eliminates an entire category of causes. USB selective suspend powers down idle ports to save battery, and some devices fail to wake properly. If disabling it fixes your problem, you can leave it off (minor battery cost) or re-enable it later once you've confirmed the real culprit."
---

USB port failures are disorienting because USB is the laptop's lifeline — mouse, keyboard, drives, chargers, everything. When ports die, the natural reaction is to assume the motherboard is finished. But the reality, the one every repair tech and tutorial walks through, is that USB failures are overwhelmingly software: controller drivers, power management, and enumeration glitches. Physical port death happens, but it's the exception.

This walkthrough follows the order you'd see in a good video tutorial: start with what you can see and touch, then move into Device Manager, then power settings, then the deeper fixes. Each step is something you can follow along with on screen.

## Why this happens

- **USB host controller driver corrupted:** All ports share controllers; one bad driver kills every port at once.
- **USB selective suspend glitch:** Power management suspends ports that then fail to wake, making devices appear dead.
- **Static charge / power state lockup:** Residual charge can leave the USB subsystem in a wedged state that survives reboots.
- **Windows Update driver replacement:** Microsoft's USB driver version may not match your chipset, breaking enumeration.
- **BIOS USB settings changed:** XHCI handoff or USB port toggles in BIOS can disable ports at the hardware level.
- **Overcurrent protection tripped:** A shorted USB device can trip the port's protection circuit, shutting down the port or hub.
- **Physical port damage:** Bent pins or broken solder joints from forceful insertions or cable strain.
- **Chipset driver missing:** The USB controllers are part of the chipset; without correct chipset drivers, ports misbehave.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do the full power reset (watch the ports wake up)

1. Shut down the laptop completely and unplug the charger and **all** USB devices.
2. If the battery is removable, remove it. Otherwise, hold the power button for **30–60 seconds** with everything unplugged.
3. Reconnect only the charger, power on, and then plug in one USB device to test.
4. This drains flea power and resets the USB controllers — it fixes more "dead USB" cases than any other single step.

### Fix 2: Test every port and identify the pattern

1. Try a simple, known-good USB device (a basic flash drive or mouse) in **every** port, one at a time.
2. Note the pattern: all dead (controller/driver issue), only USB 3 dead (xHCI driver issue), one dead (physical damage), or intermittent (power/connection issue).
3. Try the device on another computer to confirm the device itself isn't the problem.
4. This two-minute survey directs everything that follows — don't skip it.

### Fix 3: Reinstall the USB host controllers

1. Open **Device Manager** and expand **Universal Serial Bus controllers**.
2. Right-click each **USB Root Hub** and **USB Host Controller** entry → **Uninstall device**. Don't worry — they'll come back.
3. Restart the laptop. Windows redetects all USB hardware and reinstalls fresh controller drivers.
4. Test your devices. This rebuilds the entire USB software stack and resolves the classic [USB device not recognized](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) errors too.

### Fix 4: Disable USB selective suspend

1. Open **Control Panel → Power Options → Change plan settings → Change advanced power settings**.
2. Expand **USB settings → USB selective suspend setting** and set it to **Disabled** for both battery and plugged in.
3. In Device Manager, for each **USB Root Hub** → **Properties → Power Management**, uncheck **"Allow the computer to turn off this device to save power."**
4. Restart and test, especially with devices that worked briefly then died — that's the selective-suspend signature.

### Fix 5: Update or reinstall chipset drivers

1. Go to your laptop maker's support page and download the latest **chipset driver** package for your model (see [how to install chipset drivers on a laptop](/articles/how-to-install-chipset-drivers-on-laptop/) if you're unsure which package you need).
2. Install it as Administrator and reboot — this refreshes the USB controller drivers at their source.
3. For Intel systems, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can detect and update chipset components automatically.
4. Retest all ports. Chipset-level fixes resolve the stubborn cases where controller reinstalls alone didn't stick.

### Fix 6: Check BIOS USB settings

1. Enter **BIOS/UEFI** setup during boot (F2/Del).
2. Look for USB-related options: **XHCI Handoff** (should be Enabled), **USB ports** (all Enabled), **Legacy USB support**.
3. If you recently updated BIOS, choose **Load Optimized Defaults** — updates sometimes reset USB settings badly.
4. Save and boot. BIOS-level USB disables are invisible to Windows, so this check catches what Device Manager cannot.

### Fix 7: Clear overcurrent trips and inspect for damage

1. With the laptop off and unplugged, shine a light into each USB port and look for bent pins, debris, or burn marks.
2. A bent pin touching the port wall causes shorts that trip overcurrent protection — carefully straighten it with a plastic toothpick, never metal while powered.
3. If Windows ever showed an "overcurrent" or "power surge on USB port" warning, that port's protection tripped; the power reset in Fix 1 usually clears it.
4. Ports with visible burn damage or broken tongues need professional repair — stop using that port to avoid shorting the motherboard.

### Fix 8: Test in a clean environment and consider hardware

1. Boot into **Safe Mode** or a Linux live USB and test the ports there. Working ports in Linux prove a Windows driver problem; dead ports everywhere prove hardware failure.
2. Check **Device Manager** for USB entries with yellow warnings that persist across reinstalls — a controller that won't initialize is a hardware fault.
3. For confirmed hardware failure, a powered USB hub can't fix dead ports, but a USB-C dock can add working ports through a different controller.
4. Motherboard-level USB repair is rarely economical out of warranty — document the failure pattern first, as the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) advises for hardware diagnostics.

## Closing

USB port failures look scary and fix easy: power reset, controller reinstall, selective suspend off, chipset drivers. That sequence revives the vast majority of "dead" ports — and the pattern test at the start tells you immediately if you're dealing with software or hardware. Bookmark the sequence; USB gremlins return after major updates often enough that you'll be glad it's familiar.
