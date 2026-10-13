---
title: "Airplane Mode Stuck On? Reddit-Verified Fixes for Windows Laptops"
slug: how-to-fix-airplane-mode-stuck-on-reddit
date: 2026-09-12
categories: ["drivers"]
tags: ["airplane mode", "stuck on", "wifi disabled", "radio management", "windows 11"]
description: "Airplane mode won't turn off on your Windows laptop? These Reddit-verified fixes cover stuck toggles, broken radio services, and driver resets."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-reddit.webp"
faqs:
  - q: "Why is airplane mode greyed out and stuck on?"
    a: "The toggle greys out when Windows' Radio Management Service cannot communicate with the wireless hardware — usually because the WiFi driver crashed, the service itself is stopped, or a BIOS setting disabled the radio. The UI reflects the service state, not a real airplane mode, so the fix targets the service and driver rather than the toggle."
  - q: "Can a physical switch cause airplane mode to stick?"
    a: "Yes. Some laptops have a physical wireless switch or an Fn key combination that toggles the radio at the hardware level. If that switch is off, Windows shows airplane mode as stuck on and no software toggle can override it. Always check the physical switch and Fn keys before attempting software fixes."
  - q: "Will resetting the network fix stuck airplane mode?"
    a: "Often, yes. A network reset rebuilds the network stack and restarts the radio management components, which clears the stuck state in many cases. You will lose saved WiFi passwords, so have them ready. If the reset does not help, the problem is usually the wireless driver or the Radio Management Service."
  - q: "Is stuck airplane mode a sign of a dead WiFi card?"
    a: "Rarely. Hardware failure usually makes the WiFi adapter disappear from Device Manager entirely rather than sticking airplane mode on. If the adapter is visible in Device Manager with a driver loaded, the hardware is almost certainly fine and the issue is software — service, driver, or BIOS configuration."
---

Airplane mode stuck on is one of the most reported Windows laptop issues on Reddit, and it has a distinctive signature: the toggle in Quick Settings is grayed out or flips itself back, WiFi and Bluetooth are both dead, and rebooting changes nothing. It feels like the laptop is ignoring you, because in a sense it is — the software layer that controls the radio has lost contact with the hardware.

The good news is that the fix is almost always software. The radio management chain — a Windows service, the wireless driver, and a BIOS setting — just needs to be realigned. Work through the fixes below in order and the toggle will start behaving again.

## Why this happens

- **Radio Management Service stopped:** The `RmSvc` service controls the airplane mode state. If it is stopped or crashing, the toggle freezes.
- **Wireless driver crashed:** When the WiFi driver fails, Windows cannot query the radio state and defaults to showing airplane mode as on.
- **Physical wireless switch off:** A hardware switch or Fn key disabled the radio at a level software cannot override.
- **BIOS wireless setting disabled:** Some BIOS setups have a "Wireless" toggle. If it is off, Windows sees no radio at all.
- **Corrupted network stack:** Damaged networking components can leave the radio state machine stuck between on and off.
- **Fast Startup caching a bad state:** Windows' hybrid shutdown can preserve the stuck radio state across reboots.
- **Third-party VPN or network tools:** Some VPN clients and network managers hook the radio state and fail to release it.
- **Windows update driver mismatch:** An update replaced the wireless driver with an incompatible version, breaking radio communication.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical switch and Fn keys

1. Inspect the laptop's sides and front edge for a physical wireless switch and make sure it is in the **On** position.
2. Press the wireless **Fn key combination** (commonly Fn + F2, F3, F5, or F12 — look for the antenna icon).
3. Watch for an on-screen indicator. If the toggle un-greys after this, the hardware switch was the entire problem.
4. Some laptops need the Fn key pressed while in Windows, not in BIOS — try it on the desktop with Quick Settings open so you can see the result.

### Fix 2: Restart the Radio Management Service

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Radio Management Service**. If it is stopped, right-click → **Start**. Set **Startup type** to **Automatic**.
3. If it is already running, right-click → **Restart**.
4. Immediately try the airplane mode toggle in Quick Settings (**Win + A**). This single fix resolves a large share of stuck-toggle reports.

### Fix 3: Disable Fast Startup to clear the cached state

1. Open **Control Panel → Power Options → Choose what the power buttons do**.
2. Click **"Change settings that are currently unavailable"** and uncheck **"Turn on fast startup."**
3. Shut down fully (not restart), wait 10 seconds, and power on.
4. Fast Startup preserves kernel state across shutdowns, which is why plain reboots never fixed your stuck toggle — this is also why the [post-update airplane mode variant](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/) needs the same treatment.

### Fix 4: Reinstall the wireless adapter driver

1. Open **Device Manager → Network adapters**, right-click your wireless adapter → **Uninstall device** (check "delete the driver software" if offered).
2. Restart the laptop and let Windows reinstall the driver.
3. If the problem returns, download the driver from your laptop maker's support page or the [Intel driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) instead of trusting the Windows-provided one.
4. A healthy driver restores communication between Windows and the radio, which un-sticks the toggle.

### Fix 5: Reset the network stack

1. Open **Settings → Network & internet → Advanced network settings → Network reset** → **Reset now**.
2. Alternatively, in an admin Terminal run `netsh winsock reset` and `netsh int ip reset`, then restart.
3. Reconnect to your WiFi afterward — saved networks are wiped by the reset.
4. This rebuilds the state machine that got wedged, and it pairs well with the general [WiFi troubleshooting sequence](/articles/wifi-disappeared-windows-11-no-wifi-option/) when wireless is broadly misbehaving.

### Fix 6: Check the BIOS wireless setting

1. Restart into **BIOS/UEFI** (F2 or Del during boot).
2. Look under **Advanced**, **Devices**, or **Security** for a **Wireless**, **WLAN**, or **Radio** option.
3. Make sure it is **Enabled**. If it was disabled, enable it, save, and boot — the toggle should work immediately.
4. While in BIOS, also check for an "Airplane mode control" or similar option some business laptops expose.

### Fix 7: Remove interfering software and test a clean boot

1. Uninstall VPN clients and third-party network managers temporarily from **Settings → Apps**.
2. Run `msconfig`, choose **Selective startup**, uncheck **Load startup items**, and reboot to test in a clean boot state.
3. If airplane mode works in clean boot, re-enable startup items in halves until you find the culprit.
4. For persistent cases after all of this, an in-place Windows repair install (keeping files) rebuilds the radio stack without wiping your data — documented on the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Reset BIOS to defaults and check for firmware updates

1. Enter **BIOS/UEFI** setup and choose **Load Optimized Defaults** (or Reset to Default), then save and boot.
2. A misconfigured BIOS — especially after updates — can leave radio hardware in states Windows can't manage, and defaults clear that.
3. Check your manufacturer's support page for **BIOS updates** mentioning wireless, radio, or airplane mode fixes, and install if available (on AC power, battery charged).
4. After any BIOS change, boot into Windows and immediately test the toggle before reinstalling anything else — if defaults fixed it, you just saved yourself a driver hunt.

## Closing

Stuck airplane mode is a communication breakdown between Windows and the wireless radio, not a real "mode" at all. Restart the service, clear Fast Startup's cached state, fix the driver, and the toggle comes back to life.
