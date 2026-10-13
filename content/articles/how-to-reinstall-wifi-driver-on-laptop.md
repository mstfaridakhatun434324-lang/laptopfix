---
title: "How to Reinstall the Wi-Fi Driver on a Windows Laptop"
slug: "how-to-reinstall-wifi-driver-on-laptop"
date: "2026-10-02"
categories: ["drivers"]
tags: ["wifi driver", "reinstall", "device manager", "windows 11", "network"]
description: "Wi-Fi misbehaving? Learn the correct way to uninstall and reinstall your wireless driver for a clean, stable connection."
thumbnail: "/images/thumbs/how-to-reinstall-wifi-driver-on-laptop.webp"
faqs:
  - q: "How do I reinstall my Wi-Fi driver on Windows 11?"
    a: "Open Device Manager, expand Network adapters, right-click your Wi-Fi adapter, and choose Uninstall device, ticking the option to delete the driver software. Restart the laptop, then install the latest driver from your laptop manufacturer's support page. Restart once more and reconnect to your network."
  - q: "Will reinstalling the Wi-Fi driver delete my saved networks?"
    a: "Uninstalling the driver alone usually preserves your saved Wi-Fi profiles and passwords. However, a full network reset does remove them. If you want to be safe, note down important Wi-Fi passwords before major network troubleshooting, or export your profiles first."
  - q: "Should I download the driver before uninstalling?"
    a: "Yes, absolutely. If Wi-Fi is your only internet connection, uninstalling its driver leaves you offline with no way to download the replacement. Download the manufacturer's Wi-Fi driver on the laptop first, or use another device and a USB drive, before you uninstall anything."
  - q: "How often should I update my Wi-Fi driver?"
    a: "Update when you have a problem or when the manufacturer releases a version fixing a known issue. Unlike security updates, Wi-Fi drivers do not need constant refreshing. If your connection is stable, leave the driver alone; unnecessary updates are a leading cause of new Wi-Fi problems."
---

Slow speeds, random disconnects, networks that vanish and reappear: a surprising share of Wi-Fi misery traces back to the wireless driver rather than the router. And the fix is refreshingly simple. A proper reinstall clears out corrupted files and stale settings, giving the adapter a clean start.

The key word is proper. Just clicking update driver rarely helps, because it layers new files over the old mess. A real reinstall means removing the driver completely, then installing a fresh copy from the manufacturer. Card-specific issues like [Intel AX201 problems](/articles/how-to-fix-intel-wifi-6-ax201-not-working-on-lenovo-laptop/) use the same technique.

Follow the steps below in order, and download the replacement driver before you remove the old one.

## Why this happens

- **Corrupted driver files:** Interrupted updates and disk errors damage the files the adapter depends on.
- **Stale configuration:** Years of updates accumulate settings that conflict with the current driver version.
- **A bad automatic update:** Windows Update occasionally delivers a Wi-Fi driver that misbehaves on specific cards.
- **Conflicting old profiles:** Corrupted network profiles can interact badly with the driver.
- **Power management bugs:** Older driver versions mishandle sleep and wake transitions.
- **Partial installations:** Failed installs leave a mix of old and new files that never work quite right.
- **Firmware mismatch:** Some cards need a minimum driver version to work with current router features.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Download the replacement driver first

This step prevents the classic self-inflicted outage: uninstalling the Wi-Fi driver with no replacement at hand and no other way online.

1. Identify your exact laptop model and Wi-Fi card in Device Manager.
2. Go to the manufacturer's support page and download the latest Wi-Fi driver.
3. Save the installer somewhere obvious, like the desktop.
4. If Wi-Fi is already dead, use another device and a USB drive.
5. Do not proceed until the installer file is confirmed present.

### Fix 2: Uninstall the Wi-Fi adapter completely

A complete uninstall with driver deletion is what separates a real reinstall from a cosmetic refresh. It removes the files and registry entries that a simple update leaves behind.

1. Open Device Manager and expand Network adapters.
2. Right-click the Wi-Fi adapter and choose Uninstall device.
3. Tick the checkbox to delete the driver software for this device.
4. Confirm the uninstall and keep the laptop powered on.
5. Do not restart yet if you still need to copy the installer over.

### Fix 3: Restart and install the fresh driver

The restart lets Windows redetect the adapter cleanly. Installing the manufacturer's driver immediately after prevents Windows Update from substituting its own version first.

1. Restart the laptop.
2. After booting, run the downloaded manufacturer installer before connecting to anything.
3. Follow the prompts and restart again if asked.
4. Open Device Manager and confirm the adapter shows no warnings.
5. Check the driver version on the Driver tab to confirm the new one is active.

### Fix 4: Reconnect and reconfigure your network

A fresh driver deserves a fresh connection. Rejoining the network cleanly avoids carrying corrupted profile settings into the new installation.

1. Click the network icon and select your Wi-Fi network.
2. Choose Forget first if the old profile behaves strangely, then reconnect.
3. Re-enter the Wi-Fi password carefully.
4. Test browsing, streaming, and a video call for stability.
5. If the network uses enterprise authentication, re-enter those credentials too.

### Fix 5: Tune power management for stability

Fresh drivers still crash if Windows keeps powering the card down aggressively. These settings prevent the sleep-related disconnects that plague laptops.

1. In Device Manager, open the Wi-Fi adapter's Properties.
2. On the Power Management tab, uncheck Allow the computer to turn off this device to save power.
3. In the Advanced tab, set Preferred Band or Roaming Aggressiveness to moderate values if available.
4. Disable USB selective suspend in your power plan for USB-based adapters.
5. Test sleep and wake cycles specifically, since those trigger most power bugs. Our [Wi-Fi 6 guide](/articles/how-to-fix-wifi-6-not-working-on-laptop-in-windows-11-24h2/) has more card-specific tuning.

### Fix 6: Verify stability and block bad versions

The job is not done when Wi-Fi works; it is done when it keeps working. A short observation period plus protection against the bad version returning closes the loop.

1. Use the laptop normally for a full day, including sleep and wake.
2. Note any disconnects, with the time and what you were doing.
3. If problems return, note the driver version and try the previous release.
4. Use the Show or Hide Updates troubleshooter to block a problematic version.
5. Keep the working installer archived for the next time.

### Fix 7: Forget and rebuild corrupted network profiles

A fresh driver can still misbehave if it loads a corrupted saved network profile on connect. Clearing the stored profiles and rejoining the network fresh removes that variable, and it costs nothing but re-entering passwords.

1. Open Settings, then Network and internet, then Wi-Fi.
2. Choose Manage known networks to see the saved list.
3. Forget every saved network, starting with the problematic one.
4. Restart the laptop to clear any cached state.
5. Reconnect to your network and re-enter the password carefully.

### Fix 8: Test with a USB Wi-Fi adapter to isolate hardware

A cheap USB Wi-Fi adapter is the definitive hardware isolation test for wireless problems. If it works perfectly, your internal card or its antennas are suspect; if it fails identically, the problem is system-wide and hardware replacement would be wasted money.

1. Borrow or buy an inexpensive USB Wi-Fi adapter.
2. Plug it in and let Windows install its driver automatically.
3. Connect to your network through the USB adapter.
4. Compare stability over several hours against the internal card.
5. Use the result to decide between replacing the internal card and repairing Windows.

## Closing

Reinstalling a Wi-Fi driver is simple, but doing it properly, download first, full uninstall with deletion, manufacturer driver, power tuning, is what makes the fix stick. Most chronic Wi-Fi weirdness surrenders to this sequence. When it does not, the router, the environment, or the card hardware are the remaining suspects.
