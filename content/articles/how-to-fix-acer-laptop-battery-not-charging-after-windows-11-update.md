---
title: "How to Fix an Acer Laptop Battery Not Charging After a Windows 11 Update"
slug: how-to-fix-acer-laptop-battery-not-charging-after-windows-11-update
date: 2026-09-15
categories: ["battery"]
tags: ["battery", "acer", "charging", "windows 11"]
description: "Acer laptop stopped charging after a Windows 11 update? Acer Care Center settings, driver resets, and BIOS fixes that work."
thumbnail: "/images/thumbs/how-to-fix-acer-laptop-battery-not-charging-after-windows-11-update.webp"
faqs:
  - q: "Why did my Acer stop charging after the Windows 11 update?"
    a: "The update can corrupt the Microsoft ACPI battery driver, reset Acer Care Center battery charge-limit settings, or install generic chipset drivers that miscommunicate with Acer's embedded controller. Acer laptops are also sensitive to the battery reset pinhole state, which a hard reset addresses."
  - q: "What is the battery reset pinhole on Acer laptops?"
    a: "Many Acer laptops have a small pinhole on the bottom labeled with a battery icon. Pressing a paperclip into it for a few seconds disconnects the internal battery electronically, clearing stuck power states. It is Acer's built-in equivalent of removing the battery."
  - q: "Does Acer Care Center limit battery charging?"
    a: "Yes. Acer Care Center has a battery charge limit option that caps charging at 80 percent to extend battery lifespan. A Windows update can re-enable it or reset your preference. Check the battery section of Acer Care Center if charging stops at exactly 80 percent."
  - q: "Where do I get the right drivers for my Acer?"
    a: "From Acer's official support site for your exact model and serial number. Acer's chipset, Management Engine, and BIOS packages are tested for your hardware. Avoid generic driver updater tools, which frequently install wrong versions on Acer laptops."
---

Your Acer Aspire, Swift, or Nitro was charging normally until a Windows 11 update installed overnight. Now the battery icon shows the plug but the percentage is frozen, or Windows reports "plugged in, not charging." Acer laptops have a couple of brand-specific quirks — the battery reset pinhole and Acer Care Center's charge limit — that make their post-update charging failures a little different from other brands.

This guide starts with the quick Acer-specific checks, then moves through the standard driver and firmware repairs. Work in order; most Acer charging issues after a Windows update are resolved by the fourth fix.

## Why this happens

- **Acer Care Center's charge limit was re-enabled.** The update can flip the 80 percent battery charge limit back on, freezing charging at exactly 80.
- **The ACPI battery driver corrupted.** Windows 11 updates routinely damage the driver Windows uses to read battery state.
- **Generic drivers replaced Acer's.** Windows Update may install chipset drivers that do not communicate properly with Acer's embedded controller.
- **The embedded controller is stuck.** Acer's power controller can lock into a non-charging state that survives normal reboots.
- **The charger or port is at fault.** A failing adapter or a loose barrel connector produces identical symptoms and must be ruled out.
- **The battery reached end of life.** On older Acers, the update timing is coincidental — the cells simply wore out.

## How to fix it

Work through these in order, starting with Acer's own tools.

### Fix 1: Check the Acer Care Center battery charge limit

The fastest Acer-specific check. If charging stops at exactly 80 percent, this is almost certainly the cause.

1. Open **Acer Care Center** (install it from the Microsoft Store if it is missing).
2. Go to the battery or power section and look for **Battery Charge Limit**.
3. If it is enabled, turn it off to allow charging to 100 percent.
4. Unplug the charger for 10 seconds, plug it back in, and confirm the percentage climbs past 80.
5. If you want the longevity benefit without the confusion, keep the limit on but know it is there — our guide to [battery health checks](/articles/how-to-check-battery-health-on-windows-11-laptop/) explains the tradeoff.

### Fix 2: Use the battery reset pinhole

Acer's hardware-level reset clears stuck power states that software reboots cannot touch.

1. Shut down the laptop and unplug the charger.
2. Flip the laptop over and find the small pinhole with a battery icon next to it.
3. Straighten a paperclip and press it gently into the hole for 5 seconds. You may feel a slight click.
4. Plug the charger back in and power on. The embedded controller reinitializes from scratch.
5. Check whether the battery now charges. This single step resolves a surprising number of Acer charging failures.

### Fix 3: Test the charger and rule out hardware

Before deeper software work, confirm the adapter is good.

1. Inspect the cable and brick for damage, and confirm the wattage on the label matches your model's requirement.
2. Plug directly into a wall outlet, bypassing strips and hubs.
3. Test with another compatible Acer charger if available. Acer adapters are inexpensive compared to a misdiagnosed battery replacement.
4. Check the barrel connector seats firmly — a loose fit that flickers when wiggled means the port or plug is worn.

### Fix 4: Reinstall the Microsoft ACPI battery drivers

The standard repair for update-corrupted battery drivers.

1. Right-click Start and open **Device Manager**.
2. Expand **Batteries**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**, then confirm.
4. Uninstall **Microsoft AC Adapter** the same way.
5. Shut down, unplug for 30 seconds, plug back in, and power on. Windows reinstalls both drivers during boot.
6. Verify the taskbar battery icon shows the charging indicator.

If you also see odd percentage behavior, our [battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/) shows how to check what the battery is really doing.

### Fix 5: Install Acer's official chipset and BIOS updates

Replace generic update-installed drivers with Acer's tested versions.

1. Go to Acer's support site, enter your serial number or model, and download the latest **chipset**, **Intel Management Engine**, and **BIOS** packages.
2. Install the chipset and Management Engine drivers first, restarting when prompted.
3. Install the BIOS update with the charger plugged in, all apps closed, and the laptop on a stable surface. Do not interrupt the flash.
4. After the reboot, test charging before changing any other settings.

### Fix 6: Reset power plans to defaults

A corrupted power scheme from the update can interfere with charging behavior.

1. Right-click Start and open **Terminal (Admin)**.
2. Run `powercfg /restoredefaultschemes`.
3. Restart the laptop.
4. Open **Settings > System > Power & battery** and set the power mode to **Balanced**.
5. Plug in and confirm the battery percentage rises steadily. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the built-in power troubleshooter if you want to run it as an extra check.

### Fix 7: Confirm battery health and replace if worn

When all software avenues fail, measure the battery itself.

1. Run `powercfg /batteryreport /output "C:\battery-report.html"` in **Terminal (Admin)**.
2. Compare full charge capacity with design capacity. Below 60 percent of design means the cells are worn out.
3. Order a genuine Acer battery for your exact model. Third-party Acer batteries frequently cause "plugged in, not charging" errors of their own because the laptop rejects their identification.
4. On sealed models, have an authorized Acer service center perform the replacement.

Acer charging failures after Windows updates follow a familiar script: a re-enabled charge limit, a stuck controller cleared by the pinhole, or a corrupted driver. The pinhole reset alone is worth trying before anything else — it takes ten seconds and fixes what hours of driver fiddling cannot.

## Closing

Start with Acer Care Center and the battery reset pinhole — they are the two checks other brands do not have. If those do not do it, the driver reinstall and Acer's official BIOS and chipset packages finish the job in nearly every remaining case. Keep the charger connected through every firmware step, retest charging after each individual fix rather than batching changes, and you will isolate the fault quickly instead of guessing.
