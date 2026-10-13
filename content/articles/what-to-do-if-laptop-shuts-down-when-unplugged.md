---
title: "Laptop Shuts Down When Unplugged? Do This"
slug: what-to-do-if-laptop-shuts-down-when-unplugged
date: 2026-09-14
categories: ["battery"]
tags: ["laptop shuts down unplugged", "laptop dies without charger", "laptop only works plugged in"]
description: "Laptop dies the instant you unplug it? Find out whether it's a dead battery, a broken connector, or a settings issue — and fix it."
thumbnail: "/images/thumbs/what-to-do-if-laptop-shuts-down-when-unplugged.webp"
faqs:
  - q: "Why does my laptop shut off immediately when I unplug it?"
    a: "The battery isn't delivering power — either it's completely worn out, it's not detected by the system, or its internal safety circuit has tripped. In rare cases a broken battery connector or a failed charging circuit is the cause rather than the pack itself."
  - q: "The battery shows 100% but the laptop dies when unplugged. How?"
    a: "The percentage is a software estimate from the fuel gauge. If the gauge is badly miscalibrated or the battery's output circuit has failed, Windows can show 100% while the pack delivers zero usable power. A battery report reveals the truth."
  - q: "Is it safe to keep using a laptop that only works plugged in?"
    a: "Generally yes, as a desktop replacement — but back up your data. If the battery is swollen or the shutdowns are accompanied by heat or smells, stop using it and replace the battery. A dead pack can sometimes swell over time."
  - q: "Could this be a Windows setting rather than hardware?"
    a: "Unlikely for instant shutdowns — no Windows power setting kills the machine the moment AC is removed. Settings cause sleep or hibernate issues, not instant death. Instant shutdown on unplug is almost always the battery or its connection."
---
There's a special kind of frustration in a "laptop" that's actually a desktop — one that dies the second the charger comes out. If yours shuts down instantly on unplug, even showing a full battery moments before, the battery isn't delivering power at all. The question is why, and the answer determines whether this is a $50 fix or a repair-shop visit.

Let's diagnose it properly.

## Why this happens

- **Completely worn-out cells:** A battery at the end of its life can show voltage with no load but collapse the instant the laptop draws current.
- **Tripped battery safety circuit:** The pack's protection board can latch into a shutdown state after a fault, cutting output entirely.
- **Battery not detected:** If Windows doesn't see the battery at all, unplugging removes the only power source the system knows about.
- **Broken battery connector:** A loose or corroded internal connector means the pack is fine but electrically disconnected.
- **Severely miscalibrated gauge:** The rare software case — Windows thinks there's charge, but the real state is empty.

## How to fix it

Work through these in order — start with diagnosis, not parts.

### Fix 1: Check whether Windows even sees the battery

This determines the entire direction of troubleshooting.

1. With the charger plugged in, press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. You should see **Microsoft ACPI-Compliant Control Method Battery** and possibly **Microsoft AC Adapter**.
3. If the Batteries section is missing entirely, Windows doesn't detect the pack — skip to Fix 5.
4. Hover the taskbar battery icon: if it says "No battery is detected," that's your answer.

A missing battery in Device Manager points to hardware (connector, pack, or board). A present-but-useless battery points to wear or a tripped safety circuit. For the not-detected case specifically, our [battery not detected fix](/articles/best-way-to-fix-battery-not-detected-on-laptop/) goes deeper.

### Fix 2: Run a battery report for the real numbers

Don't trust the taskbar percentage — get the engineering data.

1. Open an elevated **Command Prompt** and run `powercfg /batteryreport`.
2. Compare **Design Capacity** vs **Full Charge Capacity**. A full charge capacity near zero (or a report that won't generate) confirms a dead pack.
3. Check the usage history for the pattern: if the battery has shown 0 minutes of runtime for weeks, it's been dead a while.

A pack with single-digit percentage of design capacity will collapse under load exactly as you describe. Learn to read the full report in our [battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/).

### Fix 3: Try a full power reset to unlatch the safety circuit

Battery protection boards sometimes trip and need a hard reset to recover.

1. Shut down fully and unplug the charger.
2. If the battery is removable, take it out. If sealed, hold the power button for 30 seconds.
3. Wait 5 full minutes — this drains the protection circuit's latch.
4. Reinstall/reconnect, plug in, and charge for at least an hour before testing.
5. Unplug and see if the laptop stays alive.

This revives packs whose safety circuit tripped on a transient fault. If the pack is genuinely worn out, it won't help — but it's free and takes ten minutes, so it's worth trying.

### Fix 4: Calibrate in case the gauge is lying

The long-shot software fix, for the "shows 100%, dies instantly" symptom.

1. With the charger connected, go to **Settings** > **System** > **Power & battery** and set everything to **Never** sleep — you need it to stay awake.
2. Unplug and let it run until it dies (it may die fast — that's the point).
3. Leave it off overnight, then charge uninterrupted to full.
4. Test on battery again.

If runtime improves, the gauge was miscalibrated. If it still dies instantly, the cells can't sustain a load — that's hardware. Full details in our [calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 5: Reseat the battery and inspect connectors

For removable batteries, a bad connection mimics a dead pack.

1. Shut down, unplug, and remove the battery.
2. Inspect both the battery contacts and the laptop's contacts for corrosion, bent pins, or debris.
3. Clean gently with isopropyl alcohol on a cotton swab and let dry.
4. Reseat firmly — it should click or sit flush with no wobble.
5. Boot on AC, then test on battery.

For sealed laptops, don't open the chassis unless you're experienced and out of warranty — but do check for swelling (a rocking laptop on a flat table), which means the pack needs professional replacement regardless.

### Fix 6: Reset the ACPI driver and update the BIOS

Clear any software layer that could be mismanaging the battery.

1. In **Device Manager**, uninstall **Microsoft ACPI-Compliant Control Method Battery** under **Batteries**.
2. Shut down fully, unplug for 30 seconds, plug back in, and boot.
3. Update the BIOS from your manufacturer's support page — EC firmware manages the battery power path.
4. Test on battery after each step.

This rarely fixes instant-shutdown-on-unplug by itself, but it eliminates the software variables before you spend money on hardware.

### Fix 7: Replace the battery

When diagnostics point to a dead pack, replace it.

1. Confirm with the battery report: near-zero full charge capacity or a pack Windows can't detect at all.
2. Order a genuine or high-quality battery for your exact model number — not just the laptop series.
3. Removable: swap it yourself and run a calibration cycle. Sealed: use manufacturer service or a reputable shop.
4. If a new genuine battery still isn't detected, the charging circuit or motherboard power path has failed — that's a board-level repair, and it's time for a professional quote.

Don't buy the cheapest pack on a marketplace — counterfeit batteries with fake capacity ratings are rampant, and a bad pack can damage the charging circuit. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) covers the software side, but this fix is firmly hardware.

## Closing

Instant death on unplug is the battery telling you it can't deliver power — usually because its cells are spent, occasionally because its safety circuit tripped or its connector failed. The battery report and Device Manager tell you which in minutes. Reset what can be reset, reseat what can be reseated, and replace what's genuinely dead. And back up your data now — a laptop living on AC power alone is one tripped breaker away from losing unsaved work.
