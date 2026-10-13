---
title: "Windows 11 Lagging? Fix It Step by Step"
slug: how-to-fix-windows-11-lagging-step-by-step
date: 2026-09-21
categories: ["performance"]
tags: ["windows 11 lagging", "slow windows 11", "step by step", "performance fix", "laptop slow"]
description: "A complete step-by-step sequence to fix Windows 11 lag: trim startup, fix power and thermal issues, update drivers, and repair the system."
thumbnail: "/images/thumbs/how-to-fix-windows-11-lagging-step-by-step.webp"
faqs:
  - q: "Why is my new Windows 11 laptop already lagging?"
    a: "New laptops ship with bloatware — trial antivirus, vendor utilities, and preinstalled apps that all launch at startup and run background services. A fresh machine can have 30 or more startup entries. The fix is a cleanup pass: remove what you don't need, disable unnecessary startup items, and update drivers. The hardware is fine; it's the software load that came in the box."
  - q: "Will adding more RAM fix Windows 11 lag?"
    a: "Only if you're actually running out of memory. Check Task Manager's Performance tab: if committed memory regularly exceeds physical RAM and the disk is thrashing, more RAM helps enormously. But if RAM usage sits at 50 percent while the CPU or disk is maxed, new memory changes nothing. Diagnose first — RAM is the answer only to a memory problem, and Windows 11 runs comfortably on 8 GB for typical use."
  - q: "Does a factory reset fix lag permanently?"
    a: "It fixes software-caused lag completely — you're starting from a clean system. But the lag returns if you reinstall the same bloatware and let the same 40 startup programs accumulate. A reset is also overkill for most cases: the step-by-step fixes in this guide resolve the same problems with far less disruption. Reserve resets for systems with deep corruption or years of accumulated cruft."
  - q: "How do I tell if lag is caused by overheating?"
    a: "Watch for the pattern: the laptop is fast for the first 10-20 minutes after a cold boot, then progressively slows as it warms up, with fans running hard. Confirm with a temperature monitor — sustained CPU temps above 90-95°C under load mean thermal throttling. If performance is bad from the first minute on a cold machine, heat is not your problem; look at startup load and drivers instead."
---

"Lagging" is the vaguest complaint a laptop can have, and the most frustrating to fix by guessing. Input delays, stuttering animations, apps that take forever to respond, a cursor that freezes for a second at a time — these all get called lag, but they have different causes. The only reliable approach is a sequence: measure, eliminate the common causes in order of likelihood, and re-test after each step.

This guide is that sequence. Each step targets one layer — startup load, power settings, thermals, drivers, background services, system corruption — and tells you how to confirm whether that layer was your problem before moving on. Work it top to bottom and stop when the lag is gone.

## Why this happens

- **Startup program pileup:** Dozens of programs launching at boot, each consuming CPU, RAM, and disk I/O for minutes afterward.
- **Wrong power plan:** Battery-saver or balanced throttling on a machine that should be running at full performance.
- **Thermal throttling:** Dust-clogged cooling forcing the CPU to slow itself to avoid overheating.
- **Outdated or broken drivers:** Chipset, storage, and GPU drivers that mishandle power states or interrupts.
- **Background service churn:** Windows Update, search indexing, OneDrive sync, and antivirus scans all competing for resources.
- **RAM exhaustion:** Too many browser tabs and apps for the installed memory, forcing constant paging to disk.
- **Failing storage:** A dying drive whose retry loops stall the entire system intermittently.
- **Post-update turbulence:** A recent Windows update re-indexing, re-optimizing, or carrying an incompatible driver.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure the lag properly

Open Task Manager (Ctrl+Shift+Esc), go to the Performance tab, and watch CPU, memory, disk, and GPU during the lag. Sort the Processes tab by CPU and disk to catch the offender in the act. Note the pattern: constant high CPU means a runaway process; disk pinned at 100% means storage contention (see the [disk active time guide](/articles/what-to-do-if-disk-active-time-100-percent/)); lag only after warming up means thermals. Five minutes of observation beats an hour of guessing.

1. Open Task Manager → Performance tab during the lag.
2. Sort Processes by CPU, then by Disk, and identify top consumers.
3. Note whether lag is constant, periodic, or heat-related.
4. Write down the findings — they guide every step below.

### Fix 2: Cut the startup load

