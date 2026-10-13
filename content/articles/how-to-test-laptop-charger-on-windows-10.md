---
title: "How to Test Your Laptop Charger on Windows 10 (5 Methods)"
slug: how-to-test-laptop-charger-on-windows-10
date: 2026-10-02
categories: ["battery"]
tags: ["laptop charger", "windows 10", "power adapter test"]
description: "Is your charger dead or is it the laptop? Test your laptop charger on Windows 10 with these 5 methods — from simple LED checks to multimeter readings."
thumbnail: "/images/thumbs/how-to-test-laptop-charger-on-windows-10.webp"
faqs:
  - q: "How can I tell if my laptop charger is dead?"
    a: "Start with the basics: check the LED on the brick, feel whether it gets warm during use, and watch the Windows 10 battery icon when you plug it in. If the icon never changes, try another outlet and inspect the cable for damage. For certainty, measure the output voltage with a multimeter and compare it to the label. Zero volts or a big mismatch means the charger is dead."
  - q: "Can Windows 10 tell me if my charger is working?"
    a: "Partially. The battery icon and the Battery settings page show whether the system detects AC power and whether the battery is charging. The command `powercfg /batteryreport` shows charge/discharge rates over time, which reveals a weak charger that cannot keep up. But Windows cannot measure the charger's actual voltage — for that you need a multimeter or a USB-C power meter."
  - q: "Why does my charger get hot? Is that normal?"
    a: "Warm is normal — chargers convert AC to DC and lose some energy as heat, especially under heavy load. Too hot to touch comfortably, a burning smell, buzzing, or visible swelling of the brick are not normal. Unplug an overheating charger immediately and replace it. Heat plus intermittent charging usually means failing internal components."
  - q: "Can I use a phone charger to test my laptop?"
    a: "Only for USB-C laptops, and only as a rough test. A phone charger (typically 18-30W) may make the battery icon show 'plugged in' on a laptop that needs 65W, but it will charge very slowly or not at all under load. If the icon responds to the phone charger but not to your laptop charger, your laptop charger is the problem — not the laptop."
---

When your laptop will not charge, the charger itself is suspect number one — and also the cheapest thing to replace. But before you order a new one, spend ten minutes testing the old one properly. Half the "dead charger" diagnoses I see turn out to be a bad outlet, a loose cable, or a laptop-side problem. This guide gives you five tests, from dead simple to definitive.

These steps work on any Windows 10 laptop regardless of brand. If your tests point at the laptop rather than the charger, the walkthrough for [troubleshooting a charger that is not detected](/articles/troubleshoot-laptop-charger-not-detected/) picks up where this one leaves off.

## Why This Happens

- **Cable strain at the connectors.** Years of bending where the cable meets the brick or the plug breaks internal wires while the outside looks fine.
- **Failed components inside the brick.** Capacitors age; a charger that worked for five years can die overnight.
- **Wrong wattage replacement.** A 45W charger on a 90W laptop may light the LED but never actually charge the battery.
- **Damaged DC jack on the laptop.** The charger can be perfect while the laptop's port has a cracked solder joint or bent pin.
- **Outlet or power strip problems.** Dead outlets, switched-off power strips, and overloaded strips mimic charger failure exactly.
- **USB-C negotiation failures.** With USB-C charging, the laptop and charger must agree on voltage. A damaged cable can break negotiation while still passing some power.

## How to Fix It

Work through these in order. Each test narrows down whether the charger, the cable, or the laptop is at fault.

### Fix 1: The 60-Second Visual and LED Check

Start with what you can see and feel — it catches a surprising number of failures.

1. Plug the charger into a wall outlet you know works (test the outlet with a lamp or phone charger first).
2. Look for the LED on the charger brick or plug. No light on a charger that normally has one is a strong failure signal.
3. Run your fingers along the full cable length, feeling for lumps, flat spots, or areas that bend too easily — signs of broken internal wires.
4. Check both ends where cable meets connector. Fraying, exposed wire, or a connector that wobbles means the cable is done.
5. Smell the brick. A burnt-plastic smell means failed components inside — do not use it again.
6. Feel the brick after 5 minutes plugged in with no laptop attached. Slightly warm is normal; stone cold on a charger that used to warm up suggests it is dead.

### Fix 2: Watch Windows 10's Battery Icon Response

Windows 10 tells you whether it sees AC power — a useful signal even if it cannot measure voltage.

