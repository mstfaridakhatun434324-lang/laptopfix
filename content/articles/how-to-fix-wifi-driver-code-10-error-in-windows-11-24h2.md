---
title: "Wi-Fi Driver Code 10 Error in Windows 11 24H2: What It Means and How to Fix It"
slug: how-to-fix-wifi-driver-code-10-error-in-windows-11-24h2
date: 2026-09-03
categories: ["drivers"]
tags: ["wifi driver", "code 10 error", "windows 11 24h2", "device manager"]
description: "Seeing 'This device cannot start (Code 10)' on your Wi-Fi adapter after Windows 11 24H2? Learn what Code 10 means and work through proven fixes to get wireless back."
thumbnail: "/images/thumbs/how-to-fix-wifi-driver-code-10-error-in-windows-11-24h2.webp"
faqs:
  - q: "What does Code 10 mean on a Wi-Fi adapter?"
    a: "Code 10 means Windows tried to start the device and the driver reported a failure — the hardware is detected, but it cannot initialize. On Wi-Fi adapters after the 24H2 update, this almost always means the driver version is incompatible with the updated OS, not that the adapter itself is broken. Reinstalling a compatible driver clears it."
  - q: "Will reinstalling the driver fix a Code 10 error?"
    a: "Yes, in most cases — Code 10 on wireless adapters is a driver problem roughly nine times out of ten. The key is installing the right driver: a clean reinstall of the vendor's Windows 11 driver for your exact adapter model. Generic or outdated drivers can reinstall the same Code 10, so get the package from your laptop or adapter maker's site."
  - q: "Can a Windows update cause Code 10 on Wi-Fi?"
    a: "Absolutely, and the 24H2 update is a frequent trigger. It can replace a working Wi-Fi driver with an incompatible one, corrupt the driver during migration, or change power management in ways the old driver cannot handle. If the error appeared right after an update, driver rollback or a fresh vendor install is the first thing to try."
  - q: "Is Code 10 ever a hardware failure?"
    a: "Occasionally. If the adapter shows Code 10 with every driver version, on a clean Windows install, and in the BIOS or another OS, the adapter itself may have failed. But rule out drivers, power management, and BIOS settings first — hardware failure is the least common cause, and most Code 10s are fixed in software."
---

"This device cannot start. (Code 10)." There it sits in Device Manager next to your Wi-Fi adapter, with a yellow warning triangle, and your wireless networks have vanished. The laptop that connected fine yesterday now lists no Wi-Fi at all — the network icon shows a globe, Settings shows no wireless toggle, and Ethernet is your only way online.

Code 10 is Windows telling you the driver failed to initialize the hardware. The adapter is physically present and detected — otherwise it would not appear in Device Manager at all — but the software that drives it cannot start it. After the Windows 11 24H2 update, this is overwhelmingly a driver-compatibility problem: the update swapped, corrupted, or stranded your Wi-Fi driver. Fix the driver and the adapter starts. If your Wi-Fi card is specifically a MediaTek part, you may also want our [MediaTek Wi-Fi repair guide](/articles/how-to-fix-mediatek-wifi-not-working-in-windows-11-24h2/) for chipset-specific steps.

## Why this happens

- **24H2 installed an incompatible Wi-Fi driver.** The update pulled a driver build that does not match your adapter's firmware.
- **Driver corrupted during the update.** An interrupted migration left the driver half-installed and unable to initialize the chip.
- **Old driver stranded on a new kernel.** The 24H2 kernel changed interfaces the legacy driver needs, so it fails at start.
- **Power management shutting the adapter down.** Aggressive 24H2 power settings starve the adapter before it can initialize.
- **Conflicting driver remnants.** Fragments of the old driver in the driver store conflict with the new install.
- **BIOS wireless setting toggled.** Firmware updates bundled with 24H2 can disable the wireless radio at the BIOS level.
- **Adapter firmware mismatch.** The driver's firmware blob does not match the adapter's revision.
- **Failing adapter hardware.** Rare, but a genuinely dying Wi-Fi card reports Code 10 when it cannot complete initialization.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable and re-enable the adapter

