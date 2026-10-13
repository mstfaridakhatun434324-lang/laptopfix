---
title: "Laptop Overheats When Charging? Cool It Down With These Fixes"
slug: troubleshoot-laptop-overheating-while-charging
date: 2026-10-07
categories: ["battery"]
tags: ["overheating", "thermal", "cooling", "charging"]
description: "Excess heat while charging wears out batteries fast. Diagnose the heat source and bring temperatures back under control."
thumbnail: "/images/thumbs/troubleshoot-laptop-overheating-while-charging.webp"
faqs:
  - q: "What temperature is too hot for a laptop while charging?"
    a: "CPU temperatures up to 85 to 90°C under heavy load are typical and safe; sustained readings above 95°C indicate a cooling problem. For the battery itself, anything above about 40 to 45°C accelerates aging significantly. If the chassis is too hot to touch comfortably, treat it as too hot regardless of the numbers."
  - q: "Can I use a cooling pad to fix charging overheating?"
    a: "A cooling pad helps by improving airflow under the laptop, typically dropping temperatures 3 to 8 degrees. It is a useful aid but not a cure — if the machine overheats because of dust-clogged fans, a wrong charger, or dried thermal paste, the pad only masks the real problem. Use it alongside the fixes below, not instead of them."
  - q: "Why does my charger brick get extremely hot?"
    a: "Some warmth is normal, but a brick too hot to hold suggests it is overloaded, failing, or the wrong wattage for the laptop. An overloaded adapter is both a heat source and a potential safety issue — verify the wattage matches your laptop's requirement and replace damaged or underrated chargers."
  - q: "Should I charge with the laptop off to keep it cool?"
    a: "Charging while powered off generates the least heat and is the gentlest option for the battery. If overheating is severe, charging overnight while off is a practical workaround while you fix the underlying cooling problem — but do not accept it as the permanent answer."
---

Some heat while charging is physics. Too much heat is a problem looking for a cause — and on a laptop, sustained excess heat does not just throttle performance today, it cooks the battery and shortens the life of everything inside. If your machine gets uncomfortably hot every time you plug in, it is worth a proper diagnosis rather than just living with it.

Heat while charging comes from two sources added together: the charging process itself and whatever the laptop is doing at the same time. The fixes below attack both. For the companion issue of heat on battery power, see [battery overheating diagnostics](/articles/how-to-fix-laptop-battery-overheating-after-windows-11-update/).

## Why this happens

- **Charging current heats the battery and circuitry.** Higher wattage and faster charging mean more heat — unavoidable, but manageable.
- **Heavy workloads stack on top.** Gaming or rendering while charging doubles the thermal load.
- **Blocked or dust-clogged vents.** Restricted airflow is the number-one cause of abnormal heat.
- **Soft surfaces seal the intakes.** Beds and couches trap hot air underneath the machine.
- **Wrong or failing charger.** Underrated or damaged adapters run hot and stress the charging circuit.
- **Aged thermal paste or failing fans.** Heat cannot leave the CPU/GPU efficiently.
- **Hot ambient environment.** A 35°C room leaves the cooling system almost no headroom.
- **Battery fault generating excess heat.** A damaged pack can heat abnormally during charging.

## How to fix it

Work through these in order — start with Fix 1 and only move on if temperatures stay high.

### Fix 1: Fix the setup — surface, vents, and airflow

Move the laptop to a hard, flat surface and make sure no vent — bottom intakes, side or rear exhausts — is blocked. Lift the rear an inch with a stand or even a book to let air flow underneath. If you charge with the lid closed in a dock, open the lid or verify the dock does not cover the vents. Feel the exhaust air: strong and warm is good; weak or barely warm suggests the fans are not moving air, pointing to dust or fan failure. This setup check alone resolves a large share of overheating complaints.

### Fix 2: Reduce the simultaneous workload

Do not game, render video, or run heavy compiles while charging if you can avoid it — let the battery fill first, then work hard. For lasting relief, open **Settings > System > Power & battery** and set **Power mode** to **Best power efficiency**. In **Control Panel > Power Options > Change plan settings > Change advanced power settings**, expand **Processor power management** and set **Maximum processor state** on **Plugged in** to 95 percent. You will barely notice the performance difference, but peak temperatures drop meaningfully.

### Fix 3: Clean out dust properly

Shut down and unplug. Blow short bursts of compressed air through the intake and exhaust vents — hold the can upright, keep bursts under two seconds. Do this outside; the dust cloud can be impressive on a machine that has never been cleaned. If temperatures are still high and the laptop is over two years old, have a shop open it for internal cleaning and a fan health check. While monitoring with a free tool like HWMonitor, compare before-and-after temperatures under the same charging workload to confirm the improvement.

### Fix 4: Verify the charger is correct and healthy

Check the wattage on the brick against your laptop's requirement — an underrated charger works overtime, runs hot, and heats the charging circuit. Feel the brick after an hour of charging: warm is normal, painful to hold is not. Inspect the cable for damage and the connector for a snug fit. Replace wrong or damaged chargers with the manufacturer's original; identify the correct part through maker resources like [Dell's support pages](https://www.dell.com/support). For USB-C charging, confirm both charger and cable are rated for the laptop's full wattage.

### Fix 5: Tune the thermal and charging settings

Open your manufacturer's app — **Dell Power Manager**, **Lenovo Vantage**, **MyASUS**, **Armoury Crate** — and look at thermal profiles. Switch from silent to **balanced** or **cool** while charging; silent modes delay fan response and let heat build. If the app offers charge-rate or battery-care options, choose a gentler charging mode — slower charging means less heat in the pack. Also update the **BIOS** from the manufacturer's support site, since fan-curve and thermal-management fixes ship in firmware updates regularly.

### Fix 6: Address aged thermal paste and fans

On laptops more than three years old with persistent heat, dried thermal paste between the CPU/GPU and heatsink is a prime suspect — heat simply stops transferring to the cooling system. Repasting is an effective fix but requires disassembly; have a reputable shop do it unless you are experienced. While it is open, the fans should be inspected: a fan that does not spin freely or makes grinding noises needs replacing. Fresh paste plus healthy fans can drop load temperatures 10 to 15 degrees on an old machine.

### Fix 7: Check whether the battery is the heat source

If the hottest spot is the battery area rather than the CPU exhaust, suspect the pack. Run:

```
powercfg /batteryreport
```

and check capacity health, but remember a dangerous pack can show normal numbers. Stronger clues: the battery area far hotter than the rest of the chassis, rapid or erratic charge behavior, or any swelling. If you suspect the battery, stop charging it — run on AC with the battery removed if possible — and replace it with a genuine part. Heat plus a failing lithium pack is the one combination you should never ignore. Microsoft's safety and power guidance at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) is worth reviewing.

## Closing

Charging heat is normal; charging overheating is a solvable problem with a short list of causes. Fix the airflow, clean the dust, match the charger, ease the workload, and the temperatures come down. Keep monitoring afterward — if heat creeps back despite everything, the thermal paste or the battery is telling you it is their turn for attention. A [Windows 11 battery overheating walkthrough](/articles/how-to-fix-laptop-battery-overheating-on-windows-11/) covers the battery-specific heat angle in more detail.
