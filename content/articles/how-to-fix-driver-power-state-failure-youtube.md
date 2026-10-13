---
title: "How to Fix the DRIVER_POWER_STATE_FAILURE Blue Screen"
slug: how-to-fix-driver-power-state-failure-youtube
date: 2026-09-10
categories: ["windows-errors"]
tags: ["driver power state failure", "blue screen", "sleep", "power management", "driver"]
description: "DRIVER_POWER_STATE_FAILURE usually strikes on sleep/wake. Update drivers, fix power settings, and stop the crashes with this guide."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-youtube.webp"
faqs:
  - q: "What causes DRIVER_POWER_STATE_FAILURE?"
    a: "A driver failed to complete a power state transition — typically not waking up from sleep or not powering down properly. The usual offenders are network (Wi-Fi), graphics, and USB drivers, especially on laptops where power management is aggressive."
  - q: "Why does it happen when my laptop sleeps or wakes?"
    a: "Sleep and wake are the moments drivers must change power states. If a driver hangs during the transition — because of a bug, a mismatch with the BIOS, or a device that won't respond — Windows waits, times out, and bugchecks with this stop code."
  - q: "Is DRIVER_POWER_STATE_FAILURE a hardware problem?"
    a: "Rarely. It's a driver/power-management software issue in the vast majority of cases. Suspect hardware only if it persists across a clean Windows install with manufacturer drivers, or if a specific device (like the Wi-Fi card) is also misbehaving in other ways."
  - q: "Can I just disable sleep to avoid it?"
    a: "You can as a temporary workaround (set sleep to Never), but it doesn't fix the underlying driver problem and wastes battery. Use it to stabilize the system while you update the offending driver, then re-enable sleep."
---

**DRIVER_POWER_STATE_FAILURE** is the blue screen of the sleep/wake cycle. Your laptop goes to sleep fine — or tries to — and instead of waking up, you get a blue screen. Or it crashes the moment the display turns off. The pattern is the clue: something in the driver stack can't handle power transitions.

Laptops hit this more than desktops because their power management is far more aggressive — devices constantly sleep and wake to save battery. The fix is about finding which driver chokes on the transition and either updating it or telling Windows to leave it alone. If your crashes happen specifically at startup rather than sleep, see [BSOD on startup fixes](/articles/how-to-fix-bsod-on-startup-windows-11-youtube/) instead.

The pattern of when it crashes is diagnostic gold: crashes only when entering sleep point at a device failing to power down; crashes only on wake point at a device failing to power up; crashes at random times point away from power management toward a general driver bug. Note your pattern — it tells you where to focus.

## Why this happens

- **Wi-Fi/network driver power bug:** The #1 cause — wireless drivers that hang when the radio powers down or back up.
- **Graphics driver power-state bug:** GPU drivers failing the transition, common after major driver updates.
- **USB device refusing to sleep:** External devices (or their drivers) that won't enter low-power states.
- **Outdated BIOS/UEFI:** Firmware with buggy ACPI power tables that confuse Windows' power manager.
- **Aggressive power plan settings:** PCI Express link-state power management or USB selective suspend conflicting with specific hardware.
- **Fast Startup:** The hybrid shutdown interacting badly with driver power states.
- **Dock/Thunderbolt drivers:** External docks with buggy power handling hanging the sleep transition.

## How to fix it

Work through these in order.

### Fix 1: Identify the failing driver from the dump

1. Open the latest minidump in `C:\Windows\Minidump` with **WinDbg Preview** and run `!analyze -v`.
2. Look for the driver in the stack — commonly `Netwtw10.sys`/`Netwtw12.sys` (Intel Wi-Fi), `rtwlane.sys` (Realtek), `nvlddmkm.sys` (NVIDIA), or `dxgkrnl.sys`.
3. If a driver is named, skip straight to updating it (Fix 2) — you've found your target.

### Fix 2: Update the network driver first

The Wi-Fi driver is the single most common culprit. The wireless radio powers down and up constantly on a laptop — every sleep, every idle — so a power-handling bug in this driver gets exercised more than almost any other. A clean reinstall (uninstall, reboot, fresh install) beats an in-place update.

1. Go to your laptop maker's support site and download the latest **Wi-Fi** and **Bluetooth** drivers for your exact model.
2. In **Device Manager**, expand **Network adapters**, right-click the Wi-Fi adapter, and choose **Uninstall device** (check "attempt to remove the driver software" if offered).
3. Restart, then install the freshly downloaded driver.
4. Test sleep/wake cycles: put the laptop to sleep manually (**Start > Power > Sleep**), wait a minute, wake it. Repeat a few times.

### Fix 3: Update graphics and chipset drivers

1. Clean-install the **graphics driver** (DDU in Safe Mode, then the manufacturer's recommended version).
2. Install the latest **chipset driver** from the laptop maker — it includes the power management components.
3. Update the **BIOS/UEFI firmware** — firmware updates frequently fix ACPI power-transition bugs. Keep the laptop plugged in during the flash.

### Fix 4: Change the Wi-Fi adapter's power management

If the Wi-Fi driver is implicated but no newer version exists:

1. In **Device Manager**, right-click the Wi-Fi adapter > **Properties** > **Power Management** tab.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. On the **Advanced** tab, look for power-saving properties (like "Power Saving Mode" or "Selective suspend") and set them to **Maximum Performance**.
4. Test sleep/wake again.

### Fix 5: Adjust USB and PCI Express power settings

When the driver is current but still misbehaves, stop asking it to manage power at all. These settings trade a little battery life for stability — a worthwhile deal while you wait for a fixed driver.

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set it to **Disabled** (both battery and plugged in).
3. Expand **PCI Express > Link State Power Management** and set it to **Off** (or **Moderate** if Off hurts battery too much — test).
4. Click **Apply/OK** and test sleep cycles.

### Fix 6: Disable Fast Startup

Fast Startup's hybrid shutdown is a known trigger.

1. **Control Panel > Power Options > Choose what the power buttons do > Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup** and save.
3. Shut down fully (not restart) and power back on, then test sleep/wake.

### Fix 7: Disconnect USB devices and isolate

A misbehaving USB device can hang the whole power transition.

1. Unplug all USB devices (docks, hubs, external drives, receivers).
2. Test sleep/wake. If crashes stop, reconnect devices one at a time, testing sleep after each.
3. Update or replace the driver/firmware for the device that triggers it. USB docks especially need firmware updates from their maker.

### Fix 8: Reset the power plan and update Windows fully

The cleanup pass.

1. In an admin terminal, run `powercfg /restoredefaultschemes` to reset all power plans to defaults.
2. Go to **Settings > Windows Update** and install everything, including optional driver updates — Microsoft does ship power-management fixes.
3. If a specific update caused it, use **Uninstall Updates** in WinRE to remove it and pause updates briefly. If the crashes began right after an update, our [blue screen after Windows 11 update guide](/articles/how-do-i-fix-blue-screen-after-windows-11-update/) covers update-specific causes.
4. For persistent cases, grab the latest cumulative update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).

## Closing

DRIVER_POWER_STATE_FAILURE is a power-transition problem, so think in terms of transitions: which driver handles sleep/wake for the device, and is it current? The Wi-Fi driver plus the BIOS update resolve most cases; the power-setting adjustments in Fixes 4–6 handle the rest. Test with real sleep/wake cycles after each change — that's the only test that matters for this stop code. Once sleep is reliable again, you can re-tighten power-saving settings gradually. Re-enable them one at a time, testing sleep after each, so you keep the battery savings that don't cause crashes and only sacrifice the ones that do.
