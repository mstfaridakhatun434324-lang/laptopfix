---
title: "How to Fix Copilot Not Working When Your VPN Is On"
slug: copilot-not-working-with-vpn
date: 2026-10-21
categories: ["ai-pc"]
tags: ["copilot vpn", "copilot not working with vpn", "split tunneling", "windows 11", "ai pc", "dns"]
description: "Copilot goes dead the moment your VPN connects? Fix Copilot with a VPN on using six methods: split tunneling, DNS repair, protocol swaps, and firewall rules."
thumbnail: "/images/thumbs/copilot-not-working-with-vpn.webp"
faqs:
  - q: "Why does Copilot stop working when I turn on my VPN?"
    a: "Copilot needs Microsoft's cloud endpoints, and VPNs change your route, DNS, and apparent location. Blocked endpoints, slow DNS through the tunnel, region mismatches, or aggressive VPN kill-switches can each silently break Copilot's connection."
  - q: "Is split tunneling safe for Copilot?"
    a: "Split tunneling only lets the chosen app bypass the tunnel; everything else stays protected. Routing just Copilot outside the VPN is a common, safe workaround when the tunnel breaks its endpoints — though check your organization's policy if the PC is work-managed."
  - q: "Does my VPN server location matter?"
    a: "Yes. Connecting through a country where Copilot availability differs, or where Microsoft routes you to a distant datacenter, causes timeouts and sign-in loops. Try a server in your own region first."
  - q: "Will changing VPN protocols fix it?"
    a: "Often. Some protocols (or restrictive networks) block the ports Copilot uses. Switching from OpenVPN to WireGuard, or vice versa, frequently restores the connection without any other changes."
---

Copilot works fine on your home Wi-Fi. You connect the VPN, and Copilot goes silent — no responses, endless loading, or sign-in errors. Disconnect the VPN, and it is alive again.

This is a network-path problem, not a Copilot problem. Copilot reaches Microsoft's cloud endpoints through specific domains and ports; a VPN reroutes all of that through its tunnel, swaps your DNS, and changes your apparent location. Any one of those changes can break the connection while everything else keeps working.

These six fixes start with quick confirmations and work toward routing changes: VPN-off test, server and protocol swaps, DNS repair, split tunneling, and firewall rules. Work through them in order.

## Why this happens

- **Blocked Microsoft endpoints**: Some VPN exit nodes, corporate profiles, or strict VPN firewalls block the domains or ports Copilot needs to reach Microsoft's AI services.
- **Slow or hijacked DNS through the tunnel**: The VPN's DNS resolver may be slow, leak, or return wrong results for Microsoft domains, so Copilot cannot resolve its endpoints.
- **Region mismatch**: Your account region and the VPN exit country disagree, triggering Microsoft's regional checks, sign-in loops, or throttled responses — the same [region availability error](/articles/copilot-not-available-in-my-region/) users outside supported regions see every day.
- **Kill-switch overreach**: The VPN's kill switch can block traffic it mistakes for leaks — including Copilot's WebView2 network calls — dropping its connection silently.
- **MTU or protocol breakage**: Certain protocols fragment or drop the long-lived connections Copilot holds open, causing responses that start and then die mid-stream.
- **IPv6 conflicts**: Copilot prefers certain routes while the VPN handles IPv6 poorly; the mismatch produces partial connectivity that looks like Copilot is simply ignoring you.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the VPN is the cause and try a nearby server

First prove it is the VPN, then rule out a bad exit node — many "Copilot + VPN" problems are just one overloaded server.

1. Disconnect the VPN entirely and confirm Copilot responds normally — this establishes the baseline.
2. Reconnect the VPN to a server in **your own city or country**.
3. Test Copilot with a simple prompt. If it works, the previous exit node was the problem.
4. If Copilot still fails on a nearby server, continue — the tunnel itself is interfering. Copilot failing even with the VPN off points elsewhere; see the [Copilot not responding guide](/articles/copilot-not-responding/).

