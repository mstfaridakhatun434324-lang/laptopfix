---
title: "How to Fix a Battery Not Charging After a BIOS Update"
slug: how-do-i-fix-battery-not-charging-after-bios-update
date: 2026-09-12
categories: ["battery"]
tags: ["BIOS update", "not charging", "firmware", "troubleshooting"]
description: "Battery stopped charging right after a BIOS update? Here's the step-by-step recovery, from EC resets to BIOS rollback."
thumbnail: "/images/thumbs/how-do-i-fix-battery-not-charging-after-bios-update.webp"
faqs:
  - q: "Can a BIOS update break battery charging?"
    a: "Yes. The BIOS contains the firmware for the embedded controller that manages charging. An update can reset charge-limit settings, introduce a firmware bug, or leave the controller in a bad state. The timing — charging worked before, broke immediately after — is the giveaway."
  - q: "How do I roll back a BIOS update?"
    a: "Many manufacturers allow it: Dell lets you flash an older BIOS from a USB drive or the BIOS recovery menu; HP offers BIOS rollback in its update utility; Lenovo provides older versions on the support site. Check your manufacturer's documentation — the process varies and some models block downgrades."
  - q: "Will resetting the BIOS fix charging?"
    a: "Sometimes. Loading optimized defaults clears corrupted settings the update may have left behind, including charge thresholds and power management options. It's safe and takes two minutes, so it's worth trying before a rollback."
  - q: "Should I update the BIOS again to fix it?"
    a: "Check whether the manufacturer has released a newer BIOS since yours — charging bugs are often fixed in the very next release. If your update is already the latest, a re-flash of the same version can also clear a bad flash."
---

Few things are more alarming than a laptop that charged fine yesterday and won't charge today — with the only change being a BIOS update you were told was "important." Your first instinct might be that the update killed the battery, and while that's dramatic, the reality is usually less dire: the update changed firmware settings or left the charge controller confused, both reversible. The good news: when the timing is this clear, the cause is almost certainly firmware, not a coincidental hardware failure. And firmware problems have firmware solutions. Here's the recovery order.

## Why this happens

- **Charge settings reset:** Updates wipe custom BIOS settings, including charge thresholds and battery health modes.
- **EC firmware bug:** The embedded controller firmware in the update mishandles the charging handshake.
- **Incomplete flash state:** An interrupted or glitchy flash leaves the controller in a half-updated state.
- **Driver/firmware mismatch:** The new BIOS expects updated chipset drivers that Windows hasn't installed yet.
- **Battery re-authentication:** Some updates re-run battery authentication and temporarily fail to recognize the battery.
- **Coincidence:** Rarely, the battery genuinely fails at the same time — don't assume it, but don't rule it out either.
- **Secure Boot / firmware policy changes:** Some updates tighten hardware authentication, which can briefly block charging until the battery re-authenticates on a full power cycle.

## How to fix it

Work through these in order, checking whether the battery charges after each one before moving on.

### Fix 1: Confirm the timing

1. Check **Settings > Windows Update > Update history** and your manufacturer's update log for the BIOS version and date.
2. Confirm charging worked before that date — check the battery report's usage history for the last successful charge.
3. If the failure lines up exactly, proceed as a firmware issue with confidence.
4. If charging was already flaky before, treat it as hardware that the update merely exposed.

### Fix 2: Load BIOS defaults

1. Enter BIOS Setup (**F2**, **Del**, or **F10** depending on brand).
2. Choose **Load Optimized Defaults** (often **F9**), then save and exit.
3. This clears any corrupted power settings the update left behind.
4. Boot into Windows and check whether charging resumes.

### Fix 3: Reconfigure battery settings in BIOS

1. Re-enter BIOS Setup and look for battery options: charge thresholds, Battery Health Manager (HP), Battery Health Charging (ASUS), or similar.
2. The update likely reset these to defaults — reapply your preferred settings.
3. If a charge limit got enabled by the reset, that alone explains "not charging."
4. Save, boot, and retest before doing anything more drastic.

