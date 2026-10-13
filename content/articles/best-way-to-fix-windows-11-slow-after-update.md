---
title: "The Best Way to Fix Windows 11 Slow After an Update"
slug: best-way-to-fix-windows-11-slow-after-update
date: 2026-09-10
categories: ["performance"]
tags: ["slow after update", "windows 11", "windows update", "post-update", "performance"]
description: "Windows 11 slow after the latest update? Work through the proven recovery order: finish the update, roll back drivers, and repair — without panicking."
thumbnail: "/images/thumbs/best-way-to-fix-windows-11-slow-after-update.webp"
faqs:
  - q: "Why is Windows 11 slow right after installing an update?"
    a: "Updates trigger a storm of background work: the search index rebuilds, Defender rescans the changed system, .NET and Store apps re-optimize, drivers get swapped, and telemetry uploads. This post-update churn typically lasts a few hours of plugged-in idle time, then settles. Slowness in the first day after a feature update is normal; slowness persisting past 48 hours is not."
  - q: "Should I uninstall the update that made my PC slow?"
    a: "Not as a first step. Most post-update slowness resolves once background tasks finish or with a driver update. Uninstalling is appropriate when the slowness is severe, persists beyond two days, and correlates exactly with the update — and even then, first check whether the update simply replaced a working driver, which is fixable without removing the update."
  - q: "Can a Windows update break my drivers?"
    a: "Yes — this is the most common real cause of post-update slowness. Feature updates routinely replace vendor GPU, Wi-Fi, and chipset drivers with older inbox versions, or reset custom driver settings. If performance dropped the same day as the update, check Device Manager for driver dates: a GPU driver dated years back after yesterday's update is the smoking gun."
  - q: "How long should I wait before troubleshooting post-update slowness?"
    a: "Give it one full cycle: a restart, then several hours plugged in and idle (overnight is ideal). If the machine is still slow after 24–48 hours of normal use with completed updates, start troubleshooting. Waiting avoids 'fixing' background work that would have finished on its own — but don't wait a week hoping; persistent slowness needs action."
---

Every Windows 11 feature update brings the same forum threads: "update made my laptop slow." Sometimes it's real — a replaced driver, a stuck migration task, a corrupted update. Sometimes it's just the post-update background storm that settles on its own. The skill is telling them apart quickly, because the fixes are different: patience and completion for the storm, targeted repair for the damage.

The best order: let the update finish its business, check what the update changed (especially drivers), then repair what's actually broken. Panic-uninstalling the update on day one is how people trade a temporary slowdown for an unpatched system. For update-triggered game stutter specifically see [fixing game stuttering after a Windows update](/articles/how-to-fix-game-stuttering-after-windows-update-in-windows-11-24h2/); for Defender-related post-update CPU burn see [fixing Windows Defender high CPU](/articles/best-way-to-fix-windows-defender-high-cpu-usage/).

## Why this happens

- **Post-update background churn**: Indexing, Defender rescans, and app re-optimization all firing at once.
- **Driver replacement**: The update swapping vendor drivers for older inbox versions.
- **Stuck migration or setup tasks**: SetupHost/TiWorker processes that never finished their post-update work.
- **Reset settings**: Power plans, visual effects, and refresh rates reverted to defaults.
- **Corrupt update installation**: Partially applied updates leaving the system in a degraded state.
- **Old software incompatible**: Legacy apps or drivers conflicting with the new build.
- **Disk space crunch**: The update consuming gigabytes, leaving the drive too full to perform.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Finish the update completely

Most "slow after update" is "still updating."

1. Go to **Settings** > **Windows Update** — install everything pending, including optional driver updates listed there. Reboot when asked, then check again; updates often arrive in waves.
2. After the final reboot, leave the laptop plugged in and idle for 2–3 hours (overnight is best) — this lets indexing, Defender rescans, and .NET optimization finish without competing with you.
3. Open Task Manager during this period: heavy disk/CPU from **SearchIndexer**, **MsMpEng**, or **TiWorker** is the background storm, not a malfunction.
4. Check **Settings** > **Windows Update** > **Update history** for failed updates — a failed update retries endlessly and keeps the system churning.
5. Only judge performance after updates show fully installed and the background processes have gone quiet.

