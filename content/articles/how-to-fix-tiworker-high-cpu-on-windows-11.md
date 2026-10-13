---
title: "How to Fix TiWorker High CPU Usage on Windows 11"
slug: how-to-fix-tiworker-high-cpu-on-windows-11
date: 2026-09-11
categories: ["performance"]
tags: ["tiworker", "high cpu", "windows update", "windows 11", "troubleshooting"]
description: "TiWorker.exe (Windows Modules Installer Worker) pinning your CPU? Fix stuck Windows Update processing with this ordered troubleshooting guide."
thumbnail: "/images/thumbs/how-to-fix-tiworker-high-cpu-on-windows-11.webp"
faqs:
  - q: "What is TiWorker.exe?"
    a: "TiWorker.exe — Windows Modules Installer Worker — is the background process that installs, modifies, and removes Windows updates and optional components. When Windows Update downloads patches, TiWorker does the actual installation work: unpacking files, updating the component store, and configuring changes. It's supposed to run hard during updates and then stop; sustained high CPU means an update operation is stuck."
  - q: "How long should TiWorker normally run?"
    a: "During a monthly cumulative update, TiWorker legitimately works hard for fifteen minutes to an hour depending on the update size and your disk speed. After a feature update, it can run for a couple of hours completing component work. If it's still at high CPU a full day later with no update in progress, that's abnormal — the update pipeline is stuck and needs the fixes below."
  - q: "Can I end TiWorker.exe in Task Manager?"
    a: "You can end it and Windows will restart it, but killing it mid-installation risks leaving the component store in a half-updated state — which is exactly the kind of stuck condition you're trying to fix. It's safe as a last resort, but the proper approach is letting legitimate update work finish, then using the update troubleshooter and component-store repairs in this guide."
  - q: "Why does TiWorker use so much disk as well as CPU?"
    a: "Because update installation is I/O-heavy: TiWorker reads update packages, writes thousands of files, and updates the WinSxS component store, all while the CPU compresses, decompresses, and verifies. On a hard drive this combination pins both CPU and disk; on an SSD it's mostly CPU. The disk activity is normal during updates — it's the duration, not the intensity, that signals a problem."
---

TiWorker.exe — the Windows Modules Installer Worker — is Windows Update's muscle: it installs the updates that the update service downloads. During patch Tuesday it's supposed to work hard for a while and then stop. But when it grinds at 30–80% CPU for days, with no update visibly progressing, the update pipeline is stuck — and a stuck updater doesn't just waste CPU, it blocks future updates too.

The fix sequence is specific to the update pipeline: let legitimate work finish, clear the stuck state, repair the component store, and reset the update components if needed. Follow it in order — each step addresses a deeper layer of "stuck."

## Why this happens

- **Genuinely large updates:** Feature updates legitimately keep TiWorker busy for hours — patience is sometimes the fix.
- **Stuck update download:** A corrupted or partial download that TiWorker can't process but keeps retrying.
- **Corrupted component store:** Damage in WinSxS that makes every install operation fail and retry.
- **Pending operations backlog:** Multiple queued updates and component changes piling up.
- **Corrupted SoftwareDistribution cache:** The update download folder in a bad state.
- **Third-party interference:** Antivirus or "debloating" tools breaking update components.
- **Insufficient disk space:** Updates need working room; a full drive stalls the pipeline mid-operation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check update status and give legitimate work time

Open **Settings → Windows Update** and look: is an update downloading, installing, or pending restart? Open Task Manager and correlate TiWorker CPU with that status. If an update is actively installing, let it finish — plug in, stay idle, give it up to two hours for a feature update. Check the update history for failed installs, which indicate the stuck pattern. Only proceed to active fixes if TiWorker has been hot for many hours with no update progressing, or if updates repeatedly fail. Killing legitimate update work creates the stuck state you're trying to fix.

1. Check Windows Update status for active or failed updates.
2. Correlate TiWorker CPU with actual update activity.
3. Allow up to two hours for legitimate feature-update work.
4. Proceed only if stuck for many hours or updates keep failing.

