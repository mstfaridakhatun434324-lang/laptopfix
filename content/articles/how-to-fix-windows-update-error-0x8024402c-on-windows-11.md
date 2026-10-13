---
title: "Fix Windows Update Error 0x8024402C on Windows 11: Connection Failed"
slug: how-to-fix-windows-update-error-0x8024402c-on-windows-11
date: 2026-09-09
categories: ["windows-update"]
tags: ["windows 11", "windows update", "error 0x8024402c", "proxy", "name resolution"]
description: "Error 0x8024402C means Windows Update can't reach its servers. Fix proxy, DNS, and connection issues on Windows 11 with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x8024402c-on-windows-11.webp"
faqs:
  - q: "What does error 0x8024402C mean?"
    a: "It means Windows Update could not establish a connection to the update servers — a name-resolution or proxy failure at the very first step. Your browser may work fine because it uses different connection settings than the Windows Update service does."
  - q: "Why does my browser work but Windows Update fails with this error?"
    a: "Windows Update uses the system WinHTTP proxy configuration, not your browser's proxy settings. A proxy configured for WinHTTP (or a broken one left behind by uninstalled VPN software) breaks Windows Update while browsers sail through completely unaffected — which is exactly the confusing symptom most people report."
  - q: "Can VPN software cause 0x8024402C even when disconnected?"
    a: "Yes. VPN clients often set system-level proxy or routing configurations that persist after disconnection. If the error started after installing or removing a VPN, check the WinHTTP proxy settings with netsh and look for leftover virtual adapters in Device Manager — both are classic remnants."
  - q: "Is 0x8024402C ever caused by Microsoft's servers being down?"
    a: "Rarely, but it happens during major outages. Before deep troubleshooting, check the Microsoft service status or simply wait an hour and retry. If the error persists across different networks and several days, it is local to your machine — not Microsoft — and the proxy and DNS steps in this guide are where to focus."
---

Error 0x8024402C is a connection error with a specific flavor: Windows Update could not even reach its servers. Not a failed download, not a corrupt file — the conversation never started. The technical name is a WinHTTP name-resolution failure, which in plain terms means the update service could not resolve or connect to Microsoft's update endpoints. On Windows 11, the culprits live in the connection layer: proxy configuration (especially the WinHTTP proxy, which is separate from your browser's), DNS, VPN leftovers, and firewall rules.

The confusing part for most people is that everything else on the laptop works — browsing, streaming, email. That is expected: those apps do not use the same connection path as Windows Update. The fixes below target the update service's specific path. Work them in order, retrying the update check after each.

## Why this happens

- **Misconfigured WinHTTP proxy:** The system-level proxy Windows Update uses is wrong, stale, or pointing at a server that no longer exists.
- **VPN leftovers:** Uninstalled or disconnected VPN clients leave proxy settings, routes, or virtual adapters that break the update path.
- **DNS failures:** The system's DNS cannot resolve Microsoft's update hostnames.
- **Firewall blocking:** Third-party firewalls blocking the update service's outbound connections while allowing browsers.
- **Corrupted WinHTTP configuration:** Damaged WinHTTP settings from tools or failed VPN uninstalls.
- **ISP-level blocking:** Rare, but some networks block the specific endpoints or ports Windows Update needs.
- **Incorrect date and time:** TLS certificate validation fails when the clock is far off, killing the HTTPS connection at handshake.
- **Corrupted network stack:** Damaged Winsock/TCP-IP affecting the service's connections specifically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check date, time, and try another network

Two fast eliminations: certificate-killing clock skew and network-level blocking.

1. Open **Settings > Time & language > Date & time**, enable automatic time and zone, and click **Sync now**.
2. If you are on a corporate, school, or public network, try a phone hotspot to rule out network-level blocking.
3. Retry **Settings > Windows Update > Check for updates**.

### Fix 2: Inspect and reset the WinHTTP proxy

