---
title: "High Memory Usage After a Windows 11 Update? Fix It"
slug: how-to-fix-high-memory-usage-after-windows-11-update
date: 2026-09-03
categories: ["performance"]
tags: ["high memory usage", "ram usage", "windows 11 update", "memory leak", "fix"]
description: "RAM maxed out after a Windows 11 update? Find the memory hog — leaks, runaway services, or update debris — and bring usage back to normal."
thumbnail: "/images/thumbs/how-to-fix-high-memory-usage-after-windows-11-update.webp"
faqs:
  - q: "How much RAM usage is normal in Windows 11?"
    a: "On a 16GB machine, 40–60% at idle-to-light use is normal — Windows deliberately uses free RAM for caching (it releases cache instantly when apps need it). Concern starts when usage sits above 85% constantly, the system stutters, or Task Manager shows a single non-system process consuming gigabytes. Cached memory is not a problem; committed memory pressure is."
  - q: "Can a Windows update cause a memory leak?"
    a: "Yes. Updates replace drivers and system components, and a buggy new driver or service can leak memory — slowly consuming RAM until performance collapses. The signature is usage that climbs steadily after boot without new programs opening. If high usage began the day an update installed, a driver or service from that update is the prime suspect."
  - q: "Will adding more RAM fix high memory usage?"
    a: "It helps if you're genuinely running out — 8GB machines feel Windows 11's weight. But if a leak or runaway process is consuming the RAM, more memory just postpones the problem; the leak eventually fills that too. Diagnose first: find what's using the memory in Task Manager or RAMMap, fix the cause, and only then decide if an upgrade is warranted."
  - q: "Is high 'System and compressed memory' usage bad?"
    a: "Not necessarily — memory compression is Windows working as designed, squeezing inactive pages instead of paging to disk. But if the System process uses multiple gigabytes constantly while total usage is maxed, the kernel is struggling with pressure. That's a symptom of too little RAM for your workload or a driver leaking non-paged pool memory."
---

After the update, your RAM meter never comes down. Task Manager shows 85%, 90%, 95% memory usage with nothing obvious open, apps stutter, and the disk churns as Windows pages frantically. Something in the update is eating your memory — or the update exposed a problem that was already there.

Windows 11 uses RAM aggressively by design (caching), so the first job is distinguishing normal caching from a real problem. Then we find the hog: a leaky driver, a runaway service, or update debris. For CPU-side post-update issues, pair this with our [24H2 slowdown guide](/articles/how-do-i-fix-laptop-slow-after-windows-11-24h2-update/).

## Why this happens

- **Driver memory leak**: A buggy updated driver (network, storage, GPU) leaking non-paged pool memory.
- **Runaway service**: An update component (TiWorker, Search indexer) stuck in a loop consuming RAM.
- **Compressed memory under pressure**: Legitimate compression working overtime because RAM is genuinely tight.
- **Memory-hungry startup additions**: The update re-enabled or added background apps.
- **Superfetch/SysMain re-tuned**: Preloading behavior changed by the update on low-RAM machines.
- **Browser/app bloat exposed**: The update didn't cause it — it just pushed a nearly-full system over the edge.
- **Corrupt pagefile**: A damaged pagefile forcing the kernel into expensive memory juggling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read Task Manager correctly

Distinguish caching (fine) from pressure (problem).

1. Open Task Manager > **Performance** > **Memory**. Note three numbers: **In use**, **Available**, and **Committed**.
2. High "In use" with high "Available" = caching, not a problem. Windows releases cached RAM instantly when needed.
3. The real red flag: **Committed** near or above physical RAM, or **Available** under 1GB with stuttering.
4. Go to **Processes**, sort by **Memory** — identify the top consumers. A single app (browser, IDE) using 3GB+ is a workload issue; a system process (`System`, `Registry`, `svchost`) ballooning is a leak.
5. Check the **Details** tab too — some hogs hide under generic names. Note the exact process names and their Private Working Set sizes.
6. Screenshot the top 5 — you'll compare against this after each fix.

### Fix 2: Find the leak with pool monitoring

When a driver is the leaker, Task Manager won't name it — PoolMon will.

1. If the **System** process or **Non-paged pool** (Task Manager > Performance > Memory, bottom) keeps growing after boot, it's a kernel-mode leak — almost always a driver.
2. Install the Windows Driver Kit tools or use **PoolMon** to see pool usage by tag; alternatively, **RAMMap** (Sysinternals) shows exactly where memory went (look for huge Nonpaged Pool or Metafile growth).
3. Correlate timing: did the growth start with the update? Check **Settings** > **Windows Update** > **Update history** for driver updates delivered with it.
4. The usual leaky suspects after updates: network drivers (Wi-Fi), storage drivers, and GPU drivers.
5. Once suspected, update that driver from the laptop maker's site — or roll it back (Device Manager > device > Properties > Driver > Roll Back Driver) if the leak started with the new version.

