---
title: "Laptop Battery Not Charging? 7 Fixes That Actually Work"
slug: best-way-to-fix-laptop-battery-not-charging
date: 2026-10-11
categories: ["battery"]
tags: ["battery not charging", "windows 11", "troubleshooting"]
description: "Battery plugged in but not charging? Work through these seven proven fixes, from charger checks to driver resets, to get your laptop charging again."
thumbnail: "/images/thumbs/best-way-to-fix-laptop-battery-not-charging.webp"
faqs:
  - q: "Why does my laptop say plugged in but not charging?"
    a: "The most common causes are a worn or miscalibrated battery, a weak or faulty charger, a charging limit set in your manufacturer's app, or a corrupted ACPI battery driver in Windows. Work through charger checks first, then driver resets, since those two account for the majority of cases."
  - q: "Can a driver update cause the battery to stop charging?"
    a: "Yes. Windows or BIOS updates can corrupt the Microsoft ACPI-Compliant Control Method Battery driver or reset power settings. If charging stopped right after an update, uninstalling the ACPI battery drivers in Device Manager and restarting usually restores charging, since Windows reinstalls clean copies on boot."
  - q: "Should I buy a new battery or a new charger first?"
    a: "Always test the charger first. Borrow a known-good charger with the same wattage and connector, or check your current one's output with a USB-C power meter. Chargers fail far more often than batteries do, and a new battery will not fix a charger or cable problem."
  - q: "How long does it take for a fix to start working?"
    a: "Most software fixes take effect immediately after a restart. If you reset the ACPI drivers or change a charging threshold, you should see the charging status change within a minute of rebooting. If nothing changes after trying all software fixes, the fault is almost certainly hardware."
---

A laptop that refuses to charge is one of the most stressful hardware problems you can hit. One minute everything is fine, the next you are staring at "plugged in, not charging" and watching the percentage slide toward zero. The good news is that most cases are fixable at home without spending money.

There is a best way to approach this, and it is to rule things out in order: the charger, the charge limit setting, the driver, and only then the battery itself. Skip around and you will waste time replacing the wrong part. Follow the order below and you will land on the real cause fast.

## Why this happens

- **Weak or failing charger:** A damaged cable, loose barrel connector, or underpowered adapter cannot deliver enough watts, so Windows holds the battery at its current level instead of charging it.
- **Charge limit enabled:** Many manufacturers cap charging at 80 percent (ASUS Battery Health Charging, Lenovo Conservation Mode, Dell battery settings). The battery stops at the cap and Windows reports it as "not charging."
- **Corrupted ACPI battery driver:** The Microsoft ACPI-Compliant Control Method Battery driver is what lets Windows talk to the battery. If it corrupts after an update, Windows loses the ability to manage charging.
- **Battery wear or calibration drift:** An old battery whose reported capacity is wrong can confuse the charging controller. This often shows up after a full battery report like [checking your battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) reveals high wear.
- **Overheating or power delivery fault:** If the charging circuitry gets too hot or the DC jack is damaged, the laptop protects itself by refusing charge.
- **BIOS or firmware bug:** A buggy BIOS update can break battery communication. If charging died right after a BIOS update, the firmware is the prime suspect — see [battery not charging after a BIOS update](/articles/battery-not-charging-after-bios-update-troubleshooting/).

## How to fix it

Work through these in order, from quickest to most involved. Stop at the step that solves it.

### Fix 1: Inspect the charger and cable

A huge share of "not charging" cases are just a tired adapter. Look closely before you touch software.

1. Unplug the charger from the laptop and the wall, then check the full length of the cable for kinks, fraying, or heat damage.
2. Smell the adapter brick. A burnt-plastic smell means it is dead — replace it.
3. Confirm the adapter wattage on its label matches what your laptop needs. A 45W adapter on a laptop that wants 90W will often show "plugged in, not charging."
4. Try a different wall outlet, skipping any power strip or extension cord.
5. If you use USB-C charging, flip the cable, try another port on the laptop, and test with a different USB-C cable rated for your wattage.

### Fix 2: Turn off any charge limit in the manufacturer's app

Before going deeper, make sure the laptop is not simply obeying a limit you forgot about.

