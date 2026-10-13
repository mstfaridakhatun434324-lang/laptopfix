---
title: "How Do I Fix a Laptop Charger That's Not Detected?"
slug: how-do-i-fix-laptop-charger-not-detected
date: 2026-09-22
categories: ["battery"]
tags: ["charger not detected", "ac adapter", "usb-c charging"]
description: "Plugged in the charger and Windows doesn't even notice? Here's how to fix a charger that isn't detected, from the outlet to the driver."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-charger-not-detected.webp"
faqs:
  - q: "What does 'charger not detected' mean?"
    a: "Windows shows no charging indicator at all — no plug icon, no 'plugged in' status. Power may or may not be flowing; the key point is the system doesn't acknowledge the adapter, which points to connection, adapter, port, or driver issues."
  - q: "Can a laptop charge if the charger isn't detected?"
    a: "Sometimes, slowly. Some laptops accept power without completing the identification handshake, charging at reduced rates. But an undetected charger usually means no charging or unreliable charging — fix the detection."
  - q: "Why does my USB-C charger work on my phone but not my laptop?"
    a: "Phones need 15–25W; laptops need 45–100W+. A phone charger can't negotiate the higher power contract the laptop requires, so the laptop ignores it. You need a USB-C PD charger rated at or above your laptop's wattage."
  - q: "Is it safe to use a higher-wattage charger?"
    a: "Yes. The laptop only draws what it needs — a 100W adapter on a 65W laptop is perfectly safe. What's unsafe is a lower-wattage adapter that overheats trying to keep up, or a cheap no-name adapter with poor circuitry."
---
You plug in the charger and... nothing. No plug icon in the taskbar, no "plugged in" message, no charging light. Windows is acting like you plugged in a particularly useless USB stick. Meanwhile your battery percentage keeps sliding toward zero.

"Charger not detected" is different from "plugged in, not charging" — in that case Windows at least sees the adapter. Here, the adapter is invisible to the system entirely. That narrows the suspects nicely: the connection, the adapter itself, the port, or the driver that reports adapters to Windows. Let's check them in order.

## Why this happens

