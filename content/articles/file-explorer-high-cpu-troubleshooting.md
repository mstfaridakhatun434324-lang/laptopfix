---
title: "File Explorer High CPU? Fix It on Windows 10 and 11"
slug: file-explorer-high-cpu-troubleshooting
date: 2026-10-02
categories: ["performance"]
tags: ["file explorer", "high cpu", "explorer.exe", "windows shell"]
description: "File Explorer (explorer.exe) using high CPU? Fix the shell extensions, thumbnails, and cloud overlays behind Explorer CPU spikes."
thumbnail: "/images/thumbs/file-explorer-high-cpu-troubleshooting.webp"
faqs:
  - q: "Why does File Explorer use so much CPU?"
    a: "Explorer.exe hosts the entire Windows shell — the taskbar, desktop, and every file window — plus all third-party shell extensions (context menu items, icon overlays, preview handlers). High CPU almost always comes from a misbehaving extension: cloud storage overlays (OneDrive, Dropbox), buggy context-menu entries, thumbnail generation on huge media folders, or a corrupted Quick Access cache. The shell itself is rarely the problem."
  - q: "Is it safe to restart File Explorer?"
    a: "Yes — restarting explorer.exe is completely safe and is the standard first-aid for shell weirdness. Your apps keep running; only the taskbar, desktop icons, and file windows briefly disappear and reload. In Task Manager, right-click Windows Explorer and choose Restart. Unsaved work in other apps is unaffected."
  - q: "Can I end the explorer.exe process?"
    a: "You can, but use Restart instead of End task — Restart cleanly reloads the shell, while End task leaves you with no taskbar until you manually relaunch it via Task Manager > File > Run new task > explorer.exe. Either way your files and apps are safe, but Restart is the smoother path."
  - q: "Why does Explorer CPU spike when I open certain folders?"
    a: "Folder-specific spikes point to thumbnail generation or preview handlers struggling with that folder's contents — huge video files, corrupt images, or thousands of files. Cloud-synced folders add overlay-icon processing for every file. If only one folder triggers it, the fix is disabling thumbnails or previews for that location, or fixing the specific corrupt file."
---

`explorer.exe` at 25% CPU — and all you did was open a folder. File Explorer is the Windows shell itself: the taskbar, the desktop, every file window. When it's burning CPU, the cause is almost never Explorer proper — it's the ecosystem living inside it: third-party context menu items, cloud storage icon overlays, thumbnail generators, and preview handlers. Each one runs inside Explorer's process, so their sins show up under its name. The fix is evicting the bad tenants.

