---
title: "What to Do If Your Laptop Battery Is Not Charging When Plugged In"
slug: what-to-do-if-laptop-battery-not-charging-when-plugged-in
date: 2026-10-03
categories: ["battery"]
tags: ["battery not charging", "plugged in", "troubleshooting"]
description: "Laptop plugged in but the battery won't charge? This step-by-step triage finds the cause fast — charger, settings, drivers, or the battery itself."
thumbnail: "/images/thumbs/what-to-do-if-laptop-battery-not-charging-when-plugged-in.webp"
faqs:
  - q: "What should I check first when my laptop won't charge?"
    a: "Check the physical chain first: wall outlet, adapter brick, cable, and the laptop's charging port. Then look at what Windows reports — 'plugged in, not charging' versus no detection at all point to different causes. This order matters because software fixes can't help a dead adapter."
  - q: "How can I tell if it's the charger or the battery?"
    a: "Remove the battery if possible and run on AC power alone — if the laptop runs fine, the charger works and the battery is suspect. Alternatively, test with a known-good charger: if charging resumes, your charger was bad. If neither changes anything, the charging circuit or drivers are likely at fault."
  - q: "Will a Windows update stop my battery from charging?"
    a: "It can. Updates sometimes corrupt the ACPI battery drivers or reset manufacturer charge limits. If charging broke immediately after an update, reinstall the battery drivers in Device Manager and check your manufacturer's battery tool for re-enabled limits before assuming hardware failure."
  - q: "Is 'plugged in, not charging' always a battery problem?"
    a: "No — it's often not the battery at all. Charge limits set to 80%, corrupted drivers, a failing adapter, or a stuck charge controller all produce the same message. Only after ruling those out should you conclude the battery itself has failed."
---

"Plugged in, not charging." Four words that turn your laptop into a desktop. The battery percentage sits frozen, the charger is connected, and nothing you do makes the number move. Before you order a replacement battery — which is the most common and most expensive wrong guess — run through this triage. Most charging failures are fixed without spending anything at all.

Charging failures follow a predictable pattern: power source, then settings, then drivers, then the battery itself. Most people jump straight to the battery and skip the first three, which is why so many replacement batteries "don't fix it." Work this list in order and you'll find the real cause instead of an expensive guess.

## Why this happens

- **Dead or underpowered adapter** — no power in means no charging, regardless of everything else.
- **Charge limit enabled** — manufacturer tools capping the battery at 60–80% look exactly like a charging failure.
- **Corrupted battery drivers** — Windows loses communication with the charging hardware after updates.
- **Stuck charge controller** — the embedded controller latches into a non-charging state.
- **Worn-out battery** — degraded cells can refuse charge entirely.
- **Charging port damage** — a loose or dirty port breaks the connection intermittently or completely.

## How to fix it

Work through these in order — each step eliminates a category.

### Fix 1: Verify power is actually reaching the laptop

Half of all "not charging" cases end here, at the wall outlet or the cable. Be rigorous — assumptions are the enemy, and every minute spent verifying the power chain saves an hour of pointless software troubleshooting.

1. Plug the adapter into a wall outlet you know works (test it with another device). Skip power strips for now.
2. Check for an LED on the adapter brick and a charging LED on the laptop. Note exactly which lights are on.
3. Inspect the cable end to end and the charging port for damage or debris.
4. Push the connector in firmly. If the LED flickers when you wiggle it, the port or plug is worn. No lights anywhere after trying two outlets means the adapter is dead — replace it with the correct wattage for your model.

### Fix 2: Check for a charge limit first

This two-minute check saves people from buying batteries they don't need.

1. Open your manufacturer's battery utility — Lenovo Vantage, Dell Power Manager, MyASUS, Acer Care Center, HP BIOS settings, or the Surface app.
2. Look for any charge cap, conservation mode, or battery health setting limiting the maximum charge.
3. If the battery is sitting exactly at the cap (80%, 60%, whatever's set), that's your answer — the limiter is working as designed.
4. Disable it temporarily to confirm charging resumes, then decide whether to keep it. Our guide to [limit battery charge to 80%](/articles/how-to-limit-battery-charge-to-80/) explains when the cap is actually worth keeping.

### Fix 3: Run on AC power with the battery removed

This classic test separates charger problems from battery problems in a single move.

1. Shut down, unplug, and remove the battery if your model allows it.
2. Plug in the adapter and power on with no battery installed.
3. If the laptop runs fine, the adapter and charging circuit deliver power — the battery is the suspect.
4. If it won't run or behaves erratically on AC alone, the adapter or motherboard charging circuit is at fault. For sealed-battery laptops, skip this test and use Fix 1's adapter swap instead.

### Fix 4: Reset the embedded controller

A stuck controller can block charging while everything else looks normal.

1. Shut down completely and unplug the charger.
2. Remove the battery if removable; otherwise press the pinhole reset button for 10 seconds if present.
3. Hold the power button for 30 seconds to drain residual power.
4. Reconnect everything and boot on AC power. Check whether the battery status changes from "not charging" to "charging."

### Fix 5: Reinstall the battery and adapter drivers

Corrupted drivers are the most common software cause, especially after Windows updates. The ACPI driver is the translator between Windows and your charging hardware — when it corrupts, Windows can see the charger but can't manage charging, producing the exact "plugged in, not charging" message.

1. Right-click **Start**, open **Device Manager**, and expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. Click **Action** > **Scan for hardware changes**, then restart.
4. Windows reinstalls clean drivers and renegotiates with the charging hardware. If an update broke charging, this is usually where it gets fixed.

### Fix 6: Check battery health to judge the battery itself

Only now — after eliminating power, settings, controller, and drivers — is it fair to blame the battery.

1. Open **Command Prompt** as administrator and run `powercfg /batteryreport`.
2. Compare **Design Capacity** with **Full Charge Capacity** in the report.
3. A battery at less than half its design capacity is worn out; learn to [check your battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) properly before buying a replacement.
4. Also check the recent usage history in the report — a battery that drops off a cliff under load has high internal resistance and won't charge reliably.

### Fix 7: Update the BIOS and chipset drivers

Firmware-level charging bugs survive driver resets, and manufacturers fix them in BIOS updates.

1. Note your BIOS version with `msinfo32`.
2. Download the latest BIOS and chipset driver for your exact model from the manufacturer's support site.
3. Install with AC power connected and no other programs running.
4. Retest charging from a cold boot. If your Dell specifically refuses adapters, the [Dell support site](https://www.dell.com/support) documents adapter verification behavior worth reading.

## Closing

"Not charging" is a symptom, not a diagnosis. Power first, then limits, then the controller, then drivers — and only then the battery. Follow that order and you'll fix it with the cheapest possible part, which is usually no part at all. And the next time the message appears, you'll know exactly where to look first.
