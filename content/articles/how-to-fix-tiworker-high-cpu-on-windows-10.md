---
title: "How to Fix TiWorker High CPU Usage on Windows 10"
slug: how-to-fix-tiworker-high-cpu-on-windows-10
date: 2026-09-14
categories: ["performance"]
tags: ["tiworker", "high cpu", "windows update", "windows 10", "troubleshooting"]
description: "TiWorker.exe stuck at high CPU on Windows 10? Unstick the Windows Update pipeline with these ordered repair steps."
thumbnail: "/images/thumbs/how-to-fix-tiworker-high-cpu-on-windows-10.webp"
faqs:
  - q: "Is TiWorker high CPU more common on Windows 10?"
    a: "Somewhat, yes — Windows 10's update pipeline is older and its component store has had more years to accumulate damage from interrupted updates, failed feature upgrades, and third-party 'debloating' tools. The stuck states are the same as on Windows 11, but Windows 10 machines more often need the deeper repairs (DISM with ISO source, manual component reset) because the corruption has had longer to compound."
  - q: "How do I know if TiWorker is doing legitimate update work?"
    a: "Open Settings → Update & Security → Windows Update: if an update shows downloading or installing, TiWorker's activity is legitimate — give it time, up to a couple of hours for a feature update. Check Update history for failed entries too. TiWorker is only 'stuck' when it's been hot for many hours with no update progressing, or when the same update fails repeatedly."
  - q: "Will these fixes delete my installed updates?"
    a: "No. Clearing the SoftwareDistribution cache, repairing the component store, and resetting update components all preserve installed updates — they only clear the download cache, repair the installation machinery, and reset the pipeline state. Your update history display may reset, but the actual installed updates and your files are untouched."
  - q: "What if Windows 10 is stuck on an old feature version?"
    a: "A very old feature version (several years behind) can make the update pipeline struggle — the jump is large and the component store may be damaged. In that case, the reliable path is often the Windows 10 Update Assistant or a repair install from current ISO media rather than fighting the in-place updater. Back up first, then use fresh media from Microsoft's download page."
---

TiWorker.exe on Windows 10 is the same Windows Modules Installer Worker as on Windows 11 — the process that does the actual labor of installing updates. And it gets stuck the same way: grinding at high CPU for days while no update visibly progresses, blocking future updates behind it. Windows 10 machines, being older on average, hit the stuck states slightly more often — longer history, more interrupted updates, more "debloater" damage.

The repair sequence mirrors the Windows 11 version with Windows 10's settings paths and tools. Work it in order: confirm the stuck state, run the troubleshooter, clear caches, repair the component store, and reset the pipeline. The stuck updater always yields to this sequence eventually.

## Why this happens

- **Corrupted update downloads:** Partial or damaged packages TiWorker retries endlessly.
- **Aged component store:** Years of updates leaving WinSxS damage that fails every install operation.
- **Interrupted feature updates:** Failed upgrades leaving the pipeline in a half-migrated state.
- **Debloating tool damage:** Third-party scripts removing update-related components.
- **Stuck BITS queue:** Background Intelligent Transfer jobs wedged in the download queue.
- **Low disk space:** Feature updates need 20GB+ working room; starved drives stall mid-operation.
- **Antivirus interference:** Overzealous suites blocking update file operations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stuck state in Windows Update

Open **Settings → Update & Security → Windows Update** and read the status carefully: downloading, installing, pending restart, or an error code? Check **View update history** for failed installs and their error codes — repeated failures of the same KB are the classic stuck signature. Give legitimate work its due: a feature update can keep TiWorker busy for 1–2 hours. Only treat it as stuck after many hours of heat with no progress, or repeated failures. Note any error codes — they guide the deeper fixes.

1. Check Windows Update status and update history.
2. Note repeated failures and their error codes.
3. Allow legitimate feature-update work up to two hours.
4. Proceed when stuck for many hours or failing repeatedly.

### Fix 2: Run the Windows Update troubleshooter

