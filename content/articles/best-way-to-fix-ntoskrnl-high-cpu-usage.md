---
title: "Ntoskrnl High CPU? The Best Way to Fix It on Windows"
slug: best-way-to-fix-ntoskrnl-high-cpu-usage
date: 2026-09-14
categories: ["performance"]
tags: ["ntoskrnl.exe", "high cpu", "system process", "windows kernel"]
description: "Ntoskrnl.exe (System) using huge CPU? Understand what the Windows kernel is doing and the proven fixes that actually lower it."
thumbnail: "/images/thumbs/best-way-to-fix-ntoskrnl-high-cpu-usage.webp"
faqs:
  - q: "What is ntoskrnl.exe and why does it use CPU?"
    a: "Ntoskrnl.exe is the Windows kernel — the core of the operating system itself, shown in Task Manager as System. It doesn't use CPU on its own behalf; high CPU from System means the kernel is doing work for something else: a faulty driver, hardware interrupts, memory compression, or disk I/O processing. The kernel is the messenger, so the fix is finding what's sending all the messages."
  - q: "Is ntoskrnl.exe a virus?"
    a: "The genuine ntoskrnl.exe lives in C:\\Windows\\System32 and is essential — Windows cannot run without it. Some malware uses similar names, so verify the file location in Task Manager. If it's in System32 and signed by Microsoft, it's legitimate, and the high CPU is a driver or hardware issue rather than an infection."
  - q: "Can I end the ntoskrnl.exe process?"
    a: "No — you cannot end the System process, and you shouldn't try. Ntoskrnl.exe is the kernel; killing it would crash Windows instantly. Task Manager won't even offer the option. Instead of fighting the kernel, diagnose what it's working on: outdated drivers, memory compression pressure, or hardware interrupts are the usual causes."
  - q: "How do I know which driver is causing ntoskrnl high CPU?"
    a: "Use Windows Performance Recorder or Process Explorer (from Microsoft Sysinternals) to see which driver module is consuming kernel time — ndis.sys points to network drivers, storport.sys to storage, and dxgkrnl.sys to graphics. The DPC latency checker tool LatencyMon also identifies the worst-offending drivers. Once identified, update or roll back that specific driver."
---

Seeing `System` — ntoskrnl.exe — at 20%, 40%, or higher in Task Manager feels wrong. The kernel shouldn't be the busiest thing on your laptop. But here's the thing technicians learn early: the kernel is never busy for its own sake. When ntoskrnl.exe shows high CPU, Windows is doing heavy lifting on behalf of *something else* — usually a misbehaving driver, a storage device hammering interrupts, or memory compression working overtime. You can't kill the kernel, so you have to find what's making it work.

The best approach is systematic: measure what the kernel is doing, identify the driver or subsystem responsible, and fix that. For the bigger performance picture, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); if disk usage is also pinned, read our [high disk usage fix guide](/articles/how-to-fix-windows-11-high-disk-usage-on-startup/).

## Why this happens

- **Faulty or outdated device driver**: Bad network, storage, or audio drivers generate storms of interrupts the kernel must service.
- **Memory compression working overtime**: With low free RAM, Windows compresses memory pages in the kernel — CPU-intensive by design.
- **Failing storage device**: A dying SSD or HDD generates retries and errors that the kernel processes constantly.
- **Corrupt system files**: Damaged Windows components make the kernel retry operations or take slow fallback paths.
- **Superfetch/SysMain gone wild**: Aggressive preloading hammers disk I/O, which the kernel must process.
- **Malware or rootkits**: Deep infections hook into the kernel, inflating System CPU.
- **Windows update stuck mid-install**: Update components churn in the kernel when an update is wedged.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify what's actually driving kernel CPU

Don't guess — measure.

1. Download **Process Explorer** from Microsoft Sysinternals and run it as administrator — it breaks down System CPU into driver components.
2. Double-click the **System** process and check the **Threads** tab sorted by CPU — the module names (like `ndis.sys`, `storport.sys`, `ACPI.sys`) tell you which driver family is responsible.
3. Alternatively, run **LatencyMon** (free) for a few minutes — its Drivers tab ranks drivers by DPC execution time, pointing straight at the worst offender.
4. Note the names: network drivers (`ndis.sys`, `rtwlanu.sys`), storage (`storport.sys`, `stornvme.sys`), and graphics (`dxgkrnl.sys`) are the usual suspects.
5. Write down the top offender — every fix from here targets it specifically.

