---
title: "How to Test a Laptop Charger in Windows 11 (Proven Methods)"
slug: how-to-test-laptop-charger-in-windows-11-24h2
date: 2026-10-09
categories: ["battery"]
tags: ["test charger", "adapter test", "windows 11"]
description: "Suspect your charger is the problem? Here's how to test a laptop adapter using Windows 11 tools, BIOS readings, and simple hardware checks."
thumbnail: "/images/thumbs/how-to-test-laptop-charger-in-windows-11-24h2.webp"
faqs:
  - q: "How can I test if my laptop charger is working?"
    a: "Start simple: check the charger's LED, try a different outlet, and watch whether Windows shows 'plugged in'. Then check BIOS for the detected adapter wattage, generate a battery report to see if charge accumulates, and inspect the cable for damage. Testing with a known-good charger is the definitive test."
  - q: "Can Windows 11 tell me my charger's wattage?"
    a: "Windows itself doesn't show adapter wattage, but your BIOS usually does — check Battery Information or Power status in BIOS setup. Some manufacturer apps (Dell Power Manager, Lenovo Vantage) also display the detected adapter wattage. If BIOS shows 'unknown adapter', the charger's ID chip or cable is likely damaged."
  - q: "Why does my laptop run on the charger but not charge the battery?"
    a: "The adapter is delivering some power but not enough — either it's underpowered for your laptop (wrong wattage), the cable is damaged and dropping voltage, or the laptop's charging circuit limits intake. A 45W charger on a 65W+ laptop often runs the machine but can't charge the battery simultaneously."
  - q: "Is it safe to use a higher-wattage charger?"
    a: "Yes — wattage is a maximum, not a forced output. The laptop only draws what it needs, so a 90W charger on a 65W laptop is perfectly safe. What's not safe is a lower-wattage charger (underpowered, causes the symptoms above) or a cheap no-name adapter with poor voltage regulation."
---
# How to Test a Laptop Charger in Windows 11 (Proven Methods)

When charging problems appear, everyone blames the battery — but the charger is the culprit more often than people expect. Cables fray internally, bricks overheat and degrade, and USB-C adapters quietly drop below their rated wattage. Testing the charger properly takes about 15 minutes and can save you from buying a battery you don't need.

