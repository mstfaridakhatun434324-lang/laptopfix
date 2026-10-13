---
title: "How to Fix Ntoskrnl High CPU Usage on an HP Laptop"
slug: how-to-fix-ntoskrnl-high-cpu-usage-on-hp-laptop
date: 2026-09-24
categories: ["performance"]
tags: ["ntoskrnl", "high cpu", "hp laptop", "kernel"]
description: "Ntoskrnl.exe eating CPU on your HP laptop? Since it's the Windows kernel itself, the real culprit is a driver or hardware issue underneath — here's how HP owners track it down."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-high-cpu-usage-on-hp-laptop.webp"
faqs:
  - q: "What is ntoskrnl.exe and can I disable it?"
    a: "Ntoskrnl.exe is the Windows kernel — the core of the operating system that manages memory, processes, and hardware. You cannot and must not disable or end it; doing so would crash Windows instantly. High CPU attributed to ntoskrnl almost never means the kernel itself is broken — it means a driver running in kernel mode is misbehaving, and the kernel gets blamed in Task Manager because the driver executes on its behalf."
  - q: "Why does ntoskrnl use more CPU on HP laptops specifically?"
    a: "HP laptops ship with HP-specific drivers (chipset, audio, network, power management) and utilities like HP Support Assistant and HP Wolf Security that install kernel-mode components. If any of these drivers has a bug — an interrupt storm from the Wi-Fi driver is a classic — the CPU time shows up under ntoskrnl's 'System' process. Updating HP drivers from HP's official support site resolves most HP-specific cases."
  - q: "Is ntoskrnl high CPU a sign of failing hardware?"
    a: "Sometimes. Failing RAM (causing constant error correction), a dying drive generating interrupt storms, or overheating (causing thermal throttling that the kernel manages) all inflate ntoskrnl CPU. Before assuming hardware failure, rule out drivers — but if ntoskrnl stays high in Safe Mode or a clean Windows install, hardware diagnostics (HP's built-in UEFI diagnostics) are the next step."
  - q: "How is ntoskrnl different from System Interrupts?"
    a: "They're related but distinct: 'System Interrupts' represents time the CPU spends servicing hardware interrupts, while ntoskrnl's 'System' process includes kernel-mode driver execution (DPCs — deferred procedure calls). A buggy driver shows up under System/ntoskrnl; a chatty or failing hardware device shows up under System Interrupts. LatencyMon distinguishes them precisely."
---

Seeing `System` (ntoskrnl.exe) at the top of Task Manager with 20–50% CPU is uniquely frustrating, because you can't just end the process or uninstall it — it *is* Windows. The kernel doesn't burn CPU for fun, though. When ntoskrnl shows high usage, it's almost always taking the blame for something running in kernel mode on its behalf: a buggy driver, an interrupt storm from hardware, or failing components generating constant error handling. On HP laptops specifically, HP's own drivers and utilities are frequent contributors. For a generic step-by-step ntoskrnl walkthrough (any brand), see [our brand-neutral guide](/articles/how-to-fix-ntoskrnl-high-cpu-usage-step-by-step/); for interrupt-specific issues, [System Interrupts high CPU](/articles/how-to-fix-system-interrupts-high-cpu-windows-11-step-by-step/) covers the hardware side.

## Why this happens

- **Buggy HP drivers in kernel mode**: Wi-Fi, audio (Realtek/Conexant), and chipset drivers executing badly inside the kernel.
- **DPC latency from a bad driver**: Deferred Procedure Calls from one driver monopolize kernel time.
- **Interrupt storms from failing hardware**: A dying drive or flaky USB device floods the kernel with interrupts.
- **Memory errors forcing kernel work**: Bad RAM triggers constant error correction handled at kernel level.
- **HP utilities' kernel components**: HP Support Assistant, HP Wolf Security, and Sure Sense install drivers that can misbehave.
- **Outdated BIOS/firmware**: Old BIOS versions mishandle power states, causing the kernel to spin on ACPI operations.
- **Corrupt system files**: Damaged kernel-mode components after a bad update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's really the kernel, not a misreading

Make sure Task Manager isn't misleading you before diving into drivers.

1. Open **Task Manager** > **Details** tab and confirm the process is **System** (PID 4) with sustained high CPU — not a similarly-named user process.
2. Check the **Performance** tab: if CPU is high but the System process is low, the real consumer may be **System Interrupts** (a separate pseudo-process) — different fix path.
3. Note whether it's constant or spiky: constant 20%+ suggests a driver loop; spikes tied to Wi-Fi activity, audio playback, or USB use point at those drivers.
4. Boot into **Safe Mode** (Settings > Recovery > Advanced startup): if System CPU is normal there, it's a third-party driver — if it's still high, suspect Windows drivers or hardware.
5. Run `powercfg /energy` from an elevated prompt and check the report for devices with excessive CPU wake activity — it names the misbehaving device.

