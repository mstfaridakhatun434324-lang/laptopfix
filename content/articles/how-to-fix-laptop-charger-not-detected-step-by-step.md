---
title: "How to Fix a Laptop Charger Not Detected, Step by Step"
slug: how-to-fix-laptop-charger-not-detected-step-by-step
date: 2026-10-04
categories: ["battery"]
tags: ["charger not detected", "laptop not recognizing charger", "ac adapter fix"]
description: "Laptop doesn't see the charger at all? Work from the wall outlet to the motherboard — every step to get charging detected again."
thumbnail: "/images/thumbs/how-to-fix-laptop-charger-not-detected-step-by-step.webp"
faqs:
  - q: "What does it mean when the charger is 'not detected'?"
    a: "The laptop shows no charging indicator, no 'plugged in' status — as if nothing is connected. That means the break is at the physical or electrical level (outlet, adapter, cable, port) or in the detection path (EC firmware, AC adapter driver), rather than a battery-chemistry problem."
  - q: "How do I know if the problem is the charger or the laptop?"
    a: "Test in isolation: try the charger in a different outlet, inspect it for damage and LED behavior, then test the laptop with a known-good compatible charger. If a good charger works, your adapter is dead. If no charger is detected, the laptop's port, EC, or charging circuit is suspect."
  - q: "Can a USB-C charger not be detected even if it fits?"
    a: "Yes — fitting isn't enough. The charger must support USB Power Delivery at your laptop's required wattage, and the cable must be rated for that power. Phone chargers and charge-only cables fit the port but won't register as a valid laptop charger."
  - q: "Is it safe to keep using the laptop while the charger isn't detected?"
    a: "You're just running on battery, which is safe but finite. The risk is data loss when the battery runs out mid-work. Save often, lower brightness, and avoid heavy tasks until charging is restored — or shut down to preserve the remaining charge."
---

"Plugged in, not charging" is one problem. The charger not being detected at all — no LED change, no taskbar indication, Windows acting like nothing is plugged in — is a different, more fundamental one. Somewhere between the wall socket and the motherboard, the connection is broken, and the laptop can't even start the charging conversation.

The fix is a process of elimination from the wall inward. Don't skip steps — the cause is found by ruling things out in order, not by guessing.

## Why this happens

- **The outlet or power strip is dead.** The most embarrassingly common cause — the charger was never getting power to begin with.
- **The adapter died.** Charger bricks fail: internal fuse blows, cable breaks at the strain relief, or the brick silently stops delivering power.
- **The cable or connector is damaged.** Frayed cables, bent barrel-plug pins, or worn USB-C connectors break the electrical path.
- **The laptop's charging port is damaged.** Loose DC jacks and debris-filled USB-C ports are common after years of plugging and unplugging.
- **Wrong charger, wrong wattage.** An underpowered or non-PD adapter may not be recognized as a valid charger at all.
- **The EC or AC driver glitched.** The embedded controller and the Microsoft AC Adapter driver handle detection; both can lock up.

## How to fix it

Work strictly in order, wall to motherboard. Stop when detection returns.

### Fix 1: Verify power at the wall

1. Unplug the charger from the laptop, but leave it connected to the wall.
2. Check the charger's LED (if it has one) — dark means no power reaching the brick.
3. Plug a phone charger or lamp into the same outlet to confirm the outlet is live.
4. Bypass power strips, extension cords, and surge protectors — plug directly into a wall socket.
5. Try a second outlet in a different room to rule out a tripped breaker or dead circuit.
6. Only continue when you're certain the outlet delivers power — this step alone resolves a surprising number of cases.

### Fix 2: Inspect the charger and cable

1. Examine the entire cable for fraying, kinks, chew marks, or exposed wire — especially at the strain reliefs near the brick and the connector.
2. Check barrel-plug connectors for bent or broken center pins; check USB-C plugs for debris or bent contacts.
3. Smell the brick — a burnt-plastic odor means it's dead, stop using it.
4. Feel the brick after 10 minutes plugged into the wall (disconnected from laptop): stone cold with no LED suggests a dead adapter; extremely hot suggests internal failure.
5. Confirm the wattage on the label matches your laptop's requirement — a 45W adapter on a 130W gaming laptop may not register. Our [charger wattage guide](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-in-windows-11-24h2/) explains the matching rules.

### Fix 3: Inspect and clean the laptop's charging port

1. Power off the laptop and unplug everything.
2. Shine a light into the charging port — look for lint, debris, bent pins (barrel jacks), or damaged tongues (USB-C).
3. Remove debris gently with a wooden toothpick or compressed air — never metal tools, and never while powered.
4. Wiggle the connector gently when plugged in: if detection flickers, the port is loose or worn — a repair-shop job, but now you know.
5. For USB-C laptops, try a different USB-C port if the model charges from more than one.

### Fix 4: Test with a known-good charger

1. Borrow an original charger of the correct wattage for your exact model — this is the single most definitive test.
2. If the borrowed charger is detected immediately, your adapter is dead — replace it with the correct part, not a random universal brick.
3. If no charger is detected, the problem is in the laptop — continue below.
4. For USB-C models, test with a quality PD charger at the rated wattage *and* a rated cable — this isolates port vs. adapter issues.
5. Note the result carefully; "known-good charger also not detected" changes the diagnosis completely.

### Fix 5: Reset the embedded controller

1. Shut down, unplug the charger and all peripherals.
2. Hold the **Power** button for **30 seconds**.
3. If the battery is removable, remove and reseat it during this process.
4. Reconnect only the charger, wait 30 seconds, then power on.
5. Check for the charging indicator immediately at boot — EC lockups commonly cause total non-detection.
6. Some models have a battery reset pinhole on the bottom — use it per the manual as an alternative EC reset.

### Fix 6: Reinstall the AC adapter driver

1. Press **Win + X**, open **Device Manager**.
2. Expand **Batteries** — right-click **Microsoft AC Adapter** > **Uninstall device**.
3. Also uninstall **Microsoft ACPI-Compliant Control Method Battery**.
4. Shut down fully, unplug the charger 30 seconds, reconnect, power on.
5. Windows reinstalls the detection stack at boot — check whether the charger now registers.
6. If Device Manager shows the AC adapter with a warning icon after reinstall, note the error code — it's a lead for support.

### Fix 7: Update BIOS and check for deeper faults

1. If detection is intermittent or absent with known-good chargers, update the **BIOS** from your maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — since charge detection logic lives in firmware.
2. After the BIOS update, repeat the EC reset (Fix 5) once.
3. If still nothing: the charging port, charging circuit, or motherboard power path has likely failed — this is professional repair territory. Get a quote; compare against the laptop's value.
4. As a stopgap, minimize battery use: enable [hibernation](/articles/how-to-enable-hibernation-to-save-battery-on-windows-11/), lower brightness, and shut down (not sleep) to preserve the remaining charge for essential use.
5. If the battery is also old, check its health with our [battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/) — you'll want to know its condition while planning the repair.

## Closing

Charger-not-detected is a chain, and you find the broken link by walking it: live outlet, intact cable, clean port, known-good adapter, EC reset, driver reinstall, BIOS. Most breaks are in the first four links — the cheap, external ones. Work the chain in order, don't guess, and you'll know exactly which part failed and what it costs to fix.
