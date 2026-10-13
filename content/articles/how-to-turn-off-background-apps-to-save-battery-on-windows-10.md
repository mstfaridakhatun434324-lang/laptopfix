---
title: "Turn Off Background Apps to Save Battery on Windows 10"
slug: how-to-turn-off-background-apps-to-save-battery-on-windows-10
date: 2026-10-08
categories: ["battery"]
tags: ["background apps", "battery saver", "windows 10"]
description: "Background apps silently drain your Windows 10 laptop battery. Here's every switch to turn them off and reclaim hours of runtime."
thumbnail: "/images/thumbs/how-to-turn-off-background-apps-to-save-battery-on-windows-10.webp"
faqs:
  - q: "Do background apps really drain laptop battery?"
    a: "Yes — measurably. A dozen apps with background permission can keep the CPU and network radio active, costing 10–25% of your battery over a workday. Messaging apps, updaters, and launchers are the worst offenders because they wake the system frequently."
  - q: "Where is the background apps setting in Windows 10?"
    a: "Go to Settings > Privacy > Background apps. There's a master toggle (Let apps run in the background) plus per-app switches. Turning off the master switch is the fastest win; then re-enable only the few apps you genuinely need live, like your email or messaging app."
  - q: "Will turning off background apps break notifications?"
    a: "For Microsoft Store apps, disabling background activity can delay or stop their notifications and live tiles. Desktop (Win32) apps like Chrome or Slack manage their own background behavior separately. Keep background on for the 2–3 apps whose notifications you truly need."
  - q: "What's the difference between background apps and startup apps?"
    a: "Startup apps launch when you sign in; background apps keep running and waking the system even when you're not using them. Both drain battery, but background apps are sneakier — they consume power all day, not just at boot. Fix both for the full benefit."
---

Your laptop idles, screen off, and the battery still melts away. The culprit is rarely one big app — it's the dozen little ones running in the background, phoning home, syncing, updating, and waking the CPU every few minutes. Windows 10 gives you the switches to stop them; most people just never flip them.

This is a complete lockdown guide: the master switch, the per-app list, the startup list, and the sneaky extras. Budget about fifteen minutes — you'll do it once, and then a quick quarterly review keeps new apps from creeping back in.

## Why this happens

- **Default-on background permissions.** Windows 10 grants background access liberally at install; most users never review it.
- **Updaters and launchers.** Game launchers, printer utilities, and vendor updaters run 24/7 for the rare moments they're needed.
- **Messaging and sync apps.** These wake the network radio frequently — the Wi-Fi radio is a major battery draw.
- **Preinstalled bloatware.** Vendor and trial apps often have aggressive background behavior.
- **Windows features.** Cortana, suggestions, and telemetry components run in the background by default.
- **Browser background activity.** Chrome and Edge keep running after you close the window unless told otherwise.
- **Startup pile-up.** Every app that launches at sign-in adds to the all-day background load.

## How to fix it

Work through these in order — each layer adds savings.

### Fix 1: Use the master background apps switch

1. Open **Settings > Privacy > Background apps**.
2. At the top, turn off **Let apps run in the background**. This single toggle stops all Store apps' background activity at once.
3. Test battery life for a day. If something you need (like Mail notifications) stops working, come back and use the per-app approach instead.
4. Note: this doesn't affect traditional desktop programs — those are covered in Fix 4. Microsoft documents the current layout of these toggles in their [Windows battery and power guidance](https://support.microsoft.com/en-us/windows) if your Settings look different after an update.

### Fix 2: Allow background access selectively

If the master switch breaks something you need:

1. Turn the master switch back **On**.
2. Scroll through the per-app list and turn **Off** everything you don't need live: games, trial apps, vendor utilities, anything you open manually anyway.
3. Leave **On** only essentials — typically Mail, Calendar, and one messaging app.
4. Revisit this list every few months; new installs sneak back in.

### Fix 3: Trim startup apps

1. Press **Ctrl + Shift + Esc** to open Task Manager, then go to the **Startup** tab.
2. Sort by **Startup impact**. Disable everything **High** impact that isn't security software: updaters, chat clients, cloud storage you don't use daily, game launchers.
3. Right-click > **Disable** — this doesn't uninstall anything, it just stops auto-launch.
4. Restart and confirm they stay off.

### Fix 4: Stop desktop apps running in the background

Store-app toggles don't cover traditional programs.

1. **Chrome/Edge:** go to Settings > **System** and turn off **Continue running background apps when the browser is closed**.
2. **Slack, Discord, Teams:** each has a setting like "leave app running in notification area when closed" — turn it off if you don't need instant notifications.
3. Check the **system tray** (click the ^ arrow): every icon there is a running program. Right-click > exit or open its settings to disable background running for anything non-essential.
4. **OneDrive/Dropbox:** if you don't need constant sync, set them to not start with Windows and launch manually.

### Fix 5: Disable Windows background features you don't use

1. **Settings > Privacy > General**: turn off **Let apps use advertising ID** and **Show me suggested content in the Settings app**.
2. **Settings > Privacy > Feedback & diagnostics**: set **Diagnostic data** to **Basic** (or Required) and **Feedback frequency** to **Never**.
3. **Settings > System > Notifications & actions**: turn off **Get tips, tricks, and suggestions** and suggestions on the lock screen.
4. **Cortana:** if you don't use it, disable it — on most Windows 10 builds you can restrict it via Settings or simply not sign in.

### Fix 6: Turn on Battery Saver aggressively

1. Go to **Settings > System > Battery**.
2. Turn **Battery saver** on and set **Turn battery saver on automatically** to **40%** (higher than the 20% default — earlier intervention saves more).
3. Check **Lower screen brightness while in battery saver**.
4. Battery Saver throttles background activity system-wide — it's the safety net under all the manual toggles above.
5. While you're here, note the estimated remaining time Windows shows. It's a rough guess, but check it before and after your lockdown — seeing it climb is the most satisfying confirmation that the changes worked.

### Fix 7: Check power usage per app

1. Go to **Settings > System > Battery** and click **See which apps are affecting your battery life**.
2. Change the dropdown to **24 hours** or **1 week**.
3. Any app with shocking usage gets uninstalled or has its background permission revoked (Fix 2).
4. This is also how you catch a misbehaving app after an update — check here first whenever drain suddenly worsens. For update-related drain specifically, see our guide to [fast drain after a Windows 11 update](/articles/how-to-fix-laptop-battery-drains-fast-after-windows-11-update/).

### Fix 8: Reduce sync and location background work

1. **Settings > Privacy > Location**: turn off location for apps that don't need it, or turn off the master location switch if you never use location features.
2. **Mail app:** open it, go to Settings > **Manage Accounts** > each account > **Change mailbox sync settings**, and set **Download new content** to every 30 minutes or manually instead of "as items arrive."
3. **Windows Update:** set active hours (**Settings > Update & Security > Windows Update > Change active hours**) so updates don't download and install during your workday on battery.

## Closing

Background apps are death by a thousand cuts for battery life — no single one matters, but together they can cost you an hour or more of runtime. The master switch plus a startup trim takes ten minutes and is the highest-return battery tweak on Windows 10. Do it once, audit quarterly, and your battery will last noticeably longer every single day. Pair this with sensible screen brightness and the Battery Saver threshold from Fix 6, and you've covered the three biggest software-side drains in one sitting. On Windows 11? The same principles apply — see the [Windows 11 version of this guide](/articles/how-to-turn-off-background-apps-to-save-battery-on-windows-11/).