### Fix 4: Perform an EC reset

1. Shut down completely and unplug the charger.
2. Hold the **power button for 30-40 seconds** to reset the embedded controller.
3. Plug in and boot — the controller re-initializes against the new firmware cleanly.
4. This resolves the "half-updated controller state" case that a normal reboot doesn't.

### Fix 5: Update chipset drivers and re-flash

1. Install the latest **chipset drivers** from the manufacturer's support site — the new BIOS may depend on them.
2. Check whether a **newer BIOS** has been released since your update; install it if so.
3. If yours is still the latest, **re-flash the same version** — a second clean flash fixes incomplete flashes.
4. Always flash on AC power with the battery installed, and never interrupt the process.

### Fix 6: Reset the battery drivers in Windows

1. Open **Device Manager > Batteries** and uninstall the ACPI battery driver and AC adapter driver.
2. Full shutdown, unplug 60 seconds, boot on AC — Windows rebuilds the driver stack against the new firmware.
3. The new BIOS changed the firmware interface; Windows may still be talking the old way.
4. Our [ACPI reset guide](/articles/how-to-reset-acpi-battery-driver-in-windows-11-24h2/) has the full sequence.

### Fix 7: Roll back the BIOS

1. Check your manufacturer's rollback support: Dell (BIOS recovery via **Ctrl + Esc** at boot), HP (BIOS rollback option), Lenovo (older versions on support site).
2. Download the previous version and follow the manufacturer's rollback procedure exactly.
3. Test charging on the old BIOS — if it works, you've confirmed a firmware regression; report it to the manufacturer.
4. Stay on the old version until a fixed BIOS is released, but don't ignore future updates forever.

### Fix 8: Rule out coincidence with a battery report

1. Run `powercfg /batteryreport` and check wear and recent history.
2. If wear is severe and the timeline is fuzzy, the battery may have genuinely died around the update.
3. Test charging in the BIOS setup screen (outside Windows) — if it won't charge there either on the new BIOS but did before, it's firmware, not the battery.
4. When in doubt, the manufacturer's support line with your timeline gets faster results than guessing.

### Fix 9: Report the regression properly

1. If rollback restores charging, report the bug: note the working BIOS version, the broken version, your exact model, and the symptom timeline.
2. Use the manufacturer's support portal or community forum — firmware teams do track these reports, and charging regressions are high-priority fixes.
3. Subscribe to the BIOS download page for your model so you're notified when a fixed version lands.
4. When the fixed BIOS releases, update promptly — staying on old firmware forever trades one problem for missing security fixes.

### Fix 10: Check the BIOS event log for battery errors

1. Enter BIOS Setup and look for an **Event Log**, **System Log**, or **BIOS Event** page — most Dell, HP, and Lenovo firmware keeps one.
2. Look for battery-related entries around the update date: authentication failures, charge-circuit errors, or thermal events.
3. An authentication failure entry points at the battery re-authentication issue — a full EC reset (Fix 4) followed by a complete power-off charge usually clears it.
4. A charge-circuit error that appeared exactly at the update is strong evidence for a firmware regression — include the exact log text when you report it to the manufacturer, since it tells their firmware team precisely where to look.

## Closing

A charging failure with a BIOS update timestamp on it is a firmware problem until proven otherwise — and firmware problems are fixable without new parts. Load defaults, reconfigure battery settings, EC-reset, update drivers, and only then consider rollback. Document the BIOS versions involved; if you report the regression, that detail is what gets it fixed in the next release. And next time, check the BIOS changelog for battery or power mentions before updating — a little caution beats a recovery session every time. When in doubt, wait a week after a BIOS release and check the manufacturer's forum for reports before flashing — early adopters make the best canaries.

For the diagnostic approach to the same symptom, see [troubleshooting battery charging failures after a BIOS update](/articles/troubleshoot-battery-not-charging-after-bios-update/). Manufacturer BIOS downloads: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
