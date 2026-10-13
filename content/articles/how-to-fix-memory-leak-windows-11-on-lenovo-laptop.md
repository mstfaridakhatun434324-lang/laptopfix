---
title: "Memory Leak in Windows 11 on a Lenovo Laptop? Plug It"
slug: how-to-fix-memory-leak-windows-11-on-lenovo-laptop
date: 2026-09-18
categories: ["performance"]
tags: ["memory leak", "ram usage", "windows 11", "lenovo laptop", "non-paged pool"]
description: "RAM usage climbing endlessly on your Lenovo laptop? Learn to identify memory leaks in Windows 11 and plug them — app, driver, or system."
thumbnail: "/images/thumbs/how-to-fix-memory-leak-windows-11-on-lenovo-laptop.webp"
faqs:
  - q: "What is a memory leak, exactly?"
    a: "A memory leak is when a program allocates RAM and never releases it — each operation grabs a little more, and over hours or days the process balloons until the system crawls. Unlike normal high memory usage (which is stable), a leak is defined by growth: the same workload uses more RAM the longer the system runs. The nastiest leaks are in drivers, where leaked kernel memory can't be reclaimed without a reboot."
  - q: "How can I tell a memory leak from normal high RAM usage?"
    a: "Watch it over time. Note Task Manager's memory 'In use' figure, use the laptop normally for several hours without rebooting, and check again — growth of 1GB+ with the same apps open indicates a leak. For precision, use RAMMap: a steadily growing non-paged pool means a driver leak; a single process with an ever-growing working set means an app leak."
  - q: "Can a memory leak damage my Lenovo laptop?"
    a: "Not physically — RAM doesn't wear out from being full. But the consequences are real: as the leak consumes memory, Windows compresses RAM aggressively, pages to disk (causing severe slowdowns and disk thrashing), and eventually apps crash or the system becomes unusable until reboot. Chronic kernel leaks can also destabilize the system. It's a reliability and performance problem, not a hardware-damage problem."
  - q: "Will restarting fix a memory leak?"
    a: "Temporarily — a reboot clears all RAM, so the leak starts from zero again. If you reboot daily and never notice the problem, that's a viable coping strategy, but it's not a fix: the leak is still there, growing between reboots. The real fix is updating or replacing the leaky app or driver. Use restarts as a stopgap while you identify the culprit with the steps below."
---

Your Lenovo laptop boots fine, works great for a few hours — and then the wheels come off. Everything slows, the disk starts thrashing, Task Manager shows RAM at 90%+, and the only cure is a reboot. Then the cycle repeats. That's the classic signature of a memory leak: not high memory usage, but *growing* memory usage that never comes back down.

Memory leaks come in two species, and the distinction matters. **App leaks** live in user-mode programs — a browser, a game, a utility — and you fix them by updating, reconfiguring, or replacing the app. **Driver leaks** live in kernel mode (visible as a growing "non-paged pool"), and you fix them with driver updates. This guide shows you how to determine which species you're dealing with, identify the exact culprit, and plug it.

For general high-RAM situations that aren't leaks, see [Windows 11 using too much RAM at idle](/articles/best-way-to-fix-windows-11-using-too-much-ram-idle/) and [Windows 11 high memory usage fix](/articles/windows-11-high-memory-usage-fix/).

## Why this happens

- **Buggy application**: An app allocating memory per operation without freeing it (browsers, long-running utilities).
- **Leaky device driver**: Kernel-mode driver leaking non-paged pool memory — the most damaging kind.
- **Windows component bug**: Occasionally a Windows service or shell component leaks after specific updates.
- **Antivirus filter drivers**: Security product drivers with pool leaks under certain workloads.
- **Corrupt pagefile interaction**: Rare, but pagefile misconfiguration can amplify leak symptoms.
- **Lenovo utility background processes**: Preinstalled utilities with long-running background tasks occasionally leak.
- **Hardware error retries**: Failing hardware causing drivers to allocate repeatedly for retried operations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's actually a leak (the growth test)

Don't hunt a leak that doesn't exist.

1. Reboot, then open Task Manager > **Performance** > **Memory** — write down the **In use** figure and the **Non-paged pool** size.
2. Use the laptop normally for 4–6 hours (or leave it running overnight) without rebooting and without changing your app mix dramatically.
3. Check both numbers again: **In use** growth of 1GB+ with the same apps open = likely app leak. **Non-paged pool** growth of several hundred MB+ = driver/kernel leak (more serious).
4. Also note in the **Processes** tab (sorted by Memory) whether one specific process has grown dramatically — that's your app-leak suspect.
5. If numbers are stable but high, it's not a leak — it's bloat. Stop here and work on startup trimming and app discipline instead of leak-hunting.

### Fix 2: Identify the leaking app with Task Manager and RAMMap

Name the culprit precisely.

