---
title: "The Best Way to Stop Teams Autostart From Slowing Your Laptop"
slug: best-way-to-fix-teams-autostart-slowing-laptop
date: 2026-09-03
categories: ["performance"]
tags: ["teams autostart", "slow boot", "startup", "microsoft teams", "performance"]
description: "Microsoft Teams launching at every boot and slowing your laptop? Learn the best way to stop Teams autostart without breaking it for meetings."
thumbnail: "/images/thumbs/best-way-to-fix-teams-autostart-slowing-laptop.webp"
faqs:
  - q: "Why does Microsoft Teams slow down my laptop at startup?"
    a: "Teams is an Electron/WebView2 app that loads a full browser engine, signs you in, syncs chats and files, and checks for updates — all during the most congested minutes after boot. On systems with 8 GB of RAM or a busy startup list, Teams alone can add 30 to 60 seconds before the laptop feels usable, and its background processes keep consuming memory all day."
  - q: "Will disabling Teams autostart break my meetings?"
    a: "No — disabling autostart only stops Teams from launching at boot. The app works perfectly when you open it manually, meeting links still launch Teams on demand, and notifications work once it's running. The only difference is that Teams isn't consuming resources during the hours you're not in a meeting."
  - q: "Why does Teams keep re-enabling itself at startup?"
    a: "Teams has multiple autostart mechanisms that fight each other: its own in-app auto-start setting, a Task Manager startup entry, a registry Run key, and sometimes an installer repair task. Disabling only one lets the others resurrect it — which is why people find Teams back at boot after 'disabling' it. You need to turn off all of them, as this guide shows."
  - q: "Should I uninstall Teams if I rarely use it?"
    a: "If you genuinely never use it, yes — uninstalling is cleaner than disabling. But check which Teams you have first: the personal 'Microsoft Teams' and work/school Teams are separate apps, and some workflows (like meeting links from certain organizations) expect one of them. If there's any chance you'll need it, disabling autostart keeps it available without the daily cost."
---

Microsoft Teams has a superpower nobody asked for: resurrecting itself at every boot. You disable it in one place, and it's back the next morning — because Teams maintains half a dozen autostart mechanisms, and they cover for each other. Meanwhile it's one of the heaviest startup apps on Windows, loading a full web engine and syncing everything while your laptop is still trying to wake up.

The best approach isn't a single toggle — it's a layered shutdown of every autostart path, in the right order, so Teams stays off until you actually need it. For the diagnostic walkthrough, see [troubleshooting Teams autostart](/articles/teams-autostart-slowing-laptop-troubleshooting/); for the Windows 11 24H2 variant, our [Teams autostart on 24H2 guide](/articles/how-to-fix-teams-autostart-slowing-laptop-in-windows-11-24h2/).

## Why this happens

- **Multiple autostart mechanisms**: In-app setting, Task Manager entry, registry Run key, and scheduled tasks back each other up.
- **Heavy Electron/WebView2 runtime**: Teams loads a full browser engine at boot — expensive on 8 GB machines.
- **Sign-in and sync storm**: Authentication, chat sync, file sync, and update checks all fire simultaneously.
- **Self-repair behavior**: Teams' installer routinely "repairs" its startup entries during updates.
- **Two Teams apps**: Personal and work/school Teams are separate installs, each with its own autostart.
- **Update-time re-enabling**: Teams updates frequently reset the auto-start preference.
- **Background persistence**: Even "closed," Teams often keeps running in the notification area.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off auto-start inside Teams itself

Start with the app's own setting — it's the one most people miss.

1. Open **Teams**, click your profile picture (or the **...** menu) > **Settings** > **General**.
2. Uncheck **Auto-start Teams** (wording varies: "Open application in background," "On close, keep the application running").
3. Also uncheck **On close, keep the application running** — otherwise closing the window just hides it in the tray.
4. In the new Teams, check **Settings** > **General** for **Auto-start** and any **Register Teams as the chat app** options and disable those too.
5. Fully quit Teams afterward (**right-click the tray icon** > **Quit**) — changing the setting while it runs sometimes doesn't persist. Verify in Task Manager that no Teams processes remain.

### Fix 2: Disable the Task Manager startup entry

