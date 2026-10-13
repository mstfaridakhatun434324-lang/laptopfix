---
title: "How to Disable Windows Search Indexing on Windows 10"
slug: how-to-disable-windows-search-indexing-on-windows-10
date: 2026-09-11
categories: ["performance"]
tags: ["disable search indexing", "windows 10", "windows search", "indexing options"]
description: "Windows Search indexing hammering your disk and CPU on Windows 10? Learn how to disable it completely, limit it, or rebuild it — with the tradeoffs of each option."
thumbnail: "/images/thumbs/how-to-disable-windows-search-indexing-on-windows-10.webp"
faqs:
  - q: "Is it safe to disable Windows Search indexing on Windows 10?"
    a: "Yes, it's safe — disabling indexing only affects how fast file searches return results, not system stability. Windows Search still works; it just searches in real time instead of consulting a prebuilt index, which makes searches of large drives noticeably slower. Core features like Start menu app search keep working normally, so most users notice little difference in daily use."
  - q: "Will disabling indexing speed up my laptop?"
    a: "It can, particularly on laptops with mechanical hard drives or during the initial indexing of a large file collection, when the indexer competes with everything else for disk access. On modern SSDs the indexer is usually quiet enough that disabling it yields little measurable gain. The biggest wins go to older machines and to users with huge document or photo libraries."
  - q: "What's the difference between disabling the Windows Search service and turning off indexing?"
    a: "Disabling the Windows Search service stops indexing entirely and also disables the search index backend — Start menu search becomes slower and some features like indexed file-content search stop working. Turning off indexing per-location (via Indexing Options) is gentler: the service still runs, but it has nothing to index. Choose the gentler option first; go nuclear only if the service itself misbehaves."
  - q: "How do I turn search indexing back on if I change my mind?"
    a: "Reverse whichever method you used: set the Windows Search service back to Automatic (Delayed Start) in services.msc and start it, or re-add your locations in Indexing Options. Windows will rebuild the index from scratch, which takes a few hours of idle time on a large drive. Your settings return to defaults, so reapply any location exclusions you had."
---

Windows Search indexing is one of those features that works beautifully until it doesn't. In the background, the indexer catalogs your files so searches return instantly — but while it's building or rebuilding that catalog, it can saturate a mechanical hard drive or spike CPU on older machines, making the whole laptop feel broken. If you've caught `SearchIndexer.exe` or `SearchHost.exe` red-handed in Task Manager, you have three options: tame it, limit it, or turn it off entirely.

