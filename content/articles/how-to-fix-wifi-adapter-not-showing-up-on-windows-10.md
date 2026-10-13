---
title: "How to Fix WiFi Adapter Not Showing Up on Windows 10: A Technician's Guide"
slug: "how-to-fix-wifi-adapter-not-showing-up-on-windows-10"
date: "2026-09-15"
categories: ["drivers"]
tags: ["wifi adapter", "windows 10", "network driver", "device manager", "wireless"]
description: "Your WiFi adapter has vanished from Windows 10? Learn why wireless adapters disappear from Device Manager and follow proven technician steps to bring yours back online."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-on-windows-10.webp"
faqs:
  - q: "Why did my WiFi adapter disappear from Device Manager on Windows 10?"
    a: "The most common causes are a corrupted or rolled-back wireless driver after a Windows update, the adapter being disabled in BIOS or by a physical function-key switch, power management turning the device off, or the adapter being hidden because Windows marked it as disconnected. In rarer cases the Wi-Fi card has loosened in its slot or failed entirely, which also removes it from the device list."
  - q: "Can I restore a missing WiFi adapter without reinstalling Windows?"
    a: "Yes, in most cases. Start by showing hidden devices in Device Manager, then scan for hardware changes and reinstall the wireless driver from your laptop maker's support page. Resetting the network stack and the BIOS wireless setting fixes the rest. A full Windows reinstall is almost never needed for a missing adapter, so treat it as a last resort."
  - q: "How do I know if the WiFi adapter problem is hardware or software?"
    a: "If the adapter is missing from Device Manager even with hidden devices shown, but Bluetooth still works, it is usually a software or driver issue, since both often share one card. Try a Linux live USB: if Wi-Fi works there, Windows is at fault. If the card is absent in BIOS and in Linux, the module is likely loose, disconnected, or dead."
  - q: "Will resetting network settings delete my saved WiFi passwords?"
    a: "Yes. A Windows network reset removes all saved wireless profiles, passwords, VPN settings, and custom DNS entries, returning every network adapter to factory defaults. Write down important passwords or export your profiles with netsh before you reset. It is an effective fix, but you will need to reconnect to each network afterward."
---

Nothing is more frustrating than opening your laptop and finding the WiFi icon replaced by a globe, with no wireless networks in sight. When the WiFi adapter itself is missing from Device Manager on Windows 10, the problem runs deeper than a forgotten password or a weak signal — Windows no longer sees the hardware that connects you to the internet.

The good news is that a missing adapter is a well-understood problem with a clear diagnostic path. In most cases the adapter is still physically present and healthy; it has simply been hidden by a driver failure, a disabled setting, or an aggressive power policy. I have fixed this exact issue dozens of times, and the majority of laptops are back online within twenty minutes.

Below you will find the full breakdown: why this happens, how to diagnose it step by step, and the fixes in the order a technician would actually apply them. Work through them sequentially rather than jumping to the drastic options.

## Why this happens

- **Corrupted wireless driver after a Windows update:** Feature and cumulative updates frequently replace working OEM WiFi drivers with generic versions that fail to start, which removes the adapter from the device list.
- **Adapter disabled by a function key or hardware switch:** Many laptops use Fn+F2 or a side switch to toggle wireless radios. Bumping it can disable the card at a level Windows cannot override.
- **Wireless turned off in BIOS/UEFI:** Some firmware has a dedicated WLAN toggle. If it is off, Windows never enumerates the adapter at all.
- **Aggressive power management:** Windows 10 can power down the wireless card to save battery and occasionally fails to wake it, leaving the device in a ghost state.
- **Driver marked as hidden:** When a driver fails repeatedly, Device Manager hides the device instead of showing it with an error, which makes it look like the hardware is gone.
- **Loose or failing WiFi card:** The M.2 or mini-PCIe card can work loose from vibration, or simply die of old age, taking the adapter entry with it.
- **Corrupted network stack:** Damaged Winsock or TCP/IP configuration can cascade into adapter enumeration failures during boot.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and rescan
Open Device Manager (right-click Start and choose it), then click View and select "Show hidden devices." Expand Network adapters and look for your wireless card — it may appear greyed out. Right-click it and choose Uninstall device, ticking the box to delete the driver software if offered. Then click Action and select "Scan for hardware changes." Windows will redetect the card and attempt to install a working driver. If the adapter was merely hidden by a failed driver load, this single step often restores it immediately. Check whether the WiFi icon returns to the taskbar before moving on.

