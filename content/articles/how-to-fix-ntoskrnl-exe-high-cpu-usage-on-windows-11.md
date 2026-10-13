---
title: "Ntoskrnl.exe High CPU on Windows 11? Diagnose and Fix It"
slug: how-to-fix-ntoskrnl-exe-high-cpu-usage-on-windows-11
date: 2026-09-01
categories: ["performance"]
tags: ["ntoskrnl.exe high cpu", "windows 11", "system process cpu", "kernel cpu usage"]
description: "Ntoskrnl.exe (System) eating CPU on Windows 11? Learn what the kernel process is doing and trace it to the driver or setting responsible."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-exe-high-cpu-usage-on-windows-11.webp"
faqs:
  - q: "What is ntoskrnl.exe and is it safe?"
    a: "Ntoskrnl.exe is the Windows kernel itself — the core of the operating system, shown in Task Manager as the System process. It is completely legitimate and essential; Windows cannot run without it. High CPU from ntoskrnl.exe does not mean the kernel is broken — it means some driver or hardware activity is making heavy use of kernel services. You should never try to delete, block, or disable it; the fix is always finding what is driving it."
  - q: "Why does ntoskrnl.exe use CPU even when I'm not doing anything?"
    a: "The kernel does work on behalf of drivers and hardware: servicing interrupts, managing memory compression, handling network and storage I/O, and running deferred procedure calls. On an idle system this should total under 2-3% CPU. When it is much higher at idle, a driver is typically stuck in a loop — polling hardware, retrying failed operations, or mishandling power-state transitions — and every one of those operations runs inside ntoskrnl.exe's CPU accounting."
  - q: "Can Windows Update cause ntoskrnl.exe high CPU?"
    a: "Yes, in two ways. Feature updates can install driver versions with kernel-level bugs (network and storage drivers are the classic offenders), and updates can change power-management behavior that exposes firmware bugs. If ntoskrnl.exe CPU spiked immediately after an update, check Device Manager for driver dates matching the update and roll back or update the network, storage, and chipset drivers first — that resolves most update-triggered cases."
  - q: "How is ntoskrnl.exe different from System Interrupts?"
    a: "Both represent kernel-mode CPU time, but they account differently: System Interrupts counts time servicing hardware interrupts (ISR time), while ntoskrnl.exe/System includes deferred procedure calls (DPCs), memory management, and other kernel work done on drivers' behalf. In practice they often rise together from the same root cause — a misbehaving driver. Tools like LatencyMon and Windows Performance Analyzer break down which driver is responsible regardless of which label Task Manager shows."
---

Task Manager shows a process called System — ntoskrnl.exe, the Windows kernel — consuming 15, 25, or 40 percent of your CPU, and there is nothing to end, nothing to uninstall, nothing to click. It feels like the operating system itself has turned against you. In reality, the kernel is just the messenger: some driver or hardware condition is generating enormous amounts of kernel-mode work, and ntoskrnl.exe is where that work gets billed.

Fixing it means identifying the driver behind the kernel load, which takes proper tools rather than guesswork. This Windows 11 guide walks through that diagnosis. For the Windows 10 version of this problem, see [ntoskrnl.exe high CPU on Windows 10](/articles/how-to-fix-ntoskrnl-exe-high-cpu-usage-on-windows-10/); for the Lenovo-specific angle, [ntoskrnl high CPU on Lenovo laptops](/articles/how-to-fix-ntoskrnl-high-cpu-usage-on-lenovo-laptop/).

## Why this happens

- **Buggy network drivers**: Wi-Fi and Ethernet drivers with DPC bugs are the number one cause — the kernel does their deferred work.

- **Storage driver issues**: AHCI/NVMe driver problems generate constant kernel-mode error handling and retry loops.

- **Memory compression working overtime**: Windows compresses idle memory pages in kernel mode; with RAM pressure this becomes a major CPU consumer.

- **Corrupt system files**: Damaged kernel components or driver frameworks cause exception-handling loops inside ntoskrnl.exe.

- **Malware rootkits**: Kernel-mode rootkits hide inside the System process accounting, making ntoskrnl.exe the visible symptom of infection.

- **Faulty hardware generating errors**: Bad RAM or a failing drive forces the kernel's error-handling paths to run constantly.

- **Power management firmware bugs**: Broken ACPI implementations make the kernel poll hardware or mishandle sleep-state transitions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the scope and rule out idle-time illusions

Confirm ntoskrnl.exe is genuinely the problem and not a brief spike.

1. Open **Task Manager > Processes**, sort by CPU, and watch the **System** process for 5 minutes of normal use.
2. Check the **Details** tab too — ntoskrnl.exe appears as **System**; note its average, not just peaks.
3. Test at true idle: close all apps, wait 3 minutes, and check again — kernel CPU should drop under 3%.
4. If it only spikes during specific activities (large downloads, file copies), that activity's driver is suspect — note which one.
5. Restart the laptop and check early: high kernel CPU immediately after a clean boot points at a driver or service, not your apps.

