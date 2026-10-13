---
title: "Mobile Hotspot Not Working on Your Laptop? Troubleshooting Guide"
slug: hotspot-not-working-on-laptop-troubleshooting
date: 2026-10-03
categories: ["drivers"]
tags: ["hotspot not working", "mobile hotspot windows 11", "can't turn on hotspot", "hotspot no internet", "wifi hotspot fix"]
description: "Can't turn on mobile hotspot, or devices connect but get no internet? Fix Windows laptop hotspot problems from the WiFi driver up through sharing settings."
thumbnail: "/images/thumbs/hotspot-not-working-on-laptop-troubleshooting.webp"
faqs:
  - q: "Why can't I turn on mobile hotspot on my Windows laptop?"
    a: "The most common reason is that the WiFi adapter's driver doesn't support the hosted network feature Windows needs for hotspot mode. Check by running netsh wlan show drivers in an elevated terminal and looking for Hosted network supported: Yes. If it says No, update the WiFi driver from your laptop manufacturer's site — the generic Windows driver often lacks hotspot support that the vendor driver includes."
  - q: "Devices connect to my hotspot but have no internet. What's wrong?"
    a: "This means the hotspot radio is working but internet sharing is broken. Open Settings > Network & internet > Mobile hotspot and confirm Share my internet connection from is set to the correct source (WiFi or Ethernet). Then check the sharing service: the Internet Connection Sharing service must be running. A network stack reset with netsh winsock reset followed by a restart fixes this in most cases."
  - q: "Why does my laptop hotspot keep turning off by itself?"
    a: "Windows has a power-saving feature that disables the hotspot when no devices are connected — check the Power saving toggle in the hotspot settings and turn it off. Also check the WiFi adapter's power management in Device Manager; if Windows is allowed to turn off the adapter to save power, the hotspot dies with it. Driver crashes can also kill it, so update the WiFi driver if it happens repeatedly."
  - q: "Does my WiFi adapter need to support anything special for hotspot?"
    a: "Yes — it needs hosted network (also called SoftAP) support in its driver. Most modern adapters have it, but the capability comes from the driver, not just the hardware. That's why a driver update can enable hotspot on an adapter where it previously failed. USB WiFi adapters vary widely: many cheap ones lack SoftAP support entirely, so check the specifications before buying one for hotspot duty."
---

Windows' mobile hotspot turns your laptop into a WiFi router — handy for sharing hotel Ethernet with your phone or getting a tablet online through your laptop's connection. When it breaks, it breaks in two distinct ways: the toggle won't turn on at all (a driver/capability problem), or devices connect but get no internet (a sharing/configuration problem). Each has its own fix path, and this guide covers both in order.

First, note how your laptop itself is online — WiFi or Ethernet — because hotspot shares that connection, and the sharing configuration differs slightly between the two.

A useful mental model: the hotspot feature has two halves that fail independently. The first half is the radio — the WiFi adapter creating a SoftAP network that devices can see and join. The second half is the sharing — Windows routing traffic between that hosted network and your real internet connection. "Can't turn on hotspot" is a radio-half failure (driver capability), while "devices connect but get no internet" is a sharing-half failure (configuration, services, VPN interference). Knowing which half is broken tells you which fixes below are relevant, so diagnose the symptom precisely before changing anything. A hotspot that will not turn on needs driver attention; one that turns on but shares nothing needs configuration attention — mixing up the two wastes real time.

Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official hotspot requirements if you want to confirm your setup qualifies.

## Why this happens

- **The WiFi driver lacks hosted-network (SoftAP) support**, the feature hotspot mode requires.
- **Internet Connection Sharing (ICS) service** is stopped or broken.
- **Wrong "share from" source** selected in hotspot settings.
- **Power saving** turning off the hotspot when idle or powering down the adapter.
- **Corrupted network stack** breaking the sharing path while the radio works.
- **Third-party VPN or firewall** intercepting and blocking shared traffic.
- **Airplane mode or WiFi turned off** — hotspot needs the WiFi radio on even when sharing Ethernet.
- **Outdated WiFi driver** with buggy SoftAP implementation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify hosted network support

