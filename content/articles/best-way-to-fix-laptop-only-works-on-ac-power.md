---
title: "Fix a Laptop That Only Works on AC Power"
slug: best-way-to-fix-laptop-only-works-on-ac-power
date: 2026-09-21
categories: ["battery"]
tags: ["ac power only", "battery not detected", "dies when unplugged", "troubleshooting"]
description: "Laptop dies the instant you unplug it? Find out whether the battery is dead, disconnected, or just disabled — and get portable again."
thumbnail: "/images/thumbs/best-way-to-fix-laptop-only-works-on-ac-power.webp"
faqs:
  - q: "Why does my laptop shut off immediately when I unplug it?"
    a: "The battery isn't delivering any power. The usual causes: a completely worn-out battery, a battery that's disconnected internally, a disabled battery in BIOS, or a missing battery driver. The laptop runs fine on AC because the adapter powers it directly — the battery just isn't in the circuit."
  - q: "Can I keep using a laptop with a dead battery plugged in?"
    a: "Yes, it works as a desktop — but you're one power flicker away from instant shutdown and lost work. Also, a swollen battery should never be left in the machine. If the battery is merely worn (not swollen), AC-only use is safe but save your work often."
  - q: "Will removing the dead battery help?"
    a: "On models with removable batteries, removing a dead one is fine and the laptop runs on AC alone. On modern laptops with internal batteries, don't remove it yourself unless you're comfortable opening the machine — and never run with a swollen battery installed."
  - q: "Does 'no battery detected' mean I need a new battery?"
    a: "Not necessarily. It can mean the battery connector came loose, the driver failed, or the battery is disabled in BIOS. Check Device Manager and BIOS before buying — a reseat or driver reinstall fixes many 'not detected' cases for free."
---
A laptop that works perfectly on the charger and dies the second you unplug it has a battery that's completely out of the picture — not weak, not miscalibrated, but delivering zero power. That's actually a simpler problem than a flaky battery, because the suspect list is short: the battery is dead, disconnected, disabled, or undetected.

The goal here is to figure out which one it is, in order of cheapest fix first. Many "dead" batteries turn out to be disconnected or driver-disabled — free fixes. Here's how to tell.

## Why this happens

- **The battery is completely worn out:** Past end of life, the protection circuit cuts the pack off entirely. Zero power out, instant shutdown on unplug.
- **The battery connector came loose:** Drops, heat cycling, or swelling can unseat the internal battery connector. The battery is fine; it's just not plugged in.
- **The battery is disabled in BIOS/UEFI:** Some BIOS setups have a battery disable option (for servicing). If toggled, the battery is invisible to Windows.
- **The battery driver failed:** Without the ACPI battery driver, Windows may not see the battery at all, and power management can't use it.
- **The battery is swollen and its protection tripped:** Swelling can trigger the pack's safety cutoff, disconnecting it electrically. (This one needs care, not troubleshooting.)
- **A failed battery calibration left it at true zero:** Rare, but a battery drained to absolute zero can enter a deep-discharge protection state that normal charging won't wake.
- **Motherboard charging circuit failure:** The circuit that routes battery power can fail while the AC path still works — the least common but most expensive cause.

## How to fix it

Work through these in order — stop when the battery works on its own.

### Fix 1: Check what Windows thinks about the battery

Start with the OS view — it tells you whether the battery is dead, missing, or just misbehaving.

1. **Look at the taskbar battery icon:** No battery icon at all, or an icon with a red X, points to detection failure. A battery icon showing 0% that never charges points to a dead pack.
2. **Open Device Manager** (**Windows + X > Device Manager**) and expand **Batteries**. Note what's listed: missing entries mean detection failure.
3. **Run** `powercfg /batteryreport` in an admin Terminal. If it errors or shows no battery, Windows genuinely can't see the pack.
4. **Check Settings > System > Power & battery:** A missing battery section confirms the OS-level view.

"No battery detected" anywhere here means: driver, BIOS, or connection. A detected-but-0% battery means: dead pack or deep discharge. For the detection-specific deep dive, see [laptop battery not detected in Windows 11](/articles/laptop-battery-not-detected-windows-11/).

### Fix 2: Check the BIOS for a disabled battery

A BIOS-disabled battery is invisible to Windows no matter what drivers you install.

