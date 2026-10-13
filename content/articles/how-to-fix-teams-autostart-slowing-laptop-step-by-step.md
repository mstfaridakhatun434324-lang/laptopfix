---
title: "Stop Microsoft Teams Autostart From Slowing Down Your Laptop"
slug: "how-to-fix-teams-autostart-slowing-laptop-step-by-step"
date: "2026-09-08"
categories: ["performance"]
tags: ["teams autostart", "microsoft teams", "slow startup", "windows 11", "startup apps"]
description: "Microsoft Teams launching at every boot and dragging your laptop down? Follow this step-by-step guide to stop Teams autostart for good."
thumbnail: "/images/thumbs/how-to-fix-teams-autostart-slowing-laptop-step-by-step.webp"
faqs:
  - q: "Why does Microsoft Teams slow down my laptop at startup?"
    a: "Teams is built on Electron/Chromium, so launching it is like opening a second web browser — it consumes hundreds of megabytes of RAM and significant CPU while it signs in, syncs chats, and checks for updates. When it autostarts alongside everything else, it competes for disk and CPU during the most congested seconds of the boot, stretching a 30-second startup into minutes."
  - q: "Will disabling Teams autostart break anything?"
    a: "No. Disabling autostart only stops Teams from launching at login; the app works identically when you open it manually. You will still receive calls and messages once it is running. The only change is that Teams will not consume resources until you actually need it."
  - q: "Why does Teams keep re-enabling autostart after I turn it off?"
    a: "Teams has multiple autostart mechanisms — its in-app setting, a Task Manager startup entry, and sometimes a scheduled task or registry key. Disabling only one leaves the others active. Updates to Teams can also re-enable the in-app setting, which is why this guide covers all of them."
  - q: "Is the new Teams better for startup performance than classic Teams?"
    a: "Yes, noticeably. The rebuilt Teams client uses roughly half the memory of the classic Electron version and launches faster. If you are still on classic Teams, updating to the new client reduces the autostart penalty even if you leave autostart enabled — though disabling it remains the best option."
---

Microsoft Teams has a well-earned reputation as a startup hog. It installs itself aggressively — sometimes without being asked, via Office or Windows updates — enables autostart by default, and then consumes a shocking amount of resources every time you log in. On a laptop with 8 GB of RAM and a spinning drive, Teams autostarting can easily double the time before the machine is usable.

The frustration compounds because Teams is stubborn: turn off autostart in one place and it comes back via another. The app maintains its launch behavior through at least three independent mechanisms, and updates periodically reset your preference. A one-toggle fix does not stick. This guide walks through every autostart path in order, so Teams stays off until you deliberately open it.

Note that there are now two Teams clients in the wild: the classic Electron-based Teams and the rebuilt new Teams. The steps below cover both, and I will flag where they differ.

## Why this happens

- **Autostart enabled by default:** Teams opts you into "Auto-start Teams" during setup with no meaningful consent prompt.
- **Heavy Electron/Chromium runtime:** Classic Teams launches an entire browser engine, consuming 300–500 MB of RAM before you do anything.
- **Multiple autostart mechanisms:** In-app setting, Task Manager startup entry, scheduled tasks, and registry Run keys can each launch it independently.
- **Updates reset the preference:** Teams and Office updates periodically re-enable autostart even after you disabled it.
- **Pre-installed by Windows/Office:** Many laptops get Teams pushed via Windows Update or Microsoft 365 installs without the user ever opening it.
- **Background sync on launch:** On startup Teams signs in, syncs chat history, and checks for updates simultaneously — a burst of CPU, disk, and network.
- **Competing with other startup apps:** Teams launches in the same congested window as antivirus, cloud sync, and updaters, multiplying everyone's delay.
- **Two clients installed at once:** Some systems end up with both classic and new Teams autostarting, doubling the penalty.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure Teams' actual startup impact

Before changing anything, quantify the problem so you can verify the fix later. Open Task Manager's **Startup apps** tab and check Teams' startup impact rating — it is frequently rated **High**. Then restart, time how long until the desktop is responsive, and note Teams' RAM usage in the Processes tab once it loads. This baseline turns "it feels faster" into a number. If Teams is not listed in Startup apps but still launches, skip to Fix 4 — a scheduled task or registry key is the mechanism.

1. Open Task Manager (**Ctrl + Shift + Esc**) and go to **Startup apps**.
2. Find **Microsoft Teams** and note its **Startup impact** rating.
3. Restart, time boot-to-usable, and note Teams' memory in Processes.
4. Write these numbers down for later comparison.

### Fix 2: Disable autostart inside Teams settings

