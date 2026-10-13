---
title: "Windows 11 Slow After an Update? What to Do"
slug: what-to-do-if-windows-11-slow-after-update
date: 2026-09-28
categories: ["performance"]
tags: ["windows 11 slow after update", "windows update", "performance", "troubleshooting", "rollback"]
description: "Windows 11 slow right after an update? Distinguish normal post-update settling from real problems, then fix drivers, indexing, and update residue."
thumbnail: "/images/thumbs/what-to-do-if-windows-11-slow-after-update.webp"
faqs:
  - q: "How long should I wait after an update before worrying about slowness?"
    a: "Give it 24-48 hours of normal use with the laptop plugged in and occasionally idle. Post-update Windows re-indexes files, re-optimizes apps, rebuilds caches, and completes background migrations — all legitimately resource-heavy. If the machine is still slow after two days of regular use, or if a specific thing is broken (no Wi-Fi, no sound, a particular app crashes), that's a real problem worth troubleshooting rather than waiting out."
  - q: "Can I uninstall a Windows update that made my laptop slow?"
    a: "Yes, within about 10 days for feature updates (Settings → Windows Update → Update history → Uninstall updates). Quality updates can also be uninstalled individually. This is a legitimate fix when the slowness clearly started with a specific update and nothing else changed. Note that Windows will eventually offer the update again — use the pause feature or the show/hide troubleshooter to defer it while Microsoft fixes the issue."
  - q: "Why do updates sometimes break drivers?"
    a: "Feature updates replace large parts of the OS, and drivers written against the old version can misbehave — especially GPU, audio, and network drivers. Windows Update also sometimes installs its own generic driver over your working vendor driver. The pattern is distinctive: everything was fine, update installed overnight, now something specific is slow or broken. Reinstalling the vendor driver is the standard cure."
  - q: "Should I pause Windows updates to avoid this happening again?"
    a: "Pausing for a week or two after a problematic update is reasonable — it gives Microsoft time to ship fixes and lets you update on your schedule. Pausing indefinitely is not: you'd miss security patches. The balanced approach is pausing briefly, then updating manually when you have time to deal with fallout, rather than letting updates install the night before an important day."
---

The timeline is damning: laptop was fine Tuesday, update installed overnight, laptop is miserable Wednesday. Post-update slowness is one of the most common Windows complaints, and it has two completely different explanations that demand opposite responses. Explanation one: Windows is still finishing the update's background work — indexing, optimization, migration — and the slowness is temporary. Explanation two: the update actually broke something — a driver, a setting, a system component — and waiting fixes nothing.

The first job is telling these apart. The second job is fixing whichever one you're in.

## Why this happens

- **Post-update background work:** Re-indexing, .NET optimization, app re-registration, and update cleanup consume resources for 24-48 hours.
- **Driver replacement:** The update installed a generic driver over your working vendor driver (GPU, audio, and network are the usual victims).
- **Driver incompatibility:** Old drivers misbehaving under the new OS build — common with feature updates.
- **Corrupted update installation:** An interrupted or partially failed update leaving components in a bad state.
- **Reset settings:** The update reverting power plans, display settings, or startup configurations you'd tuned.
- **Update residue:** Gigabytes of superseded update files and the Windows.old folder consuming disk space.
- **New bugs in the build:** Occasionally the update itself ships with a performance regression Microsoft later patches.
- **Coincidence:** Hardware failures and malware don't check the update calendar before striking.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it's settling or broken

Check the timeline and the symptoms. Open **Settings → Windows Update → Update history** and note exactly what installed and when. Then ask: is the whole machine uniformly slow (suggests background work or a systemic issue), or is something specific broken (no Wi-Fi, stuttering video, one app crashing — suggests a driver)? Check Task Manager for what's actually busy. If it's been less than 48 hours and the disk/CPU shows indexing and update processes working, the correct action is patience: plug in, leave it idle a few hours, and re-evaluate. The [Windows 11 lagging guide](/articles/how-to-fix-windows-11-lagging-step-by-step/) is the right next step if the slowness persists past the settling window.

1. Check Update history for what installed and when.
2. Classify: uniformly slow (background work?) vs. specifically broken (driver?).
3. Check Task Manager for the actual busy processes.
4. If under 48 hours and background processes are working, wait before acting.

### Fix 2: Let the background work finish

