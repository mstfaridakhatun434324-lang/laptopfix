---
title: "Windows 11 Slow After Update? How to Fix Post-Update Sluggishness"
slug: windows-11-slow-after-update-how-to-fix
date: 2026-10-03
categories: ["performance"]
tags: ["slow after update", "windows update", "performance", "rollback"]
description: "Windows 11 sluggish after the latest update? Diagnose post-update slowdowns — background activity, driver regressions, and when to roll back."
thumbnail: "/images/thumbs/windows-11-slow-after-update-how-to-fix.webp"
faqs:
  - q: "Why is Windows 11 slow after an update?"
    a: "The most common reasons are temporary: post-update background tasks (search reindexing, Defender rescanning, .NET optimization, OneDrive re-syncing) that settle within a day or two. Persistent slowness points to a driver regression from the update (especially storage or graphics drivers), a corrupted update installation, or the update exposing a pre-existing bottleneck like a nearly-full drive."
  - q: "How long should I wait before troubleshooting post-update slowness?"
    a: "Give it 24–48 hours of plugged-in idle time first. Windows runs a gauntlet of one-time post-update tasks — indexing, optimization, telemetry uploads — that legitimately consume resources. Troubleshoot only if slowness persists beyond two days, or immediately if something is clearly broken (a device stopped working, boot loops, specific errors)."
  - q: "Can I uninstall a Windows update that made things slow?"
    a: "Yes, for quality updates: Settings > Windows Update > Update history > Uninstall updates, select the recent KB, and uninstall. Feature updates can be rolled back within 10 days via Settings > System > Recovery > Go back. If the update was the cause, also pause updates for a few weeks so it doesn't reinstall before Microsoft fixes it."
  - q: "Will pausing updates hurt my security?"
    a: "Pausing for 1–2 weeks while a bad update gets fixed is a reasonable tradeoff — you're briefly delaying patches, not abandoning them. Don't pause indefinitely; the security risk compounds over months. Use the pause to let Microsoft ship a fixed update, then unpause and install. For a known-bad driver update specifically, hide just that update rather than pausing everything."
---

The pattern is familiar: update installs overnight, and the next morning the laptop feels like it's wading through mud — slow boot, laggy windows, disk churning. Before you panic or roll anything back, know that most post-update slowness is temporary. Windows performs a battery of one-time maintenance tasks after updates (reindexing search, recompiling .NET, rescanning with Defender, re-syncing OneDrive), and these legitimately hammer the system for a day or two.

So the first diagnostic question is time: has it been less than 48 hours? If yes, let it finish. If the slowness persists beyond that — or something is specifically broken — work the sequence: identify background culprits, check for driver regressions, repair the update, and roll back if needed. For general slowness not tied to an update, see [speeding up a slow laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); for update-caused driver breakage specifically, [rolling back a driver update](/articles/best-way-to-rollback-driver-update/).

## Why this happens

