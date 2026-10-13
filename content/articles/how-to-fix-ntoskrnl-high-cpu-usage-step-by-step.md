---
title: "How to Fix Ntoskrnl High CPU Usage: Step-by-Step Guide"
slug: how-to-fix-ntoskrnl-high-cpu-usage-step-by-step
date: 2026-10-07
categories: ["performance"]
tags: ["ntoskrnl", "high cpu", "kernel", "drivers"]
description: "A complete step-by-step guide to ntoskrnl.exe high CPU on any Windows laptop: measure with the right tools, find the guilty driver, and fix it."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-high-cpu-usage-step-by-step.webp"
faqs:
  - q: "What exactly is ntoskrnl.exe?"
    a: "Ntoskrnl.exe (NT OS Kernel) is the heart of Windows — it manages memory, scheduling, hardware abstraction, and runs all kernel-mode drivers. In Task Manager it appears as the 'System' process (PID 4). Because drivers execute inside the kernel's context, their CPU time is billed to System/ntoskrnl. So 'ntoskrnl high CPU' really means 'some driver or hardware issue is making the kernel work overtime' — the kernel itself is just the messenger."
  - q: "How do I find which driver is causing ntoskrnl CPU usage?"
    a: "Use LatencyMon (free): run it as Administrator for 10-15 minutes during the problem, then check the Drivers tab sorted by DPC count and execution time — the top entry is your culprit. For deeper analysis, Windows Performance Recorder (WPR) with the CPU profile plus Windows Performance Analyzer (WPA) shows per-driver kernel time precisely. Both tools ship clarity that Task Manager can't."
  - q: "Is it safe to use Driver Verifier for this?"
    a: "Driver Verifier is powerful but risky — it intentionally crashes the system (blue screen) when a monitored driver misbehaves, which is how it identifies the culprit. Only use it if you can recover from a boot loop (know how to reach Safe Mode or WinRE), verify one or two suspect drivers at a time, and turn it off immediately after capturing the crash. For most users, LatencyMon is the safer first tool."
  - q: "Can Windows Update cause ntoskrnl high CPU?"
    a: "Indirectly, yes — in two ways. First, a feature update can install a buggy driver version (Windows Update's driver offerings lag vendor releases and occasionally ship problematic ones). Second, the update process itself (TiWorker, driver migration) temporarily inflates kernel activity. If ntoskrnl spikes began right after an update, check Device Manager for freshly-updated drivers and roll back the suspects."
---

Ntoskrnl.exe high CPU sends people down rabbit holes because the obvious target — the kernel itself — can't be fixed, uninstalled, or ended. But here's the liberating truth: the kernel is never the actual problem. It's the accountant, billing CPU time to itself for work done by kernel-mode drivers and hardware interrupts on its behalf. So this guide is a genuine step-by-step diagnostic: measure precisely, name the guilty driver, fix or replace it, and verify. (For HP-specific driver paths, see our [HP ntoskrnl guide](/articles/how-to-fix-ntoskrnl-high-cpu-usage-on-hp-laptop/); for interrupt-side issues, [System Interrupts](/articles/how-to-fix-system-interrupts-high-cpu-windows-11-step-by-step/) covers that.)

## Why this happens

- **A buggy driver burning DPC time**: Network, audio, or storage drivers with excessive Deferred Procedure Calls.
- **Interrupt storms**: Failing hardware flooding the kernel with interrupts.
- **Memory pressure forcing kernel work**: Heavy paging and compressed-memory management at kernel level.
- **Filter drivers stacking up**: Antivirus, VPN, and backup filter drivers multiplying per-I/O cost.
- **BIOS/firmware power-state bugs**: Broken ACPI handling making the kernel spin on idle transitions.
- **Corrupt pagefile or hibernation data**: Damaged virtual memory structures causing kernel retry loops.
- **Hypervisor/VBS overhead**: Virtualization-based security adding kernel cost on some configurations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Baseline the problem properly

Get clean measurements before touching anything.

1. Open **Task Manager** > **Details** and confirm **System** (PID 4, image name `ntoskrnl.exe` shown in some views) holds sustained CPU — record the percentage at idle, light use, and heavy use.
2. Distinguish from **System Interrupts** (separate pseudo-process): interrupts = hardware signaling; System = kernel/driver execution. Note both values.
3. Boot into **Safe Mode** (minimal drivers): if System CPU normalizes, it's a third-party driver; if still high, it's a Windows driver, filter, or hardware.
4. Run `powercfg /energy` elevated and `powercfg /sleepstudy` — the reports flag devices and drivers with abnormal CPU/wake activity by name.
5. Record your baseline in a note — you'll compare against it after each fix to know what actually worked.

