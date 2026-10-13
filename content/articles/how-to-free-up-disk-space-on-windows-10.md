---
title: "Free Up Disk Space on Windows 10: Reclaim Gigabytes Safely"
slug: how-to-free-up-disk-space-on-windows-10
date: 2026-09-11
categories: ["performance"]
tags: ["disk space", "windows 10", "disk cleanup", "storage sense", "c drive full"]
description: "Windows 10 C: drive filling up? Free gigabytes safely with Disk Cleanup, Storage Sense, and targeted cleanup of update leftovers and caches."
thumbnail: "/images/thumbs/how-to-free-up-disk-space-on-windows-10.webp"
faqs:
  - q: "How do I free up the most disk space quickly on Windows 10?"
    a: "The biggest quick wins are Disk Cleanup as administrator (Windows Update Cleanup and Previous Windows installations often total 15-30 GB), emptying the Recycle Bin, clearing Delivery Optimization files, and moving large games or media off C:. Run Disk Cleanup with 'Clean up system files' first — it routinely finds more in one pass than hours of manual hunting through folders."
  - q: "What is Storage Sense and should I turn it on?"
    a: "Storage Sense is Windows 10's automatic cleanup: it deletes temporary files, empties the Recycle Bin on a schedule, and can offload unused OneDrive files to cloud-only. Turn it on at Settings > System > Storage > Storage Sense and configure it to run monthly. It's the 'set and forget' answer to gradual disk fill — the manual cleanups in this guide handle the backlog, Storage Sense prevents the next one."
  - q: "Is it safe to delete files in the Temp folder?"
    a: "Yes — files in C:\\Windows\\Temp and your user Temp folder (%TEMP%) are by definition temporary, and Windows and apps recreate what they need. The safe method is Disk Cleanup or Storage Sense rather than manual deletion, because they'll skip files currently in use. If you delete manually, skip any file Windows says is in use rather than forcing it."
  - q: "Why is the WinSxS folder so big and can I shrink it?"
    a: "WinSxS (C:\\Windows\\WinSxS) stores component versions Windows needs for updates, rollback, and optional features — it looks huge in Explorer but much of it is hard links counted multiple times. Never delete it manually. Shrink it safely with Disk Cleanup as administrator > 'Windows Update Cleanup' and the 'StartComponentCleanup' scheduled task, which remove superseded components properly."
---

Windows 10 machines have had years to accumulate digital sediment: update leftovers from a dozen feature updates, a Windows.old or three, gigabytes of temp files, and app caches from software installed in 2019. When C: turns red, everything degrades — updates fail, virtual memory chokes, and the system slows in ways that feel like aging hardware but are really just a full disk. The fix is a proper cleanup, Windows 10 style.

This guide uses Windows 10's actual tools and paths (Disk Cleanup, Storage Sense, the Settings > System > Storage breakdown) to reclaim space safely, ordered from biggest wins to ongoing prevention. For the Windows 11 version with its slightly different UI, see [low disk space on C: drive](/articles/what-to-do-if-low-disk-space-on-c-drive/).

## Why this happens

- **Feature update leftovers**: Each Windows 10 feature update leaves superseded components and possibly Windows.old.
- **Windows Update Cleanup backlog**: Never-run Disk Cleanup letting servicing files pile for years.
- **Temp file accumulation**: App and system temp folders growing without bound.
- **Recycle Bin as archive**: Deleted-but-not-emptied files still consuming disk.
- **Delivery Optimization cache**: Update files stored for peer sharing.
- **Restore points**: System Protection snapshots with generous default allocation.
- **Hibernation file**: hiberfil.sys sized to RAM on machines that never hibernate.
- **User data sprawl**: Downloads folders full of ancient installers and ISOs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Map the usage with Storage settings

Aim the cleanup at the big categories.

1. Open **Settings** > **System** > **Storage** — click **Show more categories** to see the full breakdown: Apps & features, Temporary files, System & reserved, and the rest.
2. Click **Temporary files** — check every safe box: **Windows Update Cleanup**, **Delivery Optimization Files**, **Temporary files**, **Recycle Bin**, **Thumbnails**, **DirectX Shader Cache**. Note the total before clicking **Remove files**.
3. Check **Apps & features**, sort by **Size** — the top entries are candidates for moving or uninstalling (Fix 5).
4. For a visual treemap of the whole drive, run the free **WizTree** — it scans in seconds and exposes the forgotten 30 GB folder nothing else shows clearly.
5. Record free space before/after each step — the running total is satisfying and tells you which steps matter most on your machine.

### Fix 2: Disk Cleanup as administrator (the heavy lifter)

