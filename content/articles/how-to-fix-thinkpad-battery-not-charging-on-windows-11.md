---
title: "ThinkPad Battery Not Charging on Windows 11? Fix It"
slug: how-to-fix-thinkpad-battery-not-charging-on-windows-11
date: 2026-10-13
categories: ["battery"]
tags: ["thinkpad", "not charging", "windows 11"]
description: "ThinkPad refusing to charge on Windows 11? Fix it with Lenovo-specific steps: thresholds, gauge reset, drivers, and the dual-battery quirk."
thumbnail: "/images/thumbs/how-to-fix-thinkpad-battery-not-charging-on-windows-11.webp"
faqs:
  - q: "Why does my ThinkPad say plugged in but not charging on Windows 11?"
    a: "Usually a charge threshold or Conservation Mode is capping the charge, the battery driver is stuck after the Windows 11 upgrade, or the Lenovo Vantage power settings need attention. On dual-battery ThinkPads, one battery may charge while the other waits — which looks like a fault but is normal sequencing."
  - q: "What is the ThinkPad dual-battery charging behavior?"
    a: "Many ThinkPads have internal plus removable (or dual internal) batteries. The controller charges them sequentially — typically the removable one first, then the internal. During the switchover the icon may briefly show not charging. Give it 15 minutes before assuming a fault."
  - q: "Does Lenovo Vantage control charging on Windows 11?"
    a: "Yes. Vantage manages charge thresholds, Conservation Mode, and Battery Gauge Reset on ThinkPads. If Vantage is outdated or its IM Controller driver is missing, these settings fail silently and charging behaves unexpectedly."
  - q: "Should I update the ThinkPad BIOS to fix charging?"
    a: "If driver and Vantage steps don't help, yes. Lenovo ships battery controller fixes in BIOS updates, and Windows 11 upgrades sometimes need a newer BIOS to charge correctly. Always update with the charger connected."
---
ThinkPads have their own charging personality: dual batteries on many models, Conservation Mode, charge thresholds, and Lenovo Vantage sitting between Windows and the hardware. When a ThinkPad stops charging on Windows 11, the cause is usually in that Lenovo layer — not in Windows itself.

This guide works the Lenovo-specific chain first, then the general Windows fixes.

The key insight with ThinkPads: Windows 11 shows you the symptom, but Lenovo's software usually controls the cause. Jumping straight to Windows reinstalls or registry edits wastes time — the threshold, the gauge, and the BIOS are where ThinkPad charging actually lives.

## Why this happens

- **Charge threshold or Conservation Mode active:** Vantage may be capping charge at 60% or a custom limit. After a Windows 11 upgrade, these settings sometimes re-enable themselves.
- **Stuck battery driver:** The Windows 11 upgrade frequently leaves the ACPI battery driver in a bad state on ThinkPads.
- **Dual-battery sequencing:** On two-battery models, the controller charges one pack at a time. The idle battery's "not charging" status is normal, not a failure.
- **Outdated Vantage or IM Controller driver:** Without the interface driver, Vantage can't talk to the battery controller and settings silently fail.
- **Old BIOS:** Battery controller firmware ships with BIOS updates. A pre-Windows-11 BIOS can mishandle charging on the new OS.
- **Worn battery:** ThinkPad batteries are replaceable on many models, which also means they get swapped less often — an original 4-year-old pack may simply be done.

## How to fix it

Work through these in order — Lenovo-specific checks first.

### Fix 1: Check Conservation Mode and thresholds in Vantage

The most common "fault" is a setting doing its job.

1. Open **Lenovo Vantage** and go to **Device > Power**.
2. Check **Conservation Mode** — if it's on, charging stops at 60%. Turn it off if you need a full charge.
3. Check **Battery Charge Threshold** — a custom stop limit (e.g., 80%) produces the same symptom.
4. Disable both temporarily and watch the battery icon for 10 minutes.
5. If charging resumes, it was the setting — re-enable whichever limit you prefer for battery longevity.

### Fix 2: Update Vantage and the IM Controller driver

Vantage can't manage charging without its driver bridge.

1. Update **Lenovo Vantage** from the **Microsoft Store > Library**.
2. In Vantage, go to **System Update** and install everything, especially **IM Controller** / **System Interface Foundation** and **Power Management** drivers.
3. Restart the ThinkPad.
4. Re-check the threshold settings — they sometimes reset during driver updates.

### Fix 3: Reinstall the battery drivers in Device Manager

The standard fix for the stuck "not charging" state.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**.
3. If you see two battery entries (dual-battery model), uninstall both.
4. Uninstall **Microsoft AC Adapter** too.
5. Shut down, unplug for 30 seconds, plug back in, and power on. Windows reinstalls the drivers.

### Fix 4: Run Battery Gauge Reset

Lenovo's built-in tool recalibrates the gauge and can unstick charging logic.

1. Open **Lenovo Vantage > Device > Power > Battery settings**.
2. Click **Battery Gauge Reset** and then **Start**.
3. Keep the charger connected — the process takes several hours and runs a full charge/discharge cycle.
4. Don't interrupt it. When it completes, the gauge is recalibrated and many "not charging" states clear.
5. If the reset fails immediately or won't start, the battery may not be communicating — see our [Lenovo Battery Gauge Reset troubleshooting](/articles/how-to-fix-lenovo-battery-gauge-reset-not-working-on-windows-11/) for the deeper fixes before moving on.

### Fix 5: Update the ThinkPad BIOS

Firmware-level charging fixes ship here.

1. Go to [Lenovo Support](https://support.lenovo.com/us/en/), enter your serial number, and check for a newer **BIOS/UEFI**.
2. Download and run it with the charger connected and battery above 30%.
3. Let it complete without touching the machine — it will reboot automatically.
4. Afterward, re-check Vantage threshold settings, which can reset during BIOS updates.

### Fix 6: Test each battery on dual-battery models

Isolate whether one pack is the problem.

1. If your ThinkPad has a removable external battery, power off and remove it.
2. Boot on the internal battery + charger and check charging.
3. Then test with only the external battery (if the model allows).
4. If one pack charges and the other doesn't, you've found the faulty battery — replacements are inexpensive for most ThinkPads.
5. For single-battery models, generate a battery report (`powercfg /batteryreport`) and check capacity vs. design.

### Fix 7: Perform an EC reset

Clears the embedded controller that manages charging.

1. Shut down completely and unplug the charger and all USB devices.
2. Remove the external battery if present.
3. Hold the power button for **30 seconds**.
4. Reconnect everything and power on.
5. If charging still fails with a known-good Lenovo charger, the charging circuit may need service — check warranty status in Vantage under **Device > Warranty**, and see the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for additional diagnostics.
6. For broader context on ThinkPad power issues, our [Windows 10 ThinkPad charging guide](/articles/how-to-fix-thinkpad-battery-not-charging-after-windows-11-update/) covers the same fixes on the older OS.

### Fix 8: Check the charger identification pin

ThinkPads read a signal from the charger to confirm wattage. A damaged pin means the laptop can't verify the charger and may refuse to charge.

1. Inspect the slim-tip or USB-C connector for bent, recessed, or dirty pins.
2. Clean the connector gently with a dry cotton swab — never metal tools.
3. If you use a USB-C ThinkPad charger, try the other USB-C port; some models only negotiate full wattage on one port.
4. A charger that works on another ThinkPad but not yours points to your laptop's port, not the brick.

## Closing

ThinkPad charging problems live in the Lenovo layer more often than in Windows: thresholds, Vantage, the gauge, and the BIOS. Work that chain first and most "not charging" ThinkPads are back to normal quickly, without ever touching Windows power settings.
