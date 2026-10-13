---
title: "How to Fix USB-C Charging Not Working on a Laptop"
slug: how-do-i-fix-usb-c-charging-not-working-on-laptop
date: 2026-09-18
categories: ["battery"]
tags: ["USB-C charging", "power delivery", "troubleshooting"]
description: "USB-C charger plugged in but the laptop won't charge? Work through port, wattage, cable, and driver checks to get charging back."
thumbnail: "/images/thumbs/how-do-i-fix-usb-c-charging-not-working-on-laptop.webp"
faqs:
  - q: "Why won't my laptop charge with a USB-C charger?"
    a: "Usually the charger is underpowered, the cable cannot handle the wattage, or you are using a data-only USB-C port. Less often, the USB or battery drivers are corrupted, or the BIOS has USB-C charging disabled. Test with the original high-wattage charger and a rated cable first."
  - q: "How many watts does my laptop need from USB-C?"
    a: "Check the original charger's label or your laptop's spec sheet — most ultrabooks need 45 to 65 watts, while performance laptops need 90 to 100 watts or more. The USB-C charger must support USB Power Delivery at or above that number, and the cable must be rated for it too."
  - q: "Do I need a special cable for USB-C laptop charging?"
    a: "Yes. You need a cable rated for USB Power Delivery at your laptop's wattage — typically 60W or 100W — with an e-marker chip for higher wattages. Generic charging cables and old phone cables top out at low wattages and will not charge most laptops."
  - q: "Can a BIOS update fix USB-C charging?"
    a: "Often, yes. Manufacturers fix Power Delivery negotiation bugs in BIOS and embedded-controller updates. If charging worked before and stopped after no hardware change, check your maker's support site for a BIOS update that mentions USB-C, Type-C, or power delivery fixes."
---

You plug in the USB-C charger, the connector clicks in satisfyingly, and... nothing. No charging icon, no LED change, no percentage movement. USB-C charging is a negotiation between three parties — the laptop, the charger, and the cable — and when any one of them cannot hold up its end, the deal falls through silently. The good news: the negotiation leaves clues, and working through them systematically finds the weak link fast.

This guide is the hands-on companion to the general troubleshooting walkthrough. Start with the thirty-second physical checks, because hardware causes the vast majority of USB-C charging failures.

## Why this happens

- **Wrong port:** Only specific USB-C ports on many laptops accept charge; the rest are data-only.
- **Underpowered charger:** Phone chargers and weak adapters cannot meet a laptop's Power Delivery requirements.
- **Inadequate cable:** Cables without proper PD rating or a damaged e-marker chip fail the wattage handshake.
- **Dirty or worn port:** Lint, dust, or bent pins break the negotiation contacts.
- **Driver corruption:** USB host controller or battery driver faults block charging in software.
- **BIOS/EC issue:** Disabled Type-C charging in firmware, or a PD negotiation bug awaiting an update.

## How to fix it

Work through these in order — hardware first, software second, firmware last.

### Fix 1: Use the correct port and check the connection

Thirty seconds that solves a surprising number of cases.

1. Identify the charging-capable USB-C port by the **battery** or **plug** icon printed beside it.
2. Plug the charger firmly into that port — USB-C should seat with a solid click, not feel loose.
3. Flip the connector over and try again; one side's contacts may be worn or dirty.
4. Try every USB-C port on the machine, waiting 10 seconds each, in case the icon is misleading.
5. If one port works and others do not, you have your answer — use the working port and treat the others as data-only.

### Fix 2: Match the wattage properly

Power Delivery only works when the charger can actually deliver.

1. Read your laptop's required wattage from the original charger label or the spec sheet.
2. Read your USB-C charger's label and confirm it lists **USB-PD** output at or above that wattage — not just a total that includes lower-voltage modes.
3. Remember that docks and monitors with USB-C often supply only 15 to 65W, which may be too little for your machine.
4. Test with a charger you know meets the requirement — a borrowed laptop brick is ideal for this.
5. If a proper-wattage charger works, your old charger was the problem all along. Our guide on [underpowered chargers](/articles/best-way-to-fix-65w-charger-not-enough-for-gaming-laptop/) explains the wattage math.

### Fix 3: Replace the cable with a rated one

The cable is guilty more often than people expect.

1. Swap in a cable explicitly labeled for **60W or 100W USB Power Delivery**.
2. Prefer shorter cables from reputable brands — long, thin, no-name cables are the worst offenders.
3. Check the old cable for kinks, fraying, or a loose connector housing.
4. Test the new cable flipped both ways and in the confirmed charging port.
5. Keep the known-good cable as your dedicated charging cable so the problem does not recur.

### Fix 4: Clean the USB-C port

A speck of lint can defeat a 100-watt handshake.

1. Power off the laptop and unplug everything.
2. Inspect the port with a flashlight for lint, dust, or visibly bent pins.
3. Remove debris gently with a wooden toothpick — never anything metal.
4. Use short bursts of compressed air, holding the can upright to avoid moisture.
5. Reconnect and test. If the plug wobbles loosely in the port, the port itself may be worn and need professional replacement.

### Fix 5: Reinstall USB and battery drivers

Software-side blocks are the next layer down.

1. Press **Win + X** and open **Device Manager**.
2. Under **Universal Serial Bus controllers**, uninstall each **USB Root Hub** and host controller (right-click → **Uninstall device**).
3. Under **Batteries**, uninstall **Microsoft ACPI-Compliant Control Method Battery**.
4. Restart — Windows reinstalls everything automatically.
5. After the desktop loads, plug in the USB-C charger and watch for the charging indicator. For the Windows 11-specific version of this process, see [USB-C charging fixes for Windows 11](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/).

### Fix 6: Do a full power reset

This clears stuck state in the charge controller.

1. Shut down completely and unplug the charger and all peripherals.
2. Hold the power button for **30 seconds** to drain residual power.
3. Wait two full minutes — rushing this step is the most common reason resets "do not work."
4. Plug the charger into the confirmed charging port, then power on.
5. Check the battery icon within a few minutes of reaching the desktop.

### Fix 7: Update firmware and verify with the maker

When hardware and drivers check out, suspect firmware.

1. Visit your manufacturer's support site — [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/) — and install the latest **BIOS** for your exact model.
2. Enter the BIOS setup and confirm any **USB-C charging**, **Type-C power**, or **Power Delivery** option is **enabled**.
3. Check the support site for a dedicated **USB-C or Thunderbolt firmware update**, which some brands ship separately from the BIOS.
4. After updating, retest with your known-good charger and cable.
5. If charging still fails on every port with verified-good gear, the port or charging circuit likely needs a repair shop — you have eliminated everything else, which is valuable diagnostic work.

## Closing

USB-C charging failures are negotiations that fell apart, and the fix is finding which party walked away: the wrong port, a weak charger, a tired cable, a dirty connector, or confused software. Test with known-good gear at each step and you will isolate it without guesswork. The general [USB-C charging troubleshooting guide](/articles/troubleshoot-usb-c-charging-not-working-on-laptop/) covers the same ground from a diagnostic angle if you want a second pass.
