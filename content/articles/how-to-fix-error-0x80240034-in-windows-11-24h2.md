---
title: "How to Fix Windows 11 Update Error 0x80240034 (24H2)"
slug: how-to-fix-error-0x80240034-in-windows-11-24h2
date: 2026-09-15
categories: ["windows-errors"]
tags: ["update error", "0x80240034", "Windows 11 24H2"]
description: "Update downloads keep failing with error 0x80240034 on Windows 11 24H2? Fix the download pipeline with these steps."
thumbnail: "/images/thumbs/how-to-fix-error-0x80240034-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80240034 mean?"
    a: "It's Windows Update's code for WU_E_DOWNLOAD_FAILED — the update downloaded incompletely or the download was interrupted, so the installer refused to proceed. The update files themselves are usually fine; it's the delivery that broke."
  - q: "Why does the same update fail to download repeatedly?"
    a: "Because Windows keeps resuming from a corrupted partial download in its cache. Until you clear the SoftwareDistribution folder, every retry reuses the same broken chunks. Clearing the cache forces a genuinely fresh download."
  - q: "Can my internet connection cause 0x80240034?"
    a: "Yes. Unstable Wi-Fi, VPNs, proxy servers, and metered connections that pause downloads mid-stream are common triggers. If downloads fail at roughly the same percentage each time, suspect the network path rather than Windows itself."
  - q: "Is it safe to delete the SoftwareDistribution folder?"
    a: "Yes, with the update services stopped first. It only holds downloaded update files and the update history database — Windows rebuilds it automatically on the next check. Your personal files and installed updates are not affected."
---
Error 0x80240034 shows up when Windows Update can't finish downloading an update — the progress bar climbs, stalls, and then you're looking at "There were some problems installing updates." On 24H2, with its larger update payloads, this one pops up more than it used to, especially on laptops with flaky Wi-Fi or VPNs running in the background.

The good news: this is a delivery problem, not a system problem. Your Windows installation is fine; the update files just aren't arriving intact. The fixes below go from the quick network checks to rebuilding the entire download pipeline, and one of them will get that update onto your machine.

## Why this happens

- **An interrupted or throttled connection.** Large 24H2 updates take a while to download. If your Wi-Fi drops, your VPN reconnects, or a metered connection pauses the transfer mid-stream, the partial download gets flagged as failed.
- **A corrupted download cache.** Windows resumes interrupted downloads from the SoftwareDistribution folder. If the cached chunks are corrupt, every retry reuses the same broken data and fails the same way.
- **VPN or proxy interference.** Corporate VPNs, privacy VPNs, and proxy configurations can mangle or block the connections Windows Update uses, particularly the background intelligent transfer connections.
- **The BITS service misbehaving.** Background Intelligent Transfer Service is the engine that downloads updates. If it's stuck, disabled, or crashing, downloads fail with exactly this code.
- **Antivirus or firewall blocking the download.** Overzealous security software sometimes quarantines update chunks or blocks the update servers outright.
- **Disk space running low.** If the drive fills up mid-download, the transfer can't complete. 24H2 updates need several gigabytes of breathing room beyond the download size itself.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Stabilize the connection and retry cleanly

Rule out the network before touching Windows internals.

1. Disconnect from any **VPN** completely — don't just pause it, disconnect it. Also disable any proxy under **Settings > Network & internet > Proxy**.
2. If you're on Wi-Fi, move closer to the router or, better, plug in with an **Ethernet cable** for the duration of the download.
3. Check that your connection isn't set as metered: **Settings > Network & internet > Wi-Fi**, click your network, and make sure **Metered connection** is off.
4. Go to **Settings > Windows Update**, click **Retry** or **Check for updates**, and watch whether the download now progresses past the point where it used to fail.

### Fix 2: Run the Windows Update troubleshooter

It resets the download-related services and policies automatically.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and let it finish.
3. Restart the laptop even if it says no problems were found — the troubleshooter restarts services as part of its run.
4. Try the update again. If 0x80240034 returns, the cache is likely corrupt, which Fix 3 handles.

### Fix 3: Clear the SoftwareDistribution cache

This is the fix that works most often for 0x80240034. You're deleting the broken partial download so Windows starts fresh.

1. Press **Win + X** and open **Terminal (Admin)**.
2. Stop the services that lock the cache folder:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
3. Delete the contents of the download cache:
   `del /q /s C:\Windows\SoftwareDistribution\Download\*`
   (This removes downloaded chunks only, not your update history.)
4. Restart the services:
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
5. Go to **Settings > Windows Update > Check for updates** and let it download from zero. A fresh download from clean cache succeeds the large majority of the time.

### Fix 4: Reset the BITS service

If downloads still fail, the download engine itself may need attention.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Background Intelligent Transfer Service** in the list and double-click it.
3. Set **Startup type** to **Automatic**, click **Start** if it's stopped, then click **OK**.
4. While you're here, check **Windows Update** the same way — it should also be **Automatic** and running. A disabled Windows Update service produces a whole family of errors; our guide to [error 0x80070422](/articles/how-to-fix-error-0x80070422-in-windows-11-24h2/) covers the service-disabled scenario in depth.

### Fix 5: Free up disk space

A full drive kills downloads silently.

1. Open **Settings > System > Storage** and check your free space. You want at least **10 GB free** for a smooth 24H2 update.
2. Click **Temporary files**, tick everything (especially **Windows Update Cleanup** and **Delivery Optimization Files**), and click **Remove files**.
3. Run **Disk Cleanup** as well: press **Win + R**, type `cleanmgr`, select your system drive, click **Clean up system files**, and remove old update backups.
4. Retry the update download with the new breathing room.

### Fix 6: Temporarily disable third-party antivirus

If a security suite is quarantining update chunks, this proves it.

1. Open your antivirus and turn off **real-time protection** temporarily (most have a 15–30 minute snooze option — use that, don't uninstall anything).
2. Also check its firewall section for anything blocking Windows Update or Microsoft servers, and allow those.
3. Retry the download immediately while protection is snoozed.
4. Re-enable protection right after, whether or not the download worked. If disabling it fixed the problem, add Windows Update to the antivirus's exclusions so you don't have to repeat this dance monthly.

### Fix 7: Download the update manually from the Microsoft Update Catalog

When the automatic pipeline won't cooperate, go around it.

1. Find the failing update's **KB number** in **Settings > Windows Update > Update history**.
2. Search for it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and download the x64 `.msu` file (confirm your architecture under **Settings > System > About > System type**).
3. Run the `.msu` file — it installs directly without using BITS or the SoftwareDistribution cache at all.
4. Restart when prompted. Manual installation bypasses every download-related failure mode in one move, which is why it's the reliable fallback for stubborn 0x80240034 cases.

## Closing

Error 0x80240034 is almost never a sign of real system damage — it's Windows telling you the delivery truck broke down, not that the warehouse burned. If your update downloads fine but then fails during installation, that's a different problem — see our [Windows 11 installation failure guide](/articles/windows-11-installation-failed-troubleshooting/). In practice, clearing the download cache (Fix 3) or switching to a manual catalog download (Fix 7) resolves it nearly every time. If you hit this repeatedly on the same laptop, look hard at your network setup: a VPN that drops every hour or a metered connection will keep producing this error no matter how many times you clear the cache.
