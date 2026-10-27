---
title: "How to Fix VBS and Core Isolation Slowing Down Your NPU"
slug: vbs-core-isolation-npu-performance-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["vbs", "core isolation", "npu performance", "virtualization", "windows security", "troubleshooting"]
description: "Fix VBS and Core Isolation slowing your NPU with steps to measure the impact, update drivers, tune memory integrity, and balance security with AI speed."
thumbnail: "/images/thumbs/vbs-core-isolation-npu-performance-fix.webp"
faqs:
  - q: "What are VBS and Core Isolation?"
    a: >
      Virtualization-based Security uses hardware virtualization to isolate sensitive Windows processes, and Core Isolation with Memory Integrity is its best-known feature. Together they protect credentials and kernel memory from attacks, but the isolation layer adds overhead to some workloads, including NPU tasks.
  - q: "How much do VBS and Core Isolation slow the NPU?"
    a: >
      The impact varies by workload and driver. Light AI tasks may show no measurable difference, while heavy sustained NPU inference with frequent driver calls can slow noticeably. Measuring before and after is the only reliable way to know on your machine.
  - q: "Is it safe to turn off Memory Integrity?"
    a: >
      Turning off Memory Integrity removes protection against malicious drivers and kernel attacks. It is a real security tradeoff, so it should be done deliberately for a measured performance problem, not casually, and ideally only after driver updates fail to help.
  - q: "Does VBS affect gaming or CPU performance too?"
    a: >
      VBS can affect gaming and CPU workloads as well, particularly on older processors. On modern AI laptop processors the CPU impact is usually small, but NPU and virtualization-heavy workloads show it more clearly.
---

Your AI laptop's NPU benchmarks look great in reviews, but on your machine AI features feel sluggish — Studio Effects stutter, Recall indexing crawls, or local AI apps run slower than expected. Virtualization-based Security and Core Isolation are a likely suspect: they insert a virtualization layer between Windows and the hardware, and NPU workloads that make frequent driver calls pay overhead on every crossing.

The catch is that VBS also protects you. Turning it off for a speed gain you have not measured is a bad trade. The right approach is to measure the impact first, fix the drivers that make the overhead worse, and only then decide whether the security tradeoff is worth it.

This guide walks that path: measure, update, tune, and decide — in that order.

## Why this happens

- **Virtualization overhead on NPU driver calls:** Every NPU operation that crosses the VBS isolation boundary costs extra cycles. Workloads with many small driver calls suffer more than batch-heavy ones.
- **Outdated NPU driver with poor VBS compatibility:** Early NPU drivers were not optimized for running under VBS, so the same workload costs more overhead than with a current driver.
- **Memory Integrity forcing driver validation:** Memory Integrity validates drivers at load and runtime, adding checks that slow driver initialization and some operations.
- **Hypervisor overhead on shared resources:** VBS reserves CPU and memory resources for its secure environment, leaving slightly less for the NPU driver and AI apps.
- **Firmware without VBS optimizations:** Older BIOS versions may lack virtualization optimizations that reduce the cost of VBS on newer processors.
- **Conflicting virtualization features:** Hyper-V, Windows Sandbox, and other virtualization features stack with VBS, multiplying overhead for workloads that use them alongside the NPU.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure whether VBS is actually your bottleneck

Do not change security settings on a hunch. A before-and-after measurement tells you whether VBS matters at all on your workload.

1. Pick a repeatable NPU workload — a Studio Effects session, a local AI app benchmark, or a timed Recall indexing task.
2. Run it with VBS in its current state and record the time or frame rate.
3. Check whether VBS is on by opening **System Information** and looking for **Virtualization-based security** status.
4. Note your NPU driver version from Device Manager so you can compare after updates.
5. If the workload is already fast, VBS is not your problem — look at app settings or thermals instead. If it is slow, continue to the driver fixes. Security-feature interactions like this also appear in [Smart App Control blocking cases](/articles/smart-app-control-blocking-arm-apps-fix/) on the same machines.

