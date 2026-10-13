---
title: "How to Disable Startup Apps on Windows 11"
slug: "how-to-disable-startup-apps-on-windows-11"
date: "2026-09-23"
categories: ["performance"]
tags: ["startup apps", "windows 11", "boot speed", "task manager", "autostart"]
description: "Stop programs from launching at boot on Windows 11. Covers Task Manager, Settings, Startup folders, scheduled tasks, and how to keep them from coming back."
thumbnail: "/images/thumbs/how-to-disable-startup-apps-on-windows-11.webp"
faqs:
  - q: "How do I stop apps from opening on startup in Windows 11?"
    a: "Open Task Manager with Ctrl+Shift+Esc, go to the Startup apps tab, right-click any app, and choose Disable. Alternatively, use Settings, Apps, Startup for toggle switches. Both control the same entries. For apps that do not appear in either place, check the Startup folders and Task Scheduler."
  - q: "Is it safe to disable startup apps on Windows 11?"
    a: "Yes. Disabling only prevents automatic launch — every app still works normally when you open it yourself. Keep Windows Security enabled and be careful with hardware utilities for audio, touchpads, and graphics. Chat apps, game launchers, updaters, and cloud storage are all safe to disable."
  - q: "Why do startup apps re-enable themselves after updates?"
    a: "Feature updates sometimes restore default settings, and individual apps re-create their startup entries when they update if their internal 'launch at startup' option is still on. The permanent fix is turning off the autostart option inside each app's own settings, not just in Task Manager."
  - q: "What's the difference between Disable and removing a startup app?"
    a: "Disabling keeps the entry but stops it from launching — instantly reversible. Removing (deleting the registry entry, shortcut, or scheduled task) eliminates it entirely, which is cleaner but harder to undo. For most users, disabling is sufficient and safer; removal is for entries you are certain you never want."
---

Windows 11 boots fast on modern hardware — until it does not. The usual suspect is the same as it has been for twenty years: a crowd of programs that all decided they should launch at login. Teams, Spotify, Discord, OneDrive, Steam, updaters, utilities — each one adds seconds, and together they can turn a 15-second boot into a two-minute wait for a usable desktop.

Windows 11 gives you better tools for this than Windows 10 did, including startup impact measurements based on real boot traces. But apps still hide autostart entries in the same old places: the registry, Startup folders, scheduled tasks, and services. This guide covers all of them, plus the crucial step most guides skip — stopping apps from re-enabling themselves.

## Why this happens

- **Installers opt you in silently:** "Launch at startup" defaults to on, hidden in express setup screens.
- **Every vendor wants residency:** Updaters, helpers, and tray apps from each installed program accumulate.
- **Windows 11's own additions:** Widgets, Teams Chat integration, and Phone Link add Microsoft's own autostart load.
- **Feature updates restore entries:** Major updates re-enable startup items you previously disabled.
- **In-app settings override Task Manager:** Apps with internal autostart toggles re-create entries you disable externally.
- **Scheduled tasks as stealth launch:** Logon-triggered tasks do not appear in the Startup apps tab.
- **Services starting automatically:** Heavier apps install services that launch regardless of startup lists.
- **Store apps with background rights:** Microsoft Store apps can register background tasks through a separate mechanism.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable via Task Manager's Startup apps tab

1. Press `Ctrl + Shift + Esc`, then click **Startup apps** in the left navigation.
2. Sort by Status or Startup impact to surface the enabled heavy hitters.
3. Right-click each non-essential app and choose **Disable**.
4. Restart and feel the difference — then fine-tune further.

This is the primary tool: it shows measured startup impact from actual boot telemetry, so you can see exactly what each app costs. Disable aggressively — anything you do not need within 60 seconds of login. Windows Security stays enabled; nearly everything else is optional. Every disable is reversible with one more right-click.

### Fix 2: Use Settings for a friendlier view

