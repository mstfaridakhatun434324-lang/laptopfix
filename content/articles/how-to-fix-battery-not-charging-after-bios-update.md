---
title: "How to Fix Battery Not Charging After a BIOS Update"
slug: how-to-fix-battery-not-charging-after-bios-update
date: 2026-09-21
categories: ["battery"]
tags: ["BIOS update", "not charging", "firmware"]
description: "Battery stopped charging right after a BIOS update? The update reset EC settings or broke the driver handshake — here's how to recover."
thumbnail: "/images/thumbs/how-to-fix-battery-not-charging-after-bios-update.webp"
faqs:
  - q: "Can a BIOS update stop my battery from charging?"
    a: "Yes. BIOS updates reflash the embedded controller firmware that manages charging, and they can reset battery calibration data, charge thresholds, and EC settings to defaults. They can also change how the firmware identifies the battery to Windows, which confuses the driver stack."
  - q: "Should I roll back the BIOS to fix charging?"
    a: "Try everything else first. Rolling back a BIOS carries its own risks and many manufacturers discourage it. In most cases, loading BIOS defaults, resetting the EC, and reinstalling the battery drivers restores charging without a rollback."
  - q: "Why does Windows say no battery detected after a BIOS update?"
    a: "The new firmware may report the battery hardware ID differently, so Windows' old driver binding no longer matches. Uninstalling the battery devices in Device Manager and letting Windows rediscover them usually resolves the mismatch."
  - q: "How do I prevent BIOS updates from breaking charging?"
    a: "You cannot fully prevent it, but you can reduce the risk: keep the charger connected during the update, note your battery settings beforehand so you can restore them, and check the manufacturer's release notes for known battery issues before installing."
---

Everything was fine, you installed a BIOS update, and now the battery will not charge. The timing is not a coincidence: a BIOS update rewrites the firmware that controls charging — the embedded controller tables, calibration data, and threshold settings all live there. When the new firmware comes up with different defaults or a changed hardware ID, Windows and the battery stop understanding each other.

The encouraging part is that the battery itself is almost certainly fine; it charged yesterday. This is a configuration and handshake problem, and it responds well to resets. Do not roll back the BIOS as your first move — work through the recovery steps below first.

## Why this happens

- **EC settings reset:** The update restores embedded-controller charging parameters to factory defaults, wiping custom thresholds and calibration.
- **Changed hardware ID:** New firmware can report the battery differently, breaking Windows' existing driver binding.
- **Calibration data lost:** Battery gauge tables stored in firmware may be cleared by the flash.
- **New firmware bug:** Occasionally the update itself introduces a charging regression the manufacturer later patches.
- **Driver mismatch:** Windows' battery drivers were tuned to the old firmware's behavior.
- **Interrupted update:** A flicker of power during the flash can leave the EC in a half-configured state.

## How to fix it

Work through these in order — start with the gentle resets before considering a rollback.

### Fix 1: Load optimized BIOS defaults

The new firmware may be running on stale settings carried over from the old version.

1. Restart and enter the BIOS setup (**F2**, **F10**, **Delete**, or **F1** depending on brand).
2. Find the **Load Optimized Defaults** or **Load Setup Defaults** option — usually on the **Exit** tab.
3. Apply it, then **Save and Exit**.
4. Boot into Windows and check whether charging has resumed.
5. If your BIOS has battery-specific options (thresholds, health modes), reconfigure them now, since defaults may have wiped your preferences.

### Fix 2: Reset the embedded controller

Clear any half-configured EC state left by the update.

1. Shut down completely and unplug the charger and all peripherals.
2. Hold the power button for **30 to 45 seconds**.
3. If your model has a pinhole EC reset button on the bottom, press it for 30 seconds with a paperclip.
4. Wait two minutes, reconnect the charger, and power on.
5. Give Windows a few minutes after boot — the EC and OS renegotiate the battery state during early startup.

### Fix 3: Reinstall the battery drivers

Fix the Windows side of the firmware handshake.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries** and uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. Shut down fully (not restart), unplug for 30 seconds, then reconnect and boot.
4. Windows rediscovers the battery against the new firmware and builds fresh driver bindings.
5. Check the battery icon and Device Manager for a clean, warning-free battery device.

### Fix 4: Recalibrate the battery

Restore the gauge tables the update may have cleared.

1. Charge to **100 percent** and leave plugged in for **2 hours**.
2. Unplug and drain through normal use until the laptop shuts down on its own.
3. Leave it off and unplugged for **3 hours**.
4. Recharge uninterrupted to **100 percent**.
5. This rebuilds the calibration data in the new firmware. For the detailed procedure, see [how to calibrate a laptop battery](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 5: Check for a follow-up BIOS or EC update

The manufacturer may have already fixed the regression.

1. Visit your maker's support site — [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/) — and check for a BIOS newer than the one that broke charging.
2. Read the release notes for mentions of battery, charging, EC, or power fixes.
3. If a newer version exists, install it with the charger connected and the battery at a healthy level.
4. After updating, repeat Fix 1 (load optimized defaults) before judging the result.
5. Our model-specific guide covers [battery not charging after a BIOS update on Lenovo](/articles/how-to-fix-battery-not-charging-after-bios-update-on-lenovo-laptop/) if that is your brand.

### Fix 6: Verify the battery is still detected correctly

Confirm the firmware actually sees the pack.

1. Enter the BIOS setup and look for a **Battery Information** or **Battery Health** page — most modern BIOSes show the pack's presence and charge level.
2. If the BIOS itself shows no battery, the issue is below the OS: reseat the battery if accessible, or have the connector checked.
3. If the BIOS sees the battery but Windows does not, the problem is the driver handshake — repeat Fix 3.
4. In Windows, run `powercfg /batteryreport /output "C:\battery-report.html"` and check whether the report contains current data.
5. A report with fresh timestamps means Windows and the firmware are talking again.

### Fix 7: Consider a BIOS rollback as a last resort

Only when every reset has failed and the release notes admit a regression.

1. Check whether your manufacturer officially supports BIOS rollback — some do via the same update utility, others block downgrades.
2. Download the previous BIOS version from the support site's driver archive.
3. Follow the manufacturer's rollback instructions exactly, with the charger connected throughout.
4. If rollback is blocked or unsupported, contact the manufacturer's support with your model, BIOS versions, and symptom timeline — a confirmed regression often gets escalated to engineering.
5. For the broader "not detected" variant of this problem, see [no battery detected after a Windows update](/articles/how-to-fix-no-battery-detected-after-windows-update-on-windows-11/).

## Closing

A BIOS update breaking charging feels alarming, but it is nearly always a settings-and-handshake problem, not hardware damage. Load BIOS defaults, reset the EC, reinstall the drivers, and recalibrate — that sequence recovers the overwhelming majority of cases. Save the rollback for last, and document your BIOS versions along the way so support can help if it comes to that.
