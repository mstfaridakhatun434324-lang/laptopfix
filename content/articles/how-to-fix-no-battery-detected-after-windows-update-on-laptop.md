---
title: "No Battery Detected After a Windows Update: Step-by-Step Fix"
slug: how-to-fix-no-battery-detected-after-windows-update-on-laptop
date: 2026-09-08
categories: ["battery"]
tags: ["no battery detected", "windows update", "battery driver", "device manager"]
description: "Windows says no battery is detected after an update? This step-by-step guide brings the battery back, from driver resets to BIOS checks."
thumbnail: "/images/thumbs/how-to-fix-no-battery-detected-after-windows-update-on-laptop.webp"
faqs:
  - q: "Why does Windows say no battery is detected after an update?"
    a: "The update usually replaced or corrupted the ACPI battery driver, or it reset the embedded controller that reports the battery to Windows. In rare cases a BIOS setting changed. Reinstalling the battery drivers and doing a full power reset resolves it for most laptops."
  - q: "Will my data be safe while fixing this?"
    a: "Yes. Every step here — driver reinstalls, power resets, BIOS checks — touches only power management, not your files. Still, keep the charger plugged in throughout so the laptop cannot lose power mid-fix."
  - q: "What if the battery is not detected in the BIOS either?"
    a: "Then Windows is not the problem: the system firmware itself cannot see the battery. Reseat the battery if it is removable, check for swelling, and try a BIOS update. If the BIOS still shows no battery, the battery or its connector has likely failed and needs service."
  - q: "How do I stop updates from breaking the battery driver again?"
    a: "After fixing it, install the battery and chipset drivers from your manufacturer's support page rather than relying on Windows Update's generic ones. You can also pause updates for a week or two after a fix to confirm stability before the next patch cycle."
---
Everything was fine yesterday. Then Windows installed an update overnight, and now the taskbar battery icon has a red X, hovering over it says "No battery is detected," and the laptop dies the instant you unplug it. It feels like the update killed your battery.

It didn't — or at least, probably not. What updates routinely break is the *reporting* chain between the battery and Windows: the ACPI driver, the embedded controller state, or a power management setting. The battery is usually sitting there perfectly fine, just invisible to the operating system. Here is how to make it visible again, in the order a technician would try.

## Why this happens

- **Corrupted or mismatched ACPI battery driver:** the update installed a generic driver version that cannot talk to your battery's controller.
- **Embedded controller (EC) confusion:** the firmware chip that manages power can get stuck in a bad state during the update's reboots.
- **BIOS/UEFI setting changed:** some updates flip battery-related settings or the update itself included a firmware component that misconfigured them.
- **Windows power service glitch:** the services that enumerate hardware can fail to start properly after a major update.
- **Loose battery connection exposed by reboots:** the repeated restarts during an update can jiggle a marginal battery connector into a non-contact state.
- **Fast Startup caching a bad hardware state:** hybrid shutdown preserves the broken enumeration across reboots, making the problem look permanent.
- **Actual battery failure coinciding with the update:** rarely, the timing is coincidence — the battery genuinely died the same week.

## How to fix it

Work through these in order. Keep the charger plugged in the whole time.

### Fix 1: Do a full EC power reset

This clears the embedded controller's confused state and fixes a surprising number of cases.

1. Shut the laptop down completely — hold **Shift** while clicking **Shut down** to bypass Fast Startup.
2. Unplug the charger and every USB device.
3. If the battery is removable, take it out. If not, leave it in.
4. Press and hold the power button for a full 30 seconds.
5. Reconnect the charger (and battery), then power on and check the battery icon.

### Fix 2: Reinstall the battery drivers

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. Do the same for **Microsoft AC Adapter** if listed.
3. In the **Action** menu, click **Scan for hardware changes**. Windows reinstalls both drivers.
4. If the battery appears, restart once more to make the fix stick.

### Fix 3: Check whether the BIOS sees the battery

This tells you whether it is a Windows problem or a hardware problem.

1. Restart and enter the BIOS/UEFI (usually **F2**, **F10**, **Del**, or **Esc** during boot — check your maker's splash screen).
2. Look for a battery status, battery health, or power section.
3. If the BIOS shows battery information, the hardware is fine and the problem is in Windows — continue with the software fixes.
4. If the BIOS also shows no battery, skip to Fix 7 (hardware checks).

### Fix 4: Disable Fast Startup

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup**, save, and do a full shutdown followed by a cold boot.

### Fix 5: Run the hardware troubleshooter and system file checks

1. Open **Terminal (Admin)** and run `sfc /scannow` to repair corrupted system files the update may have left behind.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` and reboot.
3. Corrupted system components can prevent the battery device stack from loading, and these two commands repair them.

### Fix 6: Install manufacturer chipset and battery drivers

1. Go to your manufacturer's support page — for example [HP support](https://support.hp.com/us-en) or [Dell support](https://www.dell.com/support) — and find your exact model.
2. Download the chipset driver and any power management or battery driver listed, even if the versions look older than what Windows installed.
3. Install them, reboot, and check Device Manager's Batteries section again.

### Fix 7: Reseat or inspect the battery hardware

1. Power off and unplug. If the battery is removable, slide it out, clean the contacts with a dry cloth, and reseat it firmly.
2. While it is out, look for swelling, a warped casing, or a burnt smell. If you spot swelling, stop and read our guide on [handling a swollen battery safely](/articles/how-to-fix-battery-swelling-slightly-laptop-safe-in-windows-11-24h2/).
3. For internal batteries, check whether the bottom panel bulges. Do not pry the machine open yourself — take it to a service center.

### Fix 8: Update or roll back the BIOS

1. If a newer BIOS exists on the manufacturer's support site, install it with the charger connected — firmware updates often fix battery enumeration bugs.
2. If the problem started with a BIOS update bundled into Windows Update, check whether the BIOS setup offers a rollback option.
3. As a last resort, a Windows **System Restore** to a point before the update can undo driver damage: search **Recovery** in Settings and choose **Open System Restore**.

## Closing

"No battery detected" after an update is scary but it is a software problem far more often than a dead battery. The EC reset plus driver reinstall brings the battery back in most cases, and the BIOS check tells you within five minutes whether you are dealing with Windows or with hardware. Work the list in order and you will know exactly which one it is before you spend money on anything. That five-minute BIOS check alone saves most people a needless battery purchase.

Related: [battery not detected on Windows 11](/articles/how-to-fix-battery-not-detected-on-laptop-in-windows-11-24h2/) and [laptop battery not charging after a Windows 11 update](/articles/how-to-fix-laptop-battery-not-charging-when-plugged-in-step-by-step/). Microsoft's official battery troubleshooting is at [Microsoft support](https://support.microsoft.com/en-us/windows).
