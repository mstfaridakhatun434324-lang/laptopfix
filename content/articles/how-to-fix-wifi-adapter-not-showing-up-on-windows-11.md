---
title: "How to Fix WiFi Adapter Not Showing Up on Windows 11"
slug: "how-to-fix-wifi-adapter-not-showing-up-on-windows-11"
date: "2026-10-01"
categories: ["drivers"]
tags: ["wifi adapter", "windows 11", "network driver", "device manager", "wireless"]
description: "WiFi adapter missing from Device Manager on Windows 11? Learn the Windows 11-specific causes and follow proven steps to restore your wireless connection."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-on-windows-11.webp"
faqs:
  - q: "Why is my WiFi adapter missing after upgrading to Windows 11?"
    a: "Upgrades frequently carry over a Windows 10 wireless driver that cannot initialize properly under Windows 11, so the adapter fails to start and Device Manager hides it. The 24H2 update is particularly aggressive about replacing OEM drivers with generic versions. Installing the Windows 11-specific driver from your laptop maker and blocking further replacements resolves the mismatch permanently."
  - q: "Where is the WiFi adapter supposed to appear in Device Manager?"
    a: "Under the Network adapters section, listed by its chip name such as Intel Wi-Fi 6 AX201, Realtek 8852CE, or MediaTek Wi-Fi 6 MT7921. If the section shows only Bluetooth and Ethernet entries, or the wireless entry is greyed out under hidden devices, the driver is not loading. A healthy adapter appears without any warning icons and with its full model name."
  - q: "Does Windows 11 fast startup affect the WiFi adapter?"
    a: "Yes, notably. Fast startup's hybrid shutdown can skip proper reinitialization of the wireless card, leaving it undetected after what looked like a reboot. Disabling fast startup forces a full hardware initialization on every boot and fixes adapters that vanish intermittently. It is one of the first settings technicians check for flaky wireless hardware detection."
  - q: "Can I use an older Windows 10 driver on Windows 11?"
    a: "Sometimes as a temporary measure, but it is unreliable — Windows 10 drivers may fail to start or cause instability under Windows 11's changed driver framework, especially on 24H2. Always prefer the Windows 11 driver from your laptop manufacturer's support page. If none exists for an older model, the chip maker's generic Windows 11 driver (Intel, Realtek, MediaTek) is the next-best option."
---

Windows 11 changed enough under the hood — driver frameworks, power management, update behavior — that WiFi adapters which were rock-solid on Windows 10 can vanish without a trace. You open quick settings and there's no WiFi toggle; Device Manager's Network adapters section shows everything except wireless. It's the same alarming symptom as on Windows 10, but the Windows 11-specific triggers deserve their own diagnostic path.

The 24H2 update in particular has been rough on wireless drivers, swapping working OEM versions for generic ones that fail to initialize certain cards. The good news: the fix sequence is well established, and it starts with confirming what Windows actually sees before you change anything.

## Why this happens

- **Windows 10 driver carried into Windows 11:** Upgrade-preserved drivers fail under the new driver framework.
- **24H2 replacing OEM drivers:** Automatic driver servicing installs generic wireless drivers that can't start the card.
- **Fast startup skipping initialization:** Hybrid boot leaves the card unenumerated after shutdowns.
- **Adapter disabled in BIOS or by function key:** Firmware-level radio off hides the hardware completely.
- **Corrupted driver stack:** Failed updates leave the wireless driver half-installed and hidden.
- **Power management parking the card:** Modern Standby power policies suspend the adapter and fail to resume it.
- **Hardware failure or loose card:** The physical M.2 card failing or unseating, least common but possible.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Disable fast startup and do a true cold boot
Open Control Panel, Power Options, "Choose what the power buttons do," click "Change settings that are currently unavailable," and uncheck "Turn on fast startup." Shut down completely, unplug the charger, hold the power button for 30 seconds, then boot. Fast startup is a prime suspect on Windows 11 because its hybrid shutdown skips device reinitialization — and a true cold boot forces Windows to rediscover the wireless card from scratch. Check Device Manager after booting.

