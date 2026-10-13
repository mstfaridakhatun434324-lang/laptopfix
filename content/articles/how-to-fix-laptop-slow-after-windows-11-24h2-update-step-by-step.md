---
title: "Laptop Slow After the Windows 11 24H2 Update? Step-by-Step Speed-Up"
slug: how-to-fix-laptop-slow-after-windows-11-24h2-update-step-by-step
date: 2026-09-13
categories: ["performance"]
tags: ["slow laptop", "windows 11 24h2", "step by step", "performance", "windows update"]
description: "Laptop sluggish after the Windows 11 24H2 update? A step-by-step recovery plan: let it settle, fix drivers, trim bloat, and restore speed."
thumbnail: "/images/thumbs/how-to-fix-laptop-slow-after-windows-11-24h2-update-step-by-step.webp"
faqs:
  - q: "How long should I wait after the 24H2 update before troubleshooting?"
    a: "Give it 48 hours of normal plugged-in use, including some idle time. The 24H2 upgrade triggers extensive background work: search re-indexing, Defender re-baselining, .NET optimization, Store app updates, and WinSxS cleanup, all competing for CPU and disk. Judging performance during this storm leads to unnecessary fixes. If the laptop is still slow after two full days of use, the slowness is real and the steps below apply."
  - q: "Will my laptop ever be as fast as before 24H2?"
    a: "In the large majority of cases, yes — post-update slowness is transitional, not permanent. Once background maintenance completes and drivers are correct, 24H2 generally performs on par with or slightly better than 23H2 on the same hardware. Persistent slowness beyond the settling period points to a specific fixable cause: a driver mismatch, a runaway background process, or settings the update reset, each addressed in this guide."
  - q: "Should I roll back to 23H2?"
    a: "Rollback is available for ten days after the upgrade and is worth considering only if the laptop is unusably slow and you have identified no fixable cause after working through proper troubleshooting. Most post-24H2 slowness has a direct fix that keeps you on the supported release with its security improvements. Roll back as a last resort, not a first step — and back up before you do."
  - q: "Does 24H2 need better hardware than 23H2?"
    a: "No. The official system requirements did not change between 23H2 and 24H2, and performance on identical hardware is comparable once settled. If your laptop met the requirements before, it meets them now. Perceived new slowness is about the update's transitional workload and driver state, not raised hardware demands. Do not buy hardware to fix what is fundamentally a software settling issue."
---

The Windows 11 24H2 update finished, you rebooted, and your laptop feels like it's wading through mud — slow boot, laggy apps, fans working overtime. Before you panic or roll back, understand what's normal: 24H2 is a huge upgrade, and the first 48 hours are a storm of background maintenance (indexing, Defender re-baselining, .NET optimization, Store updates, component cleanup) that makes any laptop feel slow. Much of the "24H2 made my laptop slow" experience is this storm, and it passes.

But not all of it. Updates also replace drivers with generic versions, reset power and gaming settings, and occasionally leave background processes stuck. This step-by-step guide separates the transient from the real: first the waiting period done right, then the ordered fixes for what remains — drivers, background hogs, settings, and disk. Work it top to bottom, measuring as you go. For the focused CPU guides, see [Defender high CPU on 24H2](/articles/how-to-fix-antimalware-service-executable-high-cpu-fix-in-windows-11-24h2/) and [Windows Modules Installer on 24H2](/articles/how-to-fix-windows-modules-installer-high-cpu-in-windows-11-24h2/).

## Why this happens

- **Post-upgrade background storm**: Indexing, Defender, .NET optimization, and cleanup all running at once.
- **Drivers replaced with generic versions**: GPU, chipset, and storage drivers swapped during the upgrade.
- **Power and performance settings reset**: Power plans and thermal profiles reverted to defaults.
- **Stuck background processes**: A servicing or scan task that never finished, burning CPU indefinitely.
- **Settings and features re-enabled**: Game Bar recording, widgets, and background apps switched back on.
- **Disk nearly full**: The upgrade needs staging room; a full drive compounds every slowdown.
- **Pending follow-up updates**: Day-one patches that fix 24H2 issues not yet installed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the storm pass — properly

Don't troubleshoot during the settling period.

1. Confirm 24H2 installed: **Settings** > **System** > **About** > **Version 24H2**; note the install date in **Windows Update** > **Update history**.
2. Keep the laptop **plugged in** and let it sit idle for several hours (overnight is ideal) — background maintenance completes fastest when you're not competing with it.
3. Install all pending updates: **Settings** > **Windows Update** > **Check for updates** — run it repeatedly until clear, including optional driver updates.
4. Use the laptop normally for 48 hours total before judging — note specific symptoms (slow boot? laggy apps? fan noise?) rather than a vague "slow."
5. After 48 hours, reassess: if it's genuinely still slow, the remaining causes are specific and fixable — continue below.

