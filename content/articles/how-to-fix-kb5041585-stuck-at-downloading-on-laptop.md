---
title: "KB5041585 Stuck at Downloading on a Laptop: Fixes"
slug: how-to-fix-kb5041585-stuck-at-downloading-on-laptop
date: 2026-10-07
categories: ["windows-update"]
tags: ["kb5041585", "stuck downloading", "laptop", "windows update"]
description: "KB5041585 stuck at downloading on your laptop? Diagnose the stall and apply the laptop-specific fixes that get this update flowing again."
thumbnail: "/images/thumbs/how-to-fix-kb5041585-stuck-at-downloading-on-laptop.webp"
faqs:
  - q: "What is KB5041585?"
    a: "KB5041585 is a Windows cumulative update package delivering that month's security and quality fixes. Like all cumulative updates it is large — often over a gigabyte — which makes download stalls more visible than with small patches. The size is also why the fixes focus on the download pipeline: cache, services, bandwidth, and staging space."
  - q: "Why do big updates get stuck downloading on laptops?"
    a: "Large packages multiply every weakness in the download path: a flaky Wi-Fi connection drops more chunks, a small cache corruption has more chances to occur, and staging needs more free disk space. Laptops add their own factors — power-saving Wi-Fi adapters that sleep mid-download and metered hotspot connections. The stall is rarely the update's fault."
  - q: "Does putting my laptop to sleep pause the download?"
    a: "Yes — sleep suspends the network adapter and the update service, freezing the download. Worse, some laptops' aggressive power saving puts the Wi-Fi adapter to sleep even while apparently idle, causing micro-interruptions that corrupt the transfer. During a large download, set the laptop to never sleep while plugged in."
  - q: "Can I download KB5041585 on another computer and transfer it?"
    a: "Yes, and it is a good workaround for a laptop with a terrible connection. Download the MSU from the Microsoft Update Catalog on any PC, copy it via USB, and run it on the laptop. The installer does not care where the file came from as long as the signature is valid and the package matches the laptop's build and architecture."
---

KB5041585 is a big download, and big downloads expose every weakness in a laptop's update pipeline. Wi-Fi power saving that naps mid-transfer, a metered hotspot flag, a cache that has been accumulating damage for months — any of these can freeze the progress bar for hours. The laptop form factor adds its own failure modes that desktops never see.

The repair has two halves: the universal download-pipeline fixes (services, cache, network) and the laptop-specific ones (power settings, Wi-Fi adapter behavior, disk space on small SSDs). This guide covers both, in the order that resolves most stalls fastest.

Work through it methodically. The goal is not just to unstick this KB but to leave the pipeline healthier than you found it.

Laptops fail downloads in ways desktops never do, and that is worth internalizing before you troubleshoot. Every power-saving feature that extends battery life — sleeping radios, dozing adapters, aggressive idle timers — is a potential interruption to a multi-gigabyte transfer. The fixes below treat the laptop as a laptop, not as a small desktop.

## Why this happens

- **USB tethering instability:** Phone-tethered connections drop more packets under sustained load, and the update downloader is less tolerant of it than a browser.
- **Wi-Fi power saving interruptions:** The wireless adapter sleeping mid-download corrupts the transfer and triggers endless restarts.
- **Metered hotspot connections:** Laptops on phone hotspots get flagged metered, throttling update downloads.
- **Sleep during download:** Closing the lid suspends everything, and some laptops never cleanly resume the transfer.
- **Cache corruption:** Damaged partial files fail validation, looping the download.
- **Small SSD staging limits:** 128–256 GB drives with little free space cannot stage a gigabyte-plus package.
- **Hung BITS jobs:** The background transfer queue jams on a bad job and blocks everything behind it.
- **Antivirus traffic inspection:** Real-time scanning of the download stream slows or stalls large transfers. The [24H2-specific KB5041585 guide](/articles/how-to-fix-kb5041585-stuck-at-downloading-in-windows-11-24h2/) covers build-targeted variants.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall and check laptop power state

