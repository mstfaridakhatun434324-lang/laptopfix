---
title: "Fix WiFi That Won't Connect on Windows 11"
slug: how-to-fix-wifi-not-working-on-windows-11
date: 2026-10-01
categories: ["drivers"]
tags: ["wifi not working", "windows 11", "wireless driver", "network fix", "troubleshooting"]
description: "WiFi broken on Windows 11? Work through this ordered diagnostic — from quick toggles to driver surgery — and get your wireless connection back."
thumbnail: "/images/thumbs/how-to-fix-wifi-not-working-on-windows-11.webp"
faqs:
  - q: "Why did WiFi stop working after a Windows 11 update?"
    a: "Updates frequently replace the wireless driver with a generic or mismatched version that fails to initialize the adapter. The WiFi icon may vanish entirely or show connected with no internet. Rolling back the driver or installing the manufacturer's package is the standard fix and works in most cases."
  - q: "Should I reset the network settings?"
    a: "A network reset is effective but destructive: it removes all saved WiFi passwords, VPN profiles, and custom settings. Try driver-level fixes first. Use the reset as a mid-list step when the adapter works but connections fail, not as the opening move."
  - q: "How do I know if it's my laptop or my router?"
    a: "Test another device on the same network. If your phone connects fine while the laptop fails, the problem is in the laptop. If every device fails, reboot the router first. Also try the laptop on a different network, like a phone hotspot, to isolate the fault."
  - q: "What does it mean when WiFi says connected but no internet?"
    a: "Your laptop reached the router but can't reach the internet beyond it. This usually indicates a DNS problem, an IP configuration failure, or the router itself losing its upstream connection. Flushing DNS and renewing the IP address resolve the laptop-side causes."
---

WiFi failures on Windows 11 come in several flavors: the icon disappears entirely, the network list is empty, you're connected with no internet, or the connection drops every few minutes. Each flavor points at a different layer — hardware switch, driver, Windows network stack, or the router itself. The mistake most people make is jumping to a network reset before knowing which layer is broken, wiping out all their saved networks for nothing.

This guide diagnoses first. Each fix targets a specific layer, in the order a technician would check them.

The layer model matters because WiFi symptoms are notoriously misleading about their cause. "Connected, no internet" feels like a router problem but is often a corrupted DNS cache on the laptop; a missing WiFi icon feels like dead hardware but is usually a failed driver; slow speeds feel like a bad router but are often the adapter clinging to 2.4 GHz. Each fix below includes a quick way to confirm its layer before you commit to it — the phone-hotspot test for hardware, the driver version check for update damage, the ping test for stack problems. Diagnose the layer, fix the layer, and verify before moving on: that discipline is the entire difference between a ten-minute fix and an afternoon of random rebooting.

## Why this happens

- **Wireless driver corrupted by update:** Windows Update replaces the OEM WiFi driver with a mismatched version that fails to start.
- **Airplane mode or physical WiFi switch stuck:** A toggled airplane mode, Fn-key wireless switch, or physical slider disables the radio at a level Windows can't override.
- **Power management turning off the adapter:** Windows powers down the WiFi card to save battery and fails to wake it.
- **Corrupted TCP/IP stack or DNS cache:** The network stack's configuration gets damaged, blocking traffic even on a good connection.
- **Wrong WiFi band or channel:** The laptop's adapter can't see 5 GHz or 6 GHz networks due to driver or region settings.
- **Router-side issues:** Full DHCP tables, MAC filtering, or a crashed router radio look exactly like laptop problems.
- **VPN or firewall interference:** A stuck VPN adapter or overzealous firewall blocks all traffic while showing "connected."
- **Antenna cable disconnected:** Internal antenna wires can detach after drops or servicing, gutting signal strength.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check airplane mode and the hardware switch

