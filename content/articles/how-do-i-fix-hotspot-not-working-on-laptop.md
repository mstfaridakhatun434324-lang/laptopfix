---
title: "How to Fix Mobile Hotspot Not Working on a Windows Laptop"
slug: how-do-i-fix-hotspot-not-working-on-laptop
date: 2026-09-22
categories: ["drivers"]
tags: ["mobile hotspot", "wifi hotspot", "internet sharing", "tethering", "network adapter"]
description: "Windows mobile hotspot turns on but devices can't connect — or it won't turn on at all? Step-by-step fixes for broken laptop hotspot sharing on Windows 11 and 10."
thumbnail: "/images/thumbs/how-do-i-fix-hotspot-not-working-on-laptop.webp"
faqs:
  - q: "Why does my hotspot turn on but no devices can connect?"
    a: "The hotspot toggle only starts the hosted network; devices still need a working DHCP assignment and a bridged internet connection to get online. If the hosted network runs but clients get no IP address or no internet, the usual culprits are a corrupted hosted-network driver, firewall rules blocking sharing, or the upstream connection not being shared properly."
  - q: "Can my Wi-Fi adapter be too old for mobile hotspot?"
    a: "Yes. The mobile hotspot feature needs an adapter that supports hosted networks. Very old adapters or outdated drivers report 'hosted network supported: no' in `netsh wlan show drivers`. Updating the wireless driver sometimes unlocks it, but genuinely old hardware may never support the feature — a USB Wi-Fi adapter is the practical workaround."
  - q: "Does mobile hotspot work over Ethernet or only Wi-Fi?"
    a: "It works with any upstream connection — Wi-Fi, Ethernet, or even USB tethering from a phone. In Settings > Network & internet > Mobile hotspot, the 'Share my internet connection from' dropdown selects the source. Sharing a wired Ethernet connection over Wi-Fi hotspot is a common and reliable setup."
  - q: "Why does my hotspot keep turning itself off?"
    a: "Windows has a power-saving option that disables the hotspot when no devices are connected — check the hotspot settings page for that toggle. Beyond that, aggressive Wi-Fi adapter power management can kill the hosted network; disabling 'allow the computer to turn off this device to save power' on the adapter usually stops the dropouts."
---

Windows' mobile hotspot turns your laptop into a Wi-Fi router for your phone, tablet, or a friend's device. When it works, it's invisible magic. When it doesn't, the failure modes are confusing: the toggle flips on but nothing can connect, devices connect but get no internet, or the hotspot dies the moment a device joins. Each symptom points at a different layer — the hosted network driver, the sharing configuration, or power management.

This guide covers all three layers in the order a technician checks them. It assumes your laptop's own internet connection works fine; if the laptop itself can't get online, fix that first — a hotspot can't share what the laptop doesn't have. For the related case where the Wi-Fi adapter itself is misbehaving, see our [Wi-Fi adapter troubleshooting guide](/articles/what-to-do-if-wifi-adapter-not-showing-up/).

## Why this happens

- **The wireless adapter doesn't support hosted networks.** Old hardware or outdated drivers can't create the virtual access point at all.
- **The hosted network driver is corrupted.** The Microsoft Hosted Network Virtual Adapter fails to start even though the toggle flips.
- **Internet Connection Sharing is misconfigured.** The upstream connection isn't actually shared with the hotspot network.
- **Firewall or antivirus blocks the sharing.** Third-party security software can silently block the NAT/DHCP traffic the hotspot needs.
- **Power management kills the adapter.** Windows powers down the Wi-Fi card to save battery, collapsing the hotspot.
- **The 5 GHz/2.4 GHz band setting conflicts.** Some client devices can't see a hotspot broadcasting on an incompatible band.
- **Corrupted network stack.** Winsock or TCP/IP corruption breaks the sharing path even with correct settings.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify hosted network support

Confirm the hardware can actually do this before changing settings.

1. Open an elevated Command Prompt and run `netsh wlan show drivers`.
2. Look for the line **Hosted network supported** — it must say **Yes**.
3. If it says No, update your wireless driver from the manufacturer's site or [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html), then re-check.
4. If it still says No after a driver update, the adapter genuinely lacks support — use a USB Wi-Fi adapter that supports hosted networks.

This one command prevents hours of wasted settings-tweaking on hardware that can never host. Note it in your troubleshooting log and move on to a hardware workaround rather than fighting it.

### Fix 2: Reset the hotspot configuration

