---
title: "How to Turn Off Background Apps to Save Battery"
slug: how-to-turn-off-background-apps-to-save-battery
date: 2026-09-30
categories: ["battery"]
tags: ["background apps", "battery drain", "startup apps", "power efficiency"]
description: "Background apps silently eat your battery all day. Here's how to find the worst offenders and shut them down without breaking anything."
thumbnail: "/images/thumbs/how-to-turn-off-background-apps-to-save-battery.webp"
faqs:
  - q: "Do background apps really drain laptop battery?"
    a: "Yes — significantly. Cloud sync tools, messaging apps, game launchers, and browser helpers can collectively consume 20-40% of a battery over a workday. The Battery usage page in Settings shows exactly how much each app used."
  - q: "Is it safe to turn off background apps?"
    a: "For most apps, yes. Turning off background activity stops them from syncing and updating when you're not using them — they'll still work normally when opened. Leave security software and anything you rely on for notifications enabled."
  - q: "What's the difference between background apps and startup apps?"
    a: "Startup apps launch when Windows boots; background apps keep running (or wake periodically) after you close their windows. An app can be both. For battery savings, you want to tame both lists."
  - q: "Will turning off background apps break notifications?"
    a: "It can delay or stop notifications from that app until you open it. If you depend on timely alerts from an app (messaging, email), leave its background activity on and restrict the ones you don't need instant updates from."
---

Your laptop's battery doesn't just power the apps you're using — it powers dozens of apps you're *not* using. Cloud drives syncing, launchers checking for updates, messaging apps polling for messages, browser extensions phoning home. Individually they're small; collectively they're often the difference between six hours of battery and three. Here's how to find them and shut them down without breaking anything you need.

Think of this as an audit, not a purge. The goal isn't to disable everything — it's to find the handful of apps doing the most damage and rein them in. In practice, three to five apps usually account for the majority of background drain, and the Battery usage page (Fix 1) will name them. Twenty focused minutes here typically buys back more runtime than any power-plan tweak.

## Why this happens

- **Apps default to maximum background activity.** Developers want their app to feel instantly alive, so background permissions default to on.
- **Startup apps pile up silently.** Every installer adds itself to startup; few ask. After a year, 15+ apps launch at every boot.
- **Cloud sync tools** (OneDrive, Dropbox, Google Drive) sync continuously, hammering CPU, disk, and network.
- **Game launchers and updaters** (Steam, Epic, EA) run background services even when you haven't gamed in weeks.
- **Browser background processes** keep running after you close the window, especially with many extensions.
- **Windows' own background activity** — indexing, telemetry, update checks — adds a baseline drain.
- **Per-app location polling.** Weather, shopping, and social apps pinging your location in the background keep the radio and CPU awake long after you've closed them.
- **Notification spam waking apps.** Every push notification wakes its app to process it — a noisy app drains by a thousand tiny wake-ups.
- **"Helper" utilities** from printer, audio, and peripheral makers that serve no purpose 99% of the time.

## How to fix it

Work through these in order, from biggest wins to fine-tuning.

### Fix 1: Find the offenders in Battery usage

Don't guess — check the actual numbers first.

1. Open **Settings** > **System** > **Power & battery** > **Battery usage**.
2. Change the dropdown to **Last 24 hours** or **Last 7 days**.
3. Sort by usage. The top 5 apps are your targets — write down the names.
4. Tap any app to see its background vs. in-use split. High background numbers mean it's draining while you're not even using it.

### Fix 2: Restrict background activity per app

1. In that same **Battery usage** list, click an offending app to expand it.
2. Set **Background activity** to **Never** (or **Managed by Windows** if you want a middle ground — Windows then decides based on your usage patterns, which is gentler than a hard block).
3. Repeat for every app you don't need live updates from. Prioritize the top offenders from Fix 1 before working down the list.
4. Alternatively: **Settings** > **Apps** > **Installed apps** > click an app's **...** > **Advanced options** > **Background apps permissions** > **Never**.
5. Check back in **Battery usage** after a day of normal use — the restricted apps' background numbers should have collapsed. If one didn't, it may be running as a service instead (see Fix 7).

### Fix 3: Clean up startup apps

1. Press **Ctrl + Shift + Esc** to open **Task Manager**, then go to the **Startup apps** tab.
2. Look at the **Startup impact** column. Disable anything rated **High** that you don't need immediately at boot — launchers, updaters, chat apps.
3. Right-click > **Disable**. This doesn't uninstall anything; the app still works when you open it manually.
4. Restart and feel the difference — both in boot time and idle drain.

