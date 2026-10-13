---
title: "Fix ntoskrnl.exe High CPU Usage in Windows 11 24H2"
slug: "how-to-fix-ntoskrnl-high-cpu-usage-in-windows-11-24h2"
date: "2026-09-22"
categories: ["performance"]
tags: ["ntoskrnl.exe", "high cpu", "windows 11 24h2", "system process", "kernel"]
description: "The System process (ntoskrnl.exe) eating CPU in Windows 11 24H2? It's usually a driver — here's how to find which one and fix it."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-high-cpu-usage-in-windows-11-24h2.webp"
faqs:
  - q: "What is ntoskrnl.exe and why does it show as 'System'?"
    a: "Ntoskrnl.exe is the Windows kernel itself — the core of the operating system handling memory, processes, and hardware communication. In Task Manager it appears as the 'System' process. High CPU here means kernel-mode code is working hard, which in practice almost always means a third-party driver misbehaving, since Microsoft's own kernel code is heavily optimized."
  - q: "Can I end the System process to stop the CPU usage?"
    a: "No — the System process is the kernel; ending it would crash Windows instantly, and Task Manager will not let you try. The CPU usage is a symptom of something the kernel is doing on behalf of a driver or hardware device. The fix is identifying and updating that driver, never attacking the System process."
  - q: "Why did ntoskrnl CPU spike after the 24H2 update?"
    a: "Feature updates change kernel interfaces that drivers rely on. A driver written for the older build can start generating excessive interrupts or deferred procedure calls under the new kernel — showing up as System CPU. Updating to 24H2-compatible driver versions from the manufacturer resolves most of these cases."
  - q: "Is high System CPU a sign of malware?"
    a: "Rarely. Malware typically hides in user-mode processes, not the kernel, because kernel-mode malware is much harder to write. Before suspecting malware, exhaust the driver causes — they account for the overwhelming majority of ntoskrnl CPU cases. A Defender offline scan is still a reasonable final check."
---

When Task Manager shows **System** (ntoskrnl.exe) consuming 20%, 40%, or more CPU continuously, it looks alarming — the operating system's own core is the hog, and you cannot end it, disable it, or uninstall it. But ntoskrnl.exe is the messenger, not the culprit. The kernel does work on behalf of drivers and hardware; when a driver misbehaves — generating interrupt storms, leaking deferred procedure calls, or mishandling power states — the CPU cost shows up under System because the kernel is where the work executes.

Windows 11 24H2 is a common trigger because it changes kernel interfaces. Drivers certified for older builds can start misbehaving under the new kernel, and the symptom is exactly this: System CPU that was fine before the update and is now constantly elevated. The diagnostic path is therefore driver forensics: find which driver is generating the load, update or remove it, and verify.

