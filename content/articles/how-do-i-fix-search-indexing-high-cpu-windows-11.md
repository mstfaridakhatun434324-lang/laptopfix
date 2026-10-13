---
title: "How Do I Fix Search Indexing High CPU on Windows 11?"
slug: how-do-i-fix-search-indexing-high-cpu-windows-11
date: 2026-09-18
categories: ["performance"]
tags: ["search indexing", "high cpu", "searchindexer", "windows 11"]
description: "SearchIndexer.exe pushing your CPU to 30% or more on Windows 11? Here's how to tame search indexing, shrink what's indexed, and rebuild a corrupt index."
thumbnail: "/images/thumbs/how-do-i-fix-search-indexing-high-cpu-windows-11.webp"
faqs:
  - q: "What is SearchIndexer.exe and why is it using so much CPU?"
    a: "SearchIndexer.exe is the Windows Search indexing service. It scans your files, emails, and Start menu entries to build a searchable database, so searches return results instantly. High CPU means it's actively building or rebuilding that index — common after adding large folders, creating a new user profile, or installing a feature update. It should settle once the index is complete."
  - q: "Is it safe to disable Windows Search indexing entirely?"
    a: "Yes, it's safe — disabling the Windows Search service won't harm Windows, but Start menu and File Explorer searches become slow because they fall back to scanning files live. A better middle ground is shrinking the indexed locations (Indexing Options > Modify) so the indexer has far less work, or limiting indexing to when you're on AC power rather than battery."
  - q: "How long should search indexing take to finish?"
    a: "On an SSD with a typical document library, the initial index usually completes within a few hours of idle time. If SearchIndexer.exe stays at high CPU for several days, the index is likely stuck or corrupt — often due to a damaged index database, a constantly-changing folder like a Downloads directory, or a huge Outlook data file being re-indexed repeatedly. Rebuilding the index usually resolves it."
  - q: "Why does search indexing start over every time I restart my laptop?"
    a: "The indexer should resume, not restart. If it rebuilds from scratch on every boot, the index database is probably corrupt, a Group Policy or third-party 'optimizer' is clearing the index, or antivirus is quarantining index files. Check that C:\\ProgramData\\Microsoft\\Search isn't being cleaned by maintenance tools, then rebuild the index once cleanly and let it finish."
---

You open Task Manager and there it is: `SearchIndexer.exe` sitting at 25%, 40%, sometimes 60% CPU — on a laptop that's supposed to be idling. The fans spin up, the battery drains faster than it should, and the machine feels warm for no apparent reason. This is the Windows Search indexing service doing its job a little too enthusiastically: building a database of every file, email, and Start menu item so your searches return instantly.

Some indexing is normal, especially after you add a big folder, create a new user account, or install a feature update like 24H2. What's not normal is the indexer grinding away for days. The good news is this is one of the most fixable high-CPU problems in Windows 11, because you control exactly what gets indexed. For related background-task slowdowns, see our guide on [Windows Modules Installer high CPU](/articles/how-to-fix-windows-modules-installer-high-cpu-in-windows-11-24h2/) and the general [slow Windows 11 laptop speedup checklist](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Initial index build after a big change**: New user profile, feature update, or a newly added drive triggers a full re-index that can run for hours.
- **Too many indexed locations**: Indexing entire drives, network shares, or game libraries multiplies the workload enormously.
- **Corrupt index database**: A damaged index causes the service to rebuild in a loop, never finishing.
- **Outlook data files being re-indexed**: Large or frequently-changing PST/OST files keep the indexer busy on every mail sync.
- **File contents indexing enabled for everything**: Indexing inside file contents (not just names) is far more CPU-intensive.
- **High-churn folders**: Downloads, build outputs, or torrent folders change constantly, forcing endless re-indexing.
- **Indexing while on battery**: By default the indexer doesn't pause on battery, so it happily eats CPU when unplugged.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the indexer is the real culprit

Make sure SearchIndexer.exe is actually what's eating CPU before you change anything.

1. Open **Task Manager** (`Ctrl + Shift + Esc`), go to the **Processes** tab, and sort by CPU — confirm **Microsoft Windows Search Indexer** is at the top.
2. Open **Indexing Options** (search for it in Start) and check the status line at the top: "Indexing complete" vs. "Indexing in progress" with a count of items.
3. If it says "Indexing complete" but CPU is still high, something else is going on — check the **Details** tab for the actual process and its CPU history.
4. Note the "items indexed" count: a healthy index for a typical laptop is tens of thousands of items; hundreds of thousands suggest overly broad locations.
5. Click **Modify** in Indexing Options and take a screenshot or note of the checked locations — you'll trim these in the next fix.