### Fix 2: Check the physical wireless switch and function keys
Look at your laptop's keyboard for a key with a wireless tower or airplane icon, usually on F2, F3, or F12, and press it together with Fn. Some models also have a physical slider on the side or front edge. Watch for an LED indicator changing state. If your machine was recently in airplane mode or the key was pressed accidentally, the radio may be off at the firmware level, which hides the adapter from Windows entirely. Toggle it and rescan for hardware changes in Device Manager. For a deeper look at connectivity symptoms, see our guide on [wifi disappearing from your laptop](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 3: Enable the adapter in BIOS/UEFI
Restart the laptop and enter firmware setup (usually F2, Del, or F12 during boot). Navigate to the Advanced or Devices section and find the WLAN, wireless, or WiFi entry. Make sure it is set to Enabled, then save and exit. While you are there, check that any "Wireless Switch" or radio control options are not forcing the card off. If the adapter was disabled here, Windows will detect it on the next boot and the missing-adapter problem disappears. This step is especially important after a BIOS update, which can reset these toggles to conservative defaults.

### Fix 4: Reinstall the wireless driver from the manufacturer
Generic Windows drivers are a frequent culprit, so install the exact driver your laptop maker provides. On another device, visit your manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — enter your model, and download the wireless driver for Windows 10. Transfer it via USB, then in Device Manager uninstall the existing wireless entry with driver deletion, and run the downloaded installer. OEM drivers include the correct firmware hooks for your specific card. When you are done, consider our walkthrough on [reinstalling your WiFi driver on Windows 10](/articles/how-to-reinstall-wifi-driver-on-windows-10/) to keep it clean.

### Fix 5: Disable power management on the adapter
In Device Manager, right-click your wireless adapter (once visible again, or the hidden entry) and open Properties. Go to the Power Management tab and uncheck "Allow the computer to turn off this device to save power." Then open Control Panel, go to Power Options, click "Change plan settings" for your active plan, then "Change advanced power settings," and expand Wireless Adapter Settings to set Power Saving Mode to Maximum Performance. This stops Windows from parking the card during idle periods, which is a common trigger for the adapter vanishing after sleep or hibernation.

### Fix 6: Reset the network stack with Command Prompt
Open an elevated Command Prompt and run these commands one at a time, pressing Enter after each: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, and `ipconfig /flushdns`. Then restart the laptop. These commands rebuild the Windows networking components that the adapter depends on to enumerate correctly. If corruption in Winsock or the TCP/IP stack was blocking detection, the adapter typically reappears after the reboot. Microsoft documents the full network troubleshooting flow at Windows support if you want to dig deeper.

### Fix 7: Perform a network reset and test the hardware
As a final software step, go to Settings, then Network and Internet, then Status, and click "Network reset." Confirm, restart, and reconnect to your WiFi. If the adapter is still missing, rule out hardware failure: boot from a Linux live USB and check whether wireless works there. If it does, your Windows installation is the problem and a repair install will fix it; if Linux also sees no card, reseat or replace the WiFi module. You can source exact driver packages manually from the Microsoft Update Catalog if the vendor site ever goes down.

## Closing
A missing WiFi adapter on Windows 10 looks alarming but is a software or configuration problem far more often than a dead card. By revealing hidden devices, checking physical and BIOS switches, reinstalling the proper OEM driver, and resetting the network stack, you cover every common cause in the right order — and only the truly stubborn cases ever need new hardware.
