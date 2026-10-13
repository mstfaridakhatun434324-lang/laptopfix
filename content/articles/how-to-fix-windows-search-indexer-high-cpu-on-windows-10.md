---
title: "Windows Search Indexer High CPU on Windows 10? Fix It"
slug: "how-to-fix-windows-search-indexer-high-cpu-on-windows-10"
date: "2026-09-08"
categories: ["performance"]
tags: ["search indexer", "searchindexer.exe", "windows 10", "high cpu", "cortana search"]
description: "SearchIndexer.exe hammering CPU on Windows 10? The Windows 10 indexer has its own quirks — Cortana integration, old database format, and scope issues. Here's the tailored fix."
thumbnail: "/images/thumbs/how-to-fix-windows-search-indexer-high-cpu-on-windows-10.webp"
faqs:
- q: "Is the Windows 10 search indexer different from Windows 11's?"
  a: "Functionally similar but with key differences: Windows 10's indexer is tied to Cortana and the older Start menu search, uses an older database format more prone to corruption, and its Settings controls live in different places (Settings → Search → Searching Windows). The core fixes — rebuild, scope trimming, loop-busting — are the same, but the navigation paths differ."
- q: "Can I disable Cortana to fix search indexer CPU?"
  a: "Disabling Cortana's consumer features doesn't stop the indexer — they're separate components sharing some infrastructure. On Windows 10, Cortana is already neutered in most regions. The indexer's CPU usage comes from file cataloging, not the voice assistant, so focus on index scope and database health instead."
- q: "Why does indexing restart from zero after every Windows 10 update?"
  a: "Cumulative and feature updates can invalidate parts of the search index, triggering partial or full rebuilds. On Windows 10's older index format, even minor corruption from an update forces a complete rebuild. If this happens after every Patch Tuesday, your index database may have an underlying issue — a clean rebuild plus scope trimming usually stabilizes it."
- q: "Does Windows 10 indexing slow down older laptops more?"
  a: "Yes. Windows 10 runs on a large installed base of older laptops with HDDs and 4–8 GB RAM, where indexing is far more noticeable than on modern SSDs. On HDD systems, indexing competes directly with everything else for slow disk I/O. Reducing indexed locations is especially impactful on these machines — sometimes the difference between usable and unusable."
---

Windows 10's SearchIndexer.exe has been annoying users for years — longer than its Windows 11 sibling, with its own set of quirks. The Cortana-era integration, the older index database format, and the fact that so many Windows 10 machines run on HDDs all combine to make indexer CPU problems more visible and more stubborn here.

The good news: the fix principles are identical, just with Windows 10 navigation and a few version-specific gotchas. This guide is written for Windows 10 throughout — no Windows 11 paths, no confusion.

## Why this happens

- **Corrupt index database** — Windows 10's older index format corrupts more easily, especially after updates.
- **Cortana/search integration overhead** — the Start menu search pipeline adds work on top of file indexing.
- **HDD-based systems** — indexing on mechanical drives is dramatically more disruptive than on SSDs.
- **Overly broad default scope** — entire user profiles including cloud sync folders indexed by default.
- **Outlook data files** — PST/OST files hammer the indexer on machines with large mailboxes.
- **Post-update rebuilds** — cumulative updates frequently invalidate the index.
- **A looping corrupt file** — same as Windows 11: one bad file retried forever.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check indexing status in Windows 10 Settings

Windows 10 puts these controls in a different place than Windows 11.

Steps:

1. Go to **Settings → Search → Searching Windows** (left sidebar).
2. Check whether status shows "Indexing complete" or in-progress with an item count.
3. Note which option is selected: Classic (limited locations) vs. Enhanced (entire PC) — Enhanced indexes everything and is a common cause of endless indexing.
4. If Enhanced is on, switch to **Classic** immediately — this alone fixes many cases.
5. Click "Advanced Search Indexer Settings" to open the classic Indexing Options panel.

### Fix 2: Switch from Enhanced to Classic indexing

The single most impactful Windows 10-specific change.

Steps:

1. In Settings → Search → Searching Windows, select **Classic** under "Find My Files."
2. Click "Customize search locations" to open Indexing Options → Modify.
3. Review and uncheck: external drives, cloud sync folders you don't search, any entire-drive entries.
4. Keep: Start Menu, your user folder (or just Documents/Pictures).
5. Click OK — the indexer drops the excess locations and CPU should fall within hours.