### Fix 2: Shrink the indexed locations

This single change fixes most persistent indexing CPU problems.

1. In **Indexing Options**, click **Modify**, then uncheck entire drives (especially secondary/data drives), game folders, and network locations.
2. Keep only what you actually search: typically **Users** (your documents) and the **Start Menu** — that's enough for most people.
3. Click **OK**, then click **Advanced** > **File Types** tab — uncheck "Index Properties and File Contents" for file types where you never search inside contents (videos, archives, executables).
4. Common file types worth keeping contents-indexed: `.docx`, `.pdf`, `.txt`, `.xlsx`. Uncheck contents indexing for `.zip`, `.mp4`, `.exe`, `.dll`.
5. Windows applies the change immediately; the indexer will prune the database, which briefly spikes CPU before settling much lower.

### Fix 3: Restart the Windows Search service cleanly

A stuck indexer often just needs a clean restart.

1. Press `Win + R`, type `services.msc`, and press Enter.
2. Find **Windows Search**, right-click it, and choose **Restart** (if it's stuck, choose **Stop**, wait 30 seconds, then **Start**).
3. Watch Task Manager for 5 minutes: a healthy restart shows a brief CPU bump, then a drop to near zero when idle.
4. If CPU immediately climbs back to 30%+ and stays there, the index database is likely corrupt — move to Fix 4.
5. While you're in services.msc, confirm the service's **Startup type** is **Automatic (Delayed Start)** — this keeps indexing from hammering the CPU during boot.

### Fix 4: Rebuild the index from scratch

When the index database is corrupt, rebuilding is the reliable cure.

1. Open **Indexing Options** > **Advanced** > **Troubleshooting** section > click **Rebuild**.
2. Confirm the prompt — Windows deletes the old index and starts over. This is safe; no files are touched, only the search database.
3. Let the rebuild run during a period you won't need peak performance (overnight works well). Initial rebuilds take 1–4 hours on an SSD.
4. Monitor via Indexing Options: the item count should climb steadily. If it stalls at the same number repeatedly, a specific file is crashing the indexer — exclude that folder (Fix 5).
5. After "Indexing complete" appears, CPU from SearchIndexer.exe should be near zero at idle.

### Fix 5: Exclude high-churn and problem folders

Stop the indexer from chasing folders that change constantly.

1. In **Indexing Options** > **Modify**, expand your user folder and uncheck **Downloads**, any code/build output folders, virtual machine directories, and game mod folders.
2. If you use Outlook with a large mailbox, consider excluding Outlook in **Modify** (under Microsoft Outlook) — mail search still works via the server, and local indexing of multi-GB OST files is a classic CPU hog.
3. Encrypted files: in **Advanced** > **Index Settings**, uncheck "Index encrypted files" unless you specifically need it — decryption during indexing costs CPU.
4. Network/mapped drives: never index these from a laptop; latency makes the indexer work far harder and it retries constantly on flaky Wi-Fi.
5. After excluding, give the indexer 15–30 minutes to prune, then confirm idle CPU is back to normal.

### Fix 6: Limit indexing to AC power and idle time

Keep the indexer from draining your battery or fighting you while you work.

1. Open the **Local Group Policy Editor** (`gpedit.msc`) — on Windows 11 Pro. Navigate to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Search**.
2. Enable **"Prevent indexing when running on battery power to conserve energy"** — this stops the indexer entirely when unplugged.
3. Also enable **"Disable indexer backoff"** only if you want indexing to continue during user activity — normally leave this off so the indexer backs off while you work.
4. On Windows 11 Home (no gpedit), the equivalent registry key is `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search` — create DWORD `PreventIndexOnBattery` = 1.
5. As a last resort, you can set **Windows Search** service startup to **Disabled** in services.msc — searches still work but are slow. Most users are happier with the trimmed-index approach instead. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the service's behavior if you need official confirmation.

## Closing

Search indexing high CPU is almost always a configuration problem, not a broken system: too much indexed, a corrupt index, or a churn-heavy folder keeping the indexer busy. Trim the locations, rebuild once cleanly, and keep it off battery power — and SearchIndexer.exe should fade back into the background where it belongs.
