---
title: "Windows 11 Slow After an Update? Step-by-Step Fix"
slug: how-to-fix-windows-11-slow-after-update-step-by-step
date: 2026-09-26
categories: ["performance"]
tags: ["windows 11 slow after update", "post-update slow", "update cleanup", "performance fix"]
description: "Windows 11 painfully slow after an update? Work through this step-by-step recovery: let background work finish, clean up, fix drivers, and roll back if needed."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-after-update-step-by-step.webp"
faqs:
  - q: "How long should I wait before fixing post-update slowness?"
    a: "Give it 24-48 hours of plugged-in idle time first. After feature updates especially, Windows runs background optimization — .NET compilation, search reindexing, Defender rescans, and update cleanup — that legitimately slows the system. If the laptop is still slow after two days of normal use with idle time, the slowness is a real problem needing the steps below, not just background work."
  - q: "Can I uninstall a Windows update that made my laptop slow?"
    a: "Yes, for 10 days after a feature update you can roll back the entire update via Settings > System > Recovery > Go back. For monthly quality updates, uninstall the specific KB via Settings > Windows Update > Update history > Uninstall updates. Rolling back is safe and keeps your files, but only the feature-update rollback has a time limit."
  - q: "Why do updates make Windows slower even after they finish?"
    a: "Updates can install buggy drivers (especially graphics and storage), reset your tuned settings (power plans, disabled services), leave behind gigabytes of staging files, and trigger incompatible third-party software. The update itself usually isn't the ongoing problem — it's one of these side effects. That's why the fix sequence targets drivers, settings, and cleanup rather than the update mechanism."
  - q: "Will pausing updates prevent future slowdowns?"
    a: "Pausing delays updates but doesn't prevent the eventual post-update settling period — it just moves it. A better strategy is controlling when updates install: set active hours, let feature updates install when you have a free evening, and keep drivers current so update-bundled driver swaps are less disruptive. Staying updated matters for security; timing is what you control."
---

The update finished, the laptop rebooted, and now everything is slow — boot takes forever, apps crawl, the fan won't quit. Post-update slowness is one of the most common Windows 11 complaints, and it's frustrating because the thing that was supposed to improve your PC made it worse. The good news: it's usually temporary background work or a fixable side effect, not permanent damage.

This is a strict step-by-step sequence. Don't skip to rollback before checking the earlier steps — most post-update slowness resolves at steps 1–4. For update-engine-specific CPU issues, see [Windows Modules Installer high CPU](/articles/how-to-fix-windows-modules-installer-high-cpu-reddit/); for general speed, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Background post-update optimization**: .NET ngen, search reindexing, and Defender rescans run for hours after updates.
- **New driver installed by the update**: Update-bundled graphics/storage drivers that are buggier than your old ones.
- **Settings reset by the update**: Power plans, disabled services, and privacy settings reverted to defaults.
- **Leftover staging files**: Gigabytes of $WINDOWS.~BT and update cache consuming disk space.
- **Pending restart or phased install**: The update isn't actually finished — more phases run on subsequent boots.
- **Third-party software incompatibility**: Antivirus, VPNs, or utilities conflicting with changed Windows components.
- **Corrupt update installation**: A partially-failed update leaving components in a degraded state.
- **Disk nearly full after update**: Updates need free space; a full drive post-update cripples performance.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the update actually finished

Half the "slow after update" cases are updates still working.

1. Open **Settings** > **Windows Update** — check for "Installing," "Pending restart," or additional updates queued behind the first one.
2. Restart when prompted — some updates don't finalize until the reboot, and the pre-reboot state is slow by design.
3. After restarting, check **Update history** for failures — a failed update followed by retries explains ongoing slowness.
4. Leave the laptop plugged in and idle overnight — post-update background tasks (indexing, Defender, .NET optimization) are designed to run when you're away.
5. Only proceed to Fix 2 if the system is still slow after updates show complete AND the machine has had idle time.

### Fix 2: Identify the new bottleneck

Find what specifically got slower.

1. Open **Task Manager** > **Performance** during normal use — which resource is saturated: CPU, Disk at 100%, or Memory maxed?
2. In **Processes**, sort by the saturated resource — name the top consumers (TiWorker, SearchIndexer, Antimalware Service Executable are the usual post-update suspects).
3. Compare boot time and app launch speed against your memory of pre-update behavior — quantify "slow" so you can verify the fix worked.
4. Check free space on C: — if the update ate your last gigabytes, that's a prime suspect.
5. This diagnosis directs the next steps: disk saturation → Fixes 3–4; specific process → target that process; everything slow → Fix 5 (drivers).

