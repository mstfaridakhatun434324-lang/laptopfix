---
title: "Windows Update Stuck Downloading on Your HP Laptop? How to Fix It"
slug: how-to-fix-windows-update-stuck-downloading-on-hp-laptop
date: 2026-09-26
categories: ["windows-update"]
tags: ["stuck downloading", "hp laptop", "windows update", "download stuck"]
description: "Windows Update is stuck downloading on your HP laptop? Unstick the download with these HP-aware fixes, from quick resets to manual install."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-downloading-on-hp-laptop.webp"
faqs:
  - q: "How long should I wait before calling a download stuck?"
    a: "Give it at least two hours of the laptop being on and connected before intervening. Large cumulative and feature updates download slowly, and the progress percentage updates in jumps rather than smoothly. If the percentage has not moved at all in two hours while your internet works fine otherwise, it is genuinely stuck."
  - q: "Why do downloads keep stalling on HP laptops specifically?"
    a: "HP laptops commonly run HP Support Assistant alongside Windows Update, and the two can contend over driver downloads. HP's customized network drivers can also interact badly with Delivery Optimization. Quieting HP's tools and updating the network driver from HP usually removes the HP-specific friction."
  - q: "Is it safe to delete stuck update downloads?"
    a: "Yes. Partial downloads in the SoftwareDistribution folder are disposable by design — Windows re-downloads whatever it still needs. Deleting them is the standard fix for corrupted partial downloads and touches nothing else on your system: no personal files, no settings, no installed programs."
  - q: "Should I use HP Support Assistant to update instead?"
    a: "HP Support Assistant is good for HP drivers and BIOS updates, but Windows system updates should still come through Windows Update or the Microsoft Update Catalog. Use each tool for its strength: HP's tool for HP hardware, Microsoft's pipeline for Windows itself."
---

The download starts, climbs to some percentage — 8%, 46%, 99% — and then nothing. Hours pass. Your HP laptop's internet works fine for everything else, but Windows Update sits frozen at the same number like a progress bar in a museum. Restarting sometimes kicks it forward a few percent before it freezes again at a new number. This is the stuck-download pattern, and on HP laptops it usually involves the standard corrupted-cache causes plus HP's own update tooling getting in the way.

Windows does not download updates the way your browser downloads a file. The Background Intelligent Transfer Service fetches the package in chunks, verifies each one, and is designed to pause and resume across reboots and network changes. That design is normally a strength — it is why updates survive lid closes — but it has a failure mode: when a chunk is corrupt, the service resumes from the damaged data instead of discarding it, and every subsequent attempt stalls at the same point. The progress bar is not lying about the percentage; it is accurately reporting that the same broken chunk keeps failing verification.

This guide walks the full recovery in order: confirm the stall, remove HP-specific interference, repair the download pipeline, and — if all else fails — install the update by hand.

## Why this happens

- **Corrupted partial download.** A damaged cached chunk makes every resume attempt stall at the same point.
- **HP Support Assistant contention.** HP's tool downloading drivers simultaneously can conflict with Windows Update's transfers.
- **Metered connection throttling.** Windows limits large downloads on connections it considers metered.
- **VPN, proxy, or network filtering.** Middleboxes breaking the connection to Microsoft's update servers.
- **Low disk space.** Insufficient staging room silently halts the download.
- **BITS service failure.** The Background Intelligent Transfer Service wedged or misconfigured.
- **Outdated HP network driver.** The wireless or Ethernet driver mishandling sustained large transfers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall properly

Make sure you are fixing a real problem.

1. Note the exact percentage in **Settings** > **Windows Update**, wait one hour, and check again. Zero movement confirms the stall.
2. Verify your internet works normally for other tasks — streaming, browsing, speed test.
3. Check free space on C: in **Settings** > **System** > **Storage**; you need several gigabytes free for the download to stage.

### Fix 2: Quiet HP Support Assistant

Remove the HP-specific contention.

1. Open **HP Support Assistant** and pause automatic updates and scheduled tune-ups.
2. If it is mid-download of its own updates, let those finish or cancel them — do not run both updaters at once.
3. Retry Windows Update with HP's tool silent. If the download starts moving, contention was the cause.

### Fix 3: Pause, restart, and resume

Force a clean download state.

1. In **Settings** > **Windows Update**, click **Pause updates** for one week.
2. Restart the laptop (a real restart, not Fast Startup shutdown).
3. Resume updates and click **Check for updates**. The download restarts from zero instead of resuming the poisoned partial file.

### Fix 4: Restart BITS and clear the download cache

Fix the transfer machinery directly. The Background Intelligent Transfer Service is the component that actually moves update bits, and when it wedges — or when the cache it writes to is corrupted — no amount of clicking Retry helps because every attempt reuses the same broken state. Stopping the services, deleting the poisoned partial downloads, and restarting fresh addresses both halves of the problem at once.

1. Open an elevated Command Prompt and run:
   ```
   net stop wuauserv
   net stop bits
   rd /s /q C:\Windows\SoftwareDistribution\Download
   net start wuauserv
   net start bits
   ```
2. Check for updates. The download starts fresh with a clean cache and a restarted transfer service.
3. The same procedure with full detail is in [our guide to resetting stuck update downloads](/articles/how-to-fix-kb5041585-stuck-at-downloading-on-dell-laptop/).

### Fix 5: Check metered settings, VPN, and the network driver

Clear the network-side blockers.

1. Turn off **Metered connection** for your network in **Settings** > **Network & internet**.
2. Disconnect any VPN completely and retry.
3. Update the wireless/Ethernet driver from [HP's support site](https://support.hp.com/us-en) for your exact model — an outdated HP network driver can stall sustained large downloads specifically.

### Fix 6: Install the update manually from the Catalog

Bypass the broken download pipeline.

1. Note the KB number of the stuck update from Update history.
2. Download it from [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and run the `.msu`.
3. This is the same update delivered by a different route. See [how to install a KB manually from the Catalog](/articles/how-to-install-kb-update-manually-from-catalog-on-laptop/) for the full walkthrough.

### Fix 7: Repair the update engine for the long term

Stop this from recurring.

1. Run the Windows Update troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow` from an elevated prompt to repair any servicing damage.
3. Keep HP's drivers current via HP Support Assistant on your own schedule — separate from Windows Update runs. Microsoft's [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the official download troubleshooting path.

## Closing

A stuck download on an HP laptop is a pipeline problem with an HP accent: corrupted partial downloads and transfer service issues underneath, HP Support Assistant contention on top. Quiet HP's tools, clear the cache, restart the transfer services, and the download almost always resumes properly. And when it does not, the Catalog manual install gets the same update onto the machine by a route the broken pipeline cannot block. Going forward, avoid running HP Support Assistant's updates and Windows Update at the same time — sequencing them instead of stacking them prevents the contention behind most HP-specific stalls. A clean, one-updater-at-a-time routine is the simplest long-term prevention. Diagnose by phase, fix in order, and even the most stubborn download eventually finishes.
