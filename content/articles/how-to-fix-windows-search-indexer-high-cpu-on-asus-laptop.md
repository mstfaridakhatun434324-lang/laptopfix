---
title: "Windows Search Indexer High CPU on ASUS Laptops: Fix It"
slug: how-to-fix-windows-search-indexer-high-cpu-on-asus-laptop
date: 2026-09-20
categories: ["performance"]
tags: ["search indexer", "high cpu", "asus laptop", "searchindexer.exe", "windows 11"]
description: "SearchIndexer.exe pinning CPU on your ASUS laptop? Fix the runaway Windows Search indexer with rebuilds, exclusions, and Armoury Crate checks."
thumbnail: "/images/thumbs/how-to-fix-windows-search-indexer-high-cpu-on-asus-laptop.webp"
faqs:
  - q: "Why is the Windows Search indexer using so much CPU on my ASUS laptop?"
    a: "The indexer (SearchIndexer.exe) spikes when it's building or rebuilding its database — normal after Windows updates, new software installs, or adding large folders. On ASUS laptops specifically, Armoury Crate's constant profile and game-library scanning creates high-churn folders that keep the indexer perpetually busy, and ASUS's preinstalled software adds indexed locations a clean install wouldn't have. Persistent high CPU beyond a few days means it's stuck, not just busy."
  - q: "How long should the indexer run at high CPU?"
    a: "An initial index on a typical laptop takes 2–6 hours of plugged-in idle time; a post-update re-index usually finishes within a day. If SearchIndexer.exe has been hot for several days, check Settings > Privacy & security > Searching Windows for the indexer status — a count that never advances means it's wedged on a corrupted database or a folder it can't process, and you should rebuild the index rather than keep waiting."
  - q: "Does ASUS Armoury Crate affect search indexing?"
    a: "Indirectly, yes. Armoury Crate monitors game libraries, creates and updates game profiles, shader caches, and configuration files frequently — all in folders the indexer crawls by default. This constant churn means the indexer never considers its work done. Excluding Armoury Crate's data folders, game libraries, and shader cache locations from indexing (via Indexing Options > Modify) noticeably calms the indexer on ASUS gaming laptops."
  - q: "Will excluding folders from the index break game search?"
    a: "No. Start menu search for installed games uses the Start menu index entries, not the file-content index of your game folders — excluding D:\\Games or your Steam library doesn't remove games from Start search results. What you lose is full-text search inside game files, which nobody needs. Excluding game libraries is one of the highest-value, lowest-risk indexing tweaks on a gaming laptop."
---

**SearchIndexer.exe** holding 15–30% CPU for days on an ASUS laptop is the Windows Search indexer stuck in a loop it can't finish. Some indexing load is normal — after updates, after installing software, the indexer has legitimate catching up to do. But when it never settles, the cause is usually one of three things: a corrupted index database, folders that change faster than the indexer can process them, or ASUS-specific software creating exactly that kind of churn.

ASUS gaming laptops (ROG, TUF) are a perfect storm for indexer problems: Armoury Crate constantly updates game profiles, game libraries churn with updates and shader caches, and the preinstalled software stack adds indexed locations. This guide fixes the indexer properly — diagnose, exclude, rebuild — with the ASUS-specific folders called out. For the broader indexing controls, see [disabling search indexing on 24H2](/articles/how-to-disable-windows-search-indexing-in-windows-11-24h2/); for the search UI process, see [SearchApp.exe high CPU](/articles/how-to-fix-searchapp-exe-high-cpu-after-windows-11-update/).

## Why this happens

- **Corrupted index database**: The most common cause of never-ending indexing — the indexer reprocesses without progress.
- **Armoury Crate churn**: Constant game-profile and config updates keep indexed folders in flux.
- **Game library churn**: Steam/Epic updates, shader caches, and mods change thousands of files regularly.
- **Post-update re-index**: 24H2 and feature updates trigger full rebuilds.
- **Overly broad indexed locations**: Entire drives indexed instead of just libraries.
- **ASUS preinstall additions**: Extra ASUS utilities and trial software add indexed paths.
- **Outlook/OneDrive weight**: Large indexed mailboxes and cloud folders multiply the work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check indexer status and confirm it's stuck

Distinguish "busy" from "broken."

1. Open **Task Manager** > sort by CPU — confirm **Microsoft Windows Search Indexer** is the consumer.
2. Go to **Settings** > **Privacy & security** > **Searching Windows** — read the **Indexer status**. "Indexing complete" + high CPU = something else is wrong; "Indexing in progress" with a number is normal-ish.
3. Open **Indexing Options** (search in Start) — note the item count. Check again in an hour: climbing = working; frozen = stuck.
4. If the update was within 72 hours and the count is climbing, let it finish — skip to Fix 3's exclusions to speed it up, but don't nuke anything yet.
5. Frozen count for 24+ hours = stuck. Proceed to rebuild (Fix 4).

