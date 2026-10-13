---
title: "ntoskrnl.exe High CPU on Windows 10? Proven Fixes"
slug: how-to-fix-ntoskrnl-high-cpu-usage-on-windows-10
date: 2026-09-21
categories: ["performance"]
tags: ["ntoskrnl.exe", "high cpu", "windows 10", "system process", "drivers"]
description: "System process (ntoskrnl.exe) eating CPU on Windows 10? Use LatencyMon to find the bad driver, fix update loops, and calm the kernel."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-high-cpu-usage-on-windows-10.webp"
faqs:
  - q: "Why is ntoskrnl.exe using high CPU on Windows 10?"
    a: "Ntoskrnl.exe is the Windows kernel, and its CPU time shows under the System process in Task Manager. The kernel itself rarely misbehaves — high usage means a driver or kernel component is generating excessive work, such as interrupt storms from a network driver, a storage driver retrying failed I/O, or a Windows service stuck in a loop. On Windows 10 the classic triggers are outdated network drivers, a wedged Windows Update, and SysMain thrashing on old hard drives."
  - q: "How do I find which driver is causing ntoskrnl high CPU?"
    a: "Use LatencyMon, a free tool that measures deferred procedure call (DPC) and interrupt service routine (ISR) execution time per driver. Run it for five minutes during the spike and sort by execution time — the driver at the top is generating the kernel load. Windows Performance Recorder with the DPC profile gives the same data in more detail. Once named, update that specific driver from your laptop maker's support site rather than guessing."
  - q: "Is it safe to disable SysMain to fix ntoskrnl CPU usage?"
    a: "Yes. SysMain (formerly Superfetch) is a caching service, not a critical system component — Windows runs fine without it, especially on SSDs where its benefit is minimal. Disabling it is a standard diagnostic step: if System CPU normalizes, SysMain was thrashing against slow or failing storage. Many technicians leave it disabled permanently on SSD systems with zero downside."
  - q: "Can Windows 10 updates cause ntoskrnl.exe spikes?"
    a: "Regularly. A failed or stuck Windows Update keeps the update service churning, which shows up as System CPU. Feature updates can also replace a working driver with a problematic inbox version. Check update history for failures around the time the problem started, clear the SoftwareDistribution cache if updates are stuck, and install pending cumulative updates — Microsoft has patched several kernel-adjacent performance bugs over Windows 10's lifetime."
---

On Windows 10, the **System** process sitting at 30–80% CPU in Task Manager means one thing: `ntoskrnl.exe`, the Windows kernel, is doing someone else's heavy lifting. You can't end it, you can't reinstall it separately, and killing it would crash the machine — because it *is* the machine's core. The productive question isn't "how do I stop ntoskrnl" but "who is making the kernel work this hard."

Windows 10 has its own greatest-hits list: aging network drivers generating interrupt storms, Windows Update wedged on a failed patch, SysMain thrashing on a mechanical hard drive, and the occasional bad storage driver. The approach is diagnostic, not random — measure the kernel's workload with the right tool, name the offender, and fix that specific thing.

Note the pattern first: constant high CPU at idle suggests a service or stuck update; spikes tied to network activity implicate the network driver; spikes after sleep point to power management. For the Windows 11 version of this guide, see [ntoskrnl on Windows 11](/articles/how-to-fix-ntoskrnl-high-cpu-usage-on-windows-11/); for the condensed step-by-step variant, the [ntoskrnl step-by-step](/articles/how-to-fix-ntoskrnl-high-cpu-usage-step-by-step/) covers the same ground faster.

## Why this happens

- **Interrupt storms from network drivers**: Old Wi-Fi/Ethernet drivers flooding the kernel with DPCs.
- **Stuck Windows Update**: A failed update retrying forever, keeping kernel services churning.
- **SysMain vs. slow storage**: The caching service thrashing on HDDs or failing SSDs.
- **Storage driver retries**: AHCI drivers re-issuing failed I/O, multiplying kernel work per operation.
- **Windows 10 feature update driver swaps**: Updates replacing tuned OEM drivers with generic inbox versions.
- **Failing hardware**: Dying drives or RAM generating errors the kernel must constantly handle.
- **Malware in kernel space**: Rootkits hiding activity inside System's CPU accounting.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure DPC latency with LatencyMon

Name the driver before touching anything.

