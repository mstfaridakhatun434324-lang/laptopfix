---
title: "Fixing High Memory Usage in Windows 11, Step by Step"
slug: "how-to-fix-high-memory-usage-step-by-step"
date: "2026-09-22"
categories: ["performance"]
tags: ["high memory usage", "ram", "windows 11", "step by step", "performance"]
description: "A methodical, step-by-step procedure for diagnosing and fixing high RAM usage on Windows 11 — from identifying the consumers to deciding on a hardware upgrade."
thumbnail: "/images/thumbs/how-to-fix-high-memory-usage-step-by-step.webp"
faqs:
  - q: "What counts as high memory usage on Windows 11?"
    a: "Sustained usage above 85% during your normal workload is the practical threshold — beyond it, Windows pages aggressively to disk and responsiveness drops. Usage between 50 and 80% is normal and healthy; Windows deliberately uses free RAM for caching. Judge by sustained percentages during real work, not by momentary spikes."
  - q: "Should I follow these steps in order?"
    a: "Yes. The sequence is designed so each step's results inform the next: measure first, then remove the biggest discretionary consumers, then address system-level causes, then verify. Skipping ahead to dramatic measures (like disabling services) before identifying your actual consumers wastes effort and risks breaking things."
  - q: "How do I know if I need more RAM or just cleanup?"
    a: "After completing the software cleanup steps, use the laptop normally for a few days. If memory still sustains above 85% during ordinary work — not gaming or video editing, just your daily tasks — the workload exceeds capacity and a RAM upgrade is justified. If cleanup brought you comfortably below 80%, you did not need hardware."
  - q: "Is it normal for Windows 11 to use a lot of RAM at idle?"
    a: "Somewhat. A clean Windows 11 install typically idles at 3 to 4 GB (35 to 50% of 8 GB), which includes the system cache that Windows happily surrenders when programs need it. Idle usage above 70% on 8 GB, however, indicates bloatware, excessive startup apps, or a leak worth investigating."
---

High memory usage is one of those problems everyone "fixes" with random tips and nobody fixes systematically. This guide is the systematic version: a numbered procedure where each step builds on the last, with clear decision points telling you when to stop. Follow it top to bottom, and you will end with either a lean system or a justified hardware upgrade — never a guess.

The procedure assumes Windows 11 and a complaint of sustained high RAM usage: the laptop feels slow, Task Manager shows 85%+ memory, and you want it resolved properly. Budget about an hour, plus a few days of observation at the end.

If your situation is HP-specific, our [HP memory guide](/articles/how-to-fix-high-memory-usage-on-hp-laptop/) targets that preload; if you suspect a leak rather than ordinary usage, our [memory leak guide](/articles/how-to-fix-memory-leak-windows-11-youtube/) covers that diagnosis.

## Why this happens

- **Too many startup apps:** Each autostart program claims RAM before you do anything.
- **Browser tab and extension bloat:** Modern browsers are the largest discretionary RAM consumer.
- **Preloaded manufacturer software:** OEM utilities consume memory from the first boot.
- **Background services accumulating:** Updaters, sync clients, and helpers each take their share.
- **Memory leaks:** Buggy programs or drivers growing without bound over days.
- **Windows features using RAM legitimately:** Caching, preloading, and compression that look alarming but are healthy.
- **Insufficient physical RAM:** 8 GB workloads on 8 GB machines — simple arithmetic.
- **Paging amplifying the pain:** Once RAM exhausts, disk paging makes everything feel far worse than the numbers suggest.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Establish your baseline measurements

1. Open Task Manager, Performance tab, Memory: record total RAM, current percentage, and speed.
2. On the Processes tab sorted by Memory, record the top ten consumers with their MB values.
3. Note uptime (Performance, CPU): high usage at 10 days uptime means something different than at 10 minutes.
4. Take a screenshot — you will compare against this at the end.

Baselines make the whole procedure scientific. Without one, you cannot tell whether a change helped, and you will keep "fixing" things that were never the problem. The top-ten list is your hit list for the steps below; everything else is secondary.

### Fix 2: Trim startup apps

