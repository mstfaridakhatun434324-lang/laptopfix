---
title: "Ntoskrnl.exe High CPU on Windows 10? Diagnose and Fix It"
slug: how-to-fix-ntoskrnl-exe-high-cpu-usage-on-windows-10
date: 2026-09-02
categories: ["performance"]
tags: ["ntoskrnl.exe high cpu", "windows 10", "system process", "kernel high cpu"]
description: "System (ntoskrnl.exe) using high CPU on Windows 10? A practical diagnostic path to find the driver or hardware fault behind the kernel load."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-exe-high-cpu-usage-on-windows-10.webp"
faqs:
  - q: "Why is the System process using so much CPU on Windows 10?"
    a: "The System process is ntoskrnl.exe, the Windows kernel, and its CPU reflects kernel-mode work done for drivers and hardware: interrupt handling, deferred procedure calls, memory compression, and I/O processing. On Windows 10 the usual triggers are aging network or storage drivers never updated for newer cumulative updates, SysMain misbehaving on old hard drives, or update components grinding in the background. High System CPU is a symptom, never a kernel defect."
  - q: "Does Windows 10's memory compression cause high System CPU?"
    a: "It can, on systems short on RAM. Windows 10 compresses idle memory pages instead of writing them to the page file, and that compression runs in kernel mode billed to System. With 4GB of RAM and modern apps, compression works constantly and System CPU stays elevated. You can confirm by watching Task Manager's Memory page: high usage plus a large Compressed figure means the kernel is compressing frantically. The real fix is freeing RAM or adding more, not disabling compression."
  - q: "Can I end the System process to stop the CPU usage?"
    a: "No — Task Manager will not let you, and that is by design. System is the kernel; terminating it would crash Windows instantly. Any guide suggesting tools to kill or suspend System is dangerous misinformation. The correct approach is diagnosing which driver is generating the kernel load with tools like LatencyMon, then updating, rolling back, or replacing that driver. Treat System's CPU as a dashboard warning light, not as a process to manage."
  - q: "Is ntoskrnl.exe high CPU more common on older Windows 10 laptops?"
    a: "Yes, for several compounding reasons: older laptops often still run mechanical hard drives (which amplify SysMain and paging kernel work), their drivers stopped receiving updates years ago while Windows 10 cumulative updates kept changing the OS around them, and 4-8GB RAM configurations face more memory-compression load from modern browsers. If your Windows 10 laptop is aging, the fixes below still apply — but also weigh whether an SSD and RAM upgrade addresses the root causes more durably than software tweaks."
---

On Windows 10, the story is familiar: Task Manager's System process — ntoskrnl.exe, the kernel — sits at 20% CPU or more while you do nothing, the laptop runs warm, and nothing you close makes a dent. Because Windows 10 is now in its mature years, the causes skew toward aging drivers, update-component wear, and hardware that has seen better days.

The diagnostic approach is the same as on newer Windows: the kernel is billing someone else's work, so we find whose. This guide is tuned for Windows 10's specific quirks — SysMain on spinning disks, older driver stacks, and the update machinery. For Windows 11, see [ntoskrnl.exe high CPU on Windows 11](/articles/how-to-fix-ntoskrnl-exe-high-cpu-usage-on-windows-11/); for the related phantom process, [System Interrupts on Windows 10](/articles/how-to-fix-system-interrupts-high-cpu-on-windows-10/).

## Why this happens

- **Aging network drivers**: Wi-Fi/Ethernet drivers abandoned by vendors develop DPC bugs as Windows 10 cumulative updates change the kernel around them.

- **SysMain on mechanical drives**: On HDDs, SysMain's preloading generates heavy kernel I/O; on failing drives it becomes a constant storm.

- **Windows Update component grind**: The older servicing stack can get stuck retrying, with TiWorker and related processes driving kernel CPU for days.

- **Memory compression under RAM pressure**: 4-8GB systems compress memory constantly, all billed to the System process.

- **Storage driver mismatch**: Old AHCI drivers or Intel RST versions conflicting with newer Windows 10 builds.

- **Failing hardware**: Aging drives and RAM generate error interrupts and retries handled in kernel mode.

- **Leftover third-party drivers**: Old antivirus filter drivers, VPN clients, and virtualization tools hooking the kernel inefficiently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Establish the baseline and find the activity trigger

Windows 10's kernel load often ties to a specific subsystem; find the correlation first.

1. Open **Task Manager > Processes**, sort by CPU, and observe the **System** process over 5 minutes.
2. Test triggers one at a time: heavy network use, large file copies, and idle time — note which moves the System CPU needle.
3. Check **Task Manager > Performance > Memory** for the **Compressed** figure and overall pressure.
4. Open **Settings > Update & Security > Windows Update** — pending or stuck updates are a prime Windows 10 suspect.
5. Note whether high System CPU survives a clean boot (see Fix 6) — that single test splits software-vs-driver causes.