### Fix 2: Check for replaced drivers

The number-one real cause.

1. Open **Device Manager** > **Display adapters** > your GPU > **Properties** > **Driver** tab — check the driver date. If it now predates the update by years, Windows replaced your vendor driver.
2. Reinstall the proper driver: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or AMD — clean install, then restart.
3. Check **Network adapters** (Wi-Fi driver) and **System devices** (chipset) the same way — update from the laptop vendor's support page if the dates look wrong.
4. Verify the display refresh rate (**Settings** > **System** > **Display** > **Advanced display**) — updates love resetting 120/144 Hz panels to 60 Hz, which feels like system-wide lag.
5. Check **Settings** > **System** > **Power & battery** > **Power mode** — reset to **Best performance** (plugged in) if the update changed it.

### Fix 3: Kill stuck post-update processes

When the background storm never ends.

1. If **TiWorker.exe** or **SetupHost.exe** has burned CPU for many hours with no update progress, the post-update work is stuck, not working.
2. Run the Windows Update troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update**.
3. Reset the update components if needed: elevated Command Prompt, `net stop wuauserv` + `net stop bits`, rename `SoftwareDistribution` and `catroot2`, restart the services.
4. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — post-update file corruption is common and these repair it.
5. Check **Event Viewer** > **Windows Logs** > **Setup** for setup errors naming the stuck phase.

### Fix 4: Free the disk space the update ate

Updates are hungry; full disks are slow.

1. Check free space on C: — feature updates can consume 20–30 GB (staging + Windows.old). Under 15% free, performance degrades across the board.
2. Run **Disk Cleanup** as admin and select **Windows Update Cleanup** and **Previous Windows installation(s)** (only if you won't roll back — you have 10 days).
3. Turn on **Storage Sense** (**Settings** > **System** > **Storage**) for ongoing maintenance.
4. If space is still tight, move personal large files off C: before judging performance — some slowness is just the full-disk effect.
5. Re-check Task Manager's disk activity after freeing space — constant 100% disk on an SSD with free space points elsewhere.

### Fix 5: Uninstall the update (when it's truly the cause)

The deliberate rollback, not the panic button.

1. Criteria: severe slowness, onset exactly matching the update, persisting 48+ hours after background work finished, and driver checks didn't help.
2. Go to **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the most recent quality update first (these uninstall cleanly).
3. For feature updates: **Settings** > **System** > **Recovery** > **Go back** (available 10 days) — this restores the previous build.
4. After rolling back, pause updates for 2–3 weeks (**Windows Update** > **Pause updates**) to avoid immediate reinstallation while Microsoft fixes the issue.
5. Report the problem via **Feedback Hub** — rollback without reporting just delays the same breakage. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the uninstall process officially.

### Fix 6: Update incompatible software

Old apps on new builds cause drag.

1. Update third-party antivirus before anything else — outdated AV on a new build causes system-wide slowdowns and is a known post-update complaint.
2. Update motherboard utilities, RGB software, VPN clients, and disk tools — these hook deep into the system and break subtly across builds.
3. Check the update's known-issues list (search the KB number) — Microsoft documents app incompatibilities, sometimes with workarounds.
4. Uninstall anything flagged incompatible rather than letting it limp along burning CPU in a compatibility shim.
5. For critical legacy software with no update, check the vendor's support pages for a Windows 11 compatibility statement before assuming the OS is at fault.

## Closing

Post-update slowness has a natural history: storm, then settle — or storm, then stuck. Give the update its completion window, check whether it replaced your drivers (it probably did), clear stuck processes, and only then consider rollback. Most machines are fast again by Fix 2 with a proper GPU driver and the refresh rate restored. The update wasn't the enemy; the unfinished business it left behind was.