If Fix 1 points to settling, help it finish: plug in the laptop, leave it idle and awake for a few hours (disable sleep temporarily), and don't fight the indexer or optimizer. You can watch progress in Indexing Options (it shows items indexed). Forcing reboots during this phase just restarts the work. Most "update ruined my laptop" complaints that resolve on their own resolve during this window — the machine wasn't broken, it was busy.

1. Plug in the laptop; temporarily set sleep to Never.
2. Leave it idle for 2-4 hours.
3. Check Indexing Options to confirm indexing is progressing.
4. Re-evaluate performance after the idle period.

### Fix 3: Reinstall the drivers the update touched

If a specific subsystem broke, reinstall its vendor driver cleanly. GPU: get it from [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, or Intel with the clean-install option. Audio/network/chipset: get them from Dell, HP, or Lenovo support pages. Check Device Manager for the driver dates — a driver dated the day of the update that you didn't install yourself is Windows Update's doing, and replacing it with the vendor version is the fix.

1. Check Device Manager for drivers dated the update day.
2. Download vendor drivers for GPU, audio, network, chipset.
3. Install with clean-install options where offered.
4. Restart and test the previously broken subsystem.

### Fix 4: Clean up update residue

Run Disk Cleanup as administrator (search Disk Cleanup → right-click → Run as administrator), click **Clean up system files**, and check **Windows Update Cleanup** and **Previous Windows installation(s)** — but only the latter if you're sure you won't roll back within 10 days. This can free 10-30 GB and removes the superseded components Windows keeps servicing. A full system drive degrades everything; this is often the difference between "slow since the update" and normal. For ongoing automation, [schedule Disk Cleanup](/articles/how-to-schedule-disk-cleanup-on-windows-10/) so residue never accumulates again.

1. Run Disk Cleanup as administrator.
2. Click **Clean up system files**.
3. Check Windows Update Cleanup (and Previous Windows installations if no rollback planned).
4. Run it and verify freed space afterward.

### Fix 5: Check what settings the update reset

Updates sometimes revert tuned settings. Verify: power plan (Settings → System → Power & battery → Power mode — back to Best performance on AC?), display refresh rate (Settings → System → Display → Advanced display — still at your monitor's max?), default GPU preferences, and startup apps (Task Manager → Startup — did disabled items get re-enabled?). These reversions produce "everything feels slightly off" slowness that's maddening until you spot it. A five-minute settings audit after every feature update prevents this class entirely.

1. Verify power mode is still Best performance on AC.
2. Check display refresh rate is still at maximum.
3. Review Task Manager Startup apps for re-enabled entries.
4. Re-apply any other tuned settings the update reverted.

### Fix 6: Uninstall the problematic update

If the slowness clearly tracks a specific update and fixes haven't helped, remove it: **Settings → Windows Update → Update history → Uninstall updates**, select the culprit, uninstall, restart. For feature updates, the **Recovery → Go back** option works within ~10 days. After uninstalling, pause updates for 1-2 weeks (Windows Update → Pause) to avoid immediate reinstallation while you monitor. This is a legitimate, supported fix — not a hack — for updates that regress performance.

1. Go to **Update history → Uninstall updates**.
2. Select the update that matches the timeline; uninstall it.
3. Restart and verify performance recovered.
4. Pause updates for 1-2 weeks to prevent immediate reinstall.

### Fix 7: Repair the update installation itself

If the update may have installed corruptly (it was interrupted, or errors appear in Update history), repair it: run the Windows Update troubleshooter (Settings → System → Troubleshoot → Other troubleshooters), then in an elevated prompt run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth`. If Update is stuck in a broken state, reset its components (stop wuauserv/bits, rename SoftwareDistribution, restart services) or use the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) to manually install the specific KB. Documented steps for all of this are in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Run the Windows Update troubleshooter.
2. Run `sfc /scannow` then DISM restore-health elevated.
3. If Update is stuck, reset its components (SoftwareDistribution rename).
4. Re-attempt the update or install the KB manually from the Update Catalog.

## Closing

Post-update slowness is a fork in the road: settling or broken. Check the timeline, watch what's actually busy, give legitimate background work its 48 hours — and if it's genuinely broken, work the driver, settings, residue, and uninstall options in order. Most cases resolve at Fix 2 or Fix 3. And the meta-lesson: after every feature update, spend five minutes verifying drivers and settings before the week gets away from you.
