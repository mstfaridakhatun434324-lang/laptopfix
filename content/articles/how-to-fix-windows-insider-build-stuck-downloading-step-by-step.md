---
title: "Windows Insider Build Stuck Downloading: A Step-by-Step Fix"
slug: how-to-fix-windows-insider-build-stuck-downloading-step-by-step
date: 2026-09-29
categories: ["windows-update"]
tags: ["windows insider", "stuck downloading", "preview build", "bits", "step by step"]
description: "An Insider preview build frozen mid-download? Follow this ordered, step-by-step repair sequence to get the download moving again."
thumbnail: "/images/thumbs/how-to-fix-windows-insider-build-stuck-downloading-step-by-step.webp"
faqs:
  - q: "How do I know the download is stuck and not just slow?"
    a: "Open Task Manager's Performance tab and watch the network graph. Steady download traffic means it's still working even if the percentage barely moves. If network activity sits at zero for over an hour while the percentage stays frozen, and you have at least 15 GB free on C:, the download is genuinely stuck and this guide's steps apply."
  - q: "Will clearing the update cache delete the part already downloaded?"
    a: "Yes — clearing the SoftwareDistribution cache removes partially downloaded data, so the build restarts from 0%. That's intentional: the partial data is usually the corrupted part causing the stall. A clean download from scratch is faster than a wedged one limping along, and it almost always completes normally."
  - q: "Do Insider builds download differently from regular updates?"
    a: "Yes. Insider builds are full OS builds of 4 to 6 GB rather than small deltas, so they stress the download pipeline much harder and take far longer. They also go through longer verification phases where the progress bar doesn't move. That's why the BITS service and the update cache — both covered here — matter so much more for Insider flights."
  - q: "What if the build downloads but fails to install?"
    a: "That's a different problem in the install phase, not the download phase. Finish this guide first to get a clean download. If installation then fails, check the error code in Update history and look at setuperr.log in C:\\$Windows.~BT\\Sources\\Panther. Driver conflicts and low disk space are the usual install-phase culprits."
---

A Windows Insider build download that freezes halfway is a test of patience like no other. The files are huge — four to six gigabytes — the progress bar lies to you during verification phases, and when it genuinely stalls, there is no error message explaining why.

The fix is a sequence, and order matters. Each step below eliminates one layer of the download pipeline, from the simplest nudge to a full reset. Do not skip ahead: the early steps fix most stalls in minutes, and the later ones are only needed when the early ones fail.

Follow the steps exactly as written. Work through these in order — diagnose first, then act.

## Why this happens

- **BITS transfer deadlock.** The Background Intelligent Transfer Service wedges on large multi-GB transfers and stops requesting new chunks.
- **Corrupted download cache.** Damaged chunks or metadata make the downloader retry the same data endlessly.
- **Delivery Optimization pulling from bad peers.** Peer-to-peer sources can feed slow or corrupt chunks that stall assembly.
- **Metered connection flag.** Windows silently pauses large downloads on connections marked as metered.
- **Bandwidth throttling.** Delivery Optimization caps can stretch a 5 GB download across an entire day.
- **Insufficient disk space.** The download freezes when C: runs out of room, often without a clear warning.
- **Antivirus scanning every chunk.** Real-time scanning of gigabytes of downloaded data can stall the transfer for hours.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall with Task Manager

Open Task Manager with Ctrl+Shift+Esc and look at the Performance tab's network graph. If you see sustained download traffic, the build is still coming — Insider downloads have long verification phases where the percentage does not move, and that is normal.

Also check Settings, System, Storage for at least 15 GB free on C:. Only proceed when the network has been flat at zero for a full hour and disk space is fine. Write down the frozen percentage; you will compare against it after each fix to confirm movement. The HP-specific version of this problem is covered in the guide to [Insider builds stuck downloading on HP laptops](/articles/how-to-fix-windows-insider-build-stuck-downloading-on-hp-laptop/), which adds manufacturer-utility angles.

### Fix 2: Pause and resume to reset the transfer

Go to Settings, Windows Update, and click "Pause for 1 week." Count to thirty, then click "Resume updates." This kills the current BITS transfer session and starts a new one while keeping downloaded data.

Watch for 15 minutes. If the percentage moves — even slowly — the stall was a wedged session and you are fixed. If it snaps back to the exact same frozen number and sits there, the cached data is corrupt and the next step is required.

### Fix 3: Restart the BITS and Windows Update services

A service-level restart clears locks that pause-resume sometimes misses.

1. Press Win+R, type `services.msc`, and press Enter.
2. Right-click "Background Intelligent Transfer Service" and choose Restart.
3. Right-click "Windows Update" and choose Restart.
4. If either service shows as Disabled, double-click it, set Startup type to Manual, and start it.

Return to Windows Update and click "Check for updates." Give it 20 minutes. A transfer that was blocked on a service deadlock usually resumes here.

### Fix 4: Clear the SoftwareDistribution download cache

When the cache holds corrupt chunks, only a clean slate works.

1. Open Command Prompt as administrator.
2. Run: `net stop wuauserv`
3. Run: `net stop bits`
4. In File Explorer, delete everything inside `C:\Windows\SoftwareDistribution\Download`.
5. Run: `net start bits`
6. Run: `net start wuauserv`
7. In Settings, Windows Update, click "Check for updates."

The download restarts from 0% — expected. Monitor it for 30 minutes: steady progress means the corrupt data is gone. If it freezes at the same spot again, the problem is deeper than the cache.

### Fix 5: Force direct download and unmeter the connection

Peer-to-peer sources can stall large builds. Go to Settings, Windows Update, Advanced options, Delivery Optimization, and turn off "Allow downloads from other PCs." This forces a direct pull from Microsoft's servers.

Then check your connection: Settings, Network & internet, Wi-Fi (or Ethernet), click your network, and make sure "Set as metered connection" is off. Under Delivery Optimization's Advanced settings, confirm no aggressive bandwidth cap is set. Retry the download — direct-from-Microsoft transfers are the most reliable path for multi-GB builds. Microsoft documents Delivery Optimization behavior in their [Windows support resources](https://support.microsoft.com/en-us/windows).

### Fix 6: Exclude the cache from antivirus scanning

Real-time antivirus scanning each downloaded chunk is a classic slowdown for 5 GB builds. Open your antivirus settings and add an exclusion for `C:\Windows\SoftwareDistribution` — or temporarily pause real-time protection during the download.

Do not leave protection off permanently; re-enable it once the build installs. If you use only Windows Security, add the exclusion under Virus & threat protection, Manage settings, Exclusions. After excluding, pause and resume the download once more to let the transfer run unimpeded. If downloads stall but your real issue is broader slowness, the [slow Windows 11 after update guide](/articles/best-way-to-fix-windows-11-slow-after-update/) covers system-wide performance.

### Fix 7: Reset all Windows Update components

The full reset, for stalls that survive everything above:

1. Open Command Prompt as administrator.
2. Stop four services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`
3. Rename the folders:
   - `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   - `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`
5. Check for updates and let the Insider build download fresh.

This rebuilds the entire download pipeline. In the rare case the build still will not download, re-check your Insider enrollment under Settings, Windows Update, Windows Insider Program — a damaged flight assignment needs re-enrollment, not more cache clearing.

## Closing

Insider build downloads stall for mechanical reasons: wedged transfers, corrupt caches, throttled or metered connections, and overzealous antivirus. The step-by-step sequence above clears them in likelihood order, and the full component reset at the end resolves nearly everything else. Once the build is downloading steadily, leave it alone — big builds reward patience more than intervention.
