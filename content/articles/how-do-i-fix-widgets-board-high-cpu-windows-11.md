---
title: "Widgets Board Using Too Much CPU? How to Fix It in Windows 11"
slug: how-do-i-fix-widgets-board-high-cpu-windows-11
date: 2026-09-01
categories: ["performance"]
tags: ["widgets board", "high cpu", "widgets.exe", "windows 11", "taskbar"]
description: "Widgets.exe driving up CPU usage in Windows 11? Learn why the Widgets Board misbehaves and how to calm it down or disable it entirely."
thumbnail: "/images/thumbs/how-do-i-fix-widgets-board-high-cpu-windows-11.webp"
faqs:
  - q: "What is the Widgets Board and why does it use CPU?"
    a: "The Widgets Board is the news, weather, stocks, and calendar panel that slides out from the left side of the taskbar, powered by the Widgets.exe process using Edge's rendering engine. It uses CPU because it continuously refreshes its content feeds, renders web content in the background, and keeps the taskbar widget live — even when you never open the board."
  - q: "Is it safe to disable the Widgets Board?"
    a: "Completely safe — Widgets is an optional feature, not a system component. Disabling it in taskbar settings removes the Widgets entry point and stops Widgets.exe from running. Nothing else in Windows depends on it: Start menu, search, notifications, and all apps work exactly as before. You can re-enable it anytime with one toggle."
  - q: "Why does Widgets.exe run even when I never open it?"
    a: "The taskbar widget (usually showing weather) keeps Widgets.exe alive to refresh its display, and the board pre-loads content so it opens instantly when clicked. Background content refreshes, ad rotations in the news feed, and Edge WebView2 rendering all consume CPU silently. Turning off the taskbar widget entry point is what actually stops the background process."
  - q: "Does the Widgets Board affect gaming performance?"
    a: "It can, modestly — Widgets.exe refreshing feeds and rendering web content in the background steals CPU cycles and occasionally causes stutter on CPU-bound systems. Gamers commonly report smoother frame pacing after disabling Widgets. It's rarely the primary cause of poor gaming performance (check GPU drivers first), but it's free performance to reclaim."
---

The Widgets Board is Windows 11's most ignorable feature burning very real CPU. Most people never open it — yet Widgets.exe sits in Task Manager refreshing news feeds, weather, and stocks around the clock, occasionally spiking CPU for no visible reason. On laptops where every watt and every CPU cycle counts, that's an easy win waiting to happen.

The fix ranges from taming it (fewer refreshes, less content) to removing it entirely (one toggle, fully reversible). Since Widgets leans on Edge's engine, related background drain is covered in our [Edge CPU troubleshooting guide](/articles/edge-high-cpu-usage-windows-11-troubleshooting/); for the deeper diagnostic version, see [troubleshooting Widgets high CPU](/articles/troubleshoot-widgets-board-high-cpu-windows-11/).

## Why this happens

- **Continuous feed refreshes**: News, weather, stocks, and sports content update on timers all day.
- **Edge WebView2 rendering**: The board is essentially a hidden browser window, with a browser's CPU appetite.
- **Taskbar widget keeping it alive**: The weather widget on the taskbar prevents the process from ever fully sleeping.
- **Ad and content rotation**: The news feed's sponsored content refreshes aggressively.
- **Pre-loading for instant open**: Content loads before you click so the board appears fast.
- **Stuck refresh loops**: A failing feed can retry endlessly, pinning CPU.
- **Multiple widget processes**: The board can spawn several helper processes that add up.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check that Widgets.exe is really the culprit

Verify before you change anything.

1. Open **Task Manager** > **Processes**, sort by **CPU**, and look for **Widgets.exe** — note whether it's sustained usage or brief spikes.
2. Click the Widgets taskbar entry (or press **Win+W**) to open the board, then watch CPU — if it jumps the moment the board renders, the feed content is the load.
3. End the Widgets.exe task and observe for an hour — if overall CPU and fan noise drop noticeably, the board was costing you real resources.
4. Check **Task Manager** > **Startup apps** — Widgets shouldn't be there as a separate entry; its autostart is tied to the taskbar setting.
5. Note your usage honestly: if you haven't opened the board in weeks, there's no reason to keep its background machinery running.

### Fix 2: Disable the Widgets taskbar entry point

The one-toggle fix that stops the background process.

