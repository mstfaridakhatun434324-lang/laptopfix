---
title: "Laptop Charger Not Detected? How to Get It Recognized Again"
slug: how-to-fix-laptop-charger-not-detected-reddit
date: 2026-10-04
categories: ["battery"]
tags: ["charger not detected", "adapter", "reddit"]
description: "Windows doesn't see your charger at all? From the power-drain reset to port cleaning, here are the fixes that get adapters recognized again."
thumbnail: "/images/thumbs/how-to-fix-laptop-charger-not-detected-reddit.webp"
faqs:
  - q: "Why does my laptop not detect the charger when it's plugged in?"
    a: "The most common reasons: a driver glitch (fixable by reinstalling the Microsoft AC Adapter driver), debris in the charging port, a damaged cable, or the embedded controller being stuck. On Dell laptops, an unrecognized adapter triggers a specific BIOS warning — the charger works but the laptop refuses to charge from it as a safety measure."
  - q: "How do I know if the problem is the charger or the laptop?"
    a: "Test the charger on another compatible laptop, or test a known-good charger on yours — whichever flips the result identifies the culprit. Also try a different wall outlet. If no charger is ever detected on your laptop but yours works elsewhere, the laptop's charging port or circuit is the problem."
  - q: "Can a Windows update cause the charger to stop being detected?"
    a: "Yes. Updates can corrupt the Microsoft AC Adapter driver or change power management settings. If detection failed right after an update, uninstall both the AC Adapter and ACPI battery drivers in Device Manager, shut down fully, and reboot — Windows rebuilds them cleanly."
  - q: "My charger is detected but the battery won't charge. Is that different?"
    a: "Yes — that's a charging problem, not a detection problem, and it has different causes (charge limits, worn battery, calibration). Detection failure means Windows doesn't see the adapter at all: no charging icon change, no 'plugged in' status. Fix detection first; charging issues get their own troubleshooting."
---
# Laptop Charger Not Detected? How to Get It Recognized Again

There's a special frustration in plugging in your charger and having the laptop act like nothing happened — no icon change, no "plugged in" message, battery still draining. This is a detection problem, which is different from a charging problem, and it has its own set of fixes.

The good news: total detection failure is very often software (a stuck controller or corrupted driver) or something physical you can see (lint in the port, a damaged cable). Work through these in order and you'll find which one you have.

## Why this happens

- **Stuck embedded controller.** The chip managing power delivery gets confused and stops recognizing the adapter until reset.
- **Corrupted AC adapter driver.** The Microsoft AC Adapter driver in Device Manager can break, especially after Windows updates.
- **Debris in the charging port.** Lint and dust in USB-C ports physically prevent the connection pins from contacting.
- **Damaged cable or connector.** A frayed cable or bent barrel plug breaks the data pin that identifies the adapter (Dell is notorious for this).
- **Dead wall outlet or power strip.** The outlet itself has no power — embarrassingly common and worth ruling out first.
- **Failing charging port.** Loose or worn solder joints on the DC jack cause intermittent or total detection failure.
- **BIOS not recognizing the adapter.** Dell laptops explicitly warn about unknown adapters and may refuse to charge from them.

## How to fix it

Work through these in order, from quickest to deepest. Most people find the answer by Fix 3.

### Fix 1: Rule Out the Outlet and Basics

Start embarrassingly simple — this fixes more cases than anyone admits.

1. Plug the charger into a different wall outlet, directly (no power strip, no extension).
2. Check the charger's LED indicator if it has one — no light means no power reaching the brick.
3. Try a different device in the same outlet to confirm the outlet is live.
4. Unplug the charger from both the wall and the laptop, wait 60 seconds, then reconnect firmly.
5. Listen and feel: a faint click or snug fit means proper seating; a loose wobbly plug is a red flag.

### Fix 2: The Full Power Drain Reset

This resets the embedded controller that handles adapter detection — the most upvoted hardware fix for this exact symptom.

1. Shut down the laptop completely.
2. Unplug the charger from the laptop and the wall.
3. If the battery is removable, remove it.
4. Hold the power button down for a full **30 seconds**.
5. Reconnect everything (battery in, charger to wall first, then laptop).
6. Power on and check whether the charger is now detected.

