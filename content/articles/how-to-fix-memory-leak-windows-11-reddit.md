---
title: "How to Fix a Memory Leak in Windows 11 (RAM Keeps Climbing)"
slug: how-to-fix-memory-leak-windows-11-reddit
date: 2026-09-20
categories: ["performance"]
tags: ["memory leak", "ram", "windows 11", "high memory", "troubleshooting"]
description: "RAM usage climbs until your laptop crawls, and only a restart fixes it? That's a memory leak. Here's how to find the leaking process and stop it."
thumbnail: "/images/thumbs/how-to-fix-memory-leak-windows-11-reddit.webp"
faqs:
  - q: "What is a memory leak?"
    a: "A memory leak happens when a program allocates RAM but never releases it back to the system. Over hours of use, the leaked memory accumulates until RAM fills up, forcing heavy paging to disk and making the laptop crawl. Restarting temporarily clears it because all processes release their memory on shutdown — but the leak returns as soon as the buggy program runs again."
  - q: "How do I know if I have a memory leak or just need more RAM?"
    a: "Watch Task Manager's Performance > Memory tab over several hours of normal use. If committed memory climbs steadily while you're running the same apps — and drops back to normal after a restart — that's a leak. If memory is simply high from the moment you boot with your normal workload, you likely just need more RAM or fewer startup programs."
  - q: "Can Windows itself have a memory leak?"
    a: "Yes, though it's less common than third-party app leaks. Buggy drivers (especially network and storage drivers) can leak kernel memory, which shows up as growing 'Non-paged pool' in Task Manager. Windows updates sometimes introduce these, and subsequent updates or driver replacements fix them."
  - q: "Will a memory leak damage my laptop?"
    a: "No physical damage — a memory leak is purely a software bug. The worst effects are severe slowdowns, application crashes, and in extreme cases a full system freeze requiring a hard reboot. It's annoying and disruptive to your work, but your RAM modules, CPU, and other hardware are completely safe."
---

The pattern is unmistakable: you boot your laptop and everything is snappy. A few hours later, it's sluggish. By evening, it's crawling — apps take forever to switch, the disk light never stops, and Task Manager shows RAM at 95 percent even though you're running the same programs as this morning. Restart, and the cycle begins again. That's the signature of a memory leak: some process is allocating memory and never giving it back, slowly drowning your system.

Memory leaks are software bugs, not hardware failures. Somewhere in your running processes — an app, a driver, occasionally Windows itself — code is requesting memory and forgetting to release it. The leak might be megabytes per hour (annoying after a full day) or hundreds of megabytes per hour (crippling within an hour or two). Either way, the fix follows the same logic: identify the leaking process by watching memory grow, then update, replace, or work around that specific software.

This guide shows you how to confirm you actually have a leak (versus simply needing more RAM), how to find the culprit using built-in tools, and what to do once you've named it.

## Why this happens

- **Buggy application code**: The classic cause — an app allocates memory for operations and never frees it, accumulating over hours.
- **Leaking drivers**: Faulty network, storage, or graphics drivers leak kernel (non-paged pool) memory, which is worse because it can't be paged out.
- **Browser tab accumulation**: Browsers are the most common user-space leakers; dozens of tabs with heavy web apps slowly consume gigabytes.
- **Windows Update bugs**: Specific Windows builds have shipped with memory leaks in system components, fixed by later updates.
- **Antivirus real-time engines**: Some security products have had leak bugs in their filter drivers.
- **Long-running background services**: Services that run for days without restart accumulate small leaks into big ones.
- **Corrupted page file or memory management**: Rare, but damaged virtual memory configuration can mimic leak symptoms.
- **Actual faulty RAM**: Bad memory modules cause crashes and errors rather than gradual leaks — different symptom, different fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's actually a leak

Don't chase a leak if you simply need more RAM. This test distinguishes the two.

1. Restart your laptop and open Task Manager (**Ctrl + Shift + Esc**) > **Performance > Memory**.
2. Note the **In use** and **Committed** values with your normal apps open.
3. Use the laptop normally for 4-6 hours without restarting — same apps, normal work.
4. Check again. If memory has grown by gigabytes with no change in workload, you have a leak. If it's roughly the same, you just run a heavy workload — consider our [virtual memory guide](/articles/how-to-increase-virtual-memory-on-laptop/) or a RAM upgrade.

