---
title: "Fix a Mobile Hotspot That Won't Share on a Laptop"
slug: how-to-fix-hotspot-not-working-on-laptop-youtube
date: 2026-09-10
categories: ["drivers"]
tags: ["mobile hotspot", "tethering", "wifi sharing", "internet", "troubleshooting"]
description: "Laptop mobile hotspot not working? Fix hotspot that won't turn on, devices that can't connect, and no-internet errors step by step."
thumbnail: "/images/thumbs/how-to-fix-hotspot-not-working-on-laptop-youtube.webp"
faqs:
  - q: "Why won't my laptop's mobile hotspot turn on?"
    a: "The hotspot fails to start when the Wi-Fi adapter driver does not support hosted networks, the Internet Connection Sharing service is disabled, or airplane mode is on. Updating the Wi-Fi driver and enabling the ICS service resolves most startup failures."
  - q: "Why can devices see my hotspot but not connect?"
    a: "Visible-but-unjoinable hotspots usually have a corrupted hosted-network profile or a password mismatch. Forgetting the network on the connecting device, then turning the hotspot off and on with a fresh password, clears the stale profile. Avoid special characters in the new password during testing to rule out encoding issues."
  - q: "Why does my hotspot say 'no internet' on connected devices?"
    a: "The hotspot is broadcasting but not sharing the upstream connection. The ICS binding may be pointing at the wrong adapter, or the upstream connection itself is down. Re-selecting the shared connection in the adapter properties fixes the routing. The sharing tab lives in the properties of your upstream connection, not the hotspot adapter."
  - q: "Can antivirus or VPN software break the mobile hotspot?"
    a: "Yes. VPN clients reroute all traffic through a virtual adapter, which breaks the sharing path, and some firewalls block the DHCP traffic the hotspot needs. Disconnecting the VPN and adding a firewall exception for hotspot sharing usually restores it. Some VPN clients leave virtual adapters behind after disconnecting; disable those in Network Connections."
---

Your laptop is connected to the internet, you flip on the mobile hotspot to share it with your phone — and nothing works. The toggle may refuse to stay on, devices may fail to connect, or they connect and get no internet. It is a small feature with a surprising number of failure points.

Windows mobile hotspot depends on three cooperating pieces: a Wi-Fi adapter that supports hosted networks, the Internet Connection Sharing (ICS) service that routes traffic, and a clean network configuration. When any piece breaks — a driver update removing hosted-network support is the classic — the whole feature collapses.

These fixes cover all three failure modes: hotspot will not start, devices cannot join, and joined devices get no internet. Identify your symptom and work the matching fixes first, though the full sequence never hurts.

One design detail explains many hotspot headaches: the mobile hotspot shares your Wi-Fi radio, so the laptop cannot be connected to a Wi-Fi network and host clients on the same radio simultaneously in all configurations. If your upstream connection is Wi-Fi (not Ethernet or cellular), try switching the hotspot band or using a different upstream source — radio contention is a real, if poorly documented, failure mode.

## Why this happens

- **Wi-Fi driver lacking hosted network support:** Some driver versions drop the hosted-network capability the hotspot requires, and the toggle silently fails.
- **Internet Connection Sharing service disabled:** Without the ICS service running, Windows cannot route traffic between your connection and hotspot clients.
- **Airplane mode or Wi-Fi radio off:** The hotspot needs the Wi-Fi radio active; airplane mode kills the feature at the source.
- **VPN client hijacking the network path:** VPN virtual adapters intercept traffic and break the sharing route hotspot clients depend on.
- **Corrupted hosted network profile:** Stale SSID and password data can leave the hotspot broadcasting a profile devices cannot authenticate against.
- **Firewall blocking hotspot DHCP:** The hotspot runs a mini DHCP server; firewalls that block it leave clients with no IP address.
- **Upstream connection itself unstable:** If the laptop's own internet drops intermittently, hotspot clients experience it as 'no internet'.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Wi-Fi is on and airplane mode is off

