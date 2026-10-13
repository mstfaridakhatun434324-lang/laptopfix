---
title: "Wi-Fi Driver Code 10 Error on ASUS Laptop? How to Fix It"
slug: "how-to-fix-wifi-driver-code-10-error-on-asus-laptop"
date: 2026-09-03
categories: ["drivers"]
tags: ["code 10", "wifi driver", "asus laptop", "device manager", "wifi not working"]
description: "Device Manager shows Code 10 on your ASUS laptop Wi-Fi adapter? Learn what the error means and how to clear it with driver reinstalls, BIOS checks, and power resets."
thumbnail: "/images/thumbs/how-to-fix-wifi-driver-code-10-error-on-asus-laptop.webp"
faqs:
  - q: "What does Code 10 mean on a Wi-Fi adapter?"
    a: "Code 10 means the device failed to start: Windows loaded a driver for the adapter but the hardware did not initialize correctly. For Wi-Fi cards this usually indicates a driver mismatch, a corrupted driver installation, or the card failing to enumerate after sleep. It rarely means the card is physically dead, so software fixes resolve most Code 10 cases on ASUS laptops."
  - q: "Why does Code 10 appear after a Windows update?"
    a: "Windows Update sometimes installs a driver version that does not match the wireless card's firmware or the laptop's hardware configuration. The new driver loads, the card rejects the initialization sequence, and Device Manager reports Code 10. Rolling back to the previous driver or installing the ASUS-validated driver for your exact model fixes the mismatch."
  - q: "Can the BIOS cause a Wi-Fi Code 10 error?"
    a: "Yes. The BIOS controls how the wireless card is powered and enumerated at boot, and outdated BIOS versions on some ASUS models mishandle this for newer MediaTek or Intel cards. If Code 10 survives every driver fix, check the ASUS support page for a BIOS update whose changelog mentions wireless, WLAN, or device enumeration fixes."
  - q: "Is a Code 10 Wi-Fi error a hardware failure?"
    a: "Not usually at first, but it becomes the likely answer after software is exhausted. If a clean ASUS driver install, a BIOS update, a cold boot power drain, and testing with a Linux live USB all still show the card failing to start, the wireless module itself is probably faulty. USB Wi-Fi adapters make a cheap workaround while you arrange a repair."
---

Code 10 is one of the least helpful errors in Windows: This device cannot start. On an ASUS laptop's Wi-Fi adapter it means the driver loaded but the wireless card refused to initialize, leaving you with no networks at all. The adapter sits in Device Manager with a yellow warning triangle and every network feature on the laptop is dead.

The encouraging news is that Code 10 on ASUS Wi-Fi is a software problem in most cases. The usual story is a driver mismatch after a Windows update, a card that failed to wake from sleep, or a BIOS that enumerates the card incorrectly. Genuine card failure happens, but it is the last thing to suspect, not the first.

This guide moves from the quickest resets to the deeper driver and BIOS work. If your adapter is missing entirely rather than showing Code 10, the [missing-driver guide](/articles/how-to-find-missing-drivers-on-windows-11-on-laptop/) is the better starting point, and [MediaTek-specific Wi-Fi fixes](/articles/how-to-fix-mediatek-wifi-not-working-on-asus-laptop/) cover that card family in depth.

## Why this happens

- **Driver mismatch after Windows Update:** an automatically installed driver version does not match the card firmware, so initialization fails.
- **Corrupted driver files:** a partial or interrupted driver update leaves files the card cannot start from.
- **Card failed to wake from sleep:** the wireless module can get stuck in a low-power state that a restart does not clear.
- **Outdated BIOS:** the BIOS mishandles power sequencing or enumeration for the wireless card model installed.
- **Fast Startup preserving bad state:** hybrid shutdown carries the failed device state from boot to boot.
- **Conflicting filter drivers:** VPN clients and some security software install network filters that interfere with adapter startup.
- **Wrong driver for the card variant:** ASUS ships Intel, MediaTek, and Realtek cards across models; the wrong vendor driver cannot start the hardware.
- **Failing wireless module:** hardware degradation eventually produces Code 10 that no software change clears.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Cold-boot to reset the wireless card

