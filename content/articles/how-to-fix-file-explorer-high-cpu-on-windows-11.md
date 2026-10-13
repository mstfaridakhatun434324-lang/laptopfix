---
title: "How to Fix File Explorer High CPU on Windows 11"
slug: how-to-fix-file-explorer-high-cpu-on-windows-11
date: 2026-09-23
categories: ["performance"]
tags: ["file explorer", "high cpu", "explorer.exe", "windows 11"]
description: "Explorer.exe spiking your CPU on Windows 11? Fix shell extension conflicts, thumbnail overload, and Quick Access issues that make File Explorer burn cycles."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-high-cpu-on-windows-11.webp"
faqs:
  - q: "Why does File Explorer use high CPU even when I'm not browsing files?"
    a: "Explorer.exe isn't just file windows — it's the entire Windows shell: taskbar, desktop, Start menu, and notification area. High CPU at idle usually means a misbehaving shell extension (right-click menu add-ons from third-party apps), thumbnail generation stuck on a corrupt media file, or Quick Access trying to reach an unreachable network location. The window you see is rarely the actual problem."
  - q: "Is it safe to restart or end Explorer.exe?"
    a: "Yes. Ending Explorer.exe only kills the shell — your apps keep running. The taskbar and desktop disappear, then you restart it via Task Manager > File > Run new task > explorer.exe. It's the standard quick fix for a glitched Explorer and is completely safe. If CPU spikes return immediately after restart, though, the trigger (extension, thumbnail, network path) is still there."
  - q: "Can right-click menu extensions cause Explorer high CPU?"
    a: "Absolutely — they're the single most common cause. Every context-menu handler from installed apps loads into Explorer's process, and one buggy handler can spin the CPU whenever you right-click or even hover. Use ShellExView (NirSoft) to disable non-Microsoft context-menu extensions in bulk, then re-enable in halves to find the culprit. Cloud-storage overlays are frequent offenders."
  - q: "Why does Explorer spike CPU when I open folders with videos or photos?"
    a: "That's thumbnail generation. Explorer extracts thumbnails and metadata for every media file in the folder, and a single corrupt video or RAW photo can make the thumbnail extractor loop. Switching the folder to Details view, clearing the thumbnail cache, or excluding the problem file fixes it. Folders with thousands of media files are inherently slow — split them up."
---

`Explorer.exe` at 20–40% CPU is disorienting because File Explorer is supposed to be lightweight — it's just windows showing files, right? Except Explorer.exe is also the entire Windows shell: the taskbar, desktop icons, Start menu, and system tray all live in that one process. So "File Explorer high CPU" can mean a stuck thumbnail, a toxic right-click extension, or the shell itself struggling — and the fix depends on which one you've got. If Explorer is merely slow rather than CPU-hungry, our [File Explorer slowness guide](/articles/how-to-fix-file-explorer-slow-windows-11-step-by-step/) covers that side; for overall system drag, the [Windows 11 speed-up checklist](/articles/laptop-running-slow-windows-11-how-to-speed-up/) applies.

## Why this happens

- **Buggy shell extensions**: Third-party right-click menu handlers load into Explorer and can spin the CPU on every interaction.
- **Thumbnail generation loops**: A corrupt video or image file makes the thumbnail extractor retry endlessly.
- **Quick Access pointing at dead locations**: Pinned folders on disconnected network drives or removed USB drives cause timeout retries.
- **Cloud storage overlay icons**: OneDrive/Dropbox status icons re-evaluate on every folder refresh.
- **Preview pane on a problem file**: The preview handler for a malformed document burns CPU trying to render it.
- **Corrupt thumbnail or icon cache**: Damaged cache databases cause constant regeneration attempts.
- **Windows 11 tabbed Explorer glitches**: The tabbed interface occasionally leaks handles on rapid tab open/close cycles.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart Explorer and confirm the pattern

A clean restart tells you whether it's a transient glitch or a persistent trigger.

1. Open **Task Manager**, find **Windows Explorer** under Processes, right-click > **Restart**. The taskbar will vanish and return — this is normal.
2. Watch CPU for 5 minutes at idle with no Explorer windows open. Drops to ~0%? It was transient — monitor whether it recurs.
3. If CPU climbs again with no windows open, open one Explorer window and note exactly when spikes happen: on right-click, on opening a specific folder, or constantly.
4. Right-click spikes point to shell extensions (Fix 2); specific-folder spikes point to thumbnails/contents (Fix 3); constant spikes point to Quick Access or cloud overlays (Fix 4).
5. Test in a second user account or Safe Mode — if Explorer is calm there, the cause is per-user (extensions, Quick Access pins) rather than system-wide.

