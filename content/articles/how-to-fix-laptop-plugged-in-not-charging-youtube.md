---
title: "How to Fix a Laptop That Is Plugged In But Not Charging"
slug: how-to-fix-laptop-plugged-in-not-charging-youtube
date: 2026-10-05
categories: ["battery"]
tags: ["not charging", "plugged in", "charger"]
description: "Laptop says 'plugged in, not charging'? Don't buy a new charger yet — run through these checks first. Most cases are settings, drivers, or the cable."
thumbnail: "/images/thumbs/how-to-fix-laptop-plugged-in-not-charging-youtube.webp"
faqs:
  - q: "What does 'plugged in, not charging' actually mean?"
    a: "Windows sees the charger but has decided not to charge the battery — or can't. Common reasons: a charge threshold capping the battery, a driver glitch, a failing charger delivering too little power, or a worn battery the system has stopped charging for safety."
  - q: "Should I buy a new charger if my laptop won't charge?"
    a: "Not immediately. Test with the steps in this guide first — most 'not charging' cases are software or settings. But if the charger is frayed, the tip is loose, the brick runs cold (no warmth = no power conversion), or a known-good charger works, then yes, replace it with the correct wattage."
  - q: "Can a dirty charging port cause 'not charging'?"
    a: "Yes, especially with USB-C. Lint and dust in a USB-C port prevent full insertion, which can drop the connection to a low-power state or break it intermittently. Power off, then clean the port gently with a wooden toothpick or compressed air."
  - q: "Why does my laptop say not charging at 95%?"
    a: "That's usually normal: many laptops pause charging near full to protect the battery, or a charge threshold is set. It becomes a problem only if the battery is low (say under 80%) and still refuses to charge."
---

"Plugged in, not charging." Six words that ruin your day. The charger is in, the light might even be on, but the percentage sits there mocking you — or worse, slowly dropping. Before you spend money on a new charger or panic about a dead battery, work through this guide. The cause is very often something simple.

The key insight: this message means Windows *sees* the charger. That's actually good news — it narrows the problem to the charging decision (settings, drivers) or the power delivery (charger, cable, port, battery).

## Why this happens

- **A charge threshold is active.** Lenovo Conservation Mode, ASUS Battery Health Charging, or a Dell/HP charge limit stops charging at 60–80% by design. The message looks like an error but it's the feature working.
- **The charger isn't delivering enough power.** A 45W charger on a laptop that wants 65W+, a failing brick, or a loose barrel connector can leave Windows seeing the charger but unable to charge.
- **The battery drivers glitched.** The ACPI driver chain that manages charging can hang after sleep cycles or updates, freezing the charging state.
- **The battery is worn or overheating.** Systems stop charging batteries that report critical wear or high temperature — a safety behavior, not a bug.
- **Dust or damage in the charging port.** Especially USB-C: lint prevents full insertion, the laptop negotiates a weak connection, and charging stalls or never starts.

## How to fix it

Work through these in order — check the easy stuff before spending money.

### Fix 1: Check for a charge limiter first

This is the most common "not charging" cause and the easiest to miss.

1. Note the exact percentage. Stuck at 55–60%? That's **Lenovo Conservation Mode**. At 80%? **ASUS Battery Health Charging** or a Dell/HP threshold.
2. Open **Lenovo Vantage**, **Dell Power Manager**, **MyASUS**, or **HP Support Assistant** and look for the limiter.
3. Turn it off (or switch to full-capacity mode) and watch for 2–3 minutes. If charging resumes, mystery solved — it was working as designed.
4. If you want the limiter for battery health but need a full charge today, disable it temporarily, charge to 100%, then re-enable it.

### Fix 2: Inspect the charger, cable, and port

Physical problems cause a huge share of charging failures.

1. Unplug everything and inspect the full length of the cable for frays, kinks, or chew marks. Check the connector tip for bent pins (barrel) or debris (USB-C).
2. Feel the brick after it's been plugged in for a few minutes — a working adapter gets slightly warm. Stone cold with no LED means it's dead.
3. Clean a USB-C port: power off, then gently remove lint with a wooden toothpick or a blast of compressed air. You'd be amazed how much packs in there.
4. Plug the charger directly into a wall outlet, not a power strip — and try a different outlet. Then firmly reseat both ends of any detachable cable.

### Fix 3: Run the battery down and do a power reset

This clears stuck charging states in the embedded controller.

1. Unplug the charger. If the battery has charge, use the laptop until it drops 10–15%.
2. Shut down fully (hold **Shift** while clicking **Shut down**).
3. Unplug everything, then hold the power button for **30 seconds**.
4. Plug the charger back in (firmly, directly to the wall) and power on. Check whether charging resumes — the EC reset fixes many "stuck" charging states.

### Fix 4: Reinstall the battery drivers

A hung charging driver is the classic software cause.

1. Press **Win + X** > **Device Manager** > **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**. Confirm.
3. Uninstall **Microsoft AC Adapter** as well.
4. Restart with the charger connected. Windows reinstalls fresh drivers on boot.
5. Give it 5 minutes after boot — charging sometimes takes a moment to kick in after a driver reinstall. The dedicated [plugged-in-not-charging walkthrough](/articles/best-way-to-fix-laptop-plugged-in-not-charging/) covers additional driver-level scenarios if this doesn't resolve it.

### Fix 5: Test with the correct wattage

An underpowered charger is a sneaky cause — the laptop sees it, tries, and gives up.

1. Check the wattage printed on your original charger (e.g., 65W, 90W, 130W).
2. If you're using a replacement, dock, or phone charger, verify it meets or exceeds the original wattage. A 45W USB-C charger will not properly charge a 90W laptop.
3. USB-C docks are frequent culprits: many deliver only 60W pass-through even when the dock's own brick is bigger. Try the laptop's original charger directly.
4. If you have access to a known-good charger of the correct wattage, test with it. Charging resumes = your charger is the problem, not the laptop.

### Fix 6: Check battery health and temperature

The system deliberately stops charging unsafe batteries.

1. Open **Terminal (Admin)** and run `powercfg /batteryreport`. Compare **Design Capacity** to **Full Charge Capacity** — under 60–70% is heavily worn.
2. Feel the battery area. If it's very hot, let the laptop cool completely (powered off, 30+ minutes) and try charging again in a cool room.
3. Check for swelling: a bulging bottom panel or raised trackpad means stop immediately and replace the battery — don't keep trying to charge a swollen pack.
4. If the battery is worn but not dangerous, the laptop may charge it slowly or intermittently. That's the system protecting you — plan a replacement.

### Fix 7: Update the BIOS

Charging logic lives partly in firmware, and BIOS updates fix charging bugs regularly.

1. Check your BIOS version with `msinfo32`.
2. Download the latest BIOS for your exact model from [Dell](https://www.dell.com/support), [Lenovo](https://support.lenovo.com/us/en/), or [HP](https://support.hp.com/us-en).
3. Install with the charger connected. After the restart, check the charging status.
4. If charging broke immediately after a *previous* BIOS update, look for a hotfix BIOS on the support page — and see [battery not charging after BIOS update](/articles/battery-not-charging-after-bios-update-troubleshooting/).

## Closing

"Plugged in, not charging" is a decision Windows made — and decisions can be unmade. Check the charge limiter, inspect the charger and port, reset the embedded controller, reinstall the drivers, and verify wattage before spending a cent. In most cases the fix is one of the first four steps. When it isn't, the battery report and a BIOS update will tell you whether you're looking at a worn battery or a firmware quirk — either way, you'll know what to do next.
