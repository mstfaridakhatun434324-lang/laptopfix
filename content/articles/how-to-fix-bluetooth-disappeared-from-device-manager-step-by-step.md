---
title: "Bluetooth Disappeared From Device Manager: Complete Step-by-Step Fix"
slug: "how-to-fix-bluetooth-disappeared-from-device-manager-step-by-step"
date: "2026-10-12"
categories: ["drivers"]
tags: ["bluetooth disappeared", "device manager", "step by step", "bluetooth fix", "troubleshooting"]
description: "The definitive step-by-step guide to restoring Bluetooth when it's gone from Device Manager — every check in order, from power cycle to hardware testing."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-disappeared-from-device-manager-step-by-step.webp"
faqs:
  - q: "What is the exact order to fix missing Bluetooth?"
    a: "Power-cycle the laptop fully, check function-key and airplane-mode toggles, show hidden devices and remove ghost adapters, reinstall the manufacturer's Bluetooth driver, restart the Bluetooth Support Service, disable USB power saving, check the BIOS, and finally test the hardware with a Linux live USB. This order moves from simplest to most invasive without skipping layers."
  - q: "How long does the full step-by-step process take?"
    a: "The first four steps take about 15 minutes and resolve most cases. The full sequence including driver downloads and a Linux live-USB test can take 45–60 minutes. Do not skip steps — each one rules out a layer, and skipping is how simple problems turn into hours of reinstalling the wrong thing."
  - q: "Do I need to download anything before starting?"
    a: "It helps to download your laptop manufacturer's latest Bluetooth or wireless driver package beforehand, plus have a USB stick ready if you may need the Linux test. Also note your exact laptop model number — driver matching depends on it. Everything else uses tools built into Windows."
  - q: "What if I complete every step and Bluetooth is still missing?"
    a: "If a Linux live USB cannot see the adapter either, the wireless card's Bluetooth function has failed at hardware level. On most laptops this is a replaceable M.2 module costing far less than board repair. Take the documented step results to a technician — you have already done the diagnosis."
---

This is the definitive, no-shortcuts walkthrough for Bluetooth that has vanished from Device Manager. Unlike the version-specific guides, it assumes nothing about your Windows version or laptop brand: every step works everywhere, and the order is deliberate — each step rules out one layer before you touch the next. Follow it top to bottom without skipping. Skipping is how a five-minute power-cycle problem turns into a wasted afternoon of driver reinstalls.

Before you start, gather two things: your exact laptop model number (bottom sticker or `msinfo32`), and the latest Bluetooth/wireless driver downloaded from your manufacturer's support page. Keep Device Manager open throughout so you can watch the Bluetooth category.

## Why this happens

- **Radio stuck in a failed power state**: the Bluetooth radio never completed initialization and the state survived restarts.
- **Ghost driver entries blocking enumeration**: failed adapter entries marked non-present prevent clean re-detection.
- **Wrong or corrupted driver**: a mismatched or damaged driver fails to load, so Windows hides the adapter.
- **Bluetooth Support Service stopped**: the service Windows needs for Bluetooth discovery and pairing is not running.
- **Firmware-level disable**: the radio is switched off in BIOS or by a function-key toggle below the OS.
- **Power management suppression**: USB selective suspend keeps the radio asleep through boot.
- **Hardware failure**: the wireless card's Bluetooth function has genuinely died.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Perform the full power cycle

Step one resets the embedded controller and the radio's power state — the most common stuck condition. Do it exactly; shortcuts here invalidate later diagnosis.

1. Hold **Shift** while clicking **Shut down** for a true shutdown that bypasses Fast Startup.
2. Unplug the charger and remove all peripherals.
3. Hold the power button for 30 seconds, then wait another 30 seconds.
4. Reconnect only the charger and power on.
5. Open Device Manager and check for the Bluetooth category. If it is back, stop here — the radio was stuck, not broken.

### Fix 2: Check every radio toggle

Function-key toggles and airplane mode operate below Device Manager. A radio switched off here is invisible to all driver-level fixes.

