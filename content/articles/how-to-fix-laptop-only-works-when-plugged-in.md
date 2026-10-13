---
title: "Laptop Only Works When Plugged In? How to Fix It"
slug: how-to-fix-laptop-only-works-when-plugged-in
date: 2026-10-09
categories: ["battery"]
tags: ["not charging", "battery dead", "AC power"]
description: "Laptop dies the second you unplug it? Diagnose whether it's a dead battery, bad connection, or settings issue — and fix it."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-when-plugged-in.webp"
faqs:
  - q: "Why does my laptop shut off immediately when I unplug it?"
    a: "The battery is not delivering power. That usually means the cells are fully worn out, the battery is disconnected or not detected, or a protection circuit has cut it off. The laptop runs fine on AC because the charger powers the system directly, bypassing the battery entirely."
  - q: "Can I still use my laptop if the battery is dead?"
    a: "Yes, as a desktop — it will run normally on AC power. Just be aware that any power interruption (a loose plug, a tripped breaker) shuts it down instantly with no graceful shutdown, so save work often and consider a UPS if your power is unreliable."
  - q: "Will a battery calibration fix this?"
    a: "No. Calibration fixes inaccurate percentage readings on a working battery. A battery that delivers zero power has an electrical problem — worn-out cells, a tripped protection circuit, or a connection fault — and no software routine can bring dead cells back."
  - q: "How do I know if it's the battery or the motherboard?"
    a: "Run the diagnostic sequence: check if Windows detects the battery at all, try an EC reset, reseat a removable battery, and run the OEM hardware test. If the battery is detected but holds no charge, it's the battery. If no battery is detected after resets and reseating, suspect the battery first (cheaper) and the charging circuit second."
---

There's a special kind of annoyance in a "laptop" that can't survive two seconds away from the wall. The good news: when a machine runs perfectly on AC power, the expensive parts — motherboard, CPU, RAM, storage — are almost certainly fine. The problem lives in the battery subsystem, which is a much narrower and cheaper thing to diagnose: the pack itself, its connection, the controller that manages it, or occasionally the charging circuit.

This guide narrows it down systematically instead of throwing parts at it. We'll check what Windows actually sees, reset the power management hardware, test the connection, and finish with a verdict you can act on. If Windows doesn't see a battery at all, you may also want [what to do when the battery is not detected](/articles/what-to-do-if-battery-not-detected-on-laptop/).

## Why this happens

- **Fully worn-out cells:** After hundreds of cycles, the pack's usable capacity can reach effectively zero — it reports a charge but collapses under any load.
- **Tripped battery protection:** The pack's internal protection circuit can latch off after a deep discharge, over-temperature event, or cell imbalance.
- **Loose or corroded connection:** A battery connector that's worked slightly loose (or corroded) breaks the power path while data lines still report "battery present."
- **Failed battery controller:** The embedded controller or the pack's own fuel-gauge chip can fail in a way that blocks discharge.
- **Swollen pack disconnecting:** A swelling battery can physically push its own connector loose — and swelling means stop using it anyway.
- **Charging circuit fault:** Rare, but the motherboard's power circuitry can fail so the battery neither charges nor discharges.

## How to fix it

Work through these in order — each step eliminates a suspect.

### Fix 1: Confirm what Windows actually sees

Get the facts before touching hardware.

1. Hover over the battery icon in the taskbar — note the exact message: a percentage that never changes, "plugged in, not charging," or no battery icon at all each point somewhere different.
2. Open **Device Manager > Batteries** and check whether **Microsoft ACPI-Compliant Control Method Battery** is present and has no warning icon.
3. Generate a report: `powercfg /batteryreport` in an elevated prompt, and check whether the report shows an installed battery with capacity numbers.
4. If Windows sees a battery with near-zero full charge capacity versus design capacity, the cells are worn out — skip to Fix 7.
5. If no battery appears anywhere, the pack isn't communicating — continue with the connection and reset fixes.

### Fix 2: Run a full power reset (EC reset)

Clear any latched protection or controller state.

