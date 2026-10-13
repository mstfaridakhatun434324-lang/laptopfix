---
title: "Laptop Shuts Off the Moment You Unplug It? Do This"
slug: how-do-i-fix-laptop-only-works-when-plugged-in
date: 2026-10-04
categories: ["battery"]
tags: ["dies on unplug", "battery failure", "AC only", "power issues"]
description: "If unplugging the charger kills your laptop instantly, the battery is out of the picture. Diagnose it and get portable power back."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-only-works-when-plugged-in.webp"
faqs:
  - q: "Why does my laptop die instantly when unplugged but shows 100% battery?"
    a: "A 100 percent reading on a battery that cannot power the laptop for a second means the gauge is wrong or the pack cannot deliver current under load. Worn cells can show full voltage with no load but collapse the moment the laptop draws power. A battery report and a load test confirm it."
  - q: "Can I damage my laptop by using it without a battery?"
    a: "Running on AC with the battery removed is generally safe on most laptops, but you lose all protection against power flickers — one blip and the machine dies instantly, risking data loss. It is a fine diagnostic step, not a lifestyle. Replace the battery when you can."
  - q: "Does a swollen battery cause instant shutdown on unplug?"
    a: "It can. Swelling indicates internal damage, and damaged packs often cannot deliver stable current. More importantly, a swollen battery is a safety hazard: stop using it, do not puncture or compress it, and replace it promptly through proper channels."
  - q: "How long should a laptop battery last before this happens?"
    a: "Most laptop batteries deliver useful life for 2 to 4 years or 300 to 500 full cycles before capacity drops sharply. Heavy heat, constant 100 percent charging, and frequent deep discharges shorten that. If yours died much sooner, a defect or harsh conditions are likely."
---

There is a special kind of annoyance in a "portable" computer that is actually a desktop: yank the charger, instant black screen. No warning, no low-battery countdown — the machine simply cannot run without wall power. The battery might as well be a paperweight right now.

This is almost always a battery problem rather than a Windows problem: a pack that cannot hold charge, cannot deliver current, or is not connected at all. The fixes below prove which one you have and get you mobile again. For the closely related case where the charger is connected but the battery refuses to charge, see [plugged in but not charging](/articles/how-to-fix-laptop-plugged-in-not-charging-step-by-step/).

## Why this happens

- **Cells too worn to deliver current.** Voltage looks fine idle but collapses under load — the classic end-of-life pattern.
- **Battery not detected by the system.** Loose connector, corrosion, or a dead battery controller.
- **Tripped protection circuit.** Deep discharge or a fault locked the pack's output.
- **Swollen or physically damaged pack.** Internal damage kills current delivery and is a safety issue.
- **Badly miscalibrated gauge.** Rare, but a confused gauge can mask a battery that is actually empty.
- **Motherboard power-path fault.** The board cannot switch from AC to battery power.
- **Wrong battery installed.** An incompatible third-party pack the system refuses to draw from.
- **BIOS battery setting disabled the pack.** Some BIOS versions have a battery disconnect or ship-mode option that cuts the pack off entirely until toggled.

## How to fix it

Work through these in order — start with Fix 1 and only move on if unplugging still kills the machine.

### Fix 1: Confirm the symptom and check detection

Unplug the charger and note exactly what happens: instant off, or a few seconds of life? Then plug back in, boot, and click the taskbar battery icon. "No battery is detected" means a connection or controller problem — jump to Fix 4. A percentage that looks normal but dies on unplug means the pack cannot deliver current — continue to Fix 2. Also try this: with the charger plugged in, shut down, unplug for 10 seconds, and plug back in. If the charging LED behaves oddly (wrong color, flickering), note it; LED codes help identify battery faults on Dell, HP, and Lenovo machines.

### Fix 2: Get the battery report verdict

Open an elevated **Command Prompt** and run:

```
powercfg /batteryreport
```

Open **battery-report.html** and compare **Design Capacity** to **Full Charge Capacity**. Under 25 percent of design is a dead pack, plain and simple. Also check **Cycle count** if shown — over 800 cycles on a consumer pack is a full life. If the report shows no battery section at all, Windows cannot see the pack and you have a detection problem, not a wear problem. Our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) walks through interpreting every number.

### Fix 3: Hard reset the power system

Shut down fully, unplug the adapter, and remove the battery if it is removable. Press and hold the power button for 30 seconds — this drains flea power and resets the embedded controller. Reconnect the adapter only and boot to Windows, then shut down, reinstall the battery, plug in, and charge undisturbed for two hours. Unplug and test. This clears tripped protection circuits that lock the pack's output after deep discharges, and it is the fix most people skip who should not.

### Fix 4: Reseat the battery and inspect everything

For removable packs: power off, remove the battery, and inspect the terminals on both the pack and the laptop for corrosion, bent pins, or debris. Clean with a dry microfiber cloth. Check the pack itself for swelling — any bulging, a trackpad that feels raised, or a bottom panel that does not sit flat means stop: that battery is unsafe, do not reinstall it. For internal batteries, reseating means opening the machine — only attempt if comfortable and out of warranty, with the adapter disconnected. A connector jarred loose by a drop is a textbook cause of sudden AC-only operation.

### Fix 5: Reinstall the battery drivers

Open **Device Manager**, expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and select **Uninstall device**. Also uninstall **Microsoft AC Adapter** if present. Click **Action > Scan for hardware changes**, then restart. If Windows was misreading the battery — showing phantom percentages or missing it entirely — fresh drivers restore proper communication. Test on battery after the reboot.

### Fix 6: Replace the battery with the right part

When the report shows a worn pack, replacement is the answer — no software revives spent chemistry. Buy a genuine battery matching the exact part number printed on your old pack, from the manufacturer or an authorized seller. Skip suspiciously cheap third-party packs: wrong cells and missing safety circuits cause the exact symptoms you are fixing, and can be dangerous. After installing, charge to 100 percent uninterrupted, then calibrate with one full discharge-charge cycle. Maker part finders like [HP's support pages](https://support.hp.com/us-en) help you match the right part number.

### Fix 7: Test for a motherboard fault

If a new genuine battery changes nothing, the motherboard's power circuitry is suspect — the charge controller or the AC/battery switchover. Clues: the battery charges normally in a different identical laptop, or two known-good batteries behave identically in yours. This is board-level diagnosis: get a quote from a reputable repair shop. Weigh the repair cost against the laptop's age and value — on a five-year-old budget machine, the money is often better put toward a replacement.

## Closing

Instant death on unplug is the battery waving a white flag — worn out, disconnected, or locked by its own protection. The battery report tells you which in minutes, a hard reset clears the tripped cases, and a genuine replacement restores the rest. Do not settle for a "portable" that is chained to the wall; the fix is usually one battery swap away, and your shoulders will thank you.
