---
title: "How to Fix a Laptop That Says 'Plugged In, Not Charging'"
slug: how-to-fix-laptop-plugged-in-not-charging
date: 2026-09-07
categories: ["battery"]
tags: ["not charging", "ac adapter", "battery driver"]
description: "Your laptop is plugged in but the battery won't charge? This is one of the most common Windows 11 issues — and most fixes take under ten minutes."
thumbnail: "/images/thumbs/how-to-fix-laptop-plugged-in-not-charging.webp"
faqs:
  - q: "Why does my laptop say 'plugged in, not charging'?"
    a: "Windows is receiving power from the adapter but has decided not to send it to the battery. The usual reasons are a charge limit set in your manufacturer's app, a confused battery driver, an underpowered or failing adapter, or a battery that needs recalibration."
  - q: "Is 'plugged in, not charging' bad for the battery?"
    a: "Usually not — in many cases it's actually protecting the battery, such as when a charge limit is active. It becomes a problem only if the battery keeps draining while plugged in, or if you need a full charge for travel and can't get one."
  - q: "Will reinstalling the battery driver delete anything?"
    a: "No. Uninstalling the Microsoft ACPI-Compliant Control Method Battery driver only removes the software interface. Windows reinstalls it automatically on the next boot. Your files, settings, and programs are untouched."
  - q: "How do I know if the charger itself is the problem?"
    a: "Try a known-good charger of the correct wattage. Also inspect the cable and connector for damage, and try a different wall outlet. If the laptop charges fine with another adapter, yours is failing — adapters die more often than batteries do."
---
Few messages are more annoying than plugging in your laptop, seeing the little plug icon appear, and then reading the words "plugged in, not charging." The laptop is clearly getting power. The battery is clearly not empty. And Windows has simply decided the two shall not meet.

The good news: this message is usually a decision Windows is making, not a hardware failure. A charge limit, a glitchy driver, or a tired adapter accounts for the vast majority of cases. Work through the fixes below and you'll find out which one it is within minutes.

## Why this happens

- **A battery charge limit is active.** Lenovo's Conservation Mode, ASUS Battery Health Charging, Dell's charge settings, or HP's Battery Health Manager can cap charging at 60–80%. When the battery sits at or above the cap, Windows reports "plugged in, not charging" — which is exactly what the limit is supposed to do.
- **The battery driver is confused.** The Microsoft ACPI-Compliant Control Method Battery driver sometimes gets stuck in a wrong state after updates, sleep cycles, or driver changes, and stops passing charge commands through.
- **The adapter is underpowered or failing.** A 45W adapter on a laptop that wants 65W, a frayed cable, or a dying power brick can deliver enough power to run the laptop but not enough to charge the battery at the same time.
- **The battery needs recalibration.** When the charge gauge drifts, Windows may think the battery is fuller than it is and refuse to charge. One full calibration cycle usually resets it.
- **Overheating protection kicked in.** Many laptops pause charging when the battery gets hot, to protect the cells. If the machine is roasting, charging waits until it cools. See [what to do about an overheating battery](/articles/how-to-fix-laptop-overheating-while-charging-in-windows-11-24h2/) if heat is a regular visitor.
- **The battery is genuinely worn out.** A battery with very high wear may refuse charge because its controller considers it unsafe. A quick [battery health check](/articles/how-to-check-battery-health-on-windows-11-laptop/) tells you where yours stands.

## How to fix it

Work through these in order. Start with the charge-limit check — it's the cause more often than people expect.

### Fix 1: Check for an active charge limit first

This takes thirty seconds and solves the mystery for a huge number of people.

