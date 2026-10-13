---
title: "How to Fix Windows Update Error 0x80070020 on a Laptop"
slug: "how-to-fix-windows-update-error-0x80070020-on-laptop"
date: "2026-09-07"
categories: ["windows-update"]
tags: ["0x80070020", "file-in-use", "windows-update", "windows-11"]
description: "Error 0x80070020 means another process is using files the update needs. Find the conflict and clear it with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070020-on-laptop.webp"
faqs:
  - q: "What does error 0x80070020 mean?"
    a: "It means 'the process cannot access the file because it is being used by another process.' During updates, the installer needs exclusive access to certain files, and if an antivirus scanner, another installer, or a stuck update process is holding them, the operation fails with this code. It is a resource conflict, not corruption — the files are fine, just busy."
  - q: "Can two Windows updates run at the same time?"
    a: "Not effectively. Windows serializes update installations because they touch shared system files. If Windows Update, the Microsoft Store, or a third-party updater is installing something when another update starts, the second one hits this file-in-use error. Letting one operation finish completely before starting another is the simplest prevention."
  - q: "Why does my antivirus cause 0x80070020?"
    a: "Real-time antivirus scanners open files to inspect them, and during an update the installer needs those same files exclusively. The scanner's lock collides with the installer's lock, producing the error. This is one of the most common triggers, which is why temporarily pausing real-time protection during updates is a standard troubleshooting step."
  - q: "Does restarting fix 0x80070020?"
    a: "Often, yes — a restart releases file locks held by stuck processes and clears half-finished operations. It is the first thing to try because it costs nothing. If the error returns after a clean restart, though, the lock is being recreated by something that starts with Windows, and you need the deeper steps to identify the conflicting program."
---

Error 0x80070020 is a traffic jam: the update installer needs a file, and another process is sitting on it. Windows file locking is strict — when the installer cannot get exclusive access, it fails rather than risk corrupting the file. The error is honest and specific, which makes it one of the more pleasant update errors to troubleshoot: find who holds the lock, release it, and retry.

The usual lock-holders are antivirus scanners, concurrent installers, and stuck processes from earlier update attempts. The fixes below identify and clear them in order of likelihood, ending with the clean-boot method that isolates the conflict definitively.

File locking is one of the oldest concepts in operating systems: when a process needs exclusive access to a file, others must wait. Error 0x80070020 is what happens when the wait never ends — the update installer needs a file, another process is holding it, and the installer fails rather than risk corrupting it. The error is refreshingly honest about the situation, which makes it one of the more pleasant update errors to troubleshoot. You are not repairing damage; you are resolving a scheduling conflict. Find who holds the lock, clear them out, and the installer proceeds.

## Why this happens

- **Antivirus real-time scanning:** The scanner locks files the installer needs exclusively.
- **Concurrent installations:** Windows Update, Store updates, or third-party updaters running simultaneously.
- **Stuck update processes:** A previous attempt's processes never released their locks.
- **Background MSI installations:** Another program's installer running silently in the background.
- **Search indexer locks:** The indexer occasionally holds files during update operations.
- **Third-party "live" utilities:** Backup or sync tools locking system areas during updates.
- **Pending restart operations:** Files queued for replacement on reboot conflict with new attempts.
- **Corrupt BITS jobs:** Wedged transfer jobs holding handles on update files.

## How to fix it

Work through these in order — diagnose first, then act.

Antivirus software is the lock-holder in the majority of real-world cases, which is why pausing real-time protection sits near the top of the fix list. But do not stop there if pausing does not help — concurrent installers, stuck processes, and wedged transfer jobs each produce the identical error code, and the clean boot in Fix 5 identifies whichever one it is.

### Fix 1: Restart and retry immediately

Clear transient locks with the simplest possible step.

1. Save your work and restart the laptop fully.
2. After booting, do not open any applications.
3. Go straight to Settings, Windows Update, and retry the update.
4. If it succeeds, a stuck process was the culprit.

### Fix 2: Pause antivirus real-time protection

Remove the most common lock-holder from the equation.

1. Open your antivirus suite and pause real-time protection.
2. Retry the update while protection is paused.
3. Re-enable protection as soon as the update completes or fails.
4. If pausing fixed it, look for an antivirus setting that excludes system update operations.

### Fix 3: Check for concurrent installations

Make sure nothing else is installing at the same time.

1. Open Task Manager and look for msiexec.exe processes — more than the update's own is a red flag.
2. Check the Microsoft Store for in-progress app updates and let them finish or pause them.
3. Close any software installers or updaters running in the background.
4. Retry Windows Update once the system is quiet.

### Fix 4: Reset the BITS queue

Clear wedged transfer jobs holding file handles.

1. Open Command Prompt as administrator.
2. Run `bitsadmin /reset /allusers`.
3. Restart the Background Intelligent Transfer Service from services.msc.
4. Retry the update.

### Fix 5: Perform a clean boot

Isolate the conflicting program definitively.

1. Press Win + R, type `msconfig`, and press Enter.
2. On the Services tab, check "Hide all Microsoft services," then click Disable all.
3. On the Startup tab, open Task Manager and disable all startup items.
4. Restart, retry the update in the clean state, then re-enable services afterward.

### Fix 6: Reset the Windows Update components

Rebuild the update infrastructure and clear stuck states.

1. In an admin Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services and reboot.
4. Retry the update.
5. For the full component-reset background, see our [0x80070002 guide](/articles/how-to-fix-windows-update-error-0x80070002-on-laptop/).

### Fix 7: Run the Windows Update troubleshooter

The automated tool detects several lock-related update faults.

1. Open Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart and retry.

### Fix 8: Install the update manually

The standalone installer faces fewer concurrent-access conflicts.

1. Note the failing KB number from update history.
2. Download the .msu from the Microsoft Update Catalog.
3. Close all applications, pause antivirus, and run the installer.
4. Restart when prompted and verify in update history.
5. Our [manual installation guide](/articles/how-to-manually-install-windows-update-on-windows-11/) walks through the Catalog download step by step.

A clean boot that resolves the error gives you a name — the startup program or service whose absence fixed it — and that name is worth keeping. Re-enable your startup items in small groups, retesting the update each time, until the error returns; the last group you enabled contains the culprit. That binary search takes a few reboots but converts a recurring mystery into a known, excludable program. Many users discover the offender is a long-forgotten utility they installed years ago and never use. For the cache and component repairs that complement this conflict hunt, our [0x80070002 walkthrough](/articles/how-to-fix-windows-update-error-0x80070002-on-laptop/) covers the infrastructure side.

## Closing

File-in-use errors are conflicts, not corruption — something is holding what the installer needs. Restart to clear the transient locks, pause the antivirus, quiet concurrent installers, and use a clean boot to name any stubborn holdout. Once the installer has the files to itself, the update proceeds without argument.
