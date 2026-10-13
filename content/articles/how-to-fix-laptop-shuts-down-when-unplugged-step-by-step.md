---
title: "Laptop Shuts Down When Unplugged? Step-by-Step Fix"
slug: how-to-fix-laptop-shuts-down-when-unplugged-step-by-step
date: 2026-09-20
categories: ["battery"]
tags: ["shuts down unplugged", "battery dead", "no battery power", "troubleshooting"]
description: "Laptop works fine on the charger but dies the instant you unplug? Here's how to find out whether the battery is dead, disconnected, or just confused."
thumbnail: "/images/thumbs/how-to-fix-laptop-shuts-down-when-unplugged-step-by-step.webp"
faqs:
  - q: "Why does my laptop turn off immediately when I unplug the charger?"
    a: "The battery isn't delivering power. Either it's completely worn out (high internal resistance means voltage collapses under load), it's disconnected (loose internal connector, especially after a drop or repair), the battery controller has failed, or the gauge is so miscalibrated the system thinks there's charge when there isn't. The battery report distinguishes these."
  - q: "Can a laptop run without a battery while plugged in?"
    a: "Most can — the charger powers the system directly. If your laptop runs fine on AC with the battery removed (removable models) but dies when unplugged with the battery in, the battery is the problem, not the motherboard. This is actually a useful diagnostic step."
  - q: "My battery shows 100% but the laptop dies when unplugged. How?"
    a: "The gauge is lying or the cells can't deliver current. A battery can show full voltage at rest (reads 100%) but collapse the instant a load is applied — classic end-of-life behavior. Alternatively the battery's internal controller reports fake values. Check the wear level; if it's extreme, the 100% reading is meaningless."
  - q: "Could a Windows update cause this?"
    a: "An update can't kill a battery, but it can expose a dying one: new power management behavior or a gauge reset can change when the system decides the battery is empty. If it started right after an update, recalibrate and check wear before assuming coincidence — the battery was likely already marginal."
---

This is the most dramatic battery failure: works perfectly on AC power, dies instantly — not in minutes, instantly — the moment you unplug. No warning, no low-battery countdown. It's as if the battery isn't there at all. And sometimes, electrically speaking, it isn't: either the cells can't deliver, the connection is broken, or the controller has given up.

The diagnostic path is short and decisive. Let's find out which one it is.

## Why this happens

- **Completely worn battery:** Internal resistance so high that any load collapses the voltage below the cutoff — the system shuts off to protect itself. The most common cause.
- **Disconnected battery:** Internal connector worked loose (drop, bump, or a previous repair). The OS may still "see" a battery via the controller while no power flows.
- **Failed battery controller:** The pack's internal circuit board died. Cells may be fine, but nothing can get in or out.
- **Deeply discharged protection lockout:** Some battery controllers permanently lock out a pack that sat at zero volts too long, as a safety measure.
- **Motherboard battery circuit fault:** The charging/power-path circuitry failed — battery can't deliver even though it's healthy. Rarer, but happens after liquid damage or power surges.
- **Severely miscalibrated gauge:** The system thinks the battery has charge (shows 60%+) when it's actually empty, so there's no graceful low-battery shutdown — just a cliff.
- **Swollen battery disconnecting:** A swelling pack can physically push its own connector loose or trigger the controller's safety cutoff.

## How to fix it

Work through these in order — the early steps give you a definitive diagnosis.

### Fix 1: Confirm the symptom precisely

Details matter for diagnosis.

1. Note exactly what happens: instant black screen on unplug? A few seconds of running? Does it happen at any battery percentage, or only when the gauge is low?
2. Check what Windows reports: with the charger connected, hover the battery icon. Note the percentage and whether it says "charging."
3. Unplug and immediately try to power on with no charger. Any signs of life — LEDs, fan spin, anything? Note exactly what happens.
4. If it runs for a few minutes then dies, that's worn cells (voltage sag). If it dies the literal instant the plug leaves, that's a disconnected/failed pack or a protection lockout.
5. Check for swelling: place the laptop on a flat surface. Rocking, a lifting trackpad, or case gaps mean a swollen battery — skip to Fix 7's safety note.

### Fix 2: Run a battery report and read the wear

Numbers first.

1. With the charger connected, open an admin terminal and run `powercfg /batteryreport`.
2. Compare **Design Capacity** vs **Full Charge Capacity**.
3. **Wear over 60-70%:** the battery is exhausted — this is your answer. Cells this worn can't sustain voltage under load. Replace (Fix 7).
4. **Moderate wear (30-50%) but instant shutdown:** wear alone doesn't explain instant death — suspect the controller, connection, or lockout. Continue.
5. **Low wear but instant shutdown:** the battery should work — this points to disconnection, controller failure, or motherboard fault. Continue to Fix 3.
6. Also check: does the report show the battery as present with sensible numbers, or are the values blank/garbage? Blank = the OS can't really talk to the pack.

