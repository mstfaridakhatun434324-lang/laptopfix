---
title: "Fix HP Laptop Battery Not Charging After a BIOS Update"
slug: how-to-fix-battery-not-charging-after-bios-update-on-hp-laptop
date: 2026-09-23
categories: ["battery"]
tags: ["hp bios update", "battery not charging", "hp laptop"]
description: "HP laptop stopped charging right after a BIOS update? The update likely reset battery settings — here is how to get charging working again."
thumbnail: "/images/thumbs/how-to-fix-battery-not-charging-after-bios-update-on-hp-laptop.webp"
faqs:
  - q: "Why did my HP battery stop charging after a BIOS update?"
    a: "BIOS updates reset embedded-controller settings, including HP Battery Health Manager thresholds and charge behavior. If the update set a charge limit (for example, stop at 80%) or the battery driver re-enumerated badly, Windows will show plugged in but not charging. Re-applying the settings and reinstalling the battery driver fixes it in most cases."
  - q: "Is it safe to roll back an HP BIOS update to fix charging?"
    a: "HP generally allows flashing an older BIOS, but only do it if every other fix fails. A BIOS rollback carries a small risk if power is lost mid-flash. First try an EC reset, driver reinstall, and HP Battery Health Manager settings — those resolve the issue far more often than a rollback does."
  - q: "What is an EC reset and does it help after a BIOS update?"
    a: "The embedded controller manages charging hardware. Holding the power button for 15 seconds with all power removed drains residual charge and forces the controller to reinitialize with the new BIOS values. It's the single most effective step for post-BIOS-update charging failures."
  - q: "My HP says 'plugged in, not charging' after the update. What should I do first?"
    a: "Run an EC reset, then reinstall the Microsoft ACPI battery drivers in Device Manager. Next, open the BIOS setup (F10) or HP Battery Health Manager and confirm the charge mode is set to 'Let HP Manage My Charging' or 100% instead of a capped threshold. That covers the cause in the large majority of cases."
---

Few things are more frustrating than updating your HP laptop's BIOS for "stability improvements" and discovering the battery no longer charges. The laptop works fine on AC power, Windows cheerfully reports "plugged in," but the percentage never moves — or worse, the battery icon shows a red X.

Before you panic: this is a settings and firmware handshake problem far more often than a hardware failure. The BIOS update rewrote the low-level rules your charging circuit follows, and something in that rewrite didn't stick. The fixes below walk you through putting it right.

## Why this happens

- **Embedded controller settings reset.** BIOS updates reinitialize the EC, which can leave charge thresholds or battery detection in a default or half-configured state.
- **HP Battery Health Manager reverted to a capped mode.** The update may have switched the policy to "Maximize battery health" (charges to 80%) or disabled charging behavior you had customized.
- **Battery driver re-enumeration glitch.** After the firmware change, Windows may load a stale or mismatched ACPI battery driver entry.
- **BIOS update interrupted or partial.** If the flash was interrupted, battery-related firmware tables can be corrupt while the rest of the system boots fine.
- **Battery calibration data wiped.** Some updates clear the fuel-gauge calibration, so the system refuses to charge until it relearns the battery.
- **New BIOS battery-protection behavior.** Recent HP BIOS versions add stricter rules (e.g., no charging below a certain temperature or after a deep discharge) that can look like a failure.

## How to fix it

Work through these in order. Do not skip the EC reset — it's the highest-success step.

### Fix 1: Perform an EC (embedded controller) reset

This drains residual power and forces the charging hardware to reinitialize under the new BIOS.

1. Shut the laptop down completely — not sleep, a full shutdown.
2. Unplug the AC adapter and remove any USB-C docks or peripherals.
3. If the battery is removable, take it out. Most modern HP laptops have internal batteries — just skip this.
4. Press and hold the **power button for 15 seconds**, then release.
5. Reconnect the AC adapter (leave the battery out if you removed it) and power on.
6. Watch the battery icon for 5–10 minutes. Charging often resumes right here.

### Fix 2: Reinstall the battery drivers

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Also uninstall **Microsoft AC Adapter** if listed.
4. Click **Action > Scan for hardware changes** to reinstall them.
5. Restart the laptop while plugged in, then check whether the percentage climbs.

### Fix 3: Check HP Battery Health Manager settings

The BIOS update may have silently capped your charge level.

1. Restart and tap **F10** repeatedly to enter BIOS Setup.
2. Navigate to the **Advanced** or **Power** tab and find **Battery Health Manager** (location varies by model).
3. Set it to **Let HP Manage My Charging** for normal 100% charging, or **Maximize My Battery Duration** — avoid "Maximize Battery Health" while troubleshooting since it caps charge at 80%.
4. Save and exit (**F10** to save), boot into Windows, and confirm charging resumes.

If you prefer doing this in Windows, HP's PC Hardware Diagnostics and the [HP support site](https://support.hp.com/us-en) both document the Battery Health Manager options for your exact model.

### Fix 4: Run HP PC Hardware Diagnostics battery test

1. Shut down, then power on while tapping **F2** to open HP PC Hardware Diagnostics UEFI.
2. Go to **Component Tests > Power > Battery** and run the battery check.
3. If the test reports the battery is fine but Windows still won't charge, the issue is software — continue with the fixes below.
4. If it reports a battery failure, note the failure ID; HP uses it for warranty claims.

### Fix 5: Re-flash or re-apply the same BIOS version

A slightly corrupt flash can leave battery tables broken while everything else works.

1. On [HP's support site](https://support.hp.com/us-en), enter your model and download the **exact same BIOS version** you just installed.
2. Close all apps, plug in the AC adapter, and run the installer.
3. Let it complete and reboot on its own — do not touch the power button.
4. After booting, repeat Fix 1 (EC reset) once more, then test charging.

### Fix 6: Drain and recharge to force gauge relearn

If the update wiped calibration data, a controlled deep cycle helps.

1. Unplug and use the laptop until it forces itself into hibernation or shuts down.
2. Leave it off for 2–3 hours.
3. Plug in and charge to 100% without interruption, ideally while powered off.
4. Boot and verify the battery now charges and reports normally.

For the full calibration procedure, see our guide on [calibrating a laptop battery in Windows 11](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 7: Update the chipset and power drivers

1. On HP's support page for your model, download the latest **chipset** driver and any **Intel/AMD power management** drivers — install chipset first.
2. Restart, then check **Windows Update** for any optional driver updates related to system firmware or battery.
3. Test charging again after both are in place.

### Fix 8: Roll back the BIOS (last resort)

Only attempt this if nothing above worked and you have the previous BIOS installer from HP.

1. Download the previous BIOS version from [HP support](https://support.hp.com/us-en) for your exact model.
2. Plug in the AC adapter and close everything.
3. Run the older BIOS installer and allow it to complete and reboot.
4. Perform one final EC reset (Fix 1) and check charging.

If charging still fails after a rollback, the battery itself may have coincidentally failed — run the HP diagnostics battery test again and contact HP support with the failure ID. And if Windows ever reports [no battery detected at all](/articles/laptop-battery-not-detected-windows-11/) after a firmware change, that's a related but distinct problem with its own fix path.

## Closing

BIOS updates and batteries clash more often than they should, but the fix is usually a settings reset away: EC reset, driver reinstall, and a check of Battery Health Manager get most HP laptops charging again within half an hour. Only treat it as hardware failure after the diagnostics say so.