1. Note the percentage and time in **Settings → Windows Update**.
2. Open **Settings → System → Power & battery** and set **screen and sleep to Never** while plugged in — temporarily.
3. In **Device Manager → Network adapters**, open your Wi-Fi adapter → **Power Management** and uncheck "Allow the computer to turn off this device".
4. Watch Task Manager's network graph for 30 minutes with the lid open.
5. If the percentage never moves with the laptop awake and plugged in, the stall is genuine.

### Fix 2: Restart the download services

1. In an admin Terminal: `net stop wuauserv`, `net stop bits`.
2. Wait 30 seconds, then `net start wuauserv`, `net start bits`.
3. Click **Retry** in Windows Update settings.
4. Keep the laptop awake, plugged in, and on stable Wi-Fi for 20 minutes.
5. Service hangs are the top cause; this alone fixes most stalls.

### Fix 3: Fix the network path

1. Turn **off** Metered connection on your Wi-Fi network.
2. Move closer to the router or switch to a wired connection via USB Ethernet if available — large downloads are far more reliable wired.
3. Disconnect VPNs and disable third-party firewalls temporarily.
4. Disable Delivery Optimization peer downloads in **Windows Update → Advanced options**.
5. Restart and retry. The [step-by-step KB5041585 variant](/articles/how-to-fix-kb5041585-stuck-at-downloading-step-by-step/) details the granular network checks.

### Fix 4: Clear the cache and BITS queue

1. In an admin Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Delete all contents of `C:\Windows\SoftwareDistribution\Download`.
3. Clear stuck BITS jobs with `bitsadmin /reset /allusers` in the same admin prompt.
4. Restart the three services.
5. Click **Check for updates** — the download restarts clean with an empty transfer queue.

### Fix 5: Free staging space on the small SSD

1. Run **Disk Cleanup** as administrator; remove temp files, update cleanup, and delivery optimization files.
2. Uninstall large unused apps until C: has **15 GB free**.
3. Empty the Recycle Bin and clear browser caches.
4. Consider `powercfg /hibernate off` to reclaim gigabytes from hiberfil.sys if you do not use hibernation.
5. Retry the download — staging failures masquerade as download stalls on full drives.

### Fix 6: Run the troubleshooter and reset components

1. Run the **Windows Update** troubleshooter at Settings → System → Troubleshoot → Other troubleshooters.
2. If the stall persists, do the full reset: stop `wuauserv`, `bits`, `cryptsvc`, `msiserver`; rename `SoftwareDistribution` and `catroot2` with `.old`; restart everything.
3. Restart the laptop.
4. Check for updates and observe for 30 minutes.
5. The full reset rebuilds the pipeline that the troubleshooter only patches.

### Fix 7: Install manually via USB transfer

1. On any computer with a good connection, download KB5041585 from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), matching the laptop's build and architecture.
2. Copy the MSU to a USB drive and then to the laptop.
3. Double-click to install, restart when prompted, and verify in Update history.
4. Re-enable your normal sleep settings and Wi-Fi power saving afterward.
5. Confirm future updates download normally — if they do, the stall was transient; if not, the pipeline needs the deeper repair described on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 8: Make the laptop update-friendly long term

A few permanent settings make every future large download uneventful.

1. Create a **power plan** named Updates with sleep set to Never while plugged in; switch to it on Patch Tuesday.
2. In Device Manager, disable **power saving** on the Wi-Fi adapter permanently.
3. Keep at least 20 GB free on C: as a standing rule, not a pre-update scramble.
4. Schedule updates overnight with **active hours** set so restarts never surprise you.
5. Leave the charger connected during any download over a gigabyte — low-battery sleep kills transfers.
6. Review these settings twice a year; Windows feature updates sometimes reset them.
7. A laptop configured this way downloads like a desktop but keeps its battery manners otherwise.

## Closing

Laptop download stalls are usually the laptop being a laptop: sleeping adapters, metered hotspots, tiny SSDs. Fix the power behavior, clear the pipeline, and keep the machine awake and plugged in during big downloads. KB5041585 will finish — and the next large update will too.
