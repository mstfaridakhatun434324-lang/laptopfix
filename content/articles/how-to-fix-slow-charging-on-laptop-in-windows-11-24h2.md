---
title: "How to Fix Slow Charging on Your Laptop in Windows 11"
slug: how-to-fix-slow-charging-on-laptop-in-windows-11-24h2
date: 2026-10-09
categories: ["battery"]
tags: ["slow charging", "windows 11 24h2", "charger"]
description: "Laptop charging painfully slowly on Windows 11 24H2? Work through these eight fixes to find out whether it's the charger, a setting, or a driver."
thumbnail: "/images/thumbs/how-to-fix-slow-charging-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my laptop charging so slowly on Windows 11 24H2?"
    a: "Most often it's an underpowered or damaged charger, a worn cable, or a USB-C port that only negotiates low wattage. Software can play a role too: battery health limiters, aggressive power plans, and corrupted battery drivers can all throttle the charge rate."
  - q: "Can Windows 11 limit my charging speed?"
    a: "Yes. Manufacturer battery-health features (like charge caps at 80%), Windows battery saver mode, and some OEM power profiles reduce charge current to protect the battery or cut heat. Check your BIOS and the manufacturer's battery utility before assuming hardware failure."
  - q: "Does using the laptop while charging slow it down?"
    a: "Absolutely. If your machine draws 60W under load and the charger only supplies 65W, barely anything is left for the battery. Heavy gaming or video rendering while plugged in can make charging crawl or even drain the battery slowly."
  - q: "Will a higher-wattage charger charge my laptop faster?"
    a: "Only up to the laptop's designed limit. A 100W charger won't push a 65W laptop past 65W, but it helps if your current charger is undersized or if you charge through a low-power dock. Always match the voltage and use a reputable brand."
---

You plug in your laptop, glance at the battery icon, and an hour later the percentage has barely moved. Sometimes Windows shows "plugged in" without the number climbing at all — frustrating, since the cause could be the hardware, the firmware, or Windows itself.

Most slow-charging cases come down to a short list of suspects you can check yourself. The steps below start with quick physical checks and move toward software and firmware fixes, so you don't waste time reinstalling drivers when the problem was a frayed cable.

## Why this happens

- **Underpowered charger:** a 45W or 65W adapter on a laptop that expects 90W+ charges slowly, especially under load. USB-C docks often deliver less than the port's rating.
- **Damaged cable or port:** a worn USB-C cable, bent barrel connector, or dirty port reduces how much power reaches the battery.
- **Heavy load while charging:** gaming, rendering, or compiling eats most of the adapter's output, leaving little for the battery.
- **Battery health limiters:** features that cap charging (for example at 80%) or slow it to protect an aging battery.
- **Corrupted battery drivers:** the Microsoft ACPI battery drivers can misreport status after a Windows update, confusing the charge controller.
- **Outdated BIOS/EC firmware:** the embedded controller manages charging; old firmware may negotiate the wrong wattage over USB-C Power Delivery.
- **Overheating:** laptops deliberately slow charging when internal temperatures are high to protect the cells.

## How to fix it

Work through these in order, testing the charge rate after each one. A simple way to measure: note the battery percentage, wait 15 minutes with the lid open but idle, and check again.

### Fix 1: Verify your charger and cable match the laptop's requirements

Start with the hardware, because no software fix can compensate for a charger that can't deliver enough power.

1. Flip your laptop over or check the manual for the rated input, for example **19.5V / 4.62A (90W)**.
2. Read the fine print on your power brick and compare the wattage. If you're using a smaller spare adapter, that's likely the whole story.
3. Inspect the full length of the cable for kinks, fraying, or heat damage, and check the connector for bent pins or debris.
4. If you charge over USB-C, confirm the cable is rated for the wattage you need. Many cheap USB-C cables top out at 60W.
5. Plug the charger directly into a wall outlet instead of a power strip, dock, or hub, then recheck the charge speed.
6. Borrow or buy a charger that meets or exceeds the laptop's rating. For reference, see [how a 65W charger behaves on a gaming laptop](/articles/how-to-fix-65w-charger-not-enough-for-gaming-laptop-in-windows-11-24h2/).

### Fix 2: Reduce the load while charging

A laptop that is working hard simply has less spare power to send to the battery.

1. Close games, video editors, and other heavy apps, then watch the battery icon for a few minutes.
2. Press **Ctrl + Shift + Esc** to open **Task Manager**, click the **Processes** tab, and sort by **Power usage** to spot energy hogs.
3. End any unnecessary high-power tasks, especially background updaters, miners, or runaway browser tabs.
4. Lower the screen brightness to around 50% using **Settings > System > Display > Brightness**.
5. If you must keep working, switch to the **Best power efficiency** mode under **Settings > System > Power & battery > Power mode**.
6. Recheck after 15 minutes. If charging speeds up dramatically, your charger is fine but was losing the tug-of-war with your workload.

