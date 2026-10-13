---
title: "How to Fix a Laptop Battery That Won't Charge After a BIOS Update (Windows 11)"
slug: how-to-fix-battery-not-charging-after-bios-update-on-windows-11
date: 2026-10-10
categories: ["battery"]
tags: ["battery not charging", "bios update", "windows 11"]
description: "BIOS update killed your laptop charging? Learn why it happens and the exact steps to get your Windows 11 battery charging again."
thumbnail: "/images/thumbs/how-to-fix-battery-not-charging-after-bios-update-on-windows-11.webp"
faqs:
  - q: "Why did my battery stop charging right after a BIOS update?"
    a: "A BIOS update rewrites the embedded controller firmware that manages charging. It can reset charge thresholds, knock the battery gauge out of calibration, or leave the ACPI battery driver in a mismatched state, so Windows thinks charging is disabled when it isn't."
  - q: "Will reinstalling the battery driver fix charging after a BIOS update?"
    a: "Often, yes. Open Device Manager, expand Batteries, uninstall Microsoft ACPI-Compliant Control Method Battery, then restart so Windows reinstalls it. This clears stale state from the old firmware and usually restores normal charging within minutes."
  - q: "Should I roll back the BIOS to fix the charging issue?"
    a: "Only as a last resort. Most cases are fixed by resetting the embedded controller, reinstalling the battery driver, or turning off a charge limit the update enabled. Roll back the BIOS only if the manufacturer supports it and nothing else works."
  - q: "How long should I wait before assuming the battery is dead?"
    a: "Work through all the software fixes first, including an EC reset and a full calibration cycle. If the battery still won't charge after those steps and a known-good charger, then suspect hardware failure and contact the manufacturer's support."
---
You ran a BIOS update — maybe Windows Update pushed it, maybe you opened your manufacturer's update tool — and the moment the laptop rebooted, the battery icon read "plugged in, not charging." Nothing else changed. Same charger, same outlet, same laptop. It's maddening, but this pattern is extremely common, and it almost always has a software-side cause.

The BIOS doesn't just start your computer. It also contains the firmware for the embedded controller (EC), the chip that actually manages charging. When a BIOS update rewrites that firmware, it can reset charge limits, confuse the battery gauge, or leave Windows' battery driver talking to firmware it no longer understands. The good news: every one of those problems is fixable, and you don't need to open the laptop.

## Why this happens

- **Charge thresholds got reset.** Many BIOS updates re-enable conservative charging modes (like stopping at 60% or 80%) that you had turned off, so the battery looks "stuck."
- **The battery gauge lost calibration.** The EC tracks charge with a fuel gauge that can lose its reference point during a firmware flash, causing false "not charging" readings.
- **The ACPI battery driver is stale.** Windows keeps driver state from the old firmware; after the update, the Microsoft ACPI-Compliant Control Method Battery driver can report charging incorrectly.
- **USB-C charging port assignments changed.** Some updates change which port accepts power delivery, especially on laptops with two USB-C ports.
- **The EC got stuck mid-update.** If the update process was interrupted or finished oddly, the embedded controller can freeze in a no-charge state.
- **Battery firmware updated too.** Some BIOS packages bundle battery firmware updates that change reported capacity or behavior.
- **Power settings were reset to defaults.** A BIOS reset can change power-related firmware settings that Windows reads at boot.

## How to fix it

Work through these in order, testing whether the battery charges after each step.

### Fix 1: Confirm what Windows actually sees

Before changing anything, get an accurate picture. Open **Settings > System > Power & battery** and look at the battery status line. If it says "Plugged in, not charging" but the percentage is slowly rising, the gauge is misreporting, not the hardware failing. For a deeper look, generate a report: open an elevated Command Prompt and run:

```
powercfg /batteryreport /output %USERPROFILE%\Desktop\battery-report.html
```

Open the HTML file and check the recent usage table — it shows charge rate in mW, which tells you whether power is actually flowing. If you want a full walkthrough of reading this report, see [how to generate a battery report with powercfg](/articles/how-to-generate-battery-report-windows-11-powercfg/). If the report shows zero charge rate, continue to the next fix.

### Fix 2: Reset the embedded controller

This is the single most effective fix for post-BIOS-update charging problems. A hard reset forces the EC to reinitialize with the new firmware.

