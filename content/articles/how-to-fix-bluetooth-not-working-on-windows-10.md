---
title: "Bluetooth Not Working on Windows 10? Fix It"
slug: how-to-fix-bluetooth-not-working-on-windows-10
date: 2026-09-12
categories: ["drivers"]
tags: ["bluetooth not working", "windows 10 bluetooth", "bluetooth pairing failed", "bluetooth driver windows 10"]
description: "Bluetooth not working on Windows 10? Fix missing settings, pairing failures, and driver problems with steps written for Windows 10."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-not-working-on-windows-10.webp"
faqs:
  - q: "Where is Bluetooth in Windows 10 Settings?"
    a: "Go to Settings > Devices > Bluetooth & other devices. The toggle lives at the top of that page. If the entire Bluetooth section is missing, Windows cannot see the adapter — check Device Manager for a disabled or flagged Bluetooth adapter, which is the usual cause."
  - q: "Why does Windows 10 say 'Bluetooth is turned off' with no way to turn it on?"
    a: "That message appears when the adapter is disabled or its driver failed. Open Device Manager, find the Bluetooth adapter, and enable it — or reinstall its driver if it shows a warning. The Action Center quick-action tile also reflects the adapter state, so fixing the adapter restores the tile too."
  - q: "Do I need to reinstall iTunes or other software for Bluetooth?"
    a: "No — Bluetooth pairing is handled by Windows itself, not by media apps. But some phone companion apps install their own Bluetooth stacks that conflict with Windows'. If pairing broke after installing phone software, uninstall the companion app's Bluetooth components and let Windows manage pairing."
  - q: "Why do paired devices keep disconnecting on Windows 10?"
    a: "Random disconnects usually mean power management is suspending the adapter, the device is at range limit, or 2.4GHz Wi-Fi interference is breaking the link. Disable the adapter's power-saving option in Device Manager, keep the device close, and move the laptop's Wi-Fi to 5GHz."
---

Windows 10's Bluetooth stack is mature but brittle: years of updates have left many machines with mismatched drivers, and the Settings layout differs just enough from Windows 11 that Win11 guides send you clicking in the wrong places. This guide is written specifically for Windows 10's menus and its particular failure modes.

The structure mirrors the way Bluetooth actually breaks on Windows 10 — adapter first, then the support service, then pairing, then the connection-quality issues. Every step names the Windows 10 location, not the Windows 11 one.

## Why this happens

- **Bluetooth adapter disabled or driver broken** after a Windows 10 update.
- **Bluetooth Support Service not running**, a classic Windows 10 failure.
- **Action Center tile out of sync** with the real adapter state.
- **Stale device pairings** with corrupted link keys.
- **Peripheral paired to another host** or not in pairing mode.
- **Power management suspending the adapter** during idle or sleep.
- **Interference on 2.4GHz** from Wi-Fi crowding the Bluetooth band.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable the adapter in Device Manager

Press Win + X and open Device Manager. Expand Bluetooth — if the adapter is greyed out, right-click and enable it. If it carries a yellow warning, uninstall it (deleting the driver) and restart. Windows 10 reinstalls the driver on boot. Check the Action Center (Win + A) afterward: the Bluetooth tile should now reflect the real state.

1. Open Device Manager via Win + X.
2. Enable the Bluetooth adapter if greyed out.
3. Uninstall it (deleting the driver) if flagged, then restart.
4. Check the Action Center Bluetooth tile.

### Fix 2: Install the Windows 10 driver from the maker

Download the Bluetooth driver from the laptop maker's support page, choosing the Windows 10 version explicitly — Windows 11 drivers sometimes install but misbehave on 10. For Intel wireless cards, Bluetooth rides with the Wi-Fi driver package. Install, reboot, and confirm the adapter is clean in Device Manager before testing pairing.

1. Download the Windows 10 Bluetooth driver from the laptop maker.
2. Install it and reboot.
3. Verify a clean adapter entry in Device Manager.
4. Open Settings > Devices > Bluetooth & other devices to confirm the toggle.

