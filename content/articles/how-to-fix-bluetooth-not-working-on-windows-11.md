---
title: "Bluetooth Not Working on Windows 11? Fix It"
slug: how-to-fix-bluetooth-not-working-on-windows-11
date: 2026-09-11
categories: ["drivers"]
tags: ["bluetooth not working", "windows 11 bluetooth", "bluetooth missing", "bluetooth driver"]
description: "Bluetooth not working on Windows 11? Fix missing toggles, pairing failures, and driver issues with this complete guide."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-not-working-on-windows-11.webp"
faqs:
  - q: "Why is there no Bluetooth toggle in Windows 11 Settings?"
    a: "A missing Bluetooth toggle means Windows cannot see a working Bluetooth adapter. The adapter is usually disabled, its driver is corrupted, or Windows Update replaced it with a broken version. Check Device Manager for the Bluetooth adapter — if it is missing even with hidden devices shown, the driver needs reinstalling or the hardware is not enumerating."
  - q: "Why won't my device pair even though Bluetooth is on?"
    a: "Pairing failures are usually about the peripheral, not Windows: the device is still paired to a phone, it is not in pairing mode, or it is too far away. Put the device in pairing mode (check its manual for the button hold), remove old pairings from both sides, and try again within a few feet of the laptop."
  - q: "Can airplane mode disable Bluetooth permanently?"
    a: "Airplane mode turns Bluetooth off, but it should restore when you toggle airplane mode off. If Bluetooth stays dead afterward, the Bluetooth Support Service may have hung — restart it in services.msc. A stuck airplane mode is a separate fault with its own fix."
  - q: "Should I update Bluetooth drivers from Windows Update or the maker?"
    a: "From the maker for the fix, then let Windows Update maintain afterward. When Bluetooth is broken, Windows Update is often the cause (it installed the bad driver), so download the Bluetooth driver from the laptop maker or Intel/Realtek/Mediatek directly, install it, and verify before re-enabling automatic driver updates."
---

Bluetooth on Windows 11 fails in three distinct ways: the toggle vanishes entirely, devices refuse to pair, or paired devices connect and then misbehave. Each has different causes, but they share the same foundation — the Bluetooth adapter, its driver, and the Bluetooth Support Service.

This guide covers all three failure modes in one pass. The first fixes restore the adapter itself; the later ones handle pairing and connection quality. Start at the top regardless of your symptom, because a broken adapter underlies many pairing complaints.

## Why this happens

- **Bluetooth adapter disabled or driver corrupted**, often by a Windows update.
- **Bluetooth Support Service stopped**, killing the toggle and pairing.
- **Airplane mode stuck on**, disabling the Bluetooth radio.
- **Peripheral not in pairing mode** or still paired to another device.
- **Stale pairings** with corrupted link keys on the Windows side.
- **2.4GHz Wi-Fi interference** degrading Bluetooth audio and connections.
- **Power management suspending** the Bluetooth adapter.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restore the Bluetooth adapter

Open Device Manager (Win + X) and expand Bluetooth. If the adapter is greyed out, right-click and enable it. If it shows a warning, uninstall it — deleting the driver — and restart so Windows reinstalls it. If Bluetooth is missing entirely, click View > Show hidden devices. A missing adapter needs the driver fix next. The deeper 'vanished from Device Manager' case is covered in [the Bluetooth disappeared guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/).

1. Open Device Manager and expand Bluetooth.
2. Enable the adapter if greyed out.
3. Uninstall it (deleting the driver) if it shows a warning, then restart.
4. Check that the adapter returns cleanly.

### Fix 2: Install the manufacturer's Bluetooth driver

Download the Bluetooth driver from the laptop maker's support page for your exact model — or from Intel for Intel wireless cards, which bundle Bluetooth with Wi-Fi. Install it over the current driver and reboot. On Intel systems, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) handles both Wi-Fi and Bluetooth together, which matters because they share the card.

1. Download the Bluetooth driver from the laptop or card maker.
2. Install it and reboot.
3. Verify the adapter in Device Manager.
4. Check that the Bluetooth toggle returns in Settings.