### Fix 2: Identify the driver with LatencyMon or WPA

This is the pivotal step — it converts a mystery into a named driver file.

1. Download **LatencyMon** (Resplendence Software) and run it as administrator for 10 minutes.
2. Open the **Drivers** tab sorted by **DPC count** — the top entries are doing the kernel work billed to System.
3. Note the exact .sys filenames (e.g., ndis.sys wrappers, tcpip.sys, storport.sys, or vendor drivers).
4. For deeper analysis, use **Windows Performance Recorder** (part of the Windows ADK): record 60 seconds, open in **Windows Performance Analyzer**, and examine the **DPC/ISR** tables by module.
5. Write down the culprit driver — every remaining fix targets it.

### Fix 3: Update or roll back the culprit driver

Most ntoskrnl.exe cases end here: the driver was buggy or mismatched.

1. In **Device Manager**, locate the device owning the culprit driver (network adapter, storage controller, etc.).
2. First try **Update driver > Search automatically**; then get the latest from the manufacturer (Intel/Realtek/Killer for network, laptop maker for storage).
3. If the problem started after a driver update, use **Properties > Driver > Roll Back Driver** instead.
4. For network culprits specifically, try disabling advanced features in the adapter's **Advanced** tab (Large Send Offload, interrupt moderation toggles) as a test.
5. Re-run LatencyMon after each driver change to confirm the DPC counts actually dropped — verify, don't assume.

### Fix 4: Check memory pressure and compression

On RAM-starved systems, the kernel's memory compression alone can explain high System CPU.

1. Open **Task Manager > Performance > Memory** and check both usage percentage and the **Compressed** figure.
2. If memory sits above 85% with a large compressed pool, RAM pressure is driving kernel work — close heavy apps and retest.
3. In **Task Manager > Startup apps**, disable memory-hungry auto-starters you do not need.
4. As a diagnostic, you can disable memory compression temporarily in an elevated PowerShell: **Disable-MMAgent -mc** (re-enable with **Enable-MMAgent -mc**) — if System CPU collapses, RAM pressure was the cause.
5. The durable fix is reducing memory load or adding RAM; our [high RAM usage guide](/articles/windows-11-high-memory-usage-fix/) covers the full playbook.

### Fix 5: Scan for rootkits and repair system files

Kernel-mode malware hides in System's CPU accounting; corruption does the same via exception loops.

1. Run a **Microsoft Defender Offline scan** (**Windows Security > Virus & threat protection > Scan options**) — it boots outside Windows where rootkits cannot hide.
2. Follow with a second-opinion scan from a reputable on-demand scanner (Malwarebytes free).
3. In an elevated terminal, run **DISM /Online /Cleanup-Image /RestoreHealth** then **sfc /scannow** to repair kernel and driver-framework files.
4. Check **Event Viewer > Windows Logs > System** for repeated driver warnings or bugcheck entries correlating with the high CPU.
5. If the offline scan finds kernel-mode threats, follow its remediation fully and change passwords afterward — rootkits imply full compromise.

### Fix 6: Test hardware: RAM and drive

Failing hardware forces the kernel's error paths to run hot.

1. Run **Windows Memory Diagnostic** (search in Start) and let the extended test complete — bad RAM is a classic ntoskrnl.exe driver.
2. Check drive health with **CrystalDiskInfo**; reallocated or pending sectors mean the storage stack is error-handling constantly.
3. Run **chkdsk C: /f** from an elevated prompt to fix file-system issues contributing to kernel I/O load.
4. If you recently added hardware (RAM stick, SSD), remove it temporarily and test — new hardware with marginal compatibility causes exactly this.
5. Hardware faults confirmed by diagnostics need replacement; document the failing component for warranty or repair.

### Fix 7: Update BIOS and chipset drivers

Firmware-level power management bugs surface as kernel CPU that no driver update fixes.

1. Check your current BIOS version with **msinfo32**, then visit your laptop maker's support site for updates mentioning stability or power management.
2. Install the latest **chipset driver** from the maker or AMD/Intel — it governs how the OS talks to firmware about power states.
3. Flash BIOS on AC power with battery charged; do not interrupt the process.
4. After updating, reset BIOS to optimized defaults, then reapply only the settings you need (boot order, virtualization).
5. Re-run LatencyMon for a final verification. If kernel CPU remains high after clean drivers, clean OS files, healthy hardware, and current firmware, consider an in-place Windows repair install via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11). Microsoft documents kernel diagnostics further in the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Ntoskrnl.exe high CPU is the kernel doing someone else's expensive work — almost always a network or storage driver, sometimes RAM pressure or failing hardware. Identify the driver with LatencyMon, fix that driver, and the System process fades back to the 1-2% background hum it should be.