1. Shut the laptop down completely — not sleep, not hibernate. Hold **Shift** while clicking **Shut down** to bypass Fast Startup.
2. Unplug the charger and remove any USB-C docks, hubs, or peripherals.
3. Press and hold the power button for a full 30–60 seconds. (Some manufacturers, like HP and Lenovo, document this exact procedure for EC resets.)
4. Release the button, wait 10 seconds, then plug the charger back in and power on.

Give it five minutes at the lock screen. Many users report charging resumes right after this step. The [official Windows power guidance](https://support.microsoft.com/en-us/windows) also recommends starting with hardware-level resets before changing drivers.

### Fix 3: Reinstall the ACPI battery driver

If the EC reset didn't help, the driver layer is the next suspect.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. You'll typically see **Microsoft AC Adapter** and **Microsoft ACPI-Compliant Control Method Battery**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. Check the box to delete the driver software if offered.
4. Do the same for **Microsoft AC Adapter**.
5. Click **Action > Scan for hardware changes**, or simply restart the laptop.

On restart, Windows reinstalls both drivers fresh against the new firmware. Plug the charger in after the desktop loads and watch the icon for a few minutes. This step resolves the majority of remaining cases.

### Fix 4: Check for a re-enabled charge limit

BIOS updates love to turn charge-limiting features back on. What to check depends on your brand:

- **Lenovo:** Open **Lenovo Vantage > Device > Power** and turn off **Battery Conservation Mode** (limits charge to 60%).
- **Dell:** Open **Dell Power Manager > Battery Settings** and switch from **Primarily AC Use** to **Standard**.
- **ASUS:** Open **MyASUS > Battery Health Charging** and set it back to **Full capacity mode**.
- **HP:** Reboot into BIOS (tap **F10** during startup), go to **Advanced > Power Management Options**, and check the **Battery Health Manager** setting — set it to **Let HP manage my charging**.
- **Acer:** Open **Acer Care Center** and check the battery charge limit.

Also check the BIOS itself for a "Battery Charge Threshold" or "Adaptive Battery Optimizer" entry and set it to allow full charging. If you're not sure your battery is actually healthy versus just limited, run through [how to check battery health on a Windows 11 laptop](/articles/how-to-check-battery-health-on-windows-11-laptop/) before deciding the battery is bad.

### Fix 5: Recalibrate the battery gauge

If the battery charges but the percentage jumps around or stalls, the fuel gauge needs recalibration.

1. Charge the laptop to 100% and leave it plugged in for two hours.
2. Unplug and use the laptop normally until it shuts itself down at 0% (save your work — disable sleep at low battery first under **Settings > System > Power & battery**).
3. Leave it off and unplugged for 3–5 hours so the cells settle.
4. Plug in and charge uninterrupted to 100%.

This full cycle teaches the EC the true empty and full points. Don't do this often — one calibration every few months is plenty — but after a BIOS update it's exactly the right move.

### Fix 6: Update the chipset and power management drivers

Sometimes the BIOS update expects newer companion drivers than Windows has installed.

1. Visit your manufacturer's support site (Dell, HP, Lenovo, ASUS, or Acer) and download the latest **chipset**, **Intel Management Engine**, and **power management** drivers for your exact model.
2. Install them, restarting when prompted.
3. Alternatively, run the manufacturer's updater tool (Dell SupportAssist, Lenovo Vantage, HP Support Assistant, MyASUS) and apply everything marked critical.

Intel users can also run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch chipset driver updates Windows missed.

### Fix 7: Reflash or roll back the BIOS (last resort)

If nothing above worked, the firmware flash itself may be incomplete or buggy.

1. Download the BIOS version you were running before the update (or the newest version if the manufacturer has since released a fix) from the manufacturer's support site.
2. Follow the manufacturer's flashing instructions exactly — keep the charger plugged in and do not touch the laptop during the flash.
3. After flashing, repeat Fix 2 (EC reset) before judging the result.

Some manufacturers allow BIOS rollback only from a USB recovery method; check your model's manual. If the battery still refuses to charge after a clean reflash, you've ruled out software — contact support, because the battery or charging circuit may genuinely have failed.

## Closing

A battery that stops charging right after a BIOS update is almost never a dead battery — it's a confused controller, a stale driver, or a charge limit the update switched back on. Start with the EC reset, reinstall the battery drivers, and check your manufacturer's charging modes. Nine times out of ten, one of those three brings charging back within the hour.
