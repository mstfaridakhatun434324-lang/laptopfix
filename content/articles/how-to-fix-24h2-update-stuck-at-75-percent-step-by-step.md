---
title: "24H2 Update Stuck at 75%? Step-by-Step Recovery Guide"
slug: how-to-fix-24h2-update-stuck-at-75-percent-step-by-step
date: 2026-10-09
categories: ["windows-update"]
tags: ["windows 11", "24h2", "stuck update", "step by step"]
description: "Windows 11 24H2 frozen at 75%? A precise step-by-step recovery: confirm the stall, clear the blockage, and get the update moving again."
thumbnail: "/images/thumbs/how-to-fix-24h2-update-stuck-at-75-percent-step-by-step.webp"
faqs:
  - q: "What is happening at 75% of the 24H2 update?"
    a: "The installer is in its driver migration and feature staging phase — moving every device driver to the new build, staging the new system files, and verifying the result. It is the most disk-intensive and least parallelizable part of the update, which is why progress reporting goes quiet. On healthy hardware it takes 30 to 90 minutes; beyond several hours with no disk activity, it is genuinely stuck."
  - q: "Is it safe to force-restart at 75%?"
    a: "A normal restart through the Start menu after ending the installer processes is reasonably safe — Windows rolls back to the pre-update state. What you must avoid is a hard power-off mid-write, which can corrupt the staging area or, in rare cases, the boot configuration. Always prefer the graceful path: end processes, then restart normally."
  - q: "Why does 24H2 always stall at exactly 75%?"
    a: "It does not always — but 75% is where the migration phase's slow serial work concentrates, so stalls cluster there visibly. The percentage is also coarse: the installer reports 75% through a wide range of sub-tasks, making a long sub-task look like a freeze at a single number. The underlying causes are the usual suspects: hung drivers, slow disks, and corrupted staging files."
  - q: "How do I prevent the 75% stall on the next attempt?"
    a: "Prepare before retrying: update all drivers from the manufacturer, disconnect USB devices, run from a clean boot, ensure 25 GB free disk space, and temporarily disable real-time antivirus scanning during the install. Each removes one stall vector. The single highest-yield preparation is fresh chipset and storage drivers, since migration hangs most often involve those two."
---

Seventy-five percent is a cruel place to stall: close enough to feel nearly done, far enough that the remaining work is the hardest part. At 75%, the 24H2 update is typically deep in the driver migration and feature staging phase — the most disk-intensive, least communicative stretch of the whole process.

This guide is a strict sequence, not a menu. Each step has a verification checkpoint, and you advance only when the checkpoint passes. That discipline matters at 75% because the wrong intervention — a forced reboot at the wrong moment — can turn a stalled update into a corrupted one. Follow the steps; skip none.

The step-by-step format here is deliberate: at 75%, the cost of a wrong move is a corrupted installation, so improvisation is the enemy. Each step below ends with a checkpoint telling you whether to advance or stop. Readers who skip ahead tend to become the authors of the horror stories — follow the sequence, respect the checkpoints, and the update completes.

## Why this happens

- **Driver migration bottleneck:** Around 75%, the installer migrates drivers to the new build — slow, serial work that reports little progress on older hardware.
- **Disk throughput ceiling:** The staging phase hammers the disk with writes. Slow or nearly full drives stretch this phase into hours of apparent stillness.
- **Hung driver migration:** One incompatible driver can hang its migration thread, freezing real progress while the percentage sits unchanged.
- **Antivirus scanning storm:** Real-time protection scanning every staged file multiplies the phase's duration on systems with heavy security suites.
- **Corrupted staging files:** Damaged files in the staging area cause the installer to retry verification loops that never complete.
- **External device deadlock:** A USB device whose driver cannot migrate can deadlock the entire migration phase.
- **Insufficient memory:** Low-RAM systems page heavily during staging, turning the phase into a swap-bound crawl that looks frozen.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Step 1 — Confirm the stall with Task Manager

Do not act on a number alone. Open Task Manager and watch the installer's disk and CPU activity for fifteen minutes. Sustained activity means the 75% phase is working through its slow stretch — the correct action is patience, not intervention. Advance to step 2 only if activity is flat zero for a full hour. Stalls at the restart screen rather than mid-install are the [update stuck on restarting](/articles/how-to-fix-windows-update-stuck-on-restarting-after-windows-11-update/) problem.

1. Open Task Manager with Ctrl + Shift + Esc.
2. Monitor disk and CPU for the setup and worker processes.
3. Active resources mean progress — wait, do not intervene.
4. Zero activity for over an hour confirms a genuine stall.

### Fix 2: Step 2 — Remove external devices

The cheapest unblock available: unplug every USB device except essentials. A single deadlocked peripheral driver is a classic 75% hang, and removal takes seconds.

1. Unplug USB drives, docks, printers, and peripherals.
2. Eject SD cards.
3. Disconnect external displays if the laptop screen suffices.
4. Wait 30 minutes for the installer to notice and resume.

### Fix 3: Step 3 — End the hung installer safely

If the stall is confirmed and devices did not unblock it, stop the installer through Task Manager rather than powering off. A process kill allows cleaner rollback than a hard power cut.

1. In Task Manager, end the Windows Setup and update worker processes.
2. Allow the system a few minutes to settle.
3. Restart the laptop normally through the Start menu.
4. Windows should roll back to the pre-update state cleanly.

### Fix 4: Step 4 — Clear staging debris and update drivers

With the system rolled back, remove the corrupted staging files and eliminate the driver suspects before retrying. Fresh drivers plus clean staging give the next attempt its best chance.

1. Run Disk Cleanup as administrator and remove temporary installation files.
2. Update chipset, storage, and display drivers from the manufacturer's site.
3. For Intel-based laptops, [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) identifies the correct versions.
4. Restart once more before the retry.

### Fix 5: Step 5 — Retry from a clean boot

Third-party services and startup apps are frequent 75% hang contributors. A clean boot strips them out so the retry runs against a minimal system. Driver-caused feature update failures that raise stop codes match the [error 0xc1900101](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/) pattern.

1. Run msconfig, hide Microsoft services, disable the rest.
2. Disable all startup items in Task Manager.
3. Restart and launch the 24H2 update again.
4. Monitor Task Manager — the 75% phase should now show real activity.

### Fix 6: Step 6 — Use installation media for the final attempt

If the in-place retry stalls identically, switch engines: the Media Creation Tool ISO performs the same 24H2 upgrade through the standard setup path, which handles migration differently than the update pipeline.

1. Create Windows 11 24H2 installation media.
2. Mount the ISO and run setup.exe, keeping files and apps.
3. Disconnect external devices before starting.
4. The setup engine's migration phase usually succeeds where the update pipeline hung.

### Fix 7: Step 7 — Recover if the rollback itself fails

In rare cases the rollback from Step 3 does not complete cleanly, leaving the system half-updated. Do not panic: Windows keeps the previous build's recovery data, and the startup repair environment can usually restore bootability when the desktop will not load.

1. Boot into the Windows Recovery Environment.
2. Choose Troubleshoot, then Advanced options, then Startup Repair.
3. If that fails, use System Restore to a point before the update attempt.
4. Once booted, clear staging debris before any retry.

## Closing

A 24H2 stall at 75% is a migration-phase problem with a migration-phase solution: verify the stall is real, strip away the external and software variables, clean the staging area, refresh the drivers, and retry — switching to installation media when the update pipeline itself is the hang. Step by step, the cruelest percentage yields.
