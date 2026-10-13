---
title: "Taming Windows Modules Installer Worker High Disk Usage"
slug: how-to-fix-windows-modules-installer-worker-high-disk-usage
date: 2026-09-10
categories: ["windows-update"]
tags: ["tiworker.exe", "high disk usage", "windows modules installer", "windows update"]
description: "TiWorker.exe pinning your disk at 100%? Windows Modules Installer Worker high disk usage is usually update processing — here is how to tell normal from broken, and fix it."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-worker-high-disk-usage.webp"
faqs:
  - q: "What is Windows Modules Installer Worker?"
    a: "It is TiWorker.exe, the background process that installs Windows updates, enables or disables optional features, and maintains the component store. It is a legitimate and essential Windows process, not malware, even though its disk usage can look alarming. You will usually see it active after Patch Tuesday or when enabling Windows features."
  - q: "Why is TiWorker.exe using 100% disk?"
    a: "Because it is actively installing updates or cleaning up the component store, both of which are disk-heavy. On laptops with mechanical hard drives this can saturate the disk for an hour or more; on SSDs the same work finishes much faster and is less noticeable."
  - q: "How long should I let it run before worrying?"
    a: "Give it at least two to three hours on an HDD, or about an hour on an SSD, while the laptop is plugged in and idle. If disk usage is still pinned at 100% after that with no update progress, something is stuck and the fixes in this guide apply."
  - q: "Can I disable Windows Modules Installer Worker?"
    a: "You should not disable it permanently — Windows Update depends on it. You can temporarily stop the related service for diagnosis, but the correct fix is to let pending updates finish or repair the update components, not to kill the worker."
---

Open Task Manager during a bad episode and you will see it: Windows Modules Installer Worker, or TiWorker.exe, holding your disk at 90 to 100 percent while the laptop crawls. Everything stutters — browsers hang, File Explorer takes ten seconds to open a folder, and the disk light never blinks off. It feels like something is broken, but most of the time TiWorker is doing exactly what it is supposed to do: installing updates.

The real question is whether it is working or stuck. A healthy TiWorker finishes its job and goes quiet; a stuck one grinds for hours or days with no progress in Windows Update. This guide shows you how to tell the difference in about five minutes, then walks through the fixes that actually resolve a stuck worker, from the simple to the structural.

Before blaming TiWorker, make sure it is actually the disk hog. Task Manager's Disk column sorts by current usage — click it and watch for a full minute. Common impostors include SysMain (the old Superfetch) preloading applications, Windows Search indexing a new file batch, and antivirus scans running silently in the background. If TiWorker sits at the top with sustained high usage while Windows Update shows pending work, the diagnosis in this guide holds. If something else leads, fix that instead.

## Why this happens

- **Pending Windows updates are being installed.** TiWorker does the heavy lifting of staging and installing updates, which is intensely disk-bound.
- **Post-update component store cleanup.** After updates install, TiWorker compresses and cleans the WinSxS store, a long disk-heavy maintenance task.
- **A stuck update keeps the worker in a retry loop.** A failed update that never completes keeps TiWorker re-attempting the same work indefinitely.
- **Corrupted update cache forces repeated reprocessing.** Damaged cached packages make the worker redo validation and staging over and over.
- **Optional features being enabled or removed.** Adding .NET Framework or similar features triggers full TiWorker processing.
- **A failing hard drive slows every disk operation.** On a deteriorating HDD, normal worker activity looks like 100 percent disk because the drive itself is slow.
- **Conflicting update components.** Broken servicing-stack state makes each TiWorker run take far longer than it should.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether updates are actually progressing

Do not kill the worker until you know whether it is doing useful work.

1. Open **Settings** > **Windows Update** and check for an update in progress or pending restart.
1. In Task Manager, watch TiWorker's disk usage for ten minutes — fluctuating usage with gradual update progress is normal.
1. If Windows Update shows a failed update alongside the disk spike, the worker is likely stuck on it.
1. Only proceed with the fixes below if the worker has been grinding for hours with no update progress.

