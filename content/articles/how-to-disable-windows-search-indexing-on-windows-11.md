---
title: "How to Disable Windows Search Indexing on Windows 11"
slug: how-to-disable-windows-search-indexing-on-windows-11
date: 2026-09-24
categories: ["performance"]
tags: ["disable search indexing", "windows 11", "searchhost.exe", "indexing options"]
description: "Windows 11 search indexing slowing your laptop? Disable it fully, limit its scope, or rebuild a corrupt index — with clear tradeoffs for each choice."
thumbnail: "/images/thumbs/how-to-disable-windows-search-indexing-on-windows-11.webp"
faqs:
  - q: "Should I disable search indexing on Windows 11?"
    a: "Only if the indexer is demonstrably causing problems — sustained high CPU or disk usage from SearchIndexer.exe or SearchHost.exe. On modern SSDs the indexer is usually quiet and genuinely useful, making Start menu and file searches instant. Try excluding busy folders first; full disable is for machines where the indexer never settles or the hardware is too weak to spare the resources."
  - q: "What's the difference between Windows 10 and 11 search indexing?"
    a: "The underlying indexer is largely the same, but Windows 11 splits the work across more processes (SearchHost.exe, SearchIndexer.exe) and ties search more deeply into the taskbar experience with highlights and web integration. Windows 11 also defaults to Enhanced indexing mode on more configurations. The disable methods — services.msc, Indexing Options, registry — work identically on both."
  - q: "Will disabling indexing break Start menu search?"
    a: "No — Start menu search for apps and settings keeps working because those use a separate fast path. What changes is file search: without an index, searching File Explorer scans in real time, which is noticeably slower on large drives. Most users find app launching unaffected and file searches merely slower, an acceptable tradeoff on struggling hardware."
  - q: "How do I re-enable indexing later?"
    a: "Reverse your method: set the Windows Search service back to Automatic (Delayed Start) in services.msc and start it, or re-add locations in Indexing Options. Windows rebuilds the index automatically over a few hours of idle time. If you used the registry method, delete the value you created. All methods are fully reversible with no lasting effects."
---

Windows 11's search indexer quietly catalogs your files so the taskbar search feels instant — and most of the time you'd never know it's there. But when it misbehaves — grinding CPU after the 24H2 update, pinning disk usage on older hardware, or rebuilding endlessly on a corrupt index — it becomes one of the most visible performance drains on the system. The processes to watch are `SearchIndexer.exe` and `SearchHost.exe` in Task Manager.

You have a spectrum of options, from gentle (exclude folders) to total (disable the service). This guide walks the spectrum in order — stop at the mildest step that solves your problem. If search isn't your main slowdown, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); for boot-time load, [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Enhanced mode indexing the entire drive**: Windows 11's Enhanced setting catalogs everything, multiplying the workload versus Classic mode.
- **Post-24H2 index migration issues**: The feature update can leave the index in a state the indexer churns on without finishing.
- **Corrupt index causing endless rebuilds**: Damage makes the service restart its work perpetually.
- **High-churn folders**: Downloads, game libraries, and developer folders trigger constant re-indexing.
- **Search highlights and web content**: The taskbar search box's dynamic content adds background activity.
- **Mechanical hard drives**: Indexer I/O competes directly with everything else on slow disks.
- **Antivirus re-scanning indexed files**: Real-time AV doubles the disk cost of every indexed file.
- **Huge Outlook mailboxes**: Indexed mail stores add enormous, ongoing indexing work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the indexer is the problem

Check before you disable.

1. Open **Task Manager** > **Processes**, sort by **CPU** or **Disk**, and look for **SearchIndexer.exe** or **SearchHost.exe** with sustained high usage.
2. Open **Settings** > **Privacy & security** > **Searching Windows** — check whether **Find my files** is **Enhanced** (whole drive) or **Classic** (libraries only), and note the indexing status.
3. If status perpetually shows indexing in progress with no completion, the index is likely corrupt (Fix 3).
4. Check your drive type (**Task Manager** > **Performance**) — on SSDs, look twice before blaming the indexer.
5. If the indexer is idle but the system is slow, stop here — your problem is elsewhere.