This guide covers all three, in order of reversibility. Start gentle — most people only need to exclude a few folders or rebuild a corrupt index. Full disable is the last resort, and even it is completely reversible. If your slowdown is broader than search, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); for startup bloat, [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Initial index build on a large drive**: The first full cataloging of hundreds of thousands of files can take hours of heavy disk activity.
- **Index corruption forcing constant rebuilds**: A damaged index makes the service restart its work endlessly, never finishing.
- **High-churn folders being indexed**: Developer directories, downloads, and game folders change constantly, triggering perpetual re-indexing.
- **Mechanical hard drive bottleneck**: Indexers are disk-hungry; on HDDs they compete directly with everything else you do.
- **Windows 10 feature updates resetting index settings**: Updates can re-enable locations you excluded or trigger a full rebuild.
- **Antivirus scanning every indexed file**: Real-time AV scanning of files as the indexer touches them doubles the disk load.
- **Outlook or other apps feeding the index**: Large mailboxes indexed for instant search add enormous indexing workload.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the indexer is the actual problem

Don't disable a useful feature on a hunch.

1. Open **Task Manager** > **Processes**, sort by **Disk** or **CPU**, and look for **Microsoft Windows Search Indexer** (`SearchIndexer.exe`) or **SearchHost.exe** consuming significant resources.
2. Check timing: is it busy constantly, or only for a while after boot? Brief post-boot activity is normal; hours-long grinding is not.
3. Open **Control Panel** > **Indexing Options** and check the status line — if it says "Indexing in progress" perpetually or shows an enormous item count that never decreases, the index is likely corrupt.
4. Note your drive type in **Task Manager** > **Performance** — on an SSD, the indexer is rarely the real culprit behind slowness.
5. If the indexer is quiet but the machine is slow, your problem is elsewhere — don't disable indexing and expect a miracle.

### Fix 2: Exclude high-churn folders from the index

The gentlest effective fix — keep instant search, lose the grind.

1. Open **Control Panel** > **Indexing Options** > **Modify**.
2. In the folder tree, uncheck locations with constant file changes: `Downloads`, game library folders, developer project directories, VM folders, and any folder with tens of thousands of files you never search.
3. Keep indexed: `Users` subfolders you actually search (Documents, Desktop), Start Menu, and Outlook if you use it.
4. Click **OK** — the indexer will trim the index, which itself takes a little while; give it an hour of idle time.
5. Recheck Task Manager after a day — for most people, excluding two or three busy folders ends the problem permanently while Start menu search stays instant.

### Fix 3: Rebuild a corrupt index

When the indexer never finishes, the index itself is usually damaged.

1. Open **Control Panel** > **Indexing Options** > **Advanced** > **Troubleshoot** — run the **Search and Indexing** troubleshooter first; it fixes common issues automatically.
2. If that doesn't help, go back to **Advanced** > **Rebuild** under Troubleshooting — confirm the prompt.
3. Rebuilding deletes the index and starts over. Expect heavy disk activity for several hours — leave the laptop plugged in and idle (overnight is ideal).
4. Don't judge performance during the rebuild — it's supposed to be busy. Judge it the day after.
5. If the new index also never completes, suspect disk problems: run `chkdsk C: /f` and check drive health before blaming the indexer further.

### Fix 4: Limit indexing to reduce its footprint

A middle ground between full indexing and disabling.

1. In **Indexing Options** > **Advanced** > **File Types** tab, uncheck file extensions you never search by content (e.g., `.log`, `.tmp`, video formats) — set the remaining ones to **Index Properties Only** instead of file contents where appropriate.
2. Uncheck **Index encrypted files** if you don't use EFS — encrypted content indexing is extra work for zero benefit to most users.
3. In the **Advanced** dialog, consider unchecking index locations on secondary drives you rarely search.
4. For Outlook users with giant mailboxes: in Outlook, **File** > **Options** > **Search** > **Indexing Options** — you can reduce what's indexed per mailbox.
5. These trims compound: fewer locations plus fewer file types equals a dramatically smaller indexing workload.

### Fix 5: Disable the Windows Search service (full off)

The nuclear option — effective and fully reversible.

1. Press **Win + R**, type `services.msc`, and find **Windows Search** in the list.
2. Double-click it, set **Startup type** to **Disabled**, and click **Stop** to halt it immediately.
3. Click **OK** — indexing stops entirely. Task Manager should show the indexer processes gone.
4. Understand the tradeoff: Start menu and File Explorer searches still work but scan in real time, so searching a large drive takes noticeably longer. App launching from Start is unaffected.
5. Microsoft documents the Windows Search service in its [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the official details on what the service controls.

### Fix 6: Prevent Windows from re-enabling it

Feature updates sometimes resurrect disabled services.

1. After major Windows 10 updates, recheck `services.msc` — if **Windows Search** is back to Automatic, set it to Disabled again.
2. Alternatively, use the gentler Group Policy approach on Pro editions: `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Search** > **Disable indexing** options — policy-based settings survive updates better.
3. If you used Fix 2's exclusion approach instead, verify your exclusions survived the update in **Indexing Options**.
4. Keep a note of which method you used (a text file on the desktop works) so future-you remembers how to reverse it.
5. Re-enable temporarily any time you need to do a big file search across the whole drive, then disable again — the index rebuilds fast enough for occasional use.

### Fix 7: Address the underlying disk bottleneck

Sometimes the indexer is just the messenger.

1. If you're on a mechanical hard drive and the indexer (or anything disk-heavy) regularly pins disk usage at 100%, the real fix is an SSD upgrade — it transforms the machine far beyond search performance.
2. Run **Defragment and Optimize Drives** (`dfrgui`) — on HDDs, a fragmented drive makes indexing much slower; on SSDs just ensure TRIM/retrim runs.
3. Free up space if the drive is nearly full — Windows struggles below ~10% free space, and the indexer is one of the first casualties. See our [disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/) for the cleanup process.
4. Check drive health (`wmic diskdrive get status`) — a failing drive makes every disk-heavy task, indexing included, crawl.
5. With an SSD, ample free space, and a healthy drive, most users can simply leave indexing on — the performance cost becomes negligible.

## Closing

Windows Search indexing is a convenience, not a necessity — and on struggling hardware it can be an expensive one. Exclude the busy folders first, rebuild if the index is corrupt, and only disable the service if the gentler steps fail. Whatever you choose, it's reversible in under a minute, so there's no reason to suffer through an indexer that's grinding your laptop to a halt.
