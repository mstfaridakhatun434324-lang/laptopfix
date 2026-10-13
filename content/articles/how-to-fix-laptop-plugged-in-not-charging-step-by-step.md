---
title: "Laptop Plugged In but Not Charging? Fix It Step by Step"
slug: how-to-fix-laptop-plugged-in-not-charging-step-by-step
date: 2026-09-15
categories: ["battery"]
tags: ["not charging", "plugged in", "charger", "ac adapter", "troubleshooting"]
description: "Your laptop says plugged in but the battery won't charge. Follow these ordered steps to find the cause and fix it fast."
thumbnail: "/images/thumbs/how-to-fix-laptop-plugged-in-not-charging-step-by-step.webp"
faqs:
  - q: "Why does my laptop say plugged in but not charging?"
    a: "The most common reasons are a failing AC adapter, a worn battery that can no longer accept charge, a charge limit set in manufacturer software, or a corrupted battery driver in Windows. Less often, the charging port is damaged or the BIOS needs updating. The steps in this guide isolate which one it is."
  - q: "How do I know if my charger or my battery is the problem?"
    a: "Test with a different compatible charger if you can. Also check Windows: if the laptop runs fine on AC power but the percentage never rises, the adapter is delivering power but the battery isn't accepting it. If the laptop dies the instant you unplug, the battery is likely dead. A battery report from powercfg /batteryreport shows the battery's real capacity."
  - q: "Can a Windows update cause the plugged in not charging error?"
    a: "Yes. Updates sometimes corrupt the Microsoft ACPI-Compliant Control Method Battery driver or reset power settings. Uninstalling that driver in Device Manager and rebooting so Windows reinstalls it fixes most update-related cases. BIOS updates from the manufacturer can also resolve charging firmware bugs."
  - q: "Should I keep using my laptop if it won't charge?"
    a: "You can use it on AC power, but back up your files first. A battery that won't charge can sometimes swell, so check whether the trackpad feels raised or the bottom case is bulging. If you see any swelling, stop using the battery immediately and have it replaced by the manufacturer or a qualified shop."
---

Few things are as annoying as plugging in your laptop, seeing the little plug icon appear, and then watching the battery percentage sit exactly where it was. "Plugged in, not charging" is one of the most common laptop complaints, and the fix ranges from a 30-second cable check to a battery replacement. The trick is testing things in the right order so you don't buy a new charger when the problem was a software setting.

This guide goes from the simplest checks to the deeper fixes. Work through them one by one — most people find the culprit within the first four steps.

## Why this happens

- **The adapter or cable is failing.** Frayed cables, loose barrel connectors, and dead power bricks are the number one cause.
- **You're using the wrong charger.** A 45W phone-style charger can't charge a laptop that needs 90W, and some laptops refuse third-party adapters outright.
- **A charge limit is enabled.** Lenovo Conservation Mode, ASUS Battery Health Charging, Dell's charge settings, and similar features intentionally stop charging at 60–80%.
- **The battery driver is corrupted.** Windows talks to the battery through a driver that updates love to break.
- **The battery is worn out.** After hundreds of cycles, some batteries simply can't accept a charge anymore.
- **The charging port is damaged.** A loose or bent DC jack breaks the connection intermittently.
- **BIOS or embedded controller bugs.** Charging is managed by firmware, and firmware has bugs that updates fix.

## How to fix it

Work through these in order — each step rules out one layer of the problem.

### Fix 1: Check the physical charging chain

Before touching software, rule out the obvious. A surprising number of "not charging" cases end here.

1. Unplug the adapter from both the wall and the laptop, then firmly reconnect both ends. Barrel connectors especially can feel seated when they aren't.
2. Plug directly into a wall outlet, not a power strip, surge protector, or extension cord.
3. Look at the adapter brick: is its LED on? Now look at the laptop's charging LED. Both should be lit.
4. Inspect the cable for frays, kinks, or a loose connector head, and sniff the brick for a burnt smell.
5. If your laptop charges over USB-C, try a different USB-C port — on many models only specific ports support charging.
6. Wiggle the connector gently while watching the charging LED. If it flickers, the port or plug is worn.

### Fix 2: Do a full power reset

This drains residual charge from the embedded controller, which manages charging, and clears confused hardware states.

