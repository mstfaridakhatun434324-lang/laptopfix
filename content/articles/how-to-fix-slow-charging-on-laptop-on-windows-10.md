---
title: "How to Fix Slow Charging on a Laptop on Windows 10"
slug: how-to-fix-slow-charging-on-laptop-on-windows-10
date: 2026-09-04
categories: ["battery"]
tags: ["slow charging", "windows 10", "battery", "charger", "usb-c"]
description: "Laptop charging at a crawl on Windows 10? These are the real causes of slow charging and eight proven fixes, from charger wattage to BIOS settings."
thumbnail: "/images/thumbs/how-to-fix-slow-charging-on-laptop-on-windows-10.webp"
faqs:
  - q: "Why does my laptop say 'plugged in' but charge very slowly?"
    a: "The most common reason is an underpowered charger or cable. A 45W adapter on a laptop that expects 65W or 90W will trickle-charge at best, and heavy CPU or GPU load can eat most of that power before it reaches the battery. Dirty contacts, a failing battery, and BIOS charge-limiting features are the next things to check."
  - q: "Can a USB-C cable cause slow charging?"
    a: "Yes, and it happens constantly. Many USB-C cables only carry 60W or even 15W, and some cheap cables carry no Power Delivery negotiation at all, so the laptop falls back to a slow 5V charge. Use the cable that came with the laptop or one explicitly rated for 100W USB-C PD, and plug into the port marked with a charging or lightning icon."
  - q: "Does Windows 10 have a setting that slows charging?"
    a: "Windows 10 itself does not throttle charge speed, but manufacturer utilities do. Dell's ExpressCharge settings, Lenovo Vantage conservation mode, ASUS Battery Health Charging, and HP's Battery Health Manager can all cap charging at 50 to 80 percent or slow it down. Check those tools before assuming the hardware is at fault."
  - q: "How long should a laptop take to charge normally?"
    a: "Most modern laptops reach 80 percent in 60 to 90 minutes with the correct charger and reach full in about two hours. If yours gains less than 10 percent in an hour with the original adapter and the machine idle, something is wrong, and the fixes below will help you find it."
---
You plug in your laptop, the little charging light comes on, and Windows 10 happily reports "plugged in." An hour later the battery has crawled from 30 percent to 41. Nothing is technically broken, yet the machine charges so slowly it is practically decorative. I see this constantly, and the cause is almost always simpler than people expect.

Slow charging is a negotiation problem. The charger, the cable, the port, the battery controller, and Windows all have to agree on how much power flows. When any one of them backs out, charging drops to a trickle. Work through the checks below in order and you will find the weak link.

## Why this happens

- **Underpowered charger.** A 45W brick on a 65W or 90W laptop charges slowly, especially under load. Universal chargers and phone chargers are the classic culprits.
- **Weak USB-C cable.** Many USB-C cables top out at 60W or lack Power Delivery entirely, so the laptop charges at a fraction of its rated speed.
- **Wrong port.** Some laptops only fast-charge through one specific USB-C port. The others accept a slow 5V trickle.
- **Heavy load while charging.** Gaming, video rendering, or a runaway background process can consume nearly everything the adapter delivers, leaving crumbs for the battery.
- **Dirty or worn contacts.** Lint in the port and oxidized pins add resistance, which the charging circuit answers by lowering current.
- **Manufacturer charge limits.** Tools like Dell Power Manager, Lenovo Vantage, or ASUS Battery Health Charging may be capping the charge rate or the maximum level without you realizing it.
- **Aging battery.** A worn battery with high internal resistance accepts charge more slowly, and the controller throttles current to keep it safe.

## How to fix it

Work through these in order, testing the charge rate after each change so you know which one did the job.

### Fix 1: Match the charger to the laptop's rated wattage

1. Flip the laptop over and read the rating plate, or check the original adapter's label for its wattage (65W, 90W, 130W, and so on).
2. Compare it with the adapter you are using now. If the numbers do not match, borrow or buy the correct wattage.
3. Prefer the manufacturer's own adapter. Third-party bricks are fine only if they are a reputable brand and match or exceed the rated wattage.
4. If you use a dock or hub, plug the charger directly into the laptop once to rule the dock out. If you want a [full battery health check](/articles/how-to-check-battery-health-on-windows-11-laptop/) afterward, the steps carry over to Windows 10 too.

