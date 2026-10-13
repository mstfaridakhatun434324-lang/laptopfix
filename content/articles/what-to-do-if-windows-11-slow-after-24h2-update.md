---
title: "Windows 11 Slow After the 24H2 Update? Here's What to Do"
slug: what-to-do-if-windows-11-slow-after-24h2-update
date: 2026-09-27
categories: ["performance"]
tags: ["windows 11 24h2", "slow after update", "windows update", "performance"]
description: "Windows 11 feels sluggish after installing the 24H2 update? Work through the real causes — from re-indexing to driver conflicts — and get your speed back."
thumbnail: "/images/thumbs/what-to-do-if-windows-11-slow-after-24h2-update.webp"
faqs:
  - q: "How long does Windows 11 stay slow after the 24H2 update?"
    a: "Some slowness for 24 to 72 hours after a feature update is normal: Windows re-indexes search, Defender rescans the system, and the .NET framework re-optimizes apps in the background. If the laptop is still noticeably slow after three days of regular use and several reboots, something is genuinely wrong — usually a driver conflict, a stuck update component, or a corrupted system file — and the steps in this guide apply."
  - q: "Should I roll back the 24H2 update if my laptop is slow?"
    a: "Rollback is a last resort, not a first step, because you have only 10 days after installing 24H2 before Windows deletes the old system files. Most post-update slowness is fixable without rolling back: updating drivers, clearing the update cache, and repairing system files resolve the majority of cases. Roll back only if a specific hardware function broke and no driver update fixes it."
  - q: "Why is my disk at 100% after installing 24H2?"
    a: "After a feature update, Windows Search rebuilds its entire index, Defender runs a full baseline scan, and Superfetch (SysMain) re-learns your app patterns — all disk-heavy jobs that can overlap. This usually settles within a day or two. If 100% disk persists beyond that, disable SysMain, check for a stuck Windows Update component, and run chkdsk to rule out drive problems."
  - q: "Can outdated drivers cause slowness after 24H2?"
    a: "Yes, driver conflicts are the most common real cause of lasting post-update slowness. Feature updates replace core OS components, and old storage, chipset, or graphics drivers may not cooperate with the new code — causing stutters, slow boot, and high CPU from driver processes. Updating chipset and storage drivers from your laptop manufacturer's support site fixes most of these cases."
---

Feature updates are supposed to make Windows better, but the 24H2 update has left plenty of laptops feeling slower than before — long boots, stuttering apps, fans working overtime. Some of that is temporary housekeeping: after a big update, Windows re-indexes your files, Defender rescans everything, and background optimizers run for a day or two. But when the slowness sticks around past the first few days, it's a real problem with a real cause.

The usual culprits are driver conflicts (old drivers meeting new OS code), corrupted update components, and re-indexing jobs that never finish. Work through this guide in order: give legitimate background work a chance to finish first, then fix what's actually stuck. For update-specific recovery steps, see [fixing Windows 11 slowness after updates](/articles/windows-11-slow-after-update-how-to-fix/); for a step-by-step walkthrough of the broader case, [laptop slow after the 24H2 update](/articles/how-to-fix-laptop-slow-after-windows-11-24h2-update-step-by-step/).

## Why this happens

- **Background re-indexing**: Windows Search rebuilds its full index after 24H2, hammering disk and CPU for a day or more.
- **Driver incompatibility**: Old chipset, storage, or graphics drivers clash with the updated OS kernel.
- **Defender re-baselining**: Microsoft Defender runs deep scans after feature updates to re-establish its baseline.
- **Stuck update components**: A partially failed update leaves Windows Update or servicing processes looping.
- **Corrupted system files**: The update process itself can damage system files, causing general instability and slowness.
- **Re-enabled bloat and startup items**: Feature updates sometimes re-enable disabled startup apps and reinstall bloatware.
- **Power plan reset**: Updates occasionally reset your power plan, dropping the laptop back to balanced or power-saver behavior.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give legitimate background work time to finish

Don't start surgery while Windows is still doing normal post-update housekeeping.

