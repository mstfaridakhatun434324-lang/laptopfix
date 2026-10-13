---
title: "KB5041585 Stuck at Downloading on Lenovo Laptop? Unstick It"
slug: how-to-fix-kb5041585-stuck-at-downloading-on-lenovo-laptop
date: 2026-09-04
categories: ["windows-update"]
tags: ["kb5041585", "stuck downloading", "lenovo laptop", "windows update", "windows 11"]
description: "KB5041585 frozen at 0% or partial download on your Lenovo laptop? Here's how to unstick the download and get this update installed."
thumbnail: "/images/thumbs/how-to-fix-kb5041585-stuck-at-downloading-on-lenovo-laptop.webp"
faqs:
  - q: "What is KB5041585?"
    a: "KB5041585 is a Windows 11 cumulative update package (from the August 2024 Patch Tuesday cycle, build 26100.1457 for 24H2-era servicing). Like all cumulative updates it bundles security and quality fixes. The troubleshooting below applies equally if a later KB sticks at downloading — the mechanism is identical."
  - q: "How long should a cumulative update take to download?"
    a: "On a decent broadband connection, 10 to 30 minutes for the full package. If the percentage hasn't moved in over an hour, or it's been sitting at 0% for 30+ minutes with an active connection, the download is stuck — not slow."
  - q: "Why does it get stuck specifically at downloading?"
    a: "Download-phase hangs come from the delivery side, not the install side: corrupted partial files in the cache, BITS jobs wedged in an error state, metered-connection throttling, VPN/proxy interference, or Lenovo network-driver issues stalling the transfer mid-stream."
  - q: "Can I download KB5041585 manually instead?"
    a: "Yes — the Microsoft Update Catalog hosts every KB as a standalone .msu. Manual download bypasses the stuck BITS/Delivery Optimization pipeline entirely and is often the fastest resolution when the automatic download won't budge, since it avoids every component that could be wedged."
---

KB5041585 downloads to 7% — and stays there. Or 0%. Or 100% "downloading" with nothing happening. The progress bar becomes a permanent fixture of your Windows Update screen, and every "Retry" just resumes the same frozen state. On Lenovo laptops this particular stuck-download pattern often traces back to network driver quirks or the update cache holding a corrupted partial file that the downloader keeps trying to resume.

Download-phase problems are actually good news: nothing has been installed yet, so there's zero risk to your system, and the fixes are all about clearing the pipe and getting a clean copy. Work through them in order. If your issue is a different KB or the update downloads fine but fails at install, our [cumulative-update install guide](/articles/how-to-fix-cumulative-update-fails-to-install-step-by-step/) picks up where this leaves off.

One diagnostic that saves time: open **Settings > Windows Update** and watch the percentage for exactly five minutes. If it creeps upward even slowly, the download is working — just leave it alone, possibly overnight. If it's byte-identical after five minutes on a connection you know is active (test by loading a webpage), the pipeline is wedged and the fixes below apply. Interrupting a slow-but-working download just forces it to restart from scratch, so confirm the stall before you clear anything.

## Why this happens

- **Corrupt partial download**: A damaged chunk in SoftwareDistribution that resume keeps tripping over.
- **Wedged BITS jobs**: Background Intelligent Transfer Service jobs stuck in transient-error limbo.
- **Metered connection throttling**: Windows pausing the download without clearly saying so.
- **VPN/proxy interference**: Corporate VPNs and proxies breaking the CDN connection mid-transfer.
- **Lenovo network driver issues**: Outdated Wi-Fi/Ethernet drivers stalling sustained downloads.
- **Delivery Optimization conflicts**: Peer-to-peer sharing getting stuck on a bad peer.
- **Disk space**: Not enough room to stage the full package, silently halting the download.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's stuck, then pause and resume

Give the downloader one clean restart signal.

1. Verify the percentage hasn't moved for **60+ minutes** on an active connection.
2. In **Settings > Windows Update**, click **Pause updates** for 1 week, wait 2 minutes, then **Resume updates**.
3. This resets the download session state — if it was a transient stall, the download restarts cleanly.

### Fix 2: Check connection, VPN, and metered status

Eliminate the network side.

1. Disconnect any **VPN** and disable proxy settings (**Settings > Network & internet > Proxy**).
2. Check **Metered connection** on your active network — turn it off or enable **Download updates over metered connections**.
3. Switch from Wi-Fi to **wired Ethernet** if possible for the download; Lenovo Wi-Fi drivers with power-saving bugs are a known stall source.

### Fix 3: Clear the corrupted partial download

The highest-success fix for frozen percentages.

1. Elevated Terminal: `net stop wuauserv`, `net stop bits`.
2. Delete the contents of `C:\Windows\SoftwareDistribution\Download` (leave the folder itself).
3. `net start wuauserv`, `net start bits`, then **Check for updates** — the download restarts from zero with clean files.

### Fix 4: Reset BITS and the full update cache

When partial-clearing isn't enough.

1. Elevated Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` → `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` → `catroot2.old`.
3. Restart all four services; check for updates. Microsoft documents this reset at the [Windows update support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Update Lenovo network drivers

Stalled sustained transfers often mean driver-level network bugs.

1. Get the latest **Wi-Fi** and **Ethernet** drivers from [Lenovo Support](https://support.lenovo.com/us/en/) for your exact model. Lenovo's validated drivers matter here — generic Windows wireless drivers have a history of power-management bugs that stall long downloads.
2. Install, restart, and retry the download.
3. In Device Manager → network adapter → **Properties > Power Management**, uncheck **Allow the computer to turn off this device to save power** during the download. Also check the **Advanced** tab for power-saving features like "Selective suspend" and disable them temporarily — a Wi-Fi radio napping mid-download is a classic cause of the frozen-percentage symptom.

### Fix 6: Limit Delivery Optimization interference

Peer-to-peer sharing occasionally wedges downloads.

1. **Settings > Windows Update > Advanced options > Delivery Optimization**.
2. Turn **Allow downloads from other PCs** off temporarily.
3. Retry the download — pure CDN fetching is more predictable.

### Fix 7: Manual download from the Update Catalog

Bypass the entire automatic pipeline.

1. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search **KB5041585**.
2. Download the x64 `.msu`, disconnect the VPN, close Lenovo utilities, and run it.
3. The standalone installer doesn't use BITS or the SoftwareDistribution cache at all.

## Closing

A stuck download is a plumbing problem, not a system problem — clear the pipe (cache, BITS, network path) and the update flows. KB5041585 specifically has no known install-blocking bug; every stuck case traces to the download pipeline. Fix the pipeline once and every future KB downloads cleanly too. Keep Lenovo's network drivers current and this particular headache stays away. And if a stalled download ever tips over into a half-installed update that won't roll back, our [undoing-changes recovery guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2/) covers that next stage.

One preventive habit for Lenovo owners: run Lenovo's own system update tool (Vantage or the support site) monthly for network and chipset drivers, separate from Windows Update days. Current network drivers are the single best defense against stuck downloads, and updating them proactively — rather than discovering they're stale mid-crisis — turns this whole category of problem into something you read about instead of experience. The same principle applies to every fix in this guide: the cache reset you do calmly on a quiet afternoon beats the one you do frantically at midnight. And if this same stuck-download pattern ever appears for a different KB, you'll recognize it instantly — the fixes are identical regardless of the update number, because the download pipeline doesn't care which package it's carrying. Same symptoms, same diagnosis, same fix — the KB number is just a label on an identical plumbing problem.
