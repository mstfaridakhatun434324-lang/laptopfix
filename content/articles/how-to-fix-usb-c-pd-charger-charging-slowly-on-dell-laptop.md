---
title: "USB-C PD Charger Charging Slowly on a Dell Laptop: Fixes"
slug: how-to-fix-usb-c-pd-charger-charging-slowly-on-dell-laptop
date: 2026-09-02
categories: ["battery"]
tags: ["dell", "usb-c", "slow charging"]
description: "USB-C charger crawling on your Dell? Slow PD charging is usually a wattage, cable, or negotiation issue. Here's how to get full-speed charging back."
thumbnail: "/images/thumbs/how-to-fix-usb-c-pd-charger-charging-slowly-on-dell-laptop.webp"
faqs:
  - q: "Why is my USB-C charger slow on my Dell laptop?"
    a: "The usual reasons: the charger doesn't supply enough watts for your model, the cable can't carry full power, the laptop negotiated a low-power PD profile, or Dell's firmware is limiting charge speed because it doesn't recognize the adapter. Any of these turns fast charging into a trickle."
  - q: "How many watts does my Dell need over USB-C?"
    a: "It depends on the model: ultrabooks typically need 45–65W, while performance models want 90–130W. Check the original barrel or USB-C adapter's rating and your manual. Using a 30W phone charger on a 90W laptop will charge painfully slowly or not at all."
  - q: "Does the USB-C cable affect charging speed?"
    a: "Absolutely. USB-C cables have different power ratings — many cheap cables only support 60W, and some only 15W. For laptops you want a cable rated for 100W (5A) with proper e-marker chips. A weak cable silently caps your charging speed."
  - q: "Can a BIOS update fix slow USB-C charging?"
    a: "Yes, Dell regularly improves USB-C PD negotiation in BIOS updates. If your Dell charges slowly with a known-good high-wattage adapter and cable, updating the BIOS is one of the most effective fixes."
---

USB-C charging was supposed to simplify everything: one cable, one charger, full speed. But on Dell laptops, plugging in a USB-C PD charger sometimes results in a maddeningly slow trickle — the percentage creeps up, or Windows warns that the charger is underpowered.

The frustration is that everything *looks* connected. The real action happens invisibly: the laptop and charger negotiate a power contract, and if anything in that chain is weak, you get a fraction of the speed you paid for.

## Why this happens

- **Charger wattage too low for the model:** A 45W adapter on a Dell that expects 90W+ will charge slowly or trigger Dell's "underpowered charger" warning.
- **Cable can't carry the power:** Many USB-C cables are rated for only 60W or less. Without a 100W-rated (5A, e-marked) cable, the laptop negotiates down.
- **PD negotiation settling on a low profile:** A flaky cable or charger can cause the handshake to fail and fall back to a basic 15W or 27W profile.
- **Dell firmware not recognizing the adapter:** Dell validates adapters; unrecognized ones may be current-limited by the BIOS as a safety measure.
- **Charging while under heavy load:** If the CPU/GPU are maxed out, most of the charger's output feeds the system, leaving a trickle for the battery.
- **Dell Power Manager throttling charge speed:** Settings like Adaptive or thermal management can intentionally slow charging to control heat.

## How to fix it

Work through these in order, checking charge speed after each step.

### Fix 1: Match the wattage to your Dell model

This is the fix in most cases.

1. Find your model's required wattage: check the original adapter's label or look up your Service Tag on [Dell support](https://www.dell.com/support).
2. Read the output rating on your USB-C charger — if it says 45W and your Dell wants 90W, you've found the bottleneck.
3. Get a USB-C PD charger rated at or above your model's requirement (65W for most ultrabooks, 90–130W for performance models).
4. Plug it in and watch: Dell usually shows a brief "best performance with Dell power adapter" style message when it recognizes adequate power.

### Fix 2: Upgrade the cable

The cable is the most overlooked link in the chain.

1. Check your cable's rating — it should say 100W or 5A on the packaging or the connector housing. Unmarked cheap cables are suspect.
2. Replace it with a certified USB-C cable rated for 100W (5A) with an e-marker chip; Thunderbolt 4 cables also work and guarantee high power delivery.
3. Keep the cable short — very long cables can cause voltage drop that reduces effective charging power.
4. Retest with the new cable and the same charger; speed often jumps immediately.

### Fix 3: Force a clean PD renegotiation

A stuck negotiation can be cleared by reseating everything.

1. Unplug the charger from both the wall and the laptop.
2. Shut the laptop down fully, wait 30 seconds, then plug the charger into the wall first.
3. Connect the cable firmly to the laptop's designated charging USB-C port — on many Dells, only one port supports full PD charging, usually marked with a plug or lightning icon.
4. Power on and check the charge rate in **Settings > System > Power & battery** over 10 minutes.

### Fix 4: Update the Dell BIOS and PD firmware

Dell improves USB-C negotiation in firmware updates regularly.

1. On [Dell support](https://www.dell.com/support), enter your Service Tag and download the latest **BIOS** update.
2. Also look for **USB-C / Thunderbolt firmware** or **PD controller firmware** updates listed for your model.
3. Install with the original Dell adapter connected if you have one, and don't interrupt the process.
4. After rebooting, retest USB-C charging — negotiation behavior often improves dramatically.

### Fix 5: Check Dell Power Manager settings

Software can be throttling you deliberately.

1. Open **Dell Power Manager** (or **Dell Optimizer** on newer models).
2. Under **Battery Settings**, note the active mode: **Adaptive** and thermal-aware modes can slow charging to manage heat.
3. Switch to **Standard** temporarily and observe the charge speed.
4. Also check **Thermal Management** — an **Ultra Performance** setting draws more system power, leaving less for the battery; **Optimized** is the balanced choice. If charging stalls entirely rather than just slowing, see our general [USB-C charging troubleshooting](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/) guide.

### Fix 6: Reduce load while charging

Make sure the system isn't eating the charger's output.

1. Open **Task Manager** (**Ctrl+Shift+Esc**) and close CPU-heavy apps you don't need.
2. Set **Settings > System > Power & battery > Power mode** to **Balanced** instead of Best performance.
3. Charge with the lid closed or the laptop in sleep for 30 minutes as a test — if speed is normal then, system load was the thief.
4. For ongoing monitoring, compare against the behavior described in our guide to [batteries that only charge when the laptop is off](/articles/how-to-fix-battery-only-charges-when-laptop-is-off-after-windows-11-update/), which shares the same power-budget root cause.

### Fix 7: Test with a genuine Dell USB-C adapter

Isolate whether the laptop or the third-party gear is at fault.

1. Borrow or buy the Dell USB-C adapter specified for your model.
2. Test with Dell's adapter and a good cable — if speed is normal, your third-party charger was the problem (even if labeled with adequate wattage, some don't implement PD correctly).
3. If Dell's own adapter is also slow, the laptop's USB-C port or PD controller may be faulty — check for debris or bent pins in the port.
4. Persistent failure with genuine Dell gear warrants a warranty call with your Service Tag ready.

## Closing

Slow USB-C PD charging on a Dell is almost always a chain problem: charger wattage, cable rating, or negotiation — rarely the battery itself. Match the watts, use a real 100W cable, update the BIOS, and use the correct port. Get those four right and USB-C charging is as fast and simple as it was promised to be.
