---
title: "Laptop Battery Stuck at 80%? How to Remove the Charge Limit on Windows 11"
slug: laptop-battery-stuck-at-80-percent-windows-11-fix
date: 2026-10-09
categories: ["battery"]
tags: ["battery", "charge limit", "windows 11", "lenovo", "asus"]
description: "Is your laptop battery stuck at 80% and refusing to charge further? It's usually a battery-health feature. Here's how to turn it off on Lenovo, HP, Dell, and Asus."
thumbnail: "/images/thumbs/laptop-battery-stuck-at-80-percent-windows-11-fix.webp"
faqs:
  - q: "Why is my laptop battery stuck at 80 percent?"
    a: "It's almost always a battery-health feature — Lenovo Conservation Mode, Asus Battery Health Charging, Dell battery settings, HP Battery Health Manager, or Surface Smart Charging — deliberately capping the charge to extend battery lifespan. It is not a fault. Turn the feature off in the vendor app or BIOS and the battery will charge to 100% again."
  - q: "Does limiting the charge to 80% damage the battery?"
    a: "No — quite the opposite. Keeping a lithium-ion battery at a lower maximum charge reduces chemical stress and heat, which can meaningfully extend its usable life over the years. That is why vendors ship the feature turned on. Disable it only if you regularly need the full runtime, such as before travel."
  - q: "Why is my battery stuck at 60% instead of 80%?"
    a: "Some vendors use 60% as the conservation threshold — Lenovo's Conservation Mode is the most common example. HP's Battery Health Manager and some Dell and Asus profiles can also cap the charge at lower levels. The fix is the same: open the vendor's power app or BIOS setting and switch to the full-charge mode."
  - q: "My laptop has no vendor app. How do I remove the limit?"
    a: "Check the BIOS or UEFI firmware settings for a battery health or charge threshold option — HP and many other brands expose it there even without a Windows app. If there is truly no such setting, reinstall the Microsoft ACPI battery drivers in Device Manager, since a stuck driver can mimic a charge cap. If neither applies, the limit may be hard-coded by the manufacturer."
---

You glance at the taskbar and your battery sits at exactly 80% — "plugged in, not charging" — no matter how long you leave the charger connected. It looks like a malfunction, and it sends plenty of laptop owners hunting for a fix. In the vast majority of cases, though, nothing is broken.

That ceiling is almost always a deliberate battery-health feature from your laptop's manufacturer. Lenovo calls it Conservation Mode, Asus calls it Battery Health Charging, and Dell, HP, and Microsoft Surface each ship their own version. They cap the maximum charge to slow the chemical wear on lithium-ion cells. The good news: switching it off takes about a minute. The fixes below cover every major brand.

## Why this happens

- **Lenovo Conservation Mode is enabled.** It caps charging at around 60% to reduce battery stress for users who mostly work plugged in.
- **Asus Battery Health Charging is set to a limited mode.** Balanced mode stops at 80% and Maximum lifespan mode at 60%; only Full capacity mode charges to 100%.
- **A Dell battery profile is limiting the charge.** Profiles like Adaptive or Primarily AC Use can lower the maximum charge based on your usage patterns.
- **HP Battery Health Manager is set to maximize battery health.** This firmware-level setting, configured in the BIOS, deliberately limits the top of the charge range.
- **Surface Smart Charging is pausing the charge.** On Microsoft Surface devices, this feature can hold the battery at 80% to extend its lifespan.
- **A stuck battery driver is mimicking a cap.** Rarely, a corrupted Microsoft ACPI battery driver freezes the reported percentage, which looks identical to a vendor charge limit.

## How to fix it

Find your brand below and follow the matching fix. Changes apply immediately — unplug and replug the charger if the percentage doesn't start climbing.

### Fix 1: Turn off Lenovo Vantage Conservation Mode

Conservation Mode limits the battery to about 60%, which is ideal for desk use but frustrating when you need full runtime.

1. Open the Lenovo Vantage app (install it free from the Microsoft Store if it's missing).
2. Go to Device > Power.
3. Find Conservation Mode and toggle it Off.
4. Unplug and replug the charger — the battery should now charge past the cap toward 100%.

Lenovo's [official support site](https://support.lenovo.com/us/en/) has model-specific instructions if Vantage looks different on your machine.

### Fix 2: Change HP's Battery Health Manager in the BIOS

HP enforces charge limits in firmware rather than in Windows, so this one requires a trip into the BIOS.

1. Shut down the laptop completely, then power it on and immediately press F10 repeatedly to enter BIOS Setup.
2. Go to the Advanced tab > Power Management Options > Battery Health Manager.
3. Select "Let HP Manage My Charging Setting" or "Maximize My Battery Duration" — the full-charge option — instead of "Maximize My Battery Health."
4. Save and exit, let Windows boot, and confirm the battery charges past the previous limit.

HP's [official support site](https://support.hp.com/us-en) lists the exact BIOS path for your model if the menu names differ.

### Fix 3: Switch Dell Power Manager to Standard

Dell's battery profiles quietly change the maximum charge based on how you use the machine.

1. Open Dell Power Manager (or Dell Optimizer on newer models).
2. Go to Battery Settings.
3. Change the selected profile from Adaptive, Primarily AC Use, or Custom to Standard.
4. Click OK or Apply, then unplug and replug the charger if charging doesn't resume on its own.

If Power Manager is missing, grab it from [Dell's official support site](https://www.dell.com/support) for your model.

### Fix 4: Set MyASUS Battery Health Charging to Full capacity mode

Asus exposes three charge modes, and two of them cap the battery below 100%.

1. Open the MyASUS app.
2. Go to Customization > Battery Health Charging (the exact location varies slightly by model).
3. Select Full capacity mode. (Balanced mode caps at 80%; Maximum lifespan mode caps at 60%.)
4. The change takes effect immediately — the battery should resume charging toward 100%.

### Fix 5: Check Windows 11 and Surface battery settings

Windows 11 has no universal charge-limit setting of its own — the cap always comes from vendor software or firmware — but two settings are worth checking.

1. On a Microsoft Surface, open the Surface app and turn off Smart charging, which can pause charging at 80%. (On some models this lives under Settings > System > Power & battery.)
2. In Settings > System > Power & battery, review your power mode and Battery saver settings. These don't impose a charge cap, but a misconfigured mode can make charging behavior confusing.
3. If the laptop runs hot or sluggish while plugged in, note that sustained heat and heavy background load can also cause some firmware to pause charging; trimming that load with our guide to [fixing high RAM usage on Windows 11](/articles/windows-11-high-ram-usage-fix/) is a sensible companion step.

### Fix 6: Reinstall the battery drivers as a fallback

If no vendor setting explains the cap, a stuck driver can produce the exact same symptom.

1. Right-click Start and open Device Manager.
2. Expand Batteries, right-click "Microsoft ACPI-Compliant Control Method Battery," and choose Uninstall device.
3. Uninstall "Microsoft AC Adapter" the same way.
4. Restart the laptop so Windows reinstalls both drivers automatically.
5. If the battery still won't charge at all — rather than stopping at a threshold — you're likely facing a different problem. See our guide to fixing a [laptop plugged in but not charging](/articles/how-to-fix-laptop-plugged-in-not-charging-windows-11/) on Windows 11.

Once the limit is off, your battery should climb to 100% on the next full charge. If you mostly use the laptop plugged in at a desk, consider leaving the feature on — your battery will hold up noticeably better a year or two from now. And if charging never starts at all, work through our [plugged-in-but-not-charging troubleshooting guide](/articles/how-to-fix-laptop-plugged-in-not-charging-windows-11/) instead.