### Fix 3: Rebuild the index

For the corrupt-database cases that Classic mode alone doesn't fix.

Steps:

1. Open Indexing Options (search "indexing options" in Start) → **Advanced**.
2. Under Troubleshooting, click **Rebuild** and confirm.
3. Leave the laptop plugged in and idle for several hours — initial rebuilds on HDDs can take a long time.
4. Check back in Settings → Search → Searching Windows for "Indexing complete."
5. If you're on an HDD, consider scheduling the rebuild overnight — it will be slow but thorough.

### Fix 4: Exclude Outlook data files

Windows 10 + Outlook + large PSTs is a classic indexer-killer combo.

Steps:

1. Indexing Options → Modify → uncheck **Microsoft Outlook** locations.
2. Or Advanced → File Types → uncheck `pst`, `ost`, `msg`.
3. Outlook search continues working via its own engine.
4. If you use Windows Mail instead, its data is lighter — but excluding it too doesn't hurt.
5. Allow a day for the index to shed the mailbox data and CPU to settle.

### Fix 5: Find the looping file via Event Viewer

Same forensic technique as Windows 11 — Windows 10 logs indexer failures identically.

Steps:

1. Event Viewer → Windows Logs → Application → filter Source **"Windows Search Service."**
2. Look for repeated errors naming the same file.
3. Move, repair, or delete the offending file.
4. Rebuild the index (Fix 3) to clear the stuck state.
5. Common Windows 10 culprits: corrupt files in Downloads, old PSTs, and damaged files synced from OneDrive.

### Fix 6: Reduce Cortana/search background activity

Trim the search pipeline's extras on Windows 10.

Steps:

1. Settings → Search → Permissions & History → turn off **Cloud content search** (Microsoft account + Work/school account) if you don't need web results in Start.
2. Turn off **Search history** on this device.
3. In Task Manager → Startup, disable **Cortana** if present (it serves no purpose on most systems now).
4. These reduce the search service's background work alongside the indexer.
5. For the full Windows 11 indexer treatment (useful if you're planning an upgrade), see our [Windows 11 indexer guide](/articles/how-to-fix-windows-search-indexer-high-cpu-on-windows-11/).

### Fix 7: Address HDD-specific indexing pain

If you're on a mechanical drive, indexing will always be heavier — mitigate it.

Steps:

1. Confirm your drive type: Task Manager → Performance → Disk (look for HDD vs SSD).
2. On HDDs, be extra aggressive with Fix 2's scope trimming — every indexed location costs real I/O.
3. Schedule indexing for idle time: the indexer respects the "only when idle" logic better when the scope is small.
4. Consider disabling Windows Search entirely on very old HDD laptops (Fix 8) — the tradeoff favors usability.
5. Long-term: an SSD upgrade transforms both indexing and everything else. Microsoft's [support hub](https://support.microsoft.com/en-us/windows) documents the search service options.

### Fix 8: Disable the Windows Search service (last resort)

The escape hatch for machines where the indexer simply won't behave.

Steps:

1. `Win + R` → `services.msc` → find **Windows Search**.
2. Set Startup type to **Disabled**, click Stop, OK.
3. Restart — Start menu search becomes slower (live scanning) but the CPU drain stops permanently.
4. Install **Everything** (voidtools) as a fast replacement for file search.
5. Reconsider after major Windows 10 updates — but honestly, on a machine this troubled, the SSD upgrade in Fix 7 is the real answer.

## Closing

Windows 10 indexer problems reward the same discipline as Windows 11: switch to Classic scope, trim locations, rebuild clean, exclude the churn. The Enhanced-to-Classic switch (Fix 1) is the Windows 10-specific move that resolves an outsized share of cases — many users don't even know Enhanced mode exists, silently indexing their entire PC. Once the scope is sane and the database is healthy, SearchIndexer.exe fades into the background where it belongs. If other Windows 10 background processes are also misbehaving, our [Windows 10 app-launch diagnostic](/articles/how-to-fix-apps-opening-slowly-on-windows-11-step-by-step/) uses the same ordered approach for general slowness.