### Fix 3: Restart the Bluetooth services

Open services.msc and restart 'Bluetooth Support Service', setting its startup type to Automatic. Also restart 'Bluetooth Audio Gateway Service' if audio devices are the problem. A hung support service produces exactly the 'toggle on but nothing works' symptom, and Microsoft documents these services in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open services.msc.
2. Restart Bluetooth Support Service; set it to Automatic.
3. Restart Bluetooth Audio Gateway Service for audio issues.
4. Test the toggle and pairing.

### Fix 4: Remove and re-pair the device properly

Go to Settings > Bluetooth & devices, remove the problematic device, and put the peripheral into pairing mode — usually a long-press on its power or pairing button until an LED blinks. Keep it within a few feet of the laptop during pairing. Also unpair it from your phone first; many peripherals only pair to one host at a time.

1. Remove the device in Settings > Bluetooth & devices.
2. Unpair it from your phone or other hosts.
3. Put the peripheral into pairing mode.
4. Pair it fresh from the laptop, kept close by.

### Fix 5: Fix Bluetooth audio stutter

If paired audio stutters, the cause is usually 2.4GHz congestion or the wrong profile. Move away from busy 2.4GHz Wi-Fi (or switch the laptop to 5GHz), and in the Sound control panel check whether the device offers both 'Stereo' (A2DP) and 'Handsfree' (HFP) — Windows sometimes defaults calls to the low-quality handsfree profile. Disable 'Handsfree Telephony' in the device's Properties > Services tab if you only need music.

1. Move the laptop's Wi-Fi to 5GHz to reduce interference.
2. In Sound settings, choose the Stereo (A2DP) playback device.
3. Disable Handsfree Telephony if you do not take calls on it.
4. Test audio quality.

### Fix 6: Disable power management on the adapter

In Device Manager, open the Bluetooth adapter's Properties > Power Management and untick 'Allow the computer to turn off this device to save power'. Bluetooth that works after boot but dies after sleep is the classic symptom. Retest across a sleep/wake cycle to confirm.

1. Open the adapter's Properties > Power Management.
2. Untick the power-saving option.
3. Reboot and test.
4. Verify it survives sleep/wake.

### Fix 7: Reset the Bluetooth stack

As a last resort, remove all Bluetooth devices, uninstall the Bluetooth adapter (deleting its driver), and restart — Windows rebuilds the entire Bluetooth stack from scratch. Then reinstall the maker's driver and pair devices fresh. If the adapter never reappears, suspect hardware: the Bluetooth module shares the Wi-Fi card on most laptops, so a combined Wi-Fi + Bluetooth failure points at the card.

1. Remove all paired Bluetooth devices.
2. Uninstall the Bluetooth adapter, deleting its driver.
3. Restart and reinstall the maker's driver.
4. Pair devices fresh, one at a time.

### Fix 8: Check for half-installed driver updates

Open Settings > Windows Update > Update history and look for failed driver updates dated around when Bluetooth broke — a half-installed driver leaves the adapter in limbo, present but nonfunctional. Uninstall the failed update, reboot, then install the laptop maker's Bluetooth driver manually. Also verify Settings > Bluetooth & devices > Devices that device discovery is working, and remove any ghost entries for devices you no longer own.

1. Check Update history for failed driver updates.
2. Uninstall the failed update and reboot.
3. Install the maker's Bluetooth driver manually.
4. Remove ghost device entries and pair fresh.

## Closing

Bluetooth failures are adapter problems, service problems, or peripheral problems — and the order matters. Restore the adapter and its driver first, restart the support service, then work the pairing side with the peripheral in proper pairing mode. Keep the laptop maker's Bluetooth driver handy, because Windows Update remains the most common source of the next breakage. If the adapter vanishes from Device Manager entirely rather than just misbehaving, the [disappeared-Bluetooth walkthrough](/articles/best-way-to-fix-bluetooth-disappeared-from-device-manager/) goes deeper.
