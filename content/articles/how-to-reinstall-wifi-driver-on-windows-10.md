---
title: "How to Reinstall the WiFi Driver on Windows 10"
slug: how-to-reinstall-wifi-driver-on-windows-10
date: "2026-09-05"
categories: ["drivers"]
tags: ["wifi driver", "windows 10", "wireless adapter", "driver reinstall", "network fix"]
description: "WiFi broken on Windows 10? Learn how to reinstall the wireless driver properly — quick Device Manager reinstall, clean manufacturer install, and rollback."
thumbnail: "/images/thumbs/how-to-reinstall-wifi-driver-on-windows-10.webp"
faqs:
- q: "How is reinstalling a WiFi driver on Windows 10 different from Windows 11?"
  a: "The core process is identical — Device Manager, uninstall, reinstall — but the settings live in different places. Windows 10 uses the classic Control Panel network applets and the older Settings layout, while Windows 11 reorganized them. Driver behavior is the same on both, so the techniques transfer directly; only the navigation paths differ, and this guide uses the Windows 10 locations throughout."
- q: "Will I lose my WiFi passwords when reinstalling the driver?"
  a: "No. A driver reinstall leaves your saved networks and passwords untouched — they are stored in Windows network profiles, separate from the driver. Only the full network reset option removes saved networks. If you plan to use the network reset as a last resort, write down your WiFi passwords first, since you will need to re-enter them afterward."
- q: "What if I have no internet to download the driver?"
  a: "Download it on another device and transfer it via USB drive — your laptop manufacturer's support page has the WiFi driver for your exact model. Alternatively, connect your phone via USB and enable USB tethering, which gives the laptop internet through the phone connection. Download the driver before uninstalling the old one, so you are never stranded without a way to get online."
- q: "Should I update to the newest WiFi driver or reinstall the old one?"
  a: "Reinstall the manufacturer's recommended version first — newest is not automatically best for wireless drivers, and some updates introduce instability. If the manufacturer's version works, stop there. Only try newer versions from the chip maker if the manufacturer's driver fails, and use rollback if a new version makes things worse. Stability beats novelty for WiFi drivers."
---

Windows 10 remains on millions of laptops, and its WiFi driver problems are the same ones Windows 11 has: updates that replace working drivers, corruption from interrupted installs, and vendor utilities fighting the OS for control of the adapter. The repair is equally the same — a proper driver reinstall — but the menus and dialogs you navigate look different from Windows 11's, which is why this guide exists as its own walkthrough.

There are two depths of reinstall. The quick version takes two minutes in Device Manager and fixes simple corruption. The clean version — downloading the manufacturer's package first, fully removing the old driver, installing fresh — fixes the stubborn cases: vanishing adapters, endless disconnects, and drivers that reinstall broken. Know which one you need before you start, and never uninstall without the replacement driver already downloaded.

Follow the fixes in order. Each builds on the last, and you stop as soon as WiFi is stable.

## Why this happens

- **Windows Update replaced the working driver**: Windows 10's update cycle regularly swaps vendor WiFi drivers for its own versions.
- **Corrupted driver files**: Failed updates and disk errors damage the driver, causing drops rather than clean failure.
- **Vendor utility conflicts**: Manufacturer wireless tools compete with Windows 10's native WiFi management.
- **Power management parking the card**: Driver power-saving puts the adapter to sleep and fails to wake it.
- **Stale configuration surviving reinstalls**: Quick uninstalls leave old settings that re-corrupt the fresh driver.
- **Wrong driver for the hardware revision**: Similar model numbers can hide different wireless chips.
- **Failing hardware mimicking software**: A dying card produces symptoms no driver reinstall will fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Quick reinstall in Device Manager

When WiFi broke suddenly — after an update, a crash, or a bad shutdown — the quick reinstall is the right first move. It forces Windows to redetect the wireless adapter and rebuild the driver binding from the local driver store. No download, no risk, and it resolves straightforward corruption in minutes.

1. Press Win + X and open Device Manager.
2. Expand "Network adapters" and right-click your wireless adapter.
3. Choose "Uninstall device" but do NOT tick "Delete the driver software for this device."
4. Click Action in the menu, then "Scan for hardware changes" — or simply restart.
5. After redetection, reconnect to your WiFi network and test stability.

### Fix 2: Download the Windows 10 driver first

Before any deeper uninstall, secure the replacement. A laptop with no working WiFi driver cannot download its own rescue, and Windows 10's built-in driver library does not cover every wireless chip. Grab the manufacturer's Windows 10 WiFi driver for your exact model now, while you still have a way to get online.

