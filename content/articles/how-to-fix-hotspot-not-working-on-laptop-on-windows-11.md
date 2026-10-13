---
title: "How to Fix Mobile Hotspot Not Working on a Laptop in Windows 11"
slug: how-to-fix-hotspot-not-working-on-laptop-on-windows-11
date: 2026-09-03
categories: ["drivers"]
tags: ["mobile hotspot", "windows 11", "hotspot fix", "internet sharing"]
description: "Windows 11 hotspot won't start or shares no internet? Fix driver, ICS, and band settings to get mobile hotspot working."
thumbnail: "/images/thumbs/how-to-fix-hotspot-not-working-on-laptop-on-windows-11.webp"
faqs:
  - q: "Why won't the Windows 11 mobile hotspot toggle stay on?"
    a: "A toggle that flips back off means the hosted network failed to initialize — usually a WiFi driver without hosted-network support, a broken virtual adapter, or the Internet Connection Sharing service not running. Update the WiFi driver from the laptop maker and restart the ICS service; those two cover most cases."
  - q: "Is the Windows 11 hotspot different from Windows 10's?"
    a: "Functionally similar, but Windows 11 changed the settings layout and tightened driver requirements. The netsh hostednetwork commands still work underneath, and the same chain — driver, virtual adapter, ICS service, firewall — determines success on both. Fixes transfer directly between versions."
  - q: "Why is my Windows 11 hotspot so slow?"
    a: "Hotspot speed is limited by your laptop's upstream connection first — the hotspot cannot share more bandwidth than the laptop receives. Beyond that, 2.4 GHz band selection, an overloaded channel, power-saving on the WiFi card, and VPN overhead all cut speed. Switch to 5 GHz and disable power saving for the best throughput."
  - q: "Can I share a VPN connection over the Windows 11 hotspot?"
    a: "Sometimes, but VPN clients frequently break ICS routing — connected devices get no internet while the laptop itself works through the VPN. Test with the VPN disconnected first to isolate the issue. Some VPNs offer hotspot-compatible modes or split tunneling that restores sharing."
---

Windows 11's mobile hotspot fails in the same three ways as its predecessor: the toggle won't stay on, devices can't see the network, or devices connect with no internet. The underlying machinery — WiFi driver hosted-network support, the virtual adapter, Internet Connection Sharing, firewall — is identical in concept to Windows 10, so the diagnostic approach transfers directly. What changed is the settings layout and stricter driver behavior.

Classify your failure before touching anything: toggle behavior points at driver/service initialization, invisible network points at the virtual adapter or band settings, and connected-but-no-internet points at ICS routing and firewall. Each has its own fix below.
Windows 11 moved the hotspot settings and renamed a few things, but the machinery underneath is the same two-adapter trick as Windows 10: your WiFi card emulates an access point through a virtual adapter while Internet Connection Sharing routes traffic to your real connection. "Toggle won't stay on" means the virtual side failed; "connected, no internet" means the routing side failed. Diagnose which half broke before touching settings.

## Why this happens

- **WiFi driver without hosted support:** Outdated or generic drivers report no hosted-network capability, killing initialization.
- **Virtual adapter broken:** The Microsoft Wi-Fi Direct Virtual Adapter is disabled or corrupted.
- **ICS service not running:** Internet Connection Sharing fails to start or is disabled.
- **Wrong sharing source:** The hotspot shares from an inactive adapter instead of the live internet connection.
- **Firewall blocking clients:** Defender or third-party firewalls block the hosted network's traffic.
- **VPN rerouting:** Active VPN tunnels capture traffic and break ICS routing for clients.
- **Band mismatch:** 5 GHz-only hotspot with 2.4 GHz-only client devices, or congested 2.4 GHz channels.
- **Power saving on the WiFi card:** The adapter sleeps under hotspot load, collapsing the network.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm hosted-network capability

1. Open **Terminal** and run `netsh wlan show drivers`.
2. Verify **Hosted network supported: Yes** — a **No** means the driver is the problem, not settings.
3. Update the WiFi driver from your laptop maker's support site if it says No, then re-run the command.
4. Modern cards support this universally; treat "No" as a driver defect to fix, never as a hardware limit.
5. If the command itself errors out, the WLAN AutoConfig service isn't running — start it in `services.msc` and retry. A stopped WLAN service breaks both the check and the hotspot, and it's a two-click fix.

