---
title: "File Explorer Slow After a Windows 11 Update? Fix It"
slug: how-to-fix-file-explorer-slow-after-windows-11-update
date: 2026-09-30
categories: ["performance"]
tags: ["file explorer slow", "windows 11 update", "explorer lag", "quick access", "fix"]
description: "File Explorer turned sluggish right after a Windows 11 update? Fix slow folder opening, green progress bars, and laggy navigation step by step."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-slow-after-windows-11-update.webp"
faqs:
  - q: "Why is File Explorer slow after updating Windows 11?"
    a: "Updates can reset Explorer settings, re-enable cloud-file on-demand fetching, corrupt the thumbnail cache, break third-party shell extensions, or leave the search indexer rebuilding — any of which makes folders open slowly. The green progress bar crawling across the address bar is the classic symptom of Explorer waiting on something: usually network locations, cloud files, or a damaged cache."
  - q: "Will clearing File Explorer history speed it up?"
    a: "Sometimes, modestly. Clearing history empties the Quick Access recent-files list, which helps if that list references dead network paths or removed drives that Explorer tries to resolve on every Home-folder open. It will not fix slowdowns caused by shell extensions, thumbnail cache corruption, or OneDrive on-demand fetching — those need their own fixes."
  - q: "Does the green loading bar mean my drive is failing?"
    a: "Rarely. The crawling green bar almost always means Explorer is waiting on a network or cloud location to respond, not a dying drive. If the bar appears even in plain local folders like Documents with no network paths involved, then suspect thumbnail cache corruption or a misbehaving shell extension rather than hardware."
  - q: "Can I roll back the update that slowed File Explorer?"
    a: "Within ten days of a feature update you can roll back via Settings > System > Recovery > Go back, which restores the previous build. For monthly cumulative updates, you can uninstall the specific update from Settings > Windows Update > Update history > Uninstall updates. But first try the targeted fixes — most post-update Explorer slowness is repairable without rolling back."
---

It worked fine yesterday. Then Windows 11 installed an update overnight, and now every folder takes seconds to open, the green progress bar crawls across the address bar, and right-clicking a file feels like wading through mud. Post-update File Explorer slowdowns are frustratingly common — but they're also very fixable.

Updates disturb Explorer in specific ways: they reset folder settings, re-enable cloud on-demand features, invalidate the thumbnail cache, and occasionally break third-party shell extensions. We'll fix each in turn. If right-click menus specifically are the slow part, also see our [right-click menu fix](/articles/how-to-fix-right-click-menu-slow-windows-11-on-laptop/).

## Why this happens

- **Thumbnail cache invalidated**: The update wiped or corrupted the thumbnail database, so Explorer regenerates every thumbnail on demand.
- **Quick Access pointing at dead paths**: Update-changed drive letters or removed network shares leave Quick Access resolving ghosts.
- **OneDrive on-demand re-enabled**: Files-on-Demand settings can reset, making Explorer fetch cloud files before showing folders.
- **Broken third-party shell extensions**: Extensions written for the old build misbehave under the new one, stalling every folder render.
- **Search indexer rebuilding**: Post-update, the indexer re-crawls everything, competing with Explorer for disk I/O.
- **Folder optimization reset**: The "Optimize this folder for" template (General items vs. Pictures) can reset, applying the wrong view to large folders.
- **Corrupt update components**: A partially applied update leaves Explorer's own files in a mixed state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart Explorer and clear its current state

The fastest possible win — do this before anything else.

1. Press `Ctrl + Shift + Esc` to open Task Manager.
2. Find **Windows Explorer** under Processes, right-click it, and choose **Restart**. Your taskbar will blink — that's normal.
3. Test folder opening immediately. If it's fast now but slows again later, a shell extension or background process is the real cause — keep going.
4. Also clear File Explorer history: open **Folder Options** (search it in Start), on the **General** tab click **Clear** next to "Clear File Explorer history," then OK.
5. In Folder Options, consider changing **Open File Explorer to:** from **Home** to **This PC** — the Home view with Quick Access is the slowest view Explorer has, especially right after an update scrambled its cached paths.

### Fix 2: Rebuild the thumbnail cache

When every image/video folder crawls, the thumbnail database is the suspect.

