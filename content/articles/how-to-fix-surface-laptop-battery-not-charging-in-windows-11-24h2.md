---
title: "Fix Surface Laptop Battery Not Charging on Windows 11 24H2"
slug: how-to-fix-surface-laptop-battery-not-charging-in-windows-11-24h2
date: 2026-10-03
categories: ["battery"]
tags: ["battery", "charging", "surface", "windows 11 24h2"]
description: "Surface Laptop won't charge on Windows 11 24H2? Follow 7 step-by-step fixes, from Surface UEFI settings and driver resets to Smart Charging and firmware updates."
thumbnail: "/images/thumbs/how-to-fix-surface-laptop-battery-not-charging-in-windows-11-24h2.webp"
faqs:
  - q: "Why won't my Surface Laptop charge after the Windows 11 24H2 update?"
    a: "The 24H2 update can corrupt the Surface battery drivers, reset UEFI charge settings, or re-enable Microsoft's Smart Charging feature that pauses charging at a limit. It can also leave the Surface UEFI battery limit in place. Working through driver reinstallation, UEFI checks, and firmware updates in order resolves it for most users."
  - q: "Is it normal for a Surface Laptop to stop charging at 80 percent?"
    a: "Yes, if Smart Charging is active. Microsoft enables it automatically on some Surface devices to extend battery lifespan, pausing charging around 50 or 80 percent. You can turn it off in the Surface app under Battery & charging if you need a full 100 percent charge."
  - q: "How do I check the battery health on a Surface Laptop?"
    a: "Open an administrator Command Prompt and run powercfg /batteryreport, then open battery-report.html from your user folder. Compare Design Capacity with Full Charge Capacity. If the full charge figure has dropped to 70 percent or less of the design figure, the battery is significantly degraded."
  - q: "Can I reset the Surface UEFI to fix battery charging?"
    a: "You can check the UEFI, but resetting it to defaults rarely fixes charging on its own. Hold the volume-up button while pressing power to enter UEFI, then verify the battery limit option isn't enabled. Update the Surface UEFI firmware through Windows Update or the Surface driver package instead."
---

Your Surface Laptop was charging perfectly yesterday, and now the battery icon on Windows 11 24H2 sits stubbornly at the same percentage no matter how long the charger stays plugged in. Sometimes the tooltip says "Plugged in" without the charging indicator, and sometimes the percentage actually drops while connected to the wall. Because Surface devices have sealed batteries and a tightly integrated charging system, this feels alarming — but the cause is very often software, not a dead battery.

The 24H2 feature update changed enough under the hood — driver stacks, power management services, and firmware handoffs — that Surface devices are among the most affected. Corrupted Surface battery drivers, a UEFI battery limit left enabled, Microsoft's Smart Charging pausing the charge, and outdated Surface firmware are the usual suspects. Work through the seven fixes below in order, and check charging after each one.

## Why this happens

- **Corrupted Surface battery drivers.** The 24H2 update frequently corrupts the Microsoft ACPI-Compliant Control Method Battery driver and Surface-specific battery drivers, so Windows reports the wrong charge state or stops requesting charge current.
- **Smart Charging is pausing the charge.** Microsoft's Smart Charging feature intentionally holds the battery at a partial charge (often 50% or 80%) to prolong lifespan. After an update it can re-enable itself or misbehave.
- **Surface UEFI battery limit is enabled.** Some Surface devices expose a battery limit in UEFI that caps charging at 50%. If it got enabled during a firmware update, your Surface will never charge past that point.
- **A damaged or mismatched Surface Connect charger.** Surface devices use a proprietary Surface Connect magnetic connector. A frayed cable, a failing power brick, or a non-Microsoft adapter can run the device without charging it.
- **Outdated Surface firmware.** The embedded controller that manages charging is updated through Surface firmware packages. If firmware didn't install cleanly during the 24H2 upgrade, the charging circuitry can misbehave.
- **Battery calibration drift.** When Windows loses track of the battery's true capacity, it can display a frozen percentage or refuse to charge past an artificial ceiling.

## How to fix it

Work through these in order, checking whether the battery charges after each fix.

### Fix 1: Inspect the Surface Connect charger and port

Start with hardware, because a failing charger mimics every software symptom in this guide.

