---
title: "How to Fix File Explorer Slow on an ASUS Laptop"
slug: how-to-fix-file-explorer-slow-on-asus-laptop
date: 2026-09-18
categories: ["performance"]
tags: ["file explorer", "slow", "asus laptop", "windows 11", "explorer freezing"]
description: "File Explorer slow or freezing on your ASUS laptop? Fix sluggish folders, hanging right-clicks, and slow navigation step by step."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-slow-on-asus-laptop.webp"
faqs:
  - q: "Why is File Explorer slow on ASUS laptops?"
    a: "The causes are mostly universal: Quick Access waiting on dead network/USB locations, third-party shell extensions hanging, Windows Search indexing churning, thumbnail generation stalling, and antivirus scanning every file enumeration. ASUS-specific contributors include Armoury Crate and bundled utilities installing context-menu shell extensions, and outdated ASUS storage/chipset drivers slowing file I/O."
  - q: "File Explorer freezes when I right-click — what's wrong?"
    a: "Almost certainly a third-party shell extension (context-menu handler) hanging. When you right-click, Explorer loads every registered handler before showing the menu — one bad handler freezes the whole window. Disabling non-Microsoft shell extensions with ShellExView and re-enabling them in groups identifies the offender, usually a cloud app, archiver, or utility."
  - q: "Does the preview pane slow down File Explorer?"
    a: "It can, especially in folders with large media or documents. The preview pane generates a live preview of the selected file, which means loading handlers and rendering content on every selection change. If navigation feels laggy, toggle the preview pane off (View > Show > Preview pane) as a test — instant improvement implicates a preview handler."
  - q: "Will reinstalling Windows fix slow File Explorer?"
    a: "Usually, but it's overkill as a first step. A reinstall clears shell extensions, corrupt caches, and broken index state — the same things the targeted fixes address individually in minutes. Reinstall only if Explorer is slow in a new user profile, Safe Mode, and after shell-extension cleanup, which indicates deep system corruption."
---

On ASUS laptops, File Explorer slowness wears the same disguises as everywhere else: folders that take seconds to populate, right-clicks that freeze the window, the address bar's green progress bar crawling. The ASUS twist is usually in the shell extensions — Armoury Crate, MyASUS, and bundled utilities love installing context-menu handlers — plus the occasional outdated storage driver. The diagnostic question remains: slow everywhere, in specific folders, or only on right-click?

Each answer points somewhere different: everywhere = shell extensions or system; specific folders = contents or location (network, thumbnails); right-click only = context-menu handlers. For the universal step-by-step see [fixing slow File Explorer](/articles/how-to-fix-file-explorer-slow-step-by-step/); for the CPU-side variant see [File Explorer high CPU troubleshooting](/articles/file-explorer-high-cpu-troubleshooting/).

## Why this happens

- **ASUS utility shell extensions**: Armoury Crate, MyASUS, and bundled tools adding context-menu handlers.
- **Quick Access dead pins**: Pinned locations on disconnected drives stalling every open.
- **Third-party handlers hanging**: Cloud apps, archivers, and utilities freezing right-click.
- **Indexing churn**: Search indexer grinding through open folders.
- **Thumbnail stalls**: Corrupt media blocking thumbnail generation.
- **Network timeouts**: Dead mapped drives delaying navigation.
- **Antivirus per-file scanning**: Real-time checks on every enumeration, worst in huge folders.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset the Explorer starting point

Kill the Quick Access stall.

1. Open Explorer > **...** > **Options** — set **Open File Explorer to:** to **This PC**.
2. Under **Privacy**, click **Clear** (File Explorer history), and temporarily uncheck recent files/frequent folders.
3. Unpin any Quick Access entries showing red X or grayed out — dead network/USB paths.
4. Restart Explorer (Task Manager > **Windows Explorer** > **Restart**) and test folder opens.
5. If speed is restored, the stall was Quick Access waiting on dead locations — re-enable the features you like, minus the dead pins.

### Fix 2: Purge the shell extensions (including ASUS ones)

The highest-yield fix for ASUS machines.

