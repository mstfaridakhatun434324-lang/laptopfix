---
title: "Laptop Running Slow in Windows 11 24H2? The Complete Speed-Up"
slug: how-to-fix-laptop-running-slow-in-windows-11-24h2
date: 2026-09-03
categories: ["performance"]
tags: ["windows 11 24h2 slow", "laptop slow fix", "speed up windows 11", "24h2 performance"]
description: "Laptop sluggish after moving to Windows 11 24H2? Speed it up with this complete checklist: startup trims, debloating, driver updates, and 24H2-specific fixes."
thumbnail: "/images/thumbs/how-to-fix-laptop-running-slow-in-windows-11-24h2.webp"
faqs:
  - q: "Is Windows 11 24H2 slower than 23H2?"
    a: "For most users, no — benchmarks show comparable performance. But 24H2 changed enough under the hood (new scheduler behaviors, Copilot+ features, updated drivers) that some systems regress, especially right after the upgrade while indexing, updates, and driver migrations settle. Give a fresh 24H2 install a few days before judging; persistent slowness after a week is fixable, not inherent."
  - q: "Should I clean-install 24H2 instead of upgrading?"
    a: "If the upgrade left your laptop slow and the checklist doesn't fix it, yes — clean installs consistently outperform in-place upgrades because they shed years of accumulated cruft, broken services, and driver remnants. Back up, install from the official ISO, install drivers from your manufacturer, and reinstall apps fresh. It's a few hours of work for a like-new system."
  - q: "What 24H2-specific features can I disable for speed?"
    a: "The safe trims: Copilot/Recall features if you don't use them (and your hardware even supports them), Widgets, Teams Chat integration, transparency and animation effects, and optional features like Windows Copilot runtime. Also review the new Energy saver aggressive settings, which can throttle performance-minded users. None of these affect core OS stability when disabled."
  - q: "How long should I wait after upgrading before troubleshooting?"
    a: "Give it 3-5 days of normal use with the laptop plugged in and connected. Post-upgrade, Windows re-indexes search, Defender runs full scans, updates download, and drivers migrate — all heavy background work that settles on its own. Troubleshooting on day one means fighting temporary load. If it's still slow after a week, work the checklist — that's real, fixable slowness."
---

Windows 11 24H2 promised refinement; your laptop delivered molasses. Whether the slowness arrived with the upgrade or crept in after, 24H2-era slow laptops share a common set of causes — and a common fix order. This is the complete checklist: the highest-yield speed-ups first, the deeper 24H2-specific tweaks after, in the sequence that gets most laptops feeling fast again within an hour.

Two ground rules: let a fresh upgrade settle for a few days before judging it, and measure before and after (boot time, app launch time) so you know what worked. This guide assumes 24H2 is installed and settled — if you just upgraded yesterday, bookmark this and come back next week. For the narrower high-CPU slice, [fixing high CPU usage](/articles/how-to-fix-high-cpu-usage-on-windows-11/) zooms in; for disk-space pressure, [freeing up disk space](/articles/how-to-free-up-disk-space-on-windows-11/) pairs well.

Work top to bottom. Most laptops are transformed by the first four fixes.

## Why this happens

- **Post-upgrade background settling**: Indexing, Defender scans, and update downloads after the 24H2 upgrade consume resources for days.
- **Startup program accumulation**: Years of installs mean dozens of auto-start apps — the perennial number-one slowdown.
- **Bloatware and preinstalled apps**: Factory images and 24H2's own bundled apps run background tasks you never asked for.
- **Outdated drivers post-upgrade**: The upgrade can leave mismatched or generic drivers, especially for storage and GPU.
- **24H2 features you don't use**: Copilot runtime, Widgets, Recall, and Teams integration consume resources for zero benefit if unused.
- **Power settings throttling**: Energy saver aggressiveness or a stuck power plan caps the performance you paid for.
- **Full or fragmented storage**: SSDs above 85% full slow down; HDDs fragment — both punish a fresh OS.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Trim startup programs