1. Unplug the Surface Connect cable and inspect the magnetic connector for bent pins, debris, or discoloration. Look along the cable for kinks or fraying, especially near the brick.
2. Blow out the Surface Connect port on the laptop with compressed air — dust and pocket lint collect in the magnetic socket.
3. Plug the charger into a wall outlet directly, skipping power strips and docking stations, and make sure the white LED on the connector lights up.
4. If you have access to another genuine Surface charger with equal or higher wattage, test with it. If charging resumes, your original adapter is the problem. [Learn how to check battery health on Windows 11](/articles/how-to-check-battery-health-on-windows-11-laptop/) to rule out a worn battery at the same time.

### Fix 2: Reinstall the battery drivers in Device Manager

This is the single most effective software fix after the 24H2 update.

1. Right-click the **Start** button and open **Device Manager**.
2. Expand the **Batteries** section.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and select **Uninstall device**, then confirm.
4. If you see a **Surface Battery** entry, uninstall that too.
5. Right-click **Microsoft AC Adapter** and uninstall it the same way.
6. Shut down the Surface completely — hold **Shift** while clicking **Shut down** to bypass fast startup — wait 30 seconds, then power it on.
7. Windows reinstalls the drivers during boot. Plug in the charger and watch the battery icon for the charging indicator.

### Fix 3: Check Smart Charging in the Surface app

Smart Charging can look identical to a charging failure, so verify it before going deeper.

1. Open the **Surface** app (install it from the Microsoft Store if it's missing).
2. Go to **Battery & charging** or **Device information**, depending on your model.
3. Look for the **Smart Charging** toggle. If it's on, your Surface is deliberately pausing the charge to protect the battery.
4. If you need a full charge right now, toggle Smart Charging off. A prompt may warn you about reduced long-term battery lifespan — that's a normal trade-off.
5. If the battery was paused at a limit, it should start charging within a few minutes of disabling the feature.

### Fix 4: Check the battery limit in Surface UEFI

A UEFI-level battery limit caps charging at 50% on supported Surface models.

1. Shut down the Surface completely.
2. Press and hold the **Volume Up** button, then press and release the **Power** button. Keep holding Volume Up until the Surface logo appears, then release it.
3. In the Surface UEFI menu, look for a **Battery** or **Boot configuration** section containing a battery limit option.
4. If the limit is enabled, turn it off, then select **Exit > Restart Now**.
5. After booting back into Windows 11, plug in the charger and confirm the battery climbs past the previous ceiling. For more on interpreting battery numbers, [generate a battery report with powercfg](/articles/how-to-generate-battery-report-windows-11-powercfg/).

### Fix 5: Install the latest Surface firmware and drivers

Surface firmware updates are delivered through Windows Update, but the standalone driver package can fix a botched install.

1. Open **Settings > Windows Update** and install every pending update, including optional driver updates under **Advanced options > Optional updates**.
2. Restart when prompted, then check charging again.
3. If Windows Update finds nothing new, download the Surface driver and firmware MSI for your exact model from [Microsoft's support site](https://support.microsoft.com/en-us/windows) and run it with the charger connected.
4. After the firmware install completes and the device restarts, give it one full charge cycle to settle.

### Fix 6: Run the battery down and recalibrate

Calibration drift can freeze the reported percentage even when charging works.

1. With the charger unplugged, use the Surface normally until it reaches about 10–15%. Don't let it die completely.
2. Plug in the original charger and let it charge uninterrupted to 100% — don't use the device while it charges.
3. Leave it plugged in at 100% for another 30 minutes so the charge controller can top off the cells.
4. Unplug and use the Surface on battery for a while, watching whether the percentage now falls smoothly. A detailed walkthrough is in [this laptop battery calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 7: Perform a two-button shutdown and reset power states

A two-button shutdown clears stuck power states on Surface hardware.

1. Shut down the Surface normally.
2. Press and hold the **Power** button for 30 seconds (on some models, hold **Power + Volume Up** together for 15 seconds).
3. Release, wait 10 seconds, then press **Power** once to boot.
4. Open **Settings > System > Power & battery** and confirm the battery status now updates in real time while charging.

## Closing

Most Surface charging problems on Windows 11 24H2 come down to corrupted drivers, Smart Charging, or a UEFI battery limit — all fixable without opening the device. If you've worked through every fix and the battery still won't charge with a known-good charger, run a battery report and compare capacities: a worn cell pack needs a service appointment, and Surface batteries are sealed, so don't attempt a DIY replacement.
