---
title: "Windows 11 Memory Leak Troubleshooting: Find the Leaky Process"
slug: memory-leak-windows-11-troubleshooting
date: "2026-09-08"
categories: ["performance"]
tags: ["memory leak", "ram usage", "high memory", "windows 11", "troubleshooting"]
description: "RAM usage climbing until your laptop crawls? Troubleshoot Windows 11 memory leaks — find the leaky process and fix it for good."
thumbnail: "/images/thumbs/memory-leak-windows-11-troubleshooting.webp"
faqs:
  - q: "How do I know if I have a memory leak or just high RAM usage?"
    a: "Watch Task Manager's Performance, then Memory tab over several hours of normal use. Normal high usage stays roughly flat. A leak shows committed memory climbing steadily without coming back down, even after you close programs. If available RAM shrinks toward zero over a day and only a restart fixes it, you are looking at a leak, not legitimate use."
  - q: "Which processes commonly leak memory on Windows 11?"
    a: "Frequent offenders include buggy device drivers (their kernel memory leaks do not show in Task Manager's process list), Chromium-based browsers with leaky extensions, the Search Indexer during a corrupted index rebuild, and specific app versions with known leaks. Driver-caused leaks are the sneakiest because the memory is charged to the system, not to any visible process."
  - q: "Will adding more RAM fix a memory leak?"
    a: "No — more RAM only delays the symptoms. A true leak consumes memory without bound, so 32 GB just takes longer to fill than 16 GB. The fix is finding and updating, reconfiguring, or removing the leaking component. Treat extra RAM as headroom for legitimate workloads, never as a treatment for a leak."
  - q: "Is high memory usage right after boot a sign of a leak?"
    a: "Not by itself. Windows 11 aggressively caches files in RAM (Superfetch/SysMain behavior), so 50 to 70 percent usage at idle can be normal — cached memory is released instantly when apps need it. A leak is specifically memory that grows over time and is never released. Judge by the trend over hours, not by a single snapshot."
---

A memory leak is the slowest-motion crash in computing. Some process — or driver — allocates RAM and never gives it back. Hour by hour, available memory shrinks. The laptop gets sluggish, apps stutter, and eventually Windows starts paging furiously to disk or processes start crashing. Restart, and everything is fine again... until it is not.

The maddening part is that Task Manager often does not show an obvious culprit, because driver leaks hide in kernel memory. Troubleshooting a leak is detective work: observe the pattern, isolate the suspect, and confirm with the right tools. Here is the playbook.

## Why this happens

- **Buggy device drivers** — kernel-mode leaks that never appear under any process name in Task Manager.
- **Leaky applications** — browsers, extensions, and apps with known allocation bugs in specific versions.
- **Corrupted Search index** — the indexer reprocessing the same files in an endless loop.
- **Windows Update stuck mid-install** — update components holding memory across days.
- **Antivirus scan loops** — security software re-scanning the same content repeatedly.
- **Standby memory mismanagement** — cached memory not being released properly on some configurations.
- **Faulty RAM** — rarely, but bad memory modules cause symptoms that mimic leaks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the leak pattern

Do not chase a leak that is actually normal caching behavior.

1. Open **Task Manager → Performance → Memory** and note **In use** and **Available**.
2. Use the laptop normally for 2–3 hours, checking every 30 minutes — write the numbers down.
3. A leak shows **Committed** memory climbing steadily with no corresponding app growth.
4. Close all your apps: if memory stays high with nothing open, the leak is in a driver or service.
5. Restart and confirm memory returns to normal — the classic leak signature is "fine after reboot, worse over days."

Only proceed if you see the steady climb; otherwise you are looking at normal Windows caching.

### Fix 2: Identify the process with Task Manager details

Start with the obvious suspects before reaching for advanced tools.

1. In Task Manager, go to **Details**, right-click the column headers, and add **Commit size** and **Handles**.
2. Sort by **Commit size** — the top consumers are your suspects.
3. Watch for a process whose commit size grows over 30–60 minutes without you using it.
4. Browsers: check `chrome://task-manager` (Shift+Esc in Chrome) for per-tab memory — extensions show here too.
5. If no user process is growing but total committed climbs, the leak is kernel/driver-level — continue to Fix 4.

