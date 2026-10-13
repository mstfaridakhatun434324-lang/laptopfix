---
title: "File Explorer High CPU on an ASUS Laptop? Fix It Fast"
slug: how-to-fix-file-explorer-high-cpu-on-asus-laptop
date: 2026-10-12
categories: ["performance"]
tags: ["file explorer", "high cpu", "asus laptop", "explorer.exe", "windows 11"]
description: "File Explorer (explorer.exe) spiking CPU on your ASUS laptop? Fix the thumbnail, cloud-sync, and shell-extension causes step by step."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-high-cpu-on-asus-laptop.webp"
faqs:
  - q: "Why does File Explorer use high CPU when I'm just browsing folders?"
    a: "Explorer generates thumbnails, extracts metadata, queries cloud-sync overlays (OneDrive/Dropbox icons), and loads third-party shell extensions for every folder you open. High CPU while browsing usually means one of those is choking — a corrupt thumbnail cache, a folder full of damaged media files, or a buggy context-menu extension from installed software."
  - q: "Is it safe to restart File Explorer from Task Manager?"
    a: "Yes, completely safe. Right-click Windows Explorer in Task Manager > Restart ends the shell and relaunches it; your open apps and unsaved work are untouched (open Explorer windows will close, though). It's the standard first-response for an Explorer that's wedged, and it takes five seconds."
  - q: "Can ASUS Armoury Crate cause File Explorer high CPU?"
    a: "Indirectly, yes. Armoury Crate and its Aura Sync components install shell extensions and background services that hook into Explorer, and outdated versions have caused sustained CPU usage in explorer.exe on several ASUS lineups. Updating Armoury Crate — or uninstalling it if you don't use its features — resolves a meaningful share of ASUS-specific Explorer CPU cases."
  - q: "Will clearing the thumbnail cache delete my files?"
    a: "No. The thumbnail cache only stores the small preview images Explorer generates; clearing it forces Explorer to regenerate previews on next visit. Your actual photos, videos, and documents are untouched. It's one of the safest maintenance operations in Windows and fixes a surprising number of Explorer performance problems."
---

File Explorer is the shell you live in — so when `explorer.exe` starts eating 25–40% CPU on your ASUS laptop, everything feels broken: folders open slowly, the taskbar stutters, and right-clicks take an eternity. The cruel irony is that Explorer rarely misbehaves on its own; it's usually being sabotaged by something plugged into it — a thumbnail it can't generate, a cloud overlay it can't resolve, or a shell extension from some installed program.

ASUS laptops add their own flavor: Armoury Crate, MyASUS background services, and Aura components all hook into the shell. This guide covers the universal Explorer fixes plus the ASUS-specific checks. For general Explorer CPU issues, see [fixing File Explorer high CPU](/articles/best-way-to-fix-file-explorer-high-cpu/); for the right-click slowness that often accompanies it, [fixing the slow context menu](/articles/best-way-to-fix-right-click-menu-slow-windows-11/).

## Why this happens

- **Corrupt thumbnail cache**: A damaged thumbcache makes Explorer regenerate thumbnails in a loop every time a folder opens.
- **Buggy third-party shell extensions**: Context-menu handlers from installed apps (archivers, cloud tools, antivirus) run inside explorer.exe — a bad one burns CPU for all of them.
- **Cloud sync overlay icons**: OneDrive/Dropbox status icons force Explorer to query sync state per file, which stalls on huge folders.
- **Damaged media files**: A corrupt video or image that the thumbnail extractor chokes on, re-attempted every folder visit.
- **ASUS Armoury Crate / Aura hooks**: Outdated ASUS shell integrations misbehaving inside the Explorer process.
- **Quick Access / Home parsing**: A pinned or recent item pointing at a dead network location makes Explorer wait on timeouts.
- **Search indexing a folder you're browsing**: The indexer and Explorer competing over the same files.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart Explorer and confirm the pattern

Establish the baseline before changing anything.

1. Open **Task Manager** (Ctrl+Shift+Esc), find **Windows Explorer** under Processes, right-click > **Restart**. The screen will blink — that's normal.
2. After restart, watch CPU for 5 minutes of normal use. If it's calm now but climbs when you open a specific folder, that folder's contents are the trigger (Fix 3).
3. If CPU climbs with no folders open, the trigger is a background hook — shell extension or ASUS service (Fixes 2 and 5).
4. Note whether high CPU correlates with OneDrive/Dropbox syncing — overlay icon queries during active sync are a known multiplier.
5. Check **Task Manager** > **Details** > right-click `explorer.exe` > **Open file location** to confirm it's the genuine `C:\Windows\explorer.exe`.

### Fix 2: Disable bad shell extensions with ShellExView

The most powerful Explorer diagnostic there is.