1. Shut down completely, unplug the charger, and if the battery is removable, take it out.
2. Press and hold the power button for **30 seconds** to drain residual power and reset the embedded controller.
3. If the battery is internal, the same hold-the-button procedure works — it just resets the EC without removing anything.
4. Reconnect everything, plug in, power on, and test on battery alone.
5. This single step resolves a surprising number of "dead battery" cases that are really just a tripped protection circuit.

### Fix 3: Reseat a removable battery

Eliminate the connection as a suspect.

1. Power off, unplug, and remove the battery (slide the latches on older models).
2. Inspect the battery's contact pads and the laptop's connector pins for corrosion, bent pins, or debris — clean gently with a dry cloth or isopropyl alcohol on a cotton swab.
3. Reinsert firmly until the latches click, then plug in and charge for at least 30 minutes before testing on battery.
4. If the laptop has an internal battery you're comfortable accessing, the same reseat applies after removing the bottom panel — disconnect the battery cable, wait a minute, reconnect firmly.
5. Never force a swollen battery back in — swelling is a replace-immediately safety issue, not a reseat candidate.

### Fix 4: Reinstall the battery drivers

Rule out a software-side block.

1. In **Device Manager > Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device** (don't worry — it reinstalls on reboot).
2. If there's a second entry (some systems list the adapter too), uninstall it as well.
3. Shut down (don't just restart), unplug for a minute, then power on with the charger connected — Windows redetects the battery hardware fresh.
4. Test on battery power after a few minutes of charging.
5. If Device Manager shows the battery with a yellow warning that persists across reinstalls, note the error code — Code 10 or Code 45 here usually means hardware, not software.

### Fix 5: Check the charger's role in the confusion

A weak charger can masquerade as a battery problem.

1. Confirm you're using the original charger or one with equal/higher wattage — an underpowered charger may run the system but never actually charge the pack.
2. Check the taskbar message while plugged in: "plugged in, charging" versus "plugged in, not charging" tells you whether charge current is flowing at all.
3. Try a different outlet and inspect the charging port for looseness — an intermittent connection can keep resetting the charge cycle.
4. If the battery charges normally with a different charger but not yours, replace the charger, not the battery.
5. For the full charging-side workup, see [plugged in, not charging — what to do](/articles/what-to-do-if-laptop-plugged-in-not-charging/).

### Fix 6: Test with the battery removed (where possible)

Isolate whether the battery is dragging the system down.

1. On models with removable batteries: power off, remove the battery, plug in AC only, and boot — if it runs perfectly, the system side is fine and the battery is the entire problem.
2. On internal-battery models, only do this if you're comfortable opening the machine: disconnect the battery cable, reassemble, and test on AC.
3. This test also reveals a shorted pack — a battery with an internal short can actually prevent booting, and removing it brings the machine back to life.
4. If the machine misbehaves even on AC with no battery, the problem is deeper (power circuitry) and needs professional diagnosis.
5. Don't run long-term without the battery if your area has flaky power — you have zero ride-through without it.

### Fix 7: Read the wear numbers and replace if needed

Make the final call with data.

1. Open that `powercfg /batteryreport` from Fix 1 and divide **Full Charge Capacity** by **Design Capacity**.
2. Under 50% on a machine that dies instantly unplugged: the cells are done — replacement is the fix, and no setting will change that.
3. Order the correct replacement: match the exact model number on the battery label (not just the laptop model), and prefer OEM or well-reviewed third-party packs — ultra-cheap no-name batteries are a fire risk.
4. After installing the new pack, charge it to 100% uninterrupted, then run one full discharge-charge cycle to let the fuel gauge learn the new cells.
5. Consider enabling a charge limit (like Lenovo's conservation mode or the equivalent) on the new battery if you mostly use the laptop docked — it will last years longer. Microsoft's power guidance is at [Microsoft Support](https://support.microsoft.com/en-us/windows).

## Closing

A laptop that only works plugged in is really a desktop wearing a laptop costume — and the fix is almost always in the battery subsystem, not the computer itself. Work the sequence, trust the wear numbers, and you'll end up either with a revived battery or a confident, data-backed decision to replace it instead of another afternoon of guessing.
