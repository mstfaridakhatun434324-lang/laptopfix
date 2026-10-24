---
title: "How to Fix Mobile Hotspot Not Working on AI Laptops (Windows 11)"
slug: mobile-hotspot-not-working-ai-laptop
date: 2026-10-24
categories: ["ai-pc"]
tags: ["mobile hotspot", "tethering", "wifi", "windows 11", "networking", "troubleshooting"]
description: "Mobile hotspot failing to start or sharing no internet on your AI laptop? Follow these step-by-step fixes for drivers, sharing services, and settings."
thumbnail: "/images/thumbs/mobile-hotspot-not-working-ai-laptop.webp"
faqs:
  - q: "Why is the mobile hotspot toggle grayed out in Windows 11?"
    a: >
      A grayed-out toggle usually means the wireless adapter's driver does not support hosted networks, Wi-Fi is turned off, or airplane mode is on. Update the wireless driver and confirm Wi-Fi itself works before troubleshooting the hotspot.
  - q: "Devices connect to my hotspot but get no internet. Why?"
    a: >
      This is a sharing/routing problem: the laptop is not forwarding its internet connection to the hotspot. Check the "share my internet connection" source, restart the Internet Connection Sharing service, and confirm the laptop's own internet works.
  - q: "Can I share a Wi-Fi connection over Wi-Fi hotspot on the same adapter?"
    a: >
      Yes, if the wireless adapter supports it — Windows 11 can share one Wi-Fi connection while hosting a hotspot on the same radio. Older drivers and some adapters only support sharing an Ethernet or cellular connection, not Wi-Fi-to-Wi-Fi.
  - q: "Why does my hotspot keep turning off by itself?"
    a: >
      Windows 11 has a power-saving option that turns the hotspot off when no devices are connected. Disable "Power saving" in the hotspot settings, and also check the wireless adapter's power management in Device Manager.
---

You need to share your laptop's internet with your phone — you flip on Mobile hotspot, and Windows errors out, or the toggle is grayed out entirely, or devices connect to the hotspot but get no internet. Tethering feels like it should be trivial, which makes the failure extra annoying.

Windows 11's mobile hotspot shares the laptop's internet connection over a hosted Wi-Fi network, and it depends on three things: a wireless driver that supports hosted networks, the Internet Connection Sharing (ICS) service running correctly, and a valid upstream connection to share. On AI laptops the wireless driver is the usual suspect — hosted-network support varies by driver version, especially on newer Wi-Fi 7 chips. The same driver-update habit fixes [Zenbook A14 Snapdragon problems](/articles/asus-zenbook-a14-snapdragon-problems/) and [Discord on ARM Windows](/articles/discord-arm-windows-issues/) where connectivity is the hidden cause. Radio power settings affect more than hotspots — see how to [reduce Studio Effects battery impact](/articles/studio-effects-battery-impact-reduce/) for the same power-management tradeoffs.

This guide gives you six fixes in order: confirm Wi-Fi and driver support, fix the grayed-out toggle, repair Internet Connection Sharing, fix no-internet-on-clients, handle Wi-Fi-to-Wi-Fi sharing limits, and reset the network stack.

## Why this happens

- **Wireless driver lacks hosted-network support:** Not all drivers implement the hosted network feature — especially early Wi-Fi 7 drivers. Without it, the toggle grays out.
- **Wi-Fi turned off or airplane mode on:** The hotspot needs the Wi-Fi radio. With Wi-Fi off or airplane mode on, there is no radio to host the network on.
- **Internet Connection Sharing service broken:** ICS does the actual routing between your upstream connection and hotspot clients. If the service is stopped or corrupted, clients connect but get no internet.
- **No valid upstream connection selected:** The hotspot may be trying to share from a disconnected or wrong adapter — sharing "from" nothing gives clients nothing.
- **Power saving killing the hotspot:** Windows turns the hotspot off when idle by default, and adapter power management can kill the hosted network silently.
- **5 GHz vs 2.4 GHz band mismatch:** Some client devices (older phones, IoT gadgets) cannot see a 5 GHz-only hotspot — they need the 2.4 GHz band.
- **Corrupted network stack:** Damaged ICS configuration or Winsock state breaks sharing in ways that survive reboots.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Wi-Fi works and the driver supports hotspots

The hotspot cannot exist without a working radio and driver support — verify both.

