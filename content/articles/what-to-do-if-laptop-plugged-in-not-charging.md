---
title: "Plugged In, Not Charging? Here's What to Do"
slug: what-to-do-if-laptop-plugged-in-not-charging
date: 2026-09-04
categories: ["battery"]
tags: ["not charging", "charger", "troubleshooting"]
description: "Laptop says 'plugged in, not charging'? Diagnose the charger, drivers, charge limits, and battery — and get charging again."
thumbnail: "/images/thumbs/what-to-do-if-laptop-plugged-in-not-charging.webp"
faqs:
  - q: "What does 'plugged in, not charging' actually mean?"
    a: "Windows detects the charger but no charge current is flowing into the battery. Sometimes this is intentional — a charge limit like Lenovo conservation mode or ASUS's 80% cap deliberately holds the charge. Other times it's a real fault: bad charger, driver issue, worn battery, or overheating protection."
  - q: "Is it bad to use a laptop that's plugged in but not charging?"
    a: "Not harmful — the laptop runs directly off the charger. The risk is practical: with no battery reserve, any power blip shuts the machine down instantly. And if the cause is a failing battery rather than a setting, it's worth diagnosing rather than ignoring."
  - q: "Can a Windows update cause 'plugged in, not charging'?"
    a: "Yes. Driver updates to the ACPI battery driver or chipset, and occasionally BIOS updates, can break charging until fixed with a driver reinstall or a subsequent update. If it started right after an update, that's your prime suspect."
  - q: "Should I try a different charger?"
    a: "Yes — it's the fastest single test. Borrow an original-spec charger (same wattage or higher) and see if charging resumes. If it does, your charger or cable is the problem, which is the cheapest fix on this entire list."
---

"Plugged in, not charging" is Windows shrugging at you: it sees the charger, but the battery isn't taking on charge. Before you panic, know that this message is sometimes completely intentional — charge-limit features deliberately produce exactly this status. The trick is distinguishing "working as designed" from "actually broken," and then, if it's broken, figuring out which link in the chain failed: the charger, the cable, the drivers, the settings, or the battery itself.

This guide runs that triage in the order a repair tech would: rule out intentional limits first, then test the power path, then drivers, then the battery. For the deeper diagnostic version of this problem, see [troubleshooting plugged in, not charging](/articles/troubleshoot-laptop-plugged-in-not-charging/).

## Why this happens

- **Intentional charge limits:** Lenovo Conservation Mode (~60%), ASUS Battery Health Charging (80%/60%), Dell adaptive settings, and Surface Smart Charging all deliberately stop charging — and Windows reports it as "not charging."
- **Underpowered charger:** A charger with too little wattage can run the laptop but not charge the battery simultaneously.
- **Faulty charger or cable:** Dead bricks, frayed cables, and loose USB-C connections deliver no (or intermittent) power.
- **Driver corruption:** The ACPI battery driver or chipset driver can break charging after updates.
- **Overheating protection:** Many laptops refuse to charge when the battery or system is too hot, resuming when it cools.
- **Worn or failed battery:** A pack the system has deemed unsafe or fully worn may be blocked from charging entirely.

## How to fix it

Work through these in order — check the intentional causes before assuming a fault.

### Fix 1: Check for charge-limit features first

The most common "false alarm."

1. **Lenovo:** Open Vantage > Device > Power — if **Conservation Mode** is on, the battery deliberately stops around 60%. Turn it off if you need a full charge.
2. **ASUS:** MyASUS > Battery Health Charging — Balanced (80%) and Maximum Lifespan (60%) modes both show "not charging" at their caps.
3. **Dell:** Dell Power Manager > Battery Settings — Adaptive or custom thresholds do the same.
4. **HP:** BIOS > Battery Health Manager set to "Let HP Manage" can limit charging.
5. **Surface:** Smart Charging pauses at 80% by design on supported devices.
6. If any of these is active and the battery sits at the cap percentage, everything is working correctly — no fix needed.

