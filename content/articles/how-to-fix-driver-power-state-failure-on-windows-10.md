---
title: "How to Fix DRIVER_POWER_STATE_FAILURE on Windows 10"
slug: how-to-fix-driver-power-state-failure-on-windows-10
date: 2026-10-13
categories: ["windows-errors"]
tags: ["bsod", "drivers", "power management"]
description: "DRIVER_POWER_STATE_FAILURE blue screen on Windows 10? A driver isn't handling sleep/wake properly. Here's how to track it down and fix it."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-on-windows-10.webp"
faqs:
  - q: "What causes DRIVER_POWER_STATE_FAILURE on Windows 10?"
    a: "A device driver fails to transition between power states — usually when the laptop sleeps, hibernates, or wakes up. The most common offenders are Wi-Fi adapters, graphics drivers, USB controllers, and chipset drivers that are outdated, corrupted, or incompatible with the current Windows 10 build."
  - q: "Why does it only crash when my laptop sleeps or wakes?"
    a: "Windows sends power-transition requests (IRPs) to every driver when sleeping or waking. If a driver doesn't respond within the timeout — often around two minutes — Windows bugchecks with this stop code to protect the system. That's why the crash is tied to lid-close, sleep, or wake events."
  - q: "Can a bad Windows update cause this error?"
    a: "Yes. Feature updates frequently install generic drivers or break compatibility with manufacturer-specific power management drivers. If the blue screen started right after an update, rolling back the driver or the update is often the fastest fix."
  - q: "Will fixing this delete any of my files?"
    a: "No. Updating or reinstalling drivers, running system scans, and changing power settings don't touch personal files. Still, keep a backup — any crash-heavy troubleshooting is safer with one in place."
---

`DRIVER_POWER_STATE_FAILURE` is one of those blue screens that almost always has a pattern: it hits when your laptop goes to sleep, hibernates, or wakes up. The stop code (0x0000009F) means a driver didn't respond to a power-transition request in time, so Windows pulled the plug on the whole system rather than risk hardware damage or data corruption.

The good news is that this error is almost never failing hardware. It's a driver behaving badly during sleep or wake — and once you identify which one, the fix is usually straightforward. Below is the exact order I'd work through if this laptop were sitting on my bench.

## Why this happens

- **Outdated Wi-Fi or network driver**: Wireless adapters are the single most common trigger. They mishandle the sleep request, time out, and Windows bugchecks.
- **Graphics driver incompatible with the current build**: GPU drivers register power callbacks; a mismatch after a Windows update can stall the whole power transition.
- **USB controller or device refusing to sleep**: External drives, USB hubs, or the USB 3.0 controller itself can hold up the power-down sequence.
- **Chipset or storage controller driver issues**: The AHCI/SATA or NVMe controller driver must flush and park the drive during sleep. A buggy version stalls it.
- **Fast Startup interaction**: Windows 10's hybrid shutdown keeps driver state between boots. A driver that saves bad state causes the crash on the next wake.
- **Corrupted driver installation**: Partially installed or corrupted driver files fail silently during normal use but blow up during power transitions.

## How to fix it

Work through these in order — the first two fixes solve the majority of cases.

### Fix 1: Update your Wi-Fi and graphics drivers

These two drivers cause most DRIVER_POWER_STATE_FAILURE crashes. Update them before touching anything else.

1. Press **Win + X** and select **Device Manager**.
2. Expand **Network adapters**, right-click your Wi-Fi adapter, and choose **Update driver** > **Search automatically for drivers**.
3. If Windows says you have the best driver, go to your laptop manufacturer's support site instead — [Dell's support page](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/) — and download the latest Wi-Fi driver for your exact model.
4. Do the same for your display adapter: expand **Display adapters**, update both the integrated and discrete GPU drivers.
5. For Intel graphics, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch the newest version.
6. Restart and test by putting the laptop to sleep and waking it twice.

