---
title: "How to Fix WiFi Driver Code 10 Error on Windows 11"
slug: how-to-fix-wifi-driver-code-10-error-on-windows-11
date: 2026-09-11
categories: ["drivers"]
tags: ["wifi driver", "code 10", "device cannot start", "windows 11"]
description: "WiFi adapter showing 'This device cannot start (Code 10)' on Windows 11? Fix it with these driver repairs — reinstall, power management tweaks, and registry-free solutions."
thumbnail: "/images/thumbs/how-to-fix-wifi-driver-code-10-error-on-windows-11.webp"
faqs:
  - q: "What does WiFi Code 10 'This device cannot start' mean?"
    a: "Code 10 means Windows tried to start the WiFi adapter's driver and the driver reported a failure during initialization. The hardware is usually fine — the driver can't complete its startup handshake with the device, typically because the driver files are corrupt, the wrong driver version is installed, power management is cutting the device, or a Windows update broke the driver-device pairing. It is a driver-layer failure, not a dead WiFi card."
  - q: "Will reinstalling the WiFi driver fix Code 10?"
    a: "In most cases, yes. Uninstalling the adapter in Device Manager with the driver software removed, then restarting, forces Windows to build a fresh driver installation — which resolves the corrupt state causing Code 10. For the best result, install the manufacturer's driver afterward rather than relying on the generic Windows one. The full [WiFi driver reinstall guide](/articles/best-way-to-reinstall-wifi-driver/) walks through the cleanest method."
  - q: "Can Windows Update cause WiFi Code 10 errors?"
    a: "Yes, this is one of the most common triggers. Windows Update frequently pushes newer WiFi drivers — especially for Intel AX200/AX201/AX210 cards — that have initialization bugs on specific laptop models. If Code 10 appeared right after an update, roll back the driver in Device Manager or install the previous version from your laptop maker's support site, then pause updates to prevent reinstallation."
  - q: "Is Code 10 a hardware problem with my WiFi card?"
    a: "Rarely. Genuine hardware failure usually shows as Code 43 or the device disappearing entirely, not Code 10. Suspect hardware only if Code 10 survives a full driver wipe, a BIOS update, and testing in another OS or a Linux live USB. Before concluding hardware failure, also check that the card is properly seated if your laptop has a replaceable M.2 WiFi module."
---

In Device Manager, your WiFi adapter wears a yellow warning triangle, and its status reads: "This device cannot start. (Code 10)." The WiFi icon is gone from the taskbar, no networks appear, and your laptop is effectively offline. It's a stark error — but Code 10 is one of the more fixable Device Manager codes.

Code 10 means the driver failed to start the device — the software handshake between Windows and the WiFi card broke down. The card itself is almost always fine. Work through these fixes in order; most Code 10 cases resolve by the third fix.

## Why this happens

- **Corrupt WiFi driver files:** Partial updates or disk errors leave the driver unable to complete initialization.
- **Wrong driver version for the card:** A driver for a different card revision (e.g., AX201 vs AX211) installs but can't start the hardware.
- **Windows Update driver conflict:** A pushed driver with an initialization bug replaces a working one.
- **Power management cutting the adapter:** Aggressive power saving prevents the card from initializing at boot.
- **Fast Startup caching a failed state:** A failed initialization gets cached and replayed on every boot.
- **BIOS/firmware incompatibility:** Old BIOS versions mishandle newer WiFi cards' power states.
- **Corrupt driver store:** Windows' driver repository holds damaged files that get reinstalled on every attempt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Uninstall the adapter and let Windows rebuild it

The standard Code 10 repair: wipe the driver state and let Windows start clean.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Network adapters**, right-click the WiFi adapter (Intel Wireless, Realtek, MediaTek, or Qualcomm), and choose **Uninstall device**.
3. Tick **Attempt to remove the driver for this device** and confirm.
4. Restart the laptop — do a full restart, not a shutdown (Fast Startup can preserve the broken state).
5. After reboot, check Device Manager: Windows will have reinstalled the adapter.

If the yellow triangle is gone and WiFi works, you're done. If Code 10 returns immediately, the driver Windows chose is itself the problem — continue.

### Fix 2: Install the manufacturer's WiFi driver

The laptop maker's driver is validated against your exact card and BIOS — Microsoft's generic one sometimes isn't.

