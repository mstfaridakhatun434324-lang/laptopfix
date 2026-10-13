---
title: "How to Fix Laptop Battery Not Charging After the Windows 11 24H2 Update"
slug: how-to-fix-laptop-battery-not-charging-after-windows-11-24h2-update
date: 2026-09-08
categories: ["battery"]
tags: ["battery", "charging", "windows 11 24h2", "update"]
description: "Battery stopped charging after the Windows 11 24H2 update? These 7 fixes repair the corrupted drivers and settings the update breaks."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-after-windows-11-24h2-update.webp"
faqs:
  - q: "Why did my battery stop charging right after the 24H2 update?"
    a: "The 24H2 update reinstalls power management components and can replace your battery driver with a generic one that misreads the battery. It can also reset power plans and re-enable a vendor charge limit you had previously turned off. The fixes in this guide repair each of those failure points in order."
  - q: "Can I just roll back the 24H2 update to fix charging?"
    a: "You can, but it is usually unnecessary. Rolling back removes security improvements and you would need to reinstall the update eventually. A driver reinstall and power plan reset resolve most 24H2 charging issues in minutes while keeping your system current. Use rollback only as a last resort."
  - q: "Does 24H2 damage the battery physically?"
    a: "No. Feature updates do not change how the physical battery or charger hardware works. What they change is the software layer: drivers, power schemes, and firmware interfaces. If the battery charged fine the day before the update, the hardware is almost certainly healthy and the issue is software."
  - q: "What if none of the software fixes restore charging?"
    a: "Generate a battery report with powercfg /batteryreport and compare design capacity with full charge capacity. If the full charge capacity has collapsed to under 60 percent of design, the battery has worn out and no software fix will restore it. Test with a known-good charger as well before concluding the battery is dead."
---

Your laptop was charging fine yesterday. Today, after the Windows 11 24H2 feature update finished installing and rebooting, the taskbar shows the plug icon but the percentage sits frozen — or Windows says "plugged in, not charging." Nothing changed about your charger or your desk setup. The only variable is the update, and that is exactly where the problem lives.

This is one of the most reported issues after every major Windows 11 feature update, and 24H2 is no exception. The good news is that it is a software problem in the overwhelming majority of cases: the update rewrote drivers, reset power plans, or disturbed the firmware handshake that manages charging. None of that requires new hardware. The seven fixes below go from the quickest checks to the deeper repairs.

## Why this happens

- **The battery driver was replaced with a generic version.** 24H2 reinstalls device drivers during setup. The Microsoft ACPI-Compliant Control Method Battery driver it installs may not talk to your laptop's embedded controller correctly, so Windows misreads the charging state.
- **Optional driver updates were installed over working vendor drivers.** 24H2's first post-install update pass often pulls chipset and firmware drivers from Windows Update that conflict with your manufacturer's own versions.
- **Power plans were reset to defaults.** Feature updates can corrupt or reset your active power scheme, which can disrupt charging behavior and sleep states tied to charging.
- **A vendor charge limit was re-enabled.** If you previously disabled Lenovo Conservation Mode, Asus Battery Health Charging, or a Dell charge cap, the update can flip it back on, freezing your charge at 60 or 80 percent.
- **The BIOS/embedded-controller handshake glitched.** The update touches firmware interfaces. A stale BIOS can misreport battery state to the newly updated Windows power stack.
- **The battery gauge was desynchronized.** Rapid driver swaps during the update can leave the fuel gauge calibration out of sync, so the reported percentage no longer reflects reality.

## How to fix it

Work through these in order. The first three resolve most 24H2 charging failures.

### Fix 1: Rule out the charger first

Before blaming the update, spend two minutes confirming the hardware still works — feature updates make convenient scapegoats.

1. Unplug the charger from both the laptop and the wall, wait 30 seconds, then plug it directly into a different wall outlet.
2. Inspect the cable and connector for fraying, bent pins, or a loose fit that makes charging flicker when wiggled.
3. If you charge over USB-C, confirm you are using the port with the charging icon and an adapter rated for your laptop's wattage, not a phone charger.
4. Borrow or test a compatible charger of equal or higher wattage. If charging works with another adapter, your charger — not the update — is the problem.

### Fix 2: Reinstall the Microsoft ACPI battery drivers

