---
title: "Windows Modules Installer High CPU After a Windows 11 Update: What to Do"
slug: how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update
date: 2026-10-10
categories: ["performance"]
tags: ["windows modules installer", "tiworker", "high cpu", "windows update", "trustedinstaller"]
description: "Windows Modules Installer Worker (TiWorker.exe) pinning your CPU after a Windows 11 update? Why it happens and how to let it finish or fix it."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "What is Windows Modules Installer Worker?"
    a: "Windows Modules Installer Worker (TiWorker.exe) is the background engine behind Windows Update and optional-feature installation. It downloads, verifies, stages, and installs updates, then cleans up afterward. High CPU from it after an update is normal — it is finishing installation work and optimizing the component store. It should taper off within a few hours. If it runs at high CPU for days, the update process is likely stuck and needs intervention."
  - q: "Is TiWorker.exe a virus?"
    a: "The legitimate TiWorker.exe lives in C:\\Windows\\WinSxS and C:\\Windows\\System32 and is a core Windows component. Malware occasionally impersonates system process names, so verify the location: right-click it in Task Manager Details tab, choose Open file location, and confirm it points to a Windows system folder. If it points anywhere else, run a full Microsoft Defender scan immediately, because that would indicate an impostor."
  - q: "How long should Windows Modules Installer run after an update?"
    a: "After a monthly cumulative update, expect 30 minutes to a few hours of activity, including the post-reboot optimization phase. After a feature update, it can legitimately work for most of a day as it migrates components and cleans the WinSxS store. Give it one full plugged-in day. Beyond 48 hours of sustained high CPU, or if it restarts its work from scratch repeatedly, treat it as stuck and work through the fixes below."
  - q: "Can I disable Windows Modules Installer Worker?"
    a: "No — disabling it breaks Windows Update, optional features, and component servicing, and Windows will not let you do it cleanly anyway. TiWorker.exe is not optional bloat; it is how Windows maintains itself. The correct approach is letting it finish its work, fixing whatever has it stuck, and scheduling updates for convenient times. Disabling Windows servicing guarantees bigger problems than high CPU."
---

Right after a Windows 11 update, Task Manager shows `Windows Modules Installer Worker` (TiWorker.exe) — sometimes alongside its parent `TrustedInstaller.exe` — consuming 30%, 60%, even 90% of your CPU, with the disk grinding away. Your first instinct might be to kill it. Don't. This process is Windows finishing the update: staging components, verifying file integrity, migrating settings, and cleaning up the component store. Interrupting it mid-work is how you get a corrupted update that has to redo everything — doubling the pain.

The real question, as always with post-update CPU spikes, is duration. A few hours of heavy TiWorker.exe activity after an update is Windows working as designed. Days of it — or the same update failing and retrying in a loop — means the servicing stack is stuck and needs help. This guide shows you how to tell the difference, how to let it finish efficiently, and how to unstick it when it won't finish on its own.

Start here: open **Task Manager** > **Processes**, find **Windows Modules Installer Worker**, and note the CPU over several minutes. Then check **Settings** > **Windows Update** — if it shows "installing," "pending restart," or a failed update, TiWorker is mid-job and the update status tells you exactly which job. For related post-update issues, see [Defender high CPU after an update](/articles/how-to-fix-antimalware-service-executable-high-cpu-after-windows-11-update/) and [Windows 11 slow after an update](/articles/windows-11-slow-after-update-how-to-fix/).

## Why this happens

- **Post-update component servicing**: TiWorker installs, verifies, and optimizes update components after the reboot.
- **WinSxS cleanup and optimization**: The component store gets reorganized and deduplicated after updates.
- **A stuck or failing update**: A corrupted download makes TiWorker retry the same work in a loop.
- **Corrupted servicing stack**: Damaged system files prevent TiWorker from completing its tasks.
- **Pending restart backlog**: Multiple updates queued behind a missed restart keep the worker busy.
- **Disk errors slowing file operations**: Bad sectors turn normal servicing into an hours-long grind.
- **Third-party interference**: Overzealous "debloater" scripts or AV products blocking servicing operations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check update status and let it finish

Most cases need patience, not intervention.

1. Open **Settings** > **Windows Update** and read the status carefully — "Downloading," "Installing," or "Pending restart" all mean TiWorker has legitimate work in progress.
2. If a restart is pending, **restart now** — much of TiWorker's post-update work only completes across the reboot, and delaying it extends the high-CPU period.
3. Leave the laptop plugged in and give it a few uninterrupted hours — servicing completes dramatically faster when the machine is idle and on AC power.
4. Watch the trend: CPU that gradually declines over hours is finishing work; CPU flat at 80%+ for a full day with no status change is stuck.
5. Check **Update history** for failed updates — a failure entry next to sustained TiWorker activity points to the loop described in Fix 3.