1. **Enter BIOS/UEFI setup:** Restart, press **F2**/**Del**/**Enter+F1** (brand-dependent) during boot.
2. **Look for battery options:** Under Power, Advanced, or Config sections — **Battery**, **Disable Built-in Battery**, or similar.
3. **Make sure the battery is enabled.** Some Lenovos have a "Disable built-in battery" option meant for servicing; if it's on, the battery is electrically disconnected.
4. **Save and exit**, boot into Windows, and check whether the battery appears.

Also note the BIOS's own battery health reading if shown — some BIOS setups display it directly, giving you a firmware-level verdict.

### Fix 3: Reinstall the battery drivers

A broken driver chain can hide a perfectly good battery.

1. **In Device Manager > Batteries**, right-click each entry (**Microsoft ACPI-Compliant Control Method Battery**, **Microsoft AC Adapter**) and choose **Uninstall device**.
2. **Shut down fully** (**Shift + Shut down**), unplug the charger for 30 seconds.
3. **Plug back in and power on.** Windows redetects the battery hardware during boot.
4. **Check the taskbar icon:** If a battery percentage appears, the driver was the problem.

If Device Manager shows the battery with a yellow warning triangle, note the error code — it points to the specific driver or hardware fault. Microsoft documents device error codes at [support.microsoft.com](https://support.microsoft.com/en-us/windows).

### Fix 4: Reseat the battery connector (internal batteries)

If the laptop was dropped, overheated, or recently serviced, the connector may have walked loose.

1. **Power off, unplug everything.** If the battery is swollen (trackpad lifting, base wobbling), STOP — do not open it yourself; take it to a shop.
2. **Remove the bottom cover:** Unscrew the back panel screws (keep them organized — they vary in length). Use a plastic pry tool, not metal.
3. **Locate the battery connector:** A wide multi-pin plug connecting the battery pack to the motherboard, often with a pull tab.
4. **Disconnect and reconnect it firmly:** Lift the latch or pull straight out (never yank by wires), then push it back until fully seated.
5. **Reassemble and test:** Before replacing all screws, plug in AC, boot, and check whether the battery is detected.

This fixes a surprising number of "dead battery" cases on laptops that took a knock. While you're in there, check for swelling — a puffy pack needs replacement, not reseating.

### Fix 5: Try to wake a deep-discharged battery

A battery drained to absolute zero can lock itself in protection mode.

1. **Plug in the original charger** (correct wattage matters here) and leave it for **at least 2–4 hours** without touching the power button.
2. **Watch the charge LED:** No LED at first is normal for deep discharge. If an LED appears after a while, the pack is waking up.
3. **After several hours**, try powering on with the charger connected.
4. **If it boots on AC but the battery still shows 0%**, leave it charging overnight. Some packs need 8+ hours to exit protection.

If 12+ hours of charging produces no battery detection at all, the pack's protection circuit has likely locked permanently — replacement time.

### Fix 6: Test with the battery removed (removable-battery models)

This isolates whether the battery is interfering with the system.

1. **Power off and unplug.** Remove the battery (slide the latches on older laptops).
2. **Run on AC only** for a while. If the laptop is stable, the system board is fine.
3. **Reinsert the battery firmly** and test again. Sometimes removal and reinsertion alone clears a bad contact.
4. **If problems return only with the battery in**, the pack is faulty — replace it.

For sealed modern laptops, skip this — the "removal" is the connector reseat in Fix 4.

### Fix 7: Get the wear verdict and replace if needed

When all the free fixes fail, confirm the battery is truly done before spending money.

1. **Generate a battery report** (`powercfg /batteryreport`) — if the battery is detected at all, compare Full Charge Capacity to Design Capacity.
2. **Use the manufacturer's diagnostic:** Dell pre-boot diagnostics (**F12**), Lenovo Vantage battery test, HP UEFI diagnostics — they give a definitive pass/fail.
3. **Match the exact part number** when ordering. OEM is safest for internal packs.
4. **Consider a shop** for glued-in batteries or if the connector reseat felt risky. A professional swap is cheaper than a damaged motherboard.

If a new genuine battery still isn't detected, the charging circuit on the motherboard is the fault — that's board-level repair territory. For the companion diagnostic guide, see [laptop only works on AC power troubleshooting](/articles/laptop-only-works-on-ac-power-troubleshooting/).

## Closing

AC-only operation means the battery is electrically absent — and the fix depends on why. Check Windows' view first, then the BIOS disable option, then the drivers: those three free checks resolve most cases. The connector reseat catches the "it worked until I dropped it" cases, and the long charge catches deep discharge. Only when all of those fail is the battery truly dead — and by then, the diagnostics have told you so definitively, so the replacement purchase is a certainty, not a gamble.
