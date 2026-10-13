---
title: "KB5055523 Stuck Downloading on Windows 11? Get It Moving"
slug: how-to-fix-kb5055523-stuck-downloading-on-windows-11
date: 2026-09-07
categories: ["windows-update"]
tags: ["kb5055523", "stuck downloading", "windows 11", "delivery optimization"]
description: "Fix KB5055523 stuck downloading on Windows 11: unstick BITS and Delivery Optimization, clear the cache, and finish the download."
thumbnail: "/images/thumbs/how-to-fix-kb5055523-stuck-downloading-on-windows-11.webp"
faqs:
  - q: "How can I tell whether the download is stuck or just slow?"
    a: "Note the exact percentage, then watch Task Manager's network graph for thirty minutes. Steady traffic means slow — leave it alone. Zero traffic with an unmoving percentage means stuck, and no amount of waiting fixes a stuck download. The distinction matters because the fixes are different."
  - q: "What is BITS and why does it matter here?"
    a: "BITS — the Background Intelligent Transfer Service — is the download engine Windows Update uses. It queues download jobs, throttles them politely, and resumes after interruptions. When its queue wedges, the progress bar freezes even though everything else looks fine. Restarting BITS is often the entire fix."
  - q: "Should I leave Delivery Optimization on or off permanently?"
    a: "Off is the safer default on home networks with one Windows PC, since peer-to-peer adds failure modes for little benefit. On a LAN with many Windows machines, local peer sharing genuinely saves bandwidth. Choose based on your network, not on habit."
  - q: "Can a full hard drive stall a download without any error?"
    a: "Yes, and it happens constantly. The downloader needs room to stage the package, and when space runs out it stalls rather than erroring clearly. Keep at least 15 GB free on the system drive and half of all mysterious download stalls disappear."
---

KB5055523 frozen mid-download on Windows 11 is a pipeline stall, not a broken update. The progress bar lies by omission: it shows you a percentage but not the wedged BITS job, the poisoned cache chunk, or the peer-to-peer peer that stopped responding behind it. Your job is to find which of those it is and clear it.

The sequence below starts with the thirty-second checks and escalates to the cache reset and manual install. Most stuck downloads resolve by Fix 4; the later steps exist for the stubborn ones.

One important distinction before you begin: a download that is genuinely slow still shows network activity in Task Manager and a percentage that creeps upward over an hour. A stuck download shows neither. Do not waste an afternoon waiting on a stuck download hoping it is slow — verify with Task Manager once, then start fixing. Also plug in the charger and confirm at least 15 GB free on C:, because a nearly full drive stalls downloads silently and mimics every network symptom.

## Why this happens

- **Wedged BITS job:** The background download job stalls and never times out on its own.
- **Corrupt partial chunk:** An interrupted piece of the package sits in the cache and fails verification on every resume.
- **Delivery Optimization peer stall:** A P2P peer stops responding and the downloader waits on it indefinitely.
- **Metered connection:** Windows quietly pauses the download on connections flagged as metered.
- **DNS/proxy interference:** Broken name resolution or a filtering proxy kills the CDN connections mid-stream.
- **Antivirus download inspection:** Real-time scanning serializes or blocks the incoming package stream.
- **Low disk space:** No room to stage the file, so the downloader stalls instead of failing loudly.
- **Corrupt DataStore database:** The local update database loses track of download state. The same database corruption sits behind the [KB5036893 Win11 stall](/articles/how-to-fix-kb5036893-stuck-downloading-on-windows-11/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall properly

1. Record the exact percentage and the time in **Settings → Windows Update**.
2. Open **Task Manager → Performance** and watch the network graph for a full 30 minutes of normal use.
3. No meaningful traffic plus an unmoving percentage equals stuck — proceed with the fixes.
4. Steady traffic means slow: check back in an hour instead of resetting things prematurely.
5. Also confirm at least 15 GB free on C: before blaming the network.

### Fix 2: Pause and resume to reset the BITS job

1. In **Settings → Windows Update**, click **Pause updates** for one week.
2. Wait two full minutes — this lets the stalled BITS job tear down completely.
3. Click **Resume updates**, then **Check for updates**.
4. Watch the percentage for 15 minutes; a fresh BITS job often starts moving immediately.
5. If it freezes at the identical percentage, the cache chunk itself is bad — continue.

### Fix 3: Disable Delivery Optimization peer sharing

1. Go to **Settings → Windows Update → Advanced options → Delivery Optimization**.
2. Turn off **Allow downloads from other PCs**.
3. Retry the download — a direct pull from Microsoft removes bad peers from the equation.
4. If the percentage starts climbing, leave P2P off on this network permanently.
5. This single toggle resolves a large fraction of home-network stalls.

### Fix 4: Clear the download cache

1. Elevated Command Prompt: `net stop wuauserv` and `net stop bits`.
2. Delete everything inside `C:\Windows\SoftwareDistribution\Download`.
3. Restart both services: `net start wuauserv`, `net start bits`.
4. Check for updates — the download restarts from 0% with verified-clean state.
5. A fresh, complete download is what you want; do not mourn the discarded partial file.

### Fix 5: Rule out metered, DNS, and proxy issues

1. **Settings → Network & internet → Wi-Fi**: open your network and turn **Metered connection** off.
2. Check **Proxy** settings for any unexpected manual configuration and disable VPNs temporarily.
3. If browsing is flaky generally, switch DNS to a reliable public resolver in the adapter settings.
4. Retry the download after each network change to isolate the culprit.
5. Try a phone hotspot as a control test — if the download flies there, your main network is the problem.

### Fix 6: Reset the network stack

1. Elevated prompt: `netsh winsock reset` and `netsh int ip reset`, then reboot.
2. After reboot: `ipconfig /flushdns`.
3. Reconnect and retry the download on the clean stack.
4. Socket-level stalls survive pause/resume cycles but not a full stack reset.
5. Microsoft documents these commands on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Test with security software paused

1. Temporarily disable third-party antivirus real-time protection.
2. Retry the download with only Windows Security active.
3. If it moves, add an exclusion for `C:\Windows\SoftwareDistribution` before re-enabling protection.
4. Never leave protection off longer than the test.
5. Download-inspection features are the usual offender when antivirus is the cause.

### Fix 8: Install KB5055523 manually from the catalog

1. Download the x64 .msu for KB5055523 from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Your browser replaces the entire stuck Windows Update pipeline.
3. Run the package, reboot, verify in Update history.
4. If even the manual download stalls, the fault is the network or ISP — try another network to confirm.
5. For the broader stuck-download playbook beyond one KB, see the [general Windows 11 guide](/articles/how-to-fix-windows-update-stuck-downloading-in-windows-11-24h2/).

## Closing

KB5055523 stuck downloading on Windows 11 is a wedged pipeline in nearly every case: a stalled BITS job, a corrupt cache chunk, or peer-to-peer sharing misbehaving. Pause and resume, kill P2P sharing, clear the download cache, and reset the network stack — in that order. When Windows Update will not cooperate, the catalog's standalone installer finishes the job in minutes. Then keep the pipeline healthy: P2P off on simple home networks, 15 GB free minimum, metered flags only where you truly pay per megabyte, and a monthly habit of checking for updates instead of letting them pile into giant catch-up downloads that stall most often.
