---
title: "Update Assistant Stuck at 99%: What to Do Next"
slug: what-to-do-if-update-assistant-stuck-at-99-percent
date: 2026-09-25
categories: ["windows-update"]
tags: ["update assistant", "stuck at 99", "feature update", "windows 11"]
description: "The Windows Update Assistant has been sitting at 99% for hours. Learn when to wait, when to intervene, and how to finish the update safely."
thumbnail: "/images/thumbs/what-to-do-if-update-assistant-stuck-at-99-percent.webp"
faqs:
  - q: "How long should I wait when the Update Assistant is stuck at 99 percent?"
    a: "Give it at least two to three hours on a laptop with a spinning hard drive, and at least one hour on an SSD machine, before touching anything. The 99 percent stage involves final file verification and driver migration, which shows no progress bar movement. Only intervene if the disk activity light is completely dead and the system is unresponsive for over three hours."
  - q: "Is it safe to restart my laptop while the Update Assistant is at 99 percent?"
    a: "A hard restart during the download phase is usually harmless, but during the install phase it can corrupt the update state and trigger a rollback. Check the phase first: if the Assistant still shows downloading or verifying, a restart is low risk. If it shows installing, wait longer, and only force a restart as a last resort."
  - q: "Why does the Update Assistant freeze at 99 percent specifically?"
    a: "The final one percent covers the slowest operations: verifying thousands of downloaded files, migrating drivers, and preparing the offline installation environment. Antivirus scans, low disk space, and a dying hard drive all stretch this phase dramatically. The bar barely moves because these tasks do not report granular progress."
  - q: "Will I lose my files if I cancel the Update Assistant?"
    a: "No. Cancelling or restarting during the Assistant's download and preparation phases does not touch your files or installed programs. Windows only modifies the system during the actual installation phase after a reboot. If a rollback happens, your files remain intact, though you may need to redo the update."
---

Ninety-nine percent is the cruelest number in computing. The Update Assistant crawls to the finish line and then sits there, motionless, while you stare at the screen wondering if anything is happening at all. On a laptop this is even worse, because you cannot tell whether the machine is working hard or has quietly given up.

Here is the technician's rule: at 99 percent, patience is a diagnostic tool. Most stuck assistants are not actually stuck. They are doing the slowest part of the job with the worst progress reporting. Intervening too early turns a slow success into a real failure, and then you get to start the whole download over.

This guide tells you how to tell the difference between slow and stuck, what to check while you wait, and exactly how to recover if the Assistant genuinely will not finish.

## Why this happens

- **File verification is slow:** The Assistant checksums every downloaded package before proceeding, and this shows almost no progress.
- **Driver migration stalls:** Moving drivers into the new build's staging area can hang on one bad driver without any visible error.
- **Antivirus real-time scanning:** Your security software scans each file as it is written, multiplying the time for thousands of small files.
- **Failing hard drive:** A laptop HDD with bad sectors retries reads endlessly at this stage, looking exactly like a freeze.
- **Low disk space:** The Assistant needs working room for extraction. Near-full drives slow the final phase to a crawl.
- **Corrupted download cache:** A damaged package forces silent re-downloads that the progress bar does not reflect.
- **Background Windows Update conflict:** The built-in Windows Update service can fight the Assistant for the same files and locks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it is actually stuck before touching anything

1. Look at the laptop's disk activity light or open Task Manager with **Ctrl + Shift + Esc** and watch the Disk column.
2. If disk usage is bouncing above zero and the Assistant's process is using CPU, it is working. Leave it alone for at least two more hours.
3. Check that the laptop is plugged in and set to never sleep: **Settings > System > Power & battery > Screen and sleep** set to Never while plugged in.
4. Only declare it stuck if there is zero disk activity and zero CPU from the Assistant for a full hour. Patience here saves you from a corrupted update state.

### Fix 2: Pause your antivirus during the final phase

1. Open your antivirus settings and temporarily disable real-time protection. With Windows Security, go to **Virus & threat protection > Manage settings** and toggle off real-time protection.
2. Do not uninstall it at this stage; just pause the scanning so file verification can proceed at full speed.
3. Give the Assistant another 30 to 60 minutes after disabling scanning. Many 99 percent hangs clear within minutes of this change.
4. Re-enable protection as soon as the update completes. If the Assistant was fighting your antivirus, consider the broader [Windows Update service troubleshooting](/articles/windows-update-service-not-running-troubleshooting/) steps after this update finishes.

### Fix 3: Free disk space for the extraction phase

1. The Assistant needs roughly 20 GB of free space to finish comfortably. Check **Settings > System > Storage**.
2. Run Disk Cleanup as administrator: search for it, right-click, choose **Run as administrator**, and clean system files including previous Windows installations if you do not need to roll back.
3. Empty the Recycle Bin and move large personal files to external storage temporarily.
4. Once you have breathing room, the Assistant often resumes on its own within 15 minutes. Do not restart it; just let the freed space unblock the queue.

### Fix 4: Restart the Assistant cleanly if it is genuinely dead

1. Only do this after the Fix 1 waiting period confirms zero activity. Open Task Manager, find **Windows Update Assistant** or `Windows10UpgraderApp.exe`, and end the task.
2. Open **Services** (Win + R, type `services.msc`), restart the **Windows Update** service and the **Background Intelligent Transfer Service**.
3. Delete the Assistant's temporary files: remove the `C:\Windows10Upgrade` folder and clear `C:\$Windows.~BT` if it exists.
4. Re-run the Update Assistant from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11). It will re-download, but the fresh cache usually sails past 99 percent.

### Fix 5: Check the drive health on older laptops

1. A dying hard drive is a classic hidden cause of 99 percent hangs. Open an admin Command Prompt and run `wmic diskdrive get status` for a quick SMART check.
2. For detail, run `chkdsk C: /scan` in an admin PowerShell window and review the output for bad clusters.
3. If errors appear, back up your data immediately before doing anything else. A failing drive plus a major update is a data-loss risk.
4. Consider cloning to an SSD before retrying. The update that took six hours on a failing HDD often finishes in forty minutes on solid state.

### Fix 6: Stop the built-in Windows Update from competing

1. Open **Settings > Windows Update** and pause updates for one week. This stops the background service from locking files the Assistant needs.
2. In Services, set the **Windows Update** service to Manual temporarily while the Assistant runs.
3. Restart the Assistant after making this change so it gets exclusive access to the update pipeline.
4. Remember to unpause updates afterward so you keep receiving security patches. Microsoft documents this interplay on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Switch to the Media Creation Tool instead

1. If the Assistant has failed at 99 percent twice, stop using it. Download the Media Creation Tool and choose **Upgrade this PC now**.
2. The Media Creation Tool uses a different download and staging pipeline that is far less prone to the 99 percent hang.
3. Select **Keep personal files and apps** to preserve everything.
4. This method also helps when the failure cascades into driver errors, which the [0xC1900101 fix guide](/articles/best-way-to-fix-update-fails-with-error-0xc1900101/) covers in depth.

## Closing

A 99 percent hang is almost always slowness in disguise, not a true freeze. Verify activity, pause the antivirus, free disk space, and give it real time before you intervene. When intervention is genuinely needed, a clean restart of the Assistant or a switch to the Media Creation Tool finishes the job.
