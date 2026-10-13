---
title: "How to Fix Mobile Hotspot Not Working on a Laptop, Step by Step"
slug: "how-to-fix-hotspot-not-working-on-laptop-step-by-step"
date: "2026-09-16"
categories: ["drivers"]
tags: ["mobile hotspot", "wifi hotspot", "windows 11", "network adapter", "tethering"]
description: "Can't share your laptop's internet via mobile hotspot? Step-by-step fixes for driver issues, hosted network errors, adapter settings, and Windows configuration."
thumbnail: "/images/thumbs/how-to-fix-hotspot-not-working-on-laptop-step-by-step.webp"
faqs:
  - q: "Why does my laptop say 'We can't set up mobile hotspot'?"
    a: "This error usually means the Wi-Fi adapter's driver does not support hosted networks, or the Microsoft Wi-Fi Direct Virtual Adapter is missing or disabled in Device Manager. Updating the wireless driver to the manufacturer's latest version and re-enabling the virtual adapter typically fixes it. Some older adapters genuinely lack hotspot support, which a driver update cannot change."
  - q: "My hotspot turns on but devices can't connect. What's wrong?"
    a: "This is usually a DHCP or firewall issue on the hotspot side: the virtual adapter is not assigning IP addresses, or the Windows Firewall is blocking the hosted network. Resetting the network stack, restarting the WLAN AutoConfig service, and temporarily testing with the firewall off isolates the cause. An outdated wireless driver can also cause this exact symptom."
  - q: "Does my Wi-Fi adapter need to support 5 GHz for hotspot to work?"
    a: "No, but it affects which band the hotspot broadcasts on. If your adapter only supports 2.4 GHz, the hotspot will be 2.4 GHz only, and Windows may refuse to start it if you force 5 GHz in the hotspot settings. Set the network band to 2.4 GHz in the mobile hotspot settings to match older adapters. Most modern Intel, MediaTek, and Realtek laptop adapters support both bands."
  - q: "Can I use mobile hotspot while connected to Wi-Fi?"
    a: "Yes, on most modern adapters. Windows shares the Wi-Fi connection by creating a virtual adapter alongside the real one, so your laptop stays connected while broadcasting. This requires a driver that supports Wi-Fi Direct and hosted networks. If your adapter cannot do both simultaneously, use a USB Wi-Fi dongle for the hotspot side or share an Ethernet or USB-tethered connection instead."
---

Windows' mobile hotspot turns your laptop into a Wi-Fi router for your phone, tablet, or a friend's laptop — until it refuses to turn on, throws a cryptic error, or broadcasts a network nothing can join. Hotspot failures live at the intersection of wireless drivers, virtual adapters, and Windows network services, which is why the fix is rarely just toggling the switch again. Follow these steps in order to find and fix the real cause.

Before you start, confirm your laptop actually has an active internet connection to share — hotspot cannot create internet from nothing. Also note whether your Wi-Fi itself works normally; if it does not, fix that first with our [Wi-Fi troubleshooting guide](/articles/how-to-fix-wifi-disappeared-from-laptop-on-windows-11/) since hotspot depends on the same adapter.

## Why this happens

- **Wireless driver lacks hosted-network support:** Old or generic drivers may not support the Wi-Fi Direct virtual adapter hotspot needs.
- **Microsoft Wi-Fi Direct Virtual Adapter disabled:** This virtual device does the actual broadcasting; if disabled, hotspot cannot start.
- **WLAN AutoConfig service stopped:** The service managing wireless connections must be running for hotspot to function.
- **Corrupted network stack:** Damaged Winsock or TCP/IP configuration breaks the address sharing hotspot relies on.
- **Firewall blocking the hosted network:** Windows Firewall or third-party security software can block hotspot traffic.
- **Wrong network band selected:** Forcing 5 GHz on a 2.4 GHz-only adapter prevents the hotspot from starting.
- **Bluetooth interfering:** On some combo cards, active Bluetooth disrupts the Wi-Fi Direct session.
- **Power management disabling the adapter:** The wireless card being powered down kills the hotspot silently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the basics and toggle correctly

Eliminate the simple configuration mistakes first.

