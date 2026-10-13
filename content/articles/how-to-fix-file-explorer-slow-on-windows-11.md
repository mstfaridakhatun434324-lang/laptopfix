---
title: "How to Fix Slow File Explorer on Windows 11"
slug: "how-to-fix-file-explorer-slow-on-windows-11"
date: "2026-09-25"
categories: ["performance"]
tags: ["file explorer slow", "windows 11", "explorer lag", "quick access"]
description: "Windows 11 File Explorer slow to open folders or freezing on right-click? These targeted fixes restore instant navigation."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-slow-on-windows-11.webp"
faqs:
  - q: "Why is Windows 11 File Explorer slower than Windows 10?"
    a: "The Windows 11 Explorer is a rewritten XAML-based app rather than the classic Win32 one, and early versions had genuine performance regressions. Microsoft has improved it substantially through cumulative updates, so an unpatched system feels much worse than a current one. Beyond that, the same classic culprits apply: Quick Access bloat, dead network paths, and third-party shell extensions."
  - q: "Does the new tabbed Explorer use more memory?"
    a: "Each tab is relatively lightweight, but tabs encourage keeping many folders open, and each open folder holds its view state and thumbnails. Ten tabs of photo folders consume noticeably more memory than one. If Explorer's memory grows without bound across days, close tabs you are not using; the Home page restores your frequent folders anyway."
  - q: "Why does right-click take seconds in Windows 11 Explorer?"
    a: "The new condensed context menu queries shell extensions to decide what to show, and a slow third-party extension delays the whole menu. Shift+F10 or Show more options reveals the classic menu, which can be faster. The permanent fix is identifying the slow extension with ShellExView and updating or removing it."
  - q: "Should I replace File Explorer with a third-party alternative?"
    a: "Third-party file managers can be faster for power users, but they do not fix the underlying issue and add their own learning curve. The built-in Explorer, once its Quick Access is cleaned and bad extensions removed, is fast enough for nearly everyone. Try the fixes here first; switching apps is a workaround, not a repair."
---

Windows 11 gave File Explorer a modern makeover: tabs, a new command bar, and the Home page. It also gave it, at least in early releases, a reputation for sluggishness that the old Windows 10 Explorer never had. Folders that hesitate, right-clicks that hang, and the occasional full freeze made the most basic PC task feel unreliable.

Microsoft has steadily improved Explorer through cumulative updates, so the first thing to know is that an unpatched Windows 11 genuinely has a slower Explorer than a current one. But updates alone do not fix the classic causes that carry over from Windows 10: a bloated Quick Access history, pinned folders on dead network shares, and third-party shell extensions dragging every window down.

This guide covers the Windows 11-specific angles alongside the proven classics: updating first, cleaning Home and Quick Access, handling the new context menu, and hunting bad extensions.

## Why this happens

- **Unpatched early Windows 11 builds:** The original 21H2 Explorer had real performance bugs fixed in later cumulative updates.
- **Bloated Home and Quick Access:** Frequent folders and recent files, including dead network paths, slow every launch.
- **New context menu querying slow extensions:** The condensed menu still loads third-party handlers, and slow ones delay it.
- **Too many open tabs:** Each tab holds view state and thumbnails; dozens of tabs bloat the process.
- **Corrupted thumbnail cache:** Damaged previews stall media folders with the crawling progress bar.
- **OneDrive sync status churn:** Constant sync-state changes in cloud folders force view refreshes.
- **Failing drive underneath:** No Explorer tweak overcomes a disk that retries every read.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install all Windows updates first

Explorer performance improved measurably across Windows 11 cumulative updates. An unpatched system is fighting fixed bugs.

1. Open Settings with Win+I and go to Windows Update.
2. Click Check for updates and install everything.
3. Pay special attention to cumulative updates mentioning File Explorer.
4. Restart when prompted.
5. Test folder navigation before changing any settings.

### Fix 2: Clean up Home, Quick Access, and pins

The Home page aggregates frequent folders and recent files. Clearing it removes the dead weight.

1. Open Explorer and go to Home.
2. Right-click dead or unwanted entries under Quick access and choose Remove from Quick access.
3. Open Folder Options via the three-dot menu, then Options.
4. Under Privacy, click Clear to wipe the history.
5. Uncheck the automatic population options if you prefer a permanently lean Home.