Screenshot the sorted list for reference; you will compare against it later.

### Fix 3: Isolate leaky apps and extensions

Application leaks are the easiest to fix — update, reconfigure, or remove.

1. Test in **Clean Boot**: `msconfig` → **Services** → **Hide all Microsoft services** → **Disable all**, then restart.
2. If the leak stops in Clean Boot, re-enable services in halves to bisect the culprit.
3. For browsers, disable all extensions and test for a day; re-enable one by one.
4. Check the vendor's site for a newer version — leaks are commonly fixed in patches once reported.
5. As a workaround for a must-keep leaky app, schedule a nightly restart of just that app via Task Scheduler.

Document which app it was; you will want to retest after each of its updates. If overall memory pressure is the issue rather than a leak, see the guide to [high memory usage after a Windows 11 update](/articles/how-to-fix-high-memory-usage-after-windows-11-update/).

### Fix 4: Hunt driver leaks with PoolMon and RAMMap

Driver leaks hide from Task Manager but not from Microsoft's free Sysinternals tools.

1. Download **RAMMap** from Microsoft Sysinternals and run it as administrator.
2. Check the **Use Counts** tab — abnormally large **Nonpaged Pool** (several GB) indicates a driver leak.
3. Use **PoolMon** (in the Windows Driver Kit) sorted by bytes to find which pool tag is growing.
4. Look up the pool tag online to identify the owning driver — network and storage drivers are frequent offenders.
5. Update or roll back that specific driver; if no update exists, check the [Update Catalog](https://www.catalog.update.microsoft.com/) for alternate versions.

Nonpaged pool growth is the smoking gun of a kernel leak — user-mode tools will never show it.

### Fix 5: Update or roll back suspect drivers

Once a driver is implicated, act on it directly.

1. Open **Device Manager**, find the device tied to the leaking driver.
2. Try **Update driver → Search automatically** first.
3. If the leak started after an update, use **Properties → Driver → Roll Back Driver**.
4. Get the manufacturer's latest driver directly (Intel, NVIDIA, AMD, Realtek) rather than relying on Windows Update.
5. Retest for 24–48 hours — driver leaks take time to manifest, so do not declare victory too early.

Keep notes on which version works; Windows Update may try to "upgrade" you back to the leaky one.

### Fix 6: Fix Windows' own memory hogs

Sometimes the leaker is part of Windows itself.

1. **Search Indexer**: rebuild via **Indexing Options → Advanced → Rebuild** if SearchIndexer.exe grows unboundedly.
2. **SysMain**: if RAMMap shows huge standby that never releases, try disabling **SysMain** in `services.msc` temporarily.
3. **Windows Update**: check for stuck updates in **Settings → Windows Update** — clear the SoftwareDistribution folder if an update has been "installing" for days.
4. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` to repair corrupted system components.
5. Install all pending Windows updates — Microsoft patches known memory leaks in cumulative updates.

Microsoft documents known issue fixes in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Test the RAM hardware itself

Rare, but faulty RAM produces leak-like symptoms that no software fix touches.

1. Run **Windows Memory Diagnostic**: search for it in Start, choose **Restart now and check**.
2. For a thorough test, boot **MemTest86** from a USB drive and run at least one full pass.
3. If errors appear, reseat the RAM modules (if accessible) and retest.
4. Replace faulty modules — mismatched or failing RAM causes exactly the "worse over time" pattern.
5. After replacing, monitor for a week to confirm the pattern is gone.

For general memory pressure that is not a leak, the [high memory usage fix guide](/articles/windows-11-high-memory-usage-fix/) covers tuning.

## Closing

Memory leak troubleshooting is pattern recognition: confirm the steady climb, separate user-mode suspects from kernel-mode ones, and use the right tool for each — Task Manager for apps, RAMMap and PoolMon for drivers. Most leaks end with a driver update or an app patch, not new hardware. The restart that "fixes" it is just the snooze button; finding the leaky component is the actual fix.
