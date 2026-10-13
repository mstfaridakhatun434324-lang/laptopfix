---
title: "How to Fix Slow Charging on a Laptop, Step by Step"
slug: how-to-fix-slow-charging-on-laptop-step-by-step
date: 2026-09-12
categories: ["battery"]
tags: ["slow charging", "charger", "usb-c charging"]
description: "Laptop charging painfully slowly? From weak adapters to background drain, here is the step-by-step diagnosis for slow charging."
thumbnail: "/images/thumbs/how-to-fix-slow-charging-on-laptop-step-by-step.webp"
faqs:
  - q: "Why is my laptop charging so slowly?"
    a: "The most common causes are an underpowered or failing charger, charging through a low-wattage USB-C port or hub, heavy usage while charging that consumes most of the incoming power, and battery-health features that deliberately slow the charge rate near full."
  - q: "How can I tell if my charger is the problem?"
    a: "Check the wattage printed on the charger and compare it to your laptop's requirement. Try the original charger if you are using a replacement. If charging speeds up dramatically with a different adapter, yours was underpowered or dying."
  - q: "Does using the laptop while charging slow it down?"
    a: "Yes, significantly. Every watt the CPU, GPU, and display consume is a watt not going into the battery. Gaming or video editing while charging can reduce net charge to a trickle or even drain the battery slowly despite being plugged in."
  - q: "Is slow charging bad for the battery?"
    a: "No, slower charging is actually gentler on battery chemistry and generates less heat. Slow charging is only a problem when it is unexpected and caused by a fault. Deliberately slow charging, like overnight, is good practice."
---

It used to take ninety minutes. Now it takes four hours, if it finishes at all. Slow charging creeps up gradually, which is why most people do not notice until it becomes absurd. The charger is plugged in, the icon says charging, but the percentage barely moves.

Charging speed is simple arithmetic: power in, minus power used, equals power stored. When the result is near zero, something is wrong on one side of that equation. This guide finds which side.

## Why this happens

- **Underpowered charger:** A 45W adapter on a laptop that wants 90W charges slowly or not at all under load.
- **Failing charger:** Adapters degrade. A dying brick may deliver a fraction of its rated wattage.
- **Wrong USB-C port or cable:** Not all USB-C ports support full charging wattage, and many cables are data-only or low-power.
- **Charging through a hub or dock:** Hubs and docks can throttle power delivery to the laptop.
- **Heavy use while charging:** The system consumes most of the incoming power, leaving a trickle for the battery.
- **Battery saver charging modes:** Some manufacturers slow charging deliberately as a battery-care feature.
- **Worn battery:** High internal resistance in old cells slows charge acceptance, especially past 80 percent.
- **Overheating:** Thermal protection throttles charging when the machine runs hot.

## How to fix it

Work through these in order, timing a charge session after each major change.

### Fix 1: Verify you are using the right charger

1. Read the wattage on your charger's label (for example 65W, 90W, 130W).
2. Check your laptop's manual or the original specs for its required wattage.
3. If you are using a replacement or travel charger with lower wattage, that is your answer.
4. Borrow the correct-wattage genuine charger to confirm before buying.

### Fix 2: Fix the USB-C chain

1. If your laptop charges over USB-C, plug directly into the laptop, not through a hub or dock.
2. Try every USB-C port on the machine. Manufacturers often designate one port for full-wattage charging.
3. Use a cable rated for the wattage you need. Cheap cables often cap at 60W or less.
4. Look for a charging indicator light or check **Settings** > **System** > **Power & battery** for slow-charger warnings.

### Fix 3: Reduce load while charging

1. Close heavy applications during charging sessions. Check **Task Manager** (**Ctrl + Shift + Esc**) sorted by CPU and GPU.
2. Lower screen brightness while charging. The display is a major consumer.
3. If the battery [drains while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-on-windows-11/) under load, your charger cannot even cover consumption, let alone charge.
4. For the fastest charge, shut the laptop down or let it sleep while plugged in.

### Fix 4: Check for deliberate slow-charge modes

1. Open your manufacturer's app (**Lenovo Vantage**, **MyASUS**, **Dell Power Manager**) and look for battery care or adaptive charging options.
2. Some modes slow charging past 80 percent intentionally to protect the cells.
3. Decide whether the slower top-end is acceptable. For overnight charging, it is ideal.
4. Disable it temporarily to test whether full-speed charging returns.

### Fix 5: Rule out heat throttling

1. Feel the charger brick and the laptop. Excessive heat triggers protective throttling.
2. Charge on a hard surface with vents clear, in a cool room.
3. If the machine runs hot generally, clean the vents with compressed air.
4. A hot charger brick itself can be a sign of a failing adapter.

### Fix 6: Test the outlet and the battery

1. Plug into a wall socket directly, skipping power strips and extension cords.
2. Run `powercfg /batteryreport` in an elevated Terminal and check wear. Very worn batteries accept charge slowly.
3. Try the [step-by-step plugged-in charging diagnosis](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/) if charging also stalls or stops.
4. If a second known-good charger of the right wattage is still slow, the laptop's charging circuit or battery is suspect.

### Fix 7: Update BIOS and charging firmware

1. Check your manufacturer's support site for BIOS updates: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
2. Charging and power-delivery logic lives partly in firmware, and updates fix negotiation bugs with USB-C chargers especially.
3. Keep the adapter connected during the update and do not interrupt it.
4. Retest charge speed after rebooting.

### Fix 8: Test the charge rate with the laptop powered off

This isolates the charger and battery from Windows power consumption.

1. Note the current battery percentage, then shut the laptop down completely. Not sleep, full shutdown.
2. Plug in the charger and leave it for exactly 30 minutes.
3. Power on and check the new percentage. Calculate the gain per 30 minutes.
4. A healthy setup typically gains 25 to 40 percent in 30 minutes powered off, depending on battery size and charger wattage.
5. If the powered-off charge rate is normal but Windows charging is slow, the problem is software-side: background load, drivers, or power settings consuming the incoming power.
6. If the powered-off rate is also slow, the problem is hardware-side: charger, cable, port, or battery.
7. This one test splits the entire diagnostic tree in half and tells you which branch to keep climbing.

## Closing

Slow charging is an equation with two sides, and the powered-off charge test is the fastest way to learn which side is guilty. Normal speed while off but slow in Windows means the charger and battery are fine and something in software, background load, drivers, or power settings, is consuming the incoming power before it reaches the cells. Slow even while off means the hardware chain itself is weak: the adapter, the cable, the port, or the battery's ability to accept charge. The wattage check comes first because an underpowered charger is the single most common cause and the easiest to fix. The USB-C chain, ports, cables, and hubs, is second, since power delivery negotiation fails in subtle ways. Heat throttling and deliberate battery-care slowdowns explain the cases where everything is technically working as designed. Work the equation methodically, and slow charging stops being a mystery and becomes a measurement.
