---
title: "Windows Update Error 0x80070652 on Laptop? Here's the Fix"
slug: how-to-fix-windows-update-error-0x80070652-on-laptop
date: 2026-09-11
categories: ["windows-update"]
tags: ["windows update error 0x80070652", "error_install_already_running", "msiexec stuck", "update already in progress"]
description: "Error 0x80070652 means another installation is already running. Learn how to find the stuck installer, clear the blockage, and let Windows Update finish."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070652-on-laptop.webp"
faqs:
  - q: "What does error 0x80070652 mean?"
    a: "It means ERROR_INSTALL_ALREADY_RUNNING: Windows Installer believes another installation is already in progress and refuses to start a second one. On laptops this usually happens when a background program installer, an Office update, or a previous Windows Update session never released the installer lock."
  - q: "How do I know which installer is stuck?"
    a: "Open Task Manager, go to the Details tab, and look for msiexec.exe processes. If one has been running for a long time with no progress, or several are stacked up, that is your culprit. Ending the stuck process usually clears the error immediately."
  - q: "Can I just restart my laptop to fix 0x80070652?"
    a: "Yes, a restart is the simplest fix and works in most cases because it terminates every installer process and releases the lock. Only move on to manual steps if the error returns right after a clean reboot, which suggests some program is grabbing the installer again at startup."
  - q: "Why does 0x80070652 keep coming back?"
    a: "A program may be trying to install or update itself at every boot, such as a half-removed application or a broken Office Click-to-Run task. Check your startup items and scheduled tasks for installers that launch automatically, and disable the offender once you identify it."
---

Error 0x80070652 has a refreshingly honest meaning: another installation is already running. Windows Installer is strictly single-file — it will not start your update while it thinks a different install is in progress. The trouble is that the other install is often invisible, a background process that started hours ago and quietly wedged itself.

On laptops, the usual suspects are easy to name. Microsoft Office's Click-to-Run updater, a third-party program's auto-updater, or a Windows Update session that stalled mid-install can all hold the installer lock indefinitely. Sometimes the process is genuinely gone but the lock was never released, leaving Windows convinced an install is still underway.

The good news is that this is one of the faster update errors to resolve. Most of the time a reboot or a quick trip to Task Manager clears it. The steps below move from the thirty-second fixes to the deeper cleanup for cases where the error keeps resurrecting itself.

## Why this happens

- **A background installer is genuinely running.** Office Click-to-Run, a driver package, or another application's updater may be installing silently while Windows Update tries to start.

- **A stuck msiexec.exe process.** The Windows Installer process sometimes hangs after its parent program closes, holding the system-wide install lock forever.

- **A previous update never finished.** An interrupted Windows Update session can leave the servicing stack believing an installation is still active.

- **Pending restart lock.** Some installers set a flag that blocks new installations until the machine reboots, and the reboot never happened.

- **Corrupt Windows Installer registration.** If the installer service's registration is damaged, it can report itself as busy when it is actually idle.

- **Auto-starting installer at boot.** A broken program may launch its installer on every startup, re-creating the conflict within minutes of each reboot.

- **Third-party software updaters.** OEM utilities and third-party update managers that install drivers or apps in the background compete with Windows Update for the lock.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Restart the laptop

The fastest resolution, and it works more often than not. A restart terminates every installer process, releases the lock, and lets Windows Update start with a clean slate. Do a full restart, not a shutdown with Fast Startup, so nothing is preserved in the hibernation file.

1. Click Start, then Power, then Restart. Avoid Shut down for this test.
2. After the reboot, wait two minutes for startup tasks to settle.
3. Open Settings, then Windows Update, and click Check for updates.

### Fix 2: Fix 2: End the stuck installer in Task Manager

If a reboot is not convenient or the error returns, look for the wedged process directly. A msiexec.exe entry that has been sitting for ages with no CPU activity is almost certainly the process holding your lock.

1. Press Ctrl + Shift + Esc to open Task Manager and switch to the Details tab.
2. Look for msiexec.exe. If you see one that has been running a long time, select it and click End task.
3. Also end any obvious third-party installer processes, such as setup.exe entries you did not start.
4. Retry Windows Update immediately.

### Fix 3: Fix 3: Restart the Windows Installer service

When the service itself is confused about its state, restarting it clears the phantom busy flag. This is a gentle reset that does not touch your installed programs.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find Windows Installer in the list, right-click it, and choose Restart. If it is stopped, choose Start instead.
3. Close the Services window and run Windows Update again.

### Fix 4: Fix 4: Run the Windows Update troubleshooter

Microsoft's troubleshooter knows how to detect and clear installer conflicts, including the pending-restart flags that block new installations. It is worth running even if you suspect a stuck process, because it cleans up the flags a manual kill leaves behind.

1. Open Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Click Run next to Windows Update.
3. Apply all recommended fixes and restart the laptop before retrying the update.

### Fix 5: Fix 5: Clean-boot to find the conflicting program

If the error returns after every reboot, something launching at startup is grabbing the installer. A clean boot strips startup items away so you can confirm the conflict, then re-enable items in halves to identify the offender.

1. Press Win + R, type `msconfig`, and on the Services tab check Hide all Microsoft services, then Disable all.
2. In Task Manager's Startup apps tab, disable everything, then restart.
3. If the update now works, re-enable startup items in groups until the error returns, and you have found the culprit.

### Fix 6: Fix 6: Reset the Windows Update components

When the servicing stack itself believes an install is in progress, resetting its components clears the stored state. This stops the update services, renames the cache folders, and restarts everything fresh.

1. Open Terminal as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the four services with `net start` and check for updates.

### Fix 7: Fix 7: Install the update manually from the Catalog

If the automatic path stays blocked, sidestep it. A manual install through the standalone package does not go through the same queued installer path, and it often succeeds where Windows Update kept complaining about a phantom conflict.

1. Note the KB number from your update history.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run the .msu file, restart when asked, and verify in update history. For related installer-failure codes, see our guide on [fixing update error 0x80070643](/articles/how-to-fix-windows-update-error-0x80070643-on-laptop/).

## Closing

Error 0x80070652 is Windows being overcautious: it would rather refuse your update than risk two installers colliding. In practice, a reboot or ending a stuck msiexec process resolves it in minutes, and the deeper resets here cover the stubborn cases where the lock keeps coming back. If you run into the closely related download-side failures instead, our walkthrough for [update error 0x8024200d](/articles/how-to-fix-windows-update-error-0x8024200d-on-laptop/) picks up that thread, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official troubleshooter path.