A wireless card stuck in a bad power state can report Code 10 through every restart because restarts never fully power it down. A cold boot with residual power drained forces the card to reinitialize from scratch.

1. Shut the laptop down fully instead of restarting.
2. Unplug the charger and remove all USB devices.
3. Hold the power button down for 20 seconds.
4. Wait a full minute, reconnect the charger, and power on.
5. Open Device Manager and check whether the Code 10 is gone.

### Fix 2: Roll back the driver

If Code 10 appeared right after an update, the previous driver was working. Rolling back takes a minute and immediately tests the mismatch theory.

1. Open Device Manager and expand Network adapters.
2. Right-click the Wi-Fi adapter and open Properties.
3. Go to the Driver tab and click Roll Back Driver if it is available.
4. Choose a reason and confirm, then restart the laptop.
5. Verify Wi-Fi connects; if so, pause driver updates for the adapter.

### Fix 3: Clean-reinstall the ASUS-validated driver

When rollback is unavailable, do a full clean install of the driver ASUS validated for your exact model. Identify your card's vendor first so you install the right package.

1. In Device Manager, check the adapter name to identify Intel, MediaTek, or Realtek.
2. Right-click it, choose Uninstall device, and check Attempt to remove the driver.
3. Restart the laptop.
4. Download the WLAN driver from the ASUS support page for your exact model number.
5. Install it, restart again, and confirm the adapter starts without Code 10.

### Fix 4: Disable Fast Startup

Fast Startup can reload the failed device state on every boot, making Code 10 look permanent. Disabling it forces a true initialization of all hardware at each startup.

1. Open Control Panel and go to Power Options.
2. Click Choose what the power buttons do.
3. Click Change settings that are currently unavailable.
4. Uncheck Turn on fast startup and save changes.
5. Shut down fully and power on to test the adapter.

### Fix 5: Remove conflicting VPN and filter drivers

VPN clients install network filter drivers that bind to the adapter. A corrupted or incompatible filter can block the adapter from starting with Code 10.

1. Uninstall any VPN client you do not actively need, then restart.
2. In Device Manager, click View and choose Show hidden devices.
3. Expand Network adapters and uninstall any greyed-out WAN Miniport or filter entries.
4. Check the adapter properties for third-party items you can uncheck for testing.
5. Reinstall your VPN fresh afterward if you need it.

### Fix 6: Update the BIOS

ASUS BIOS updates regularly fix device enumeration and power sequencing for wireless cards. If Code 10 survives driver work, the BIOS is the next layer down.

1. Find your current BIOS version in System Information.
2. Compare it with the latest on the ASUS support page for your model.
3. Download and run the BIOS update with the charger firmly connected.
4. Do not interrupt the update for any reason.
5. After it completes, enter the BIOS, load optimized defaults, save, and boot.

### Fix 7: Test with a live USB and consider hardware

A Linux live USB boots an entirely independent driver stack. If the card fails there too, the fault is in hardware, not Windows. This test gives a confident answer before spending money.

1. Create a bootable Ubuntu USB stick on another computer.
2. Boot your ASUS laptop from it and try the live session without installing.
3. Check whether Wi-Fi works in the live environment.
4. If it fails there too, the wireless module is likely faulty.
5. A USB Wi-Fi adapter is a cheap interim fix; check warranty for a proper repair.

## Closing

Code 10 looks fatal but is usually just a driver or power-state disagreement between Windows and the wireless card. Cold boot, roll back or clean-install the ASUS driver, and update the BIOS, in that order, and the adapter starts again in the large majority of cases. Microsoft documents these same wireless repair steps in the [Windows support hub](https://support.microsoft.com/en-us/windows), which is worth bookmarking for the next driver-related outage.