### Fix 2: Name the driver with LatencyMon

Guessing wastes hours; LatencyMon names the .sys file in minutes.

1. Download **LatencyMon** from Resplendence Software and run it elevated for 10 minutes of typical use.
2. Sort the **Drivers** tab by **DPC count** and **ISR count**; the leaders are your suspects.
3. Identify each top driver: network (ndis wrappers, vendor Wi-Fi .sys), storage (storahci, iaStor), or audio.
4. Cross-check with **Event Viewer > Windows Logs > System** for repeating warnings from the same driver.
5. Record the exact filenames — the next two fixes act on them directly.

### Fix 3: Update or replace the suspect drivers

On Windows 10, the newest driver is not always on Windows Update — go to the source.

1. For network culprits: download the latest driver from Intel, Realtek, or Killer's site (not just Windows Update) — vendor drivers for Windows 10 are often newer than Microsoft's catalog versions.
2. For storage culprits: try the standard Microsoft AHCI driver (**Device Manager > IDE ATA/ATAPI controllers > Update driver > Browse > Let me pick > Standard SATA AHCI Controller**) if a vendor driver is misbehaving, or vice versa.
3. For recently-updated-then-broken drivers: **Properties > Driver > Roll Back Driver**.
4. Uninstall third-party antivirus/VPN filter drivers you no longer use — their kernel hooks are a notorious Windows 10 System-CPU source; use vendor removal tools.
5. Re-run LatencyMon after each change to verify the driver's DPC counts dropped.

### Fix 4: Tame SysMain and Windows Update grind

Windows 10's background machinery is a heavier kernel citizen than on newer Windows.

1. Test SysMain: **services.msc > SysMain > Stop**, watch System CPU for 10 minutes; if it drops, set SysMain to **Disabled** (safe on SSDs; usually beneficial on HDDs too when it misbehaves).
2. Reset Windows Update components: elevated Command Prompt, **net stop wuauserv**, **net stop bits**, rename **C:\Windows\SoftwareDistribution** to **.old**, restart the services.
3. Run **Settings > Update & Security > Troubleshoot > Windows Update > Run the troubleshooter**.
4. Let pending updates fully install — a half-applied cumulative update keeps TiWorker grinding kernel CPU indefinitely.
5. Check **Task Scheduler > Microsoft > Windows > WindowsUpdate** for stuck tasks and disable any third-party updaters firing constantly.

### Fix 5: Relieve memory pressure

If compression is the kernel's main job, give it less to compress.

1. In **Task Manager > Startup** tab, disable everything non-essential to cut idle memory footprint.
2. Sort **Processes** by Memory and address the top consumers — browsers with many tabs, Electron apps, and old toolbars.
3. Check **System > Advanced system settings > Performance > Advanced > Virtual memory**: ensure the page file is **System managed**.
4. Consider readying a RAM upgrade: 8GB is the practical minimum for Windows 10 in 2026, 16GB the comfort zone — check your laptop's manual for upgradeability.
5. Our [RAM usage guide](/articles/windows-11-high-memory-usage-fix/) details the memory-trimming techniques that apply equally to Windows 10.

### Fix 6: Clean-boot to isolate third-party drivers

A clean boot strips the system to Microsoft's own drivers and services — the definitive split test.

1. Press **Win + R**, type **msconfig**, go to the **Services** tab, check **Hide all Microsoft services**, then **Disable all**.
2. In **Task Manager > Startup**, disable all startup items, then restart.
3. Check System CPU in the clean state: if it is normal, re-enable services in halves until the culprit half is found, then narrow item by item.
4. Pay special attention to old VPN clients, disk utilities, and RGB/fan control software — their kernel drivers age badly.
5. Once identified, update or uninstall the offending software; re-enable everything else.

### Fix 7: Verify hardware health and finish with OS repair

On aging Windows 10 laptops, hardware is guilty often enough to check explicitly.

1. Run **Windows Memory Diagnostic** (extended) and **CrystalDiskInfo** — replace failing RAM or drives rather than tuning around them.
2. Run **chkdsk C: /f** and schedule the restart scan to fix file-system contributors.
3. Update the BIOS from your laptop maker's support site if updates mention stability fixes.
4. Finish with **DISM /Online /Cleanup-Image /RestoreHealth** and **sfc /scannow** in an elevated prompt.
5. If System CPU remains high after all of this on healthy hardware, an in-place Windows 10 repair install (via Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) media creation guidance) rebuilds the kernel driver stack cleanly.

## Closing

Windows 10's ntoskrnl.exe CPU is usually an aging driver arguing with a modern cumulative update, SysMain misbehaving on an old drive, or the update machinery stuck mid-grind. Name the driver with LatencyMon, fix that layer, and check the hardware — the kernel goes quiet once nobody is making it work overtime.
