---
title: "Stop Microsoft Teams From Slowing Your Laptop at Startup (Windows 11)"
slug: how-to-fix-teams-autostart-slowing-laptop-on-windows-11
date: 2026-09-14
categories: ["performance"]
tags: ["teams autostart", "microsoft teams slow startup", "windows 11", "startup programs", "teams disable"]
description: "Teams launching at every boot and dragging your laptop down? Disable its autostart properly — in Teams, Task Manager, and the registry — for a faster boot."
thumbnail: "/images/thumbs/how-to-fix-teams-autostart-slowing-laptop-on-windows-11.webp"
faqs:
  - q: "Why does Teams slow down my laptop startup?"
    a: "Teams is a heavy Electron app that launches at boot, signs you in, syncs chats and files, and checks for updates — all while Windows is still starting other services. On older laptops this can add 30 to 60 seconds of sluggishness to every boot."
  - q: "If I disable Teams autostart, will I miss messages?"
    a: "No. Teams syncs everything the moment you open it, so no message is ever lost — you simply will not see notifications before launching the app. If instant alerts matter for your job, keep autostart but delay it by a few minutes with Task Scheduler instead. That gives you a fast boot and notifications shortly after."
  - q: "Why does Teams keep re-enabling autostart?"
    a: "Because Teams has its own in-app autostart toggle that operates independently of Task Manager — disabling it in one place while leaving the other on means it comes back. Some setups also hide entries in the registry Run keys or the Startup folder. You must turn off all of them: the in-app setting first, then Task Manager, then the registry."
  - q: "Is the new Teams faster than classic Teams?"
    a: "Noticeably. The new Teams client launches roughly twice as fast, uses significantly less memory, and puts less load on the disk at startup. If you are still on classic Teams — common on Windows 10 — upgrading is one of the highest-impact single changes for Teams-related slowdowns, whether or not you keep autostart enabled."
---

Microsoft Teams has a talent for making a fast laptop feel slow every single morning. It launches at boot — whether you asked it to or not — then spends the next minute signing in, syncing conversations, and checking for updates, all while you are trying to open your first app. On Windows 11, where Teams is woven into the system, it can feel impossible to stop.

The frustration compounds because Teams is sneaky about autostart: disable it in one place and it re-enables itself from another. Task Manager alone is not enough. You have to hit all three control points — the in-app setting, the Startup tab, and the registry entry it hides behind.

This guide covers all three, plus what to do when a work policy keeps turning it back on.

## Why this happens

- **In-app autostart setting:** Teams' own 'Auto-start Teams' toggle re-enables itself independently of Task Manager.

- **Heavy Electron client:** Teams loads a full browser engine at boot, which is expensive on older CPUs and spinning drives.

- **Sign-in and sync storm:** Authentication, chat sync, and file sync all fire simultaneously at startup.

- **Update checks at launch:** Teams checks for client updates on every start, adding network and disk load.

- **Multiple startup entries:** Teams can register in Task Manager, the Startup folder, and the registry simultaneously.

- **IT policy re-enabling it:** Work-managed devices may enforce autostart via group policy. Broader startup cleanup is in [how to disable startup programs in Windows 11](/articles/how-to-disable-startup-programs-windows-11/).

- **Classic Teams client:** The older client is dramatically heavier than the new Teams.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable autostart inside Teams first

This is the master switch. Skipping it is why Teams keeps coming back after Task Manager disables.

1. Open Microsoft Teams.
2. Click the three dots next to your profile picture, then Settings.
3. Go to General and uncheck 'Auto-start Teams'.
4. Also uncheck 'Open application in background' if present.
5. Close Teams completely — right-click its system tray icon and choose Quit.
6. Restart the laptop and check whether Teams launches.

### Fix 2: Disable Teams in Task Manager startup

The second control point. Both must be off for autostart to actually stop.

1. Open Task Manager with Ctrl plus Shift plus Esc.
2. Go to the Startup apps tab.
3. Find Microsoft Teams and set it to Disabled.
4. Look for any second Teams entry (updater or machine-wide installer) and disable it too.
5. Restart and verify Teams stays closed.

### Fix 3: Remove the registry autostart entry

Teams sometimes leaves a Run key that relaunches it. Removing it closes the third door.

1. Press Win plus R, type `regedit`, and press Enter.
2. Navigate to HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run.
3. Look for a Teams-related value and delete it.
4. Also check HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run for machine-wide entries.
5. Close the registry editor and restart.
6. Verify in Task Manager that no Teams process starts at boot.

### Fix 4: Upgrade to the new Teams client

If you must keep Teams autostarting for work, the new client makes it far less painful — faster launch, lower memory. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has deployment guidance for rolling out the new Teams client.

1. Open Teams and look for the 'Try the new Teams' toggle at the top.
2. Switch it on and let the new client install.
3. Alternatively, download the new Teams from the Microsoft Store.
4. Uninstall the classic Teams client afterward to avoid duplicates.
5. Re-apply your autostart preferences in the new client.
6. Measure boot time before and after — the difference is usually obvious.

### Fix 5: Delay Teams instead of disabling it

If work requires Teams running, a delayed start gives Windows time to finish booting first — most of the benefit, none of the missed messages.

1. Keep autostart enabled in Teams settings.
2. Download a free startup-delayer tool or use Task Scheduler.
3. In Task Scheduler, create a task that launches Teams 3 minutes after logon.
4. Disable the normal Teams startup entries so only the delayed task runs.
5. Test with a restart — the desktop should be responsive long before Teams appears.

### Fix 6: Handle IT-enforced autostart

On work laptops, group policy may force Teams to start. You need a different conversation, not a different toggle.

1. Check with your IT department whether Teams autostart is policy-enforced.
2. If it is, ask whether the new Teams client can be deployed — it is the approved fix.
3. Do not fight policy with registry hacks; they get reverted and can flag your device.
4. As a compromise, ask IT about the delayed-start approach.
5. For personal devices with the same symptom on Windows 10, see [Teams autostart on Windows 10](/articles/how-to-fix-teams-autostart-slowing-laptop-on-windows-10/).

### Fix 7: Audit hidden Teams entries with Autoruns

Teams is notorious for autostart entries in places Task Manager never shows. Autoruns from Microsoft Sysinternals lists every single one — Logon entries, scheduled tasks, services — for a definitive cleanup.

1. Download Autoruns from Microsoft Sysinternals and run it as administrator.
2. Open the Logon tab and look for Teams entries.
3. Uncheck every Teams-related entry you find.
4. Check the Scheduled Tasks tab for Teams updaters and uncheck those too.
5. Restart the laptop.
6. Confirm in Task Manager that no Teams process starts at boot.

## Closing

Teams autostart is a three-lock door — the in-app setting, Task Manager, and the registry — and you have to turn all three keys. Do that, or upgrade to the lighter new client, and your Windows 11 mornings get noticeably faster without missing a single message. Revisit these settings after Teams updates itself, since client updates sometimes restore the in-app autostart toggle. Your boot times will thank you.
