---
title: "Memory Leak in Windows 11? Find and Fix It Step by Step"
slug: how-to-fix-memory-leak-windows-11-step-by-step
date: 2026-09-30
categories: ["performance"]
tags: ["memory leak", "ram leak", "windows 11", "high memory usage", "step by step"]
description: "Suspect a memory leak in Windows 11? Follow this step-by-step guide to confirm the leak, identify the culprit, and fix it permanently."
thumbnail: "/images/thumbs/how-to-fix-memory-leak-windows-11-step-by-step.webp"
faqs:
  - q: "How long does it take to confirm a memory leak?"
    a: "Plan for at least 4–6 hours of normal use between measurements, or ideally a full day. Slow leaks — the most common kind — grow by hundreds of megabytes per hour, which is invisible in a 15-minute window but obvious across a workday. Fast leaks that eat gigabytes in an hour are easier to catch but rarer. Patience is the actual diagnostic tool here."
  - q: "What is the difference between paged and non-paged pool?"
    a: "Both are kernel memory pools. Paged pool can be swapped to disk when RAM is tight; non-paged pool must stay in physical RAM always because it is used by drivers at interrupt level where paging is impossible. Non-paged pool leaks are more dangerous — they consume unpageable RAM directly — and they always indicate a driver problem, never an app problem."
  - q: "Can Windows Memory Diagnostic find a memory leak?"
    a: "No — it finds faulty RAM hardware, which is a different problem. A memory leak is software allocating memory and not freeing it; the RAM itself is fine. Memory Diagnostic is still worth running to rule out bad hardware (bad RAM causes crashes, not leaks), but it will report healthy RAM on a system with a severe software leak. Do not confuse the two diagnostics."
  - q: "Will adding more RAM fix a memory leak?"
    a: "It delays the symptoms but never fixes the cause. More RAM gives the leak a bigger bucket to fill — instead of crawling after 8 hours, the system crawls after 24. The leak continues until it exhausts any amount of RAM. Fix the leaking software or driver; treat a RAM upgrade as a separate decision about your workload, not as a leak remedy."
---

Memory that never comes back is the defining symptom of a leak: you close every app, but Task Manager still shows 80% RAM in use, and only a reboot restores it. Hours later, the memory is gone again. Something is allocating RAM and never releasing it — and rebooting treats the symptom while the cause keeps leaking. The reboot treadmill is the signature frustration of memory leaks.

This guide is the systematic version of memory-leak hunting. You will confirm the leak with before-and-after measurements, determine whether the leaker is a user-mode app or a kernel driver (the fixes are completely different), identify the specific process or driver, and apply the targeted fix. It takes patience — leaks reveal themselves over hours — but the method is reliable. Leaks reveal themselves over hours, so patience is part of the toolkit.

For the HP-specific variant with vendor driver steps, see [memory leak on HP laptops](/articles/how-to-fix-memory-leak-windows-11-on-hp-laptop/). For general high RAM usage that is not a leak, see [Windows 11 high memory usage](/articles/windows-11-high-memory-usage-fix/). Confirm the leak first; high usage alone is not a leak.

## Why this happens

- **Leaking user-mode applications**: apps that allocate memory without freeing it — browsers, Electron apps, games.
- **Kernel driver pool leaks**: drivers leaking non-paged or paged pool memory over time.
- **Handle leaks**: programs leaking handles, each pinning kernel memory.
- **Windows service bugs**: specific builds with leaking services (search, widgets).
- **Corrupted driver binaries**: damaged drivers misbehaving after updates or bad installs.
- **Standby memory misread as leak**: normal caching mistaken for a leak — ruled out in Fix 1.
- **Memory compression issues**: broken compression keeping pages pinned.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Prove the leak with measurements

Do not chase a leak you have not confirmed. Numbers first. The non-paged pool number is the single most informative figure here.

1. After a fresh boot, record Task Manager > Performance > Memory: In use, and the Non-paged pool size.
2. Use the PC normally for 4–6 hours without rebooting, then record the same figures.
3. Growth of 1GB+ in use with the same workload, or hundreds of MB in non-paged pool, confirms a real leak.

### Fix 2: Rule out normal caching

Windows fills free RAM with cache deliberately. Make sure that is not what you are seeing. Standby cache is Windows being smart, not Windows leaking.

1. In Task Manager > Performance > Memory, check the Cached and Available figures.
2. High 'In use' with high 'Available' is just caching — not a leak.
3. A real leak shows Available shrinking toward zero while Cached stays flat.

### Fix 3: Find the growing user-mode process

Sort and watch: the leaker's number climbs while others stay flat. Sort by Handles too; handle leaks are memory leaks in disguise.

1. In Task Manager's Details tab, add the Handles and Memory columns.
2. Sort by Memory and watch for 15 minutes; note any process climbing steadily.
3. Also watch Handles — a climbing handle count with climbing memory is a classic leak signature.

### Fix 4: Check for kernel pool leaks

If no user process grows but memory vanishes, a driver is leaking kernel pool. PoolMon's output is cryptic but the tag-to-driver mapping is well documented.

1. Compare Non-paged pool size from Fix 1's before/after measurements.
2. Growth over ~200MB points to a driver; use PoolMon (in the Windows Driver Kit) to identify the pool tag.
3. Map the tag to its driver and update, roll back, or disable that device.

### Fix 5: Update or remove the leaking software

Once named, the fix is specific to the offender. Check changelogs for the word leak; vendors do fix these.

1. For apps: update to the latest version — leak fixes are common in changelogs.
2. For drivers: get the update from your laptop maker's support site, not just Windows Update.
3. If no update exists, disable or replace the component — a leaking optional driver is not worth keeping.

### Fix 6: Use Driver Verifier for stubborn driver leaks

When PoolMon is inconclusive, Verifier stresses drivers until the leaker crashes identifiably. Do not leave Verifier on permanently; it slows the whole system.

1. Run verifier.exe as admin and choose standard settings for suspect third-party drivers.
2. Reboot and use the PC; Verifier will bugcheck on the misbehaving driver.
3. Analyze the minidump, fix the driver, then run verifier /reset to turn it off.

### Fix 7: Reset Windows if the leaker cannot be found

Some leaks come from deep system corruption no tool will name. Reinstall apps slowly afterward, watching memory after each.

1. Back up your files completely.
2. Use Settings > System > Recovery > Reset this PC, keeping files.
3. Install drivers from the manufacturer first, then monitor memory for two days before reinstalling apps. See [Microsoft's Windows help](https://support.microsoft.com/en-us/windows).

### Fix 8: Analyze memory usage with RAMMap

Microsoft's free RAMMap utility breaks down exactly how Windows is using every megabyte — active processes, the file cache, driver locked memory, and the pools. When Task Manager's numbers do not add up, RAMMap's Use Counts tab shows where the missing memory went, distinguishing a process leak from a driver or system leak at a glance.

1. Download RAMMap from Microsoft Sysinternals and run it as administrator.
2. Open the Use Counts tab and sort by Total.
3. Look for abnormally large Nonpaged Pool, Paged Pool, or Driver Locked rows.
4. Match the finding to Fix 3 (process), Fix 4 (driver pool), or Fix 6 (Verifier).

## Closing

Memory leaks are found with patience and a stopwatch, not with guesswork: measure before and after, separate user-mode leakers from kernel pool leaks, name the specific offender, and fix that component. Reboots reset the clock; only removing the leaker stops it. Work the steps in order and the vanishing RAM will have a name — and a fix. Measure, name, fix: the only sequence that works.
