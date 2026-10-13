---
title: "Laptop Charger Not Detected? Here’s the Fix"
slug: how-to-fix-laptop-charger-not-detected-youtube
date: 2026-09-10
categories: ["battery"]
tags: ["charger not detected", "laptop not recognizing charger", "ac adapter not detected"]
description: "Windows says no charger is connected even though it's plugged in? Diagnose the adapter, port, and drivers with these proven fixes."
thumbnail: "/images/thumbs/how-to-fix-laptop-charger-not-detected-youtube.webp"
faqs:
  - q: "Why does my laptop say no charger is detected when it's plugged in?"
    a: "The laptop isn't sensing the adapter's identification signal. Common causes: a failing charger brick, a damaged DC jack or USB-C port, the wrong wattage adapter, or a driver issue. The laptop may still receive power without 'detecting' the charger on some models."
  - q: "Can I use a lower-wattage charger temporarily?"
    a: "Sometimes, but many laptops — especially Dell and HP — refuse to charge or throttle heavily if the adapter wattage doesn't match. A 45W charger on a 90W laptop may power it but not charge the battery. Match the original wattage for reliable charging."
  - q: "The charger LED is on but the laptop doesn't detect it. Why?"
    a: "The LED only proves the brick gets wall power. The output cable, the connector tip, or the adapter's ID chip can all fail independently. Try a known-good charger to isolate whether the problem is the adapter or the laptop."
  - q: "Does 'charger not detected' mean my battery is dead?"
    a: "No — detection is about the adapter, not the battery. The battery can be perfectly healthy while the laptop refuses to acknowledge the charger. Fix the detection issue first; the battery will charge normally once the adapter is recognized."
---
"Plugged in" — but Windows insists no charger is connected. Or worse, the laptop doesn't react at all when you plug in. This is a detection problem: somewhere between the wall outlet and the motherboard, the adapter's presence signal is getting lost. The fix depends on where it's lost, so this guide helps you isolate the break step by step.

We'll start with the physical chain (outlet, brick, cable, port) because that's where most detection failures live, then move to drivers and firmware.

## Why this happens

- **Failing charger brick:** The adapter's output stage or its identification chip dies while the LED still lights — the classic misleading failure.
- **Damaged DC jack or USB-C port:** Loose, bent, or debris-filled ports break the detection pins even when power pins still make contact.
- **Wrong-wattage adapter:** Many laptops query the adapter's wattage and reject chargers that don't match, showing "not detected" or "unknown adapter."
- **Broken cable near the strain relief:** Internal wire fractures cause intermittent detection that comes and goes when you wiggle the cable.
- **Driver or EC glitch:** The embedded controller or ACPI driver can stop reporting adapter status after updates or power events.

## How to fix it

Work through these in order — each step isolates a different link in the chain.

### Fix 1: Verify the outlet and the charger LED

Start at the wall and work inward.

1. Plug the charger into a different wall outlet — not a power strip, directly into the wall.
2. Check the brick's LED. No light means no wall power or a dead brick.
3. If the LED lights, wiggle the cable gently near both ends while watching the LED. Flickering indicates a fractured cable.
4. Smell the brick — a burnt-plastic odor means it's done, unplug it.

A flickering LED with cable movement is a definitive cable failure. Stop using that charger; intermittent shorts can damage the laptop's charging circuit. For slow-charging USB-C variants of this problem, see [what to do if your USB-C PD charger charges slowly](/articles/what-to-do-if-usb-c-pd-charger-charging-slowly/).

### Fix 2: Inspect and clean the charging port

Detection pins are small and easily fouled.

1. Power off the laptop and unplug everything.
2. Shine a flashlight into the charging port. Look for lint, bent pins (barrel jacks), or debris (USB-C).
3. Clean gently with compressed air or a dry wooden toothpick — never metal tools, and never while powered.
4. For barrel jacks, check that the center pin isn't bent or pushed in.
5. Plug in firmly and check detection.

On USB-C laptops, try a different USB-C port if the machine has more than one — only some ports support charging on certain models, and the manual will tell you which.

### Fix 3: Confirm the adapter wattage matches

An underpowered adapter is "detected" as inadequate on many laptops.

1. Read the output wattage printed on your charger brick (e.g., 65W, 90W, 130W).
2. Check your laptop's required wattage in its manual or on the manufacturer's support page.
3. If you're using a third-party or borrowed charger with lower wattage, that's likely the rejection cause.
4. Dell laptops famously show "unknown adapter" warnings in BIOS with non-Dell chargers — enter BIOS to see the adapter status directly. For Dell-specific charging quirks beyond detection, see [what to do if your Dell laptop battery is not charging](/articles/what-to-do-if-dell-laptop-battery-not-charging/).

Match the original wattage. Bigger is generally fine (the laptop draws what it needs); smaller is where detection problems start. Genuine adapters from your laptop manufacturer's support site avoid the ID-chip issues cheap knockoffs cause.

### Fix 4: Test with a known-good charger

This single test splits the problem in half.

1. Borrow a charger with matching wattage and connector from the same brand.
2. If the laptop detects the borrowed charger, your adapter is dead — replace it.
3. If it still shows not detected, the fault is in the laptop: port, EC, or drivers. Continue below.

Don't skip this. Everything after this point assumes the charger is good, and guessing wrong wastes hours.

### Fix 5: Reset the ACPI drivers and EC

Clear any software-side detection failure.

1. Press **Win + X**, open **Device Manager**, and expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter** (right-click > **Uninstall device**).
3. Shut down fully, unplug the charger, and hold the power button for 30 seconds.
4. Plug in and power on; Windows rebuilds both drivers at boot.
5. Check **Settings** > **System** > **Power & battery** for the charging status.

The 30-second hold with no power drains the EC's capacitors and forces a cold reset of the charging logic. Microsoft covers adapter troubleshooting basics on their [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 6: Update the BIOS

The EC firmware handles adapter detection at the hardware level.

1. Check your BIOS version with `msinfo32`.
2. Download the latest BIOS from your manufacturer's support page and flash it with a known-good charger connected.
3. After rebooting, check whether the original charger is now detected.

BIOS updates often include EC fixes for adapter detection, especially for "unknown adapter" warnings. If you can't keep the laptop powered during the flash because no charger is detected, use a borrowed charger for the update process.

### Fix 7: Evaluate the DC jack for repair

If a good charger, clean port, fresh drivers, and new BIOS still show nothing, the jack itself is likely broken.

1. With the charger plugged in, gently wiggle the connector — if detection flickers, the jack's solder joints are cracked.
2. Check whether the jack feels loose compared to when the laptop was new.
3. DC jack replacement is a board-level repair: on some models it's a cheap cable, on others it's soldered to the motherboard.

Get a quote from a reputable shop before deciding. On an older laptop, the repair cost may exceed the machine's value — in which case a USB-C PD charger (if the model supports it) can be a workaround that avoids the broken barrel jack entirely.

## Closing

"Charger not detected" is a chain-of-custody problem: wall, brick, cable, port, firmware. Test each link in order and the break reveals itself — usually a dead brick or a dirty port, occasionally a driver or EC glitch, rarely a broken jack. The known-good charger test is the hinge everything turns on, so borrow one early and save yourself the guesswork.
