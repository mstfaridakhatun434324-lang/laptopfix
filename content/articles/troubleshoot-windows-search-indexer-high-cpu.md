---
title: "Troubleshoot Windows Search Indexer High CPU"
slug: troubleshoot-windows-search-indexer-high-cpu
date: 2026-09-20
categories: ["performance"]
tags: ["search indexer", "high cpu", "windows search", "indexing", "searchindexer.exe"]
description: "SearchIndexer.exe burning CPU? Troubleshoot Windows Search indexing: find what's churning, fix the index, and scope it correctly."
thumbnail: "/images/thumbs/troubleshoot-windows-search-indexer-high-cpu.webp"
faqs:
  - q: "What does the Windows Search indexer do?"
    a: "The indexer (SearchIndexer.exe) crawls your files, emails, and settings to build a searchable database, so Start-menu and File Explorer searches return instant results. It runs in the background, prioritizing idle time. High CPU from it means it's actively crawling — normal after big changes (updates, new files), abnormal when it never stops."
  - q: "Is it safe to disable Windows Search indexing?"
    a: "Disabling the Windows Search service is safe but degrades search: Start-menu and Explorer searches become slow filename-only scans. A better middle ground is scoping the index (fewer locations, no file contents) rather than killing the service. Only fully disable it if you never use Windows search and the indexer demonstrably misbehaves after repair attempts."
  - q: "Why is the indexer rebuilding constantly?"
    a: "Constant rebuilds signal either a corrupt index database (Windows keeps restarting the crawl), an included folder with endless churn (a downloads folder, dev build outputs, or a cloud-synced folder changing constantly), or a permissions problem where the indexer can't complete and retries. Fixing the scope or rebuilding the index cleanly resolves most loops."
  - q: "How long should initial indexing take?"
    a: "On a typical laptop with 100–300 GB of indexed content: a few hours of plugged-in idle time. It pauses when you're actively using the machine, so elapsed wall-clock time can be a day or two of normal use. If it's still going hard after a week with no big file changes, something is wrong — usually scope or corruption."
---

`SearchIndexer.exe` at 20–40% CPU for hours is Windows Search doing its job badly — or doing a reasonable job on an unreasonable workload. The indexer is supposed to be a polite background citizen: crawl when idle, pause when you're working. When it burns CPU all day, either the index is corrupt (and it's stuck retrying), or you've pointed it at folders that change endlessly (and it can never finish). The troubleshooting path distinguishes the two fast.

Check the indexer's current state first: **Settings** > **Privacy & security** > **Searching Windows** shows index status and what's included. For the question-format companion see [fixing search indexing high CPU](/articles/how-do-i-fix-search-indexing-high-cpu-windows-11/); for the nuclear option see [disabling search indexing](/articles/how-to-disable-search-indexing-on-windows-11/).

## Why this happens

- **Corrupt index database**: Damaged index causing endless rebuild loops.
- **High-churn folders indexed**: Downloads, build outputs, cloud-synced folders changing faster than the crawl.
- **Post-update re-indexing**: Major updates invalidating the index, triggering a full rebuild.
- **File-contents indexing on huge files**: Deep content parsing of archives, PSTs, or developer artifacts.
- **Permissions failures**: Folders the indexer can't read, retried forever.
- **Outlook/PST churn**: Large mail stores re-indexing on every sync.
- **Stuck at 0% / never completing**: The classic corrupt-index symptom.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check what the indexer is actually doing

Look before changing.

1. Go to **Settings** > **Privacy & security** > **Searching Windows** — note the indexed locations count and whether it says indexing is in progress.
2. Open **Indexing Options** (search in Start) — click **Modify** and review every included location. Anything surprising (entire secondary drives, network paths, cloud folders) is suspect.
3. In Task Manager, confirm **SearchIndexer.exe** (or **SearchHost.exe**) is the actual CPU consumer — don't blame the indexer for another process's burn.
4. Note the pattern: constant CPU since boot (stuck/corrupt) vs. spikes during specific activity (churn folders) vs. heavy for a day after an update (normal rebuild).
5. Check **Event Viewer** > **Applications and Services Logs** > **Microsoft** > **Windows** > **Search** > **Operational** for indexer errors — they often name the failing location.

