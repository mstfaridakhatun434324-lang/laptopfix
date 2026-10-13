---
title: "How to Fix WiFi Driver Code 10 Error on Windows 10"
slug: how-to-fix-wifi-driver-code-10-error-on-windows-10
date: 2026-09-14
categories: ["drivers"]
tags: ["wifi driver", "code 10", "windows 10", "network adapter"]
description: "Code 10 on your WiFi adapter in Windows 10? These 7 fixes repair the 'device cannot start' error — driver reinstalls, power settings, and update rollbacks."
thumbnail: "/images/thumbs/how-to-fix-wifi-driver-code-10-error-on-windows-10.webp"
faqs:
  - q: "What causes Code 10 on a WiFi adapter in Windows 10?"
    a: "Code 10 means the WiFi driver failed during device initialization. On Windows 10 the typical triggers are a Windows Update that replaced a working driver with an incompatible one, corrupt driver files from a partial update, aggressive power management preventing the card from starting, or a driver version mismatched to the card revision. The hardware is usually healthy — the driver simply can't complete its startup sequence, and reinstalling or rolling back the driver resolves it."
  - q: "How do I reinstall the WiFi driver on Windows 10 without internet?"
    a: "Download the driver on another device from your laptop manufacturer's support site, copy it to a USB flash drive, and run the installer on the offline laptop. Alternatively, USB-tether your phone: connect via USB, enable USB tethering on the phone, and the laptop gets internet through the phone connection — then download the driver directly. Windows 10 includes generic drivers that usually restore basic connectivity after an uninstall-and-restart."
  - q: "Should I let Windows 10 update my WiFi driver automatically?"
    a: "For WiFi adapters, manual control is safer. Windows 10's automatic driver updates have a history of pushing problematic WiFi drivers, particularly for Intel cards. Once you have a working driver, pause updates or use the Show or hide updates troubleshooter to block driver updates while allowing security updates. Check the manufacturer's site yourself every few months instead of relying on Windows Update."
  - q: "Does Code 10 affect Ethernet too, or just WiFi?"
    a: "Code 10 can hit any device, but WiFi adapters are the most common victims because their drivers update frequently and interact with power management. If both WiFi and Ethernet show Code 10 simultaneously, suspect a system-wide cause: a corrupt driver store, a bad Windows update, or failing system files — run sfc /scannow and check recent updates. For Intel-specific card issues, see the [Intel WiFi troubleshooting guide](/articles/how-do-i-fix-intel-wifi-6-ax201-not-working/)."
---

Windows 10's Device Manager shows your wireless adapter with the dreaded yellow triangle: "This device cannot start. (Code 10)." No WiFi networks, no taskbar icon, no internet — and the error gives you almost nothing to work with. It looks serious, but Code 10 on a WiFi adapter is a driver initialization failure, and it's very fixable.

Windows 10 is particularly prone to this because of its aggressive automatic driver updates. The repair sequence below is tuned for Windows 10's Device Manager, update system, and power management. Start at Fix 1.

## Why this happens

- **Windows Update replaced a working driver:** The most common Windows 10 trigger — a pushed driver with an init bug.
- **Corrupt driver installation:** Interrupted updates leave the driver half-installed and unable to start.
- **Power management blocking initialization:** Windows 10's power plans can starve the card during startup.
- **Driver/card revision mismatch:** Similar card models (Intel 9560 vs AX200, for example) need exact driver matches.
- **Fast Startup replaying a failed state:** The hibernation-based shutdown caches the failed initialization.
- **Third-party driver updaters:** These tools install wrong or beta WiFi drivers that fail to start.
- **Antenna or card seating issues:** On laptops with accessible M.2 cards, a loose card or antenna causes init failures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Uninstall the adapter with driver removal, then restart

This is the canonical Code 10 repair on Windows 10.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Network adapters**, right-click the WiFi adapter, and choose **Uninstall device**.
3. Check the box **Delete the driver software for this device** and click **Uninstall**.
4. Click **Action > Scan for hardware changes** — or restart the laptop for a full rebuild.
5. Check whether the adapter now starts without the warning.

Windows 10 will install its inbox driver after the restart. If Code 10 clears, the old driver files were corrupt. If it returns, Windows' chosen driver is the problem — keep going.

### Fix 2: Install the manufacturer's driver (offline if needed)

No internet on the laptop is no obstacle with a USB drive or phone tethering.

