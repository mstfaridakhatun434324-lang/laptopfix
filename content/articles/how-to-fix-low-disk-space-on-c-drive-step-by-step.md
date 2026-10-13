---
title: "How to Fix Low Disk Space on the C Drive, Step by Step"
slug: how-to-fix-low-disk-space-on-c-drive-step-by-step
date: 2026-10-03
categories: ["performance"]
tags: ["low disk space", "c drive full", "disk cleanup", "free up space", "windows 11"]
description: "C: drive full? Follow this step-by-step guide to reclaim gigabytes safely — Storage Sense, Disk Cleanup, old Windows installs, and finding the hidden space hogs."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-step-by-step.webp"
faqs:
  - q: "How much free space should I keep on my C: drive?"
    a: "Aim for at least 15 to 20 percent of the drive's capacity free — on a 256 GB drive that means roughly 40 to 50 GB. Below 10 percent, Windows cannot stage updates, manage the page file, or write temporary files efficiently, and the whole system slows down. Treat the low-disk warning as a real performance problem, not just an annoyance."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you are confident you will not roll back the last feature update. Windows.old is the previous Windows installation kept for 10 days as a safety net. After that window — or once you are happy with the update — deleting it via Disk Cleanup's system files option reclaims 15 to 25 GB safely. Never delete it manually from File Explorer."
  - q: "Why does my C: drive fill up again after I clean it?"
    a: "The usual repeat offenders are Windows Update delivery files re-downloading, the Recycle Bin quietly accumulating deletions, cloud sync folders (OneDrive, Dropbox) set to keep files locally, and applications like browsers or chat apps with ever-growing caches. Enable Storage Sense for automatic maintenance and audit which folders grow week over week."
  - q: "Can I just move programs to another drive instead of deleting them?"
    a: "For Microsoft Store apps, yes — Settings lets you move them to another drive. For traditional desktop programs, moving is unreliable because registry entries and shortcuts point to the original location; reinstalling them to the other drive is the safe approach. Games from Steam, Epic, and similar launchers can usually be moved through the launcher's own library settings."
---

The red bar in File Explorer is Windows telling you something important: a full C: drive is not just an inconvenience, it is a performance problem. Updates fail, apps crash on launch, virtual memory chokes, and the whole system gets sluggish. The fix is methodical rather than dramatic — a sequence of safe cleanups that typically reclaims 20 to 60 GB without deleting anything you actually need.

Work through these steps in order. Each one is safe, reversible in effect, and targets a different category of wasted space.

## Why this happens

- **Windows Update leftovers:** Every feature update keeps the old installation (Windows.old) plus delivery optimization files, often consuming 20–30 GB silently.
- **Temporary files accumulate endlessly:** App installers, crash dumps, thumbnail caches, and temp folders grow for months without any automatic cleanup.
- **The Recycle Bin is a hidden second drive:** Deleted files sit in the Recycle Bin consuming space until it is emptied — sometimes tens of gigabytes.
- **Hibernation file reserves gigabytes:** hiberfil.sys typically equals 40 percent of your RAM — on a 16 GB machine that is over 6 GB locked away.
- **System Restore points multiply:** Each restore point snapshots system files, and Windows keeps many of them by default.
- **Cloud sync set to "always keep on this device":** OneDrive, Dropbox, and Google Drive can mirror your entire cloud storage onto the small system drive.
- **App caches grow without limits:** Browsers, chat apps, and creative tools cache gigabytes of data with no built-in ceiling.
- **Page file sized for worst case:** The virtual memory page file can balloon on systems with lots of RAM, eating space for a scenario that rarely occurs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See exactly what is eating the space

1. Open **Settings → System → Storage** and wait for the scan to finish.
2. Click **C:** to see the breakdown: Apps, Temporary files, System & reserved, and Other.
3. Note the two largest categories — they decide which fixes below matter most for you.
4. For a deeper view, install a free disk analyzer like WinDirStat or WizTree (run as admin) to find individual giant files and folders. This diagnosis prevents deleting the wrong things.

### Fix 2: Run Disk Cleanup with system files

