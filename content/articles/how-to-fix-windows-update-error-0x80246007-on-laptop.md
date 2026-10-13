---
title: "Windows Update Error 0x80246007 on Laptop: Complete Fix Guide"
slug: how-to-fix-windows-update-error-0x80246007-on-laptop
date: 2026-09-13
categories: ["windows-update"]
tags: ["windows update error 0x80246007", "sus_e_dm_notdownloaded", "bits download failed", "update not downloaded"]
description: "Error 0x80246007 means the update metadata arrived but the content never downloaded. Reset the download manager, fix BITS, and complete the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80246007-on-laptop.webp"
faqs:
  - q: "What does 0x80246007 mean?"
    a: "It means the update's metadata, its description and catalog entry, downloaded successfully, but the actual payload files were never retrieved. Windows Update knows the update exists and keeps trying to fetch the content, but the download manager never completes the job."
  - q: "Is 0x80246007 a network problem or a Windows problem?"
    a: "It can be either. A stuck BITS queue or corrupted download cache is the most common cause, which is a Windows problem. But proxies, VPNs, and firewalls that block the content servers while allowing the metadata servers produce the identical code."
  - q: "Will resetting Windows Update delete my files?"
    a: "A stuck BITS queue or corrupted download cache is the most common cause, which is squarely a Windows problem. But proxies, VPNs, and firewalls that block the content servers while allowing the metadata servers produce the identical code, so test both sides before deciding where the fault lies."
  - q: "How is 0x80246007 different from 0x8024200d?"
    a: "No. Resetting the update components only renames the SoftwareDistribution and catroot2 cache folders so fresh ones are created. Your documents, programs, and settings are untouched; only the update download cache and its history database are rebuilt from scratch on the next update check."
---

Error 0x80246007 describes a peculiar half-finished state: Windows Update successfully downloaded everything about the update except the update itself. The metadata — the title, the KB number, the description — arrived fine, but when the download manager went to fetch the actual payload, the job never completed.

Think of it as ordering a package and receiving only the shipping label. The system keeps showing the update as available, keeps attempting the download, and keeps failing with the same code because the underlying download machinery is wedged or the network path to the content servers is broken.

Fixing it means unwedging the download machinery first and verifying the network path second. The steps below reset the components in the right order so the content download can finally complete.

One more thing worth knowing before you start: this error is almost never caused by the update itself being broken. The payload on Microsoft's servers is fine; the failure is in your laptop's download machinery or its path to those servers, which is why every fix below targets the machinery rather than the update.

## Why this happens

- **Stuck BITS job queue.** The Background Intelligent Transfer Service can hold a dead download job that blocks every new attempt at fetching the payload.

- **Corrupted download cache.** Damaged state files in SoftwareDistribution make the download manager believe content is already fetched when it is not.

- **Proxy misconfiguration.** A proxy that serves metadata requests but blocks or mangles content-server requests creates exactly this split-brain symptom.

- **Firewall blocking content servers.** Third-party firewalls sometimes allow the update check-in but block the high-volume content delivery endpoints.

- **Incorrect system date and time.** TLS validation to the content servers fails when the clock is significantly wrong, while cached metadata keeps working.

- **Stuck pending.xml.** A wedged servicing transaction can prevent the download manager from staging new content.

- **VPN routing issues.** Split-tunnel or misconfigured VPNs may route metadata traffic correctly while black-holing the content delivery network.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Reset the Windows Update components

This is the heavy hammer that fixes most 0x80246007 cases. It stops every update-related service, renames the cache folders so they are rebuilt from scratch, and restarts the services in the correct dependency order. Renaming rather than deleting the folders is deliberate: if anything goes wrong you can restore the .old folders, though in practice the fresh ones work and the old ones can be deleted after a week.

1. Open Terminal as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Check for updates and let the content download fresh.

### Fix 2: Fix 2: Restart BITS specifically

If a full reset feels like overkill, try restarting just the Background Intelligent Transfer Service. A wedged BITS queue is the single most common cause, and this clears it in seconds. If BITS refuses to restart or immediately stops again, check its dependencies in the service properties; the COM+ Event System and RPC services must be running first.

1. Press Win + R, type `services.msc`, and press Enter.
2. Right-click Background Intelligent Transfer Service and choose Restart.
3. Set its Startup type to Automatic if it is not already, then retry the update.

### Fix 3: Fix 3: Reset the WinHTTP proxy

A stale proxy configuration can send content requests into the void. Resetting the WinHTTP proxy to direct access removes that variable entirely. Some corporate networks genuinely require a proxy, in which case re-enter the correct proxy afterward and verify the update works through it rather than leaving direct access in place.

1. Open Terminal as administrator.
2. Run `netsh winhttp reset proxy` and confirm it reports direct access.
3. Also check Settings, then Network and internet, then Proxy, and disable any manual proxy you do not need.
4. Retry Windows Update.

### Fix 4: Fix 4: Check date, time, and time zone

Content servers validate TLS certificates, and a clock that is hours or days off breaks that validation. Metadata may still work from cache, producing exactly this error's signature. A clock off by even a few hours can break certificate validation, so do not dismiss this step as too simple; it resolves a surprising number of content-download failures.

1. Open Settings, then Time and language, then Date and time.
2. Turn on Set time automatically and Set time zone automatically.
3. Click Sync now, then check for updates again.

### Fix 5: Fix 5: Run the Windows Update troubleshooter

The troubleshooter specifically checks for the stuck-download states behind this code, including pending restart flags and corrupted download registrations. Let it run before moving to manual repairs. The troubleshooter also re-registers the update DLLs in some Windows builds, which repairs the registration damage that occasionally underlies this error.

1. Open Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply everything it suggests.
3. Restart and retry the download.

### Fix 6: Fix 6: Temporarily disable third-party firewall and VPN

Security software that filters traffic can allow the lightweight metadata check while blocking the content delivery. Disabling it for one download attempt isolates the variable cleanly. If you must keep the firewall active for policy reasons, look for an application rule covering svchost.exe's update traffic rather than disabling protection broadly.

1. Disconnect the VPN entirely and disable any third-party firewall.
2. Keep Windows Firewall on so you are not unprotected.
3. Retry the update; if it works, add an exception or update the security software.

### Fix 7: Fix 7: Download the update manually from the Catalog

When the content servers are unreachable through the normal pipeline, fetch the payload yourself. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) serves the same files over a plain browser download. After a successful manual install, unpause automatic updates and confirm the next Patch Tuesday payload downloads normally, proving the pipeline itself is healed.

1. Copy the KB number from update history.
2. Search the catalog, download the x64 .msu, and run it.
3. Restart and verify. If manual downloads also stall, the network-focused fixes in our [0x8024401c timeout guide](/articles/how-to-fix-windows-update-error-0x8024401c-on-laptop/) apply.

## Closing

Error 0x80246007 is frustrating because everything looks like it should work — the update is listed, the check succeeds — but the payload never arrives. Resetting the download components and clearing any proxy or VPN interference resolves the large majority of cases. For the sibling error where the download completes but fails validation, see our [0x8024200d guide](/articles/how-to-fix-windows-update-error-0x8024200d-on-laptop/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers the official component-reset procedure.
