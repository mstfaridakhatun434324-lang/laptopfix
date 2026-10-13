---
title: "Laptop Dies the Second You Unplug It? Fix It After the Windows 11 Update"
slug: how-to-fix-laptop-only-works-when-plugged-in-after-windows-11-update
date: 2026-10-07
categories: ["battery"]
tags: ["only works plugged in", "battery dead", "windows 11 update", "power issue"]
description: "Your laptop shuts off instantly when unplugged after a Windows 11 update? Diagnose whether it's the battery, the driver, or the charger."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-when-plugged-in-after-windows-11-update.webp"
faqs:
  - q: "Why does my laptop turn off immediately when I unplug the charger?"
    a: "The battery isn't delivering power — either it's deeply discharged, its protection circuit has tripped, the battery driver is broken after the update, or the cells are dead. If it happens suddenly right after an update, suspect software or a tripped protection circuit before assuming dead cells."
  - q: "Can a Windows update kill a laptop battery?"
    a: "No, updates can't damage cells. But they can corrupt the battery driver so Windows can't use the battery, or trigger a protection-circuit trip during the update's restart cycle. Both look exactly like a dead battery but are fully reversible."
  - q: "How do I test if my battery is dead or just disconnected?"
    a: "Shut down, unplug, hold the power button 30 seconds, then plug in and boot. Check Device Manager > Batteries for warning icons, and run powercfg /batteryreport to see if Windows sees any capacity at all. Zero reported capacity with no detection usually means hardware."
  - q: "Is it safe to use a laptop with a dead battery permanently plugged in?"
    a: "Yes, with caveats. It works fine as a desktop, but you lose all protection against power cuts — unsaved work vanishes instantly. Also remove or replace a swollen battery immediately; never keep using a bulging pack."
---

Unplug the charger and the screen goes black instantly. No warning, no "low battery" — just dead, as if you'd yanked the power cord from a desktop. It's the most alarming thing a laptop can do short of smoking, because it breaks the basic promise of portability. Plug it back in, it boots fine, and the battery icon might say 100%, 0%, or show nothing at all — three different lies for the same underlying problem. Since the Windows 11 update, your "laptop" has become a very small desktop, tethered to the wall.

This symptom has a short list of causes, which is good news: battery not delivering power comes down to a tripped protection circuit, a broken driver handshake, a truly dead pack, or a charger problem masquerading as a battery issue. Work the list and you'll know which within the hour — and you'll know it from evidence, not guesswork. If Windows reports [no battery detected](/articles/laptop-battery-not-detected-windows-11/) at all, start there — the fixes overlap.

## Why this happens

- **The battery's protection circuit tripped.** A voltage anomaly during the update's restart cycle can make the battery's safety board disconnect the cells — reversible with a full reset.
- **The battery driver broke.** If Windows can't communicate with the battery after the update, it can't draw from it either; the machine behaves as if no battery exists.
- **The battery is deeply discharged.** A pack drained to absolute zero sometimes needs an extended trickle charge before the controller allows discharge again.
- **The cells are genuinely dead.** Old batteries can fail suddenly — one weak cell group hitting its cutoff makes the whole pack cut out under load.
- **The charger is faulty, not the battery.** A dying adapter may deliver enough to run the laptop but trigger protection circuits that confuse the whole power system.
- **A loose internal battery connector.** The update's forced restarts involve thermal cycling that can worsen an already-loose connector until contact breaks.
- **Corrupted power management firmware settings.** The update can flip BIOS-level battery settings (like battery disconnect for service mode) that cut the pack off electrically until reset.

## How to fix it

Work through these in order — they go from "free and instant" to "buy a part."

### Fix 1: The 30-second power reset

1. Shut down completely and unplug the charger.
2. Disconnect every peripheral, dock, and USB device.
3. Hold the power button down for a full 30 seconds, then release.
4. Plug the charger into a wall outlet, wait 10 seconds, and power on.
5. Unplug the charger for 10 seconds and see if the laptop survives — this reset alone revives tripped protection circuits surprisingly often.

### Fix 2: Charge undisturbed for two hours

1. With the laptop powered off, plug in the charger and leave it for two full hours.
2. Don't power on to "check" — some deeply discharged packs only accept trickle charge while off.
3. Watch the charging LED if your model has one: no light at all for the first 30 minutes can be normal for a deeply depleted pack, but no light after two hours points to a dead pack or bad charger.
4. After two hours, boot up and check the reported percentage.
5. If it now holds a charge, the pack was just deeply depleted, not dead.

### Fix 3: Reinstall the battery drivers

1. Open **Device Manager** (right-click **Start**).
2. Expand **Batteries** and uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. Click **Action > Scan for hardware changes**.
4. Restart, then test on battery power. A broken post-update driver is a top cause of this exact symptom.

### Fix 4: Disable Fast Startup and cold boot

1. Go to **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully (not restart) and power back on with the charger connected.
4. Unplug and test. Fast Startup's cached device state can include a "battery unavailable" flag from the update reboot.

### Fix 5: Inspect the battery physically

1. Power off and unplug. If the battery is removable, take it out.
2. Look for swelling — any bulging, rounded shape, or a trackpad/keyboard that's lifting means stop immediately and replace it.
3. Check the contacts for corrosion or dirt; clean with a dry cloth.
4. Reseat firmly. On sealed laptops, only open the case if you're comfortable doing so.
5. A swollen battery is a safety issue: don't charge it, don't puncture it, recycle it properly.

### Fix 6: Test the charger and check battery health data

1. Borrow a correct-wattage charger and test whether the laptop runs on battery with it connected-then-removed.
2. Run `powercfg /batteryreport` in **Terminal (Admin)** — if Windows reports no battery or zero capacity, that's a hardware-level answer.
3. Check the capacity history: a gradual decline to nothing means natural death; a sudden cliff means an event (like the update restart) tripped something.
4. A [full battery health check](/articles/how-to-check-battery-health-on-windows-11-laptop/) confirms whether replacement is warranted.

### Fix 7: Update the BIOS, then replace the battery if needed

1. Flash the latest BIOS from your manufacturer's support site on wall power.
2. Load optimized defaults in the BIOS setup afterward.
3. If the laptop still dies the instant it's unplugged, the pack is done — order a genuine replacement for your exact model.
4. After installing the new battery, charge to 100% uninterrupted before the first unplugged use.

## Closing

A laptop that only works plugged in is telling you the battery has left the conversation — the question is whether it left voluntarily (tripped protection, broken driver) or permanently (dead cells). The resets and driver fixes answer that question for free, usually in less time than it takes to research replacement batteries. Only when they all fail should you conclude the battery itself is gone, and by then you'll know it with confidence instead of guessing.
