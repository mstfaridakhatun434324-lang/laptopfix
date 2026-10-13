---
title: "No Battery Detected After a Windows Update? Here's What to Do"
slug: what-to-do-if-no-battery-detected-after-windows-update
date: 2026-10-02
categories: ["battery"]
tags: ["no battery detected", "windows update", "driver", "device manager", "battery missing"]
description: "Windows update finished and now your battery has vanished. Get detection back with these proven steps."
thumbnail: "/images/thumbs/what-to-do-if-no-battery-detected-after-windows-update.webp"
faqs:
  - q: "Why does Windows say no battery detected after an update?"
    a: "Updates can corrupt or replace the battery driver stack, leaving Windows unable to communicate with the battery hardware. The battery is usually physically fine — the OS just lost the ability to see it. Reinstalling the drivers fixes most cases."
  - q: "How do I know if it's a software problem or a dead battery?"
    a: "Check the BIOS: restart and enter setup (F2/Del/F10). If the BIOS shows the battery, it's a Windows software problem. If the BIOS doesn't see it either, it's hardware — reseat the connector or replace the battery."
  - q: "Should I roll back the Windows update?"
    a: "Try the driver fixes first — they're faster and preserve the update's security fixes. Only roll back the update if the battery was detected immediately before it and nothing else restores detection. You can uninstall recent updates from Settings > Windows Update > Update history."
  - q: "Can a Windows update physically damage the battery?"
    a: "No. Updates can't damage battery hardware. They can only break the software communication with it. If the battery doesn't come back after all software fixes, it coincidentally failed at the same time — frustrating, but not caused by the update."
---

The update installed, the laptop rebooted, and now there's a red X on the battery icon: "No battery is detected." Your laptop works fine on AC power, but as far as Windows is concerned, the battery doesn't exist. Before you assume the worst, remember the timing — hardware doesn't usually die at the exact moment software changes. This is almost certainly a driver problem wearing a hardware costume.

Let's get Windows talking to the battery again.

## Why this happens

- **The battery driver was corrupted during the update.** The most common cause — the driver stack didn't migrate cleanly.
- **Windows installed a generic or wrong driver.** Feature updates sometimes replace manufacturer battery drivers with incompatible ones.
- **The update changed power management settings.** New defaults can disable battery-related devices.
- **Firmware and driver versions now conflict.** The update moved the OS forward without matching firmware.
- **Fast Startup cached the pre-update state.** The hybrid shutdown preserved stale device enumeration.
- **The battery was already marginal.** An update reboot can be the moment a weak battery's communication finally fails.
- **Coincidental hardware failure.** Rare, but verify rather than assume.

## How to fix it

Work through these in order — software first, hardware last.

### Fix 1: Reinstall the battery drivers

This resolves the majority of post-update detection failures. It's quick and safe.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. You may see entries with warning icons, or the section may be missing entirely.
3. Right-click each entry under **Batteries** and choose **Uninstall device**. Check **Attempt to remove the driver** if the option appears.
4. Shut down completely — do not restart — and unplug the adapter for 30 seconds.
5. Reconnect AC power and boot up.
6. Windows will detect the battery hardware and install fresh drivers. Check the taskbar icon within a few minutes.
7. If the Batteries section was missing entirely, click **Action > Scan for hardware changes** in Device Manager after rebooting. Give Windows a full five minutes after boot before concluding it failed — driver installation and hardware detection sometimes lag behind the desktop appearing.

### Fix 2: Check the BIOS for the battery

This two-minute check separates software from hardware definitively.

1. Restart and press **F2**, **Del**, or **F10** to enter BIOS/UEFI setup.
2. Look for battery information — most BIOS versions show battery presence, charge level, or health.
3. **Battery visible in BIOS:** the hardware is fine; stay on the software fixes below.
4. **Battery missing in BIOS:** the problem is hardware — skip to Fix 6. No Windows fix will help.
5. While in the BIOS, check for any battery enable/disable options and confirm the battery is enabled.

### Fix 3: Disable Fast Startup and cold boot

Fast Startup can freeze the pre-update device state in place across reboots.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup** and save.
4. Shut down fully, wait 10 seconds, and power on.
5. This forces Windows to re-enumerate all hardware from scratch, including the battery.

### Fix 4: Roll back or update the battery driver

If the reinstall didn't work, the driver version itself may be the problem.

1. In **Device Manager**, expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and open **Properties**.
2. Go to the **Driver** tab. If **Roll Back Driver** is available, use it — this restores the pre-update driver.
3. If rollback isn't available, click **Update driver > Search automatically for drivers**.
4. Also check your manufacturer's support site for a chipset or power management driver package newer than what Windows installed.
5. Restart and check detection again.

### Fix 5: Uninstall the problematic update

When the battery vanished immediately after a specific update and nothing else helps, remove that update.

1. Go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Sort by date and uninstall the most recent update — particularly driver or feature updates.
3. Restart and check for the battery.
4. If it returns, pause updates for a couple of weeks (**Settings > Windows Update > Pause updates**) to avoid immediate reinstallation, and check the manufacturer's site for a compatible driver in the meantime.
5. For manually obtaining specific updates, the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) lets you search for and install individual packages.

### Fix 6: Reset the EC and check the physical connection

If the BIOS doesn't see the battery either, it's hardware — but check the cheap possibilities first.

1. Shut down, unplug AC, and hold the power button for 30 seconds (or use the pinhole EC reset).
2. If comfortable opening the laptop, reseat the battery connector on the motherboard.
3. Check for swelling — a swollen battery can trigger protection cutoffs that look like detection failure.
4. Boot to the BIOS again and check for the battery. If it appears now, the connector or EC was the issue.
5. If it's still invisible everywhere, the battery has failed and needs replacing.

### Fix 7: Replace the battery if hardware is confirmed dead

Only reach this step after the BIOS check confirmed a hardware problem.

1. Get the exact part number from the battery label or manufacturer support.
2. Install the replacement, charge to 100%, and confirm Windows detects it immediately.
3. Run one calibration cycle so the system learns the new battery correctly.
4. For the Windows 11 24H2-specific variant of this problem, see our [24H2 no-battery-detected guide](/articles/how-to-fix-no-battery-detected-after-windows-update-in-windows-11-24h2/), and for general detection issues our [battery not detected overview](/articles/laptop-battery-not-detected-windows-11/).

## Closing

"No battery detected" after a Windows update is a software problem until proven otherwise — and the BIOS check is the proof either way. Reinstall the drivers, kill Fast Startup, and re-enumerate the hardware before you spend a cent. The battery was there yesterday; in most cases, it's still there today, just waiting for Windows to notice it again.