### Fix 2: Test with a different charger and outlet

Isolate the power path.

1. Borrow or buy a charger matching your laptop's original wattage (higher is fine, lower is not) and test — if charging resumes, your old charger or cable is dead.
2. Try a wall outlet directly, skipping power strips, extension cords, and surge protectors.
3. Inspect the cable along its full length for kinks, fraying, or crushed sections; check the connector for bent pins or debris.
4. For USB-C charging, try a different USB-C port on the laptop — some ports charge, some don't, and one may be damaged.
5. Wiggle the connector gently while watching the taskbar icon — flickering between charging/not charging means a loose port or plug.

### Fix 3: Cool the machine down

Heat-triggered charge blocking is more common than people think.

1. Feel the laptop: if it's very hot, unplug and let it cool for 20-30 minutes with vents clear.
2. Check whether charging resumes once temperatures drop — many laptops block charging above ~45-50°C battery temperature as a safety measure.
3. Clean dust from vents with compressed air; sustained heat during charging often traces back to clogged cooling.
4. Don't charge on insulating surfaces (beds, couches) — this alone causes heat-blocked charging.
5. If overheating is the pattern, our [charging-overheating guide](/articles/how-to-fix-laptop-overheating-while-charging/) covers the full thermal workup.

### Fix 4: Reinstall the battery drivers

Fix the software path.

1. Open **Device Manager > Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
2. Shut down fully (not restart), disconnect the charger for 60 seconds, then reconnect and power on — Windows reinstalls the driver fresh.
3. Also update chipset drivers under **Device Manager > System devices**, or via your OEM's support site.
4. Check **Windows Update** for pending driver updates that might contain the actual fix.
5. If charging broke right after a specific driver update, use **Device Manager > driver Properties > Roll Back Driver** on the suspect.

### Fix 5: Reset the embedded controller

Clear a latched charge-block state.

1. Shut down, unplug everything including the charger.
2. Hold the power button for **30 seconds** to drain residual power and reset the EC.
3. Reconnect the charger (laptop still off) and wait 5 minutes — many machines show a charging LED even when off; its behavior is diagnostic.
4. Power on and check the taskbar status.
5. The EC governs charging at the firmware level, so this reset resolves blocks that no driver reinstall can touch.

### Fix 6: Check battery health and temperature blocks

See what the battery itself reports.

1. Run `powercfg /batteryreport` in an elevated prompt and check wear — a pack at extreme wear may be blocked from charging as a safety measure.
2. In your OEM app (Vantage, MyASUS, SupportAssist, HP diagnostics), run the battery health test — it reports temperature faults and cell failures Windows doesn't show.
3. If the battery is swollen, hot, or smells sweet/chemical, stop troubleshooting and replace it — do not keep trying to charge a damaged pack.
4. Some BIOS setups show battery status and temperature directly — check there for a definitive hardware verdict.
5. For the wear workup, see [dealing with high battery wear](/articles/best-way-to-fix-battery-wear-level-too-high/).

### Fix 7: Update BIOS as the last software step

When everything else checks out.

1. Check your manufacturer's support site for a **BIOS update** newer than yours — charging-logic fixes are common in changelogs.
2. Flash on AC power following the manufacturer's instructions exactly; don't interrupt it.
3. After the update, test charging from a mid-range percentage (not from full, where limits legitimately block charging).
4. If a BIOS update caused the problem, most manufacturers allow flashing back to the previous version.
5. If nothing here restored charging and the battery tests bad, replacement is the answer — Microsoft's power troubleshooting reference is at [Microsoft Support](https://support.microsoft.com/en-us/windows).

## Closing

"Plugged in, not charging" resolves into one of three stories: a feature doing its job, a power-path problem (charger/cable/port), or a battery/driver/firmware fault. Check the charge limits first — they're the cause more often than anyone expects — then work the power path, and you'll almost always find the answer without spending money on the wrong part.
