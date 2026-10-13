---
title: "How to Disable Background Apps on Windows 11 (3 Methods)"
slug: "how-to-disable-background-apps-on-windows-11"
date: "2026-10-07"
categories: ["performance"]
tags: ["background apps", "windows 11", "disable background", "battery life", "performance"]
description: "Too many apps running in the background on Windows 11? Here are three safe methods to disable them — Settings, Task Manager, and Group Policy."
thumbnail: "/images/thumbs/how-to-disable-background-apps-on-windows-11.webp"
faqs:
  - q: "What happens when I disable background apps in Windows 11?"
    a: "Disabled apps can't run background tasks — no live tile updates, no background notifications, no pre-loading content, and no background syncing. The app itself still works perfectly when you open it; it just goes fully dormant when closed instead of lingering. For most desktop programs this changes nothing noticeable; for messaging and mail apps it means notifications arrive only when the app is open."
  - q: "Will disabling background apps improve battery life?"
    a: "Yes, measurably on laptops. Background apps wake the CPU from low-power states to sync, poll, and update — each wakeup costs battery. Users typically report 30-90 minutes of additional battery life after disabling background activity for apps they don't need live, with the biggest gains on laptops that had dozens of Store apps running background tasks. It's one of the highest-yield battery tweaks in Windows 11."
  - q: "Is it safe to disable all background apps?"
    a: "Mostly, but be selective rather than blanket-disabling. Safe to disable: games, media apps, manufacturer bloatware, shopping apps, and anything you open manually anyway. Keep enabled: your email client (if you want notifications), messaging apps you rely on, security software, and cloud sync (OneDrive/Dropbox) if you depend on background syncing. Disabling Windows Security's background activity is not recommended."
  - q: "Why do disabled apps sometimes re-enable themselves?"
    a: "Major Windows updates occasionally reset background-app permissions, and some apps (particularly manufacturer utilities and apps updated through the Store) re-register background tasks on update. It's worth re-checking your settings after each feature update. Apps can't re-enable the system-wide Group Policy block though — that's why the policy method in Fix 3 is the most durable option."
---

Your laptop is 'idle' — no apps open — yet the fan hums, the battery drains, and Task Manager shows dozens of processes busy. That's background apps: programs Windows lets run tasks, sync data, and push notifications while you're not looking. A few are useful. Most are just spending your battery and CPU on updates you'll never see.

Windows 11 changed how background permissions work compared to Windows 10 — the old global 'let apps run in the background' toggle is gone, replaced by per-app settings plus battery-based controls. That makes cleanup slightly more fiddly but also more precise: you can silence the freeloaders while keeping your email and messenger live.

Below are three methods, from the simple per-app switches to the set-and-forget policy block. If startup programs (a different thing — apps launching at login) are your bigger problem, see our guide to [fixing slow app launches](/articles/how-to-fix-apps-opening-slowly-on-windows-11/) which covers those.

## Why this happens

- **Default-allowed Store apps** — Fresh Windows 11 installs grant background permission to dozens of inbox apps — news, weather, games, Clipchamp — most of which you'll never open, let alone need live.
- **Manufacturer utilities phoning home** — Dell, HP, and Lenovo utilities run background tasks for update checks, telemetry, and 'optimization' scans that wake the system regularly.
- **Chat and Teams integrations** — Windows 11's Teams Chat integration and other messaging apps maintain persistent background connections — constant, low-level CPU and network activity.
- **Cloud sync clients** — OneDrive, Dropbox, and Google Drive sync engines run continuously, watching the file system and uploading changes — legitimate but costly on battery.
- **Browser background processes** — Chrome and Edge keep background processes alive for notifications and updates even with no window open, unless configured otherwise.
- **Gaming overlays and launchers** — Steam, Epic, Discord, and GeForce Experience all run background services for updates, friends lists, and overlays — pure overhead when you're working.
- **Windows features you don't use** — Widgets board refreshes, Phone Link syncing, and search highlights all run background work for features many users never touch.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Method 1: Per-app background settings (precise)