This guide gives you every practical test, from the 30-second checks to BIOS wattage readings to the definitive swap test. No multimeter required (though I'll mention it for the thorough).

## Why this happens

- **Internal cable breaks.** The most common failure — wires fracture inside intact-looking insulation, usually near the plug or brick.
- **Degraded brick.** Capacitors age; an old adapter can output noisy or sagging voltage under load.
- **Wrong wattage.** A replacement or borrowed charger with too few watts runs the laptop but can't charge it.
- **Damaged ID chip/wire.** Dell and others identify adapters via a data pin — damage it and the laptop refuses the charger.
- **USB-C PD negotiation failure.** A damaged cable or port can fail the power-delivery handshake, dropping to 5V trickle.
- **Overheating brick.** A failing adapter overheats, its thermal protection throttles output, and charging stalls.
- **Outlet/power strip issues.** Sometimes the "charger problem" is the dead outlet it's plugged into.

## How to fix it

Work through these in order, from quickest to deepest. Most people find the answer by Fix 4.

### Fix 1: The 60-Second Basic Test

Rule out the obvious before anything else.

1. Plug the charger into a wall outlet directly — no power strip, no extension cord.
2. Check the LED on the brick (if it has one) — lit means it's receiving mains power.
3. Connect to the laptop and watch the taskbar battery icon — it should change to the charging indicator within seconds.
4. Hover over the battery icon — Windows should say "plugged in" and show a percentage climbing.
5. Unplug and replug firmly — a loose connection mimics a dead charger.

### Fix 2: Check Adapter Detection in BIOS

The BIOS reads the adapter independently of Windows — this is the most reliable software-side test.

1. Shut down, then power on pressing **F2** (Dell), **F1** (Lenovo), **F10** (HP), or **Del** (others) to enter BIOS setup.
2. Navigate to **Battery Information**, **Power**, or **System Information**.
3. Look for **AC Adapter Type** or **Adapter Wattage** — it should match your charger's rating (e.g., 65W).
4. If it says **Unknown** or shows nothing, the adapter's ID signal isn't reaching the laptop — cable or brick fault.
5. On Dell, an unknown adapter usually triggers a warning at boot — note the exact message.

### Fix 3: Verify Charging With a Battery Report

Confirm the charger is actually putting energy into the battery, not just lighting the icon.

1. Plug in and charge for at least 30 minutes of normal use.
2. Open admin **Command Prompt** and run `powercfg /batteryreport`.
3. Open the report and check **Recent usage** — the charge percentage should climb during plugged-in periods.
4. If the percentage is flat or falling while plugged in, the charger isn't delivering net positive power.
5. Compare: repeat the test with the laptop asleep — if it charges while asleep but not while awake, the adapter is underpowered for your workload.

For help reading the report, see [how to generate a battery report with powercfg](/articles/how-to-generate-battery-report-windows-11-powercfg/).

### Fix 4: Inspect the Cable and Connectors

Physical inspection catches the most common real failures.

1. Run fingers along the full cable length, feeling for flat spots, kinks, or soft sections where internal wires broke.
2. Flex the cable gently near the plug and near the brick while watching the charging icon — flickering means an internal break.
3. Check the plug: USB-C should be straight and clean; barrel plugs should have an undamaged center pin.
4. Smell the brick — burnt plastic odor means internal component failure. Stop using it.
5. Feel the brick during charging — warm is normal, too-hot-to-touch is not.

### Fix 5: The Swap Test (Definitive)

Nothing beats testing with known-good hardware. This is the test repair shops run.

1. Borrow a compatible charger — same connector, equal or higher wattage, ideally the manufacturer's.
2. Test it on your laptop: if charging works normally, your charger is faulty.
3. Alternatively, test your charger on another compatible laptop: if it fails there too, confirmed.
4. For USB-C: try a different quality USB-C PD cable with your brick — cables fail more often than bricks.
5. Try your brick with a different cable — this isolates brick vs. cable.

### Fix 6: Check USB-C Power Delivery Details

USB-C charging has extra failure modes worth checking specifically.

1. Try every USB-C port on the laptop — only some support charging on many models.
2. Clean lint from the port with a wooden toothpick and flashlight.
3. Check the cable's rating — it must support USB-C PD at your laptop's wattage (look for printed specs or use the original cable).
4. Avoid USB-C hubs and docks for testing — connect the charger directly.
5. If the laptop charges slowly via USB-C but the barrel charger works fine, the PD negotiation is the issue — cable or port.

### Fix 7: Monitor Under Load

Some chargers work at idle but collapse under load — test accordingly.

1. Plug in, then run something demanding (a game, a 4K YouTube video, a benchmark).
2. Watch the battery percentage: if it drops while plugged in under load, the charger can't keep up.
3. Check whether the brick gets excessively hot during this test.
4. An adapter that can't sustain its rated wattage under load is failing — replace it.
5. Note: a few high-performance laptops intentionally drain slightly under extreme load even with the correct charger (hybrid power) — check your manual.

### Fix 8: Replace the Charger Correctly

If testing condemns the charger, replace it without creating new problems.

1. Match the original wattage or go higher — never lower.
2. Match the connector type exactly (barrel size matters: 7.4mm vs 4.5mm Dell plugs are not interchangeable).
3. Buy manufacturer-original or a reputable brand (Anker, Belkin for USB-C) — avoid unbranded marketplace bricks.
4. For Dell/Lenovo/HP barrel chargers, genuine adapters include the ID chip your laptop expects.
5. After replacing, verify in BIOS that the new adapter is detected at the correct wattage.

## Closing

Charger testing is really about isolation: outlet, cable, brick, port — test each link and the weak one reveals itself. The BIOS wattage reading plus the swap test together give you near-certainty, no special tools needed. And remember the lesson most people learn the hard way: when charging acts up, suspect the $30 charger before the $100 battery. It's the cheaper fix and the more common fault.

## Verify your results

With a good charger, the battery percentage should climb steadily during normal use, and BIOS should report the correct adapter wattage. If a confirmed-good charger still doesn't charge the battery, the problem is downstream — start with [reinstalling the battery driver](/articles/how-to-fix-laptop-battery-not-charging-reddit/) or check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for power troubleshooting.
