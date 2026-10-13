---
title: "How to Fix Windows Update Error 0x80070020 on a Dell Laptop"
slug: how-to-fix-windows-update-error-0x80070020-on-dell-laptop
date: 2026-09-21
categories: ["windows-update"]
tags: ["0x80070020", "file in use", "dell laptop", "process locking files"]
description: "Error 0x80070020 on your Dell means another process is using files the update needs. Find and release the lock with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070020-on-dell-laptop.webp"
faqs:
  - q: "What does Windows Update error 0x80070020 mean?"
    a: "It means 'the process cannot access the file because it is being used by another process.' The update installer needs to replace files that something else currently has open. It is a file-locking conflict, not corruption — identifying and stopping the program holding the lock lets the update proceed."
  - q: "What usually locks the files Windows Update needs?"
    a: "Third-party antivirus real-time scanners are the most common culprit, followed by Dell utilities, backup software, and indexing or search tools. Any program that hooks into system files or scans them continuously can hold the exact locks the installer needs. Clean-booting isolates the offender quickly."
  - q: "Is it safe to stop the process holding the lock?"
    a: "Stopping a third-party program temporarily is safe. Never force-stop Windows system processes or the update installer itself to clear a lock — that causes the corruption this error is trying to prevent. Use clean boot or the program's own exit/quit option rather than killing processes indiscriminately in Task Manager."
  - q: "Why does 0x80070020 happen more on Dell business laptops?"
    a: "Corporate Dells run endpoint protection, encryption agents, backup clients, and management tools simultaneously — each a potential file-lock holder. The more agents hooking system files, the higher the chance one holds a lock during the update window. Coordinating updates with IT, or updating in safe mode, avoids most of these collisions."
---

Error 0x80070020 is a file-locking conflict: the update installer tried to replace a file that another process had open. Windows will not let two programs write the same system file, so the installer fails rather than risk corruption. On Dell laptops — especially business models running endpoint protection, encryption agents, and Dell's own utilities — there are plenty of candidates holding those locks.

The strategy is elimination: quiet the likely lock-holders, retry, and if needed strip the system down to a clean boot where nothing third-party can interfere. This error resolves quickly once you stop guessing and start isolating.

File locking is one of operating systems' oldest problems: two programs, one file, and a referee (the OS) that refuses to let them collide. Windows' answer is strict — the installer fails rather than risk corruption — which is the right call, even when it is inconvenient. The philosophical point matters because it tells you the fix is never to force the lock: it is to find the other program and ask it, politely via its own controls, to let go.

## Why this happens

- **Third-party antivirus real-time scanning** holding locks on files the installer must replace.
- **Dell utilities (SupportAssist, Dell Update, encryption agents)** accessing system files during the update.
- **Backup or sync software** (OneDrive, corporate backup clients) locking files mid-update.
- **Windows Search indexing** holding file handles during the install phase.
- **A previous update's processes** still running and locking files from an incomplete install.
- **Third-party firewall or endpoint protection** hooking file operations.
- **Corrupted lock state** — a crashed process left a stale lock the system still honors.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and retry — clear stale locks

1. Do a full **Restart** (**Start** > **Power** > **Restart**).
2. Immediately after booting, before opening any programs, go to **Settings** > **Windows Update** and retry.
3. Many 0x80070020 cases are stale locks from crashed processes — a clean boot cycle releases them.
4. If it fails again identically, the lock-holder is a persistent program, not a stale lock — continue.

### Fix 2: Temporarily disable third-party antivirus

1. Open your antivirus and disable **real-time protection** (and any tamper protection toggle).
2. Retry the update immediately with protection off.
3. Re-enable protection the moment the attempt finishes, pass or fail.
4. Antivirus scanners are the number one lock-holder for this error. If the update succeeds, add the update working folders to the antivirus exclusions to prevent recurrence.

### Fix 3: Pause Dell utilities and background agents

1. Open **Dell SupportAssist** and make sure no scan or update is running — close it fully.
2. In Task Manager (**Ctrl + Shift + Esc**), look for Dell, backup, or sync processes consuming resources and end the non-essential ones via their own quit options.
3. Pause OneDrive syncing (click the OneDrive tray icon > **Pause syncing**) during the update.
4. Retry. Dell's own tools are frequent lock-holders on Dell hardware — keep their drivers current via [Dell Support](https://www.dell.com/support) to reduce conflicts.

### Fix 4: Clean boot to isolate the lock-holder

1. Press **Windows key + R**, type `msconfig`, press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then **Disable all**.
3. In Task Manager's **Startup** tab, disable everything, then restart.
4. Retry the update in this minimal state. If it succeeds, re-enable services in halves to identify the locking program — then decide whether to keep it disabled during updates or replace it. Microsoft documents the method on the [Windows Update support page](https://support.microsoft.com/en-us/windows).

### Fix 5: Stop the Windows Update services and clear their state

1. Open an elevated Command Prompt:
   `net stop wuauserv`, `net stop bits`
2. Delete the contents of `C:\Windows\SoftwareDistribution\Download`.
3. `net start wuauserv`, `net start bits`.
4. Sometimes the lock-holder is a stuck update process itself — stopping the services releases its locks, and the fresh state prevents it from re-locking. Related: [resetting update components](/articles/how-to-reset-windows-update-components-in-windows-11-24h2/).

### Fix 6: Run the update in Safe Mode with Networking

1. Hold **Shift** while clicking **Restart** (or use recovery) to reach **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **5** for Safe Mode with Networking.
2. In Safe Mode, only essential drivers and services load — third-party lock-holders cannot start.
3. Run **Settings** > **Windows Update** and install from Safe Mode.
4. Restart normally afterward. If the update installs cleanly in Safe Mode, you have proven a third-party program was the lock-holder — the clean-boot bisection in Fix 4 will name it.

### Fix 7: Manual install with minimal interference

1. Note the KB from **Update history** and download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Clean-boot the laptop (Fix 4), then run the `.msu` installer.
3. Restart when prompted, then undo the clean boot.
4. The standalone installer holds its file operations in a tighter window than the full Windows Update pipeline, making it less vulnerable to lock contention. Confirm in Update history, and see [monthly cumulative failure repairs](/articles/how-to-fix-monthly-cumulative-update-failed-on-windows-11/) for recurring patterns.

### Fix 8: Identify the locking process with Microsoft's Handle tool

When you must know exactly which process holds a file, Sysinternals' Handle utility (from Microsoft) names it.

1. Download **Handle** from Microsoft's Sysinternals site and extract it to a folder.
2. In an elevated Command Prompt in that folder, run `handle.exe <filename>` for the file the installer chokes on (check the CBS log for the name).
3. Handle lists the process and its PID — exit that program normally through its own interface.
4. Retry the update. Knowing the exact culprit beats disabling half your startup items blindly, and you only need this tool when the clean-boot bisection is inconclusive.

## Closing

0x80070020 on a Dell is a traffic jam, not a breakdown: something else is holding files the installer needs. Restart to clear stale locks, quiet the antivirus and Dell agents, and use clean boot or Safe Mode to prove which program is the culprit. Once the lock-holder is identified, every future update can be scheduled around it. Lock conflicts are a coordination problem, and coordination has a boring, effective solution: update when the other programs are not running. A monthly habit — close everything, disable the antivirus for the duration, install, re-enable — prevents this entire error class without any detective work.
