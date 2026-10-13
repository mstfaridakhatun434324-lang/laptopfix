---
title: "Laptop Battery Not Charging When Plugged In: A Step-by-Step Diagnostic"
slug: how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step
date: 2026-09-14
categories: ["battery"]
tags: ["battery", "charging", "windows 11", "troubleshooting"]
description: "A methodical step-by-step diagnostic for a laptop that won't charge when plugged in, from outlet to battery, with exact commands."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step.webp"
faqs:
  - q: "My laptop runs on the charger but the battery never charges. What is wrong?"
    a: "The laptop is drawing AC power but the charging circuit is not engaging the battery. The most common causes are a charger that cannot deliver enough wattage, a corrupted battery driver, or a vendor charge-limit feature. Work through the steps in order — the fault usually reveals itself by step four."
  - q: "How do I know if the problem is the charger or the laptop?"
    a: "Test with a different charger of equal or higher wattage from the same brand. If the battery charges with the second charger, your charger is faulty. If neither charges, the problem is in the laptop's port, drivers, settings, or battery. Also try your charger on another compatible laptop if one is available."
  - q: "The charging LED is on but Windows says not charging. Which do I believe?"
    a: "Believe the LED for hardware and Windows for software. An LED that shows charging while Windows disagrees usually means a driver or reporting glitch — reinstall the battery drivers. An LED that stays off or blinks amber while Windows says nothing points to a charger, port, or battery hardware fault."
  - q: "Can dust in the charging port stop charging?"
    a: "Yes, especially with USB-C ports. Lint and dust packed into a USB-C port prevent full contact, and the laptop may negotiate a low-power connection that runs the machine without charging the battery. Power off and carefully clean the port with a wooden toothpick and compressed air."
---

The charger is in. The LED might even be lit. But the percentage does not move — not after ten minutes, not after an hour. This guide is built as a diagnostic sequence: each step tests one link in the charging chain, from the wall outlet to the battery cells, so you find the broken link instead of guessing. Follow it in order and do not skip ahead, because later steps assume earlier ones passed.

Grab your charger, a wall outlet, and about thirty minutes. By the end you will know exactly which component is at fault.

## Why this happens

- **The outlet or power strip is the fault.** Dead outlets, switched-off power strips, and overloaded strips are embarrassingly common and take seconds to rule out.
- **The charger cannot deliver enough power.** A damaged cable, a failing brick, or an underpowered third-party adapter can run the laptop without charging the battery.
- **The charging port is damaged or dirty.** A loose barrel jack or lint-packed USB-C port breaks the connection just enough to stop charging.
- **Battery drivers are corrupted.** Windows reads charging state through the ACPI battery driver; when it corrupts, the reported state freezes.
- **A charge-limit feature is engaged.** Vendor battery-health settings cap charging at 60 or 80 percent, which looks exactly like a charging failure.
- **The battery has failed.** Cells that no longer accept charge, or a tripped protection circuit, end the chain.

## How to fix it

Work through these in order. Each step isolates one link in the chain.

### Fix 1: Verify the wall power

Start at the very beginning of the chain — the outlet.

1. Unplug the charger from the wall and plug in a phone charger or lamp to confirm the outlet is live.
2. Bypass all power strips, extension cords, surge protectors, and UPS units — plug the laptop charger directly into the wall.
3. If the outlet is controlled by a wall switch, make sure the switch is on.
4. Try a second outlet on a different circuit. If charging starts, your outlet or strip was the entire problem.

### Fix 2: Inspect the charger and cable

Most charging failures live in the ten inches of cable near the connectors.

1. Run your fingers along the full cable feeling for kinks, flat spots, or fraying, especially where the cable meets the brick and the laptop plug.
2. Check the brick for swelling, burn smells, or rattling. Any of these means the charger is unsafe — replace it, do not keep using it.
3. Confirm the wattage printed on the brick matches or exceeds your laptop's requirement. A 45W phone-style adapter will not charge a laptop that expects 90W.
4. Gently wiggle the plug at the laptop port. If charging flickers, the cable or the port is failing — note which end causes it.

### Fix 3: Clean and test the charging port

A dirty port is a silent charging killer.

1. Power off the laptop and unplug everything.
2. Shine a light into the charging port. For USB-C, use a wooden or plastic toothpick to gently lift out packed lint — never metal.
3. For barrel-jack ports, check that the center pin is straight and centered.
4. Blow out the port with short bursts of compressed air, then reconnect firmly and check for charging.

### Fix 4: Reinstall the battery drivers

If hardware checks pass, the driver layer is the next suspect.

1. Right-click Start and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Uninstall **Microsoft AC Adapter** the same way.
4. Shut down, unplug the charger for a full 60 seconds, plug back in, and power on.
5. Windows reinstalls the drivers during boot. Check the battery icon for the charging symbol.

### Fix 5: Check for a vendor charge limit

If charging always stops at the same round number, this is your answer.

1. **Lenovo:** Lenovo Vantage > Device > Power — turn off Conservation Mode.
2. **Asus:** MyASUS > Battery Health Charging — select Full capacity mode.
3. **Dell:** Dell Power Manager > Battery Settings — choose Standard.
4. **HP:** BIOS (F10) > Advanced > Power Management Options > Battery Health Manager — select full charge.
5. If you want to keep a limit for battery longevity, our guide to [limiting charge to 80 percent](/articles/how-to-limit-battery-charge-to-80/) explains how to set it deliberately.

### Fix 6: Reset power plans and test with a battery report

Corrupted power schemes and a worn battery are the remaining software and hardware suspects.

1. In **Terminal (Admin)**, run `powercfg /restoredefaultschemes` and restart.
2. Run `powercfg /batteryreport /output "C:\battery-report.html"` and compare full charge capacity with design capacity.
3. If full charge capacity is under 60 percent of design, the battery is worn out — charging circuitry is fine, but the cells cannot accept charge.
4. Our [battery report walkthrough](/articles/how-to-generate-battery-report-windows-11-powercfg/) helps you read the rest of the data.

### Fix 7: Update the BIOS and test with a known-good charger

The last two variables: firmware and a definitive hardware test.

1. Check your BIOS version with `msinfo32` and install the latest BIOS from your manufacturer's support site with the charger connected. For driver-level help, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers the built-in troubleshooters.
2. Borrow a genuine charger of the correct wattage for your brand. If it charges, buy a genuine replacement — third-party adapters cause repeat failures.
3. If a known-good charger, clean port, fresh drivers, and updated BIOS still do not charge, the charging circuit or battery needs professional service.

You now know which link failed: outlet, charger, port, driver, setting, or battery. That is the whole point of going in order — no guessing, no replacing parts blindly.

## Closing

Nine times out of ten, this sequence ends at step two, four, or five: a bad cable, a corrupted driver, or a charge limit nobody remembers enabling. The steps that feel tedious are the ones that save you from buying a battery you did not need.
