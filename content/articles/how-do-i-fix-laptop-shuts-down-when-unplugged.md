---
title: "Laptop Shuts Down When Unplugged? Fix the Instant Power-Off"
slug: how-do-i-fix-laptop-shuts-down-when-unplugged
date: 2026-10-08
categories: ["battery"]
tags: ["shuts down unplugged", "instant shutdown", "battery failure"]
description: "Laptop dies the second you unplug the charger? Here's how to find out whether it's a dead battery, a connection fault, or a settings issue."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-shuts-down-when-unplugged.webp"
faqs:
  - q: "Why does my laptop turn off immediately when I unplug it?"
    a: "The battery isn't delivering power. Most often the cells are completely worn out (zero usable capacity), the battery isn't detected at all, or an internal connection is broken. Less commonly, a corrupted battery driver or a critical-level misconfiguration causes Windows to shut down the instant AC power disappears."
  - q: "Can a laptop run without a battery?"
    a: "Yes — most laptops run fine on AC power with the battery removed (for removable-battery models) or with a dead battery installed. If your laptop works perfectly on the charger but dies when unplugged, that itself confirms the rest of the hardware is fine and isolates the problem to the battery subsystem."
  - q: "Is it safe to keep using a laptop whose battery is dead?"
    a: "Generally yes, on AC power — but watch for warning signs. If the battery is swollen, extremely hot, or smells odd, stop using the laptop and remove/disconnect the battery (or have a shop do it). A merely worn-out battery with no swelling is safe to leave installed while running on AC."
  - q: "My battery shows 100% but the laptop still dies when unplugged. Why?"
    a: "The gauge is lying — the battery has no real capacity left, but the uncalibrated gauge reports full. This is classic end-of-life behavior: voltage collapses the instant a load is applied. A battery report will show full-charge capacity near zero or a huge gap vs. design capacity."
---
# Laptop Shuts Down When Unplugged? Fix the Instant Power-Off

Working fine on the charger, dead the instant you unplug — it's one of the clearest symptoms in laptop troubleshooting, and it points squarely at the battery subsystem. The laptop itself is fine (it runs on AC, after all). Something between the battery cells and the motherboard isn't delivering power.

This guide isolates exactly where the break is: dead cells, undetected battery, broken connection, or software confusion. Let's find it.

## Why this happens

- **Completely worn-out battery.** Zero usable capacity left — the most common cause on laptops over 3–4 years old.
- **Battery not detected by the system.** If Windows doesn't see a battery at all, unplugging means instant power loss.
- **Broken internal connection.** The battery connector or its cable has worked loose or corroded.
- **Failed battery cells with voltage collapse.** The gauge says 100% but voltage crashes the moment a load hits.
- **Swollen battery pressing on components.** Swelling can break connections or trigger safety cutoffs.
- **Corrupted battery driver.** Windows mishandles the AC-to-battery transition and shuts down instead.
- **Critical battery level misconfigured.** If the critical action triggers at the wrong threshold, unplugging can cause an immediate shutdown.

## How to fix it

Work through these in order, from quickest to deepest. Most people find the answer by Fix 3.

### Fix 1: Confirm the Battery Is Detected

First establish whether Windows even sees a battery — this splits the diagnosis in half.

1. Look at the taskbar battery icon: does it show a battery with a percentage, or a red X / "no battery detected"?
2. Open **Device Manager > Batteries** — is **Microsoft ACPI-Compliant Control Method Battery** listed?
3. Open admin **Command Prompt** and run `powercfg /batteryreport` — if it says no battery found, the system doesn't see one at all.
4. If no battery is detected, skip to Fix 5 (connection/hardware).
5. If a battery is detected with a percentage, continue below.

### Fix 2: Check the Battery's True Capacity

A "100%" reading on a dead battery is the classic trap. Get the real numbers.

1. Run `powercfg /batteryreport` in an admin **Command Prompt**.
2. Compare **Design Capacity** vs **Full Charge Capacity**.
3. If full-charge capacity is near zero or under 20% of design, the battery is done — it can't power the laptop for even a second.
4. Check the usage history: does the battery ever actually discharge, or does it sit at the same percentage forever?
5. This data decides between "replace the battery" and "keep troubleshooting software."

