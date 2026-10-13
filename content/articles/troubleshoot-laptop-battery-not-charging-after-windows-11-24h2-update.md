---
title: "Laptop Battery Not Charging After the Windows 11 24H2 Update: Full Troubleshooting Guide"
slug: troubleshoot-laptop-battery-not-charging-after-windows-11-24h2-update
date: 2026-09-30
categories: ["battery"]
tags: ["battery not charging", "windows 11 24h2", "troubleshooting", "driver fix"]
description: "Battery stuck at the same percentage after the Windows 11 24H2 update? Run through this complete troubleshooting sequence to get charging again."
thumbnail: "/images/thumbs/troubleshoot-laptop-battery-not-charging-after-windows-11-24h2-update.webp"
faqs:
  - q: "Why did my battery stop charging right after the Windows 11 24H2 update?"
    a: "The update commonly corrupts or replaces the ACPI battery driver, which breaks the charging handshake between Windows and the battery controller. It can also enable battery saver limits or change power-plan behavior. The battery hardware is almost always fine — the software layer just needs repair."
  - q: "What does 'plugged in, not charging' actually mean?"
    a: "It means Windows sees the charger but has paused charging, either deliberately (charge limit, battery saver, thermal protection) or because the driver can't communicate with the battery. Check whether the percentage is capped at a round number like 80% — that points to a deliberate limit rather than a fault."
  - q: "Should I uninstall the 24H2 update to fix charging?"
    a: "Only as a last resort. Driver reinstallation and a controller reset fix the vast majority of cases without rolling back. If you do roll back, go to Settings > Windows Update > Update history > Uninstall updates, but do it within 10 days of the update while rollback files still exist."
  - q: "How long should I spend troubleshooting before replacing the battery?"
    a: "Give the software fixes one focused session — about 45 minutes. If the battery was charging normally the day before the update and now shows zero response to every software fix, test with a known-good charger first. Only consider a new battery if a battery report shows severe wear."
---

The update finished, the laptop rebooted, and now the battery icon says "plugged in, not charging" — or worse, the percentage slowly slides downward while the charger sits connected. Yesterday everything was fine. The timing makes the 24H2 update the obvious suspect, and most of the time, it is.

Before you assume the worst, know this: post-update charging failures are one of the most fixable laptop problems there is, and technicians see them in waves after every major Windows release. The update didn't fry your battery; it scrambled the software that manages charging. This guide walks the full sequence, from the two-minute checks to the deeper repairs, and links out to companion fixes like [no battery detected](/articles/laptop-battery-not-detected-windows-11/) when the symptoms overlap.

## Why this happens

- **Corrupted ACPI battery driver.** The 24H2 update's driver migration can leave the Microsoft ACPI-Compliant Control Method Battery driver half-installed, breaking charge commands.
- **A charge limit got enabled.** Some updates re-enable manufacturer charge thresholds (60% or 80% caps) or Windows battery saver rules that pause charging.
- **Power plan corruption.** The update can reset or damage custom power plans, leaving the system in a state where it refuses to request charge current.
- **Fast Startup preserved a bad state.** The hibernation-style shutdown caches device state; if the battery interface glitched during the update reboot, the glitch gets restored every boot.
- **BIOS/EC mismatch.** Firmware that updated alongside Windows may now expect a driver version that isn't installed, stalling the charging handshake.
- **Coincidental hardware failure.** Batteries and chargers sometimes fail the same week as an update by pure coincidence — always verify with a second charger before concluding it's software.
- **Overheating protection engaged.** If the update triggered heavy background indexing or a stuck update process, the battery may be too hot to accept charge. Charging resumes once temperatures drop, which is why the problem can appear and vanish on its own.

## How to fix it

Work through these in order. Stop when charging resumes — and give each step a full restart before moving on, since driver changes only take effect after a reboot.

### Fix 1: Check for a deliberate charge limit first

1. Hover over the battery icon: if it says "plugged in, not charging" at exactly 80%, 60%, or 50%, a limiter is active.
2. Open your manufacturer's app (Lenovo Vantage, Dell Power Manager, MyASUS, HP BIOS settings) and look for battery charge thresholds.
3. Set the threshold to 100% or disable conservation/limited charging mode.
4. In **Settings > System > Power & battery**, turn off **Battery saver** if it's stuck on.

### Fix 2: Power-cycle the charging hardware

1. Shut down completely and unplug the charger.
2. Disconnect all USB-C docks, hubs, and peripherals.
3. Hold the power button for 30 seconds to drain residual charge.
4. Plug the charger directly into a wall outlet, wait 10 seconds, then power on.
5. Give it five minutes — the controller sometimes needs a moment to renegotiate charging.

### Fix 3: Reinstall the battery drivers

1. Open **Device Manager** (right-click **Start**).
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Repeat for any second battery entry.
4. Click **Action > Scan for hardware changes**.
5. Restart the laptop and watch the battery icon for a full two minutes.

### Fix 4: Disable Fast Startup

1. Go to **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)**, then **Save changes**.
4. Shut down fully and cold-boot. This forces Windows to re-detect the battery from scratch instead of restoring a cached bad state.

### Fix 5: Restore or reset your power plan

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. If your custom plan is selected, switch to **Balanced** and test charging.
3. To rebuild cleanly, open **Terminal (Admin)** and run `powercfg -restoredefaultschemes`.
4. Restart and recheck. Corrupted plan settings are an underrated cause of "not charging" after feature updates.

### Fix 6: Update chipset and BIOS from the manufacturer

1. Identify your exact model (sticker on the bottom or **System Information** via `msinfo32`).
2. Download the latest chipset driver and BIOS from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Install the chipset driver first, restart, then run the BIOS update on wall power with nothing else running.
4. After the BIOS update, enter setup and **Load Optimized Defaults**, then save and exit.

### Fix 7: Test with a different charger and check battery wear

1. Borrow a charger with the correct wattage and connector for your model.
2. If charging resumes, your adapter died — replace it with a genuine one.
3. If it still won't charge, run `powercfg /batteryreport` in **Terminal (Admin)** and compare design vs. full charge capacity.
4. Severe wear plus zero charging response means the battery itself has failed; everything else on this list being clean points squarely at hardware.

### Fix 8: Run the built-in battery calibration cycle

1. Charge the laptop to 100% and leave it plugged in for two extra hours so every cell tops up.
2. Unplug and use the laptop normally until it shuts itself off at critically low battery — don't plug in early.
3. Leave it off and unplugged for at least three hours so the cells settle to their true resting voltage.
4. Plug in and charge uninterrupted back to 100%. This full cycle teaches the fuel gauge the battery's real capacity, which often clears a "not charging" state that was really a misreported full battery.

## Closing

Post-update charging problems feel catastrophic and fix like minor glitches. In the overwhelming majority of cases, the sequence above — limit check, power cycle, driver reinstall, Fast Startup off — gets the battery charging again without spending a cent. Save the hardware conclusions for last, after the software has had its fair chance, and keep notes on which step worked so you can repeat it after the next big update. If the battery charges but then empties suspiciously fast, the [fast-drain checklist](/articles/laptop-battery-drains-fast-windows-11/) picks up where this guide leaves off.