1. Search **Disk Cleanup** in Start, right-click it, and choose **Run as administrator**.
2. Select **C:**, then click **Clean up system files** and select C: again.
3. Check **Temporary files**, **Recycle Bin**, **Delivery Optimization Files**, **Temporary Windows installation files**, and **Previous Windows installations**.
4. Click OK. This single pass often reclaims 15–40 GB and is completely safe — it only removes files Windows knows it can regenerate.

### Fix 3: Empty the Recycle Bin properly

1. Right-click the **Recycle Bin** on the desktop and check its reported size before emptying — users are routinely surprised by 10–30 GB sitting there.
2. Click **Empty Recycle Bin** and confirm.
3. To prevent recurrence, right-click the Recycle Bin → **Properties** and reduce its maximum size, or enable the option to delete files immediately (use with caution).
4. Remember that files deleted from external drives and network locations may also route through the bin — check it after big cleanup sessions.

### Fix 4: Turn on Storage Sense for automatic maintenance

1. Go to **Settings → System → Storage → Storage Sense** and toggle it **On**.
2. Click into its settings: set it to run **Every week**, delete temporary files unused by apps, and empty the Recycle Bin after **30 days**.
3. Configure **OneDrive cloud content** to become online-only after 30–60 days unused — this alone can free enormous space on synced machines.
4. Storage Sense prevents the slow re-accumulation that brings the red bar back every few months.

### Fix 5: Reclaim the hibernation file (if you never hibernate)

1. Open an **admin Command Prompt or Terminal**.
2. Run `powercfg /hibernate off` — this deletes hiberfil.sys immediately, freeing RAM-sized space (often 4–8 GB).
3. Note that this also disables **Fast Startup**, which depends on hibernation. If boot times matter to you, weigh the trade-off.
4. To re-enable later, run `powercfg /hibernate on`. This is fully reversible.

### Fix 6: Trim System Restore and the page file

1. Search **"Create a restore point"** → select C: → **Configure** → reduce **Max Usage** to 3–5 percent, and delete all but the most recent restore point.
2. For the page file: **System → About → Advanced system settings → Performance Settings → Advanced → Virtual memory → Change**.
3. If you have 16 GB+ of RAM and rarely max it out, a custom size of **2048–4096 MB** is plenty and frees several gigabytes versus the automatic setting.
4. Do not disable the page file entirely — some applications and crash diagnostics require it to exist. Our [disk space after update guide](/articles/how-to-fix-low-disk-space-on-c-drive-after-windows-11-update/) covers update-specific bloat.

### Fix 7: Move the big personal folders off C:

1. In File Explorer, right-click **Documents**, **Downloads**, **Pictures**, or **Videos** → **Properties → Location** → **Move** to a folder on another drive.
2. For Steam/Epic/GOG libraries, use each launcher's settings to add a library folder on the second drive and move installed games there.
3. Check OneDrive: **OneDrive settings → Sync and backup → Manage backup** — stop backing up Desktop/Documents/Pictures to the cloud copy on C: if space is critical, or set files to online-only.
4. Future downloads: change your browser's download location to the second drive so the C: drive stops refilling. For the full picture on freeing space, see [how to free up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/).

### Fix 8: Uninstall what you do not use

1. Go to **Settings → Apps → Installed apps**, sort by **Size (large to small)**.
2. Uninstall preinstalled trials, old game launchers, duplicate utilities, and apps you have not opened in months.
3. Check for multiple versions of the same runtime (old Java, Visual C++ redistributables from 2015) — but leave redistributables alone unless you are certain; other apps may depend on them.
4. After uninstalling, run Disk Cleanup once more — uninstallers frequently leave temp files behind. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has additional guidance on managing storage.

## Closing

A full C: drive is almost never one big file — it is a dozen small accumulations, each with its own safe fix. Diagnose with Storage settings, sweep with Disk Cleanup, automate with Storage Sense, and move the big personal data off the system drive. Done in this order, the red bar turns blue, updates install cleanly again, and the mysterious slowdowns that came with the full drive disappear with it.