Also check the **Non-paged pool** value — if it's several GB and growing, the leak is in a driver (kernel space), which points to Fix 5.

### Fix 2: Find the leaking process with Task Manager

The simplest identification method works for most user-space leaks.

1. In Task Manager's **Processes** tab, click the **Memory** column to sort by usage.
2. Note the top consumers and their values.
3. Leave Task Manager open (or check back hourly) and watch which process's memory keeps growing while others stay stable.
4. The one that climbs steadily without coming back down is your leaker.

Common findings: web browsers with many tabs, Electron apps (Discord, Slack, Teams), Adobe software, and game launchers. Once identified, update that app first — leaks are often fixed in newer versions.

### Fix 3: Use Resource Monitor for precise tracking

For trickier cases, Resource Monitor gives per-process detail Task Manager doesn't.

1. Open Task Manager, go to the **Performance** tab, and click **Open Resource Monitor** at the bottom.
2. Go to the **Memory** tab and sort by **Commit** or **Working Set**.
3. Watch the **Hard Faults/sec** column too — high hard faults mean the system is paging heavily, confirming memory pressure.
4. The process with the largest and still-growing commit size is the leak source.

### Fix 4: Tame browser memory usage

Browsers are the number one source of user-space memory leaks. You don't need to abandon your browser — just manage it.

1. Install pending browser updates — memory leak fixes ship regularly.
2. Use a tab manager extension or the browser's built-in tab discarding (Chrome: Settings > Performance > Memory Saver).
3. Disable or remove extensions you don't need — each one is a potential leaker. Test in incognito/private mode (extensions disabled) to confirm.
4. For persistent problems, try a fresh browser profile, which eliminates corrupted profile data.
5. See our guide on [Chrome high CPU and memory](/articles/what-to-do-if-chrome-high-cpu-windows-11/) for browser-specific tuning.

### Fix 5: Update drivers to fix kernel leaks

A growing Non-paged pool means a driver is leaking. Network and storage drivers are the usual suspects.

1. In Task Manager's **Performance > Memory**, check the **Non-paged pool** size — over 1-2 GB on an idle-ish system is suspicious.
2. Use **PoolMon** (in the Windows Driver Kit) or the simpler **poolmon-like** views to identify the leaking pool tag, or just update the most likely drivers.
3. Update network (Wi-Fi/Ethernet), chipset, and storage drivers from your manufacturer's support page: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo.
4. For Intel systems, the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) finds the right versions.
5. Restart and monitor the Non-paged pool over several hours.

### Fix 6: Install all Windows updates

Microsoft does fix memory leaks in system components — but only if you install the updates.

1. Open **Settings > Windows Update** and install everything pending.
2. Check **Advanced options > Optional updates** for driver updates too.
3. Restart and monitor for a full day.
4. If a specific update is known to cause a leak (check the release notes), you may need to wait for the follow-up fix — in the meantime, scheduled nightly restarts mask the symptom.

### Fix 7: Mitigate while you wait for a proper fix

Sometimes the leaking software is essential and no fixed version exists yet. These workarounds manage the symptom.

1. **Scheduled restarts**: Set the leaky app to restart daily, or schedule a nightly reboot via Task Scheduler.
2. **Process isolation**: Run the leaky app in a separate user session or VM so its leak doesn't affect your main work.
3. **Memory limit tools**: Utilities can cap a process's working set, forcing it to page rather than consume all RAM.
4. **Find alternatives**: For chronic leakers with no fix, switching to a competing app is often the pragmatic answer.

If high memory is your constant state rather than a growing leak, our guide on [Windows 11 high memory usage](/articles/windows-11-high-memory-usage-fix/) covers the broader optimization picture.

## Closing

Memory leaks are found, not guessed at: confirm the growth pattern, identify the climbing process, and fix that specific software. Most leaks turn out to be a browser, an Electron app, or a driver — all fixable with updates. The restart-and-hope cycle ends the moment you name the culprit.
