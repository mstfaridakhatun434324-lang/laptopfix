---
title: "How to Fix Windows Update Error 0x80070020 on an HP Laptop"
slug: how-to-fix-windows-update-error-0x80070020-on-hp-laptop
date: 2026-10-10
categories: ["windows-update"]
tags: ["windows update", "0x80070020", "hp laptop", "windows 11"]
description: "Error 0x80070020 on your HP laptop means another program is locking update files. This HP-focused guide finds the locker with clean boot and finishes the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070020-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x80070020 mean on an HP laptop?"
    a: "It is ERROR_SHARING_VIOLATION: the updater tried to replace a file that another process was using, and Windows refused. The usual locker is antivirus real-time protection, but HP utilities, backup tools, and even a stuck installer can hold the file. The fix is identifying the locking process — usually via clean boot — and retrying the update without it running."
  - q: "Can antivirus really block Windows Update?"
    a: "Yes, and it is the most common cause of this exact code. Real-time protection locks files to scan them, and if the updater needs that same file at that moment, the install fails with 0x80070020. Temporarily pausing third-party protection during the update is safe — Windows Security activates automatically — and the update typically completes on the next attempt."
  - q: "Is it safe to end msiexec.exe in Task Manager?"
    a: "Ending a stuck Windows Installer process (msiexec.exe) is generally safe when no installation is visibly progressing, and it is a documented step for the 0x80070652 sibling error too. If an installer was genuinely mid-work, the worst case is that particular install needs rerunning. Never end it repeatedly in a loop; one clean termination followed by a reboot is the correct approach."
  - q: "Why does this error happen on HP laptops specifically?"
    a: "It isn't HP-exclusive, but HP laptops ship with several background utilities — Support Assistant, HP Wolf Security components, audio and power managers — that can lock shared system files during their own operations. When one of these holds a file the updater needs, you get 0x80070020. The clean-boot procedure below isolates exactly which one is responsible."
---

Error 0x80070020 is Windows' way of saying "that file is busy": ERROR_SHARING_VIOLATION. The updater reached for a file it needed to replace, found another process holding it open, and aborted rather than risk corruption. Your system is fine — nothing half-installed — but the update can't proceed until the file is free.

On HP laptops the prime suspects are the extras that ship with the machine: real-time antivirus, HP's own background utilities, backup agents, and occasionally a previous installer that never exited. The repair is detective work more than surgery — find what's holding the file, stop it, and let the update through. The sequence below moves from the quick checks to the definitive clean-boot isolation.

There's a useful way to think about this error: Windows is protecting you. Overwriting a file that another process is actively using could corrupt that process or the file itself, so the updater declines rather than risks it. The frustration is that Windows doesn't name the locker — it just reports the collision. Everything below is designed to answer that one unanswered question: who is holding the file?

## Why this happens

- **Antivirus real-time protection locking files.** The most common cause — the scanner holds files the updater needs to replace.
- **HP background utilities.** Support Assistant, audio managers, and security components can lock shared libraries during their own tasks.
- **A stuck previous installer.** An msiexec process that never exited keeps its files claimed.
- **Backup or sync tools.** OneDrive, Dropbox, or backup agents locking user and system files mid-sync.
- **Windows Search indexer.** The indexer occasionally locks files the updater wants.
- **Pending restart from an earlier update.** Files flagged for replacement at reboot can't be touched until it happens.
- **Corrupted update state.** A confused updater retrying against files it already has open.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and retry — clear the transient locks

The simplest locks evaporate at reboot.

1. Save your work and restart the laptop normally — don't shut down with fast startup games, do a real restart.
2. Before opening anything else, go to **Settings > Windows Update** and click **Check for updates** or **Retry**.
3. If the update proceeds, the lock was transient — a background task that has since finished.
4. If 0x80070020 returns immediately, the locker is persistent; continue below.

### Fix 2: Pause third-party antivirus during the update

The number-one persistent locker gets a timeout.

1. Temporarily disable real-time protection in your third-party antivirus (Windows Security steps in automatically).
2. Immediately retry the failing update while protection is paused.
3. Re-enable your antivirus right after the test, whatever the result.
4. If the update succeeded, schedule future updates with protection paused, or add the `C:\Windows\SoftwareDistribution` folder to the antivirus exclusions.

### Fix 3: End stuck installer processes

A previous install may still be squatting on the files.

1. Open Task Manager (**Ctrl + Shift + Esc**) and go to the **Details** tab.
2. Look for `msiexec.exe`, `setup.exe`, or `TrustedInstaller.exe` processes that aren't doing visible work.
3. Right-click a stuck one and choose **End task** — one clean termination, then stop.
4. Restart the laptop and retry the update with the squatter gone.

### Fix 4: Pause sync and backup tools

Cloud sync clients are stealthy file-lockers.

1. Pause OneDrive sync (click its taskbar icon > **Pause syncing**) and quit Dropbox or other sync clients temporarily.
2. If you run a scheduled backup tool, make sure no backup job is currently running.
3. Retry the update with the sync tools quiet.
4. Resume syncing afterward; consider scheduling backups outside your usual update window to avoid future collisions.

### Fix 5: Perform a clean boot to identify the locker

The definitive test: strip the startup down to Microsoft only.

1. Press **Windows key + R**, type `msconfig`, and on the **Services** tab check **Hide all Microsoft services**, then **Disable all**.
2. In Task Manager's **Startup apps** tab, disable every entry, then restart.
3. Retry the update in this minimal state — it almost always succeeds here.
4. Re-enable services in halves, rebooting and retesting, until the error returns; the last group enabled contains your locker. HP utilities you actually use can be reinstalled from the [HP support site](https://support.hp.com/us-en) if one proves problematic.

### Fix 6: Reset the update components

A confused updater can lock its own files; reset clears the state.

1. In an administrator Command Prompt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
2. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`.
4. Retry the update; the fresh component state has no stale locks.

### Fix 7: Install the update manually in a quiet state

For the last stubborn package, combine manual install with minimal interference.

1. Note the failing KB from Update history and download its x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Pause antivirus and sync tools as in Fixes 2 and 4.
3. Run the standalone installer — its simpler flow holds fewer files open at once.
4. Confirm success in Update history. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents sharing-violation scenarios for deeper reading.

### Fix 8: Route HP drivers through HP's own channel

Reduce contention permanently by separating HP driver updates from Microsoft's queue.

1. In **HP Support Assistant**, make sure all HP drivers are current through HP's own channel first.
2. If a specific HP driver keeps colliding in Windows Update, hide that driver update with Microsoft's "show or hide updates" troubleshooter.
3. Keep getting that driver from HP going forward — one channel per driver means no more two-way tug-of-war over the same files.
4. Retry the full Windows Update check; with HP drivers out of Microsoft's queue, the remaining updates face far less contention.

## Closing

Error 0x80070020 is a file-access dispute, not system damage, and the clean-boot isolation in Fix 5 definitively names the locking program on any HP laptop. For the generic walkthrough, see the [step-by-step 0x80070020 guide](/articles/how-to-fix-windows-update-error-0x80070020-step-by-step/), and if your error is invalid data rather than a locked file, the [0x8007000D guide for HP laptops](/articles/how-to-fix-windows-update-error-0x8007000d-on-hp-laptop/) covers that distinct failure.
