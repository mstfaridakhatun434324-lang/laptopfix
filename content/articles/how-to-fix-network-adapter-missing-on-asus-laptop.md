---
title: "Network Adapter Missing on ASUS Laptop? Restore It Now"
slug: how-to-fix-network-adapter-missing-on-asus-laptop
date: 2026-10-12
categories: ["drivers"]
tags: ["network adapter missing", "asus laptop", "wifi adapter", "device manager", "network driver"]
description: "Network adapter vanished from your ASUS laptop? Bring it back with Device Manager rescans, driver reinstalls, BIOS checks, and power management fixes."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-on-asus-laptop.webp"
faqs:
  - q: "Why did my network adapter disappear from Device Manager?"
    a: "The most common cause is a failed driver update that left the adapter in an error state, after which Windows hid it. Power management aggressively suspending the adapter, a BIOS update disabling the wireless card, or actual hardware failure are the other usual suspects in that order."
  - q: "Can I get Wi-Fi back without the original driver disc?"
    a: "Yes — you do not need any disc. Download the wireless and LAN drivers from ASUS support using another device, transfer them on a USB stick, and install them offline. Alternatively, USB-tether a phone for temporary internet and let Windows Update fetch the drivers."
  - q: "Why does the adapter disappear after sleep but return on restart?"
    a: "That pattern points to power management or a buggy driver that fails to reinitialize the card on wake. Disable 'allow the computer to turn off this device' for the adapter and update to the ASUS-validated driver. If it persists, the card itself may be failing."
  - q: "Is a missing network adapter a hardware problem?"
    a: "Sometimes, but check software first. If the adapter is absent even in BIOS/UEFI network information and a Linux live USB cannot see it either, the card is likely dead or unseated. If BIOS sees it, the problem is drivers or Windows configuration."
---

There is no Wi-Fi icon, no Ethernet adapter, and Device Manager shows no network devices at all — not even with warning icons. Your ASUS laptop has simply forgotten it has networking hardware. It is alarming, but in most cases the adapter is still physically fine; Windows has just lost track of it.

The network adapter can vanish for several distinct reasons: a driver update that failed halfway, Windows power management parking the device and never waking it, a BIOS setting that disabled the wireless card, or the adapter being hidden after repeated errors. Each cause has a different fix, so diagnosis matters.

This ASUS-focused guide walks you through the recovery sequence technicians use: rescan and unhide, driver surgery, power management, BIOS verification, and finally hardware checks. Work through these in order — diagnose first, then act.

## Why this happens


- **Failed driver update hiding the device:** When a network driver update fails, Windows may mark the device as failed and hide it from the default Device Manager view.
- **Aggressive power management:** ASUS power profiles can suspend the wireless card to save battery, and some cards never reinitialize properly.
- **BIOS wireless toggle disabled:** Many ASUS laptops have a firmware-level wireless switch; BIOS updates and resets can turn it off silently.
- **Airplane mode stuck at firmware level:** The Fn + F2 wireless toggle can leave the radio in a stuck-off state that Windows cannot override.
- **Corrupt driver store entries:** Repeated install/uninstall cycles can corrupt the driver store so Windows refuses to bind any driver to the card.
- **Windows update replacing the ASUS driver:** Generic drivers from Windows Update sometimes fail on ASUS-specific wireless card firmware, causing the device to drop out.
- **Loose M.2 wireless card:** On older laptops, the Wi-Fi card can work loose in its slot from drops or heat cycling, disappearing intermittently.
- **Dead wireless card:** Cards do fail — usually after years of heat — and when they do, they vanish from BIOS as well as Windows.

## How to fix it


Work through these in order — diagnose first, then act.

### Fix 1: Unhide and rescan for the adapter


The adapter is often present but hidden. Showing hidden devices and forcing a hardware rescan brings ghosted adapters back into view so you can see what state they are in.

1. Press Windows + X and open Device Manager.
2. Click View, then Show hidden devices.
3. Expand Network adapters and look for greyed-out or warning-marked entries.
4. Click Action, then Scan for hardware changes.
5. If the adapter appears with a warning icon, right-click it, Properties, and read the Device status — error codes 10, 31, and 43 each point to driver problems.
6. If nothing appears even as hidden, move to the BIOS check later in this guide.

### Fix 2: Toggle the wireless with Fn + F2 and check Airplane mode