The built-in, supported way — best for most people.

1. Open **Settings > Apps > Installed apps**.
1. Click the **⋯** next to an app > **Advanced options**.
1. Under **Background apps permissions**, change **Let this app run in background** from 'Power optimized' to **Never**.
1. Work through the list: set **Never** for games, media apps, manufacturer bloatware, and anything you open manually. Leave **Power optimized** (or Always) for email, messaging, and cloud sync you rely on.

### Fix 2: Method 2: Task Manager startup + background cleanup

Background apps and startup apps are different — handle both.

1. Open Task Manager (**Ctrl + Shift + Esc**) > **Startup apps** — **Disable** updaters, launchers, and chat apps you don't need at login.
1. In **Processes**, sort by **CPU** and **Power usage** columns to spot the busiest background dwellers — match them to apps you can restrict in Method 1.
1. For Store apps specifically, **Settings > System > Power & battery > Battery usage** shows per-app drain — the worst offenders go on your Never list.
1. Restart and compare: idle CPU in Task Manager should sit near 0-2% with nothing open.

### Fix 3: Method 3: Group Policy block (durable, Pro only)

The set-and-forget option that survives updates and app reinstalls.

1. Press **Win + R**, type `gpedit.msc`, and go to **Computer Configuration > Administrative Templates > Windows Components > App Privacy**.
1. Open **Let Windows apps run in the background**, set it to **Enabled**, then choose **Deny** in the dropdown — this blocks background activity for all Store apps.
1. For finer control, the per-app settings in Method 1 still work alongside; the policy is the backstop.
1. **Windows 11 Home** users: the equivalent is a registry value, but per-app settings (Method 1) are safer and sufficient — skip the registry unless you manage multiple machines.

### Fix 4: Calm the big-ticket background consumers

A few specific apps deserve individual attention beyond the generic switches.

1. **Widgets**: right-click taskbar > **Taskbar settings** > toggle **Widgets** off — or see our [widgets.exe CPU fix](/articles/how-to-fix-widgets-exe-high-cpu-on-hp-laptop/) if it's burning CPU.
1. **Phone Link**: if you never use it, **Settings > Bluetooth & devices > Phone Link** > turn it off.
1. **Teams Chat**: **Settings > Apps > Installed apps > Microsoft Teams > Advanced options** > background **Never** (unless you live in Teams).
1. **OneDrive**: right-click tray icon > **Pause syncing** during battery-critical work; or **Settings > Account > Choose folders** to shrink what's watched.

### Fix 5: Tame browser background activity

Browsers are the sneakiest background residents.

1. Chrome: **Settings > System** > disable **Continue running background apps when Google Chrome is closed**.
1. Edge: **Settings > System and performance** > disable **Continue running background extensions and apps when Microsoft Edge is closed**.
1. In both, review **On startup** pages — 'Continue where you left off' with 40 tabs is a background workload disguised as a convenience.
1. These two toggles alone reclaim meaningful idle CPU on many laptops.

### Fix 6: Audit gaming and utility background services

Launchers and RGB tools don't need to run 24/7.

1. Open `services.msc` and set game-launcher and RGB/fan-control services you rarely need to **Manual** instead of **Automatic** — they start when you open the app.
1. In each launcher (Steam, Epic, Discord): **Settings** > disable **Run on startup** / **Start minimized** options.
1. Keep security software and hardware-monitoring services on Automatic — don't touch those.
1. The goal: when you're working, only work-related background activity runs.

## Closing

Background apps are death by a thousand cuts — no single one matters, but thirty of them do. Twenty minutes with the per-app settings, the two browser toggles, and a pass through startup entries buys you quieter fans, a cooler lap, and real battery life back. Revisit after each feature update; Windows has a habit of re-inviting guests you uninvited. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the background-app permission model if you want the official reference.
