---
title: "Fix Windows Update Error 0x80070652 on Windows 11 (Another Install Running)"
slug: how-to-fix-windows-update-error-0x80070652-on-windows-11
date: 2026-09-23
categories: ["windows-update"]
tags: ["windows update", "0x80070652", "windows installer", "msiexec", "windows 11"]
description: "Error 0x80070652 means another installation is already in progress on Windows 11. Clear the stuck installer and let your updates finish."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070652-on-windows-11.webp"
faqs:
  - q: "What does 'another installation is already in progress' mean?"
    a: "On Windows 11, it means the Windows Installer engine (msiexec) can only run one installation at a time, and something else claimed it first — a background program updater, a Store app update, or a hung setup process. Error 0x80070652 is Windows Update being turned away at the door. Waiting, restarting, or ending the stuck process frees the engine."
  - q: "How do I know if the other installer is stuck or just slow?"
    a: "Watch it in Task Manager for five to ten minutes: a working installer shows changing CPU, disk, or memory activity, while a stuck one sits at zero indefinitely with no progress. Slow deserves patience; stuck deserves End task. When in doubt, a restart safely resolves both without you having to decide."
  - q: "Can two Windows Updates install at the same time?"
    a: "No — and that is by design. The servicing stack serializes installations to prevent two updates from modifying the same system files simultaneously, which would corrupt the component store. Error 0x80070652 is that serialization doing its job. Let the first operation finish completely before starting the second."
  - q: "Will ending msiexec harm my system?"
    a: "Ending a genuinely hung msiexec process is safe — it was never going to complete. The risk is ending a healthy installer mid-flight, which can leave that program half-installed. That is why the guide has you watch for activity first and restart before resorting to End task. If you do interrupt a healthy install, simply reinstall that program afterward."
---
Error 0x80070652 is Windows Installer's traffic cop holding up a stop sign: ERROR_INSTALL_ALREADY_RUNNING. Only one Windows Installer session can run at a time, and something — a program's background updater, a Store app, a hung setup — is already using the engine when Windows Update tries to start its own installation. On Windows 11 laptops this commonly happens when OEM utilities and app updaters fire at the same time as Patch Tuesday.

The fix is about the queue, not the update: find what is holding the installer, let it finish or clear it out, and then give Windows Update its turn. Most cases resolve with patience or a restart; the stubborn ones need the stuck process ended by hand.

If your other PC shows the same collision, the [Windows 10 guide](/articles/how-to-fix-windows-update-error-0x80070652-on-windows-10/) covers Windows 10, and when the competing process is a file lock rather than an installer, the [companion guide for 0x80070020](/articles/how-to-fix-windows-update-error-0x80070020-on-windows-11/) is the related guide. Start with the simplest move: wait.

## Why this happens

- **A program is installing or updating in the background:** OEM utilities, game launchers, and app updaters routinely run silent MSI installations. If one is active when Windows Update starts its own, the second one is refused with 0x80070652.
- **A previous installer hung and never released the engine:** A crashed or frozen setup can leave msiexec.exe running indefinitely, holding the single-installer lock forever and failing every subsequent installation with this code.
- **Store apps are updating simultaneously:** Microsoft Store app updates use the same installer infrastructure on some packages, and a Store update storm after a fresh boot can collide with Windows Update.
- **Windows Update is installing while you install software:** The collision works both ways: starting a program's installer manually while Windows Update is mid-install produces the same error from the other direction.
- **A scheduled task triggered an installer:** OEM and third-party scheduled tasks — driver updaters, support assistants — launch installers on their own timers, sometimes exactly when you are trying to update.
- **The installer service is wedged from an interrupted session:** A force-shutdown during an installation can leave the Windows Installer service believing a session is still active, blocking all new ones until the service restarts.
- **Corrupted installer registration confuses the queue:** Damaged Windows Installer registration can make the engine report busy when nothing is actually installing, a rarer but real cause of persistent 0x80070652.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait ten minutes, then retry

The most underused fix in troubleshooting: a legitimate background installation usually finishes within minutes, and retrying after a short wait succeeds with zero intervention. Many 0x80070652 reports are simply two installers politely colliding, and patience is the entire cure.

