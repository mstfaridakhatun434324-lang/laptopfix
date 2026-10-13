---
title: "System Thread Exception Not Handled in Windows 11 24H2: How to Fix"
slug: how-to-fix-system-thread-exception-not-handled-in-windows-11-24h2
date: 2026-10-01
categories: ["windows-errors"]
tags: ["bsod", "system-thread-exception", "windows-11-24h2"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on Windows 11 24H2? A driver crashed that the new build won't tolerate. Fix it with these steps."
thumbnail: "/images/thumbs/how-to-fix-system-thread-exception-not-handled-in-windows-11-24h2.webp"
faqs:
  - q: "Why does 24H2 trigger this error more than older builds?"
    a: "The 24H2 kernel changed driver interfaces and tightened exception handling. Drivers written for 23H2 — especially graphics, audio, and peripheral drivers that were never updated — can throw exceptions the new build can't handle. The driver was always fragile; 24H2 just exposes it."
  - q: "The blue screen names a driver file. How reliable is that?"
    a: "Very reliable for this stop code. The filename in parentheses after SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is the driver whose thread crashed. Update, roll back, or clean-reinstall exactly that driver — it's the fastest possible fix."
  - q: "It crashes in a loop and I can't get to the desktop. What now?"
    a: "Break the loop with Safe Mode: interrupt the boot three times to reach the recovery environment, then Startup Settings > Safe Mode with Networking. Safe Mode skips third-party drivers, giving you a stable desktop to remove or roll back the bad driver."
  - q: "Should I roll back to 23H2 instead of fixing the driver?"
    a: "That's a last resort, not a first step. Rolling back the whole build is disruptive and only temporary — 24H2 will be offered again. Fixing the one bad driver takes twenty minutes and solves it permanently."
---
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (stop code 0x0000007E) on Windows 11 24H2 means a driver's system thread threw an exception the kernel couldn't handle. In practice on this build, it's a driver that 23H2 tolerated and 24H2 doesn't — the new kernel's changed interfaces and stricter exception handling expose fragility that was always there.

The good news hasn't changed either: this blue screen frequently names the crashing driver right on the screen, often in parentheses after the stop code. On 24H2, that name plus a build-compatible driver replacement is the whole fix for most people — no need to reinstall Windows or replace hardware. The steps below walk through the entire process, from reading the crash details to verifying the fix holds.

## Why this happens

- **23H2-era drivers on the 24H2 kernel.** Graphics, audio, and peripheral drivers never updated for 24H2 throw exceptions under the new build's changed interfaces.
- **The 24H2 upgrade installed a buggy driver.** The upgrade process pushes driver updates that may themselves crash.
- **Lenovo/OEM utility drivers lagging behind.** Manufacturer system drivers (hotkeys, power, WMI) are frequent 24H2 offenders.
- **Corrupted driver files from the upgrade.** The 24H2 installation can damage driver store files.
- **Third-party kernel software.** Antivirus, VPN, and system utilities with drivers that haven't been updated for 24H2.
- **Overheating or failing GPU.** Rare, but thermal stress makes marginal drivers throw exceptions under load.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once the crashes stop.

### Fix 1: Read the driver name off the blue screen

One glance can end the troubleshooting — don't skip this step.

1. Look for the filename in parentheses after the stop code, e.g. **SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (nvlddmkm.sys)**. Photograph it with your phone — it's gone in seconds.
2. Common 24H2 names: `nvlddmkm.sys` (NVIDIA), `atikmdag.sys` (AMD), `igdkmd64.sys` (Intel graphics), `Netwtw10.sys` (Intel Wi-Fi), `rtkvhd64.sys` (Realtek audio).
3. Once identified, jump to Fix 3 and target that driver. If nothing is named, continue in order.

### Fix 2: Break the boot loop with Safe Mode

A driver that crashes every boot needs bypassing before you can fix anything.

1. Interrupt the boot three times (hold the power button at the logo screen) to reach the **Windows Recovery Environment**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **5** for **Safe Mode with Networking**.
3. Safe Mode loads only Microsoft's basic drivers, so the crashing third-party driver can't fire. Stability here confirms the diagnosis and gives you room to work.

### Fix 3: Install the 24H2-compatible driver

The core fix — replace the 23H2-era driver with one built for this build.

1. In Safe Mode, press **Win + X** and open **Device Manager**.
2. Find the device for your culprit driver (**Display adapters** for GPU files, **Network adapters** for Wi-Fi, **Sound, video and game controllers** for audio).
3. Download the driver from your laptop maker's support site — Dell, HP, [Lenovo](https://support.lenovo.com/us/en/) — choosing the version explicitly listed for **Windows 11 24H2** and your exact model.
4. Install it over the old driver. For NVIDIA, choose **Custom install** and tick **Perform a clean installation** on [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx).
5. Restart normally and test. The [post-update version of this error](/articles/how-to-fix-system-thread-exception-not-handled-after-windows-11-update/) covers the same driver-first approach for other builds.

### Fix 4: Roll back the driver the upgrade installed

When 24H2 itself delivered the bad driver.

1. In **Device Manager**, right-click the suspect device and open **Properties > Driver tab**.
2. Click **Roll Back Driver**, choose a reason, and confirm.
3. Restart and test. Then install the manufacturer's 24H2 driver (Fix 3) rather than sitting on the rolled-back version, which misses security fixes.

### Fix 5: Remove un-updated third-party kernel software

Antivirus, VPN, and utilities that haven't caught up with 24H2.

1. In Safe Mode, go to **Settings > Apps > Installed apps**.
2. Fully uninstall third-party antivirus (disabling leaves its kernel driver loaded), VPN clients, and system utilities.
3. Restart normally. If stability returns, reinstall only the latest versions — check the vendor's site for explicit 24H2 support first. The same cleanup resolves sibling 24H2 crashes like [kernel security check failures](/articles/how-to-fix-kernel-security-check-failure-after-windows-11-update/).

### Fix 6: Repair system files and check thermals

Cover upgrade corruption and heat — both can make borderline drivers throw exceptions they wouldn't otherwise.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Monitor CPU/GPU temperatures under load with HWMonitor — sustained temps above 95°C destabilize drivers. Clean vents and fans with compressed air.
4. Test RAM with `mdsched.exe` if crashes are erratic rather than tied to one driver.

### Fix 7: Clean-install 24H2 as the final software step

When every driver is 24H2-current and it still crashes, the upgrade itself is suspect.

1. Back up everything.
2. Create fresh 24H2 media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and clean-install, or use **Settings > System > Recovery > Reset PC** with **Remove everything** and **Cloud download**.
3. Install manufacturer 24H2 drivers first, verify stability, then restore files.
4. Crashes on a clean install indicate a hardware fault — GPU or motherboard — and need professional diagnosis.

## Closing

On 24H2, SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is the new kernel refusing to tolerate a driver that 23H2 let slide. Read the filename off the blue screen, install the 24H2-compatible driver from your laptop maker, and you're done in most cases. Don't roll back the whole build to avoid fixing one driver — the driver fix is faster, permanent, and keeps you on the supported build with its security updates intact. One driver, twenty minutes, problem solved for good — and a restore point set before the next update.