### Fix 2: Update HP drivers from the official source

The single most effective fix for HP laptops.

1. Go to [HP's official support site](https://support.hp.com/us-en), enter your exact model or serial number, and open the **Drivers** section.
2. Prioritize in this order: **BIOS**, **chipset**, **network (Wi-Fi/Ethernet)**, **audio**, then **graphics** — these are the kernel-mode drivers that inflate ntoskrnl.
3. Install the BIOS update first (on AC power, battery charged, nothing else running), then chipset, then the rest — rebooting between major ones.
4. Alternatively, open **HP Support Assistant** > **Updates** and install everything it offers, but cross-check versions against the website — Support Assistant sometimes lags.
5. After updating, monitor Task Manager for an hour of normal use: a driver fix shows up as System CPU dropping to low single digits at idle.

### Fix 3: Identify the guilty driver with LatencyMon

Stop guessing which driver — measure it.

1. Download **LatencyMon** (Resplendence, free) and run it as Administrator for 10–15 minutes during the high-CPU condition.
2. Check the **Drivers** tab sorted by **DPC count** and **Execution time** — the top driver is your prime suspect (common names: `ndis.sys` wrappers, `storport` miniports, audio drivers like `RTKVHD64.sys`).
3. Also check the **Processes** tab — it breaks down kernel time per driver more precisely than Task Manager.
4. Once identified, update that specific driver from HP's site or the chip vendor (Intel/Realtek). If it's already current, try the previous version — new drivers introduce bugs too.
5. If LatencyMon shows `ntoskrnl.exe` itself at the top with no driver standing out, the issue is likely hardware interrupts — move to Fix 5.

### Fix 4: Clean up HP utilities and kernel-mode extras

HP's bundled software installs drivers you may not need.

1. Open **Settings** > **Apps** > **Installed apps** and review HP entries: HP Support Assistant, HP Wolf Security, HP Sure Sense, HP Audio Switch.
2. Keep **HP Support Assistant** (useful for driver updates) but disable its automated scans/schedules if they coincide with CPU spikes — run it manually monthly instead.
3. If you don't use HP Wolf Security/Sure Sense features, uninstall them — their real-time kernel hooks add overhead and have had buggy releases.
4. Check **Task Scheduler** for HP tasks that run at logon and disable non-essential ones (telemetry, "optimization" helpers).
5. Reboot and compare System CPU at idle — removing one bad kernel hook can drop ntoskrnl usage dramatically. HP documents these utilities on [hp.com support](https://support.hp.com/us-en) if you need reinstallers later.

### Fix 5: Test the hardware underneath

If drivers don't explain it, the hardware might.

1. Restart and press **F2** (or **Esc** > **F2**) to enter **HP UEFI Diagnostics** — run the **System** > **Extensive** test, especially memory and drive checks.
2. Pay attention to the drive: run `chkdsk C: /scan` from an elevated prompt and check S.M.A.R.T. data — a failing drive's interrupt storms show up as ntoskrnl CPU.
3. Test RAM with **Windows Memory Diagnostic** — memory errors force the kernel into constant correction work.
4. Disconnect all USB devices and disable Wi-Fi/Bluetooth temporarily — if System CPU drops, a peripheral or its driver is the storm source; reintroduce one at a time.
5. Check thermals: overheating causes the kernel's thermal management to throttle aggressively — clean vents and confirm fans run; HP's UEFI diagnostics include fan tests.

### Fix 6: Repair Windows' own kernel components

When the OS itself is damaged rather than the drivers.

1. Run `sfc /scannow` from an elevated Command Prompt, then `DISM /Online /Cleanup-Image /RestoreHealth` — repairs the kernel files SFC protects.
2. Check **Windows Update** for pending updates — Microsoft ships kernel and driver-compatibility fixes in cumulative updates.
3. If high ntoskrnl started right after a feature update, use **Settings** > **Recovery** > **Go back** (within 10 days) or reinstall the update cleanly.
4. As a diagnostic, perform an **in-place upgrade** with the [Windows 11 ISO](https://www.microsoft.com/en-us/software-download/windows11) (keep files/apps) — this refreshes all system files without a full wipe.
5. If ntoskrnl is still high after a clean Windows install with HP drivers, it's hardware — contact HP support with your diagnostics results in hand.

## Closing

Ntoskrnl high CPU is the kernel taking the blame for a driver or hardware problem underneath. On HP laptops, the fix path is almost always: update HP's drivers (BIOS and chipset first), identify the guilty driver with LatencyMon, trim HP's kernel-mode utilities, and test the hardware if drivers don't explain it. The kernel itself is fine — find what's making it work so hard.
