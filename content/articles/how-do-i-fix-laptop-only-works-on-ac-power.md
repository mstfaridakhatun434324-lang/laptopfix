---
title: "Laptop Only Works on AC Power? Here's the Fix"
slug: how-do-i-fix-laptop-only-works-on-ac-power
date: 2026-10-03
categories: ["battery"]
tags: ["ac power", "battery dead", "won't hold charge", "troubleshooting"]
description: "Laptop dies the instant you unplug it? Diagnose why your laptop only works on AC power and get it running on battery again."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-only-works-on-ac-power.webp"
faqs:
  - q: "Why does my laptop turn off when I unplug the charger?"
    a: "The battery isn't delivering power — either it's completely worn out, it's not detected by the system, the battery driver is corrupted, or there's a hardware disconnect. If the laptop runs fine on AC but dies instantly unplugged, the battery (or its connection) is the problem, not the charger or Windows."
  - q: "Can a dead battery cause a laptop to only work plugged in?"
    a: "Yes — this is the most common cause. A lithium battery that's degraded past usefulness, or one with a failed cell, can't sustain the laptop for even a second. The laptop then behaves exactly like a desktop: fine on AC, dead without it."
  - q: "Will my laptop work without a battery if it's plugged in?"
    a: "Most laptops run fine on AC power with the battery removed or dead — that's why yours still works plugged in. But you lose your built-in UPS: any power flicker means an instant shutdown, so don't do critical work without the battery as backup."
  - q: "How do I know if I need a new battery?"
    a: "Check the battery report (powercfg /batteryreport): if full charge capacity is a small fraction of design capacity, or the battery isn't detected at all after driver resets, replacement is the answer. Physical signs like swelling or extreme heat mean replace immediately."
---
Your laptop works perfectly — as long as the charger stays plugged in. The second you unplug, it's instant black screen, no warning, no graceful shutdown. You've basically got a very portable desktop.

This symptom narrows things down nicely: the charger, the wall power, and Windows itself are all fine. The problem is somewhere between the battery and the motherboard. Let's find it.

## Why this happens

- **The battery is completely worn out.** A battery degraded past the point of usefulness can't deliver even a few seconds of power — the laptop dies the instant AC disappears.
- **The battery isn't detected.** If Windows can't see the battery (driver issue, loose connection, failed battery controller), it can't draw from it.
- **A cell has failed.** One dead cell in the pack can collapse the whole pack's voltage under load, causing instant shutdown on unplug.
- **The battery connector is loose or corroded.** Especially after drops or on older removable-battery models, poor contact means no power flows.
- **The charging circuit is faulty.** Less common, but a failed charging IC on the motherboard can leave the battery uncharged and unusable even though AC passthrough works.
- **BIOS battery settings are wrong.** Some BIOS versions have battery disconnect, ship mode, or calibration settings that can leave the battery logically disconnected.

## How to fix it

Work through these in order — software first, then hardware.

### Fix 1: Check what Windows sees

Start by confirming whether the battery is detected at all.

1. Hover over the **battery icon** in the taskbar — note exactly what it says (percentage, "plugged in," or nothing).
2. Open **Command Prompt as administrator** and run: `powercfg /batteryreport /output "C:\battery-report.html"`
3. If the report shows **no battery information**, Windows can't see the battery — continue with the driver and hardware fixes below. Our [battery not detected guide](/articles/how-to-fix-battery-not-detected-on-laptop/) covers this path in full.

### Fix 2: Reset the battery driver

A corrupted driver can make a healthy battery invisible.

1. Press **Win + X**, open **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery**, choose **Uninstall device**.
3. If you see **Microsoft AC Adapter**, leave it alone.
4. Shut down (don't restart), unplug AC, wait **30 seconds**, plug AC back in, and power on.

### Fix 3: Power-cycle the embedded controller

The EC manages battery communication and sometimes needs a reset.

1. Shut down the laptop completely and unplug the charger.
2. If the battery is **removable**, take it out; if it's **internal**, hold the **power button for 30–60 seconds** with everything unplugged.
3. Reinsert/reconnect, plug in AC, and power on.
4. Check whether the battery is now detected and charging.

### Fix 4: Inspect the physical battery

For removable batteries, this takes two minutes.

1. Power off, unplug, remove the battery, and inspect the **contacts** for corrosion, dirt, or bent pins — clean gently with a dry cloth or pencil eraser.
2. Look for **swelling** — if the battery is puffed up or the case doesn't sit flat, stop here and replace it (see our [swollen battery safety guide](/articles/how-to-fix-laptop-battery-swelling-reddit/)).
3. Reseat the battery firmly, plug in AC, and check detection.

### Fix 5: Check BIOS battery settings

Firmware can logically disconnect the battery.

1. Restart into **BIOS/UEFI** (**F2**, **Del**, or **Fn+F2** depending on brand).
2. Look for battery options — **ship mode**, **battery disconnect**, or calibration settings — and make sure the battery is enabled/connected.
3. While there, check whether the BIOS itself reports battery health; many Dell, HP, and Lenovo BIOS setups show it.
4. Save with **F10** and exit.

### Fix 6: Test with a known-good battery (if possible)

This definitively separates battery failure from motherboard failure.

1. If you can borrow an identical battery or your model has a removable battery you can test, swap it in.
2. If the laptop runs on battery with the test unit, your battery is dead — replace it.
3. If it still dies instantly, the charging circuit or motherboard is at fault — that's a repair-shop job.

### Fix 7: Replace the battery

When the diagnosis points at the battery, don't delay.

1. Buy a **genuine or high-quality replacement** for your exact model — cheap no-name batteries are a false economy and a safety risk.
2. Follow the manufacturer's replacement guide (many are on [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support pages).
3. After installing, run one full **calibration cycle** (charge to 100%, discharge to shutoff, recharge) so the gauge learns the new battery.

## Closing

"Laptop only works on AC" is actually one of the more diagnosable battery problems — the instant-death-on-unplug symptom points squarely at the battery or its connection, and the steps above will tell you which within half an hour. If the battery turns out to be merely worn rather than dead, our [guide to batteries that won't hold charge](/articles/how-to-fix-laptop-battery-won-t-hold-charge-after-windows-11-update/) covers the middle ground. And if Windows can't see the battery at all, the [not-detected troubleshooting path](/articles/troubleshoot-laptop-only-works-on-ac-power/) continues from here. Whatever the outcome, don't put off the fix: running indefinitely without a working battery means every power flicker is a potential data-loss event. Laptops are designed with the battery as part of the power system, not just a portable extra — restoring it restores the machine's resilience, not just its mobility.

If a replacement battery is on order and you're limping along on AC in the meantime, a small uninterruptible power supply (UPS) is a worthwhile stopgap — even a basic one gives you the few minutes of ride-through that the dead battery used to provide, turning power flickers from crashes into non-events. And once the new battery arrives, run that first calibration cycle promptly; a fresh battery with an uncalibrated gauge will give you strange percentages for its first few cycles, which is normal and settles down on its own.
