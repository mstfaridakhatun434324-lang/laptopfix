---
title: "Windows 11 Not Detecting Your Laptop Battery? Here's the Fix"
slug: how-to-fix-battery-not-detected-on-laptop-in-windows-11-24h2
date: 2026-09-10
categories: ["battery"]
tags: ["battery not detected", "windows 11 24h2", "device manager", "troubleshooting"]
description: "Windows 11 24H2 cannot see your laptop battery? Follow this ordered fix list to restore battery detection without losing your files."
thumbnail: "/images/thumbs/how-to-fix-battery-not-detected-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why does Windows 11 24H2 not detect my battery?"
    a: "Usually a driver or firmware mismatch introduced by the 24H2 update: the ACPI battery driver fails to load, or the embedded controller gets stuck. Reinstalling the battery drivers and performing a full power reset fixes most cases. A BIOS update from your manufacturer often finishes the job."
  - q: "My laptop works on AC power but shows no battery. Is the battery dead?"
    a: "Not necessarily. If the machine runs fine on the charger, power delivery works — the issue is detection, not power. Check whether the BIOS sees the battery: if it does, this is a Windows driver problem. If the BIOS cannot see it either, the battery or its connector is the suspect."
  - q: "Should I uninstall the battery drivers? Is that safe?"
    a: "Yes, completely safe. Uninstalling the Microsoft ACPI-Compliant Control Method Battery entries in Device Manager only removes the software interface; Windows reinstalls them on the next boot. Your files and settings are untouched."
  - q: "How long does this fix usually take?"
    a: "Most people resolve it in 20 to 40 minutes. The driver reinstall and power reset take about ten minutes; a BIOS update adds another fifteen. Only if you reach the hardware checks does it stretch into a service-center visit."
---
Your laptop runs perfectly on the charger, but Windows 11 insists there is no battery at all. The taskbar icon shows a plug with a red X, **Settings > System > Power & battery** shows nothing about battery health, and the moment someone trips over the cable, everything dies. If this started around the Windows 11 24H2 update, you are in crowded company — this specific update has a track record of breaking battery detection.

The pattern is consistent: the battery hardware is fine, but the software chain that reports it to Windows is broken. That chain has four links — the embedded controller, the BIOS, the Windows driver, and the power services — and we are going to test and repair each one in turn.

## Why this happens

- **24H2 replaced the battery driver:** the feature update can install a generic ACPI driver that fails to enumerate your specific battery controller.
- **Embedded controller stuck mid-update:** the 24H2 install reboots several times, and the EC firmware that manages battery reporting can lock up.
- **BIOS incompatibility with 24H2:** older BIOS versions sometimes misreport battery data to the newer Windows power stack.
- **Corrupted device enumeration:** the Plug and Play re-scan during the update can leave the battery device in a failed state that persists across reboots.
- **Power services not starting:** the services behind hardware detection can be left in a broken state by the update.
- **Fast Startup preserving the broken state:** hybrid shutdown reloads the failed detection every boot, so restarts never clear it.
- **Coincidental hardware failure:** a battery connector that was already marginal can fail during the update's repeated thermal cycles.

## How to fix it

Work through these in order, keeping the charger connected throughout.

### Fix 1: Perform a full power reset

This unsticks the embedded controller, which is the most common culprit after 24H2.

1. Shut down fully: hold **Shift** and click **Shut down** in the Start menu to bypass Fast Startup.
2. Disconnect the charger and all USB devices.
3. Hold the power button down for 30 seconds — on some models you will see the keyboard backlight flash, which confirms the EC reset.
4. Reconnect the charger, power on, and check the battery icon within a minute of reaching the desktop.

### Fix 2: Reinstall the ACPI battery drivers

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and select **Uninstall device**. Check **Attempt to remove the driver for this device** if the option appears.
3. Repeat for **Microsoft AC Adapter** under the same section.
4. Click **Action > Scan for hardware changes** and wait for Windows to redetect both devices.
5. Restart the laptop normally and verify the battery appears.

### Fix 3: Check for the battery in the BIOS

1. Restart and press **F2**, **Del**, or **Esc** (varies by brand) to enter UEFI/BIOS setup.
2. Find the battery information or battery health page.
3. Battery visible here means Windows is at fault — continue with software fixes below.
4. No battery here either means the firmware cannot see it — jump to Fix 7.

### Fix 4: Update the BIOS to a 24H2-compatible version

1. On another device if needed, visit your manufacturer's support site and search your exact model.
2. Look for a BIOS update whose notes mention Windows 11 24H2, battery, or power — manufacturers released several such fixes.
3. Install it with the AC adapter plugged in and do not interrupt the flash.
4. After the reboot, check battery detection again before trying anything else.

### Fix 5: Repair system files and re-register power components

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. When it finishes, run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart. These commands repair the system components that the battery device stack depends on.

### Fix 6: Turn off Fast Startup and check power services

1. Go to **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**, uncheck **Turn on fast startup**, and save.
3. Press **Win + R**, type `services.msc`, and confirm **Plug and Play** and **Power** services are running.
4. Do a full shutdown and cold boot.

### Fix 7: Inspect the battery hardware

1. With the machine off and unplugged, check the underside for bulging — a swollen battery can lose contact with its connector. If you see swelling, follow our [swollen battery safety guide](/articles/how-to-fix-battery-swelling-slightly-laptop-safe-in-windows-11-24h2/) instead of continuing here.
2. If the battery is externally removable, take it out, clean the contacts, and reseat it firmly.
3. Boot into the BIOS again to see if the battery is now visible.

### Fix 8: Roll back or repair the 24H2 installation

1. Go to **Settings > System > Recovery**. If **Go back** is available (within ten days of the update), use it to return to the previous build.
2. Alternatively, download the [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) and perform an in-place upgrade, which reinstalls Windows while keeping files and apps.
3. After either path, immediately check battery detection before reinstalling anything else.

## Closing

Battery detection failures after 24H2 look dramatic but resolve at the software layer for the large majority of laptops. The power reset and driver reinstall take twenty minutes and fix most cases; the BIOS check tells you quickly whether you are in the unlucky minority with a hardware fault. Either way, you will have a clear answer instead of a red X — and most of the time, that answer is a driver, not a dead battery. The whole sequence takes under forty minutes, and you'll know exactly which layer failed. That's far better than guessing — or paying for a repair you didn't need.

See also: [no battery detected after a Windows update](/articles/how-to-fix-no-battery-detected-after-windows-update-on-laptop/) and [how to check battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/). For Microsoft's own troubleshooting steps, visit [Microsoft support](https://support.microsoft.com/en-us/windows).
