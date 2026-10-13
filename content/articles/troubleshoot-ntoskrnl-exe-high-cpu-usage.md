---
title: "Troubleshooting ntoskrnl.exe High CPU: Kernel-Level Diagnostics That Work"
slug: troubleshoot-ntoskrnl-exe-high-cpu-usage
date: 2026-10-04
categories: ["performance"]
tags: ["ntoskrnl.exe", "troubleshooting", "kernel", "process explorer", "driver diagnostics"]
description: "Go beyond Task Manager: use Process Explorer, WPA, and poolmon-style checks to find exactly which driver or kernel subsystem is driving ntoskrnl.exe CPU usage."
thumbnail: "/images/thumbs/troubleshoot-ntoskrnl-exe-high-cpu-usage.webp"
faqs:
  - q: "How can I see which driver inside ntoskrnl.exe is using CPU?"
    a: "Task Manager only shows the System process as a whole. Use Process Explorer from Microsoft Sysinternals: run it as administrator, double-click System, open the Threads tab, and sort by CPU. Each thread's start address names its owner — ntoskrnl.exe functions with Mm or Mi prefixes mean memory management, while a third-party .sys filename points directly at the responsible driver. That name is your investigation target."
  - q: "What does it mean when ntoskrnl.exe threads show Mi or Mm functions?"
    a: "Mi and Mm prefixes are the Windows memory manager's internal functions. High CPU there means the kernel is doing memory work: compressing pages, handling page faults, trimming working sets, or servicing the pagefile. This almost always traces back to memory pressure — too little RAM for the workload — or a driver leaking memory and forcing the manager into expensive reclamation. Check Task Manager's memory figures alongside."
  - q: "Can Windows Performance Analyzer trace ntoskrnl.exe CPU usage?"
    a: "Yes, and it is the definitive tool for stubborn cases. Install the Windows Performance Toolkit, record a trace with wpr.exe -start CPU, reproduce the high usage for a few minutes, then stop with wpr.exe -stop trace.etl. Opening the trace in Windows Performance Analyzer and expanding the System process's CPU Usage (Sampled) table shows exactly which functions and drivers consumed the cycles, sampled across the whole recording."
  - q: "Is high System CPU after a Windows update normal?"
    a: "Temporarily, yes. After feature updates Windows runs the .NET native image optimizer, re-indexes files, re-baselines Defender, and compacts the component store — all kernel-heavy work that can keep the System process busy for hours. Give it 24 to 48 hours of plugged-in idle time. If System CPU is still elevated after two days with no pending updates, treat it as a real problem and start the diagnostic steps."
---

Task Manager tells you *that* ntoskrnl.exe is using CPU. It doesn't tell you *why*, and "why" is the entire troubleshooting problem — because ntoskrnl.exe is the kernel, and the kernel does work on behalf of dozens of subsystems. The System process at 25% CPU could be memory compression, a leaking driver, interrupt handling, file-system filtering, or virtualization overhead. Each has a different fix, and guessing between them wastes days.

This guide is the diagnostic deep-dive: the tools and techniques that decompose that single "System" number into its real components. You'll use Process Explorer for quick thread-level answers, the Windows Performance Toolkit for definitive traces, and a few targeted checks (pool usage, DPC correlation, memory pressure) that narrow the field fast. Pair it with the straight fix guide [how to fix ntoskrnl.exe high CPU](/articles/how-do-i-fix-ntoskrnl-exe-high-cpu-usage/) once you know your culprit.

## Why this happens

- **Memory manager thrashing under pressure**: Page compression, trimming, and fault handling scale with how overcommitted RAM is.
- **Kernel pool leaks from buggy drivers**: A driver allocating nonpaged pool and never freeing it forces expensive scavenging.
- **File-system filter drivers stacking up**: Antivirus, backup, and sync tools chain filters that each add kernel CPU per file operation.
- **Interrupt and DPC load billed to System**: Heavy interrupt handling shows up under the System process, not the device's driver.
- **Registry and object-manager churn**: Misbehaving software hammering the registry or creating objects in a loop.
- **Virtualization-based security**: Hypervisor-protected code integrity and memory integrity add per-operation kernel cost.
- **WMI provider abuse**: A broken WMI provider or a monitoring tool polling WMI aggressively burns kernel cycles.
- **Post-update servicing storms**: Component store cleanup, driver staging, and migration tasks running for days after a feature update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Decompose the System process with Process Explorer

Five minutes here replaces hours of guessing.

1. Download **Process Explorer** from Microsoft Sysinternals and run it **as administrator** (required to see kernel thread details).
2. Double-click the **System** process, go to the **Threads** tab, click the **CPU** column header twice to sort descending, and watch for 30 seconds.
3. Read the **Start Address** column: `ntoskrnl.exe!Mi...` or `!Mm...` = memory manager; `!Ke...` = scheduler/interrupts; a name like `ndis.sys`, `storport.sys`, or a vendor `.sys` = that driver directly.
4. Click **Stack** on the top thread for the full call stack — it shows the exact code path, e.g., memory compression routines vs. a driver's dispatch routine.
5. Write down the top two or three owners. If they're all memory-manager functions, your investigation is about RAM pressure and leaks (Fix 2). If a third-party driver dominates, jump to Fix 4.

