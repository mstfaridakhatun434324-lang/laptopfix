---
title: "How to Turn Off Windows Tips and Suggestions in Windows 11 24H2"
slug: how-to-turn-off-windows-tips-and-suggestions-in-windows-11-24h2
date: 2026-09-20
categories: ["performance"]
tags: ["windows tips", "suggestions", "notifications", "windows 11 24h2"]
description: "Stop Windows 11 24H2's tips, suggestions, and notification ads. Every toggle — Settings, notifications, and lock screen — in one guide."
thumbnail: "/images/thumbs/how-to-turn-off-windows-tips-and-suggestions-in-windows-11-24h2.webp"
faqs:
  - q: "Do Windows tips and suggestions slow down my laptop?"
    a: "Slightly, yes. The Tips app content, suggestion notifications, and Start menu recommendations each consume background resources — the notification system polls for new suggestions, and the Tips app can preload content. The performance gain from disabling them is modest, but the bigger wins are fewer interruptions, less telemetry, and a cleaner interface. On low-end laptops, every background process you remove helps."
  - q: "What's the difference between tips, suggestions, and Start recommendations?"
    a: "Tips are tutorial popups and the Tips app content teaching Windows features. Suggestions are notification-style prompts recommending apps, settings, or Microsoft services. Start menu recommendations are the 'Recommended' section showing recently used files and suggested apps. They're controlled by separate toggles, so silencing one doesn't silence the others — this guide covers all three."
  - q: "Will turning off suggestions disable important Windows notifications?"
    a: "No. These toggles only affect Microsoft's promotional and tutorial content — tips, app suggestions, and 'suggested' settings. Security alerts, Windows Update notifications, app notifications you've allowed, and system warnings are completely unaffected. You're turning off the marketing layer, not the notification system itself."
  - q: "Do these settings stay off after Windows updates?"
    a: "Mostly, but feature updates occasionally re-enable suggestion toggles — it's a known pattern with Windows 11 updates. After any major update (like moving to a new annual version), revisit Settings > System > Notifications and the Privacy settings to confirm your choices stuck. It takes thirty seconds and prevents the suggestions from quietly creeping back."
---

Windows 11 24H2 loves to "help": tips about features you didn't ask about, suggestions to try apps you don't want, notifications promoting Microsoft services, and a Start menu recommending files at you. Individually they're minor; collectively they're a steady drip of interruptions plus background activity you never opted into. Worse, they're scattered across half a dozen settings pages, so most people only disable one or two and wonder why the suggestions continue.

This guide kills all of them in one pass: notification suggestions, the Tips app, Start menu recommendations, lock-screen suggestions, and the Settings-app nudges. It takes about five minutes and leaves your important notifications untouched. For more ways to quiet Windows down, see [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/); for overall responsiveness, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Suggestions are on by default**: Every fresh install and many updates enable the full suggestion stack without asking.
- **Multiple independent toggles**: Tips, notification suggestions, Start recommendations, and lock-screen tips are separate settings in separate locations.
- **Feature updates re-enable them**: Annual updates have a habit of resetting suggestion toggles to Microsoft's preferred defaults.
- **The Tips app preloads content**: It fetches and caches tutorial content in the background, using network and disk.
- **Notification system polls for suggestions**: The suggestion pipeline periodically checks for new promotional content to push.
- **Settings app shows "suggested" content**: The Settings home page surfaces suggestions that add clutter and minor load.
- **Lock screen shows tips and ads**: "Get fun facts, tips, tricks" on the lock screen is enabled by default on many installs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable notification suggestions

The most visible offender — suggestion popups from the notification center.

1. Open **Settings** > **System** > **Notifications**.
2. Scroll to the bottom and turn off **Offer suggestions on how I can set up my device**.
3. On the same page, turn off **Get tips and suggestions when I use Windows** — this is the master switch for tip-style notifications.
4. While here, review the per-app list and disable notifications for apps you don't need pinging you (promotional app notifications often hide here).
5. These two toggles alone eliminate the majority of suggestion popups.