The layer most guides stop at (but you shouldn't).

1. Open **Task Manager** > **Startup apps** and find **Microsoft Teams** (there may be two entries — personal and work/school).
2. Right-click each and choose **Disable**.
3. Check the **Startup impact** column — Teams is usually rated **High**, confirming it was a major boot cost.
4. Restart and verify Teams doesn't appear — if it does, one of the deeper mechanisms (Fixes 3–4) is resurrecting it.
5. Re-check this list after every Teams update — updates are the number one cause of mysteriously re-enabled startup entries.

### Fix 3: Remove the registry Run entries

The persistence layer that survives Task Manager disables.

1. Press **Win+R**, type `regedit`, and navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`.
2. Look for values like **com.squirrel.Teams.Teams** (classic Teams) or Teams-related entries — right-click and delete them.
3. Also check `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` for machine-wide Teams entries (you'll need admin rights).
4. Check `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run` — entries here track the "disabled" state; stale data can confuse Windows into re-enabling.
5. Reboot and verify — registry-level removal is what finally stops the resurrection cycle for most people. Our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) covers the general technique.

### Fix 4: Disable Teams' scheduled tasks

The updater's back door.

1. Open **Task Scheduler** (`taskschd.msc`) and look under **Task Scheduler Library** for Teams-related tasks (Microsoft Teams update tasks, "TeamsMachineInstaller" entries).
2. Right-click Teams update tasks > **Disable** — not delete, so you can re-enable if needed.
3. Be careful to disable only Teams' own tasks, not shared Microsoft update infrastructure you might want.
4. Note that Teams may recreate these on update — this is why Fix 5's approach matters for the long term.
5. Verify over two or three reboots — scheduled-task resurrection usually shows up within a few days, not immediately.

### Fix 5: Change how Teams updates itself

Stop the update cycle from undoing your work.

1. Understand the mechanism: Teams' per-user installer (Squirrel) checks for updates at launch and "repairs" its installation — including startup entries — during the process.
2. In Teams **Settings**, look for update-related options and set updates to manual if available.
3. For work/school Teams deployed by IT, talk to your administrator — they can control autostart via policy, which overrides everything you do locally.
4. Consider switching to the **Teams web app** for occasional use — no installer, no autostart, no background processes, and it handles meetings fine in Edge or Chrome.
5. If you rarely need Teams at all, uninstall it (**Settings** > **Apps** > **Installed apps**) — the web app remains as a fallback, and this is the only truly permanent solution.

### Fix 6: Measure the boot improvement

Confirm the payoff.

1. Before/after comparison: time from login to a responsive desktop with Teams autostarting vs. after these fixes — most people gain 30–60 seconds.
2. Check **Task Manager** > **Startup apps** > **Last BIOS time** and the startup impact list — with Teams gone, the next-heaviest entries become visible targets.
3. Monitor idle RAM: **Task Manager** > **Performance** > **Memory** — Teams' background processes typically hold several hundred MB even when idle.
4. Test meeting functionality: have someone send you a test meeting link and confirm Teams launches on demand and joins correctly.
5. Set a monthly reminder to re-check startup entries — Teams updates are persistent, and a 30-second monthly check beats a slow laptop. General boot optimization continues in our [slow laptop guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

### Fix 7: The nuclear option — replace or remove

When Teams and your laptop just can't coexist.

1. If you need Teams only for meetings, uninstall the desktop app and use meeting links in the browser — full meeting functionality, zero background cost.
2. If your organization mandates the desktop app, ask IT about the **VDI-optimized** or policy-controlled deployment, which behaves better.
3. Check whether you have *both* personal Teams and work Teams installed — removing the one you never use halves the autostart battle.
4. After uninstalling, verify the registry Run keys and scheduled tasks are actually gone — uninstallers sometimes leave them behind.
5. Microsoft's official Teams deployment and autostart documentation is on [Microsoft Support](https://support.microsoft.com/en-us/windows) — worth checking if IT policies are involved.

## Closing

Teams autostart is a hydra — cut off one head (the in-app setting) and the Task Manager entry, registry key, or scheduled task grows it back. Kill all of them in order, verify across reboots and updates, and your laptop boots to a usable desktop instead of a Teams loading screen. The app will still be there when a meeting invite arrives; it just won't be there at 8 AM when you're trying to check email.
