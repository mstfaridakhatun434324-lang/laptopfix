---
title: "Windows 11 Slow After 24H2 Update? Complete Step-by-Step Recovery"
slug: "how-to-fix-windows-11-slow-after-24h2-update-step-by-step"
date: "2026-10-07"
categories: ["performance"]
tags: ["windows 11 24h2", "slow after update", "performance fix", "step by step", "system restore"]
description: "A complete ordered walkthrough for fixing Windows 11 slowness after the 24H2 update — from quick checks to driver repairs to rollback, each step building on the last."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-after-24h2-update-step-by-step.webp"
faqs:
- q: "What is the first thing to do when Windows 11 is slow after 24H2?"
  a: "First, confirm the slowdown is real and not just post-update settling: use the laptop normally for 48–72 hours plugged in, since Windows re-indexes files and rebuilds caches after a feature update. If it is still slow, update chipset, storage, and graphics drivers — outdated drivers are the number one cause of persistent 24H2 slowness."
- q: "Will resetting Windows fix 24H2 slowness?"
  a: "A reset usually fixes it because it gives you a clean 24H2 install with fresh drivers and no leftover conflicts, but it is a heavy hammer — you will reinstall apps and reconfigure settings. Try driver updates, SFC/DISM repairs, and update-component resets first. Use 'Keep my files' reset only when those fail, and back up everything beforehand regardless."
- q: "How do I know if a driver is causing 24H2 slowness?"
  a: "Check Device Manager for warning icons, look at Task Manager for processes with constant high disk or CPU (especially storage-related services), and compare performance in Safe Mode — if the system is fast in Safe Mode, a third-party driver is almost certainly the cause. Updating the chipset and storage drivers first resolves most cases."
- q: "Is it safe to pause Windows updates after fixing 24H2 slowness?"
  a: "Pausing updates for a few weeks while you stabilize drivers is reasonable and safe. Pausing them indefinitely is not — you would miss security patches. A better long-term approach is to keep quality updates on but defer feature updates, giving manufacturers time to release compatible drivers before the next big update lands."
---

This is the master sequence. If your Windows 11 laptop slowed down after the 24H2 update and you want one guide that starts at "is this even a real problem" and ends at "here's the nuclear option," this is it. Every step is ordered deliberately: cheap and safe first, invasive last. Don't skip ahead — each step either fixes it or gives the next step a clean foundation.

I've structured this so you can stop the moment things improve. Most people won't need the later steps. But if you're one of the unlucky few with a genuinely stubborn case, the full sequence will get you there.

## Why this happens

- **Driver incompatibility** — 24H2 changed storage, memory, and graphics subsystems; old drivers interact badly with the new code.
- **Post-update background processing** — indexing, optimization, and migration tasks consume resources for days.
- **Corrupted servicing stack** — the update process itself can leave Windows' component store damaged.
- **Stuck update services** — Windows Update or Modules Installer looping forever in the background.
- **Reset power and performance settings** — the update reverts tuned configurations to defaults.
- **Third-party software conflicts** — antivirus, system utilities, and old drivers hooking into changed Windows internals.
- **Failed or partial update** — the system reports success but key components didn't apply cleanly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out normal post-update settling

Before touching anything, verify you're dealing with a real problem and not background migration work.

Steps:

