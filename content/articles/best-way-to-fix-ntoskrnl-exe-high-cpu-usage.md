---
title: "ntoskrnl.exe Using High CPU? The Best Fixes That Actually Work"
slug: best-way-to-fix-ntoskrnl-exe-high-cpu-usage
date: 2026-09-18
categories: ["performance"]
tags: ["ntoskrnl.exe", "system high cpu", "windows 11", "kernel cpu", "drivers"]
description: "ntoskrnl.exe (System) eating your CPU on Windows 11? Learn why the kernel spikes and the best fixes that actually resolve it."
thumbnail: "/images/thumbs/best-way-to-fix-ntoskrnl-exe-high-cpu-usage.webp"
faqs:
  - q: "What is ntoskrnl.exe and is it a virus?"
    a: "ntoskrnl.exe is the Windows kernel itself — the core of the operating system, shown in Task Manager as 'System'. It is absolutely not a virus when located in C:\\Windows\\System32. High CPU from ntoskrnl.exe means the kernel is doing work on behalf of something else: usually a misbehaving driver, hardware interrupts, or memory management churn. The kernel is the messenger, not the culprit."
  - q: "Why does System (ntoskrnl.exe) use 20-30% CPU constantly?"
    a: "Constant kernel CPU usage typically comes from a driver stuck in a loop, excessive hardware interrupts (check the 'System interrupts' process too), memory compression working overtime due to RAM pressure, or Windows Update components churning. Less commonly, failing hardware generates interrupts the kernel must service. The fix is finding what's driving the kernel, not fighting the kernel itself."
  - q: "Can faulty RAM cause ntoskrnl.exe high CPU?"
    a: "Yes. Bad RAM causes page faults and memory-management exceptions that the kernel must handle, which shows up as ntoskrnl.exe CPU usage. If kernel CPU is high alongside application crashes, blue screens, or file corruption, run Windows Memory Diagnostic (search for it in Start) to test your RAM. Memory errors are a legitimate and underappreciated cause of kernel CPU spikes."
  - q: "Will reinstalling Windows fix ntoskrnl.exe high CPU?"
    a: "It often does, because a reinstall replaces all drivers and eliminates software corruption — but it's the nuclear option. In most cases you can fix it surgically: update the offending driver, repair system files, or address the RAM pressure causing memory compression. Try the targeted fixes first; reinstall only when the kernel CPU persists through all of them."
---

Seeing **System** — ntoskrnl.exe, the Windows kernel itself — consuming 20%, 40%, or more CPU is unsettling. You can't end the task (it's the operating system), you can't uninstall it, and killing it would crash the machine. But here's the key insight: the kernel is almost never the actual problem. It's doing work *on behalf* of something else — a bad driver, interrupt storms, or memory pressure — and that something else is what you need to fix.

The best approach isn't fighting the kernel; it's interrogating it. Windows gives you the tools to see what the kernel is busy with, and once you know, the fix is usually a driver update, a settings change, or a hardware check away.

## Why this happens

- **Misbehaving device drivers**: A driver stuck in a loop makes the kernel burn CPU servicing it endlessly.
- **Excessive hardware interrupts**: Failing or chatty hardware floods the kernel with interrupts to service.
- **Memory compression under RAM pressure**: With little free RAM, the kernel compresses memory constantly — visible as System CPU.
- **Windows Update churn**: Update components (TiWorker, orchestrator) driving kernel-mode file and registry work.
- **Corrupt system files**: Damaged kernel-mode components retrying failed operations.
- **Faulty RAM**: Memory errors generating exceptions the kernel must handle.
- **Malware using rootkit techniques**: Kernel-mode malware hiding its activity as System CPU (rare but real).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: See what the kernel is actually doing

Use the right tools to look inside System's CPU usage.