### Fix 2: Find the resource hog

Identify what's actually slow.

1. Open **Task Manager** > **Performance** during normal use — which is saturated: CPU, memory, or disk? That determines everything.
2. **Processes** sorted by CPU: look for MsMpEng.exe (Defender), TiWorker.exe (servicing), SearchIndexer.exe, or a third-party process stuck high.
3. If **disk** is pegged at 100%, note the top disk consumers — servicing, indexing, and antivirus are the usual trio.
4. Check **Startup** impact in Task Manager > **Startup apps** — the upgrade sometimes re-enables disabled entries.
5. Write down the top 2–3 consumers — each has a targeted fix in the linked guides; don't guess.

### Fix 3: Restore proper drivers

The highest-impact real fix.

1. **GPU driver**: check **Device Manager** > **Display adapters** > driver date — if it matches the upgrade, Windows replaced it. Reinstall from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) with a clean install.
2. **Chipset driver**: get it from your laptop manufacturer's support site by exact model — chipset drivers govern power management and I/O performance.
3. **Storage/network drivers**: update from the manufacturer — stale storage drivers are a quiet source of system-wide sluggishness.
4. **BIOS/firmware**: check for a 24H2-era BIOS update from the manufacturer — firmware fixes for new OS versions are common.
5. Reboot fully after driver updates and re-measure — driver restoration is the fix behind most "24H2 permanently slowed my laptop" reports.

### Fix 4: Fix power and thermal settings

The update may have capped your performance.

1. Set the battery power slider to **Best performance** when plugged in; check **Settings** > **System** > **Power & battery** > **Power mode**.
2. Open your manufacturer's control app (Vantage, Armoury Crate, Dell Power Manager, MyASUS) and confirm the thermal/performance profile — upgrades often reset these to balanced/quiet.
3. Clean dust from vents with compressed air (laptop off) — thermal throttling feels exactly like "update made it slow" and worsens as background work heats the machine.
4. Ensure the laptop sits on a hard surface — blocked vents during the post-upgrade storm cause throttling that persists.
5. Verify the fix under load: run your normal heavy task and confirm CPU boosts properly instead of throttling early.

### Fix 5: Trim what the upgrade re-enabled

Reclaim your configuration.

1. **Task Manager** > **Startup apps** — re-disable everything the upgrade turned back on.
2. **Settings** > **Gaming** > **Xbox Game Bar** off (if unused); **Captures** > background recording off.
3. **Settings** > **Personalization** > **Taskbar** > **Widgets** off if you don't use them.
4. **Settings** > **Apps** > **Installed apps** — remove any bloatware the upgrade reinstalled (it happens).
5. Review **Task Scheduler** for re-enabled manufacturer tasks and disable the unnecessary ones. Our [bloatware removal guide](/articles/how-to-remove-bloatware-from-windows-11-laptop/) covers the full cleanup.

### Fix 6: Address disk pressure

Upgrades are disk-hungry.

1. Free space to 15%+ on C: — the upgrade stages gigabytes and a full drive slows everything (see [freeing disk space](/articles/how-to-free-up-disk-space-on-windows-11/)).
2. Run **Disk Cleanup** > **Clean up system files** and remove **Previous Windows installations** once you're committed to 24H2 — often 20–30 GB.
3. Enable **Storage Sense** for automatic maintenance going forward.
4. Check drive health: `wmic diskdrive get status` — rule out hardware as the slowness source.
5. If still on an HDD, this is the moment to consider the SSD upgrade — 24H2's background workload is punishing on spinning disks.

### Fix 7: Decide on rollback vs. repair

The final decision point.

1. If you've done Fixes 1–6 and the laptop is still clearly slower than pre-24H2, check **Settings** > **System** > **Recovery** — **Go back** is available for 10 days post-upgrade.
2. Before rolling back, run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow` — corruption, not 24H2, is sometimes the real cause, and repair keeps you current.
3. Search for your specific symptom plus 24H2 — widely-reported issues get patched within weeks; waiting for the patch beats rolling back.
4. If you roll back, back up first, and plan the 24H2 retry later with drivers pre-downloaded.
5. Whatever you choose, keep Windows updated afterward — Microsoft's Windows Update support pages track known 24H2 issues and their fixes.

## Closing

The 24H2 slowdown playbook is simple: respect the 48-hour storm, then work the real causes in order — drivers, resource hogs, power settings, re-enabled bloat, disk pressure. Almost nobody needs to roll back; they need the upgrade's aftermath properly finished. Do the steps, measure the difference, and 24H2 becomes what it was supposed to be: a quieter, slightly faster Windows.