If you notice crashes only started after a recent driver update, skip to Fix 4 instead — you may need to roll back rather than update. For a general overview of blue screen troubleshooting, see our guide on [how to fix the blue screen of death on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 2: Disable Fast Startup

Fast Startup saves driver state to disk on shutdown and reloads it on boot. If a driver saves corrupted state, every boot carries the problem forward.

1. Press **Win + R**, type `control`, and press Enter to open Control Panel.
2. Go to **Hardware and Sound** > **Power Options** > **Choose what the power buttons do**.
3. Click **Change settings that are currently unavailable** at the top.
4. Uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes** and do a full restart (**Win + X** > **Shut down or sign out** > **Restart**).
6. Test sleep/wake a few times. This alone fixes a surprising number of cases.

### Fix 3: Change what your laptop does on lid close

If the crash happens specifically when you close the lid, stop the laptop from sleeping on lid close while you troubleshoot — then address the driver properly.

1. Open **Control Panel** > **Hardware and Sound** > **Power Options**.
2. Click **Choose what closing the lid does** in the left pane.
3. Set both **On battery** and **Plugged in** to **Do nothing** temporarily.
4. Click **Save changes**. Use sleep from the Start menu instead of the lid.
5. If crashes stop, the issue is tied to the lid-triggered sleep path — continue with Fix 4 to roll back the offending driver.

### Fix 4: Roll back the suspect driver

If the crashes began right after a driver or Windows update, the new driver is guilty until proven innocent.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Right-click the suspect device (start with your Wi-Fi adapter, then GPU) and choose **Properties**.
3. Go to the **Driver** tab and click **Roll Back Driver** if it's available.
4. Choose a reason, click **Yes**, and restart.
5. Test sleep/wake. If the roll-back button is greyed out, use Fix 5 instead.

### Fix 5: Uninstall and reinstall the device driver

A clean reinstall clears corrupted driver files and bad registry state that an update leaves behind.

1. In **Device Manager**, right-click the problem device and choose **Uninstall device**.
2. Check **Attempt to remove the driver for this device** (or **Delete the driver software for this device**), then click **Uninstall**.
3. Restart the laptop. Windows will reinstall a baseline driver automatically.
4. Download the latest manufacturer driver from your laptop maker's support site and install it fresh.
5. Restart once more and verify with several sleep/wake cycles.
6. If Windows keeps reinstalling a bad driver, use **Show or hide updates** (`wushowhide.diagcab`) to block that specific driver version.

### Fix 6: Disconnect USB devices before sleep

USB devices — especially external drives, docks, and hubs — can block the power transition.

1. Unplug all USB devices except your mouse.
2. Put the laptop to sleep and wake it. If it's stable, plug devices back one at a time, testing sleep each round, to find the culprit.
3. For a permanent offender, open **Device Manager** > **Universal Serial Bus controllers**, right-click the device's entry, open **Properties** > **Power Management**, and uncheck **Allow the computer to turn off this device to save power** — or replace the device.
4. Also update your chipset/USB drivers from the manufacturer support site.

### Fix 7: Run system file checks

Corrupted system files can break the power management framework itself, making every driver's job harder.

1. Open an elevated Command Prompt: **Win + S**, type `cmd`, right-click **Command Prompt**, choose **Run as administrator**.
2. Run `sfc /scannow` and wait for it to finish.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store SFC draws from.
4. Restart and retest. If SFC reports unfixable corruption and crashes continue, an [in-place upgrade using Windows 10 installation media](https://www.microsoft.com/en-us/software-download/windows11) repair is the next step (the media tool can repair without deleting files).

If crashes persist across all of these, check whether Windows keeps restarting too fast to read the screen — our guide on [disabling automatic restart after a BSOD on Windows 10](/articles/how-to-disable-automatic-restart-after-bsod-on-windows-10/) helps you capture the stop code and offending driver name from the blue screen itself.

## Closing

DRIVER_POWER_STATE_FAILURE is frustrating because it interrupts the most basic laptop behavior — closing the lid and walking away. But it's a solvable problem: in almost every case, it's one driver (usually Wi-Fi or graphics) that needs updating, rolling back, or cleanly reinstalling, or Fast Startup preserving bad driver state. Work the list in order, test sleep and wake after each change, and you'll almost certainly find the fix before reaching the end.