The universal number-one speed-up — fewer residents, faster everything.

1. Open Task Manager, Startup apps, sort by Startup impact.
2. Disable everything High/Medium impact you don't need at login — full method in [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).
3. Restart and feel the difference in login-to-usable time.
4. Revisit quarterly; startup creep is relentless.

### Fix 2: Debloat 24H2's extras

Remove the background cost of features you never touch.

1. Uninstall preinstalled apps you don't use: Settings, Apps, Installed apps, sort by name and remove trials and duplicates.
2. Disable Widgets, Chat, and Copilot/taskbar extras in Taskbar settings.
3. Turn off transparency and animations (Settings, Accessibility, Visual effects) for a snappier feel.
4. In Optional features, remove anything irrelevant (like legacy media features you never use).

### Fix 3: Update everything: Windows, drivers, BIOS

Post-upgrade mismatches are a real 24H2 slowdown source.

1. Install all Windows updates — 24H2's early cumulative updates fixed performance regressions.
2. Update GPU drivers from the manufacturer ([NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx) for NVIDIA, Intel's driver tool or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) for others).
3. Update chipset and storage drivers from your laptop maker's support page.
4. Check for a BIOS update too — 24H2-era firmware fixes are common.

### Fix 4: Set the right power mode

Make sure 24H2 isn't throttling you to save watts you don't need to save.

1. Set Power mode to Best performance (plugged in) or Balanced.
2. Check Energy saver isn't stuck on — it throttles aggressively.
3. In your manufacturer's app, select a performance profile over silent/eco.
4. Verify CPU boosts under load with Task Manager's CPU speed readout.

### Fix 5: Free disk space and check drive health

A full drive punishes every OS, and 24H2 needs room for updates.

1. Get C: below 75% full via Disk Cleanup (system files) and uninstalling bulk.
2. Check SSD health with CrystalDiskInfo if the drive is old.
3. On remaining HDDs, run Optimize (defrag) from the drive's Properties, Tools.
4. See [Microsoft's storage documentation](https://support.microsoft.com/en-us/windows) for the built-in tools.

### Fix 6: Tame background services

Quiet the background so the foreground gets the resources.

1. Let search indexing finish its post-upgrade build instead of fighting it.
2. Pause OneDrive sync during work hours if it's churning — or trim its sync set.
3. Set active hours so Windows Update doesn't ambush you.
4. Check Task Manager for any single process hogging CPU/disk at idle and address it.

### Fix 7: Reset or clean-install as the final option

When the checklist isn't enough, start fresh — it works.

1. First try Settings, System, Recovery, Reset this PC (keep files) — fixes deep OS issues.
2. If still slow, do a true clean install from the ISO at [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Install drivers from your manufacturer before anything else, then apps one by one.
4. A clean 24H2 on healthy hardware is fast — if it isn't, suspect the hardware.

### Fix 8: Scan for malware and audit Task Scheduler

Two hidden slowdowns that checklists miss: malware masquerading as system load, and third-party scheduled tasks firing constantly.

1. Run a full scan with Windows Security (Virus & threat protection, Scan options, Full scan) — do it overnight if needed.
2. Follow with a second-opinion scan using the free Microsoft Safety Scanner for anything Defender missed.
3. Open Task Scheduler and browse the Task Scheduler Library for third-party tasks set to run frequently (every few minutes).
4. Disable telemetry, 'optimization,' and updater tasks from software you barely use — each firing task costs CPU.
5. Check Task Manager's Startup tab once more for anything that crept back after updates.
6. A clean bill of health here means your slowness is configuration, not infection or background churn — and the checklist above addresses configuration completely.

## Closing

A slow laptop on Windows 11 24H2 is fixable far more often than it's inherent — startup trims, debloating, current drivers, and correct power settings restore speed on the vast majority of machines. Give fresh upgrades a week to settle, then work the checklist top to bottom. And if an upgrade left things tangled beyond repair, a clean install is the reset button that actually works: a few hours of effort for a laptop that feels new.
