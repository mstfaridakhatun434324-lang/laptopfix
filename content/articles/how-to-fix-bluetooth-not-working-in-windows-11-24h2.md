---
title: "Bluetooth Not Working in Windows 11 24H2? Fix It Now"
slug: how-to-fix-bluetooth-not-working-in-windows-11-24h2
date: 2026-09-30
categories: ["drivers"]
tags: ["windows 11", "24h2", "bluetooth", "driver", "wireless"]
description: "Fix Bluetooth not working after the Windows 11 24H2 update: repair the Bluetooth driver stack, fix pairing failures, and restore wireless accessories."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did Bluetooth stop working after the Windows 11 24H2 update?"
    a: "24H2 changed the driver framework, and older Bluetooth drivers from Intel, Realtek, or MediaTek can fail to load under it. Uninstall the Bluetooth adapter driver with the 'remove driver' option, then install the latest driver from your laptop manufacturer's support site or Intel's driver assistant."
  - q: "Bluetooth toggle is missing from Settings in 24H2. How do I get it back?"
    a: "A missing toggle means Windows cannot see the adapter — the driver failed. Check Device Manager under Bluetooth for a warning icon, uninstall the adapter driver completely, install the current manufacturer driver, and reboot. The toggle returns once the adapter starts."
  - q: "Why do my Bluetooth devices pair but immediately disconnect?"
    a: "The pairing database or the Bluetooth Support Service is usually at fault. Restart the Bluetooth services in services.msc — including Bluetooth Support Service, Audio Gateway, and User Support — then remove all pairings from Settings. Run netsh winsock reset in an elevated prompt, reboot, and pair each device fresh one at a time."
  - q: "Should I disable power management for Bluetooth?"
    a: "Yes, if Bluetooth dies after sleep. Uncheck 'Allow the computer to turn off this device' on the Bluetooth adapter and its USB hubs in Device Manager, and turn off Fast Startup. This prevents the radio from being suspended into a state it cannot wake from."
---

The Windows 11 24H2 update has a documented habit of breaking Bluetooth: the toggle vanishes from Settings, paired devices refuse to reconnect, or the Bluetooth adapter shows a yellow warning in Device Manager. If your Bluetooth died within days of the 24H2 update, you are looking at a driver compatibility problem, not failing hardware.

24H2 changed enough of the driver framework that older Bluetooth drivers — particularly Intel, Realtek, and MediaTek stacks — can fail to load or pair. The failure modes are consistent enough that the fix sequence below resolves the large majority of cases without a reinstall.

Work in order. Each fix targets one layer of the Bluetooth stack, from the radio switch up to the full driver rebuild.

## Why this happens

- **24H2-incompatible Bluetooth driver:** The pre-update Bluetooth driver fails under 24H2's driver framework, producing Code 10/43 or a missing adapter.
- **Bluetooth Support Service stopped:** The background service that manages pairing and profiles can fail to start after the update.
- **Airplane mode or Fn wireless toggle:** The update can leave the radio in a soft-disabled state that the Settings toggle doesn't reflect.
- **Corrupted pairing database:** Stored pairings from the old driver version conflict with the new stack, causing connect-then-drop loops.
- **Power management disabling the radio:** USB-attached Bluetooth radios get suspended by power management and never wake.
- **Fast Startup caching the broken state:** The hibernated driver state preserves the failure across rebooks until a full shutdown clears it.
- **Third-party Bluetooth stacks:** Old Toshiba, Broadcom, or CSR Bluetooth suites conflict with Windows' native stack after the update.
- **WiFi/Bluetooth combo card driver mismatch:** The WiFi and Bluetooth functions share one card; updating only the WiFi driver can desync the Bluetooth side.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the radio is actually on

Eliminate the trivial causes before touching drivers.

1. Check **Settings → Bluetooth & devices** — is the Bluetooth toggle present? If missing entirely, skip to Fix 3 (driver problem confirmed).
2. Press **Win + A** and ensure **Airplane mode** is off. Try your laptop's wireless Fn key (often **Fn + F2** or a dedicated key).
3. Go to **Settings → Bluetooth & devices → Devices** and confirm Bluetooth is toggled on there too.
4. If the toggle exists but devices won't pair, remove all pairings (**… → Remove device**) and continue.