1. Identify your exact model from the bottom sticker or System Information (msinfo32).
2. Visit the manufacturer's support page and find the Wireless/WiFi driver for Windows 10 64-bit.
3. Save the installer somewhere obvious, like the Desktop.
4. No connection on the laptop? Use a phone or second PC and a USB flash drive.
5. Verify the download completed fully before proceeding — a partial installer is worse than none.

### Fix 3: Clean install with full driver removal

The clean install is for adapters that misbehave identically after a quick reinstall, show warnings in Device Manager, or appear as [unknown devices](/articles/how-to-fix-unknown-device-in-device-manager/). This time the old driver is deleted entirely — files and settings — so the manufacturer's package installs onto clean ground instead of inheriting corruption.

1. In Device Manager, right-click the wireless adapter and choose "Uninstall device."
2. TICK "Delete the driver software for this device" and confirm.
3. Run the manufacturer's installer from Fix 2 and restart when prompted. For Intel cards, [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects and installs the right package automatically.
4. After reboot, confirm the adapter appears in Device Manager without warnings.
5. Reconnect to WiFi and test for at least ten minutes — drops often take a while to recur.

### Fix 4: Roll back a bad driver update

If WiFi broke right after a driver update, the previous version was working — restore it. Windows 10 keeps the old driver available through the rollback button, which is faster and safer than hunting down old installers. This is the correct move whenever the timeline implicates an update.

1. In Device Manager, right-click the wireless adapter and open Properties.
2. Go to the Driver tab and click "Roll Back Driver."
3. Choose a reason and confirm, then restart.
4. Test WiFi stability on the restored driver.
5. If rollback is unavailable, install the older version manually from the manufacturer's driver archive.

### Fix 5: Use Windows 10's network reset

When the adapter is present but connections fail strangely — "connected, no internet," endless "identifying," or profiles that will not connect — the network configuration itself is damaged. Windows 10's network reset (Settings, Network and Internet, Status, Network reset) reinstalls every network adapter and wipes all network settings to defaults. Remember: this deletes saved WiFi passwords.

1. Open Settings, Network and Internet, Status, and click "Network reset."
2. Click "Reset now" and confirm — the PC will restart automatically.
3. After reboot, check Device Manager for a healthy wireless adapter.
4. Reconnect to your WiFi network, re-entering the password.
5. If problems persist past the reset, the issue is likely the driver version — revisit Fix 3 with a different version.

### Fix 6: Stop Windows 10 reinstalling the bad driver

Windows 10 will cheerfully replace your fixed driver with the problematic one again via Windows Update. To make the repair stick, block driver updates: open System Properties (Win + Pause), Advanced system settings, Hardware tab, "Device Installation Settings," and choose "No." This stops Windows fetching drivers while leaving security updates untouched. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document this setting.

1. Press Win + Pause/Break to open System, then "Advanced system settings."
2. Open the Hardware tab and click "Device Installation Settings."
3. Select "No (your device might not work as expected)" and save.
4. Alternatively, use the Group Policy "Do not include drivers with Windows Updates" on Pro editions.
5. Get future driver updates from the manufacturer, not Windows Update.

### Fix 7: Confirm the hardware is healthy

If every driver version fails identically and the adapter is missing even with hidden devices shown, test below the OS. Boot a Linux live USB: wireless working there proves Windows is at fault (consider a Windows refresh); no wireless there either proves the card is dead. Most Windows 10-era laptops use replaceable M.2 WiFi cards, and a USB WiFi adapter is an instant workaround.

1. Boot a Linux live USB and check for WiFi networks.
2. Working in Linux means a Windows-side problem — back up and consider refreshing Windows.
3. Dead in both means hardware — reseat the M.2 card if comfortable, or replace it.
4. A USB WiFi adapter bypasses the internal card entirely and works in minutes.
5. For in-warranty machines, report the Linux test result to support — it proves hardware failure cleanly.

On Windows 11 instead of 10, the companion [Windows 11 WiFi driver reinstall](/articles/how-to-reinstall-wifi-driver-on-windows-11/) covers the same process with that OS's interface. If the adapter is missing rather than misbehaving, see [network adapter missing](/articles/how-to-fix-network-adapter-missing-youtube/).

## Closing

Windows 10 WiFi driver repair is a sequence, not a single click: quick reinstall for simple corruption, clean manufacturer install for stubborn cases, rollback when updates cause the damage, and a network reset for configuration wreckage. Download the driver before you uninstall, block Windows Update from undoing the fix, and test stability before declaring victory — the card hardware is the last suspect, not the first.