1. Download and run **LatencyMon** (free) — click the play button and let it run 5 minutes during the CPU spike.
2. Check the **Drivers** tab sorted by **Total execution** — the top driver is your prime suspect (common: network miniport drivers, `storport.sys` chains, audio drivers like `rtkvhd64.sys`).
3. Note the **Highest reported DPC/ISR routine execution time** on the main tab — values consistently over 1–2ms indicate a real problem driver.
4. If DPC times are clean but System CPU is high, the load is service-driven — skip to Fix 4.
5. Write down the exact driver filename; precision here saves hours of guessing.

### Fix 2: Update or roll back the flagged driver

Surgical driver work beats blanket reinstalls.

1. Identify the device behind the driver in **Device Manager** (network adapter, storage controller, audio device).
2. Download the driver from your laptop maker's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — for your exact model and Windows 10.
3. Install it, reboot, and re-run LatencyMon for 5 minutes to verify the driver's execution time collapsed.
4. If the problem *started* with a driver update, roll back instead: Device Manager > device **Properties** > **Driver** > **Roll Back Driver**.
5. For Intel network parts, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) automates finding the right build.

### Fix 3: Unstick Windows Update

The most common service-side cause on Windows 10.

1. Go to **Settings** > **Update & Security** > **Windows Update** > **View update history** — look for failed updates with error codes.
2. Run the **Windows Update troubleshooter**: Settings > Update & Security > Troubleshoot > Additional troubleshooters.
3. If updates are stuck "installing" forever, open an elevated Command Prompt and run: `net stop wuauserv`, `net stop bits`, then rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`, then `net start wuauserv` and `net start bits`.
4. Return to Windows Update and check again — it will rebuild its cache and usually complete normally.
5. For a specific failed KB, download it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it directly.

### Fix 4: Disable SysMain and check the drive

The classic Windows 10 HDD scenario.

1. Open `services.msc`, find **SysMain** (may still show as Superfetch on older builds), set **Startup type** to **Disabled**, and stop it.
2. Test for an hour. On SSDs you won't miss it; on HDDs, weigh the tradeoff — but a quiet system beats a theoretically faster cache.
3. Check drive health: **Task Manager** > **Performance** > disk — 100% active time with tiny throughput means the drive is the bottleneck.
4. Run `wmic diskdrive get status` — anything but "OK" means back up immediately.
5. Run `chkdsk C: /f` (schedule on reboot) to fix file-system errors that multiply kernel I/O work.

### Fix 5: Clean-boot to isolate the service

Bisect the startup set when DPCs are clean.

1. Run `msconfig` > **Services** tab > check **Hide all Microsoft services** > **Disable all**.
2. **Task Manager** > **Startup** tab > disable everything, then reboot.
3. If System CPU is normal, re-enable services in halves with reboots between — when the spike returns, you've found its half; keep bisecting.
4. Usual non-Microsoft offenders on Windows 10: third-party antivirus, backup agents, VPN clients, hardware RGB utilities.
5. Update, reconfigure, or remove the identified software — don't leave it half-disabled indefinitely.

### Fix 6: Disable fast startup and update firmware

Power-transition bugs are a Windows 10 classic.

1. **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable** > uncheck **Turn on fast startup**.
2. Fast startup's hybrid shutdown keeps driver state across "shutdowns" — a corrupted state then persists indefinitely; a full shutdown clears it.
3. Check your maker's support page for a **BIOS update** — firmware fixes for interrupt routing and sleep/wake are common.
4. In **Device Manager**, open your network adapter's **Power Management** tab and uncheck **Allow the computer to turn off this device to save power** as a test.
5. Deliberately test sleep/wake cycles after each change, watching System CPU for 10 minutes post-wake.

### Fix 7: Scan for rootkits and verify hardware

Rule out the serious causes.

1. Run **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan**.
2. Review **Event Viewer** > **Windows Logs** > **System** for repeating disk errors, driver warnings, or WHEA hardware errors timestamped with the spikes.
3. Run **Windows Memory Diagnostic** (`mdsched.exe`) — faulty RAM shows up as kernel CPU handling correctable errors.
4. If disk errors repeat, back up now — no software tuning fixes failing hardware.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the built-in diagnostic tools if you need official step-by-step references.

## Closing

ntoskrnl.exe high CPU on Windows 10 follows the same rule as on any Windows: the kernel is the messenger, and LatencyMon tells you who sent the message. On Windows 10 that sender is usually an aging network driver, a stuck Windows Update, or SysMain fighting a tired hard drive. Measure first, fix the actual offender, and the System process drops back to the 1–2% where it belongs.
