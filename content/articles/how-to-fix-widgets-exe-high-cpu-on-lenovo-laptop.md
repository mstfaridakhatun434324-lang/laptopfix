---
title: "Widgets.exe High CPU on a Lenovo Laptop? Shut It Down"
slug: how-to-fix-widgets-exe-high-cpu-on-lenovo-laptop
date: 2026-09-05
categories: ["performance"]
tags: ["widgets.exe", "high cpu", "lenovo laptop", "windows widgets", "taskbar"]
description: "Widgets.exe burning CPU on your Lenovo laptop? Stop the widgets board from draining processor and battery with these fixes."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-on-lenovo-laptop.webp"
faqs:
  - q: "What is Widgets.exe and do I need it?"
    a: "Widgets.exe is the backend process for the Windows 11 widgets board — the news, weather, stocks, and calendar panel that slides out from the taskbar. If you never open the widgets board, you don't need the process running at all. Disabling the widgets board is safe and doesn't affect anything else in Windows."
  - q: "Why does Widgets.exe use CPU even when the board is closed?"
    a: "The board pre-fetches content in the background so it opens instantly — news feeds refresh, weather updates, and MSN content syncs on a schedule. On Lenovo laptops, aggressive Lenovo telemetry and network-management utilities can interfere with these background fetches, causing retry loops that pin CPU. The board is never truly idle by design."
  - q: "Will disabling widgets break the weather icon on my taskbar?"
    a: "The taskbar weather widget is part of the same widgets feature — disabling the board removes it too. If you like the at-a-glance weather, you can keep the board enabled but reduce its background activity instead (Fix 3). Most users who disable it don't miss it within a week."
  - q: "Is Widgets.exe related to Lenovo Vantage or Legion Zone?"
    a: "Not directly — Widgets.exe is pure Microsoft. But Lenovo's utilities (Vantage, Legion Zone/Armoury equivalents, network boosters) install services that interact with Windows' background task scheduling, and outdated versions have been observed aggravating widgets' background CPU usage. Keeping Lenovo software updated is part of the fix on Lenovo machines."
---

The Windows 11 widgets board is a nice idea — glanceable weather, news, and calendar — with an ugly implementation detail: `Widgets.exe` runs constantly in the background, refreshing content you'll never look at, and on some systems it develops a CPU habit that's wildly disproportionate to its job. On Lenovo laptops, where Lenovo's own background services add their own scheduling noise, widgets CPU spikes are a recurring complaint.

The honest assessment: if you don't use the widgets board, the correct fix is turning it off entirely — not tuning it. If you do like the weather glance, there are ways to keep it while taming the background cost. Either way, this is a 10-minute fix. For the widgets board's taskbar lag cousin, see [fixing taskbar lag](/articles/best-way-to-fix-taskbar-lag-windows-11/); for general background CPU hogs, [Runtime Broker fixes](/articles/best-way-to-fix-runtime-broker-high-cpu/).

## Why this happens

- **Background content refresh loops**: News/weather feeds refreshing on aggressive schedules, retrying on network hiccups.
- **MSN content sync storms**: The board's content pipeline occasionally gets stuck re-syncing the same feed items.
- **Lenovo service interference**: Outdated Lenovo utilities conflicting with Windows' background task scheduling.
- **Corrupt widgets cache**: Damaged board data causing the refresh cycle to fail and retry endlessly.
- **WebView2 runtime issues**: The widgets board renders on WebView2 — a broken runtime makes the whole board thrash.
- **Location polling**: Weather widgets hammering location services, each poll brokered through system processes.
- **Multiple board instances**: Occasionally two Widgets.exe instances run concurrently after sleep/wake cycles, doubling the cost.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm widgets is the problem (and how bad)

Quantify before you operate.

1. Open **Task Manager** > **Processes**, find **Windows Widgets** (or **Details** > `Widgets.exe`) — note its CPU at idle, and whether there are multiple instances.
2. Normal: 0–2% at idle, brief spikes when opening the board. Abnormal: sustained 10%+ at idle, or constant saw-toothing.
3. Test: open the widgets board (Win+W), close it, and watch CPU for 5 minutes — if opening the board triggers a CPU episode that doesn't settle, the content pipeline is the issue.
4. Check network activity too — a widgets process burning CPU with zero network traffic is stuck in a local loop (cache corruption, Fix 4); with heavy traffic it's a feed problem (Fix 3).
5. Note your Lenovo model and whether the spikes correlate with sleep/wake — Lenovo power-management quirks around Modern Standby are a known aggravator.

### Fix 2: Just turn the widgets board off

The fix most people actually want.

