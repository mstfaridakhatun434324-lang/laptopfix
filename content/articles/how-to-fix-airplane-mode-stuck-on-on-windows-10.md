---
title: "How to Fix Airplane Mode Stuck On in Windows 10"
slug: how-to-fix-airplane-mode-stuck-on-on-windows-10
date: 2026-09-13
categories: ["drivers"]
tags: ["airplane mode stuck", "windows 10", "wifi not working", "radio management", "network fix"]
description: "Airplane mode stuck on in Windows 10 with the toggle greyed out? Seven ordered fixes — from the Radio Management service to BIOS radio settings — get your Wi-Fi back."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-on-windows-10.webp"
faqs:
  - q: "Why is the airplane mode toggle greyed out in Windows 10?"
    a: "The toggle greys out when the Radio Management Service is not running, when a hardware wireless switch is in the off position, or when Windows cannot see a working Wi-Fi adapter. Start the service and set it to Automatic first, then check the physical switch and Fn key. If the Wi-Fi adapter itself shows an error in Device Manager, fix the adapter — the greyed toggle is a symptom, not the disease."
  - q: "Can a Windows update cause airplane mode to get stuck?"
    a: "Yes. Feature updates sometimes fail to migrate the radio management state or install a Wi-Fi driver that reports the radio as unavailable, which wedges the toggle. The standard recovery is the same ordered approach: restart the Radio Management Service, reset the network stack with netsh commands, and reinstall the Wi-Fi driver from the laptop manufacturer's site rather than relying on the Windows Update version."
  - q: "My laptop has no physical wireless switch. What else could lock airplane mode?"
    a: "Many laptops without a visible switch still have an Fn-key radio toggle (often Fn+F2) that behaves identically, and business laptops may expose a 'Wireless Switch' behavior in BIOS. Additionally, some BIOS setups allow disabling WLAN at firmware level, which greys out the Windows toggle permanently. Check both the Fn key and the BIOS wireless settings before concluding it is a Windows problem."
  - q: "Will resetting the network stack delete my files?"
    a: "No. The netsh winsock reset and netsh int ip reset commands only rebuild the networking configuration — TCP/IP stack, Winsock catalog, and DNS cache. Your files, apps, and settings are untouched. You will need to re-enter Wi-Fi passwords and reconfigure any static IP or VPN settings afterward, so note those down before running the reset."
---

Airplane mode stuck on is one of Windows 10's most maddening failures: the toggle is greyed out or flips itself back, Wi-Fi and Bluetooth both die, and the taskbar shows the little airplane no matter what you click. Because airplane mode is a software kill-switch for every radio in the machine, being stuck means Windows believes — rightly or wrongly — that the radios must stay off.

The usual culprits are the Radio Management Service failing to start, a corrupted network stack, a physical wireless switch or Fn-key combination stuck in the off position, or a BIOS setting that disabled the radios at firmware level. Driver problems with the Wi-Fi adapter itself can also present as stuck airplane mode, because Windows hides the toggle when it cannot see a working radio.

Related radio failures often travel together: if Wi-Fi vanished entirely rather than being switched off, our [missing Wi-Fi guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) covers that branch, and [mobile hotspot failures](/articles/how-to-fix-hotspot-not-working-on-laptop-in-windows-11-24h2/) share several of these same fixes. Start below with the service check — it is the most common cause.

## Why this happens

- **Radio Management Service not running** — This service owns the airplane-mode state; when it fails to start, the toggle greys out permanently.
- **Physical wireless switch or Fn key stuck off** — Many laptops have a hardware switch or Fn+F-key radio toggle that overrides software completely.
- **Corrupted network stack / Winsock catalog** — Damaged TCP/IP and Winsock state can wedge the radio management layer.
- **Wi-Fi adapter driver failed or disabled** — With no working Wi-Fi device, Windows 10 may lock airplane mode on and hide individual toggles.
- **BIOS/UEFI wireless setting disabled** — A firmware-level radio disable survives every Windows reinstall and greys out the toggle.
- **Power management cutting the adapter** — Aggressive power saving can leave the radio in a state Windows interprets as intentionally off.
- **Corrupt user profile radio settings** — Rare, but per-user radio state can corrupt such that a new profile works fine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Start the Radio Management Service

