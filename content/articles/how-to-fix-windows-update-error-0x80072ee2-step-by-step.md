---
title: "How to Fix Windows Update Error 0x80072EE2 Step by Step"
slug: how-to-fix-windows-update-error-0x80072ee2-step-by-step
date: 2026-10-07
categories: ["windows-update"]
tags: ["windows update", "0x80072ee2", "timeout", "windows 11"]
description: "Error 0x80072EE2 means the Windows Update connection timed out. Follow this step-by-step guide to clear proxies, repair BITS, and complete the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80072ee2-step-by-step.webp"
faqs:
  - q: "What causes Windows Update error 0x80072EE2?"
    a: "The code is ERROR_WINHTTP_TIMEOUT: the update operation started but exceeded its time limit. Causes include slow or congested connections, proxy servers adding delay, firewalls deeply inspecting traffic, a stalled Background Intelligent Transfer Service, VPN instability, or corrupted update metadata causing negotiation loops. It is a transit problem, so the fixes focus on the connection path and transfer service."
  - q: "How do I reset the Background Intelligent Transfer Service?"
    a: "Open services.msc, find Background Intelligent Transfer Service, and restart it, making sure its startup type is Manual rather than Disabled. In an administrator Command Prompt you can also run bitsadmin /reset /allusers to cancel stuck transfer jobs. BITS is the engine behind update downloads, so a stalled BITS queue produces exactly this timeout behavior."
  - q: "Why does the error only happen on large updates?"
    a: "Timeouts are time-based, so they strike the longest operations first. Small definition updates finish before any limit is hit, while multi-hundred-megabyte cumulative updates on a slow or inspected connection run out the clock. If small updates succeed and large ones time out, the cause is almost certainly bandwidth, proxy delay, or firewall inspection rather than system damage."
  - q: "Is it safe to disable my firewall to test?"
    a: "Briefly disabling a third-party firewall for one update test is low-risk if you re-enable it immediately and stay off untrusted networks during the test. Do not leave it off, and do not disable Windows Firewall permanently. The test simply isolates whether the firewall's traffic inspection is the delay source; if it is, add proper exclusions instead of leaving protection off."
---

Error 0x80072EE2 reports ERROR_WINHTTP_TIMEOUT — Windows Update found the servers, began the exchange, and ran out of patience. The operation took longer than the allowed window, so Windows aborted it. Everything about your system is fine; the conversation just stalled.

Timeouts punish the longest operations first, which is why this error loves large cumulative updates on slow, proxied, or heavily inspected connections. The repair sequence works inward from the network: clear the bandwidth, remove proxy and inspection delays, fix the transfer service, and only then touch update components.

Here's the key insight for diagnosing timeouts: if small updates (like Defender definitions) succeed while large cumulative updates fail, the fault is almost certainly in the transfer path — bandwidth, proxy, inspection, or drivers — not in Windows itself. That pattern tells you to spend your time on Fixes 1 through 4 and the network driver check, rather than on component-store repairs that won't help a transit problem. Conversely, if every update fails — small definitions included — the problem is more fundamental, and the cache reset and network-stack rebuild in Fix 5 become the priority. Reading the failure pattern first is what separates a ten-minute fix from an afternoon of guessing, so note which updates succeed before you start, and keep a simple log as you test each fix.

## Why this happens

- **Congested or slow connection.** Large updates exceed internal timeouts on saturated links.
- **Proxy-induced delay.** Each request detours through a slow proxy.
- **Firewall deep inspection.** Security software scanning every chunk adds fatal latency.
- **Stalled BITS queue.** The transfer service hangs on dead jobs.
- **Unstable VPN.** Tunnels dropping mid-transfer force restarts that never finish in time.
- **Corrupted update metadata.** Negotiation loops waste the timeout window.
- **Peak rollout congestion.** Microsoft's endpoints slow during major release waves.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Quiet the connection

Give the update the whole pipe and see if that's enough.

1. Pause cloud syncs, streaming, and other downloads on the network.
2. Disconnect any VPN for the test.
3. Retry **Settings > Windows Update > Check for updates**.
4. If the timeout clears, you've diagnosed congestion — run big updates off-hours or on a faster link rather than repairing the system.

### Fix 2: Remove proxy delays

Check both the user-level and system-level proxy.

1. Open **Settings > Network & internet > Proxy** and turn off any proxy you don't require.
2. Run `netsh winhttp show proxy` in an administrator Command Prompt to see the proxy Windows Update itself uses.
3. Clear stale entries with `netsh winhttp reset proxy`.
4. Retry the update; direct connections eliminate proxy-added latency entirely.

### Fix 3: Bypass security inspection temporarily

Test whether your security software is the bottleneck.

1. Temporarily pause your third-party antivirus's web shield or real-time protection.
2. Retry the update immediately.
3. Re-enable protection right away, pass or fail.
4. If the update succeeded, configure exclusions for Windows Update or disable the product's HTTPS traffic scanning, which is the usual delay source.

### Fix 4: Repair the Background Intelligent Transfer Service

BITS does the actual downloading; when it stalls, everything times out.

1. Open `services.msc`, locate **Background Intelligent Transfer Service**, set startup to **Manual**, and restart it.
2. In an administrator Command Prompt, run `bitsadmin /reset /allusers` to cancel hung transfer jobs.
3. Also restart the **Windows Update** service while you're in the Services console.
4. Retry the update check with a clean transfer queue.

### Fix 5: Reset update cache and the network stack

Clear stale metadata and rebuild low-level networking together.

1. In an administrator Command Prompt: `net stop wuauserv`, `net stop bits`, `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`, `net start wuauserv`, `net start bits`.
2. Run `netsh winsock reset` and `netsh int ip reset`, then restart.
3. After reboot, run the **Windows Update** troubleshooter from **Settings > System > Troubleshoot > Other troubleshooters**.
4. Retry the update on the fresh stack and cache.

### Fix 6: Download the package manually

Sidestep the timeout-prone automatic transfer.

1. Copy the failing KB number from **Settings > Windows Update > Update history**.
2. Fetch the x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), on another machine via USB if your link is the problem.
3. Run the standalone installer on the affected laptop.
4. Verify success in Update history. For background on these transfer failures, Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) is the authoritative reference.

### Fix 7: Update the network adapter drivers

Unstable Wi-Fi or Ethernet drivers stall long transfers in ways that mimic server timeouts.

1. Open **Device Manager**, expand **Network adapters**, and note your adapter's exact model.
2. Get the latest driver from your laptop maker's support site (or Intel's driver tool for Intel wireless), install it, and restart.
3. Prefer a wired connection for the update test if one is available — it removes wireless variability entirely.
4. Retry the update; healthy drivers sustain the long transfer a cumulative update requires.

### Fix 8: Perform an in-place upgrade as the final repair

If the transfer path is clean and timeouts persist, rebuild the update stack itself.

1. Download the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it.
2. Run `setup.exe`, accept the terms, and choose **Keep personal files and apps**.
3. Let the 30-to-90-minute upgrade complete with the charger connected.
4. After signing in, retry the update — the fresh BITS and update components complete transfers normally.

## Closing

Error 0x80072EE2 is about a conversation that ran too long, so the fixes that shorten the path — bandwidth, proxy, inspection, BITS — outperform system repairs nearly every time. For HP-specific wrinkles like Support Assistant contention, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x80072ee2-on-hp-laptop/), and if downloads fail outright rather than timing out, the [0x80240034 step-by-step guide](/articles/how-to-fix-windows-update-error-0x80240034-step-by-step/) addresses that variant.
