---
title: "How to Fix Windows Update Error 0x80070652 on a Lenovo Laptop"
slug: "how-to-fix-windows-update-error-0x80070652-on-lenovo-laptop"
date: 2026-10-05
categories: ["windows-update"]
tags: ["error 0x80070652", "windows update", "lenovo laptop", "installer busy", "windows 11"]
description: "Error 0x80070652 on a Lenovo laptop means another installation is already in the checkout lane. Seven fixes to clear the conflict and install cleanly."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070652-on-lenovo-laptop.webp"
faqs:
  - q: "What does error 0x80070652 mean?"
    a: "It means ERROR_INSTALL_ALREADY_RUNNING: another installation is already underway, and Windows will not start a second one. The trusted installer is a single checkout lane — a background Windows update, a Store app update, a Lenovo driver install, or an MSI setup can each be holding it. The right response is usually patience: identify the running installer, let it finish, and retry."
  - q: "How do I find what is installing?"
    a: "Open Task Manager, switch to Details, and look for msiexec.exe for MSI installs, TiWorker.exe for the Windows update worker, or SetupHost.exe. Check Settings, Windows Update for an actively installing update, and glance at the Microsoft Store's download queue. Lenovo Vantage sometimes shows driver installs in progress too. Whatever you find, let it complete rather than killing it mid-install."
  - q: "The error persists after everything finished — why?"
    a: "The installation-in-progress flag can jam when an installer crashes without clearing it. A reboot releases most stuck flags; if one survives the reboot, resetting the Windows Update components and restarting the installer services clears it. Only inspect the InProgress registry key if you are comfortable there — the component reset is the safer equivalent."
  - q: "Can I force two updates to install at once?"
    a: "No, and you should not attempt it. The single-installer rule exists because concurrent installs can corrupt shared components and leave the system unbootable. Tools promising to bypass it are dangerous. Queue the updates, let each one finish, and reboot between major ones — slower, but the Lenovo laptop will repay you by actually working afterward."
---

Error 0x80070652 means "another installation is already in progress." Windows runs a single trusted-installer checkout lane, and your update was correctly turned away at the entrance. On Lenovo laptops the usual occupants are a background Store app update, a Lenovo Vantage driver install, or a previous Windows update still working its way through the lane.

This is a queue, not a breakdown — nothing is corrupted. If the installer stalls mid-run rather than refusing outright, the [0x8024200D stalled-installer walkthrough](/articles/how-to-fix-windows-update-error-0x8024200d-on-lenovo-laptop/) covers that adjacent symptom.

Resist the urge to shove past the line. The remedies below identify whoever is in the lane, let them finish, and clear the rare jammed states where the "busy" flag never lifts.

## Why this happens

- **A Windows update still in the lane:** A previous update may be installing silently — TiWorker.exe working away while you try to start another.
- **Store apps checking out:** Microsoft Store app updates use the same installer infrastructure and count as an in-progress installation.
- **Lenovo Vantage mid-driver-install:** Lenovo's utility can be halfway through a driver installation when Windows Update attempts its own operation.
- **An MSI installer holding the lane:** A software installation via msiexec.exe from earlier — even a minimized one — keeps the installer lock.
- **A jammed installer flag:** Sometimes the installation-in-progress registry flag survives a crashed install and never clears, blocking everything behind it.
- **A pending reboot:** Some installers need a restart to release the lane; until you reboot, new installs are refused.
- **Two sessions colliding:** Triggering an install manually while the automatic schedule is already running creates a self-inflicted collision.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Let whoever is in the lane finish

The most common resolution is also the simplest: wait. Windows allows one trusted installer operation at a time, and if another update, a Store app refresh, or an MSI installer is legitimately working, your update was correctly refused until it completes. Verify what is running, give it time, and retry on an idle system — patience, not force. Task Manager's Details tab shows msiexec.exe and TiWorker.exe plainly, and Microsoft's [official Windows support hub](https://support.microsoft.com/en-us/windows) documents which installer processes are normal.

1. Look in Settings, Windows Update for anything mid-install.
2. Scan Task Manager for msiexec.exe or TiWorker.exe activity.
3. Let the active installation finish, then restart the laptop.
4. Retry the update when the system is idle.

### Fix 2: Confirm the update services are on duty

Windows Update leans on a handful of background services, and a disabled or stuck one mimics an installer conflict. Aggressive debloating scripts and tuning tools sometimes switch these off. A minute in the Services console rules the possibility out.

1. Press Win + R, run services.msc, and hit Enter.
2. Review Windows Update, Background Intelligent Transfer Service, Cryptographic Services, and Windows Installer.
3. Configure every service for Automatic startup (Manual for Windows Installer), starting any that are stopped.
4. Retry the update with all four services running.

### Fix 3: Clear the jammed flag by resetting the update folders

When the "busy" flag is a phantom — a crashed install that never released the lane — the stale state lives in the update folders. Halt the services, rename both folders, restart the services — Windows then rebuilds the directories from nothing, and the phantom busy flag dies with the stale state that housed it.

1. Open an elevated Terminal (Admin) via right-click on Start.
2. Switch the services off: run net stop wuauserv, net stop cryptSvc, net stop bits, and net stop msiserver.
3. Rename the update folders: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Switch the services back on with net start, then check for updates.

### Fix 4: Test the install under a clean boot

Startup programs — third-party updaters, overlays, and driver utilities — can keep the installer lane hostage by locking the files or services the installer needs. A clean boot launches Windows on Microsoft services only, testing whether a third-party program is the one refusing to leave the lane, without uninstalling anything.

1. Bring up msconfig with Win + R and head to the Services tab.
2. Check Hide all Microsoft services, then press Disable all.
3. Turn off each item in Task Manager's Startup apps tab.
4. Restart, retry the update, then turn the startup items back on.

### Fix 5: Pause and resume updates to reset the queue

The update queue can lock into a state where an unfinished operation bars everything waiting behind it, and the busy flag never lifts. Pausing updates for a short period, restarting, then resuming forces the queue to rebuild and often releases the stuck install.

1. Navigate to Settings, Windows Update.
2. Choose Pause updates, then 1 week.
3. Reboot the laptop while paused.
4. Click Resume updates and retry the installation.

### Fix 6: Let the Windows Update troubleshooter clear the jam

The built-in troubleshooter is the fastest route through a stuck update state: it inspects the update services, resets pending operations, and repairs common configuration problems automatically. The two-minute pass clears a surprising number of conflicts with no command-line work at all.

1. Open Settings, then head into System, and click Troubleshoot.
2. Pick Other troubleshooters and locate Windows Update.
3. Press Run, wait out the scan, and apply all suggested fixes.
4. Restart the laptop, then revisit Windows Update and retry the installation.

### Fix 7: Scan protected system files with SFC

Damaged system files can leave the installer machinery itself in a state where it reports busy forever. The System File Checker inspects every guarded Windows file against its known-good original and replaces the casualties, removing a whole class of installer failures that masquerade as conflicts.

1. Start an elevated Command Prompt — Terminal (Admin) works too.
2. Run sfc /scannow at the elevated prompt and wait for completion.
3. If any files were repaired, restart the laptop.
4. Attempt the update installation when the restart is done.

## Closing

0x80070652 is Windows protecting the system from concurrent installs — one lane keeps everything consistent. In the overwhelming majority of cases the "other installation" is real and finishes if given time; only genuinely jammed flags need the resets. If downloads rather than installs are the problem, the [0x80246007 download-manager walkthrough](/articles/how-to-fix-windows-update-error-0x80246007-on-lenovo-laptop/) is the right guide.
