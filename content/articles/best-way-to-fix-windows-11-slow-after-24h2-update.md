---
title: "The Best Way to Fix a Slow Windows 11 After the 24H2 Update"
slug: best-way-to-fix-windows-11-slow-after-24h2-update
date: 2026-10-11
categories: ["performance"]
tags: ["windows 11 24h2", "slow after update", "performance fix", "24h2 slow", "update issues"]
description: "Windows 11 24H2 left your laptop sluggish? This is the best fix sequence: finish the update's background work, repair what it broke, and restore your tuned settings."
thumbnail: "/images/thumbs/best-way-to-fix-windows-11-slow-after-24h2-update.webp"
faqs:
  - q: "How long does Windows 11 24H2 take to settle after updating?"
    a: "Typically 24 to 72 hours of normal use while plugged in. During this window Windows rebuilds the search index, re-optimizes apps, runs compatibility telemetry, and completes deferred update tasks. Judging performance during the first day is premature — let the background work finish before deciding anything is broken."
  - q: "Should I roll back the 24H2 update if my laptop is slow?"
    a: "Only as a last resort, and only within the 10-day rollback window. Most post-24H2 slowness is fixable: background tasks finishing, drivers needing updates, or settings that got reset. Rollback also forfeits security improvements. Work through the fix sequence first — rollback is for cases where the update itself is fundamentally incompatible with your hardware."
  - q: "Why did 24H2 make my laptop slower when it was fine before?"
    a: "Feature updates do four disruptive things at once: they run days of background re-indexing and optimization, they replace your tuned drivers with generic ones, they reset power and privacy settings to defaults, and they reinstall apps you had removed. The slowness is usually the combination, not any single failure — which is why a sequence of fixes works better than one tweak."
  - q: "Will 24H2 slow down older laptops permanently?"
    a: "Not inherently. 24H2's system requirements match 23H2's, so hardware that ran the old version fine can run the new one fine. Persistent slowness after the settling period points to fixable issues — outdated drivers, reset settings, or re-enabled background services — not to the update being too heavy for your machine."
---

The pattern is familiar: 24H2 installs overnight, and the next morning your laptop feels like it aged three years. Apps crawl, the disk churns, the fans spin — and nothing you did caused it. Before you blame the update itself, know this: most post-24H2 slowness is not the new Windows being heavier. It is the update's aftermath — background tasks, replaced drivers, and reset settings — all hitting at once. And aftermath is fixable.

This is the best-practice sequence for post-24H2 slowness: let the legitimate background work finish, repair what the update disturbed, and restore the optimizations it undid.

## Why this happens

- **Post-update background storm:** Search index rebuilds, app re-optimization, telemetry uploads, and deferred tasks saturate CPU and disk for 1–3 days.
- **Drivers replaced with generics:** 24H2 often swaps manufacturer-tuned graphics, storage, and chipset drivers for Microsoft's generic versions.
- **Settings reset to defaults:** Power mode, privacy toggles, notification preferences, and disabled services frequently revert during feature updates.
- **Removed apps reinstalled:** Bloatware you uninstalled can return with the new feature release, along with new preinstalled apps.
- **Old update files lingering:** Windows.old and delivery optimization files consume 20–30 GB until cleaned, and a nearly full drive slows everything.
- **Search index invalidated:** The old index is discarded, forcing a full rebuild that hammers slower drives.
- **Antivirus re-registration:** Security software re-hooks into the system after the update, sometimes triggering full re-scans.
- **Firmware mismatch:** Old BIOS/UEFI versions can interact poorly with 24H2's changed power and security behavior until updated.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the background storm finish (patience as a fix)

1. Plug in the laptop, leave it on for several hours (overnight is ideal), and let Windows complete its post-update tasks.
2. Open **Task Manager** and check whether heavy activity comes from **Search Indexer**, **Windows Modules Installer**, or **CompatTelRunner** — these are legitimate one-time tasks.
3. Do not judge performance until these settle. Interrupting them repeatedly (by shutting down mid-task) stretches a one-day process into a week.
4. If heavy background activity persists beyond 72 hours of plugged-in idle time, it is no longer normal — continue with the fixes below.

