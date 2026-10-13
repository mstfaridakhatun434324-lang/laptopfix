---
title: "How to Fix Windows Update Error 0x80244010 on a Laptop"
slug: how-to-fix-windows-update-error-0x80244010-on-laptop
date: 2026-09-21
categories: ["windows-update"]
tags: ["windows update error 0x80244010", "wu_e_pt_exceeded_max_server_trips", "wsus leftover", "update server trips exceeded"]
description: "Error 0x80244010 means update requests bounced between servers too many times. Fix proxy, VPN, and leftover server settings to reconnect."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80244010-on-laptop.webp"
faqs:
  - q: "What does error 0x80244010 mean?"
    a: "It means the update client exceeded the maximum number of server round trips while trying to get update metadata. In practice the client is being bounced between servers, usually by a proxy, a misconfigured VPN, or leftover enterprise server settings, and gives up after too many redirects."
  - q: "What are leftover WSUS settings?"
    a: "WSUS, Windows Server Update Services, lets companies serve updates from a local server. If your laptop was ever managed by a workplace, registry settings may still point Windows Update at the old corporate server, which no longer responds, causing endless redirects."
  - q: "Can a VPN cause 0x80244010?"
    a: "WSUS, Windows Server Update Services, lets companies serve updates from a local server. If your laptop was ever managed by a workplace, registry settings may still point Windows Update at the old corporate server, which no longer responds, causing endless redirects and this error."
  - q: "How do I know if a proxy is the problem?"
    a: "Disconnect the VPN and disable all proxies, then retry the update check immediately. If it succeeds, the proxy or VPN was the cause, and you can re-enable it afterward with an exception for update traffic so the problem does not return."
---

Error 0x80244010 has one of the more descriptive internal names in the update system: the client exceeded the maximum server trips. Picture Windows Update asking for directions, being sent to another server, being sent to another, and another, until it throws up its hands. Something in the network path is redirecting requests in circles.

On corporate machines this historically meant WSUS misconfiguration. On personal laptops, the far more common culprits are VPNs, proxies, and the ghost of a previous workplace: registry settings still pointing Windows Update at a long-gone company update server.

The fix is to straighten the path: remove the middlemen, evict the leftover server settings, and let the client talk to Microsoft directly.

Imagine asking for directions and being sent from desk to desk in an endless loop — that is what your update client experiences with 0x80244010. Each redirect is individually reasonable, but together they exceed the client's patience. The middlemen causing the loop are almost always on your machine or your network, which is good news: you control both.

## Why this happens

- **VPN redirecting update traffic.** VPNs that intercept HTTPS can bounce update requests between endpoints until the trip limit is hit.

- **Proxy misconfiguration.** A proxy that chains or loops requests creates the redirect storm this code describes.

- **Leftover WSUS registry settings.** A previously managed laptop may still point Windows Update at a dead corporate server.

- **Corrupt update cache.** Damaged metadata in the local cache can send the client requesting the same data repeatedly.

- **DNS hijacking or filtering.** DNS-level filters that redirect Microsoft domains break the client's server negotiation.

- **Firewall interfering with redirects.** Security software that rewrites update traffic can create artificial redirect loops.

- **Stuck BITS jobs.** Wedged transfer jobs can compound the retry behavior behind this error.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Disconnect the VPN and disable the proxy

Remove the two most common redirect sources in one move. If the update check succeeds with a clean path, you have your answer in under a minute. Some VPNs offer a split-tunneling or trusted-networks feature; adding Microsoft's update endpoints to the bypass list keeps protection for browsing while letting updates through directly.

1. Disconnect the VPN completely.
2. In Settings, then Network and internet, then Proxy, turn off all manual and automatic proxy settings you do not need.
3. Open an admin Terminal and run `netsh winhttp reset proxy`.
4. Check for updates again.

### Fix 2: Fix 2: Remove leftover WSUS server settings

If the laptop was ever workplace-managed, the registry may still name a corporate update server. Clearing those values returns Windows Update to Microsoft's servers. The Policies key sometimes contains a whole WindowsUpdate subtree from mobile device management; if the laptop was ever enrolled, removing the stale subtree is safe once unenrolled.

1. Press Win + R, type `regedit`, and go to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate.
2. If WUServer or WUStatusServer values exist pointing to a company server, back up the key and delete those values.
3. Also check the AU subkey for restrictive policies, restart, and retry.

### Fix 3: Fix 3: Flush DNS and reset the network stack

Stale or poisoned DNS entries can keep sending the client to the wrong endpoints. Flushing the resolver and resetting the stack clears the whole layer. These three commands each target a different layer — DNS cache, socket state, and IP configuration — which is why running all three covers the bases one alone might miss.

1. In an admin Terminal, run `ipconfig /flushdns`, then `netsh winsock reset`, then `netsh int ip reset`.
2. Restart the laptop.
3. Check for updates on the fresh stack.

### Fix 4: Fix 4: Reset the Windows Update components

Corrupted local metadata can make the client re-request the same data in a loop. Resetting rebuilds the metadata store from scratch. Renaming the folders with .old suffixes rather than deleting them means you can compare old and new DataStore contents later if you are curious what was corrupted.

1. Open an elevated Terminal and stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services and retry the update check.

### Fix 5: Fix 5: Try a different network

Switching from Wi-Fi to a phone hotspot, or vice versa, bypasses every middlebox on the current network at once. It is the fastest way to prove the problem is the network, not the laptop. Tethering over USB instead of a Wi-Fi hotspot is worth trying too; it uses a different network path on some carriers and can behave differently.

1. Connect to a mobile hotspot or a different Wi-Fi network.
2. Check for updates there. If it works, the original network's proxy, DNS, or filtering is the cause.

### Fix 6: Fix 6: Temporarily disable third-party security software

Traffic-filtering security suites can manufacture the redirect loops behind this code. Disabling them for one update check isolates the variable. Web-filtering features with names like Bank Mode or Secure DNS are the usual culprits inside security suites; disabling just that module is often enough.

1. Disable third-party firewall and web-filtering features, keeping Windows Security active.
2. Retry the update check immediately.
3. Re-enable the software afterward, adding exceptions for Windows Update if needed.

### Fix 7: Fix 7: Run the troubleshooter and repair system files

Finish with the automated pass and the file repair. The troubleshooter resets the client's server configuration, and SFC fixes any damaged client binaries. SFC rarely fixes this error directly, but it rules out client-binary damage definitively, which matters when you have exhausted the network-side suspects.

1. Run the Windows Update troubleshooter from Settings, then System, then Troubleshoot.
2. Then in an admin Terminal run `sfc /scannow` and restart.
3. Check for updates. For timeout-flavored connection failures, our [0x8024401c guide](/articles/how-to-fix-windows-update-error-0x8024401c-on-laptop/) covers the next scenario, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the official steps.

## Closing

Error 0x80244010 is the update client getting lost between servers, and the fix is giving it a straight path: drop the VPN and proxy, evict any leftover corporate server settings, and reset the local metadata. Once the client talks to Microsoft directly, the redirect storm ends. For the related timeout variant, see our [0x8024401c walkthrough](/articles/how-to-fix-windows-update-error-0x8024401c-on-laptop/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official troubleshooting path. On 24H2 builds, the [24H2 edition of this fix](/articles/how-to-fix-windows-update-error-0x80244010-in-windows-11-24h2/) replays the same straighten-the-path playbook with build-specific steps.
