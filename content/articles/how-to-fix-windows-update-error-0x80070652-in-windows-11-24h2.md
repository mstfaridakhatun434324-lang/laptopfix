---
title: "How to Fix Windows Update Error 0x80070652 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80070652-in-windows-11-24h2
date: 2026-10-12
categories: ["windows-update"]
tags: ["windows update", "0x80070652", "error code", "windows 11", "msiexec"]
description: "Error 0x80070652 means another installation is already running. Clear the ghost installer session with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070652-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80070652 mean?"
    a: "ERROR_INSTALL_ALREADY_RUNNING: the Windows Installer service — or the update engine — rejected the new install because an earlier session is still active, or a crashed one never surrendered its lock. Only one installation may hold the installer lock at a time, so the newcomer is turned away."
  - q: "How do I tell a real install from a ghost?"
    a: "Open Task Manager with Ctrl + Shift + Esc and look for msiexec.exe, setup.exe, or TiWorker.exe doing visible work — CPU activity and growing runtime mean something real is installing. A process sitting at 0 percent CPU for a long time, or no such process at all, means the lock is a ghost and safe to clear."
  - q: "Is it safe to end msiexec.exe in Task Manager?"
    a: "Only when no install is visibly progressing. Ending the process of a genuine in-flight installation can leave software half-installed. A plain restart is the safest ghost-buster: it ends every installer process cleanly and lets the Windows Installer service start fresh."
  - q: "The error returns every Patch Tuesday. Why?"
    a: "Something on your system routinely collides with the update window — a scheduled third-party updater, a Store app update, or a driver installer that runs at the same time. Stagger those schedules, or pause the third-party updaters on update day. A crashed installer that never released its lock is the other classic repeat offender."
---

Somebody is already in the shower, and the bathroom door is locked. That is 0x80070652: the Windows Installer service turned your update away because an earlier installation session is still holding the lock — or a crashed one never gave it back. Only one install may proceed at a time, so the newcomer waits outside.

On 24H2 laptops the "somebody" is usually a phantom rather than a real installation. The classic story is a crashed installer that kept its lock, and every subsequent update fails until that phantom session is evicted. Laptops are prone to this because sleep and hibernation interrupt installers more often than desktops do. But sometimes the occupant is real: Store apps updating, Office Click-to-Run working in the background, or a driver installer mid-flight.

So the first job is detective work, not repair: determine whether the busy installer is genuine or a phantom. The fixes below start there and escalate only as needed — jumping straight to process-killing without diagnosing first is how half-installed software happens.

## Why this happens

- **A crashed installer kept its lock.** The process died, yet the Installer service still believes a session is active.
- **Another installation is legitimately running.** Office Click-to-Run, Store apps, or a background driver installer currently holds the lock.
- **A previous install awaits its reboot.** Certain installers retain the session until a restart finishes their work.
- **Manual and automatic installs collided.** Launching an .msu by hand during an automatic update run triggers exactly this code.
- **Two sessions launched together.** Uncommon, but frantic retry-clicking can queue conflicting update sessions.
- **A wedged msiexec.exe process lingers.** The installer executable hangs out of sight and obstructs everything queued behind it.
- **Installer service state corrupted.** The Windows Installer service itself becomes confused after an unclean shutdown.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Ascertain whether the installer is genuine or a phantom

Hold off on terminating anything — first discover what truly holds the lock.

1. Open Task Manager with Ctrl + Shift + Esc and scan the Processes tab for `msiexec.exe`, `setup.exe`, or `TiWorker.exe`.
2. Inspect the CPU and runtime columns: a hung process idles at 0 percent CPU for ages, while a genuine one shows activity.
3. Glance at the Downloads section of the Microsoft Store for app updates currently in flight.
4. If something real is installing, give it time to finish — interrupting a genuine install creates bigger problems. If it is a phantom, or nothing shows at all, continue below.

### Fix 2: Restart to evict the ghost session

A plain restart is the safest way to evict a phantom: it terminates every installer process, giving the Windows Installer service a clean start. Make it a full Restart rather than a shutdown, since fast startup can otherwise preserve the stuck state across the power cycle.

1. Save your work and choose Restart (not Shut down) from the Start menu.
2. After signing in, wait a few minutes for startup installations to settle.
3. Open Settings > Windows Update, press Check for updates a single time, and let it run undisturbed.

### Fix 3: End the hung installer process by hand

When restarts do not dislodge it — or restarting is impossible right now — terminating the hung msiexec process frees the lock. Attempt this only when no installation is visibly underway.

1. In Task Manager's Details tab, find `msiexec.exe`.
2. End the task, then confirm the process is fully gone.
3. Retry the Windows Update installation at once, before another process seizes the lock.

### Fix 4: Rebuild the installer engine's registration

When the service is confused rather than merely occupied, re-registering its engine wipes the corrupted session state. This is the deepest repair short of reinstalling Windows, and it resolves the cases where restarts and Task Manager both fail.

1. Launch an elevated Command Prompt.
2. Run `msiexec /unregister`, then pause a few seconds.
3. Run `msiexec /regserver` to rebuild the registration.
4. Reboot the laptop, then retry the update check.

### Fix 5: Deploy the automated troubleshooter

The Windows Update diagnostic detects stuck installer states and applies safe automatic repairs.

1. Pop open Settings > System > Troubleshoot > Other troubleshooters.
2. Punch Run on the Windows Update line and trail its prompts.
3. Restart after it wraps and probe the update again.

### Fix 6: Reset the update components

If the phantom keeps returning after restarts, the engine's own cache may be re-creating the bad state. A full component reset clears that cache and forces Windows to rebuild it from nothing.

1. Freeze the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Park the folders under backup names: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Thaw the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Probe for updates once the lock is free and confirm the install proceeds.

### Fix 7: Reinstall Windows as the ultimate repair

A permanently confused installer service is rare, but when nothing else evicts the phantom lock, reinstalling 24H2 over the existing install rebuilds the service. Source the ISO solely from [Microsoft's Windows 11 download site](https://www.microsoft.com/en-us/software-download/windows11).

1. Display the ISO and mobilize `setup.exe`.
2. Acquiesce to the license terms while retaining **Keep personal files and apps** selected.
3. Designate half an hour to ninety minutes for the installer's restarts, and abandon the machine throughout.
4. Demonstrate that updates install cleanly afterward.

## Closing

Most of the time this resolves to patience or evicting a phantom session — restart first, investigate second. With the installer lock released, updates move forward normally. If updates then fail with different codes, the [24H2 update-error decoder](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) interprets whatever appears next, and the [troubleshooter guide](/articles/best-way-to-fix-windows-update-with-troubleshooter/) automates the simple checks. The [Windows support hub](https://support.microsoft.com/en-us/windows) documents installer behavior officially.