The in-app setting is the primary switch and the one updates most often reset. Open Teams, go to Settings > General, and uncheck **Auto-start Teams**. In new Teams the path is Settings > General > **Open application in background** and **Auto-start** toggles — disable both. This stops the sanctioned launch path. Do not stop here: verify with the next fixes that no secondary mechanism remains, because this toggle alone is the fix that famously "doesn't stick."

1. Open Teams and click **Settings** (gear icon or ••• menu).
2. Go to **General** and uncheck **Auto-start Teams**.
3. In new Teams, also disable **Open application in background**.
4. Close Teams completely (right-click tray icon > Quit).

### Fix 3: Disable the Teams entry in Task Manager Startup

Windows tracks Teams as a startup app independently of the in-app setting. Even with auto-start unchecked inside Teams, this entry can launch it. Open Task Manager's **Startup apps** tab, find Microsoft Teams, and set it to **Disabled**. This is a separate switch from Fix 2 — both must be off. While you are here, audit the rest of the list: every disabled startup app shortens boot time, and our [startup disk usage guide](/articles/how-to-fix-windows-11-high-disk-usage-on-startup-on-lenovo-laptop/) covers the broader cleanup.

1. In Task Manager, open the **Startup apps** tab.
2. Right-click **Microsoft Teams** and choose **Disable**.
3. If two Teams entries appear (classic + new), disable both.
4. Restart and confirm Teams no longer launches.

### Fix 4: Remove Teams scheduled tasks and registry Run entries

If Teams still appears after Fixes 2 and 3, a scheduled task or registry Run key is launching it. Open Task Scheduler and check the Task Scheduler Library for Teams-related update/login tasks — the updater task sometimes triggers a launch. Then check the registry Run keys for both the current user and local machine. Delete only entries that clearly reference Teams; leave everything else alone.

1. Press **Win + R**, type `taskschd.msc`, and press Enter.
2. Look for Teams entries under **Task Scheduler Library**; disable login-triggered ones.
3. Open regedit and check `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for Teams values.
4. Delete the Teams value (export the key first as backup).

### Fix 5: Uninstall Teams if you never use it

The most decisive fix for a Teams you did not choose: remove it. Many laptops carry Teams purely because Office or Windows Update installed it, and if your work or school does not require it, uninstalling eliminates the autostart problem permanently — along with its background update service. Use **Settings > Apps > Installed apps**, and remove both "Microsoft Teams" and "Teams Machine-Wide Installer" if present. You can always reinstall from Microsoft's site later.

1. Open **Settings > Apps > Installed apps**.
2. Uninstall **Microsoft Teams** (and **Teams Machine-Wide Installer** if listed).
3. Restart and verify no Teams processes or startup entries remain.
4. Reinstall manually later only if you actually need it.

### Fix 6: Switch to the new Teams client

If you must keep Teams, make it cheaper. The rebuilt Teams client launches faster and uses roughly half the memory of classic Teams, so even with autostart enabled the penalty shrinks dramatically. Check for the "Try the new Teams" toggle in the classic client, or download it fresh. After switching, re-apply Fixes 2 and 3, because the new client has its own autostart settings that default to on. Microsoft documents the new client rollout on the official [Windows support hub](https://support.microsoft.com/en-us/windows).

1. In classic Teams, toggle **Try the new Teams** (top-left) or download new Teams.
2. Verify the new client signs in and works for your meetings.
3. Uninstall the classic client to avoid double autostart.
4. Re-disable autostart in the new client's settings and Task Manager.

### Fix 7: Set a calendar reminder to re-check after updates

Teams updates have a habit of re-enabling autostart, so the durable fix includes a maintenance habit: after any Teams or Office update, glance at Task Manager's Startup tab. Better, make the check part of a monthly routine alongside the general startup audit. If Teams keeps resurrecting itself despite all fixes, the nuclear option is blocking it via the registry Run key permissions or AppLocker — but for most users, the five-minute monthly check is enough.

1. After each Teams/Office update, open Task Manager's **Startup apps** tab.
2. Confirm Teams is still **Disabled**; re-disable if it returned.
3. Re-check the in-app auto-start setting too.
4. Consider uninstalling if the pattern repeats and you rarely use Teams.

## Closing

Teams autostart is a solved problem once you address all of its launch paths instead of just the obvious toggle. Disable it in-app, disable it in Task Manager, clear the scheduled tasks, and — if you never asked for Teams in the first place — uninstall it outright. Pair this with our [startup high disk usage fix](/articles/best-way-to-fix-windows-11-high-disk-usage-on-startup/) for the full boot-time cleanup, and your mornings get faster every single day.