The hotspot is built on the Wi-Fi radio. If the radio is off, nothing else in this guide can work.

1. Open **Settings > Network & internet** and confirm **Airplane mode** is off.
2. Ensure **Wi-Fi** is turned on, even if you are not connected to a Wi-Fi network.
3. Try enabling the hotspot at **Settings > Network & internet > Mobile hotspot**.
4. If the toggle immediately flips back off, continue to the driver fix.

### Fix 2: Update the Wi-Fi adapter driver

Hosted-network support lives in the Wi-Fi driver. The manufacturer's driver restores it when Windows' generic one drops it.

1. Open **Device Manager > Network adapters**, right-click your Wi-Fi adapter, and choose **Update driver**.
2. If that fails, download the latest Wi-Fi driver for your exact model from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) or your laptop vendor.
3. Install it, restart, and test the hotspot toggle.
4. Verify in an elevated Command Prompt with **netsh wlan show drivers** that **Hosted network supported** says **Yes**. If the Wi-Fi adapter itself has disappeared, fix that first with the [missing Wi-Fi guide](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 3: Restart the Internet Connection Sharing service

ICS is the routing engine behind the hotspot. When it is stopped, clients get nothing.

1. Press **Win + R**, type **services.msc**, and press Enter.
2. Find **Internet Connection Sharing (ICS)**, right-click, and choose **Restart**.
3. Set its **Startup type** to **Automatic**.
4. Toggle the mobile hotspot off and on, then test with your phone.

### Fix 4: Disconnect the VPN and check the firewall

VPNs and aggressive firewalls are the top software causes of 'connected but no internet' on hotspots.

1. Disconnect any VPN client completely — not just pause it.
2. Open your firewall settings and ensure hotspot and ICS traffic is allowed on private networks.
3. Temporarily disable third-party firewall software to test, then re-enable with an exception.
4. Reconnect a device and confirm internet works.

### Fix 5: Reset the hotspot configuration

A corrupted hotspot profile resists toggling. Wiping it forces a clean rebuild.

1. Turn the mobile hotspot **Off** in Settings.
2. In an elevated Command Prompt, run **netsh wlan stop hostednetwork** to clear any stuck state.
3. Change the hotspot **network name and password** to something new — this forces a fresh profile.
4. Turn the hotspot back on and join with the new credentials.

### Fix 6: Rebind Internet Connection Sharing to the right adapter

ICS sometimes shares the wrong connection, leaving hotspot clients routed nowhere.

1. Open **Control Panel > Network and Sharing Center > Change adapter settings**.
2. Right-click your active internet connection, choose **Properties > Sharing**.
3. Check **Allow other network users to connect through this computer's Internet connection**.
4. In the dropdown, select the hotspot's virtual adapter, click OK, and retest.

### Fix 7: Reset the network stack

When configuration corruption runs deep, a full reset rebuilds every network component including the hotspot path.

1. Open **Settings > Network & internet > Advanced network settings > Network reset**.
2. Confirm and restart when prompted.
3. Set up the hotspot fresh with a new name and password.
4. Reconnect your devices. If the adapter itself is missing, see the [missing adapter guide](/articles/how-to-fix-network-adapter-missing-on-windows-11/) first.

### Fix 8: Switch the hotspot network band

The default band can conflict with your environment. Switching bands sidesteps interference and radio-contention issues.

1. Open **Settings > Network & internet > Mobile hotspot** and expand the properties.
2. Change **Network band** from the default to the other option (**2.4 GHz** or **5 GHz**).
3. Update the connecting devices to join the new broadcast.
4. If one band works and the other does not, interference or radio contention was the cause.

## Closing

Mobile hotspot failures trace back to the Wi-Fi driver, the ICS service, or something hijacking the traffic path like a VPN. Get the hosted-network capability confirmed, the sharing service running, and the profile rebuilt, and the feature works reliably. It is plumbing, not magic — every piece is testable.