1. Confirm Wi-Fi itself works: connect the laptop to a Wi-Fi network and browse — if Wi-Fi is broken, fix that first.
2. Open an elevated Terminal and run `netsh wlan show drivers` — look for **Hosted network supported: Yes**.
3. If it says **No**, update the wireless driver from your OEM's support page — hosted-network support is a driver feature.
4. Make sure **airplane mode is off** and Wi-Fi is **on** in Quick Settings before opening the hotspot settings.
5. If hosted-network support stays "No" on the latest driver, your adapter genuinely lacks the feature — USB Wi-Fi adapters with hotspot support are the workaround.

### Fix 2: Fix the grayed-out hotspot toggle

The toggle will not switch on — unblock it.

1. Open **Settings > Network & internet > Mobile hotspot** and check the **Share my internet connection from** dropdown — select your active connection (Wi-Fi or Ethernet).
2. Toggle **Mobile hotspot** on — if it errors immediately, note the exact message.
3. Restart the **Internet Connection Sharing (ICS)** service: `services.msc` > find it > **Restart** (set Startup type to **Automatic**).
4. Also restart the **WLAN AutoConfig** service while you are in the services list.
5. Retry the toggle — if it now stays on, connect a client device and confirm it gets an IP address.

### Fix 3: Repair Internet Connection Sharing

Hotspot turns on, devices connect, but nothing loads — ICS is not routing. Fix the sharing path.

1. On the laptop, confirm its **own** internet works — ICS cannot share a dead upstream connection.
2. In hotspot settings, verify **Share my internet connection from** points at the adapter that actually has internet (not a disconnected Ethernet or VPN adapter).
3. Open `services.msc` and confirm **Internet Connection Sharing (ICS)** is **Running** and set to **Automatic** — restart it if it is stopped.
4. Temporarily disable any third-party firewall and retest — firewalls frequently block ICS's NAT traffic.
5. Disconnect any VPN on the laptop and retest — VPNs reroute traffic in ways that break ICS routing for hotspot clients.

### Fix 4: Fix client devices getting no IP or no internet

Devices see the hotspot but cannot use it — the DHCP/NAT side needs attention.

1. On the client device, **forget** the hotspot network and reconnect fresh — stale DHCP leases cause "connected, no internet."
2. In the laptop's hotspot settings, try switching the **band** (2.4 GHz vs 5 GHz) — some clients only work on one band.
3. Change the hotspot **password** and network name to something simple (no special characters) and reconnect clients.
4. In an elevated Terminal on the laptop, run `ipconfig /release` and `ipconfig /renew`, then restart the hotspot.
5. Test with a second client device — if one device works and another does not, the problem is the client, not the hotspot.

### Fix 5: Handle Wi-Fi-to-Wi-Fi sharing limitations

You want to share the laptop's Wi-Fi connection over a Wi-Fi hotspot using the same adapter — this needs specific driver support.

1. Check `netsh wlan show drivers` again — Wi-Fi-to-Wi-Fi sharing needs both hosted-network support and a driver that allows concurrent station + AP mode.
2. If the driver does not support it, the practical alternative is sharing from **Ethernet** (dock or USB adapter) or **USB-tethered phone data** instead.
3. Update to the latest wireless driver — concurrent-mode support has been added to several Wi-Fi 7 drivers in recent updates.
4. As a workaround, use **Bluetooth tethering** for a single device (**Settings > Bluetooth & devices**) — slower, but it works when Wi-Fi hotspot will not.
5. For a permanent travel setup needing Wi-Fi-to-Wi-Fi, a small travel router does the job more reliably than any laptop hotspot.

### Fix 6: Reset the network stack

Persistent hotspot failures across all the above — clear corrupted sharing state.

1. Turn the hotspot **off**, then in an elevated Terminal run `netsh winsock reset` and `netsh int ip reset`.
2. Restart the laptop, then go to **Settings > Network & internet > Advanced network settings > Network reset** and reset.
3. After reboot, reinstall the latest wireless driver from the OEM (the reset can revert drivers).
4. Reconfigure the hotspot from scratch: set the source connection, network name, password, and band.
5. Test with a client device immediately — if it works now, the old ICS configuration was corrupt; if not, the adapter's hosted-network support is the remaining suspect.

## Closing

Mobile hotspot on AI laptops is a driver-and-service feature: confirm hosted-network support with `netsh wlan show drivers`, keep the wireless driver current, and make sure ICS is running and pointing at a live upstream connection. Most failures resolve by Fix 3. The honest limits: some adapters simply do not support Wi-Fi-to-Wi-Fi sharing (share from Ethernet instead), and Windows' idle power-saving will keep turning the hotspot off unless you disable it. For driver updates, your OEM's support page remains the authoritative source.
