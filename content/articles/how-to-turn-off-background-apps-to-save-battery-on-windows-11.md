---
title: "Turn Off Background Apps to Save Battery on Windows 11"
slug: how-to-turn-off-background-apps-to-save-battery-on-windows-11
date: 2026-09-03
categories: ["battery"]
tags: ["background apps", "battery saver", "windows 11"]
description: "Windows 11 background apps eat battery all day. Here's exactly where every toggle lives and which ones to flip for maximum runtime."
thumbnail: "/images/thumbs/how-to-turn-off-background-apps-to-save-battery-on-windows-11.webp"
faqs:
  - q: "Where do I turn off background apps in Windows 11?"
    a: "Go to Settings > Apps > Installed apps, click the three dots on any app > Advanced options, and set Background apps permissions to Never. Windows 11 removed the old master toggle, so it's per-app — start with the apps shown as top consumers on the Battery usage page."
  - q: "Is there a master switch for background apps in Windows 11?"
    a: "Not like Windows 10 had. Windows 11 requires per-app control via each app's Advanced options. The closest system-wide tools are Battery Saver (which throttles background activity) and disabling startup apps in Task Manager."
  - q: "Will disabling background apps break anything?"
    a: "The app still works normally when you open it — it just won't sync, update, or notify while closed. Keep background on for the few apps where you need live notifications (email, messaging), and turn it off for everything else."
  - q: "Do background apps really make a big difference to battery?"
    a: "Yes. Independent tests and the Battery usage page consistently show background activity accounting for 15–30% of drain on typical setups. On a 6-hour battery, that's an hour or more of runtime recovered — the biggest free win in Windows 11 power tuning."
---

Windows 11 doesn't have Windows 10's convenient master background-apps switch. Instead, background permissions are per-app, scattered across Advanced options pages — which means most people never touch them, and a dozen apps happily burn battery all day behind their back.

This guide maps every relevant toggle in Windows 11 and gives you a priority order, so you spend fifteen minutes once and gain runtime every day after. Unlike generic "battery tips" lists, everything here is a specific switch in a specific place — no vague advice, just the actual clicks. Still on Windows 10? See the [Windows 10 version of this guide](/articles/how-to-turn-off-background-apps-to-save-battery-on-windows-10/) — the master switch there makes it even faster.

## Why this happens

- **Per-app defaults favor the app.** Fresh installs typically get background permission; Windows 11 rarely prompts you.
- **No master switch.** Without a single toggle, the setting stays invisible to most users.
- **Widgets board.** The Widgets feed refreshes news, weather, and stocks continuously.
- **Teams Chat integration.** The built-in Chat syncs in the background unless removed.
- **Startup apps.** Everything launching at sign-in adds to the all-day load.
- **Browser background modes.** Edge and Chrome keep processes alive after you close the window.
- **Sync services.** OneDrive, Dropbox, and similar tools poll continuously.
- **Misbehaving drivers.** A driver that doesn't handle power transitions cleanly can leave its hardware in a powered state, burning battery long after you close the lid.

## How to fix it

Work through these in order of impact.

### Fix 1: Restrict background permissions per app

1. Open **Settings > Apps > Installed apps**.
2. For each app you don't need live: click **...** > **Advanced options** > set **Background apps permissions** to **Never**.
3. Prioritize: games and launchers, printer/scanner utilities, trial apps, social apps you open manually anyway.
4. Keep **Power optimized** (the default) or **Always** only for email, calendar, and your primary messaging app.
5. There's no need to do all fifty apps in one sitting — handle the obvious ones now, then let the Battery usage page (Fix 2) tell you which remaining apps actually matter. Most people's top offenders are just three or four apps.

### Fix 2: Start from the Battery usage page

Don't guess which apps matter — let Windows tell you.

1. Go to **Settings > System > Power & battery > Battery usage**.
2. Sort by usage over the **Last 24 hours**.
3. Take the top 5 non-essential apps and set their background permission to **Never** (Fix 1).
4. Recheck in a few days — the list changes as your habits change, so this is worth a monthly glance.

### Fix 3: Clean up startup apps

1. **Ctrl + Shift + Esc** > Task Manager > **Startup apps**.
2. Disable everything you don't need within seconds of signing in: updaters, chat clients, cloud tools you rarely use, game launchers.
3. Disabling doesn't uninstall — the app still works when you launch it manually.
4. Restart and confirm the list stays as you set it.
5. Pay special attention to anything with **High** startup impact — those entries don't just slow your boot, they tend to be the same apps that keep running (and draining) all day.

### Fix 4: Tame Widgets and Teams Chat

1. **Widgets:** open the Widgets board, click your profile picture > **Settings**, and turn off the feed, notifications, and content you don't read. Or remove Widgets from the taskbar entirely: **Settings > Personalization > Taskbar** > toggle **Widgets** off.
2. **Teams Chat:** if you don't use the built-in Chat, right-click its taskbar icon > **Unpin**, then uninstall **Microsoft Teams** (the built-in one) via **Settings > Apps** if you use a different chat app.
3. These two are among the most common surprise entries on the Battery usage page.

### Fix 5: Stop browsers running in the background

1. **Edge:** Settings > **System and performance** > turn off **Continue running background extensions and apps when Microsoft Edge is closed** and **Startup boost** (startup boost keeps processes alive for faster launching — at a battery cost).
2. **Chrome:** Settings > **System** > turn off **Continue running background apps when Google Chrome is closed**.
3. Audit extensions in both — each active extension is a small background process. Remove the ones you don't use weekly.

### Fix 6: Calm down sync services

1. **OneDrive:** click its tray icon > Settings > decide whether you need **Start OneDrive automatically**; if not, launch it manually when you need to sync.
2. In OneDrive settings, use **Choose folders** to sync only what you need — fewer files means less background indexing.
3. Same logic for Dropbox, Google Drive, or any sync client: manual launch beats always-on unless you truly need instant sync.

### Fix 7: Use Battery Saver as the system-wide net

1. **Settings > System > Power & battery**: set **Battery saver** to turn on automatically at **20%** (or higher if you want earlier intervention).
2. Enable **Lower screen brightness while in battery saver**.
3. Battery Saver throttles background activity across the board — it catches everything the per-app toggles miss.
4. You can also turn it on manually any time you need to stretch the remaining charge. Microsoft's [Windows power guidance](https://support.microsoft.com/en-us/windows) has more detail on how Battery Saver interacts with background tasks.

### Fix 8: Reduce notification and location background work

1. **Settings > System > Notifications**: turn off notifications for apps you restricted in Fix 1 — a silenced app that still pings you is still waking the system.
2. **Settings > Privacy & security > Location**: turn off location access for apps that don't need it.
3. **Settings > Accounts > Windows backup** and sync settings: disable anything syncing that you don't use.
4. Do a final pass on the Battery usage page a week later to confirm the changes held and no new app has crept into the top consumers. New app installs default back to generous background permissions, so every new install is worth a ten-second check in its Advanced options.

## Closing

Windows 11 makes background control per-app instead of global, which is more work upfront but actually more precise — you keep the three apps you need live and silence everything else. Fifteen minutes here routinely buys back an hour of runtime, making it the single best time investment in Windows 11 battery tuning. Check the Battery usage page monthly and you'll keep it that way. And when friends complain their laptop "just doesn't last," you'll know exactly which three settings to check on their machine first. If drain persists even after the full lockdown, run the [fast-drain diagnostic](/articles/laptop-battery-drains-fast-windows-11/) to check the hardware side.