Go to **Settings → Update & Security → Troubleshoot → Additional troubleshooters → Windows Update → Run the troubleshooter**. Let it complete and apply its repairs — it handles the common stuck states (stalled services, bad cache configuration) automatically. Reboot, then check for updates again. On Windows 10 this troubleshooter is particularly effective because the stuck states it targets are the ones that accumulate over years. If updates now install and TiWorker settles, you're done — verify across the next Patch Tuesday that the pipeline stays healthy.

1. Run the Windows Update troubleshooter.
2. Apply its recommended repairs.
3. Reboot and retry updates.
4. Verify TiWorker settles after successful installs.

### Fix 3: Clear the SoftwareDistribution and BITS state

Stop the Windows Update service (wuauserv) and BITS in services.msc. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`. For the BITS queue, the rename handles most of it — but you can also clear it via `bitsadmin /reset /allusers` in an admin Command Prompt. Restart both services and check for updates: Windows rebuilds clean caches and re-downloads. This breaks the corrupted-download retry loop cold. Installed updates survive; only the pipeline's working state resets.

1. Stop wuauserv and BITS services.
2. Rename the SoftwareDistribution folder.
3. Run `bitsadmin /reset /allusers` as admin.
4. Restart services and check for updates.

### Fix 4: Repair the component store (DISM) and system files (SFC)

In an admin Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`. On Windows 10 with a damaged pipeline, the online repair sometimes fails — then use Windows 10 installation media as the source: mount the ISO and run DISM with `/Source:WIM:X:\Sources\Install.wim:1` (adjust the drive letter to your mounted ISO). Follow with `sfc /scannow`. The component store is TiWorker's workbench — repairing it is what lets installs complete instead of retrying forever. This is the deepest common fix and resolves most stubborn cases.

1. Run DISM RestoreHealth online first.
2. Fall back to ISO-sourced repair if online fails.
3. Run `sfc /scannow` afterward.
4. Retry the failing updates.

### Fix 5: Manually reset all Windows Update components

When automated repairs aren't enough, do the full manual reset: stop wuauserv, cryptSvc, bits, and msiserver; rename `SoftwareDistribution` and `System32\catroot2`; restart the four services. Then re-register the update DLLs if you're thorough (`regsvr32` on wuapi, wuaueng, wups, and friends — Microsoft's official reset script automates this). This returns the entire update stack to factory state while keeping installed updates. The first update check afterward is slow as everything rebuilds — that's normal. Microsoft documents the component reset in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Stop the four update services.
2. Rename SoftwareDistribution and catroot2.
3. Restart all four services.
4. Run a full update check and let it complete slowly.

### Fix 6: Free space, check companions, and consider the version jump

Ensure 20GB+ free on C: — feature updates stall without working room; clear with Disk Cleanup's system-files mode. If TiWorker is calm but the system still feels slow, hunt companion hogs with the general method in the [Lenovo high-CPU guide](/articles/how-to-fix-high-cpu-usage-on-lenovo-laptop/). For a stubborn specific KB, download it manually from the [Update Catalog](https://www.catalog.update.microsoft.com/) and install offline. And if the machine is years behind on feature versions, seriously consider the Update Assistant or a repair install from current media — sometimes the pipeline is too far gone to fix incrementally, and fresh media is faster than another week of troubleshooting.

1. Free 20GB+ on the system drive.
2. Check for companion CPU hogs with the general method.
3. Manually install stubborn KBs from the Update Catalog.
4. Use the Update Assistant or fresh media for very old builds.

## Closing

Windows 10's TiWorker gets stuck for the same reasons as Windows 11's — corrupted downloads, damaged component store, wedged pipeline — just more often, because the history is longer. The repair order doesn't change: troubleshooter, cache clear, DISM, component reset. Work it patiently, and the updater that ground for days will finish its work in an hour and go quiet until next month. For the Windows 11 pipeline specifically, see the [post-update TiWorker guide](/articles/how-to-fix-tiworker-high-cpu-after-windows-11-update/).