In Task Manager → **Startup apps**, disable everything you don't need in the first minute after boot — updaters, chat apps, cloud storage, game launchers. Then open **Settings → Apps → Installed apps** and uninstall bloatware you never use. Restart and time the boot. A machine that went from 40 startup entries to 8 feels like a different computer. Keep security software and hardware utilities enabled; disable the rest.

1. Open Task Manager → **Startup apps**.
2. Disable every non-essential entry (right-click → Disable).
3. Uninstall unused bloatware in **Settings → Apps → Installed apps**.
4. Restart and compare responsiveness in the first five minutes.

### Fix 3: Set the right power mode

Click the battery icon (or go to **Settings → System → Power & battery → Power mode**) and set it to **Best performance** while plugged in. In the classic Power Options, make sure you're on Balanced or High performance — not Power saver. Laptops on power-saver plans cap CPU frequency aggressively, and the "lag" is literally the processor being told not to run fast. This is the most embarrassing common cause: a one-click fix people overlook for months.

1. Set **Power mode** to **Best performance** while plugged in.
2. Check classic Power Options — avoid the Power saver plan.
3. Test the same laggy tasks again.
4. If fixed, create the habit: Best performance on AC, balanced on battery.

### Fix 4: Check thermals and cooling

Install a temperature monitor (HWiNFO or Core Temp) and watch CPU temps under load. Sustained readings above 90°C with heavy fan noise mean thermal throttling. The fix ladder: clean the vents with compressed air, elevate the laptop for airflow, check that fans actually spin, and for older machines consider repasting — or a repair shop if you're not comfortable opening it. If your [fan is screaming at idle](/articles/how-to-fix-laptop-fan-loud-idle-windows-11/), that's the same cooling system telling you something, and that guide goes deeper.

1. Install HWiNFO or Core Temp and monitor CPU temperature under load.
2. Blow out vents and fan intakes with compressed air.
3. Elevate the rear of the laptop for better airflow; test on a hard surface.
4. If temps stay above 90°C under moderate load, get the cooling serviced.

### Fix 5: Update drivers from the right sources

Update the chipset driver, storage (NVMe/SATA) driver, and GPU driver from your laptop maker's support page — Dell, HP, or Lenovo — or the component vendor for GPUs ([NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, [Intel](https://www.intel.com/content/www/us/en/support/detect.html)). Windows Update's generic drivers are a common source of power-state bugs that manifest as micro-stutters. Do the chipset first; it's the driver most responsible for how the CPU, storage, and USB subsystems behave.

1. Download the latest chipset driver from your laptop maker's support site.
2. Update the GPU driver from the GPU vendor with a clean install.
3. Update the storage controller driver if a newer one is offered.
4. Restart and re-test the exact scenarios that lagged before.

### Fix 6: Calm the background services

Pause the usual suspects one at a time and re-test: pause Windows Update (Settings → Windows Update → Pause), pause OneDrive sync for a few hours, and check whether a Defender full scan is running (Windows Security). If pausing one of them fixes the lag, you've found a contributor — schedule it for idle hours rather than disabling it permanently. Background churn is often the difference between a machine that lags "sometimes" and one that's fine. The [slow-after-update guide](/articles/what-to-do-if-windows-11-slow-after-update/) covers the case where this all started right after a patch.

1. Pause Windows Update for 7 days as a test.
2. Pause OneDrive syncing for 2 hours as a test.
3. Check Windows Security for an active full scan.
4. Whichever pause fixed it: reschedule that task for idle hours.

### Fix 7: Repair system corruption

In an elevated Command Prompt, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then check Windows Update for anything pending. Corrupted system files cause exactly the kind of intermittent hangs people describe as lag — the system retries failed operations with timeouts. This is the last software step before considering hardware: if SFC finds and repairs corruption, re-test thoroughly; if the lag survives a clean system, suspect the drive or RAM and test those next.

1. Run `sfc /scannow` in an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Install all pending Windows Updates and restart.
4. If lag persists on a clean system, test the drive (chkdsk/SMART) and RAM (Windows Memory Diagnostic).

## Closing

Lag yields to method, not to random tweaks. Measure first, then cut startup bloat, fix the power plan, check thermals, update the right drivers, calm background services, and repair the system — testing after each. Somewhere in that sequence your lag lives. And once you know which layer it was, you'll spot it in seconds the next time it appears, because it always appears in the same costume.
