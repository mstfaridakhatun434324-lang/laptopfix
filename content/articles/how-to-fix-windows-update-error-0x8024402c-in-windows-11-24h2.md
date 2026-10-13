---
title: "How to Fix Windows Update Error 0x8024402C in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x8024402c-in-windows-11-24h2
date: 2026-10-05
categories: ["windows-update"]
tags: ["windows update", "0x8024402c", "error code", "windows 11", "proxy"]
description: "Error 0x8024402C means Windows Update cannot resolve or reach the update servers. Fix the proxy, DNS, and firewall with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x8024402c-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x8024402C mean?"
    a: "WU_E_PT_WINHTTP_NAME_NOT_FOUND: the WinHTTP layer could not resolve or connect to the update server's hostname. Windows never even starts talking to Microsoft — the connection dies at the addressing stage, which points squarely at proxy, DNS, or firewall trouble rather than a broken update."
  - q: "Why does my browser work but Windows Update doesn't?"
    a: "Windows Update consults the system WinHTTP proxy, which lives separately from the browser proxy settings most people check. Your browser can be perfectly configured while the system-level proxy points update traffic into a dead end. That split is exactly why this code confuses people."
  - q: "How do I reset the WinHTTP proxy?"
    a: "Open an administrator Command Prompt and run netsh winhttp reset proxy. This clears the system-level proxy configuration that only background services use — including the stale entries VPN clients leave behind. Your browser proxy settings are untouched."
  - q: "Can the system clock really break updates?"
    a: "Yes. TLS certificate validation depends on the clock, and a clock too far off makes every HTTPS connection to Microsoft fail. Open Settings > Time & language > Date & time, enable Set time automatically, and click Sync now. Two quick checks — firewall and clock — resolve a surprising number of instant-failure cases."
---

Your browser loads websites fine. Your apps sync. But Windows Update insists it cannot reach its servers. That paradox defines 0x8024402C: the WinHTTP layer — Windows Update's own plumbing, distinct from the browser's — fails to resolve or reach the update server's hostname.

The official designation: WU_E_PT_WINHTTP_NAME_NOT_FOUND. Windows does not even begin conversing with Microsoft — the connection perishes at the addressing stage. With 24H2 laptops, suspicion usually falls on an outdated proxy configuration, a VPN client that abandoned its settings, or a firewall obstructing the update components.

The split between browser networking and WinHTTP networking is the key insight. Everything below targets the system-level path only — your browser configuration is irrelevant here, so resist the urge to tweak browser proxy settings. A working browser proves the internet is fine — the fault lies in the update-specific connection path. That single observation narrows the suspect list to proxy, DNS, firewall, and clock.

## Why this happens

- **Proxy stale or misconfigured.** Residual configuration from a VPN client, office network, or campus Wi-Fi routes update traffic into a dead end.
- **WinHTTP proxy store corrupted.** The system-level proxy setup may contain invalid entries used solely by background services.
- **DNS fails to resolve Microsoft's hostnames.** Bad DNS servers or a poisoned resolver cache break name resolution.
- **Firewall obstructing update components.** Third-party firewalls occasionally block svchost-hosted update traffic following a rules update.
- **The system clock is too far off.** TLS validation fails when the clock drifts, killing every HTTPS connection.
- **A captive portal intercepts traffic.** Hotel and campus Wi-Fi login pages grab the connection before authentication.
- **The hosts file has stale entries.** Rare, but manual hosts edits can redirect update hostnames nowhere. If you ever edited the hosts file for ad-blocking, review those lines — a stale Microsoft entry there defeats everything else in this guide.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Ascertain the PC reaches the internet at all

Rule out the obvious before touching proxy settings.

1. Launch a browser and open two or three everyday websites to verify general connectivity. This single test divides the problem in half: a dead browser means a dead connection, while a live browser means the system-level update path alone is broken.
2. Over hotel, campus, or airport Wi-Fi, finish the captive-portal login inside the browser first.
3. Also observe whether the network is a captive-portal type, like hotel or campus Wi-Fi.
4. If the browser works but updates fail instantly, the fault lies in the update-specific connection path — continue, because only the proxy, DNS, firewall, and clock can explain that split.

### Fix 2: Wipe the proxy settings Windows Update relies on

Windows Update reads the system WinHTTP proxy, stored apart from the browser proxy settings most people inspect. Resetting the store erases the stale entries VPN clients abandon.

1. Launch an administrator Command Prompt first.
2. Run `netsh winhttp reset proxy` to clear the system proxy completely and immediately.
3. In Settings > Network & internet > Proxy, turn off any manual proxy unless your network genuinely needs one. Home connections almost never do.
4. Sever any VPN connection fully, then attempt the update check once more.

### Fix 3: Repair DNS and empty the resolver cache

Where hostnames will not resolve, moving to a dependable public DNS and emptying the cache takes name resolution out of the picture.

1. Go to Settings > Network & internet > Wi-Fi (or Ethernet), open the active connection, and switch DNS to manual: `8.8.8.8` and `8.8.4.4` (or `1.1.1.1` and `1.0.0.1`).
2. In the administrator prompt, run `ipconfig /flushdns`.
3. Retry the update check.

### Fix 4: Inspect the firewall and the clock

Two swift checks settle a surprising share of instant failures — a trigger-happy firewall rule, and a clock too skewed for TLS.

1. Switch off any third-party firewall briefly — leaving Windows Firewall active — then retry the update check.
2. Should the update succeed with the third-party firewall down, create a Windows Update exception instead of leaving it off.
3. Visit Settings > Time & language > Date & time, and turn on Set time automatically, plus Set time zone automatically.
4. Press Sync now under Additional settings to compel a time sync.

### Fix 5: Reset the Windows Update components

If the connection path is clean but updates still fail instantly, the engine's own state may be corrupt.

1. Staunch the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Quarantine the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Reopen the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Test for updates and confirm the connection finally succeeds now.

### Fix 6: Reinstall Windows as the final measure

When the addressing layer resists every repair, the network stack or servicing infrastructure is damaged beyond targeted fixes. This is uncommon — proxy and DNS repairs settle the vast majority of cases — but a thoroughly wedged stack justifies the heavier hammer. Reinstalling 24H2 over the existing install rebuilds both. Secure the ISO strictly from [Microsoft's Windows 11 download portal](https://www.microsoft.com/en-us/software-download/windows11).

1. Mount the ISO and ignite `setup.exe`.
2. Receive the license terms, then ordain **Keep personal files and apps**.
3. Confer 30–90 minutes for several restarts, and desert the process throughout.
4. Display that updates connect cleanly afterward.

## Closing

Name resolution is the foundation every update stands on: fix the proxy, the DNS, or the firewall, and the connection succeeds. Should downloads begin but then stall, the [24H2 update-error handbook](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) picks up from there, while the [Update troubleshooter walkthrough](/articles/best-way-to-fix-windows-update-with-troubleshooter/) handles the automated checks. The official connectivity checks are documented in [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