### Fix 3: Stop runaway update and indexing processes

Post-update background work that never finishes.

1. In Task Manager, look for `TiWorker.exe`, `SearchIndexer.exe`, `MsMpEng.exe` with large and growing memory footprints.
2. Let legitimate post-update work finish: plug in, leave idle overnight. Check in the morning — settled = it was just the update storm.
3. If TiWorker is stuck for days: run the Windows Update troubleshooter (**Settings** > **System** > **Troubleshoot** > **Other troubleshooters**).
4. For a stuck indexer: rebuild it (**Settings** > **Privacy & security** > **Searching Windows** > **Advanced indexing options** > **Advanced** > **Rebuild**).
5. For Defender: update definitions and let one full scan complete — a wedged scan loop holds memory.
6. Persistent runaways after 72 hours are bugs, not settling — treat them as such and repair (Fix 6).

### Fix 4: Trim what loads at boot

The update re-enabled things — take them back off.

1. Task Manager > **Startup apps**: disable high-impact and unneeded entries, especially anything the update re-enabled.
2. **Settings** > **Apps** > **Installed apps**: uninstall anything the update added that you don't want (trial apps, "suggested" software).
3. **Settings** > **Privacy & security** > **Background apps**: revoke background permission for apps that don't need it — each holds RAM.
4. Check browser extensions too — updates don't touch them, but a bloated browser is often the actual top consumer people blame on Windows. Test with extensions disabled.
5. Reboot and compare against your Fix 1 screenshot — the top-5 list should look leaner.

### Fix 5: Tune virtual memory and SysMain

Give Windows the paging room it expects.

1. **System Properties** > **Advanced** > **Performance** > **Settings** > **Advanced** > **Virtual memory** > **Change**: ensure it's **System managed**. A fixed small pagefile under update-induced pressure causes thrashing.
2. To clear a possibly corrupt pagefile: set **No paging file**, reboot, set back to **System managed**, reboot.
3. Consider SysMain: on 8GB machines with HDDs it helps; on SSDs with tight RAM it can add pressure. Test disabling the **SysMain** service (`services.msc`) — if memory pressure eases, leave it off.
4. Enable **Storage Sense** (**Settings** > **System** > **Storage**) to auto-clean temp files — update debris consuming disk space indirectly worsens memory pressure via paging.
5. Aim for 15%+ free disk space — paging needs room to work.

### Fix 6: Repair system files and drivers broadly

When the cause resists identification.

1. Elevated terminal: `DISM /Online /Cleanup-Image /RestoreHealth` → `sfc /scannow` → reboot.
2. Update **chipset**, **storage**, **network**, and **graphics** drivers from the laptop maker's support site — cover all four, since any can leak.
3. Install all pending Windows updates — Microsoft fixes leaks in cumulative updates; also check the [Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update is stuck.
4. [Perform a clean boot](/articles/how-to-perform-clean-boot-windows-11-on-laptop/) — if memory is calm in clean boot, a third-party driver/service leaks; binary-search by halves to find it.
5. For machines where the maker offers it, update the BIOS — firmware-level memory management bugs are rare but real.

### Fix 7: Decide on the RAM question honestly

Sometimes the answer is hardware.

1. After all fixes, measure idle-to-typical usage: if your normal workload (browser + Office + Teams) genuinely needs 10GB on an 8GB machine, no software fix creates RAM.
2. Check if your laptop's RAM is upgradeable (many thin-and-lights are soldered — check the maker's specs). If upgradeable, 16GB is the Windows 11 comfort zone.
3. In the meantime, reduce the workload: fewer browser tabs (use tab suspension extensions), close the IDE when not coding, quit Teams/Slack when not needed.
4. Use **Task Manager** > **Startup** discipline permanently — every auto-starting app is RAM you'll never get back.
5. Document the leaky driver if you found one — report it to the maker. Driver leaks get fixed when users report them with specifics (pool tag, driver version, growth rate). Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) has channels for update-related issues.

## Closing

High memory usage after an update is a who-done-it: read Task Manager correctly, identify whether it's caching or a real leak, find the driver or runaway process, trim the re-enabled bloat, and repair what's damaged. Most cases resolve without new RAM — but when the workload genuinely exceeds the hardware, that's data worth having too.