### Fix 2: Use the right cable and the right port

1. On USB-C laptops, use a cable explicitly rated for 100W USB-C Power Delivery. Phone cables and bargain cables are the usual suspects.
2. Plug into the port marked with a battery, plug, or lightning icon. On many machines only one USB-C port supports full-speed charging.
3. On the charging screen in Windows, click the battery icon and confirm it says "plugged in, charging" rather than just "plugged in."
4. If the laptop has a barrel-jack adapter as well, test with that. If the barrel jack charges fast and USB-C does not, the cable or port is your problem.

### Fix 3: Clean the charging port and connector

1. Unplug everything and power the laptop off completely.
2. Shine a light into the charging port and look for lint, dust, or bent pins.
3. Use a wooden toothpick or a blast of compressed air to clear debris. Never use metal tools inside the port.
4. Wipe the charger's connector with a dry cloth. If you see green or dark oxidation, a pencil eraser rubbed gently over the contacts cleans it well.
5. Reconnect firmly and check whether the charge rate improves within ten minutes.

### Fix 4: Cut the power drain while charging

1. Press **Ctrl + Shift + Esc** to open **Task Manager**, then click the **Processes** tab and sort by **CPU**.
2. End any runaway task you recognize (a stuck updater, a browser tab eating 40 percent CPU). Leave system processes alone.
3. Close games, video editors, and anything using the discrete GPU while you charge.
4. Open **Settings > System > Battery** and turn on **Battery saver** temporarily if you need the machine usable while it charges.
5. Give it 30 minutes and compare the percentage gained. If the rate jumps, the charger was fine all along and the load was the thief. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) explain how power plans affect drain if you want to dig deeper.

### Fix 5: Check manufacturer battery utilities for charge limits

1. Open the tool your brand ships: Dell Power Manager, Lenovo Vantage, HP Support Assistant, ASUS MyASUS, or Acer Care Center.
2. Look for battery settings with names like ExpressCharge, Conservation Mode, Battery Health Charging, or Maximum Lifespan Mode.
3. If a limit is active (for example, capped at 80 percent or set to a slow overnight profile), switch it to **Standard** or **Adaptive** and test again.
4. Note that some of these modes intentionally slow charging to protect the battery. That is by design, not a fault, so only change it if slow charging actually bothers you.

### Fix 6: Update the BIOS and embedded controller firmware

1. The battery charging circuit is managed by firmware, and manufacturers regularly fix charging bugs in BIOS updates.
2. Go to your manufacturer's support site, for example [Dell Support](https://www.dell.com/support), enter your service tag, and download the latest BIOS.
3. Run the update with the charger plugged in and the battery above 20 percent. Do not interrupt it.
4. After the update, check the BIOS battery settings for options like "Primarily AC Use" or adaptive charging and set them to your preference.

### Fix 7: Reset the battery gauge with a calibration cycle

1. A miscalibrated fuel gauge can make charging look slower than it is, because the reported percentage lags reality.
2. Charge to 100 percent, then unplug and use the laptop normally until it shuts itself down at critical battery.
3. Leave it off for an hour, then charge uninterrupted back to 100 percent without using it.
4. Repeat once more if the gauge still looks jumpy. For a deeper dive, [generate a battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/) with `powercfg /batteryreport` and compare design capacity against full charge capacity.

### Fix 8: Test the battery's actual health

1. Press **Win + R**, type `cmd`, and press **Ctrl + Shift + Enter** to open an elevated Command Prompt.
2. Run `powercfg /batteryreport` and open the generated HTML file from the path it prints.
3. Compare **Design Capacity** with **Full Charge Capacity**. If full charge capacity is under 60 percent of design, the battery is worn and will charge slowly no matter what you do.
4. At that point, a replacement battery is the honest fix. Check the manufacturer's parts store or a reputable third-party seller with the exact model number.

## Closing

Nine times out of ten, slow charging on Windows 10 comes down to the charger, the cable, or a manufacturer utility quietly limiting things. Start with the adapter and port, clear the load, then look at firmware and battery health. One of those steps will crack it, and your laptop will be back to charging like it should.
