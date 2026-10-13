---
title: "How to Disable Startup Apps on Windows 10"
slug: "how-to-disable-startup-apps-on-windows-10"
date: "2026-09-16"
categories: ["performance"]
tags: ["startup apps", "windows 10", "boot speed", "task manager", "performance"]
description: "Too many programs launching at boot slows your Windows 10 laptop to a crawl. Learn the three places startup apps hide and how to disable them safely."
thumbnail: "/images/thumbs/how-to-disable-startup-apps-on-windows-10.webp"
faqs:
  - q: "How do I stop apps from opening on startup in Windows 10?"
    a: "The easiest method is Task Manager: press Ctrl+Shift+Esc, open the Startup tab, right-click any app, and choose Disable. You can also use Settings, Apps, Startup for a simpler toggle list. For stubborn entries, check the Startup folders and the Task Scheduler, where some programs hide their auto-launch entries."
  - q: "Is it safe to disable startup apps?"
    a: "Yes, with common sense. Disabling a startup entry only stops the program from launching automatically — the app still works when you open it manually. Keep your antivirus enabled and be cautious with hardware utilities (audio, touchpad, graphics). Everything else — chat apps, updaters, game launchers — is safe to disable."
  - q: "Why do disabled startup apps keep coming back?"
    a: "Some programs re-add themselves when they update, and a few use scheduled tasks or services instead of the normal startup registry entries. Check Task Scheduler for the app's tasks, look in both Startup folders (user and all-users), and check the app's own settings for a 'launch at startup' option that needs turning off inside the program."
  - q: "Will disabling startup apps make my laptop boot faster?"
    a: "Usually, noticeably. Every startup app competes for CPU and disk during boot, and on hard-drive laptops the difference can be dramatic — cutting 20 autostart items can halve boot time. Measure with Task Manager's 'Last BIOS time' and your own stopwatch before and after for satisfying proof."
---

Every program you install seems to believe it deserves a seat at your boot sequence. Chat clients, updaters, game launchers, cloud storage, printer utilities — they pile into startup, and one day you realize your Windows 10 laptop takes four minutes to become usable after the login screen. The apps are not malicious; they are just inconsiderate, each assuming it is the only one launching.

The fix is straightforward, but it has a wrinkle: startup apps hide in several places, and the obvious one (Task Manager) does not show them all. Programs can autostart from the registry, from Startup folders, from scheduled tasks, and from services. A complete cleanup visits each location. None of this is risky — disabling autostart never uninstalls anything, and every change is reversible in seconds.

Here is the full tour, in the order that catches the most offenders with the least effort.

## Why this happens

- **Installers default to autostart:** Most installers enable "launch at startup" silently, burying the opt-out in custom setup screens.
- **Updaters insist on running:** Every vendor wants its updater resident, so updaters accumulate with each installed program.
- **Chat and collaboration apps:** Teams, Slack, Discord, and Zoom all default to launching at boot and sitting in the tray.
- **Game launchers:** Steam, Epic, and others autostart to deliver updates and show you the store.
- **OEM bloatware:** Manufacturer utilities for support, updates, and "experiences" autostart on new laptops.
- **Scheduled tasks as stealth autostart:** Some programs use Task Scheduler entries that Task Manager's Startup tab does not show.
- **Services set to automatic:** Heavier programs install Windows services that start with the system regardless of startup lists.
- **All-users vs per-user entries:** Startup items exist in both per-user and machine-wide locations, so one cleanup pass misses half.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Audit with Task Manager's Startup tab

1. Press `Ctrl + Shift + Esc` to open Task Manager and click the **Startup** tab (click More details first if needed).
2. Enable the "Startup impact" column if hidden — sort by it to find the worst offenders.
3. For each high-impact app you do not need instantly at boot, right-click and choose **Disable**.
4. Restart and time your boot; compare against your previous experience.

The Startup tab is the highest-yield, lowest-risk cleanup available. "Startup impact" is measured from real boot traces, so trust it over brand familiarity — that chat app you "need" might cost 15 seconds of boot time. Keep antivirus enabled; disable everything else you do not need within the first minute. You can re-enable anything in seconds if you miss it.

