---
title: "How to Fix the Driver Power State Failure Blue Screen on Windows 11"
slug: driver-power-state-failure-windows-11-fix
date: 2026-09-12
categories: ["windows-errors"]
tags: ["bsod", "driver-power-state-failure", "windows-11"]
description: "DRIVER_POWER_STATE_FAILURE on Windows 11 is almost always a driver issue. Follow these proven steps to stop the crashes for good."
thumbnail: "/images/thumbs/driver-power-state-failure-windows-11-fix.webp"
faqs:
  - q: "What does DRIVER_POWER_STATE_FAILURE mean on Windows 11?"
    a: "It's a blue screen (stop code 0x0000009F) that happens when a device driver fails to respond to a power-state change, such as your laptop going to sleep or waking up. The usual culprits are graphics, Wi-Fi, or chipset drivers, a bad Windows update, or Fast Startup holding onto stale driver states."
  - q: "Can DRIVER_POWER_STATE_FAILURE damage my laptop?"
    a: "The crash itself rarely damages hardware, but repeated forced shutdowns can corrupt Windows system files and cost you unsaved work. If the error appears regularly, treat it as a warning sign — a driver or firmware update usually resolves it before it turns into data loss."
  - q: "Why does it only happen when my laptop wakes from sleep?"
    a: "Because that's exactly when drivers have to change power states. A driver that handles normal operation fine can still hang when asked to sleep or wake a device. Turning off Fast Startup and disabling PCI Express Link State Power Management fixes this pattern in most cases."
  - q: "Should I update drivers through Windows or the manufacturer?"
    a: "Use the laptop manufacturer's support site (Dell, HP, Lenovo, ASUS) first, since they test drivers against your exact model. Windows Update is a decent fallback, and Intel's Driver & Support Assistant works well for Intel Wi-Fi and chipset drivers on any brand."
---
The DRIVER_POWER_STATE_FAILURE blue screen is one of the most common crashes on Windows 11 laptops, and it almost always points to the same thing: a driver that misbehaves when your machine changes power states. It tends to strike when your laptop goes to sleep, wakes up, or shuts down — moments when drivers are asked to power devices down or bring them back online.

The good news is this error is very fixable. In the vast majority of cases it's a software problem — an outdated graphics or Wi-Fi driver, a Windows update that replaced a working driver with a generic one, or a power setting like Fast Startup getting in the way. Work through the fixes below in order and you should have it sorted within the hour.

## Why this happens

- **Outdated or buggy device drivers.** Graphics, Wi-Fi, Bluetooth, and chipset drivers that don't properly handle sleep/wake transitions are the number one cause of this stop code.
- **A Windows update swapped your driver.** Major Windows 11 updates sometimes replace a manufacturer-tuned driver with a generic Microsoft one that doesn't handle your laptop's power management correctly.
- **Fast Startup is holding stale driver states.** This hybrid shutdown feature saves driver state to disk, which means a misbehaving driver gets reloaded in its broken state every single boot.
- **Aggressive power-saving settings.** PCI Express Link State Power Management and USB selective suspend can cause devices to enter low-power states their drivers can't wake them from cleanly.
- **Outdated BIOS or firmware.** Your motherboard firmware mediates power transitions between Windows and your hardware; old firmware can time out drivers that expect faster responses.
- **Failing hardware or overheating.** Less common, but a dying SSD, flaky RAM, or a laptop that crashes because it's running too hot can produce the same stop code.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Test sleep and wake a few times after each step — you don't need to keep going once the crashes stop.

### Fix 1: Boot into Safe Mode first (if the crashes won't stop)

If the blue screen hits before you can do anything, get into Safe Mode so you have a stable environment to work from.

1. Power your laptop off completely, then turn it on. As soon as you see the manufacturer's logo, hold the power button to force it off again.
2. Repeat this **three times**. On the fourth boot, Windows will enter the **Windows Recovery Environment**.
3. Go to **Troubleshoot > Advanced options > Startup Settings** and click **Restart**.
4. Press **5** to start in **Safe Mode with Networking**. If the crashes were constant, you should now have a stable desktop. If you can boot normally already, skip this fix.

For more detail on the different ways to get there, see our guide on [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/).

