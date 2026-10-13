---
title: "How to Fix Windows Update Error 0x80246007 on a Dell Laptop"
slug: "how-to-fix-windows-update-error-0x80246007-on-dell-laptop"
date: 2026-09-27
categories: ["windows-update"]
tags: ["windows update", "0x80246007", "bits", "download error", "dell laptop"]
description: "Error 0x80246007 means update content never finished downloading on your Dell laptop. Repair BITS and the download pipeline to fix it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80246007-on-dell-laptop.webp"
faqs:
  - q: "What is BITS and why does it matter?"
    a: >
      BITS — the Background Intelligent Transfer Service — is the Windows
      component that downloads updates in the background using idle
      bandwidth. If it is stopped, misconfigured, or crashing, update
      downloads cannot start, producing errors like 0x80246007. It is
      designed to transfer files without disrupting your work, throttling
      itself when you need bandwidth. Restarting it and clearing its queue
      fixes most download-side update failures.
  - q: "Why does the update show as available but never download?"
    a: >
      Windows received the update metadata (the ‘what’) but the BITS
      transfer of the actual files (the ‘payload’) never completed. The
      error fires when the installer goes looking for files that were
      never fetched. Common blockers are a stopped BITS service, a metered
      connection flag, or a firewall killing the transfer. Fix the
      download path, and the pending update will finally fetch its files.
  - q: "Can a VPN really break Windows Update?"
    a: >
      Yes. VPNs and strict firewalls can interrupt or block the long-lived
      HTTP connections BITS uses. Disconnecting the VPN for the download
      is a legitimate diagnostic step recommended by many support
      engineers. The tunnel adds latency, can drop idle connections, and
      sometimes routes update traffic through regions where the CDN
      performs poorly. If updates work with the VPN off, check its
      split-tunneling or protocol settings.
  - q: "How do I know if my connection is metered?"
    a: >
      In Settings > Network & internet, select your connection and look
      for the ‘Metered connection’ toggle. Mobile hotspots are often
      auto-marked metered, which silently blocks large update downloads.
      Windows does this to save your mobile data, but it also stalls
      updates indefinitely with errors like 0x80246007. Turn the toggle
      off while on unlimited Wi-Fi, or use the hotspot only for the
      download and switch back after.
---

Error 0x80246007 (SUS_E_DM_NOTDOWNLOADED) reports that the update content was never actually downloaded — the update metadata arrived, but the payload behind it did not. Windows Update knows an update exists, shows it as available or pending, and then fails when it tries to fetch the files. The download stage, handled by the Background Intelligent Transfer Service (BITS), is where this breaks.

On Dell laptops the classic triggers are a disabled or crashing BITS service, a metered connection silently blocking large downloads, or a firewall or VPN that kills the transfer mid-stream. Because BITS transfers in the background at low priority, the failure can be silent for hours: the update just sits at 0% or fails immediately with this code when you force a retry.

Fixing it means making the download path healthy again — service, network, and cache — and then letting the update fetch its files. The order below starts with the most common BITS problems and ends with a manual install that skips the downloader entirely. If you are dealing with a related symptom instead, see [the 0x8024200D re-download error](/articles/how-to-fix-windows-update-error-0x8024200d-on-dell-laptop/) and [update errors after a clean install on Dell](/articles/how-to-fix-windows-update-error-after-clean-install-on-dell-laptop/).

Because BITS works quietly in the background, this error can be confusing — the update appears in the list, you click retry, and it fails without any visible download ever happening. What is actually happening is that the transfer never starts: the service is stopped, the connection is flagged metered, or a filter kills each attempt. The fixes below restore each link in that chain, starting with the BITS service itself since it is the single most common culprit.

## Why this happens

- **BITS service disabled or crashing** the background downloader Windows Update depends on is not running.

- **Metered connection blocking downloads** Windows refuses large downloads on connections marked metered.

- **Firewall or VPN interrupting transfers** security software kills the long-lived BITS connections.

- **Corrupt BITS queue** a wedged job in the transfer queue blocks everything behind it.

- **Corrupt SoftwareDistribution cache** metadata says downloaded, files say otherwise.

- **Proxy misconfiguration** BITS cannot reach the update servers through a bad proxy.

- **Low disk space aborting the transfer** downloads silently stop when the drive fills mid-transfer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify and restart the BITS service

BITS is the engine behind update downloads; if it is stopped, nothing downloads. BITS is easy to overlook because it never shows a window, but every update download flows through it; if the service is stopped or set to Disabled, nothing you do in Windows Update will produce a single downloaded byte until it runs again.

1. Press Win + R, type services.msc, and press Enter.

2. Find ‘Background Intelligent Transfer Service’.

3. Set its Startup type to Automatic (Delayed Start).

4. Click Start (or Restart if already running).

5. Retry Windows Update.

### Fix 2: Turn off the metered connection flag

A metered flag tells Windows to avoid big downloads — exactly what triggers this error. This flag is the silent killer on laptops that tether to phones: Windows marks hotspots metered automatically, then refuses large downloads indefinitely without ever explaining why the update will not start.

1. Open Settings > Network & internet.

2. Select your Wi-Fi network or Ethernet connection.

3. Turn off ‘Metered connection’.

4. Go to Settings > Windows Update and click Retry.

### Fix 3: Clear the BITS queue and update cache

A stuck transfer job can jam the queue indefinitely. The bitsadmin reset command clears jobs for every user on the machine, which matters because a stuck job from another account can jam the shared queue just as thoroughly as one of your own.

1. Open Command Prompt as administrator.

2. Run: bitsadmin /reset /allusers to clear all BITS jobs.

3. Run: net stop wuauserv and net stop bits.

4. Delete the contents of C:\Windows\SoftwareDistribution\Download.

5. Run: net start bits and net start wuauserv, then retry.

### Fix 4: Check proxy settings

A leftover or broken proxy is a classic silent download killer. If your workplace requires a proxy, get the exact address and port from IT rather than guessing; a half-remembered proxy setting causes more update failures than having no proxy at all.

1. Open Settings > Network & internet > Proxy.

2. Turn off ‘Use a proxy server’ unless your network genuinely requires one.

3. Ensure ‘Automatically detect settings’ is on.

4. Retry the update.

### Fix 5: Temporarily disable VPN and firewall filtering

Test whether security software is the thing aborting transfers. Test methodically: disconnect the VPN first and retry, then disable the firewall filter and retry again, so you know exactly which layer was responsible.

1. Disconnect any VPN completely.

2. If you use third-party firewall software, disable its web filtering temporarily.

3. Retry the update download.

4. Re-enable protection once the download completes.

### Fix 6: Run the Windows Update troubleshooter

It specifically checks the BITS and download-related services. The troubleshooter specifically validates the BITS and download-related services, so it is more targeted here than it is for generic update errors.

1. Open Settings > System > Troubleshoot > Other troubleshooters.

2. Run the Windows Update troubleshooter.

3. Apply its fixes and restart the laptop.

4. Retry the update.

### Fix 7: Install the update manually

When the downloader will not cooperate, a direct download ends the standoff. A browser download does not use BITS at all, which is precisely why it succeeds in cases where the automatic downloader is fundamentally wedged.

1. Find the KB number in Settings > Windows Update > Update history.

2. Download it from the Microsoft Update Catalog in your browser.

3. Run the .msu installer and restart when prompted.

4. Confirm it is listed in update history afterward.

## Closing

Error 0x80246007 is a download that never happened, so the whole fix is about the download path: a running BITS service, an unmetered connection, and a clean cache. Once transfers can actually complete, this error disappears and rarely comes back. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