ASUS laptops have a hardware-level wireless toggle that operates below Windows. If it is stuck off, no driver reinstall will help — you have to flip the radio back on at this level first.

1. Press Fn + F2 (the wireless icon key) and wait ten seconds.
2. Open Settings, Network & internet, and check whether Airplane mode is on — turn it off.
3. Click the network icon in the taskbar and confirm Wi-Fi appears as an option.
4. If the key does nothing, the ASUS System Control Interface driver may be missing — install it from ASUS support.
5. Test again after installing that driver, since it powers the Fn-key layer.

### Fix 3: Reinstall the network drivers cleanly


This is the core fix for most missing-adapter cases. You remove the broken driver state completely, then install the ASUS-validated wireless and LAN drivers fresh — not the generic ones Windows prefers.

1. In Device Manager (with hidden devices shown), right-click the network adapter and choose Uninstall device.
2. Check Attempt to remove the driver for this device, then click Uninstall.
3. Restart the laptop.
4. On another device, download the Wireless and LAN drivers for your exact ASUS model from ASUS support to a USB stick — or temporarily USB-tether your phone for internet.
5. Install the LAN driver first, then the wireless driver, restarting after each.
6. Open Device Manager and confirm the adapter appears without warnings. For general driver technique, see our [OEM driver installation guide](/articles/how-to-install-oem-drivers-manually-on-windows-11/).

### Fix 4: Disable power management on the adapter


If the adapter vanishes after sleep but returns on restart, Windows is parking the card and failing to wake it. Disabling device-level power saving breaks that cycle.

1. In Device Manager, right-click the network adapter and choose Properties.
2. Go to the Power Management tab and uncheck Allow the computer to turn off this device to save power.
3. On the Advanced tab, look for power-saving properties (like Power Saving Mode or Selective Suspend) and set them to Maximum Performance.
4. In Settings, System, Power & battery, set your power mode to Best performance while testing.
5. Put the laptop to sleep and wake it three times to confirm the adapter survives.

### Fix 5: Reset the network stack


Corrupted TCP/IP and Winsock state can prevent a working adapter from appearing functional. A full stack reset returns all network components to factory state without touching your drivers.

1. Open an elevated Command Prompt (Windows + X, Terminal (Admin)).
2. Run these commands in order: netsh winsock reset, then netsh int ip reset, then ipconfig /release, ipconfig /renew, ipconfig /flushdns.
3. Restart the laptop.
4. Go to Settings, Network & internet, Advanced network settings, Network reset, and click Reset now as a final sweep.
5. After the restart, reconnect to your Wi-Fi network and test stability. For additional official network repair steps, see the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 6: Verify the adapter in BIOS/UEFI


If Windows cannot see the adapter at all, check whether the firmware can. This single check separates software problems from hardware problems definitively.

1. Restart and enter BIOS (F2 or Del on most ASUS laptops).
2. Look under Advanced for Onboard Devices, Wi-Fi, WLAN, or Network Stack settings.
3. Make sure wireless/LAN controllers are Enabled.
4. Check whether the BIOS lists the wireless card model — if it does, the hardware is alive and Windows is the problem.
5. If the BIOS shows no wireless hardware, reseat the M.2 card (if comfortable opening the laptop) or arrange service.
6. Our [post-update adapter recovery guide](/articles/how-to-fix-network-adapter-missing-after-windows-11-update/) covers cases where a Windows update triggered the disappearance.

### Fix 7: Test with a live USB and consider hardware service


The last diagnostic: boot a Linux live USB. If Linux sees the wireless card, your hardware is fine and Windows needs a repair install. If Linux cannot see it either, the card is dead.

1. Create a Ubuntu live USB on another PC and boot your ASUS from it (Esc for boot menu).
2. Check whether Wi-Fi networks appear in the live environment.
3. If they do, back up your data and perform a Windows in-place upgrade to rebuild the driver stack.
4. If they do not, the wireless card has likely failed — contact ASUS support for a replacement.
5. As a stopgap, a USB Wi-Fi adapter ($15-25) restores connectivity immediately on any laptop.

## Closing


A missing network adapter feels like a hardware death sentence, but the overwhelming majority of cases end at the driver or BIOS layer. The hidden-devices rescan and clean driver reinstall recover most ASUS laptops; the BIOS check tells you definitively whether you are fighting software or shopping for a replacement card. Either way, you now know exactly where you stand.