### Fix 2: Switch to Classic mode and exclude folders

Keep instant search where it matters, drop the grind.

1. Go to **Settings** > **Privacy & security** > **Searching Windows** — set **Find my files** to **Classic** if it's on Enhanced.
2. Click **Advanced indexing options** (or open **Control Panel** > **Indexing Options**) > **Modify**.
3. Uncheck high-churn locations: Downloads, game folders, developer directories, VM folders — keep Documents, Desktop, and Start Menu.
4. In **Advanced** > **File Types**, uncheck extensions you never search by content, and set the rest to **Index Properties Only** where content search isn't needed.
5. Give it a day — the indexer trims its workload and most users see the problem vanish while search stays fast for the locations they actually use.

### Fix 3: Rebuild a corrupt index

When the indexer never finishes its work.

1. In **Indexing Options** > **Advanced**, run the **Search and Indexing** troubleshooter first (**Settings** > **System** > **Troubleshoot** > **Other troubleshooters**).
2. If that fails, click **Rebuild** under Troubleshooting in the Advanced dialog and confirm.
3. Leave the laptop plugged in and idle for several hours — overnight is ideal. Expect heavy activity during the rebuild; that's normal and temporary.
4. Judge results the day after the rebuild completes — not during it.
5. If the fresh index also never completes, check drive health (`wmic diskdrive get status`) and run `chkdsk C: /f` — persistent rebuild failure often means disk trouble.

### Fix 4: Disable search highlights and web integration

Reduce what the search UI does in the background.

1. Go to **Settings** > **Privacy & security** > **Search permissions**.
2. Turn off **Cloud content search** for both Microsoft and work/school accounts.
3. Turn off **Search highlights** — this stops the dynamic content (trivia, images) in the search box that generates background network and CPU activity.
4. Also disable **History** options you don't need on the same page.
5. Restart the search process: **Task Manager** > **Details** > end **SearchHost.exe** (it restarts automatically) and observe CPU over the next hour.

### Fix 5: Disable the Windows Search service

The full off-switch — reversible in a minute.

1. Press **Win + R**, type `services.msc`, find **Windows Search**.
2. Double-click > set **Startup type** to **Disabled** > click **Stop**.
3. Confirm in Task Manager that SearchIndexer.exe is gone and disk/CPU settle.
4. Understand the tradeoff: File Explorer searches now scan in real time (slower on big drives); Start menu app search still works fine.
5. Microsoft documents the service's role in its [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the official breakdown.

### Fix 6: Use the registry for a harder disable

When the service keeps getting re-enabled.

1. Back up the registry (**File** > **Export** in `regedit`).
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search` (create keys as needed).
3. Create DWORD `AllowIndexingEncryptedStoresOrItems` = `0` to block encrypted-file indexing, or for the stronger approach use Group Policy on Pro: `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Search** > enable **Disable indexer backoff** controls as needed.
4. The most reliable persistent disable remains the services.msc method combined with re-checking after feature updates.
5. To reverse any registry change, delete the value you created and restart.

### Fix 7: Address the hardware underneath

When the indexer is just the messenger.

1. On a mechanical HDD with 100% disk during indexing, the fundamental fix is an SSD — indexing load that cripples an HDD is trivial for an SSD.
2. Ensure 15%+ free space on C: — cramped drives make every background task worse.
3. Run **Disk Cleanup** (`cleanmgr`) with system files to clear update leftovers competing for disk.
4. Check drive health — a failing drive makes the indexer (and everything) crawl; `wmic diskdrive get status` is the 10-second check.
5. With an SSD, free space, and a healthy drive, re-enable indexing and enjoy instant search — the performance cost on decent hardware is genuinely negligible.

## Closing

Windows 11 search indexing is a useful servant and a terrible master. Start by shrinking its workload — Classic mode, excluded folders, no web extras — and rebuild if the index is corrupt. Only disable the service if the gentler steps fail, and remember it's all reversible. The goal isn't killing search; it's making it quiet again.
