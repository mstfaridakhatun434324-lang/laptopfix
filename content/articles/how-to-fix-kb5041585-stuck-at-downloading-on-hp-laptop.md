---
title: "KB5041585 Stuck at Downloading on Your HP Laptop? Unstick It"
slug: how-to-fix-kb5041585-stuck-at-downloading-on-hp-laptop
date: 2026-09-07
categories: ["windows-update"]
tags: ["kb5041585", "stuck downloading", "hp laptop", "bits", "windows 11 24h2"]
description: "Unstick KB5041585 frozen at downloading on an HP laptop: repair the delivery pipeline, reset BITS, and get the download moving again."
thumbnail: "/images/thumbs/how-to-fix-kb5041585-stuck-at-downloading-on-hp-laptop.webp"
faqs:
  - q: "Why is KB5041585 stuck at 0% or a fixed percentage?"
    a: "A download frozen at 0% means the request never reached the delivery servers — usually a BITS or network issue. Frozen at a fixed percentage means chunks are failing hash checks and retrying silently, which points to a corrupted cache or an interfering proxy or VPN. Task Manager's network graph distinguishes the two cases: zero traffic means a connection problem, while traffic with no progress means failing verification."
  - q: "Does pausing and resuming the update help?"
    a: "Sometimes. Pausing for a few minutes and resuming forces the delivery client to renegotiate its connections, which clears transient server-side stalls. For persistent freezes, though, you need the pipeline repairs in this guide. The pause forces the delivery client to renegotiate its server connections, which clears stalls caused by dead sessions rather than corruption."
  - q: "Could HP software be blocking the download?"
    a: "HP's own update tools do not block Windows Update downloads, but third-party firewalls, VPNs, and aggressive 'game booster' network tools bundled on some HP laptops can throttle or break the BITS connections Windows Update relies on. Check for trial VPN clients and network prioritizers in your installed apps — these install filter drivers that specifically disrupt background transfers."
  - q: "How long should a cumulative update download take?"
    a: "On a decent broadband connection, a cumulative update of a few hundred megabytes should finish in minutes, not hours. Anything stuck for over an hour with no percentage movement is genuinely stalled, not merely slow. If the percentage has not moved in fifteen minutes and Task Manager shows no network activity, treat it as stalled and work the fixes in order."
---

KB5041585 sitting at "Downloading — 0%" (or frozen at 47% for three hours) is a delivery problem, not an install problem — the update has not even arrived yet. On HP laptops this frequently traces to the Background Intelligent Transfer Service getting wedged, a corrupted partial download that the client keeps retrying, or network interference from VPNs and "optimizer" tools. The fix sequence below restarts the delivery machinery from the network up.

Work in order: verify the stall, clear network interference, repair BITS and the cache, then pull a fresh copy.

HP laptops deserve one specific note: many ship with network "optimization" utilities — gaming network prioritizers, bandwidth managers, or trial VPN clients — that install filter drivers on the Wi-Fi adapter. These tools are the single most common HP-specific cause of BITS stalls, because they intercept the exact traffic pattern update downloads use. If you find one in your installed apps, disable its filtering (or uninstall it) before blaming Windows.

## Why this happens

- **Wedged BITS queue:** The Background Intelligent Transfer Service manages the download; a wedged job blocks the queue and the percentage never moves.
- **Corrupted partial download:** Damaged chunks in the SoftwareDistribution cache fail verification, and the client re-downloads them in an endless loop.
- **VPN or proxy interference:** VPNs, corporate proxies, and "game booster" network filters break the range-request connections BITS uses.
- **Metered connection throttling:** Windows pauses or trickles update downloads on connections marked as metered.
- **DNS or network stack issues:** Stale DNS or a corrupted Winsock catalog prevents the client from reaching the delivery endpoints reliably.
- **Antivirus web filtering:** Real-time web shields from third-party antivirus can intercept and stall the update download streams.
- **Server-side throttling:** Occasionally Microsoft's delivery network is simply slow in a region; the client handles this badly and appears frozen.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall and try pause-resume

