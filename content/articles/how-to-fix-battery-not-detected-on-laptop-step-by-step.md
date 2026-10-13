---
title: "How to Fix 'No Battery Detected' on Your Laptop: Step by Step"
slug: how-to-fix-battery-not-detected-on-laptop-step-by-step
date: 2026-09-07
categories: ["battery"]
tags: ["battery not detected", "device manager", "acpi battery", "troubleshooting"]
description: "Windows says no battery is detected on your laptop? Follow this step-by-step guide to bring the battery back — drivers, resets, BIOS, and hardware checks."
thumbnail: "/images/thumbs/how-to-fix-battery-not-detected-on-laptop-step-by-step.webp"
faqs:
  - q: "What does 'no battery is detected' mean in Windows?"
    a: "It means Windows cannot communicate with the battery pack at all — the battery icon may show an X, and Device Manager may be missing the battery entries. This is different from 'plugged in, not charging': here Windows doesn't even know a battery exists. The cause is usually a driver failure, a stuck embedded controller, a loose battery connector, or a genuinely dead battery."
  - q: "Can a Windows update cause the battery to disappear?"
    a: "Yes. Updates — especially major ones like Windows 11 24H2 — can replace the ACPI battery driver with a broken version or leave the embedded controller in a confused state. If the battery vanished right after an update, reinstalling the battery drivers and performing a full power drain (holding the power button 30 seconds with everything unplugged) fixes it in most cases."
  - q: "Will reinstalling battery drivers delete my data?"
    a: "No. Uninstalling the 'Microsoft ACPI-Compliant Control Method Battery' entries in Device Manager only removes the driver interface Windows uses to talk to the battery. Windows reinstalls them automatically on restart. Your files, apps, and settings are completely untouched — it's one of the safest fixes you can try."
  - q: "How do I know if the battery is dead or just not detected?"
    a: "Shut the laptop down, unplug it, and see what happens. If it dies instantly with no battery power at all, the battery is likely dead or disconnected. If it runs fine on battery but Windows still says 'no battery detected,' the battery is working and the problem is software — drivers or firmware. A battery report (powercfg /batteryreport) will also show whether Windows ever sees the pack."
---

"No battery is detected." Those four words in Windows are alarming because the battery icon gets a red X and your laptop suddenly behaves like a desktop — unplug the charger and it dies instantly. Or sometimes the laptop runs on battery just fine, but Windows insists there is no battery at all, which means no charge percentage, no low-battery warnings, and no battery settings.

Don't assume the battery is dead. In most cases Windows has simply lost communication with a perfectly healthy battery pack, and the fix is a driver reinstall or a power reset you can do yourself in minutes.

## Why this happens

- **Corrupted ACPI battery driver.** The "Microsoft ACPI-Compliant Control Method Battery" driver can break after a Windows update, leaving Windows blind to the pack.
- **Embedded controller glitch.** The EC chip that manages battery communication can lock up after a bad shutdown or sleep/wake cycle.
- **Loose battery connector.** On laptops with removable batteries (or recently serviced ones), the pack may not be seated fully in its connector.
- **BIOS not recognizing the battery.** An outdated or glitched BIOS may fail to enumerate the battery to Windows.
- **Genuinely dead battery.** A battery worn to near-zero capacity or with a failed protection circuit stops responding entirely.
- **Damaged ribbon cable or connector.** On ultrabooks with internal batteries, the small cable between battery and motherboard can work loose.

## How to fix it

Work through these in order, starting with the easiest. Stop when your issue is resolved.

### Fix 1: Do a full power drain (EC reset)

This is the single most effective fix for a battery that vanished after an update or a bad shutdown.

1. Shut the laptop down completely and unplug the charger and every USB device.
2. If the battery is removable, slide it out now. If it's internal, leave it alone — don't open the laptop yet.
3. Press and hold the **power button for a full 30 seconds**.
4. If you removed the battery, reseat it firmly until it clicks, then reconnect the charger.
5. Power on and check the battery icon in the taskbar.

