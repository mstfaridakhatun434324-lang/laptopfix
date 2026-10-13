---
title: "Laptop Battery Not Charging When Plugged In? Troubleshoot It"
slug: troubleshoot-laptop-battery-not-charging-when-plugged-in
date: 2026-09-22
categories: ["battery"]
tags: ["not charging", "plugged in not charging", "troubleshooting", "diagnosis"]
description: "Plugged in, not charging? Systematically isolate whether it's the charger, the port, Windows, or the battery with this diagnostic walkthrough."
thumbnail: "/images/thumbs/troubleshoot-laptop-battery-not-charging-when-plugged-in.webp"
faqs:
  - q: "What does 'plugged in, not charging' mean?"
    a: "Windows detects AC power but the battery isn't accepting charge. It can mean the charger can't deliver enough power, a charge limiter is active (Lenovo Conservation Mode, ASUS 80% cap), the battery driver is corrupt, the battery is worn out, or the charging circuitry has failed. The diagnostic steps narrow it to one of these."
  - q: "How can I tell if my charger is the problem?"
    a: "Check the wattage on the brick against your laptop's original adapter rating. Inspect the cable and connector for damage. Try a different wall outlet. If you can borrow an identical-wattage charger and charging resumes, yours is faulty. Also watch the charger's behavior under load — a failing brick may work at idle but collapse when the system draws power."
  - q: "Should I uninstall the battery driver?"
    a: "Yes, it's a safe and common fix: Device Manager > Batteries > uninstall Microsoft ACPI-Compliant Control Method Battery, then shut down, unplug for 30 seconds, and reboot. Windows reinstalls it automatically. This clears corrupt battery state that can block charging."
  - q: "When is 'not charging' actually normal?"
    a: "Near full charge (95-100%), Windows often shows 'plugged in, not charging' while running on AC — that's charge termination, not a fault. Manufacturer limiters (60%/80% caps) also show this. And some laptops pause charging when the battery is hot. Only troubleshoot when it happens well below full charge."
---

"Plugged in, not charging" is Windows' least helpful message. It tells you the symptom and nothing about the cause — and the cause could be a $0 settings toggle or a $150 battery. Randomly trying fixes wastes time; what you need is a diagnostic sequence that eliminates suspects one by one until only the culprit remains.

That's what this is: not a bag of tricks, but an order of operations. Each step rules something out.

## Why this happens

- **Charge limiter active:** Conservation Mode, ASUS caps, Dell Adaptive, HP Battery Health Manager — the battery is being told not to charge.
- **Underpowered or failing charger:** Detected as AC, but can't deliver charging current.
- **Corrupt battery driver/state:** Windows' ACPI battery driver stuck in a bad state.
- **EC confusion:** The embedded controller latched into a no-charge state (common after deep discharge or hard crash).
- **Worn or failed battery:** Cells that can't accept charge, or a failed pack controller.
- **Charging port/jack fault:** Intermittent connection the OS reads as "plugged in" while no real current flows.
- **Motherboard charging circuit failure:** The power-path IC failed — rare, but the end of the diagnostic road.

## How to troubleshoot it

Follow in order. Don't skip — each step's result directs the next.

### Step 1: Read the exact symptom

Precision now saves confusion later.

1. Hover the battery icon: note the **exact percentage** and the exact message ("plugged in, charging" vs "plugged in, not charging").
2. Note whether the percentage is **rising slowly**, **frozen**, or **falling** while plugged in. Rising slowly = weak charger. Frozen = limiter or driver. Falling = charger can't cover load, or no real power flowing.
3. Check the **charging LED** on the laptop: on, off, or blinking? Compare with your manual's LED codes.
4. Note when it started: after an update? After the battery fully drained? Gradually over weeks? Sudden onset points to settings/drivers; gradual points to wear.
5. If the battery is at 95-100% and says "not charging" — stop. That's normal charge termination. Only continue if it's well below full.

### Step 2: Eliminate the charger and outlet

The most common real cause. Rule it out definitively.

1. Unplug from the wall and the laptop. Inspect the entire charger: brick, cable, connector. Look for fraying, kinks, bent pins, burn marks, or a loose barrel fit.
2. Plug into a **different wall outlet directly** — no power strips, no extension cords.
3. Verify wattage: read the brick's label and confirm it matches your laptop's original adapter rating. A 45W brick on a 90W laptop explains everything.
4. If possible, test with a **known-good charger** of correct wattage. Charging resumes = your charger is bad. Still nothing = charger is innocent; continue.
5. For USB-C: test with the charger plugged **directly into the correct port**, bypassing hubs. Try a 100W-rated cable if you suspect the cable.

