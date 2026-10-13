---
title: "Widgets.exe High CPU? Fix the Windows Widgets Board Drain"
slug: how-to-fix-widgets-exe-high-cpu-reddit
date: 2026-10-04
categories: ["performance"]
tags: ["widgets.exe", "widgets board", "high cpu", "windows 11"]
description: "Widgets.exe burning CPU on Windows 11? Fix the Widgets board high CPU drain — from quick toggles to full removal."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-reddit.webp"
faqs:
  - q: "What is widgets.exe and why is it using CPU?"
    a: "Widgets.exe powers the Windows 11 Widgets board — the news, weather, stocks, and calendar panel that slides in from the left. It uses CPU because it's constantly fetching fresh content: news feeds, weather updates, stock tickers, and MSN content cards. The web-content rendering (it's essentially a browser under the hood) is surprisingly expensive, especially with the animated and ad-heavy MSN feed."
  - q: "Is it safe to disable widgets.exe?"
    a: "Yes, completely safe. The Widgets board is an optional feature — disabling or uninstalling it affects nothing else in Windows. Your taskbar, Start menu, notifications, and weather app (if installed separately) all work fine. Many performance-conscious users remove it as standard practice with zero downsides beyond losing the news panel."
  - q: "Why does widgets.exe use CPU even when I never open it?"
    a: "The Widgets board pre-fetches and refreshes content in the background so it's instant when you do open it — news, weather, and stocks update on a schedule regardless of whether you look. The taskbar widgets icon (weather display) also triggers refreshes. Background content fetching is by design, which is why the only real fix for background CPU is disabling the feature."
  - q: "Does uninstalling Widgets break Windows Update?"
    a: "No. Widgets is a removable app package with no dependencies in the update system. Windows Update works identically without it. Feature updates may reinstall it (Microsoft occasionally restores removed inbox apps), in which case you simply uninstall it again — a 30-second job."
---

It's a top complaint on Reddit's Windows forums: `widgets.exe` sitting at 10–30% CPU, doing nothing you asked for, on a Widgets board you've never intentionally opened. Windows 11's Widgets panel is a web-content machine — news feeds, weather, stocks, MSN cards — constantly fetching and rendering in the background so the panel feels instant. That background work costs real CPU, real battery, and real fan noise, all for a feature many users never wanted.

