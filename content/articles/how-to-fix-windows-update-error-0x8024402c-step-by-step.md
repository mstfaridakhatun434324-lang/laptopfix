---
title: "How to Fix Windows Update Error 0x8024402C Step by Step"
slug: how-to-fix-windows-update-error-0x8024402c-step-by-step
date: 2026-10-05
categories: ["windows-update"]
tags: ["windows update", "0x8024402c", "dns", "windows 11"]
description: "Error 0x8024402C means Windows Update can't reach Microsoft's servers. Follow this step-by-step guide to fix the clock, DNS, proxy, and firewall causes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x8024402c-step-by-step.webp"
faqs:
  - q: "What does Windows Update error 0x8024402C mean?"
    a: "It is WU_E_PT_WINHTTP_NAME_NOT_FOUND: Windows Update could not resolve or connect to the update server hostname. Your general internet can work fine while this happens, because Windows Update uses the system-level WinHTTP stack with its own proxy and DNS behavior. The fix targets that system-level network configuration — clock, DNS, proxy, and firewall — rather than your browser or Wi-Fi signal."
  - q: "How can the system clock break Windows Update?"
    a: "Update servers use encrypted connections with certificates that are only valid in a specific time window. If your laptop's clock is days, months, or years off — common after a dead CMOS battery or a long shutdown — the certificate check fails and the connection is refused, producing 0x8024402C. Enabling automatic time and syncing once fixes it instantly in those cases."
  - q: "What is the WinHTTP proxy and why does it matter?"
    a: "WinHTTP is the system-level HTTP stack that Windows Update uses, separate from your browser's settings. Old VPNs, privacy tools, and some malware set a WinHTTP proxy that routes update traffic to a dead address. Your browser ignores it and works normally, which is exactly why this error is so confusing. Resetting the WinHTTP proxy removes the stale route."
  - q: "Could my ISP be blocking Windows Update?"
    a: "It is possible but uncommon. Some restrictive networks, school filters, and misconfigured routers block Microsoft's update endpoints. Test by connecting through a phone hotspot: if updates work there, the block is in your router or ISP path, not your laptop. For home routers, check for custom DNS filtering or parental-control blocklists covering Microsoft domains."
---

Error 0x8024402C means Windows Update can't find its way to Microsoft's servers: WU_E_PT_WINHTTP_NAME_NOT_FOUND. The maddening part is that everything else online works — browsing, streaming, email — because those apps don't use the same network path that Windows Update does. The updater relies on the system-level WinHTTP stack, with its own proxy settings and DNS behavior, and something in that stack is misdirected.

The repair order follows the connection outward from your laptop: first the clock (which breaks encryption), then DNS (which resolves the server names), then the proxy (which routes the traffic), then the firewall (which may block it). Each check takes minutes, and one of them is the culprit in nearly every case.

A useful mental model: your browser and Windows Update are two different travelers using two different roads to the internet. Your browser uses its own proxy and DNS settings; Windows Update uses the system-level WinHTTP stack. A roadblock on the system road — a stale proxy, a poisoned DNS entry, a firewall rule aimed at the update service — stops updates cold while browsing sails through. Every fix below repairs the system road specifically. Work them in the order given — clock, DNS, proxy, firewall — because each test takes under two minutes and the sequence runs from most to least likely cause. By the end of Fix 4, the great majority of 0x8024402C failures are resolved without touching a single system file.

## Why this happens

- **Wrong system date and time.** Certificate validation fails when the clock is far off, killing the secure connection.
- **Failing DNS resolution.** The system resolver can't translate update server hostnames.
- **Stale WinHTTP proxy settings.** Leftovers from uninstalled VPNs route update traffic into the void.
- **Third-party firewall rules.** Security suites blocking the update service while browsers pass through.
- **Corrupted Winsock or TCP/IP stack.** Damaged system networking that browsers work around but WinHTTP can't.
- **Router or ISP filtering.** Update endpoints blocked upstream of the laptop.
- **Corrupted update components.** A damaged local update stack misreporting a network failure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Sync the system clock

Start with the quickest possible win.

1. Right-click the taskbar clock and choose **Adjust date and time**.
2. Enable **Set time automatically** and click **Sync now**; confirm the time zone matches your location.
3. If the clock was wildly wrong, check whether it drifts again after reboot — repeated drift suggests a dying CMOS battery, a hardware issue worth knowing about.
4. Retry the update check; a corrected clock restores the secure handshake immediately.

### Fix 2: Change DNS servers

Give name resolution a reliable path.

1. Open **Settings > Network & internet**, click your connection, and find the DNS settings (or use adapter properties in the Control Panel).
2. Switch to manual DNS with a dependable public pair such as 8.8.8.8 and 8.8.4.4, noting your original values first.
3. Flush the resolver cache with `ipconfig /flushdns` in Command Prompt.
4. Retry Windows Update. If it works, your previous DNS was failing on Microsoft's hostnames specifically.

### Fix 3: Inspect and reset the WinHTTP proxy

This is the signature fix for "browser works, updates don't."

1. Check **Settings > Network & internet > Proxy** and disable any proxy server you don't actively need.
2. In an administrator Command Prompt, run `netsh winhttp show proxy` to see what Windows Update actually uses.
3. If it lists a stale or unfamiliar proxy, run `netsh winhttp reset proxy` to clear it to direct access.
4. Retry the update check. Also disable leftover virtual adapters from uninstalled VPNs in **Network Connections**.

### Fix 4: Rule out firewall interference

Test whether security software is blocking the updater.

1. Temporarily turn off any third-party firewall or security suite (leave Windows Firewall enabled).
2. Immediately retry the update check.
3. Re-enable the software right after the test.
4. If the test succeeded, add explicit allow rules for the Windows Update service (wuauserv) and BITS in that product's firewall settings.

### Fix 5: Reset the network stack

Rebuild Winsock and TCP/IP when the configuration is tangled.

1. In an administrator Command Prompt: `netsh winsock reset` then `netsh int ip reset`.
2. Restart the laptop — the reset only takes effect at boot.
3. After reboot, run `ipconfig /flushdns` once more.
4. Retry the update. Test on a phone hotspot too, to separate laptop problems from router or ISP blocking.

### Fix 6: Repair the update components

Clear local damage that can mimic a network failure.

1. Run the **Windows Update** troubleshooter from **Settings > System > Troubleshoot > Other troubleshooters**.
2. Reset the cache in an administrator Command Prompt: `net stop wuauserv`, `net stop bits`, `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`, `net start wuauserv`, `net start bits`.
3. Retry the update check.
4. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) has additional connectivity diagnostics for stubborn cases.

### Fix 7: Isolate the network with a hotspot test

Determine conclusively whether the fault is the laptop or the network path.

1. Connect to a mobile phone hotspot and retry **Settings > Windows Update > Check for updates**.
2. If updates work on the hotspot, your router, ISP, or upstream filter is blocking the update endpoints — the laptop is innocent.
3. On the home network, restart the router, check its firmware, and look for DNS filtering, parental controls, or firewall rules covering Microsoft domains.
4. If the hotspot fails too, the problem is definitely local — re-verify Fixes 1 through 6 carefully, especially the WinHTTP proxy.

## Closing

Error 0x8024402C is a routing problem in the system network stack, and the clock-DNS-proxy-firewall sequence above finds it in the great majority of cases. For HP-specific considerations like bundled security software, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x8024402c-on-hp-laptop/), and if the connection works but downloads keep failing partway, the [0x80240034 step-by-step guide](/articles/how-to-fix-windows-update-error-0x80240034-step-by-step/) picks up where this one leaves off.
