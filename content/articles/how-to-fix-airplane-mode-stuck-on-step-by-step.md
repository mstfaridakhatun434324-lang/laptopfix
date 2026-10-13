---
title: "Airplane Mode Stuck On? Fix It Step by Step"
slug: how-to-fix-airplane-mode-stuck-on-step-by-step
date: 2026-10-06
categories: ["drivers"]
tags: ["airplane mode stuck", "airplane mode won't turn off", "windows 11 airplane mode", "radio management service"]
description: "Airplane mode stuck on and won't turn off in Windows 11? Fix the toggle with service restarts, driver fixes, and registry checks."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-step-by-step.webp"
faqs:
  - q: "Why won't airplane mode turn off in Windows 11?"
    a: "The usual causes are a stuck Radio Management Service, a corrupted wireless driver that cannot report the radio state, or a physical wireless switch holding the radio off. Less commonly, a registry value or group policy locks the toggle. The service restart and driver reinstall below fix the software causes in most cases."
  - q: "Can a physical switch keep airplane mode on?"
    a: "Yes. Many business laptops have a side switch or an Fn key that controls the wireless radio at the hardware level. If that switch is off, Windows shows airplane mode as on and no software toggle can override it. Always check the physical switch before assuming a Windows problem."
  - q: "Is it safe to edit the registry to fix airplane mode?"
    a: "The specific RadioEnable value edit is safe if you back up the key first, but it is a last resort. Try the service restart, the network reset, and the driver reinstall before touching the registry. A wrong edit elsewhere in the registry can cause bigger problems than a stuck toggle."
  - q: "Why does airplane mode turn itself back on after reboot?"
    a: "That usually means a startup program, a driver, or Fast Startup is restoring the stuck state on every boot. Disabling Fast Startup and checking startup apps for wireless utilities (especially vendor connection managers) breaks the cycle. A clean driver reinstall also stops drivers from reasserting the bad state."
---

Airplane mode is supposed to be a simple toggle. But when it gets stuck on — greyed out, instantly re-enabling, or refusing to switch off — it takes your Wi-Fi and Bluetooth down with it, and the usual click-the-toggle advice goes nowhere. This is a surprisingly common Windows 11 fault, and it has a clear set of causes.

The toggle is controlled by the Radio Management Service talking to your wireless drivers. When the service hangs, the driver misreports the radio state, or a physical switch overrides everything, the toggle locks up. The fixes below attack each layer in order: the switch, the service, the drivers, and finally the registry.

## Why this happens

- **Radio Management Service stuck or stopped**, leaving the toggle with no backend to talk to.
- **Corrupted Wi-Fi or Bluetooth driver** misreporting the radio state to Windows.
- **Physical wireless switch or Fn key** holding the radio off at the hardware level.
- **Fast Startup restoring the stuck state** on every boot, making the problem survive restarts.
- **Registry value forcing the radio off** — the RadioEnable key stuck at 0.
- **Third-party wireless utility or VPN** fighting Windows for control of the radio.
- **BIOS wireless setting disabled**, which Windows reads as a permanently-off radio.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical wireless switch

Look along the sides and front edge of the laptop for a small wireless switch — Lenovo ThinkPads and many Dell Latitudes have one. Also try the Fn + wireless key (often F2 or a radio-tower icon). If the switch is off, Windows cannot override it, and every software fix below will fail until the switch is on.

1. Inspect all edges of the laptop for a physical wireless switch.
2. Slide it to the on position if present.
3. Press Fn + the wireless function key once.
4. Check Quick Settings to see if airplane mode now toggles.

### Fix 2: Restart the Radio Management Service

The Radio Management Service is the backend behind the airplane mode toggle. Restarting it unsticks the toggle in a large share of cases. Set it to automatic startup while you are there so it cannot end up stopped again after updates.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find Radio Management Service in the list.
3. Right-click it, choose Restart, then open Properties and set Startup type to Automatic.
4. Try the airplane mode toggle again.

### Fix 3: Reinstall the Wi-Fi and Bluetooth drivers

A corrupted wireless driver feeds Windows a permanent 'radio off' signal. Reinstall both the Wi-Fi and Bluetooth adapters in Device Manager, deleting the driver software so clean copies install on reboot. Download fresh drivers from the laptop maker first so you are not dependent on Windows Update finding them. If the underlying issue is the [Wi-Fi adapter itself misbehaving](/articles/wifi-disappeared-windows-11-no-wifi-option/), that guide covers deeper adapter diagnostics.

1. In Device Manager, uninstall the Wi-Fi adapter, deleting its driver.
2. Uninstall the Bluetooth adapter the same way.
3. Restart — Windows reinstalls both adapters.
4. Install the manufacturer's latest drivers over the top and retest the toggle.

### Fix 4: Run the network reset

The built-in network reset reinstalls every network adapter and resets the radio state along with everything else. It is worth doing here because a stuck airplane mode often comes bundled with corrupted adapter states. Microsoft documents the reset in the [Windows support hub](https://support.microsoft.com/en-us/windows). Have your Wi-Fi passwords ready — they get forgotten.

1. Open Settings > Network & internet > Advanced network settings.
2. Click Network reset > Reset now and confirm.
3. Restart when prompted.
4. Test the airplane mode toggle after reboot.

### Fix 5: Disable Fast Startup

Fast Startup preserves device and service states across shutdowns, which is exactly how a stuck radio state survives every reboot. Turning it off forces a genuine cold boot. If airplane mode works after a restart but breaks again after a shutdown, Fast Startup is your culprit.

1. Open Power Options > Choose what the power buttons do.
2. Click 'Change settings that are currently unavailable'.
3. Untick 'Turn on fast startup' and save.
4. Shut down fully, boot, and test the toggle.

### Fix 6: Fix the RadioEnable registry value

When everything else fails, the registry may be forcing the radio off. Back up the key first, then check the RadioEnable value. This is a targeted, low-risk edit — but only touch this specific value.

1. Press Win + R, type `regedit`, and press Enter.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\RmSvc`.
3. Double-click RadioEnable (create it as a DWORD if missing) and set it to 1.
4. Restart and test the airplane mode toggle.

### Fix 7: Check the BIOS and test for driver conflicts

Enter the BIOS and confirm wireless is enabled — a disabled radio in firmware shows up as permanent airplane mode. Back in Windows, check startup apps for vendor wireless utilities or VPN clients that manage the radio, and disable them temporarily. If the toggle works in Safe Mode with Networking but not normally, a third-party program is the cause.

1. Reboot into the BIOS and verify wireless is enabled.
2. In Windows, disable third-party wireless utilities and VPNs from startup.
3. Boot into Safe Mode with Networking and test the toggle.
4. Uninstall the conflicting program if Safe Mode works.

## Closing

A stuck airplane mode toggle is almost always the Radio Management Service, a corrupted wireless driver, or a physical switch — the three checks at the top of this guide. The registry edit and BIOS check are there for the stubborn cases, but most people never need them. Once the toggle moves freely again, keep Fast Startup off if it was part of the problem, since it is the most common reason the fault comes back. A stuck radio also kills Bluetooth — if Bluetooth stays dead after the toggle frees up, see [the Bluetooth disappeared checklist](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/). And if the toggle works but flips itself back on after every reboot, check Task Scheduler and startup apps for vendor wireless utilities reasserting the state — disabling them from startup breaks the loop without affecting normal wireless use.
