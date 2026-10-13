---
title: "Laptop Charger Not Detected on Windows 11: Step-by-Step Fix"
slug: how-to-fix-laptop-charger-not-detected-on-windows-11
date: 2026-09-13
categories: ["battery"]
tags: ["charger not detected", "windows 11", "usb-c pd", "not charging"]
description: "Windows 11 doesn't recognize your charger? Work through these checks — from USB-C PD quirks to driver resets — to get charging detected again."
thumbnail: "/images/thumbs/how-to-fix-laptop-charger-not-detected-on-windows-11.webp"
faqs:
  - q: "Why won't Windows 11 detect my USB-C charger?"
    a: "USB-C charging requires the Power Delivery (PD) protocol and enough wattage. A phone charger or a USB-C cable without PD support won't be recognized as a valid charger. Use a proper USB-C PD charger rated at or above your laptop's requirement, with a PD-rated cable."
  - q: "My charger worked yesterday and stopped today. What changed?"
    a: "Cables and bricks fail suddenly — internal wire breaks often happen all at once. Windows updates can also corrupt the battery driver overnight. Test with a different charger first; if that works, your old charger died. If not, reinstall the battery drivers."
  - q: "Should I try a different USB-C port on my laptop?"
    a: "Yes — on many laptops only one or two USB-C ports support charging. Check your manual for which ports are marked with a charging or Thunderbolt symbol, and try each one. A port that handles data but not power won't charge the laptop."
  - q: "Can a Windows 11 update break charger detection?"
    a: "It can, usually by replacing the manufacturer's power driver with a generic one or corrupting the ACPI battery driver. Uninstalling the Microsoft ACPI-Compliant Control Method Battery driver in Device Manager and restarting forces a clean reinstall that usually fixes it."
---

Same charger, same laptop, worked fine yesterday — and today Windows 11 shows no charging indicator at all. No "plugged in" text, no LED change, nothing. On Windows 11 this complaint has a couple of modern twists (USB-C Power Delivery quirks, driver updates that arrive silently overnight), but the diagnostic path is straightforward.

We'll isolate the fault methodically: power source, charger, cable, port, then Windows itself.

## Why this happens

- **Dead outlet or power strip** — the simplest cause and worth ruling out first.
- **Failed cable or brick** — cables break internally without visible damage.
- **Wrong USB-C port** — only specific ports on many laptops accept charge.
- **Non-PD USB-C charger or cable** — the laptop requires USB-C Power Delivery negotiation.
- **Underpowered charger** — firmware rejects chargers below the minimum wattage.
- **Corrupted ACPI battery driver** — Windows ignores a working charger after a driver glitch.
- **Debris in the charging port** — lint in USB-C ports blocks proper contact.

## How to fix it

Work through these in order — don't skip the physical checks.

### Fix 1: Rule out the outlet

Plug the charger directly into a different wall outlet, bypassing any power strip, dock, or extension. Then verify the original outlet works by plugging in something else. Check whether the charger's LED (if it has one) lights up. This takes 60 seconds and eliminates the most embarrassing possibility.

### Fix 2: Try the right USB-C port with the right cable

USB-C charging is pickier than barrel chargers:

1. Check your laptop's manual or the symbols beside the ports — use the port marked for charging/Thunderbolt, not a data-only port.
2. Try every USB-C port; on some machines only one supports PD input.
3. Use a cable rated for USB-C PD at your laptop's wattage — thin phone-charging cables often can't negotiate laptop-level power.
4. If you're using a dock or hub, plug the charger directly into the laptop instead to rule out the dock.

A surprising number of "charger not detected" cases on Windows 11 are just the wrong port or a phone-grade cable.

### Fix 3: Inspect and swap the charger

Look for fraying near the connectors, a brick that's ice-cold when plugged in (dead) or scorching hot (failing), and any burnt smell. Then test with a different charger that meets your laptop's wattage — borrow one if you can. If a known-good charger is detected immediately, yours has failed; replace it with one matching the original voltage exactly and wattage equal or higher. For more on choosing a replacement, see our Windows 10 [charger detection guide](/articles/how-to-fix-laptop-charger-not-detected-on-windows-10/), which covers wattage matching in detail.

### Fix 4: Clean the charging port

Power off the laptop and unplug everything. Shine a light into the port — USB-C ports collect lint remarkably fast. Gently tease debris out with a wooden toothpick (never metal) and use short bursts of compressed air with the can held upright. A port packed with lint can prevent the pins from seating, which the laptop reads as "no charger."

### Fix 5: Reset the embedded controller

The EC manages charging negotiation and can get stuck:

1. Shut down fully (hold **Shift** while clicking **Shut down** to bypass fast startup).
2. Unplug the charger and all peripherals.
3. Hold the power button for **30–60 seconds**.
4. Reconnect the charger and power on.

Test detection immediately after boot, before opening any apps.

### Fix 6: Reinstall the battery drivers in Device Manager

If hardware checks pass, this is the key Windows-side fix:

1. Press **Win + X**, open **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**.
3. Right-click **Microsoft AC Adapter** > **Uninstall device**.
4. Restart the laptop with the charger plugged in.

Windows rebuilds both drivers during startup. After logging in, wait a minute and check the system tray battery icon for the charging indicator. If the icon shows "plugged in" but the percentage never rises, that's a different problem — the charger is detected but the battery isn't accepting charge, which points to battery wear or a charge-control issue rather than detection.

### Fix 7: Check Windows Update for driver updates

Go to **Settings > Windows Update** and install all updates, then check **Advanced options > Optional updates** for driver updates — Microsoft sometimes ships fixed ACPI or chipset drivers as optional updates. Also visit your manufacturer's support site for the latest chipset driver, since the chipset driver handles power management communication on modern laptops.

### Fix 8: Test in the BIOS

Restart and enter the BIOS/UEFI setup. Most BIOS screens show whether AC power is detected, independent of Windows. If the BIOS sees the charger but Windows doesn't, you've confirmed a Windows-side problem (drivers or OS). If the BIOS doesn't see it either, the issue is hardware — charger, port, or charging circuit — and no Windows tweak will fix it. Note the distinction: if Windows sees the charger but reports no battery at all, that's a [battery detection problem](/articles/laptop-battery-not-detected-windows-11/) rather than a charger problem, and it needs a different fix path.

If the BIOS test points to hardware and you've already tried a second charger, inspect the port with a flashlight for bent pins or debris you might have missed, and check whether the port feels loose when the plug is inserted. A wobbly port usually means damaged solder joints — a repair shop can often re-solder or replace the port for far less than a new laptop, so it's worth getting a quote before giving up on the machine.

## Closing

On Windows 11, undetected chargers are usually a USB-C port/cable mismatch or a dead brick — both quick to test. The driver reinstall handles the software side in a few minutes. And the BIOS test is your tiebreaker: it tells you definitively whether to keep troubleshooting Windows or start looking at hardware. Work the list in order and you'll rarely need to guess.

Going forward, treat your charger gently — don't wrap the cable tightly around the brick, avoid yanking it out by the cord, and keep the brick ventilated rather than buried under papers. Most charger deaths are really cable deaths from repeated stress at the connector ends, and a little care adds years to a charger's life.
