---
title: "How to Fix Mobile Hotspot Not Working on a Laptop in Windows 10"
slug: how-to-fix-hotspot-not-working-on-laptop-on-windows-10
date: 2026-10-09
categories: ["drivers"]
tags: ["mobile hotspot", "windows 10", "hotspot not working", "wifi sharing"]
description: "Windows 10 mobile hotspot won't turn on or devices can't connect? Fix driver, service, and adapter issues step by step."
thumbnail: "/images/thumbs/how-to-fix-hotspot-not-working-on-laptop-on-windows-10.webp"
faqs:
  - q: "Why does my Windows 10 hotspot say 'We can't set up mobile hotspot'?"
    a: "That error means the hosted network capability failed to initialize, almost always because the WiFi driver does not support hosted networks, the Microsoft Hosted Network Virtual Adapter is broken, or the Internet Connection Sharing service is disabled. Updating the WiFi driver and restarting the ICS service resolves it in most cases."
  - q: "Do I need a special WiFi adapter for hotspot to work?"
    a: "The adapter must support hosted networks, which nearly all modern laptop WiFi cards do. You can verify with the command netsh wlan show drivers — look for Hosted network supported: Yes. If it says No, the driver is the problem, not the hardware; install the manufacturer's driver."
  - q: "Why do devices connect to my hotspot but get no internet?"
    a: "Connected-but-no-internet means the hotspot radio works but traffic is not being routed. The usual causes are the ICS service failing, the wrong network selected in Share my Internet connection from, firewall rules blocking the hosted network, or a VPN capturing all traffic. Check the sharing source selection first."
  - q: "Can antivirus or VPN software break the Windows 10 hotspot?"
    a: "Yes, frequently. VPN clients reroute all traffic through their tunnel and often break ICS routing, while some firewalls block the hosted network adapter outright. Temporarily disable both to test — if the hotspot works, re-enable them and configure exceptions for the hosted network."
---

Windows 10's mobile hotspot is convenient right up until it refuses to turn on, throws "we can't set up mobile hotspot," or lets devices connect with no internet access. The feature depends on a small chain — WiFi driver hosted-network support, the virtual adapter, Internet Connection Sharing, and the firewall — and any broken link kills the whole feature. The error messages are vague, but the diagnostic path is not.

Start by classifying your failure: hotspot toggle won't stay on, toggle works but devices can't find the network, or devices connect but get no internet. Each maps to a different layer, and the fixes below follow that mapping.
Windows 10's hotspot looks simple in Settings, but underneath it's a clever trick: your WiFi card pretends to be an access point using a virtual adapter, while Internet Connection Sharing routes traffic between your real connection and that virtual network. Understanding that two-adapter dance explains every failure mode — "can't set up" means the virtual side failed, "no internet" means the routing side failed.

## Why this happens

- **WiFi driver lacks hosted network support:** Generic or outdated drivers report "Hosted network supported: No," and the feature cannot initialize.
- **Microsoft Hosted Network Virtual Adapter broken:** The virtual adapter is disabled, corrupted, or missing from Device Manager.
- **Internet Connection Sharing service disabled:** The ICS service (SharedAccess) is stopped or set to manual, so no routing happens.
- **Wrong sharing source selected:** The hotspot shares from a disconnected or wrong adapter instead of the active internet connection.
- **Firewall blocking the hosted network:** Windows Firewall or third-party security software blocks traffic on the virtual adapter.
- **VPN capturing traffic:** Active VPN clients reroute everything through the tunnel, starving the hotspot of a route.
- **Bluetooth interfering:** On some adapters, Bluetooth coexistence bugs break hosted mode until Bluetooth is toggled off.
- **Power management on the WiFi card:** The adapter sleeps the moment hotspot mode engages, collapsing the hosted network.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify hosted network support

1. Open **Command Prompt** and run `netsh wlan show drivers`.
2. Find the line **Hosted network supported** — it must say **Yes**.
3. If it says **No**, update the WiFi driver from your laptop maker's support site (not Windows Update's generic pick).
4. Re-run the command after the driver update. Hardware from the last decade supports this; a "No" is a driver problem, not a hardware limit. See our [Intel AX201 driver guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-on-windows-10/) for the clean-reinstall method.
5. If hosted networks are supported but the hotspot still fails, compare with the general [hotspot troubleshooting reference](/articles/hotspot-not-working-on-laptop-troubleshooting/) — it covers adapter-level issues that affect hosted mode regardless of the hosted-network flag.