1. Note the current time and stop starting new installations.
2. Open Task Manager and watch for installer or updater processes showing CPU or disk activity.
3. Wait ten full minutes without launching anything new.
4. Open Settings > Windows Update and click Retry on the failed update.
5. If it succeeds, the collision was legitimate — no further action needed.

### Fix 2: Restart to clear the installer queue

A restart ends every installer session — healthy, hung, or wedged — and resets the Windows Installer service to a clean idle state. This is the definitive fix for stuck msiexec processes and the fastest way to resolve 0x80070652 when waiting did not help.

1. Save your work and close open programs.
2. Click Start > Power > Restart.
3. After logging in, wait three minutes for startup installers and Store updates to settle.
4. Open Settings > Windows Update and retry the failed update.
5. If the error is gone, the queue was holding a stuck session.

### Fix 3: End the stuck msiexec process manually

When a restart is inconvenient or the stuck installer returns, end it directly: Task Manager shows every msiexec.exe instance, and ending a genuinely hung one releases the installer lock immediately. A healthy installer shows activity; a stuck one sits at zero CPU indefinitely.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Go to the Details tab and sort by Name.
3. Right-click each `msiexec.exe` entry and choose End task.
4. Also end any hung setup.exe or installer processes from third-party programs.
5. Retry the update in Settings > Windows Update immediately.

### Fix 4: Restart the Windows Installer service

If no msiexec process is visible but the engine still claims to be busy, the service itself is wedged. Restarting the Windows Installer service (msiserver) resets its internal session tracking without a reboot, which clears phantom busy states.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find Windows Installer in the list.
3. Right-click it and choose Restart (or Start, if it shows as stopped).
4. If it will not restart, reboot the laptop instead.
5. Retry the update once the service shows as running cleanly.

### Fix 5: Pause Store app updates during Windows Update

Microsoft Store updates are a frequent silent collider: after boot or on a schedule, the Store updates all your apps at once, grabbing the installer engine for an extended period. Pausing Store updates while Windows Update runs removes the competition entirely.

1. Open the Microsoft Store app.
2. Click your profile icon > Settings and turn off App updates temporarily.
3. Alternatively, open Store > Library and pause any in-progress app updates.
4. Run Windows Update from Settings > Windows Update to completion.
5. Re-enable Store app updates afterward and let them finish in their own time.

### Fix 6: Re-register the Windows Installer engine

For the stubborn cases where the engine reports busy with nothing running, re-registering msiexec rebuilds its COM registration and clears corrupted queue state. The unregister/re-register pair is a classic technician fix for installer-service weirdness.

1. Open Command Prompt as administrator.
2. Run `msiexec /unregister` and wait for it to return silently.
3. Run `msiexec /regserver` and wait again.
4. Restart the laptop to let the fresh registration take effect.
5. Retry the update; if it still claims busy, see Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for deeper servicing diagnostics.

### Fix 7: Stagger scheduled updaters that keep colliding

If 0x80070652 recurs on a schedule — every Patch Tuesday, every boot — the collision is structural: an OEM updater or Store refresh is programmed to run at the same time as Windows Update. Rather than fighting each occurrence, reschedule the third-party updater or pause Store auto-updates during your maintenance window so the two never compete.

1. Press Win + R, type `taskschd.msc`, and press Enter.
2. Browse the Task Scheduler Library for updater tasks from your PC maker or third-party vendors.
3. Right-click a colliding task, choose Properties, and move its trigger to a time you never update (or disable it if you update drivers manually).
4. In the Microsoft Store, pause automatic app updates while Windows Update runs.
5. Retry the update in Settings > Windows Update and confirm the collision no longer occurs.

## Closing

Error 0x80070652 is a scheduling conflict, not a system failure: something is using the installer and Windows Update has to wait its turn. Patience, a restart, or ending the stuck msiexec resolves nearly every case on Windows 11. If collisions keep happening at the same time each month, stagger your schedules — let Windows Update finish before launching big app installs — and the traffic jam stops forming.
