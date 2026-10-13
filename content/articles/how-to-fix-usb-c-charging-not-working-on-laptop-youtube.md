---
title: "How to Fix USB-C Charging Not Working on a Laptop (Video Walkthrough)"
slug: how-to-fix-usb-c-charging-not-working-on-laptop-youtube
date: 2026-09-11
categories: ["battery"]
tags: ["battery", "charging", "usb-c"]
description: "USB-C charging not working on your laptop? Check wattage, cables, ports, and BIOS settings with this step-by-step fix guide for USB-C power issues."
thumbnail: "/images/thumbs/how-to-fix-usb-c-charging-not-working-on-laptop-youtube.webp"
faqs:
  - q: "Why won't my laptop charge through USB-C?"
    a: "The most common reasons are a charger or cable that does not support USB Power Delivery at the wattage your laptop needs, a USB-C port on the laptop that does not accept charging, or debris in the port. Less often, the cause is a BIOS setting that disables USB-C charging, outdated firmware, or a failed port. Work from the charger inward toward the laptop."
  - q: "Do all USB-C ports on a laptop support charging?"
    a: "No, and this trips up a lot of people. Many laptops have several USB-C ports but only one that accepts power input, sometimes marked with a small plug or lightning icon. Check your manual or the icons next to the ports. Plugging the charger into a data-only USB-C port does nothing, and it is not a fault."
  - q: "Can any USB-C cable charge a laptop?"
    a: "No. Many USB-C cables are built only for data or for low-power phone charging and cannot carry the 45 to 100 watts a laptop needs. For laptop charging you need a cable rated for USB Power Delivery at your charger's wattage. If your cable came with a phone, assume it is inadequate until proven otherwise."
  - q: "Is 65W enough to charge a gaming laptop over USB-C?"
    a: "Usually not while you are using it. Many gaming laptops need 180 to 280 watts, so a 65W USB-C charger may only slow the discharge or charge the battery while the machine is off or asleep. Check your laptop's required wattage on the original adapter's label and match or exceed it."
---

USB-C charging promises one cable for everything, right up until you plug it in and nothing happens. No charging LED, no battery icon change, just silence. Or worse, the laptop charges on one port but not another, or charges only when powered off. USB-C power problems are confusing because the connector is universal but the capabilities behind it are not.

The good news is that most USB-C charging failures come down to three things: the wrong charger, the wrong cable, or the wrong port. This guide walks through each one with concrete checks, then moves to the firmware and driver fixes for the stubborn cases.

## Why this happens

- **The charger does not support USB Power Delivery, or its wattage is too low.** A phone charger with a USB-C plug may deliver only 15 to 25 watts, far below what a laptop needs to charge.
- **The cable cannot carry enough power.** Thin phone cables and cheap no-name cables often lack the wiring for 60W or 100W Power Delivery.
- **You are using a data-only USB-C port.** Many laptops accept charging on just one of their USB-C ports. The others are data and display only.
- **Debris or damage in the port.** Pocket lint and dust packed into a USB-C port prevent the pins from making proper contact.
- **BIOS or firmware has USB-C charging disabled or broken.** Some laptops have a BIOS toggle for USB-C/Thunderbolt charging, and firmware bugs can break power negotiation.
- **Power negotiation failed.** USB-C charging requires the charger and laptop to agree on voltage. A glitch in this handshake can leave the port dead until reset.

## How to fix it

Work through these in order, starting with the charger and cable, which cause the majority of failures.

### Fix 1: Verify the charger meets your laptop's wattage

USB-C chargers are not interchangeable the way barrel chargers of the same voltage were.

1. Find your laptop's required wattage on the original adapter's label or in the manual. Common values are 45W, 65W, 90W, and 100W.
2. Check the USB-C charger's label for its Power Delivery output. It must list the voltage and amperage combinations, such as 20V at 3.25A for 65W.
3. The charger should support **USB Power Delivery (USB PD)**. Chargers that only support proprietary fast-charging standards often will not charge a laptop at all.
4. Match or exceed the laptop's requirement. A 65W laptop on a 45W charger may charge very slowly or only while asleep.
5. If you suspect the wattage is marginal, see our guide on [65W chargers not being enough for gaming laptops](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-in-windows-11-24h2/).

