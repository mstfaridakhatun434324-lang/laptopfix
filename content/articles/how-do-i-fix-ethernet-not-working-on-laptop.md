---
title: "Ethernet Not Working on Your Laptop? How to Fix It Step by Step"
slug: how-do-i-fix-ethernet-not-working-on-laptop
date: "2026-10-06"
categories: ["drivers"]
tags: ["ethernet", "wired network", "lan driver", "network adapter", "no internet"]
description: "Laptop Ethernet port not working? Follow this step-by-step guide to check cables, drivers, and Windows network settings to get your wired connection back."
thumbnail: "/images/thumbs/how-do-i-fix-ethernet-not-working-on-laptop.webp"
faqs:
- q: "Why is my laptop Ethernet port not working but WiFi is fine?"
  a: "WiFi and Ethernet use completely separate adapters and drivers, so one can fail while the other works perfectly. The usual suspects are a disabled Ethernet adapter, a corrupted LAN driver after a Windows update, or power management turning the port off to save energy. Because the two paths are independent, a working WiFi connection tells you the router and internet service are fine, narrowing the problem to your laptop's wired hardware or its driver."
- q: "How do I know if my Ethernet port is physically broken?"
  a: "Plug in a cable and watch the small LEDs next to the port. A working port shows a solid link light and a blinking activity light. No lights at all with a known-good cable and router port points to a dead port or a disabled adapter. If lights appear but Windows shows no connection, the hardware is likely fine and the issue is a driver or software setting, which is far more common and fixable."
- q: "Do I need a driver for my laptop Ethernet port?"
  a: "Yes. The Ethernet controller needs its driver to communicate with Windows, and without it the adapter may not appear in Device Manager at all or show a warning icon. Most laptops use Realtek, Intel, or Killer networking chips. The correct driver comes from your laptop manufacturer's support page for your exact model, and installing it resolves a large share of Ethernet failures after Windows updates."
- q: "Can a Windows update break Ethernet on a laptop?"
  a: "Absolutely, and it happens regularly. Feature updates sometimes replace a working vendor LAN driver with a generic Microsoft one that lacks proper support, or they reset power management settings that then switch the adapter off. If Ethernet died right after an update, reinstalling the manufacturer's LAN driver and disabling power saving on the adapter are the two fixes to try first."
---

A dead Ethernet port is uniquely annoying: WiFi works, the router is fine, but the wired connection your laptop used to pick up instantly now does nothing. No "identifying network," no lights, or a permanent "network cable unplugged" message while the cable sits firmly in the jack. Because wired connections are usually the fallback you trust, losing one feels like a betrayal by the most reliable part of your setup.