### Fix 2: Update your graphics, Wi-Fi, and chipset drivers

This resolves the error most of the time. Prioritize the drivers most likely to cause power-state issues.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Display adapters**, right-click your GPU, and choose **Update driver > Search automatically for drivers**.
3. Do the same under **Network adapters** for your Wi-Fi card and under **System devices** for chipset/PCI entries.
4. For the best results, also grab drivers from your laptop maker's support site — for example, [Dell's support page](https://www.dell.com/support) or HP's support site — and install the latest chipset, graphics, and network drivers for your exact model.
5. Intel-based laptops can also use [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect and update Intel Wi-Fi and chipset drivers automatically.
6. Restart normally (not from Safe Mode) and test sleep and wake a few times.

### Fix 3: Turn off Fast Startup

Fast Startup is a frequent trigger for this specific error because it preserves driver state across shutdowns.

1. Open **Control Panel** and go to **Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do** in the left pane.
3. Click **Change settings that are currently unavailable** at the top.
4. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
5. Shut down completely (hold **Shift** while clicking **Shut down** for a full shutdown this once), then power back on.

### Fix 4: Tame the power plan settings

Stop Windows from putting devices into deep low-power states that drivers struggle to recover from.

1. Open **Control Panel > Hardware and Sound > Power Options** and click **Change plan settings** next to your active plan.
2. Click **Change advanced power settings**.
3. Expand **PCI Express > Link State Power Management** and set it to **Off** for both battery and plugged in.
4. Expand **USB settings > USB selective suspend setting** and set it to **Disabled**.
5. Expand **Wireless Adapter Settings > Power Saving Mode** and set it to **Maximum Performance** while plugged in.
6. Click **OK** and restart. These changes cost a small amount of battery life but eliminate a whole class of wake-related driver crashes.

### Fix 5: Repair corrupted Windows system files

A crashed driver can leave system files damaged, which causes further crashes. Clean them up with two built-in tools.

1. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Run the system file checker: `sfc /scannow` — let it finish, which can take 10–15 minutes.
3. Then run the image repair tool: `DISM /Online /Cleanup-Image /RestoreHealth` — this one needs an internet connection.
4. Restart your laptop when both complete. If SFC reports it couldn't fix everything, run it once more after the DISM step.

Microsoft's own [Windows support hub](https://support.microsoft.com/en-us/windows) has additional guidance on these repair tools if you run into errors while they run.

### Fix 6: Update your BIOS and firmware

If the crashes started after a Windows 11 feature update, your BIOS may be behind what the new build expects.

1. Find your exact model on the manufacturer's support site (the same Dell or HP pages linked in Fix 2 work fine).
2. Download the latest **BIOS/UEFI** update listed for your model.
3. Close all programs, plug in the charger (never flash BIOS on battery), and run the updater. Don't touch the laptop while it flashes.
4. After it restarts, test sleep/wake again. BIOS updates often include fixes for exactly these power-transition timing issues.

### Fix 7: Check the hardware and Event Viewer

If everything above failed, look for a hardware culprit before considering a clean install.

1. Press **Win + X** and open **Event Viewer**. Navigate to **Windows Logs > System** and look for red **Error** entries from source **Kernel-Power** or **BugCheck** around the time of each crash — the BugCheck details include the failing driver filename (often ending in `.sys`).
2. If a specific `.sys` file is named, search for it and update or remove the software that owns it (common offenders: `nvlddmkm.sys` for NVIDIA, `rtwlane.sys` for Realtek Wi-Fi).
3. Run a memory check: press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
4. As a last resort, use **Settings > System > Recovery > Reset this PC** and choose **Keep my files**. This reinstalls Windows with clean drivers while preserving your documents. This general approach is covered more broadly in our [blue screen of death troubleshooting guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Closing

DRIVER_POWER_STATE_FAILURE looks alarming, but on Windows 11 laptops it's a driver problem far more often than a hardware one. Updating your GPU, Wi-Fi, and chipset drivers, switching off Fast Startup, and relaxing the PCI Express power settings will resolve it for the overwhelming majority of people. If you got as far as the BIOS update and the crashes continue, the Event Viewer step above is your best clue for what to replace or reinstall next.
