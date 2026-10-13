---
title: "ntoskrnl.exe Using Too Much CPU? How to Fix It on Windows"
slug: how-do-i-fix-ntoskrnl-exe-high-cpu-usage
date: 2026-10-03
categories: ["performance"]
tags: ["ntoskrnl.exe", "high cpu", "system process", "windows 11", "memory compression"]
description: "ntoskrnl.exe (System) eating CPU in Task Manager? It's usually memory compression, a bad driver, or update leftovers. Here's how to fix it step by step."
thumbnail: "/images/thumbs/how-do-i-fix-ntoskrnl-exe-high-cpu-usage.webp"
faqs:
  - q: "What is ntoskrnl.exe and is it a virus?"
    a: "ntoskrnl.exe is the Windows kernel itself — the core of the operating system, shown in Task Manager as the System process. It is not a virus when located in C:\\Windows\\System32. High CPU from it means kernel-level work is heavy: memory compression, driver activity, or interrupt handling. Malware sometimes uses similar names, so verify the file location, but in the genuine location it is always legitimate Windows code doing real work."
  - q: "Why does ntoskrnl.exe use CPU when my computer is idle?"
    a: "The most common idle-time cause is memory compression: Windows compresses rarely-used memory pages to avoid writing them to disk, and that compression runs inside the System process. Other idle causes include Superfetch/SysMain preloading apps, Windows Update servicing in the background, and drivers polling hardware. Idle CPU from System between 1 and 5 percent is normal; sustained double digits deserves investigation."
  - q: "Can I end or disable ntoskrnl.exe?"
    a: "No — ending the System process would crash Windows instantly, and Task Manager will not even offer the option. ntoskrnl.exe is the kernel; everything depends on it. The correct approach is finding what is making the kernel work hard: a misbehaving driver, runaway memory compression, or background servicing. Fix the workload and the System process calms down on its own."
  - q: "Does disabling memory compression fix ntoskrnl.exe high CPU?"
    a: "It can lower the System process's reported CPU, but it is usually a bad trade: without compression, Windows pages to disk instead, and on machines with spinning drives or slow SSDs that feels far worse. Only consider disabling it as a diagnostic test (powercfg aside, the command is Disable-MMAgent -mc in PowerShell). If compression was the cause, the real fix is usually adding RAM or finding the memory leak forcing excessive compression."
---

Seeing **System** (ntoskrnl.exe) consume 15%, 30%, or more CPU in Task Manager is unsettling because you can't just "close" it — it *is* Windows. The kernel doesn't burn CPU for fun, though. When ntoskrnl.exe runs hot, it's doing work on behalf of something: compressing memory, servicing a chatty driver, handling a flood of interrupts, or grinding through update maintenance. Your job is to find the client, not fight the kernel.

The most common story goes like this: a laptop with 8 GB of RAM runs Chrome with forty tabs, Windows starts compressing memory aggressively to cope, and the System process sits at 20% CPU indefinitely. The second most common story: a buggy driver (often network or storage) generates constant kernel work. Both are fixable without reinstalling Windows, and both reveal themselves with the right checks. For general CPU-hog hunting beyond the System process, see [fixing high CPU usage on Windows 11](/articles/how-to-fix-high-cpu-usage-on-windows-11/).

## Why this happens

- **Memory compression working overtime**: With RAM nearly full, Windows compresses pages constantly — CPU-intensive work billed to the System process.
- **A misbehaving driver generating kernel work**: Bad network, storage, or USB drivers issue excessive I/O or interrupts the kernel must service.
- **Windows Update servicing**: Update installation, .NET optimization (ngen), and post-update maintenance run heavily in the kernel.
- **SysMain (Superfetch) preloading**: The prefetch service analyzes usage patterns and preloads apps, generating disk and CPU activity.
- **Corrupt system files**: Damaged kernel components or drivers can loop or retry operations endlessly.
- **Memory leak in a driver**: A driver leaking kernel pool memory forces the memory manager into expensive reclamation work.
- **Hypervisor / virtualization overhead**: Virtualization-based security features add kernel work, especially on systems with marginal drivers.
- **Failing hardware causing retries**: A dying disk or flaky RAM forces the kernel's error-handling paths to run constantly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm what's driving the System process

Don't treat the symptom — identify the workload.

1. Open **Task Manager** > **Performance** > **Memory** and check **In use (Compressed)** — if several gigabytes show as compressed and RAM is above 85% in use, memory compression is your prime suspect.
2. Open **Resource Monitor** (search for it in Start) > **CPU** tab, and check the **System** process's associated handles and modules for clues about which driver is active.
3. For a definitive answer, download **Process Explorer** (Microsoft Sysinternals), run as administrator, double-click the **System** process, and open the **Threads** tab sorted by CPU — the thread start addresses name the actual driver (e.g., `ntoskrnl.exe!Mi...` means memory management; a third-party `.sys` name means that driver).
4. Note whether the CPU usage is constant or tied to activity (opening apps, network traffic, idle time) — the pattern points at the subsystem.
5. If the top threads are all memory-management functions (`Mm`, `Mi` prefixes) and RAM is full, skip to Fix 2. If a specific driver `.sys` dominates, skip to Fix 4.