This is the highest-success fix for post-update charging issues. The update-damaged driver gets cleanly replaced.

1. Right-click the Start button and open **Device Manager**.
2. Expand **Batteries**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**, then confirm. Do not check any "delete driver" box.
4. Right-click **Microsoft AC Adapter** and uninstall it the same way.
5. Shut down the laptop completely, unplug the charger for 30 seconds, then plug it back in and power on.
6. Windows detects the battery hardware during boot and reinstalls fresh drivers. Check the taskbar battery icon for the charging indicator.

### Fix 3: Check optional updates for driver fixes

Microsoft often ships a follow-up driver patch within days of a feature update. Make sure you actually have it.

1. Open **Settings > Windows Update**.
2. Click **Check for updates** and install everything offered, including cumulative updates.
3. Go to **Advanced options > Optional updates**, expand **Driver updates**, and look for anything related to battery, chipset, or firmware from your laptop's manufacturer.
4. Install those optional driver updates, then restart. A corrected battery or chipset driver from this list has fixed many 24H2 charging cases.

For more on reading what your battery is actually doing, see our guide on [how to generate a battery report in Windows 11](/articles/how-to-generate-battery-report-windows-11-powercfg/).

### Fix 4: Reset power plans to Windows defaults

A corrupted power scheme from the update can block normal charging behavior.

1. Right-click Start and open **Terminal (Admin)**.
2. Run `powercfg /restoredefaultschemes` and wait for it to finish.
3. Restart the laptop.
4. After signing in, open **Settings > System > Power & battery** and confirm the power mode is set to **Balanced** or **Best power efficiency**.
5. Plug in the charger and watch the battery percentage for a few minutes to confirm it climbs.

### Fix 5: Verify no vendor charge limit was re-enabled

If charging stops at exactly 60 or 80 percent, the update likely reactivated a battery-health feature.

1. On Lenovo: open **Lenovo Vantage > Device > Power** and turn off **Conservation Mode**.
2. On Asus: open **MyASUS > Battery Health Charging** and select **Full capacity mode**.
3. On Dell: open **Dell Power Manager > Battery Settings** and choose **Standard**.
4. On HP: open the **HP BIOS (F10 at boot) > Advanced > Power Management Options > Battery Health Manager** and select the full-charge option.
5. On Samsung or MSI: check **Samsung Settings > Battery** or **MSI Center > Battery** for a charge-cap toggle.

If you were already near a cap before the update, the behavior may look identical to a charging failure — see our [full guide to battery health on Windows 11 laptops](/articles/how-to-check-battery-health-on-windows-11-laptop/) for how to tell the difference.

### Fix 6: Update the BIOS and chipset drivers

The 24H2 power stack expects modern firmware. A BIOS from two years ago can misreport battery state.

1. Press **Win + R**, type `msinfo32`, press Enter, and note the **BIOS Version/Date**.
2. Visit your manufacturer's support page — [Dell](https://www.dell.com/support) or [Lenovo](https://support.lenovo.com/us/en/) — and compare your BIOS version with the latest for your exact model.
3. Also run Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to update chipset and management engine drivers, which govern how Windows talks to the battery.
4. Install any BIOS update with the charger plugged in and all apps closed, letting the laptop restart on its own.

### Fix 7: Roll back the 24H2 update as a last resort

If charging worked an hour before the update and every fix above failed, the update itself may be at fault.

1. Open **Settings > System > Recovery**.
2. Under **Previous version of Windows**, click **Go back** and follow the prompts. This option is only available for 10 days after the update.
3. If the 10 days have passed, reinstall Windows 11 from the official Windows 11 download page using a fresh install USB instead.
4. After rollback, test charging before reinstalling anything else.

In almost every case, one of the first four fixes gets the battery charging again without touching your files or reinstalling anything. If the battery report shows severe wear alongside these symptoms, the update may simply have coincided with a battery reaching the end of its life — but give the software fixes a fair chance first.

## Closing

A battery that stops charging right after 24H2 is a software problem until proven otherwise, and the proof is quick: fresh ACPI drivers, updated drivers from optional updates, and a reset power scheme fix the vast majority of cases. Start at Fix 1, give each step a fair test, and you will very likely have your percentage climbing again within the hour.
