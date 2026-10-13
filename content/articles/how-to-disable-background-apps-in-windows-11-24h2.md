---
title: "How to Disable Background Apps in Windows 11 24H2"
slug: how-to-disable-background-apps-in-windows-11-24h2
date: 2026-09-17
categories: ["performance"]
tags: ["background apps", "windows 11 24h2", "battery life", "performance", "privacy"]
description: "Stop Windows 11 24H2 apps from running in the background: per-app controls, system-wide settings, and battery-saving tweaks explained step by step."
thumbnail: "/images/thumbs/how-to-disable-background-apps-in-windows-11-24h2.webp"
faqs:
  - q: "Will disabling background apps break notifications?"
    a: "For the apps you restrict, yes — that's the tradeoff. An app set to Never run in the background can't fetch new messages or show notifications until you open it. That's why the per-app approach in this guide matters: restrict the apps whose notifications you don't need (games, shopping, news) and leave messaging and email apps allowed."
  - q: "What's the difference between background apps and startup apps?"
    a: "Startup apps launch when you sign in and typically keep running visibly. Background apps can run without ever appearing — syncing, updating tiles, fetching data — even if you never opened them this session. Both consume resources, but background apps are sneakier because Task Manager's Startup tab doesn't list them; you manage them in Settings → Apps instead."
  - q: "Does disabling background apps really improve battery life?"
    a: "Yes, measurably — especially on laptops where dozens of apps wake the CPU and radio for background syncs. Microsoft's own battery guidance lists background activity among the top drains. Users typically see the biggest gains from restricting social, news, and shopping apps that sync aggressively, plus a snappier-feeling system from reduced background CPU."
  - q: "Why do some apps not have a background permission setting?"
    a: "Only Microsoft Store (UWP) apps use the background-permissions model — traditional desktop (Win32) apps like Chrome or Steam manage their own background behavior in their own settings. If an app lacks the toggle in Settings → Apps, it's a desktop app: check its own preferences for background, startup, or 'run at login' options."
---

Windows 11 24H2 lets apps run in the background by default — syncing, updating, fetching — whether you opened them today or not. Individually each is trivial; collectively, dozens of background apps wake your CPU, use the network, and drain the battery around the clock. On a laptop, that background churn is one of the most fixable performance and battery drains there is.

The good news: 24H2 gives you proper per-app control, and it takes about ten minutes to audit. This guide shows the per-app method, the battery-saver angle, and how to handle desktop apps that don't respect the toggle.

## Why this happens

- **Default-allow permissions:** Newly installed Store apps default to running in the background.
- **Preinstalled app sprawl:** Manufacturer and Microsoft inbox apps all request background rights.
- **Aggressive sync schedules:** Social, news, and mail apps wake frequently to fetch content.
- **Live tiles and notifications:** Background execution powers tiles, badges, and push alerts.
- **Update checks:** Apps phoning home for updates on their own timers.
- **Desktop apps opting out:** Win32 apps ignore the Store permission model and run background services freely.
- **Battery Saver gaps:** Default Battery Saver thresholds still allow significant background activity.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Audit per-app background permissions

The core fix. Go to **Settings → Apps → Installed apps**, and for each Store app, open **Advanced options** and set **Background apps permissions** to Never for anything you don't need live: games, shopping, news, weather widgets you never check, preinstalled utilities. Work through the list once — it takes ten minutes and the effect is permanent. Leave messaging, email, and authenticator apps on **Power optimized** (the default) so their notifications keep working. The [laptop-focused background apps guide](/articles/how-to-disable-background-apps-on-laptop/) covers the same audit with laptop-specific priorities.

1. Open **Settings → Apps → Installed apps**.
2. For each Store app, open Advanced options.
3. Set **Background apps permissions** to Never for unneeded apps.
4. Leave essential messaging/email apps on Power optimized.

### Fix 2: Use Battery Saver to enforce background limits

**Settings → System → Power & battery → Battery saver** is the system-wide enforcer. Turn it on manually when you need maximum quiet, and set **Turn battery saver on automatically** to a high threshold (like 40–50%) so it kicks in early on battery. Battery Saver aggressively throttles background activity, push notifications, and sync across the board. It's the single toggle that covers even apps you missed in the per-app audit. Pair it with the per-app restrictions for layered control: audit for the plugged-in state, Battery Saver for mobile.

1. Open **Settings → System → Power & battery**.
2. Set Battery Saver to turn on automatically at 40–50%.
3. Turn it on manually when you need maximum battery.
4. Observe reduced background CPU in Task Manager.

### Fix 3: Handle desktop apps that ignore the toggle

Chrome, Steam, Spotify, Discord, and similar Win32 apps don't appear in the background-permissions list — they manage themselves. For each: open the app's own settings and disable **Continue running background apps**, **Launch at startup**, or **Start minimized to tray** as appropriate. Also check **Task Manager → Startup apps** and disable their startup entries. These apps are often the heaviest background consumers precisely because the Windows toggle can't touch them — their own settings are the only lever. The [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) walks through the Task Manager side.

1. Identify heavy Win32 apps in Task Manager's Processes tab.
2. Disable background/launch options inside each app's settings.
3. Disable their entries in Task Manager → Startup apps.
4. Verify they stay closed after a reboot.

### Fix 4: Trim notifications and sync at the source

Background activity exists to serve notifications, tiles, and sync — reduce the demand. In **Settings → System → Notifications**, turn off notifications for apps you restricted; a silenced app has less reason to wake. In **Settings → Accounts → Windows backup** and individual app settings, reduce sync frequency for cloud services you don't need real-time. Fewer push triggers means fewer background wakes even for apps you left allowed. Microsoft documents the notification model in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Turn off notifications for restricted apps.
2. Reduce cloud sync frequency where real-time isn't needed.
3. Unpin live tiles you never look at.
4. Confirm fewer background wakes in Task Manager.

### Fix 5: Check the battery usage report to verify

Prove the fix worked. Go to **Settings → System → Power & battery** and open the **Battery usage** breakdown — it shows per-app consumption over the last 24 hours or 7 days. Compare before and after your audit: background-heavy apps should drop dramatically. If an app still shows high background usage despite being set to Never, it's likely a desktop app needing Fix 3's in-app treatment, or a system component you shouldn't restrict. Let the data guide a second pass.

1. Open **Settings → System → Power & battery → Battery usage**.
2. Review per-app background consumption.
3. Target remaining high-background apps with Fix 1 or Fix 3.
4. Re-check after 48 hours.

### Fix 6: Consider the nuclear option for unused apps

Apps you never open shouldn't exist, background permissions or not. Go back through **Settings → Apps → Installed apps** and uninstall the preinstalled games, trials, partner apps, and duplicate utilities you skipped during the audit. Uninstalled apps consume zero background resources — the ultimate restriction. Be careful to keep drivers, hardware utilities, and anything you might need; when in doubt, restrict first (reversible) and uninstall later (less reversible). The [battery-focused background guide](/articles/best-way-to-turn-off-background-apps-to-save-battery/) prioritizes which categories to cut first.

1. Revisit Installed apps with fresh eyes.
2. Uninstall preinstalled apps you never open.
3. Keep drivers and hardware utilities.
4. Final check: Task Manager background processes should be lean.

## Closing

Background apps are death by a thousand cuts for laptop battery and responsiveness — and Windows 11 24H2 gives you the knife to stop it. Audit per-app permissions once, enforce with Battery Saver, handle the Win32 exceptions in their own settings, and verify with the battery report. Ten minutes of setup, permanent quiet.
