---
title: "Laptop Battery Not Charging When Plugged In: Fix Guide"
slug: how-to-fix-laptop-battery-not-charging-when-plugged-in
date: 2026-10-11
categories: ["battery"]
tags: ["not charging", "plugged in", "troubleshooting"]
description: "Plugged in but the battery won't charge? Diagnose the charger, drivers, and settings with this complete step-by-step repair guide."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-when-plugged-in.webp"
faqs:
  - q: "What does 'plugged in, not charging' mean?"
    a: "It means Windows detects the AC adapter but no current is reaching the battery. Common causes: a failing charger, a charge limit set in the manufacturer's app, a stuck battery driver, or a worn-out battery. The fixes below isolate each cause in order."
  - q: "Can a Windows update cause the battery to stop charging?"
    a: "Yes. Feature updates sometimes replace the battery driver with a broken version or reset manufacturer power settings. If charging broke right after an update, reinstalling the battery drivers and checking the manufacturer's battery app usually resolves it."
  - q: "Should I remove the battery to fix charging?"
    a: "On laptops with removable batteries, reseating the battery can help. On sealed modern laptops, don't open the case — you'll void the warranty and risk damaging the battery. All the effective fixes here are software or external hardware checks."
  - q: "How do I know if the charger or the laptop is the problem?"
    a: "Test with a different charger of equal or higher wattage. If a known-good charger works, yours is faulty. If no charger works, the issue is the laptop's port, drivers, or battery. Also check whether the charger works on a different laptop of the same brand."
---
The charger is plugged in, the LED is on, Windows says "plugged in" — but the percentage doesn't move. Or it says "plugged in, not charging" outright. This is the most common laptop battery complaint there is, and the fix is usually simpler than people expect.

Charging involves a chain: wall → brick → cable → port → driver → battery controller → cells. This guide tests each link in order so you find the broken one fast.

## Why this happens

- **Failing charger or cable:** The brick's LED can glow while the cable carries no real current. Chargers die gradually — partial failure looks exactly like this.
- **Charge limit enabled:** Manufacturer apps (Lenovo Vantage, MyASUS, Dell Power Manager) can cap charging at 60–80%. It looks broken, but it's a setting.
- **Stuck battery driver:** The ACPI battery driver can wedge after updates or sleep cycles, reporting "not charging" while everything else is fine.
- **Dirty or loose charging port:** Lint and worn connectors break the electrical contact even when the plug feels seated.
- **Wrong-wattage charger:** A 45W brick on a laptop that needs 90W may show "plugged in" while the battery slowly drains under load.
- **Worn-out battery:** A battery at the end of its life may refuse charge entirely. The controller protects dead cells by blocking charging.
- **Overheated battery:** Charging pauses when the battery is too hot — common during gaming on a soft surface that blocks vents.

## How to fix it

Work through these in order — each step tests one link in the charging chain.

### Fix 1: Check the charger, cable, and outlet

Start with the hardware — it's the most common failure point.

1. Unplug the brick from the wall for 30 seconds, then plug it directly into a wall outlet (not a power strip).
2. Check the brick's LED. No light, or a flickering light, means the charger is dying.
3. Inspect the full cable length for kinks, chew marks, or a loose strain-relief near the brick.
4. Try a different outlet to rule out a dead socket.
5. If you have access to another charger with the **same connector and equal or higher wattage**, test with it.

### Fix 2: Reseat the connection and clean the port

A surprising number of "not charging" cases are just a bad connection.

1. Unplug the charger from the laptop and the wall.
2. Blow out the laptop's charging port with compressed air.
3. Plug the charger firmly into the laptop — it should seat with no wobble.
4. For USB-C charging, try a different USB-C port if your laptop has more than one; not all ports support charging.
5. Wiggle the connector gently while watching the taskbar icon. If charging flickers on and off, the port or cable is worn.

### Fix 3: Check for a charge limit in the manufacturer's app

Before deeper troubleshooting, rule out a deliberate cap.

1. Open your manufacturer's app: **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, **HP Support Assistant**, or **MSI Center**.
2. Look for battery health / charge limit settings (Conservation Mode, Battery Health Charging, charge threshold).
3. If a limit is set (e.g., stops at 60% or 80%), that's why charging "stopped" — it's working as configured.
4. Temporarily disable it to confirm full charging works, then re-enable it if you want the longevity benefit.
5. Our [charge threshold guide for 24H2](/articles/how-to-limit-battery-charge-to-80-percent-in-windows-11-24h2/) explains these settings in depth.

### Fix 4: Reinstall the battery drivers

The classic fix for "plugged in, not charging" — it resolves a huge share of cases.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**.
3. Right-click **Microsoft AC Adapter** and uninstall it too.
4. Shut down the laptop (don't just restart), unplug the charger for 30 seconds, then plug back in and power on.
5. Windows reinstalls both drivers during boot. Check the battery icon after a few minutes.

### Fix 5: Run a power reset (EC reset)

This drains residual charge that can lock up the embedded controller.

1. Shut down the laptop completely and unplug everything, including USB devices.
2. If the battery is removable, take it out. If sealed, skip this.
3. Hold the power button down for **30 seconds**.
4. Reconnect the battery (if removed), plug in the charger, and power on.
5. Check whether charging resumes.

### Fix 6: Check battery health with a report

If charging hardware and drivers are fine, the battery itself may be refusing charge.

1. Open an admin Terminal (**Terminal (Admin)** from right-clicking **Start**).
2. Run `powercfg /batteryreport /output %USERPROFILE%\battery-report.html` and open the file.
3. Compare **FULL CHARGE CAPACITY** to **DESIGN CAPACITY**. Under 50% on an old battery means it's worn out.
4. Also check for sudden shutdowns at 20–30% — a classic dying-cell symptom no driver fix will solve.
5. If wear is the verdict, our [capacity decline guide](/articles/how-to-fix-full-charge-capacity-dropping-in-windows-11-24h2/) covers your options.

### Fix 7: Update the BIOS and chipset drivers

The charging controller is firmware-driven, and updates fix negotiation bugs.

1. Visit your manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)) and check for a newer BIOS.
2. Install it with the charger connected — never update BIOS on battery alone.
3. Also install the latest **chipset drivers** from the same site.
4. Retest charging after the update completes.

### Fix 8: Cool the laptop down

An overheated battery refuses charge as a safety measure.

1. If the laptop is hot, shut it down and let it cool for 20 minutes in a ventilated spot.
2. Elevate the rear for airflow and clean dust from the vents.
3. Avoid charging on beds or couches that block intakes.
4. If charging works when cool but stops when hot, heat — not the charger — is your problem.

## Closing

"Plugged in, not charging" is a chain problem, and the chain usually breaks at the charger, the driver, or a charge-limit setting — in that order. Work the steps, and you'll either be charging again or know exactly which part needs replacing.
