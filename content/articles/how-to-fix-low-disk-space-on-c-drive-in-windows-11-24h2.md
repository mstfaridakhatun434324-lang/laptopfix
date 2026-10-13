---
title: "Reclaim Space When Your C: Drive Is Full in Windows 11 24H2"
slug: how-to-fix-low-disk-space-on-c-drive-in-windows-11-24h2
date: 2026-10-11
categories: ["performance"]
tags: ["low disk space c drive", "windows 11 24h2", "free up disk space", "c drive full", "storage sense"]
description: "C: drive redlining after the 24H2 update? Clear Windows.old, tame hibernation and restore points, and reclaim tens of gigabytes without deleting your files."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my C: drive suddenly full after the 24H2 update?"
    a: "Feature updates keep a Windows.old folder — often 15 to 30 GB — so you can roll back for 10 days. The update also downloads fresh component stores and temporary files. Running Disk Cleanup with the 'Previous Windows installations' option typically recovers the bulk of it."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you are confident the 24H2 update is stable on your laptop — usually after a week or two of normal use. Delete it through Disk Cleanup, not by hand, so permissions and hard links are handled correctly. After deletion you cannot roll back the update."
  - q: "How much free space should I keep on C:?"
    a: "Aim for 15 to 20 percent of the drive free — on a 256 GB SSD that is roughly 40 to 50 GB. Below 10 percent, Windows struggles: updates fail, the page file cannot grow, and everyday operations slow down. If you are constantly near the line, consider moving user folders to a second drive rather than fighting the same battle monthly."
  - q: "Does Storage Sense actually help?"
    a: "Yes, for maintenance. Storage Sense automatically clears the Recycle Bin, temp files, and stale Downloads on a schedule, which prevents the slow creep back to full. It will not fix a drive that is full today — do the manual cleanup first, then let Storage Sense hold the line."
---

There is a special kind of dread in seeing the C: drive bar turn red in File Explorer. Everything gets slower, Windows Update starts failing with cryptic errors, and some apps refuse to launch at all. After the Windows 11 24H2 update, this became a wave: the update itself parks 15 to 30 GB of rollback files on your drive and does not clean up after itself.

The good news is that a 'full' C: drive is usually full of things you do not need — old update leftovers, hibernation files, bloated restore points, and temp folders that have been growing for months. You rarely need to delete a single personal file to recover serious space.

This guide targets the big wins first. Follow the order and you can typically reclaim 30 to 60 GB in under half an hour.

## Why this happens

- **Windows.old rollback folder:** The 24H2 update keeps your previous installation — often 15 to 30 GB — for 10 days in case you roll back.

- **Bloated WinSxS component store:** Years of updates accumulate component versions; the store grows until cleaned with DISM.

- **Hibernation file (hiberfil.sys):** Reserves disk space equal to a large chunk of your RAM, even if you never hibernate.

- **System restore points piling up:** Each restore point can be several gigabytes, and old ones linger indefinitely.

- **Temp and delivery optimization files:** Windows Update cache and peer-to-peer delivery files quietly consume gigabytes.

- **Oversized Recycle Bin and Downloads:** Deleted files still occupy space until the bin is emptied; Downloads folders grow unchecked for years.

- **Apps installed to C: by default:** Games and creative apps default to C: and can eat tens of gigabytes each. Our general guide to [freeing up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/) covers app-level cleanup too.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Remove Windows.old with Disk Cleanup

This is the biggest single win after a feature update — often 15 to 30 GB recovered in one operation, safely.

1. Search for Disk Cleanup in Start and run it as administrator.
2. Select the C: drive and click 'Clean up system files'.
3. Select C: again and wait for the scan to finish.
4. Check 'Previous Windows installation(s)' and 'Temporary Windows installation files'.
5. Click OK, then Delete Files, and let it finish — do not interrupt it.
6. Confirm the freed space in File Explorer afterward.

### Fix 2: Shrink the WinSxS component store

The component store holds superseded update files. DISM's cleanup removes the ones Windows no longer needs, often freeing several gigabytes.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /AnalyzeComponentStore` to see how much is reclaimable.
3. Run `DISM /Online /Cleanup-Image /StartComponentCleanup` to clean it.
4. For maximum savings add `/ResetBase`, but note this prevents uninstalling current updates.
5. Wait for completion — it can take 10 to 20 minutes on older drives.
6. Recheck C: free space when done.

### Fix 3: Disable hibernation to delete hiberfil.sys

If you never use hibernate — most laptop users just use sleep — the hibernation file is dead weight equal to a big slice of your RAM.

1. Open Command Prompt as administrator.
2. Run `powercfg /hibernate off` and press Enter.
3. The hiberfil.sys file is deleted immediately — check C: free space.
4. If you ever want hibernate back, run `powercfg /hibernate on`.
5. Note: Fast Startup also uses hibernation mechanics, so disabling it turns Fast Startup off too.
6. On modern SSDs, cold boot is fast enough that most users never miss it.

### Fix 4: Cap System Restore disk usage

Restore points are useful, but unlimited ones are not. Capping their space keeps protection while stopping the slow bleed.

1. Search for 'Create a restore point' in Start and open it.
2. Select the C: drive and click Configure.
3. Move the Max Usage slider to 5 percent — plenty for several restore points.
4. Click Delete to remove all existing restore points, then create one fresh restore point.
5. Click OK to save the new cap.
6. Future restore points will now automatically delete the oldest when the cap is hit.

### Fix 5: Clear delivery optimization and temp files

Windows Update cache and peer-to-peer sharing files accumulate silently. Clearing them is safe — Windows re-downloads anything it still needs.

1. Open Settings, System, Storage, Temporary files.
2. Wait for the scan, then check every category you do not need — especially Delivery Optimization Files and Windows Update Cleanup.
3. Click Remove files.
4. Go to Settings, Windows Update, Advanced options, Delivery Optimization, and turn off 'Allow downloads from other PCs'.
5. Run Disk Cleanup once more to catch anything the Settings page missed.
6. For update-related disk hogs, see [low disk space on C: after the Windows 11 update](/articles/how-to-fix-low-disk-space-on-c-drive-after-windows-11-update/).

### Fix 6: Turn on Storage Sense and move big folders

Manual cleanup fixes today; Storage Sense and folder relocation prevent the problem from returning next month.

1. Open Settings, System, Storage, and turn on Storage Sense.
2. Click Storage Sense and configure it to run weekly, empty the Recycle Bin after 30 days, and clean Downloads of files older than 60 days.
3. Move your Documents, Pictures, and Videos libraries: right-click each folder, Properties, Location tab, Move.
4. Point them at a second drive or partition if you have one.
5. Uninstall apps you no longer use via Settings, Apps, Installed apps, sorted by size.
6. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for the latest Storage Sense options in 24H2.

## Closing

A full C: drive after 24H2 is almost always update leftovers, not your files. Clear Windows.old, trim WinSxS, drop hiberfil.sys if you never hibernate, and cap restore points — then let Storage Sense keep it that way. Your laptop will update cleanly and run noticeably better with breathing room restored.
