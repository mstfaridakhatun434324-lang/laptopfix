---
title: "How to Fix DRIVER_POWER_STATE_FAILURE on an HP Laptop"
slug: how-to-fix-driver-power-state-failure-on-hp-laptop
date: 2026-09-30
categories: ["windows-errors"]
tags: ["bsod", "drivers", "hp"]
description: "DRIVER_POWER_STATE_FAILURE blue screen on your HP laptop? It's a driver power-management issue — here's how to find and fix the bad driver."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-on-hp-laptop.webp"
faqs:
  - q: "What does DRIVER_POWER_STATE_FAILURE mean?"
    a: "A driver didn't handle a power-state change correctly — usually when the laptop sleeps, wakes, hibernates, or shuts down. The driver took too long to respond or responded wrongly, so Windows crashed to protect itself. Wi-Fi, Bluetooth, graphics, and storage drivers are the usual offenders on HP laptops."
  - q: "Why does it happen when my HP laptop wakes from sleep?"
    a: "Sleep and wake are the heaviest power transitions a laptop performs. Every device driver must power down and back up in sequence; if one driver hangs during the transition — very commonly the Wi-Fi or graphics driver — Windows hits its timeout and throws this exact stop code."
  - q: "Can Windows Update cause DRIVER_POWER_STATE_FAILURE?"
    a: "Yes, and it's one of the most common triggers. Windows Update sometimes replaces a working manufacturer driver with a generic or newer-but-buggy version. If the crashes started right after an update, rolling back the recently updated driver is the fastest fix."
  - q: "Is DRIVER_POWER_STATE_FAILURE a hardware problem?"
    a: "Rarely. It's almost always a driver or power-settings issue, not failing hardware. The exception is a genuinely failing device (like a dying Wi-Fi card) whose driver can't complete power transitions because the hardware beneath it is misbehaving — but start with drivers first."
---
Your HP laptop goes to sleep, you open the lid, and instead of the login screen there's a blue screen: DRIVER_POWER_STATE_FAILURE. Or maybe it happens on shutdown, or when the screen wakes from idle. Either way, the pattern is the same — the crash is tied to power transitions, and something in the driver stack isn't handling them.

This is one of the more fixable blue screens because the culprit is almost always software: a driver that mishandles sleep/wake, or a power setting that puts devices into states their drivers can't recover from. Here's how to track it down.

## Why this happens

- **Wi-Fi/Bluetooth driver mishandling sleep** — the most common single cause on HP laptops. The wireless driver fails to power down or back up cleanly during sleep transitions.
- **Graphics driver power bug** — Intel, NVIDIA, or AMD graphics drivers with broken power management fault during display sleep/wake.
- **Windows Update replaced a working driver** — a generic driver from Windows Update lacks the HP-specific power handling the original had.
- **USB selective suspend conflicts** — Windows powering down USB devices (docks, external drives, receivers) while their drivers expect them awake.
- **Fast Startup saving a bad driver state** — the hibernation-based fast boot preserves a corrupted driver power state across restarts.
- **Outdated BIOS** — power management is partly firmware; old BIOS versions mishandle modern Windows sleep states (Modern Standby).
- **Failing device beneath the driver** — a Wi-Fi card or SSD with hardware faults can't complete power transitions, and its driver takes the blame.

## How to fix it

Work through these in order. Note when your crashes happen (sleep, wake, shutdown) — it helps confirm each fix.

### Fix 1: Identify the faulting driver from the crash dump

Don't guess — read the evidence Windows saved.

1. After a crash, boot normally and press **Windows + R**, type `eventvwr.msc`, and open **Windows Logs** > **System**.
2. Look for **BugCheck** entries around the crash time — the details often name the faulting driver file (like Netwtw10.sys for Intel Wi-Fi or nvlddmkm.sys for NVIDIA).
3. For deeper detail, install WinDbg Preview from the Microsoft Store, open **File** > **Start debugging** > **Open dump file**, and load the latest file from C:\\Windows\\Minidump. Run `!analyze -v` — the MODULE_NAME line names the driver.
4. Whatever driver is named becomes your prime suspect for Fix 2.