The good news is that genuinely broken Ethernet hardware is rare. In most cases the port is fine and the problem sits in one of three places: the physical link (cable, router port, or the laptop's jack), the driver (missing, corrupted, or replaced by a Windows update), or Windows' own network stack and power settings. Each has a distinct signature, and checking them in the right order gets you reconnected fast.

This guide works through the problem the way a technician would — physical layer first, then driver, then software.

## Why this happens

- **Damaged or low-quality cable**: A kinked, chewed, or cheap cable can fail silently; Ethernet needs all eight conductors, and one broken wire kills the link.
- **Disabled network adapter**: The Ethernet adapter can be disabled in Windows network settings, sometimes by a utility or an accidental keypress.
- **Corrupted or replaced LAN driver**: Windows updates frequently swap vendor LAN drivers for generic ones that do not fully support the chip.
- **Power management switching the port off**: Windows may power down the Ethernet controller to save energy, especially on battery, and fail to wake it.
- **Corrupted TCP/IP stack or Winsock catalog**: Misbehaving VPNs, firewalls, or malware can corrupt the network stack so no adapter can get an address.
- **Router or switch port problem**: The fault can sit on the other end — a dead router LAN port looks identical to a dead laptop port.
- **BIOS or hardware fault**: Rare, but a disabled onboard LAN in BIOS or a failed controller chip produces a port with no lights at all.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the physical link — cable, port LEDs, and router

Ethernet troubleshooting always starts at the physical layer because it is the fastest thing to rule out and the most embarrassing to miss. The tiny LEDs beside the jack are a built-in diagnostic: a solid link light means the electrical connection is good, and a blinking light means traffic is flowing. No lights with a known-good cable points at the port or the other end.

1. Check the LEDs next to the Ethernet jack while plugged in — note whether any light up.
2. Swap in a different, known-good Ethernet cable (Cat5e or better).
3. Plug the cable into a different LAN port on your router or switch.
4. If possible, test the same cable and router port with another device to confirm they work.
5. Blow out dust from the laptop's jack and make sure the cable clicks in firmly.

### Fix 2: Make sure the Ethernet adapter is enabled

An adapter that is disabled in Windows behaves exactly like a dead port — no lights activity in software, no connection attempts. Adapters get disabled by power utilities, by "network reset" tools, or by accident in the Control Panel. Re-enabling takes seconds and is worth checking before touching any drivers.

1. Press Win + R, type `ncpa.cpl`, and press Enter to open Network Connections.
2. Look for "Ethernet" — if it is grayed out, right-click it and choose Enable.
3. If Ethernet does not appear at all, the driver is missing; skip to Fix 3.
4. Once enabled, wait 30 seconds and check whether it shows "Identifying" or connects.
5. If it enables but shows "Network cable unplugged" with a good cable, continue to the next fixes.

### Fix 3: Reinstall the Ethernet driver from the manufacturer

The LAN driver is the most common root cause, especially after Windows updates. Device Manager may show the controller with a yellow triangle, list it as an [unknown device](/articles/how-to-fix-unknown-device-in-device-manager/), or hide it entirely. Installing the vendor's driver for your exact model restores full functionality, including proper speed negotiation and power behavior.

1. Open Device Manager (Win + X) and expand "Network adapters."
2. Right-click the Ethernet controller, choose "Uninstall device," and tick "Attempt to remove the driver."
3. Restart the laptop — Windows will try to reinstall a driver automatically.
4. If it still fails, download the LAN driver from your maker's support page (e.g. [Dell Support](https://www.dell.com/support)) using WiFi or another computer.
5. Install the downloaded driver, restart, and test the wired connection.

### Fix 4: Reset the TCP/IP stack and Winsock

When the adapter looks healthy but cannot obtain an IP address — stuck on "Identifying" or showing a 169.254.x.x address — the network stack itself is corrupted. The `netsh` reset commands rebuild TCP/IP and Winsock to a clean state without touching your files, curing damage left by VPN clients and third-party firewalls.

1. Open Terminal or Command Prompt as administrator.
2. Run `netsh winsock reset` and press Enter.
3. Run `netsh int ip reset` and press Enter.
4. Run `ipconfig /release` followed by `ipconfig /renew`.
5. Restart the laptop and plug in the cable to test.

### Fix 5: Stop Windows from powering off the adapter

Windows power management can switch the Ethernet controller off to save energy and then fail to wake it, particularly on laptops running on battery. The symptom is an adapter that works after a restart but dies after sleep. Disabling the power-saving option on the adapter itself stops this behavior permanently.

1. In Device Manager, right-click the Ethernet adapter and choose Properties.
2. Open the Power Management tab.
3. Untick "Allow the computer to turn off this device to save power."
4. Click OK, then also check the Advanced tab for "Energy Efficient Ethernet" and disable it.
5. Restart and confirm the connection survives sleep and wake cycles.

### Fix 6: Check for driver conflicts and BIOS settings

If the adapter is missing from Device Manager entirely, look deeper. A conflict with a VPN virtual adapter or a disabled onboard LAN in BIOS can both hide the controller. The BIOS check matters because some laptops ship with onboard LAN disabled by default, and a BIOS update can flip the setting back.

1. In Device Manager, click View and enable "Show hidden devices" to reveal grayed-out adapters.
2. Remove any stale or duplicate Ethernet entries and old VPN virtual adapters.
3. Restart into BIOS/UEFI setup and confirm onboard LAN is enabled.
4. While in BIOS, consider loading optimized defaults if settings look wrong.
5. Boot back into Windows and rescan for hardware changes in Device Manager.

### Fix 7: Test with a USB-to-Ethernet adapter

If nothing above revives the port, a USB-to-Ethernet adapter (about the price of a pizza) both diagnoses and solves the problem: if the USB adapter works, your internal controller or jack is dead and the USB adapter is a perfectly good permanent replacement. This is the pragmatic endpoint — motherboard-level Ethernet repair rarely makes economic sense on an older laptop.

1. Borrow or buy a USB 3.0 to Gigabit Ethernet adapter.
2. Plug it in and let Windows install its driver automatically.
3. Connect your cable to the adapter and test the connection.
4. If it works, the internal port is faulty; keep using the adapter.
5. If even the USB adapter fails, suspect the cable, router, or a deeper OS issue and revisit Fix 1 and Fix 4.

Related network headaches often travel together: if your wireless is also acting up, see our guide on [troubleshooting a mobile hotspot not working](/articles/troubleshoot-hotspot-not-working-on-laptop/), and for brand-specific wireless driver issues the [Acer laptop WiFi fix](/articles/how-to-fix-wifi-not-working-on-acer-laptop/) covers the same driver-reinstall technique for WiFi adapters.

## Closing

Ethernet failures look dramatic but are usually mundane: a bad cable, a disabled adapter, or a driver that a Windows update quietly replaced. Work the layers in order — physical, driver, stack, power — and you will find the culprit fast. When the port itself is truly dead, a USB Ethernet adapter restores wired speed for very little money.
