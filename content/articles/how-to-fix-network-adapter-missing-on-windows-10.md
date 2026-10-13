---
title: "Bring Back a Missing Network Adapter on Windows 10"
slug: how-to-fix-network-adapter-missing-on-windows-10
date: 2026-09-08
categories: ["drivers"]
tags: ["network adapter", "wifi missing", "windows 10", "device manager", "troubleshooting"]
description: "Network adapter missing on Windows 10? Restore vanished Wi-Fi and Ethernet adapters with these Device Manager and driver fixes."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-on-windows-10.webp"
faqs:
  - q: "Where did my network adapter go in Device Manager?"
    a: "It may be hidden, disabled, or failed to the point that Windows cannot enumerate it. Enable Show hidden devices in Device Manager first. If it appears greyed out, enable it. If it is absent entirely, the driver is corrupt or the hardware is disabled in the BIOS."
  - q: "Can a Windows 10 update delete my network adapter?"
    a: "Updates do not delete the hardware, but they can install an incompatible driver that fails to start, which makes the adapter vanish from the network UI. Rolling back the driver or installing the manufacturer's version brings it back. Note the driver version that works, so you can recognize a bad update if it happens again."
  - q: "Why is there no Wi-Fi option in Settings at all?"
    a: "Windows hides the entire Wi-Fi section when no wireless adapter is detected. This points to a missing or failed wireless driver, a BIOS-disabled radio, or a hardware switch in the off position. The adapter must reappear in Device Manager before Settings will show Wi-Fi."
  - q: "Does resetting the network bring back a missing adapter?"
    a: "The network reset reinstalls all network adapters and resets their configuration, which fixes corruption that hides them. It is one of the most effective single fixes, though you will need to re-enter Wi-Fi passwords afterward. Export your Wi-Fi profiles beforehand if you have many saved networks to preserve."
---

Opening Device Manager to find your network adapter simply gone is alarming — no Wi-Fi section in Settings, no Ethernet adapter, no way to get online at all. On Windows 10 this usually follows an update, a driver crash, or a power event that left the adapter in a failed state.

A 'missing' adapter is rarely actually gone. The hardware is almost certainly still on the motherboard; Windows has just lost the ability to see it. The device may be hidden, disabled, failed with an error code, or missing its driver entirely. Each state has a specific recovery path, and the trick is identifying which state yours is in before acting.

This guide walks the detection chain from top to bottom: hidden devices, BIOS, driver repair, and the network reset that rebuilds everything. Follow it in order and the adapter comes back in the great majority of cases.

Windows 10's Device Manager has a behavior that confuses people: it hides devices that fail to start, rather than showing them with an error. So 'missing' very often means 'present but failed.' Training yourself to check **View > Show hidden devices** first — before any driver work — will save you real time on every future device disappearance, not just network adapters.

## Why this happens

- **Adapter hidden after a driver failure:** Windows hides devices that fail to start, making a present-but-broken adapter look absent.
- **Incompatible driver installed by Windows Update:** A mismatched driver fails its start routine, and Windows removes the device from the active view.
- **Adapter disabled in Device Manager or BIOS:** A disabled device is invisible to the network UI; a BIOS-disabled radio is invisible to Windows entirely.
- **Corrupted network stack or adapter configuration:** Damaged registry configuration for the adapter can prevent enumeration.
- **Power management killing the device:** Aggressive power settings can leave the adapter in a D3 sleep state it never wakes from.
- **Hardware wireless switch off:** Older laptops with physical Wi-Fi switches hide the adapter when the switch is off.
- **Failed network controller hardware:** The controller chip itself can die, usually after surge damage — the last possibility, not the first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Show hidden devices in Device Manager

The adapter is often present but hidden. This single menu option reveals it in seconds.

1. Open **Device Manager** and click **View > Show hidden devices**.
2. Expand **Network adapters** and look for greyed-out entries.
3. If your adapter appears greyed, right-click it and choose **Enable device**.
4. If it shows a yellow warning, note the error code — it tells you whether this is a driver or hardware problem. Bluetooth adapters vanish through the same mechanism; the [Bluetooth disappearance guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2/) covers that parallel case.

### Fix 2: Run the network reset

The network reset removes and reinstalls every network adapter, clearing the corruption that hides them.

1. Open **Settings > Network & Internet > Status**.
2. Click **Network reset** and confirm.
3. Restart when prompted — Windows reinstalls all adapters during boot.
4. Reconnect to your Wi-Fi network afterward; saved networks are cleared by the reset.

### Fix 3: Reinstall the adapter driver manually

When the driver is the problem, a deliberate reinstall with the manufacturer's driver beats hoping Windows figures it out.

1. In Device Manager, right-click the adapter (or the unknown device) and choose **Uninstall device**, checking **Delete the driver software**.
2. Restart the laptop.
3. Download the Wi-Fi and LAN drivers for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) using another device if needed, and install them.
4. Confirm the adapter appears and connects.

### Fix 4: Check the BIOS and physical wireless switch

Firmware-level or hardware-switch disabling overrides every Windows fix, so rule it out early.

1. Restart and enter the BIOS; confirm the wireless LAN and LAN controllers are **Enabled**.
2. Check the laptop chassis and Fn keys for a physical wireless switch or toggle — ensure it is on.
3. Boot into Windows and recheck Device Manager.
4. If the adapter appears now, the disable was the entire problem.

### Fix 5: Disable power management on the adapter

An adapter stuck in a sleep state can vanish from the active device list until power management stops interfering.

1. In Device Manager, right-click the network adapter and open **Properties**.
2. On the **Power Management** tab, uncheck **Allow the computer to turn off this device to save power**.
3. Restart and verify the adapter stays visible through sleep and wake cycles.
4. This also fixes adapters that disappear specifically after the laptop sleeps.

### Fix 6: Reset the TCP/IP stack and Winsock

Deep configuration corruption can block enumeration. These commands rebuild the stack from scratch.

1. Open an elevated Command Prompt.
2. Run **netsh winsock reset catalog** and **netsh int ipv4 reset reset.log**.
3. Run **netsh int ipv6 reset reset.log** as well for completeness.
4. Restart and check for the adapter. Related guidance for Windows 11 lives in the [Windows 11 missing adapter guide](/articles/how-to-fix-network-adapter-missing-on-windows-11/).

### Fix 7: Test with a USB network adapter

A USB Wi-Fi or Ethernet adapter bypasses the internal controller and proves whether the hardware is dead.

1. Plug in a USB network adapter and let Windows install it.
2. If it works, your internal controller is likely failed or its motherboard connection is bad.
3. Use the USB adapter as a permanent workaround — it is far cheaper than a motherboard repair.
4. If even the USB adapter fails, the Windows network stack needs a repair install.

### Fix 8: Restore to before the adapter vanished

If the adapter disappeared right after an update, System Restore is the fastest way back to a working state.

1. Open **Create a restore point > System Restore** and pick a date before the disappearance.
2. Complete the restore and restart.
3. Verify the adapter is back in Device Manager and connects.
4. Then pause updates and install the manufacturer's driver manually so the bad update does not return.

## Closing

A missing network adapter on Windows 10 is a detection problem, not a disappearance — the hardware is still there in nearly every case. Reveal hidden devices, reset the network stack, reinstall the manufacturer's driver, and check the BIOS. The adapter comes back from one of those steps far more often than it turns out to be dead hardware.
