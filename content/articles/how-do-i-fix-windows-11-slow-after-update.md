---
title: "Windows 11 Slow After an Update? Roll Back the Damage Step by Step"
slug: how-do-i-fix-windows-11-slow-after-update
date: 2026-09-28
categories: ["performance"]
tags: ["windows 11 slow after update", "slow performance", "windows update", "rollback", "troubleshooting"]
description: "Windows 11 turned sluggish right after an update? Here's how to confirm the update is the cause, roll it back safely, and prevent it from reinstalling."
thumbnail: "/images/thumbs/how-do-i-fix-windows-11-slow-after-update.webp"
faqs:
  - q: "How long should I wait before deciding an update made my laptop slow?"
    a: "Give it 24 to 48 hours of normal use first. After a feature update, Windows runs background optimization — indexing, .NET optimization, Defender scans, and Store app updates — that legitimately slows the machine for a day or two. If performance is still clearly worse after two full days and reboots, the update itself is the problem and the fixes below apply."
  - q: "Will uninstalling a Windows update delete my files?"
    a: "No. Uninstalling a quality update removes only the update's changes; your personal files, installed apps, and settings remain. A feature-update rollback (within the 10-day window) also preserves files but takes longer. Either way, keep a current backup before major system changes — it is cheap insurance against the unexpected."
  - q: "Can I stop Windows from reinstalling the update I removed?"
    a: "For quality updates, you can pause updates for up to five weeks in Settings, which is usually enough time for Microsoft to fix a bad patch. For a specific problematic update, Microsoft's Show or Hide Updates troubleshooter lets you block it individually. For drivers, disabling automatic driver updates prevents Windows from reinstalling the bad driver version."
  - q: "What if the 10-day rollback window for a feature update has expired?"
    a: "After ten days, Windows deletes the Windows.old folder and the one-click rollback disappears. Your options then are an in-place upgrade repair using fresh installation media, which reinstalls Windows while keeping files and apps, or a clean install. Both take longer than a rollback, which is why acting within the window matters."
---

The pattern is maddeningly consistent: the laptop was fine yesterday, Windows installed an update overnight, and now everything is slow — boot takes twice as long, apps hesitate, the whole machine feels like it's wading through mud. You're not imagining it. Updates change drivers, reset settings, and sometimes ship with genuine performance regressions. The fix is a disciplined sequence: confirm the update is actually the cause, repair what it broke, and roll it back if repair fails.

Resist the urge to start "optimizing" randomly. The update changed specific things; your job is to find which change hurt and reverse it.

## Why this happens

- **Post-update background optimization:** Indexing rebuilds, .NET native image generation, and Store app updates hammer the disk and CPU for a day or two after major updates.
- **Driver replacement:** Windows Update installs generic drivers over vendor-tuned ones — graphics, storage, and chipset drivers are frequent victims.
- **Reset power and performance settings:** Feature updates can revert custom power plans, re-enable eco modes, or reset GPU preferences.
- **Corrupted update installation:** A partially failed update leaves the system in a degraded state with mismatched components.
- **New bugs in the update itself:** Some updates ship with real performance regressions affecting specific hardware.
- **Re-enabled bloatware and startup items:** Updates can reinstall removed apps and re-enable startup entries you previously disabled.
- **Disk space consumed by update files:** Windows.old and update caches can eat tens of gigabytes, leaving the system starved for working space.
- **Antivirus re-scanning everything:** Defender often performs full re-scans of the changed system after major updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait out the background storm (but verify it ends)

Open Task Manager and check whether Search indexer, .NET optimization (mscorsvw), TiWorker, or Defender scans are consuming resources. If they are, the slowdown may be legitimate post-update work. Give it 24–48 hours of plugged-in idle time to finish — but set a deadline. If the same processes are still hammering the system after two days, it's not optimization anymore, it's a stuck process. For the step-by-step version of post-update recovery, see [laptop slow after the 24H2 update](/articles/how-to-fix-laptop-slow-after-windows-11-24h2-update-step-by-step/).

1. Task Manager → identify post-update background processes.
2. Leave the laptop plugged in and idle to let them finish.
3. Set a 48-hour deadline; re-evaluate after.
4. If heavy background use persists past the deadline → stuck process, continue.

### Fix 2: Confirm the timeline in Reliability Monitor

