---
title: "Battery Not Charging After a BIOS Update? What to Do"
slug: what-to-do-if-battery-not-charging-after-bios-update
date: 2026-10-10
categories: ["battery"]
tags: ["bios update", "not charging", "firmware", "troubleshooting"]
description: "Battery stopped charging right after a BIOS update? The firmware likely reset a setting or glitched the controller — here's how to recover."
thumbnail: "/images/thumbs/what-to-do-if-battery-not-charging-after-bios-update.webp"
faqs:
  - q: "Can a BIOS update really break battery charging?"
    a: "Yes. BIOS updates rewrite the firmware that controls the embedded controller, charge thresholds, and battery communication. Updates can reset custom settings, introduce EC bugs, or leave the controller in a bad state. The hardware is almost always fine — the firmware configuration just needs correcting."
  - q: "Should I downgrade the BIOS to fix it?"
    a: "Only as a last resort. First try the safer steps: check BIOS battery settings, reset the EC, reinstall battery drivers, and reflash the same BIOS version. Downgrading carries its own risks and some manufacturers block it. If you must, use only the manufacturer's official rollback method."
  - q: "What if the laptop won't stay on without the charger now?"
    a: "Run through the EC reset and driver reinstall steps below — they resolve most cases. If the battery isn't detected at all, the update may have corrupted EC data; reflashing the BIOS (same version) often restores it. Don't panic: this pattern is well documented and usually reversible."
  - q: "How do I prevent this next time?"
    a: "Before any BIOS update: note your BIOS battery/power settings, close all apps, keep the charger connected, and never interrupt the flash. After updating, verify charging works and re-check any custom thresholds or conservation settings, which updates love to reset."
---

Everything was fine, you installed a BIOS update, and now the battery won't charge. The timing makes the cause obvious — but the fix isn't "undo the update." BIOS flashes rewrite the firmware that manages charging: the embedded controller's configuration, battery thresholds, and communication tables. When charging breaks right after a flash, it's almost always a settings reset or a controller left in a bad state, both of which are correctable without exotic measures.

Stay calm, keep the charger plugged in, and work through this recovery sequence.

## Why this happens

- **The update reset BIOS battery settings.** Charge thresholds, conservation modes, and adapter settings often revert to defaults during a flash — and the default may not be what you had.
- **The embedded controller was left in a bad state.** If the flash process didn't cleanly reinitialize the EC, it can refuse to manage charging until reset.
- **New firmware has an EC or charging bug.** Occasionally the update itself introduces a regression. Manufacturers usually follow with a fix, but you need a workaround now.
- **Windows drivers no longer match the firmware.** The ACPI battery driver expects certain firmware tables; a major BIOS revision can change them, confusing the driver.
- **A threshold got silently enabled.** Some BIOS updates enable battery-care caps by default, making it look like charging is broken when it's actually limited.
- **The flash was interrupted or incomplete.** Power loss or a forced shutdown mid-flash can corrupt EC data while leaving the system superficially working.

## How to fix it

Work through these in order. Do not attempt a BIOS downgrade until you've exhausted the safer steps.

### Fix 1: Check BIOS battery settings first

The update probably changed something in here — look before touching anything else.

1. Restart and enter BIOS Setup (**F1**/**F2**/**F10**/**Del** at the logo, depending on brand).
2. Go to the **Power** tab (or **Advanced** > **Power**) and review every battery-related option: charge thresholds, conservation mode, adapter settings, battery health manager.
3. If a threshold or conservation cap got enabled, either disable it or set it to your preference.
4. Look for an option like **Reset to default** vs your previous custom config — restore what you had.
5. Save with **F10**, exit, and test charging in Windows.

### Fix 2: Reset the embedded controller

The EC is the most likely component left in a bad state by the flash.

1. Shut down completely and unplug the charger and all peripherals.
2. Hold the **power button** for 30–60 seconds.
3. If your model has a pinhole battery-reset button on the bottom, press it for 15 seconds with a paperclip.
4. Reconnect only the charger, boot up, and check whether charging resumes.
5. This single step resolves a large share of post-BIOS-update charging failures.

### Fix 3: Reinstall the battery drivers in Windows

Fresh firmware sometimes needs a fresh driver handshake.

1. Press **Win + X** > **Device Manager** > expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. Shut down fully, unplug the charger for 60 seconds, reconnect, and boot.
4. Windows reinstalls the drivers against the new firmware tables.
5. Verify charging starts. If Windows now reports [no battery detected](/articles/laptop-battery-not-detected-windows-11/), continue to the reflash step.

### Fix 4: Reflash the same BIOS version

Reflashing the identical version rewrites the firmware cleanly and reinitializes the EC properly.

1. Go to your manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) and download the exact BIOS version already installed.
2. Close all applications. Keep the charger firmly connected — do not touch the power button during the flash.
3. Run the BIOS update utility and let it complete fully, including the automatic reboot.
4. After booting, re-enter BIOS Setup and confirm your battery settings are as you want them.
5. Test charging. A clean reflash fixes corrupted EC data that the original update left behind.

### Fix 5: Check for a newer BIOS with a fix

If the update introduced a genuine regression, the manufacturer may have already fixed it.

1. Check the support site for a BIOS version newer than what you installed.
2. Read the release notes for mentions of battery, charging, EC, or power — those are the fixes you want.
3. Install the newer BIOS with the charger connected and no interruptions.
4. Re-verify BIOS battery settings afterward, since updates reset them.
5. For the Windows-11-specific variant of this problem, see [battery not charging after BIOS update](/articles/how-to-fix-battery-not-charging-after-bios-update-in-windows-11-24h2/).

### Fix 6: Test with a full power drain cycle

Sometimes the fuel gauge and controller just need to re-sync from a known state.

1. With the charger connected, confirm the current behavior: not charging at all, or stuck at a percentage?
2. If the battery has charge, unplug and run it down to auto-shutdown. Save work first.
3. Leave it off and unplugged for an hour.
4. Plug in and charge uninterrupted. Watch whether the controller picks up charging from the true empty state.
5. If charging works from empty but not from partial, the gauge tables were the issue — now corrected.

### Fix 7: Consider rollback only as a last resort

If everything else failed and charging worked perfectly before the update, a rollback is on the table — carefully.

1. Check whether your manufacturer officially supports BIOS rollback for your model. Some do via the same flash utility; some block downgrades entirely.
2. Never flash a BIOS from an unofficial source. Use only the manufacturer's site.
3. Before rolling back, contact manufacturer support and describe the issue — they may have a targeted fix or be tracking the regression for the next release.
4. If you roll back, re-test charging immediately and re-apply your BIOS battery settings.
5. Report the regression to the manufacturer so the next update actually fixes it.

## Closing

Post-BIOS-update charging failures look scary but are usually firmware-configuration problems, not hardware damage: a reset setting, a stuck controller, or a driver mismatch. Work the recovery stack — BIOS settings, EC reset, driver reinstall, clean reflash — before even thinking about rollback. And next time, screenshot your BIOS power settings before flashing; thirty seconds of prevention beats an hour of recovery.
