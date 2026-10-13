---
title: "How to Turn Off Background Apps to Save Battery in Windows 11 24H2"
slug: how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2
date: 2026-09-17
categories: ["battery"]
tags: ["battery", "background apps", "windows 11 24h2", "battery life"]
description: "Background apps silently drain your laptop battery. Here's how to find and disable them in Windows 11 24H2 for longer runtime."
thumbnail: "/images/thumbs/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2.webp"
faqs:
  - q: "Do background apps really drain laptop battery?"
    a: "Yes, measurably. Apps running in the background keep the CPU from entering deep sleep states, use the network radio, and wake the disk. On a typical laptop, a handful of chat, cloud sync, and updater apps running in the background can cost 30 to 90 minutes of runtime compared to a clean idle."
  - q: "Will turning off background apps break notifications?"
    a: "For most Store apps, turning off background activity stops live tile updates and push notifications from that app. Messaging apps like Teams or WhatsApp may not alert you to new messages until you open them. Keep background access on for the two or three apps where timely notifications matter, and disable the rest."
  - q: "What is the difference between background apps and startup apps?"
    a: "Startup apps launch when you sign in and may then sit idle or keep working. Background apps are specifically Store apps that Windows allows to run tasks while you are not using them. Both drain battery, but they are controlled in different places: startup apps in Task Manager, background permissions in Settings."
  - q: "Should I just use Battery Saver instead?"
    a: "Battery Saver helps, but it is a blunt instrument that throttles everything below a threshold. Selectively disabling background permissions for apps you do not need gives you most of the savings without degrading the apps you actually use. Use both: trim background apps permanently, and let Battery Saver handle the low-battery emergencies."
---

Your laptop idles at your desk, screen dimmed, nothing visibly running — yet the battery ticks down far faster than it should. The culprit is usually invisible: a crowd of apps doing work in the background. Cloud drives syncing, chat clients polling, updaters phoning home, widgets refreshing. Individually each sips power; together they keep your processor from ever truly resting.

Windows 11 24H2 gives you proper controls for this, but they are scattered across three different settings pages. This guide walks through all of them: per-app background permissions, startup apps, and the background processes that Task Manager reveals. Trim these once and the savings are permanent.

## Why this happens

- **Store apps run background tasks by default.** Many apps installed from the Microsoft Store register background activity on install, and most users never change it.
- **Cloud sync apps poll constantly.** OneDrive, Dropbox, and similar tools watch the file system and network continuously, which prevents deep CPU sleep.
- **Chat and messaging apps stay connected.** Teams, Slack, Discord, and WhatsApp maintain live connections so messages arrive instantly — at a steady power cost.
- **Updaters and launchers phone home.** Game launchers, Adobe Creative Cloud, and manufacturer utilities run background services that check for updates on schedules.
- **Widgets and news feeds refresh.** The Widgets board and apps with live tiles fetch fresh content periodically, waking the network radio each time.
- **Startup apps accumulate silently.** Every installer that adds itself to startup adds another permanent background resident.

## How to fix it

Work through these in order. Steps 1 and 2 deliver most of the savings.

### Fix 1: Disable background permissions per app

This is the main control. Go through the list and be ruthless.

1. Open **Settings > Apps > Installed apps**.
2. Click the three dots next to an app you rarely need live updates from, and choose **Advanced options**.
3. Under **Background apps permissions**, change the dropdown from **Power optimized** or **Always** to **Never**.
4. Repeat for every app where you do not need background activity: games, media apps, shopping apps, manufacturer bloatware, and anything you open less than weekly.
5. Keep **Never** off for your two or three essential messaging apps if you rely on their notifications.

Prioritize the worst offenders first. Our [battery usage guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) is about battery health, but the same **Settings > System > Power & battery > Battery usage** screen shows which apps consumed the most power in the last 24 hours — start your cull there.

### Fix 2: Trim startup apps in Task Manager