1. On another device, visit your laptop maker's support site and download the WiFi driver for your exact model.
2. Copy it to a USB flash drive, or USB-tether your phone (**Settings > Network > Hotspot > USB tethering** on Android) to get the laptop online temporarily.
3. Run the manufacturer's installer on the laptop.
4. Restart and verify the adapter starts cleanly.

Manufacturer drivers are validated against your BIOS and card revision — they succeed where generic drivers fail. The detailed offline method is in the [WiFi driver reinstall guide](/articles/best-way-to-reinstall-wifi-driver/).

### Fix 3: Roll back to the previous driver

If WiFi died right after a Windows 10 update, the old driver was fine — restore it.

1. In Device Manager, right-click the WiFi adapter, choose **Properties**, and open the **Driver** tab.
2. Click **Roll Back Driver**, select a reason, and confirm.
3. Restart the laptop.
4. Open **Settings > Update & Security > Windows Update > Advanced options** and **Pause updates** for 7–35 days.
5. Download Microsoft's **Show or hide updates** troubleshooter to hide the bad driver update permanently.

This is the highest-success fix for update-triggered Code 10. Don't skip the pause — Windows 10 will cheerfully reinstall the broken driver overnight.

### Fix 4: Disable power saving on the adapter

Windows 10 power plans are aggressive about WiFi power, and it can block initialization.

1. In Device Manager, right-click the WiFi adapter > **Properties > Power Management** tab.
2. Untick **Allow the computer to turn off this device to save power**.
3. Open the **Advanced** tab; set **Power Saving Mode** to **Maximum Performance** and disable any **Selective Suspend** or **USB selective suspend** entries.
4. Go to **Control Panel > Power Options**, select **High performance** (click **Show additional plans** if hidden), then **Change plan settings > Change advanced power settings > Wireless Adapter Settings > Power Saving Mode > Maximum Performance**.
5. Restart.

Test on both AC and battery — if Code 10 only strikes on battery, power management is confirmed as the cause.

### Fix 5: Disable Fast Startup and reset network components

Windows 10's Fast Startup is a frequent accomplice in persistent Code 10.

1. **Control Panel > Power Options > Choose what the power buttons do** > **Change settings that are currently unavailable** > untick **Turn on fast startup**.
2. Open Command Prompt as administrator:
   `netsh winsock reset`
   `netsh int ip reset`
3. **Shut down** (not restart), wait 30 seconds, power on.
4. Verify the adapter in Device Manager.

The full shutdown forces genuine hardware re-initialization instead of replaying the cached failed state. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents these network reset commands alongside the GUI steps above.

### Fix 6: Remove third-party driver updaters and clean the driver store

Driver updater utilities are a notorious source of mismatched WiFi drivers on Windows 10.

1. Uninstall any driver updater software (**Settings > Apps**) — Driver Booster, Driver Easy, Snappy Driver Installer, and similar.
2. In Device Manager, **View > Show hidden devices**, and uninstall all greyed-out network adapter entries.
3. Open Command Prompt as administrator: `pnputil /enum-drivers` to list third-party drivers, and remove WiFi-related stale packages with `pnputil /delete-driver oemXX.inf /uninstall`.
4. Restart and install only the manufacturer's driver.

After this, let Windows manage drivers or update manually — never both through a third-party tool.

### Fix 7: Check the physical card and test in another OS

When software is exhausted, verify the hardware.

1. If your laptop has a service panel, power off, remove the battery if possible, open the panel, and reseat the M.2 WiFi card — remove it, reinsert firmly, and reconnect both antenna wires (black and white/grey, labeled 1 and 2).
2. Boot a Linux live USB and test WiFi there — working WiFi in Linux proves the card is fine.
3. If Linux also fails, the card is likely faulty; replacement M.2 cards cost $20–30 and take ten minutes to swap.
4. As an immediate workaround, a USB WiFi adapter restores connectivity for a few dollars.

Antenna wires are fragile — reconnect them gently, matching the numbered labels. If reseating feels out of your depth, a repair shop does it cheaply. For cards using newer standards, the [WiFi 6 troubleshooting guide](/articles/best-way-to-fix-wifi-6-not-working-on-laptop/) covers AX-specific quirks.

## Closing

On Windows 10, WiFi Code 10 is usually Windows Update's doing — a pushed driver that can't initialize your specific card. The fix ladder (uninstall with driver deletion, manufacturer driver, rollback with update blocking) addresses exactly that pattern. Once a known-good driver is in place and automatic driver updates are tamed, Code 10 stays gone.
