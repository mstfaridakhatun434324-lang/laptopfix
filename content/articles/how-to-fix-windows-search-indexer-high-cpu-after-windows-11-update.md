---
title: "Windows Search Indexer High CPU After a Windows 11 Update: Fix It"
slug: how-to-fix-windows-search-indexer-high-cpu-after-windows-11-update
date: 2026-09-03
categories: ["performance"]
tags: ["search indexer", "searchindexer", "high cpu", "windows update", "windows search"]
description: "SearchIndexer.exe hammering your CPU after a Windows 11 update? Why the index rebuilds and how to speed it up or tame it."
thumbnail: "/images/thumbs/how-to-fix-windows-search-indexer-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "What is SearchIndexer.exe and why is it using CPU?"
    a: "SearchIndexer.exe is the Windows Search indexing engine. It catalogs your files, emails, and Start menu entries so searches return instantly instead of scanning the disk each time. After a Windows update it rebuilds or re-verifies large parts of the index, which is CPU and disk intensive. This is normal maintenance — the indexer is supposed to work hard after system changes, then go quiet once the index is current."
  - q: "How long does the post-update index rebuild take?"
    a: "Typically a few hours of plugged-in idle time, though large file collections or slow drives can stretch it to a day. The indexer deliberately throttles itself while you are actively using the PC and works harder when idle, which is why the high CPU often appears when you step away. If it is still at high CPU after 48 hours of normal plugged-in use, the index is likely corrupted or stuck on a problem file."
  - q: "Can I just disable Windows Search indexing?"
    a: "You can, but you will feel it every day: Start menu search, File Explorer search, and Outlook search become slow disk scans instead of instant index lookups. Disabling is only sensible if you genuinely never search your PC. The better approach is narrowing what gets indexed — excluding folders you never search — which cuts the indexer's workload while keeping fast search where it matters."
  - q: "Will rebuilding the index delete my files?"
    a: "No. Rebuilding the index only deletes and recreates the search catalog database; your actual files, emails, and settings are untouched. The worst case is that search results are incomplete while the rebuild runs, which resolves itself as indexing progresses. It is one of the safest troubleshooting operations in Windows, and it fixes a large share of stuck-indexer problems."
---

After a Windows 11 update, `SearchIndexer.exe` (or `SearchHost.exe` / Microsoft Windows Search Indexer in Task Manager) starts consuming 20–50% CPU, the disk churns, and the laptop runs warm while seemingly doing nothing. It's tempting to kill it — but the indexer is doing legitimate post-update work: the update changed thousands of files, and the search catalog must be re-verified so your Start menu and File Explorer searches keep working instantly.

As with every post-update background process, duration is the diagnostic. A few hours to a day of indexing after an update is expected. High CPU that never ends, an index that never reports complete, or the indexer stuck on the same file count for days means the index is corrupted or wedged on a problem file — and that's fixable. This guide shows you how to check indexing status, help it finish faster, narrow its workload, and rebuild it when it's broken.

First, check the state: open **Settings** > **Privacy & security** > **Searching Windows** and look at the indexing status — it tells you whether indexing is in progress and roughly how many items remain. If it says indexing is complete but CPU is still high, something is stuck. For related post-update CPU issues, see [Defender high CPU after an update](/articles/how-to-fix-antimalware-service-executable-high-cpu-after-windows-11-update/) and [Windows Modules Installer high CPU](/articles/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update/).

## Why this happens

- **Post-update index re-verification**: The update changed system files; the catalog must be rechecked.
- **New file types or locations**: Updates can add indexed locations or content types, expanding the workload.
- **Corrupted index database**: A damaged catalog makes the indexer loop instead of completing.
- **Problem files**: A corrupted file (often a huge PST/OST or damaged document) wedges the indexer mid-file.
- **Overly broad indexing scope**: Indexing entire drives including folders you never search multiplies the work.
- **Disk slowness**: On HDDs or nearly-full SSDs, indexing takes far longer and uses more CPU waiting on I/O.
- **Conflicting search tools**: Third-party search utilities fighting the indexer for the same files.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check indexing status and let it finish

Verify it's working, not stuck.

1. Open **Settings** > **Privacy & security** > **Searching Windows** — read the status: "Indexing in progress" with a decreasing item count means healthy progress.
2. Click **Advanced indexing options** > **Modify** to see which locations are indexed and confirm nothing unexpected (like an entire external drive) was added.
3. Leave the laptop plugged in and idle for a few hours — the indexer is designed to work hardest when you're away; babysitting it slows it down.
4. Check back periodically: the pending item count should shrink steadily. Shrinking = finishing. Frozen for hours = stuck (proceed to Fix 4).
5. If status shows "Indexing complete" yet SearchIndexer.exe still burns CPU, the status and the engine disagree — treat it as stuck and rebuild (Fix 4).