The tool that finds what Settings misses.

1. Search Start for **Disk Cleanup** > right-click > **Run as administrator** > select **C:**.
2. Click **Clean up system files** > select C: again — now check **Windows Update Cleanup** (often 5-15 GB on neglected machines), **Previous Windows installation(s)** (Windows.old, 15-30 GB — only if you're stable and past needing rollback), **Device driver packages**, **Delivery Optimization Files**.
3. Click **OK** > **Delete Files** — Update Cleanup can take 15+ minutes; let it finish.
4. Go to the **More Options** tab > **System Restore and Shadow Copies** > **Clean up** — removes all but the latest restore point. (Check Fix 4 first if you depend on restore points.)
5. One admin Disk Cleanup pass routinely reclaims 15-40 GB on machines that have never had it — it's the highest-value 20 minutes in Windows maintenance.

### Fix 3: Enable and configure Storage Sense

Automate so this never happens again.

1. **Settings** > **System** > **Storage** > turn **Storage Sense** **On** > click **Configure Storage Sense or run it now**.
2. Set **Run Storage Sense** to **Every month** (or **During low free disk space** for chronic cases).
3. Under **Temporary Files**: check **Delete temporary files that my apps aren't using**, set Recycle Bin deletion to **30 days** (or 14 if you're disciplined), and set Downloads cleanup only if you don't archive in Downloads.
4. Under **OneDrive** (if applicable): enable **cloud-backed content** offloading — files you haven't opened recently become online-only placeholders, freeing real disk.
5. Click **Clean now** for an immediate first run, then forget about it — that's the point. Pair with the broader [Windows 11 disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/) concepts if you manage mixed-version machines.

### Fix 4: Shrink hibernation, restore points, and pagefile

The big system files nobody looks at.

1. Check hiberfil.sys: enable hidden items in Explorer and look at `C:\hiberfil.sys` — roughly 40-75% of your RAM. If you never hibernate: elevated Command Prompt > `powercfg /hibernate off` deletes it entirely (also disables Fast Startup — fine on most desktops, think twice on laptops).
2. Prefer keeping hibernation but smaller: `powercfg /hibernate /size 50` halves it.
3. System Protection: search Start for **Create a restore point** > select C: > **Configure** — reduce **Max Usage** to ~5% and **Delete** old points if they're eating tens of GB.
4. Pagefile: **SystemPropertiesPerformance.exe** > **Advanced** > **Virtual memory** > **Change** — if C: is critically full and you have a D: drive, move it (C: > **No paging file** > Set; D: > **System managed size** > Set). Never disable it entirely.
5. Restart after pagefile changes. These three tweaks commonly free 10-25 GB combined.

### Fix 5: Move or remove the giants

Structural fixes for drives that fill again.

1. **Games**: Steam > Settings > Storage > create a D: library and move games (50-150 GB each). Other launchers have similar move options — two moved games often solve the crisis permanently.
2. **Large apps**: **Settings** > **Apps** > **Apps & features** > sort by size — uninstall what you don't use; for Store apps, **Move** to another drive where offered.
3. **User folders**: right-click **Downloads** (and Documents/Pictures if huge) > **Properties** > **Location** > **Move** to D:. Downloads is where installers accumulate for years.
4. **Cloud sync**: relocate OneDrive/Dropbox folders off C: in the client's settings if they're large.
5. **The Downloads purge**: sort Downloads by size, delete ancient installers, ISOs, and zips you've already used — nobody needs the 2021 printer driver setup file.

### Fix 6: Verify and maintain

Lock in the gains.

1. Re-run admin **Disk Cleanup** once more as a final sweep, then check free space: target **15-20% free** or **20-30 GB minimum**.
2. Confirm **Storage Sense** is on with a monthly schedule — this is what keeps Fix 1-5 from being needed again.
3. Glance at **Settings** > **System** > **Storage** quarterly — two minutes, four times a year.
4. If still below target after everything, the drive is genuinely too small — clone to a larger SSD rather than fighting it monthly. Check SSD deals against your laptop's supported form factor on the maker's page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
5. Microsoft's storage guidance for Windows 10 is in the Windows support hub if you need the official documentation.

## Closing

Windows 10 disk cleanup is archaeology: years of updates, temps, and forgotten downloads compressed into one red bar. Disk Cleanup as admin (Fix 2) does the heavy excavation, Storage Sense (Fix 3) prevents re-burial, and moving the giants (Fix 5) fixes the structural problem. An hour here typically returns 20-50 GB — and a C: drive with breathing room makes the whole machine feel younger.