Stale hotspot settings — wrong band, corrupted password, half-applied sharing — cause the "on but unusable" state.

1. Open **Settings > Network & internet > Mobile hotspot** and turn the hotspot **Off**.
2. Change **Share my internet connection over** to **Wi-Fi**, and set **Band** to **2.4 GHz** for maximum client compatibility.
3. Click **Edit** under network properties, set a fresh network name and a strong password, and save.
4. Turn the hotspot back on and try connecting a device.

The 2.4 GHz recommendation is deliberate: some older phones and IoT devices can't see 5 GHz hotspots at all. Start with the compatible band, confirm it works, then experiment with 5 GHz if you need the speed.

### Fix 3: Rebuild the hosted network adapter

When the virtual adapter itself is broken, Device Manager surgery fixes it.

1. Open **Device Manager** and click **View > Show hidden devices**.
2. Expand **Network adapters** and find **Microsoft Hosted Network Virtual Adapter** (or **Microsoft Wi-Fi Direct Virtual Adapter**).
3. Right-click it, choose **Disable device**, wait 10 seconds, then **Enable device**.
4. If it's missing entirely, click **Action > Scan for hardware changes** to force re-detection.

The virtual adapter is created on demand, so disabling and re-enabling it forces Windows to rebuild its configuration from scratch. If the adapter shows a yellow warning, uninstall it and scan for hardware changes instead — Windows recreates it cleanly.

### Fix 4: Check Internet Connection Sharing settings

The hotspot broadcasts; sharing is what gives clients internet. Verify the upstream connection is actually shared.

1. Open **Control Panel > Network and Internet > Network Connections**.
2. Right-click your active internet connection (Wi-Fi or Ethernet) and choose **Properties > Sharing**.
3. Check **Allow other network users to connect through this computer's Internet connection**.
4. In the dropdown, select the hotspot's network connection (often named "Local Area Connection* 10" or similar) and click OK.

If the Sharing tab is missing, the connection doesn't support sharing (some VPN or metered setups block it) — disconnect the VPN and retry. This setting is the classic cause of "devices connect to the hotspot but have no internet."

### Fix 5: Temporarily disable firewall and antivirus filtering

Security software can block the DHCP and NAT traffic that makes a hotspot usable, with no visible warning.

1. Temporarily disable your third-party antivirus firewall (keep Windows Defender on) and test the hotspot.
2. If it works, open the antivirus firewall settings and allow the hotspot/virtual adapter network as trusted.
3. Check **Windows Defender Firewall > Allow an app** to confirm no hotspot-related blocks.
4. Re-enable your antivirus firewall after adding the exception — don't leave protection off.

If you'd rather not touch the firewall, test with Windows' built-in firewall only for five minutes. The goal is diagnosis: if the hotspot springs to life, you've found your culprit and can craft a precise exception.

### Fix 6: Disable adapter power management

Power-saving features love to kill hotspots, especially on battery.

1. In **Device Manager > Network adapters**, right-click your Wi-Fi adapter and choose **Properties > Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Go to **Settings > System > Power & battery** and set the power mode to **Best performance** while testing.
4. In the hotspot settings, disable **Power saving — turn off mobile hotspot automatically when no devices are connected** if you want it to stay up.

Also check your manufacturer's power utility (Dell Power Manager, Lenovo Vantage) — these can impose their own adapter power policies that override Windows settings. For broader adapter issues, our [network adapter missing guide](/articles/how-to-fix-network-adapter-missing-reddit/) covers deeper driver recovery.

### Fix 7: Reset the network stack and recreate sharing

When nothing else explains it, wipe the network configuration and start clean.

1. Open **Settings > Network & internet > Advanced network settings > Network reset** and click **Reset now**.
2. After the restart, reconfigure the hotspot from scratch (Fix 2's steps).
3. Re-apply the Internet Connection Sharing setting (Fix 4), since the reset clears it.
4. Test with one device before re-adding VPNs, custom DNS, or other network customizations.

A network reset removes saved Wi-Fi networks and VPN profiles, so export anything important first. It's the definitive "clean slate" — if the hotspot works after this, some corrupted setting was the cause, and rebuilding incrementally will keep it working.

## Closing

Hotspot failures are sharing failures more often than Wi-Fi failures: the radio works, but the hosted network, the sharing bridge, or power management breaks the chain. Work the layers in order — capability, configuration, virtual adapter, sharing, firewall, power — and the break reveals itself. Once it's up, leave the band on 2.4 GHz unless you have a reason to change it; compatibility beats speed for a hotspot.
