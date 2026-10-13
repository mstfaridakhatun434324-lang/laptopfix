---
title: "Low Disk Space on Your C Drive? A Technician's Cleanup Playbook"
slug: troubleshoot-low-disk-space-on-c-drive
date: "2026-10-09"
categories: ["performance"]
tags: ["low disk space", "c drive", "disk cleanup", "storage", "windows 11"]
description: "Getting low disk space warnings on the C drive? This technician's playbook finds the hidden space hogs and reclaims gigabytes safely."
thumbnail: "/images/thumbs/troubleshoot-low-disk-space-on-c-drive.webp"
faqs:
  - q: "How much free space should I keep on the C drive?"
    a: "Aim for at least 10 to 15 percent of the drive free, or a minimum of 20 GB on modern installations. Below that threshold, Windows cannot manage its paging file, updates fail to install, and performance drops sharply. If you are under 10 GB free, treat it as urgent — large Windows updates need several gigabytes of working room to install safely."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, if you do it through Disk Cleanup rather than deleting the folder manually. Windows.old holds your previous Windows installation for rollback purposes and can consume 15 to 30 GB. After about ten days, Windows removes it automatically, but you can reclaim the space sooner via Disk Cleanup's 'Clean up system files' option."
  - q: "Why does my C drive fill up again after I free space?"
    a: "Usually one of three culprits: Windows Update staging large downloads, a runaway log file or app cache, or System Restore points accumulating. Check Settings, then System, then Storage to see the breakdown by category. If 'Temporary files' keeps growing, schedule automatic cleanup so the drive maintains itself instead of needing manual rescues."
  - q: "Can low disk space actually slow down my laptop?"
    a: "Yes, noticeably. A nearly full system drive starves the paging file, slows temp file operations, prevents proper defragmentation or SSD optimization, and blocks updates that contain performance fixes. Freeing space is one of the highest-return performance tweaks on an older laptop because it removes several bottlenecks at once."
---

That red bar in File Explorer is Windows waving a warning flag. Low disk space on the C drive is not just an annoyance — it is a performance problem and a reliability risk rolled into one. Windows needs breathing room on its system drive for the paging file, temporary files, and the staging area that feature updates use. When free space drops toward zero, updates fail, apps crash, and the whole machine slows to a crawl.

The tricky part is that the space rarely disappears because of your documents. On most laptops I have serviced, the biggest consumers are invisible: old Windows installations, update caches, hibernation files, restore points, and application caches that never clean up after themselves. The fix is methodical — find the real hogs, remove them safely, and set up automation so the drive stays healthy.

## Why this happens

- **Windows.old leftovers** — every major upgrade keeps the old installation for rollback, costing 15–30 GB until it auto-deletes.
- **Update download cache** — Windows Update stages installers in SoftwareDistribution; failed updates can leave gigabytes behind.
- **Hibernation file (hiberfil.sys)** — typically 40 percent of installed RAM, reserved on the system drive even if you never hibernate.
- **System Restore points** — each snapshot consumes space, and Windows keeps several unless you cap the allocation.
- **Application caches** — browsers, game launchers, and creative apps accumulate multi-gigabyte caches with no self-cleaning.
- **User profile bloat** — the Downloads folder, desktop, and app data (especially Teams, Discord, and Electron apps) quietly grow.
- **Recycle Bin and temp files** — deleted files sit in the bin, and temp folders accumulate leftovers from installers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See exactly what is eating the space

Guessing wastes time. Windows 11 has a built-in storage map that shows the biggest categories in seconds.

1. Open **Settings → System → Storage** and wait for the scan to finish.
2. Note the top three categories — usually **Temporary files**, **Apps & features**, or **System & reserved**.
3. Click **Temporary files**, check every category except **Downloads** (review that one manually), and click **Remove files**.
4. Click **Show more categories** to see per-folder usage if something looks odd.
5. For a visual map, install the free **WizTree** or **WinDirStat** portable app and scan the C: drive — the treemap makes giant folders obvious.

Write down what you find before deleting anything; knowing the culprit keeps you from repeating this cleanup monthly.

### Fix 2: Run Disk Cleanup with system files

The classic Disk Cleanup tool still removes categories the Settings page misses, including old Windows installations.

