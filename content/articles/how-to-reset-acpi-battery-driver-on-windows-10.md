---
title: "How to Reset the ACPI Battery Driver on Windows 10"
slug: how-to-reset-acpi-battery-driver-on-windows-10
date: 2026-10-08
categories: ["battery"]
tags: ["ACPI driver", "device manager", "windows 10", "battery driver"]
description: "A corrupted ACPI battery driver causes wrong percentages, missing icons, and charging glitches. Reset it properly in minutes."
thumbnail: "/images/thumbs/how-to-reset-acpi-battery-driver-on-windows-10.webp"
faqs:
  - q: "What is the ACPI battery driver?"
    a: "The Microsoft ACPI-Compliant Control Method Battery driver is Windows' translator for your battery — it reads charge level, charging state, and capacity from the battery's controller and reports it to the system. When it corrupts, you get wrong percentages, missing battery icons, phantom 'not charging' messages, and sometimes a completely undetected battery."
  - q: "Is it safe to uninstall the ACPI battery driver?"
    a: "Yes. Windows reinstalls it automatically the moment you scan for hardware changes or reboot — it is a standard inbox driver, not something you can permanently break. The laptop keeps running on AC power throughout, so there is no risk of shutdown mid-process."
  - q: "How often should I reset the battery driver?"
    a: "Only when troubleshooting — it is a fix, not maintenance. If you find yourself resetting it monthly, something deeper is wrong: a Windows update keeps breaking it, the battery controller is flaky, or the BIOS needs updating. Fix the root cause instead of repeating the reset."
  - q: "Will resetting the driver delete my battery calibration?"
    a: "No. Calibration data lives in the battery's own controller and the firmware, not in the Windows driver. Resetting the driver only refreshes Windows' communication channel — your charge history and gauge calibration survive intact."
---

The ACPI battery driver is the quiet middleman between Windows and your battery. When it works, you never think about it. When it corrupts — usually after a Windows update, a bad shutdown, or a driver conflict — the symptoms are bizarre and varied: a frozen percentage, a vanished battery icon, "plugged in, not charging" on a healthy battery, or Windows claiming no battery exists at all.

Resetting it takes about two minutes and fixes an outsized share of battery weirdness on Windows 10. This guide shows the proper way to do it — plus what to try when a simple reset is not enough. If your driver issues come with a missing battery, our [battery not detected guide](/articles/how-to-fix-no-battery-detected-after-windows-update-on-lenovo-laptop/) pairs well with this one.

## Why this happens

- **Windows update replaced or corrupted the driver.** The most common trigger by far.
- **Bad shutdown left driver state inconsistent.** A crash or forced power-off mid-write can corrupt it.
- **Conflicting power-management software.** Manufacturer tools fighting Windows over battery control.
- **Driver version mismatch.** A new Windows build with an old driver, or vice versa.
- **Corrupted driver store.** System file corruption in the driver repository.
- **BIOS/firmware changed the battery interface.** The driver no longer matches what the firmware reports.
- **Fast startup preserved a bad driver state.** Hybrid shutdowns can reload the same corrupted driver session after session until you do a full restart.

## How to fix it

Work through these in order — start with Fix 1 and only move on if symptoms persist.

### Fix 1: Uninstall and reinstall via Device Manager

Open **Device Manager** (press **Win + X** and select it). Expand **Batteries**. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. If you see a checkbox for deleting the driver software, check it — this forces Windows to install a truly fresh copy rather than reusing the corrupted one. If **Microsoft AC Adapter** is listed, uninstall it too. Now click **Action > Scan for hardware changes** in the Device Manager menu bar. Both devices reinstall within seconds. Restart the laptop and check whether your battery symptoms are gone.

### Fix 2: Do it with the battery out (removable batteries)

For a deeper reset, shut down completely and unplug the adapter. Remove the battery. Plug in the adapter only and boot into Windows. Open **Device Manager > Batteries** and uninstall the ACPI battery device as in Fix 1, then shut down. Reinstall the battery, plug in, and boot. Windows now discovers the battery hardware completely fresh — new hardware detection plus new driver, with no stale state surviving. This variant fixes cases where the in-place reinstall did not take.

### Fix 3: Drain flea power with a hard reset

Shut down, unplug everything, and remove the battery if removable. Press and hold the power button for a full 30 seconds — this drains residual "flea power" from the motherboard capacitors and resets the embedded controller that the ACPI driver talks to. Reconnect the adapter, boot, and let Windows reinstall the battery drivers via **Action > Scan for hardware changes** if needed. The EC reset matters because the driver is only half the conversation; the firmware side needs clearing too.

### Fix 4: Update the driver from Windows Update and the manufacturer

Sometimes the inbox driver is simply outdated for your hardware. In **Device Manager**, right-click the ACPI battery device, choose **Update driver > Search automatically for updated drivers**. Then visit your manufacturer's support site and install the latest **chipset** driver package for your exact model — chipset packages include the power-management interfaces the battery driver depends on. Reboot after installing. If a Windows update caused the original corruption, check [Microsoft's Update Catalog](https://www.catalog.update.microsoft.com/) for a revised driver that supersedes the bad one.

### Fix 5: Repair system file corruption

If the driver keeps corrupting, the driver store itself may be damaged. Open an elevated **Command Prompt** (search "cmd", right-click, **Run as administrator**) and run:

```
sfc /scannow
```

Wait for it to finish — 10 to 20 minutes — then reboot and reinstall the battery driver once more via Device Manager. If SFC found and fixed corruption, the fresh driver install should now stick. For deeper damage, run `DISM /Online /Cleanup-Image /RestoreHealth` first, then SFC, then the driver reinstall. Microsoft documents these repair tools at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Update the BIOS to match the driver

The ACPI driver talks to firmware, and mismatches cause chronic issues. Download the latest **BIOS** for your exact model from the manufacturer's support site and flash it with the adapter connected — do not interrupt the process. After the update, boot into Windows, uninstall and reinstall the ACPI battery driver one final time so the driver and firmware handshake from a clean state on both sides. This resolves the stubborn cases where the driver "works" but reports garbage.

### Fix 7: Check for software conflicts

Open **Settings > Apps > Installed apps** and look for multiple battery or power-management tools — old manufacturer utilities alongside new ones, or third-party "battery optimizers." Uninstall everything except the current manufacturer app (or nothing at all if you do not need it). These tools hook into the same ACPI interfaces and can recorrupt the driver or feed Windows conflicting data. After cleaning up, do one final driver reinstall from Fix 1 and restart. Our [ACPI reset on Windows 11](/articles/how-to-reset-acpi-battery-driver-on-windows-11/) covers the same procedure with Windows 11 screenshots.

## Closing

The ACPI battery driver is small, but when it breaks, everything battery-related breaks with it — which is exactly why resetting it fixes so many different symptoms. Two minutes in Device Manager resolves most cases; the deeper variants here cover the rest. And remember to do a full **Restart** (not shutdown) after the reset if you use fast startup, so the fresh driver actually loads. If you are resetting it repeatedly, stop and fix the root cause — usually a pending BIOS update or a conflicting utility — because a driver that keeps corrupting is a symptom, not the disease.
