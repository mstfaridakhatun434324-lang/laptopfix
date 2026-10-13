---
title: "How to Fix Windows Update Error 0x8024401C in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x8024401c-in-windows-11-24h2
date: 2026-09-10
categories: ["windows-update"]
tags: ["windows update", "0x8024401c", "error code", "windows 11", "proxy timeout"]
description: "Error 0x8024401C means your proxy timed out on Windows Update requests. Fix or bypass the proxy path with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x8024401c-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x8024401C mean?"
    a: "It is a proxy timeout: Windows Update sent its request through the configured proxy, but the response took too long. Leftover corporate proxy settings, slow proxy auto-detection, VPN-routed proxy hops, and overloaded proxies are the typical causes. Clearing the stale proxy or fixing the proxy configuration resolves it."
  - q: "I do not use a proxy. Why am I getting a proxy timeout?"
    a: "Because a stale proxy is still configured at the system level — often left by a former employer's setup, a VPN client, or an old network. Windows Update uses the WinHTTP system proxy, which is separate from browser settings, so browsing can work fine while updates time out. netsh winhttp reset proxy clears it."
  - q: "Should I just disable proxy auto-detection permanently?"
    a: "On home networks, yes — there is no proxy to detect, and the WPAD lookup only adds delay. On corporate or campus networks that genuinely use a proxy, do not disable it blindly; instead configure the correct proxy explicitly so detection is not needed. Ask the network administrator for the right settings."
  - q: "Can my VPN cause this even when disconnected?"
    a: "Yes, if the VPN client left its proxy settings or virtual adapter behind. Some clients configure a system proxy on connect and fail to remove it on disconnect or uninstall. Check netsh winhttp show proxy for entries naming the VPN provider, reset them, and fully uninstall clients you no longer use."
---

Error 0x8024401C is the proxy variant of a timeout: Windows Update sent its request through the configured proxy and waited, and waited, until the wait itself became the error. On 24H2 laptops this hits users with leftover corporate proxy settings, slow auto-detecting proxies on public Wi-Fi, and VPN clients that proxy traffic through distant servers.

Under the hood, 0x8024401C means the proxy timed out while Windows Update waited for a response. Technically it is WU_E_PT_HTTP_STATUS_REQUEST_TIMEOUT: the request went out through the configured proxy, but the proxy (or the chain beyond it) took too long to respond. The connection is proxied — unlike direct-connection timeouts — which narrows the blame to the proxy path.

The encouraging part: 0x8024401C is one of the better-understood update errors, and the fixes below are ordered from quickest to most thorough. Work through them in sequence — most readers never need the last two.

## Why this happens

- **Leftover corporate proxy settings.** An old work proxy configured at the system level no longer responds.
- **Slow proxy auto-detection.** WPAD lookups hanging on networks without a proxy eat the timeout budget.
- **VPN proxying through distant servers.** Tunneled proxy hops add latency that exceeds the request timeout.
- **Overloaded or dying proxy server.** The configured proxy itself is too slow or half-down.
- **Proxy authentication failing silently.** The proxy demands credentials the update client cannot provide, and the wait times out.
- **Firewall delaying proxied traffic.** Deep inspection on the proxy path slows each request past the limit.
- **Stale WinHTTP proxy entries.** The system proxy store holds entries for a proxy that no longer exists.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the proxy is in the path

0x8024401C specifically implicates the proxy, so verify what the system proxy actually is before changing it — you might find a corporate ghost.

1. In an administrator Command Prompt, run `netsh winhttp show proxy` to see the system-level proxy.
2. Open **Settings > Network & internet > Proxy** and review auto-detect, script, and manual settings.
3. Note any proxy address referencing a company, school, or VPN provider you no longer use.
4. If a stale proxy appears, go to Fix 2. If settings look empty, the WinHTTP store may still hold ghosts — Fix 2 covers that too.

### Fix 2: Remove the stale proxy and go direct

On a home network there is usually no legitimate proxy at all — the stale one is pure leftover. Clearing it lets update traffic go direct and fast.

1. In an administrator Command Prompt, run `netsh winhttp reset proxy`.
2. In **Settings > Network & internet > Proxy**, turn off **Automatically detect settings**, clear any setup script, and turn off manual proxy.
3. Disconnect any VPN completely for the test.
4. Retry the update check immediately — direct connections rarely time out.

### Fix 3: Fix proxy auto-detection hangs

When a proxy is genuinely required (some offices and campuses), the fix is making detection fast and correct rather than removing it.

1. If your network requires a proxy, get the correct PAC script URL or manual address from the network administrator — do not guess.
2. Enter exactly that configuration in **Settings > Network & internet > Proxy** and turn off automatic detection.
3. Test in the browser that the proxy serves pages quickly.
4. Then retry Windows Update through the working proxy.

### Fix 4: Bypass traffic inspection on the update path

Security software that proxies or inspects traffic can push requests past the timeout. A controlled bypass test identifies it.

1. Temporarily disable the web-filtering/proxy component of third-party security software.
2. Retry the update check while it is off.
3. If it succeeds, add Windows Update traffic to the software's exclusions instead of leaving filtering off.
4. Re-enable the component right after the test either way.

### Fix 5: Run the Windows Update troubleshooter

The built-in troubleshooter knows the usual suspects behind 0x8024401C: it checks the service state, the update cache, and the network path to Microsoft's servers, then applies safe automatic repairs. It will not fix deep corruption, but it clears the simple causes in a few minutes and is worth trying before anything manual.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and follow the on-screen prompts.
3. Restart the PC when it finishes, then check for updates again at **Settings > Windows Update**. If 0x8024401C is still there, move on to the next fix.

### Fix 6: Reset the Windows Update components

When 0x8024401C keeps returning no matter what you try, the update engine's own cache is usually the culprit. Stopping the services, renaming the SoftwareDistribution and catroot2 folders, and restarting forces Windows to rebuild its download state from scratch — no personal data is touched.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, and `net stop cryptsvc`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, and `net start cryptsvc`.
4. Go to **Settings > Windows Update**, check for updates, and see whether 0x8024401C is gone.

### Fix 7: Install the update manually from the Microsoft Update Catalog

If the automatic channel keeps failing with 0x8024401C, sidestep it: download the exact KB package and install it by hand. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) hosts every cumulative and servicing-stack update, and a manual install bypasses the broken download pipeline entirely.

1. Open **Settings > Windows Update > Update history** and note the KB number of the update that failed with 0x8024401C.
2. Search that KB number on the Microsoft Update Catalog and download the x64 build for Windows 11.
3. Double-click the downloaded `.msu` file and follow the installer prompts.
4. Restart when asked, then confirm the update appears in your update history.

## Closing

0x8024401C is a timeout with the proxy's fingerprints on it — clear the stale proxy path and updates go direct. Most home users should have no proxy configured at all. If timeouts persist on a direct connection, our [Windows 11 24H2 update error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) covers the direct-timeout codes, and the [troubleshooter](/articles/best-way-to-fix-windows-update-with-troubleshooter/) automates the network checks. Proxy configuration is documented in [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
