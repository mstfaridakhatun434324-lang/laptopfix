---
title: "Best Way to Fix a Wi-Fi Adapter That Won't Show Up on a Laptop"
slug: "best-way-to-fix-wifi-adapter-not-showing-up"
date: "2026-09-10"
categories: ["drivers"]
tags: ["wifi adapter", "device manager", "wireless driver", "windows 11"]
description: "Wi-Fi adapter missing from Device Manager and the network list? This guide walks through the fastest, most reliable fixes — from unhiding the device to reinstalling the correct driver."
thumbnail: "/images/thumbs/best-way-to-fix-wifi-adapter-not-showing-up.webp"
faqs:
  - q: "Why did my Wi-Fi adapter disappear after a Windows update?"
    a: "Windows feature updates often replace your manufacturer's wireless driver with a generic version or leave the driver stack half-updated. The adapter then fails to start and drops out of Device Manager. Reinstalling the correct driver from Intel or your laptop maker, or running a network reset, restores it in most cases."
  - q: "Can a missing Wi-Fi adapter be a hardware problem?"
    a: "Yes, though it is less common than a driver issue. The M.2 wireless card can work loose after a drop or fail from heat and age. If the adapter never appears in Device Manager — not even as an unknown device or when hidden devices are shown — hardware failure becomes the leading suspect."
  - q: "Will a network reset delete my files?"
    a: "No. A network reset only reinstalls network adapters and returns networking settings to defaults. Your documents, apps, and photos are untouched. It does remove saved Wi-Fi passwords, VPN profiles, and custom DNS settings, so keep your Wi-Fi password handy before you run it."
  - q: "Why does my adapter vanish every time the laptop sleeps?"
    a: "This is almost always aggressive power management. Windows puts the wireless card into a deep sleep state that some drivers cannot wake from, so the adapter drops off the bus. Disable the 'allow the computer to turn off this device' option in Device Manager and set wireless power saving to Maximum Performance."
---

When your laptop's Wi-Fi adapter doesn't show up at all — no wireless icon in the taskbar, no Wi-Fi option in Settings, nothing under Network adapters in Device Manager — the problem is almost never your router. It is a driver, firmware, or hardware-enumeration issue: the adapter is hidden, disabled in BIOS, or running a driver Windows cannot load.

This is one of the most common wireless failures on Windows 11 laptops after a feature update — the Intel AX201/AX211, Realtek 8852, and MediaTek MT7921 are the usual suspects, and most cases are fixed in minutes.

If the adapter is listed but you cannot connect, see our guide on [Wi-Fi disappearing with no option in Settings](/articles/wifi-disappeared-windows-11-no-wifi-option/). This article covers the case where the adapter itself is gone entirely.

## Why this happens

- **Driver corruption after a Windows update:** Feature updates frequently replace the manufacturer's wireless driver with a generic one or leave the driver stack half-updated, so the adapter fails to start and drops out of Device Manager.
- **Adapter hidden in Device Manager:** Windows hides devices it does not currently detect, so an installed adapter can look vanished.
- **Wireless disabled in BIOS/UEFI:** Many business laptops from Dell, HP, and Lenovo have a BIOS toggle for the wireless radio. A BIOS update or reset can flip it off.
- **Airplane mode or hardware radio switch stuck on:** Some laptops have a physical Wi-Fi switch or a function key (often Fn+F2) that cuts power to the radio, which can prevent the adapter from enumerating.
- **Aggressive power management:** Windows may turn off the wireless adapter to save power, leaving it in a state where it never reappears after sleep or hibernation.
- **Loose or failing M.2 wireless card:** The Wi-Fi card sits in an M.2 slot under the bottom panel; knocks, heat, or age can loosen or kill it, and no software fix revives dead hardware.
- **Conflicting VPN or virtual adapters:** Third-party VPN clients and virtual-machine network drivers sometimes interfere with the physical adapter's binding, causing it to disappear from the network stack.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Whether the Adapter Is Simply Hidden

Open Device Manager (Windows key + X), click View, and choose Show hidden devices. Expand Network adapters — your wireless card may appear grayed out, meaning Windows knows about it but cannot start it.

If the adapter appears grayed out, right-click it, choose Uninstall device (deleting the driver if offered), and restart. Windows redetects the hardware on boot and reinstalls a working driver. Our guide on [enabling hidden devices in Device Manager](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/) walks through this view in detail.

1. 1. Press Windows key + X and open Device Manager.
2. 2. Click View, then select Show hidden devices.
3. 3. Expand Network adapters and look for a grayed-out wireless entry.
4. 4. Right-click it, choose Uninstall device, and delete the driver if prompted.
5. 5. Restart the laptop and let Windows redetect the adapter.