1. In Task Manager's Startup apps tab, sort by Startup impact.
2. Disable everything High or Medium impact that you do not need within a minute of boot.
3. Keep antivirus enabled; disable chat apps, launchers, updaters, and utilities.
4. Restart and re-measure idle memory against your baseline.

Startup apps are RAM you pay for before doing any work. This step typically reclaims 500 MB to 1.5 GB on a cluttered machine — often enough to drop sustained usage out of the paging zone. Our [Windows 11 startup guide](/articles/how-to-disable-startup-apps-on-windows-11/) details the hiding spots (scheduled tasks, Startup folders) for thoroughness.

### Fix 3: Audit the browser

1. Open the browser's task manager (Shift+Esc in Chrome/Edge) and sort by memory.
2. Remove extensions you do not use weekly; disable the rest you do not need today.
3. Enable sleeping tabs so background tabs release memory.
4. Close the browser completely once daily — it is the simplest leak mitigation that exists.

Browsers routinely consume more RAM than the entire operating system. A disciplined tab and extension policy is the highest-yield behavioral change in this guide. If your top-ten baseline was browser-dominated, this step alone may resolve the complaint.

### Fix 4: Remove unneeded programs and manufacturer bloat

1. Go to Settings, Apps, Installed apps, and sort by size or review by vendor.
2. Uninstall trial antivirus (let Defender take over), manufacturer "experiences," and software you have not opened in months.
3. Use vendor removal tools for antivirus products to clear leftover services.
4. Restart and re-measure.

Every installed program is a potential background service, updater, or shell extension consuming RAM. The uninstall pass also removes future startup entries and scheduled tasks. Be honest about what you actually use — the "might need it someday" programs are costing you memory every day.

### Fix 5: Check for memory leaks

1. Leave Task Manager's Details tab (with memory columns enabled) visible during a normal workday.
2. Watch for any process whose memory climbs steadily without dropping — that is a leak signature.
3. For System-attributed growth, check the non-paged pool on the Performance tab; growth there means a driver leak.
4. Update, reconfigure, or replace leaking programs; update drivers for pool leaks.

Leaks reveal themselves over hours, which is why this step sits mid-procedure: by now the obvious consumers are gone, so remaining growth stands out. Our [memory leak guide](/articles/how-to-fix-memory-leak-windows-11-youtube/) has the full PoolMon procedure for driver-level leaks. Do not confuse normal growth (a video editor caching footage) with leaking (a utility growing while idle).

### Fix 6: Tune Windows memory features

1. Verify the paging file is system-managed: `sysdm.cpl`, Advanced, Performance Settings, Advanced, Virtual memory.
2. Check Memory Compression status in PowerShell with `Get-MMAgent` — it should normally be enabled.
3. Review SysMain (services.msc): on RAM-constrained systems, disabling it can reduce memory pressure.
4. Ensure Windows is fully updated — Microsoft tunes memory management in cumulative updates; check Microsoft's Windows support pages for known issues.

These are the system-level tunables, placed late deliberately: they matter less than the application-level fixes above, and misapplied they cause more harm. The paging file should almost always stay system-managed; compression should stay on unless testing shows otherwise. Make one change at a time and measure.

### Fix 7: Decide on a hardware upgrade with data

1. After all software steps, use the laptop normally for three to five days.
2. If sustained usage during ordinary work stays above 85%, the workload exceeds capacity — upgrade RAM.
3. Check your model's maximum and slot configuration via the manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
4. Install matching RAM and verify the new total and dual-channel operation in Task Manager.

This is the earned conclusion, not a guess: you have the baseline, the cleanup results, and days of post-cleanup measurements proving the workload needs more headroom. Buy the right generation and speed, install per the service manual, and enjoy the headroom. If the machine has soldered RAM and cannot upgrade, the software leanness you achieved is the permanent solution — maintain it with quarterly audits.

## Closing

High memory usage surrenders to procedure: measure, trim startup, audit the browser, remove bloat, check for leaks, tune system features, and only then consider hardware — with data justifying the purchase. Each step's measurements feed the next step's decisions, so nothing is guesswork. Follow the sequence fully once, maintain it lightly afterward, and memory pressure stops being a recurring problem.