1. Search for **Disk Cleanup** in the Start menu and run it as administrator.
2. Select the **C:** drive, then click **Clean up system files**.
3. Check **Previous Windows installation(s)**, **Windows Update Cleanup**, **Delivery Optimization Files**, and **Device driver packages**.
4. Click **OK**, confirm the deletion, and let it finish — this can take 10–20 minutes.
5. Restart the laptop afterward and re-check free space in File Explorer.

This single step commonly reclaims 10–30 GB on machines that have been through a feature update. For more options, see how to [free up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/) with the full toolkit.

### Fix 3: Shrink or disable the hibernation file

If you never hibernate your laptop, hiberfil.sys is dead weight — often 6–16 GB on machines with 16–32 GB of RAM.

1. Open **Terminal (Admin)** or **Command Prompt (Admin)**.
2. To disable hibernation entirely, run `powercfg /hibernate off` — this also removes Fast Startup.
3. If you want hibernation but a smaller file, run `powercfg /hibernate /size 50` to halve it instead.
4. Verify the freed space in File Explorer immediately — the file is deleted the moment the command succeeds.
5. Note that disabling hibernation also disables Fast Startup; on an SSD the boot-time difference is negligible.

Only do this if you shut down or sleep your laptop normally — hibernation matters most for machines left unplugged for days.

### Fix 4: Cap System Restore disk usage

System Restore is worth keeping, but its default space allocation is generous and restore points accumulate.

1. Search for **Create a restore point** and open the System Protection tab.
2. Select the **C:** drive and click **Configure**.
3. Drag the **Max Usage** slider down to about **5 percent** of the drive.
4. Click **Delete** to remove all existing restore points, then click **Create** to make one fresh point right now.
5. Confirm protection is still **On** — you want one good restore point, not twenty stale ones.

This typically frees several gigabytes while keeping the safety net intact.

### Fix 5: Hunt down application caches and giant folders

With the system categories handled, the remaining space is usually in your own profile or app data.

1. Check **Downloads** and move installers, ISOs, and videos you have already watched to an external drive.
2. Clear browser caches: in Edge or Chrome, open **Settings → Privacy → Clear browsing data** and remove cached images and files.
3. Uninstall apps you have not opened in months via **Settings → Apps → Installed apps**, sorted by size.
4. Check game launchers (Steam, Epic) for shader caches and unused games — these are frequent multi-gigabyte offenders.
5. Empty the **Recycle Bin** — right-click it and choose **Empty Recycle Bin**, since "deleted" files still occupy space.

Work through this list once a quarter and the drive will stay healthy. Microsoft's own guidance on freeing space is documented in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Move user folders to another drive

If your laptop has a second drive or partition, relocating bulky user folders is a permanent fix rather than a recurring chore.

1. Create folders like `D:\Documents`, `D:\Downloads`, and `D:\Pictures` on the larger drive.
2. Right-click your **Documents** folder, choose **Properties → Location**, and point it at the new folder.
3. Repeat for Downloads, Pictures, Videos, and Music.
4. When prompted, choose **Yes** to move existing files so nothing is left behind.
5. Confirm the C: drive shows the freed space, then restart to make sure nothing references the old paths.

This is especially effective on laptops with a small SSD for Windows plus a larger HDD for data.

### Fix 7: Enable Storage Sense for automatic maintenance

Manual cleanups fail because people forget. Storage Sense does the routine work on a schedule you set once.

1. Go to **Settings → System → Storage** and toggle **Storage Sense** on.
2. Click **Storage Sense** to open its settings and set it to run **Every week**.
3. Enable **Delete temporary files that my apps aren't using**.
4. Set **Delete files in my recycle bin if they have been there for over 30 days**.
5. Do the same for the **Downloads** folder if you treat it as a temporary staging area.

For a more thorough automated approach, you can [schedule Disk Cleanup on your laptop](/articles/how-to-schedule-disk-cleanup-on-laptop/) with Task Scheduler for categories Storage Sense does not touch.

## Closing

Low disk space on the C drive is almost always fixable in under an hour: map the usage, clear system leftovers with Disk Cleanup, tame hibernation and restore points, and let Storage Sense handle the future. The goal is not just to silence the warning — it is to keep 15 percent or more of the drive free at all times, because that headroom is what keeps Windows fast, updates installing, and your data safe.
