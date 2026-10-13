---
title: "How to Fix an Acer Laptop Battery Not Charging"
slug: how-to-fix-acer-laptop-battery-not-charging-youtube
date: 2026-09-13
categories: ["battery"]
tags: ["acer battery not charging", "acer plugged in not charging", "acer care center"]
description: "Acer laptop says plugged in but the battery won't charge? Fix it with Acer Care Center checks, battery resets, and charger diagnostics."
thumbnail: "/images/thumbs/how-to-fix-acer-laptop-battery-not-charging-youtube.webp"
faqs:
  - q: "Why is my Acer laptop plugged in but not charging?"
    a: "Common causes include a battery charge limit set in Acer Care Center, a worn battery that refuses charge, a failing or underpowered adapter, corrupted ACPI battery drivers, or the embedded controller locking up. Acer's charge-limit feature is the first thing to check because it looks exactly like a fault."
  - q: "Where is the battery charge limit on an Acer?"
    a: "Open Acer Care Center (or AcerSense on newer models), go to the battery or Battery Health section, and look for the charge limit option. If it's set to 80% or a similar cap, the battery will stop there by design. Set it back to 100% if you need full charges."
  - q: "How do I reset the battery on my Acer laptop?"
    a: "Shut down, unplug the charger and all peripherals, then press and hold the power button for 30 seconds. If your model has a battery reset pinhole on the bottom, press it with a paperclip for 5 seconds. Reconnect the charger and power on."
  - q: "My Acer battery is not detected at all. Is it dead?"
    a: "Not necessarily. Try the battery reset pinhole procedure and reinstall the Microsoft ACPI-Compliant Control Method Battery driver in Device Manager first. If the battery is still invisible after a BIOS update and a reset, then it's likely a hardware failure — check warranty status on Acer's support site."
---

"Plugged in, not charging" on an Acer has a few brand-specific twists that generic guides skip. Acer Care Center can silently cap your charge level, many Acer models hide a battery reset pinhole on the bottom panel, and Acer's BIOS updates frequently carry battery-logic fixes. Here's the order that actually resolves it.

Start with the software limit — it takes thirty seconds to check and it's the most common cause by far.

## Why this happens

- **Acer's battery charge limit is enabled.** Acer Care Center and AcerSense let you cap charging at 80% to extend battery lifespan. When it's on, the battery parks at the cap and Windows reports "not charging," which looks broken but is intentional.
- **The embedded controller locked up.** The EC handles charge negotiation, and it can freeze after power events — the pinhole reset exists precisely for this.
- **The adapter is failing or underpowered.** Acer gaming laptops need high-wattage bricks; a 65W adapter on a machine that wants 135W+ may run the laptop without charging the battery.
- **ACPI battery drivers are corrupted.** Windows talks to the battery through the Microsoft ACPI-Compliant Control Method Battery driver, and it breaks often enough that reinstalling it is standard practice.
- **The battery is genuinely worn.** Cells that have lost most of their capacity can refuse charge entirely, especially if one cell in the pack has failed.
- **BIOS battery logic is outdated.** Acer ships charging-behavior fixes in BIOS updates that Windows Update doesn't deliver.

## How to fix it

Work through these in order — Fix 1 alone resolves a large share of cases.

### Fix 1: Check the charge limit in Acer Care Center

1. Open **Acer Care Center** from the Start menu (on newer models, open **AcerSense** instead).
2. Go to the **Battery** or **Battery Health** section.
3. Look for a **charge limit** or **battery charge threshold** option — if it's set to 80% or similar, that's your "not charging."
4. Set it to **100%** (or disable the limit) if you need full charges, then watch the battery for a few minutes.
5. Keep the limit on if you mostly use the laptop plugged in — it's genuinely good for longevity. Our guide to [limiting charge to 80%](/articles/how-to-limit-battery-charge-to-80/) explains the tradeoff.

### Fix 2: Do the Acer battery reset

1. Shut the laptop down completely and unplug the charger and all USB devices.
2. Flip the laptop over and look for a small **battery reset pinhole** (many Acer models have one — check your manual if unsure).
3. Straighten a paperclip, press it gently into the pinhole, and hold for **5 seconds**.
4. If there's no pinhole: press and hold the **Power** button for **30 seconds** with everything unplugged.
5. Reconnect only the charger, wait a minute, then power on and check the charging status.

### Fix 3: Verify the charger and port

1. Confirm the adapter wattage on its label matches what your model requires — gaming models often need 135W or more, and an underpowered brick causes exactly this symptom.
2. Inspect the DC jack or USB-C port for looseness, debris, or bent contacts.
3. Try a different wall outlet with no power strip in between.
4. Check the charger's LED (if it has one) — no light means no power, even if the laptop detects the plug.
5. If you have access to a known-good Acer adapter of the correct wattage, test a full charge cycle with it.

### Fix 4: Reinstall the battery drivers

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. Do the same for **Microsoft AC Adapter** if listed.
4. Shut down (don't restart — do a full shutdown).
5. Unplug the charger, wait 30 seconds, plug it back in, then power on. Windows reinstalls both drivers fresh during boot.
6. Check the battery icon after a few minutes. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents these Device Manager recovery steps if you want the official reference.

### Fix 5: Run Acer's built-in battery diagnostics

1. Open **Acer Care Center** and go to **Checkup** or **Battery Check**.
2. Run the battery health test and note the reported condition and capacity.
3. If Care Center reports the battery as poor or failed, that's a definitive answer — software won't fix it.
4. Cross-check with a Windows battery report: in an elevated terminal run `powercfg /batteryreport /output "C:\battery-report.html"` and compare **Full Charge Capacity** against **Design Capacity** (see our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/)).

### Fix 6: Update the BIOS from Acer's support site

1. Find your exact model on Acer's official support site via serial-number lookup (the most reliable way to get the right files).
2. Download the latest **BIOS** and read the release notes for battery or charging mentions.
3. Connect the charger, close all apps, and run the BIOS updater exactly as instructed — don't interrupt it.
4. After the update, recheck the charge limit in Acer Care Center (BIOS updates sometimes reset it) and test charging.

### Fix 7: Calibrate or replace the battery

1. If the battery charges but the percentage behaves erratically, run a calibration: full charge, two-hour rest plugged in, discharge to ~5% through normal use, then an uninterrupted recharge to 100%.
2. If calibration fails and capacity is under 60% of design, the battery needs replacing — follow our [worn-battery guide](/articles/how-to-fix-laptop-battery-won-t-hold-charge-youtube/) for the replacement decision.
3. For internal batteries, use Acer's service manual or an authorized shop; for removable ones, match the exact part number on the battery label.
4. If the laptop is under warranty, contact Acer support before opening anything — a failed battery is often covered.

## Closing

On Acer laptops, always check the Care Center charge limit first — it's designed to look like a fault when it's working as intended. After that, the pinhole reset, a driver reinstall, and a genuine-wattage charger test resolve nearly everything else. Only when the capacity numbers themselves have collapsed is it truly a dead battery.