1. Download **Process Explorer** (Microsoft Sysinternals, free) and run it as administrator. Find the **System** process, double-click it, and check the **Threads** tab — sort by CPU. The thread start addresses name the driver (e.g., `ndis.sys`, `ntoskrnl.exe!...`).
2. Note the top threads: threads starting in a third-party `.sys` driver convict that driver immediately.
3. Alternatively, open **Task Manager** > **Performance** > **CPU** and check whether **System interrupts** is also high — paired System + System interrupts elevation points to hardware interrupts.
4. Run **Resource Monitor** (search in Start) > **CPU** tab and sort by CPU to see which services correlate with the kernel load.
5. Record your baseline: System CPU at idle, and which threads dominate. If the whole machine is broadly slow, also review [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

### Fix 2: Update or roll back device drivers

Bad drivers are the #1 cause — fix them first.

1. Open **Device Manager** and look for any device with a yellow warning icon — start there.
2. Based on Process Explorer findings, update the specific driver: network drivers from your vendor ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)), GPU from NVIDIA / AMD / Intel.
3. Don't forget the **chipset driver** from your laptop vendor — it governs how the kernel talks to the motherboard, and stale chipset drivers are a classic ntoskrnl CPU cause.
4. If high kernel CPU started right after a driver update, roll it back: Device Manager > device > Properties > Driver > Roll Back Driver.
5. Update **one driver at a time**, rebooting and checking System CPU after each — shotgunning five driver updates teaches you nothing about which one mattered.

### Fix 3: Relieve memory pressure

Memory compression is kernel work — give the kernel less to compress.

1. Open **Task Manager** > **Performance** > **Memory**. If usage sits above 80% constantly, memory pressure is likely driving System CPU.
2. In Task Manager's **Processes** tab, sort by Memory and close or tame the biggest consumers. Our [high RAM usage guide](/articles/windows-11-high-memory-usage-fix/) covers this in depth.
3. Disable unnecessary startup apps per [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) — every auto-started app is RAM the kernel must manage.
4. Check **Settings** > **System** > **About** to confirm how much RAM is installed. 8GB is workable; 4GB in 2026 means constant compression — a RAM upgrade is the real fix.
5. Verify the pagefile is system-managed: **Settings** > **System** > **About** > **Advanced system settings** > **Performance Settings** > **Advanced** > **Virtual memory** — it should be on automatic. A disabled or tiny pagefile forces more compression.

### Fix 4: Repair Windows system files

Corrupt kernel-mode components cause retry loops that burn CPU.

1. Open **Command Prompt as administrator** and run `sfc /scannow`. Let it complete — it repairs protected system files including kernel components.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
3. Run `chkdsk C: /f` (schedule at reboot if asked) to rule out file-system corruption contributing to kernel I/O retries.
4. Check **Settings** > **Windows Update** and install all pending updates — Microsoft ships kernel fixes in cumulative updates, and a half-applied update state can itself cause kernel churn.
5. After repairs and updates, reboot and re-check System CPU at idle for 10 minutes before declaring victory.

### Fix 5: Test your RAM and storage hardware

Hardware faults manifest as kernel CPU — rule them out.

1. Search Start for **Windows Memory Diagnostic**, run it, and choose **Restart now and check for problems**. Let the full test complete (it takes a while).
2. If errors are found, you've likely found your cause: reseat the RAM modules (if accessible) and retest; replace faulty sticks. On soldered-RAM ultrabooks, this means a warranty claim.
3. Check drive health with **CrystalDiskInfo** (free) — a failing SSD generating I/O errors forces kernel retry loops.
4. Run your vendor's built-in hardware diagnostics (boot menu, usually F12) for a second opinion on memory and storage.
5. Also scan for malware with a full **Windows Security** scan — kernel-mode rootkits are rare, but a scan is cheap insurance when System CPU is unexplained.

### Fix 6: Address Windows Update and background churn

Sometimes the kernel is busy because Windows itself is churning underneath.

1. Open **Settings** > **Windows Update** and check for stuck updates — an update failing to install can loop indefinitely, driving kernel CPU.
2. Run the **Windows Update troubleshooter**: Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run.
3. If `TiWorker.exe` (Windows Modules Installer Worker) correlates with the kernel load, let it finish — interrupting updates causes more churn, not less. Give it an hour on AC power.
4. Clear the update cache if stuck: stop the Windows Update service, delete `C:\Windows\SoftwareDistribution\Download` contents, restart the service, and check for updates again.
5. Microsoft documents kernel and update troubleshooting at Windows support — check for known issues with your specific build.

## Closing

ntoskrnl.exe high CPU is the kernel telling you something else is wrong — a driver, memory pressure, failing hardware, or update churn. Interrogate it with Process Explorer, fix what you find, and the kernel goes back to its normal near-zero idle. Don't fear the System process; read it.
