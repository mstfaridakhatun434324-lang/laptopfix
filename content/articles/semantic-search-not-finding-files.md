---
title: "How to Fix Semantic Search Not Finding Files in Windows 11"
slug: semantic-search-not-finding-files
date: 2026-10-20
categories: ["ai-pc"]
tags: ["semantic search", "windows search", "troubleshooting", "ai pc", "files not found", "windows 11"]
description: "Semantic search can't find your files on a Copilot+ PC? Diagnose the AI search layer and fix indexing, NPU, permission, and settings issues step by step."
thumbnail: "/images/thumbs/semantic-search-not-finding-files.webp"
faqs:
  - q: "What is semantic search in Windows 11?"
    a: "Semantic search is the AI layer on top of Windows Search available on Copilot+ PCs. Instead of only matching filenames, it understands descriptions — typing 'budget spreadsheet from March' can surface the right file even when those words never appear in its name. It runs on the NPU and needs a completed AI index to work."
  - q: "Why does semantic search find some files but not others?"
    a: "Partial results usually mean partial indexing: those files were crawled before the semantic layer finished, or they sit in folders excluded from indexing. If the gap persists for old files in indexed folders, the index database is likely damaged and needs a rebuild."
  - q: "Does semantic search work for files on OneDrive or network drives?"
    a: "OneDrive files that are synced locally can be indexed, but files that are online-only placeholders often are not processed by the semantic layer. Network drives are excluded from indexing by default. For reliable semantic results, keep the files you search in indexed local folders."
  - q: "Can I turn off semantic search and keep normal search?"
    a: "There is no single toggle labeled semantic search, but limiting indexed locations and disabling cloud-backed content reduces what the AI layer processes. Most users should not disable it, though — when the index is healthy, semantic search strictly improves on filename matching rather than replacing it."
---

Semantic search is supposed to be the smarter half of Windows 11 Search on Copilot+ PCs. You describe what you remember — "the presentation with the blue charts" — and the NPU-powered index matches meaning, not just filenames. When it works, it feels like the PC actually understands your files.

When it does not work, the experience is worse than plain old search. You know the file exists, but the natural-language query returns nothing or irrelevant results. Users often assume the AI is just bad, when in reality the semantic index is incomplete, corrupted, or starved of the NPU resources it needs.

This guide fixes that. You will confirm the feature is available, get the index healthy, rule out permissions and scope problems, and repair the NPU layer underneath — stopping once your files show up.

## Why this happens

- **Semantic index incomplete:** the AI layer needs a finished index; a half-built one returns partial results.
- **Files outside indexed locations:** anything outside your indexed folders is invisible to semantic search.
- **Corrupted index database:** damage makes the crawler skip files or serve stale embeddings.
- **NPU driver issues:** without a working NPU, the semantic model cannot process new files.
- **Online-only cloud files:** placeholders for OneDrive files are often skipped by the AI indexer.
- **Search settings misconfigured:** disabled content types or strict privacy settings can hide results.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm semantic search is available on your PC

Semantic search is a Copilot+ PC exclusive, so verify the foundation before troubleshooting results. Open Task Manager, check the Performance tab for a healthy NPU tile, and confirm Windows 11 is on a recent build — the feature needs both. If the NPU is missing or shows a warning, fix that first: our guide to [Intel AI Boost driver problems](/articles/intel-ai-boost-driver-not-installing/) covers one common vendor-specific failure. Without a working NPU, the semantic layer simply cannot run.

1. Open Task Manager and confirm the NPU tile on the Performance tab.
2. Check Settings, then System, then About for a recent Windows 11 build.
3. If the NPU is missing or erroring, repair the NPU driver first.
4. Restart the laptop after any driver change.
5. Recheck that the NPU looks healthy before continuing.

### Fix 2: Make sure your files are inside indexed locations

Semantic search can only understand files the indexer has actually processed, and Windows indexes a limited set of folders by default. Open Settings, then Privacy and security, then Searching Windows, and review which folders are included. If your missing files live on a secondary drive, in a custom folder, or on a network share, add those locations or move the files into an indexed folder.

1. Open Settings, then Privacy and security, then Searching Windows.
2. Review the folders currently included in indexing.
3. Add any missing folders that hold the files you search for.
4. Remove locations you do not need to keep the index lean.
5. Allow several plugged-in hours for the new locations to be processed.

### Fix 3: Rebuild the search index

If your files are in indexed folders and semantic search still misses them, the index database is probably damaged — the crawler may have skipped files or stored broken embeddings. Rebuilding wipes the database and recreates it from scratch; your files are never touched. Start the rebuild from Advanced indexing options and leave the laptop plugged in for several hours.

1. Open Settings, then Privacy and security, then Searching Windows.
2. Click Advanced indexing options, then the Rebuild button.
3. Confirm the rebuild when Windows asks.
4. Leave the laptop plugged in and idle for several hours.
5. Test the same natural-language query once indexing completes.

### Fix 4: Check file permissions and cloud placeholders

Files you cannot open cannot be indexed properly, and cloud placeholders trip up the semantic layer in particular. Right-click a missing file, check its properties, and confirm it opens normally — permission errors and corrupted files get skipped silently. For OneDrive files, make them available offline with "Always keep on this device," since online-only placeholders are frequently excluded from AI processing.

1. Right-click a missing file and confirm it opens without errors.
2. Check the file's security permissions for your user account.
3. For OneDrive files, set them to Always keep on this device.
4. Wait for the files to download fully.
5. Allow the indexer a few plugged-in hours, then search again.

### Fix 5: Repair the NPU and AI runtime underneath

Semantic search depends on the NPU twice over: once to build embeddings during indexing, and again to interpret your query. If results are consistently wrong rather than merely missing, the model pipeline itself may be degraded by a faulty driver. Update the NPU driver from your manufacturer's support site and install all Windows updates. Related AI features share this stack — for example, a broken [Restyle Image tool in Cocreator](/articles/restyle-image-cocreator-not-working/) often traces back to the same driver problem.

1. Update the NPU driver from your laptop maker's support page.
2. Install all pending Windows 11 updates and restart.
3. Confirm the NPU tile is healthy in Task Manager.
4. Rebuild the search index so embeddings regenerate cleanly.
5. Test semantic queries again after the rebuild finishes.

### Fix 6: Check Recall and system health for deeper corruption

On Copilot+ PCs, semantic search shares infrastructure with Recall's snapshot processing, and system-level corruption can poison both. If nothing above helped, run System File Checker from an elevated terminal to repair Windows components. Also review Recall's settings for errors — [Recall failing with BitLocker enabled](/articles/recall-not-working-bitlocker-enabled/) is one example of how storage-layer problems cascade into AI features. Fix any underlying errors, rebuild the index a final time, and retest.

1. Open an elevated Terminal or Command Prompt.
2. Run `sfc /scannow` and let it finish.
3. Restart the laptop if repairs were made.
4. Check Recall settings for snapshot or storage errors.
5. Rebuild the search index and test your queries again.

## Closing

Semantic search fails quietly — no error, just missing results — which makes it tempting to blame the AI. In practice the cause is almost always an incomplete or damaged index, files outside the indexed scope, or an unhealthy NPU. Fix those layers in order and your files will start answering to descriptions again. Microsoft's own notes on search and AI features live on the [Windows support site](https://support.microsoft.com/en-us/windows) — a good reference when behavior changes after an update.
