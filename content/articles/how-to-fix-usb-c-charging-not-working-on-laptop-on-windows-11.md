---
title: "Fix USB-C Charging Not Working on Windows 11 Laptops"
slug: how-to-fix-usb-c-charging-not-working-on-laptop-on-windows-11
date: 2026-10-11
categories: ["battery"]
tags: ["usb-c charging", "windows 11", "power delivery"]
description: "USB-C charger plugged in but nothing happens on Windows 11? Diagnose port, cable, and driver causes with this ordered fix sequence."
thumbnail: "/images/thumbs/how-to-fix-usb-c-charging-not-working-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why won't my laptop charge via USB-C even though the cable fits?"
    a: "Fitting isn't enough — the port must support USB-C Power Delivery input, the cable must carry the PD protocol, and the charger must offer a voltage profile the laptop accepts. Any broken link means zero charging. Also check for lint in the port and try the laptop's designated charging port, since not all USB-C ports accept power."
  - q: "How do I know which USB-C port charges my laptop?"
    a: "Check the symbols next to the ports: a plug or battery icon, or a Thunderbolt lightning bolt, usually marks the charging-capable port. Your manual or the manufacturer's spec page confirms it. When in doubt, try every USB-C port — the charging one typically triggers the charging LED immediately."
  - q: "Can a Windows 11 update break USB-C charging?"
    a: "Yes. Updates reinstall USB and battery drivers, and a bad driver handshake can break Power Delivery negotiation — the charger is fine, but the laptop never agrees on a voltage with it. Reinstalling the USB controller and battery drivers usually restores negotiation."
  - q: "Does USB-C charging work when the laptop is off?"
    a: "On most laptops, yes — charging is handled by firmware below the OS level. If USB-C charging fails both in Windows and while powered off, the problem is hardware (port, cable, or charger), not Windows. That's a useful isolation test."
---

You plug in the USB-C charger and... nothing. No charging light, no "plugged in" message, just the battery percentage sitting there mocking you. USB-C charging involves more moving parts than the old barrel plug — port, cable, charger, and a negotiation protocol all have to agree — so the diagnosis needs to be methodical.

The key isolation test first: try charging with the laptop **powered off**. If it charges while off but not in Windows, it's software. If it won't charge either way, it's hardware. This single test saves you from chasing driver fixes for a broken cable, or buying a new charger for a driver problem.

## Why this happens

- **Wrong port.** Many laptops have several USB-C ports but only one accepts charging input.
- **Non-PD cable.** A basic USB-C cable without Power Delivery support can't negotiate charging.
- **Charger lacking the right PD profile.** The brick must offer a voltage/current combo the laptop accepts.
- **Lint or damage in the port.** The most common physical cause — pocket lint compacts into USB-C ports and prevents full contact.
- **Driver failure after update.** Broken USB or battery drivers kill PD negotiation in Windows.
- **Dead USB-C controller.** The port's controller chip can fail, especially after power surges.
- **BIOS/EC issue.** Firmware controls charging below the OS; a glitch here blocks charging even with perfect hardware.

## How to fix it

Work through these in order.

### Fix 1: Try every USB-C port

1. With the charger plugged in, try each USB-C port on the laptop, waiting 10 seconds per port.
2. Watch for the charging LED — the correct port usually lights it immediately.
3. Note which port works and use it consistently. Check your manual afterward to confirm it's the designated charging port.
4. If no port responds, continue — but you've ruled out the most common user error.

### Fix 2: Test with the laptop powered off

1. Shut the laptop down completely.
2. Plug in the USB-C charger and watch for the charging LED.
3. **LED on while off** → hardware is fine; the problem is Windows drivers or settings. Skip to Fix 5.
4. **No LED while off** → hardware problem: cable, charger, or port. Continue with Fix 3.

### Fix 3: Clean the port and check the cable

1. Power off and unplug everything.
2. Shine a light into the USB-C port. Use a **wooden or plastic toothpick** to gently pick out compacted lint — never metal.
3. Inspect the cable ends for bent pins or damage.
4. Confirm the cable supports Power Delivery: look for **100W/5A/240W** markings or USB-IF certification. Swap in a known-good PD cable if you have one.
5. Reconnect firmly — USB-C should click in solidly with no wobble.

### Fix 4: Verify the charger

1. Read the brick's label for its PD output profiles (e.g., **20V⎓3.25A**).
2. Compare against your laptop's requirement (original charger spec or manual).
3. Test the charger on another USB-C device (phone, tablet) to confirm the brick itself works.
4. Test your laptop with a different PD charger of adequate wattage. If a different charger works, replace yours — chargers do die, often silently.

### Fix 5: Reinstall USB and battery drivers (Windows-side fix)

1. Open **Device Manager** (**Win + X**).
2. Expand **Universal Serial Bus controllers**: uninstall every **USB Root Hub**, **USB-C**, and host controller entry. They reinstall on reboot.
3. Expand **Batteries**: uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
4. Restart with the charger connected. Windows rebuilds the entire USB-C PD negotiation stack.
5. After booting, plug in the charger and check for the charging indicator.
6. If charging works now, the driver stack was the problem. To prevent recurrence, check Windows Update for pending driver updates and install your manufacturer's chipset package from their support site so Windows doesn't fall back to the generic drivers that caused this.

### Fix 6: Update BIOS, chipset, and USB drivers

1. Find your exact model via `msinfo32`.
2. Download the latest **BIOS**, **chipset**, and any **USB/Thunderbolt** drivers from your manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
3. Install chipset/USB drivers first, then the BIOS on AC power (use the barrel charger if you have one, since USB-C isn't working).
4. After the reboot, test USB-C charging again.

### Fix 7: Reset the EC

1. Shut down, unplug everything including the USB-C charger.
2. Hold the **power button for 20 seconds**, release.
3. Reconnect the USB-C charger first, then power on.
4. The embedded controller re-initializes the PD controller with this reset.

### Fix 8: Diagnose a dead port

1. Test the suspect port with other USB-C devices: does it still transfer data or drive a display? A port that does data but not charging has a PD-specific fault.
2. Try charging via the barrel-plug adapter if your laptop has one — if barrel charging works fine, the issue is isolated to the USB-C subsystem.
3. A physically loose port (cable wobbles, intermittent connection) needs professional repair — USB-C ports are soldered to the board.
4. If under warranty, contact the manufacturer with your test results; "charges via barrel but not USB-C, tested with two PD chargers" gets you past tier-one scripts fast.
5. If Windows also reports [no battery detected](/articles/laptop-battery-not-detected-windows-11/) alongside the USB-C failure, treat that as the primary problem — a battery the system can't see won't negotiate charging either, and that guide's driver fixes often resolve both symptoms together.

For the related but distinct problem of USB-C charging slowly rather than not at all, see our guide to [slow USB-C PD charging on Windows 11 24H2](/articles/how-to-fix-usb-c-pd-charger-charging-slowly-in-windows-11-24h2/).

## Closing

USB-C charging failures are a chain — port, cable, charger, negotiation — and the powered-off test tells you instantly whether you're debugging hardware or software. Clean the port, verify the cable is PD-rated, reinstall the USB stack, and most cases resolve without a repair shop. Keep a known-good PD cable in your bag once this is fixed; it's the fastest diagnostic tool you own for any future USB-C weirdness.