1. **Settings** > **Personalization** > **Taskbar** > toggle **Widgets** to **Off** — the taskbar icon and board disappear.
2. Open Task Manager and end any remaining **Widgets.exe** processes — they should not restart with the board disabled.
3. Verify over the next hour: no Widgets.exe in Task Manager, CPU calm. This is the complete fix for non-users of the board.
4. If a Widgets.exe instance respawns despite the toggle, check **Task Scheduler** > **Microsoft** > **Windows** > **Widgets**-related tasks and disable them.
5. You lose the taskbar weather glance — replacements: the Weather app pinned to Start, or any lightweight weather app. Most ex-widgets users report missing it for about two days.

### Fix 3: Keep the board but tame its background activity

For those who actually like the weather glance.

1. Open the widgets board (**Win+W**) > click your **profile icon** (top right) > **Settings** — review content preferences and disable feed categories you don't read (sports, finance, entertainment).
2. Fewer feed categories = fewer background refreshes = less CPU. Keep weather and calendar, drop the rest.
3. In the same settings, check for **notification** toggles — widgets board notifications trigger background wakes; disable them.
4. **Settings** > **Privacy & security** > **Location** — if weather is the only thing using location, that's fine; but deny location to any other widget-driven apps to cut polling.
5. Monitor for a day — a trimmed board typically idles at 0–1% instead of the 10%+ of a fully-loaded one.

### Fix 4: Clear the widgets cache and repair WebView2

For boards stuck in refresh loops.

1. End all **Widgets.exe** processes in Task Manager.
2. Clear the board's cache: navigate to `%localappdata%\Microsoft\Windows\Widgets` (if present) and delete its contents — the board rebuilds it on next open. (If the folder doesn't exist on your build, the cache lives under the WebView2 data — step 3 covers it.)
3. Repair **WebView2**: **Settings** > **Apps** > **Installed apps** > **Microsoft Edge WebView2 Runtime** > **...** > **Modify** > **Repair**. The widgets board is a WebView2 app — a damaged runtime makes it thrash.
4. Reopen the board once, let it fully load, then close it — confirm CPU settles within a couple of minutes.
5. If loops return within days, the board's content pipeline itself is flaky on your network — consider Fix 2 (disable) rather than fighting it indefinitely.

### Fix 5: Update Lenovo software and drivers

The Lenovo-specific angle.

1. Open **Lenovo Vantage** (or Legion Zone on gaming models) > **System Update** — install all recommended updates, especially **power management**, **network**, and **chipset** drivers.
2. In Vantage, review **background features**: disable network-boosting / "game mode" network prioritization if you don't game — these hook network traffic that widgets' background fetches depend on.
3. Check **Task Scheduler** > **Lenovo** tasks — disable aggressive inventory/telemetry tasks that run at every logon or wake; keep update checks.
4. Update the **BIOS** if Lenovo lists power-management or Modern Standby fixes for your model — sleep/wake-triggered duplicate Widgets.exe instances often trace to firmware.
5. Cross-check drivers on [Lenovo's official support site](https://support.lenovo.com/us/en/) by entering your serial number — Vantage sometimes lags the website's driver versions.

### Fix 6: Stop duplicate instances after sleep/wake

A Lenovo-flavored widgets bug.

1. If Task Manager shows **two** Widgets.exe instances after waking from sleep, that's the bug — one is orphaned from the pre-sleep session.
2. Immediate relief: end both instances in Task Manager; the board relaunches cleanly on next Win+W.
3. Longer-term: **Settings** > **System** > **Power & battery** — change sleep behavior so the laptop **hibernates** instead of Modern Standby sleep (or disable "stay connected" during sleep) — orphaned processes come from the half-awake Modern Standby state.
4. In **Device Manager**, check network adapter **Power Management** tab — uncheck **Allow this device to wake the computer** for everything except what you need; spurious wakes create the orphan instances.
5. If duplicates persist across weeks, disabling the board (Fix 2) is the pragmatic answer — a feature you don't use shouldn't get to spawn zombie processes.

### Fix 7: Group Policy / registry enforcement

For widgets that won't stay dead.

1. If the Settings toggle doesn't stick (Widgets.exe keeps respawning), use Group Policy: **Win+R** > `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > **Allow widgets** > **Disabled**.
2. On Windows 11 Home (no gpedit): registry — `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh`, create DWORD **AllowNewsAndInterests** = `0` (create the Dsh key if missing). Back up the registry first.
3. Restart — Widgets.exe should be entirely absent from Task Manager.
4. To reverse later, set the policy back to **Not configured** or delete the registry value.
5. This is also the enterprise-friendly way to kill widgets across managed Lenovo fleets. For remaining background CPU mysteries, our [Runtime Broker guide](/articles/best-way-to-fix-runtime-broker-high-cpu/) covers the next most common invisible hog.

## Closing

Widgets.exe high CPU is a feature doing busywork nobody asked for. If you don't use the board, turn it off and enjoy the silence — it's the rare Windows fix with zero downside. If you love the weather glance, trim the feeds, repair WebView2, and keep Lenovo's software current. Either way, a news panel has no business burning double-digit CPU, and now it won't.
