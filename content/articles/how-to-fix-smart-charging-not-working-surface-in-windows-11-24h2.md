---
title: "Surface Smart Charging Not Working on Windows 11 24H2? Fix It"
slug: how-to-fix-smart-charging-not-working-surface-in-windows-11-24h2
date: 2026-10-12
categories: ["battery"]
tags: ["battery", "smart charging", "surface", "windows 11 24h2"]
description: "Surface Smart Charging stuck on, stuck off, or pausing at the wrong level on Windows 11 24H2? Fix it with these 7 steps."
thumbnail: "/images/thumbs/how-to-fix-smart-charging-not-working-surface-in-windows-11-24h2.webp"
faqs:
  - q: "What is Smart Charging on a Surface device?"
    a: "Smart Charging is a Microsoft battery-protection feature that pauses charging before 100 percent — typically at 50 or 80 percent — to reduce chemical stress on the battery and extend its lifespan. It's managed through the Surface app and works at the firmware level."
  - q: "Why is Smart Charging stuck on after the 24H2 update?"
    a: "The 24H2 update can corrupt the Surface app's configuration, mismatch the Surface firmware with the OS, or leave the feature's toggle out of sync with the firmware state. Reinstalling the Surface app and updating Surface firmware usually restores control."
  - q: "Can I turn off Smart Charging permanently?"
    a: "Yes. Open the Surface app, go to Battery & charging, and toggle Smart Charging off. It stays off until you re-enable it. Note that keeping it on meaningfully extends battery lifespan if you mostly work plugged in."
  - q: "Does Smart Charging work on all Surface models?"
    a: "No. It's available on newer Surface Laptop and Surface Pro models. Older devices may only offer the UEFI battery limit (50 percent cap) instead. If your Surface app has no Smart Charging toggle, your model likely doesn't support the feature."
---

Smart Charging is supposed to be the quiet guardian of your Surface's battery — pausing the charge at a healthy level while you work plugged in. But on Windows 11 24H2, it misbehaves: the toggle won't turn off, the battery pauses at the wrong percentage, the Surface app says one thing while the battery does another, or the feature simply does nothing at all. The 24H2 update disrupted the handshake between the Surface app, the OS, and the firmware that actually enforces the limit.

Because Smart Charging lives partly in firmware, fixing it means getting all three layers — app, OS, and firmware — back in agreement. The seven steps below do exactly that, from the simplest toggle checks to a full firmware refresh.

## Why this happens

- **The Surface app's configuration corrupted during the 24H2 upgrade.** The toggle state in the app no longer matches the firmware state, so changes you make don't take effect.
- **Surface firmware is out of sync with the OS.** Smart Charging is enforced by firmware; if the firmware predates the 24H2 driver stack, commands from the app get ignored.
- **The UEFI battery limit conflicts with Smart Charging.** On models that have both, an enabled UEFI limit can override or confuse the Smart Charging behavior.
- **A stale Surface driver package.** The 24H2 update may have partially overwritten Surface system drivers, breaking the app-to-firmware communication channel.
- **The feature paused at a learned pattern.** Smart Charging adapts to usage; after an update it can lock onto a wrong pattern and pause charging at odd times.
- **Third-party battery utilities interfering.** Rare on Surface, but any installed power-management tool can fight the Surface app for control.

## How to fix it

Work through these in order, testing the toggle after each step.

### Fix 1: Toggle Smart Charging properly in the Surface app

Make sure you're operating the right control — and that the app is healthy.

1. Open the **Surface** app. If it's missing, install **Surface** from the Microsoft Store.
2. Navigate to **Battery & charging** (on some models it's under **Device information**).
3. Toggle **Smart Charging** off, wait 30 seconds, then toggle it back on if that's your preference.
4. Plug in the charger and watch for 5–10 minutes: with Smart Charging on, charging should pause at the limit; with it off, it should climb past it.
5. If the toggle is greyed out or missing, your model may not support the feature — check for a UEFI battery limit instead (Fix 4).

### Fix 2: Reset the Surface app

A corrupted app cache is the most common cause of a dead toggle.

1. Open **Settings > Apps > Installed apps**.
2. Find **Surface**, click the three dots, and choose **Advanced options**.
3. Click **Repair** first and test the toggle.
4. If it's still broken, go back and click **Reset**. This clears the app's stored configuration.
5. Reopen the Surface app, set Smart Charging to your preference, and test with the charger connected.

### Fix 3: Reinstall the Surface app completely

When reset isn't enough, a fresh install rebuilds the app-to-firmware link.

1. In **Settings > Apps > Installed apps**, find **Surface** and **Uninstall** it.
2. Restart the Surface.
3. Open the **Microsoft Store**, search for **Surface**, and reinstall the app.
4. Open it, go to **Battery & charging**, and configure Smart Charging fresh.
5. Test charging behavior for 10 minutes. A clean app install resolves most "toggle does nothing" cases.

### Fix 4: Check the UEFI battery limit

The firmware-level limit can override everything the app does.

1. Shut down the Surface completely.
2. Hold **Volume Up**, press and release **Power**, and keep holding Volume Up until the Surface logo appears.
3. In Surface UEFI, look for the battery limit setting under the battery or boot configuration section.
4. If it's enabled and you want full Smart Charging control from Windows, disable it here, then **Exit > Restart Now**.
5. Back in Windows, set your Smart Charging preference in the Surface app and verify the battery now obeys it. For context on what the limits mean for longevity, [check your battery's design vs full charge capacity](/articles/how-to-check-battery-design-vs-full-charge-capacity-on-windows-11/).

### Fix 5: Update Surface firmware and drivers

The firmware enforcing Smart Charging must match the 24H2 driver stack.

1. Open **Settings > Windows Update** and install all pending updates, including **Optional updates** under Advanced options.
2. Restart and test Smart Charging.
3. If Windows Update offers nothing, download the **Surface driver and firmware MSI** for your exact model from [Microsoft support](https://support.microsoft.com/en-us/windows) and install it with the charger connected.
4. After the firmware update and restart, open the Surface app and reconfigure Smart Charging — firmware updates can reset it to defaults.

### Fix 6: Reinstall the Surface system drivers via Device Manager

Repair the communication channel between the OS and firmware.

1. Open **Device Manager** and expand **System devices** and **Firmware**.
2. Look for **Surface**-named entries (Surface System Aggregator, Surface UEFI, Surface Battery).
3. Right-click each, choose **Uninstall device**, but do **not** check "delete driver software" — you want Windows to rebind the existing driver cleanly.
4. Click **Action > Scan for hardware changes**, then restart.
5. Open the Surface app and test the Smart Charging toggle again.

### Fix 7: Do a two-button shutdown to reset the charge controller

Clear stuck firmware state in the charging hardware itself.

1. Shut down the Surface.
2. Press and hold **Power + Volume Up** together for 15 seconds, then release.
3. Wait 10 seconds and press **Power** once to boot.
4. Once in Windows, set Smart Charging to your preference in the Surface app.
5. Charge from below the limit to above it and confirm the behavior is correct. If Smart Charging now works but the gauge seems off, [recalibrate the battery](/articles/how-to-calibrate-laptop-battery-windows-11/) to finish the job.

## Closing

Smart Charging problems on 24H2 are almost always a disagreement between the Surface app and the firmware — not a broken battery. Reset or reinstall the app, update the firmware, and check the UEFI limit, and the three layers fall back into agreement. Once the toggle reliably controls the charge pause again, leave the feature on if you spend most of your day plugged in; your battery's lifespan will thank you in two years.
