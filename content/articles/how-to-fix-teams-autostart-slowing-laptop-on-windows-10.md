---
title: "Stop Teams From Slowing Down Your Windows 10 Laptop at Boot"
slug: how-to-fix-teams-autostart-slowing-laptop-on-windows-10
date: 2026-09-15
categories: ["performance"]
tags: ["teams autostart", "windows 10", "slow boot", "microsoft teams", "startup disable"]
description: "Teams hijacking every Windows 10 boot? Disable its autostart in the app, Task Manager, and registry — plus handle the classic Teams client."
thumbnail: "/images/thumbs/how-to-fix-teams-autostart-slowing-laptop-on-windows-10.webp"
faqs:
  - q: "How do I stop Teams from opening on startup in Windows 10?"
    a: "Uncheck 'Auto-start Teams' in Teams Settings, General; set Teams to Disabled in Task Manager's Startup tab; and delete its entry under HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run in the registry. All three are needed because Teams re-enables itself from any remaining entry."
  - q: "Does Teams slow down Windows 10 boot a lot?"
    a: "On older hardware, yes — the classic Teams client can add 30 to 60 seconds of heavy disk and CPU load at boot. On an SSD with a modern CPU it is more like 10 to 20 seconds of sluggishness. Either way, disabling autostart gives you a cleaner boot."
  - q: "What is the Teams Machine-Wide Installer?"
    a: "It is the installer IT departments use to deploy Teams to all users on a PC. It adds its own startup entry that reinstalls Teams per user at logon. If you see it in Task Manager startup, disable it too — otherwise Teams keeps resurrecting itself."
  - q: "Can I just uninstall Teams on Windows 10?"
    a: "On a personal machine, yes — remove it from Settings, Apps and it is gone, along with its startup entries. On a work laptop, check with IT first: they may require Teams, and the Machine-Wide Installer can reinstall it at next logon anyway. For work machines, disabling autostart is the safer path that IT will not override."
---

On Windows 10, Microsoft Teams is the classic uninvited boot guest. The old 'classic' Teams client is particularly heavy — a full Electron app that grabs CPU and disk the moment you log in, right when Windows is at its busiest. The result is a boot that feels twice as long as it should be, every single day.

Windows 10 users get an extra wrinkle: the Teams Machine-Wide Installer, which many workplaces deployed, adds its own startup entry that reinstalls and relaunches Teams per user. Disable one entry and the other brings it back. You have to find them all.

Here is the complete shutdown sequence for Teams autostart on Windows 10, including the machine-wide installer trap.

## Why this happens

- **Classic Teams client weight:** The old Electron client is far heavier at startup than the new Teams.

- **In-app autostart toggle:** Teams' own setting overrides Task Manager if left enabled.

- **Machine-Wide Installer entry:** The IT deployment tool re-registers Teams at every logon.

- **Registry Run keys:** Per-user and machine-wide Run entries relaunch Teams silently.

- **Startup folder shortcuts:** Legacy shortcuts that survive every other disable method.

- **Update and sync at logon:** Sign-in, chat sync, and update checks compound the boot load. The Windows 11 version of this fix is at [Teams autostart on Windows 11](/articles/how-to-fix-teams-autostart-slowing-laptop-on-windows-11/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off autostart inside Teams

The in-app toggle is the master switch. Everything else is secondary until this is off.

1. Open Microsoft Teams and click your profile picture.
2. Choose Settings, then General.
3. Uncheck 'Auto-start application'.
4. Uncheck 'On close, keep the application running' to prevent background lingering.
5. Right-click the Teams tray icon and choose Quit to fully exit.
6. Restart and check whether Teams appears.

### Fix 2: Disable all Teams entries in Task Manager

Windows 10 Task Manager often lists two Teams-related startup entries. Both must go.

1. Press Ctrl plus Shift plus Esc to open Task Manager.
2. Go to the Startup tab.
3. Right-click Microsoft Teams and choose Disable.
4. Find 'Teams Machine-Wide Installer' — right-click and Disable it too.
5. Check the Startup impact column to confirm both show Disabled.
6. Restart and verify.

### Fix 3: Clean the registry Run keys

Leftover Run values relaunch Teams even with the other switches off. This is the deep clean.

1. Press Win plus R, type `regedit`, and press Enter.
2. Go to HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run.
3. Delete any value pointing to Teams.
4. Go to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run and check there too.
5. Close regedit.
6. Restart and confirm no Teams process starts.

### Fix 4: Check the Startup folders

The old-school Startup folder is the last hiding place. A shortcut here beats every other setting.

1. Press Win plus R and type `shell:startup`, then press Enter.
2. Delete any Teams shortcut you find.
3. Repeat with `shell:common startup` for the all-users folder.
4. Restart the laptop.
5. Open Task Manager's Startup tab for a final review — it should be Teams-free.

### Fix 5: Replace classic Teams with the new client

If you need Teams running, the new client is dramatically lighter. On Windows 10 it is available as a separate install. See Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for the latest new-Teams system requirements on Windows 10.

1. Download the new Microsoft Teams client from Microsoft.
2. Install it and sign in.
3. Uninstall the classic Teams client via Settings, Apps.
4. Remove the Machine-Wide Installer too if IT policy allows.
5. Configure autostart preferences fresh in the new client.
6. Compare boot responsiveness — the improvement is usually dramatic.

### Fix 6: Measure the boot improvement

Verification matters: confirm the fix worked and quantify it so you know it was worth it.

1. Before the final restart, note your typical time from logon to responsive desktop.
2. After all fixes, restart and time it again.
3. Check Task Manager's Startup tab — the 'Last BIOS time' and startup impact list tell the story.
4. If boot is still slow, the culprit is elsewhere: see [how to disable startup programs in Windows 11](/articles/how-to-disable-startup-programs-windows-11/) for the general method, which applies equally to Windows 10.
5. Enjoy the faster mornings.

### Fix 7: Do a final Autoruns sweep

On Windows 10, Teams and its machine-wide installer hide autostart entries where Task Manager never looks — including scheduled tasks. Autoruns from Microsoft Sysinternals exposes every single one for a definitive cleanup.

1. Download Autoruns from Microsoft Sysinternals and run it as administrator.
2. Open the Logon tab and uncheck every Teams entry.
3. Open the Scheduled Tasks tab and uncheck Teams updaters.
4. Check the Services tab for Teams-related services and disable them.
5. Restart the laptop.
6. Verify in Task Manager's Startup tab that Teams is completely gone.

### Fix 8: Keep the new Teams client updated and lean

Once autostart is under control, keep it that way: an updated new-Teams client launches faster when you do open it, and a lean configuration prevents the settings from drifting back.

1. In the new Teams client, check Settings for the automatic update toggle and leave it on.
2. Revisit Teams Settings, General, every few months to confirm autostart is still off.
3. After major Teams updates, re-check Task Manager's Startup tab for re-added entries.
4. Remove the classic Teams client completely if it is still installed.
5. On shared machines, repeat the in-app disable for each user profile.

## Closing

Teams on Windows 10 hides its autostart in more places than most apps — the in-app toggle, two Task Manager entries, registry Run keys, and the Startup folder. Clear them all, consider the lighter new client, and your boot goes back to belonging to you.