### Fix 2: Disable misbehaving shell extensions

The highest-yield fix for right-click and interaction-triggered spikes.

1. Download **ShellExView** from NirSoft (free, portable) and run it as Administrator.
2. Go to **Options** > **Filter by Extension Type** > **Context Menu**, then sort by **Company** — select all non-Microsoft entries.
3. Right-click the selection > **Disable Selected Items**, then restart Explorer via Task Manager.
4. Test right-clicking and general use for 15 minutes. Calm? Re-enable extensions in halves to identify the culprit (binary search).
5. Common offenders: cloud storage overlays, archive tools, "scan with antivirus" handlers, and GPU control-panel entries. Leave the culprit disabled and check the vendor's site for an update — or keep it off permanently if you don't use that context menu.

### Fix 3: Fix thumbnail and preview problems

For spikes tied to specific folders full of media.

1. In the problem folder, switch to **Details** view (View > Details) — if CPU drops instantly, thumbnails are the trigger.
2. Clear the thumbnail cache: open **Disk Cleanup** (`cleanmgr`), select the drive, check **Thumbnails**, and clean. Or run `del /f /s /q %LocalAppData%\Microsoft\Windows\Explorer\thumbcache_*.db` from a prompt, then restart Explorer.
3. Turn off the preview pane for testing: in Explorer, **View** > **Show** > uncheck **Preview pane** — a malformed file's preview handler is a classic CPU burner.
4. Find the poison file: sort the folder by type/date and move recently added media files out temporarily; reintroduce in batches until the spike returns.
5. For folders with thousands of images/videos, split them into subfolders — Explorer's thumbnail pipeline was never designed for 10,000-file flat folders.

### Fix 4: Clean up Quick Access and cloud overlays

Stops the shell from chasing unreachable locations.

1. In Explorer, right-click **Quick Access** items pointing to network drives, old USB sticks, or deleted folders > **Unpin from Quick access**.
2. Go to **Folder Options** (View > Options): set **"Open File Explorer to"** to **This PC** instead of Quick Access/Home, and uncheck **"Show recently used files"** and **"Show frequently used folders"** under Privacy, then **Clear** the history.
3. If you use OneDrive/Dropbox, check their overlay-icon health — reinstalling the sync client fixes broken overlay handlers that spam Explorer with refresh requests.
4. Disconnect stale mapped drives: in **This PC**, right-click any disconnected network drive > **Disconnect**.
5. Restart Explorer and confirm idle CPU is flat — the shell should no longer be retrying dead paths.

### Fix 5: Repair the Explorer installation itself

When the shell is corrupt rather than triggered.

1. Open an elevated **Command Prompt** and run `sfc /scannow` — this repairs protected system files including Explorer components.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to fix the component store SFC draws from.
3. Reset folder views to defaults: **Folder Options** > **View** tab > **Reset Folders** — corrupt saved views can cause per-folder CPU loops.
4. Check for Windows updates at **Settings** > **Windows Update** — Microsoft has shipped several Explorer CPU fixes via cumulative updates; the [Update Catalog](https://www.catalog.update.microsoft.com/) lists them if you need a specific KB.
5. As a deeper reset, create a fresh user profile and migrate — per-user shell corruption that survives SFC usually lives in the profile's registry hive.

### Fix 6: Reduce Explorer's workload on modest hardware

Make the shell lighter if your laptop is older or low-spec.

1. **Folder Options** > **View** > check **"Always show icons, never thumbnails"** for a global thumbnail off-switch (reversible anytime).
2. Uncheck **"Display file icon on thumbnails"** and **"Show preview handlers in preview pane"** if you don't use them.
3. In **Settings** > **Personalization** > **Taskbar**, turn off **Widgets** and **Search highlights** — these are Explorer-hosted processes that add background CPU.
4. Disable **transparency effects** (Settings > Personalization > Colors) — DWM compositing cost drops, which helps on integrated graphics.
5. Consider **Details** view as your default for large folders: **Folder Options** > **View** > **Apply to Folders** after setting one folder the way you like. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents these folder options officially.

## Closing

File Explorer high CPU is a detective problem: the process is the whole shell, so the trigger could be an extension, a thumbnail, or a dead network path. Restart to confirm the pattern, kill the toxic shell extensions, clear the thumbnail pipeline, and unpin the dead locations — one of those four resolves the vast majority of cases.
