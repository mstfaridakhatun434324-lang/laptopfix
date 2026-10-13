---
title: "Fix a Laptop Hotspot That Won't Share Internet"
slug: how-to-fix-hotspot-not-working-on-laptop
date: 2026-09-01
categories: ["drivers"]
tags: ["mobile hotspot", "internet sharing", "wifi hotspot", "windows 11", "network fix"]
description: "Mobile hotspot on your laptop won't share internet? Fix the hosted-network driver, ICS settings, and adapter issues that break Windows hotspots."
thumbnail: "/images/thumbs/how-to-fix-hotspot-not-working-on-laptop.webp"
faqs:
  - q: "Why won't my laptop's mobile hotspot turn on?"
    a: "The most common reasons are the wireless adapter driver lacking hosted-network support, airplane mode blocking the radio, or the Internet Connection Sharing service being disabled. Check that your WiFi driver supports hosted networks first — some older drivers and certain USB adapters simply can't do it."
  - q: "Why do devices connect to my hotspot but get no internet?"
    a: "The hotspot radio is working but internet sharing isn't bridging to your connection. This usually means Internet Connection Sharing is misconfigured, the firewall is blocking the shared connection, or the laptop's own internet dropped. Verify the laptop itself has working internet first, then check the sharing settings."
  - q: "Can a VPN break the mobile hotspot?"
    a: "Yes, frequently. VPN clients reroute all traffic through their virtual adapter, which breaks the bridge between your real internet connection and the hotspot. Disconnect the VPN entirely — not just pause it — and test the hotspot before troubleshooting anything else."
  - q: "Does the hotspot need a special WiFi driver?"
    a: "It needs a driver with hosted-network (SoftAP) support. Most modern built-in adapters have it, but the capability can break when Windows Update installs a generic driver. Reinstalling the manufacturer's wireless driver usually restores hotspot functionality. Verify the capability anytime with `netsh wlan show drivers` in an admin terminal, checking the hosted-network line."
---

Windows' mobile hotspot turns your laptop into a WiFi router for your phone, tablet, or a friend's laptop — until it doesn't. The failure modes are specific: the hotspot toggle greys out, devices see the network but can't connect, or they connect and get no internet. Each points at a different layer: the wireless driver's hotspot capability, Windows' sharing service, or the bridge between your internet connection and the hotspot.

Diagnose the layer first, then fix it. The steps below do exactly that.

A useful mental model: the mobile hotspot is really two products glued together. The first is a virtual WiFi access point created by your wireless driver (the SoftAP), which is why driver capability matters so much. The second is Internet Connection Sharing, a mini-router inside Windows that bridges that access point to your real internet connection. Most hotspot failures are the glue between the two failing — the access point works but the bridge doesn't, or vice versa. That is why the fixes alternate between driver-level steps and sharing-level steps: you are repairing each half of the product and the joint between them. Keep a second device handy for testing, and test after every fix rather than batching them, so you know exactly which step did the job.

## Why this happens

- **Wireless driver lacks hosted-network support:** Generic or outdated drivers may not support the SoftAP mode hotspots need.
- **Airplane mode or radio off:** The hotspot needs the WiFi radio active even when sharing a wired connection.
- **Internet Connection Sharing (ICS) misconfigured:** The sharing bridge between your internet and the hotspot breaks.
- **VPN intercepting traffic:** VPN virtual adapters hijack the routing the hotspot depends on.
- **Firewall blocking the hotspot:** Overzealous firewall rules block DHCP or DNS on the hosted network.
- **IP address conflict:** The hotspot's default 192.168.137.x range collides with your main network.
- **Corrupted hosted-network state:** Stale virtual adapter configuration from previous hotspot sessions.
- **Power management disabling the adapter:** The wireless card sleeps mid-sharing and kills the hotspot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the laptop's own internet works

1. Disconnect the hotspot and confirm the **laptop itself** browses normally on its WiFi or Ethernet.
2. You can't share what you don't have — fix the laptop's connection first if it's down.
3. **Disconnect any VPN completely** — VPNs are the number-one hotspot killer.
4. Only proceed once the laptop has solid, VPN-free internet.

