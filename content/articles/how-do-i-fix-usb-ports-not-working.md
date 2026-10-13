---
title: "USB Ports Not Working on Your Laptop? Here's How to Fix Them"
slug: how-do-i-fix-usb-ports-not-working
date: 2026-09-13
categories: ["drivers"]
tags: ["usb ports", "usb not working", "device manager", "power management"]
description: "USB ports dead on your Windows laptop? Work through port testing, power settings, and controller driver fixes to bring them back."
thumbnail: "/images/thumbs/how-do-i-fix-usb-ports-not-working.webp"
faqs:
  - q: "Why did all my USB ports stop working at once?"
    a: "All ports dying simultaneously almost always points to software: the USB host controller driver crashed or was replaced by a bad update, or USB selective suspend put the controller to sleep and it never woke. Hardware rarely kills every port at once — a single dead port suggests physical damage, but all ports together means the controller or its driver."
  - q: "How do I reset USB ports without restarting?"
    a: "Open Device Manager, expand Universal Serial Bus controllers, right-click each USB Root Hub and USB Host Controller, choose Uninstall device (don't check delete driver), then click Action > Scan for hardware changes. Windows redetects and reinitializes the controllers immediately — this resets the ports without a reboot in most cases."
  - q: "Can power settings disable USB ports?"
    a: "Yes. USB selective suspend lets Windows power down individual ports to save battery, and aggressive power plans can leave ports asleep. Disable it in Control Panel > Power Options > Change plan settings > Change advanced power settings > USB settings > USB selective suspend setting, setting both battery and plugged-in to Disabled. Also uncheck 'Allow the computer to turn off this device' on each USB Root Hub's Power Management tab."
  - q: "One USB port works but others don't — is it hardware?"
    a: "Most likely, yes. When some ports work and others don't, the controller and driver are fine (they're shared), so the dead ports usually have physical damage — bent pins, debris, or a cracked solder joint. Try the dead port with a simple low-power device like a wired mouse to confirm, and inspect the port with a flashlight for bent pins before assuming the worst."
---

USB ports are the laptop's universal translators — mice, drives, phones, docks — so when they all go dark at once, the laptop feels broken in a dozen ways simultaneously. The encouraging pattern: every port dying together is almost always software (controller driver or power management), while a single dead port is usually physical damage. That distinction tells you exactly where to start.

Work the sequence: test with a simple device, reset the controllers in Device Manager, kill the power-saving features that put ports to sleep, then update the chipset drivers underneath it all. For "device not recognized" errors on ports that do have power, see [fixing USB device not recognized](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/); for the chipset drivers that run the USB controllers, see [installing chipset drivers](/articles/how-can-i-install-chipset-drivers/).

## Why this happens

- **USB host controller driver crashed or corrupted**: The driver managing all ports fails, taking every port with it at once.
- **USB selective suspend stuck**: Windows powers down ports to save battery and the controller fails to wake them.
- **"Allow the computer to turn off this device" enabled**: Per-hub power management aggressively sleeps ports, especially on battery.
- **Bad chipset driver update**: The USB controllers are part of the chipset; a bad chipset driver update breaks them all.
- **Static charge / controller lockup**: The embedded controller gets into a bad state that persists across normal restarts.
- **Physical port damage**: Bent pins or debris in individual ports — usually affects one port, not all.
- **BIOS USB settings changed**: XHCI hand-off or USB legacy settings altered by a BIOS update or reset.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with a simple device and different ports

Establish the actual scope of the failure.

1. Plug a simple, low-power device — a wired USB mouse is ideal — into each port one at a time. A mouse needs almost no power and minimal driver support, so it's the cleanest test.
2. Note exactly which ports respond: all dead (software/controller), some dead (physical damage on those ports), or all working with the mouse but not with a specific device (that device's problem, not the ports').
3. Try the device that "doesn't work" on another computer to rule out a dead peripheral.
4. Inspect each dead port with a flashlight — bent pins, lint, or corrosion are visible and explain single-port failures instantly.
5. If all ports are dead with the mouse, continue — this is the software path.

### Fix 2: Power-drain the embedded controller

Clears the static/lockup state that survives restarts.

