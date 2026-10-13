---
title: "Laptop Fan Not Working on Windows 11? Diagnose It Safely"
slug: how-to-fix-laptop-fan-not-working-on-windows-11
date: 2026-09-03
categories: ["drivers"]
tags: ["laptop fan", "overheating", "cooling", "windows 11", "hardware"]
description: "Laptop fan not spinning on Windows 11? Learn when silence is normal, how to test the fan safely, and how to fix control and hardware failures."
thumbnail: "/images/thumbs/how-to-fix-laptop-fan-not-working-on-windows-11.webp"
faqs:
  - q: "Is it normal for my laptop fan to not spin sometimes?"
    a: "Yes, completely. Modern laptops use zero-RPM fan curves — the fans stay off during light use and only spin up when temperatures cross a threshold, typically around 50-60°C. Silence while browsing or typing is normal and desirable. Worry only if the fans stay off under heavy load while the laptop gets hot, or if temperatures climb past 90°C without any fan response."
  - q: "How can I test if my laptop fan is actually broken?"
    a: "Put the system under load — run a game, a benchmark, or a stress test — and listen and feel for airflow at the vents. Monitor temperatures with HWMonitor or HWiNFO: if temps exceed 90°C under load with no fan activity, the fan or its control is faulty. Your manufacturer's built-in diagnostics (F2/F12 at boot) usually include a fan test that's definitive."
  - q: "Can a Windows update stop my laptop fan from working?"
    a: "Indirectly, yes. Updates can break the embedded controller driver or power management driver that governs fan curves, leaving fans stuck off or stuck at one speed. Reinstalling the chipset and power management drivers from your laptop manufacturer's site restores proper fan control. True fan hardware failure doesn't correlate with updates — timing is the diagnostic clue."
  - q: "Is it safe to use my laptop if the fan isn't working?"
    a: "For light tasks with monitoring, briefly. For anything demanding, no — sustained overheating throttles performance and can permanently damage the CPU, GPU, or battery. If the fan is confirmed dead, limit use to light browsing, keep the laptop on a hard cool surface, and arrange repair promptly. Don't run games or renders on a fanless laptop."
---

A silent laptop fan triggers instant anxiety, and rightly so — fans are the only thing standing between your CPU and thermal damage. But here's the thing most guides bury: a fan that isn't spinning is often working exactly as designed. Modern laptops keep fans at zero RPM until temperatures demand cooling. The real question isn't "is the fan spinning?" but "does the fan spin when it should?"

This guide teaches you to answer that question safely, without disassembly. You'll learn the temperature thresholds that matter, how to force a fan test, how to fix the driver and firmware issues that break fan control, and how to recognize the genuine hardware failures. Overheating damage is cumulative and permanent, so getting this diagnosis right matters.

## Why this happens

- **Zero-RPM fan curve by design:** Fans intentionally stay off below ~50-60°C. Silence during light use is normal operation, not failure.
- **Embedded controller driver broken:** The EC firmware/driver that translates temperature into fan speed can break after Windows updates, freezing fans off or at one speed.
- **Power plan set to passive cooling:** Windows' passive cooling policy slows the CPU instead of spinning fans — quiet, but it can look like dead fans under moderate load.
- **Dust-clogged heatsink:** Heavy dust buildup insulates the heatsink; the fan may spin but move no air, or the EC may behave erratically with abnormal temperature readings.
- **Failed fan motor or bearing:** Mechanical failure — the fan doesn't spin even when commanded. Often preceded by grinding or rattling noises.
- **Disconnected fan cable:** The fan's ribbon cable can work loose, especially after drops or amateur repasting attempts.
- **BIOS fan control bug:** Firmware bugs can mismanage fan curves; manufacturers fix these in BIOS updates more often than you'd think.
- **Sensor failure:** A dead temperature sensor feeds the EC garbage data, so it never commands the fans to spin — rare, but it happens.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether the fan should be spinning