### Fix 3: Start the Bluetooth Support Service

Press Win + R, type services.msc, and find Bluetooth Support Service. If it is stopped, start it; set Startup type to Automatic so it survives reboots. This service is the backend for pairing and the Settings toggle — on Windows 10 it stops more often than it should, especially after feature updates. Microsoft documents it in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open services.msc.
2. Start Bluetooth Support Service.
3. Set its Startup type to Automatic.
4. Retry the Bluetooth toggle in Settings.

### Fix 4: Re-pair devices cleanly

In Settings > Devices > Bluetooth & other devices, remove the failing device. Put the peripheral in pairing mode (long-press its button until the LED blinks — check its manual), and make sure it is unpaired from your phone, since most peripherals bond to one host. Click 'Add Bluetooth or other device' > Bluetooth and pair fresh, keeping the devices close together.

1. Remove the device in Bluetooth settings.
2. Unpair it from other hosts like your phone.
3. Put the peripheral into pairing mode.
4. Add it fresh via 'Add Bluetooth or other device'.

### Fix 5: Stop the random disconnects

In Device Manager, open the Bluetooth adapter's Properties > Power Management and untick 'Allow the computer to turn off this device to save power'. Then reduce 2.4GHz congestion: connect the laptop's Wi-Fi to 5GHz instead, and keep the Bluetooth device within a few meters with a clear line of sight. The [Windows 11 Bluetooth guide](/articles/how-to-fix-bluetooth-not-working-on-windows-11/) covers the same interference physics if you run both OS versions.

1. Disable adapter power management in Device Manager.
2. Move laptop Wi-Fi to the 5GHz band.
3. Keep the Bluetooth device close and unobstructed.
4. Monitor for disconnects over a day of use.

### Fix 6: Run the Bluetooth troubleshooter

Windows 10 still ships the classic troubleshooters: Settings > Update & Security > Troubleshoot > Additional troubleshooters > Bluetooth. Run it — it checks the service, the adapter state, and the radio, and fixes what it can. It is not thorough, but it catches the simple misconfigurations quickly.

1. Open Settings > Update & Security > Troubleshoot.
2. Run the Bluetooth troubleshooter.
3. Apply its recommended fixes.
4. Retest pairing.

### Fix 7: Rebuild the Bluetooth stack

Remove every paired device, uninstall the Bluetooth adapter in Device Manager (deleting the driver), and restart. Windows rebuilds the stack cleanly on boot. Reinstall the maker's Windows 10 driver, then pair devices one at a time, testing each before adding the next. If the adapter never returns, the wireless card (which hosts Bluetooth) may have failed.

1. Remove all paired devices.
2. Uninstall the Bluetooth adapter, deleting its driver.
3. Restart and reinstall the maker's driver.
4. Pair devices fresh, one at a time.

### Fix 8: Update the chipset driver and check the BIOS

Bluetooth lives on the wireless card, which depends on the chipset — an outdated chipset driver produces exactly the flaky-Bluetooth-after-update pattern. Install the latest chipset driver from the laptop maker's support page for your Windows 10 model. Also check the BIOS for a Bluetooth or wireless enable toggle: on some business laptops Bluetooth can be disabled independently of Wi-Fi in firmware, and no Windows setting overrides a firmware-disabled radio.

1. Install the latest chipset driver from the laptop maker.
2. Reboot and test Bluetooth stability.
3. Check the BIOS for a Bluetooth/wireless enable option.
4. Enable it in firmware if present, then retest in Windows.

## Closing

Windows 10 Bluetooth is fixable in the same order every time: adapter, driver, support service, then pairing hygiene. The Device Manager enable and the service restart resolve the 'no toggle' cases; clean re-pairing handles the rest. Note the Windows 10 driver explicitly when downloading — the Windows 11 package is not an acceptable substitute, and mixing them is a quiet source of recurring breakage. For the Device Manager disappearance variant on Windows 10, see [Bluetooth missing from Device Manager](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-10/).