1. On another device (or via USB tethering from your phone), go to your laptop maker's support site — Dell, HP, or Lenovo.
2. Enter your exact model and download the **wireless/WiFi driver**.
3. Transfer it to the laptop via USB drive if needed, and install it.
4. Restart and check Device Manager.

For Intel cards specifically, Intel's own driver from [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is also reliable. The step-by-step [reinstall walkthrough](/articles/best-way-to-reinstall-wifi-driver/) covers the offline-install scenario in detail.

### Fix 3: Disable power management on the WiFi adapter

Power saving can prevent the card from initializing — a classic Code 10 trigger on laptops.

1. In Device Manager, right-click the WiFi adapter and choose **Properties**.
2. Go to the **Power Management** tab and untick **Allow the computer to turn off this device to save power**.
3. Go to the **Advanced** tab and look for power-related properties (**Power Saving Mode**, **Selective Suspend**) — set them to **Maximum Performance** or **Disabled**.
4. In **Settings > System > Power & battery**, set **Power mode** to **Best performance** temporarily.
5. Restart and test.

If Code 10 clears on AC power but returns on battery, you've confirmed power management as the cause — keep those settings.

### Fix 4: Roll back the driver

If Code 10 appeared after an update, the previous driver was working — go back to it.

1. In Device Manager, right-click the WiFi adapter, choose **Properties**, then the **Driver** tab.
2. Click **Roll Back Driver** if it's available, choose a reason, and confirm.
3. Restart and verify WiFi works.
4. Immediately go to **Settings > Windows Update** and **Pause updates** for a few weeks to stop the bad driver returning.
5. Use **Show or hide updates** troubleshooter to block the specific driver version if needed.

If rollback is greyed out, manually install the older driver from the manufacturer's site (Fix 2's method, choosing a previous version).

### Fix 5: Disable Fast Startup and reset the network stack

A cached failed initialization can survive normal restarts.

1. **Control Panel > Power Options > Choose what the power buttons do** > **Change settings that are currently unavailable** > untick **Turn on fast startup**.
2. Open Command Prompt as administrator and run:
   `netsh winsock reset`
   `netsh int ip reset`
   `ipconfig /flushdns`
3. Shut down fully, wait 30 seconds, power on.
4. Check Device Manager for the adapter status.

The network stack reset also clears corrupted TCP/IP state that can accompany driver failures.

### Fix 6: Update the BIOS

BIOS updates frequently include fixes for WiFi card power sequencing and initialization.

1. Check your current BIOS version: **Win + R**, type `msinfo32`, look at **BIOS Version/Date**.
2. On the manufacturer's support site, compare with the latest for your model.
3. Download and install the BIOS update following the maker's instructions exactly — keep the laptop plugged into AC power throughout.
4. After the update, boot into Windows and check the adapter.

Never interrupt a BIOS update. This fix specifically helps when Code 10 appears with newer WiFi cards (AX211, BE200) in older laptop models.

### Fix 7: Clean the driver store and test the hardware

If Code 10 survives everything, purge Windows' driver repository and verify the card itself.

1. In Device Manager, enable **View > Show hidden devices** and uninstall every greyed-out WiFi adapter entry.
2. Open Command Prompt as administrator and run `pnputil /enum-drivers`, then remove stale WiFi driver packages with `pnputil /delete-driver oemXX.inf /uninstall` (match the WiFi provider name carefully).
3. Restart and install the manufacturer's driver fresh.
4. As a hardware test, boot a Linux live USB — if WiFi works there, the card is fine and Windows is the problem; if it fails there too, the card may genuinely be faulty.

Persistent Code 10 across operating systems means hardware failure — replace the M.2 WiFi card (a $20–30 part on most laptops) or use a USB WiFi adapter. If the adapter has vanished from Device Manager entirely instead, see the [missing WiFi adapter guide](/articles/best-way-to-fix-wifi-adapter-not-showing-up/).

## Closing

Code 10 looks alarming but it's a software handshake failure, not a dead card. The repair ladder — uninstall and rebuild, install the manufacturer's driver, tame power management — resolves it in the large majority of cases. Once WiFi is back, pausing driver updates through Windows Update for a while prevents the same bad driver from being pushed again.
