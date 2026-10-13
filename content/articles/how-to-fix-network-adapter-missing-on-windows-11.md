---
title: "Restore a Vanished Network Adapter on Windows 11"
slug: how-to-fix-network-adapter-missing-on-windows-11
date: 2026-09-18
categories: ["drivers"]
tags: ["network adapter", "wifi missing", "windows 11", "device manager", "troubleshooting"]
description: "Network adapter missing on Windows 11? Bring back disappeared Wi-Fi and Ethernet adapters with these detection and driver repairs."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 hide my network adapter?"
    a: "Windows 11 hides adapters that fail to start, usually because a Windows update installed an incompatible driver. The hardware is still present — enabling Show hidden devices in Device Manager reveals the greyed-out adapter and its error code. An error code 10 or 43 points to drivers, while total absence points to firmware or hardware."
  - q: "Will the network reset delete my files?"
    a: "No. The network reset only removes and reinstalls network adapters and clears saved Wi-Fi networks and VPN profiles. Your files, apps, and settings are untouched — you will just need to re-enter Wi-Fi passwords. The reset also clears VPN profiles, so have those connection details handy before you confirm."
  - q: "Why is there no Wi-Fi toggle in Quick Settings?"
    a: "The Quick Settings Wi-Fi toggle appears only when Windows detects a working wireless adapter. Its absence means the adapter is missing, disabled, or driverless in Device Manager — fix the adapter and the toggle returns automatically. If the toggle is present but Wi-Fi will not turn on, the radio is likely disabled in the BIOS."
  - q: "Can BIOS updates make the network adapter disappear?"
    a: "Rarely, but a BIOS update can reset the onboard LAN or WLAN enable settings to disabled. If the adapter vanished right after a BIOS update, check the firmware settings for wireless and LAN toggles before doing anything in Windows. The toggles are usually under Advanced or Onboard Devices, labeled WLAN, Wireless, or LAN Controller."
---

You open Quick Settings and the Wi-Fi toggle is simply gone. Settings shows no Wi-Fi section, Device Manager shows no network adapter, and the laptop is an island. On Windows 11 this scenario follows updates with frustrating regularity, because the OS aggressively replaces network drivers during feature updates.

Here is the reassuring truth: the adapter hardware has not evaporated. In the great majority of cases Windows has hidden a failed device, disabled it, or lost its driver. The recovery path is a detection chain — reveal hidden devices, check firmware, repair the driver, reset the stack — and each step either fixes it or narrows the search.

This is the Windows 11 edition of the recovery sequence, accounting for 11's reorganized Settings paths and its more aggressive driver replacement behavior.

Windows 11's Quick Settings panel is actually a useful diagnostic here: the Wi-Fi toggle only appears when a working wireless adapter is detected. No toggle means no detected adapter — full stop. That turns the toggle into a quick health indicator you can glance at after each fix, without opening Device Manager. When the toggle reappears, you have won.

## Why this happens

- **Failed adapter hidden by Device Manager:** Windows 11 hides devices that fail to start, making a present adapter look absent.
- **Incompatible driver from Windows Update:** Feature updates install generic network drivers that fail on specific controller hardware.
- **Adapter disabled in Settings or Device Manager:** A disabled adapter vanishes from the network UI entirely.
- **BIOS wireless or LAN toggle off:** Firmware disables are invisible to Windows and survive every software fix.
- **Corrupted adapter registry configuration:** Damaged device configuration blocks enumeration even with a good driver.
- **Fast Startup preserving a failed state:** The hibernation-based shutdown can carry a failed adapter state across reboots.
- **Dead network controller hardware:** The last resort explanation — the controller chip itself has failed.
- **Driver Store corruption:** Windows keeps a central Driver Store, and corruption there makes every reinstall of the network driver fail identically. Clearing it with pnputil or a repair install is the only way out.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices in Device Manager

Windows 11 hides failed adapters by default. One menu click often reveals the whole problem.

1. Open **Device Manager** and click **View > Show hidden devices**.
2. Expand **Network adapters** and look for greyed-out or warning-marked entries.
3. Right-click a greyed adapter and choose **Enable device**; note any error code on failed ones.
4. An error code 10 or 43 points to drivers; a completely absent adapter points to firmware or hardware.

### Fix 2: Perform the network reset

Windows 11's network reset is the highest-yield single fix — it reinstalls every adapter from scratch.

1. Open **Settings > Network & internet > Advanced network settings**.
2. Click **Network reset** and confirm, then restart when prompted.
3. Windows reinstalls all network adapters during boot.
4. Reconnect to Wi-Fi afterward — saved networks are cleared. If the adapter never returns, continue below. If Wi-Fi specifically has vanished rather than all adapters, the [missing Wi-Fi guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) narrows the diagnosis.

### Fix 3: Reinstall the manufacturer's network driver

Windows 11's generic drivers fail on many controllers. The laptop vendor's driver is built for your exact hardware.

1. Identify your exact model and download the Wi-Fi and LAN drivers from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. In Device Manager, uninstall the failed adapter, checking **Delete the driver software**.
3. Install the manufacturer's driver and restart.
4. Confirm the adapter appears and the Wi-Fi toggle returns to Quick Settings.

### Fix 4: Disable Fast Startup

Fast Startup can preserve a failed adapter state across every 'restart', making the problem look permanent.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully — not restart — then power on fresh.
4. Check Device Manager for the adapter after the cold boot.

### Fix 5: Check BIOS toggles for wireless and LAN

Firmware disables beat every Windows fix. Verify the hardware is actually handed to the OS.

1. Restart and enter the BIOS/UEFI setup.
2. Confirm **WLAN**, **Wireless**, and **Onboard LAN** are all **Enabled**.
3. Save and boot into Windows, then recheck Device Manager.
4. This is especially worth checking if the adapter vanished after a BIOS update.

### Fix 6: Reset TCP/IP and Winsock from the terminal

When the stack itself is corrupt, these commands rebuild the layers the adapter depends on.

1. Open **Terminal as administrator**.
2. Run **netsh winsock reset** and **netsh int ip reset**.
3. Follow with **ipconfig /flushdns**.
4. Restart and verify. The Windows 10 variant of this sequence is in the [Windows 10 missing adapter guide](/articles/how-to-fix-network-adapter-missing-on-windows-10/).

### Fix 7: Rule out hardware with a USB adapter

A USB network adapter bypasses the internal controller and delivers a definitive verdict.

1. Plug in a USB Wi-Fi or Ethernet adapter.
2. If it works immediately, the internal controller is dead or its connection has failed.
3. Keep the USB adapter as a permanent fix — it costs little and performs fully.
4. If USB networking also fails, the Windows network stack needs a repair install rather than another driver swap.

### Fix 8: Perform an in-place repair install

When the adapter is missing across every driver and the stack resets have failed, a repair install rebuilds Windows around your files.

1. Download the Windows 11 ISO from Microsoft's official software download page.
2. Mount it, run **setup.exe**, and choose **Keep personal files and apps**.
3. After the repair, install your manufacturer's network driver before letting Windows Update run.
4. This resolves deep OS-level corruption that no driver swap can fix.

## Closing

A vanished adapter on Windows 11 is a detection failure, not a hardware evaporation — reveal hidden devices, reset the network, install the vendor driver, and check the firmware toggles. Windows 11's aggressive driver replacement makes the vendor driver step more important here than on any previous version. Keep a USB network adapter in your kit regardless — it turns any future adapter disappearance from a crisis into a minor inconvenience while you work the real fix.
