---
title: "How to Reset the ACPI Battery Driver on Windows 11"
slug: how-to-reset-acpi-battery-driver-on-windows-11
date: 2026-09-02
categories: ["battery"]
tags: ["acpi battery driver", "battery driver reset", "windows 11 battery fix"]
description: "Reset the ACPI battery driver on Windows 11 to fix not-charging, stuck percentages, and phantom drain with this step-by-step driver reinstall guide."
thumbnail: "/images/thumbs/how-to-reset-acpi-battery-driver-on-windows-11.webp"
faqs:
  - q: "Is it safe to uninstall the Microsoft ACPI-Compliant Control Method Battery driver?"
    a: "Yes. Windows reinstalls it automatically on the next reboot. This is a standard, manufacturer-approved troubleshooting step. The driver only reports battery state — removing it does not affect power delivery, and your data is never at risk during the process."
  - q: "Will resetting the ACPI battery driver fix a battery stuck at a percentage?"
    a: "Often, yes. A stuck percentage is frequently a reporting glitch in the driver rather than a real battery fault. Reinstalling the driver forces Windows to re-read the battery gauge from the firmware, which corrects frozen or jumping percentages in most cases."
  - q: "Do I need to be plugged in when I reset the driver?"
    a: "It is best to have the charger connected. While the driver is uninstalled, Windows cannot accurately report battery level, so keeping AC power attached avoids any chance of the machine dying mid-reboot if the battery is low."
  - q: "How long does a battery driver reset take?"
    a: "About five minutes. Uninstalling takes under a minute, the restart takes two to three, and Windows rebuilds the driver entries automatically during boot. You may need one extra full charge cycle to confirm the reporting is accurate again."
---
Plug your charger in, glance at the battery icon, and nothing changes — the percentage is frozen, the "plugged in, not charging" message taunts you, or the level jumps ten points in a minute. Nine times out of ten this isn't a dying battery. It's the Microsoft ACPI-Compliant Control Method Battery driver, the small piece of software Windows uses to talk to your battery's firmware, feeding the system bad information.

Resetting this driver is one of the safest and fastest battery fixes on Windows 11. It takes about five minutes, touches none of your files or settings, and forces Windows to rebuild its communication channel with the battery from scratch. Below is exactly how to do it, plus what to try if the reset alone doesn't finish the job.

## Why this happens

- **Corrupted driver state after an update:** Windows 11 feature updates and driver rollouts sometimes leave the ACPI battery driver half-configured, so it reports stale or impossible values.
- **Firmware/driver handshake mismatch:** The battery's embedded controller and Windows can fall out of sync, especially after a BIOS update, causing the gauge to freeze or jump.
- **Multiple conflicting driver entries:** Sometimes Device Manager shows two or three battery entries (including a generic "Microsoft AC Adapter"), and duplicates fight over which one reports state.
- **Residual state from hibernation:** A botched resume from hibernation can lock the driver's last-known reading in place until it is forcibly reinstalled.
- **Aggressive power-plan tweaks:** Third-party battery tools and OEM utilities can write settings the driver doesn't expect, leading to "plugged in, not charging" even on healthy hardware.

## How to fix it

Work through these in order. Most people are done after the first fix.

### Fix 1: Uninstall and reinstall the ACPI battery driver

This is the core reset. Windows rebuilds the driver automatically on reboot, which clears corrupted state.

1. Press **Win + X** and choose **Device Manager** from the menu.
2. Expand the **Batteries** section.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and select **Uninstall device**.
4. In the confirmation dialog, click **Uninstall**. Do **not** check any box about deleting driver software if one appears.
5. If you see a second ACPI battery entry or **Microsoft AC Adapter**, uninstall those too.
6. Shut the laptop down fully — click **Start**, then **Power**, then **Shut down** (don't use Restart, a cold boot is cleaner here).
7. Unplug the charger, wait 30 seconds, plug it back in, then power on.
8. Once Windows boots, open **Device Manager** again and confirm the **Batteries** entries reappeared.

Your battery icon should now report live values. Run `powercfg /batteryreport` from an elevated **Command Prompt** afterward if you want to verify that charge history looks sane again — this is the same report method described in our guide to [generating a battery report with powercfg](/articles/how-to-generate-battery-report-windows-11-powercfg/).

### Fix 2: Scan for hardware changes without rebooting

If a full reboot is inconvenient, Device Manager can rebuild the driver entry immediately.

1. In **Device Manager**, right-click your computer name at the top of the tree and choose **Scan for hardware changes**.
2. Watch the **Batteries** section — the ACPI entries should reappear within seconds.
3. Unplug and replug the charger, then check whether the battery percentage updates normally.

This is a lighter version of Fix 1. If the reading freezes again within a day or two, do the full uninstall-plus-shutdown instead — the cold boot matters.

### Fix 3: Run the built-in power troubleshooter

Windows 11 still ships a power troubleshooter that can detect driver-level power reporting faults.

1. Open **Settings** with **Win + I**.
2. Go to **System** > **Troubleshoot** > **Other troubleshooters**.
3. Find **Power** and click **Run**.
4. Apply whatever fixes it recommends, then restart when prompted.

The troubleshooter sometimes resets power policies that the driver depends on. It's worth the two minutes even if it reports "no issues found," because it also validates the power plan database. For deeper drain investigations, see our walkthrough on [finding which app is draining your battery](/articles/best-way-to-find-which-app-is-draining-battery/).

### Fix 4: Update the chipset and battery drivers from the manufacturer

A reset helps only if the underlying driver files are healthy. Pull fresh ones from your laptop maker's support site.

1. Find your exact model on your manufacturer's support page — for example [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
2. Download the latest **chipset** driver and any **power management** or **battery** driver listed for Windows 11.
3. Install the chipset driver first, reboot, then install the battery/power driver.
4. Repeat **Fix 1** afterward so the new files get a clean install.

OEM drivers often include firmware interface updates that Microsoft's inbox driver lacks, and they fix reporting bugs the generic reset can't touch.

### Fix 5: Reset the power plan to defaults

A corrupted power plan can feed the driver bad thresholds, producing "not charging" messages on perfectly good hardware.

1. Open an elevated **Command Prompt** (search **cmd**, right-click, **Run as administrator**).
2. Type `powercfg -restoredefaultschemes` and press Enter.
3. Restart the laptop.
4. Go to **Settings** > **System** > **Power & battery** and re-check your power mode.

Your screen-timeout and sleep settings will return to defaults, so note them down first if you've customized them.

### Fix 6: Update the BIOS

If driver resets keep failing, the battery's embedded controller firmware may be the culprit. A BIOS update refreshes that firmware.

1. Check your current BIOS version with `msinfo32` (look at the **BIOS Version/Date** line).
2. Compare it against the newest release on your manufacturer's support page.
3. Download the BIOS updater, run it with the charger connected, and let it finish without touching anything.
4. After the update, perform **Fix 1** once more so Windows renegotiates with the refreshed firmware.

Never interrupt a BIOS update — a power loss mid-flash can brick the machine. This is a last resort, but it resolves stubborn reporting faults that survive everything else.

## Closing

Resetting the ACPI battery driver is the kind of fix that feels too simple to work until you've watched a frozen 63% start climbing again. Start with the uninstall-and-cold-boot in Fix 1, verify with a battery report, and only escalate to chipset drivers or a BIOS update if the problem keeps coming back. If the percentage still misbehaves after all six fixes, you're likely looking at a genuinely worn battery — and that's a hardware conversation, not a software one.