### Fix 2: Reseat a removable battery

A battery that isn't making clean contact can disappear from Windows entirely.

1. Power off the laptop and unplug the charger.
2. Slide the battery release latches and remove the pack.
3. Inspect the metal contacts on the battery and in the bay for dust, corrosion, or bent pins.
4. Wipe the contacts gently with a dry cloth — no liquids.
5. Slide the battery back in until both latches click, plug in, and power on.

### Fix 3: Reinstall the battery drivers

This forces Windows to rebuild its communication path to the battery.

1. Press **Win + X** and open **Device Manager**.
2. Expand the **Batteries** category.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device** (repeat for each entry).
4. Right-click **Microsoft AC Adapter** and uninstall it too.
5. Shut the laptop down (don't just restart), unplug the charger for 30 seconds, then power back on.
6. Windows will reinstall the drivers automatically during boot — check the battery icon.

### Fix 4: Run the Power troubleshooter

Windows has a built-in troubleshooter that can detect broken battery enumeration.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Find **Power** and click **Run**.
3. Let it scan and apply any recommended fixes.
4. Restart and check whether the battery is detected.

### Fix 5: Check the BIOS battery page

The BIOS talks to the battery independently of Windows — if the BIOS can't see it either, the problem is hardware.

1. Restart and press your manufacturer's BIOS key (**F2**, **Del**, or **F10** depending on brand) during boot.
2. Look for a **Battery**, **Power**, or **System Information** page.
3. Check whether the battery is listed with a health/capacity reading.
4. If the BIOS shows the battery but Windows doesn't, the fix is software — go back to Fix 3 and Fix 6. If the BIOS shows nothing, skip to the hardware checks below.

### Fix 6: Update the BIOS

BIOS updates frequently include battery detection and EC firmware fixes.

1. Find your exact model at **Settings > System > About** or on the bottom sticker.
2. Download the latest **BIOS** from your manufacturer's support site.
3. Install it with the charger connected (use the barrel charger if USB-C charging is unreliable).
4. After the update completes and the laptop restarts, check the battery icon.

### Fix 7: Inspect the internal battery connection (advanced)

For laptops with internal batteries, a loose ribbon cable is a real possibility — especially if the laptop was recently opened.

1. Power off, unplug, and remove the bottom panel screws (keep track of which goes where).
2. Locate the battery cable connecting the pack to the motherboard.
3. Unplug it, check for damage, then reconnect it firmly.
4. Reassemble and test.
5. If you're not comfortable opening the laptop, take it to a shop for this step — it's a 10-minute job for a technician.

### Fix 8: Generate a battery report to confirm the verdict

This gives you hard data on whether Windows ever sees the battery.

1. Open **Terminal (Admin)** and run `powercfg /batteryreport`.
2. Open the generated HTML file from your user folder.
3. If the report shows **no battery information at all** after all the fixes above, the pack is almost certainly dead or disconnected — time for a replacement battery.
4. If the report shows design capacity and charge cycles, the battery is alive and one of the earlier software fixes should have worked — repeat Fix 1 and Fix 3 together.

A dead battery is the end of the road for DIY fixes, but at least you'll know for certain rather than guessing. If your battery shows up but won't take a charge, our guide on a [laptop battery not charging when plugged in](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/) picks up where this one leaves off, and the general [battery-not-detected troubleshooting page](/articles/laptop-battery-not-detected-windows-11/) covers additional Windows-side causes.

For manufacturer-specific help, check [Dell's support site](https://www.dell.com/support) or [HP's support site](https://support.hp.com/us-en) for your model's battery diagnostics, and Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) for the built-in troubleshooters.

## Closing

"No battery detected" sounds like a death sentence for the pack, but it's a communication problem far more often than a dead-battery problem. The power-drain reset and driver reinstall fix the majority of cases in under ten minutes — the hardware checks are only needed when Windows and the BIOS both insist the battery isn't there.