### Fix 4: Tame cloud sync tools

1. Open **OneDrive** settings (click the cloud icon in the system tray > gear > **Settings**) and pause syncing when on battery, or limit it to specific folders.
2. Do the same for Dropbox, Google Drive, or others — set them to manual sync or "pause on battery" if the option exists.
3. Sync tools are consistently among the top background consumers; this one change often buys 30+ minutes.

### Fix 5: Stop browsers running in the background

1. In Chrome/Edge, go to **Settings** > **System** and turn off **Continue running background apps when the browser is closed**.
2. Audit extensions — remove any you don't recognize or no longer use. Each one is a small always-on process.
3. Enable tab sleeping/suspension features so inactive tabs stop consuming resources.

### Fix 6: Disable unnecessary Windows background activity

1. Go to **Settings** > **System** > **Power & battery** > **Power mode** and set it to **Best power efficiency** — this alone throttles background work.
2. In **Settings** > **Privacy & security** > **Background apps** (wording varies by build), review the global list.
3. Turn on **Battery saver / Energy saver** to automatically kick in at 20% — it suppresses background activity system-wide.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents these settings if anything looks different on your build.

**Cut location polling and notification wake-ups:** Two permission types turn quiet apps into background drainers: location and notifications.

5. Go to **Settings** > **Privacy & security** > **Location**. Turn off location access entirely, or leave it on and disable it per-app for everything that doesn't genuinely need it (weather apps need it; shopping apps don't).
6. Go to **Settings** > **System** > **Notifications**. Disable notifications for apps whose alerts you ignore anyway — each one wakes the app to process it.
7. For apps you keep notifications on for, check their in-app settings for notification frequency. "All activity" vs. "mentions only" can be the difference between 200 wake-ups a day and 5.
8. If one app still dominates the battery chart after all of this, it may be misbehaving rather than merely busy — check [battery draining fast on Windows 11](/articles/laptop-battery-drains-fast-windows-11/) for the deeper causes.

### Fix 7: Hunt down background services, not just apps

Apps are only half the story — Windows services run constantly whether or not their app is open.

1. Press **Ctrl + Shift + Esc**, go to **Task Manager** > **Processes**, and sort by **Power usage** (or CPU) to spot service-hosted drain.
2. Press **Win + R**, type `services.msc`, and look for third-party services set to Automatic: printer updaters, audio enhancers, RGB lighting services, and "helper" services from software you uninstalled months ago.
3. For services tied to software you still use, leave them. For leftovers from uninstalled software, set them to **Disabled** — or better, uninstall the parent software properly.
4. Be conservative with Microsoft's own services; disabling the wrong one breaks things. When in doubt, set to **Manual** rather than **Disabled** — a Manual service still starts if something actually needs it.

**Put hungry processes in Efficiency mode:** For processes you can't or won't close, Task Manager's Efficiency mode throttles them instead.

5. Open **Task Manager** (**Ctrl + Shift + Esc**) and sort by CPU or power usage.
6. Right-click a consistently hungry background process and choose **Efficiency mode**. Windows caps its CPU priority and resource appetite.
7. Good candidates: updaters, sync helpers, and browser sub-processes. Don't apply it to games or creative apps while you're actively using them — it will slow them down.
8. Efficiency mode persists across restarts for that process, so this is a set-and-forget throttle rather than a daily chore.

### Fix 8: Uninstall what you don't use

The ultimate background-app fix is removal.

1. **Settings** > **Apps** > **Installed apps**, sort by size or last used.
2. Uninstall manufacturer bloatware, old game launchers, and utilities you haven't opened in months.
3. Fewer apps means fewer updaters, fewer background services, fewer startup entries — a compounding win.

If your battery still drains fast after taming the apps, the problem may be deeper — see [why a laptop battery discharges quickly](/articles/how-to-fix-battery-discharges-quickly-on-laptop/) for hardware and system-level causes.

## Closing

Background apps are the slow leak in most laptops' battery life — invisible, cumulative, and entirely fixable. The Battery usage page tells you exactly who's guilty, and twenty minutes of disabling startup entries and background permissions typically buys back an hour or more of real runtime. Make it a twice-a-year habit: installers will keep adding themselves back, so a periodic cleanup keeps the leak sealed.

Overnight drain deserves its own check too — if the battery also drops while the laptop sleeps, see our [sleep mode drain troubleshooting](/articles/troubleshoot-laptop-battery-drains-in-sleep-mode/) for the wake-timer and Modern Standby fixes that daytime app cleanup won't touch.
