---
title: "How to Fix a Wi-Fi Adapter Not Showing Up in Windows"
slug: "how-to-fix-wifi-adapter-not-showing-up"
date: "2026-10-01"
categories: ["drivers"]
tags: ["wifi adapter", "not showing", "device manager", "windows 11", "network"]
description: "Wi-Fi adapter missing from Windows entirely? Bring it back with BIOS checks, driver reinstalls, and network resets in this ordered guide."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up.webp"
faqs:
  - q: "Why is my Wi-Fi adapter not showing in Device Manager?"
    a: "The adapter may be disabled in the BIOS, hidden as an unknown device, or physically disconnected. First check the BIOS for a wireless or WLAN enable option. In Device Manager, choose View and then Show hidden devices. If it appears greyed out, the driver is missing or the device is disabled."
  - q: "Can airplane mode hide the Wi-Fi adapter?"
    a: "Airplane mode disables the radio but should not remove the adapter from Device Manager. However, a stuck airplane mode combined with a driver problem can make the adapter seem absent. Fix the airplane mode issue first, then rescan for hardware changes in Device Manager."
  - q: "How do I rescan for a missing Wi-Fi adapter?"
    a: "Open Device Manager, click Action, then Scan for hardware changes. This forces Windows to redetect hardware on the buses. If the adapter appears with a warning, reinstall its driver. If nothing appears, check the BIOS setting and consider a network reset."
  - q: "Could my Wi-Fi card be dead if it is not showing up?"
    a: "It is possible. If the adapter is absent from both the BIOS device list and Device Manager after a BIOS reset, and reseating does not help on models with accessible cards, the card has likely failed. USB Wi-Fi adapters are a cheap way to confirm the rest of the system is healthy."
---

There is no Wi-Fi icon, no networks list, and no wireless adapter in Device Manager. It is as if the laptop never had Wi-Fi at all. This is different from a broken connection: the hardware itself has vanished from Windows' view.

A missing adapter means Windows cannot see the hardware, which points to the BIOS, the driver, or the physical card rather than your router or settings. The diagnostic question is simple: does the BIOS see it? Everything flows from that answer. Our [24H2-specific adapter guide](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) covers the update-triggered variant.

Follow these fixes in order, from the BIOS check that answers the big question to the resets that bring the adapter back.

## Why this happens

- **Wireless disabled in the BIOS:** Business laptops and BIOS resets can turn the WLAN device off at the hardware level.
- **Missing or corrupted driver:** Without a driver, the adapter may appear as an unknown device or not at all.
- **The adapter is hidden:** Device Manager hides disconnected devices unless you ask to see them.
- **Airplane mode stuck on:** A stuck radio kill can combine with driver issues to hide the adapter.
- **Failed Windows update:** Major updates can lose the driver binding for the wireless card.
- **Loose M.2 wireless card:** On serviceable laptops, the card can creep out of its slot over time.
- **Dead wireless card:** Electronics fail; Wi-Fi cards are no exception.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the BIOS for the wireless adapter

This is the decisive test. The BIOS enumerates hardware independently of Windows, so its answer tells you whether to chase software or hardware.

1. Restart and enter the BIOS setup.
2. Look for Wireless, WLAN, or Network settings, often under Advanced or Security.
3. Make sure the wireless device is enabled, not disabled.
4. Save and exit, then boot Windows.
5. Open Device Manager and check whether the adapter now appears.

### Fix 2: Show hidden devices and scan for hardware changes

Windows may know about the adapter but be hiding it. Revealing hidden devices and forcing a rescan brings it into view.

1. Open Device Manager.
2. Click View and select Show hidden devices.
3. Expand Network adapters and look for greyed-out wireless entries.
4. Click Action and choose Scan for hardware changes.
5. If the adapter appears with a warning icon, move on to the driver fixes.

### Fix 3: Reinstall the Wi-Fi driver from the manufacturer

A missing adapter is often just a missing driver wearing a disguise. Installing the manufacturer's driver package frequently makes the adapter reappear.

1. Identify your exact laptop model.
2. On another device, download the Wi-Fi driver from the maker's support page.
3. Transfer it via USB drive and run the installer.
4. Restart the laptop after installation.
5. Open Device Manager and confirm the wireless adapter is present and working. Similar disappearances are tracked in our [Wi-Fi vanished guide](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 4: Perform a network reset

When the adapter exists but Windows' network configuration is tangled, the built-in network reset clears every adapter, profile, and binding back to a clean state.

1. Open Settings, then Network and internet, then Advanced network settings.
2. Choose Network reset and confirm.
3. The laptop will restart automatically.
4. After reboot, check Device Manager for the adapter.
5. Reconnect to your Wi-Fi network and test.

### Fix 5: Reset the BIOS to defaults

A BIOS setting changed by an update or an accidental keypress can hide the adapter. Loading defaults restores the factory hardware configuration.

1. Enter the BIOS setup on restart.
2. Find the Load Defaults, Optimized Defaults, or Reset option.
3. Confirm and save, then exit.
4. Boot Windows and rescan for hardware changes in Device Manager.
5. Reconfigure any custom BIOS settings you need afterward, such as boot order.

### Fix 6: Reseat or replace the wireless card

If the BIOS cannot see the adapter after a defaults reset, the problem is physical: a loose card or a dead one. This is the last step because it involves opening the laptop.

1. Power down completely and disconnect the charger.
2. Open the service panel and locate the M.2 wireless card.
3. Disconnect the antenna wires carefully, noting their positions.
4. Remove the card, reseat it firmly, and reconnect the antennas.
5. If it is still invisible, replace the card with a compatible model or use a USB Wi-Fi adapter as a workaround.

### Fix 7: Check the physical wireless switch and Fn toggle

Some laptops hide the wireless adapter from the operating system when the physical radio switch is off, because the BIOS stops reporting the device. Before concluding the card is dead, rule out the switch layer completely; it takes a minute and saves a needless hardware replacement.

1. Inspect the laptop's sides and front edge for a physical wireless switch and set it to on.
2. Press the Fn wireless key combination and watch for on-screen radio indicators.
3. Restart, enter the BIOS, and confirm the wireless device is enabled there.
4. Boot Windows and use Action, then Scan for hardware changes in Device Manager.
5. If the adapter appears, the switch was the whole story.

### Fix 8: Run the Windows network troubleshooter

Windows includes a network adapter troubleshooter that can rebind drivers, restart services, and reset adapter states automatically. It is a long shot at this stage of diagnosis, but it is automated, safe, and occasionally catches something manual steps missed.

1. Open Settings, then System, then Troubleshoot.
2. Choose Other troubleshooters and run the Network and Internet troubleshooter.
3. Select the Wi-Fi adapter when prompted.
4. Apply any fixes it recommends and restart the laptop.
5. Check Device Manager for the adapter afterward.

## Closing

A Wi-Fi adapter that does not show up is a visibility problem, and the BIOS check tells you which world you are in: software or hardware. Most cases resolve in the software world with driver reinstalls and network resets. When the BIOS cannot see the card either, reseating or replacing the physical card is the honest fix.
