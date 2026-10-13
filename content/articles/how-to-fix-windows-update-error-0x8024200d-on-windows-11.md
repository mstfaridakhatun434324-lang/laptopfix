---
title: "Fix Windows Update Error 0x8024200d on Windows 11 (Update Installer Hung)"
slug: how-to-fix-windows-update-error-0x8024200d-on-windows-11
date: 2026-09-25
categories: ["windows-update"]
tags: ["windows update", "0x8024200d", "installer hung", "troubleshooting", "windows 11"]
description: "Windows 11 error 0x8024200d means the update installer hung mid-installation. Unstick the servicing pipeline with these proven steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x8024200d-on-windows-11.webp"
faqs:
  - q: "What does error 0x8024200d mean?"
    a: "On Windows 11, 0x8024200d (WU_E_UH_INSTALLERHUNG) means the update handler began installing but stopped progressing until Windows Update timed out. Typical causes are driver/OS update collisions, corrupted payloads, exhausted disk throughput, or antivirus interference. Resetting the update components and retrying on an idle machine resolves most cases."
  - q: "How long should I wait before calling an update 'hung'?"
    a: "Big updates can legitimately take one to two hours on slower laptops, particularly during the Working on updates phase with disk activity. Call it hung only with zero disk/CPU activity for 30+ minutes, or when Windows Update itself reports 0x8024200d. Interrupting a merely slow update creates the corruption you are trying to avoid."
  - q: "Can a failing hard drive cause installer hangs?"
    a: "Yes. Servicing writes thousands of files, and a drive with bad sectors or degraded flash turns those writes into retries and timeouts that mimic a hung installer exactly. If 0x8024200d recurs across unrelated updates even after component resets, run `chkdsk C: /f /r` and check SMART health — the drive may be the real problem."
  - q: "Why do driver updates hang the OS update?"
    a: "Because both use the servicing stack and can fight over the same locks and reboot sequencing. Installing them in one combined session occasionally deadlocks the handler. Updating drivers first — via Device Manager or the manufacturer's tool — then running the OS update separately avoids the collision entirely."
---
With 0x8024200d (WU_E_UH_INSTALLERHUNG), the update engine is telling you its installer began work and then froze: the handler made no progress, the timer ran out, and Windows abandoned the wait. On Windows 11 the usual triggers are a driver package colliding with the OS update, a disk too sluggish to finish servicing in time, or a damaged package trapping the installer in an endless loop.

A hang is messier than a clean failure because it abandons the system midway — partially staged files, half-applied operations. So the goal is getting the servicing stack back to a calm, known-good idle: reboot, sweep away the debris, confirm integrity — and only then give the update another try, this time without rushing it.

If the same hung-installer behavior shows on your other laptop, the [Windows 10 guide](/articles/how-to-fix-windows-update-error-0x8024200d-on-windows-10/) covers Windows 10; when the failure is fatal instead of a hang, the [companion guide for 0x80070643](/articles/how-to-fix-windows-update-error-0x80070643-on-windows-11/) is the relevant read. Begin by breaking the deadlock.

## Why this happens

- **A driver update collided with the OS update:** installing a driver package and an OS update in one session can deadlock their installers over shared servicing resources, with the handler hanging until the timeout fires.
- **The installer choked on corrupted payload data:** a damaged package can push the installer into retry loops or parsing stalls it never escapes — a hang instead of a clean error.
- **Disk throughput fell behind:** servicing is I/O-intensive; on a nearly full drive, a failing drive, or one pounded by antivirus scanning, the installer creeps so slowly the handler's timeout beats it.
- **Antivirus intercepted servicing operations:** real-time scanning of every file the installer touches can slow servicing to a crawl or deadlock against the installer's own file locks, appearing as a hang.
- **Resources ran dry mid-install:** very low RAM or CPU saturation from background tasks during a large update can starve the installer until it looks hung.
- **Leftover operations from the last attempt stalled progress:** half-applied operations awaiting a reboot can clog the servicing queue, so the next attempt stalls on the previous one's unfinished business.
- **Disk or encryption filters interfered:** filter drivers — encryption, backup, storage utilities — live in the I/O path of every file the installer writes, and a misbehaving filter can stall servicing indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart, then give the update a quiet, undisturbed run

A hung installer is often resource contention in disguise. A restart clears the half-applied state; then — crucially — leaving the machine alone during the retry gives the installer the CPU and disk it lacked the first time.

1. Click Start > Power > Restart to clear the hung state fully.
2. After signing in, close unnecessary programs and pause big downloads or scans.
3. Open Settings > Windows Update, start the update, then leave the machine untouched for at least 30 minutes.
4. Look for steady disk activity — slow progress still means it is working.
5. If it finishes, the hang was contention, not corruption.

### Fix 2: Reset the Windows Update components

When the hang repeats, assume the servicing queues are holding debris from the stalled attempt — half-staged files and wedged service states that would hang the next try identically. Stopping the services, renaming SoftwareDistribution and catroot2, and restarting rebuilds the whole operational layer from zero.

1. Bring up Command Prompt as administrator.
2. Halt the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart all four services with the matching `net start` commands.
5. Attempt the update again in Settings > Windows Update on a quiet, idle machine.

### Fix 3: Mend system files with DISM and SFC

A hang can both cause and stem from file damage: the stalled installer may have left protected files broken, or pre-existing damage might have stalled it. DISM repairs the store, SFC restores protected files — together they remove integrity as a variable.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` until it completes.
3. Follow it with `sfc /scannow` and let that finish.
4. Reboot the laptop.
5. Retry the update; hangs persisting after clean integrity point to drivers, covered next.

### Fix 4: Install drivers separately ahead of the OS update

Driver-update collisions lead the causes of installer hangs, so defuse them with sequencing: update drivers first via Device Manager or your manufacturer's tool, restart, and only then run the OS update. Separating the two removes the deadlock opening entirely.

1. Open Device Manager and inspect the storage controllers, display adapters, and network adapters for warning icons.
2. Refresh chipset and storage drivers from your laptop manufacturer's support site (Dell, HP, or Lenovo).
3. On Intel-based laptops, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) automates chipset and graphics driver updates.
4. Restart once driver updates finish.
5. Then run the OS update via Settings > Windows Update on its own.

### Fix 5: Update in a clean boot to remove contention

A clean boot strips away the antivirus filters, backup agents, and utilities that drag or deadlock servicing. If the update sails through here, third-party interference is proven — identify the specific program by re-enabling halves.

1. Press Win + R, enter `msconfig`, and hit Enter.
2. On the Services tab, tick Hide all Microsoft services, then choose Disable all.
3. Switch off all startup items via Task Manager's Startup tab.
4. Restart, run the update via Settings > Windows Update, and leave the machine idle.
5. Restore normal startup afterward with `msconfig`, then reboot again.

### Fix 6: Install the update manually from the Catalog

When the automatic handler keeps stalling on the same package, lift the handler out of the loop: download the standalone .msu from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install it directly. The standalone installer runs outside the hung handler path and often succeeds where the pipeline stalls.

1. Locate the failing update's KB number in Settings > Windows Update > Update history.
2. Look it up on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and download your architecture's package.
3. Close other programs, then run the .msu.
4. Allow up to an hour on an idle machine without interruption.
5. Reboot when prompted, then verify with a normal update check.

## Closing

Error 0x8024200d means the engine stopped waiting on an installer that quit making progress — most often starved of resources, tangled with a driver update, or stuck on damaged data. Reset the servicing state, handle drivers on their own schedule, and hand the installer a quiet machine. On Windows 11, once the contention is gone, these hangs usually turn out to be servicing simply asking for elbow room.
