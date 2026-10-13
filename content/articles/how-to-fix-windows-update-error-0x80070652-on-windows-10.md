---
title: "Fix Windows Update Error 0x80070652 on Windows 10: Quick Solutions"
slug: how-to-fix-windows-update-error-0x80070652-on-windows-10
date: 2026-09-24
categories: ["windows-update"]
tags: ["windows update", "0x80070652", "windows installer", "msiexec", "windows 11"]
description: "On Windows 10, error 0x80070652 means another installer is already using the Windows Installer engine. Free the queue and get updates installing with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070652-on-windows-10.webp"
faqs:
  - q: "What does 'another installation is already in progress' mean?"
    a: "Windows 10's installer engine (msiexec) handles exactly one installation at a time. The message means something else claimed the engine first — a background app updater, a Store app refresh, or a frozen setup that never released it. Windows Update, arriving second, is refused with error 0x80070652. Waiting for the first job to finish, restarting, or ending the stuck process returns the engine."
  - q: "How do I know if the other installer is stuck or just slow?"
    a: "Observe it in Task Manager for five to ten minutes: a healthy installer shows moving CPU, disk, or memory figures, while a frozen one sits at zero with no change. Slowness deserves patience; a total standstill deserves End task. If you genuinely cannot tell, a restart settles both possibilities safely without requiring you to judge."
  - q: "Can two Windows Updates install at the same time?"
    a: "No, and the restriction is deliberate. The servicing stack installs updates sequentially so two of them never modify the same system files simultaneously, which could corrupt the component store. Error 0x80070652 is that ordering mechanism doing its job. Allow the first operation to finish completely before launching the second."
  - q: "Will ending msiexec harm my system?"
    a: "Terminating a genuinely frozen msiexec process is safe — it was never going to complete. The danger lies in stopping a healthy installer halfway, which can leave that application partially installed. That is why this guide has you check for activity first and prefer a restart. If you do interrupt a working install, simply install that program again afterward."
---
Windows 10 greets you with 0x80070652 when Windows Update tries to begin an installation while the Windows Installer engine is already claimed by something else. The engine — msiexec — handles one installation at a time, so a second installer arriving mid-job is politely refused, and that refusal surfaces as this error code.

Usually the squatter finishes quickly: a game launcher patching itself, a Store app refreshing, an OEM utility running its silent setup. The painful case is a setup process that froze and never released the engine, blocking every installation behind it indefinitely. Your first task is telling the two situations apart, and the fixes below move from the gentlest response to the most forceful so you never terminate a healthy installation by mistake.

For the same error on the newer OS, the [Windows 11 edition](/articles/how-to-fix-windows-update-error-0x80070652-on-windows-11/) has you covered, and the [file-lock sibling guide](/articles/how-to-fix-windows-update-error-0x80070020-on-windows-10/) addresses 0x80070020, this error's close relative. Begin by letting the current activity run its course.

## Why this happens

- **Something is installing quietly in the background:** game clients, OEM tools, and app auto-updaters frequently run MSI setups you never see. When Windows Update begins its own installation while one of these is active, the newcomer is rejected with 0x80070652.
- **A previous setup froze and kept the engine:** crashed or hung installers can leave msiexec.exe alive indefinitely, clutching the single-install lock and failing everything queued behind it.
- **Store app updates are racing Windows Update:** after a fresh boot, a wave of Microsoft Store app updates can grab the installer infrastructure at the same moment Windows Update wants it.
- **Two installers were started by hand:** the conflict runs both directions — launching a program's installer manually while Windows Update is mid-install triggers the identical refusal from the other side.
- **A scheduled task fired an updater:** manufacturer assistants and driver utilities launch installers on timers that sometimes land exactly on your update attempt.
- **An interrupted session left the service confused:** a forced shutdown during an install can leave the Windows Installer service believing a session is still live, vetoing all newcomers until it restarts.
- **The installer's registration is damaged:** less common, but corrupted engine registration can make Windows claim the installer is busy when nothing is actually running.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give the current installer ten minutes, then retry

When the blockage is legitimate, patience is the whole cure — but use the wait to confirm activity is genuinely winding down rather than frozen solid.

1. Note the time and refrain from launching anything new.
2. Open Task Manager and look for setup or updater processes showing CPU or disk movement.
3. Allow ten full minutes to pass without starting new installations.
4. Head to Settings > Update & Security > Windows Update and retry the failed update.
5. Success means the clash was genuine — nothing further is required.

### Fix 2: Reboot to flush the installer state

A restart ends every installer session and resets the engine's bookkeeping — but choose Restart deliberately, since Shut down with Fast Startup can preserve the very state you want gone.

1. Save your open work and close your programs.
2. Open Start > Power > Restart.
3. After signing in, allow three minutes for startup updaters to finish settling.
4. Retry the update in Settings > Update & Security > Windows Update.
5. If the code is gone, a stale session was the culprit.

### Fix 3: End the wedged msiexec process by hand

If waiting and restarting did not help — or you would rather skip straight here — Task Manager lets you evict the squatter directly. Target installer processes only.

1. Hit Ctrl + Shift + Esc to bring up Task Manager.
2. Switch to the Details tab and sort by name.
3. Right-click every `msiexec.exe` listing and select End task.
4. Do the same for any frozen setup.exe or third-party installer you spot.
5. Immediately retry the update in Settings > Update & Security > Windows Update.

### Fix 4: Restart the Windows Installer service from Services

This achieves the service-level reset without a full reboot — useful when the engine itself is wedged but you cannot restart the machine right now.

1. Press Win + R, enter `services.msc`, and hit Enter.
2. Scroll to Windows Installer in the services list.
3. Right-click it and select Restart — or Start, if it appears stopped.
4. Should it refuse to restart, reboot the laptop instead.
5. Once the service reports running normally, attempt the update again.

### Fix 5: Temporarily suspend Microsoft Store updates

Both updaters are working correctly here; they simply need to run in sequence instead of simultaneously.

1. Launch the Microsoft Store app.
2. Open your profile icon > Settings and switch App updates off for now.
3. Alternatively, open Store > Library and pause updates already in progress.
4. Run Windows Update from Settings > Update & Security > Windows Update until it finishes.
5. Turn Store app updates back on afterward and let them complete separately.

### Fix 6: Unregister and re-register the installer engine

When Windows insists the installer is busy though nothing is installing, the engine's registration may be damaged. Unregistering and re-registering rebuilds it cleanly.

1. Open an elevated Command Prompt.
2. Execute `msiexec /unregister` and wait for the silent return.
3. Execute `msiexec /regserver` and wait again.
4. Reboot so the fresh registration loads properly.
5. Retry the update; if the phantom busy signal persists, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) offers deeper servicing diagnostics.

### Fix 7: Reschedule automated updaters that collide every month

If this error returns like clockwork, an automated task — a manufacturer assistant or driver updater — is firing on a timer that overlaps your updates. Shifting its schedule ends the cycle for good.

1. Press Win + R, key in `taskschd.msc`, then press Enter.
2. Scan the Task Scheduler Library for updater tasks belonging to your PC maker or third-party vendors.
3. Right-click the offender, open Properties, and move its trigger to a time you never update — or disable it if you manage drivers manually.
4. Pause automatic Store app updates while Windows Update is working.
5. Retry the update in Settings > Update & Security > Windows Update and confirm the clash is gone.

## Closing

On Windows 10, "another installation is in progress" is almost always temporary — a background updater, a Store refresh, or a frozen setup sitting on the single-install lock. Wait it out, restart past it, or end the stuck process, in that order. The installer lane admits one vehicle at a time; once the stalled one is towed, everything moves again.