1. In Task Manager's **Details** tab, right-click the column headers > **Select columns** > enable **Memory (active private working set)** and **Handles** — sort by memory.
2. A leaking app shows a huge and growing private working set, often with a climbing handle count too (handle leaks accompany memory leaks).
3. For deeper analysis, download **RAMMap** (Microsoft Sysinternals, free) — its **Use Counts** tab breaks down exactly where RAM is going, and sorting processes by private bytes confirms the leader.
4. Common app-leak offenders: browsers with many tabs (test by restarting the browser — if RAM plummets, the browser or an extension leaks), Electron apps (Teams, Discord, Slack) left running for days, and utilities with background monitoring.
5. Write down the exact process name and version — you'll need it for the update/replace step.

### Fix 3: Fix the leaking app

Update, reconfigure, or replace.

1. Update the app to the latest version — memory leaks are common bug-fix items in changelogs. Check the vendor's site directly, not just the in-app updater.
2. For browser leaks: disable extensions one by one (extensions leak too), enable **Memory Saver**, and make a habit of restarting the browser daily rather than running week-long sessions.
3. For Electron apps: check settings for memory-related options, update them, and quit them fully (not minimize-to-tray) when not in active use.
4. If the app is non-essential and still leaks after updating, replace it — there's almost always an alternative without the leak. Life's too short to babysit leaky software.
5. As a stopgap, schedule a daily restart of just the app (Task Scheduler can kill and relaunch it overnight) while you wait for a vendor fix.

### Fix 4: Diagnose a driver (non-paged pool) leak

The kernel-level investigation.

1. If **Non-paged pool** is growing (Fix 1), download **PoolMon** (in the Windows Driver Kit) or use RAMMap's pool tagging — the pool tag with the largest growing allocation identifies the leaking driver.
2. Alternatively, run `poolmon.exe -b` in an elevated terminal and sort by **Bytes** — watch which tag grows over 30–60 minutes.
3. Look up the pool tag online (Microsoft documents many; vendor tags are searchable) to identify the owning driver — network, storage, and antivirus filter drivers are the usual suspects.
4. On Lenovo laptops, also suspect Lenovo's own drivers: check [Lenovo's support site](https://support.lenovo.com/us/en/) and **Lenovo Vantage** for driver updates before anything else.
5. Document the tag and driver name — Fix 5 targets it.

### Fix 5: Update or replace the leaking driver

Plug the kernel leak.

1. Get the latest driver for the identified component: network drivers from Intel ([Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)) or the card vendor; storage from Lenovo's site; GPU from NVIDIA / AMD / Intel download pages.
2. For a **clean** update: uninstall the old driver in Device Manager (check "attempt to remove the driver software"), restart, then install fresh — this clears any corrupted driver state contributing to the leak.
3. If the leak *started* with a driver update, roll back: Device Manager > device > **Properties** > **Driver** > **Roll Back Driver**.
4. For antivirus filter driver leaks: update the AV product, or temporarily switch to Windows Defender (uninstall the third-party product with its removal tool) to confirm the leak stops — then decide whether to reinstall a fixed version.
5. Re-run the growth test (Fix 1) after the driver change — non-paged pool should now stay flat over hours.

### Fix 6: Check Lenovo-specific background processes

The OEM angle.

1. Open Task Manager and look for Lenovo-named processes (Lenovo Vantage Service, ImController, etc.) with growing memory — Lenovo's **ImController** has had leak bugs in specific versions.
2. Update **Lenovo Vantage** and all Lenovo system software to the latest versions — leak fixes ship in these updates.
3. If a Lenovo utility is the confirmed leaker and you don't need it, disable its service (**services.msc** > set to **Manual**) or uninstall the utility — keep only what you actively use.
4. Check Lenovo Vantage's **System Update** section for BIOS and firmware updates too — low-level firmware leaks are rare but real.
5. After changes, run the growth test again focusing on those processes.

### Fix 7: System-level repair for unidentified leaks

When the culprit won't reveal itself.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow` — corrupt system components can leak, and these repairs cover them.
2. Install all pending Windows updates — Microsoft fixes Windows-component leaks in cumulative updates. Check their official [Windows support page](https://support.microsoft.com/en-us/windows) for known leak issues in your build.
3. Do a **clean boot** (`msconfig` > hide Microsoft services > disable all) and run the growth test — if the leak stops, re-enable in halves to isolate the leaking third-party component.
4. Check for failing hardware: `wmic diskdrive get status`, memory test via `mdsched.exe` — hardware errors can drive driver retry loops that look like leaks.
5. Last resort: a clean Windows reinstall eliminates every software leak definitively — back up, reinstall from the Microsoft ISO, and add apps back gradually, running the growth test after each batch to catch the leaker if it returns.

## Closing

Memory leaks are diagnosed by growth, not by snapshots — the time-based test in Fix 1 is the foundation everything else builds on. Identify whether it's an app or a driver, update or replace the culprit, and verify with a second growth test. A system without leaks is a system that runs as well on day thirty as on day one — no ritual reboots required.