### Fix 2: Use the Settings startup list

1. Go to Settings, Apps, **Startup**.
2. Toggle off everything non-essential — the list mirrors Task Manager but with friendlier names.
3. Pay attention to the impact labels (High/Medium/Low) shown under each app.
4. Restart and verify the toggles held.

The Settings list covers the same ground as Task Manager with a simpler interface, and on some builds it shows Store apps that Task Manager lists cryptically. Use whichever interface you prefer — changes in one appear in the other. This is also the best place to show less technical users how to manage their own startup.

### Fix 3: Clean the Startup folders

1. Press `Win + R`, type `shell:startup`, and press Enter — this is your personal Startup folder.
2. Delete shortcuts for anything you do not want autostarting (deleting the shortcut does not uninstall the program).
3. Repeat with `shell:common startup` for the all-users Startup folder (needs admin approval).
4. Restart to confirm the changes.

The Startup folders are the oldest autostart mechanism in Windows, and some installers still use them instead of the registry — which is why entries here do not appear in Task Manager's Startup tab. They are just shortcuts: removing them is completely safe and instantly reversible by re-adding the shortcut.

### Fix 4: Hunt scheduled-task autostart entries

1. Press `Win + R`, type `taskschd.msc`, and open Task Scheduler Library.
2. Look for tasks from vendors (Adobe, Google, game companies) with triggers "At log on" or "At startup."
3. Right-click suspicious auto-launch tasks and choose **Disable** (not Delete — disabling is reversible).
4. Focus on updaters and "helpers"; leave Microsoft and hardware-vendor system tasks alone.

This is where the stubborn ones hide. Programs that "come back" after you disable them in Task Manager are often re-armed by scheduled tasks. Disabling the task breaks the resurrection cycle. Be conservative: only disable tasks clearly tied to third-party applications, and never touch tasks under Microsoft\Windows that you do not understand. Microsoft documents Task Scheduler in [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Turn off in-app "launch at startup" settings

1. For each app that keeps returning, open the app itself and find its settings or preferences.
2. Look for "Launch at startup," "Open at login," "Start minimized," or similar — and turn it off inside the app.
3. Check chat apps, cloud storage, game launchers, and music apps especially.
4. Then re-disable the entry in Task Manager to catch any already-created autostart.

The in-app setting is the root control: as long as it is on, the app will re-create whatever startup entry you delete on its next launch or update. This is the step people miss, and it is why "I disabled it but it came back" is such a common complaint. Fix it at the source and the resurrection stops.

### Fix 6: Review autostart services

1. Press `Win + R`, type `services.msc`, and sort by Startup Type.
2. Look at third-party services set to Automatic — updaters, "helpers," and vendor services.
3. For non-essential ones, set Startup type to **Manual** (not Disabled — Manual lets the app start its service on demand).
4. Never change Microsoft services or hardware services (audio, networking, security) unless you know exactly why.

Services are the heaviest form of autostart because they start before login and run with system privileges. Setting third-party services to Manual is the safe middle ground: the service still works when its app needs it, but it no longer consumes boot time and idle resources. When in doubt, research the specific service name before changing it.

### Fix 7: Measure the improvement and maintain it

1. Before-and-after: time from power button to usable desktop with a stopwatch.
2. Check Task Manager's Performance tab for "Last BIOS time" as a firmware-side metric.
3. Re-audit startup quarterly — installers will keep trying to add entries.
4. When installing new software, choose Custom setup and decline autostart options.

Maintenance beats one-time heroics. A quarterly two-minute audit keeps boot fast permanently, and declining autostart during installs prevents most accumulation. If your laptop is slow beyond boot times, our [Windows 11 speed-up guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/) (principles apply to Windows 10) and [TiWorker troubleshooting](/articles/how-to-fix-tiworker-high-cpu-on-hp-laptop/) cover the other common drags.

## Closing

Slow boots are almost always a startup pileup, not aging hardware. Task Manager's Startup tab handles the bulk, the Startup folders and Task Scheduler catch the hiders, and in-app settings stop the resurrection cycle. Audit once thoroughly, then spend two minutes quarterly keeping it clean — your laptop will boot like it did on day one, and stay that way.
