---
title: "File Explorer High CPU? Fix It Step by Step"
slug: how-to-fix-file-explorer-high-cpu-step-by-step
date: 2026-09-05
categories: ["performance"]
tags: ["file explorer", "high cpu", "explorer.exe", "step by step"]
description: "Explorer.exe burning CPU on Windows 11? Step-by-step fixes for thumbnail loops, shell extensions, cloud overlays, and corrupt caches."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-high-cpu-step-by-step.webp"
faqs:
  - q: "Why does File Explorer use high CPU even when I'm not using it?"
    a: "Explorer.exe does background work constantly: generating thumbnails, updating cloud-sync overlay icons (OneDrive, Dropbox), refreshing network folder contents, and running shell extensions loaded by third-party apps. High CPU at idle usually means one of these background jobs is stuck — a thumbnail generator looping on a corrupt image, a cloud overlay fighting over icon states, or a buggy shell extension. The Details tab in Task Manager confirms whether it's really explorer.exe."
  - q: "Can I just end File Explorer to stop the high CPU?"
    a: "Ending explorer.exe kills your taskbar and desktop along with it — Windows restarts it automatically, and the CPU problem comes right back because the underlying trigger (thumbnail cache, shell extension, overlay) reloads too. Restarting Explorer is a useful temporary reset (Task Manager > right-click Windows Explorer > Restart), but the permanent fix is finding and removing the trigger with the steps in this guide."
  - q: "Do cloud storage apps cause File Explorer high CPU?"
    a: "Frequently, yes. OneDrive, Dropbox, Google Drive, and similar apps install shell overlay handlers that Explorer queries for every file icon — with multiple cloud apps installed, each file gets several overlay lookups. Sync conflicts, huge synced folders, and stuck uploads multiply the work. If Explorer CPU spikes when browsing synced folders but not elsewhere, a cloud overlay is the prime suspect."
  - q: "Will clearing the thumbnail cache delete my pictures?"
    a: "No. The thumbnail cache only stores the small preview images Windows generates — your actual photos, videos, and documents are untouched. Deleting the cache (Disk Cleanup > Thumbnails) just forces Windows to regenerate previews on next view, which fixes the corrupt-cache loops that cause sustained Explorer CPU usage. It's one of the safest fixes in this guide."
---

`explorer.exe` is the shell you live in — taskbar, desktop, file windows — so when it burns CPU, everything feels broken. The tricky part is that Explorer itself is rarely at fault: it's the ecosystem around it (thumbnails, shell extensions, cloud overlays, preview handlers) doing the damage. This guide walks you through identifying which hanger-on is guilty and removing it, step by step.

Restarting Explorer (Task Manager > Windows Explorer > Restart) is fine as a momentary reset, but the CPU always comes back until the trigger is gone. Work the list in order — each fix targets one of Explorer's hangers-on, and the testing notes tell you when to stop. If the whole system is slow beyond Explorer, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Corrupt thumbnail cache**: The thumbnail database loops regenerating previews for damaged files.
- **Buggy shell extensions**: Third-party right-click menu handlers with inefficient or broken code.
- **Cloud overlay overload**: Multiple sync apps' icon overlays queried for every file.
- **Preview pane on huge files**: The preview pane trying to render massive videos or documents.
- **Network folder polling**: Explorer constantly refreshing slow or dead network locations.
- **Corrupt Quick Access**: Damaged frequent-folders data causing refresh loops.
- **Search indexing interaction**: Explorer and the indexer amplifying each other on big folders.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's explorer.exe and find the trigger folder

Narrow down where the CPU burns.

1. Open **Task Manager** > **Details** tab — confirm `explorer.exe` CPU, and note whether it spikes only when specific folders are open.
2. Open File Explorer to different locations (Documents, a photo folder, a network drive) and watch CPU per location — folder-specific spikes implicate thumbnails or overlays in that folder.
3. Close all Explorer windows and wait 2 minutes — CPU that persists with no windows open points to shell extensions or background handlers.
4. Check whether the **Preview pane** (**View** > **Show** > **Preview pane**) is on — turn it off as a test.
5. This tells you which fixes below to prioritize: thumbnails, overlays, extensions, or network.

