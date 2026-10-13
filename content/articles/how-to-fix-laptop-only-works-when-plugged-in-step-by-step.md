---
title: "Laptop Only Works When Plugged In: Step-by-Step Fix"
slug: how-to-fix-laptop-only-works-when-plugged-in-step-by-step
date: 2026-09-13
categories: ["battery"]
tags: ["plugged in", "battery dead", "power issue"]
description: "Your laptop runs fine on the charger but dies the moment you unplug? Step-by-step diagnosis to find whether the battery, connection, or board is at fault."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-when-plugged-in-step-by-step.webp"
faqs:
  - q: "Why does my laptop only work when plugged in?"
    a: "The battery isn't supplying power. The most common reason is a dead battery with no usable capacity left, but it can also be a disconnected battery, corrupted battery drivers, a failed charging circuit, or a battery stuck in protection mode after a fault."
  - q: "Can I keep using my laptop without a working battery?"
    a: "Yes — it will run normally on adapter power. The risks are losing unsaved work in a power outage and, if the dead battery is swelling, leaving a hazard inside the chassis. Remove or replace a swollen battery promptly; a merely worn one can stay until you replace it."
  - q: "Will removing the battery let the laptop work normally?"
    a: "On models with removable batteries, yes — the laptop runs fine on the adapter alone, sometimes even cooler. For internal batteries, don't remove it unless you're comfortable opening the chassis; a dead-but-present battery is harmless as long as it isn't swelling."
  - q: "How do I confirm the battery is truly dead vs just disconnected?"
    a: "Run powercfg /batteryreport: a detected battery with near-zero full charge capacity is dead; no battery detected at all suggests a connection or driver issue. Reseating the battery and resetting drivers distinguishes the two."
---

A laptop that only works plugged in has been demoted to a desktop. It boots, it runs, it's fast — but the cord is a leash, and one accidental tug means instant black screen and lost work. The battery has stopped participating entirely. Before you buy anything, though, it's worth proving which part actually quit — batteries get blamed for sins committed by drivers and connectors every day.

The fix is a process of elimination across three suspects: the battery itself, its connection to the system, and the software that manages it. Follow the steps in order and the culprit reveals itself.

## Why this happens

- **Battery at end of life:** The most common cause — cells so worn they hold effectively zero charge.
- **Battery in protection mode:** After a fault (over-temperature, deep discharge), the pack's safety circuit can shut it off entirely.
- **Loose or corroded battery connector:** Physical connection issues electrically isolate an otherwise fine battery.
- **Corrupted battery drivers:** Windows may fail to communicate with the battery, treating it as absent.
- **Charging circuit failure:** The motherboard circuit that charges the battery and switches power sources can fail while the adapter path keeps working.
- **BIOS battery cutoff:** Some firmware disables charging to a battery it has flagged as failed, as a safety measure.
- **Swollen battery disconnected by design:** Severe swelling can break internal connections, cutting the battery off electrically.

## How to fix it

Work through these in order, from quick software checks to hardware verdicts.

### Fix 1: Confirm the battery's status in Windows

Start with what the system reports.

1. Plug in and open **Settings > System > Power & battery** — note the percentage, and whether it says "charging," "not charging," or shows no battery.
2. Hover the taskbar battery icon for the detailed status tooltip.
3. Open **Terminal (Admin)** and run `powercfg /batteryreport` to see if the battery is detected and its full charge capacity.
4. If Windows reports the battery at 0% and never charging, or doesn't detect it at all, continue below. For the update-related version of this issue, see [only works when plugged in after Windows 11 update](/articles/how-to-fix-laptop-only-works-when-plugged-in-after-windows-11-update/).

### Fix 2: Reset the battery drivers and embedded controller

Rule out the software layer completely.

1. Open **Device Manager**, expand **Batteries**, and uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
2. Shut down, unplug the adapter, and hold the power button for 30–60 seconds.
3. Reconnect the adapter and boot — Windows rebuilds the driver stack.
4. Unplug briefly to test. If the laptop now runs on battery even for a minute, the drivers were the problem.

### Fix 3: Reseat the battery connection

A physical fix for a physical problem.

1. Shut down and unplug. If the battery is externally removable, slide it out.
2. Inspect the contacts for corrosion or dirt; clean gently with a dry eraser if needed.
3. Reseat firmly — you should feel or hear the latches engage fully.
4. For internal batteries, open the chassis only if warranty allows and you're comfortable; disconnect and reconnect the battery cable, checking that it seats squarely.

### Fix 4: Wake a battery stuck in protection mode

Some packs can be coaxed back.

1. With the laptop off, plug in the correct charger and leave it for 2–3 hours undisturbed.
2. Some batteries need an extended trickle period to exit protection mode — don't interrupt it to "check."
3. Afterward, boot and check whether the battery percentage has moved off zero.
4. If it charges even slightly, run a full calibration cycle to assess how much capacity actually remains.

### Fix 5: Update BIOS and check firmware battery status

Firmware may be blocking the battery deliberately.

1. Install the latest **BIOS** from your manufacturer's support site with the charger connected.
2. Enter the BIOS setup (**F2**, **Del**, or **Esc** depending on brand) and look for a battery health or status readout.
3. If the BIOS reports the battery as failed or not present while Windows sees it, trust the BIOS — it reads the hardware directly.
4. Check [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) for guidance on battery diagnostics if you need a second opinion on the numbers.

### Fix 6: Test with the battery removed (where possible)

Isolate whether the battery is dragging the system down.

1. On removable-battery models, take the battery out and run on the adapter alone for a day.
2. If the laptop is *more* stable without the battery (no random shutdowns), the pack was causing issues beyond just being dead.
3. Check the removed battery for swelling — a bulging pack explains everything and needs safe disposal.
4. Never run a laptop with an internal battery disconnected unless you know what you're doing; the chassis is designed around it.

### Fix 7: Replace the battery or service the board

Reach the final verdict.

1. If the battery report shows near-zero capacity, diagnostics fail it, or it's swollen: replace it with a genuine pack for your exact model.
2. If a brand-new genuine battery *also* doesn't work, the charging circuit or motherboard power path is faulty — that's a service-center repair.
3. Get a repair quote before committing; on older laptops, a motherboard repair can exceed the machine's value.
4. After any battery replacement, calibrate once and verify with a fresh battery report. If the underlying issue is charging rather than the pack, our [battery not charging when plugged in](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/) guide covers that angle.

## Closing

"Only works plugged in" is the battery's resignation letter — but verify it's really the battery before accepting it. Reset the drivers, reseat the connection, wake it from protection mode, and check what the BIOS says. When the evidence confirms a dead pack, a genuine replacement restores the whole point of owning a laptop: leaving the wall behind. Do the checks in order and you'll spend money only on the part that's actually broken.
