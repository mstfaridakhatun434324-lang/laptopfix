---
title: "Surface Laptop Battery Not Charging on Windows 11: Fix Guide"
slug: how-to-fix-surface-laptop-battery-not-charging-on-windows-11
date: 2026-09-24
categories: ["battery"]
tags: ["surface laptop", "not charging", "windows 11", "battery limit"]
description: "Surface Laptop not charging after upgrading to Windows 11? Fix connector, driver, and battery-limit issues with this focused guide."
thumbnail: "/images/thumbs/how-to-fix-surface-laptop-battery-not-charging-on-windows-11.webp"
faqs:
  - q: "Why did my Surface stop charging after the Windows 11 upgrade?"
    a: "The upgrade can replace Surface-specific battery drivers with generic ones, re-enable the UEFI battery limit, or leave the embedded controller in a confused state. Reinstalling the Surface battery drivers and checking the UEFI battery limit resolves most post-upgrade charging failures."
  - q: "Where is the battery limit setting on a Surface with Windows 11?"
    a: "Shut down, then hold Volume Up while pressing Power until the UEFI screen appears. Under Boot configuration, find Battery Limit. Turn it off if your charge stalls at 50 percent — this limit is commonly re-enabled by firmware updates."
  - q: "Should I use the Surface app to check battery health?"
    a: "Yes. The Surface app (from the Microsoft Store) shows battery health and charging status, and the Surface Diagnostic Toolkit runs automated battery tests. Both are more Surface-aware than Windows' generic battery report."
  - q: "Can I charge my Surface with USB-C instead?"
    a: "Many newer Surface Laptops support USB-C Power Delivery charging. If the Surface Connect port is the problem, a 65W USB-C PD charger is a good workaround — see our USB-C charging guide for cable and wattage requirements."
---
Upgrading a Surface Laptop to Windows 11 should be uneventful. For many owners it is — until they notice the battery percentage frozen in place, or the dreaded "plugged in, not charging" message that wasn't there yesterday. The upgrade touches drivers, firmware interfaces, and power settings all at once, which gives charging failures several new ways to appear. If your upgrade completed in the last few days and charging worked fine before, treat this as a software problem first — the odds are strongly in your favor.

The good news: post-upgrade Surface charging problems are overwhelmingly software. The connector and charger rarely break at the exact moment of an OS upgrade. This guide focuses on what the upgrade actually changes, in the order that finds it.

## Why this happens

- **Generic drivers replacing Surface drivers:** Windows 11 setup can install standard ACPI battery drivers instead of Microsoft's Surface-tuned ones.
- **UEFI Battery Limit re-enabled:** firmware updates bundled with the upgrade can flip the 50-percent charge cap back on.
- **Embedded controller confusion:** the upgrade's multiple reboots can leave the EC in a state where it stops reporting charge correctly.
- **Fast Startup carrying over a bad state:** the hybrid shutdown from the old install can preserve broken power state into the new OS.
- **Surface app / firmware mismatch:** old Surface firmware paired with new Windows 11 power management miscommunicates.
- **Dirty connector (coincidence):** sometimes the timing really is coincidence — check the physical layer too.
- **Deeply discharged battery:** if the battery was low during the long upgrade process, it may need an extended charge to recover.
- **Corrupted power plans carried over:** the upgrade migrates your old power plans, and a damaged plan can carry broken charging behavior into the new OS even though everything else looks fine.

## How to fix it

Work through these in order, starting with what the upgrade most likely changed.

### Fix 1: Reinstall the Surface battery drivers

The single most effective post-upgrade fix. Windows 11's setup is notorious for swapping Microsoft's Surface-tuned battery drivers for generic ones that don't fully understand the Surface power hardware.

1. Press **Win + X**, open **Device Manager**, and expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and any **Surface**-named battery entries.
3. Expand **Firmware** and **System devices**, looking for warning icons on Surface-related entries — update or reinstall those drivers too.
4. Shut down fully, wait 30 seconds, and boot with the charger connected.

### Fix 2: Check the UEFI Battery Limit

1. Shut down completely.
2. Press and hold **Volume Up**, then press **Power**; release Power but keep holding Volume Up until UEFI appears.
3. Under **Boot configuration**, check **Battery Limit**. If it's on and charging stalls at 50 percent, turn it **Off**.
4. Exit saving changes and check charging in Windows.

### Fix 3: Do a two-button EC reset

1. Hold **Power** for 30 seconds and release.
2. Hold **Power + Volume Up** for 15 seconds, release, wait 10 seconds.
3. Press **Power** to boot. This is Surface's equivalent of the embedded-controller reset and clears post-upgrade charging glitches.

### Fix 4: Disable Fast Startup to clear carried-over state

1. Go to **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Do a full shutdown and cold boot. The old install's hibernation-flavored state can't survive this.

### Fix 5: Update Surface firmware and drivers

1. Open **Settings > Windows Update** and install everything, then check **Advanced options > Optional updates** for Surface firmware entries.
2. Install the **Surface** app from the Microsoft Store and check its battery health readout.
3. Run the **Surface Diagnostic Toolkit** battery tests — it validates the charger handshake end to end.
4. Microsoft documents Surface-specific recovery steps at [Microsoft support](https://support.microsoft.com/en-us/windows).

### Fix 6: Clean the connector and verify the charger

1. Unplug everything and wipe the Surface Connect pins with a dry cloth; use a pencil eraser for light corrosion.
2. Confirm the LED glows white on a wall outlet and the brick gets warm in use.
3. If you have access to another Surface charger, test with it — even post-upgrade, hardware can fail coincidentally.

### Fix 7: Try USB-C charging as a workaround

1. If your Surface Laptop model supports USB-C PD charging, connect a 65W USB-C PD charger with a rated cable.
2. If USB-C charges but Surface Connect doesn't, the magnetic port or its circuitry is the fault — useful evidence for a service claim.
3. Our [USB-C charging guide](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/) covers wattage and cable requirements.

### Fix 8: Check the battery report and consider service

1. Run `powercfg /batteryreport` in **Terminal (Admin)** and compare full charge capacity to design capacity.
2. If the battery is healthy but nothing charges it, and the connector is clean, the charging circuitry may have failed — Surface devices aren't user-serviceable, so contact Microsoft support with your diagnostic results in hand.

## Closing

A Surface that stops charging right after the Windows 11 upgrade is telling you exactly what happened: the upgrade changed the software, so the software is where the fix lives. Fresh Surface drivers, the UEFI battery limit check, and an EC reset resolve nearly all of them — no hardware heroics required. Save the connector cleaning for the cases where the timing is just coincidence. And if you upgraded recently, don't wait weeks hoping it fixes itself; driver issues don't self-heal, but they do take five minutes to fix. Check the drivers today and get back to a laptop that charges like it should. The fix is quick, free, and permanent — there's no reason to live with a Surface that won't charge.

Related: [Surface not charging on Windows 10](/articles/how-to-fix-surface-laptop-battery-not-charging-on-windows-10/) and [USB-C charging not working](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/).
