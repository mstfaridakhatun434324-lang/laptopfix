---
title: "TiWorker High CPU on ASUS Laptop? Calm It Down"
slug: how-to-fix-tiworker-high-cpu-on-asus-laptop
date: 2026-10-07
categories: ["performance"]
tags: ["tiworker", "high cpu", "windows modules installer", "asus laptop", "windows update"]
description: "TiWorker.exe eating CPU on your ASUS laptop? Learn what the Windows Modules Installer Worker does and how to stop its CPU spikes."
thumbnail: "/images/thumbs/how-to-fix-tiworker-high-cpu-on-asus-laptop.webp"
faqs:
  - q: "What is TiWorker.exe and is it safe?"
    a: "TiWorker.exe is the Windows Modules Installer Worker, a legitimate Microsoft process that installs, modifies, and removes Windows updates and optional components. It is completely safe and essential — without it, your system cannot install updates. High CPU from TiWorker means it is actively working on updates, not that anything is broken."
  - q: "Why does TiWorker use 100% CPU for so long?"
    a: "TiWorker is single-threaded for many operations and does heavy file compression, decompression, and component-store maintenance, which is CPU intensive. On first run after a feature update, or when the component store needs cleanup, it can run at high CPU for 30 minutes to several hours. ASUS laptops with slower CPUs or HDDs feel this much more."
  - q: "Can I disable TiWorker.exe?"
    a: "You should not disable it permanently — it is the engine behind Windows Update, and disabling it breaks updating entirely. What you can do is manage when it runs: install updates on your schedule, clean the component store to reduce its workload, and fix corrupted update components that make it loop endlessly."
  - q: "How do I know if TiWorker is stuck versus just working?"
    a: "Open Task Manager's Details tab, add the CPU time column, and watch TiWorker over 15 minutes. If CPU time climbs steadily and disk activity is high, it is working — let it finish. If CPU time barely moves but CPU percentage stays high, or it has run for many hours with no progress in Windows Update, it is likely stuck and needs the fixes below."
---

Task Manager shows **TiWorker.exe** — the Windows Modules Installer Worker — devouring your CPU, the fans are screaming, and your ASUS laptop is barely usable. Before you reach for the kill button: TiWorker is supposed to run. It's the engine that installs Windows updates and maintains the component store. Killing it mid-update can corrupt your system.

The real question is whether it's *working* or *stuck*. A working TiWorker finishes in under an hour and never returns until the next update. A stuck one grinds for hours, returns daily, or loops forever on corrupted update components. ASUS laptops get this complaint often because Armoury Crate and ASUS updaters add their own update activity on top of Windows'. We'll distinguish working from stuck, then fix the stuck cases properly.

## Why this happens

- **Active update installation**: TiWorker legitimately spikes during monthly cumulative and feature updates.
- **Component store (WinSxS) maintenance**: Post-update cleanup and compression of the component store is CPU-heavy.
- **Corrupt update components**: Damaged update files make TiWorker retry endlessly instead of completing.
- **Stuck Windows Update queue**: A failed update keeps TiWorker attempting installation on every boot.
- **ASUS updater overlap**: Armoury Crate, MyASUS, and ASUS Live Update triggering driver installs alongside Windows Update.
- **Slow storage amplifying the work**: HDD-based ASUS laptops stretch a 20-minute job into hours.
- **Pending feature update**: Major version upgrades keep TiWorker busy far longer than monthly patches.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether TiWorker is working or stuck

This decides everything that follows.

1. Open **Task Manager** > **Details** tab, right-click the column headers, and enable **CPU time**.
2. Find **TiWorker.exe** and watch for 10–15 minutes: if **CPU time** climbs steadily and **Windows Update** shows activity, it's working — let it finish.
3. Check **Settings** > **Windows Update**: if updates are downloading or installing, TiWorker's CPU use is expected and temporary.
4. Signs of stuck: TiWorker runs for 3+ hours with no update progress, CPU time barely advances, or it returns at high CPU every single boot with no updates pending.
5. If it's working, the best fix is scheduling: let updates install overnight while plugged in, and the "problem" disappears. If it's stuck, continue below.

### Fix 2: Run the Windows Update troubleshooter