### Fix 2: Reveal hidden devices and check adapter status
In Device Manager, enable View > "Show hidden devices" and expand Network adapters. A greyed-out wireless entry means the driver is installed but not starting — right-click, uninstall with driver deletion, then Action > "Scan for hardware changes." A missing entry means Windows isn't loading any driver for the card. Note any error codes on warning icons; they direct the next steps. Our detailed [adapter recovery guide](/articles/wifi-adapter-not-showing-up-troubleshooting/) covers error-code interpretation.

### Fix 3: Install the Windows 11 driver from your laptop maker
Download the wireless driver explicitly labeled for Windows 11 and your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). Uninstall the current wireless entry with driver deletion, install the downloaded package, and reboot. Do not accept the Windows 10 driver as a substitute unless no Windows 11 version exists. Immediately set Device Installation Settings to "No" so 24H2's driver servicing doesn't replace your working driver next week. See our [reinstall walkthrough](/articles/how-to-reinstall-wifi-driver-in-windows-11-24h2/) for the clean method.

### Fix 4: Check BIOS wireless settings and the function key
Reboot into firmware setup and verify the WLAN/wireless toggle is Enabled — 24H2-era BIOS updates sometimes reset it. Also press the laptop's wireless function key (Fn + tower icon) in Windows and watch for state changes. These firmware-level controls hide the card from the OS entirely, so no driver work can help until they're on. If the adapter appears in Device Manager right after a BIOS change, you've found it.

### Fix 5: Reset the network stack and run the troubleshooter
In an elevated Command Prompt, run `netsh winsock reset` and `netsh int ip reset`, then restart. Then go to Settings > System > Troubleshoot > Other troubleshooters and run the Network troubleshooter — on Windows 11 it can repair adapter registrations and reset the network profile store. These steps address stack corruption that prevents an otherwise healthy driver from enumerating the card. Microsoft's wireless diagnostics at Windows support add further checks.

### Fix 6: Adjust Modern Standby power behavior
Open Device Manager, find the wireless adapter, and on the Power Management tab uncheck "Allow the computer to turn off this device to save power." In Settings > System > Power & battery, review the power mode — test with Best Performance while diagnosing. Windows 11's Modern Standby aggressively suspends the wireless card, and on some models the resume path is broken, leaving the adapter missing until a full reboot. Disabling the suspension confirms or eliminates this cause.

### Fix 7: Verify hardware with a live USB and consider replacement
Boot a Linux live USB and check for wireless networks. WiFi working in Linux proves Windows is the problem (consider a repair install); absent in Linux too, after BIOS shows no wireless device, points to a failed or unseated card. Reseat the M.2 card if accessible, or use a USB WiFi adapter as an inexpensive permanent workaround. Alternate driver versions are available from the Microsoft Update Catalog if the OEM site lacks a Windows 11 build.

## Closing
On Windows 11, a missing WiFi adapter is usually the OS getting in its own way: fast startup skipping init, 24H2 swapping drivers, or power policies parking the card. Disabling fast startup, installing the proper Windows 11 OEM driver, and blocking driver replacement resolves the overwhelming majority of cases — the hardware is almost always fine. The long-term defense here is update discipline: Windows 11's driver servicing will keep trying to "help" by replacing your wireless driver, so verify the driver version after every feature update and keep the OEM installer within reach. Consider noting the working driver version in a text file — when WiFi breaks six months from now, comparing versions instantly tells you whether an update swapped it. If you travel with the laptop, remember that some captive portals and enterprise networks expose driver quirks that home networks never trigger; a driver that is rock-solid at home can still stumble on 802.1X enterprise WiFi, which is a configuration challenge rather than a broken adapter. Keep fast startup disabled permanently if your model showed any sensitivity to it — the slightly longer boot is a fair trade for hardware that initializes correctly every time. And as with all wireless repairs, a cheap USB WiFi adapter in your bag turns any future adapter crisis into a minor inconvenience.