1. Press your brand's wireless toggle (**Fn + F8**, **Fn + F2**, or **Fn + F3**) and watch for the on-screen indicator.
2. Toggle airplane mode on and off in **Settings > Network & internet**, waiting 15 seconds between.
3. Check for a physical wireless switch on the laptop's side or front edge.
4. Look in vendor utilities (Vantage, MyASUS, SupportAssist, Omen Gaming Hub) for disabled radios.
5. Recheck Device Manager. If Bluetooth appeared, the toggle was the entire problem.

### Fix 3: Clear ghost devices and rescan

Failed adapters hide as non-present devices. Removing them lets Windows attempt a genuinely clean enumeration.

1. In Device Manager, click **View > Show hidden devices**.
2. Under **Bluetooth**, **Network adapters**, and **USB controllers**, right-click every grayed-out Bluetooth-related entry and choose **Uninstall device**, ticking driver removal.
3. Click **Action > Scan for hardware changes** and watch for the adapter to reappear.
4. If it returns with a warning icon, the driver is corrupt — proceed to Fix 4.
5. If nothing appears, note that and continue — the firmware check in Fix 6 addresses invisible hardware, following the ghost-cleanup method in [our hidden-devices guide](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/).

### Fix 4: Install the manufacturer's driver cleanly

With ghosts cleared, install the correct driver — from your laptop manufacturer's support page for your exact model, not from Windows Update.

1. Disconnect from the internet to prevent Windows Update from racing the install.
2. Run the manufacturer's Bluetooth/wireless driver installer (or use Device Manager > Update driver > Browse my computer).
3. If the installer offers a clean-installation option, take it.
4. Do a full shutdown (Shift + Shut down) and cold boot — not a quick restart.
5. Verify the Bluetooth category persists across two reboots, then pair an actual device. The manufacturer-first rule is the backbone of [our Windows 11 Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/) too.

### Fix 5: Fix the service layer

The driver can be perfect while the Bluetooth Support Service stays stopped. This step takes a minute and is frequently the missing piece.

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Set **Bluetooth Support Service** to **Automatic** and click **Start**.
3. Do the same for **Bluetooth Audio Gateway Service** if present.
4. Run **Settings > System > Troubleshoot > Other troubleshooters > Bluetooth > Run**.
5. Check **Settings > Bluetooth & devices** for the toggle, and retest pairing.

### Fix 6: Check the BIOS and disable power suppression

Two firmware-adjacent layers remain: a BIOS-disabled radio (invisible to Windows) and power management that sleeps the radio through boot.

1. Restart into the BIOS/UEFI and verify Bluetooth/wireless devices are **Enabled**; load optimized defaults, save, exit.
2. In Device Manager, uncheck "Allow the computer to turn off this device to save power" on the Bluetooth adapter and all USB Root Hubs.
3. In Power Options > Advanced, set **USB selective suspend** to **Disabled**.
4. Full shutdown, cold boot, and check Device Manager.
5. If the adapter was firmware-disabled, it appears now — no driver step could ever have fixed that.

### Fix 7: Lock the fix and test the hardware

Protect the working state, then — if Bluetooth never appeared — get a definitive hardware verdict with an independent operating system.

1. Set **Device Installation Settings** to **No** to stop Windows Update replacing your driver.
2. Create a system restore point while Bluetooth works.
3. If the adapter never appeared in any step, boot an Ubuntu live USB and check Settings > Bluetooth.
4. Adapter visible in Linux means Windows is damaged beyond manual repair — do an in-place repair install from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
5. Invisible in Linux too means the M.2 wireless card failed — check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for any final known-issue notes, then replace the card; bring your step-by-step notes to the technician.

## Closing

Seven steps, one principle: walk the enumeration chain from the wall socket inward and never skip a layer. Power cycle, toggles, ghosts, driver, services, firmware and power policy, then hardware isolation. Most Bluetooth disappearances surrender at step one or step four; the later steps exist so the stubborn cases end with a definitive answer instead of a shrug. Document what each step showed — that log is worth real money if the trail ends at a repair shop, and it is the difference between "Bluetooth doesn't work" and a diagnosis.