1. Note the exact percentage and wait 15 minutes — if it has not moved a single percent, it is stalled, not slow.
2. In **Settings > Windows Update**, click **Pause updates**, wait two minutes, then **Resume updates**.
3. The pause forces the delivery client to drop and renegotiate its connections, clearing transient stalls.
4. If the percentage jumps after resuming, let it run — the problem was server-side or connection-state, and it is over.

### Fix 2: Disconnect the VPN and check metered status

1. Fully disconnect any VPN — BITS range requests frequently break inside VPN tunnels.
2. Go to **Settings > Network & internet > Wi-Fi**, click your network, and check **Metered connection** — turn it **Off** for the update.
3. If you use a third-party firewall or "game booster," disable its network filtering temporarily.
4. Retry the download with a clean, unmetered, unfiltered connection. Our guide to [metered connections blocking updates](/articles/best-way-to-fix-metered-connection-blocking-windows-update/) covers the edge cases.

### Fix 3: Restart BITS and the update services

1. Open an elevated Command Prompt and run `net stop wuauserv`, `net stop bits`, `net stop cryptSvc`, `net stop msiserver`.
2. Wait ten seconds, then run `net start cryptSvc`, `net start bits`, `net start wuauserv`, `net start msiserver`.
3. Check for updates again — a restarted BITS picks up the download with a fresh job queue.
4. If BITS refuses to start, check its dependencies (it needs RPC and the Event Log service) in `services.msc`.

### Fix 4: Clear the corrupted partial download

1. With the services stopped (as in Fix 3), rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
2. Also rename `C:\Windows\System32\catroot2` to `catroot2.old` for a complete cache reset.
3. Restart the services and check for updates — KB5041585 downloads from zero with clean chunks.
4. The old folders can be deleted after a successful install; keep them until then as a fallback.

### Fix 5: Reset the network stack

1. In an elevated Command Prompt, run `netsh winsock reset` and `netsh int ip reset`.
2. Run `ipconfig /flushdns` to clear stale DNS entries that may point at dead delivery endpoints.
3. Restart the laptop — these resets only take effect after a reboot.
4. After rebooting, retry the download before reinstalling any VPN or network-filtering tool.

### Fix 6: Temporarily disable antivirus web filtering

1. Open your third-party antivirus and disable its web shield / real-time web filtering (keep file protection on if the product allows granular control).
2. Retry the KB5041585 download immediately.
3. If it completes, the web filter was intercepting the BITS streams — add an exclusion for Windows Update or consider switching to Defender.
4. Re-enable the web shield right after the download finishes. Microsoft documents safe update practices at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Pull the update manually from the Catalog

1. If the automated download still will not move, go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and search **KB5041585**.
2. Download the x64 package and install it directly — this skips BITS, the delivery client, and the entire download pipeline.
3. After manual install, run **Check for updates** so the system registers the KB as installed.
4. Keep an eye on the next Patch Tuesday: if downloads stall again, the BITS or network issue is systemic and deserves the deeper network diagnosis, plus a check that [driver updates](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) are not piling up behind the blockage.

### Fix 8: Switch to a wired connection and alternate DNS

1. If Wi-Fi is your only test so far, connect via Ethernet (or USB tethering from your phone) and retry — this isolates Wi-Fi driver and router quirks from the diagnosis.
2. Temporarily set your DNS to a public resolver (8.8.8.8 / 1.1.1.1) in the adapter properties to rule out ISP DNS returning stale delivery endpoints.
3. If the download completes on the alternate connection, the problem was your network path, not Windows — update the Wi-Fi driver or investigate the router.
4. Revert the DNS change afterward unless you prefer the public resolver permanently.

## Closing

A stuck download is the delivery pipeline telling you it cannot do its job — wedged BITS, poisoned cache, filtered network, or metered connection. Restart the machinery, clear the interference, and the megabytes flow again. And when the automated path refuses, the Update Catalog is always there: the same update, no delivery drama.