### Fix 2: Identify the driver with LatencyMon

The single most useful step in this entire guide.

1. Download **LatencyMon** (Resplendence, free) and run it **as Administrator** — standard user misses kernel data.
2. Click play and let it sample for **10–15 minutes** while the high CPU is occurring (use the laptop normally).
3. Open the **Drivers** tab, sort by **DPC count** and then **ISR count** — the driver with overwhelmingly high counts is your prime suspect. Note its filename (e.g., `ndis.sys`-based miniport, `storport` miniport, `HDAudBus`-related).
4. Check the **Processes** and **Stats** tabs for corroboration — the highest hard pagefault and DPC execution times should point the same direction.
5. Write down the exact driver filename — Fix 3 maps it to a device and an update.

### Fix 3: Update, roll back, or replace the guilty driver

Act on what LatencyMon named.

1. Map the filename to hardware: `ndis`-family = network adapter, `stor`/`nvme` = storage controller, `HDA`/`RTK` = audio, `USB` = USB controller. **Device Manager** > **View** > **Devices by connection** helps confirm.
2. Update from the best source in order: **laptop maker's support page** (matched, tested drivers) → **chip vendor** (Intel [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA/AMD direct) → Windows Update (last resort for drivers).
3. If the problem started with a recent driver update, **roll back**: Device Manager > device > Properties > Driver > Roll Back Driver.
4. For network drivers specifically, try both the maker's version and the chip vendor's — Wi-Fi driver DPC bugs differ between builds, and one is usually clean.
5. Re-run LatencyMon after each change and compare against your Fix 1 baseline — only keep changes that measurably reduce kernel CPU.

### Fix 4: Strip filter drivers and conflicting software

Filters multiply every I/O's kernel cost.

1. List filter drivers: in elevated Command Prompt, `fltmc filters` shows file-system minifilters (antivirus, backup, sync tools) — each adds kernel overhead per operation.
2. Temporarily uninstall (not just disable) third-party antivirus, VPN clients, and backup tools one at a time, rebooting and re-measuring with LatencyMon between each.
3. Keep only one real-time antivirus — stacked AV products are a classic ntoskrnl inflator.
4. Check **Device Manager** > **View** > **Show hidden devices** for ghosted/duplicate devices (grayed out) — uninstall them; phantom devices generate interrupt and DPC noise.
5. Reinstall your chosen security software last, from a current installer — old AV filter drivers are disproportionately represented in DPC-latency complaints.

### Fix 5: Update BIOS and check firmware-level causes

The kernel talks to firmware constantly; buggy firmware wastes its time.

1. Check your current BIOS version (`msinfo32` > BIOS Version/Date) against the maker's support page — update if behind, following the maker's instructions exactly (AC power, no interruptions).
2. In BIOS/UEFI setup, look for **Intel VMD**, **ACPI settings**, and **power management** options — try defaults if they've been tweaked; exotic settings cause ACPI spin loops.
3. Disable **Memory integrity** temporarily (Windows Security > Device security > Core isolation) as a test — VBS/HVCI adds kernel overhead that amplifies a marginal driver's cost. Re-enable after testing unless it's clearly the multiplier.
4. If the laptop has a **MUX switch** or GPU mode setting, test both positions — hybrid graphics handoff bugs show up as kernel CPU.
5. After BIOS updates, re-run LatencyMon — firmware fixes for DPC latency are common in changelogs ("improved system stability").

### Fix 6: Verify hardware and repair Windows

When no driver explains it.

1. Run **Windows Memory Diagnostic** and your maker's **UEFI hardware diagnostics** (memory, drive, fans) — hardware faults are the remaining explanation after drivers are clean.
2. Test storage: `chkdsk C: /scan` plus S.M.A.R.T. data — a struggling drive's interrupt load lands on the kernel.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — repairs kernel components themselves.
4. As a diagnostic nuclear option, **clean-install Windows** from the [Windows 11 ISO](https://www.microsoft.com/en-us/software-download/windows11) with only maker drivers — if ntoskrnl is still high on a clean install, it's definitively hardware.
5. Document your findings (guilty driver, BIOS version, LatencyMon numbers) — if it's a warranty claim, this evidence gets you past first-line support instantly. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers the built-in diagnostic tools referenced here.

## Closing

Ntoskrnl high CPU is a measurement problem with a driver answer: baseline it, name the driver with LatencyMon, update or replace that driver, strip conflicting filters, and check firmware. Follow the steps in order and the kernel stops looking guilty — because it never was.
