---
title: "What to Do If Bluetooth Is Not Working on Your Windows Laptop"
slug: what-to-do-if-bluetooth-not-working
date: 2026-09-28
categories: ["drivers"]
tags: ["bluetooth", "bluetooth not working", "wireless", "device manager", "drivers"]
description: "Bluetooth not working on your Windows laptop? Run through this technician's checklist: quick toggles, driver repair, service restarts, and hardware checks that restore the connection."
thumbnail: "/images/thumbs/what-to-do-if-bluetooth-not-working.webp"
faqs:
  - q: "Why did Bluetooth suddenly stop working after a Windows update?"
    a: "Windows updates sometimes replace your Bluetooth driver with a generic version or reset the Bluetooth Support Service. The fix is usually to reinstall the manufacturer's Bluetooth driver and set the Bluetooth Support Service back to automatic. This is one of the most common post-update issues and rarely indicates failing hardware."
  - q: "My Bluetooth toggle is missing from Settings. What does that mean?"
    a: "A missing toggle means Windows cannot see the Bluetooth radio at all. Check Device Manager for the Bluetooth section — if it is absent, enable hidden devices, look for unknown devices, and reinstall the driver. If the hardware never appears even in BIOS diagnostics, the wireless card itself may have failed or loosened."
  - q: "Bluetooth pairs but keeps disconnecting. How do I stabilize it?"
    a: "Open Device Manager, find your Bluetooth adapter, and on the Power Management tab uncheck 'Allow the computer to turn off this device to save power.' Then update the Bluetooth and Wi-Fi drivers together, since both usually live on the same card and share an antenna. Moving the laptop away from USB 3.0 hubs also helps."
  - q: "Should I remove and re-pair my Bluetooth device first?"
    a: "Yes, it is a fast first step. Go to Settings, Bluetooth & devices, remove the device, restart the laptop, and pair again from scratch. Corrupted pairing profiles cause a surprising share of 'connected but no sound' and intermittent dropouts. If re-pairing fails, move on to the driver-level fixes in this guide."
---

Bluetooth failures are annoying precisely because they feel random. Your headphones worked yesterday, and today the toggle is gone, or the device pairs and immediately drops, or audio stutters like a bad stream. As a technician, I treat Bluetooth problems as a stack: physical radio, driver, Windows services, pairing profile. Work the stack bottom-up and you find the fault fast instead of reinstalling things at random.

The good news is that most Bluetooth failures on Windows laptops are software. The radio hardware is a small chip on the Wi-Fi card, and it rarely dies on its own. Driver corruption, stopped services, power management, and stale pairings account for nearly everything. This guide takes you through the checks in the order a repair bench would run them.

## Why this happens

- **Driver replaced by a Windows update:** Update packages sometimes swap the manufacturer's Bluetooth driver for a generic one that lacks the right firmware hooks.
- **Bluetooth Support Service stopped:** The background service Bluetooth depends on can be disabled by updates, tune-up utilities, or aggressive debloating scripts.
- **Power management killing the radio:** Windows may power down the Bluetooth adapter to save battery, and on some laptops it never wakes back up properly.
- **Airplane mode or hardware switch engaged:** A stuck airplane mode or a physical wireless switch cuts the radio before Windows even gets involved.
- **Corrupted pairing profile:** Stored pairing data for a device can corrupt, causing "connected" with no audio or immediate disconnections.
- **Wi-Fi/Bluetooth combo interference:** Both radios share one card and often one antenna; a bad Wi-Fi driver update can take Bluetooth down with it.
- **BIOS-level radio disable:** Some laptops let the BIOS disable Bluetooth independently of Windows, which no driver reinstall can override.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the basic toggles and restart

Start with the thirty-second checks. Open Settings, go to Bluetooth & devices, and confirm the Bluetooth switch is on. Press Win + A to open Quick Settings and make sure airplane mode is off — a stuck airplane mode is a classic Bluetooth killer, and we have a dedicated guide for when [airplane mode gets stuck on](/articles/how-do-i-fix-airplane-mode-stuck-on/). If your laptop has a physical wireless switch or an Fn-key combo for wireless, cycle it. Then restart the laptop fully (Start, Power, Restart — not just closing the lid). A real restart clears the radio's firmware state, which sleep and hibernate do not. Re-test with your Bluetooth device before going deeper.