### Fix 3: Reseat the battery connection

A loose connector causes exactly this symptom.

1. **Removable battery:** power off, unplug, remove the battery, inspect the contacts (clean, straight, no corrosion), reinsert firmly until it clicks. Test.
2. **Internal battery:** power off, unplug. Remove the bottom panel (usually 8-12 screws — keep them organized).
3. Locate the battery connector on the motherboard — a wide multi-pin plug, often with a pull tab.
4. Disconnect it, inspect for damage or corrosion, then reconnect firmly. Also check the battery cable for nicks.
5. While you're in there, look for swelling, and check that no screws or debris are shorting anything.
6. Reassemble, plug in, charge for 15 minutes, then test unplugged. If reseating fixed it, the connector had worked loose — consider a small piece of kapton tape over the connector to prevent recurrence (don't use regular tape inside a laptop).

### Fix 4: Test with the battery removed (removable models)

Isolates battery vs motherboard definitively.

1. Power off, unplug, remove the battery.
2. Plug in the charger and power on. If the laptop runs normally on AC alone, the motherboard and charger are fine.
3. This confirms the fault is in the battery pack itself (cells or controller), not the laptop's power circuitry.
4. If the laptop **doesn't** run properly even on AC with no battery (crashes, won't boot), the motherboard's power circuitry is suspect — that's a board-level repair, not a battery problem.
5. For sealed laptops you can't easily do this test — rely on Fix 2's numbers and Fix 3's reseat instead.

### Fix 5: Try to wake a locked-out battery

Some controllers lock after deep discharge but can be revived.

1. This applies if the problem started after the laptop sat dead/unplugged for weeks or months.
2. Plug in the original charger and **leave it for 4-6 hours without touching it** — some controllers trickle-charge locked packs back to a safe voltage before allowing normal operation. The charging LED may stay off or red for a long time; that's normal during recovery.
3. After several hours, check if the LED changed and whether Windows now shows charging progress.
4. Try the **EC reset**: unplug, hold power 30 seconds (or the pinhole reset), replug, wait, power on.
5. If nothing after 6+ hours, the lockout is permanent (by design — deeply discharged lithium is unsafe to revive aggressively). Replace the battery.
6. Never try to "jump-start" a laptop battery with external power supplies — the pack's controller must manage recovery, or it isn't safe.

### Fix 6: Reinstall drivers and update BIOS

Rule out the software/firmware layer.

1. **Device Manager > Batteries**: uninstall **Microsoft ACPI-Compliant Control Method Battery**. Shut down, unplug 30 seconds, reboot on AC.
2. Update **BIOS** from the manufacturer — the EC firmware manages the battery power path, and updates fix path-switching bugs.
3. After updating, charge for 30 minutes on AC, then test unplugged.
4. Run the manufacturer's battery diagnostic (**Dell ePSA** via F12, **HP F2 diagnostics**, **Lenovo Vantage**, **MyASUS**) for an authoritative second opinion.
5. If the manufacturer's tool says the battery failed and Windows agrees, that's two independent verdicts — replace with confidence.

### Fix 7: Replace the battery (safely)

When the diagnosis points at the pack, replace it — carefully.

1. **Swelling check first:** if there's any bulge, stop using the laptop immediately. Back up data without flexing the machine. Have a professional do the replacement — swollen packs are fire hazards, and puncturing one during DIY removal is the classic accident.
2. Get the exact part number (battery label or manufacturer's site via serial number).
3. Buy **genuine**. A counterfeit pack with a bad controller can cause this exact symptom out of the box.
4. Check warranty — instant-death on a battery under 12 months old is a strong warranty claim, especially with a battery report showing the failure.
5. After installing the new battery: charge to 100% uninterrupted, then run one full calibration cycle so the controller learns the new pack. Verify with `powercfg /batteryreport` that full charge capacity matches design.
6. If a **new genuine battery** still doesn't power the laptop unplugged, the motherboard's battery power path is faulty — that's a board repair or replacement decision. Document everything for the service center.

## Closing

Instant shutdown on unplug is the battery's way of saying it can't deliver power — and the battery report usually tells you why in one glance. Reseat the connector before you buy anything (it's free and fixes a surprising number of cases), try the long trickle-charge for lockouts, and replace when the numbers say the cells are done. Don't keep using a machine that dies on unplug without diagnosing it — one day it'll die mid-save.

*Related reading: [battery won't hold charge](/articles/how-to-fix-laptop-battery-won-t-hold-charge-step-by-step/), [check design vs full charge capacity](/articles/best-way-to-check-battery-design-vs-full-charge-capacity/)*