### Fix 3: Check manufacturer battery-health settings

Many laptops deliberately slow or cap charging to extend battery lifespan, and these settings sometimes get enabled by updates.

1. Open your manufacturer's battery utility: **Dell Power Manager**, **HP Battery Health Manager**, **Lenovo Vantage**, **MyASUS**, or **Acer Care Center**.
2. Look for charge-limit options such as "Primarily AC use", "Adaptive charging", or "Maximum lifespan mode".
3. If a limiter is active and you want full speed, set it to **Standard** or **Full charge mode**.
4. Check the BIOS/UEFI too: restart and press **F2**, **F10**, or **Del** during boot, then look under the **Power** or **Advanced** tab for battery charge settings.
5. Save with **F10**, boot back into Windows, and test charging again.
6. For a deeper look at your battery's condition, [generate a full battery report with powercfg](/articles/how-to-generate-battery-report-windows-11-powercfg/).

### Fix 4: Reinstall the battery drivers

Corrupted ACPI battery drivers are a classic cause of odd charging behavior after Windows updates.

1. Right-click **Start** and open **Device Manager**, then expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**, then confirm.
3. Do the same for **Microsoft AC Adapter**.
5. Shut the laptop down completely (not sleep, not hibernate). Unplug the charger and, if the battery is removable, take it out for 30 seconds.
6. Reconnect everything and power on. Windows will reinstall fresh copies of both drivers automatically.
7. Check whether the charge rate improves over the next 20 minutes.

### Fix 5: Update the BIOS and chipset drivers

The embedded controller firmware negotiates USB-C Power Delivery wattage, and bugs here directly affect charging speed.

1. Identify your exact model from **Settings > System > About**.
2. Visit the manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)) and download the latest **BIOS** and **chipset** drivers.
3. Close all programs, plug in the charger, and run the BIOS update. **Do not interrupt it**.
4. After rebooting, install the chipset drivers and restart once more.
5. On Intel-based laptops, the Intel Driver & Support Assistant can also catch related power-management driver updates.
6. Test charging again; BIOS release notes often mention USB-C charging fixes.

### Fix 6: Run the Windows power troubleshooter and reset the power plan

A misconfigured power plan can throttle the charge controller indirectly through aggressive thermal policies.

1. Open **Settings > System > Troubleshoot > Other troubleshooters** and run the **Power** troubleshooter.
2. Apply any recommended fixes and restart.
3. Open **Control Panel > Hardware and Sound > Power Options** and check your active plan.
4. Click **Change plan settings**, then **Restore default settings for this plan**.
5. If you use a manufacturer custom plan, switch temporarily to **Balanced** to compare charge rates.
6. Disable **Battery saver** while testing: set **Settings > System > Power & battery > Battery saver** to **Off** while plugged in.

### Fix 7: Calibrate the battery gauge

Sometimes the battery isn't actually charging slowly — the gauge is just wrong, making progress look slower than it is. A calibration pass gives you honest numbers.

1. Charge the laptop to 100% and leave it plugged in for two extra hours.
2. Unplug and use the laptop normally until it shuts itself down from low battery. Save your work as the percentage gets low.
3. Leave it off for at least five hours (overnight is ideal).
4. Plug in and charge uninterrupted back to 100%.
5. If you want the full procedure with report verification, follow [how to calibrate your laptop battery on Windows 11](/articles/how-to-calibrate-laptop-battery-windows-11/).
6. After calibration, repeat the 15-minute charge test. If the rate is still poor, the issue is real and not just a confused gauge.

### Fix 8: Check for overheating and blocked vents

Heat protection is one of the most overlooked causes of slow charging.

1. Feel the bottom of the laptop and listen to the fans while charging. Excessive heat triggers charge throttling.
2. Make sure vents aren't blocked by a bed, couch, or your lap. Use a hard, flat surface.
3. Open **Task Manager > Performance > CPU** and check temperatures if your OEM utility exposes them (many do via their support apps).
4. Clean dust from vents with short bursts of compressed air, holding the can upright.
5. If the laptop is several years old, the thermal paste or fan may need professional service.
6. Retest charging in a cool room. If speed returns to normal, heat was the limiter.

## Closing

Slow charging usually traces back to an undersized charger, a heavy workload, or a battery-health setting quietly doing its job. Work the list from the top and you'll either fix it or arrive at a confident diagnosis of what to replace.