### Fix 3: Fix the slow right-click menu

If right-clicks hang, test whether the classic menu is faster, then find the slow extension.

1. Right-click a file and note the delay.
2. Press Shift+F10 on the same file to open the classic menu and compare speed.
3. If the classic menu is fast, a new-menu extension is the problem.
4. Download ShellExView and disable non-Microsoft context menu handlers in batches.
5. Restart Explorer from Task Manager after each batch to isolate the offender.

### Fix 4: Close unused tabs and reset views

Tab sprawl bloats the Explorer process over long sessions. A periodic reset keeps it lean.

1. Close tabs for folders you are not actively using.
2. In Folder Options, View tab, click Reset Folders.
3. This clears corrupted per-folder view settings.
4. Restart the Explorer process from Task Manager.
5. Observe whether navigation feels snappier.

### Fix 5: Rebuild the thumbnail cache

Media folders with broken thumbnails stall on the green progress bar. A rebuild fixes it in minutes.

1. Press Win+R, type cleanmgr, and press Enter.
2. Select C and check Thumbnails.
3. Click OK to clear the cache.
4. Open one photo folder and let it regenerate once.
5. Microsoft documents Explorer behavior in its [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Check OneDrive sync status

Folders mid-sync refresh constantly. Pausing sync during heavy file work stops the churn.

1. Click the OneDrive cloud icon in the system tray.
2. Check whether large sync operations are in progress.
3. Pause syncing for two hours during intensive file work.
4. Consider Files On-Demand so huge folders do not all download.
5. Resume sync when the work is done.

### Fix 7: Turn off Home page recommendations

The Home page shows recommended files pulled from your Microsoft account activity. Disabling the feed lightens every Explorer launch.

1. Open Folder Options from Explorer's three-dot menu.
2. On the General tab, uncheck Show recommended section under Privacy.
3. Click Clear to wipe the existing history.
4. Click Apply and OK.
5. New windows now open to a leaner Home page.

### Fix 8: Test with a new local user profile

If Explorer is slow in your profile but fine elsewhere, your profile's Explorer configuration is corrupt. A new profile confirms it in minutes.

1. Open Settings, Accounts, Other users.
2. Add a new local account without a Microsoft login.
3. Sign into the new account and open Explorer.
4. If it is fast there, migrate your files to the new profile.
5. This is faster than hunting the exact corrupted setting.

### Fix 9: Turn off Home page recommendations

The Home page shows recommended files pulled from your Microsoft account activity. Disabling the feed lightens every Explorer launch.

1. Open Folder Options from Explorer's three-dot menu.
2. On the General tab, uncheck Show recommended section under Privacy.
3. Click Clear to wipe the existing history.
4. Click Apply and OK.
5. New windows now open to a leaner Home page.

### Fix 10: Test with a new local user profile

If Explorer is slow in your profile but fine elsewhere, your profile's Explorer configuration is corrupt. A new profile confirms it in minutes.

1. Open Settings, Accounts, Other users.
2. Add a new local account without a Microsoft login.
3. Sign into the new account and open Explorer.
4. If it is fast there, migrate your files to the new profile.
5. This is faster than hunting the exact corrupted setting.

## Closing

Windows 11's Explorer rewards the same maintenance the old one did: stay updated, keep Home lean, and evict bad shell extensions. The rewrite's early stumbles are largely patched, so a current system with a clean Quick Access feels as snappy as Windows 10 ever did. If Explorer lags and the entire machine lags with it, the problem is systemic rather than Explorer-specific, and our [100 percent disk guide](/articles/disk-active-time-100-percent-troubleshooting/) is the right next step. A fresh profile that behaves perfectly proves the old profile's Explorer configuration was corrupt. For deeper diagnostics, see [this File Explorer fix guide](/articles/how-do-i-fix-file-explorer-slow-windows-11/). A fresh profile that behaves perfectly proves the old profile's Explorer configuration was corrupt. For deeper diagnostics, see [this File Explorer fix guide](/articles/how-do-i-fix-file-explorer-slow-windows-11/). Test with a couple of different folder types, since thumbnail and network issues affect each view differently. If only network folders are slow, the problem is the network path, not Explorer itself.
