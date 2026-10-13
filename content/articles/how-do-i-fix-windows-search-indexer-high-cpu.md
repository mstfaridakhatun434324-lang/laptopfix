---
title: "Windows Search Indexer High CPU? Fix SearchIndexer.exe Spikes"
slug: "how-do-i-fix-windows-search-indexer-high-cpu"
date: "2026-10-04"
categories: ["performance"]
tags: ["search indexer", "searchindexer.exe", "high cpu", "windows search", "indexing"]
description: "SearchIndexer.exe eating your CPU? Learn why Windows Search indexing spikes, how to rebuild a corrupt index, and when to limit or disable indexing."
thumbnail: "/images/thumbs/how-do-i-fix-windows-search-indexer-high-cpu.webp"
faqs:
  - q: "What is SearchIndexer.exe and is it safe?"
    a: "SearchIndexer.exe is the legitimate Windows Search indexing service — it crawls your files, emails, and Start menu entries to build the database that makes instant search work. It's a genuine Microsoft process signed and located in System32, and it's completely safe. High CPU from it means the index is being built, rebuilt, or is corrupted and looping — not malware. (Malware impersonating the name would live outside System32, which is worth one verification check.)"
  - q: "How long should initial indexing take?"
    a: "On an SSD with a typical user profile (50-100 GB of indexed content), initial indexing usually completes in 30 minutes to a few hours. On a mechanical HDD with hundreds of gigabytes, it can take a full day or more of plugged-in idle time. If indexing never completes after 48 hours of idle opportunity, the index is corrupted — not slow — and needs a rebuild, not more patience."
  - q: "Will disabling indexing speed up my computer?"
    a: "On SSDs, disabling indexing yields almost no speedup and you lose instant file search — a bad trade. On mechanical HDDs, disabling it can noticeably reduce background disk/CPU churn, which is why it's a legitimate option there. The middle path suits most people: keep indexing on but shrink the indexed locations to folders you actually search, excluding video archives and game libraries."
  - q: "Why does indexing restart from scratch after every Windows update?"
    a: "Feature updates sometimes invalidate the search database format or reset indexed locations, triggering a full rebuild — that's why SearchIndexer spikes for a day or two after each major update. Cumulative (monthly) updates don't do this. If full rebuilds happen without any update, something is corrupting the database — disk errors, aggressive 'privacy' tools deleting the index, or a failing drive."
---

SearchIndexer.exe is supposed to be a background citizen — quietly cataloging your files so Start-menu search feels instant. But when the index corrupts or a major update triggers a rebuild, it transforms into a CPU and disk hog that runs for days, heats up your laptop, and makes everything else stutter. The Task Manager reading is unmistakable; the fix depends on which of three states you're in.

Those three states: legitimate first-time indexing (wait it out), a corrupted index looping forever (rebuild it), or an index that will never be worth its cost on your hardware (shrink or disable it). Most guides jump straight to 'disable indexing' — which throws away instant search to fix what a ten-minute rebuild would have cured. This guide diagnoses first.

The steps below work identically on Windows 10 and 11. If your search UI itself (not the indexer) is the CPU hog, see our [Cortana/SearchHost fix guide](/articles/how-to-fix-cortana-high-cpu-on-lenovo-laptop/) — different process, different fixes.

## Why this happens

- **Post-update full rebuild** — Feature updates invalidate the index format, triggering a from-scratch rebuild that legitimately consumes heavy CPU/disk for hours — self-resolving if left alone.
- **Corrupted index database** — Crashes, disk errors, or killed indexing processes corrupt the database; the indexer then loops — scanning, failing, restarting — forever, never finishing.
- **Too many indexed locations** — Indexing entire secondary drives, network shares, or 500 GB media archives multiplies the workload far beyond what instant search needs.
- **Outlook/PST churn** — Large Outlook data files that change constantly (or a corrupted PST) keep the indexer re-crawling mail indefinitely — a classic corporate-laptop cause.
- **'Privacy' tools deleting the index** — Aggressive cleaner apps that wipe the search database on every run force a full rebuild each time — the indexer can never finish.
- **Disk errors corrupting the database files** — Bad sectors where the index lives cause silent corruption; the indexer retries, fails, retries — permanent high CPU until the disk is fixed.
- **Stuck on a single file** — A corrupted file with a broken property handler (often a damaged video or Office file) can hang the indexer on one item indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check indexing status first

