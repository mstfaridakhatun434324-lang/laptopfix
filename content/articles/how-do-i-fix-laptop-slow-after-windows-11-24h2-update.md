---
title: "Laptop Slow After the Windows 11 24H2 Update? Fix It Now"
slug: how-do-i-fix-laptop-slow-after-windows-11-24h2-update
date: 2026-10-01
categories: ["performance"]
tags: ["24h2 slow", "windows 11 update", "laptop slow", "performance fix", "troubleshooting"]
description: "Your laptop got sluggish right after the Windows 11 24H2 update? Work through the real causes — background migration, drivers, and settings — and restore speed."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-slow-after-windows-11-24h2-update.webp"
faqs:
  - q: "How long does Windows 11 24H2 take to settle after updating?"
    a: "Give it 48 to 72 hours of normal use with the laptop plugged in. During this window Windows re-indexes search, Defender re-baselines with full scans, the .NET framework re-optimizes, and drivers settle. Judging performance in the first two days leads to fixing problems that would have resolved themselves — but slowness persisting past day three is real and needs attention."
  - q: "Should I roll back the 24H2 update if my laptop is slow?"
    a: "Only as a last resort after trying the targeted fixes. Rollback is available for ten days via Settings > System > Recovery > Go back, and it restores your previous build cleanly. But most 24H2 slowness comes from fixable causes — outdated drivers, background tasks, re-enabled settings — and rolling back just postpones the update while losing its security improvements."
  - q: "Why does 24H2 feel slower on older laptops?"
    a: "Feature updates raise the baseline: new background services, re-enabled visual effects, reset power plans, and heavier default apps. On 8GB RAM machines or older dual-core processors the difference is noticeable. The fixes that matter most are updating drivers (especially chipset and storage), trimming startup apps, and switching the power plan back to Best performance."
  - q: "Can a clean install of 24H2 fix the slowness?"
    a: "Usually yes — a clean install removes years of accumulated cruft, broken drivers, and conflicting software that feature updates carry forward. It is the most reliable fix for persistent post-update slowness, but it is also the most work: back up everything, reinstall apps, and reconfigure settings. Try the in-place repair install first; it refreshes Windows while keeping your files and programs."
---

The 24H2 update finished, the laptop rebooted, and... everything feels heavier. Apps take longer to open, the fans run more, battery drains faster, and the whole machine has a sluggishness it didn't have last week. You're not imagining it — feature updates genuinely disturb a working system, and 24H2 is a big one.

But here's the technician's perspective: most post-24H2 slowness is temporary background work plus a handful of settings the update reset. Work through this guide in order — diagnose what's actually slow, let the settling finish, fix what the update broke — and only then consider drastic measures. For boot-specific slowness, our [slow boot on SSD guide](/articles/how-to-fix-windows-11-boot-time-slow-ssd-step-by-step/) pairs well with this.

## Why this happens