1. Press **Windows + A** and make sure **Airplane mode** is off.
2. Look for a physical WiFi switch or slider on the laptop's side or front edge — some business laptops still have them.
3. Try the wireless **Fn-key combination** (often Fn+F2 or a dedicated key with an antenna icon).
4. If the WiFi icon is missing entirely rather than just disconnected, skip ahead to the driver fixes — a missing adapter is a driver problem.

### Fix 2: Isolate laptop vs. router

1. Check whether your **phone** connects to the same WiFi network successfully.
2. Try connecting the laptop to your **phone's hotspot** — if that works, the laptop's WiFi hardware is fine and the router is suspect.
3. Restart the **router** (unplug 30 seconds) — this alone fixes a large share of "connected, no internet" cases.
4. Only continue with laptop-side fixes after confirming other devices work on the target network.

### Fix 3: Run the network troubleshooter

1. Go to **Settings → System → Troubleshoot → Other troubleshooters → Network and Internet → Run**.
2. Apply whatever it suggests — it resets adapters and the DNS cache automatically.
3. Restart after it finishes.
4. The troubleshooter is shallow but fast, and it catches stopped services and misconfigured adapters in under two minutes.

### Fix 4: Reinstall the WiFi driver

1. Open **Device Manager → Network adapters**, right-click your wireless adapter (Intel, Realtek, MediaTek, or Qualcomm), and choose **Uninstall device**.
2. Check **Attempt to remove the driver for this device** if offered, then restart.
3. Windows reinstalls a fresh driver on boot — test WiFi before doing anything else.
4. If Windows Update then offers a WiFi driver under Optional updates, note whether the problem returns with it. For Intel-specific wireless failures, our [Intel WiFi 6 fix](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) goes deeper.

### Fix 5: Install the manufacturer's driver

1. Find your exact model on the maker's support site and download their **wireless driver** package.
2. Install it over (or after uninstalling) the current driver, then restart.
3. OEM drivers include power-management and band-configuration tuning the generic driver lacks.
4. If the adapter shows **Code 10** in Device Manager, see our [Code 10 repair guide](/articles/best-way-to-fix-wifi-driver-code-10-error/) before continuing.

### Fix 6: Disable adapter power management

1. In **Device Manager → Network adapters**, right-click the WiFi adapter → **Properties → Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. In **Settings → System → Power & battery → Power mode**, avoid the most aggressive battery-saver setting while testing.
4. This fixes WiFi that works after boot but dies when the laptop idles or sleeps.

### Fix 7: Reset the TCP/IP stack and DNS

1. Open **Terminal as administrator** and run these commands in order:
   `netsh winsock reset`
   `netsh int ip reset`
   `ipconfig /flushdns`
2. Restart the laptop.
3. Reconnect to your WiFi network and test.
4. This repairs corrupted network-stack configuration without touching your drivers — ideal for "connected, no internet" cases where the driver is healthy.

### Fix 8: Perform a network reset (last resort)

1. Go to **Settings → Network & internet → Advanced network settings → Network reset**.
2. Click **Reset now** and confirm — this reinstalls all network adapters and returns networking to factory defaults.
3. You'll need to re-enter **all WiFi passwords** and reconfigure VPNs afterward, so only do this when earlier fixes failed.
4. Microsoft documents current networking known issues on the [Windows support site](https://support.microsoft.com/en-us/windows) — check it if the failure followed a specific update. If your WiFi option vanished completely, see [how to fix WiFi that disappeared](/articles/wifi-disappeared-windows-11-no-wifi-option/).

## Closing

WiFi repair is a layer cake: radio switches, router, troubleshooter, driver, power management, network stack, and only then the nuclear reset. Most failures surrender at the driver reinstall or the stack reset. Resist the urge to start with the network reset — diagnose the layer first, and you'll fix it faster with far less collateral damage. Keep this guide's order in your back pocket for next time, too: WiFi breaks more often than any other laptop subsystem, and the second occurrence always goes faster when you already know the layers.
