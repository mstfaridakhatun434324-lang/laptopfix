---
title: "KB5055523 Stuck Downloading? Step-by-Step Fix"
slug: how-to-fix-kb5055523-stuck-downloading-step-by-step
date: 2026-10-11
categories: ["windows-update"]
tags: ["kb5055523", "stuck downloading", "step by step", "windows update"]
description: "The definitive step-by-step repair for KB5055523 stuck downloading: verify, restart, clear, reset, and finish with a verified manual install."
thumbnail: "/images/thumbs/how-to-fix-kb5055523-stuck-downloading-step-by-step.webp"
faqs:
  - q: "What is the correct order for fixing a stuck KB5055523 download?"
    a: "Verify the stall with measurements first, then restart the update services, then remove network obstructions like metered flags and VPNs, then clear the download cache, then reset the full update components, and finally install manually from the catalog. Each step is more invasive than the last, which is why the order matters — most stalls resolve in the first three steps."
  - q: "How do I verify each step actually worked?"
    a: "After every fix, return to Settings then Windows Update, retry or check for updates, and observe for 20 to 30 minutes while noting the percentage at the start and end. Movement means progress — let it finish. No movement means the step did not address your blocker, so continue to the next one. This checkpoint discipline is what makes step-by-step repair effective."
  - q: "Why does KB5055523 keep failing even after a cache clear?"
    a: "If a cache clear does not help, the corruption is deeper than the download folder: the update database, the BITS job queue, or the component registrations may be damaged. The full component reset — renaming SoftwareDistribution and catroot2 — addresses those layers. Persistent failure past that point usually means network-level interference, like a proxy altering traffic, which the manual install bypasses."
  - q: "After the manual install, how do I confirm everything is healthy?"
    a: "Check three things: Update history shows KB5055523 as successfully installed, winver shows the expected build number, and Settings then Windows Update completes a fresh check without errors or phantom downloads. If all three pass, the pipeline is healthy. Run one more check the next day to confirm normal behavior before considering the issue closed."
---

This is the methodical, no-shortcuts version of the KB5055523 download repair. Every step in order, every checkpoint explicit, every escalation justified. If you follow it exactly — verifying after each step instead of running everything at once — you will find the exact layer where your download was stuck, fix it, and know that you fixed it.

The philosophy is simple: a stuck download is a pipeline with one broken segment. Random fixes sometimes hit it; ordered fixes always find it. The seven steps below move from observation through gentle restarts, cache surgery, full resets, and finally the manual installation that succeeds regardless.

Budget forty-five minutes. Keep the laptop plugged in, awake, and on a stable connection throughout.

This guide is deliberately slower than the quick-fix versions. Each step ends with a checkpoint because the goal is not just to fix the download but to identify which layer was broken. That knowledge is reusable: the next stuck download, on this or any machine, starts from evidence instead of guesses.

## Why this happens

- **Validation-failure loop:** Corrupted chunks fail checksums and restart the transfer repeatedly.
- **Service deadlock:** Wuauserv or BITS hangs with progress frozen on screen.
- **Network policy interference:** Metered flags, VPNs, proxies, and firewalls silently degrading the transfer.
- **BITS queue jam:** A stuck background job blocking the KB behind it.
- **Database corruption:** The update database misdirecting the downloader to wrong byte ranges.
- **Staging space exhaustion:** The drive unable to hold the package as it lands.
- **Peer-source stall:** Delivery Optimization waiting on dead peers. The [HP-focused KB5055523 guide](/articles/how-to-fix-kb5055523-stuck-downloading-on-hp-laptop/) adds vendor-specific follow-through.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall with hard evidence

1. Record the percentage in **Settings → Windows Update** and the exact time.
2. Open **Task Manager → Performance** and watch the network graph for five minutes — note any traffic.
3. Check **Task Manager → Processes** for disk writes from Service Host processes.
4. Wait 45 minutes and compare the percentage; also confirm at least 10 GB free on C:.
5. **Checkpoint:** identical percentage plus zero network and disk activity for the full period means a confirmed stall. Anything else means wait longer.