### Fix 2: Let it finish on AC power

The simplest fix is patience, applied correctly.

1. Plug the laptop into AC power — TiWorker throttles on battery.
1. Leave the machine idle with the lid open for one to three hours.
1. Check **Update history** afterward for newly installed updates.
1. If the disk settles on its own, the worker was healthy; consider scheduling active hours so it works overnight.

### Fix 3: Restart the Windows Update services

A clean restart of the update pipeline often unsticks a looping worker.

1. Open an elevated Command Prompt.
1. Run `net stop wuauserv`, `net stop bits`, and `net stop trustedinstaller`.
1. Wait thirty seconds, then run the three matching `net start` commands.
1. Watch Task Manager for fifteen minutes to see whether the worker now completes and exits.

### Fix 4: Clear the SoftwareDistribution cache

A corrupted cache is the most common reason TiWorker loops forever.

1. Stop the update services as in Fix 3.
1. Rename `C:\Windows\SoftwareDistribution` to `C:\Windows\SoftwareDistribution.old`.
1. Restart the services and check for updates.
1. A fresh cache gives the worker clean packages to process instead of damaged ones it keeps choking on.

### Fix 5: Run the update troubleshooter and repair system files

Broken servicing components make every TiWorker run slow and endless.

1. Run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update**.
1. Then in an elevated Command Prompt run `DISM /Online /Cleanup-Image /RestoreHealth`.
1. Follow with `sfc /scannow` and restart.
1. Retry updates; a repaired servicing stack lets the worker finish normally. Related reading: [high disk usage by the worker on Windows 11](/articles/how-to-fix-windows-modules-installer-worker-high-disk-usage-on-windows-11/).

### Fix 6: Set updates to manual-heavy control via active hours and metering

If the worker's timing is the problem rather than its health, constrain when it runs.

1. Set **Active hours** in Windows Update to cover your working day.
1. On a metered connection, enable **Metered connection** so large updates wait for your approval.
1. Use **Pause updates** for up to a week when you need guaranteed quiet.
1. This does not fix a stuck worker, but it stops a healthy one from ruining your workday.

### Fix 7: Check drive health and consider an SSD upgrade

On old mechanical drives, even a healthy TiWorker saturates the disk — the hardware is the bottleneck.

1. Run `wmic diskdrive get status` and check SMART data with your maker's tool, e.g. [Lenovo support](https://support.lenovo.com/us/en/) or [Dell support](https://www.dell.com/support) diagnostics.
1. Run `chkdsk C: /f` to fix file-system errors that slow the worker.
1. If the drive is healthy but slow, the lasting fix is an SSD: the same TiWorker workload that takes hours on an HDD takes minutes on solid state.
1. After any drive change, let one full update cycle complete before judging disk behavior. For the step-by-step variant of this repair, see [TiWorker high disk step by step](/articles/how-to-fix-windows-modules-installer-worker-high-disk-usage-step-by-step/).

### Fix 8: Rule out the other usual disk hogs

TiWorker gets blamed for disk spikes it did not cause.

1. In Task Manager, sort by Disk and identify the true top consumer over several minutes.
1. If **SysMain** leads, disable it: `services.msc` > SysMain > Disabled — safe on SSDs.
1. If **Windows Search** or antivirus leads, schedule indexing and scans for idle hours.
1. Re-check during the next update cycle; with impostors quieted, TiWorker's real footprint is usually modest.

## Closing

Windows Modules Installer Worker at 100 percent disk is usually a symptom, not the disease: pending updates, a stuck package, or a slow drive. Diagnose first by checking update progress, then clear the cache and repair the servicing stack if it is genuinely stuck. And if your laptop still has a spinning hard drive, know that an SSD upgrade does more for TiWorker episodes than any software tweak ever will.