1. Open **Settings** > **Windows Update** and confirm 24H2 shows as fully installed with no pending restarts.
2. Open **Task Manager** > **Processes** and look for `SearchIndexer.exe`, `MsMpEng.exe`, or `TiWorker.exe` — these are the normal post-update workers.
3. Use the laptop normally (plugged in) for 2–3 days, rebooting once daily — most background jobs finish within 72 hours.
4. If after three days the same processes are still hammering CPU or disk, they're stuck, not working — move to the fixes below.
5. Check **Settings** > **Privacy & security** > **Searching Windows** > **Find my files** — consider switching to Classic indexing to permanently reduce this load.

### Fix 2: Update chipset, storage, and graphics drivers

The single most effective fix for lasting post-update slowness.

1. Identify your laptop's exact model (check the sticker underneath or run `msinfo32`).
2. Visit your manufacturer's support site — Dell, HP, or Lenovo — and download the latest **chipset**, **storage/IRST**, and **BIOS** drivers for Windows 11 24H2.
3. Install chipset drivers first, then storage, then reboot.
4. Update graphics drivers from your GPU maker's download page: NVIDIA, AMD, or Intel all publish Windows 11 24H2-ready drivers — avoid relying on the older copy Windows Update installed.
5. Reboot and compare: driver-related stutters and slow boots usually vanish immediately.

### Fix 3: Repair the Windows Update components

Clear out stuck update machinery that's looping in the background.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** and run the **Windows Update** troubleshooter.
2. Open **Command Prompt as administrator** and run: `net stop wuauserv`, `net stop bits`, then rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
3. Restart the two services: `net start wuauserv`, `net start bits` — Windows rebuilds the update cache cleanly.
4. Go to **Settings** > **Windows Update** > **Check for updates** and install any new cumulative updates — Microsoft ships post-24H2 performance fixes regularly.
5. Reboot once more and watch Task Manager for 15 minutes to confirm `TiWorker.exe` and `wuauclt` have settled.

### Fix 4: Repair corrupted system files

Fix damage the update process itself may have caused.

1. Open **Command Prompt as administrator**.
2. Run `sfc /scannow` and wait for it to complete — this repairs protected Windows files.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the component store that SFC draws from.
4. If DISM reports it fixed corruption, run `sfc /scannow` once more to confirm everything is clean.
5. Reboot and test the specific slowness (boot time, app launches) — file corruption causes exactly the vague, general sluggishness people report after 24H2.

### Fix 5: Re-trim startup apps and bloat the update re-enabled

Feature updates love to undo your cleanup work.

1. Open **Task Manager** > **Startup apps** and disable everything you had disabled before — updates frequently re-enable updaters, launchers, and OEM utilities.
2. Open **Settings** > **Apps** > **Installed apps**, sort by install date, and remove any bloatware the update reinstalled.
3. Check **Settings** > **System** > **Power & battery** > **Power mode** — set it back to **Best performance** if the update reset it.
4. Run a full guide pass with [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) to make sure nothing was missed.
5. Reboot and time your boot — a cleaned startup list often cuts 30–60 seconds off post-update boot times.

### Fix 6: Roll back the update (within 10 days)

When nothing else works and the timeline fits, go back.

1. Open **Settings** > **System** > **Recovery** > **Go back** — this option only exists for 10 days after installing 24H2.
2. Follow the wizard, choosing to keep your files; Windows restores the previous build.
3. After rollback, immediately pause updates for a few weeks: **Settings** > **Windows Update** > **Pause updates**.
4. Use the pause window to check your manufacturer's site for 24H2-ready drivers before trying again.
5. If the 10-day window has passed, your options are a repair install (in-place upgrade from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)) or a clean install.

### Fix 7: Do a repair install as a final refresh

Reinstall Windows without losing files when rollback isn't available.

1. Download the Windows 11 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO, run `setup.exe`, and choose **Keep personal files and apps**.
3. Let the in-place upgrade complete — this reinstalls all OS files while preserving your data and programs.
4. Reinstall drivers from the manufacturer afterward, since the repair can reset some to generic versions.
5. This resolves nearly all lingering post-update weirdness short of hardware failure.

## Closing

Post-24H2 slowness is usually temporary background work or a driver mismatch — both fixable without drastic measures. Give the background jobs their 72 hours, update your drivers from the manufacturer, repair what's corrupted, and only roll back if the timeline allows and nothing else helped. Most laptops come out of this process faster than they were before the update.
