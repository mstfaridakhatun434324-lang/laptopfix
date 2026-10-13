---
title: "How to Turn Off Background Apps to Save Battery in Windows 11"
slug: how-can-i-turn-off-background-apps-to-save-battery
date: 2026-09-02
categories: ["battery"]
tags: ["background apps", "battery saving", "windows 11"]
description: "Background apps quietly drain your laptop battery. Learn exactly where to find them in Windows 11 and shut them down for longer runtime."
thumbnail: "/images/thumbs/how-can-i-turn-off-background-apps-to-save-battery.webp"
faqs:
  - q: "Where is the background apps setting in Windows 11?"
    a: "Go to Settings → Apps → Installed apps, click the three dots next to an app, choose Advanced options, and set Background apps permissions to Never. There is no single master switch in Windows 11 — you control it per app."
  - q: "Will turning off background apps break notifications?"
    a: "For that specific app, yes — it won't be able to fetch new messages or show notifications while closed. Keep background access on for messaging and email apps you rely on, and turn it off for everything else."
  - q: "How much battery do background apps actually use?"
    a: "It varies wildly. A few idle apps cost almost nothing, but sync-heavy apps — cloud storage, game launchers, social apps — can consume 10–25% of a charge over a day. The worst offenders show up in Task Manager's power usage column."
  - q: "Do I need to redo this after Windows updates?"
    a: "Sometimes. Major Windows updates can reset background permissions for some apps. It's worth re-checking your top offenders after each feature update, which you can verify through the official Windows support pages."
---

You close an app, but it doesn't really close. It keeps syncing, checking for updates, and refreshing feeds in the background — all on your battery's dime. On a typical laptop, a handful of greedy background apps can quietly eat an hour or more of runtime every day. The fix is straightforward once you know where Windows 11 hides the controls.

This guide shows you every place background activity lives in Windows 11, how to shut down the worst offenders without breaking the apps you actually need, and how to keep them from creeping back.

## Why this happens

- **Apps default to background access** — Most apps request background permission at install, and Windows grants it silently.
- **Sync services never sleep** — Cloud storage, email, and messaging apps poll servers constantly to stay "fresh."
- **Update checkers and launchers** — Game stores and manufacturer utilities run 24/7 checking for updates you could fetch manually.
- **Windows updates reset permissions** — Feature updates sometimes restore background access you previously revoked.
- **Startup apps become background apps** — Anything launching at boot tends to linger in the background all day.
- **No single off switch** — Windows 11 removed the old global background-apps toggle, so the drain hides across per-app settings most people never open.

## How to fix it

Work through these in order — from the biggest wins to the fine-tuning.

### Fix 1: Kill background access per app in Settings

This is the main control. It takes a few minutes but pays off daily.

1. Open **Settings → Apps → Installed apps**.
2. For each app you don't need live in the background, click the **three dots (⋯)** next to it and choose **Advanced options**.
3. Under **Background apps permissions**, change the dropdown from **Power optimized** or **Always** to **Never**.
4. Prioritize: social media apps, game launchers (Steam, Epic), cloud sync tools you rarely use, manufacturer bloatware, and shopping apps.

Start with the 5–10 apps you use least. You can always re-enable one if you miss its notifications.

### Fix 2: Stop apps from launching at startup

Startup apps are background apps waiting to happen — stop them at the source.

1. Press **Ctrl + Shift + Esc** to open **Task Manager**.
2. Go to the **Startup apps** tab.
3. Look at the **Startup impact** column — disable anything marked **High** that you don't need immediately at boot.
4. Right-click each offender and choose **Disable**.

Fewer startup apps means a faster boot and fewer background processes draining power from minute one.

### Fix 3: Use Task Manager to find the worst background drainers

Let Windows tell you which background processes are actually expensive.

1. In **Task Manager**, go to the **Processes** tab.
2. Enable the **Power usage** column (right-click a column header → check it) and sort by it.
3. Expand any app to see its background processes underneath.
4. For chronic offenders, go back to **Settings → Apps → Installed apps → Advanced options** and set them to **Never** as in Fix 1.
5. Also check the **Startup** tab while you're in Task Manager — apps set to launch at boot almost always keep background processes running all day, so disabling them there compounds the savings.

This pairs well with the broader drain hunt in [why your laptop battery drains so fast](/articles/how-to-fix-laptop-battery-drains-fast-step-by-step/).

### Fix 4: Turn off background activity for Microsoft Store apps

Store apps have their own background habits worth checking.

1. Open the **Microsoft Store**, click your profile icon → **Settings**.
2. Turn off **Update apps automatically** if you prefer updating manually on AC power — auto-updates often run on battery.
3. Back in **Settings → Apps → Installed apps**, filter for the preinstalled apps (Xbox Game Bar, Clipchamp, Teams, etc.) and set background permissions to **Never** for the ones you never open.

### Fix 5: Quiet the system-level background features

Windows itself runs background features that cost power.

1. Go to **Settings → Privacy & security → Background apps** — on some builds this page still exists as an overview; use it if present.
2. In **Settings → System → Notifications**, turn off notifications for apps you don't care about — each notification can wake the app.
3. Go to **Settings → Accounts → Windows backup** and pause or limit sync frequency for settings sync you don't need constantly.
4. In **Settings → Bluetooth & devices**, turn off **Bluetooth** when not in use.

### Fix 6: Limit cloud sync apps' background behavior

Cloud storage apps are among the heaviest background users.

1. Open your sync app's settings (OneDrive, Dropbox, Google Drive) and look for bandwidth or sync-frequency options.
2. In **OneDrive settings → Sync and backup**, pause syncing while on battery, or use **Pause syncing** for a set number of hours when you need maximum runtime.
3. Consider quitting the sync app entirely (**right-click tray icon → Quit**) during long battery sessions and relaunching it when plugged in.

### Fix 7: Enable Battery Saver to throttle what's left

After trimming the worst offenders, let Battery Saver handle the rest automatically.

1. Go to **Settings → System → Power & battery**.
2. Set **Turn battery saver on automatically at** to **40%**.
3. Enable **Lower screen brightness when using battery saver**.

Battery Saver restricts background activity for Store apps system-wide, which catches anything you missed. For the official rundown of power features, see [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Audit monthly — updates undo your work

This isn't a one-time fix, because Windows feature updates can re-enable background permissions.

1. After each major Windows update, spend 5 minutes re-checking **Settings → Apps → Installed apps** for your known offenders.
2. Re-check **Task Manager → Startup apps** too — updates love to re-enable manufacturer utilities.
3. Keep a mental shortlist of your 5 worst apps so the audit takes minutes, not half an hour.

## Closing

Background apps are death by a thousand cuts for battery life — no single one matters much, but together they steal real hours. The per-app permissions in Settings are your main weapon: set the apps you don't need to Never, keep the ones you do, and let Battery Saver sweep up the rest. Do the audit after each Windows update and your battery will thank you every single day. On a current Windows 11 build, the [Windows 11 background-apps walkthrough](/articles/how-to-turn-off-background-apps-to-save-battery-on-windows-11/) shows the exact Settings screens you'll see.