Don't 'fix' a healthy indexer that's just working.

1. Open **Control Panel > Indexing Options** and read the status line at the top.
1. 'Indexing complete' + high CPU = corrupted loop or stuck file (continue below). 'Indexing in progress' with a count climbing = legitimate work; give it plugged-in idle time.
1. Click **Modify** to see how many locations are indexed — thousands of folders on secondary drives is a red flag.
1. This one screen tells you whether to wait, rebuild, or shrink.

### Fix 2: Give legitimate indexing its chance

If it's genuinely building, the fix is idle time — not tweaks.

1. Leave the laptop plugged in, lid open (or set to do nothing when closed), overnight.
1. Pause CPU-heavy apps so the indexer gets its I/O window — it politely yields to foreground work, which is why it never finishes on a busy machine.
1. Check status in the morning. Completed = done forever (until the next feature update). Still 'in progress' after 48 idle hours = corruption; proceed.

### Fix 3: Rebuild a corrupted index

The definitive fix for the infinite loop — ten clicks, a few hours.

1. **Control Panel > Indexing Options > Advanced > Rebuild** > confirm.
1. The old database is deleted and indexing restarts clean — CPU will be high during the rebuild itself, which is normal and temporary.
1. Leave it plugged in and idle; don't judge results until Indexing Options says 'Indexing complete'.
1. If it never completes across two rebuild attempts, suspect disk errors (Fix 6) or a stuck file (Fix 5).

### Fix 4: Shrink indexed locations to what you search

Most people search Documents and Start Menu — not their Steam library.

1. **Indexing Options > Modify**: uncheck secondary drives, game folders, video archives, and cloud-sync roots you never search.
1. Keep checked: Start Menu, Users\<you>\Documents, and any work folder you actually search daily.
1. After shrinking, do one final **Rebuild** so the database matches the new scope — future indexing load drops permanently.
1. Our [search indexing disable guide](/articles/how-to-disable-search-indexing-on-windows-10/) covers the full-disable path if shrinking isn't enough.

### Fix 5: Hunt the stuck file

When the indexer hangs at the same count forever, one file is the culprit.

1. Watch the indexing count in Indexing Options for 30 minutes — if the 'items indexed' number never moves, it's stuck.
1. Think about recently added files: downloaded videos, large email attachments, new photo imports — move suspects out of indexed folders temporarily.
1. Corrupted video files are the most common hangers; re-encode or delete the suspect.
1. Rebuild after removing it and confirm the count now climbs steadily.

### Fix 6: Check the disk underneath

An index can't be healthy on a sick drive.

1. Run `chkdsk C: /f` from an admin Command Prompt (reboot to complete) to fix file-system errors.
1. Check SMART status with CrystalDiskInfo — reallocated sectors near the index location cause exactly this corruption loop.
1. If the drive is failing, replace it before fighting the indexer further — no rebuild survives bad sectors.
1. After disk repair, do one clean rebuild (Fix 3).

### Fix 7: Disable indexing (HDDs and special cases)

The legitimate last resort — with eyes open about the tradeoff.

1. Open `services.msc`, find **Windows Search**, double-click, **Stop** it, and set **Startup type** to **Disabled**.
1. Consequence: Start-menu file search becomes slow (it falls back to live crawling); app and settings search still work.
1. Best suited to: mechanical-HDD laptops where indexing never finishes, and users who navigate by folders rather than search.
1. To re-enable later, set the service back to **Automatic (Delayed Start)** and rebuild once.

## Closing

SearchIndexer.exe high CPU is a three-way diagnosis — working, corrupted, or unwanted — and each has its own fix. Rebuild the corrupted, shrink the bloated, and only disable as a last resort. Instant search is worth keeping when the index is healthy; it's the broken index that's the enemy, not the feature. Microsoft documents indexing behavior in detail in the [Windows support hub](https://support.microsoft.com/en-us/windows).
