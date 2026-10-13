---
title: "How to Disable Windows Search Indexing (Safely, and When Not To)"
slug: how-can-i-disable-windows-search-indexing
date: 2026-10-02
categories: ["performance"]
tags: ["disable windows search indexing", "search indexer", "high cpu", "windows 11", "services"]
description: "Windows Search indexer hammering your CPU and disk? Learn how to disable or tame indexing safely — and when disabling it is the wrong call."
thumbnail: "/images/thumbs/how-can-i-disable-windows-search-indexing.webp"
faqs:
  - q: "Is it safe to disable Windows Search indexing completely?"
    a: "Mostly safe, with one clear cost: Start menu and File Explorer searches become slow because Windows must scan files live instead of consulting the index. Everything else keeps working. A smarter middle ground is limiting which folders get indexed rather than killing the service — you keep fast search where you need it and stop the indexer from churning on folders you never search."
  - q: "Will disabling indexing break the Start menu search?"
    a: "No, it still works — just slower. Start menu search falls back to a live crawl of indexed locations, so results for files take noticeably longer while app and settings results remain fast. If you rarely search for files by name, you may never notice the difference. Heavy file-searchers should limit locations instead of disabling entirely."
  - q: "Why is the Search indexer using 100% disk or high CPU?"
    a: "Usually because it is building or rebuilding the index — after a Windows update, after you add a huge folder to indexed locations, or because it is stuck looping on a corrupted file. First-time indexing of a large drive can take hours. Give a fresh build one full pass; if it never finishes or restarts endlessly, the index is corrupted and needs a rebuild, not a disable."
  - q: "What's the difference between disabling the service and turning off indexing per drive?"
    a: "Disabling the Windows Search service stops all indexing system-wide. Unchecking 'Allow files on this drive to have contents indexed' in a drive's properties only excludes that drive while the service keeps running for everything else. Per-drive or per-folder exclusion is the surgical option; the service toggle is the blunt one. Use the surgical option first."
---

The Windows Search indexer is supposed to be invisible — quietly cataloging your files in the background so searches return instantly. When it misbehaves, it's anything but invisible: SearchIndexer.exe pins the CPU, hammers the disk to 100%, and the laptop sounds like it's rendering video while you read email. Disabling indexing is the popular fix, and it works — but it's also the bluntest tool in the box. This guide shows you the full ladder: from taming the indexer to disabling it properly, with honest notes on what each step costs.

## Why this happens

- **Initial index build on a huge drive:** First-time indexing of hundreds of gigabytes legitimately takes hours of heavy disk and CPU.
- **Post-update index rebuilds:** Feature updates can invalidate the index, triggering a full rebuild that looks like a malfunction.
- **Corrupted index database:** A damaged index makes the service loop — rebuilding forever without finishing.
- **Monster folders in indexed locations:** Developer directories, video archives, or VM folders with hundreds of thousands of files overwhelm the indexer.
- **Corrupted or pathological files:** A damaged Outlook PST/OST, a malformed document, or a file the filter can't parse stalls the indexer in a retry loop.
- **Too many indexed locations:** Adding entire drives or network shares multiplies the workload far beyond the useful default set.
- **Antivirus fighting the indexer:** Real-time scanning of every file the indexer touches doubles the I/O cost.
- **Failing storage:** A dying drive's slow reads make indexing crawl, which looks like the indexer is the problem when the disk is.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether it's building or broken

Settings → Privacy & security → Searching Windows: look at the indexing status. "Indexing in progress" with a count that's climbing means legitimate work — let it finish (plugged in, overnight if needed). "Indexing complete" while SearchIndexer.exe still hammers resources means it's stuck or looping. Also note how many items are indexed: a healthy personal index is typically tens of thousands of items; millions suggests monster folders got included. This status check takes thirty seconds and prevents you from "fixing" normal behavior. For the high-CPU-specific diagnosis, see [Search indexer high CPU fixes](/articles/how-to-fix-windows-search-indexer-high-cpu-in-windows-11-24h2/).

1. Settings → Privacy & security → Searching Windows → check status.
2. Climbing count = legitimate build; let it finish (plugged in).
3. "Complete" but still busy = stuck; continue below.
4. Note the item count — millions means over-inclusive locations.

### Fix 2: Shrink the indexed locations (the smart fix)