### Step 3: Check for active charge limiters

The "it's a feature" check — fast and decisive.

1. **Lenovo Vantage** → Conservation Mode off? **MyASUS** → Battery Health Charging → Full capacity? **Dell Power Manager** → Standard? **HP BIOS (F10)** → Battery Health Manager?
2. Check **BIOS/UEFI** battery settings directly — the BIOS can enforce limits no Windows utility shows.
3. After changing any limiter, do a **full shutdown** (not restart), wait 10 seconds, cold boot, then test.
4. If charging resumes, it was the limiter. Decide whether to keep it (good for desk-bound battery longevity) — but at least now it's your choice.
5. If your battery stops specifically at 80%, see our focused guide on [what to do when the battery won't reach 100%](/articles/what-to-do-if-laptop-battery-not-charging-to-100-percent/).

### Step 4: Reset the EC and reinstall drivers

Clear the confused-controller layer.

1. **Device Manager > Batteries**: uninstall **Microsoft ACPI-Compliant Control Method Battery** (and Microsoft AC Adapter if present).
2. Shut down fully. Unplug the charger.
3. **EC reset**: hold power 30 seconds (or use the pinhole reset if your model has one — many Acer/Lenovo/HP do).
4. Plug in, wait 10 seconds, power on. Let Windows reinstall drivers.
5. Test for 15 minutes. If charging starts, the EC or driver was latched — common after deep discharges and hard crashes.
6. Still nothing? The problem is below the software layer. Continue.

### Step 5: Get the battery report numbers

Let the data speak.

1. Admin terminal: `powercfg /batteryreport`. Open the HTML.
2. Check **Design Capacity** vs **Full Charge Capacity**. Compute wear.
3. **Wear under 25%** with no charging = not a wear problem. Suspect port/circuit (Step 6).
4. **Wear 25-50%**: battery degraded but should still accept charge. If it won't charge at all, the pack controller may have failed rather than the cells wearing out.
5. **Wear over 50-60%**: the battery is likely done. But confirm with the manufacturer's diagnostic before buying (Step 7).
6. Check the report's recent history: did charging stop abruptly on a specific date? Correlate with updates or incidents.

### Step 6: Test the port and the power path

Hardware connection checks.

1. Gently wiggle the charger plug while watching the LED and Windows battery icon. Flickering = loose DC jack or worn USB-C port.
2. Inspect the port with a light: debris, bent pins, corrosion, burn smell.
3. **Removable battery test**: remove the battery, run on AC alone. Runs fine = adapter + motherboard OK, battery is the suspect. Won't run right = deeper motherboard issue.
4. For sealed laptops: note whether the laptop runs normally on AC. If yes, the power path mostly works and the fault is battery-side.
5. Try charging while the laptop is **off**. If it charges while off but not while on, the adapter can't cover system load + charging (underpowered/failing adapter — back to Step 2 with fresh eyes).

### Step 7: Run the manufacturer's diagnostic

Get the authoritative verdict.

1. **Dell:** F12 at boot → Diagnostics (ePSA) — includes battery and adapter tests with error codes.
2. **HP:** Esc → F2 → Component Tests → Battery + AC Adapter.
3. **Lenovo:** Lenovo Vantage → battery test, or Lenovo Diagnostics bootable tool.
4. **ASUS:** MyASUS → System Diagnostics → battery test.
5. If the manufacturer's tool reports battery failure, that's definitive — replace with a genuine battery.
6. If all diagnostics pass but charging still fails, you're looking at a motherboard charging-circuit fault — a service-center repair. Bring your notes: symptom details, what you tested, and the battery report. It makes the technician's job (and your bill) smaller.

## Closing

"Plugged in, not charging" surrenders to method: charger, limiter, EC/driver, numbers, port, manufacturer diagnostic. Most cases resolve in the first four steps — it's a charger, a forgotten Conservation Mode, or a latched controller far more often than a dead battery. The diagnostic order matters because it stops you from buying a battery to fix a charger problem.

*Related reading: [battery won't reach 100%](/articles/what-to-do-if-laptop-battery-not-charging-to-100-percent/), [Dell battery not charging](/articles/how-to-fix-dell-laptop-battery-not-charging-step-by-step/)*
