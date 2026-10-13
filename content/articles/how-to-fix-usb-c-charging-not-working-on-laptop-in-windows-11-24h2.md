---
title: "How to Fix USB-C Charging Not Working on a Laptop in Windows 11 24H2"
slug: how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2
date: 2026-09-18
categories: ["battery"]
tags: ["battery", "usb-c", "charging", "windows 11 24h2"]
description: "USB-C charger plugged in but laptop won't charge on 24H2? Fix port, cable, driver, and power-delivery issues step by step."
thumbnail: "/images/thumbs/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why won't my laptop charge over USB-C after the 24H2 update?"
    a: "The 24H2 update can replace the USB-C port controller or chipset drivers with versions that mishandle power-delivery negotiation. The laptop and charger fail to agree on voltage, so no charging starts. Reinstalling the chipset and USB controller drivers usually restores proper negotiation."
  - q: "Do all USB-C ports on a laptop support charging?"
    a: "No. Many laptops have multiple USB-C ports but only one or two support charging, usually marked with a small plug or battery icon. Check your manual. Plugging the charger into a data-only USB-C port does nothing, and this is the most common cause of USB-C charging complaints."
  - q: "Can I use any USB-C charger for my laptop?"
    a: "No. The charger must support USB Power Delivery and deliver your laptop's required wattage. A 30W phone charger cannot charge a laptop that needs 65W — at best it charges extremely slowly, at worst the laptop ignores it. Match the wattage printed on your original adapter."
  - q: "Does cable quality matter for USB-C charging?"
    a: "Enormously. Many cheap USB-C cables only carry data and low-power charging, or lack the e-marker chip required for wattages above 60W. For laptop charging you need a cable explicitly rated for 65W or 100W USB Power Delivery. A data-only cable in a charging port still will not charge."
---

USB-C was supposed to simplify charging: one cable for everything. Instead you are staring at a laptop that ignores its USB-C charger completely — or charges for a minute, then stops. After the Windows 11 24H2 update, USB-C charging failures spiked, because the update touches exactly the drivers that negotiate power delivery between your charger and your laptop.

USB-C charging is a negotiation, not just a power flow. The charger and laptop must agree on voltage and current through the USB Power Delivery protocol, and that handshake involves the cable, the port, the port controller driver, and the chipset driver. Any one of them can break the deal. This guide tests each participant in order.

## Why this happens

- **You are using the wrong USB-C port.** Only designated ports support charging; data-only ports ignore the charger entirely.
- **The cable cannot carry laptop wattage.** Data-only or low-power cables fail the power-delivery handshake above 60W.
- **The charger is underpowered.** A phone charger cannot satisfy a laptop's power-delivery request, so the laptop refuses the connection.
- **24H2 replaced the USB or chipset drivers.** New generic drivers can mishandle the power-delivery negotiation the old ones performed correctly.
- **The port is dirty or damaged.** Lint in a USB-C port prevents the full pin contact the negotiation needs.
- **BIOS power-delivery firmware is outdated.** The port controller's firmware governs the handshake at a level below Windows.

## How to fix it

Work through these in order. Each step eliminates one party to the negotiation.

### Fix 1: Use the correct USB-C port

This resolves more USB-C charging complaints than everything else combined.

1. Look closely at your laptop's USB-C ports for a small charging icon — a plug, a battery, or a lightning bolt symbol next to the port.
2. Plug the charger into that specific port. On many laptops only the left-side or rear port supports charging.
3. Check your manual if no port is marked. Some laptops, especially budget models, have no charging-capable USB-C port at all and require the barrel charger.
4. Once connected to the right port, wait a full minute — power-delivery negotiation can take longer than you expect on the first connection.

### Fix 2: Verify the charger wattage and standard

An incompatible charger fails the handshake before charging begins.

1. Read the wattage on your original laptop adapter — commonly 45W, 65W, or 90W — and match it with your USB-C charger.
2. Confirm the USB-C charger explicitly supports **USB Power Delivery (USB PD)**. Chargers that only support Quick Charge or proprietary phone standards will not charge most laptops.
3. If your laptop needs 65W and your charger delivers 65W but charging is slow or intermittent, the charger may not sustain its rated output. Try a charger rated one step higher.
4. Our guide to [underpowered chargers on gaming laptops](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-in-windows-11-24h2/) explains the wattage math in detail.

### Fix 3: Use a proper USB PD cable

The cable is an active participant in power delivery, not a dumb wire.

1. Check your cable's rating — it should be printed on the cable or packaging as 60W, 100W, or 240W USB PD.
2. For anything above 60W, the cable needs an e-marker chip. If your cable came with a phone, it almost certainly lacks one.
3. Test with the cable that came with the laptop or a certified 100W USB PD cable. Keep the cable short — very long cables can cause negotiation failures.
4. Inspect both ends for bent pins, corrosion, or debris.

### Fix 4: Clean the USB-C port

Lint is the silent killer of USB-C charging.

1. Power off the laptop completely and unplug everything.
2. Shine a bright light into the USB-C port. You will often see a visible mat of lint at the bottom.
3. Use a wooden or plastic toothpick to gently loosen and lift out the debris. Work carefully around the center tongue — it is fragile. Never use metal tools.
4. Finish with short bursts of compressed air, then reconnect and test.

### Fix 5: Reinstall USB and chipset drivers

If the hardware is right, 24H2's driver swap is the likely culprit.

1. Right-click Start and open **Device Manager**.
2. Expand **Universal Serial Bus controllers**. Right-click each **USB Root Hub** and **USB-C** or **UCSI** entry and choose **Uninstall device**.
3. Expand **System devices** and uninstall anything labeled **Intel USB** or **AMD USB** controller the same way.
4. Restart. Windows redetects the controllers and reinstalls drivers during boot.
5. Then update the chipset drivers properly: run Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) or download the chipset package from your laptop manufacturer's support site. The chipset driver governs power-delivery negotiation.

### Fix 6: Update the BIOS for port-controller firmware

The USB-C port controller runs its own firmware, updated through BIOS packages.

1. Note your BIOS version with `msinfo32`.
2. Check your manufacturer's support site for a BIOS update whose changelog mentions USB-C, power delivery, or charging.
3. Install it with the barrel charger connected (not USB-C, since that is the broken path) and all apps closed.
4. After rebooting, test USB-C charging again — port-controller firmware fixes are a common entry in BIOS changelogs.

For general charging diagnostics beyond USB-C, our [step-by-step charging diagnostic](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/) covers the full chain.

### Fix 7: Reset the embedded controller

A stuck power controller can refuse USB-C negotiation until cleared.

1. Shut down and unplug all chargers and USB devices.
2. Hold the power button for 30 seconds to drain residual power.
3. On Acer laptops, use the battery reset pinhole on the bottom instead.
4. Reconnect only the USB-C charger to the correct port and power on.

USB-C charging failures feel mysterious because the negotiation is invisible, but the checklist is mechanical: right port, right wattage, right cable, clean port, correct drivers, current firmware. Miss any one and the handshake fails silently.

## Closing

Start with the port and cable — they cause the majority of USB-C charging failures and take minutes to verify. If the hardware checks out, the 24H2 driver reinstall and a BIOS update restore the negotiation in nearly every remaining case.