### Fix 2: Reinstall your proper drivers

1. Open **Device Manager** and check **Display adapters**, **IDE ATA/ATAPI controllers**, and **System devices** for generic Microsoft drivers where manufacturer drivers used to be.
2. Download fresh drivers from your laptop manufacturer's support site: chipset first, then graphics, then storage/network.
3. For Intel systems, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) automates detection; NVIDIA and AMD users should get graphics drivers from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
4. Restart after each driver family and retest. Driver restoration alone fixes a large share of post-update slowness.

### Fix 3: Restore your power and performance settings

1. Check **Settings → System → Power & battery → Power mode** — 24H2 commonly resets this to Balanced or Best power efficiency.
2. Set it back to your preference (**Best performance** while plugged in for heavy work).
3. Re-verify any manufacturer performance modes (Turbo/Performance) — their utilities sometimes revert after OS updates too.
4. Check **Settings → Gaming → Game Mode** is still on if you game. Our [power plan guide](/articles/how-to-change-power-plan-to-best-performance-in-windows-11-24h2/) details the full setup.

### Fix 4: Clean up the update's leftovers

1. Run **Disk Cleanup** as administrator → **Clean up system files** → check **Previous Windows installations**, **Delivery Optimization Files**, and **Temporary Windows installation files**.
2. This typically reclaims 20–30 GB and removes the rollback copy once you are committed to 24H2 (past the 10-day window or confident in stability).
3. Enable **Storage Sense** (**Settings → System → Storage**) so future update debris gets cleaned automatically.
4. Verify C: has at least 15–20 percent free afterward — a cramped drive after the update explains lingering sluggishness. See [low disk space after update](/articles/how-to-fix-low-disk-space-on-c-drive-after-windows-11-update/) for the deep version.

### Fix 5: Remove the apps 24H2 brought back

1. Go to **Settings → Apps → Installed apps** and sort by install date — the update's additions cluster at the top.
2. Uninstall the bloatware you had previously removed, plus any new preinstalled apps you do not want.
3. Check **Task Manager → Startup apps** for new autostart entries the update added and disable them.
4. Fewer background apps means less competition for CPU, RAM, and disk from the moment you log in.

### Fix 6: Repair the system files the update may have damaged

1. Open an **admin Terminal** and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. Feature updates touch thousands of system files; these tools find and repair the ones that did not land cleanly.
3. Restart and test your slowest scenarios (app launches, game loading, boot time).
4. If corruption is found and repaired, this step alone can transform the system's feel.

### Fix 7: Update BIOS/UEFI firmware

1. Check your manufacturer's support site for BIOS updates released around or after 24H2 — changelogs often mention 24H2 compatibility or power behavior fixes.
2. Apply the update following the manufacturer's instructions exactly (plugged in, no interruptions).
3. After updating, re-check power and thermal behavior — firmware updates frequently resolve the mysterious "slow since the update" cases that software fixes cannot.
4. This is especially important on laptops 2+ years old, where the factory BIOS predates 24H2's expectations.

### Fix 8: Decide on rollback (last resort)

1. Go to **Settings → System → Recovery** and check whether **Go back** is available (only within ~10 days of the update).
2. Roll back only if the laptop is unusably slow after all fixes above and you have identified no other cause.
3. Before rolling back, back up your files — the process preserves them, but a backup is non-negotiable insurance.
4. After rollback, pause feature updates temporarily while you research whether your specific model's issues have known fixes, so 24H2 does not reinstall before you are ready.

## Closing

Post-24H2 slowness feels like the update broke your laptop, but it is almost always the update's aftermath: background tasks still running, drivers swapped for generics, settings reset, and bloatware returned. Give the background work its 72 hours, restore your drivers and settings, clean the leftovers, and repair what landed badly. In that order, the laptop that felt three years older wakes back up — running the new Windows at the speed of the old one.