- **The adapter isn't delivering identifiable power.** A dead brick, broken cable, or damaged connector means no power and no identification signal — Windows sees nothing because there's nothing to see.
- **The wattage handshake fails.** Modern laptops (USB-C PD especially, plus Dell's barrel-connector ID chip) require the adapter to identify itself. An underpowered or non-compliant adapter gets ignored.
- **The port is damaged or obstructed.** Bent pins, a wobbly DC jack, or lint packed into a USB-C port breaks the connection before any detection can happen.
- **The AC adapter driver is missing or broken.** Windows learns about adapters through the **Microsoft AC Adapter** driver. If it's corrupted or missing, a perfectly good charger goes unreported.
- **The embedded controller is stuck.** The EC handles the physical detection; a latched error state can make it blind to a charger that's actually connected.
- **BIOS/firmware issues.** Outdated or buggy firmware can break adapter identification — Dell's adapter-ID warnings are the famous example, but all brands can suffer detection bugs.

## How to fix it

Work through these in order, from outside the laptop inward.

### Fix 1: Confirm the basics — outlet, cable, seating

Don't skip this. A huge share of "not detected" cases end here.

1. Plug the adapter into a wall outlet you know works (test with another device). Skip power strips for this test.
2. Check the brick's indicator light if it has one. No light on a good outlet = dead adapter, full stop.
3. Inspect the entire cable for kinks and fraying, especially at the strain-relief points near the brick and the connector.
4. Push the connector firmly into the laptop — USB-C should click and sit flush; barrel connectors shouldn't wobble. For USB-C, flip the connector and try the other orientation, and try a different USB-C port if your laptop has more than one.

### Fix 2: Verify the wattage is sufficient

An ignored charger is often just an inadequate one.

1. Read the wattage on your original adapter's label (e.g., 65W, 90W, 130W).
2. Compare with what you're using. A 45W adapter on a 65W laptop, or a phone charger on any laptop, will typically not be detected as a valid charger.
3. For USB-C: the charger must support **USB Power Delivery (PD)** at your laptop's required wattage. A "USB-C charger" without PD is just a phone charger with ambition.
4. Rule of thumb: match or exceed the original wattage. Higher is safe; lower causes exactly this problem. If you're borrowing a charger to test, make sure it's up to spec or the test proves nothing.

### Fix 3: Clean and inspect the charging port

The handshake can't happen through lint.

1. Power off and unplug everything. Shine a flashlight into the port.
2. For USB-C: gently pick out lint and debris with a wooden toothpick or plastic dental pick. Work carefully around the center tongue — it's fragile. Never use metal tools.
3. For barrel jacks: check the center pin isn't bent and the jack doesn't wobble in the chassis. A loose DC jack needs professional resoldering — note it and move on.
4. Blow out remaining dust with compressed air, reconnect firmly, and check whether Windows now detects the charger.

### Fix 4: Test with a known-good adapter

The definitive adapter test.

1. Borrow an adapter with the correct connector and equal-or-higher wattage (for USB-C PD, any reputable PD charger at sufficient wattage).
2. If Windows detects the borrowed adapter immediately, yours is dead or non-compliant — replace it with the correct spec.
3. If the borrowed adapter is also not detected, the fault is in the laptop: port, controller, or drivers. Continue.
4. Dell users: if you see an "AC adapter not recognized" warning at boot with a third-party adapter, that's Dell's ID chip check — only a genuine Dell adapter (or one with the ID chip) clears it.

### Fix 5: Reinstall the AC adapter driver

Windows can't report what its driver can't see.

1. Open **Device Manager** (**Windows key + X > Device Manager**) and expand **Batteries**.
2. Right-click **Microsoft AC Adapter** → **Uninstall device**. Also uninstall **Microsoft ACPI-Compliant Control Method Battery** while you're here.
3. Shut down fully (not restart), unplug the charger for 30 seconds, reconnect it, and power on.
4. Windows reinstalls both drivers during boot. Check the taskbar: the plug icon should appear if the driver was the problem.

### Fix 6: Reset the embedded controller

The EC does the physical detecting — reset it when it's blind.

1. Shut down, unplug the charger and all peripherals. Remove the battery if it's removable.
2. Hold the power button for 20–30 seconds.
3. Reconnect the charger first, wait 30 seconds, then power on. Watch for the charging LED before Windows loads — a light at this stage means the hardware sees the adapter even if Windows doesn't (driver issue); no light means hardware-level blindness.
4. If the LED lights pre-boot but Windows still shows nothing, repeat Fix 5 — and check **Device Manager** for any devices with warning icons that might indicate a deeper driver problem.

### Fix 7: Update BIOS and check the port hardware

Last stops: firmware, then physical repair.

1. Check your BIOS version (`msinfo32`) and update from the manufacturer's support page if newer firmware exists — [Dell](https://www.dell.com/support), [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en/). Adapter-detection fixes appear in BIOS changelogs regularly.
2. After updating, test detection again with the known-good adapter.
3. If a specific port is dead but others work (USB-C laptops with multiple ports), just use the working port — port failure on one of several is common and not worth a motherboard repair on its own. For USB-C-specific charging faults, see [USB-C charging not working](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/).
4. If no adapter is detected on any port and drivers/firmware are current, you're looking at a failed charging circuit or DC jack — a repair-shop job. Don't keep forcing a wobbly jack; intermittent connections can arc and damage the motherboard. If the battery still holds some charge, our guide to [stretching battery life](/articles/laptop-battery-drains-fast-windows-11/) can buy you time until the repair.

## Closing

A charger Windows can't see is a chain-of-custody problem: outlet, cable, wattage, port, driver, controller. Check them in that order and the break reveals itself — usually at the cable or the wattage, occasionally at the driver, rarely at the motherboard. And remember the golden rule of chargers: match or exceed the original wattage, because an underpowered adapter doesn't just charge slowly — sometimes it doesn't get detected at all.
