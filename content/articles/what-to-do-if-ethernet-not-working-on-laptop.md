---
title: "Ethernet Not Working on Your Laptop? Wired Network Fixes That Work"
slug: what-to-do-if-ethernet-not-working-on-laptop
date: 2026-10-03
categories: ["drivers"]
tags: ["ethernet not working", "wired network", "lan driver", "network adapter", "windows 11"]
description: "Laptop Ethernet not working? Fix unidentified networks, dead LAN ports, and driver issues with this step-by-step wired networking guide."
thumbnail: "/images/thumbs/what-to-do-if-ethernet-not-working-on-laptop.webp"
faqs:
  - q: "Why is my laptop's Ethernet port not working but WiFi is fine?"
    a: "When WiFi works but Ethernet doesn't, the problem is isolated to the wired path: the cable, the port, the Ethernet adapter driver, or the router's LAN port. Start by swapping the cable and trying a different port on the router. If those don't help, reinstall the Ethernet adapter driver in Device Manager — Windows Update frequently breaks wired drivers while leaving WiFi untouched."
  - q: "What does 'Unidentified network' mean on Ethernet?"
    a: "It means your laptop got a link to the router or switch but couldn't obtain a valid IP configuration — usually a DHCP failure. Releasing and renewing the IP (ipconfig /release then /renew), restarting the router, or resetting the TCP/IP stack typically resolves it. A bad cable that passes link but corrupts data can also cause this exact symptom."
  - q: "How do I know if my laptop's Ethernet port is physically dead?"
    a: "Check for link lights: most Ethernet ports have LEDs that blink with activity when a cable is connected. No lights with a known-good cable and a working router port strongly suggests hardware failure. Also check Device Manager — if the Ethernet adapter is missing entirely (not just disabled), the controller may have failed or been disabled in BIOS."
  - q: "Do I need a driver for a USB Ethernet adapter?"
    a: "Most modern USB Ethernet adapters work with Windows' built-in drivers, but for full speed and reliability you should install the manufacturer's driver (usually Realtek or ASIX chipset). If a USB adapter isn't recognized, try a different USB port, install the vendor driver from another computer via USB stick, and check Device Manager for error codes on the device."
---

WiFi works fine, but the moment you plug in an Ethernet cable — nothing. No connection, an 'Unidentified network' warning, or Windows acting like the cable doesn't exist. Wired networking is supposed to be the reliable option, which makes it doubly annoying when it's the thing that breaks.
The diagnostic advantage of Ethernet is that it's beautifully isolatable: cable, laptop port, adapter driver, router port. Each can be tested independently, and link LEDs give you instant physical-layer feedback that WiFi never provides. This guide works that chain in order. If your laptop has no Ethernet port at all and you're using a USB adapter, most steps still apply — and our [USB device troubleshooting](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) helps when the adapter itself isn't recognized.
One quick check before you start: many modern thin laptops dropped the RJ45 port entirely, so confirm you're actually dealing with a built-in port versus a dongle. Dongle problems are usually driver or USB-power issues in disguise. For the driver side, our deep dive on [Ethernet adapter driver issues](/articles/how-to-fix-ethernet-not-working-on-laptop-in-windows-11-24h2/) covers the Device Manager specifics.

## Why this happens

- **Faulty Ethernet cable.** Cables fail internally while looking perfect — a single broken pair kills the connection while link lights may still blink.
- **Dead router/switch port.** The far end fails just as often as the laptop end, and people rarely suspect it.
- **Corrupted Ethernet adapter driver.** Windows Update replaces working wired drivers with broken generic ones on a regular basis.
- **DHCP failure.** The laptop gets link but no IP address, producing the classic 'Unidentified network' status.
- **Adapter disabled in Windows or BIOS.** Power management or a BIOS toggle can switch the Ethernet controller off entirely.
- **TCP/IP stack corruption.** Winsock and IP stack corruption breaks all wired connectivity while WiFi sometimes keeps working.
- **Duplex/speed mismatch.** Forced speed settings that don't match the switch cause link-but-no-traffic symptoms.
- **Physically damaged RJ45 port.** Bent pins or a broken retention clip cause intermittent or total failure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the cable and the far end first

Ethernet troubleshooting starts with the physical layer — link lights don't lie, and cables are the cheapest component to swap.