1. Open your manufacturer's utility: **Lenovo Vantage**, **MyASUS**, **MyDell / Dell Power Manager**, **HP Support Assistant**, **Acer Care Center**, or **MSI Center**.
2. Look for a battery section with names like **Conservation Mode**, **Battery Health Charging**, **Battery Health Manager**, or **Charging limit**.
3. If a limit is enabled (commonly 60%, 80%, or a "maximum lifespan" mode), that is your answer. Either disable it to charge fully, or leave it on — it's protecting your battery. Our guide to [limiting charge to 80 percent](/articles/how-to-limit-battery-charge-to-80/) explains the trade-off.
4. No manufacturer app installed? Check the BIOS/UEFI setup at boot for a battery charge threshold setting — some vendors put it there instead.

### Fix 2: Rule out the adapter and outlet

A surprising number of "not charging" cases are just a bad brick.

1. Unplug the adapter from both the wall and the laptop. Inspect the cable along its full length for kinks, fraying, or a loose connector barrel.
2. Plug the adapter directly into a wall outlet, not a power strip or extension cord, and try a different outlet.
3. Smell the brick (seriously) — a burnt-plastic smell means it's dying. Feel it too: stone cold while plugged in is suspicious; a working adapter gets slightly warm.
4. If you can borrow an adapter with the same connector and equal or higher wattage, test with it. If charging resumes, replace your adapter with the correct wattage for your model.

### Fix 3: Reinstall the battery driver

This is the classic fix for a reason — it works.

1. Press **Windows key + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**. Confirm if asked.
3. Shut the laptop down completely (**Start > Power > Shut down**) — don't restart, do a full shutdown.
4. Unplug the charger, wait 30 seconds, plug it back in, and power on. Windows reinstalls the driver during boot.
5. Check the battery icon. If it now says "charging," you're done.

### Fix 4: Reset the power state with a hard reset

This clears stuck charge-controller states that survive normal reboots.

1. Shut down the laptop and unplug everything, including USB devices and the charger.
2. If the battery is removable, take it out. If it's internal, skip this — the next step still helps.
3. Press and hold the power button for a full 20 seconds. This drains residual charge from the capacitors and resets the embedded controller.
4. Reinsert the battery (if removed), plug in the charger, wait a minute, then power on and check the charge status.

### Fix 5: Run one full calibration cycle

If the gauge is lying about the charge level, Windows makes bad charging decisions.

1. Charge to whatever maximum the laptop allows and keep it plugged in for two hours past that.
2. Unplug and use the laptop until it shuts itself off. Save work before the battery gets critical.
3. Leave it off and unplugged for two hours.
4. Charge it uninterrupted back to full, then boot and check the status. The step-by-step version lives in our [battery calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 6: Update the BIOS and chipset drivers

The embedded controller firmware manages charging, and old firmware has bugs.

1. Check your BIOS version with `msinfo32` (press **Windows key + R**, type `msinfo32`, look at **BIOS Version/Date**).
2. Visit your manufacturer's support page and compare. [Lenovo](https://support.lenovo.com/us/en/), [Dell](https://www.dell.com/support), and [HP](https://support.hp.com/us-en) all list BIOS updates by model.
3. Install any newer BIOS with the charger connected and battery above 50%. Also grab the latest chipset driver while you're there.
4. Reboot and check whether charging resumes.

### Fix 7: Check battery health and consider replacement

If nothing above helped, get the numbers.

1. Open **Terminal (Admin)** and run: `powercfg /batteryreport /output "C:\battery-report.html"`.
2. Open the report and compare **FULL CHARGE CAPACITY** to **DESIGN CAPACITY**. Below 60–70% of design, the controller may refuse charging as a safety measure.
3. If wear is extreme and the laptop is otherwise fine, a replacement battery (genuine, from the manufacturer or a reputable seller) is the fix. If the laptop is under warranty, contact support before buying anything — a battery that won't charge is a valid warranty claim.

## Closing

"Plugged in, not charging" is Windows telling you it has a reason — usually a charge limit you forgot about, a driver that needs a reset, or an adapter that's quietly dying. Check the limit first, test the brick second, reinstall the driver third, and you'll resolve the overwhelming majority of cases without spending a cent.
