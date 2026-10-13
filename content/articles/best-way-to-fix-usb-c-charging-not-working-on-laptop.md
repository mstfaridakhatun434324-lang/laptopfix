---
title: "USB-C Charging Not Working on Your Laptop? Here's How to Fix It"
slug: best-way-to-fix-usb-c-charging-not-working-on-laptop
date: 2026-10-02
categories: ["battery"]
tags: ["usb-c", "charging", "power delivery", "thunderbolt"]
description: "Laptop won't charge over USB-C? Check the port, cable wattage, and drivers with this step-by-step fix guide for USB-C power delivery."
thumbnail: "/images/thumbs/best-way-to-fix-usb-c-charging-not-working-on-laptop.webp"
faqs:
  - q: "Why does my laptop charge with the barrel charger but not USB-C?"
    a: "The most common reasons: you're using a USB-C port that doesn't support charging (many laptops have USB-C ports for data only), the charger or cable doesn't supply enough wattage, or the cable isn't rated for Power Delivery. Check your manual for which port accepts power and what wattage it needs."
  - q: "Can any USB-C cable charge a laptop?"
    a: "No. Basic USB-C cables top out at 60W and some cheap ones far less; laptops needing 65W, 90W, or more require a cable explicitly rated for that wattage with USB Power Delivery support. A phone cable will usually charge very slowly or not at all."
  - q: "Is USB-C charging slower than the original charger?"
    a: "It can be, if the USB-C charger delivers less wattage than the original. A 65W laptop on a 45W USB-C charger will charge slowly and may even discharge under heavy load. Match or exceed the original charger's wattage for full-speed charging."
  - q: "Could a Windows update break USB-C charging?"
    a: "Yes — Thunderbolt and USB4 controller driver updates (or failed ones) can disable charging on those ports. If USB-C charging broke right after an update, reinstalling the Thunderbolt/USB4 drivers from your manufacturer's support site usually restores it. Also check Device Manager for warning icons on the USB4 host router, which confirm a driver problem rather than hardware."
---

USB-C charging is wonderfully convenient — one cable for everything — until you plug in and nothing happens. No charging light, no "plugged in" message, just a battery percentage slowly ticking downward. Before you assume the port is dead, know that most USB-C charging failures are boringly simple: wrong port, weak charger, or wrong cable. This guide walks through the checks in the order that solves the problem fastest.

## Why this happens

- **You're using the wrong USB-C port.** Many laptops have multiple USB-C ports but only one supports charging. The others are data/display only — plugging power into them does nothing.
- **The charger doesn't supply enough wattage.** A 45W phone-style charger can't properly feed a laptop that wants 65W or 90W. The laptop may refuse to charge or charge painfully slowly.
- **The cable can't handle the power.** Not all USB-C cables support Power Delivery at laptop wattages. Thin, unmarked, or very long cables often fail where a proper rated cable works.
- **Thunderbolt/USB4 drivers are broken.** On Intel and AMD machines, the USB4/Thunderbolt controller manages power negotiation. Corrupt drivers after an update can kill charging on those ports.
- **The embedded controller needs a reset.** The chip negotiating power delivery can get stuck, especially after the laptop fully died or a charger was hot-unplugged.
- **BIOS or firmware disabled the port.** Some BIOS updates reset USB-C power settings, and a few laptops let you disable USB-C charging in BIOS entirely.

## How to fix it

Work through these in order — the first three solve the majority of cases.

### Fix 1: Use the correct port

This sounds obvious, but it's the single most common cause.

1. Check your laptop's manual or the manufacturer's spec page for which USB-C port supports charging — it's often marked with a small **power/plug icon** or a **lightning bolt** next to the port.
2. On many laptops only the rear or left-side port accepts power; the other USB-C ports are data-only.
3. Plug the charger directly into that port — not through a hub or dock for this test.
4. Watch for the charging LED or the Windows battery icon change within 10 seconds.
5. If you're unsure, try every USB-C port on the machine with the same charger and cable, waiting 15 seconds on each.

### Fix 2: Verify charger wattage

An underpowered charger is the second most common culprit.

