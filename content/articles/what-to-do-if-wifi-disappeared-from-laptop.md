---
title: "WiFi Disappeared From Your Laptop? What to Do Next"
slug: what-to-do-if-wifi-disappeared-from-laptop
date: "2026-09-08"
categories: ["drivers"]
tags: ["wifi disappeared", "no wifi option", "wifi icon missing", "wireless gone", "wifi fix"]
description: "WiFi option completely gone from your laptop? Learn what to do when WiFi disappears — from quick toggles to driver repair and BIOS checks."
thumbnail: "/images/thumbs/what-to-do-if-wifi-disappeared-from-laptop.webp"
faqs:
- q: "What is the difference between WiFi disappeared and WiFi adapter missing?"
  a: "WiFi disappeared usually refers to the user-facing side: no WiFi icon in the taskbar, no WiFi section in Settings, no networks listed — while the adapter may still exist in Device Manager. A missing adapter means Device Manager itself shows no wireless hardware. The disappeared variant is more often a settings or service issue; the missing-adapter variant points to drivers or BIOS. This guide covers the disappeared case, where the fix is usually quick."
- q: "Why did the WiFi icon vanish from my taskbar?"
  a: "The icon disappears when Windows has no active wireless adapter to show — because the adapter is disabled, its driver failed, airplane mode is stuck on, or the WLAN AutoConfig service stopped. It can also vanish after updates that reset network settings. The icon is a symptom, not the problem: restoring the underlying adapter or service brings the icon back automatically."
- q: "Can I get WiFi back without reinstalling anything?"
  a: "Often, yes. Toggling airplane mode off, pressing the laptop's wireless Fn-key combination, restarting the WLAN AutoConfig service, and running the network troubleshooter all restore disappeared WiFi without any reinstall. These take a few minutes combined and resolve the majority of cases where the adapter hardware and driver are actually fine."
- q: "Will a network reset bring back disappeared WiFi?"
  a: "It frequently does, because the reset reinstalls all network adapters and rebuilds the network configuration from scratch — clearing whatever corruption hid the WiFi option. The tradeoff is that saved WiFi passwords are deleted, so note them first. Use the reset after the quicker toggle and service checks in this guide have failed."
---

You open Quick Settings and the WiFi tile is gone. Settings shows no WiFi section — just Ethernet and VPN. The taskbar network icon shows a globe or an Ethernet symbol, and no wireless networks exist anywhere on the machine. WiFi has not just disconnected; it has vanished from the interface entirely, as if the laptop forgot it was ever wireless.

This is different from weak signal or wrong passwords — those are connection problems. A disappeared WiFi is a visibility problem: something between the hardware and the Windows shell broke, and the usual suspects are a stuck airplane mode, a stopped WLAN service, a disabled adapter, or a driver Windows can no longer load. The hardware is very often fine.

What follows is the recovery sequence in order of speed: the toggles and services first (minutes), then the driver repairs, then the deeper checks. Most people get WiFi back well before the end.

## Why this happens

- **Airplane mode stuck on**: A latched airplane mode hides all wireless options from Settings and Quick Settings.
- **WLAN AutoConfig service stopped**: This Windows service manages wireless; when it stops, the WiFi UI disappears.
- **Wireless adapter disabled**: Disabled in Device Manager or via Fn key, the adapter takes its UI with it.
- **Corrupted wireless driver**: A driver Windows cannot load removes the adapter from the active device list.
- **Network settings corruption**: Damaged profiles and stack configuration can hide the WiFi section.
- **BIOS wireless toggle off**: Firmware-level disable removes the radio where Windows cannot see it.
- **Failed Windows update**: Interrupted updates leave networking in a half-configured state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle airplane mode and the wireless Fn key

Two switches control wireless visibility, and both must be correct: Windows airplane mode and the laptop's physical/Fn radio toggle. When they disagree or latch, WiFi vanishes from the interface while everything else looks normal. Cycling both forces a clean state — the fastest possible fix.

1. Press Win + A to open Quick Settings and toggle Airplane mode on, wait five seconds, then off.
2. Press your laptop's wireless Fn combination (commonly Fn + F2/F3, antenna icon).
3. Check for a physical wireless switch on the laptop's edge and set it to on.
4. Restart the laptop and reopen Quick Settings.
5. If the WiFi tile reappears, connect to your network — solved.

### Fix 2: Restart the WLAN AutoConfig service

