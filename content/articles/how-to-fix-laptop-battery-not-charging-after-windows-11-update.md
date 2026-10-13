---
title: "Battery Stopped Charging After a Windows 11 Update? Here's the Fix"
slug: how-to-fix-laptop-battery-not-charging-after-windows-11-update
date: 2026-09-07
categories: ["battery"]
tags: ["battery not charging", "windows 11 update", "drivers"]
description: "Windows 11 update broke your battery charging? These targeted fixes undo what the update changed — drivers, firmware, and settings."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-after-windows-11-update.webp"
faqs:
  - q: "Why would a Windows update stop my battery from charging?"
    a: "Windows 11 updates can replace your battery and chipset drivers with generic versions, reset power plans, deliver firmware updates that re-enable charge limits, or leave the ACPI driver out of sync with the embedded controller. Any of these breaks the charging chain."
  - q: "Should I uninstall the Windows update to fix charging?"
    a: "Try targeted fixes first — driver reinstalls and settings checks resolve most cases without losing security patches. Uninstalling the update is a valid diagnostic step if charging broke immediately after it, but don't stay on an unpatched system long-term."
  - q: "How do I stop Windows Update from breaking charging again?"
    a: "You can't block all updates safely, but you can prevent driver surprises: in System > Advanced system settings > Hardware > Device Installation Settings, choose not to automatically download manufacturer apps, and manage drivers through your manufacturer's own update tool instead."
  - q: "Could the update have damaged my battery physically?"
    a: "No. Software updates can't damage battery chemistry. If the battery genuinely won't hold charge after all software fixes, the timing was coincidental — the battery was already failing and the update just happened to be the moment you noticed."
---
The pattern is unmistakable: Windows 11 installs updates overnight, and in the morning the battery icon says "plugged in, not charging." You changed nothing. The update changed things for you — drivers, firmware, power settings — and one of those changes broke the charging chain.

The fix is about undoing exactly what the update did, in the right order. Don't start by uninstalling the update; start with the pieces it most likely touched.

## Why this happens

- **Battery drivers replaced with generic versions.** The update may have overwritten manufacturer battery drivers with inbox generics that misreport charging.
- **Firmware delivered alongside the update.** Windows Update ships BIOS/EC firmware that can reset charge thresholds and calibration.
- **Power plan settings reset.** Custom plans can revert to defaults, including aggressive battery settings.
- **Fast Startup re-enabled.** Updates frequently turn Fast Startup back on, preventing full EC reinitialization.
- **Charge-limit features re-enabled.** Manufacturer battery-care modes switched back on by firmware updates.
- **Corrupt update installation.** A partially applied driver update leaves the battery stack in a broken state.
- **New power management bugs.** Occasionally the update itself contains a regression affecting specific hardware.

## How to fix it

Work through these in order, testing whether the battery charges after each step.

### Fix 1: Roll back the battery driver

If the update replaced your driver, put the old one back.

1. Open **Device Manager** (**Win + X**).
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** → **Properties**.
3. Go to the **Driver** tab. If **Roll Back Driver** is clickable, click it, choose a reason, and restart.
4. Do the same for **Microsoft AC Adapter**.

If Roll Back is grayed out, the driver wasn't changed by this update — move on. This takes ninety seconds and fixes a large share of update-related charging failures.

### Fix 2: Reinstall the battery drivers fresh

When rollback isn't available, do a clean reinstall:

1. In **Device Manager > Batteries**, uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter** (check delete driver software if offered).
2. Shut down fully: hold **Shift** while clicking **Shut down**.
3. Unplug everything, hold the power button 30–60 seconds (EC reset).
4. Reconnect the charger and boot.

Windows installs fresh drivers against the current firmware. Check the icon after a few minutes at the desktop.

### Fix 3: Check for re-enabled charge limits

Update-delivered firmware loves to switch these back on:

- **Lenovo Vantage:** disable **Conservation Mode**.
- **Dell Power Manager:** back to **Standard**.
- **MyASUS:** **Full capacity mode**.
- **HP BIOS:** **Battery Health Manager** → **Let HP Manage My Charging**.

Also open **Settings > System > Power & battery** and look for **Smart charging** notices. If your machine caps at 80% by design, that's explained in [why the battery only charges when the laptop is off](/articles/how-to-fix-battery-only-charges-when-laptop-is-off-in-windows-11-24h2/) — different symptom, same family of causes.

### Fix 4: Disable Fast Startup (again)

Updates re-enable this constantly.

1. Go to **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup** and save.

Then do a full shutdown and cold boot. Fast Startup's hybrid shutdown can preserve a broken driver state across restarts indefinitely — which is why "I already restarted" doesn't count until Fast Startup is off. Our dedicated guide covers [disabling Fast Startup to fix battery drain](/articles/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2/) in more depth.

### Fix 5: Install the manufacturer's drivers over Microsoft's

Get the drivers Windows should have used:

1. Visit your manufacturer's support site, enter your exact model, and download the latest **chipset**, **Intel Management Engine**, **ACPI/power management**, and **BIOS/EC firmware** packages.
2. Install them in that order, restarting as prompted.
3. Check the manufacturer's update utility (Vantage, SupportAssist, HP Support Assistant, MyASUS) for anything Windows Update missed.

Manufacturer drivers report battery state through paths the generic drivers don't use. The [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) catches chipset updates on Intel machines.

### Fix 6: Use System Restore or uninstall the update (diagnostic step)

If charging broke within hours of the update, prove the connection:

1. Open **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent update and restart.
3. If charging returns, you've confirmed the culprit — then reinstall the update and apply Fixes 1–5, which usually resolve the conflict while keeping you patched.

Alternatively, **Control Panel > Recovery > Open System Restore** can roll back to a pre-update restore point. Don't remain unpatched; use this as diagnosis, then fix forward.

### Fix 7: Check battery health to rule out coincidence

Sometimes the update is innocent and the battery simply died that week. Run from an elevated Command Prompt:

```
powercfg /batteryreport /output %USERPROFILE%\Desktop\battery-report.html
```

If **Full Charge Capacity** is under 50% of **Design Capacity**, the battery was already gone — replace it. If capacity is healthy, the problem is software and one of the above fixes will land it. Microsoft documents this diagnostic flow at [support.microsoft.com](https://support.microsoft.com/en-us/windows).

### Fix 8: Repair Windows with an in-place upgrade (last resort)

If every targeted fix has failed, the update may have damaged the OS power subsystem beyond what driver reinstalls can reach. An in-place upgrade reinstalls Windows 11 over itself while keeping your files, apps, and settings: download the official Windows 11 ISO from Microsoft, mount it, run **setup.exe**, and choose **Keep personal files and apps**. The process takes 30–90 minutes and rebuilds system components including the power management stack. After it completes, reinstall your manufacturer's chipset and battery drivers on top, then test charging. This resolves the small fraction of cases where the update corrupted system files that SFC and DISM couldn't repair. Only consider a clean install if the in-place upgrade also fails — and back up first either way.

## Closing

When an update breaks charging, think like the update: it touched drivers, firmware, and settings — so you check drivers, firmware, and settings, in that order. Roll back or reinstall the battery drivers, kill the re-enabled charge limits, turn off Fast Startup, and layer the manufacturer's drivers back on top. The update didn't kill your battery; it just rearranged the furniture. Put it back.