1. Open your manufacturer's power app: **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, or **HP Smart**.
2. Look for battery settings named Conservation Mode, Battery Health Charging, Battery Care Function, or an 80 percent cap.
3. Set the limit to **Full capacity / 100 percent** or turn the conservation feature off.
4. Some models need this change in the BIOS instead: restart, press **F2** (Dell), **F1**/**F2** (Lenovo), or **F2**/**Del** (ASUS) to enter BIOS, and check the battery configuration page.
5. Save, exit, and check whether charging resumes within a minute.

If your cap is stuck and will not switch off, you may be dealing with [a battery limiter that is not working](/articles/battery-limiter-not-working-troubleshooting/).

### Fix 3: Run the Windows power troubleshooter

Windows 11 still ships a power troubleshooter that catches misconfigured power plans.

1. Open **Settings** with **Win + I**, then go to **System > Troubleshoot > Other troubleshooters**.
2. Find **Power** and click **Run**.
3. Apply any fixes it suggests, then restart the laptop.
4. If it reports nothing, continue — this step only takes a minute and rules out plan corruption.

### Fix 4: Reset the ACPI battery drivers

This is the classic fix and resolves a surprising number of cases, especially after Windows updates.

1. Shut down the laptop, unplug the charger, and if the battery is removable, take it out for 30 seconds.
2. Press and hold the power button for **15 seconds** to drain residual power, then reconnect everything and boot up.
3. Press **Win + X** and open **Device Manager**.
4. Expand **Batteries**, right-click each **Microsoft ACPI-Compliant Control Method Battery** entry, and choose **Uninstall device**.
5. Do the same for **Microsoft AC Adapter** if it appears.
6. Restart the laptop. Windows reinstalls the drivers automatically on boot.
7. Plug in the charger and watch the battery icon for two minutes.

This procedure is covered in more depth in the guide on [resetting the ACPI battery driver](/articles/how-to-reset-acpi-battery-driver-on-laptop/).

### Fix 5: Check the battery report for wear

If the drivers are fine, find out whether the battery itself is the problem.

1. Press **Win + X**, open **Terminal (Admin)**, and run `powercfg /batteryreport /output "C:\battery-report.html"`.
2. Open the file in your browser and compare **Design Capacity** to **Full Charge Capacity**.
3. If full charge capacity is under 50 percent of design capacity, the battery is worn out and no software fix will bring it back.
4. Also check the recent usage section for sudden drops, which point to failing cells.

For help reading the numbers, see [battery design capacity vs full charge capacity](/articles/best-way-to-check-battery-design-vs-full-charge-capacity/). If the battery is healthy on paper, a full [battery calibration](/articles/how-to-calibrate-laptop-battery-windows-11/) can fix a confused fuel gauge.

### Fix 6: Update the BIOS and chipset drivers

A BIOS update from the manufacturer often includes fixes for battery communication.

1. Go to your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and enter your exact model.
2. Download the latest **BIOS** and **chipset** updates, nothing else.
3. Close all apps, keep the charger plugged in, and run the BIOS update. Do not interrupt it.
4. After the laptop restarts, check the battery status again.

Only download firmware from the manufacturer's own site. Random driver updater tools are a common way to make battery problems worse.

### Fix 7: Test with a known-good charger, then replace the battery

By this point you have ruled out software. Time for hardware elimination.

1. Borrow a charger of equal or higher wattage with the same connector and test for 15 minutes.
2. If the borrowed charger works, buy a replacement adapter — the original is the fault. If your laptop is a gaming model, make sure the wattage is sufficient, since [an underpowered charger can cause charging weirdness](/articles/best-way-to-fix-65w-charger-not-enough-for-gaming-laptop/).
3. If no charger helps and the battery report shows heavy wear, replace the battery with a genuine or manufacturer-approved part.
4. If a brand-new battery still will not charge, the charging circuit or DC jack on the motherboard is faulty — that is a repair-shop job.

## Closing

Nine times out of ten, a laptop battery that will not charge comes down to the charger, a charge limit setting, or the ACPI driver — all fixable in under half an hour. Only when all three check out should you spend money on a new battery, and by then you will know exactly what to buy.