1. Install **HWiNFO** or **HWMonitor** (free) and note your CPU temperature at idle.
2. Below ~55°C at idle with no fan noise: normal. Fans should start as load pushes temps past 60-70°C.
3. Now put the system under real load — play a demanding game or run Cinebench — and watch temperatures and listen at the vents.
4. If temps climb past 85-90°C with zero fan activity, you have a genuine problem — continue. If fans spin up and temps stabilize, your laptop is fine and this was a false alarm.

### Fix 2: Run the manufacturer's built-in fan test

1. Restart and enter diagnostics: **F2** on Dell, **F2** on Acer, **F10/F2** on HP, **F12** boot menu on Lenovo — look for hardware diagnostics.
2. Run the **fan test** specifically. These tests command the fan directly, bypassing Windows entirely.
3. If the fan spins in diagnostics, the motor is good and the problem is Windows-side fan control — continue with driver fixes. If it doesn't spin in diagnostics, it's hardware — skip to Fix 7. The [step-by-step fan guide](/articles/how-to-fix-laptop-fan-not-working-step-by-step/) walks through per-brand diagnostics keys.

### Fix 3: Check Windows cooling policy

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **Processor power management > System cooling policy** and set it to **Active** for both battery and plugged-in. Passive policy suppresses fans in favor of throttling.
3. Set the power mode to **Best performance** in Settings > System > Power & battery while testing.
4. Retest under load. An incorrect cooling policy is a common cause of "fans never spin up" on fresh Windows installs. If the policy was already Active and fans still don't respond, the issue is deeper in the driver or firmware chain — Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents additional power and thermal troubleshooting steps for this scenario.

### Fix 4: Reinstall chipset and power management drivers

1. Visit your laptop manufacturer's support site and download the latest **chipset driver** and any **power management** or **thermal framework** driver for your model.
2. Install the chipset driver first, restart, then the power/thermal driver, and restart again.
3. Retest under load. These drivers are the software path between temperature sensors and fan commands — when a Windows update breaks them, fans lose their instructions.

### Fix 5: Update the BIOS

1. Check your current BIOS version (`msinfo32`) against the manufacturer's support site.
2. If a newer BIOS mentions thermal, fan, or EC fixes, install it with the charger connected and nothing else running.
3. After updating, load BIOS defaults once (the update can leave fan tables in an odd state), save, and retest under load. BIOS-level fan curve bugs are a documented fix category across all major brands.

### Fix 6: Clean the cooling system (external only)

1. With the laptop off, blow compressed air **into the exhaust vents** in short bursts to dislodge dust — then blow through the intakes.
2. Hold the fan still with a toothpick through the vent if you can reach it; letting it spin freely from air blasts can damage bearings.
3. Never disassemble the heatsink unless you're experienced — breaking the thermal paste seal without replacing it makes cooling worse. If external cleaning doesn't help and temps stay high, professional cleaning and repasting is the next step, not DIY surgery on a whim.

### Fix 7: Confirm hardware failure and act

1. Fan fails the built-in diagnostics, makes grinding noises, or visibly doesn't spin when commanded: the fan unit needs replacement.
2. Stop heavy workloads immediately — use the laptop only for light tasks on a hard, cool surface until repaired.
3. A replacement fan is usually an inexpensive part; labor is the cost. Check warranty status first — fan failure on a machine under warranty is a free repair. The [24H2 fan troubleshooting guide](/articles/how-to-fix-laptop-fan-not-working-in-windows-11-24h2/) has additional model-specific notes for the latest Windows build.

## Closing

Fan diagnosis is about asking the right question: not "is it spinning?" but "does it spin under load?" Verify with temperatures and the built-in diagnostics before touching anything — you'll either discover normal zero-RPM behavior or get a definitive hardware verdict in minutes. For the software side, cooling policy, chipset drivers, and BIOS updates restore fan control in most cases. And if the fan is truly dead, you'll know quickly enough to protect the machine from heat damage while you arrange the repair.
