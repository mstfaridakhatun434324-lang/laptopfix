---
title: "Windows 11 Update Error 0x80244010: Stop the Server Trip Loop"
slug: how-to-fix-windows-update-error-0x80244010-on-windows-11
date: 2026-10-13
categories: ["windows-update"]
tags: ["windows update", "0x80244010", "windows 11", "wsus", "server trips"]
description: "Error 0x80244010 means Windows 11 exceeded its allowed trips to the update server. Fix the misdirected requests — usually stale WSUS keys or proxy issues."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80244010-on-windows-11.webp"
faqs:
  - q: "What does Windows Update error 0x80244010 mean?"
    a: "The update client exceeded the maximum number of round trips allowed to the update server in one session. In practice this means the client's requests kept getting redirected or rejected — most often by stale WSUS registry keys, a proxy loop, or a server that never gives a final answer."
  - q: "Why do I get 0x80244010 on a home PC with no WSUS server?"
    a: "Laptops that were once on a work or school network often keep the WSUS pointer in the registry after leaving. The client keeps asking a dead internal server, gets redirected, retries, and eventually exceeds the trip limit. Registry cleanup fixes it."
  - q: "Can a proxy cause 0x80244010?"
    a: "Yes. A proxy that rewrites or loops update requests can make the client bounce between endpoints until the trip budget is exhausted. Disabling the proxy for a test is a quick way to confirm or rule this out. Corporate laptops returning home are the classic case for this exact pattern."
  - q: "Will this error stop all updates permanently?"
    a: "No — it is a session-level failure, not permanent damage. Once the misdirection is removed (stale keys deleted, proxy fixed, components reset), the next update scan starts with a fresh trip budget and succeeds. If a big feature upgrade is your goal, our [24H2 failure guide](/articles/best-way-to-fix-feature-update-to-windows-11-24h2-failed/) is the companion read."
---

Error 0x80244010 is the update client crying uncle: it tried to talk to the update server, got bounced around, retried, got bounced again, and finally exceeded the maximum number of round trips Windows allows in a single session. Think of it as calling a phone number that keeps forwarding you until the carrier cuts the call. The client is fine; the directions it is following are wrong.

On home laptops, those wrong directions almost always come from one of two places: registry keys left over from a former workplace or school that still point at an internal WSUS server, or a proxy or VPN that mangles the request path. Both are fixable without reinstalling anything, and both are quick to check. The steps below start with the redirection causes because they are the most common, then repair the client state as a backstop.

One caution: do not hammer Check for updates repeatedly while troubleshooting. Each attempt burns through the trip budget and can temporarily lock the client out, making you think a fix failed when it just needs a few minutes of quiet.

## Why this happens

- **Stale WSUS registry keys**: WUServer values from a previous employer or school redirecting to a dead internal server.
- **Proxy request loops**: A proxy rewriting update URLs so the client bounces between endpoints.
- **VPN tunneling quirks**: Split-tunnel misconfigurations sending update traffic down a path that redirects endlessly.
- **Corrupt update metadata cache**: Damaged local metadata causing the client to request invalid update sets repeatedly.
- **Third-party update managers**: Tools that intercept Windows Update traffic and mishandle the redirect protocol.
- **Hosts file or DNS tampering**: Redirects of Microsoft update hostnames, sometimes left by old tweaking tools.
- **Damaged servicing stack**: An outdated client that mishandles the server's redirect responses.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Remove stale WSUS registry keys

This is the number one fix for 0x80244010 on formerly managed laptops. If the registry points the client at an internal server that no longer exists, every scan becomes a redirect loop that burns the trip budget.

1. Press Windows + R, type regedit, and press Enter. Export a backup via File > Export first.
2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate.
3. If the key contains WUServer or WUStatusServer and you are not on a managed corporate network, delete the entire WindowsUpdate key.
4. Reboot and run Check for updates — the client will now talk directly to Microsoft.

### Fix 2: Disable proxy and VPN for the test

Anything that rewrites update traffic can create the bounce pattern behind this code. Removing intermediaries temporarily tells you whether the path or the client is at fault.

1. Disconnect any VPN fully and turn off manual proxy settings in Settings > Network & internet > Proxy.
2. Ensure Automatically detect settings is off during the test as well.
3. Run ipconfig /flushdns in an elevated Command Prompt.
4. Wait five minutes, then Check for updates.

### Fix 3: Inspect the hosts file and DNS

Old tweaking tools and some malware redirect Microsoft hostnames through the hosts file. Even a single stale entry for an update domain breaks the request chain in ways that look exactly like this error.

1. Open Notepad as administrator and open C:\Windows\System32\drivers\etc\hosts.
2. Remove or comment out (with #) any lines mentioning microsoft.com, windowsupdate, or update.microsoft domains that you did not add deliberately.
3. Save the file and run ipconfig /flushdns.
4. Consider switching DNS to a neutral provider temporarily to rule out ISP-level redirection.

### Fix 4: Run the Windows Update troubleshooter

With the redirection causes handled, let the troubleshooter verify the client's own state. It checks service health and repairs common metadata problems automatically.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Windows Update troubleshooter and apply all recommendations.
3. Restart the laptop.
4. Test Check for updates.

### Fix 5: Reset the update components and metadata

Corrupt local metadata makes the client ask for update sets the server cannot resolve, triggering repeated redirects. Clearing the caches forces a clean metadata download on the next scan.

1. In an elevated Command Prompt, run net stop wuauserv, net stop cryptSvc, net stop bits, and net stop msiserver.
2. Run ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
3. Restart the four services and reboot.
4. Run Check for updates and allow the longer first scan to complete.

### Fix 6: Update the servicing stack manually

An old servicing stack can mishandle modern redirect responses, looping where a current client would settle. Installing the latest stack from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) brings the protocol handling up to date.

1. Check your build in Settings > System > About.
2. On the Update Catalog, search for the latest servicing stack update for that build and download the x64 package.
3. Install it and reboot when prompted.
4. Retry the update scan.

### Fix 7: Check with Microsoft support resources

If the trip loop survives every local fix, the problem may be account- or region-specific on the service side. Microsoft's documentation covers the remaining edge cases, including delivery optimization and enterprise configurations.

1. Visit [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) and search for 0x80244010 plus your build number.
2. Try the scan on a different network (phone hotspot) to isolate ISP-level interference.
3. As a final local step, perform an in-place repair install from the Windows 11 ISO, which rebuilds the entire update stack.
4. After the repair, the client's trip budget starts fresh and scans succeed.

## Closing

Error 0x80244010 is a story about bad directions, not a broken car: the client drives in circles because something keeps redirecting it. Remove the stale WSUS keys, straighten the network path, and the loop ends. The lesson worth keeping is that laptops carry their network history with them — a machine that once lived on a corporate domain needs its registry deloused before it can update cleanly at home. Related: our [Windows 10 0x80244010 guide](/articles/how-to-fix-windows-update-error-0x80244010-on-windows-10/) mirrors these steps, and the [24H2 failure recovery guide](/articles/best-way-to-fix-feature-update-to-windows-11-24h2-failed/) covers upgrade-specific server issues.