1. Download **ShellExView** from NirSoft (free, portable — no install needed).
2. Run it, click **Options** > **Hide all Microsoft extensions** — what's left is third-party code running inside your Explorer.
3. Sort by **Type** and look at **Context Menu** handlers first — these are the most common CPU offenders.
4. Select non-Microsoft context menu extensions and press **F7** (or right-click > **Disable Selected Items**) to disable them. Start with archivers, cloud tools, and anything from software you barely use.
5. Restart Explorer (Task Manager > **Restart**) and test. Re-enable extensions in small groups to identify the culprit — then update or uninstall its parent app. This single tool resolves the majority of persistent explorer.exe CPU cases.

### Fix 3: Clear the thumbnail cache and fix problem folders

For CPU that spikes when browsing specific folders.

1. Open **Disk Cleanup** (`cleanmgr.exe`), select your system drive, check **Thumbnails**, and run it. This deletes the corrupt cache safely.
2. Alternatively: **Settings** > **System** > **Storage** > **Temporary files** > check **Thumbnails** > **Remove files**.
3. Reopen the problem folder — Explorer regenerates thumbnails once (brief CPU, expected), then should stay calm on later visits.
4. If one specific file seems to trigger it (Explorer hangs generating its preview), move that file out and test — corrupt videos are the classic case. Re-encode or delete the damaged file.
5. For folders with thousands of images/video: switch the view to **Details** instead of large icons/thumbnails — no thumbnails, no thumbnail CPU. Consider whether you need thumbnails at all in archival folders.

### Fix 4: Quiet cloud overlay icons

Stop sync-state queries from stalling folder rendering.

1. If you use OneDrive: right-click its tray icon > **Pause syncing** for 2 hours as a test, then browse folders. Dramatic improvement confirms overlay overhead.
2. Long-term: reduce synced folder count (**OneDrive settings** > **Choose folders**) — fewer synced files means fewer per-file overlay queries.
3. In **File Explorer** > **View** > **Options** > **View** tab: check **Always show icons, never thumbnails** as a test toggle — if this fixes it, the issue is thumbnail generation, not overlays (back to Fix 3).
4. Uncheck **Display file icon on thumbnails** and **Show preview handlers in preview pane** temporarily to isolate preview-pane extractors.
5. If Dropbox or Google Drive overlays are the issue, their settings offer ** Finder/Explorer integration** toggles — disabling the overlay integration keeps sync working while removing the per-file Explorer queries.

### Fix 5: Update or remove ASUS shell hooks

The ASUS-specific step generic guides skip.

1. Open **Armoury Crate** > **Settings** > check for updates — ASUS has fixed Explorer-interacting bugs in several Armoury Crate releases.
2. In **MyASUS**, run **System Diagnostics** and install recommended updates, especially anything labeled chipset or ATK Package.
3. If you don't use Armoury Crate's features (performance profiles, Aura lighting), consider uninstalling it — many ASUS users run perfectly well on Windows power plans plus the standalone drivers. Use the official **Armoury Crate uninstall tool** from ASUS support for a clean removal.
4. Check **Task Scheduler** for ASUS tasks that scan or inventory files frequently — set aggressive ones to run weekly instead of at logon.
5. After changes, restart Explorer and monitor for a full day — ASUS service interactions sometimes only manifest after sleep/wake cycles.

### Fix 6: Fix Quick Access and folder view settings

Dead shortcuts make Explorer wait on timeouts.

1. Open **File Explorer** > **...** > **Options** > **General**: set **Open File Explorer to** > **This PC** instead of Home/Quick Access.
2. In the **Privacy** section, click **Clear** next to File Explorer history, and uncheck **Show recently used files** and **Show frequently used folders** temporarily.
3. Unpin any Quick Access items pointing to network drives, disconnected USB drives, or dead paths — right-click > **Unpin from Quick access**. Each dead path costs Explorer a timeout on every Home render.
4. Under the **View** tab in Folder Options, check **Launch folder windows in a separate process** — this isolates a crashing folder view from taking down the whole shell (slight memory cost, big stability win).
5. If you map network drives, ensure they're set to **reconnect** properly or disconnect stale mappings — a sleeping NAS is a classic Explorer CPU/timeout trap.

### Fix 7: Repair system files and reset folder views

When Explorer itself is damaged.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an elevated terminal — Explorer is a core Windows component and these repairs cover it.
2. Reset all folder views to default: **File Explorer** > **...** > **Options** > **View** > **Reset Folders** — corrupt per-folder view settings can cause repeated parsing failures.
3. Create a new local user profile and test Explorer there — a profile-specific shell corruption (damaged registry bags) won't follow you, confirming the damage is local to your profile.
4. Check Windows Update for pending cumulative updates — Explorer performance fixes ship regularly; see Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for the latest.
5. As a final measure, an in-place upgrade (Settings > **System** > **Recovery** > **Fix problems using Windows Update**) reinstalls the shell cleanly while keeping your files and apps.

## Closing

File Explorer high CPU is almost never Explorer's fault — it's the ecosystem plugged into it. Disable the rogue shell extension, clear the corrupt thumbnail cache, quiet the cloud overlays, and update ASUS's hooks, and explorer.exe drops back to the near-zero background hum it should maintain. The shell is the last thing that should be slowing you down; now it won't be.
