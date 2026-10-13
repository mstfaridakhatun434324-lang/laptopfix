---
title: "Chrome Using Too Much RAM on Your Laptop in Windows 11 24H2? Fix It"
slug: how-to-fix-chrome-using-too-much-ram-laptop-in-windows-11-24h2
date: 2026-10-01
categories: ["performance"]
tags: ["chrome ram", "browser memory", "windows 11 24h2", "memory saver"]
description: "Chrome devouring RAM on your Windows 11 24H2 laptop? Cut its memory footprint with Memory Saver, tab discipline, and extension audits."
thumbnail: "/images/thumbs/how-to-fix-chrome-using-too-much-ram-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why does Chrome use so much RAM compared to other programs?"
    a: "Chrome's architecture isolates each tab, extension, and plugin in its own process for stability and security — one crashing tab can't take down the browser. The cost is memory overhead per process: 20 tabs means 20+ processes plus GPU, network, and extension processes. Modern web apps (Gmail, Docs, Figma, YouTube) are also genuinely heavy, each easily consuming 200–500MB. It's architecture plus the modern web, not a bug."
  - q: "How much RAM should Chrome use with 10 tabs open?"
    a: "Roughly 1–2GB for 10 typical tabs (news, docs, email), more like 2–3GB if they're heavy web apps or video sites. If 10 light tabs consume 4GB+, something's wrong — usually a leaky tab, a bloated extension, or hardware acceleration misbehaving. Use Chrome's own Task Manager (Shift + Esc) to see per-tab usage; the numbers often surprise people, with one bad tab eating more than the other nine combined."
  - q: "Does Chrome's Memory Saver actually work?"
    a: "Yes — it's the single most effective built-in fix. Memory Saver puts inactive tabs to sleep, freeing their RAM (up to 30–40% savings in heavy sessions), and instantly reloads them when you click back. The reload is fast enough that most users never notice. Enable it in Settings > Performance, and add sites you need always-live (music, chat, docs you're actively editing) to the exclusion list."
  - q: "Will switching browsers fix high RAM usage?"
    a: "Partially. All Chromium browsers (Edge, Brave, Opera) share Chrome's process architecture, though Edge's Efficiency mode and Sleeping Tabs are slightly more aggressive by default. Firefox uses a different architecture that's often leaner with many tabs. But the biggest wins come from tab discipline and extension audits regardless of browser — a 50-tab Firefox session with leaky extensions will still eat RAM."
---

Chrome is the most common reason a Windows 11 laptop feels out of memory: a dozen tabs, a handful of extensions, and suddenly 4GB is gone while Task Manager shows a wall of identical `chrome.exe` processes. On 24H2 laptops with 8GB of RAM, Chrome alone can push the system into paging — and paging on any drive feels like the whole laptop is dying.

The good news: Chrome gives you the tools to fix this without giving up the browser. Memory Saver, tab management, extension audits, and a few settings changes typically cut Chrome's footprint by a third or more. This guide walks through all of them, plus how to spot the one bad tab or extension ruining everything. For system-wide memory issues beyond the browser, see [Windows 11 high idle RAM on Lenovo](/articles/how-to-fix-windows-11-using-too-much-ram-idle-on-lenovo-laptop/); for general speed, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Process-per-tab architecture**: Isolation for stability/security means per-process overhead multiplied by tab count.
- **Heavy modern web apps**: Gmail, Notion, Figma, and video sites each consume hundreds of MB.
- **Extension processes**: Every extension runs persistently; bloated ones rival tabs in memory use.
- **Leaky tabs**: Some sites (looking at you, infinite-scroll social feeds) grow unboundedly the longer they're open.
- **Hardware acceleration overhead**: The GPU process can balloon with many video/canvas-heavy tabs.
- **Preloading and prefetch**: Chrome preloads pages it thinks you'll visit, spending RAM speculatively.
- **Zombie processes**: Occasionally closed tabs leave orphaned renderer processes behind.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the offenders in Chrome's Task Manager

Chrome's own task manager beats Windows' for this job.

1. In Chrome, press **Shift + Esc** to open Chrome's Task Manager — it breaks down memory per tab, extension, and sub-process.
2. Click the **Memory footprint** column to sort — the top entries are your targets.
3. Look for: a single tab using 500MB+ (leaky tab), an extension using hundreds of MB (bloated extension), or a huge **GPU Process** (Fix 5).
4. Select an offender and click **End process** as an immediate test — if system RAM drops dramatically, you've confirmed the culprit.
5. Note the worst names; Fixes 2–4 address each category permanently.

### Fix 2: Enable Memory Saver and Energy Saver

The highest-impact two toggles.