### Fix 2: Restart the pipeline services

1. Open an admin Terminal.
2. Run `net stop wuauserv`, then `net stop bits`, waiting for each to confirm.
3. Wait 30 seconds, then run `net start wuauserv` and `net start bits`.
4. In Windows Update settings, click **Retry**.
5. **Checkpoint:** observe 20 minutes. Percentage movement means a hung service was the cause — let it complete. Frozen at the same point means cache corruption — continue.

### Fix 3: Remove every network obstruction

1. In **Settings → Network & internet → Wi-Fi**, open your network and turn **off** Metered connection.
2. Fully disconnect any **VPN** — not just pause it.
3. Temporarily disable third-party antivirus web filtering and firewall features.
4. In **Windows Update → Advanced options → Delivery Optimization**, turn off peer downloads.
5. Restart the laptop, retry the download, and **checkpoint** after 20 minutes. The [Windows 11 download-path variant](/articles/how-to-fix-kb5055523-stuck-downloading-on-windows-11/) covers OS-specific network settings.

### Fix 4: Clear the cache and reset BITS

1. In an admin Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Delete everything in `C:\Windows\SoftwareDistribution\Download`.
3. Run `bitsadmin /reset /allusers` to purge jammed transfer jobs.
4. Restart the three services with `net start` commands.
5. Click **Check for updates** and **checkpoint** after 30 minutes — most real stalls end here with a clean cache and empty queue.

### Fix 5: Run the troubleshooter, then the full reset

1. Run the **Windows Update** troubleshooter at Settings → System → Troubleshoot → Other troubleshooters; apply its fixes.
2. **Checkpoint:** retry the download for 20 minutes. If still stuck, proceed to the full reset.
3. In an admin Terminal, stop `wuauserv`, `bits`, `cryptsvc`, `msiserver`.
4. Rename `C:\Windows\SoftwareDistribution` → `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` → `catroot2.old`; restart the services; restart the laptop.
5. **Checkpoint:** check for updates and observe 30 minutes. This rebuilds the entire pipeline.

### Fix 6: Install KB5055523 manually from the catalog

1. Confirm the exact KB number from Update history.
2. Download the matching package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) — correct build, correct architecture.
3. Install any listed servicing stack update first and restart.
4. Double-click the KB5055523 MSU, approve the UAC prompt, and let the standalone installer complete; restart when asked.
5. **Checkpoint:** Update history must show the KB as successfully installed. The [Windows 10 manual path](/articles/how-to-fix-kb5055523-stuck-downloading-on-windows-10/) mirrors this for the older OS.

### Fix 7: Verify pipeline health and close out

1. Run `winver` and confirm the build number advanced as the KB specifies.
2. In **Settings → Windows Update**, run **Check for updates** — it should complete cleanly with no phantom stuck download.
3. Re-enable antivirus filtering, VPN, and Delivery Optimization to their normal settings.
4. Restore your normal sleep and power settings if you changed them during the repair.
5. Recheck the next day: one clean automatic check confirms the pipeline is healthy per the expected behavior documented on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 8: Build a personal update toolkit

Assemble a small toolkit now so the next stuck download is a fifteen-minute task.

1. Save the **Microsoft Update Catalog** URL in your bookmarks with your build noted.
2. Keep a text file with your exact Windows build, edition, and architecture for quick catalog matching.
3. Store the service restart and cache-clear commands in a batch file on your desktop.
4. Bookmark the official servicing documentation for error-code lookups.
5. Keep a USB drive with the latest servicing stack update for offline repairs.
6. Document your network's quirks — VPN behavior, metered flags, proxy settings — in the same notes file.

## Closing

Step-by-step repair is slower than guessing but faster than guessing wrong five times. Verify the stall, restart the services, clear the obstructions, reset the pipeline, install manually — checking your work at every stage. KB5055523 installs, the pipeline is verified healthy, and you know precisely which step did it.