### Fix 2: Exclude ASUS and gaming high-churn folders

The highest-value tweak for ASUS machines.

1. Open **Indexing Options** > **Modify**.
2. Uncheck game libraries: Steam (`C:\Program Files (x86)\Steam` or your library drive), Epic Games, EA, Ubisoft Connect folders.
3. Uncheck Armoury Crate data: `%ProgramData%\ASUS` and `%LocalAppData%\ASUS` — constant config churn lives here.
4. Uncheck shader caches and temp-heavy locations: `%LocalAppData%\Temp`, game shader cache folders, video editing scratch disks.
5. Keep: Start Menu, your Documents/Pictures/Music libraries, Desktop. Click OK and give the indexer an hour to shed the excluded content — CPU should drop noticeably.

### Fix 3: Switch Enhanced search to Classic

Cut the indexer's territory down to size.

1. **Settings** > **Privacy & security** > **Searching Windows** > **Find my files** > select **Classic**.
2. Classic indexes libraries and Start menu only — Enhanced crawls the whole PC including every game and tool install.
3. On a gaming laptop with terabytes of games, this is transformative for indexer load.
4. File Explorer searches outside libraries become live (slower) searches — fine for occasional use.
5. Combine with Fix 2's exclusions for the calmest possible indexer. Microsoft's documentation: [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 4: Rebuild the corrupted index

The actual fix for the stuck cases.

1. **Indexing Options** > **Advanced** > **Rebuild** (admin approval required).
2. The rebuild takes several hours — run it overnight, plugged in, sleep disabled temporarily.
3. Monitor in the morning via **Settings** > **Privacy & security** > **Searching Windows** — status should read "Indexing complete."
4. If the rebuild stalls at the same count repeatedly, a specific file or folder is unprocessable — note where it stalls and exclude that location (Fix 2), then rebuild again.
5. One clean rebuild fixes the overwhelming majority of never-ending indexer cases.

### Fix 5: Calm Armoury Crate's background activity

Reduce the churn at its source.

1. Open **Armoury Crate** > settings — disable automatic game library scanning intervals you don't need, and turn off features that constantly write profiles (like per-game macro syncing you never use).
2. In Armoury Crate's **Operating Mode**, avoid leaving it on **Turbo/Manual** with aggressive fan curves 24/7 — not an indexer issue directly, but the thermal/noise complaints often arrive together.
3. Update Armoury Crate itself — ASUS regularly fixes background-activity bugs; check for updates within the app or via MyASUS.
4. If you don't use Armoury Crate's features, consider uninstalling it and using G-Helper (a lightweight open-source alternative) — less background churn overall.
5. Keep MyASUS for driver/BIOS updates even if you drop Armoury Crate.

### Fix 6: Check for the Outlook/OneDrive multiplier

Heavy indexed sources hiding in plain sight.

1. **Indexing Options** > **Modify** — if **Microsoft Outlook** is checked and you have a multi-GB mailbox, that's a major indexer load. Uncheck it if you search email in the browser instead.
2. OneDrive: files-on-demand placeholders are cheap to index, but a fully-synced multi-GB OneDrive isn't — consider which folders truly need offline sync.
3. **Settings** > **Privacy & security** > **Searching Windows** — review **Cloud content search** toggles; disable work/school account search if unused.
4. Each disabled heavy source is a permanent reduction in indexer workload.
5. Rebuild the index (Fix 4) after major source changes so the database reflects the new scope.

### Fix 7: Disable the indexer service (HDD or last resort)

When taming isn't enough.

1. **Services** (`services.msc`) > **Windows Search** > Stop, set **Startup type** to **Disabled**. Or elevated Terminal: `sc stop WSearch` + `sc config WSearch start=disabled`.
2. Start menu app search keeps working; File Explorer file search becomes slow live search.
3. This is most justified on ASUS laptops still running HDDs (some budget Vivobooks) — the indexer on a spinning drive is brutal.
4. On SSDs, prefer Fixes 2–4 — a tamed indexer on an SSD costs almost nothing and keeps instant search.
5. Re-enable anytime: set to **Automatic (Delayed Start)**, start it, rebuild the index.

## Closing

SearchIndexer.exe high CPU on an ASUS laptop is usually the indexer drowning in gaming-related churn or stuck on a corrupted database. Exclude the game libraries and Armoury Crate data folders, drop to Classic search, rebuild the index once — and the indexer goes back to being the quiet background librarian it's supposed to be instead of the loudest process on your machine.