The fixes range from a 10-second toggle to full uninstallation. Pick your level of commitment. For other background-drain culprits, see our [Runtime Broker fix](/articles/best-way-to-fix-runtime-broker-high-cpu/) and [startup trim guide](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Constant content fetching**: News, weather, and stocks refresh on schedules whether you look or not.
- **WebView2 rendering overhead**: The board is essentially a browser — rendering MSN's heavy pages costs real CPU.
- **Animated taskbar widget**: The weather/stocks taskbar icon updates and animates, triggering refresh cycles.
- **Ad-heavy MSN feed**: The default news content is laden with trackers and media that burn CPU rendering.
- **Notification badge updates**: Widgets pushing badge updates wake the process repeatedly.
- **Corrupt widget cache**: Damaged cached content makes the fetcher retry in loops.
- **Reinstalled by updates**: Feature updates restore it silently, resurrecting the drain.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm widgets.exe is the drain

Verify before removing anything.

1. Open **Task Manager** > **Processes**, sort by CPU — find **Widgets** (widgets.exe) and note its sustained usage.
2. Check **Settings** > **System** > **Power & battery** > **Battery usage** — Widgets often appears as a notable background drain.
3. Note whether it's constant or spiky — constant 10%+ at idle is the classic complaint; brief spikes when opening the board are normal.
4. Press **Win+W** to open the board — if CPU jumps while it's open and stays high after closing, background fetching is the issue.
5. This confirms the target — the fixes below escalate from gentle to complete.

### Fix 2: Turn off the Widgets board toggle

The quick Settings-level disable.

1. Right-click the taskbar > **Taskbar settings** (or **Settings** > **Personalization** > **Taskbar**).
2. Toggle **Widgets** to **Off** — this removes the taskbar entry point and stops most background activity.
3. Restart and check Task Manager — widgets.exe should be absent or dormant.
4. This is the fix most users need — quick, reversible, no side effects.
5. If widgets.exe still runs after this, proceed to the stronger fixes — something is re-triggering it.

### Fix 3: Disable Widgets via Group Policy / Registry

The policy-level kill.

1. **Registry method**: open `regedit`, go to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh` (create the Dsh key if missing).
2. Create **AllowNewsAndInterests** (DWORD 32-bit), set to `0`. (Yes, the name is a legacy holdover — it controls Widgets.)
3. **Group Policy method** (Pro): `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > enable **Allow widgets** set to **Disabled**.
4. Restart — the Widgets board is now policy-disabled and won't launch from any trigger.
5. Back up the registry key before editing (right-click > **Export**) — standard precaution.

### Fix 4: Uninstall the Widgets package

Complete removal via PowerShell.

1. Open PowerShell as administrator.
2. Run: `Get-AppxPackage *WebExperience* | Remove-AppxPackage` — this removes the Windows Web Experience Pack that hosts Widgets.
3. Verify: Win+W should do nothing, and widgets.exe should never appear in Task Manager again.
4. To reinstall later: get **Windows Web Experience Pack** from the Microsoft Store.
5. This is the Reddit-favorite fix — clean, complete, reversible. Microsoft documents app package management on [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Block WebView2 runtime abuse (targeted)

When you want Edge's engine but not the Widgets drain.

1. Note: Widgets uses the **WebView2** runtime, which other apps (Teams, Office) also use — don't uninstall WebView2 itself.
2. The package removal in Fix 4 is the correct granularity — it removes the Widgets host, not the shared runtime.
3. If widgets.exe persists after Fix 4, check for third-party apps embedding their own widget-like feeds — some manufacturer utilities mimic this behavior.
4. In **Settings** > **Apps** > **Installed apps**, look for manufacturer "info" or "news" apps and disable their background permissions.
5. Keep WebView2 updated via Windows Update — an outdated runtime is buggier and hungrier.

### Fix 6: Clean up after major updates

Updates reinstall it — stay vigilant.

1. After each Windows **feature update**, check Task Manager for widgets.exe's return — Microsoft periodically restores inbox apps.
2. If it's back, re-run Fix 4's PowerShell command — 30 seconds, done.
3. Re-check the taskbar toggle (Fix 2) — updates sometimes re-enable the taskbar entry.
4. Consider a post-update checklist: Widgets, Teams (personal), Clipchamp, and other inbox apps you removed — verify they're still gone.
5. This maintenance takes a minute per feature update — trivial compared to the daily CPU drain.

### Fix 7: Replace the functionality you actually used

If you liked *parts* of Widgets, get them cheaper.

1. **Weather**: pin your favorite weather site, or use the standalone MSN Weather app with background refresh off.
2. **News**: an RSS reader or news app uses a fraction of the resources of the Widgets board's ad-heavy feed.
3. **Calendar**: the taskbar clock's calendar flyout (click the date/time) covers quick date checks with zero background cost.
4. **Stocks**: your broker's app or site — updated when you look, not 24/7.
5. The pattern: on-demand beats always-on for everything. Your CPU will thank you, and our [slow laptop guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/) has more background-drain wins.

## Closing

Widgets.exe high CPU is Windows spending your processor on a news panel you didn't open. The taskbar toggle fixes most cases in ten seconds; the PowerShell uninstall ends it permanently. It's your CPU — spend it on things you actually use, not MSN's ad feed rendering in the background. And if a future update brings the Widgets board back, you'll recognize the symptoms instantly now: unexplained idle CPU, a warm laptop doing nothing, and a process name you already know how to remove.