1. Open Settings > Network & internet > Mobile hotspot and confirm "Share my internet connection from" is set to Wi-Fi (or your active connection).
2. Set "Share over" to Wi-Fi and note the network name and password — click Edit to set a strong password.
3. Set the Network band to 2.4 GHz if you are unsure what your adapter supports.
4. Toggle the hotspot off, wait ten seconds, and toggle it on.
5. On your phone, forget the old hotspot network entry and reconnect fresh — stale saved credentials cause silent failures.

### Fix 2: Check hosted-network support

Find out whether your adapter can even do this, so you do not chase a hardware limitation.

1. Open Command Prompt as administrator.
2. Run `netsh wlan show drivers` and look for "Hosted network supported: Yes".
3. If it says No, update the wireless driver from your laptop maker's site — newer drivers sometimes add support.
4. If it still says No after updating, the adapter genuinely lacks the feature; a USB Wi-Fi dongle with hotspot support is the workaround.
5. While you are here, run `netsh wlan show wirelesscapabilities` to confirm Wi-Fi Direct support.

### Fix 3: Re-enable the Wi-Fi Direct Virtual Adapter

This hidden virtual device is the actual hotspot broadcaster.

1. Press Win + X, open Device Manager, and click View > Show hidden devices.
2. Expand Network adapters and look for "Microsoft Wi-Fi Direct Virtual Adapter".
3. If it has a down arrow, right-click and choose Enable device.
4. If it is missing, right-click your physical Wi-Fi adapter and choose "Scan for hardware changes".
5. If it shows a warning icon, uninstall it (without removing drivers) and scan for hardware changes to recreate it.
6. Toggle the mobile hotspot off and on again in Settings.

### Fix 4: Restart the WLAN AutoConfig service

Hotspot depends on this service; when it stalls, hotspot fails silently.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find "WLAN AutoConfig", double-click it, and set Startup type to Automatic.
3. Click Stop, wait five seconds, then click Start.
4. Also restart the "Internet Connection Sharing (ICS)" service the same way.
5. Try enabling the hotspot again immediately after the services restart.

### Fix 5: Reset the network stack

Corrupted network configuration breaks the address translation hotspot needs.

1. Open Command Prompt as administrator.
2. Run these commands in order, pressing Enter after each: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Restart the laptop — the reset only completes on reboot.
4. Reconfigure your hotspot settings (name, password, band) since the reset clears them.
5. Test with one device before reconnecting everything.

### Fix 6: Update the wireless driver

An outdated driver is the most common deep cause of hotspot failures.

1. In Device Manager, note your exact wireless adapter model under Network adapters.
2. Download the latest driver for your laptop model from the manufacturer's support site.
3. Install it, choosing a clean install if offered, then restart.
4. Recheck `netsh wlan show drivers` — hosted network support sometimes appears only with the new driver.
5. Intel users can also use the official [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to get the newest wireless package.
6. The [Windows 11 hotspot guide](/articles/how-to-fix-hotspot-not-working-on-laptop-on-windows-11/) covers the same driver path with Windows 11 screenshots.

### Fix 7: Check firewall and antivirus interference

Security software can block the hosted network without any visible warning.

1. Temporarily disable any third-party antivirus firewall and test the hotspot.
2. If it works, add an exception for the hosted network in that product rather than leaving protection off.
3. For Windows Firewall, open Windows Security > Firewall & network protection and confirm the hotspot network is not being blocked.
4. As a diagnostic step only, you can briefly turn off the firewall for the Private network profile — turn it back on immediately after testing.
5. Microsoft documents hotspot requirements on their [Windows support site](https://support.microsoft.com/en-us/windows) if you need the official checklist.

### Fix 8: Disable power saving on the wireless adapter

Power management can shut the adapter down mid-broadcast.

1. In Device Manager, right-click your Wi-Fi adapter and choose Properties.
2. On the Power Management tab, uncheck "Allow the computer to turn off this device to save power".
3. Go to Control Panel > Power Options > Change advanced power settings.
4. Set Wireless Adapter Settings > Power Saving Mode to Maximum Performance for both battery and plugged in.
5. Restart, enable the hotspot, and leave it running for ten minutes to confirm stability.

## Closing

Mobile hotspot failures almost always come down to the virtual adapter, the wireless driver, or the network stack — the fixes above address each in turn. Once it works, keep your wireless driver current from the manufacturer's site and resist the urge to force the 5 GHz band unless you have confirmed your adapter supports it. A working hotspot is one of the most useful tricks a laptop has; it is worth the fifteen minutes to get it reliable.