### Fix 2: Update the NPU driver and BIOS

Driver and firmware updates are the highest-value fix because they reduce VBS overhead without touching security at all.

1. Download the latest NPU and chipset drivers for your exact model from your laptop maker's support page.
2. For Intel systems, also check [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for newer NPU and chipset packages.
3. Install the chipset driver first, then the NPU driver, and restart.
4. Check your maker's support page for a BIOS update mentioning virtualization or VBS, and install it on AC power.
5. Re-run your benchmark from Fix 1 and compare — a current driver often recovers most of the VBS overhead.

### Fix 3: Update Windows and the AI app itself

Windows builds and AI apps both improve their VBS behavior over time. A stale build can carry overhead that newer versions eliminated.

1. Open **Settings > Windows Update** and install all pending updates.
2. Update the AI app in question through the Microsoft Store or the developer's site.
3. Restart and re-run your benchmark to see whether the update alone closed the gap.
4. If the app offers a performance or quality setting for NPU features, try lowering it one notch — the visual difference is often small while the speed gain is large.
5. Record the new numbers so you have a baseline for the tuning steps below.

### Fix 4: Tune Memory Integrity and virtualization features

Before turning anything off, reduce the stacked virtualization load. Fewer active virtualization features means less overhead for the NPU.

1. Open **Settings > Privacy & security > Windows Security > Device security > Core isolation details**.
2. Note the current Memory Integrity setting, but do not change it yet.
3. Turn off virtualization features you do not use — Hyper-V, Windows Sandbox, or Virtual Machine Platform — in **Turn Windows features on or off**.
4. Restart and re-run your benchmark to measure the effect of the reduced stack.
5. If performance recovers enough, stop here — you kept full Memory Integrity protection while removing unnecessary overhead.

### Fix 5: Make an informed decision about Memory Integrity

Only reach this step if measurements prove VBS is the bottleneck and driver updates did not fix it. This is a genuine security tradeoff, so decide deliberately.

1. Review your benchmark numbers from Fixes 1 through 4 — you need proof the gain is real and worth the tradeoff.
2. Consider your threat model: a laptop handling sensitive work benefits more from Memory Integrity than a test machine does.
3. If you decide to proceed, turn off Memory Integrity in **Core isolation details** and restart.
4. Re-run your benchmark to confirm the gain, and record both the gain and the date so you can revisit the decision later.
5. Re-enable Memory Integrity after any major Windows update or driver update, then re-measure — newer drivers may have eliminated the overhead that justified turning it off.

### Fix 6: Optimize the workload itself for VBS environments

If you keep VBS on, workload design can reduce the overhead without any security change.

1. Prefer batch processing over many small NPU calls where the app allows it — fewer driver crossings mean less overhead.
2. Close other AI apps competing for the NPU during heavy workloads, since contention amplifies VBS overhead.
3. Keep the laptop on AC power with the best-performance power mode during AI benchmarks and heavy tasks.
4. Check the app's settings for a GPU fallback option and test whether GPU inference is faster than NPU inference under VBS for your specific task.
5. If NPU performance remains unacceptable with VBS on and current drivers, document your measurements and report them to your laptop maker — driver teams prioritize VBS overhead fixes with real data. For general guidance, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) and related [ChatGPT app issues](/articles/chatgpt-app-windows-arm-issues-fix/) on ARM laptops.

## Closing

VBS and Core Isolation can slow NPU workloads, but the size of the slowdown depends on your driver, firmware, and workload — so measure first. Update the NPU driver and BIOS, trim unused virtualization features, and only consider turning off Memory Integrity when measurements prove it is the bottleneck and the gain justifies the security cost. Most users recover acceptable performance without ever touching the security setting. If this fix did not fully resolve the issue, related troubleshooting for [Lenovo Thinkpad X9 Aura Ai Issues](/articles/lenovo-thinkpad-x9-aura-ai-issues-fix/) and [Copilot Quick View Not Opening](/articles/copilot-quick-view-not-opening/) covers neighboring causes that can produce the same symptom on AI laptops.