### Fix 2: Switch your VPN protocol

Protocols handle Microsoft's traffic differently. WireGuard, OpenVPN (UDP/TCP), and IKEv2 each take different paths through networks and firewalls.

1. Open your VPN app's settings and find the **Protocol** option (often under Connection or Advanced).
2. Switch to a different protocol — if you are on OpenVPN, try **WireGuard**; if on WireGuard, try **OpenVPN (UDP)**.
3. Reconnect and test Copilot.
4. If one protocol works, keep it. Some hotel or campus networks throttle specific protocols, so what works can vary by location.

### Fix 3: Flush DNS and set reliable resolvers

Stale or broken DNS inside the tunnel is a classic cause of Copilot connecting to the wrong Microsoft datacenter — or none at all.

1. Right-click Start, open **Terminal (Admin)**, and run `ipconfig /flushdns`.
2. Run `ipconfig /registerdns` to re-register your connection.
3. In **Settings > Network & internet**, open your adapter's DNS settings and set **1.1.1.1** and **1.0.0.1** (Cloudflare) or **8.8.8.8** and **8.8.4.4** (Google).
4. Reconnect the VPN and test Copilot. Microsoft's Windows networking docs at [Microsoft Support](https://support.microsoft.com/en-us/windows) cover DNS basics if your VPN overrides these settings.

### Fix 4: Use split tunneling for Copilot

Split tunneling lets Copilot talk directly to Microsoft while the rest of your traffic stays in the tunnel — the most reliable long-term fix. It is also the only fix that keeps working when you switch VPN servers daily, since the exclusion follows the app rather than the network.

1. Open your VPN app's settings and find **Split tunneling** (also called per-app settings or bypass).
2. Enable it and add **Microsoft Copilot** to the list of apps that bypass the VPN.
3. Some VPNs need the WebView2 process too — add **msedgewebview2.exe** if Copilot still stalls.
4. Reconnect the VPN and confirm Copilot answers promptly. On work-managed PCs, check with IT first, since some organizations forbid split tunneling.

### Fix 5: Check the VPN kill switch and firewall rules

Kill switches and custom firewall rules can block Copilot's traffic while looking like normal protection.

1. Temporarily **disable the kill switch** in your VPN settings, reconnect, and test Copilot.
2. If Copilot works, re-enable the kill switch but add Copilot (and WebView2) to its **allowlist/exceptions**.
3. Open **Windows Security > Firewall & network protection > Allow an app through firewall** and make sure Copilot is allowed on Private and Public networks.
4. Test again with the kill switch on. Display or power quirks sometimes ride along with network weirdness on ARM machines — the [fast startup issues guide for ARM laptops](/articles/fast-startup-issues-arm-laptop/) is worth a look if boot behavior changed too.

### Fix 6: Reinstall Copilot and reset network stacks

When the VPN has corrupted Copilot's cached connection state, a clean slate plus fresh network stacks clears it.

1. Uninstall Copilot from Settings > Apps > Installed apps, then restart.
2. In an admin terminal, run `netsh winsock reset` and `netsh int ip reset`, then restart again.
3. Reinstall Copilot from the Microsoft Store and sign in with the VPN **off**.
4. Reconnect the VPN and test. If Copilot only breaks after the machine sleeps or updates firmware, a missing NPU can produce eerily similar symptoms — rule that out with the [NPU missing after BIOS update guide](/articles/npu-missing-after-bios-update/).

## Closing

Copilot and VPNs clash because the VPN changes every assumption Copilot makes about its network: the route, the DNS, and the location. A nearby server, a protocol swap, or split tunneling resolves nearly every case — start simple and only change one thing at a time. Keep Copilot on the bypass list once you find the combination that works. If you travel often, save two favorite servers — one nearby for speed and one in your home region for services that check location — so Copilot keeps working wherever you connect.