### Fix 2: Restart the Bluetooth services

A stopped service produces exactly the 'can't connect' symptom with a healthy-looking toggle.

1. Press **Win + R**, type **services.msc**, and find **Bluetooth Audio Gateway Service**, **Bluetooth Support Service**, and **Bluetooth User Support Service**.
2. Set each to **Automatic**, then right-click → **Restart** (or Start if stopped).
3. Also restart the **Device Association Service**, which handles pairing handshakes.
4. Try pairing your device again immediately.

### Fix 3: Reinstall the Bluetooth driver for 24H2

The core fix for post-24H2 Bluetooth death: a driver built for the new framework.

1. Open **Device Manager → Bluetooth**, right-click your adapter (Intel Wireless Bluetooth, Realtek Bluetooth, etc.) → **Uninstall device**, checking **Attempt to remove the driver**.
2. Expand **Universal Serial Bus controllers** and uninstall any **USB** Bluetooth radio entries the same way.
3. Download the latest Bluetooth driver — from your laptop maker's support site, or Intel's driver tool at [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel adapters.
4. Install, reboot, and re-pair your devices from scratch. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for 24H2-specific Bluetooth guidance if issues persist.

### Fix 4: Run the Bluetooth troubleshooter and reset the stack

Windows' own tooling can clear pairing-database corruption.

1. Go to **Settings → System → Troubleshoot → Other troubleshooters → Bluetooth → Run**.
2. In an elevated Command Prompt, reset the network stack (which includes Bluetooth profiles): **netsh winsock reset** then reboot.
3. Remove all Bluetooth devices from **Settings → Bluetooth & devices → Devices** before re-pairing.
4. Pair one device at a time, testing each before adding the next — a single corrupt pairing can poison the queue.

### Fix 5: Disable power management and Fast Startup

For Bluetooth that works after reboot but dies after sleep.

1. In Device Manager → **Bluetooth**, open your adapter → **Power Management** → uncheck **Allow the computer to turn off this device**.
2. Do the same under **Universal Serial Bus controllers** for the USB root hubs feeding the radio.
3. Turn off **Fast Startup** (Control Panel → Power Options → Choose what the power buttons do), then do a full **Shut down**.
4. Power on and verify Bluetooth survives a sleep/wake cycle.

### Fix 6: Remove conflicting Bluetooth software

Legacy stacks fight the native Windows driver after 24H2.

1. Open **Settings → Apps** and uninstall any **Toshiba Bluetooth Stack**, **Broadcom**, **CSR Harmony**, or **BlueSoleil** software.
2. In Device Manager, check for duplicate Bluetooth adapters — uninstall the non-primary one.
3. Reboot and let Windows use its native Bluetooth stack with the fresh driver from Fix 3.
4. If you rely on special profiles (aptX management apps), reinstall only the current version from the manufacturer after the base stack works.

### Fix 7: Update BIOS/chipset and test the hardware

When the driver is correct and services run but the adapter still won't start.

1. Install the latest **chipset** driver and **BIOS** from your laptop manufacturer's support site — 24H2-era BIOS updates often include Bluetooth firmware fixes.
2. In BIOS, confirm the **Wireless**/**Bluetooth** device is enabled.
3. Boot a Linux live USB and test Bluetooth there — working in Linux proves the radio hardware is fine.
4. If the adapter shows Code 45 (not connected) everywhere including Linux, the combo card may have failed; a USB Bluetooth dongle is a cheap workaround.

## Closing

Bluetooth failures after the 24H2 update are a driver-framework story, not a hardware story. The sequence that works: confirm the radio switch, restart the services, then reinstall a 24H2-era driver from the manufacturer — not the one Windows Update carried over. Strip power management off the radio and remove legacy Bluetooth suites, and the stack stays up. Re-pair devices fresh afterward; old pairings from the broken driver version are not worth keeping. If the adapter has vanished from Device Manager entirely, see [Bluetooth disappeared in 24H2](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2/). Our general [Bluetooth repair guide](/articles/bluetooth-not-working-on-windows-11-laptop-fix/) covers the non-update cases.