### Fix 2: Update the offending driver

The single highest-yield fix for ntoskrnl CPU issues.

1. Open **Device Manager**, find the device matching your suspect driver (network adapter, storage controller, display adapter).
2. Right-click > **Update driver** > **Search automatically** — but don't stop there; Windows' driver database lags behind.
3. Go to your laptop manufacturer's support site ([Dell](https://www.dell.com/support), HP, or Lenovo) and download the latest driver for your exact model — OEM drivers are tuned for your hardware.
4. For Intel network or chipset drivers, Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) auto-detects and updates them.
5. Restart after updating and compare System CPU — a fixed driver often drops kernel CPU to near zero immediately.

### Fix 3: Roll back a recently updated driver

If the problem started after a driver update, undo it.

1. In **Device Manager**, right-click the suspect device > **Properties** > **Driver** tab > **Roll Back Driver** (if available).
2. If the button is greyed out, check **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the driver update from there.
3. Alternatively, download the previous driver version from the manufacturer's site and install it manually over the new one.
4. After rolling back, pause driver updates temporarily: **System** > **Advanced system settings** > **Hardware** > **Device Installation Settings** > **No**.
5. This is especially common with network drivers pushed through Windows Update — the generic version misbehaves on specific laptop Wi-Fi chips.

### Fix 4: Reduce memory pressure

Kernel memory compression is a top hidden cause.

1. Open Task Manager > **Performance** > **Memory** — if **In use** is consistently above 80-85%, compression is working hard inside ntoskrnl.
2. Check which apps use the most memory and close or replace the heavy ones; browsers with dozens of tabs are the classic offender.
3. Disable unnecessary startup programs via our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) to free RAM at boot.
4. Consider disabling memory compression as a test: in an elevated terminal, run `Disable-MMAgent -mc` (PowerShell) — if System CPU drops, RAM pressure was the cause and a RAM upgrade is the real fix.
5. Re-enable with `Enable-MMAgent -mc` if it didn't help — compression is generally beneficial.

### Fix 5: Check your storage health

A struggling drive makes the kernel work constantly.

1. Open an elevated Command Prompt and run `wmic diskdrive get status` — anything other than "OK" means trouble.
2. Run `chkdsk C: /f /r` (schedule at reboot) to find and repair bad sectors — a drive with growing bad sectors generates endless kernel-level retries.
3. Check SSD health with your manufacturer's tool (Samsung Magician, WD Dashboard, Intel MAS) — look at wear level and available spare.
4. If the drive is failing, back up immediately and replace it — no software fix compensates for dying hardware.
5. After confirming a healthy drive, move on — storage is either the cause or it's eliminated.

### Fix 6: Disable SysMain and Windows Search temporarily

These services generate the I/O storms the kernel processes.

1. Press **Win+R**, type `services.msc`, find **SysMain**, double-click, set **Startup type** to **Disabled**, and stop the service.
2. Do the same test for **Windows Search** — set to Disabled and stop it, then watch System CPU for 15 minutes.
3. If System CPU drops significantly, one of these was the trigger. Our [Windows Search indexing guide](/articles/how-to-disable-windows-search-indexing-on-windows-11/) covers a more surgical approach than full disable.
4. If there's no change, re-enable both — they weren't the cause, and disabling them permanently has downsides.
5. This diagnostic is quick and reversible, which is exactly what you want before deeper surgery.

### Fix 7: Repair Windows system files

Corrupt system components force the kernel onto slow paths.

1. Open an elevated terminal and run `DISM /Online /Cleanup-Image /RestoreHealth` — wait for it to complete (it can take 15+ minutes).
2. Then run `sfc /scannow` and restart when done.
3. Check **Settings** > **Windows Update** and install everything pending — kernel bugs are fixed in cumulative updates, and a stuck update itself can cause this.
4. If a specific update is wedged, use the Microsoft Update Catalog to manually download and install it.
5. After repair and updates, monitor for a full day — kernel CPU should settle below 5% at idle on a healthy system.

## Closing

Ntoskrnl.exe high CPU is the kernel telling you something underneath is wrong — almost always a driver, memory pressure, or a failing drive. Measure first with Process Explorer or LatencyMon, fix the specific offender, and the kernel goes quiet. Chasing the System process itself is a dead end; chasing what drives it is the whole game.
