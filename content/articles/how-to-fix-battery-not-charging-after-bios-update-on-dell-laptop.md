---
title: "Dell Laptop Battery Not Charging After a BIOS Update? Fix It"
slug: how-to-fix-battery-not-charging-after-bios-update-on-dell-laptop
date: 2026-09-14
categories: ["battery"]
tags: ["battery", "charging", "dell", "bios"]
description: "Dell battery stopped charging right after a BIOS update? Recover with these 7 steps — BIOS rollback, EC reset, and Dell diagnostics."
thumbnail: "/images/thumbs/how-to-fix-battery-not-charging-after-bios-update-on-dell-laptop.webp"
faqs:
  - q: "Can a BIOS update break battery charging on a Dell?"
    a: "Yes. The BIOS update also flashes the embedded controller firmware that manages charging. If the new EC firmware has a bug, misdetects the adapter, or reset battery settings to defaults, charging can stop. Dell occasionally pulls problematic BIOS versions for exactly this reason."
  - q: "Should I roll back the Dell BIOS?"
    a: "If charging worked before the update and broke immediately after, rolling back is the most direct fix. Dell allows BIOS downgrades on most models — download the previous version from Dell support and flash it the same way. Only do this if you're confident the update caused it."
  - q: "What is the Dell battery health setting in BIOS?"
    a: "Under Power Management in Dell BIOS setup, the battery health/charging behavior setting includes options like Standard, ExpressCharge, Adaptive, and Primarily AC Use. A BIOS update can reset this — Primarily AC Use, for example, may limit charging behavior in ways that look like a fault."
  - q: "Will Dell fix a bad BIOS that broke charging?"
    a: "Dell typically releases a corrected BIOS quickly when a version causes widespread issues, and their support can confirm whether your version is affected. Check Dell's support site for a newer BIOS and read the release notes for battery or charging mentions."
---

The sequence is damning: your Dell charged perfectly, you installed a BIOS update, and now the battery won't charge. Windows says "plugged in, not charging," or the percentage sits frozen. BIOS updates touch the embedded controller — the chip that physically manages charging — so a bad flash, a buggy EC firmware, or reset battery settings can absolutely break charging overnight.

The good news: because the cause is a firmware change, the fix is usually a firmware-level correction — rolling back, reflashing, or resetting what the update changed. These seven steps are Dell-specific and ordered from least to most invasive. Resist the urge to start with the BIOS rollback; the settings check and EC reset in the first three steps fix a large share of cases with far less risk.

## Why this happens

- **Buggy EC firmware in the new BIOS.** The embedded controller code bundled with the update may mishandle charge negotiation on your specific hardware revision.
- **Battery settings reset to defaults.** The update can reset BIOS power management options — like switching to "Primarily AC Use" — changing charge behavior.
- **Adapter misdetection after the flash.** New firmware can fail to recognize a third-party or aging adapter, and Dell throttles charging with unrecognized adapters.
- **A bad flash.** An interrupted or glitched BIOS update can leave the EC in a partially updated, malfunctioning state.
- **Battery health settings changed.** Options like Adaptive charging or charge thresholds may have been altered by the update.
- **Coincidental battery failure.** Rare, but verify — don't flash firmware repeatedly chasing a dead pack.

## How to fix it

Work through these in order.

### Fix 1: Check the BIOS battery settings the update may have reset

The update may have simply changed a setting.

1. Restart and press **F2** repeatedly to enter BIOS setup.
2. Go to **Power Management** (or **Power**) and find the battery charging behavior / battery health setting.
3. If it's set to **Primarily AC Use** or a custom threshold, change it to **Standard** or **Adaptive**.
4. Check for any **Battery Charge Configuration** with start/stop thresholds and disable them for testing.
5. Save, exit, boot into Windows, and check charging.

### Fix 2: Verify the adapter is still recognized

Dell is strict about adapter identification.

1. In BIOS setup (**F2**), look at the main page — it shows **AC Adapter Type**.
2. If it says **Unknown** or **None** with the charger connected, the new firmware isn't recognizing your adapter.
3. Test with a genuine Dell adapter of the correct wattage. If a genuine adapter is recognized and charging resumes, the update tightened adapter validation.
4. With an unrecognized adapter, Dell laptops typically run but refuse to charge — exactly your symptom. A genuine Dell adapter from [dell.com/support](https://www.dell.com/support) parts is the fix.

### Fix 3: Reset the embedded controller

Clear any stuck EC state from the flash.

1. Shut down the laptop and unplug the charger. Remove the battery if it's removable.
2. Hold the power button for 60 seconds.
3. Reconnect the charger (no battery if removable), wait a minute, power on.
4. Shut down, reinsert the battery, boot normally.
5. Check whether charging resumes. EC resets resolve many post-flash charging glitches.

### Fix 4: Reflash the same BIOS version

A clean reflash fixes a bad flash.

1. Download the same BIOS version you installed from [Dell support](https://www.dell.com/support) for your exact model (service tag).
2. Run the installer with the charger connected and the battery installed.
3. Let it complete without interruption — don't touch the machine.
4. Sometimes the first flash glitched the EC region; a second clean flash writes it correctly.
5. Test charging after the reboot.

### Fix 5: Roll back to the previous BIOS version

If the new version is the problem, go back.

1. On Dell support, find the **previous** BIOS version for your model in the version history.
2. Download it. Dell's flash utility generally permits downgrades, though it will warn you.
3. Flash with the charger connected. If the utility refuses the downgrade, check BIOS setup for a **BIOS Downgrade** or **Allow BIOS Downgrade** option and enable it first.
4. After rolling back, verify charging works.
5. Then check periodically for a newer BIOS with fixed battery behavior before updating again — read the release notes.

### Fix 6: Run Dell's built-in battery diagnostics

Confirm the battery itself survived the update.

1. Restart, press **F12**, select **Diagnostics**.
2. Run the full diagnostic, paying attention to the **battery** test results.
3. You can also run Dell's **SupportAssist** battery test from within Windows.
4. If diagnostics report battery failure, the timing was coincidence — replace the pack. If they pass, the problem is firmware-side, and Fix 7 is next. For ongoing capacity questions, [learn to read the battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/). BIOS-update charging issues aren't unique to Dell either — [Lenovo laptops hit the same problem](/articles/how-to-fix-battery-not-charging-after-bios-update-on-lenovo-laptop/).

### Fix 7: Reinstall chipset and power drivers in Windows

The new BIOS may need matching Windows-side drivers.

1. From Dell support for your model, download the latest **chipset driver**, **Intel Management Engine**, and **Dell Power Manager** (if applicable).
2. Install them in that order, restarting as prompted.
3. In **Device Manager > Batteries**, uninstall **Microsoft ACPI-Compliant Control Method Battery**, then restart so Windows rebinds it against the new firmware.
4. Test charging. Matched firmware + drivers resolve the remaining stubborn cases.

## Closing

A Dell that stops charging right after a BIOS update is a firmware problem until proven otherwise — check the reset settings, verify adapter recognition, reflash or roll back, and let Dell's diagnostics rule out the battery. And the lesson for next time: read the BIOS release notes before flashing, especially the lines about battery, EC, and power. A two-minute read can save you an afternoon of recovery. And if Dell ever pulls the problematic BIOS version — which they do when a release causes widespread issues — take it as confirmation your diagnosis was right, and wait for the corrected release before updating again. Patience with BIOS updates is a virtue; the early adopters are the beta testers. Your charging works again — that's what matters.