### Fix 3: Clean up update leftovers

Reclaim the space and remove the debris.

1. Run **Disk Cleanup** (`cleanmgr`) > **Clean up system files** — check **Previous Windows installations** (only if you're sure you won't roll back within 10 days), **Temporary Windows installation files**, **Delivery Optimization Files**, and **Windows Update Cleanup**.
2. This can free 10–30GB after a feature update — and a cramped drive is a slow drive.
3. Go to **Settings** > **System** > **Storage** > **Cleanup recommendations** for additional large-file wins.
4. Don't manually delete `C:\Windows\SoftwareDistribution` contents unless updates are failing — the cleanup tools handle the safe parts.
5. Verify C: now has 15–20% free space, then restart and re-test performance.

### Fix 4: Let background tasks finish, then tame them

Distinguish one-time settling from permanent problems.

1. Open **Task Scheduler** (`taskschd.msc`) — check **Microsoft** > **Windows** > **.NET Framework** for `ngen` tasks; these compile .NET assemblies post-update and are legitimately heavy but finite.
2. Check the search index status (**Settings** > **Privacy & security** > **Searching Windows**) — reindexing after a feature update takes hours; let it complete.
3. In **Windows Security**, check whether Defender is running a post-update full scan — let it finish rather than fighting it.
4. Once these complete (give it the overnight idle session), they shouldn't return — if the same heavy processes persist for days with no new updates, they're stuck, not settling.
5. For processes that won't settle, apply their specific fixes (SysMain disable, index rebuild, Defender reschedule) rather than enduring them.

### Fix 5: Fix update-installed drivers

The most common permanent post-update slowdown cause.

1. Open **Device Manager** > **Display adapters** — if the driver date changed with the update, the new graphics driver is suspect #1.
2. Roll back: right-click > **Properties** > **Driver** > **Roll Back Driver** — test performance for a day.
3. If rollback isn't available, download the previous known-good driver from your laptop manufacturer's support page (or [Intel](https://www.intel.com/content/www/us/en/support/detect.html)/[NVIDIA](https://www.nvidia.com/Download/index.aspx)/[AMD](https://www.amd.com/en/support/download/drivers.html)) and install it cleanly.
4. Also check **Storage controllers** and **Network adapters** for update-swapped drivers.
5. To prevent recurrence: **Settings** > **Windows Update** > **Advanced options** > turn off **Receive updates for other Microsoft products** if driver swaps keep causing trouble, and consider pausing driver updates via Group Policy on Pro.

### Fix 6: Restore your tuned settings

Updates reset customizations silently.

1. Check **Settings** > **System** > **Power & battery** > **Power mode** — updates often reset this; restore your preferred setting.
2. Recheck `services.msc` for services you'd disabled (SysMain, Windows Search) — re-disable as needed.
3. Review **Task Manager** > **Startup apps** — updates and reinstalled apps re-add startup entries; trim again.
4. Check your default apps and privacy settings if the update was a feature release — these get reset too.
5. Keep a personal checklist (text file) of your post-update re-tuning steps — you'll use it twice a year.

### Fix 7: Roll back the update

When the update itself is the problem.

1. For feature updates (within 10 days): **Settings** > **System** > **Recovery** > **Go back** — follow the prompts; your files are preserved.
2. For quality updates: **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the specific KB, then **Pause updates** for 1–2 weeks while Microsoft fixes it.
3. Before rolling back, try the in-place repair first: `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — a corrupt (not buggy) update sometimes repairs cleanly.
4. After rollback, use the "Show or hide updates" troubleshooter to block the problematic update from reinstalling immediately.
5. Report the issue via **Feedback Hub** — Microsoft prioritizes fixes partly by report volume. Check the [Windows support hub](https://support.microsoft.com/en-us/windows) for known issues with your specific update.

## Closing

Slow after an update follows a predictable arc: background settling, then cleanup, then driver and settings repair, then rollback if truly necessary. Most cases never reach rollback — they resolve when the background work finishes or the bad driver is replaced. Work the steps in order, verify each one, and your laptop comes back.
