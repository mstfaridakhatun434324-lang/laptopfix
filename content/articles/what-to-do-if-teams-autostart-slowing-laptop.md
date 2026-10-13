---
title: "What to Do If Microsoft Teams Autostart Is Slowing Your Laptop"
slug: "what-to-do-if-teams-autostart-slowing-laptop"
date: "2026-09-14"
categories: ["performance"]
tags: ["teams autostart", "startup apps", "microsoft teams", "windows 11"]
description: "Teams launching at every boot and slowing your laptop? Stop Teams autostart properly across all its startup hooks."
thumbnail: "/images/thumbs/what-to-do-if-teams-autostart-slowing-laptop.webp"
faqs:
  - q: "Why does Teams keep re-enabling itself at startup?"
    a: "Teams registers in multiple startup locations: the Windows Startup apps list, its own in-app auto-start setting, and sometimes a scheduled task. Disabling only one of them lets the others resurrect it. The reliable approach is to turn off auto-start inside Teams settings, disable it in Task Manager's Startup apps tab, and check the Startup folder, covering all three hooks."
  - q: "Does Teams use resources when I am not in a meeting?"
    a: "Yes. Even idle, the Teams client maintains its connection, syncs chats, checks calendar, and in the new Teams version runs several background processes. Typical idle usage is 200 to 500 MB of RAM and periodic CPU spikes. On laptops with 8 GB of RAM or less, that footprint is significant enough to slow everything else at boot."
  - q: "Should I use the new Teams or Teams classic?"
    a: "Microsoft has replaced Teams classic with the new Teams client, which is genuinely lighter and faster to launch. If you are still on the classic client, switching to the new Teams reduces both startup impact and idle resource usage. The classic client is deprecated, so migrating also avoids future compatibility problems."
  - q: "Will disabling Teams autostart affect meeting notifications?"
    a: "You will not get meeting reminders until you actually launch Teams. If you depend on pop-up reminders, keep autostart on but mitigate its impact by delaying launch or closing it after boot. Alternatively, use the Outlook calendar reminders as your meeting nudge and launch Teams manually a few minutes before calls."
---

Microsoft Teams is one of the heaviest autostart offenders on Windows laptops. It launches at every boot, loads its chat sync, calendar integration, and background services, and typically consumes 200 to 500 MB of RAM before you have even opened a single app yourself. On an 8 GB laptop, that is a meaningful chunk of memory gone before your workday starts.

Worse, Teams is stubborn. Many users disable it in Task Manager only to find it back the next morning, because Teams registers itself in several startup locations at once: its own settings, the Windows Startup apps list, and occasionally a scheduled task. Killing just one hook is like pulling one weed root and leaving the rest.

This guide covers every hook: the in-app setting, Task Manager, the Startup folder, and the new Teams client's lighter behavior. Follow all the steps and Teams will stay off until you deliberately launch it.

## Why this happens

- **Multiple startup registrations:** Teams hooks itself into several autostart locations, so disabling one leaves the others active.
- **In-app auto-start enabled by default:** Fresh installs enable Start Teams on startup without asking clearly.
- **Heavy client initialization:** Chat sync, calendar fetch, and background services all run at launch, hammering CPU and disk.
- **New Teams background processes:** Even the lighter new client keeps updater and notification helpers running.
- **Startup boost-style preloading:** Related Microsoft 365 components preload alongside Teams at login.
- **Large chat history syncing:** Accounts with years of chat history spend minutes syncing at every launch.
- **GPU acceleration in the client:** Teams uses GPU compositing, adding load on integrated graphics at boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off auto-start inside Teams

The in-app setting is the master switch. If this stays on, Teams will fight every other method you try.

1. Open Microsoft Teams.
2. Click the three dots or your profile picture, then Settings.
3. Under General, uncheck Auto-start Teams or Start Teams on startup.
4. Also uncheck Open application in background if present.
5. Close Teams completely, then restart to test.

### Fix 2: Disable Teams in Task Manager Startup apps

This covers the Windows-level registration that survives the in-app toggle on some installs.

