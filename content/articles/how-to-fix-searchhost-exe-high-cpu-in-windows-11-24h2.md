---
title: "SearchHost.exe High CPU in Windows 11 24H2? Fix It Fast"
slug: how-to-fix-searchhost-exe-high-cpu-in-windows-11-24h2
date: 2026-09-28
categories: ["performance"]
tags: ["searchhost.exe", "high cpu", "windows search", "24h2", "indexing"]
description: "SearchHost.exe pinning your CPU after the Windows 11 24H2 update? Diagnose the indexing loop and bring CPU usage back to normal."
thumbnail: "/images/thumbs/how-to-fix-searchhost-exe-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "What is SearchHost.exe and is it safe?"
    a: "SearchHost.exe is the legitimate Windows Search host process that powers the taskbar search box, Start menu search, and File Explorer search in Windows 11. It is a genuine Microsoft component and is safe. High CPU from it almost always means the search indexer is stuck, rebuilding, or choking on a corrupted index — not malware, though malware can disguise itself with the same name."
  - q: "Why is SearchHost.exe using CPU after the 24H2 update?"
    a: "The 24H2 update migrates and rebuilds the search index, and on many systems the indexer gets stuck in a loop — constantly re-crawling the same locations or failing on a corrupted catalog. This typically settles within a day or two, but if it persists beyond 48 hours, the index is damaged and needs a manual rebuild."
  - q: "Can I just disable SearchHost.exe?"
    a: "You can disable Windows Search, but you lose Start menu search, taskbar search, and File Explorer search — a heavy price. Killing the process in Task Manager only works until it restarts itself. The better fix is repairing the indexer (rebuild the index, exclude problem folders) so SearchHost idles at near-zero CPU as designed."
  - q: "How do I know if SearchHost.exe is actually malware?"
    a: "Right-click it in Task Manager's Details tab and choose Open file location — the genuine file lives in C:\\Windows\\SystemApps\\MicrosoftWindows.Client.CBS_cw5n1h2txyewy. Anything running from a Temp folder, Downloads, or your user profile is an imposter. When in doubt, run a full Microsoft Defender offline scan."
---

After the Windows 11 24H2 update, plenty of laptop owners opened Task Manager to find `SearchHost.exe` sitting at 20%, 40%, even 70% CPU — permanently. Your fans spin, your battery drains, and the search box you barely use is somehow the busiest thing on the system. This is a known 24H2 pattern: the update disturbs the search index, and the indexer gets stuck in a loop trying to rebuild it.

The fix is almost never disabling search. It's diagnosing what the indexer is choking on — a corrupt catalog, a problem folder it keeps re-crawling, or a stuck 24H2 migration — and clearing it. If search itself is broken too (no results, blank box), see our [Windows Search repair guide](/articles/how-to-fix-windows-search-not-working-on-windows-11/) alongside this one.

## Why this happens

- **24H2 index migration loop**: The feature update rebuilds the search catalog; on many machines the rebuild never completes and restarts endlessly.
- **Corrupted search index**: A damaged catalog makes the indexer retry the same files forever instead of finishing.
- **Problem folder being re-crawled**: A constantly changing folder (build outputs, a huge Downloads folder, a cloud-synced drive mid-sync) keeps the indexer permanently busy.
- **Stuck SearchHost process**: The process itself can hang in a bad state that survives the condition that caused it.
- **OneDrive/SharePoint sync churn**: Cloud files flipping between online-only and local states generate endless re-indexing.
- **Corrupt user profile search data**: Per-user search databases in AppData can corrupt during the update.
- **Malware impersonating the process**: Rare, but worth ruling out since the name is trusted and unremarkable.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's really the indexer (and not an imposter)

Two minutes of verification before you change anything.

1. Open **Task Manager** > **Details** tab, right-click **SearchHost.exe** > **Open file location**. The real one lives in `C:\Windows\SystemApps\MicrosoftWindows.Client.CBS_cw5n1h2txyewy`. Anywhere else — kill it and scan.
2. Check **Task Manager** > **Processes** > **Windows Explorer** — SearchHost runs under the search host; note whether CPU is constant or spikes when you type in the search box (spikes on typing are normal).
3. Open **Settings** > **Privacy & security** > **Searching Windows** and look at **Indexing status** — if it says "Indexing in progress" perpetually, you've found the loop.
4. Note how long this has gone on: under 48 hours since the 24H2 update, give it one more night of plugged-in idle time. Beyond that, proceed — it's stuck.
5. Run a quick Defender scan anyway to rule out the imposter scenario — cheap insurance. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) has guidance on verifying system processes.

### Fix 2: Restart the Windows Search service

Clear a hung process state without touching your data.

