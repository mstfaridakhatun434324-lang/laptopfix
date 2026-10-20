---
title: "How to Fix Windows Search AI Indexing Being Too Slow"
slug: windows-search-ai-indexing-slow
date: 2026-10-20
categories: ["ai-pc"]
tags: ["windows search", "ai indexing", "troubleshooting", "ai pc", "search slow", "windows 11"]
description: "Windows Search AI indexing crawling on your Copilot+ PC? Learn why semantic indexing stalls and how to speed it up with settings, driver, and index fixes."
thumbnail: "/images/thumbs/windows-search-ai-indexing-slow.webp"
faqs:
  - q: "Why is Windows Search indexing so slow on my new Copilot+ PC?"
    a: "A new PC builds its entire search index from scratch, and the AI semantic layer adds extra processing on top. Give it a few days of plugged-in idle time. If indexing still crawls after a week, a stuck indexer, a corrupted database, or a throttled NPU is the likely cause."
  - q: "Does AI indexing use the NPU, and does it drain the battery?"
    a: "Yes, the semantic understanding layer runs on the NPU to keep it efficient, which is why it is a Copilot+ PC feature. During the initial index build you may notice extra power draw, but it settles once indexing completes. If the NPU is stuck at high usage for weeks, the indexer itself is probably looping."
  - q: "Can I speed up indexing by changing which folders are indexed?"
    a: "Absolutely. Every extra folder, especially network drives and huge media collections, adds work. Trim the indexed locations in Settings to the folders you actually search, and exclude anything you never need. Fewer locations mean a smaller index that builds and updates much faster."
  - q: "Will rebuilding the index delete my files?"
    a: "No. Rebuilding only deletes and recreates the search database; your files, photos, and documents stay exactly where they are. The trade-off is that search results will be incomplete while the rebuild runs, so start it when you can leave the laptop plugged in for several hours."
---

Windows 11 on Copilot+ PCs adds an AI layer to Search. Beyond matching filenames, it builds semantic embeddings of your documents, photos, and settings so you can type a description — "the sunset beach photo" — and find the right file.

When that indexer is too slow, the symptoms pile up. New files take days to appear in results, searches feel no smarter than before, and the indexer process seems permanently busy in Task Manager. Some of this is normal first-pass work on a new laptop, but indexing that never finishes points to a real problem.

This guide explains what makes AI indexing slow and how to fix it. You will trim the workload, unstick the indexer, repair its database, and check the NPU it depends on — quickest wins first.

## Why this happens

- **First-pass indexing is unfinished:** a new or reset PC needs days of idle time to build the full index.
- **Too many indexed locations:** network drives and giant media folders multiply the indexer's workload.
- **Indexer throttled on battery:** Windows slows background indexing to save power when unplugged.
- **Corrupted search database:** a damaged index makes the crawler loop or stall instead of progressing.
- **NPU driver problems:** the semantic layer needs a healthy NPU; driver issues starve it.
- **Disk or system overload:** heavy background apps and a nearly full drive slow every crawl pass.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give the first pass time — plugged in and idle

Before changing anything, check whether the indexer is simply still doing its initial build. Open Settings, then Privacy and security, then Searching Windows, and look at the indexing status: if it shows a large number of items remaining, the system is working as designed. Leave the laptop plugged in, connected to power, and idle overnight — indexing throttles on battery, so a laptop that is always unplugged may never finish.

1. Open Settings, then Privacy and security, then Searching Windows.
2. Note the indexing status and how many items remain.
3. Plug the laptop into power and leave it idle overnight.
4. Recheck the remaining count the next morning.
5. If the count is stuck, continue with Fix 2.

### Fix 2: Trim indexed locations to what you actually search

Every folder you include costs indexing time, and the defaults are generous — they often cover entire user profiles plus locations you never search. In Searching Windows settings, use the folder exclusion list to drop heavy media archives, game installs, and network drives. A smaller index builds faster, updates faster, and returns results faster.

1. Open Settings, then Privacy and security, then Searching Windows.
2. Review the list of indexed folders.
3. Remove or exclude folders you never search, like game libraries.
4. Exclude network drives and huge archived media collections.
5. Let the indexer run and watch the remaining count drop.

### Fix 3: Rebuild the search index

When the remaining-items count is frozen or the indexer loops forever, the database itself is usually corrupted. Rebuilding deletes the index and starts clean — your files are untouched, only the search database is recreated. Find the option in Advanced indexing options, then Rebuild, and do not interrupt it.

1. Open Settings, then Privacy and security, then Searching Windows.
2. Click Advanced indexing options near the bottom.
3. In the dialog, click the Rebuild button.
4. Confirm and leave the laptop plugged in for several hours.
5. Verify new files start appearing in search results.

### Fix 4: Check the NPU the semantic layer depends on

AI indexing's semantic understanding runs on the NPU, so a broken NPU driver quietly cripples it — searches keep working at the old filename level while the smart layer never completes. Open Task Manager and confirm the NPU tile is present and not erroring; if Windows cannot see the neural processor at all, our [NPU driver error code 43](/articles/npu-driver-error-code-43/) guide covers that exact failure. Update the NPU driver from your laptop maker's support page and restart.

1. Open Task Manager and check the NPU tile on the Performance tab.
2. If the NPU is missing or erroring, fix the driver first.
3. Download the latest NPU driver from your manufacturer's support site.
4. Install it and restart the laptop.
5. Recheck indexing status in Settings after the restart.

### Fix 5: Stop resource hogs from starving the indexer

The indexer is a background citizen: when the CPU, disk, or memory is saturated, Windows deprioritizes it and progress crawls. Open Task Manager and look for processes hammering the disk or CPU — cloud sync tools doing an initial upload are a classic culprit. Pause heavy syncs and make sure the drive has at least 10 to 15 percent free space. If [semantic search still cannot find files](/articles/semantic-search-not-finding-files/) after indexing completes, that is a separate retrieval problem worth investigating on its own.

1. Open Task Manager and sort processes by CPU and Disk.
2. Identify anything saturating resources for extended periods.
3. Pause cloud sync uploads or heavy background tasks temporarily.
4. Free up disk space to at least 10 to 15 percent free.
5. Leave the laptop idle and confirm indexing progress resumes.

### Fix 6: Repair Recall and system components if slowness persists

On Copilot+ PCs the AI search index shares infrastructure with Recall snapshots, and a damaged Recall database can drag the whole semantic pipeline down. If indexing is still stuck after the fixes above, check Recall's settings and storage health — a [corrupted Recall database](/articles/recall-database-corrupted-fix/) is a documented cause of endless background AI processing. As a final step, run the System File Checker to repair Windows components the indexer depends on.

1. Open an elevated Command Prompt or Terminal.
2. Run `sfc /scannow` and wait for it to complete.
3. Restart the laptop after any repairs.
4. Check Recall settings for snapshot errors or storage warnings.
5. Rebuild the search index once more if corruption was found and fixed.

## Closing

Slow AI indexing is usually a workload problem — too many folders, an unfinished first pass, or a corrupted database — rather than a hardware defect. Trim the scope, rebuild once, keep the laptop plugged in, and the semantic layer will finish its work and get out of your way. For the official rundown of how indexing is supposed to behave, see the troubleshooting guidance on the [Windows support site](https://support.microsoft.com/en-us/windows).
