---
title: "How to Fix a Laptop Battery Stuck at 50% While Charging"
slug: how-to-fix-battery-stuck-at-50-percent-charging-reddit
date: 2026-09-09
categories: ["battery"]
tags: ["battery stuck", "charge limit", "battery threshold", "not charging to 100"]
description: "Laptop battery stuck at 50% and won't charge further? It's usually a charge limit setting, not a broken battery. Here's how to find and fix it."
thumbnail: "/images/thumbs/how-to-fix-battery-stuck-at-50-percent-charging-reddit.webp"
faqs:
  - q: "Why is my battery stuck at 50% and says 'plugged in'?"
    a: "In most cases a charge limit is active — many laptops ship with a battery-preservation mode that caps charging at 50, 60, or 80 percent to extend battery lifespan. ASUS calls it Battery Health Charging, Lenovo calls it Conservation Mode, and Dell has a similar setting. The battery isn't broken; it's being deliberately held there. Check your manufacturer's battery app first."
  - q: "Is it bad to remove the 50% charge limit?"
    a: "Not bad, just a trade-off. Charge limits exist because lithium batteries degrade faster when held at 100% for long periods. If you mostly use the laptop plugged in at a desk, keeping a 50-80% limit will noticeably extend the battery's lifespan. If you need full runtime for travel, turn the limit off — that's exactly what it's designed for."
  - q: "My battery is stuck at 50% but I never set a limit. Why?"
    a: "Some manufacturers enable a limit by default, or it gets switched on during a driver/BIOS update. A few laptops also misreport the percentage when the battery gauge is out of calibration — the battery is actually fuller or emptier than 50% and the gauge is just wrong. Running a full calibration cycle (charge to 100, drain to empty, recharge) usually corrects a drifting gauge."
  - q: "Can a weak charger cause the battery to stick at 50%?"
    a: "Yes, though it's less common than a limit setting. If the charger can't supply enough wattage to both run the laptop and charge the battery, charging can stall partway — the system prioritizes running the machine. If you're using a third-party or USB-C charger, try the original charger and see if the percentage climbs past the stuck point."
---

Your laptop sits at exactly 50% — plugged in, "charging," for hours — and the number never moves. Unplug it and it drains normally. Plug it back in and it climbs right back to 50% and stops dead. It feels like the battery is broken in a very specific, suspicious way.

Here's the twist: a battery stuck at a round number like 50% is almost never a broken battery. It's your laptop doing exactly what it was told to do. Modern laptops include battery-preservation features that cap charging at 50%, 60%, or 80% to make the battery last years longer — and these limits get switched on by default, by updates, or by accident far more often than people realize.

## Why this happens

- **Manufacturer charge limit enabled.** ASUS Battery Health Charging (Balanced mode = 80%, Maximum lifespan = 60%), Lenovo Conservation Mode (60%), MSI's battery health options, and Dell's adaptive charging all cap the percentage.
- **Limit turned on by an update.** BIOS or driver updates sometimes reset or enable these modes without asking.
- **Battery gauge miscalibration.** The fuel gauge chip drifts over time and reports 50% when the true charge is different — the number is wrong, not the charging.
- **Underpowered charger.** A weak charger can stall charging partway when the laptop's power draw eats everything the charger provides.
- **Windows "Smart charging."** On supported devices (mainly Surface), Windows itself pauses charging at a limit to protect the battery.
- **Failing battery cell.** Rare at exactly 50%, but a battery with a dead cell group can plateau — usually accompanied by sudden shutdowns, though.

## How to fix it

Work through these in order, starting with the easiest. Stop when your issue is resolved.

### Fix 1: Check your manufacturer's battery app for a charge limit

This is the cause in the large majority of cases. The setting hides in a different app on every brand.

1. **ASUS:** Open **MyASUS > Battery Health Charging** and check whether it's set to Balanced (80%) or Maximum lifespan (60%). Set it to **Full capacity mode** for 100%.
2. **Lenovo:** Open **Lenovo Vantage > Device > Power** and turn off **Conservation Mode** (caps at ~60%). Check **Battery Settings** for a custom charge threshold too.
3. **Dell:** Open **Dell Power Manager > Battery Settings** and switch from Adaptive or "Primarily AC Use" to **Standard**.
4. **MSI:** Open **MSI Center > Features > Battery Health Option** and select **Best for Mobility** (100%).
5. **HP:** Restart into BIOS (**F10**) and check **Advanced > Power Management Options > Battery Health Manager** — set it to **Let HP Manage My Charging** or disable the limit.
6. After changing the setting, keep the charger plugged in for 30 minutes and watch whether the percentage climbs past 50%.

### Fix 2: Check Windows Smart charging (Surface and supported devices)

Windows itself can hold the charge below 100% on some hardware.

1. Open **Settings > System > Power & battery**.
2. Look for a **Smart charging** section or notice.
3. If it's active and holding your battery at a limit, you can pause it when you need a full charge — the option appears on the same page.
4. Note that Smart charging is automatic and adaptive; it learns your routine and isn't a malfunction.

### Fix 3: Rule out a weak charger

Before assuming software, make sure the charger can actually finish the job.

1. Check the wattage on your original charger and on the one you're using.
2. Switch to the **original charger** that came with the laptop.
3. Plug in and leave the laptop alone (or shut it down) for an hour.
4. If the percentage now climbs past 50%, your everyday charger is underpowered — replace it with one matching the original wattage.

### Fix 4: Reinstall the battery drivers

A confused driver can freeze the reported percentage even while the battery keeps charging underneath.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click each **Microsoft ACPI-Compliant Control Method Battery** entry, and choose **Uninstall device**.
3. Shut down fully, unplug for 30 seconds, then boot back up.
4. Windows reinstalls the drivers — check whether the percentage now moves normally.

### Fix 5: Calibrate the battery gauge

If the gauge is lying about 50%, a full calibration cycle teaches it the battery's real capacity.

1. Charge the laptop to whatever maximum it currently allows, then keep it plugged in for 2 extra hours.
2. Unplug and use the laptop normally until it shuts itself off from low battery.
3. Leave it off and unplugged for 3–5 hours (this lets the cells settle).
4. Plug in and charge **uninterrupted** to 100% (or to your set limit).
5. The reported percentage should now track reality. You can read more about the process in our [battery calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 6: Update the BIOS

Battery threshold behavior is controlled by firmware, and updates fix threshold bugs regularly.

1. Find your model at **Settings > System > About**.
2. Download the latest BIOS from the manufacturer's support site.
3. Install with the charger connected and don't interrupt the process.
4. After rebooting, re-check the battery app from Fix 1 — updates sometimes reset the threshold, so confirm it's set the way you want.

### Fix 7: Check the battery's true health with a report

If nothing above moves the needle, verify the battery itself is healthy.

1. Open **Terminal (Admin)** and run `powercfg /batteryreport`.
2. Open the report and compare **Design Capacity** to **Full Charge Capacity**.
3. If full charge capacity is close to design capacity, the battery is fine — the stall is definitely a limit or gauge issue, so revisit Fixes 1 and 5.
4. If capacity has collapsed (say, under 50% of design), the battery is worn out and plateauing because it genuinely can't hold more — replacement is the fix. Our guide on [checking battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) walks through reading the report.

## Closing

A battery parked at exactly 50% is your laptop protecting itself, not failing — some charge-limit feature is doing its job a little too well. Find the setting in your manufacturer's app, decide whether you want the longevity benefit or the full runtime, and set it deliberately instead of wondering why the number never moves.