### Fix 2: Quantify memory pressure and hunt leaks

Memory-manager CPU almost always means the RAM situation is bad.

1. In Task Manager > **Performance** > **Memory**, record four numbers: **In use**, **Available**, **Committed**, and **Paged/Non-paged pool**.
2. Non-paged pool above ~1 GB on a 16 GB system (or growing without bound) is the classic driver-leak signature — non-paged pool can only be allocated by kernel drivers.
3. To find the leaking driver, enable pool tagging: open an elevated prompt and run `verifier /flags 0x1 /driver <suspect.sys>` only if you have a suspect; for general hunting, the `poolmon` technique (documented in Microsoft's driver docs, linked from the [Windows support hub](https://support.microsoft.com/en-us/windows)) shows per-tag allocations.
4. A simpler practical test: reboot, note non-paged pool, use the laptop normally for a few hours, and check again. Growth of hundreds of MB with no new apps points at a driver loaded at boot — often network, VPN, or RGB/utility drivers.
5. For plain overcommitment (no leak, just too much running), the fixes are reducing load — see [fixing high memory usage](/articles/windows-11-high-memory-usage-fix/) — or adding physical RAM.

### Fix 3: Capture a definitive trace with Windows Performance Recorder

When thread inspection isn't conclusive, record the truth.

1. Install the **Windows Performance Toolkit** (part of the Windows ADK, or via the Microsoft Store's performance tools package).
2. Open an elevated Command Prompt and run `wpr.exe -start CPU -start DiskIO -start FileIO` to begin recording.
3. Reproduce the high System CPU for **3-5 minutes** of representative use — don't just stare at the desktop; do the work that triggers it.
4. Stop with `wpr.exe -stop C:\trace.etl` and open the file in **Windows Performance Analyzer (WPA)**.
5. In WPA, open **CPU Usage (Sampled)** > expand the **System** process > group by **Stack**: the hottest stacks name the exact functions and drivers. This is the same technique Microsoft support engineers use, and it ends arguments about what's "really" using the CPU.

### Fix 4: Neutralize the identified driver

A named driver is an actionable driver.

1. With the driver file name from Fix 1 or Fix 3 (e.g., `rtwlanu.sys`, `iaStorAC.sys`), find its device in **Device Manager** and check the driver version and date.
2. Get the replacement from your laptop maker's support page — Dell, HP, Lenovo — matched to your exact model, since OEMs validate interrupt and power behavior per machine.
3. If the problem began with a recent driver update, **Roll Back Driver** from the device's Driver tab instead.
4. For network drivers, also try the chip vendor's latest (Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)) — wireless drivers are the most frequent kernel-CPU offenders.
5. Re-measure with Process Explorer after the change: the offending thread's CPU should collapse. If a *different* driver rises to take its place, you had stacked causes — repeat the loop.

### Fix 5: Strip filter drivers and background agents

Filters multiply kernel work on every file operation.

1. List filter drivers: run `fltmc` in an elevated prompt — every third-party entry (antivirus, backup, cloud sync, disk tools) adds per-I/O kernel CPU.
2. Temporarily uninstall (not just disable) non-essential filter owners one at a time — backup tools, "PC optimizers," duplicate antivirus products — rebooting and re-measuring between each.
3. Check **Autoruns** (Sysinternals) > **Drivers** tab for unsigned or stale drivers loading at boot; uncheck suspects to test (Autoruns lets you re-enable safely).
4. Audit WMI abuse: in WPA traces or Process Explorer, `wmiprvse.exe` CPU alongside System CPU suggests a polling loop — often a monitoring gadget or vendor utility. Remove or update the polling app.
5. Re-run `fltmc` afterward to confirm the stack is clean, and keep only one antivirus filter active.

### Fix 6: Rule out servicing storms and hardware faults

Last checks before concluding it's environmental.

1. **Settings** > **Windows Update** > **Update history**: if a feature update landed in the last 48 hours, give servicing time — check Task Manager for `TiWorker.exe` or `ngen` activity correlating with System CPU.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt to eliminate corruption as a contributor.
3. Test hardware: **Windows Memory Diagnostic** for RAM, CrystalDiskInfo for SMART health — faults in either force kernel error-handling paths to run hot.
4. If System CPU stays high on a clean Windows install (from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)) with only vendor drivers, suspect hardware: a failing SSD's retry storms and marginal RAM both present as kernel CPU.
5. Document your findings (driver name, pool numbers, trace file location) — if you end up opening a support case with your laptop maker, this evidence gets you past tier-one scripts immediately.

## Closing

The System process is a black box only if you never open it. Process Explorer's Threads tab answers most ntoskrnl.exe cases in minutes; WPA traces answer the rest definitively. Once you can name the subsystem — memory manager, a specific driver, a filter stack — the fix is usually straightforward and permanent. Keep these tools installed: kernel-level CPU issues recur with driver updates, and a two-minute thread check beats a weekend of guesswork every time.