1. Press `Win + R`, type `services.msc`, and press Enter.
2. Find **Windows Search** in the list, right-click it, and choose **Restart**.
3. If Restart is greyed out, choose **Stop**, wait 30 seconds, then **Start**.
4. Watch Task Manager for 10 minutes — if SearchHost.exe settles to near-zero, the process was simply wedged.
5. If CPU climbs right back up within minutes, the trigger is still active (corrupt index or problem folder) — continue to Fix 3.
6. Also restart **Windows Explorer** from Task Manager (right-click > Restart) since search UI components live partly in Explorer.

### Fix 3: Rebuild the search index

The definitive fix for a corrupted catalog — the 24H2 classic.

1. Open **Settings** > **Privacy & security** > **Searching Windows** > **Advanced indexing options** (or search "Indexing Options" in Control Panel).
2. Click **Advanced**, then under Troubleshooting click **Rebuild**.
3. Confirm — Windows deletes the catalog and starts over. This is safe; it only affects search speed temporarily, not your files.
4. Leave the laptop plugged in and idle for a few hours (overnight is ideal). Indexing is I/O-heavy at first, then tapers off.
5. Check **Indexing Options** the next day — status should read "Indexing complete" with a stable item count.
6. If the rebuild itself never finishes (stuck at the same count for hours), a specific folder is choking the crawler — continue to Fix 4 before rebuilding again.
7. Patience matters here: interrupting a rebuild mid-way can re-corrupt the catalog and send you back to square one.

### Fix 4: Exclude high-churn folders from indexing

Stop the indexer from re-crawling folders that never sit still.

1. In **Indexing Options** > **Modify**, review the checked locations.
2. Uncheck folders with constant churn: build output directories, `node_modules`, game mod folders, video render scratch disks, and any folder with tens of thousands of tiny files.
3. If you use OneDrive heavily, consider unchecking the OneDrive folder during an active large sync, then re-adding it after the sync completes.
4. Click OK, then rebuild the index (Fix 3) so the exclusions take full effect on a clean catalog.
5. For developers: excluding your code directories barely hurts — you search code with your IDE's own search, which is faster anyway.
6. After exclusions + rebuild, SearchHost.exe should idle under 1% CPU during normal use.

### Fix 5: Run the Search and Indexing troubleshooter

Let Windows attempt the automated repair first.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Run the **Search and Indexing** troubleshooter and check the boxes matching your symptoms ("Files don't appear in search results", "Search is slow").
3. Apply whatever fixes it proposes — it commonly resets the search service configuration and clears stale catalog locks.
4. Restart the laptop after the troubleshooter finishes, then monitor SearchHost.exe for an hour.
5. If the troubleshooter reports it couldn't fix the issue, that's still useful information — it confirms manual intervention (rebuild, exclusions) is needed.

### Fix 6: Clear per-user search data

When the corruption lives in your profile rather than the system catalog.

1. Stop the **Windows Search** service (services.msc) first.
2. In File Explorer, navigate to `%ProgramData%\Microsoft\Search\Data\Applications\Windows` — this holds the system catalog files.
3. Also check `%LOCALAPPDATA%\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy` for the SearchHost app data; renaming the `LocalState` folder forces it to regenerate.
4. Restart the **Windows Search** service and let it rebuild from scratch.
5. Sign out and back in to regenerate any per-user search state cleanly.
6. If the problem follows only one user account, the profile itself may be damaged — testing with a fresh local account (Settings > Accounts > Other users) confirms it quickly.

### Fix 7: Repair Windows as a last resort

For 24H2 upgrades where the search stack itself is damaged.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an elevated terminal — the search components are Windows components and these tools repair them.
2. Install every pending update in **Settings** > **Windows Update** — Microsoft has shipped several 24H2 search fixes as cumulative updates, available via the [Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update misses them.
3. If problems began immediately after the 24H2 update and nothing else helps, consider rolling back within the 10-day window: **Settings** > **System** > **Recovery** > **Go back**.
4. Beyond that window, an in-place upgrade (repair install) using 24H2 media refreshes the search stack while keeping files and apps.
5. Do not "fix" this by permanently disabling Windows Search via registry hacks — you lose Start menu search and gain almost nothing once the index is healthy. If the whole machine feels slow rather than just search, work through our [slow Windows 11 laptop guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/) alongside these fixes.

## Closing

SearchHost.exe high CPU after 24H2 is the indexer telling you it's stuck, not that search is broken by design. Verify the process is genuine, restart the service, rebuild the index, exclude the folders that keep it churning — and in nearly every case it drops back to the near-zero idle CPU it was designed for. A healthy search index is invisible; that's the goal.