- **Post-update background tasks**: Indexing, Defender rescans, .NET NGEN optimization, and Store app updates — heavy but temporary.
- **Driver regressions in the update**: New storage, graphics, or chipset drivers that perform worse or malfunction.
- **Corrupted update installation**: A partially-applied update leaving the system in a degraded state.
- **Update reset your settings**: Power plans, startup entries, or privacy settings changed by the update.
- **Exposed pre-existing bottleneck**: The update's extra activity pushes a nearly-full drive or maxed RAM over the edge.
- **Windows.old consuming space**: The pre-update backup eats tens of gigabytes, pushing SSDs past the performance cliff.
- **Incompatible third-party software**: Antivirus, VPNs, or utilities that break against the new build.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait out the background storm (but verify it's the storm)

Confirm the slowness is post-update activity, not something worse.

1. Open **Task Manager** > **Processes**, sort by Disk and CPU — post-update culprits have recognizable names: `SearchIndexer.exe`, `MsMpEng.exe` (Defender), `.NET Runtime Optimization Service` (`mscorsvw.exe`), `OneDrive.exe` syncing, `TiWorker.exe` (Windows Modules Installer).
2. If these are the top consumers and the update was within the last 48 hours, the system is doing legitimate one-time work. Leave the laptop plugged in and idle (or at least not heavily used) to let it finish faster.
3. Check **Settings** > **Windows Update** — if it shows "updates in progress" or pending restarts, the update isn't even done yet.
4. Give it a firm deadline: if the same processes are still hammering after 48 hours of idle opportunity, it's not the storm anymore — continue.
5. Do NOT start uninstalling updates during this window — interrupting post-update finalization causes the corruption you're trying to avoid.

### Fix 2: Clear space — especially Windows.old

Updates eat disk space, and full SSDs are slow SSDs.

1. Check **Settings** > **System** > **Storage** — if free space dropped sharply after the update, the **Windows.old** folder (your pre-update backup, 15–30 GB) is the likely cause.
2. If you're confident you won't roll back (past the 48-hour storm and everything works), remove it: **Disk Cleanup** (`cleanmgr`) > **Clean up system files** > check **Previous Windows installation(s)** > OK.
3. Also clean **Windows Update Cleanup** and **Temporary files** in the same pass — updates leave gigabytes of superseded components.
4. Verify free space is back above 15–20% of the drive — SSD performance recovers noticeably once past the capacity cliff.
5. If space is still tight after cleanup, the update merely exposed a chronic shortage — move media libraries off the system drive or uninstall large unused programs.

### Fix 3: Check for driver regressions

Updates ship drivers; drivers cause the persistent slowdowns.

1. Open **Device Manager** and look for warning icons — especially under **Storage controllers**, **Display adapters**, **IDE ATA/ATAPI controllers**, and **Network adapters**.
2. Check **Settings** > **Windows Update** > **Update history** for driver updates bundled with the quality/feature update.
3. For any suspect driver: **Properties** > **Driver** tab > **Roll Back Driver** — storage controller and graphics driver rollbacks fix the majority of update-caused persistent slowness.
4. Specifically check the storage driver: an update-swapped AHCI/NVMe driver running in the wrong mode (or a generic instead of Intel RST/AMD) tanks disk performance visibly.
5. After rolling back, hide the driver update with the Show or hide updates troubleshooter so the next update cycle doesn't reinstall it. Our [driver rollback guide](/articles/best-way-to-rollback-driver-update/) covers this in full.

### Fix 4: Repair the update installation

For updates that applied badly.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run** — let it detect and repair update-component issues.
2. In an elevated terminal, reset the update components' cache: stop the Windows Update service (`net stop wuauserv`), rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`, restart the service (`net start wuauserv`), and check for updates again.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` — corrupted system files from a bad update application cause exactly this kind of pervasive sluggishness.
4. Restart (full restart) after the repairs and reassess — repaired updates often need one clean boot to settle.
5. If the troubleshooter reports it couldn't fix things, the update may need reinstalling — uninstall it (Fix 6) and let Windows offer it fresh.

### Fix 5: Audit what the update changed or broke

Updates reset things — find what changed.

1. Check your power plan: **Settings** > **System** > **Power & battery** > **Power mode** — feature updates sometimes reset this to Balanced/Power saver. Set **Best performance** (plugged in).
2. Recheck **Task Manager** > **Startup apps** — updates occasionally re-enable disabled startup entries. Disable the returnees.
3. Check third-party software: antivirus, VPN clients, and manufacturer utilities sometimes break against new builds — update them to versions certified for your Windows build, or temporarily uninstall to test.
4. Review **Privacy & security** settings you had customized — updates can re-enable telemetry and background app permissions you turned off.
5. If a specific program got slow (not the whole system), check that program's vendor for a compatibility update — app-level, not OS-level.

### Fix 6: Uninstall the problematic update

When the update itself is the problem and waiting didn't help.

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — select the most recent quality update (KB number) and uninstall it. Restart.
2. For feature updates (annual major versions): **Settings** > **System** > **Recovery** > **Go back** — available for 10 days after the feature update. This restores the previous build wholesale.
3. After uninstalling, **pause updates** for 2–3 weeks (**Settings** > **Windows Update** > **Pause updates**) so the bad update doesn't reinstall immediately.
4. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) and the update's KB article for known issues — if Microsoft acknowledges the problem, a fixed update is usually days away; wait for it rather than fighting.
5. For a bad *driver* delivered via update, prefer hiding just that driver (Fix 3) over uninstalling the whole update — more surgical, less security exposure.

### Fix 7: The clean slate — in-place upgrade repair

When the system is slow and nothing identifies why.

1. Download the [Windows 11 Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11) and run an **in-place upgrade** (keep files and apps) — this reinstalls Windows over itself, repairing update damage while preserving everything.
2. This takes 30–90 minutes and several reboots — plan accordingly, stay plugged in.
3. After the repair install, immediately check drivers (chipset first — see our [chipset guide](/articles/how-can-i-install-chipset-drivers/)) and run Windows Update to get current.
4. Reassess performance over 48 hours (remember Fix 1's background storm applies to repair installs too).
5. If even a repair install doesn't help, the update likely exposed hardware limits (aging HDD, full SSD, failing drive) — check drive health with CrystalDiskInfo and revisit the hardware upgrades in our [slow-laptop guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Closing

Post-update slowness is a patience-first problem: most of it is the 48-hour background storm, and troubleshooting during the storm causes more harm than good. After the storm, the culprits are usually disk space (Windows.old), a regressed driver, or a badly-applied update — each with a clean fix. And when an update is genuinely bad, uninstalling it and pausing for a few weeks is not defeat; it's maintenance.