### Fix 2: Remove Start menu recommendations

Stop the Start menu from advertising apps and files at you.

1. Open **Settings** > **Personalization** > **Start**.
2. Turn off **Show recommendations for tips, shortcuts, new apps, and more**.
3. Decide on **Show recently added apps** and **Show recently opened items** — these are functional, not promotional; keep them if you find them useful, or turn them off for a minimal Start menu.
4. The Recommended section will now shrink to nothing or disappear, leaving a cleaner Start.
5. Note: this doesn't remove pinned apps — those are yours and stay put.

### Fix 3: Quiet the Tips app and Settings nudges

The tutorial layer most people never open deliberately.

1. Open the **Tips** app (search "Tips" in Start), click the three-dot menu or Settings within the app, and disable its notifications and background content if options are offered.
2. Better: if you never use it, uninstall it — right-click **Tips** in Start > **Uninstall** (on 24H2 it can be removed like a normal app).
3. Open **Settings** > **Privacy & security** > **General** and turn off **Show me suggested content in the Settings app**.
4. On the same page, turn off **Let apps show me personalized ads by using my advertising ID** — adjacent clutter worth killing in the same pass.
5. These changes remove the "suggested settings" cards from the Settings home page.

### Fix 4: Clean up the lock screen

The lock screen is a suggestion surface too.

1. Open **Settings** > **Personalization** > **Lock screen**.
2. If **Personalize your lock screen** is set to **Windows spotlight**, either switch to **Picture** or uncheck **Get fun facts, tips, tricks, and more on your lock screen**.
3. Spotlight's tips are the source of lock-screen suggestions; a static picture eliminates them entirely.
4. While here, set **Lock screen status** to **None** if you don't need app status on the lock screen — fewer background hooks.
5. This also slightly speeds up the lock-to-desktop transition by removing content fetching.

### Fix 5: Disable suggested actions and search highlights

Two subtler suggestion channels worth closing.

1. Open **Settings** > **System** > **Clipboard** and turn off **Suggested actions** — this stops Windows from popping up app suggestions when you copy phone numbers, dates, or addresses.
2. Open **Settings** > **Privacy & security** > **Search permissions** and turn off **Show search highlights** — this removes the decorative, Bing-driven content and doodles from the search box.
3. Both are minor individually, but they complete the quiet-Windows picture.
4. Restart File Explorer (**Task Manager** > **Windows Explorer** > **Restart**) to apply the search-box change immediately.
5. If you use the search box heavily for files, note that disabling highlights doesn't affect actual search results — only the decorative content.

### Fix 6: Verify with a Group Policy / Registry lock (optional)

For keeping them off permanently, including across updates.

1. Press Win + R, type `gpedit.msc` (Pro editions) and navigate to **User Configuration** > **Administrative Templates** > **Start Menu and Taskbar** > **Remove Recommendations from Start Menu** — set to **Enabled**.
2. On Home edition, use the Registry: go to `HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Explorer`, create DWORD **HideRecommendedSection** = `1` (create the Explorer key if missing; back up first).
3. Policy-level settings survive feature updates better than Settings toggles.
4. After the next annual update, do a 30-second re-check of Fix 1's toggles anyway — belt and suspenders.
5. Document what you changed (a screenshot of each page) so future-you can re-apply quickly.

## Closing

Windows 11 24H2's suggestion machinery is spread across notifications, Start, lock screen, Settings, and search — which is exactly why it feels impossible to fully silence. Hit all six areas in one sitting and you get a quieter, slightly leaner system with zero loss of real functionality. Just remember the post-update re-check: Microsoft likes to flip these back on when you're not looking. For deeper documentation on Windows notification controls, see [Microsoft Support](https://support.microsoft.com/en-us/windows).