- **Post-update background storm**: Search re-indexing, Defender re-baselining, and .NET optimization all run hard for 2–3 days after the update.
- **Outdated drivers**: Old chipset, storage, and graphics drivers from the previous build misbehave under 24H2's changed kernel.
- **Reset power plan**: The update often flips laptops back to Balanced (or even Power saver), throttling the CPU.
- **Re-enabled visual effects and features**: Transparency, animations, and widgets the user had disabled come back on.
- **Startup bloat re-enabled**: Disabled startup entries and services sometimes get re-enabled by the feature update.
- **OneDrive / cloud re-sync**: The update can trigger a full re-scan of synced folders.
- **Leftover update debris**: The Windows.old folder and temporary update files consume tens of GB, pressuring low disk space.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the settling period finish (but verify it's actually settling)

Don't fix what time fixes — but confirm time is actually fixing it.

1. Check how long ago 24H2 installed: **Settings** > **Windows Update** > **Update history** — note the feature update date.
2. If it's been under 3 days, plug the laptop in overnight and leave it on (not sleeping) — background tasks need idle power-on time, and sleep pauses them.
3. Open Task Manager > **Processes** and sort by CPU and Disk — legitimate settling shows `SearchIndexer.exe`, `MsMpEng.exe`, `TiWorker.exe`, or `.NET` optimization processes busy. These should trend downward day by day.
4. After 72 hours, those processes should be quiet at idle. If the same ones are still hammering the system on day four, it's not settling anymore — continue with the fixes below.
5. Track it: note idle CPU % in Task Manager each morning. A settling system shows a clear downward trend; a stuck one doesn't.

### Fix 2: Update drivers — chipset and storage first

The single highest-impact post-24H2 fix on most laptops.

1. Start with the chipset and storage drivers from your laptop maker's support site — not Windows Update. For Dell use [Dell Support](https://www.dell.com/support), for HP [HP Support](https://support.hp.com/us-en), for Lenovo [Lenovo Support](https://support.lenovo.com/us/en/).
2. Enter your exact model, download the latest chipset, Intel RST/storage, and BIOS/firmware drivers marked 24H2-compatible, and install them.
3. Update graphics: Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA from [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), AMD from [AMD drivers](https://www.amd.com/en/support/download/drivers.html).
4. In **Device Manager**, check for any yellow warning icons — resolve every one; a device with a broken driver can stall the whole I/O subsystem.
5. Reboot after driver installs and re-test. On many "24H2 made my laptop slow" machines, the chipset driver alone restores most of the lost responsiveness.

### Fix 3: Restore your power plan and performance settings

24H2 loves resetting these to defaults.

1. Open **Settings** > **System** > **Power & battery** > **Power mode** — set it to **Best performance** while plugged in.
2. Open the classic Power Options (`powercfg.cpl`) and verify your active plan; recreate custom plans if the update wiped them.
3. Check **Settings** > **System** > **Display** > **Graphics** > **Default graphics settings** — re-enable **Hardware-accelerated GPU scheduling** if you had it on.
4. Turn off the visual effects you had disabled: **Settings** > **Accessibility** > **Visual effects** — toggle off **Transparency effects** and **Animation effects** for a snappier feel on weaker hardware.
5. Disable Widgets and other re-enabled extras: right-click the taskbar > **Taskbar settings** — turn off Widgets, Copilot, and Search highlights if you don't use them.

### Fix 4: Re-trim startup apps and background services

The update re-enables things you had carefully disabled.

1. Open Task Manager > **Startup apps** — compare against your memory; re-disable anything the update turned back on (manufacturer utilities, updaters, chat clients).
2. Check **Settings** > **Apps** > **Installed apps** for new additions the update may have installed (trial apps, "recommended" software) — uninstall what you don't want.
3. Review **Settings** > **Privacy & security** > **Background apps** permissions — revoke background access for apps that don't need it.
4. Run a [clean boot](/articles/how-to-perform-clean-boot-windows-11-on-laptop/) to test: if the laptop is fast in clean boot, a third-party startup item is the drag — re-enable items in halves to find it.
5. Don't forget scheduled tasks: open **Task Scheduler** and check for manufacturer tasks (telemetry, "experience improvement") that the update re-armed.

### Fix 5: Clean up update debris and free disk space

Low free space after a feature update silently throttles everything.

1. Open **Settings** > **System** > **Storage** > **Temporary files** — check **Previous Windows installation(s)** (Windows.old, often 15–30 GB), **Delivery Optimization Files**, and **Temporary Windows installation files**, then **Remove files**.
2. Only delete Windows.old after you're sure you won't roll back (10-day window) — it's your rollback path.
3. Aim for at least 15–20% free space on C:. Below 10%, Windows can't page, update, or index properly and everything slows.
4. Run **Disk Cleanup** > **Clean up system files** for the deeper categories (Windows Update Cleanup, Device driver packages).
5. Our [free up disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/) covers the bigger wins if you're still tight after cleanup.

### Fix 6: Repair system files and finish pending updates

A ragged update leaves the system in a half-migrated state.

1. In an elevated terminal, run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. Open **Settings** > **Windows Update** and install everything pending — Microsoft ships 24H2 performance fixes as cumulative updates, and being behind means missing them.
3. Check **Optional updates** > **Driver updates** too — install relevant ones, especially storage and chipset.
4. If Windows Update itself is stuck, run the Windows Update troubleshooter (**Settings** > **System** > **Troubleshoot** > **Other troubleshooters**).
5. After repairs and updates, reboot and give the system one more idle night — repaired components often trigger one final round of background optimization.

### Fix 7: The escalation ladder — repair install, rollback, clean install

When targeted fixes don't restore speed.

1. **In-place repair install**: download 24H2 media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), run setup from within Windows, choose **Keep personal files and apps**. This refreshes every system component — fixes most stubborn post-update issues.
2. **Rollback** (within 10 days): **Settings** > **System** > **Recovery** > **Go back**. Clean and quick, but you lose 24H2's security updates and will face the update again later.
3. **Clean install**: the definitive fix. Back up everything, create USB media, wipe and install. Only for machines where the repair install didn't help — usually indicates years of accumulated cruft, not a 24H2-specific problem.
4. Before any escalation, check one thing: **Task Manager** > **Performance** — is RAM constantly above 85%? If 24H2 pushed an 8GB machine over the edge, no software fix fully compensates; a RAM upgrade (if the laptop allows) is the real answer.
5. Document what you tried — if you end up on support forums or with the manufacturer, "I updated chipset drivers, trimmed startup, ran DISM/SFC, and did a repair install" gets you past tier-one scripts instantly.

## Closing

Post-24H2 slowness is usually a mix of temporary background work and reset settings, not a broken update. Give it three days, update your chipset and storage drivers, restore your power plan, re-trim startup — and most laptops come back faster than before. Save the rollback and reinstall options for when the evidence says the update truly damaged something, not for day-one impatience.