Open **Device Manager**, expand **Network adapters**, right-click your Wi-Fi adapter, and choose **Disable device**. Wait ten seconds, right-click again, and choose **Enable device**. This forces Windows to tear down the failed start sequence and attempt initialization fresh. It sounds too simple, but it clears Code 10 in a surprising number of cases where the failure was a one-time initialization race during boot. Check whether the yellow triangle is gone and whether networks appear.

### Fix 2: Run the network troubleshooter

Press **Windows + I**, go to **System > Troubleshoot > Other troubleshooters**, and run **Network and Internet**. On some 24H2 builds it is under **Get help** instead. The troubleshooter can reset the adapter's failed state, clear the TCP/IP stack's cached failure, and restart the WLAN AutoConfig service. It is not magic, but it automates the first layer of resets and occasionally clears Code 10 when combined with a restart. If it reports it could not fix the problem, continue — the driver needs manual attention.

### Fix 3: Roll back the Wi-Fi driver

In Device Manager, right-click the Wi-Fi adapter, open **Properties > Driver**, and click **Roll Back Driver** if available. The 24H2 update's driver replacement is the single most common trigger, and rolling back to the pre-update driver restores the last known working configuration in about a minute. Restart after the rollback and check for networks. If the rollback button is greyed out, Windows did a full replacement rather than an upgrade — move on to the clean reinstall.

### Fix 4: Clean-reinstall the Wi-Fi driver

Right-click the adapter in Device Manager and choose **Uninstall device**, checking **Attempt to remove the driver for this device** if offered. This purges the broken driver package from the driver store so Windows cannot reinstall the same bad version. Restart the laptop — since the adapter is uninstalled, you will need another way to get online for the next step, or download the driver on another machine first. After the restart, check Device Manager: if Windows installed a working driver, networks return. If it installed the same broken one or nothing at all, proceed to the vendor package.

### Fix 5: Install the vendor's Wi-Fi driver package

Download the Wi-Fi driver for your exact laptop model from [Lenovo support](https://support.lenovo.com/us/en/) or your own manufacturer's site — or from Intel, MediaTek, Realtek, or Qualcomm if you know the adapter brand. For Intel cards specifically, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects your adapter and installs the correct driver automatically. Run the installer, restart, and verify the Code 10 is gone. Vendor and chipset-maker packages include the correct firmware blobs and are validated against your exact hardware — this is the definitive fix for update-induced Code 10s.

### Fix 6: Disable power management on the adapter

In Device Manager, open the Wi-Fi adapter's **Properties > Power Management** tab and uncheck **Allow the computer to turn off this device to save power**. Then go to **Settings > System > Power & battery**, and under the active power mode make sure the wireless adapter is set to **Maximum Performance** when plugged in. The 24H2 update's aggressive power policies can cut power to the adapter mid-initialization, producing a Code 10 that no driver change fixes. This step matters most on laptops where the error appears after sleep or hibernate but not after a cold boot. Lenovo owners seeing this exact error should also check our [Code 10 guide for Lenovo laptops](/articles/how-to-fix-wifi-driver-code-10-error-on-lenovo-laptop/).

### Fix 7: Check the BIOS and reset the network stack

Restart into the BIOS (F2, Del, or your brand's key) and verify the wireless radio is enabled — look under **Advanced** or **Security** for a wireless/WLAN toggle. While there, consider updating the BIOS from the manufacturer's site, since Wi-Fi initialization fixes ship in firmware updates. Back in Windows, open an elevated Command Prompt and run `netsh winsock reset` and `netsh int ip reset`, then restart. This clears corrupted network state that can masquerade as a driver failure. If Code 10 persists through all of this on multiple driver versions, the adapter itself is likely failing and needs replacement.

## Closing

A Code 10 on your Wi-Fi adapter after 24H2 is almost always the update's doing, not your hardware's. The reliable sequence is: disable and re-enable, roll back, clean-reinstall, then install the vendor's exact driver package — with power management checked along the way. Once wireless is back, note which driver version works so you can block Windows Update from replacing it again.
