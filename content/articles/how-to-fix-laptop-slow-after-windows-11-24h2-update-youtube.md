---
title: "Fix a Laptop Slowing Down After the Windows 11 24H2 Update"
slug: how-to-fix-laptop-slow-after-windows-11-24h2-update-youtube
date: 2026-09-27
categories: ["performance"]
tags: ["windows 11 24h2", "laptop slow after update", "24h2 performance", "windows update", "fix slow laptop"]
description: "Laptop sluggish after the Windows 11 24H2 update? Diagnose post-update slowdowns and restore speed with this technician-tested sequence."
thumbnail: "/images/thumbs/how-to-fix-laptop-slow-after-windows-11-24h2-update-youtube.webp"
faqs:
  - q: "Why is my laptop slow after installing the Windows 11 24H2 update?"
    a: "The 24H2 update rebuilds the search index, re-runs driver installations, resets some power and graphics settings, and triggers background optimization tasks. These settle within a day or two. If slowness persists beyond 48 hours, the usual culprits are outdated drivers conflicting with 24H2, corrupted update components, or power plans reset to balanced instead of best performance."
  - q: "Should I roll back the 24H2 update to fix the slowness?"
    a: "Rollback is a last resort, available for ten days after installing the update. It fixes the speed problem but returns you to an older, less-supported Windows build with known security gaps. In most cases the performance fixes in this guide restore full speed while keeping 24H2's improvements and security updates. Only roll back if the laptop is unusable and every fix fails."
  - q: "How long should I wait before troubleshooting post-update slowness?"
    a: "Give the laptop 24 to 48 hours of normal plugged-in use first. During this window Windows finishes indexing, optimizes the drive, and completes background update tasks that legitimately consume CPU and disk. If the machine is still sluggish after two days of regular use, the slowdown is no longer 'settling in' — start the diagnostic steps in this guide."
  - q: "Can the 24H2 update damage my hardware or SSD?"
    a: "No. The 24H2 update cannot physically damage hardware. What it can do is install a problematic storage or chipset driver that makes the drive run slowly, which feels like hardware trouble but is purely software. Updating to the latest manufacturer drivers almost always resolves it. If drive health tools report actual errors, that indicates a pre-existing hardware issue the update merely exposed."
---

The pattern is depressingly familiar: your laptop ran fine, Windows installed the big 24H2 feature update overnight, and now everything feels like it's moving through syrup. Boot takes twice as long, apps hesitate, and the fans seem busier than before. You're not imagining it, and you're not alone — post-feature-update slowdowns are one of the most reported Windows 11 issues in repair shops.

Here's the reassuring part: in the large majority of cases, nothing is broken. The update kicks off a storm of background work — reindexing, driver reinstallation, optimization passes — that settles on its own. And when it doesn't settle, the causes are a short, known list: driver conflicts, reset settings, or corrupted update components. This guide tells you how to tell the difference and fix each one, in the order a technician would.

## Why this happens

