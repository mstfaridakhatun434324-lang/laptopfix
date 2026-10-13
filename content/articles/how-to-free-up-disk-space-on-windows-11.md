---
title: "Low Disk Space in Windows 11? Free Up Gigabytes Fast"
slug: how-to-free-up-disk-space-on-windows-11
date: 2026-10-04
categories: ["performance"]
tags: ["disk space", "windows 11", "storage", "disk cleanup", "free up space"]
description: "Running out of disk space on Windows 11? Reclaim gigabytes safely with Storage Sense, Disk Cleanup, and smart cleanup of temp files, caches, and unused apps."
thumbnail: "/images/thumbs/how-to-free-up-disk-space-on-windows-11.webp"
faqs:
  - q: "How much free disk space does Windows 11 need?"
    a: "Aim to keep at least 15 to 20 percent of your system drive free, with an absolute minimum of 10 GB. Windows needs room for update staging, the pagefile, hibernation data, and temporary files, and SSDs slow down noticeably when nearly full. If your C: drive shows a red bar in File Explorer or updates fail with error 0x80070070, you are past the safe threshold and should free space immediately."
  - q: "Is it safe to delete everything Disk Cleanup finds?"
    a: "Mostly yes, but review the list before confirming. Temporary files, thumbnails, DirectX shader cache, and Delivery Optimization files are safe to remove. Be cautious with Downloads, since Disk Cleanup can include it, and only remove Previous Windows installations if you are sure you will not roll back within ten days. Device driver packages and Windows Update Cleanup are generally safe once your system is running stably."
  - q: "Why does my disk fill up again so quickly?"
    a: "The usual repeat offenders are Windows Update staging files, Delivery Optimization uploads shared to other PCs, hibernation data equal to your RAM size, restore points accumulating, and applications with ever-growing caches like browsers and chat apps. Enabling Storage Sense to run automatically handles most of this. If space vanishes overnight, check for a stuck update or a runaway log file in a specific folder."
  - q: "Should I disable hibernation to save disk space?"
    a: "Disabling hibernation deletes hiberfil.sys, which can free several gigabytes equal to a large portion of your RAM, and it is safe on desktops and laptops that use Sleep or Modern Standby. However, you lose the ability to hibernate, which protects unsaved work during power loss on battery. On laptops, keep hibernation enabled unless you are critically short on space and understand the tradeoff."
---

That red bar next to your C: drive in File Explorer is Windows 11's way of telling you things are about to get worse. A nearly full system drive doesn't just mean you can't install new apps — it causes failed updates, sluggish performance, app crashes, and eventually a machine that refuses to boot properly. The good news: on most laptops, 15–40 GB of reclaimable space is hiding in plain sight in temporary files, old updates, caches, and apps you forgot existed.

Windows genuinely needs breathing room. Between update staging, the pagefile, hibernation data, and SSD over-provisioning, a drive that's 95% full will perform worse than the same drive at 70% — and feature updates can fail outright with error 0x80070070 ("not enough disk space") even when they theoretically need less than what's free. The goal isn't a pristine drive; it's getting back to a comfortable 15–20% free so Windows can do its job.

This guide walks through the safe, high-yield cleanup sources in order of impact: what's actually eating your space, the built-in cleaners, the big-ticket items like hibernation and old Windows installs, and habits that keep the drive from filling up again. If your laptop is slow for other reasons too, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); for trimming preinstalled junk, check [removing bloatware from your laptop](/articles/how-to-remove-bloatware-from-windows-11-laptop/).

## Why this happens

- **Windows Update staging and leftovers**: Downloaded updates, rollback data, and Delivery Optimization cache pile up over time.
- **The hibernation file**: hiberfil.sys reserves disk space roughly equal to your RAM — 16 GB of RAM means ~16 GB of disk.
- **Temporary files and caches**: App temp files, browser caches, thumbnail caches, and installer leftovers accumulate silently.
- **System restore points**: Each restore point snapshots system files; several of them can consume tens of gigabytes.
- **Old Windows installations**: After a feature update, Windows.old keeps your previous install for rollback — often 20–30 GB.
- **Unused apps and games**: A few forgotten games or creative suites can eat 50+ GB without you noticing.
- **User data growth**: Downloads folders, desktop clutter, and duplicated files grow steadily on every machine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find out what's actually eating the space

Don't delete blindly — get a map first.

1. Open **Settings** > **System** > **Storage** and wait for the breakdown to load — it shows Apps, Temporary files, Documents, and Other by size.
2. Click **Temporary files** to see the itemized list with sizes (this is the safest cleanup screen in Windows).
3. For a visual map, install the free **WizTree** (portable, no install needed) — it scans in seconds and shows exactly which folders are the hogs. Delete only inside folders you understand.
4. Check your **Downloads**, **Desktop**, and **Documents** folders manually — sort by size to spot forgotten ISOs, installers, and video files.
5. Note the top 3 space consumers before touching anything; that tells you which fixes below matter most. If the System drive is small by design (128 GB eMMC), every gigabyte counts double.

### Fix 2: Run Storage Sense and Disk Cleanup