Windows manages all wireless through the WLAN AutoConfig service. If it stops — after updates, crashes, or software conflicts — the entire WiFi interface disappears: no tile, no Settings section, no networks. Restarting the service rebuilds the wireless UI in seconds, and setting it to automatic prevents recurrence.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find "WLAN AutoConfig" in the list.
3. If it is stopped, right-click and choose Start; if running, choose Restart.
4. Double-click it and set "Startup type" to Automatic.
5. Wait thirty seconds, then check Quick Settings for the WiFi tile.

### Fix 3: Check Device Manager for a disabled adapter

If the service is fine but WiFi is still gone, the adapter itself may be disabled. A disabled adapter removes the WiFi UI just as thoroughly as a missing one. Device Manager shows the truth: look under Network adapters for a grayed-out or warning-marked wireless entry and re-enable it.

1. Press Win + X and open Device Manager.
2. Expand "Network adapters" and look for WiFi/wireless entries.
3. If grayed out, right-click and choose "Enable device."
4. If it shows a warning icon, the driver is corrupt — continue to Fix 5.
5. If no wireless adapter appears at all, enable View, "Show hidden devices" and look again.

### Fix 4: Run the network troubleshooter and reset

Windows' built-in troubleshooters can detect and repair several disappeared-WiFi causes automatically — stuck radio states, service problems, and configuration corruption. If the troubleshooter fails, the full network reset (which reinstalls all adapters and wipes network settings) is the stronger version of the same idea. Note your WiFi passwords before resetting.

1. Go to Settings, System, Troubleshoot, Other troubleshooters, and run "Network Adapter."
2. Select WiFi when prompted and apply any recommended fix.
3. If WiFi is still gone, go to Settings, Network and internet, Advanced network settings.
4. Click "Network reset," then "Reset now," and let the PC restart.
5. After reboot, check for the WiFi tile and reconnect with your password.

### Fix 5: Reinstall the wireless driver

When the adapter shows a warning, appears as an [unknown device](/articles/how-to-fix-unknown-device-in-device-manager/), or the UI stays gone after the above steps, the driver is corrupt. A clean reinstall — removing the old driver completely, then installing the manufacturer's package — restores the adapter Windows can actually load. For Intel wireless cards, [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the correct version automatically.

1. In Device Manager, right-click the wireless adapter and choose "Uninstall device."
2. Tick "Attempt to remove the driver for this device" and confirm.
3. Restart the laptop.
4. Install the WiFi driver from your laptop manufacturer's support page for your exact model.
5. Restart once more and verify the WiFi tile and Settings section return.

### Fix 6: Check the BIOS wireless toggle

A firmware-level wireless disable is invisible to Windows — no adapter, no UI, nothing to troubleshoot from inside the OS. BIOS updates sometimes reset this setting, which explains WiFi that vanishes overnight "for no reason." Two minutes in BIOS setup answers the question definitively.

1. Restart and enter BIOS/UEFI setup (F2 or Del during boot).
2. Find the wireless/WLAN setting (under Advanced, Devices, or Security).
3. Set it to Enabled, save, and exit.
4. Boot into Windows and check Quick Settings.
5. If the toggle was already enabled, the fault is software-side — continue to Fix 7.

### Fix 7: System Restore to before WiFi vanished

When every targeted fix fails, the damage is spread across system configuration in ways individual repairs miss. System Restore rolls drivers, services, and settings back to a date when WiFi worked, undoing whatever update or install broke it. Personal files are untouched. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the restore process alongside other recovery options.

1. Search for "Create a restore point" and open System Protection.
2. Click "System Restore" and pick a date before WiFi disappeared.
3. Complete the wizard and let the laptop restart.
4. Check for the WiFi tile after the restore completes.
5. If no restore point exists, a Windows reset keeping your files is the final software option.

If the adapter itself is absent from Device Manager rather than just the UI, the deeper [WiFi adapter not showing up guide](/articles/wifi-adapter-not-showing-up-troubleshooting/) covers that hardware-oriented case. For a full driver replacement walkthrough, see [reinstalling the WiFi driver on Windows 11](/articles/how-to-reinstall-wifi-driver-on-windows-11/).

## Closing

Disappeared WiFi is a visibility problem, not a hardware problem, in the large majority of cases: a stuck airplane mode, a stopped WLAN service, a disabled adapter, or a corrupt driver hiding the interface. Work the toggles and services first, reinstall the driver if needed, and check BIOS before suspecting the card. The WiFi tile comes back as soon as the underlying cause is cleared.