1. Find your laptop's required wattage: check the original barrel charger brick (e.g., 65W, 90W) or the spec sheet.
2. Check the USB-C charger's label for its output — it must list a profile at or above your laptop's needs (e.g., 20V⎓3.25A = 65W).
3. If the charger is weaker, the laptop may charge very slowly, refuse to charge while in use, or show "plugged in, not charging."
4. Borrow or buy a USB-C PD charger rated at or above the original wattage for testing.
5. Multi-port chargers split wattage — a "100W" charger with two devices plugged in may only give your laptop 65W or less. Test with only the laptop connected.

### Fix 3: Swap the cable

Cables fail more often than ports do, and most people test with whatever cable was nearest.

1. Use a cable explicitly rated for USB Power Delivery at your needed wattage (look for "100W" or "240W" printed on the connector or packaging).
2. Keep it short for testing — under 1 meter. Long cables drop more voltage.
3. Try the cable in both orientations (USB-C is reversible, but a damaged pin can behave differently per side).
4. If you have another known-good PD cable, swap it in before suspecting the laptop.
5. Avoid bargain-bin unbranded cables for laptop charging; a bad cable can negotiate the wrong voltage.

### Fix 4: Reset the embedded controller

When hardware is fine but negotiation is stuck, a full power reset clears it.

1. Shut down completely and unplug everything, including the USB-C charger.
2. Hold the **power button** for 30–60 seconds.
3. If your model has a pinhole **battery reset** button on the bottom, press it with a paperclip for 15 seconds instead.
4. Reconnect only the USB-C charger (correct port, good cable) and power on.
5. Check whether charging starts. If it does, the controller just needed a clean renegotiation.

### Fix 5: Reinstall Thunderbolt/USB4 and chipset drivers

Driver corruption after Windows updates is a classic cause of sudden USB-C charging loss.

1. Open **Device Manager** (Win + X) and expand **System devices**.
2. Look for **Thunderbolt Controller**, **USB4 Host Router**, or **Intel(R) USB4** entries.
3. Right-click each > **Uninstall device** (do not delete driver software if asked — actually, if the problem started after an update, ticking **delete the driver** and reinstalling fresh from the manufacturer is better).
4. Visit your manufacturer's support site (e.g., [Dell](https://www.dell.com/support), [Lenovo](https://support.lenovo.com/us/en/)) and install the latest **Thunderbolt/USB4** and **chipset** drivers for your exact model.
5. Restart and test USB-C charging again.

### Fix 6: Check BIOS settings and update firmware

Some laptops gate USB-C charging behind BIOS options.

1. Enter BIOS (**F2**, **F10**, or **Del** at boot depending on brand).
2. Look under **Power**, **Advanced**, or **USB Configuration** for options like **USB-C Charging**, **Type-C Power**, or **USB PowerShare** — make sure charging-related options are enabled.
3. While there, check the BIOS version against the manufacturer's support site and update if a newer one mentions USB-C, Thunderbolt, or power delivery fixes.
4. Keep the barrel charger (if you have one) connected during any BIOS update.
5. After updating, retest with the USB-C charger.

### Fix 7: Test methodically to isolate the fault

If nothing has worked, narrow it down to exactly one faulty component.

1. Test your charger + cable on a different USB-C laptop or phone that supports PD charging.
2. Test a known-good charger + cable on your laptop's charging port.
3. If your gear works elsewhere but nothing works on your laptop's port (and drivers/BIOS are current), the port's power circuitry may be damaged — that needs professional repair.
4. If only your charger fails everywhere, replace the charger — and match the wattage this time.
5. For laptops that charge only when off or behave oddly while plugged in, see [battery only charges when the laptop is off](/articles/how-to-fix-battery-only-charges-when-laptop-is-off-in-windows-11-24h2/) and our general [not charging troubleshooting](/articles/laptop-battery-not-charging-after-windows-11-24h2-update-troubleshooting/).

Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) has additional guidance on USB-C and power issues if you need the official reference.

## Closing

USB-C charging failures are a process of elimination: right port, enough watts, good cable, clean controller, healthy drivers. Work that chain and you'll find the weak link — it's rarely the laptop itself. Once charging works, label your good cable and charger so future-you doesn't grab the phone cable in a hurry and wonder why the battery is draining while "plugged in."