### Fix 3: Reinstall the AC Adapter Driver

If Windows' driver for the adapter is corrupted, it can't see the charger no matter how good the hardware is.

1. Right-click **Start** and open **Device Manager**.
2. Expand **Batteries**.
3. Right-click **Microsoft AC Adapter** and choose **Uninstall device**.
4. Right-click **Microsoft ACPI-Compliant Control Method Battery** and uninstall it too.
5. Shut down fully (hold **Shift** while clicking **Shut down** to force a full shutdown).
6. Plug in the charger, then power on — Windows reinstalls both drivers during boot.

### Fix 4: Clean the Charging Port

For USB-C laptops especially, pocket lint compacts into the port and blocks the pins. This is extremely common and invisible until you look.

1. Power off the laptop and unplug everything.
2. Shine a flashlight into the USB-C or barrel port.
3. For USB-C: gently scrape out lint with a wooden or plastic toothpick — never metal.
4. For barrel jacks: check the center pin isn't bent and blow out dust with compressed air.
5. Reconnect the charger firmly and check for detection.

### Fix 5: Inspect the Cable and Brick

Adapter cables fail from the inside — they look fine but a broken wire kills detection, particularly the ID pin Dell uses.

1. Run your fingers along the entire cable feeling for kinks, flat spots, or fraying.
2. Check where the cable meets the brick and the plug — these stress points fail first.
3. Smell the brick: a burnt-plastic smell means internal failure — stop using it.
4. If the brick is unusually hot when plugged in with no laptop attached, it's failing.
5. Test with a different compatible charger if possible — this instantly separates charger faults from laptop faults.

For a methodical approach, [how to test a laptop charger in Windows 11](/articles/how-to-test-laptop-charger-in-windows-11-24h2/) walks through verifying actual power delivery.

### Fix 6: Check BIOS Adapter Detection

The BIOS sees the adapter independently of Windows — this tells you whether it's hardware or software.

1. Restart and enter BIOS (**F2** Dell, **F1** Lenovo, **F10** HP, **Del** others).
2. Look for **Battery Information**, **Power**, or **Adapter** status.
3. If BIOS shows the adapter type and wattage correctly but Windows doesn't, it's a Windows driver problem — revisit Fix 3.
4. If BIOS also shows "unknown" or nothing, it's hardware: charger, port, or motherboard.
5. On Dell, note the exact warning message — "adapter type cannot be determined" points squarely at the charger's ID chip or cable.

### Fix 7: Update BIOS and Chipset Drivers

Firmware updates fix adapter-detection bugs, and chipset drivers handle the power-delivery communication.

1. Go to your manufacturer's support site ([Dell](https://www.dell.com/support), [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en)) and enter your model.
2. Download the latest **BIOS** and **chipset** drivers.
3. Install the chipset driver first, then the BIOS update.
4. Keep the charger plugged in during the BIOS update (use a working charger or borrow one).
5. Reboot and check adapter detection in both BIOS and Windows.

### Fix 8: Assess for Hardware Repair

If nothing above works, the fault is physical — usually the DC jack or the charging circuit.

1. Wiggle the plug gently while watching the charging icon — intermittent detection means a loose jack.
2. If the jack feels loose or the plug falls out easily, the DC jack needs resoldering or replacement.
3. Check warranty status — charging-port failure is typically covered.
4. For out-of-warranty laptops, a repair shop usually fixes DC jacks for $75–$150.
5. Don't attempt motherboard-level repair yourself unless you have soldering experience — it's easy to make worse.

## Closing

"Charger not detected" feels like a dead laptop, but it's most often a stuck controller (fixed by the power drain), a corrupted driver (fixed in Device Manager), or lint in the port (fixed with a toothpick). The BIOS check is your dividing line: if BIOS sees the adapter, Windows can be fixed; if BIOS doesn't, it's hardware. Either way, you now know exactly which side of that line you're on — and that's most of the battle.

## Verify your results

Once detected, confirm the charger actually charges: watch the battery percentage climb over 15–20 minutes, and check that the adapter wattage in BIOS matches your charger's rating. If detection works but charging doesn't, the next step is [troubleshooting a Dell battery that won't charge](/articles/troubleshoot-dell-laptop-battery-not-charging/) or the equivalent guide for your brand.