### Fix 2: Use a proper Power Delivery cable

The cable is the most underestimated part of the chain.

1. Use the cable that came with the charger if it did. Third-party cables must be rated for the wattage you need: look for 60W, 100W, or 240W ratings printed on the packaging.
2. Avoid thin phone-charging cables. If the cable feels flimsy compared to the charger's output, it is probably inadequate.
3. Try a different known-good USB-C cable, ideally a short, thick one rated for 100W PD.
4. Test the charger and cable with another USB-C device, like a phone or tablet. If nothing charges, the charger or cable is dead.
5. If the phone charges but the laptop does not, the wattage or the PD negotiation is the issue, not a dead charger.

### Fix 3: Plug into the correct USB-C port

This single step resolves an embarrassing number of cases.

1. Look closely at the icons next to each USB-C port. A plug or battery icon marks the charging port. A lightning bolt marks Thunderbolt, which usually also charges.
2. Check your laptop's manual for which port accepts power. On many models only one port does.
3. Move the charger to the designated charging port and watch the LED and battery icon for 30 seconds.
4. If your laptop has a barrel charging port as well, test that too. If barrel charging works but USB-C does not, the problem is isolated to the USB-C subsystem.

### Fix 4: Clean and inspect the USB-C port

Lint is the silent killer of USB-C connections.

1. Power the laptop off and unplug everything.
2. Shine a light into the USB-C port and look for packed lint, dust, or bent pins.
3. Gently loosen debris with a wooden or plastic toothpick. Never use metal tools, which can short the pins.
4. Blow out the port with short bursts of compressed air, holding the can upright.
5. Reconnect the charger firmly. USB-C connectors should seat with a distinct click and no wobble.
6. Try all USB-C ports again after cleaning, in case debris was the only issue.

### Fix 5: Reset the power negotiation with a full power cycle

A failed PD handshake can leave the port unresponsive until the controller resets.

1. Shut the laptop down completely and unplug the charger from both ends.
2. If the battery is removable, remove it. Otherwise, press and hold the power button for 30 seconds.
3. Wait two full minutes with everything disconnected.
4. Reconnect the charger to the wall first, then to the laptop's charging port.
5. Power on and check whether charging starts. This clears more stuck negotiations than you would expect.

### Fix 6: Check BIOS settings for USB-C and Thunderbolt charging

Some laptops let the firmware disable USB-C power input.

1. Restart and enter the BIOS or UEFI setup, usually with **F2**, **Del**, or **F12** depending on the brand.
2. Look for sections named **USB Configuration**, **Thunderbolt**, **Power**, or **Advanced**.
3. Enable options like **USB-C Charging**, **Thunderbolt Boot Support**, or **USB PowerShare** if present.
4. Save and exit, then test charging again.
5. While you are there, check whether a newer BIOS is available. Firmware updates frequently fix USB-C power negotiation bugs.

### Fix 7: Update USB and Thunderbolt drivers and firmware

Windows-side drivers participate in the charging handshake on many models.

1. Open **Device Manager** and expand **Universal Serial Bus controllers**.
2. Right-click each **USB Root Hub** and **USB-C** or **Thunderbolt** entry, choose **Update driver**, then **Search automatically**.
3. Visit your manufacturer's support page for Thunderbolt firmware updates, which Windows Update often misses. Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can find current Thunderbolt and chipset drivers.
4. In **Device Manager**, also check **System devices** for anything related to USB-C power delivery with a warning icon.
5. Restart and test. If charging works on the barrel port but no USB-C port works after all of this, the USB-C power circuitry may have failed and needs professional repair.

## Closing

USB-C charging failures look mysterious but follow a simple chain: enough watts, a cable that can carry them, the right port, and a clean connection. Verify the chain piece by piece before assuming the laptop is broken, and you will find the weak link quickly. For step-by-step charging checks that apply to any connector, see [laptop battery not charging when plugged in](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/).