1. Swap in a known-good Ethernet cable (borrow one that's currently working elsewhere).
2. Plug into a different LAN port on your router or switch.
3. Check the laptop port's LEDs: solid link light plus blinking activity light means the physical layer is up.
4. If another device works on the same cable and router port, the problem is your laptop — continue below.
5. If no device works on that cable/port combo, replace the cable first; it's the most common failure.

### Fix 2: Confirm the adapter exists and is enabled

A missing or disabled adapter in Device Manager explains 'cable unplugged' messages when a cable is clearly plugged in.

1. Open Device Manager (Windows + X) → expand 'Network adapters.'
2. Look for your Ethernet controller (Realtek PCIe GbE, Intel Ethernet, Killer, etc.).
3. If it has a down-arrow icon, right-click → Enable device.
4. If it's missing entirely, click View → 'Show hidden devices'; if it appears grayed out, the hardware may be disabled in BIOS.
5. Restart into BIOS/UEFI and verify the onboard LAN / Ethernet controller is Enabled.

### Fix 3: Release, renew, and reset the IP stack

'Unidentified network' with good link lights is almost always a DHCP or stack problem — these commands rebuild it.

1. Open Command Prompt as administrator.
2. Run: ipconfig /release then ipconfig /renew — check whether you get a valid 192.168.x.x or 10.x.x.x address.
3. If you get a 169.254.x.x address, DHCP failed: restart your router and try again.
4. Run: netsh winsock reset and netsh int ip reset, then reboot.
5. After reboot, run ipconfig /all and confirm a proper IP, subnet mask, and gateway.

### Fix 4: Reinstall the Ethernet adapter driver

The most reliable fix for driver-level Ethernet failures: remove the corrupted driver completely and install the right one.

1. In Device Manager, right-click the Ethernet adapter → Uninstall device, checking 'Attempt to remove the driver for this device.'
2. Restart — Windows reinstalls a base driver on boot.
3. Test the connection; if it works, you're done — but get the proper driver next.
4. Download the LAN driver for your exact model from your laptop maker's support site and install it over the generic one.
5. Intel-based laptops can use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to identify the correct wired driver automatically.

### Fix 5: Fix speed, duplex, and power management

Auto-negotiation usually works, but mismatches and aggressive power-saving break wired connections in subtle ways.

1. In Device Manager, open the Ethernet adapter's Properties → Advanced tab.
2. Find 'Speed & Duplex' and set it to 'Auto Negotiation' (or try '1.0 Gbps Full Duplex' if auto fails against your switch).
3. Go to the Power Management tab and uncheck 'Allow the computer to turn off this device to save power.'
4. In the Advanced tab, disable 'Energy Efficient Ethernet' as a test — it causes dropouts on some switches.
5. Click OK, disable/re-enable the adapter (right-click → Disable, then Enable), and retest.

### Fix 6: Reset the network stack completely

When individual fixes fail, Windows' built-in network reset wipes every adapter and setting back to factory — the nuclear option that works.

1. Open Settings → Network & internet → Advanced network settings → Network reset.
2. Click 'Reset now' and confirm — the laptop will reboot.
3. After reboot, reconnect the Ethernet cable and let Windows redetect everything fresh.
4. Re-enter any static IP settings or VPN configurations you were using (write them down first).
5. If you use 802.1X corporate authentication, reconfigure it — the reset wipes those profiles.

### Fix 7: Bypass with a USB Ethernet adapter

If the built-in port is physically dead, a USB Ethernet adapter restores wired networking for the price of lunch.

1. Buy a USB 3.0 Gigabit Ethernet adapter from a reputable brand (check reviews for your Windows version).
2. Plug it directly into the laptop (not through a hub) and let Windows install its driver.
3. If it's not recognized, install the vendor driver from another PC via USB stick — see Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for driver-install basics.
4. Disable the broken built-in adapter in Device Manager to avoid confusion.
5. This is also a fine permanent solution — many technicians prefer USB adapters over motherboard-level port repairs.

## Closing

Ethernet problems reward methodical work: cable, far end, adapter state, IP stack, driver, then the nuclear network reset. Because each layer is testable, you can usually pin the fault in under twenty minutes — and a USB adapter means even a dead port doesn't have to end your wired connection.