1. Run **ShellExView** (NirSoft, free) — sort by **Company** and look at non-Microsoft entries, including any from ASUS utilities.
2. Disable all non-Microsoft shell extensions, restart Explorer, and test: folder opens, right-clicks, preview pane.
3. If fixed, re-enable in small groups until slowness returns — the last group holds the offender.
4. Common ASUS-adjacent offenders: utility context menus and "send to device" handlers from bundled software. Common general offenders: cloud-storage overlays, archivers, video tools.
5. Leave the offender disabled, or update its parent app — and think twice before installing utilities that inject into Explorer.

### Fix 3: Fix indexing and thumbnails

For slowness tied to specific folders.

1. **Indexing Options** — if the index is rebuilding, wait it out; then **Modify** to exclude churn folders (Downloads, dev folders, game libraries).
2. **Advanced** > **Rebuild** for a corrupt index — takes hours plugged in, but ends chronic slowness afterward.
3. **Disk Cleanup** > check **Thumbnails** — clears the thumbnail cache; first open of media folders regenerates (slow once), then fast.
4. If one file always stalls thumbnails, it's corrupt — move it out and test; delete or repair the file.
5. For giant media folders, use **Details** view instead of icons — no thumbnails, instant render. Toggle the preview pane off as a test too.

### Fix 4: Cut network timeouts

Airplane-mode test tells all.

1. Enable airplane mode (or unplug Ethernet) and test Explorer — sudden speed means network timeouts were the cause.
2. In **This PC**, disconnect mapped drives with red X (right-click > **Disconnect**).
3. Remove shortcuts to dead server/NAS paths from Quick Access and user folders.
4. When mapping drives you need occasionally, uncheck **Reconnect at sign-in** — map on demand instead.
5. VPN users: connect the VPN before browsing office shares, or keep those mappings disconnected when off-network.

### Fix 5: Update ASUS storage and chipset drivers

The I/O layer matters for file browsing.

1. Visit ASUS's support site for your exact model — install the latest **chipset** and **storage/IRST** drivers; these govern how fast Explorer reads the drive.
2. Update the BIOS if the changelog mentions storage, USB, or stability — Explorer stalls on external drives often trace to USB controller firmware.
3. In **Device Manager**, clear any yellow-warning devices — broken drivers cause retry delays that surface as Explorer hangs.
4. For external-drive slowness specifically, test the drive on another PC — a dying external HDD makes Explorer crawl regardless of laptop drivers.
5. Keep Armoury Crate and MyASUS updated (Microsoft Store) — old versions' background services occasionally interfere with shell operations.

### Fix 6: Tune antivirus and Explorer settings

Reduce per-folder overhead.

1. In Windows Security > **Exclusions**, add trusted high-file-count folders you browse constantly (project directories — never Downloads or system paths).
2. **Folder Options** > **View** — uncheck **Show sync provider notifications** (OneDrive/Dropbox status chatter slows rendering).
3. **Folder Options** > **View** > **Reset Folders** — clears corrupt saved views causing per-folder weirdness.
4. **Folder Options** > **General** — set **Open File Explorer to: This PC** (from Fix 1) and uncheck **Show recently used files in Quick access** if still slow.
5. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the official Explorer troubleshooting path as a complement.

### Fix 7: Repair and escalate

When it's system-wide and stubborn.

1. `sfc /scannow` + `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated terminal.
2. Test in a new local user account — fast there means profile corruption; migrate.
3. Test in Safe Mode — fast there means a driver or service; slow there means deep system issues.
4. `chkdsk C: /scan` plus the SSD/HDD maker's health tool — struggling storage slows every enumeration.
5. Final: in-place Windows upgrade (ISO setup, keep files and apps) rebuilds Explorer cleanly.

## Closing

Slow File Explorer on ASUS laptops is usually the shell-extension story with an ASUS cast: utility context menus plus the usual third-party handlers, dead Quick Access pins, or a churning indexer. Disable the handlers, clear the dead pins, fix the index — in that order — and folder browsing goes back to instant. Explorer was fast before everything hooked into it; unhooking is the fix.