### Fix 2: Repair the virtual adapter

1. Open **Device Manager → View → Show hidden devices → Network adapters**.
2. Find **Microsoft Wi-Fi Direct Virtual Adapter** — enable it if disabled.
3. If missing or error-flagged, disable and re-enable the physical WiFi adapter to regenerate it.
4. As a deeper rebuild, uninstall the WiFi adapter with driver deletion and reinstall the manufacturer's driver package. This mirrors the virtual-adapter repair in our [Windows 10 hotspot guide](/articles/how-to-fix-hotspot-not-working-on-laptop-on-windows-10/).
5. The general [hotspot troubleshooting reference](/articles/hotspot-not-working-on-laptop-troubleshooting/) covers adapter-level hosted-mode issues that persist across both Windows versions — useful when the Windows 11-specific steps stall.

### Fix 3: Restart ICS and its dependencies

1. Open `services.msc` and set **Internet Connection Sharing (ICS)** to **Automatic**, then **Start** it.
2. Confirm **Windows Firewall**, **Base Filtering Engine**, and **Network Connections** services are running.
3. Toggle the hotspot off and on in **Settings → Network & internet → Mobile hotspot**.
4. If ICS refuses to start, check the System event log for its error code — dependency failures show up there explicitly.

### Fix 4: Set sharing source and band correctly

1. In Mobile hotspot settings, set **Share my internet connection from** to your active connection (the one actually online).
2. Set **Share over** to **WiFi**, then open **Properties → Edit** if available to choose the network band.
3. Try **5 GHz** for speed with modern devices, or **2.4 GHz** for maximum compatibility with older clients and IoT gadgets.
4. Use a simple SSID and strong password — avoid special characters that confuse some clients.
5. After changing band settings, forget the hotspot network on your client devices and rejoin fresh — clients cache the old band and channel information, and a stale cache produces "can't connect" errors on a hotspot that's actually working fine.

### Fix 5: Rule out firewall and VPN interference

1. Temporarily disconnect any VPN entirely and test — VPNs are the top cause of connected-but-no-internet hotspots.
2. In **Windows Security → Firewall**, verify the private network firewall is not blocking the hosted adapter; test briefly with it off.
3. Third-party security suites: look for a "WiFi hotspot" or "internet sharing" exception to enable.
4. If the VPN is essential, explore its split-tunneling or hotspot-sharing options rather than fighting ICS.
5. [Microsoft's hotspot support page](https://support.microsoft.com/en-us/windows) documents the current Windows 11 hotspot requirements, including which adapter features the feature depends on.

### Fix 6: Reset network components

1. In an admin terminal, run `netsh winsock reset` and `netsh int ip reset`, then restart.
2. Use **Settings → Network & internet → Advanced network settings → Network reset** for the full reset (clears saved WiFi passwords).
3. Reconfigure the hotspot from scratch after the reset — do not assume old settings survived.
4. Reconnect your own WiFi first and confirm the laptop itself is online before enabling the hotspot.

### Fix 7: Stabilize power and test client-side

1. In Device Manager, disable power management on the WiFi adapter (**Properties → Power Management** → uncheck).
2. Set **Wireless Adapter Settings → Power Saving Mode** to **Maximum Performance** in Power Options.
3. Test with a second client device — if one phone connects fine and another doesn't, the failing client is the problem (forget the network on it and rejoin).
4. Keep the laptop plugged in while hosting — battery-saver modes throttle the radio and collapse hotspot throughput.
5. If you host regularly, consider a dedicated travel router instead — it offloads the AP duty from your laptop's WiFi card entirely, runs cooler, and sidesteps every driver quirk in this guide. The Windows hotspot is best treated as a backup, not infrastructure.

## Closing

Windows 11 hotspot repair follows the same chain as Windows 10: driver capability, virtual adapter, ICS service, sharing source, firewall. The `netsh wlan show drivers` check up front prevents wasted effort, and the VPN test resolves the most common connected-but-no-internet complaint in one step. Once stable, leave the manufacturer's WiFi driver alone — Windows Update's generic replacements are how most hotspot breakages begin.
