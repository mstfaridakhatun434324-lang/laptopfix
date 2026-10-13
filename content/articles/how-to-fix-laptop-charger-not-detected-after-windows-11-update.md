---
title: "Laptop Charger Not Detected After a Windows 11 Update? Restore Detection"
slug: how-to-fix-laptop-charger-not-detected-after-windows-11-update
date: 2026-09-16
categories: ["battery"]
tags: ["charger not detected", "windows 11 update", "drivers"]
description: "Windows 11 update no longer sees your charger? Fix adapter detection with driver resets, BIOS checks, and hardware tests."
thumbnail: "/images/thumbs/how-to-fix-laptop-charger-not-detected-after-windows-11-update.webp"
faqs:
  - q: "What does it mean when Windows doesn't detect the charger?"
    a: "Windows shows no charging icon, the battery icon may disappear or show only battery, and the laptop runs purely on battery despite the adapter being plugged in. The break can be software (drivers, EC state) or hardware (dead adapter, broken port)."
  - q: "How can I tell if the charger is dead or Windows is confused?"
    a: "Check the charger's LED if it has one, try the adapter on another compatible laptop, and watch the BIOS setup screen — most BIOS versions show adapter status. If BIOS sees the adapter but Windows doesn't, it's software. If neither sees it, it's hardware."
  - q: "Can a Windows update kill charger detection?"
    a: "It can break the software side: replacing ACPI drivers, corrupting the battery driver stack, or delivering firmware that changes EC behavior. It cannot damage the physical adapter or port — if hardware is dead, the timing was coincidence."
  - q: "Should I try a different charger before troubleshooting software?"
    a: "Yes, if one is available. A 30-second test with a known-good adapter of the correct wattage instantly splits the problem in half: if it detects, your adapter is dead; if not, the laptop or its software is the issue."
---
This is a step beyond "plugged in, not charging" — here Windows doesn't acknowledge the charger at all. No icon change, no LED, the battery just keeps draining as if nothing is plugged in. When it starts right after a Windows 11 update, the instinct is to blame the update, and sometimes that's right. But an adapter can also die coincidentally, so the first job is splitting hardware from software.

Work this sequence — it isolates the fault fast.

## Why this happens

- **ACPI drivers replaced or corrupted by the update.** Windows can't enumerate the adapter without working ACPI drivers.
- **Embedded controller stuck.** The EC reports adapter presence; a stuck EC reports nothing.
- **Dead adapter.** The brick failed — no output, no detection.
- **Broken charging port or cable.** Physical damage severs the connection.
- **BIOS adapter validation failing.** Dell and others reject adapters that fail identification.
- **Battery driver stack corrupt.** The Batteries device class in a bad state can hide adapter status.
- **Firmware mismatch after update.** New firmware expects drivers the update didn't install.

## How to fix it

Work through these in order.

### Fix 1: Check the BIOS — hardware or software?

Restart and enter BIOS setup (**F2**, **F10**, **Del**, or **F12** boot menu depending on brand). Look for **Battery Information**, **Adapter Type**, or **Power** status. This is the great divider:

- **BIOS sees the adapter, Windows doesn't:** software problem. Continue with Fixes 2–5.
- **BIOS doesn't see it either:** hardware problem. Skip to Fixes 6–7.

Write down what the BIOS reports — you'll need it later.

### Fix 2: Reset the EC and driver stack together

1. Shut down fully (hold **Shift** while clicking **Shut down**).
2. Unplug the charger and all peripherals.
3. Hold the power button 30–60 seconds.
4. Boot into Windows, open **Device Manager** (**Win + X**).
5. Expand **Batteries**, uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
6. **Action > Scan for hardware changes**, then restart.

The EC reset restores adapter reporting at the firmware level; the driver reinstall restores it at the Windows level. Test detection after the reboot by plugging in the charger and watching the taskbar icon.

### Fix 3: Roll back or update the chipset drivers

The update may have installed a broken chipset or ACPI driver.

1. In **Device Manager**, expand **System devices** and look for **Intel(R) Management Engine Interface**, **AMD SMBus**, or chipset entries with warning icons.
2. Right-click → **Properties > Driver** → **Roll Back Driver** if available.
3. If not, download the latest **chipset** driver from your manufacturer's support site (or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)) and install it.

Chipset drivers own the low-level communication the battery stack depends on. A bad one breaks adapter detection silently.

### Fix 4: Check Windows Update for the fix

Ironic but common: the update that broke detection is followed days later by the driver update that fixes it.

1. Go to **Settings > Windows Update** and install everything pending.
2. Click **Advanced options > Optional updates** and install any driver updates listed — especially anything mentioning ACPI, chipset, battery, or firmware.
3. Restart and test.

Also check your manufacturer's update utility (Vantage, SupportAssist, MyASUS, HP Support Assistant) — vendor drivers often arrive there before Windows Update.

### Fix 5: Run the power troubleshooter and SFC

1. **Settings > System > Troubleshoot > Other troubleshooters** → run **Power**.
2. Then, in an elevated Command Prompt, check system file integrity:

```
sfc /scannow
```

3. Follow with:

```
DISM /Online /Cleanup-Image /RestoreHealth
```

Corrupt system files can break the power subsystem's ability to report adapter state. These commands repair the OS layer without touching your files. Microsoft documents this repair sequence at [support.microsoft.com](https://support.microsoft.com/en-us/windows).

### Fix 6: Test the adapter hardware

If BIOS didn't see the adapter (Fix 1), test the hardware:

1. Check for an LED on the brick — no light with a live outlet means a dead adapter.
2. Inspect the cable and connector for damage.
3. Try a known-good adapter with the correct voltage and equal-or-higher wattage.
4. Try your adapter on another compatible laptop if possible.

If a good adapter is detected, yours is dead — replace it with the correct spec. If no adapter is detected by BIOS, the charging port, DC jack, or motherboard circuit is faulty.

### Fix 7: Inspect the charging port and get the verdict

With the laptop off and unplugged, examine the charging port with a flashlight: bent pins, debris, looseness, or scorch marks. For USB-C, check for lint packed in the port. If the port is damaged, or if BIOS detects no adapter across multiple known-good chargers, it's a hardware repair — DC jack replacement or board-level work at a shop. For the battery-health side of the aftermath, run [a battery report](/articles/how-to-check-battery-health-on-windows-11-laptop/) once charging is restored to make sure the outage didn't mask a worn pack.

### Fix 8: Repair Windows with an in-place upgrade

When drivers, EC resets, and chipset updates all fail to restore adapter detection, the OS power subsystem itself may be damaged beyond component-level repair. An in-place upgrade reinstalls Windows 11 over itself while keeping files, apps, and settings: download the official Windows 11 ISO from Microsoft, mount it, run **setup.exe**, and choose **Keep personal files and apps**. The process takes 30–90 minutes and rebuilds the entire system component store, including the ACPI and power management stack the update broke. Afterward, reinstall your manufacturer's chipset drivers before testing the charger again. This fixes the stubborn minority of cases where `sfc /scannow` and DISM reported clean but detection stayed broken. Back up important files first regardless — and if detection still fails after a repair install while the adapter shows in BIOS, revisit the [battery driver refresh steps](/articles/how-to-fix-laptop-battery-not-charging-after-windows-11-update/) for a related charging fault that sometimes travels with this one.

## Closing

Charger-not-detected after an update is a fork in the road, and the BIOS screen is the signpost: adapter visible there means Windows is confused (drivers, EC, chipset — all fixable in software); invisible there means hardware (adapter, port, board). Take the right fork and you stop wasting time on the wrong half of the problem.