### Fix 2: Check hotspot capability

1. Open **Terminal as administrator** and run: `netsh wlan show drivers`
2. Look for **Hosted network supported: Yes** — if it says No, your current driver can't do hotspots.
3. If unsupported, update to the manufacturer's wireless driver (Fix 5) — capability often returns with the right driver.
4. Some USB WiFi adapters genuinely lack SoftAP support; built-in laptop adapters almost always have it with the correct driver.

### Fix 3: Toggle the hotspot cleanly

1. Go to **Settings → Network & internet → Mobile hotspot** and turn it **off**.
2. Change the **Share my internet connection from** dropdown to your active connection (WiFi or Ethernet).
3. Change the **band** to 2.4 GHz if devices struggle to see the 5 GHz hotspot.
4. Turn the hotspot back on and test with one device. A clean reconfiguration clears stale hosted-network state.

### Fix 4: Repair Internet Connection Sharing

1. Open **Control Panel → Network and Internet → Network Connections**.
2. Right-click your **internet source** adapter (the WiFi or Ethernet with internet) → **Properties → Sharing**.
3. Check **Allow other network users to connect through this computer's Internet connection** and select the hotspot adapter from the dropdown.
4. If the Sharing tab is missing, the **Internet Connection Sharing service** is disabled — start it in `services.msc` and set it to Automatic.

### Fix 5: Reinstall the wireless driver

1. In **Device Manager → Network adapters**, uninstall the wireless adapter with driver deletion checked.
2. Restart, then install the **manufacturer's wireless driver** for your exact model.
3. Re-run `netsh wlan show drivers` to confirm **Hosted network supported: Yes**.
4. The OEM driver restores the SoftAP capability that generic drivers often lack. For MediaTek-specific wireless repair, see our [MediaTek WiFi guide](/articles/best-way-to-fix-mediatek-wifi-not-working/).

### Fix 6: Check the firewall

1. Open **Windows Security → Firewall & network protection** and temporarily test with the firewall on a **private** network profile.
2. Look for third-party firewall or "internet security" suites and disable their network filtering temporarily.
3. The hotspot needs **DHCP and DNS** traffic between devices — aggressive firewalls block exactly this.
4. If disabling the firewall fixes it, add a proper exception rather than leaving protection off. The Windows 11-specific walkthrough is in our [hotspot on Windows 11 guide](/articles/how-to-fix-hotspot-not-working-on-laptop-on-windows-11/).

### Fix 7: Fix IP conflicts

1. If your main network also uses **192.168.137.x**, the hotspot's default range collides with it.
2. Change your **router's** LAN subnet (e.g., to 192.168.2.x) rather than fighting Windows' fixed hotspot range.
3. Alternatively, share a different source connection (Ethernet instead of WiFi) to sidestep the conflict.
4. After changing, restart the hotspot and reconnect devices fresh.

### Fix 8: Prevent the adapter from sleeping

1. In **Device Manager → wireless adapter → Power Management**, uncheck **Allow the computer to turn off this device to save power**.
2. Keep the laptop **plugged into AC power** while hosting — battery saver modes aggressively kill hotspots.
3. In **Settings → System → Power & battery**, set the power mode to **Best performance** during sharing.
4. A hotspot that dies after 10–20 minutes is almost always power management. For the general troubleshooting variant, see [hotspot troubleshooting](/articles/hotspot-not-working-on-laptop-troubleshooting/).

## Closing

Hotspot repair is a chain: the laptop's own internet, the driver's SoftAP capability, the sharing bridge, and the firewall. Verify each link in order and the weak one reveals itself quickly. The VPN check alone — disconnect it fully — resolves a remarkable number of "devices connect but no internet" cases before any real troubleshooting begins. Once the hotspot is stable, leave the sharing configuration alone: hotspot settings are one of those Windows features that works best when set once and never touched again, since every reconfiguration risks recreating the stale state you just cleared.