The built-in tools handle the easy wins safely.

1. In **Settings** > **System** > **Storage**, turn on **Storage Sense** and click it to configure: set it to run automatically, delete temp files apps aren't using, and clean the Recycle Bin and Downloads folder on your chosen schedule.
2. Click **Run Storage Sense now** for an immediate cleanup.
3. For the deeper pass, open **Disk Cleanup** (search it in Start), select C:, then click **Clean up system files** — this reveals Windows Update Cleanup, Previous Windows installations, and Device driver packages.
4. Check **Temporary files**, **Thumbnails**, **DirectX Shader Cache**, **Delivery Optimization Files**, and **Recycle Bin**. Review **Downloads** carefully before checking it.
5. If you've been on your current Windows version more than a few weeks and everything works, check **Previous Windows installation(s)** — this alone often frees 20–30 GB. See Microsoft's official guidance on [freeing drive space in Windows](https://support.microsoft.com/en-us/windows) for the full walkthrough.

### Fix 3: Clear caches apps leave behind

App caches rebuild themselves — safe to purge.

1. Press **Win + R**, type `%temp%`, and delete everything Windows allows (skip files in use — that's normal).
2. Do the same with `temp` (system temp folder) — you'll need admin approval for some items.
3. Clear browser caches: in Chrome/Edge, **Settings** > **Privacy** > **Clear browsing data** > **Cached images and files**. Browser caches can quietly reach several gigabytes.
4. Empty the **Recycle Bin** — files you "deleted" still occupy disk until you do.
5. Check chat and creative apps (Teams, Discord, Adobe) — many keep multi-gigabyte caches in `%appdata%`; most have a cache-clear option in their own settings.

### Fix 4: Uninstall what you don't use

Apps are the biggest single category on most laptops.

1. Go to **Settings** > **Apps** > **Installed apps**, sort by **Size**, and look at the top of the list.
2. Remove games you finished, trial software, duplicate utilities, and apps you installed "to try once."
3. Tackle preinstalled bloatware: manufacturer utilities you never open, extra antivirus trials, and game launchers for stores you don't use.
4. For stubborn apps that don't offer uninstall, the Microsoft Store versions can be removed from the same list.
5. Reboot after a big uninstall round — some space only frees after pending operations complete.

### Fix 5: Move personal files off the system drive

Keep C: for Windows and apps; bulk data belongs elsewhere.

1. If you have a second drive or partition, move your **Videos**, large photo libraries, and game installs there (Steam lets you add a library folder on another drive in **Settings** > **Storage**).
2. Enable **OneDrive Files On-Demand**: right-click the OneDrive cloud icon > **Settings** > **Sync and backup** > **Advanced settings** — files stay visible but download only when opened, freeing local space.
3. In OneDrive, right-click big folders you rarely open > **Free up space** to convert them to online-only immediately.
4. Consider relocating your default **Downloads** and **Documents** folders: right-click the folder > **Properties** > **Location** tab > **Move**.
5. Don't move the Windows folder, Program Files, or AppData — relocating system folders breaks things.

### Fix 6: Reclaim the big hidden space hogs

Hibernation, restore points, and old updates are the heavy hitters.

1. Check hibernation: open an admin terminal and run `powercfg /hibernate off` to delete hiberfil.sys (frees GBs equal to much of your RAM). Run `powercfg /hibernate on` to re-enable if you miss it — see the tradeoff discussion in the FAQ above.
2. Trim restore points: search **Create a restore point**, click **Configure**, and either lower the **Max Usage** slider to 3–5% or delete all but the latest point via Disk Cleanup > **More Options** > **System Restore and Shadow Copies** > **Clean up**.
3. Shrink the WinSxS component store: in an admin terminal, run `Dism.exe /online /Cleanup-Image /StartComponentCleanup` — safe, Microsoft-supported, and can free several GB.
4. Clear Delivery Optimization cache: **Settings** > **Windows Update** > **Advanced options** > **Delivery Optimization** > review settings and clear the cache; consider limiting upload bandwidth to other PCs.
5. Empty **C:\Windows\SoftwareDistribution\Download** only if Windows Update is stuck — stop the Windows Update service first, delete the contents, restart the service.

### Fix 7: Keep it from filling up again

Cleanup is a one-time win; habits keep it that way.

1. Leave **Storage Sense** on with automatic scheduling — it's the single best set-and-forget defense.
2. Uninstall apps the moment you're done with them instead of "maybe later."
3. Store large media on external drives or cloud storage with Files On-Demand rather than on C:.
4. Watch out for apps with runaway logging — if space vanishes suddenly, WizTree shows which folder ballooned.
5. Check **Settings** > **System** > **Storage** monthly — two minutes of review catches problems before the red bar returns.

## Closing

Freeing disk space on Windows 11 is mostly about knowing where Windows hides the bodies: temp files, old updates, hibernation data, restore points, and forgotten apps account for nearly everything. Work through the list above, get back to a healthy 15–20% free, and let Storage Sense handle the maintenance. Your updates will install cleanly, your SSD will thank you, and that red bar will stay gone.