### Fix 2: Run a Full Network Reset

Windows 11 includes a network reset that reinstalls every network adapter and returns all networking components to their defaults, clearing corrupted configurations and stale driver states in one shot.

Note: a network reset removes saved Wi-Fi passwords and VPN profiles, so have your Wi-Fi password handy. After the reset, the wireless adapter almost always reappears if the underlying driver is intact.

1. 1. Open Settings, then go to Network and internet.
2. 2. Scroll down and select Advanced network settings.
3. 3. Click Network reset, then click Reset now and confirm.
4. 4. Wait for the automatic restart — do not force it.
5. 5. After reboot, check Device Manager for the wireless adapter.

### Fix 3: Reinstall the Wireless Driver From the Manufacturer

The most reliable long-term fix is a clean install of the driver from the chip maker or your laptop maker — use [Intel's driver detection page](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards, or your laptop manufacturer's support site for Realtek and MediaTek cards.

Download the package on another device if needed, copy it over by USB, and choose a clean install if offered — this wipes old driver files instead of layering over them.

1. 1. On a working device, download the latest Wi-Fi driver for your exact laptop model.
2. 2. Copy the installer to the affected laptop via USB drive.
3. 3. Run the installer and choose clean install if offered.
4. 4. Restart when prompted, even if it does not ask.
5. 5. Verify the adapter appears in Device Manager under Network adapters.

### Fix 4: Check BIOS Settings and the Physical Radio Switch

Enter the BIOS/UEFI setup during boot and look for a Wireless, WLAN, or Radio setting — make sure it is enabled, then save and exit. Also check for a physical Wi-Fi switch on the chassis and try the wireless function key (often Fn+F2).

A BIOS update that silently disabled the radio, or an accidentally toggled function key, accounts for a surprising number of vanished adapters.

1. 1. Restart and enter BIOS/UEFI setup with the correct key for your brand.
2. 2. Find the wireless/WLAN/radio option and set it to Enabled.
3. 3. Save changes and exit the BIOS.
4. 4. Check for a physical Wi-Fi switch and the Fn-key wireless toggle.
5. 5. Boot into Windows and confirm the adapter is back.

### Fix 5: Stop Windows From Powering Off the Adapter

In Device Manager, open the wireless adapter's Properties and uncheck 'Allow the computer to turn off this device to save power' on the Power Management tab. Then set wireless adapter power saving to Maximum Performance in your power plan's advanced settings.

This matters most when the adapter disappears after sleep: the power-saving logic puts some cards into a deep state the driver cannot wake from, so the adapter drops off the bus until a full reboot.

1. 1. In Device Manager, right-click the wireless adapter and choose Properties.
2. 2. Open the Power Management tab and uncheck the power-saving option.
3. 3. Open Control Panel, Power Options, and edit your active plan.
4. 4. Set wireless adapter power saving to Maximum Performance.
5. 5. Restart and test sleep/wake cycles to confirm the adapter stays visible.

### Fix 6: Reset the TCP/IP Stack and Winsock

If the adapter is visible in Device Manager but missing from the network list, the network stack itself may be damaged. Open an elevated Command Prompt and run netsh winsock reset and netsh int ip reset to rebuild the sockets catalog and TCP/IP configuration.

This safe operation is documented in Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows). Restart after running both commands.

1. 1. Search for cmd, right-click, and choose Run as administrator.
2. 2. Type netsh winsock reset and press Enter.
3. 3. Type netsh int ip reset and press Enter.
4. 4. Restart the laptop.
5. 5. Check the taskbar — the Wi-Fi icon should return within a minute.

### Fix 7: Reseat or Replace the Wireless Card

If nothing brings the adapter back — not even as an unknown device — the card may have failed or worked loose. Power off, remove the bottom panel, and reseat the M.2 card: unscrew it, pull it out at its angle, reinsert firmly, and screw it back down.

M.2 Wi-Fi cards like the Intel AX201 are inexpensive and user-replaceable on most laptops. For soldered-down cards (common on ultrabooks), a USB Wi-Fi adapter is the practical workaround.

1. 1. Power off completely and unplug the charger.
2. 2. Remove the bottom panel and locate the M.2 wireless card.
3. 3. Unscrew, remove, and firmly reseat the card.
4. 4. Reassemble, boot, and check Device Manager.
5. 5. If still absent, replace the card or use a USB Wi-Fi adapter.

## Closing

A Wi-Fi adapter that will not show up looks like a hardware death, but it is a software problem about eight times out of ten. Work from the hidden-device check through the driver reinstall before opening the chassis.