1. Open Chrome **Settings** > **Performance** and turn on **Memory Saver** — inactive tabs sleep and release RAM automatically.
2. On the same page, turn on **Energy Saver** — it additionally throttles background tab activity, helping both RAM and battery on laptops.
3. Under Memory Saver, use **Always keep these sites active** to exempt what must stay live: music streaming, video calls, web chat, active documents.
4. Test for a day of normal use — most users see 30–40% lower Chrome memory with zero perceived downside.
5. If a site misbehaves when woken (rare: some banking or streaming pages), add it to the exemption list rather than disabling the feature.

### Fix 3: Audit and purge extensions

Extensions are silent, permanent residents.

1. Go to `chrome://extensions` and review every single one — be ruthless.
2. In Chrome's Task Manager (Shift + Esc), check each extension's memory footprint; anything over ~100MB idle deserves scrutiny.
3. Remove: duplicate-function extensions, "free VPN" extensions (often bloated and shady), shopping coupon injectors, and anything you installed once and forgot.
4. Keep: password manager, ad blocker (uBlock Origin is light and actually *saves* memory by blocking heavy ads), and genuine daily-use tools.
5. After purging, restart Chrome and compare total memory in Windows Task Manager — extension purges often free 500MB+.

### Fix 4: Practice tab discipline (with tools, not willpower)

You won't manually manage 40 tabs — automate it.

1. Use **Tab Groups** (right-click a tab > Add to new group) to collapse project contexts instead of leaving everything open.
2. Enable **Tab freeze** behavior via Memory Saver (Fix 2) — it automates what discipline can't.
3. Install a session manager (like Session Buddy or OneTab) to park research sessions as lists instead of open tabs — OneTab famously collapses dozens of tabs into a page using a fraction of the RAM.
4. Close infinite-scroll tabs (social feeds, news) when done — they're the leakiest category; reopen fresh rather than leaving them for days.
5. Set a personal rule: if you haven't looked at a tab in 3 days, bookmark or OneTab it and close it.

### Fix 5: Tune hardware acceleration and preloading

Two settings that trade RAM for speed — adjust the trade.

1. Go to Chrome **Settings** > **System**: if the **GPU Process** is enormous in Chrome's Task Manager, try toggling **Use hardware acceleration when available** off and on (test each way for a day) — on some laptop iGPUs, software rendering is leaner.
2. Go to **Settings** > **Performance** (or Privacy) and turn off **Preload pages** — this stops Chrome spending RAM on pages you might visit.
3. At `chrome://settings/cookies` level thinking: also limit **background** activity by disabling "Continue running background apps when Chrome is closed" in **Settings** > **System** — this kills the tray-resident Chrome that holds RAM after you "close" it.
4. Restart Chrome after these changes and re-measure.
5. Keep a note of what you changed — if video playback suffers with acceleration off, revert that one toggle.

### Fix 6: Update Chrome and clear the cruft

Stale builds and corrupted profiles waste memory.

1. Go to **Help** > **About Google Chrome** and let it update — memory-leak fixes ship regularly; running months behind is a needless handicap.
2. Clear bloated site data: **Settings** > **Privacy and security** > **Delete browsing data** > **Advanced** — clear **Cached images and files** (keep passwords/history).
3. If a specific site always leaks, clear its data individually: padlock icon > **Site settings** > **Clear data**, or via `chrome://settings/siteData`.
4. For a deeply misbehaving profile, create a fresh one (**Profile icon** > **Add**) and migrate bookmarks — corrupted profiles can hold memory oddly.
5. Verify in `chrome://version` that you're current after updating.

### Fix 7: Consider the nuclear options (informed)

When Chrome's architecture itself is the mismatch.

1. If you consistently need 50+ tabs, try **Firefox** for a week — its architecture is often leaner at high tab counts, and its tab unloading is aggressive.
2. Or try **Edge** — same Chromium engine, but Sleeping Tabs and Efficiency mode are excellent and it's already on your Windows 11 laptop.
3. Whatever you choose, import bookmarks/passwords via the new browser's import wizard — switching costs are lower than people fear.
4. Alternatively: add RAM. On 8GB laptops where Chrome is your whole workflow, a 16GB upgrade is the honest fix — check your model's SODIMM slots. Windows memory-management basics are explained further on [Microsoft Support](https://support.microsoft.com/en-us/windows).
5. Don't run two heavy browsers simultaneously — pick one daily driver and close the other completely (including background processes).

## Closing

Chrome's RAM appetite is architectural — process isolation plus heavy web apps — but it's manageable: enable Memory Saver, audit extensions ruthlessly, automate tab parking, and find the one leaky tab with Chrome's Task Manager. Those four steps resolve the vast majority of "Chrome ate my laptop" cases on 24H2. And if your workflow genuinely needs 40 tabs and 8GB isn't cutting it, that's a hardware answer, not a settings failure.