If the numbers look wrong, [checking the battery wear level](/articles/how-to-check-battery-wear-level-on-windows-10/) explains how to interpret them properly.

### Fix 3: Reset the Power System

A stuck embedded controller can fail the AC-to-battery handoff. Reset it.

1. Shut down completely and unplug the charger.
2. If removable, take the battery out.
3. Hold the power button for **30 seconds** to drain residual power.
4. Reinsert the battery (if removable), plug in the charger, and power on.
5. Once booted and showing a charge, unplug and observe — does it stay on now?
6. If it still dies instantly, the problem is deeper than a stuck controller.

### Fix 4: Reinstall Battery Drivers

If Windows mishandles the power transition, fresh drivers can fix it.

1. Open **Device Manager > Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. Full shutdown (hold **Shift** while clicking **Shut down**).
4. Unplug for 30 seconds, plug back in, and boot.
5. Let Windows reinstall the drivers, then test unplugging again.
6. Also check **Control Panel > Power Options > Change advanced power settings > Battery** — make sure **Critical battery action** is **Hibernate**, not **Shut down**.

### Fix 5: Reseat the Battery Connection

For removable batteries, a poor connection is a real possibility. For internal batteries, this means opening the laptop — proceed only if comfortable.

1. **Removable battery:** power off, unplug, remove the battery, and inspect the contacts for corrosion or dirt.
2. Clean contacts gently with a dry cloth or pencil eraser — never wet.
3. Reinsert firmly until it clicks/locks, plug in, and test.
4. **Internal battery:** power off, unplug, remove the back panel (check your manual), and locate the battery connector on the motherboard.
5. Carefully disconnect and reconnect the battery cable, ensuring it's fully seated.
6. Reassemble and test. If you're not comfortable with this, a shop does it in minutes.

### Fix 6: Test With the Battery Removed (Removable Models)

This isolates whether the battery is actively causing problems vs. just dead.

1. Power off, unplug, and remove the battery.
2. Plug in the charger and power on — confirm the laptop runs fine on AC alone.
3. If it runs fine, the motherboard and charger are good; the battery is the sole problem.
4. Inspect the removed battery for swelling — lay it on a flat table and check for wobble or bulging.
5. A swollen battery should be recycled promptly, not reinstalled.

### Fix 7: Check for Swelling and Safety Issues

Instant shutdown on unplug plus any physical symptom means stop troubleshooting and handle the battery safely.

1. Check if the trackpad feels raised, clicks oddly, or the bottom panel bulges.
2. Set the laptop on a flat surface — wobbling indicates swelling.
3. If swollen: power off, unplug, don't charge it, don't puncture it.
4. Take it to a repair shop or manufacturer service for safe removal.
5. Swollen batteries are a fire risk — this jumps ahead of all other fixes.

### Fix 8: Replace the Battery

When the data says the battery is done, replace it properly.

1. Confirm with the battery report: near-zero full-charge capacity = certain.
2. Check warranty — dead batteries within the warranty period get replaced free.
3. Get the exact battery model/part number for your laptop.
4. Buy genuine or manufacturer-certified batteries only.
5. After installing, charge to 100% and run one calibration cycle.
6. Test: unplug and confirm the laptop stays on and discharges normally.

For related charging issues after replacement, [troubleshooting a Dell battery that won't charge](/articles/troubleshoot-dell-laptop-battery-not-charging/) covers the driver side.

## Closing

Instant shutdown on unplug is actually a friendly symptom — it tells you exactly where to look. The battery report gives you the verdict in two minutes: near-zero capacity means replace, decent capacity means keep digging through connections and drivers. And remember the safety check: a swollen battery turns a simple replacement into a "handle with care" situation. Diagnose first, then act.

## Verify your results

The final test is simple: charge to full, unplug, and use the laptop. It should discharge gradually over hours, not die in seconds. If it survives unplugged but runtime is short, you're dealing with wear rather than failure — see the [battery wear guide](/articles/how-to-fix-battery-wear-level-too-high-reddit/) for next steps. For parts and service, [Lenovo Support](https://support.lenovo.com/us/en/) and [HP Support](https://support.hp.com/us-en) have model-specific battery information.