The automated first pass for stuck update workers.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply whatever it recommends — it resets update services and clears common blockages.
3. After it completes, check **Settings** > **Windows Update** and install anything pending — a clean successful update cycle often settles TiWorker permanently.
4. Reboot and watch TiWorker for 30 minutes: a fixed system shows brief TiWorker activity that tapers off.
5. If the troubleshooter reports it couldn't fix everything, note the error codes — they point to the specific repair needed in the following fixes.

### Fix 3: Reset Windows Update components manually

When the troubleshooter isn't enough, reset the machinery by hand.

1. Open **Command Prompt as administrator** and stop the services:
   `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the software distribution folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
4. Check for updates again — Windows rebuilds fresh update metadata, and TiWorker gets a clean job queue instead of a corrupted one.
5. This is Microsoft's own documented procedure (see their [Windows support hub](https://support.microsoft.com/en-us/windows)) and is safe — the .old folders can be deleted after a week of stable updates.

### Fix 4: Clean the component store (WinSxS)

TiWorker maintains WinSxS — a bloated store means endless work.

1. Open **Command Prompt as administrator** and analyze: `DISM /Online /Cleanup-Image /AnalyzeComponentStore`.
2. If reclaimable packages are large, run `DISM /Online /Cleanup-Image /StartComponentCleanup` — this is the maintenance TiWorker was struggling to do.
3. For deeper cleaning (after a stable update cycle), `/StartComponentCleanup /ResetBase` removes superseded components permanently — but you can't uninstall updates afterward, so only run it when the system is stable.
4. Our [WinSxS cleanup guide](/articles/how-to-clean-up-winsxs-folder-on-windows-11/) covers this in full detail.
5. After cleanup, TiWorker's maintenance workload shrinks dramatically — future spikes are shorter and rarer.

### Fix 5: Repair corrupt system files TiWorker depends on

Corruption in the servicing stack keeps TiWorker spinning.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated terminal — this repairs the component store itself from Windows Update.
2. Follow with `sfc /scannow` to repair protected system files.
3. If DISM fails with its own errors, the component store is deeply damaged — an in-place upgrade repair install (using [Windows 11 media](https://www.microsoft.com/en-us/software-download/windows11)) rebuilds it while keeping your files.
4. After repair, run Windows Update to completion — TiWorker should now process updates smoothly.
5. Check **Event Viewer** > **Windows Logs** > **System** for **CBS** or ** servicing** errors to confirm the corruption is actually gone.

### Fix 6: Manage ASUS updater overlap

ASUS's own updaters compete with Windows Update for the same servicing stack.

1. Open **MyASUS** and **Armoury Crate** and check for pending driver/BIOS updates — install them deliberately rather than letting them auto-trigger during Windows Update runs.
2. In MyASUS settings, change update checks from automatic to manual or weekly — you stay current without surprise servicing load.
3. Disable **ASUS Live Update** scheduled tasks in **Task Scheduler** if they fire daily — weekly is plenty.
4. Update the BIOS from the ASUS support site if a newer version mentions stability or update behavior — servicing-stack-adjacent firmware bugs exist.
5. Stagger the workloads: run Windows Update to completion first, reboot, then run ASUS updates — never both simultaneously.

### Fix 7: Schedule updates so TiWorker works on your terms

If TiWorker is healthy but badly timed, take control of the schedule.

1. Set **Active hours** (**Settings** > **Windows Update** > **Advanced options**) to cover your working day so restarts and heavy install work happen outside it.
2. Use **Pause updates** strategically — pause during critical work weeks, then unpause and let everything install overnight while plugged in.
3. For metered connections, set the network as metered to prevent surprise downloads — then manually update weekly.
4. Consider our [Windows Modules Installer guide](/articles/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update/) for the closely related servicing-host process.
5. Long-term: an SSD upgrade transforms TiWorker episodes from hours to minutes on ASUS laptops still running HDDs — the servicing workload is I/O-bound as much as CPU-bound.

## Closing

TiWorker high CPU on an ASUS laptop is usually either legitimate update work (let it finish, schedule it better) or a stuck servicing stack (reset update components, clean WinSxS, repair with DISM). Don't kill or disable it — fix what's making it loop. A healthy TiWorker is invisible: brief activity after updates, then silence until next month.