1. Check when 24H2 installed: Settings → Windows Update → Update history.
2. If it's been less than 72 hours, use the laptop normally (plugged in) and monitor Task Manager → Performance.
3. Declining disk/CPU activity over days means it's settling — let it finish.
4. If it's been over 72 hours with no improvement, continue to Fix 2.
5. Either way, install any pending Windows updates now — Microsoft ships 24H2 performance fixes regularly. Check the [Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update seems stuck.

### Fix 2: Update chipset, storage, and graphics drivers

The single most effective step. Do this before anything else that modifies the system.

Steps:

1. Identify your hardware: run `msinfo32` and note the system manufacturer, model, and processor.
2. Visit your manufacturer's support site (Dell, HP, Lenovo, Acer, ASUS) and download the latest **chipset**, **storage/IRST**, and **graphics** drivers for your exact model.
3. Install chipset first, restart; then storage, restart; then graphics, restart.
4. For Intel graphics/chipset, Intel's Driver & Support Assistant can automate detection; NVIDIA and AMD offer their own official driver download pages — always prefer the manufacturer's site over Windows Update's generic drivers.
5. Test performance after all restarts.

### Fix 3: Repair Windows system files

Fix corruption in the files 24H2 installed or migrated.

Steps:

1. Open an elevated Terminal (right-click Start → Terminal (Admin)).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` first (repairs the component store).
3. When DISM finishes, run `sfc /scannow` (repairs protected system files from the now-healthy store).
4. Restart the laptop.
5. If SFC reported corrupt files it couldn't fix, note the CBS log location it gives you — that's a sign you may need Fix 7.

### Fix 4: Reset Windows Update components

Clear stuck update services that keep churning in the background.

Steps:

1. In elevated Terminal, stop the services:
   `net stop wuauserv` / `net stop bits` / `net stop cryptSvc` / `net stop msiserver`
2. Rename the data folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
3. Restart the services with `net start` for each.
4. Run Windows Update and install everything offered.
5. Restart and monitor Task Manager for an hour — background update activity should settle.

### Fix 5: Check Safe Mode performance

This is the key diagnostic fork: it tells you whether the problem is Windows itself or something loading with it.

Steps:

1. Hold Shift while clicking Restart → Troubleshoot → Advanced options → Startup Settings → Restart → press 4 for Safe Mode.
2. Use the system for 10–15 minutes in Safe Mode — open apps, browse files.
3. If it's fast in Safe Mode: a third-party driver or startup program is the cause. Do a [clean boot](/articles/how-to-perform-clean-boot-windows-11-on-laptop/) to identify it.
4. If it's slow in Safe Mode too: the problem is in Windows core or hardware — continue to Fix 6.
5. Restart normally to exit Safe Mode.

### Fix 6: Restore power plans and disable visual bloat

24H2 resets performance-related settings. Reclaim them.

Steps:

1. Settings → System → Power & battery → set Power mode to **Best performance** while plugged in.
2. Control Panel → Power Options → advanced settings → set Minimum processor state (plugged in) to 80–100%.
3. Search "performance" → "Adjust the appearance and performance of Windows" → select **Adjust for best performance** (or custom with only "Smooth edges" and "Show thumbnails" kept).
4. Disable transparency: Settings → Personalization → Colors → Transparency effects Off.
5. Restart and test.

### Fix 7: Perform an in-place upgrade repair

Reinstalls 24H2 over itself, fixing deep corruption while keeping files and apps. This resolves most stubborn cases.

Steps:

1. Download the Windows 11 Media Creation Tool or ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO (double-click it) and run `setup.exe`.
3. Choose **"Keep personal files and apps"** when prompted.
4. Let the repair install complete — it takes 30–90 minutes with several restarts.
5. Afterward, re-run Windows Update and reinstall manufacturer drivers (Fix 2).

### Fix 8: Roll back or clean install (last resort)

If the in-place repair didn't help, the update and your hardware simply aren't cooperating.

Steps:

1. Within 10 days of the update: Settings → System → Recovery → **Go back**.
2. Beyond 10 days: back up everything, then do a clean install from the Microsoft ISO.
3. After a clean install, install manufacturer drivers *before* connecting to Windows Update, so Windows doesn't install generic ones first.
4. Pause feature updates afterward to control when the next big update arrives.
5. Document which driver versions work — you'll want them if this happens again.

## Closing

This sequence is ordered by effort-to-reward ratio: settling check, drivers, file repair, update reset, Safe Mode diagnosis, settings, repair install, rollback. The vast majority of 24H2 slowdowns resolve by Fix 4. If yours needed the later steps, keep a note of what worked — and consider deferring future feature updates by a month to let driver issues shake out first. For brand-specific 24H2 trouble, our [HP-focused guide](/articles/how-to-fix-windows-11-slow-after-24h2-update-on-hp-laptop/) covers manufacturer quirks in depth.
