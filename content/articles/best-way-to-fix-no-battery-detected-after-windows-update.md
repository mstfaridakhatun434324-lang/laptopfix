---
title: "No Battery Detected After a Windows Update: Best Fix"
slug: best-way-to-fix-no-battery-detected-after-windows-update
date: 2026-10-05
categories: ["battery"]
tags: ["no battery detected", "windows update", "battery driver", "acpi"]
description: "Windows update left you with 'no battery detected'? Here is the best fix order: driver reset, BIOS check, and update rollback."
thumbnail: "/images/thumbs/best-way-to-fix-no-battery-detected-after-windows-update.webp"
faqs:
  - q: "Why does Windows say no battery detected after an update?"
    a: "Feature updates sometimes replace the ACPI battery driver with a version that cannot talk to your laptop's embedded controller, or they change power firmware behavior. The battery is physically fine; Windows just lost the ability to see it."
  - q: "Will I lose files by uninstalling the battery driver?"
    a: "No. Uninstalling the Microsoft ACPI-Compliant Control Method Battery driver only removes the software interface. Your files, apps, and settings are untouched, and Windows reinstalls the driver automatically on reboot."
  - q: "Should I roll back the Windows update?"
    a: "Only as a last resort. The driver reset and BIOS update below fix the problem without giving up security patches. Roll back only if the error appeared immediately after the update and nothing else works — and even then, reinstall the update later after updating drivers."
  - q: "Can a dead CMOS battery cause this?"
    a: "Rarely, but on older laptops a dead CMOS battery can cause BIOS settings to reset in ways that disable battery detection. If your clock also resets on every boot, replace the CMOS battery too."
---

You install a Windows update, reboot, and the battery icon shows a red X with the cheerful message "No battery is detected." The battery was fine yesterday. It is probably still fine today — Windows just cannot see it anymore.

This is one of the most common post-update battery issues, and the fix success rate is very high because the root cause is almost always software: a driver the update broke, a firmware setting it disturbed, or a power state it left behind. Here is the best order to fix it, starting with the two-minute solution.

## Why this happens

- **ACPI driver replaced or corrupted:** The update installed a new version of the battery driver that cannot communicate with your laptop's embedded controller.
- **Fast Startup hibernation state:** The update rebooted through Fast Startup, leaving the hardware in a half-initialized state where the battery never gets enumerated.
- **BIOS setting disturbed:** Rare, but updates that touch firmware can reset battery-related BIOS options.
- **Chipset driver mismatch:** The new Windows build expects a newer chipset driver for battery communication, and the old one no longer works.
- **Battery protection tripped during the update:** The long update process with restarts can deep-discharge an already weak battery, tripping its protection circuit.
- **Coincidental hardware failure:** Occasionally the timing is just bad luck — a loose battery cable finally gives out during the reboot. Worth ruling out before assuming software.
- **Generic chipset driver swapped in:** Major updates sometimes replace the manufacturer's chipset driver with a Microsoft generic that lacks battery communication support. Detection breaks until the OEM chipset driver is reinstalled.

## How to fix it

Work through these in order. Most people are fixed by Fix 1 or Fix 2.

### Fix 1: Reset the ACPI battery drivers (the best first fix)

This resolves the majority of post-update "no battery detected" errors.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. Confirm.
3. If **Microsoft AC Adapter** appears, uninstall it too.
4. **Shut down** the laptop completely — do not restart. Unplug the charger.
5. Wait **60 seconds**. This clears the hardware state that Fast Startup preserves.
6. Plug the charger back in and power on. Windows detects the battery hardware fresh and reinstalls clean drivers. Check the battery icon within a minute of reaching the desktop.

### Fix 2: Cold boot with the battery reseated

If the driver reset did not work, force the hardware to redetect.

1. Shut down and unplug. If the battery is removable, take it out for **2 minutes**, then reinsert firmly.
2. If it is internal, remove the bottom cover, disconnect the battery cable for **2 minutes**, and reconnect it.
3. Plug in and boot. The embedded controller enumerates the battery as new hardware. This step also catches the coincidental loose-cable case.

### Fix 3: Disable Fast Startup

Fast Startup is a frequent accomplice in post-update detection failures.

1. Open **Control Panel → Hardware and Sound → Power Options → Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully, wait 30 seconds, and boot. With Fast Startup off, every boot is a clean hardware initialization.

### Fix 4: Update chipset drivers

The update may have outrun your chipset drivers.

1. Visit your manufacturer's support site (Dell, HP, Lenovo, ASUS, Acer) and download the latest **chipset** drivers for your exact model and Windows build.
2. Install them and restart.
3. You can also check **Settings → Windows Update → Advanced options → Optional updates → Driver updates** for manufacturer drivers Microsoft distributes. Getting the driver stack current is also central to fixing [batteries Windows cannot see at all](/articles/laptop-battery-not-detected-windows-11/).

### Fix 5: Check the BIOS for battery status

1. Shut down, power on, and enter BIOS setup (**F2**, **Del**, or **Esc** depending on brand).
2. Look for **Battery Information** or **Power** section. If the BIOS sees the battery and Windows does not, the problem is 100% in Windows — continue with Fix 6.
3. If the BIOS also shows no battery, the issue is hardware or firmware: reseat the battery again, then update the BIOS. Dell owners can follow the model-specific steps in our [Dell no-battery-detected guide](/articles/how-to-fix-no-battery-detected-after-windows-update-on-dell-laptop/).

### Fix 6: Update the BIOS

1. Find your current version with `msinfo32` → **BIOS Version/Date**.
2. Download the latest BIOS from the manufacturer's support site and install it on AC power without interruption.
3. BIOS updates frequently fix embedded-controller communication that Windows updates disturb. This is especially effective on Dell and Lenovo models.

### Fix 7: Roll back the problematic update (last resort)

1. Go to **Settings → Windows Update → Update history → Uninstall updates**.
2. Find the most recent **Feature Update** or **Quality Update** installed right before the problem started, and uninstall it.
3. After rolling back, immediately update your chipset and BIOS drivers, then reinstall the Windows update. The second attempt usually succeeds once drivers are current. Microsoft documents update troubleshooting on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 8: Use System Restore to a pre-update point

If the rollback option is unavailable (Windows removes it after 10 days), System Restore can still take you back.

1. Press **Win + R**, type `rstrui`, and press Enter.
2. Choose a restore point dated before the update. Your personal files are not affected — only system files, drivers, and registry settings roll back.
3. After restoring, the battery should be detected again. Immediately update chipset and BIOS drivers before letting Windows Update run, so the problem does not return with the next update cycle.

## Closing

"No battery detected" after a Windows update is alarming but almost always fixable without new hardware. The driver reset plus a true cold boot resolves it most of the time; chipset and BIOS updates handle the rest. Work the list in order, and only consider the update rollback if everything else fails — your battery is almost certainly still good. If the error ever returns after a future update, you will already know the drill: cold boot, driver reset, chipset drivers, done.
