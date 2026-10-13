---
title: "How to Fix Windows Update Error 0x80070652 on a Dell Laptop"
slug: "how-to-fix-windows-update-error-0x80070652-on-dell-laptop"
date: 2026-09-25
categories: ["windows-update"]
tags: ["windows update", "0x80070652", "install already running", "dell laptop", "update error"]
description: "Error 0x80070652 means another installation is already running on your Dell laptop. Learn how to clear the stuck installer and finish the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070652-on-dell-laptop.webp"
faqs:
  - q: "What does error 0x80070652 mean?"
    a: >
      It means ERROR_INSTALL_ALREADY_RUNNING: Windows detected another
      installation already in progress and refused to start a second one.
      The other install may be visible or completely hidden in the
      background. Windows Installer allows only one MSI session at a time,
      so the second attempt is rejected outright. Finding and clearing the
      stuck or hidden installer resolves it.
  - q: "Can I just keep clicking retry?"
    a: >
      Sometimes that works if the other installer finishes on its own. But
      if the blocking process is hung — crashed and never exiting —
      retrying forever changes nothing, and you need to end the stuck
      process in Task Manager. Give it one restart and a few minutes
      first; if the error survives that, open Task Manager, look for
      leftover msiexec.exe or setup processes, and end them before
      retrying.
  - q: "Why does this happen on Dell laptops specifically?"
    a: >
      Dell ships background utilities like SupportAssist and Dell Update
      that install drivers and firmware automatically. When one of those
      runs at the same moment as Windows Update, the installer lock
      collides and one of them reports 0x80070652. It is not a Dell defect
      — any vendor’s background updater can cause it — but Dell’s tools
      are simply the ones most likely to be running on a Dell machine at
      update time.
  - q: "Is it safe to end msiexec.exe in Task Manager?"
    a: >
      Yes, if no installer window is visibly running. A healthy installer
      finishes and exits on its own; a leftover msiexec.exe with no window
      is a crashed process. Ending it releases the lock, and you can
      simply re-run the update.
---

Error 0x80070652 translates to ERROR_INSTALL_ALREADY_RUNNING — Windows believes another installation is in progress and refuses to start yours. Most often there genuinely is one: a background app installer, a Dell SupportAssist update, or a previous Windows Update session that never released its lock. The frustrating part is that the blocking installer is frequently invisible, with no window and no progress bar anywhere on screen.

On Dell laptops, the usual suspects are Dell’s own background updaters — SupportAssist, Dell Update, or Dell Command Update — installing a driver or firmware package at the same time Windows Update wants the machine. Office Click-to-Run updates and Microsoft Store app updates can also hold the installer lock. The fix is to identify and clear the stuck process, then let Windows Update run unopposed.

Start with the simplest interpretation: sometimes the ‘other installation’ is just Windows Update itself still finishing. But if the error persists across restarts, one of the fixes below will find and release the lock. If you are dealing with a related symptom instead, see [the similar 0x80240016 install-conflict error](/articles/how-to-fix-windows-update-error-0x80240016-on-dell-laptop/) and [Windows Update stuck while downloading](/articles/how-to-fix-windows-update-stuck-downloading-on-acer-laptop/).

The tricky part of this error is that the ‘other installation’ is often completely invisible — no window, no progress bar, nothing in the taskbar. That is why the fixes below are ordered as a hunt: first give any legitimate installer time to finish, then look for the stuck processes in Task Manager, then quiet Dell’s background updaters, and finally reset the update machinery itself. One of these layers is holding the lock, and the sequence finds it without you having to guess.

## Why this happens

- **Another installer holding the lock** only one MSI/Windows Installer session can run at a time.

- **Dell SupportAssist updating in the background** driver or BIOS staging can coincide with Windows Update.

- **Stuck msiexec.exe process** a crashed installer leaves its process running forever.

- **Office Click-to-Run updating** Office background updates use the same installer service.

- **Microsoft Store app updates** store updates can queue behind or ahead of system updates.

- **Pending restart from an earlier install** Windows waits for a reboot that never happened.

- **Corrupt installer service state** the Windows Installer service itself is wedged.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait and restart, then retry

The blocking install may simply need a few minutes. A clean restart clears transient locks. One genuine restart resolves a surprising share of these cases, because the blocking installer was real and simply needed a few more minutes to finish.

1. Save your work and restart the laptop normally.

2. After signing in, wait 5–10 minutes for background installers to finish.

3. Open Settings > Windows Update and click Retry.

4. If 0x80070652 persists, continue to the next fix.

### Fix 2: End stuck installer processes in Task Manager

A hung msiexec.exe or setup process is the most common real cause. Sort Task Manager’s Details tab by CPU or disk to spot the stuck installer quickly — a healthy setup process finishes and exits on its own.

1. Press Ctrl + Shift + Esc to open Task Manager.

2. Go to the Details tab and sort by Name.

3. Look for msiexec.exe, setup.exe, or Dell update processes using CPU or disk.

4. Right-click each and choose End task.

5. Retry Windows Update immediately.

### Fix 3: Pause Dell background updaters temporarily

Dell’s utilities are helpful, but they should not race Windows Update. You are not removing these utilities, only pausing them for one update cycle; re-enable everything once Windows Update completes successfully.

1. Open Dell SupportAssist or Dell Command Update.

2. Pause automatic scans and updates, or close the app entirely.

3. Also check Task Manager for DellClientManagementService and stop it temporarily.

4. Run Windows Update to completion, then re-enable Dell updates.

### Fix 4: Restart the Windows Installer service

If the service itself is wedged, restarting it releases the phantom lock. If the service refuses to restart, reboot and try again before assuming deeper damage — services sometimes need a clean boot to release their state.

1. Press Win + R, type services.msc, and press Enter.

2. Find ‘Windows Installer’ in the list.

3. Right-click it and choose Restart (or Start if it is stopped).

4. Also restart the ‘Windows Update’ service.

5. Retry the update.

### Fix 5: Perform a clean boot to isolate the conflict

A clean boot starts Windows with only Microsoft services, exposing any third-party installer hogging the lock. Keep notes on which services you disabled so re-enabling them afterward takes a minute instead of becoming a second troubleshooting project.

1. Press Win + R, type msconfig, and press Enter.

2. On the Services tab, check ‘Hide all Microsoft services’, then click Disable all.

3. On the Startup tab, click Open Task Manager and disable all startup items.

4. Restart, then run Windows Update.

5. Re-enable services afterward via msconfig.

### Fix 6: Clear pending install state in the registry (careful)

Leftover InProgress markers can convince Windows an install is still running. Export the registry key before deleting anything, and only remove InProgress when you are certain no installer window is actually running.

1. Back up the registry first (File > Export in regedit).

2. Press Win + R, type regedit, and navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer.

3. Look for an ‘InProgress’ key — if present and no installer is visibly running, delete it.

4. Restart the laptop and retry Windows Update.

### Fix 7: Reset Windows Update components

When the update engine itself is confused about state, a full component reset clears it. This is the deepest non-destructive reset available: it clears the update engine’s memory of the phantom ‘installation in progress’ without touching your files.

1. Open Command Prompt as administrator.

2. Stop the services: net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver.

3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old.

4. Restart the four services with net start.

5. Retry the update.

## Closing

Error 0x80070652 is a traffic jam, not a breakdown: two installers wanted the same road. Finding the stuck process — usually a background Dell updater or a hung msiexec — and clearing it lets Windows Update through on the next attempt. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