### Fix 2: Update or roll back the suspect driver

Target the driver you identified — or the usual suspects if you couldn't identify one.

1. Open **Device Manager** (**Windows + X** > **Device Manager**).
2. For Wi-Fi: expand **Network adapters**, right-click your wireless adapter > **Properties** > **Driver** tab. If the crashes started after an update, click **Roll Back Driver**. Otherwise click **Update driver** > **Search automatically for drivers**.
3. For the definitive version, download the driver from [HP's support site](https://support.hp.com/us-en) for your exact model — HP's wireless and graphics drivers include power-management fixes generic versions lack.
4. Repeat for **Display adapters** (your GPU) and **Bluetooth**.
5. For Intel-based HPs, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can also supply current Wi-Fi and Bluetooth drivers.

### Fix 3: Change the power plan settings

Stop Windows from putting devices into states their drivers can't handle.

1. Open **Control Panel** > **Hardware and Sound** > **Power Options** > **Change plan settings** (for your active plan) > **Change advanced power settings**.
2. Expand **Wireless Adapter Settings** > **Power Saving Mode** and set both On battery and Plugged in to **Maximum Performance**.
3. Expand **USB settings** > **USB selective suspend setting** and set both to **Disabled**.
4. Expand **PCI Express** > **Link State Power Management** and set it to **Moderate power savings** (not Maximum) or **Off** for testing.
5. Click **Apply** > **OK**, then test sleep/wake cycles deliberately: sleep the laptop, wait a minute, wake it — repeat several times.

### Fix 4: Disable Fast Startup

Fast Startup's saved driver state can perpetuate the crash across reboots.

1. Open **Control Panel** > **Hardware and Sound** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully (not restart), power back on, and test your usual crash trigger.
5. Many DRIVER_POWER_STATE_FAILURE cases disappear at this step alone.

### Fix 5: Update the BIOS

Firmware-level power management fixes come through BIOS updates.

1. Find your exact model: press **Windows + R**, type `msinfo32`, note **System Model** and **BIOS Version/Date**.
2. Go to [HP Support](https://support.hp.com/us-en), enter your model, and check **BIOS** under drivers.
3. If a newer BIOS exists, download it, plug in the AC adapter, close everything, and run the installer — don't interrupt it.
4. After the update, retest sleep/wake. BIOS updates frequently resolve Modern Standby transition bugs behind this stop code.

### Fix 6: Run the power troubleshooter and check for device issues

Let Windows audit its own power configuration.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** and run the **Power** troubleshooter.
2. In **Device Manager**, check every category for yellow warning icons — a device with a problem driver often shows one.
3. For USB devices you always keep plugged in (docks, receivers), right-click each under **Universal Serial Bus controllers** > **Properties** > **Power Management** tab, and uncheck **Allow the computer to turn off this device to save power**.
4. If you use an HP docking station, check HP's site for dock firmware updates too.

### Fix 7: Reset the power plans to default

If settings have been tweaked over time, start clean.

1. Open an admin Terminal (**Windows + X** > **Terminal (Admin)**) and run:
   `powercfg -restoredefaultschemes`
2. Restart the laptop.
3. Reapply only the specific changes from Fix 3 that you need, testing sleep/wake after each.
4. As a final software step, run `sfc /scannow` in the admin Terminal to repair any corrupted power-related system files.

## Closing

DRIVER_POWER_STATE_FAILURE is Windows telling you a driver fumbled a power transition — and on HP laptops, that driver is usually the Wi-Fi, the GPU, or something Windows Update swapped in without asking. Identify it from the crash dump, get HP's proper driver version, and tame the aggressive power settings, and the sleep/wake crashes stop. If your crashes happen at boot instead of during power transitions, see [fixing startup blue screens on HP](/articles/how-to-fix-bsod-on-startup-windows-11-on-hp-laptop/); for the broader driver-focused approach, [driver power state failure step by step](/articles/how-to-fix-driver-power-state-failure-step-by-step/) covers the same ground in checklist form.