Start with the instant test: restart Explorer from Task Manager and see if the CPU was a transient glitch. For the file-manager slowness companion, see [fixing slow File Explorer](/articles/how-to-fix-file-explorer-slow-windows-11-step-by-step/); for system-wide issues, [speeding up Windows 11](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Buggy shell extensions**: Third-party context-menu items and overlays running inside Explorer's process.
- **Cloud storage icon overlays**: OneDrive, Dropbox, and Google Drive computing sync status icons for thousands of files.
- **Thumbnail generation overload**: Folders full of large videos or corrupt images that the thumbnailer chokes on.
- **Corrupt Quick Access / Recent cache**: Damaged jump-list data making Explorer loop on launch.
- **Preview pane handlers**: Buggy preview handlers for PDFs, videos, or CAD files burning CPU per file.
- **Network folder timeouts**: Explorer waiting on unreachable network locations, spinning while it waits.
- **Malware injecting into the shell**: Malicious shell extensions are a classic persistence technique.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart Explorer and observe the pattern

Separate transient glitches from persistent problems.

1. Open **Task Manager**, find **Windows Explorer** under Processes, right-click > **Restart** — taskbar and windows flicker and reload.
2. Watch CPU for 10 minutes of normal use — if it stays low, it was a transient stuck state.
3. Note the trigger pattern: spikes when right-clicking (context menu extensions), when opening specific folders (thumbnails/previews), or constant (overlay icons or corrupt cache).
4. Open a plain folder like `C:\Windows\Temp` (few files, no cloud sync) — high CPU even here means a systemic shell problem, not a folder problem.
5. The pattern you observe directs every fix below — don't skip the observation.

### Fix 2: Disable thumbnail previews as a test

The quickest way to rule in or out the thumbnailer.

1. Open **File Explorer** > **View** > **Options** > **Change folder and search options** > **View** tab.
2. Check **Always show icons, never thumbnails** and click **OK**.
3. Browse the folders that previously spiked CPU — if the spikes vanish, thumbnail generation was the cause.
4. For a targeted approach instead: clear the thumbnail cache via Disk Cleanup (`cleanmgr.exe` > **Thumbnails**), then re-enable thumbnails and see if the rebuilt cache behaves.
5. If one specific folder still spikes, a corrupt media file inside it is likely — move files out in batches to isolate it.

### Fix 3: Audit shell extensions with ShellExView

Find the misbehaving third-party extension.

1. Download **ShellExView** (free, from NirSoft) and run it — it lists every shell extension with its publisher.
2. Sort by **Type** and focus on **Context Menu** extensions from non-Microsoft publishers — these are the top offenders.
3. Select suspicious third-party entries (especially from uninstalled software leftovers), right-click > **Disable Selected Items**.
4. Restart Explorer (Task Manager > **Restart**) and test — right-click in folders and watch CPU.
5. Re-enable extensions one at a time if you need them — or leave the unused ones disabled permanently. Fewer extensions, calmer shell.

### Fix 4: Tame cloud storage overlays

Icon overlays are a notorious CPU drain in big synced folders.

1. If you use OneDrive/Dropbox/Google Drive, check whether spikes correlate with synced folders — overlay icons are computed per file.
2. Reduce synced scope with selective sync (see our [OneDrive CPU guide](/articles/onedrive-high-cpu-usage-troubleshooting/)) — fewer synced files means fewer overlays.
3. Pause cloud sync temporarily as a test — if Explorer CPU drops, overlays are confirmed as the amplifier.
4. In the cloud app's settings, disable **Files On-Demand** icon states you don't need, or move high-file-count folders out of sync.
5. This doesn't mean abandoning cloud sync — it means syncing less, which helps both the sync app and Explorer.

### Fix 5: Clear Quick Access and jump-list caches

Corrupt shell caches cause launch-time CPU storms.

1. **File Explorer** > **View** > **Options** > under **Privacy**, click **Clear** next to "Clear File Explorer history."
2. Uncheck **Show recently used files** and **Show frequently used folders in Quick access** temporarily — if CPU calms, the cache was corrupt.
3. For a deeper clear, delete `%appdata%\Microsoft\Windows\Recent\AutomaticDestinations\*` (close Explorer windows first).
4. Re-enable the Quick Access options after a day of calm behavior — fresh caches rebuild cleanly.
5. If the corruption returns, a pinned item pointing at a dead network location is usually the cause — unpin network folders from Quick Access.

### Fix 6: Disable the preview pane and details pane

Buggy preview handlers burn CPU per selected file.

1. In File Explorer, press **Alt+P** to toggle the **Preview pane** off, and check **View** > **Show** > **Details pane** is off too.
2. Browse previously problematic folders — if CPU is now calm, a preview handler (PDF, video, image) was the culprit.
3. Identify it: re-enable the preview pane and select files by type until CPU spikes — the file type that triggers it names the handler.
4. Update or reinstall the application that provides that preview handler (PDF readers and codec packs are frequent offenders).
5. Leave the panes off if you don't use them — they're optional UI, not essential function. Microsoft documents Explorer options on [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Scan for shell-injecting malware

When the shell misbehaves with no benign explanation.

1. Run a **Full scan** in **Windows Security** — malware persistence via shell extensions is common.
2. In ShellExView, look for extensions with blank publishers or suspicious paths — disable anything you don't recognize.
3. Check **Autoruns** (Sysinternals) > **Explorer** tab for shell hooks that shouldn't be there.
4. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` — corrupt shell components mimic extension problems.
5. If Explorer is still wild after all this, test in a new user profile — a corrupt profile shell configuration is the remaining suspect.

## Closing

File Explorer high CPU is a tenant problem, not a landlord problem — the shell is fine; something living inside it isn't. Restart to clear the transient, disable thumbnails to test the thumbnailer, audit extensions with ShellExView, tame the cloud overlays, and the shell goes back to sipping CPU instead of gulping it.