You will need two free Microsoft tools for the deep diagnosis: **Process Explorer** (to see System's threads) and optionally **Windows Performance Analyzer**. Both are part of the Sysinternals suite and are safe, official utilities.

## Why this happens

- **Outdated driver under 24H2:** A driver built for an older Windows build generating excessive DPCs/interrupts under the new kernel.
- **Network driver interrupt storm:** Faulty Wi-Fi or Ethernet drivers are the single most common cause of System CPU spikes.
- **Storage driver issues:** AHCI/NVMe driver problems manifest as kernel CPU during disk I/O.
- **Antivirus filter drivers:** Kernel-mode AV filters doing excessive per-operation work.
- **Corrupted system files:** Damaged kernel components causing retry loops in kernel mode.
- **Failing hardware:** A dying drive or flaky device generating hardware interrupts the kernel must service.
- **Power management conflicts:** Drivers fighting Windows' power states, especially on laptops with aggressive power saving.
- **Hypervisor/virtualization drivers:** Hyper-V or third-party virtualization drivers misbehaving after the build update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's DPC/interrupt load, not a hidden process

First, make sure the CPU is genuinely kernel-mode work and not a misattributed user process. In Task Manager's **Performance > CPU** tab, check the breakdown — high **kernel time** (the darker portion of the graph) confirms it. Even better, open Resource Monitor's CPU tab: the **Interrupts** and **DPCs** pseudo-processes quantify exactly how much CPU goes to interrupt handling. If DPCs/Interrupts account for most of the System usage, you have a driver interrupt problem — proceed with driver forensics. If not, look for a different cause. Our [post-update variant](/articles/how-to-fix-ntoskrnl-high-cpu-usage-after-windows-11-update/) covers the non-24H2 cases.

1. Open Task Manager > **Performance > CPU**; check kernel time portion.
2. Open Resource Monitor > CPU; note **DPCs** and **Interrupts** CPU.
3. High DPC/Interrupt CPU confirms a driver cause.
4. Low DPC with high System suggests a different kernel workload — continue diagnosing.

### Fix 2: Identify the guilty driver with Process Explorer

Download **Process Explorer** from Microsoft Sysinternals, run it as administrator, and examine the **System** process's threads (double-click System > Threads tab, sort by CPU). The thread stack's top frames name the driver file (e.g., ndis.sys for network, storahci.sys for storage, or a third-party .sys). This is the definitive diagnosis — it names the exact driver instead of guessing. Write down the driver filename; everything downstream targets it specifically.

1. Download **Process Explorer** (Microsoft Sysinternals) and run as administrator.
2. Double-click the **System** process; open the **Threads** tab.
3. Sort by **CPU**; note the top thread's module/driver name.
4. Record the driver filename — this is your target.

### Fix 3: Update the identified driver

With the driver named, update it properly: get the latest version from your laptop manufacturer's support site (preferred for laptops, since they validate the whole stack) or the chip vendor (Intel/Realtek for network). For network drivers — the most common offenders — Intel's official [detection tool](https://www.intel.com/content/www/us/en/support/detect.html) finds the right package. Install, reboot, and re-check System CPU. If the manufacturer has no 24H2-era driver, try the chip vendor's generic latest — it is usually newer than the laptop vendor's.

1. Identify the driver from Fix 2 (e.g., Netwtw10.sys = Intel Wi-Fi).
2. Download the latest version from manufacturer or chip vendor.
3. Install and reboot.
4. Verify System CPU in Task Manager/Resource Monitor.

### Fix 4: Roll back or replace a bad driver update

Sometimes the guilty driver is one Windows Update just installed — the "update" is the bug. In **Device Manager**, open the device's Properties > **Driver** tab and use **Roll Back Driver** if available. If rollback is grayed out, manually install the previous known-good version from the manufacturer's archive. This is particularly common with network and audio drivers pushed via Windows Update. After rolling back, consider pausing driver updates via Group Policy/registry so Windows does not reinstall the bad version overnight.

1. Open Device Manager; find the device using the guilty driver.
2. **Properties > Driver > Roll Back Driver** (if available).
3. Otherwise, install the previous version from the manufacturer's site.
4. Block the bad version from reinstalling via update settings.

### Fix 5: Disable the device to confirm, then address it

For a definitive confirmation, disable the suspect device in Device Manager and watch System CPU: if it drops to normal, the device's driver is proven guilty. This is diagnostic — you then decide the permanent fix: updated driver, replacement device, or leaving it disabled if it is non-essential (e.g., an unused fingerprint reader or SD card reader with a buggy driver). On laptops, also test with Wi-Fi/Bluetooth toggled in hardware — wireless drivers are the top offenders and the toggle test takes seconds.

1. In Device Manager, right-click the suspect device > **Disable device**.
2. Watch System CPU for 5 minutes.
3. If it normalizes, the driver is confirmed guilty.
4. Re-enable and apply the permanent driver fix, or leave disabled if non-essential.

### Fix 6: Run DISM/SFC and check hardware health

If no single driver stands out, the kernel itself may be damaged or hardware may be generating the interrupts. Run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow` to repair system files. Then check hardware: run your manufacturer's diagnostics (Lenovo/Dell/HP all include bootable diagnostics) focusing on storage and memory, since failing drives and bad RAM generate interrupt loads that surface as System CPU. A drive with reallocated sectors can absolutely cause this symptom — check SMART data. Our [memory diagnostic guide](/articles/how-to-run-memory-diagnostic-tool-in-windows-11-24h2/) covers the RAM side.

1. Run DISM RestoreHealth, then `sfc /scannow`; reboot.
2. Run the manufacturer's bootable hardware diagnostics.
3. Check SMART drive health and run Windows Memory Diagnostic.
4. Replace any failing hardware — no driver fix compensates for it.

### Fix 7: Clean-install the driver stack as a last resort

When the guilty driver cannot be identified or updates do not help, reset the whole driver stack: uninstall the device drivers (checking **delete driver software**), reboot to let Windows install its baseline drivers, then install only the manufacturer's validated driver pack — nothing from third-party updaters. As the final option, an in-place Windows repair install (from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps) refreshes the kernel and driver store together, resolving corruption that per-driver updates cannot. Back up first regardless.

1. Uninstall suspect drivers with **Delete driver software** checked.
2. Reboot; let Windows install baseline drivers.
3. Install only the manufacturer's validated driver pack.
4. Final resort: in-place repair install of Windows 11 (back up first).

## Closing

Ntoskrnl.exe high CPU in 24H2 is a driver problem wearing a kernel costume — and Process Explorer's thread view unmasks it in minutes. Name the driver, update or roll back that specific driver, and the System process drops back to its usual near-zero. The kernel was never the enemy; it was just doing what a misbehaving driver asked, thousands of times per second.