1. Shut the laptop down completely (not sleep, not hibernate — **Shut down**).
2. Unplug the AC adapter and every USB device.
3. If the battery is removable, take it out. If it's internal, hold the power button down for a full 30 seconds with everything unplugged.
4. Reconnect only the AC adapter (leave USB devices unplugged), power on, and test the ports with your mouse before plugging anything else in.
5. This drains residual charge from the embedded controller, which manages the USB ports at firmware level — a surprising number of "all ports dead" cases end here.

### Fix 3: Reset the USB controllers in Device Manager

Reinitialize the whole USB stack without rebooting.

1. Press **Win + X** > **Device Manager** and expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub** and each **USB Host Controller** entry: right-click > **Uninstall device**. Do NOT check "delete driver software" — you want Windows to reuse the existing driver files.
3. Work top to bottom; your USB mouse will stop working partway through — that's expected. Switch to the touchpad or keyboard (**Win + X**, arrows, Enter) to continue.
4. When all are uninstalled, click **Action** > **Scan for hardware changes**. Windows redetects every controller and reinstalls the stack fresh.
5. Test the ports. This reset fixes controller lockups and corrupted enumerations without a restart.

### Fix 4: Disable USB selective suspend and hub power management

Stop Windows from putting your ports to sleep.

1. Open **Control Panel** > **Power Options** > **Change plan settings** (for your active plan) > **Change advanced power settings**.
2. Expand **USB settings** > **USB selective suspend setting** and set both **On battery** and **Plugged in** to **Disabled**. Click OK.
3. Back in **Device Manager** > **Universal Serial Bus controllers**, right-click each **USB Root Hub** > **Properties** > **Power Management** tab, and uncheck **Allow the computer to turn off this device to save power**.
4. Do this for every Root Hub entry — missing one leaves a sleeping port.
5. Restart and test, especially on battery — selective suspend misbehaves most when unplugged.

### Fix 5: Update the chipset drivers

The USB controllers live in the chipset — fix the foundation.

1. Identify your chipset: Intel, AMD, or Qualcomm (**Device Manager** > **System devices**, or check your CPU in **Settings** > **System** > **About**).
2. Download the latest chipset driver package: Intel users should run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html); AMD users get theirs from [AMD's driver page](https://www.amd.com/en/support/download/drivers.html); everyone else, use the laptop manufacturer's support page.
3. Install the chipset package and restart — this refreshes the USB host controller drivers with versions matched to your hardware.
4. After restart, recheck Device Manager for any remaining yellow warnings under USB controllers.
5. If Windows Update previously installed the chipset driver, consider whether the problem started then — [roll it back](/articles/best-way-to-rollback-driver-update/) if the timeline matches.

### Fix 6: Check BIOS USB settings

Firmware-level USB configuration, especially after BIOS updates.

1. Restart into BIOS/UEFI (**F2**/**Del**/**F10** during boot, varies by maker).
2. Look under **Advanced** or **Devices** for USB-related options: **XHCI Hand-off**, **USB Legacy Support**, **USB ports** enable/disable.
3. Ensure USB ports are enabled and XHCI hand-off is on (it should be for Windows 10/11).
4. If a recent BIOS update preceded the failure, use **Load Optimized Defaults**, save, and retest — updates sometimes scramble these settings.
5. Save (**F10**), exit, and test in Windows.

### Fix 7: Repair system files and test in a clean boot

For the stubborn cases where everything looks right but nothing works.

1. Open an elevated terminal (**Win + X** > **Terminal (Admin)**) and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. If system files were corrupt, restart and retest the ports.
3. Still dead? Run `msconfig`, go to the **Services** tab, check **Hide all Microsoft services**, click **Disable all**, restart — this clean boot rules out third-party software interfering with USB.
4. If ports work in clean boot, re-enable services in halves to find the conflicting program (USB security/lockdown software is a classic).
5. For persistent all-port failure across clean boot and BIOS defaults with no Device Manager errors, suspect motherboard-level hardware failure — a repair shop diagnosis is the next step.

## Closing

USB port failures follow a clean diagnostic logic: all ports dead means software or controller — reset the stack, kill the power-saving, refresh the chipset driver. One port dead means physical — look inside it with a flashlight. Match the symptom pattern to the fix and you'll rarely need more than twenty minutes.
