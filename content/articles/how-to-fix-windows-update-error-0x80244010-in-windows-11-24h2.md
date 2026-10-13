---
title: "How to Fix Windows Update Error 0x80244010 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80244010-in-windows-11-24h2
date: 2026-09-09
categories: ["windows-update"]
tags: ["windows update", "0x80244010", "error code", "windows 11", "wsus"]
description: "Error 0x80244010 means Windows Update exceeded its server redirect limit. Break the redirect loop by removing stale WSUS and proxy settings."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80244010-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80244010 mean?"
    a: "WU_E_PT_EXCEEDED_MAX_SERVER_TRIPS: the client bounced between servers more times than allowed while resolving where to download from. This is Windows Update going in circles — it tries to work out which server to talk to, gets redirected, redirected again, and finally gives up after too many round-trips."
  - q: "What causes the redirect loop?"
    a: "On personal 24H2 laptops the cause is almost always stale corporate configuration — WSUS keys pointing at a long-dead server that redirects nowhere — or a proxy chain looping the requests. The loop has an author, usually stale policy or proxy config, and finding it decides the fix."
  - q: "Is it safe to delete the WSUS registry keys?"
    a: "Yes, on a personal PC. The WUServer and WUStatusServer values under the WindowsUpdate registry key only matter for corporate WSUS environments. Deleting them returns the client to Microsoft's public servers. Back up the key first via File > Export, as standard registry hygiene."
  - q: "I never worked for a company on this laptop. Why WSUS keys?"
    a: "Tweak tools and debloat scripts sometimes write WSUS-style keys to block updates, and some OEM images ship with them. A previous owner's corporate enrollment can also leave them behind. Whatever the author, dead WSUS pointers are the most common loop authors on home machines."
---

This is Windows Update going in circles. It attempts to determine its server, gets redirected, redirected once more, and ultimately surrenders after excessive round-trips. Formally: WU_E_PT_EXCEEDED_MAX_SERVER_TRIPS — your client ricocheted between servers beyond the permitted count while locating its download source.

On personal 24H2 machines, the culprit is nearly always fossilized corporate configuration — WSUS keys aimed at a defunct server that leads nowhere — or a proxy chain circling the requests. Circling proxies and outdated auto-config scripts ricochet the update protocol until its trip budget runs dry.

Every loop has its author — typically outdated policy or proxy configuration. Identifying the author determines whether the registry, the proxy, or both need editing. The fixes below hunt the author first, because treating a proxy loop with a registry edit wastes an afternoon. Two minutes of diagnosis now saves two hours of wrong repairs later — and on shared machines, it also tells you whether a previous user's corporate leftovers are to blame.

## Why this happens

- **WSUS keys expired.** Residual WUServer entries aim at a server that spins the client in circles.
- **Proxy auto-config circling.** A faulty PAC file or auto-detect chain ricochets update requests between proxies.
- **Corporate proxy leftovers persist.** Antiquated proxy settings from a work network route requests through a dead hop.
- **VPN routing circles.** Misconfigured VPN paths may shuttle update traffic out and back repeatedly.
- **MDM remnants remain.** Partially removed management leaves update-source policies conflicting with defaults.
- **Redirector cache damaged.** Impaired local redirect data sends the client chasing phantom servers.
- **ISP transparent proxy meddling.** Certain providers' transparent proxies botch the update protocol's redirects.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Hunt for the loop's author

Finding the author decides the repair: registry, proxy, or both.

1. Open Settings > Network & internet > Proxy, recording every auto-detect entry, PAC script, or manual proxy.
2. Drop any VPN and observe whether the error shifts — a VPN-born loop disappears instantly, which is the fastest diagnosis in this entire guide.
3. Press Win + R, type `regedit`, and carefully inspect `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` for WUServer values.
4. Note what you find; Fixes 2 and 3 target the two authors, and Fix 1's notes tell you which to attempt first. Skipping this diagnosis is the most common reason people cycle through all seven fixes without progress.

### Fix 2: Remove stale WSUS redirection keys

Deceased WSUS pointers author the most common loops on home hardware. Tweak utilities and debloat scripts are frequent culprits — some inscribe WSUS-style keys deliberately to block updates, leaving the client bouncing off a server that was never real. Their removal restores the client to Microsoft's servers, which never redirect circularly.

1. In regedit, navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`.
2. First export the key through File > Export as a safety backup.
3. Delete the WUServer and WUStatusServer values (and the AU subkey if it forces WSUS).
4. Reboot the PC and check for updates — the round-trips ought to settle on the first attempt.

### Fix 3: Straighten out the proxy chain

A faulty PAC file or auto-detect chain ricochets update requests between proxies until the trip budget is spent.

1. Under Settings > Network & internet > Proxy, disable automatic detection and any setup script, unless the network genuinely requires one.
2. Uninstall legacy VPN clients whose virtual adapters could still steer traffic.
3. From an elevated Command Prompt, execute `netsh winhttp reset proxy` to wipe the system proxy.
4. Retry the update check.

### Fix 4: Purge the network state entirely

Where the configuration appears clean yet the loop endures, stale cached network state is feeding it. A complete flush purges every layer simultaneously.

1. From the elevated prompt, run `netsh winsock reset` and `netsh int ip reset`.
2. Run `ipconfig /flushdns`.
3. Reboot — winsock and IP resets activate only across a restart, so do not skip this step even if everything looks fine.
4. Check for updates and confirm the loop is broken.

### Fix 5: Let the troubleshooter attempt repairs

The troubleshooter detects bad update-source configurations and repairs them automatically.

1. Hoist Settings > System > Troubleshoot > Other troubleshooters on the laptop.
2. Spring the Windows Update entry and see its prompts through to full completion.
3. Restart the PC and re-try the update check.

### Fix 6: Renew the Windows Update components

If the loop survives the configuration fixes, the engine's cached redirect data may be at fault. This is the least common cause — loops are usually authored by live configuration, not cached state — but a reset is cheap and definitive. A full reset clears it.

1. Arrest the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Isolate the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Reinstate the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Request updates and confirm the engine talks to Microsoft directly.

### Fix 7: Install the package manually via the Catalog

A manual install talks to the Catalog directly, bypassing the redirect machinery entirely. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) publishes every cumulative release.

1. Transcribe the KB number from Update history; the troubleshooter page can help if you are unsure where that lives.
2. Retrieve the x64 Windows 11 package in your browser — pick the cumulative update matching your installed build.
3. Launch the `.msu` and reboot if asked. A manual install bypasses the entire redirect chain, so success here confirms the loop lived in the configuration, not the update itself.

## Closing

Redirect loops always have an author — find it, remove it, and updates fly straight. For different connectivity-flavored failures, the [24H2 update-error atlas](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) extends the map, while the [troubleshooter](/articles/best-way-to-fix-windows-update-with-troubleshooter/) automates the network checks. [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents update-source configuration.