1. Go to Settings, Apps, **Startup**.
2. Toggle off apps using the switches; note the impact labels beneath each name.
3. This list includes some Microsoft Store apps shown more clearly than in Task Manager.
4. Changes sync with Task Manager — use whichever interface you prefer.

The Settings page is the same data with a simpler presentation, and it is the better teaching tool when helping someone else clean their machine. There is no functional difference between disabling here versus Task Manager, so pick one and be thorough rather than splitting attention.

### Fix 3: Clean both Startup folders

1. Press `Win + R`, type `shell:startup` — delete shortcuts you do not want (your user folder).
2. Repeat with `shell:common startup` for machine-wide entries (requires admin).
3. Remember: deleting a shortcut never uninstalls the program.
4. Restart to confirm the entries are gone from Task Manager too.

Startup-folder entries are invisible to the Startup apps tab on some builds, which is why installers still use them. They are the simplest autostart mechanism — just shortcuts — and the simplest to clean. If an entry here keeps reappearing, its program is regenerating it: find that program's internal setting (Fix 5).

### Fix 4: Disable stealth scheduled tasks

1. Open Task Scheduler (`taskschd.msc`) and browse the Task Scheduler Library root and vendor subfolders.
2. Identify tasks with "At log on" triggers from third-party vendors (Adobe, Google, game publishers, OEMs).
3. Right-click and **Disable** them — disabling beats deleting for reversibility.
4. Leave Microsoft\Windows system tasks alone unless you have a specific, researched reason.

This catches the entries Task Manager never shows. Updaters are the most common residents here, and they are also the most common "it came back" mechanism: the scheduled task re-enables what you disabled. A ten-minute audit of logon-triggered tasks often finds half a dozen programs phoning home at every boot. Microsoft documents Task Scheduler in [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Turn off autostart inside each app

1. Open each persistent app's settings: look for "Launch at startup," "Open at login," "Start minimized."
2. Turn the option off inside the app — this is the master switch.
3. Then disable any remaining entry in Task Manager for cleanliness.
4. Update the app afterward to confirm the setting survives updates.

This is the step that makes the cleanup permanent. Task Manager disables the current entry; the in-app setting controls whether the app creates a new one. Skip this and you will be repeating the cleanup after every app update. Prioritize chat apps, launchers, cloud storage, and music apps — the worst repeat offenders.

### Fix 6: Set third-party services to Manual

1. Press `Win + R`, type `services.msc`, sort by Startup Type.
2. Find third-party services set to Automatic: updaters, vendor helpers, media services.
3. Change them to **Manual** — the app can still start its service when actually used.
4. Do not touch Microsoft, security, audio, or networking services.

Services launch before login and run constantly, making them the most expensive form of autostart. Manual is the safe compromise: zero boot cost, full functionality on demand. If a service name is unfamiliar, search it before changing — ten seconds of research prevents breaking something you actually need.

### Fix 7: Audit Windows 11-specific autostart and maintain

1. Check Settings, Apps, Installed apps for Widgets-adjacent and Teams components you do not use; disable or uninstall.
2. Review Phone Link: if you do not use it, disable its startup and background activity.
3. Re-audit quarterly and after every feature update — updates restore entries.
4. When installing new software, always choose Custom setup and decline autostart.

Windows 11 adds its own autostart surface (Widgets board, Chat, Phone Link) on top of the classic mechanisms, so the audit must cover both. Make the quarterly check a habit — two minutes, four times a year — and boot performance stays fast permanently. If slowness extends beyond boot, our [Windows 11 speed-up guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/) and [slow-wake guide](/articles/how-to-fix-laptop-slow-to-wake-from-sleep/) address the other dimensions.

## Closing

Fast boots on Windows 11 are a maintenance outcome, not a hardware lottery: Task Manager handles the visible entries, Startup folders and scheduled tasks catch the hidden ones, in-app settings stop the resurrection, and services set to Manual remove the deepest costs. Do the full pass once, spend two minutes quarterly keeping it clean, and your laptop will keep booting like it is new.