Apps that launch at sign-in start draining from minute one.

1. Press **Ctrl + Shift + Esc** to open Task Manager, then go to the **Startup apps** tab.
2. Look at the **Startup impact** column. Anything marked **High** that you do not need immediately at login is a candidate.
3. Right-click entries like game launchers, Adobe services, Spotify, or manufacturer utilities and choose **Disable**.
4. Keep your antivirus, cloud sync (if you need instant sync), and audio drivers enabled.
5. Restart and notice both faster login and slower battery drain.

### Fix 3: Turn off background activity for system features you do not use

Windows itself runs background features many people never touch.

1. Open **Settings > Personalization** and turn off background slideshow themes if you use them — a static wallpaper uses no ongoing power.
2. Go to **Settings > Apps > Installed apps** and disable background permissions for preinstalled apps you never open: Clipchamp, Teams (if you do not use it), TikTok, Spotify, and trial antivirus apps.
3. In **Settings > Privacy & security > Background apps** (on some 24H2 builds this is under Apps), review the master list and toggle off anything non-essential.
4. Disable **Widgets** from refreshing: open the Widgets board, click the gear, and turn off the news feed if you do not read it.

### Fix 4: Stop unnecessary services and scheduled tasks

Some drain comes from services, not apps.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Look for third-party services set to **Automatic** that you do not need constantly — updater services for software you rarely use, printer services for a printer you no longer own.
3. Double-click such a service, change **Startup type** to **Manual**, and stop it. Never disable Microsoft services or your antivirus this way.
4. Open **Task Scheduler** and check the **Task Scheduler Library** for third-party tasks that run hourly — software updaters are the usual suspects — and disable the aggressive ones.

### Fix 5: Tame OneDrive and cloud sync

Cloud sync is useful but does not need to run at full intensity on battery.

1. Click the OneDrive cloud icon in the system tray, open **Settings**, and on the **Sync and backup** page, pause syncing while on battery if your version offers it.
2. Use **Files On-Demand** so files download only when opened, instead of keeping everything synced locally.
3. If you use multiple cloud apps, consider quitting the ones you do not need during a battery-critical work session — right-click their tray icons and choose Quit.
4. For Dropbox and similar, set bandwidth limits in their settings so sync bursts do not pin the CPU.

### Fix 6: Use Battery Saver and power mode strategically

After trimming the app list, let Windows handle the rest automatically.

1. Go to **Settings > System > Power & battery** and set **Battery saver** to turn on automatically at 30 percent.
2. Set **Power mode** to **Best power efficiency** — this caps CPU boost behavior that background apps love to trigger.
3. In the same page, check **Battery usage** weekly for the first month. New culprits appear after software installs, and a quick glance catches them early.
4. Consider creating the habit: when you install any new app, immediately check its background permission in **Installed apps > Advanced options**. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has more detail on how Battery Saver interacts with background activity.

If your battery still drains unusually fast after this cleanup, the issue may be deeper than apps — our guide to [rapid battery discharge](/articles/how-to-fix-battery-discharges-quickly-on-laptop-in-windows-11-24h2/) covers hardware and driver causes.

### Fix 7: Audit monthly to keep the savings

Background permissions creep back with updates and reinstalls.

1. Once a month, revisit **Settings > Apps > Installed apps** and sort by install date to catch newcomers.
2. After every feature update, recheck — updates sometimes reset app permissions.
3. Uninstall apps you have not opened in three months instead of merely disabling them. Fewer apps means fewer updaters, fewer services, fewer surprises.

An hour of your time spent trimming background activity pays back every single day in longer runtime. The laptop you bought had this battery life all along — it was just sharing it with thirty apps you never asked to run.

## Closing

Be systematic rather than aggressive: check battery usage to find the real offenders, set their background permissions to Never, trim startup, and let Battery Saver handle the rest. Your idle drain will drop noticeably, and the apps you actually use will keep working exactly as before.
