---
title: "System Thread Exception Not Handled After a Windows 11 Update: How to Fix"
slug: how-to-fix-system-thread-exception-not-handled-after-windows-11-update
date: 2026-09-24
categories: ["windows-errors"]
tags: ["bsod", "system-thread-exception", "windows-11"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED after a Windows 11 update is usually a driver that broke. Find the culprit and fix it here."
thumbnail: "/images/thumbs/how-to-fix-system-thread-exception-not-handled-after-windows-11-update.webp"
faqs:
  - q: "What does SYSTEM_THREAD_EXCEPTION_NOT_HANDLED mean?"
    a: "It's a blue screen (stop code 0x0000007E) that occurs when a system thread — usually inside a driver — throws an exception the error handler can't deal with. After a Windows update, the cause is almost always a driver that became incompatible with the new build, with graphics drivers leading the list."
  - q: "The error shows a driver name like atikmdag.sys or nvlddmkm.sys. What does that tell me?"
    a: "Everything. That filename identifies the exact driver that crashed: atikmdag.sys is AMD graphics, nvlddmkm.sys is NVIDIA graphics, Netwtw10.sys is Intel Wi-Fi. Update, roll back, or clean-reinstall that specific driver and the crashes usually stop immediately."
  - q: "Why does it happen in a boot loop after updating?"
    a: "Because the broken driver loads on every boot and crashes the same way each time. Windows can't get past it. Break the loop by booting into Safe Mode (which skips third-party drivers) or the recovery environment, then remove or roll back the driver."
  - q: "Can I prevent this before installing the next Windows update?"
    a: "Largely, yes. Update your graphics, Wi-Fi, and chipset drivers from the laptop manufacturer's site before installing a feature update, and create a system restore point first. That combination prevents the great majority of post-update driver crashes."
---
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (stop code 0x0000007E) is Windows telling you that a driver crashed so badly the system couldn't recover from it. When it shows up right after a Windows 11 update, the diagnosis is straightforward: the update changed something, and one of your drivers couldn't handle the change.

The encouraging part is that this blue screen very often names the failing driver right on the screen — sometimes with the filename in parentheses after the stop code. That turns a scary crash into a simple driver replacement job. Here's the full process.

## Why this happens

- **A graphics driver incompatible with the new build.** The update changed kernel interfaces the GPU driver relies on — the single most common cause.
- **The update installed a faulty driver version.** Windows Update bundles driver updates with OS updates, and the bundled version may itself be buggy.
- **Old drivers that the new build no longer tolerates.** Drivers written for much older Windows 11 builds can throw unhandled exceptions under the new kernel.
- **Corrupted driver files from the update process.** An interrupted or partial update can damage driver files in the driver store.
- **Conflicting third-party software.** Antivirus, VPN clients, and system utilities with kernel drivers can clash with the updated system.
- **Underlying hardware faults.** Rare for this stop code, but failing RAM or an overheating GPU can make a healthy driver throw exceptions.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once the crashes stop.

### Fix 1: Read the driver name off the blue screen

This single step can save you an hour.

1. The next time it crashes, look for text after the stop code — it often reads **SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (atikmdag.sys)** or similar.
2. Photograph the screen with your phone; it's gone in seconds.
3. Common names: `atikmdag.sys` / `amdkmdag.sys` (AMD graphics), `nvlddmkm.sys` (NVIDIA graphics), `igdkmd64.sys` (Intel graphics), `Netwtw10.sys` (Intel Wi-Fi), `rtwlane.sys` (Realtek Wi-Fi).
4. Once you know the file, jump to Fix 3 and target that driver. If nothing is named, keep going in order.

### Fix 2: Break the boot loop via Safe Mode

A crashing driver that loads at boot needs to be bypassed.

1. Interrupt the boot three times (hold the power button at the logo screen) to reach the **Windows Recovery Environment**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **5** for **Safe Mode with Networking**.
3. Safe Mode loads only Microsoft's basic display driver, so a broken GPU driver can't crash the boot. If the system is stable here, the third-party driver is confirmed as the cause.

### Fix 3: Update, roll back, or clean-reinstall the driver

The fix that works in the large majority of cases.

1. In Safe Mode, press **Win + X** and open **Device Manager**.
2. Find the device for your culprit driver: **Display adapters** for GPU files, **Network adapters** for Wi-Fi files.
3. Right-click it, choose **Properties > Driver tab**. If the crash started with the update, click **Roll Back Driver** to restore the pre-update version.
4. Otherwise, download the latest driver from the source and install it over the old one: your laptop maker's support page, or [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) for NVIDIA cards (choose **Custom install** and tick **Perform a clean installation**).
5. For AMD or Intel graphics, get the driver from the laptop manufacturer's site first — their builds are validated for your model's switchable graphics. Then restart normally.
6. The [24H2-specific version of this error](/articles/how-to-fix-system-thread-exception-not-handled-in-windows-11-24h2/) follows the same driver-first logic with build-specific notes.

### Fix 4: Uninstall the Windows update that triggered it

Useful when the driver was fine until the update landed.

1. In Safe Mode, go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent update and restart normally.
3. If the system is stable, update the driver from the manufacturer's site (Fix 3), then reinstall the Windows update. Pause updates briefly if you need time to get the driver sorted.

### Fix 5: Remove conflicting third-party software

Kernel-level utilities are the next suspects after drivers.

1. In Safe Mode, go to **Settings > Apps > Installed apps**.
2. Uninstall third-party antivirus completely (not just disable — the kernel driver stays loaded otherwise), plus any VPN client, system optimizer, or driver-updater tools installed recently.
3. Restart normally. Windows Defender protects you while the third-party product is gone.
4. If stability returns, reinstall the latest version of the software — vendors patch these incompatibilities quickly. Similar post-update conflicts cause errors like [kernel security check failures](/articles/how-to-fix-kernel-security-check-failure-after-windows-11-update/), which respond to the same cleanup.

### Fix 6: Repair system files and test the hardware

Cover corruption and the rare hardware causes.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Test RAM with `mdsched.exe` (**Restart now and check for problems**) — replace sticks that fail.
4. Monitor GPU temperatures under load; sustained temps above 90°C on a laptop GPU can make drivers throw exceptions. Clean the cooling system with compressed air.

### Fix 7: Reset Windows as the final software step

When the driver is current, files are clean, and it still crashes.

1. Back up your files.
2. Go to **Settings > System > Recovery > Reset PC**, choose **Remove everything** with **Cloud download**.
3. After setup, install drivers from the laptop manufacturer's site before anything else, and verify stability before reinstalling third-party software.
4. Persistent crashes on a clean install indicate a hardware fault — most likely the GPU or motherboard. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has guidance on repair options.

## Closing

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED after an update is a driver problem wearing a frightening mask. Read the filename off the blue screen, roll back or clean-reinstall that driver, and you're usually done in twenty minutes. And the next time a feature update arrives, update your graphics and chipset drivers first and set a restore point — it's the cheapest insurance against ever seeing this screen again.