- **Post-update background tasks:** After 24H2, Windows rebuilds the search index, re-optimizes the drive, and completes deferred update work. This legitimately consumes CPU and disk for 24–48 hours.
- **Driver conflicts:** The update may install generic drivers over manufacturer-tuned ones — especially storage, chipset, and graphics drivers — silently reducing performance.
- **Reset power plans:** Feature updates sometimes reset custom power plans or revert the system to Balanced, capping CPU boost behavior you were relying on.
- **Corrupted update components:** A partially failed update can leave the servicing stack retrying operations endlessly, burning CPU in the background.
- **Re-enabled startup items:** Updates occasionally re-enable startup programs you'd previously disabled, restoring the congestion you'd cleaned up.
- **Old drivers incompatible with 24H2:** 24H2 changed some driver model behaviors. Drivers written for older builds can cause stuttering, high DPC latency, or excessive CPU usage.
- **Disk nearly full after the update:** Feature updates need 20GB+ of working space and leave a Windows.old folder behind. A drive that was already tight can cross into the slow zone.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it 48 hours (and verify it's actually settling)

Before touching anything, confirm whether the laptop is still doing legitimate post-update work or genuinely stuck. Open **Settings → Windows Update** and check for pending items. Open Task Manager and look at what's actually consuming resources — if it's SearchIndexer, TiWorker, or the .NET optimization service, that's the settling-in storm. Note the trend over a day: decreasing background activity means it's resolving itself.

1. Open **Settings → Windows Update** and install anything pending.
2. In Task Manager, identify the top CPU/disk consumers over several checks.
3. If they're Windows servicing processes (TiWorker.exe, SearchIndexer.exe, ngen), allow up to 48 hours of plugged-in use.
4. If usage doesn't trend downward after two days, continue to Fix 2.

### Fix 2: Check and restore your power plan

The 24H2 update is notorious for resetting power settings. A laptop silently switched from Best Performance to Balanced (or worse, Power Saver) will feel dramatically slower — lower boost clocks, aggressive throttling — with no other symptom. This two-minute check resolves a surprising share of "slow after update" reports.

1. Open **Settings → System → Power & battery**.
2. Set **Power mode** to **Best performance** while plugged in.
3. If you use a custom plan, open **Control Panel → Power Options** and verify it's still selected.
4. For the full walkthrough of performance power settings, see [changing to best performance](/articles/how-to-change-power-plan-to-best-performance-in-windows-11-24h2/).

### Fix 3: Update drivers from the manufacturer (not just Windows Update)

Windows Update's drivers are generic. Your laptop maker's versions are tuned for your exact hardware. After 24H2, the storage and chipset drivers deserve priority — they're the most common source of post-update disk slowness. Get them from Dell, HP, Lenovo, ASUS, or Acer support for your exact model.

1. Visit your manufacturer's support site and enter your model or serial number.
2. Download and install the latest **chipset** and **storage (Intel RST / AMD)** drivers for Windows 11 24H2.
3. Update the **graphics driver** too — from Intel, NVIDIA, or AMD directly if the maker lags behind.
4. Restart and compare responsiveness.

### Fix 4: Re-disable startup items the update re-enabled

Feature updates have a habit of resurrecting startup entries you'd killed. Open Task Manager's **Startup apps** tab and look for familiar faces that are enabled again — updaters, chat clients, vendor utilities. Disable the non-essentials once more.

1. Open Task Manager → **Startup apps**.
2. Sort by status and review everything Enabled.
3. Disable items you had previously turned off or don't need at boot.
4. Restart and observe.

### Fix 5: Repair Windows Update components

If Task Manager shows TiWorker.exe or the Windows Modules Installer burning CPU days after the update, the servicing stack may be stuck retrying a failed operation. The fix is a controlled reset of the update components plus a system file repair.

1. Open **Command Prompt as administrator**.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run the **Windows Update troubleshooter**: Settings → System → Troubleshoot → Other troubleshooters.
4. Check for updates again and install whatever appears. Microsoft's update guidance lives at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 6: Clean up post-update disk usage

The Windows.old folder and update working files can consume 20–30GB. On a drive that was already tight, that's enough to push an SSD into its slow zone. Disk Cleanup's system-files mode removes them safely.

1. Search for **Disk Cleanup**, run it, then click **Clean up system files**.
2. Check **Previous Windows installation(s)** and **Temporary Windows installation files**.
3. Click OK and let it finish (it takes a while).
4. Verify C: has at least 15–20% free space afterward.

### Fix 7: Consider rollback only as a last resort

If the laptop is still unusable after all of the above — and you've genuinely given each fix a chance — the 10-day rollback window lets you return to the previous build. Go to **Settings → System → Recovery → Go back**. You'll keep your files but lose the update. Treat this as a last resort, not a first step: most 24H2 slowness is fixable driver or settings trouble, and the [step-by-step 24H2 slowdown guide](/articles/how-to-fix-laptop-slow-after-windows-11-24h2-update-step-by-step/) covers additional angles like clean-boot diagnosis before you give up on the new build.

1. Open **Settings → System → Recovery**.
2. If **Go back** is available (within 10 days of the update), click it and follow the prompts.
3. Back up important files first — rollbacks are reliable but not risk-free.
4. After rolling back, pause feature updates temporarily while you research the conflict.

## Closing

A slow laptop after the 24H2 update is frustrating, but it's a known quantity: background settling, driver regressions, reset power plans, or stuck update components. Give it 48 hours, restore your power plan, update manufacturer drivers, and clean up the leftovers — in that order. The overwhelming majority of post-24H2 slowdowns yield to this sequence without ever needing a rollback.
