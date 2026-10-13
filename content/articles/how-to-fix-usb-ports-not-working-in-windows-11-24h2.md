---
title: "USB Ports Not Working After Windows 11 24H2? Fix Them Now"
slug: "how-to-fix-usb-ports-not-working-in-windows-11-24h2"
date: 2026-09-19
categories: ["drivers"]
tags: ["usb ports not working", "windows 11 24h2", "usb driver", "usb selective suspend", "device manager"]
description: "USB ports dead after the Windows 11 24H2 update? Restore USB with controller driver reinstalls, power settings, and update-specific fixes."
thumbnail: "/images/thumbs/how-to-fix-usb-ports-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did the 24H2 update break my USB ports?"
    a: "Feature updates replace low-level drivers including USB host controller drivers, and the 24H2 versions can mismatch certain controller hardware or carry over corrupted settings. Power management policies also get reset during upgrades, re-enabling aggressive USB suspend. Reinstalling the chipset and USB controller drivers and disabling selective suspend resolves most post-24H2 USB failures."
  - q: "Some USB ports work but others do not after 24H2. Why?"
    a: "Partial failure usually means different USB controllers serve different ports, and only some controllers got bad drivers from the update. Laptops commonly have separate controllers for USB 2.0, USB 3.x, and USB-C ports. Check Device Manager for warning icons on specific USB host controllers and reinstall the driver for the affected controller rather than treating all ports the same."
  - q: "Should I roll back the 24H2 update to fix USB?"
    a: "Rollback is a last resort. The USB problem is fixable in place with driver reinstalls in nearly all cases, and rolling back a feature update within its ten-day window disrupts everything else. Only consider rollback if USB remains broken after clean chipset driver installs, BIOS updates, and power management fixes, and the ports are essential for your work."
  - q: "Can USB selective suspend break ports permanently?"
    a: "No, selective suspend cannot damage ports, but it can make them appear dead until the power state is cleared. Disabling selective suspend in the power plan plus a full shutdown usually revives affected ports. The setting is per power plan, so disable it in every plan you use, for both battery and plugged-in states."
---

The Windows 11 24H2 update has a documented habit of breaking USB ports on some laptops: devices that worked for years suddenly are not recognized, ports go silent, or only some ports on the machine keep working. If your USB trouble started within days of the 24H2 upgrade, the update is the prime suspect and the fix is well mapped.

Feature updates touch the USB stack at a low level. They replace host controller drivers, reset power management policies, and occasionally corrupt the driver store entries for specific controllers. The result looks like hardware failure but is configuration damage that a driver reinstall repairs.

This guide targets the 24H2 scenario specifically: controller driver repair, power policy reset, and the update-level steps. For general USB trouble unrelated to 24H2, the [USB port guides](/articles/how-to-fix-usb-ports-not-working-on-windows-11/) cover the same ground without the update focus.

## Why this happens

- **Host controller driver replaced:** 24H2 installs a USB controller driver that mismatches the laptop's hardware.
- **Corrupted driver store entries:** the upgrade corrupts specific USB driver registrations.
- **Power policies reset:** selective suspend and hub power saving get re-enabled by the upgrade.
- **Chipset driver outdated:** the old chipset driver conflicts with 24H2's USB stack expectations.
- **Fast Startup stale state:** hybrid shutdown preserves the broken USB state across boots.
- **BIOS incompatibility:** older BIOS versions mishandle 24H2's USB power sequencing.
- **Device-specific driver loss:** per-device USB drivers fail to migrate during the upgrade.
- **Partial controller failure:** only the controllers with bad drivers fail, so some ports keep working.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Identify which controllers failed

Partial USB failure means specific controllers, not all USB. Device Manager shows exactly which host controllers carry warnings so you can target the reinstall.

1. Open Device Manager and expand Universal Serial Bus controllers.
2. Look for yellow warning icons on USB host controllers or hubs.
3. Note which physical ports map to the failing controller by testing devices.
4. Check the driver date on the failing controllers.
5. Leave healthy controllers alone and focus on the flagged ones.

### Fix 2: Uninstall and rescan USB controllers

Removing the broken controller registrations and letting Windows rediscover them clears upgrade corruption. This is safe: USB input may freeze briefly, so have a backup plan.

1. In Device Manager, right-click each flagged USB controller and choose Uninstall device.
2. Do not check driver removal unless the driver is clearly wrong.
3. After uninstalling, click Action, then Scan for hardware changes.
4. Windows redetects the controllers and reinstalls drivers.
5. Restart the laptop and test all USB ports.

### Fix 3: Reinstall the chipset driver

The chipset driver package contains the USB controller drivers matched to your hardware. Reinstalling the manufacturer's package overwrites whatever 24H2 installed.

1. Download the latest chipset driver from your laptop manufacturer's support page.
2. Run the installer and follow the prompts.
3. Restart when the installer finishes.
4. Check Device Manager to confirm the controller warnings are gone.
5. Test USB devices on every port.

### Fix 4: Disable USB selective suspend everywhere

24H2 resets power plans, re-enabling the suspend behavior that makes ports appear dead. Disabling it in all plans removes the variable.

1. Open Power Options and edit each power plan you use.
2. Open Change advanced power settings for each plan.
3. Set USB selective suspend to Disabled for battery and plugged in.
4. Also disable Allow the computer to turn off this device on USB hubs in Device Manager.
5. Shut down fully, power on, and retest.

### Fix 5: Disable Fast Startup

Fast Startup preserves the broken USB enumeration across boots, making the failure look permanent. A true cold boot after disabling it clears the state.

1. Open Power Options, Choose what the power buttons do.
2. Click Change settings that are currently unavailable.
3. Uncheck Turn on fast startup and save.
4. Shut down fully and unplug for 30 seconds.
5. Power on and verify USB devices enumerate.

### Fix 6: Install pending 24H2 cumulative updates

Microsoft ships USB stack fixes in cumulative updates after feature releases. An update from weeks after the 24H2 install may contain the exact fix.

1. Open Windows Update and check for updates.
2. Install all cumulative and optional driver updates.
3. Restart after installation.
4. Test the previously dead ports.
5. Check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for newer USB drivers if issues persist.

### Fix 7: Update the BIOS

When USB stays broken through driver work, the BIOS may mishandle 24H2's USB initialization. Manufacturers release BIOS updates for exactly this class of issue.

1. Check your BIOS version against the manufacturer's support page.
2. Install any update mentioning USB or 24H2 compatibility.
3. Keep the charger connected throughout the update.
4. Load optimized defaults in the BIOS after updating.
5. Boot into Windows and do a final USB port test.

## Closing

USB failures after 24H2 look like hardware damage but are driver and policy damage from the upgrade. Reinstall the controller and chipset drivers, disable selective suspend and Fast Startup, and install the latest cumulative updates. The ports come back without any hardware work. For related symptoms, see our guide on [USB headset problems](/articles/how-to-fix-usb-headset-not-working-on-lenovo-laptop/). Going forward, treat Patch Tuesday with mild suspicion where USB is concerned: after each cumulative update, plug a USB device into each port group and confirm they all enumerate. Catching a regression the same day makes rollback or driver repair trivial compared to discovering it weeks later. Consider also creating a system restore point before major updates; it takes a minute and gives you a one-click rewind when an update misbehaves. If 24H2 keeps fighting a particular controller, the manufacturer's forums often have a thread where users share which exact driver version finally stabilized their hardware. As a final safeguard, create a system restore point once the ports are healthy. If a future update breaks USB again, rolling back to that point takes minutes and beats repeating the full driver repair.