Find out whether your adapter can do hotspot duty at all.

1. Open **Terminal (Admin)** and run: `netsh wlan show drivers`
2. Look for the line **Hosted network supported**. It must say **Yes**.
3. If it says **No**, update the WiFi driver from your laptop maker's support site — vendor drivers enable SoftAP where generic ones don't.
4. If it still says No after updating, your adapter genuinely lacks the feature; a USB WiFi adapter with SoftAP support is the workaround.

### Fix 2: Check the hotspot settings basics

The settings page has several gotchas.

1. Go to **Settings > Network & internet > Mobile hotspot**.
2. Set **Share my internet connection from** to the correct source — **WiFi** if the laptop is on WiFi, **Ethernet** if wired.
3. Set **Share over** to **WiFi** (not Bluetooth, which is painfully slow).
4. Turn off the **Power saving** toggle so Windows doesn't kill the hotspot when idle.
5. Click **Edit** on the network properties and set a simple SSID and password to rule out special-character issues.

### Fix 3: Toggle WiFi and restart the sharing stack

Clears the stuck states that block hotspot startup.

1. Turn the laptop's WiFi off and back on.
2. Toggle the hotspot off, wait 10 seconds, toggle it on.
3. If it still won't start, restart the laptop — hotspot failures often clear with a fresh boot because they involve driver-level state.

### Fix 4: Reset the network stack

Fixes the "connects but no internet" class of failures.

1. Open **Terminal (Admin)** and run:
   `netsh winsock reset`
   `netsh int ip reset`
   `ipconfig /flushdns`
2. Restart the laptop.
3. Reconfigure the hotspot (Fix 2) and test with a phone.

### Fix 5: Check the Internet Connection Sharing service

The background service that does the actual sharing.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Internet Connection Sharing (ICS)** — set **Startup type** to **Manual** (it starts on demand) and make sure it isn't **Disabled**.
3. Also verify **Windows Mobile Hotspot Service** is running if present.
4. Try starting the hotspot again.

### Fix 6: Disable VPN and check firewall

VPNs and firewalls love to break hotspot sharing.

1. Disconnect any VPN completely (not just pause — fully disconnect or quit the app).
2. In **Windows Security > Firewall & network protection**, temporarily test with the firewall off for the active profile.
3. If the hotspot works with the VPN/firewall off, add an exception or use split tunneling so hotspot traffic bypasses the VPN.
4. Re-enable protection after testing.

### Fix 7: Update or reinstall the WiFi driver

The driver owns the SoftAP feature.

1. Download the latest WiFi driver from your laptop maker's support site.
2. In Device Manager, uninstall the wireless adapter with driver deletion.
3. Install the fresh driver and restart.
4. Re-run `netsh wlan show drivers` to confirm **Hosted network supported: Yes**, then test the hotspot.

If the underlying WiFi itself is flaky, fix that first — see our [5GHz WiFi connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-11/) and [missing WiFi adapter guide](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/).

## Closing

Hotspot problems split cleanly: toggle won't turn on means driver capability (check hosted network support), connects-but-no-internet means sharing configuration (check the source selection and reset the stack). The `netsh wlan show drivers` check is the single most informative diagnostic — it tells you in one line whether the hardware/driver combination can even do hotspot duty. If your laptop's WiFi is solid but you need the reverse — getting the laptop online through your phone — USB tethering is more reliable than WiFi hotspot in most situations and worth trying as a fallback. And if the hotspot works but drops whenever the laptop sleeps, revisit the power management settings in Fix 3 and the adapter settings from our [5GHz WiFi guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-11/) — sleep-related radio shutdowns are the usual culprit there.