This is the highest-yield fix for 0x8024402C. The WinHTTP proxy is invisible in browser settings, so it gets overlooked.

1. Open **Terminal (Admin)**.
2. Run `netsh winhttp show proxy` to see the current configuration.
3. If it shows a proxy you do not recognize or no longer use, reset it: `netsh winhttp reset proxy`.
4. If you do need a proxy, set it correctly: `netsh winhttp set proxy proxy-server="your-proxy:port"`.
5. Retry the update check.

### Fix 3: Check the Settings proxy page too

Windows 11 has both the WinHTTP proxy and the user-level proxy; check both.

1. Go to **Settings > Network & internet > Proxy**.
2. Turn off **Use a proxy server** unless you actively need one, and disable any suspicious **automatic setup** scripts.
3. Retry Windows Update.

### Fix 4: Remove VPN leftovers

VPN clients are repeat offenders for this error, even when "disconnected."

1. Fully uninstall any VPN you no longer use via **Settings > Apps > Installed apps**.
2. In **Device Manager > Network adapters**, remove greyed-out or orphaned virtual adapters (check **View > Show hidden devices**).
3. In an elevated Terminal, run `netsh winhttp reset proxy` again to clear anything the uninstaller left.
4. Restart and retry.

### Fix 5: Flush DNS and switch resolvers

If name resolution is the broken link, fix it directly.

1. In **Terminal (Admin)**, run `ipconfig /flushdns`.
2. Change your DNS to 1.1.1.1 / 1.0.0.1 or 8.8.8.8 / 8.8.4.4 in the adapter's IPv4 properties (**Settings > Network & internet > Advanced network settings**).
3. Retry the update. If it works, your ISP's DNS was failing on Microsoft's hostnames — a more common issue than people expect.

### Fix 6: Reset the network stack

For corrupted stack configurations affecting the service's connections.

1. In **Terminal (Admin)**, run `netsh winsock reset` and `netsh int ip reset`.
2. Restart the laptop.
3. Retry Windows Update. This reset also helps the [download-failure error 0x80240034](/articles/how-to-fix-windows-update-error-0x80240034-on-windows-11/), which lives one layer above this connection error.

### Fix 7: Check firewall rules and run the troubleshooter

Make sure nothing is blocking the update service's outbound traffic.

1. Temporarily disable any third-party firewall and retry the update check. Re-enable it immediately after the test.
2. In **Windows Security > Firewall & network protection**, confirm the firewall is not blocking system services.
3. Run **Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run** for automated repairs.
4. For persistent enterprise-proxy scenarios, the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) documents the endpoints that must be reachable.

The WinHTTP proxy confusion at the heart of this error catches even experienced users, so it is worth explaining the split plainly. Windows maintains two separate proxy configurations: the WinINet proxy used by browsers and most applications (set in Settings or Internet Options), and the WinHTTP proxy used by system services like Windows Update (set only via netsh). They do not sync automatically. VPN clients, enterprise management tools, and old internet optimizer utilities commonly write to the WinHTTP proxy and never clean up — leaving Windows Update pointed at a proxy server that vanished years ago while your browser works perfectly. The netsh winhttp show proxy command is the only way to see this hidden configuration, which is why it sits near the front of this guide and not as an afterthought. In managed environments, the correct fix is to get the real proxy address from IT and set it properly rather than resetting to direct access. For Windows 10's version of this error, see our [Windows 10 0x8024402C guide](/articles/how-to-fix-windows-update-error-0x8024402c-on-windows-10/).

## Closing

Error 0x8024402C is the update service saying it cannot phone home, and the fix is almost always in the connection layer it uniquely uses: the WinHTTP proxy, VPN leftovers, or DNS. The `netsh winhttp` commands are the star of this show — a stale proxy there breaks updates while everything else works fine. Clear it, fix DNS, remove VPN debris, and the update check connects on the first try again.