### Fix 2: Remove and re-pair the device

If the toggle is on but your device misbehaves, the pairing profile is suspect. Go to Settings, Bluetooth & devices, Devices, find your device, click the three dots, and choose Remove device. Restart the laptop, put your Bluetooth accessory back into pairing mode, and pair it fresh. This clears corrupted link keys and stale audio profiles that cause "paired but no sound" and rapid disconnects. Pair only one device first and test it thoroughly before reconnecting others — if the first device works and the second breaks things, you have a multi-device profile conflict rather than a laptop problem.

### Fix 3: Restart the Bluetooth Support Service

Press Win + R, type `services.msc`, and find Bluetooth Support Service. If it is not running, right-click and start it. Double-click it and set Startup type to Automatic so it survives reboots. Also check the Bluetooth Audio Gateway Service and Bluetooth User Support Service on newer Windows builds — start any that are stopped. These services are the plumbing between the driver and your apps; when a Windows update or a "privacy" utility disables them, the toggle can look fine while nothing actually connects. This single fix resolves a large share of post-update Bluetooth failures, so do it before any driver surgery.

### Fix 4: Reinstall the Bluetooth driver in Device Manager

Open Device Manager (Win + X, Device Manager), expand Bluetooth, right-click your Bluetooth adapter, and choose Uninstall device. If you see a checkbox for deleting the driver software, check it. Restart the laptop — Windows will detect the radio on boot and reinstall a driver automatically. If Device Manager shows no Bluetooth section at all, click View and enable Show hidden devices, then look under Network adapters and Other devices for the radio or an unknown device. A fully missing radio points to BIOS settings or hardware, covered in Fix 6. After reinstalling, verify the driver version is what you expect by following our guide to [check driver versions in Device Manager](/articles/how-to-check-driver-version-in-device-manager-on-windows-11/).

### Fix 5: Install the manufacturer's Bluetooth and Wi-Fi drivers

The automatic driver Windows installs is generic. Go to your laptop maker's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — enter your model, and download both the Bluetooth and the Wi-Fi driver packages. Install Wi-Fi first, then Bluetooth, rebooting between them, because both live on the same physical card and the Bluetooth stack depends on the Wi-Fi driver's firmware loading correctly. This matched pair from the OEM is what the laptop shipped with and tested against. If your exact Bluetooth adapter has vanished from Device Manager entirely, our guide on [fixing Bluetooth missing from Device Manager](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/) goes deeper on recovery. Microsoft's Windows support hub also documents the built-in Bluetooth troubleshooter as a supplementary check.

### Fix 6: Disable power management on the Bluetooth adapter

Back in Device Manager, right-click the Bluetooth adapter, choose Properties, and open the Power Management tab. Uncheck "Allow the computer to turn off this device to save power." Do the same for the Wi-Fi adapter under Network adapters. On battery-conscious laptops, Windows aggressively sleeps the radio and some firmware never resumes it cleanly, producing the classic "Bluetooth dies after the laptop sleeps" pattern. While you are here, go to Settings, System, Power & battery, and set the power mode to Best performance temporarily for testing. If the problem disappears on mains power with power saving off, you have confirmed a power-management fault, not broken hardware.

### Fix 7: Check BIOS settings and run hardware diagnostics

Restart and enter the BIOS/UEFI setup (usually F2, Del, or F12 at boot). Look for a Wireless, Bluetooth, or Onboard Devices section and confirm Bluetooth is enabled. Some business laptops ship with Bluetooth disabled at the firmware level, and no Windows fix can override that. Save and exit, then run your manufacturer's hardware diagnostics — Dell's SupportAssist, HP's PC Hardware Diagnostics, or Lenovo's Vantage diagnostics all include a wireless/Bluetooth test. If diagnostics report the radio as failed or absent, the Wi-Fi/Bluetooth card needs reseating or replacement, which on most laptops is a small, inexpensive part. Do not open the chassis while under warranty; let the manufacturer handle it.

## Closing

Bluetooth troubleshooting is a stack problem, and the stack almost always fails in software: a stopped service, a swapped driver, a power setting, or a stale pairing. Work from toggles to services to drivers to firmware, and you will find the fault without guesswork. Keep the manufacturer's Bluetooth and Wi-Fi drivers as a matched pair, keep the support service on automatic, and the radio will stay where it belongs — quietly working.