### Fix 2: Run the Windows Update troubleshooter

The built-in tool fixes common servicing stalls.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. Let it complete and apply any recommended fixes — it resets stuck update components and re-registers servicing DLLs.
3. Restart the laptop after the troubleshooter finishes, even if it doesn't explicitly ask.
4. Re-check **Settings** > **Windows Update** — a previously stuck update often proceeds normally after this reset.
5. If the troubleshooter reports it couldn't fix something, note the details — they guide which manual fix below to try. Microsoft's [Windows Update support](https://support.microsoft.com/en-us/windows) documents additional recovery steps.

### Fix 3: Clear the stuck update cache

A corrupted download cache is the most common cause of TiWorker loops.

1. Open an **elevated Command Prompt** (search CMD > Run as administrator).
2. Stop the update services: run `net stop wuauserv`, then `net stop bits`, then `net stop cryptSvc` — wait for each to confirm.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old` — this forces Windows to rebuild fresh caches.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptSvc`.
5. Go to **Settings** > **Windows Update** > **Check for updates** — Windows re-downloads cleanly, and TiWorker should now complete instead of looping. Don't delete the `.old` folders for a week, in case you need to revert.

### Fix 4: Repair the servicing stack with DISM and SFC

For corruption TiWorker can't work around.

1. In an elevated terminal, run `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the Windows component store that TiWorker services. It can take 15–30 minutes; let it finish.
2. Follow with `sfc /scannow` to repair protected system files.
3. Restart, then check **Windows Update** again — repaired servicing components often unstick the exact update that was looping.
4. If DISM fails with its own errors, run it with an explicit source: mount a Windows 11 ISO and use `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:X:\sources\install.wim:1` (replace X: with your mounted drive).
5. After repair, give TiWorker one idle plugged-in session — it may briefly spike as it completes the work that was previously blocked, then settle.

### Fix 5: Check disk health

Servicing on a failing drive grinds forever.

1. In an elevated Command Prompt, run `chkdsk C: /scan` — this online scan finds file-system errors without a reboot.
2. If errors are found, schedule the full repair: `chkdsk C: /f`, confirm the reboot prompt, and restart — the repair runs before Windows loads.
3. Check SMART status: `wmic diskdrive get status` — anything other than "OK" means the drive is failing and servicing slowness is a symptom; back up immediately.
4. On HDDs, heavy fragmentation amplifies TiWorker's disk load — run **Defragment and Optimize Drives** after the update completes (never on SSDs).
5. If the drive is healthy and TiWorker is still stuck, the problem is software (cache or corruption), not hardware — return to Fixes 3–4.

### Fix 6: Manually install the stuck update

Bypass the broken automatic path.

1. In **Update history**, identify the exact KB number of the failing update (e.g., KB5037771).
2. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search the KB number, and download the version matching your system (x64 for most laptops).
3. Disconnect from metered or unstable connections first — interrupted downloads are how caches get corrupted.
4. Run the downloaded `.msu` file and let it install, then reboot when prompted.
5. Verify in **Update history** that it shows as successfully installed — TiWorker should stand down within an hour of a successful manual install.

### Fix 7: Schedule updates to avoid the disruption

Make future servicing invisible.

1. Set **Active Hours** (**Settings** > **Windows Update** > **Advanced options**) to cover your full workday so installs and reboots happen outside it.
2. On metered connections, updates download only when you allow — useful for controlling when the TiWorker storm hits, but don't defer security updates indefinitely.
3. After each Patch Tuesday, proactively check for updates in the evening and reboot before bed — TiWorker does its heavy work overnight instead of during your morning.
4. Keep at least 15% free on C: — servicing needs staging room, and a full drive makes TiWorker dramatically slower.
5. Leave automatic maintenance alone (**Control Panel** > **Security and Maintenance** > **Maintenance**) — its scheduled 2 AM run handles WinSxS cleanup that would otherwise pile onto TiWorker.

## Closing

Windows Modules Installer Worker high CPU after an update is Windows doing necessary maintenance — usually. Give it its few hours, restart when pending, and it stands down on its own. When it doesn't, it's a stuck cache, a corrupted component store, or a failing update, and the fixes above address each in turn. Never kill TiWorker or disable servicing; helping it finish is always faster than fighting it.
