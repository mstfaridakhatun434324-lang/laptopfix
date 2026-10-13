---
title: "How to Fix an MSI Battery Not Charging After a Windows 11 Update"
slug: how-to-fix-msi-battery-not-charging-after-windows-11-update
date: 2026-10-08
categories: ["battery"]
tags: ["msi", "not charging", "windows 11 update", "battery"]
description: "MSI laptop stopped charging after a Windows 11 update? 7 fixes from driver resets to MSI Center settings that get charging working again."
thumbnail: "/images/thumbs/how-to-fix-msi-battery-not-charging-after-windows-11-update.webp"
faqs:
  - q: "Why did my MSI stop charging right after a Windows 11 update?"
    a: "The update likely replaced MSI's battery or chipset driver with a generic Microsoft one, breaking communication between Windows and the battery controller. MSI Center's battery health options can also get reset or corrupted by updates, leaving a charge cap stuck in place."
  - q: "My MSI says 'plugged in, not charging.' Is the battery dead?"
    a: "Usually not — that message means Windows sees the charger but has paused charging, which is exactly what happens with a stuck charge limit or a confused driver. If the laptop runs fine on battery when unplugged, the cells are okay and this is a software problem."
  - q: "Should I uninstall the Windows update that caused it?"
    a: "Try the driver and MSI Center fixes first — they're faster and preserve security patches. Only uninstall the update if charging broke within hours of installing it and nothing else helps, and even then, reinstall it later after MSI publishes compatible drivers."
  - q: "Can MSI Center's Battery Health Option block charging?"
    a: "Yes. Its 'Best for Battery' mode caps charging at 60–80 percent, and after updates the setting can glitch into a state where charging stops entirely. Resetting it to 'Best for Mobility' (100%) is one of the first things to try."
---
You installed a Windows 11 update on your MSI laptop, rebooted, and now the battery icon says "plugged in, not charging" — or the percentage just sits frozen while the charger is connected. Everything worked yesterday. The timing makes the culprit obvious: the update changed something in the power stack.

MSI laptops have an extra layer of complexity because MSI Center manages battery behavior at a low level. When Windows Update and MSI Center disagree about who's in charge of charging, charging simply stops. Here's how to get them agreeing again.

## Why this happens

- **The update replaced MSI's battery driver.** Windows Update often swaps manufacturer drivers for generic ones, and the generic ACPI driver doesn't always speak MSI's battery controller language correctly.
- **MSI Center's Battery Health Option glitched.** The update can corrupt the stored charge-limit setting, leaving the battery capped at its current level permanently.
- **The chipset or EC driver mismatched.** Battery charging involves the chipset and embedded controller; an update that refreshes one without the other breaks the chain.
- **Fast Startup preserved a bad power state.** Hybrid shutdown carries the pre-update charging state forward, so the glitch survives reboots.
- **The update reset power plans.** Custom MSI power profiles can be wiped, leaving a plan that misconfigures charging behavior.
- **BIOS and Windows are now out of sync.** Some updates expect newer EC firmware; without it, charge commands from Windows go unanswered.
- **The battery controller needs a reset.** The update process can leave the battery's microcontroller in a confused state that only a hard reset clears.

## How to fix it

Work through these in order. MSI Center settings (Fix 1) and the driver reset (Fix 2) solve most cases.

### Fix 1: Reset MSI Center's Battery Health Option

This is the MSI-specific culprit — check it before touching anything else.

1. Open **MSI Center** (reinstall it from the Microsoft Store if the update broke it).
2. Go to **Features** > **Battery Health Option** or **System Tuner** > **Battery**.
3. If it's set to **Best for Battery** (caps at 60–80%), switch it to **Best for Mobility** (charges to 100%).
4. If it's already on Best for Mobility, toggle it to another mode, apply, then toggle back — this rewrites the stuck setting. Unplug and replug the charger, then watch the icon for five minutes.

### Fix 2: Reinstall the battery drivers

Clear out whatever driver the update installed and let Windows rediscover the battery cleanly.

1. Press **Win + X**, open **Device Manager**, expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and any duplicate, plus **Microsoft AC Adapter**.
3. Shut down fully (hold **Shift** while clicking **Shut down**), wait ten seconds, and power on.
4. Windows reinstalls fresh drivers at boot. Check charging status after a few minutes. If the battery itself is suspect, [check its health numbers](/articles/how-to-check-battery-health-on-windows-11-laptop/) to rule out worn cells.

### Fix 3: Install MSI's own drivers, not Microsoft's

Generic drivers are the root cause often enough that MSI's versions deserve a manual install.

1. Find your exact model on the sticker underneath or via `wmic csproduct get name`.
2. Download the **Chipset**, **Intel Management Engine**, and any **Battery/Power** drivers from MSI's support site for your model.
3. Install them with the charger connected, rebooting when prompted.
4. In **Device Manager**, verify no warning icons remain under **Batteries** or **System devices**, then test charging.

### Fix 4: Update the BIOS/EC firmware

MSI frequently ships EC firmware updates that fix charging behavior after Windows updates.

1. Check your current BIOS version with `wmic bios get smbiosbiosversion` in Command Prompt.
2. Compare against the latest on MSI's support page for your model — download it if yours is older.
3. Run the updater on AC power with all apps closed. Do not interrupt it; an interrupted flash can brick the board.
4. After reboot, do a full shutdown and power-on, then verify charging. Check MSI's guidance alongside Microsoft's [Windows update troubleshooting](https://support.microsoft.com/en-us/windows) if the update itself keeps re-breaking things.

### Fix 5: Disable Fast Startup and reset the EC

This clears the stale power state the update left behind.

1. Go to **Control Panel** > **Hardware and Sound** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**, and uncheck **Turn on fast startup**.
2. Shut down, unplug the charger, and hold the power button for 30 seconds to reset the embedded controller.
3. Reconnect the charger, power on, and check the battery icon.
4. Leave Fast Startup off for a few days to confirm stability before deciding whether to re-enable it.

### Fix 6: Roll back the problematic update

If charging died within hours of a specific update, remove the suspect.

1. Go to **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Remove the most recent **driver** update first — those are the usual culprits, not the security patches.
3. Restart and test charging. If it works, pause updates for two weeks via **Windows Update** > **Pause updates** to give MSI time to publish a fixed driver.
4. Reinstall the update later once MSI confirms compatibility. For broader not-charging scenarios, our general guide to [laptops not charging when plugged in](/articles/best-way-to-fix-laptop-battery-not-charging-when-plugged-in/) covers hardware-side checks like the adapter and DC jack.

### Fix 7: Run MSI's battery calibration

If charging works but stops at a weird percentage, the gauge — not the charger — is confused.

1. In **MSI Center**, find **Battery Calibration** under the battery tools section.
2. Plug in, run the calibration, and don't interrupt it — it takes several hours.
3. Afterward, charge to 100 percent uninterrupted and confirm the icon reads correctly.
4. If calibration fails or the battery won't hold a charge at all afterward, the pack itself may have failed coincidentally with the update — contact MSI support with your serial number for warranty options.

## Closing

Post-update charging failures on MSI laptops are a software disagreement, not a hardware death. Reset MSI Center's battery option, reinstall the drivers with MSI's own versions, and update the EC firmware — that sequence restores charging for the overwhelming majority of machines.
