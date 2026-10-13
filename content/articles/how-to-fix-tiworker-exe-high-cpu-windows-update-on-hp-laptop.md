---
title: "TiWorker.exe High CPU During Windows Update on HP Laptops: Fix It"
slug: how-to-fix-tiworker-exe-high-cpu-windows-update-on-hp-laptop
date: 2026-09-25
categories: ["windows-update"]
tags: ["tiworker.exe", "high cpu", "windows modules installer", "hp laptop", "windows update"]
description: "TiWorker.exe eating your HP laptop's CPU during Windows Update? Learn what the Windows Modules Installer Worker does, when to wait, and how to calm it down."
thumbnail: "/images/thumbs/how-to-fix-tiworker-exe-high-cpu-windows-update-on-hp-laptop.webp"
faqs:
  - q: "What is TiWorker.exe and is it safe?"
    a: "TiWorker.exe is the Windows Modules Installer Worker, a legitimate Microsoft system process that installs, modifies, and removes Windows updates and optional components. It is completely safe and essential. High CPU from TiWorker during an update is normal behavior — it becomes a problem only when the high usage persists for many hours with no update activity, which signals a stuck update process."
  - q: "How long should TiWorker.exe use high CPU before I worry?"
    a: "On an HP laptop, allow up to two hours during an active update, longer on a mechanical hard drive. TiWorker compresses and decompresses update packages, which is CPU-intensive by design. Worry when Task Manager shows sustained high CPU for several hours while Settings > Windows Update shows no progress, or when it happens with no update running at all."
  - q: "Can I just kill TiWorker.exe in Task Manager?"
    a: "You can end it, but it will usually restart because the underlying update task is still queued. Worse, killing it mid-install can corrupt the update and trigger a rollback. The correct approach is to let the current update finish or to stop the Windows Update service cleanly first, then clear the update cache so TiWorker has nothing broken to chew on."
  - q: "Do HP utilities make TiWorker.exe worse?"
    a: "Indirectly, yes. HP Support Assistant can queue large driver packages through Windows Update, giving TiWorker much more work per update cycle. Outdated HP drivers that fail to install also cause TiWorker to retry repeatedly. Keeping HP Support Assistant and HP drivers current reduces both the workload and the retry loops that keep CPU pinned."
---

Open Task Manager on your HP laptop during a Windows Update and one process dominates the list: TiWorker.exe, the Windows Modules Installer Worker, chewing through 50, 80, sometimes nearly 100 percent of your CPU. The fans spin up, the machine feels sluggish, and the natural instinct is that something is wrong. Most of the time, nothing is — TiWorker is doing exactly the heavy lifting updates require.
The process becomes a genuine problem when the high CPU never ends. Hours pass, the update shows no progress, and TiWorker keeps grinding. On HP laptops this pattern often traces back to a stuck update package, a corrupted component store, or HP-queued driver updates that fail and retry in a loop. The fix is not to kill the process but to unstick whatever it is working on.
Below is the technician's sequence: how to tell normal TiWorker activity from a stuck one, how to calm it safely, and how to fix the underlying update problem so it does not recur. HP owners should also keep their drivers current via [HP's support site](https://support.hp.com/us-en), since HP-queued drivers are a frequent hidden workload. If updates are failing outright rather than just grinding, the [update-fails-on-Lenovo guide](/articles/how-to-fix-windows-update-fails-to-install-on-lenovo-laptop/) covers the same repair logic, and the [troubleshooter walkthrough](/articles/how-to-fix-windows-update-with-troubleshooter-on-windows-11/) automates several of these steps.

## Why this happens

- **An update is actively installing.** TiWorker compresses, decompresses, and installs update packages — legitimately CPU-intensive work.
- **The component store is being cleaned.** TiWorker also runs background maintenance that spikes CPU on its own schedule.
- **An update package is stuck.** A corrupted download keeps TiWorker retrying the same failed operation for hours.
- **The component store is corrupted.** Damage in WinSxS forces TiWorker into long, failing repair attempts.
- **HP-queued driver updates are failing.** Large HP driver packages that fail to install trigger repeated TiWorker retry loops.
- **The update cache is damaged.** Bad files in SoftwareDistribution give TiWorker broken input to process.
- **Multiple updates are queued.** A long backlog, common after months without updating, multiplies the workload.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is a real problem, not normal work

TiWorker at high CPU during an active update is expected. Verify the stall before intervening — killing a healthy install causes the very corruption you are trying to avoid.

1. Open Settings > Windows Update and check whether an update is actively downloading or installing.
2. If an update is progressing, give TiWorker up to two hours on an SSD, longer on a hard drive.
3. Open Task Manager > Performance and confirm sustained high CPU with zero update progress over several hours.
4. Only proceed if CPU stays pinned with no update activity, or the same update has been 'installing' all day.

### Fix 2: Stop the update service cleanly

Rather than killing TiWorker directly, stop the service driving it. This halts the work gracefully instead of mid-write.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv` and `net stop bits` to halt the update pipeline.
3. Confirm in Task Manager that TiWorker.exe CPU drops to zero within a minute.
4. Leave the services stopped while you clear the cache in the next fix.

### Fix 3: Clear the corrupted update cache

A damaged download is the most common reason TiWorker grinds forever. Clearing the cache removes the broken package it keeps retrying.

1. With the services stopped, rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
2. Restart the services: `net start wuauserv` and `net start bits`.
3. Reboot the laptop and let Windows Update pull a fresh copy of the package.
4. Watch Task Manager — TiWorker should now show brief spikes, not a permanent plateau.

### Fix 4: Run the Windows Update troubleshooter

The built-in troubleshooter automates the service resets and cache checks, and it is tuned for exactly this stuck-update pattern.

1. Go to Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Windows Update troubleshooter and apply every fix it recommends.
3. Restart the laptop after the troubleshooter completes.
4. Check for updates again and observe TiWorker behavior during the fresh attempt.

### Fix 5: Repair the component store with DISM

When TiWorker struggles with a corrupted WinSxS store, DISM repairs the underlying damage so the worker can finish normally.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and allow 15 to 30 minutes.
3. Follow with `sfc /scannow` to verify system file integrity.
4. Reboot, then retry the update and monitor CPU usage.

### Fix 6: Update HP drivers to stop retry loops

Failing HP driver packages are a classic hidden cause of endless TiWorker activity on HP hardware. Current drivers install cleanly on the first attempt.

1. Open HP Support Assistant and install all pending driver and BIOS updates.
2. Visit [HP's support site](https://support.hp.com/us-en), enter your model, and compare against what is installed.
3. Check the official [Microsoft support guidance](https://support.microsoft.com/en-us/windows) if a specific HP driver update keeps failing.
4. In Device Manager, roll back any driver dated from a failed update attempt before retrying.

### Fix 7: Install updates in smaller batches

A huge backlog after months offline overwhelms TiWorker. Smaller batches let each install complete cleanly.

1. After the cache clear, check for updates and install only the smallest available update first.
2. Reboot between batches rather than stacking everything at once.
3. Connect to AC power and a stable network for each batch — never update on battery.
4. Once caught up, leave automatic updates on so the backlog never rebuilds.

## Closing

TiWorker.exe at high CPU is usually Windows Update doing its job — the red flag is high CPU with no progress for hours. Stop the pipeline cleanly, clear the corrupted cache, repair the component store, and keep HP's drivers current. Treat the worker as a symptom, fix the stuck update underneath it, and the fans will quiet down on their own.