### Fix 2: Repair the virtual hosted network adapter

1. Open **Device Manager → View → Show hidden devices** and expand **Network adapters**.
2. Look for **Microsoft Hosted Network Virtual Adapter** — if disabled, right-click → **Enable device**.
3. If it is missing, right-click the WiFi adapter → **Disable**, wait ten seconds, **Enable** — this often regenerates the virtual adapter.
4. If still missing, uninstall the WiFi adapter (with driver removal) and reinstall the manufacturer's driver, which rebuilds the virtual adapter cleanly.

### Fix 3: Restart Internet Connection Sharing

1. Press **Win + R**, type `services.msc`, and find **Internet Connection Sharing (ICS)**.
2. Set **Startup type** to **Automatic**, then click **Start** (or **Restart**).
3. Also verify **Windows Firewall** and **Base Filtering Engine** services are running — ICS depends on them.
4. Toggle the hotspot off and on in **Settings → Network & Internet → Mobile hotspot** and test.
5. If ICS starts but clients still get no internet, open the hosted adapter's **Properties → Sharing** tab in `ncpa.cpl` and verify **Allow other network users to connect** is ticked with the correct home networking connection selected — this legacy setting still governs the routing on some Windows 10 builds.

### Fix 4: Set the correct sharing source

1. In **Mobile hotspot** settings, check **Share my Internet connection from** — it must be your active connection (WiFi or Ethernet), not a disconnected adapter.
2. Set **Share over** to **WiFi** (not Bluetooth) for normal use.
3. Click **Edit** and set a simple network name and a strong password — special characters in the SSID occasionally cause client issues.
4. Turn the hotspot off and on again after changing any of these.

### Fix 5: Check firewall and disable VPN temporarily

1. In **Windows Defender Firewall → Allow an app**, ensure hotspot-related entries are not blocked; as a test, briefly turn the firewall off for the private network.
2. Disconnect any VPN client completely (not just paused) and test the hotspot.
3. If the VPN is the cause, look in its settings for split tunneling or local-network sharing options.
4. Third-party antivirus with its own firewall: add an exception for the hosted network or test with it disabled.
5. For persistent firewall mysteries, [Microsoft's mobile hotspot documentation](https://support.microsoft.com/en-us/windows) lists the exact firewall and service dependencies the feature requires.

### Fix 6: Reset the network stack and hotspot configuration

1. Open **Command Prompt as administrator** and run `netsh winsock reset` and `netsh int ip reset`.
2. Run `netsh wlan set hostednetwork mode=disallow` followed by `netsh wlan set hostednetwork mode=allow` to reset the hosted network state.
3. Go to **Settings → Network & Internet → Status → Network reset** as a deeper option — note it clears saved WiFi passwords.
4. Restart and reconfigure the hotspot from scratch.

### Fix 7: Disable power management and Bluetooth coexistence

1. In Device Manager, open the WiFi adapter's **Properties → Power Management** and uncheck power saving.
2. Turn **Bluetooth off** in Settings while testing — on some Realtek and Intel cards, Bluetooth coexistence breaks hosted mode.
3. In the adapter's **Advanced** tab, look for **802.11 mode** or **Preferred band** and try 2.4 GHz-only — some clients connect more reliably to 2.4 GHz hotspots.
4. If the hotspot now works, re-enable Bluetooth afterward and confirm stability; the toggle was diagnostic.
5. Once stable, save the working configuration: note the driver version, band setting, and sharing source. Hotspot settings drift across Windows updates, and a written record turns the next failure into a two-minute restore.

## Closing

Windows 10 hotspot failures are a chain problem: driver hosted-network support, the virtual adapter, the ICS service, the sharing source, and the firewall each get a vote. The `netsh wlan show drivers` check at the start tells you in seconds whether the driver is even capable, which prevents an hour of fiddling with settings on a broken foundation. Once working, leave the manufacturer's WiFi driver in place and Windows Update away from it.