1. Shut down the laptop completely.
2. Unplug the AC adapter.
3. If the battery is removable, take it out. If it's internal, skip this.
4. Hold the power button down for a full 30 seconds.
5. Reconnect the battery (if removed), plug in the adapter, and power on.
6. Check whether the battery icon now shows charging. If your machine has a pinhole EC reset button on the bottom panel, pressing it for 10 seconds with a paperclip accomplishes the same thing.

### Fix 3: Turn off charge limits in manufacturer software

Modern laptops ship with battery-longevity features that cap charging — and they often get turned on by accident during setup or updates.

1. **Lenovo:** Open Lenovo Vantage, go to **Device > Power**, and turn off **Conservation Mode**.
2. **ASUS:** Open MyASUS, go to **Battery Health Charging**, and set it to **Full capacity mode**.
3. **Dell:** Open Dell Power Manager, go to **Battery Settings**, and choose **Standard**.
4. **HP:** Open HP BIOS (press **F10** at boot), find **Power Management**, and disable any battery charge threshold.
5. **Microsoft Surface:** Check the Surface app for a battery limit setting.
6. After disabling, unplug and replug the adapter, then watch the percentage for five minutes. For a deeper look at these settings, see our guide on [limiting battery charge to 80 percent](/articles/how-to-limit-battery-charge-to-80/).

### Fix 4: Reinstall the battery driver in Windows

This is the classic fix for "plugged in, not charging" after a Windows update, and it takes two minutes.

1. Press **Win + X** and select **Device Manager**.
2. Expand the **Batteries** section.
3. Right-click **Microsoft AC Adapter** and choose **Uninstall device**.
4. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device** (do both entries if there are two).
5. Shut down — don't restart — then unplug the adapter for 30 seconds.
6. Plug back in, power on, and let Windows reinstall both drivers automatically.
7. Give it a few minutes and check the battery icon again.

### Fix 5: Check battery health with a battery report

If the driver reinstall didn't help, find out whether the battery itself is the problem before spending money.

1. Right-click the Start button and open **Terminal (Admin)**.
2. Type `powercfg /batteryreport` and press Enter.
3. Open the generated HTML file from the path it shows (usually your user folder).
4. Look at **Design Capacity** versus **Full Charge Capacity**. A battery at less than half its design capacity is heavily worn.
5. Scroll to the recent usage history — if capacity drops off a cliff at certain percentages, the cells are failing.
6. Our walkthrough on [checking battery health on Windows 11](/articles/how-to-check-battery-health-on-windows-11-laptop/) explains how to read every section of this report if you want more detail.

### Fix 6: Update the BIOS and chipset drivers

Charging behavior is controlled by firmware, and manufacturers regularly fix charging bugs in BIOS updates. This step is especially worth trying if the problem started after a Windows feature update.

1. Identify your exact model from the sticker on the bottom or via **Settings > System > About**.
2. Download the latest BIOS from your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Keep the adapter plugged in, close all programs, and run the updater without touching the machine.
4. While you're there, also install the latest chipset driver package.
5. After rebooting, check charging again. If Windows still shows the error, revisit Fix 4 — a driver that didn't reinstall cleanly is the most common reason this step appears to fail.

### Fix 7: Test with a known-good charger

By now you've ruled out settings, drivers, and firmware. Time to test the hardware.

1. Borrow a charger with the same connector and equal or higher wattage, ideally the original manufacturer's.
2. If the laptop charges with the borrowed adapter, yours is dead — replace it with the correct wattage for your model (check the label on the original brick).
3. If it still won't charge, try your adapter on another compatible laptop if possible.
4. For USB-C laptops, make sure any replacement supports USB Power Delivery at your laptop's required wattage — a 65W brick won't properly charge a 130W machine.

### Fix 8: Replace the battery

If a good charger, fresh drivers, updated BIOS, and no charge limits still leave you at "plugged in, not charging," the battery has reached the end of its life.

1. Confirm with the battery report from Fix 5 — very low full charge capacity seals the diagnosis.
2. Check for swelling: a raised trackpad, a case that won't sit flat, or a creaking bottom panel are warning signs. Handle a swollen battery carefully and don't puncture it.
3. Order a genuine replacement battery for your exact model — third-party batteries are a gamble on safety and longevity.
4. On models with internal batteries, a repair shop can usually swap it in under an hour if you're not comfortable opening the machine.

## Closing

"Plugged in, not charging" looks scary but is usually a cable, a charge limit, or a driver — all fixable without spending money. Only after the physical checks, driver reinstall, and battery report point at the battery itself should you reach for your wallet.