1. Open **Settings** > **System** > **Storage** > **Temporary files**.
2. Check **Thumbnails** (uncheck everything else unless you want a broader cleanup), then click **Remove files**.
3. Alternatively, run **Disk Cleanup** (`cleanmgr`), select your drive, check **Thumbnails**, and OK.
4. Open a photo-heavy folder and let it regenerate thumbnails once — the first pass is slow, subsequent opens are instant.
5. To reduce future pain: in **Folder Options** > **View**, you can check **Always show icons, never thumbnails** as a test — if folders fly with thumbnails off, the cache was definitely the bottleneck. Turn thumbnails back on after the rebuild unless you prefer the speed.
6. Keep the [Windows 11 download](https://www.microsoft.com/en-us/software-download/windows11) media handy only if deeper repair becomes necessary — thumbnails rarely need it.

### Fix 3: Fix OneDrive Files On-Demand behavior

Cloud placeholders are the number-one cause of the crawling green bar.

1. Click the OneDrive cloud icon in the system tray > gear > **Settings** > **Sync and backup** > **Advanced settings**.
2. If **Download all files** got enabled by the update, switch back to **Free up disk space** (Files On-Demand) — or vice versa: for folders you open constantly, right-click them in Explorer and choose **Always keep on this device**.
3. The green bar appears when Explorer waits for cloud files to download before rendering — "Always keep on this device" on your working folders eliminates the wait.
4. Pause OneDrive sync entirely for 10 minutes as a test: if Explorer is instantly fast, you've confirmed the culprit.
5. In **Folder Options** > **View**, uncheck **Show sync provider notifications** — this stops Explorer querying OneDrive status per file, which speeds rendering in cloud folders.

### Fix 4: Disable misbehaving shell extensions

Third-party context-menu and icon-overlay handlers stall every folder.

1. Download **ShellExView** (NirSoft, free) — run it as administrator.
2. Sort by **Type** and look at **Context Menu** and **Icon Overlay** handlers from non-Microsoft companies.
3. Select third-party context-menu extensions added around the update (cloud storage, archivers, antivirus) and disable them (red button), a few at a time.
4. Restart Explorer after each batch (Task Manager > Windows Explorer > Restart) and test.
5. When speed returns, you've found the offender — check that vendor's site for an updated version compatible with your Windows build, then re-enable.
6. Pay special attention to icon-overlay handlers: cloud apps each register overlays, and Windows only supports 15 — overflow causes weird slowdowns. Disable overlays for services you barely use.

### Fix 5: Set correct folder optimization templates

A Pictures-optimized template on a folder of 10,000 mixed files is slow.

1. Right-click the slow folder > **Properties** > **Customize** tab.
2. Check what **Optimize this folder for:** is set to. For generic large folders, **General items** is fastest; use **Pictures** or **Videos** only where accurate.
3. Check **Also apply this template to all subfolders** if the whole tree is the same type, then OK.
4. For the global default: in **Folder Options** > **View**, click **Apply to Folders** while viewing a fast, correctly configured folder — this pushes its view settings as the default for that template type.
5. Updates sometimes reset these to the slowest options; re-applying takes a minute and the difference in big folders is dramatic.

### Fix 6: Address the post-update indexer storm

The search indexer rebuilds after updates and fights Explorer for disk.

1. Open **Settings** > **Privacy & security** > **Searching Windows** — if indexing is perpetually "in progress," it's competing with you.
2. Give it one overnight plugged-in session to finish — don't fight it, out-wait it.
3. If it never finishes, rebuild: **Advanced indexing options** > **Advanced** > **Rebuild**.
4. Reduce indexed scope (**Modify**) — exclude folders Explorer opens constantly but you never search (build outputs, temp folders).
5. Our [Windows Search repair guide](/articles/how-to-fix-windows-search-not-working-on-windows-11/) covers the deeper indexer fixes if search itself is also broken.

### Fix 7: Repair the update itself

When Explorer's own files are in a mixed state from a bad update.

1. Open **Settings** > **Windows Update** and install anything pending — Microsoft frequently ships follow-up fixes for Explorer regressions within days.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an elevated terminal to repair system files including Explorer's.
3. If a specific cumulative update caused it and no fix has shipped, uninstall it: **Settings** > **Windows Update** > **Update history** > **Uninstall updates**, select the suspect KB, uninstall, reboot, and pause updates for a week (**Pause updates** option) while Microsoft fixes it. The [Update Catalog](https://www.catalog.update.microsoft.com/) lets you research the specific KB first.
4. For feature-update regressions within 10 days: **Settings** > **System** > **Recovery** > **Go back**.
5. As a final measure, an in-place upgrade repair install refreshes all Explorer components while keeping your files and apps.

## Closing

Post-update File Explorer slowness is almost always one of a handful of things: a trashed thumbnail cache, cloud files being fetched on demand, a broken shell extension, or the indexer rebuilding. Work through them in order and you'll usually have snappy folders back within half an hour — no rollback required.