1. Right-click the taskbar and choose **Taskbar settings**.
2. Toggle **Widgets** to **Off** — the weather widget disappears from the taskbar.
3. Open Task Manager and confirm **Widgets.exe** is gone (end it once if it's lingering — it won't restart without the taskbar entry).
4. Reboot and verify it stays gone — the toggle persists across restarts.
5. Live without it for a few days — most people never miss it, and you can re-enable it in seconds if you do. This single step resolves the issue for the majority of sufferers.

### Fix 3: Tame the board instead of killing it

If you actually like Widgets but not its appetite.

1. Open the board (**Win+W**), click your profile icon or the settings gear, and review the widget list — remove every widget you don't read.
2. Fewer widgets means fewer feeds refreshing: keep weather and calendar, drop news, stocks, and sports if you don't check them.
3. In the board's settings, look for notification and content-refresh options and set them to the least frequent available.
4. Sign out of the Microsoft account feed personalization if offered — personalized ad-laden feeds refresh more aggressively than static ones.
5. Compare CPU after the trim — a minimal board costs a fraction of the default content firehose. Lenovo and Dell specific notes are in our [Widgets on Lenovo](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-lenovo-laptop/) and [Dell](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-dell-laptop/) guides.

### Fix 4: Block its network refresh triggers

For Widgets that spike on metered or slow connections.

1. Go to **Settings** > **Network & internet** > **Wi-Fi** (or Ethernet) > set your connection as **metered** — Windows throttles background content refreshes on metered connections.
2. In **Settings** > **Apps** > **Installed apps**, check for **Windows Web Experience Pack** — this is the Store package behind Widgets; updating it via the Microsoft Store sometimes fixes runaway refresh bugs.
3. Open the Microsoft Store > **Library** > **Get updates** and install any Web Experience Pack update — Microsoft has shipped Widgets performance fixes through this channel.
4. If spikes correlate with network activity, a failing feed endpoint may be retrying — the Store update is the usual cure.
5. As a diagnostic, disconnect from the internet for 10 minutes and watch Widgets.exe — if CPU drops to zero offline, feed refreshes were the entire cost.

### Fix 5: Disable via Group Policy or Registry (Pro/permanent)

For a more thorough removal.

1. On Windows 11 Pro: open `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > enable **Allow widgets** set to **Disabled**.
2. On Home (no gpedit): open Registry Editor, go to `HKLM\SOFTWARE\Policies\Microsoft\Dsh`, create DWORD **AllowNewsAndInterests** = `0` (create the Dsh key if missing).
3. Reboot — the Widgets toggle disappears from taskbar settings and the process never launches.
4. To reverse: set the policy to **Not Configured** or delete the registry value, then reboot.
5. This is overkill for most users — the taskbar toggle (Fix 2) is sufficient and simpler. Reserve the policy method for managed machines or if the toggle keeps re-enabling after updates.

### Fix 6: Update Edge WebView2 and the Web Experience Pack

Widgets runs on shared components — fix them.

1. Widgets renders through **Microsoft Edge WebView2** — a broken WebView2 runtime causes rendering loops that burn CPU.
2. Download the latest WebView2 runtime from Microsoft's official site (search "WebView2 runtime" on [Microsoft Support](https://support.microsoft.com/en-us/windows) for the current link) and install it.
3. Update **Windows Web Experience Pack** via the Microsoft Store as described in Fix 4.
4. Install all pending Windows updates — Widgets fixes ride along in cumulative updates.
5. Re-test with the board open for 10 minutes — component-level fixes resolve the "board spikes CPU the moment it renders" pattern.

### Fix 7: Check for the broader background-app problem

Widgets might be one of several drains.

1. Go to **Settings** > **Apps** > **Installed apps**, and for apps you don't use, set **Background app permissions** to **Never** (via Advanced options).
2. Review **Task Manager** > **Startup apps** for other quiet consumers — Teams, OneDrive, and manufacturer utilities often run alongside Widgets.
3. Our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) covers the full audit — Widgets is rarely the only background tax.
4. Consider the cumulative effect: Widgets + Teams autostart + OneDrive sync + search indexing can collectively keep a laptop's CPU from ever idling.
5. After the full cleanup, check Task Manager at idle — a healthy Windows 11 laptop idles under 5% CPU, and getting there is the real goal.

## Closing

The Widgets Board is optional, and optional features don't get to burn your CPU. If you use it, trim it to the widgets you read; if you don't, one toggle in taskbar settings silences it for good. Either way, Widgets.exe stops being a line item in your Task Manager — which is all anyone ever wanted from it.