This is the fix in the plurality of cases. The service must be running and set to start automatically.

If the service refuses to stay running, check its dependencies: the Radio Management Service relies on the Remote Procedure Call (RPC) service and the Windows Connection Manager. Open each dependency in services.msc and confirm they are running and set to Automatic — a disabled dependency silently prevents the radio service from starting, which is a rarer but real variant of this failure.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find **Radio Management Service**, double-click it.
3. Set Startup type to **Automatic** and click **Start**.
4. If it is already running, right-click and choose **Restart**.
5. Try the airplane mode toggle again — it should now respond.

### Fix 2: Check the physical switch and Fn key

No software fix can override a hardware radio kill switch. Rule this out before deeper surgery.

1. Inspect the laptop's sides and front edge for a physical Wi-Fi/wireless switch and slide it to On.
2. Press the Fn radio key (commonly Fn+F2, Fn+F3, or Fn+F12 — look for the antenna icon) and watch for an on-screen indicator.
3. On some business laptops, the BIOS has a 'Wireless Switch' behavior setting — note it for Fix 6.
4. Retry the Windows airplane mode toggle after each attempt.

### Fix 3: Reset the network stack

A corrupted Winsock/TCP-IP catalog wedges radio management. These commands rebuild it from scratch.

1. Open Command Prompt as administrator (Win + X > Command Prompt (Admin) / Windows PowerShell (Admin)).
2. Run, in order: `netsh winsock reset` then `netsh int ip reset` then `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Restart the PC when prompted.
4. Test airplane mode and Wi-Fi after reboot. Microsoft documents these netsh resets in its [Windows networking support content](https://support.microsoft.com/en-us/windows).

### Fix 4: Re-enable and reinstall the Wi-Fi adapter

A disabled or failed Wi-Fi device makes Windows 10 lock the airplane toggle. Bringing the adapter back often unlocks everything.

1. Open Device Manager > Network adapters.
2. If the Wi-Fi adapter shows a down arrow, right-click > **Enable device**.
3. If it shows a yellow warning, right-click > Uninstall device (do not delete the driver), then Action > Scan for hardware changes.
4. Update the driver from the laptop maker's support site if problems persist.

### Fix 5: Disable power management on the Wi-Fi adapter

Windows 10 powering the adapter down at the wrong moment can wedge the radio state machine.

1. In Device Manager, right-click the Wi-Fi adapter > Properties.
2. Open the Power Management tab and uncheck **Allow the computer to turn off this device to save power**.
3. On the Advanced tab, set **Power Saving Mode** / Roaming Aggressiveness to **Maximum Performance** while testing.
4. Restart and verify the toggle behaves.

### Fix 6: Check BIOS/UEFI wireless settings

A firmware-disabled radio cannot be fixed from Windows. This check takes two minutes.

1. Restart into BIOS/UEFI (Del/F2/F12 during boot).
2. Look for Wireless, WLAN, Bluetooth, or 'Wireless Switch' settings under Advanced or Security.
3. Ensure WLAN and Bluetooth are **Enabled**.
4. Save, exit, and test the toggle in Windows.

### Fix 7: Run the network troubleshooter and test a new profile

When all else fails, the automated troubleshooter plus a fresh user profile isolates the last software variables.

1. Open Settings > Update & Security > Troubleshoot > Additional troubleshooters > **Network Adapter** > Run the troubleshooter.
2. Apply any fix and restart.
3. If still stuck, create a new local user account and test airplane mode there — if it works, your main profile's radio state is corrupt and migrating profiles is the pragmatic fix.

## Closing

A stuck airplane mode toggle in Windows 10 is a radio-management problem, not a Wi-Fi problem: the Radio Management Service, a hardware switch, or a wedged network stack. The service restart in Fix 1 and the hardware-switch check in Fix 2 resolve most cases in minutes; the network reset and BIOS checks catch the stubborn remainder.