### Fix 2: Run the Windows Update troubleshooter

Go to **Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run**. The troubleshooter detects and repairs the common stuck states: stalled services, corrupted caches, misconfigured components. It's automated and safe — let it complete, apply its fixes, and reboot. Then check Windows Update again: if previously-failed updates now install and TiWorker settles afterward, you're done. This resolves a surprising share of TiWorker cases because the "stuck" state is often a trivial service or cache issue the troubleshooter was built to clear.

1. Run the Windows Update troubleshooter.
2. Apply all recommended fixes.
3. Reboot and retry the failed updates.
4. Verify TiWorker settles after updates complete.

### Fix 3: Clear the SoftwareDistribution download cache

If the troubleshooter didn't clear it, the download cache is likely corrupt. Open services.msc and stop the Windows Update service (wuauserv) and Background Intelligent Transfer Service (BITS). Then rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` (don't delete — renaming preserves a fallback). Restart both services and check Windows Update — it rebuilds a clean cache and re-downloads what's needed. This clears the corrupted-download retry loop that keeps TiWorker spinning. Your update history resets, but installed updates remain installed.

1. Stop the Windows Update and BITS services.
2. Rename SoftwareDistribution to SoftwareDistribution.old.
3. Restart both services.
4. Check for updates and let them reinstall cleanly.

### Fix 4: Repair the component store with DISM

TiWorker works directly on the WinSxS component store, so a corrupted store keeps it failing. In an admin Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the store using Windows Update as the source. If that fails (often because the update pipeline itself is broken), use a Windows 11 ISO as the source: mount the ISO and run `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:X:\Sources\Install.wim:1` (adjust the drive letter). Follow with `sfc /scannow` to repair system files. A healthy component store lets TiWorker complete its work instead of retrying forever. The ISO comes from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

1. Run DISM RestoreHealth in an admin Command Prompt.
2. Use a mounted ISO as source if the online repair fails.
3. Follow with `sfc /scannow`.
4. Retry updates and watch TiWorker complete normally.

### Fix 5: Reset Windows Update components manually

For deeply stuck pipelines, reset the whole update stack. In an admin Command Prompt, stop the wuauserv, cryptSvc, bits, and msiserver services; rename `SoftwareDistribution` and `Catroot2` folders (in System32); then restart all four services. This is the manual version of what the troubleshooter attempts — more thorough because you control each step. Alternatively, Microsoft's official "reset Windows Update components" script automates the same sequence. After resetting, check for updates — the first scan takes longer as it rebuilds everything, then updates should flow normally. Microsoft documents component resets in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Stop the four update-related services.
2. Rename SoftwareDistribution and Catroot2 folders.
3. Restart all four services.
4. Run a full update check and let it complete.

### Fix 6: Free disk space and check for the bigger picture

Updates need elbow room — ensure at least 15–20GB free on C: (feature updates need more). If space is tight, the pipeline stalls mid-operation and TiWorker spins. Clear space with Disk Cleanup's system-files mode. Then step back: if TiWorker is calm but idle CPU is still high, other processes may be contributing — run the general identification from the [Lenovo high-CPU guide](/articles/how-to-fix-high-cpu-usage-on-lenovo-laptop/) to catch them. And if a specific update repeatedly fails even after all repairs, check the [update-troubleshooting angle](/articles/how-to-fix-tiworker-high-cpu-after-windows-11-update/) and consider manually installing the KB from the [Update Catalog](https://www.catalog.update.microsoft.com/).

1. Ensure 15–20GB+ free on the system drive.
2. Clear space with Disk Cleanup if needed.
3. Check for other idle-CPU contributors.
4. Manually install stubborn KBs from the Update Catalog.

## Closing

TiWorker high CPU is the update pipeline crying for help — and the pipeline has a specific repair order: let real work finish, troubleshoot, clear the cache, repair the store, reset the components. Work it top to bottom and the stuck state clears, updates flow again, and TiWorker returns to its proper behavior: busy during updates, silent the rest of the month.