### Fix 2: Narrow what gets indexed

Less to index means less CPU, permanently.

1. In **Settings** > **Privacy & security** > **Searching Windows**, review **Find my files** — **Classic** (indexed locations only) is far lighter than **Enhanced** (entire PC).
2. Switch to **Classic** if you don't need whole-drive search — most users search Documents, Start menu, and settings, all covered by Classic.
3. Click **Advanced indexing options** > **Modify** and uncheck folders you never search: game libraries, VM images, node_modules-heavy code folders, video archives.
4. In **Advanced Options** > **File Types**, uncheck exotic file types you never search by content — each registered type adds parsing work.
5. After narrowing, the indexer trims the catalog — give it one idle session, then enjoy permanently lower indexing overhead. Microsoft documents these options in its [Windows search support](https://support.microsoft.com/en-us/windows).

### Fix 3: Exclude problem folders and Outlook data

Target the usual wedges.

1. If you have a gigantic Outlook data file (multi-GB PST/OST), it's a prime suspect — in **Indexing Options** > **Modify**, temporarily uncheck **Microsoft Outlook** and see if CPU drops.
2. Exclude folders with constantly-changing or corrupted content: active download folders, torrent directories, and folders full of half-written files.
3. Exclude developer folders with tens of thousands of tiny files — indexers choke on file count more than file size.
4. After each exclusion change, restart the **Windows Search** service (**Services** > **Windows Search** > **Restart**) so the new scope takes effect cleanly.
5. Re-add Outlook indexing afterward if you depend on email search — but consider archiving old mail to shrink the data file first.

### Fix 4: Rebuild the index

The definitive fix for a corrupted or stuck catalog.

1. Open **Settings** > **Privacy & security** > **Searching Windows** > **Advanced indexing options** > **Advanced** > **Rebuild** (under Troubleshooting).
2. Confirm the rebuild — Windows deletes the catalog and starts fresh. Your files are untouched; only the search database is recreated.
3. Alternatively, run the troubleshooter first: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Search and Indexing** — it detects common index problems automatically.
4. Leave the laptop plugged in and idle — a full rebuild on a large file collection takes several hours; using the PC during it just stretches the timeline.
5. Verify completion: indexing status should reach "Indexing complete" and SearchIndexer.exe should drop to near-zero CPU at idle. If it wedges again at the same point, a specific file is the culprit (Fix 3's exclusions).

### Fix 5: Repair the search components

When rebuilds don't stick.

1. Restart the **Windows Search** service: **Services** (`services.msc`) > **Windows Search** > **Restart**. If it's stuck stopping, reboot.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an elevated terminal — search components are Windows components and benefit from the same repairs.
3. Check for pending **Windows Update** items — search-indexer fixes ship regularly, and a post-update indexer bug is often patched within weeks.
4. If you use a third-party search tool (Everything, Listary), check its settings for conflicts — some hook into the same files aggressively.
5. As a test, create a new local user account and check indexer CPU there — a calm indexer on the new account points to profile-specific index corruption on yours.

### Fix 6: Address the disk bottleneck

Indexing is disk-bound; slow disks mean long, CPU-wasteful indexing.

1. Free disk space to at least 15% on C: — a nearly-full drive makes every index write slower (see [freeing up disk space](/articles/how-to-free-up-disk-space-on-windows-11/)).
2. On HDDs, run **Defragment and Optimize Drives** after the update settles — fragmentation multiplies the indexer's disk seeks.
3. Check drive health: `wmic diskdrive get status` should return OK; a failing drive turns indexing into an endless grind.
4. If you're still on a spinning drive, an SSD upgrade transforms indexing from an all-day event into a background hum.
5. During active rebuilds, avoid disk-heavy tasks (big copies, game installs) — they compete with the indexer for I/O and stretch the job.

### Fix 7: The deliberate disable (last resort)

Only if you truly never search.

1. Understand the cost: Start menu search, File Explorer search, and Outlook search all become slow without the index.
2. To disable: **Services** > **Windows Search** > **Properties** > **Startup type: Disabled** > **Stop** the service.
3. Alternatively, keep the service but strip indexed locations to nearly nothing — you keep the infrastructure with minimal cost.
4. If you disable it and miss fast search later, re-enable the service and rebuild — nothing is permanent.
5. For most users, Fix 2's narrowing is strictly better than disabling — fast search where you need it, minimal CPU everywhere else.

## Closing

The Windows Search indexer after an update is a worker with a deadline: re-verify the catalog, then go quiet. Help it hit the deadline with idle plugged-in time, narrow its territory to folders you actually search, and rebuild the catalog when it's corrupted. A healthy indexer is invisible — and with the steps above, that's exactly what yours will be again.