Searching Windows → Advanced indexing options → Modify: uncheck everything you never search — entire secondary drives, video archives, developer folders, VM directories, game libraries. Keep Documents, Desktop, and whatever you actually search. This is the fix most people should use instead of disabling: the indexer goes quiet because its workload shrank 90%, and search stays instant where it matters. Rebuild the index afterward so the change takes full effect.

1. Searching Windows → Advanced indexing options → Modify.
2. Uncheck drives/folders you never search (video, VMs, dev folders).
3. Keep Documents, Desktop, and genuinely searched locations.
4. Rebuild the index; verify the indexer goes quiet.

### Fix 3: Rebuild a corrupted index

If the indexer loops forever or status never reaches "complete": Searching Windows → Advanced indexing options → Advanced → Rebuild. This deletes the index database and starts fresh — the correct fix for corruption, and far better than disabling the service to dodge a broken database. The rebuild takes hours on large drives; run it overnight plugged in. One clean rebuild resolves most "indexer never finishes" cases permanently. Step-by-step variant: [search indexing high CPU step-by-step](/articles/how-to-fix-search-indexing-high-cpu-windows-11-step-by-step/).

1. Advanced indexing options → Advanced → Rebuild.
2. Confirm; leave the laptop plugged in overnight.
3. Verify status reaches "Indexing complete" the next day.
4. Confirm SearchIndexer.exe idles afterward.

### Fix 4: Exclude problem file types and folders

In Advanced indexing options → Advanced → File Types: uncheck extensions you never search by content (video formats, disk images, archives). For Outlook users with giant mailboxes: the OST/PST is a notorious indexer trap — in Outlook, consider disabling "improve search speed" integration or archiving old mail. Also exclude any folder containing files the indexer visibly chokes on (watch which path it stalls at in the indexing status details). Surgical exclusions beat global disabling every time.

1. Advanced → File Types → uncheck unneeded extensions.
2. Address giant Outlook data files (archive or exclude).
3. Exclude folders where indexing visibly stalls.
4. Rebuild after exclusions; verify.

### Fix 5: Disable indexing per-drive (medium-blunt option)

For a drive you never search (a media or backup drive): File Explorer → right-click the drive → Properties → uncheck "Allow files on this drive to have contents indexed in addition to file properties" → apply to all subfolders. Windows strips the indexed attribute drive-wide. The Search service keeps running for everything else, so Start menu and main-drive search stay fast. This is the right call for secondary/internal data drives that exist purely as storage. Microsoft documents indexing options on the [Windows support site](https://support.microsoft.com/en-us/windows).

1. Right-click the drive → Properties.
2. Uncheck "Allow files on this drive to have contents indexed..."
3. Apply to all subfolders and files; let it process.
4. Verify the indexer ignores the drive going forward.

### Fix 6: Disable the Windows Search service (the blunt option)

Only after the surgical options failed or you genuinely never search files: `services.msc` → Windows Search → Stop, then set Startup type to Disabled. Alternatively, admin Terminal: `sc stop "WSearch"` then `sc config "WSearch" start=disabled`. Effects: file search becomes slow (live crawl), but app/settings search still works, and SearchIndexer.exe never runs again. Re-enable anytime by reversing the steps. Don't do this casually on a work machine where colleagues expect instant file search — the productivity cost is real.

1. `services.msc` → Windows Search → Stop.
2. Set Startup type to Disabled (or use `sc config` commands).
3. Test Start menu and Explorer file search — note the slower speed.
4. Re-enable by reversing if the tradeoff isn't worth it.

### Fix 7: Rule out the disk itself

If the indexer crawls even on a tiny location set, the storage may be the bottleneck: run `chkdsk C: /f`, check SMART health with your SSD vendor's tool, and watch disk response times in Task Manager → Performance (average response time consistently in hundreds of milliseconds is bad). A failing drive makes every indexer operation stall, and no indexing setting fixes hardware. Back up first, diagnose second — a dying drive with your only copy of data is an emergency, not a tuning exercise.

1. `chkdsk C: /f`; check SMART health.
2. Task Manager → Performance → disk response times.
3. Hundreds of ms sustained or SMART warnings = failing drive.
4. Back up immediately; replace the drive.

## Closing

Disabling Windows Search indexing works, but it's the last resort, not the first step — shrinking indexed locations and rebuilding a corrupt index solve most cases while keeping fast search. The indexer is genuinely useful when its workload is sane; the trick is giving it a sane workload. Start surgical, go blunt only if surgery fails, and always check the disk before blaming the software.
