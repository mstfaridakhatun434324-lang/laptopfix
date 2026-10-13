---
title: "Fix Windows 11 Running Slow After an Update"
slug: how-to-fix-windows-11-slow-after-update-youtube
date: 2026-09-14
categories: ["performance"]
tags: ["slow after update", "windows 11", "performance", "windows update"]
description: "Windows 11 slow after the latest update? Work through the post-update checklist: background tasks, drivers, index rebuilds, and rollbacks."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-after-update-youtube.webp"
faqs:
  - q: "Why is my laptop slow right after a Windows update?"
    a: "The first 24–48 hours after an update are legitimately busy: Windows rebuilds the search index, SysMain re-learns your app patterns, the .NET framework re-optimizes, antivirus re-scans changed files, and leftover update files await cleanup. Most post-update slowness resolves on its own within two days — only treat it as a problem if it persists beyond that window."
  - q: "How long should I wait before trying to fix post-update slowness?"
    a: "Give it 48 hours of normal use while plugged in, with the laptop allowed to idle so background tasks can finish. If the system is still slow after two days — or if something is clearly broken like a non-working device — start the fixes in this guide. Acting in the first few hours usually means fighting background tasks that would have finished on their own."
  - q: "Can I uninstall a Windows update that made my laptop slow?"
    a: "Yes, within limits. Go to Settings, then Windows Update, then Update history, then Uninstall updates, and remove the offending cumulative update. Feature updates can be rolled back within ten days from Settings, then System, then Recovery. Note that uninstalling security updates leaves you exposed, so treat removal as a diagnostic step, not a permanent strategy."
  - q: "Will updating drivers fix slowness caused by a Windows update?"
    a: "Often, yes. Feature updates replace core system components that old drivers were built against, and mismatched graphics, chipset, or storage drivers are a top cause of persistent post-update slowness. Check your laptop manufacturer's support site for drivers released specifically for the new Windows build before assuming the update itself is at fault."
---

It is the classic sequence: Windows installs an update overnight, you boot up in the morning, and the laptop that was fine yesterday now takes forever to do anything. Fans spin, disk churns, apps hesitate. Your first instinct — that the update broke something — is sometimes right. But just as often, the update is fine and the system is simply busy digesting it.

The skill here is telling those two situations apart without wasting a weekend. This guide gives you the post-update triage order: what is normal and needs patience, what is a driver mismatch needing updates, what is leftover junk needing cleanup, and when to roll the update back entirely.

## Why this happens

- **Post-update background tasks:** Index rebuilds, SysMain re-profiling, and .NET optimization all run after updates and saturate CPU and disk for a day or two.
- **Driver mismatches:** The update replaced OS components that old GPU, chipset, or storage drivers were built against, causing stutters and hangs.
- **Leftover update files:** Staging files, the Windows.old folder, and update caches consume disk space and keep background cleaners busy.
- **Reset settings and re-enabled features:** Feature updates restore defaults — re-enabling suggestions, telemetry, and background apps you had turned off.
- **Corrupted update installation:** A partially failed update leaves the system in a half-migrated state with broken services and constant error retries.
- **Antivirus re-scanning:** Security software re-scans every changed system file after an update, adding hours of background I/O.
- **Firmware/BIOS lagging behind:** New Windows builds sometimes expect newer firmware behavior, and an old BIOS causes subtle performance and power issues.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it 48 hours (the legitimate waiting period)

1. Keep the laptop plugged in and let it idle for extended periods over the next two days — background tasks need idle time to finish.
2. Check **Settings → Windows Update** to confirm no update is still downloading or installing.
3. Open Task Manager and note which processes are busy — **Search Indexer**, **SysMain**, and **.NET Runtime Optimization Service** are all normal post-update workers.
4. If everything is calm after 48 hours but the laptop is still slow, the problem is real — continue. If it recovered, you just saved yourself a wasted troubleshooting session.

### Fix 2: Clean up the update leftovers

1. Press **Win + R**, type `cleanmgr`, select C:, click **Clean up system files**, and check **Windows Update Cleanup** and **Delivery Optimization Files**.
2. Let it run — the first cleanup after a feature update can free 10–20GB and take a while.
3. Decide on **Previous Windows installation(s)** (Windows.old): keep it if you might roll back within ten days, remove it if the update is staying.
4. Our [temporary files deep-clean](/articles/how-to-clean-temporary-files-in-windows-11-24h2/) covers every leftover category if disk space stays tight after this pass.

### Fix 3: Update drivers for the new build

1. Visit your manufacturer's support site (Dell, HP, and Lenovo each host model-specific driver pages) and check for drivers released for your current Windows build.
2. Prioritize **chipset**, **graphics**, and **storage** drivers; these three cause the most post-update slowness when stale.
3. For Intel graphics or Wi-Fi, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) often has newer drivers than Windows Update.
4. Restart after each major driver install and test — install one at a time so you know which one helped.

### Fix 4: Repair the update installation itself

1. Run **Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run**.
2. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` when it finishes.
3. Check **Settings → Windows Update → Update history** for failed updates and retry them individually.
4. A failed update stuck in a retry loop keeps background services busy indefinitely — clearing it often fixes "slow since the update" in one move.

### Fix 5: Re-tame the settings the update reset

1. Re-check **Settings → System → Notifications → Additional settings** — updates re-enable tips and suggestions.
2. Review **Settings → Apps → Installed apps** for anything the update reinstalled or added.
3. Check **Task Manager → Startup apps** for re-enabled entries and disable the ones you had turned off.
4. Our guide to [turning off tips and suggestions](/articles/how-can-i-turn-off-windows-tips-and-suggestions/) is the checklist for this exact cleanup.

### Fix 6: Address the usual post-update resource hogs

1. If **Search Indexer** is still rebuilding after 48 hours, rebuild it manually (**Control Panel → Indexing Options → Advanced → Rebuild**) to clear a stuck crawl.
2. If **SysMain** is saturating a mechanical drive, restart the service or disable it per our [SysMain guide](/articles/how-to-fix-sysmain-high-disk-usage-step-by-step/).
3. If disk is pegged at 100% generally, work through the [100% disk diagnosis](/articles/how-to-fix-disk-active-time-100-percent-youtube/) — updates expose marginal disks.
4. Give each fix a few hours of observation before stacking the next one; post-update systems are noisy and premature changes muddy the diagnosis.

### Fix 7: Roll back the update as a last resort

1. For a cumulative update: **Settings → Windows Update → Update history → Uninstall updates**, select the recent one, and uninstall.
2. For a feature update (within ten days): **Settings → System → Recovery → Go back**.
3. Before rolling back, use **Pause updates** (up to five weeks) to stop Windows from immediately reinstalling the problematic update.
4. If rollback is impossible and slowness persists, consider an in-place repair install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — it refreshes system files while keeping your apps and data.

## Closing

Post-update slowness is usually patience (48 hours), cleanup (update leftovers), or drivers (mismatched with the new build) — in that order. Work the list, give each step time to prove itself, and reserve the rollback for the rare update that is genuinely broken. Most "slow since the update" laptops are fast again by Fix 3.