1. Press Ctrl+Shift+Esc to open Task Manager.
2. Open the Startup apps tab.
3. Find Microsoft Teams in the list and check its Startup impact rating.
4. Right-click it and choose Disable.
5. Restart and confirm Teams no longer appears after login.

### Fix 3: Check the Startup folder and scheduled tasks

Some installs drop a shortcut in the Startup folder or create a scheduled task. Check both for completeness.

1. Press Win+R, type shell:startup, and press Enter.
2. Delete any Teams shortcut you find there.
3. Press Win+R, type taskschd.msc, and press Enter.
4. Look under Task Scheduler Library for Teams-related update or launch tasks.
5. Disable any task that launches the Teams client itself at logon.

### Fix 4: Switch to the new Teams client

If you are still on Teams classic, the new client launches faster and idles lighter. Migration is worth it even if you keep autostart on.

1. Open Teams classic and look for the Try the new Teams toggle at the top.
2. Enable it and let the new client install.
3. Verify your chats, teams, and calendar carried over.
4. Uninstall Teams classic from Settings, Apps afterward.
5. Re-apply the autostart-off settings in the new client.

### Fix 5: Delay launch instead of blocking it

If you need Teams reminders but hate the boot hit, a delayed launch gives you the best of both: fast boot, Teams a few minutes later.

1. Keep autostart disabled using the steps above.
2. Open Task Scheduler with taskschd.msc.
3. Create a basic task that launches Teams five minutes after logon.
4. Set the trigger to At log on with a five-minute delay.
5. This spreads the startup load instead of stacking it.

### Fix 6: Reduce Teams resource usage when it runs

For times you do run Teams, these settings keep its footprint smaller, which matters on 8 GB machines.

1. In Teams Settings, General, disable GPU hardware acceleration if the client feels heavy.
2. Turn off read receipts and large gallery views you do not need.
3. Close Teams fully after meetings instead of minimizing it to the tray.
4. On very constrained laptops, use Teams in the browser for light chat days.
5. Monitor total RAM in Task Manager to confirm the savings.

### Fix 7: Use Teams on the web for light days

On days with no heavy meetings, the browser version of Teams gives you chat and light calls without the desktop client's memory footprint or autostart hooks.

1. Open teams.microsoft.com in Edge or Chrome and sign in.
2. Pin the tab so it is always one click away.
3. Use it for chat-heavy days and reserve the desktop app for video meetings.
4. Compare Task Manager memory with the desktop client closed.
5. Many users find the web version covers 80 percent of their Teams needs.

### Fix 8: Use Teams on the web for light days

On days with no heavy meetings, the browser version of Teams gives you chat and light calls without the desktop client's memory footprint or autostart hooks.

1. Open teams.microsoft.com in Edge or Chrome and sign in.
2. Pin the tab so it is always one click away.
3. Use it for chat-heavy days and reserve the desktop app for video meetings.
4. Compare Task Manager memory with the desktop client closed.
5. Many users find the web version covers 80 percent of their Teams needs.

## Closing

Teams autostart is a multi-headed problem, which is why single fixes seem to fail: you have to disable the in-app setting, the Task Manager entry, and any Startup folder shortcut together. Once all three are off, boot times and idle memory usage improve immediately. If your laptop is still slow to settle after login, the remaining culprits are usually other startup programs, covered in our guide to [disabling startup apps on Windows 11](/articles/how-to-disable-startup-apps-on-windows-11/). If boot is still slow with Teams fully tamed, the remaining startup load is covered in our [Teams autostart deep dive](/articles/how-do-i-fix-teams-autostart-slowing-laptop/), and Microsoft documents startup management in its [Windows support hub](https://support.microsoft.com/en-us/windows). If boot is still slow with Teams fully tamed, the remaining startup load is covered in our [Teams autostart deep dive](/articles/how-do-i-fix-teams-autostart-slowing-laptop/), and Microsoft documents startup management in its [Windows support hub](https://support.microsoft.com/en-us/windows). Give each change a full reboot to verify, since Teams re-registers itself aggressively after updates.
