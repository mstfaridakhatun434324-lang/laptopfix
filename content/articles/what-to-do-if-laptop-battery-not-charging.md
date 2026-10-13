---
title: "What to Do If Your Laptop Battery Won't Charge at All"
slug: what-to-do-if-laptop-battery-not-charging
date: 2026-09-14
categories: ["battery"]
tags: ["battery not charging", "ac adapter", "troubleshooting"]
description: "Laptop battery completely dead and won't take a charge? Before you buy a replacement, run through these checks — most are free and fast."
thumbnail: "/images/thumbs/what-to-do-if-laptop-battery-not-charging.webp"
faqs:
  - q: "What's the difference between 'not charging' and 'plugged in, not charging'?"
    a: "'Plugged in, not charging' means Windows sees the adapter but chooses not to charge — often a charge limit or driver issue. A battery that won't charge at all shows no charging activity, keeps draining, or isn't detected — pointing more toward adapter, battery, or hardware faults."
  - q: "Can a completely dead battery be revived?"
    a: "Sometimes. A battery that sat at 0% for months may have entered deep-discharge protection. Leaving it on the charger for several hours (powered off) can occasionally wake it. But a battery that won't hold any charge after that is chemically spent."
  - q: "How do I know if it's the charger or the battery?"
    a: "If the laptop runs fine on the adapter with the battery removed (or with the battery at 0% but powered), the adapter delivers power and the battery is suspect. If the laptop won't even power on with the adapter, the adapter or charging circuit is suspect."
  - q: "Is it safe to keep using a laptop whose battery won't charge?"
    a: "Generally yes, as a desktop — running on AC power with a dead battery is fine. The exception is a swollen battery: if the case is bulging or the trackpad is lifting, stop using it and get the battery replaced or removed professionally."
---
There's a special kind of dread in watching your battery percentage tick downward while the charger is plugged in. Not "plugged in, not charging" — just... nothing. No charging icon, no progress, the slow march toward a black screen.

A battery that won't charge at all is a broader problem than the "plugged in, not charging" message, and it needs a broader approach: adapter, cable, port, driver, firmware, and finally the battery itself. The good news is that most of these checks cost nothing. Let's find out what's actually broken before you spend money.

## Why this happens

- **The adapter isn't delivering power.** Dead bricks, frayed cables, and loose DC jacks are the single most common cause of a total no-charge situation. Adapters fail more often than batteries.
- **The charging port is damaged or dirty.** A wobbly DC jack, bent USB-C port, or pocket lint packed into the connector can break the connection intermittently or completely.
- **The battery has entered deep-discharge protection.** Lithium batteries that sit at zero for a long time trip a safety cutoff. The controller may refuse charging until the cells recover slightly — or permanently, if they've degraded too far.
- **The battery driver stack is broken.** Without the ACPI battery driver functioning, Windows can't manage charging at all. This often follows major Windows updates.
- **The embedded controller or BIOS is misbehaving.** Charging is orchestrated by firmware. Corrupt EC state or buggy BIOS versions can halt charging entirely, sometimes after an update.
- **The battery is genuinely at end of life.** High wear, a failed cell group, or a dead controller chip means no amount of software fiddling will bring it back. A [battery health check](/articles/how-to-check-battery-health-on-windows-11-laptop/) quantifies this.

## How to fix it

Work through these in order, from the wall outlet inward.

### Fix 1: Verify power is actually reaching the laptop

Start at the wall — you'd be surprised how often the problem is upstream.

1. Plug the adapter into a wall outlet you know works (test it with a lamp or phone charger). Avoid power strips for this test.
2. Check the adapter's indicator light, if it has one. No light with a known-good outlet means the brick is likely dead.
3. Inspect the full cable for damage, and check the connector: USB-C ends should be clean and straight; barrel connectors shouldn't wobble in the jack.
4. Listen and feel: a working adapter gets slightly warm and some emit a very faint hum. Stone cold and silent while plugged in is a bad sign.

### Fix 2: Test with a different adapter

This single test eliminates half the possibilities.

1. Borrow or buy an adapter with the correct connector and equal or higher wattage than your original (wattage is printed on the brick — match or exceed it).
2. For USB-C laptops, any quality USB-C PD charger of sufficient wattage works for testing — this is the easiest standard to borrow.
3. If the battery charges with the test adapter, your adapter is the problem. Replace it with the correct wattage; underpowered adapters cause their own set of [charging problems](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/).
4. If it still doesn't charge, the adapter is innocent — continue.

### Fix 3: Clean and inspect the charging port

A surprising number of "dead" laptops just have dirty ports.

1. Power off and unplug everything. Shine a flashlight into the charging port.
2. For USB-C: use a wooden toothpick or plastic pick to gently remove lint and debris. Never use metal — you'll short the pins.
3. For barrel jacks: check that the center pin isn't bent and the jack doesn't wobble. A loose DC jack usually needs professional resoldering.
4. Blow out dust with compressed air, reconnect firmly, and test.

### Fix 4: Try to wake a deeply discharged battery

If the battery sat at 0% for weeks or months, it may be in protection mode.

1. Power the laptop completely off (not sleep — full shutdown).
2. Plug in the known-good charger and leave it, powered off, for at least 3–4 hours. Some controllers need an extended quiet charge to lift cells above the safety threshold.
3. Check for any charging LED. Some laptops show an amber light during this recovery even with the lid closed.
4. After several hours, try powering on. If it boots and shows even 1–2%, the battery woke up — let it charge fully, then run a calibration cycle. If there's still zero response, the cells are likely beyond recovery.

### Fix 5: Reinstall the battery drivers

When Windows can't talk to the battery, it can't charge it either.

1. Open **Device Manager** (**Windows key + X > Device Manager**), expand **Batteries**.
2. Right-click each entry and choose **Uninstall device**. Include **Microsoft AC Adapter** if listed.
3. Shut down fully, disconnect the charger for 30 seconds, reconnect, and boot. Windows rebuilds the entire battery driver stack.
4. Check the battery icon for charging activity. If Windows now detects the battery but it still won't charge, the hardware side is the problem.

### Fix 6: Reset the embedded controller

The EC manages charging at the hardware level, and it can get stuck.

1. Shut down, unplug the charger, and disconnect all peripherals.
2. If the battery is removable, take it out. Hold the power button for 20–30 seconds.
3. Reinsert the battery, reconnect the charger (directly to a wall outlet), wait one minute, then power on.
4. For sealed laptops, the same procedure without battery removal still drains residual power and resets the EC on most models.

### Fix 7: Update BIOS and run the numbers

Firmware bugs and dead batteries are the two remaining explanations.

1. Check your BIOS version with `msinfo32` and update from your manufacturer's support page if a newer one exists — [Dell](https://www.dell.com/support), [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en/). Keep the charger connected during the update.
2. Generate a battery report: `powercfg /batteryreport` in an elevated Terminal. If **FULL CHARGE CAPACITY** is a small fraction of **DESIGN CAPACITY** (or the battery isn't detected at all), the battery is spent.
3. If the battery isn't detected even after driver reinstalls, try reseating it (if accessible). A battery that remains invisible to the system has a dead controller or broken connection.
4. For a confirmed-dead battery, buy a genuine replacement matched to your exact model — and recycle the old one properly instead of binning it.

## Closing

A battery that won't charge at all is telling you to check the power path from the wall inward: outlet, adapter, port, then drivers and firmware, and only then the battery itself. Most of the time the culprit is the adapter or a stuck controller — both fixable without buying parts. And when it really is the battery, the report numbers will tell you honestly, so you're spending money on certainty instead of hope.
