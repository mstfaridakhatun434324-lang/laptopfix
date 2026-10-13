---
title: "Fix Acer Laptop Battery Not Charging on Windows 11"
slug: how-to-fix-acer-laptop-battery-not-charging-on-windows-11
date: 2026-09-27
categories: ["battery"]
tags: ["acer", "battery not charging", "windows 11"]
description: "Acer laptop won't charge on Windows 11? Check Acer's charge limit, reset the battery drivers, and update the BIOS with these 8 targeted fixes."
thumbnail: "/images/thumbs/how-to-fix-acer-laptop-battery-not-charging-on-windows-11.webp"
faqs:
  - q: "Why won't my Acer battery charge after upgrading to Windows 11?"
    a: "Windows 11 upgrades frequently corrupt the Microsoft ACPI battery driver or change power management behavior. Acer's Battery Charge Limit in Acer Care Center can also behave differently after the upgrade. Reset the battery drivers in Device Manager first, then check Acer Care Center's charge limit setting."
  - q: "Where is the battery setting in Acer Care Center on Windows 11?"
    a: "Open Acer Care Center from the Start menu, go to the Checkup tab, and look for Battery Charge Limit. If it's enabled at 80%, the battery stops charging there by design. Turn it off to allow full charging. On some models this setting lives in the BIOS instead, accessible by pressing F2 during startup."
  - q: "Does Windows 11 need different Acer drivers for charging?"
    a: "Yes — make sure you've installed Acer's Windows 11 chipset and power management drivers for your exact model, not the old Windows 10 ones. Mismatched drivers after an upgrade are a common cause of charging failures. Download them from Acer's support site for your specific model number."
  - q: "My Acer charges to 80% and stops on Windows 11. Is that a fault?"
    a: "No, that's almost certainly the Battery Charge Limit feature working as designed. It's meant to extend battery lifespan for laptops that stay plugged in. If you want a full charge, disable the limit in Acer Care Center or the BIOS — the behavior will change immediately."
---

Upgrading to Windows 11 and discovering your Acer laptop no longer charges is a special kind of frustration. Everything worked yesterday; today the battery sits frozen at some percentage with "plugged in, not charging" mocking you from the taskbar. The upgrade didn't kill your battery — but it very likely scrambled the drivers and settings that manage charging.

Acer laptops have a few brand-specific wrinkles on Windows 11: the Battery Charge Limit feature, Acer Care Center's power management, and firmware that sometimes needs an update to play nicely with the new OS. This guide tackles the Acer-specific causes first, then the general Windows 11 fixes.

## Why this happens

- **Battery Charge Limit enabled** — Acer Care Center caps charging at 80% to prolong battery life; after an upgrade it may be on without you knowing.
- **Corrupted ACPI battery driver** — the Windows 11 upgrade process commonly breaks the driver handshake with Acer's firmware.
- **Old Windows 10 drivers** — chipset and power drivers carried over from Windows 10 can mismanage charging on Windows 11.
- **BIOS incompatibility** — older BIOS versions may not fully support Windows 11's power management calls.
- **Stuck embedded controller** — the charge controller can latch into a non-charging state during the upgrade reboots.
- **Worn battery exposed by recalibration** — the upgrade sometimes triggers a battery recalibration that reveals degradation that was already there.

## How to fix it

Work through these in order.

### Fix 1: Check Acer Care Center's Battery Charge Limit

Start here — this is the most common Acer-specific cause, and it takes thirty seconds to rule out.

1. Open **Acer Care Center** from the Start menu. If it's missing after the upgrade, install it fresh from the Microsoft Store.
2. Go to the **Checkup** tab and find **Battery Charge Limit**.
3. If it's enabled (usually capped at 80%), toggle it **Off**.
4. Watch the battery icon for a minute. If charging resumes past the previous stopping point, that was the entire problem — the feature was doing its job, just without your knowledge.

### Fix 2: Check the BIOS-level charge limit

On some Acer models the charge limit lives in firmware rather than in Windows software, so Acer Care Center won't show it.

1. Restart the laptop and press **F2** repeatedly to enter the BIOS setup.
2. Look through the **Main**, **Power**, or **Advanced** tabs for a battery charge limit or battery health option.
3. Disable any limit you find, then **Save and Exit**.
4. Boot into Windows and verify the battery charges fully. Firmware limits override every Windows setting, so this check matters.

### Fix 3: Reinstall the battery drivers

The Windows 11 upgrade is notorious for corrupting these drivers on Acer machines. A clean reinstall fixes it.

1. Right-click **Start** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Uninstall **Microsoft AC Adapter** the same way.
4. Click **Action** > **Scan for hardware changes**, then restart with the charger connected.
5. Windows rebuilds the charging driver stack against the new OS — detection and charging usually return immediately.

### Fix 4: Install Acer's Windows 11 chipset and power drivers

Drivers carried over from Windows 10 are a frequent culprit after an in-place upgrade.

1. Find your exact model number on the bottom label of the laptop.
2. Visit Acer's support site and download the **chipset**, **power management**, and **ATK/ACPI** drivers specifically marked for Windows 11.
3. Install the chipset driver first, then the others, restarting when prompted.
4. Test charging after the final restart. Correct Windows 11 drivers restore the proper communication between the OS and Acer's charging firmware.

### Fix 5: Update the BIOS for Windows 11 compatibility

Acer has released BIOS updates for many models specifically to fix Windows 11 power behavior.

1. Check your current version with `msinfo32` under **BIOS Version/Date**.
2. Download the latest BIOS for your exact model from Acer's support site.
3. Connect the AC adapter, close everything, and run the update. Do not touch the laptop until it finishes and reboots on its own.
4. After updating, check both charging behavior and the Acer Care Center charge limit setting, which sometimes resets during a BIOS flash.

### Fix 6: Reset the embedded controller

Upgrade reboots can leave the charge controller in a stuck state that survives normal restarts.

1. Shut down completely and unplug the charger.
2. If the battery is removable, take it out. Otherwise, use the pinhole reset button on the bottom if your model has one — press for 10 seconds with a paperclip.
3. Hold the power button for 30 seconds, then reconnect everything and boot.
4. This clears the controller's latched state and forces it to renegotiate charging from scratch.

### Fix 7: Run the Windows 11 power troubleshooter

Windows 11 moved things around, but the troubleshooter still catches common misconfigurations.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Run the **Power** troubleshooter and apply its recommendations.
3. Then open **Command Prompt** as administrator and run `powercfg /restoredefaultschemes` to reset any power plan corruption from the upgrade.
4. Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) has additional power troubleshooting guidance if the built-in tool doesn't resolve it.

### Fix 8: Verify the battery's actual health

If everything above checks out, make sure the battery itself isn't the problem — the upgrade may have simply revealed existing wear.

1. Open **Command Prompt** as administrator and run `powercfg /batteryreport`.
2. Open `C:\Windows\System32\battery-report.html` and compare **Design Capacity** with **Full Charge Capacity`.
3. A battery holding less than half its design capacity is worn out. Learn how to [check your battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) in detail before deciding on replacement.
4. For a badly degraded battery, replacement with a genuine Acer part is the fix — no setting recovers lost chemistry. If the drain happens overnight instead, see our guide on [batteries draining overnight while off](/articles/what-to-do-if-battery-drains-overnight-when-laptop-is-off/).

## Closing

On Acer laptops, Windows 11 charging failures are usually the charge limit feature, upgrade-damaged drivers, or outdated firmware — all fixable without new hardware. Work the Acer-specific settings first, then the Windows-side resets, and confirm with a battery report before spending money on a replacement.