### Fix 2: Relieve memory pressure (the most common fix)

Less pressure means less compression work.

1. Press **Ctrl + Shift + Esc**, go to the **Processes** tab, click **Memory** to sort, and identify the biggest consumers. Browsers with dozens of tabs are the usual winners.
2. Close what you don't need, and in Chrome/Edge enable **Memory Saver** (Settings > Performance) so inactive tabs sleep instead of consuming RAM.
3. Disable unnecessary startup apps: Task Manager > **Startup apps**, disable anything with **High** startup impact you don't use daily. Full guide: [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).
4. Check for a memory leak: note **Committed** memory in Task Manager > Performance > Memory, leave the laptop idle for an hour, and check again — steadily climbing committed memory with no apps running means something is leaking; the Processes tab sorted by memory usually names it.
5. If you consistently sit above 85% memory use in normal work, the honest fix is more RAM (if your laptop allows upgrades) — 16 GB is the comfortable minimum for Windows 11 in 2026. Check your maker's specs page (Dell, HP, Lenovo) for your model's maximum.

### Fix 3: Calm down SysMain and background servicing

Windows' own maintenance can keep the kernel busy for days.

1. Open **Services** (`services.msc`), find **SysMain**, double-click it, set **Startup type** to **Disabled**, and click **Stop**. SysMain preloads apps based on usage patterns; on systems with fast SSDs its benefit is small and its cost is real.
2. Let Windows Update finish: **Settings** > **Windows Update** — if updates are pending or "installing," let them complete and reboot. Post-update, the .NET optimizer (`ngen`) can run for hours; it finishes on its own.
3. Open **Task Scheduler** and check **Microsoft** > **Windows** > **MemoryDiagnostic** and **.NET Framework** tasks — a stuck scheduled task can loop kernel work. Don't disable them permanently, but note if one is perpetually "Running."
4. Run **Disk Cleanup** as administrator and clear **Windows Update Cleanup** and **Delivery Optimization Files** — servicing leftovers sometimes keep the update stack churning.
5. Give it 24 hours after any fix: background servicing genuinely needs time to settle, and premature conclusions waste effort.

### Fix 4: Update or roll back the offending driver

When Process Explorer names a driver, act on that driver.

1. In Device Manager, find the device for the named `.sys` file (network adapters, storage controllers, and USB controllers are the usual suspects) and check its driver date on the **Driver** tab.
2. Download the newest driver from your laptop maker's support page — Dell, HP, or Lenovo — using your exact model number.
3. If the high CPU **started** right after a driver update, roll back instead: Device Manager > device **Properties** > **Driver** tab > **Roll Back Driver**.
4. For network drivers specifically, Intel users can use the [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to get the latest validated wireless driver.
5. Restart fully (hold **Shift** while clicking Restart, or use `shutdown /r /t 0`) and re-check the System process CPU after 10 minutes of normal use.

### Fix 5: Repair system files and the component store

Corruption makes the kernel work harder than it should.

1. Open an elevated Command Prompt (**Win + X** > **Terminal (Admin)**) and run `sfc /scannow` — let it complete; it repairs protected system files including kernel components.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the component store that SFC draws from. It can take 15-30 minutes.
3. Restart and re-run `sfc /scannow` once more to confirm everything is clean.
4. If SFC found corruption it couldn't fix on the first pass, the DISM + second SFC sequence usually resolves it.
5. Microsoft documents both tools in the [Windows support hub](https://support.microsoft.com/en-us/windows) — they're safe, built-in, and the correct first repair step before considering a reset.

### Fix 6: Check for failing hardware

Hardware faults disguise themselves as kernel CPU usage.

1. Check disk health: Task Manager > Performance > Disk — sustained 100% **Active time** with high **Average response time** during System CPU spikes implicates storage. Confirm with CrystalDiskInfo (free SMART reader).
2. Test RAM: search Start for **Windows Memory Diagnostic**, run it, and reboot — bad RAM causes page faults and error handling that inflate System CPU.
3. Check temperatures with HWiNFO: thermal throttling forces the kernel's power management code to work overtime.
4. If a specific device is failing (SMART warnings, memory errors), replace it — no software fix compensates for dying hardware, and kernel CPU is often the first symptom users notice.
5. Still stuck after all six fixes? A clean Windows install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) with fresh vendor drivers eliminates software causes definitively; if System CPU is still high on a clean install, it's hardware.

## Closing

ntoskrnl.exe high CPU is Windows telling you the kernel is overworked, not that the kernel is broken. In most cases the answer is memory pressure (Fix 2) or a single bad driver (Fix 4) — both diagnosable in under half an hour with Task Manager and Process Explorer. Work the list in order, measure after each change, and you'll find the System process back under 5% where it belongs.