Run `perfmon /rel` and look at the timeline: mark the date the update installed and the date slowness began. If they line up within a day or two, causation is likely. Note exactly which update (KB number) installed — you'll need it for targeted uninstallation. Also check for driver updates installed the same day; Windows Update history (Settings → Windows Update → Update history) lists them. This evidence prevents you from rolling back the wrong thing.

1. Run `perfmon /rel`; correlate update date with slowdown onset.
2. Note the KB number of the suspect update.
3. Check Update history for same-day driver updates.
4. Proceed only if the timeline implicates the update.

### Fix 3: Roll back replaced drivers

Device Manager → check Display adapters, Storage controllers, and System devices for driver dates matching the update day. For each suspect: Properties → Driver → Roll Back Driver. Graphics drivers are the priority — a generic Microsoft display driver replacing the vendor's can halve perceived performance. If rollback is grayed out, download the vendor driver manually (NVIDIA, AMD, or Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)) and install it over the generic one.

1. Device Manager → find devices with driver dates matching the update.
2. Properties → Driver → Roll Back Driver for each suspect.
3. Prioritize graphics, chipset, and storage drivers.
4. If rollback unavailable, install the vendor driver manually.

### Fix 4: Restore your power and startup configuration

Check Settings → System → Power & battery: confirm your power mode survived the update, and re-disable any eco modes the update re-enabled. Then Task Manager → Startup apps: disable everything the update re-enabled that you don't need. Updates also reinstall bloatware — revisit Settings → Apps and remove what came back. These three checks (power mode, startup, bloatware) take ten minutes and recover a surprising amount of lost performance. The broader [Windows 11 slow-after-update guide](/articles/windows-11-slow-after-update-how-to-fix/) covers the same ground with extra detail.

1. Verify power mode; re-disable re-enabled eco modes.
2. Task Manager → Startup apps → disable unneeded re-enabled entries.
3. Settings → Apps → remove reinstalled bloatware.
4. Reboot and compare responsiveness.

### Fix 5: Free the disk space the update consumed

Check free space on C:. If it's under 15–20GB, the update's leftovers are starving the system: run Disk Cleanup as admin (clean system files, including Windows Update Cleanup and Previous Windows installations — but only delete Windows.old if you're sure you won't roll back). Also run Storage Sense. Low disk space after an update is a direct, mechanical cause of slowness — paging, temp files, and updates all need breathing room. Aim for at least 20% free on the system drive.

1. Check free space on C:; under 15–20GB is a problem.
2. Disk Cleanup (admin) → Clean up system files → remove update leftovers.
3. Keep Windows.old only if you plan a rollback (Fix 6).
4. Confirm 20%+ free space afterward.

### Fix 6: Uninstall the update or roll back the feature update

For a quality update: Settings → Windows Update → Update history → Uninstall updates → remove the suspect KB. For a feature update within 10 days: Settings → System → Recovery → Go back. After removal, pause updates (up to 5 weeks) or use Microsoft's Show/Hide Updates tool to block the specific KB so it doesn't reinstall overnight. Microsoft documents these steps on the [Windows support site](https://support.microsoft.com/en-us/windows). Test thoroughly for a day before unpausing — you need to know the rollback actually fixed it.

1. Uninstall the suspect KB (or Go back for feature updates).
2. Pause updates or block the specific KB from reinstalling.
3. Use the laptop normally for a full day.
4. Only unpause once you're confident the problem is gone.

### Fix 7: Repair install as the last resort

If rollback isn't available (window expired) or didn't help, do an in-place upgrade repair: download the Windows 11 media from the [official download page](https://www.microsoft.com/en-us/software-download/windows11), run setup, and choose to keep files and apps. This reinstalls Windows cleanly over itself, fixing corrupted update states while preserving your setup. It's the closest thing to a fresh install without the fresh-install pain, and it resolves update damage that uninstallation can't reach.

1. Download official Windows 11 installation media.
2. Run setup → choose Keep personal files and apps.
3. Let the repair install complete (1–2 hours).
4. Re-verify performance and reinstall blocked updates cautiously.

## Closing

Post-update slowness is one of the few performance problems with a clear suspect and a clear paper trail — the update history tells you exactly what changed and when. Work the timeline, repair drivers and settings first, and roll back only when repair fails. And once you're stable, pause updates for a few weeks after each Patch Tuesday; letting other people's machines beta-test a patch is the cheapest performance insurance there is.
