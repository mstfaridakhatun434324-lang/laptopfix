---
title: "Battery Charge Limiter Not Working in Windows 11 24H2? Fix It"
slug: how-to-fix-battery-limiter-not-working-in-windows-11-24h2
date: 2026-10-01
categories: ["battery"]
tags: ["battery limiter", "charge limit", "windows 11 24h2"]
description: "Set a battery charge limit but the laptop still charges to 100%? Fix broken battery limiters on Windows 11 24H2 with these 7 steps."
thumbnail: "/images/thumbs/how-to-fix-battery-limiter-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my battery charge limit not working after the 24H2 update?"
    a: "The 24H2 update can break the link between manufacturer battery tools and the firmware that enforces the limit. Outdated manufacturer apps, old BIOS versions, and corrupted ACPI drivers are the usual causes. Updating the manufacturer's app and the BIOS fixes it in most cases."
  - q: "Where do I set a battery charge limit on Windows 11?"
    a: "Windows 11 has no built-in charge limiter — it's handled by manufacturer tools: Lenovo Vantage (Conservation Mode), Dell Power Manager or Dell Optimizer, MyASUS (Battery Health Charging), Acer Care Center (Battery Charge Limit), HP BIOS (Battery Health Manager), or the Surface app (Smart Charging)."
  - q: "Does the charge limit work if the manufacturer's app is closed?"
    a: "Yes, once set, the limit is enforced by firmware, not the app — the app is just the switch. But if the firmware or the driver the app talks to is broken after an update, the setting won't apply. That's why BIOS and driver updates matter even though the limit itself lives in firmware."
  - q: "My laptop charges past the limit only sometimes. Why?"
    a: "Some limiters behave adaptively: Dell's Adaptive mode and Lenovo's Conservation Mode can allow occasional full charges for calibration. Also, some tools pause the limit temporarily after a BIOS update or EC reset. If it consistently ignores the limit, though, the enforcement chain is broken — work through the fixes below."
---

You set the charge limit to 80% to protect your battery, and the laptop cheerfully charges straight past it to 100%. Or the toggle in the manufacturer's app does nothing at all. Or the limit worked for months and broke the week you installed Windows 11 24H2. A charge limiter that doesn't limit is worse than useless — it gives you false confidence while the battery soaks at full voltage.

Here's the thing most guides skip: the limiter is a chain with three links — the manufacturer's app, a Windows driver, and the firmware (BIOS/EC) that actually enforces the cap. The 24H2 update is good at breaking the middle link. Fix the chain link by link, starting with the easiest.

## Why this happens

- **Outdated manufacturer app** — the battery tool predates 24H2 and can't communicate with the new OS properly.
- **Old BIOS firmware** — the firmware that enforces the limit may need an update for 24H2 compatibility.
- **Corrupted ACPI drivers** — the driver layer between the app and firmware breaks during major updates.
- **Conflicting power tools** — two manufacturer utilities (or a Windows power plan) fighting over charge control.
- **Limit reset by update** — BIOS updates and EC resets silently clear the limit setting.
- **Wrong limit location** — the limit set in the app while a different limit is active in the BIOS, with the BIOS winning.

## How to fix it

Work through these in order.

### Fix 1: Verify the limit is actually set where you think it is

Before troubleshooting, confirm the setting itself. Updates love to silently revert it.

1. Open your manufacturer's battery tool and check the charge limit setting — write down exactly what it says.
2. Restart into the BIOS (usually **F2** or **Del**) and check for a separate battery charge limit there.
3. If the BIOS has its own limit set differently, the BIOS wins. Align them: set the BIOS to your desired limit or disable it and control everything from the app.
4. If the app shows the limit as on but the BIOS shows nothing, the app-to-firmware link is suspect — continue below.

### Fix 2: Update the manufacturer's battery app

An outdated app is the most common single cause after 24H2.

1. Open the **Microsoft Store**, go to **Library**, and update the manufacturer's app (Lenovo Vantage, MyASUS, Dell Optimizer, Acer Care Center).
2. If the app isn't from the Store, download the latest version from the manufacturer's support site.
3. After updating, toggle the charge limit off, restart, then toggle it back on. This re-registers the setting with the firmware.
4. Charge from below the limit and watch: the battery should stop at the cap within one full cycle.

### Fix 3: Update the BIOS

The firmware enforces the limit, so outdated firmware is a prime suspect — especially if the limiter broke right after 24H2.

1. Check your BIOS version with `msinfo32`.
2. Download the latest BIOS for your exact model from the manufacturer's support site.
3. Install with the AC adapter connected, all apps closed, and don't interrupt it.
4. After the flash, re-enter the BIOS and re-check the charge limit setting — BIOS updates often reset it. Re-enable it, boot up, and test. For Lenovo-specific threshold issues, our guide to [fix Lenovo battery thresholds](/articles/how-to-fix-battery-threshold-not-working-lenovo-in-windows-11-24h2/) goes deeper.

### Fix 4: Reinstall the ACPI battery drivers

The driver layer between the app and firmware can corrupt during the 24H2 upgrade.

1. Open **Device Manager** and expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. Click **Action** > **Scan for hardware changes** and restart.
4. Re-open the manufacturer's app, verify the limit is still set, and test charging. Fresh drivers restore the communication path the limiter depends on.

### Fix 5: Remove conflicting power software

Two tools fighting over charge control produces exactly this symptom — settings that appear to apply but don't.

1. Check **Settings** > **Apps** > **Installed apps** for duplicate manufacturer utilities (for example, both Dell Power Manager and Dell Optimizer, or Lenovo Vantage plus an old Lenovo Settings app).
2. Uninstall the older or redundant one.
3. Also check for third-party "battery care" utilities and remove them — they conflict with the manufacturer's firmware-level control.
4. Restart, set the limit once in the surviving app, and test.

### Fix 6: Reset the embedded controller

A stuck EC can ignore limit commands even when everything else is correct.

1. Shut down, unplug the charger, and remove the battery if removable (or use the pinhole reset button for 10 seconds).
2. Hold the power button for 30 seconds.
3. Reconnect, boot, and re-apply the charge limit in the manufacturer's app.
4. The EC reset clears any latched state, and re-applying the limit afterward ensures the fresh controller receives the command cleanly.

### Fix 7: Test the limit with a controlled charge

Don't just eyeball it — run a proper test so you know for certain whether the fix worked.

1. Discharge the battery to at least 10% below your limit (for an 80% cap, get under 70%).
2. Plug in and leave the laptop charging, checking every 30 minutes.
3. The charge should slow as it approaches the limit and stop at or very near it. Some firmware stops 1–2% above or below the nominal limit — that's normal tolerance, not failure.
4. If it still sails past to 100%, note exactly what happens and contact the manufacturer's support — at that point you've proven the enforcement chain is broken at the firmware level, which is their bug to fix. Meanwhile, you can still protect the battery manually by unplugging at your target percentage.

## Closing

A charge limiter that ignores its limit is a broken chain: app, driver, firmware. Update the app, update the BIOS, reset the drivers, and re-apply the setting — in that order. Once the chain is whole again, the limit holds, and your battery gets the protection you set up in the first place. A limiter you can trust is worth the twenty minutes this takes. If you're configuring limits on a different brand, our [80% charge limit guide](/articles/how-to-limit-battery-charge-to-80/) covers every major manufacturer.