### Fix 2: Scope the index to sane locations

The highest-impact fix for churn problems.

1. In **Indexing Options** > **Modify**, uncheck everything except: **Start Menu**, **Users** (your user folder), and **Offline Files** if used.
2. Specifically exclude: Downloads, game libraries, development folders (especially build/output dirs), VM folders, cloud-synced roots (OneDrive/Dropbox — their contents churn), and any network locations.
3. Click **OK** and give it an hour — CPU should drop as the indexer stops crawling the excluded churn.
4. In **Searching Windows** settings, set **Find my files** to **Classic** (libraries + desktop) instead of **Enhanced** (entire PC) — Enhanced is the number-one cause of never-ending indexing.
5. Re-check Task Manager after the scope change — this single fix resolves most chronic indexer CPU cases.

### Fix 3: Turn off file-contents indexing for heavy types

Stop deep-parsing files that don't need it.

1. In **Indexing Options** > **Advanced** > **File Types** tab — review which extensions index **properties and file contents**.
2. Change heavy, low-value types to **Index Properties Only**: archives (zip, rar, 7z), disk images (iso), video files, PST/OST (if Outlook search isn't critical), and developer artifacts (log, bin, obj).
3. Keep contents indexing for document types you actually search inside (docx, pdf, txt) — that's the feature's real value.
4. Click **OK**, then **Rebuild** (Advanced tab) to apply the new rules to a fresh index — schedule this overnight, plugged in.
5. After the rebuild completes, searches still find filenames everywhere indexed, and contents only where it matters — with far less CPU.

### Fix 4: Rebuild a corrupt index

For the stuck-at-it-forever cases.

1. **Indexing Options** > **Advanced** > **Rebuild** — deletes the index database and starts clean. Takes several hours; leave the laptop plugged in and idle.
2. Before rebuilding, fix the scope (Fix 2) — rebuilding with a bad scope just recreates the problem.
3. Check disk space first — the index database needs room; under 10% free on C:, the rebuild itself struggles.
4. Run `sfc /scannow` if rebuilds repeatedly corrupt — system file damage can break the indexer persistently.
5. After a clean rebuild with sane scope, the indexer should go quiet within a day — if it doesn't, the cause is external (Fix 5).

### Fix 5: Handle the external churn sources

When the index is fine but the workload is infinite.

1. **Outlook**: huge OST/PST files re-index on every mail sync — in Outlook, reduce cached mail (Account Settings > **Mail to keep offline**) or exclude Outlook from indexing if you search mail in the web client.
2. **Cloud sync**: folders syncing constantly (shared Dropbox folders, active OneDrive collaboration) — exclude them from the index; search them via the cloud service instead.
3. **Developer folders**: `node_modules`, build outputs, `.git` directories — exclude aggressively; nobody full-text-searches compiled artifacts.
4. **Antivirus interplay**: real-time scanning of the index database location can fight the indexer — the index lives under `C:\ProgramData\Microsoft\Search`; don't exclude it from AV (that's risky), but ensure AV isn't quarantining index files.
5. After excluding churn sources, monitor for 48 hours — the indexer should settle into brief, occasional activity.

### Fix 6: Repair or reset Windows Search

When the indexer itself is broken.

1. Run the **Search and Indexing** troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Restart the Windows Search service: `services.msc` > **Windows Search** > **Restart** (set Startup to **Automatic (Delayed Start)** to reduce boot-time indexing).
3. Re-register the search components: in an elevated PowerShell, run the search reset — or use **Settings** > **Apps** > **Installed apps** > **Windows Search** > **Advanced options** > **Reset** where available.
4. Check for Windows updates — search/indexer bugs are fixed in cumulative updates; verify your build is current at [Microsoft's Windows support](https://support.microsoft.com/en-us/windows).
5. Final option: disable the **Windows Search** service (services.msc > Disabled) — searches get slower but the CPU burn ends permanently. Only after the repair attempts above.

## Closing

Search indexer high CPU is a workload problem or a corruption problem, and the state page plus Indexing Options tells you which in two minutes. Scope the index to locations that don't churn, stop deep-indexing file types you never search inside, rebuild once cleanly — and the indexer goes back to being the quiet background helper it was designed to be. An index that never finishes isn't indexing; it's just spinning.