### Fix 2: Clear the thumbnail cache

Fix the most common corrupt-cache loop.

1. Open **Disk Cleanup** (`cleanmgr.exe`), select C:, check **Thumbnails**, and click OK.
2. For a deeper clear, open **File Explorer** > **View** > **Show** > **Hidden items**, then delete all `thumbcache_*.db` files in `%LOCALAPPDATA%\Microsoft\Windows\Explorer`.
3. Restart Explorer (**Task Manager** > **Windows Explorer** > **Restart**) or reboot.
4. Browse the previously problematic folder — thumbnails regenerate cleanly; expect brief CPU during regeneration only.
5. If CPU spikes return in the same folder, a specific corrupt media file is the trigger — identify it (often the file whose thumbnail never renders) and move or repair it.

### Fix 3: Disable problematic shell extensions

Remove the third-party code running inside Explorer.

1. Download **ShellExView** (NirSoft) — it lists all shell extensions with their vendors.
2. Sort by **Company** and disable all **non-Microsoft** context-menu extensions (select > right-click > **Disable Selected Items**).
3. Restart Explorer and test CPU for 15 minutes — a dramatic drop confirms a shell extension culprit.
4. Re-enable extensions in small groups until CPU returns — the last group contains the offender; leave it disabled or update that app.
5. Usual suspects: outdated archivers, old cloud clients, "tune-up" utilities, and abandoned freeware.

### Fix 4: Tame cloud storage overlays

Reduce the per-file overlay tax.

1. If you run multiple cloud apps (OneDrive + Dropbox + Google Drive), consider whether you need all three — each adds overlay lookups to every file.
2. In each cloud app's settings, disable ** Finder/Explorer integration** or **overlay icons** if the option exists and you can live without sync badges.
3. Resolve any **sync conflicts** or stuck uploads — conflicted states multiply overlay queries (see [OneDrive high CPU fix](/articles/how-to-fix-onedrive-sync-high-cpu-on-windows-11/)).
4. Exclude giant folders from syncing if you don't need them locally.
5. Test Explorer CPU in synced vs. non-synced folders to confirm the improvement.

### Fix 5: Fix Quick Access and folder view corruption

Clear damaged Explorer state data.

1. Open **File Explorer** > **...** > **Options** > **General** tab > **Clear** next to "Clear File Explorer history."
2. Set **Open File Explorer to** to **This PC** instead of Home/Quick Access — damaged frequent-items data is a known CPU loop source.
3. Delete the automatic destinations: `%APPDATA%\Microsoft\Windows\Recent\AutomaticDestinations\*` (this resets jump lists — safe).
4. Restart Explorer and test.
5. If Quick Access was the trigger, leave it on This PC permanently.

### Fix 6: Address network location polling

Stop Explorer from waiting on dead network paths.

1. In **File Explorer**, disconnect dead network drives (**This PC** > right-click > **Disconnect**).
2. Remove offline printers and disable **Offline Files** if unused (**Control Panel** > **Sync Center**).
3. In **Folder Options** > **View**, uncheck **Automatically search for network folders and printers**.
4. Test Explorer CPU with no network locations present — network-timeout loops are a classic hidden cause.
5. Re-add only the network resources you actively use.

### Fix 7: Repair system files and reset Explorer

Fix OS-level damage as the final step.

1. Elevated **Command Prompt**: `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Install pending updates via **Settings** > **Windows Update** — Explorer CPU regressions get patched; see [Microsoft support](https://support.microsoft.com/en-us/windows).
3. As a deeper reset, create a new local user profile — per-user Explorer settings and caches that resist all cleaning live in the profile.
4. Test Explorer CPU in the new profile; migrate if it's clean.
5. Final option: in-place repair install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps.

## Closing

Explorer.exe high CPU is guilt by association — thumbnails, shell extensions, cloud overlays, and network timeouts doing their damage inside the shell's process. Isolate the trigger folder, clear the thumbnail cache, audit shell extensions with ShellExView, and tame the cloud overlays. Worked in order, these steps find the real culprit instead of just restarting the victim — and a calm Explorer usually means a calm taskbar and desktop too.