1. Note the current battery percentage, then plug in the charger.
2. Watch the taskbar battery icon: it should gain a plug symbol within 5-10 seconds.
3. Hover over the icon. It should say something like "84% available (plugged in, charging)".
4. Open **Settings** > **System** > **Battery** and confirm the status line matches.
5. If the icon never changes, unplug and replug firmly — then try rotating a barrel plug slightly in the jack. Intermittent response points to the port or plug, not the brick.
6. No response at all after Fix 1 looked fine? Move to the multimeter test in Fix 4 for a definitive answer.

### Fix 3: Check the Charge Rate With powercfg

A weak charger sometimes "works" but cannot deliver enough current. Windows 10's battery report exposes this.

1. Press **Win + X**, choose **Windows PowerShell (Admin)** or **Command Prompt (Admin)**.
2. Run `powercfg /batteryreport` and open the HTML file it generates (it prints the path).
3. Scroll to **Recent usage** and find periods where the laptop was plugged in. Compare the charge rate (mW) against your charger's rated wattage.
4. A 65W charger showing only 10-15W of charge rate while the laptop idles suggests the charger is failing or the laptop is throttling it.
5. Also check **Battery capacity history**: if full charge capacity is healthy but charging is slow, the charger is the bottleneck, not the battery. For help reading the full report, see [how to check your battery report via CMD](/articles/best-way-to-check-battery-report-via-cmd/).
6. Repeat the test with the laptop powered off. If it charges fine while off but not while on, the charger is underpowered for the load.

### Fix 4: Measure Output Voltage With a Multimeter

This is the definitive test. A $15 multimeter answers the question with certainty.

1. Set the multimeter to **DC voltage** (V with a straight line, not a wavy one), at a range above your charger's rated output (usually 19-20V — check the label).
2. Plug the charger into the wall. Touch the red probe to the inner contact of the barrel plug and the black probe to the outer barrel.
3. Read the voltage. It should match the label within about 5% (e.g., 19V-20.5V for a 19.5V charger).
4. Zero volts or wildly low voltage: the charger is dead. Replace it.
5. Correct voltage but the laptop still will not charge: the charger is fine — suspect the laptop's DC jack, charging circuit, or battery. That is a repair-shop diagnosis.
6. For USB-C chargers, use a USB-C power meter dongle (about $15-20) instead — it shows live voltage, amperage, and wattage during negotiation, which a multimeter cannot do on USB-C.

### Fix 5: Swap-Test to Isolate the Fault

When you cannot measure, substitute. This test needs either a second charger or a second laptop.

1. Borrow a charger with the **same connector, voltage, and equal-or-higher wattage**. Never test with a higher voltage than your laptop's rating.
2. If the borrowed charger charges your laptop, your charger is bad. Order an exact replacement.
3. If the borrowed charger also fails, your laptop's charging port or circuit is the problem — not the charger.
4. Alternatively, test your charger on a compatible second laptop. If it charges that one, your laptop is at fault.
5. No spare hardware? Many repair shops will test your charger free in under a minute — cheaper than guessing with a $60 replacement order.
6. When buying a replacement, match voltage exactly and wattage at least equally. Genuine or manufacturer-certified chargers are worth it; cheap no-name bricks cause the exact problems in [battery health unknown errors](/articles/troubleshoot-dell-battery-health-unknown/) and worse.

### Fix 6: Check BIOS Adapter Status and Run the Power Troubleshooter

When Windows 10's reporting is ambiguous, the firmware and the built-in troubleshooter give independent verdicts.

1. Reboot into BIOS/UEFI (**F2**, **Del**, or **F10** at the logo screen) and find the **AC Adapter**, **Adapter Type**, or **Power** page.
2. Note whether the BIOS detects the adapter and what wattage it reports. A BIOS that shows "Unknown" or "Not detected" while the charger tests fine electrically points to a damaged ID pin or a non-genuine adapter the firmware rejects.
3. Boot back into Windows 10 and open **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters** > **Power** > **Run the troubleshooter**.
4. Let it scan and apply any recommended fixes, which sometimes reset stuck power configurations.
5. Re-test charging after the troubleshooter completes. If the BIOS sees the adapter but Windows 10 still does not, the problem is in Windows' driver stack — reinstall the battery drivers as described in [charger detection troubleshooting](/articles/troubleshoot-laptop-charger-not-detected/).
6. If neither the BIOS nor Windows detects the adapter and the multimeter test failed, you have triple confirmation: replace the charger with confidence.

## Closing

Testing a charger is really about ruling things out in the cheapest order: eyes and nose first, Windows' own reporting second, a multimeter for certainty, and a swap test when you have the hardware. Most of the time you will know the answer before you reach Fix 4. Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) has additional background on battery and power status indicators if you want the official reference.
