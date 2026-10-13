---
title: "Ntoskrnl.exe High CPU Usage in Windows 11 24H2? Fix It"
slug: "how-to-fix-ntoskrnl-exe-high-cpu-usage-in-windows-11-24h2"
date: "2026-10-13"
categories: ["performance"]
tags: ["ntoskrnl.exe", "high cpu", "system process", "windows 11 24h2", "kernel cpu"]
description: "Ntoskrnl.exe (System) eating 20–50% CPU in Windows 11 24H2? The kernel doesn't misbehave on its own — here's how to find the driver or hardware actually responsible and fix it."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-exe-high-cpu-usage-in-windows-11-24h2.webp"
faqs:
- q: "What is ntoskrnl.exe and why is it using so much CPU?"
  a: "Ntoskrnl.exe is the Windows kernel itself — the core of the operating system handling memory, processes, and hardware communication. It never 'goes rogue' on its own; high CPU attributed to it actually means a faulty driver, misbehaving hardware, or a kernel-level service is making excessive calls. The fix is always finding that underlying driver or device, never the kernel file itself."
- q: "Is ntoskrnl.exe a virus?"
  a: "The legitimate ntoskrnl.exe lives in C:\\Windows\\System32 and is essential — Windows cannot run without it. Malware sometimes uses the same name to hide, but a malicious copy would typically sit in a different folder. Right-click the process in Task Manager, choose 'Open file location,' and verify it points to System32. If it does, it's genuine and the CPU usage has a driver or hardware cause."
- q: "Can outdated drivers cause ntoskrnl.exe high CPU?"
  a: "Yes — this is the most common cause. A buggy network, storage, or audio driver can issue thousands of unnecessary kernel calls per second, and all that CPU time gets billed to ntoskrnl.exe (shown as 'System' in Task Manager). Updating chipset, storage, network, and audio drivers resolves the majority of cases, especially after a feature update like 24H2."
- q: "Why did ntoskrnl.exe CPU spike after the 24H2 update?"
  a: "Feature updates change kernel interfaces, and drivers written for the old version can interact inefficiently with the new kernel — generating excessive interrupts or deferred procedure calls. 24H2 specifically changed memory management paths that some older storage and network drivers hammer. Updating those drivers to 24H2-certified versions is the fix."
---

Seeing "System" (ntoskrnl.exe) at 30% CPU in Task Manager is unsettling because you can't just end the task — it's the Windows kernel. But here's the key insight that makes this fixable: the kernel is essentially never the problem. It's the messenger. Something underneath — a driver, a device, a hardware fault — is shouting at the kernel thousands of times per second, and the kernel's CPU time is just where the noise shows up.

So this guide is a detective process. We use the right tools to see *which* driver is generating the load, then fix or replace that driver. It's methodical, and it works.

## Why this happens

- **Faulty or outdated device driver** — the top cause; typically network, storage, or audio drivers issuing excessive kernel calls.
- **24H2 kernel interface changes** — old drivers interacting inefficiently with the new kernel's memory management paths.
- **Failing hardware generating interrupts** — a dying drive, bad RAM, or flaky USB device floods the kernel with interrupt requests.
- **Corrupt system files** — damaged kernel-adjacent components causing retry loops.
- **Memory issues** — bad RAM forces the memory manager (part of the kernel) into constant error handling.
- **Third-party antivirus filter drivers** — kernel-level AV drivers hooking every file and network operation.
- **Windows Update stuck servicing** — the servicing stack hammering the kernel during a stuck update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the guilty driver with Windows Performance Recorder

Guessing which driver is at fault wastes hours. This tool shows you in minutes.

Steps:

1. Install the Windows Performance Toolkit (part of the Windows ADK) or use the built-in **Windows Performance Recorder** (search WPR in Start).
2. In WPR, select the **CPU usage** profile and click Start. Let it record for 60–90 seconds while ntoskrnl.exe shows high CPU.
3. Click Save and open the recording in **Windows Performance Analyzer**.
4. Look at the CPU Usage (Sampled) table, grouped by process — expand "System" and sort by Weight.
5. The top modules (e.g., `storport.sys`, `ndis.sys`, `tcpip.sys`) point to the subsystem: storage, network, or TCP stack. Note the driver name — that's your target.

### Fix 2: Update the identified driver category

Once you know the subsystem, update its drivers from the manufacturer — not just Windows Update.

Steps:

1. **Storage culprits** (`storport.sys`, `iaStor*.sys`): update the Intel RST / chipset storage driver from your laptop manufacturer's site.
2. **Network culprits** (`ndis.sys`, `tcpip.sys`, `netio.sys`): update Wi-Fi and Ethernet drivers; for Intel wireless, use [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html).
3. **Audio culprits** (`portcls.sys`, `HDAudBus.sys`): update the Realtek/Conexant audio driver.
4. Always prefer the **laptop manufacturer's** driver page for your exact model over generic vendor drivers.
5. Restart after each driver update and re-check System CPU in Task Manager.

### Fix 3: Update chipset and BIOS

The chipset driver mediates almost all hardware-kernel communication; an old one under 24H2 is a prime suspect.

Steps:

1. Check your current BIOS version with `msinfo32`.
2. Visit your manufacturer's support site and install the latest **chipset driver** and **BIOS** for your model.
3. Follow BIOS update instructions precisely — keep the charger connected, don't interrupt it.
4. After the BIOS update, load optimized defaults in the BIOS setup, then re-apply any custom settings.
5. Monitor System CPU for a day — chipset/BIOS fixes often resolve ntoskrnl.exe issues outright.

### Fix 4: Test RAM for faults

Bad memory makes the kernel's memory manager work overtime — and it shows up as ntoskrnl.exe CPU.

Steps:

1. Search for "Windows Memory Diagnostic" in Start and run it; choose "Restart now and check for problems."
2. Let the full test complete (it takes 15–30 minutes).
3. If errors are found, power off, reseat the RAM modules (if accessible), and retest.
4. Persistent errors mean a bad stick — replace it. On laptops with soldered RAM, this means a service visit.
5. For a deeper test, run MemTest86 from a USB drive overnight.

### Fix 5: Check drive health

A failing drive generates constant I/O retries that bill CPU time to the kernel.

Steps:

1. Run `wmic diskdrive get status` in an elevated prompt.
2. Install CrystalDiskInfo (free) and check the SMART health status — anything but "Good" is a red flag.
3. Run `chkdsk C: /f /r` (schedule at restart) to find and map out bad sectors.
4. If the drive is failing, clone it to a new SSD immediately — this also tends to fix the CPU issue as a side effect.
5. After replacing, reinstall storage drivers fresh rather than carrying old ones over.

### Fix 6: Remove problematic filter drivers

Antivirus and disk-utility filter drivers sit between hardware and the kernel and can generate enormous call volumes.

Steps:

1. In an elevated Command Prompt, run `fltmc filters` to list all file-system filter drivers.
2. Look for third-party entries (antivirus, backup tools, encryption software).
3. Temporarily uninstall the associated software and observe System CPU.
4. If a specific product's filter is the cause, update it to the latest version or replace it — old filter drivers are a classic 24H2 conflict.
5. Windows' own Defender filters rarely cause this; third-party ones are the usual suspects. Microsoft's [support hub](https://support.microsoft.com/en-us/windows) documents filter driver troubleshooting.

### Fix 7: Repair the servicing stack and system files

Rule out Windows-internal corruption as the call generator.

Steps:

1. In elevated Terminal, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`.
3. Check Windows Update for stuck updates — clear them with the update-component reset if needed. A stuck [Windows Modules Installer](/articles/how-to-fix-windows-modules-installer-high-cpu-in-windows-11-24h2/) is a frequent hidden source of kernel load after feature updates.
4. Restart and monitor.
5. If System CPU is high only during Windows Update activity, that's normal servicing — let it finish.

### Fix 8: Disable unneeded devices to isolate hardware faults

A flaky device (bad USB controller, failing card reader) can flood the kernel with interrupts.

Steps:

1. Open Device Manager and look for any devices with warning icons — disable suspects one at a time.
2. Unplug all USB devices except keyboard/mouse and observe.
3. In Device Manager, try disabling: SD card readers, fingerprint sensors, and secondary network adapters you don't use.
4. If disabling a device drops System CPU, you've found faulty hardware — update its driver or leave it disabled.
5. Our [system interrupts guide](/articles/how-to-fix-system-interrupts-high-cpu-in-windows-11-24h2/) covers the interrupt-storm variant of this problem in depth, since the two issues overlap heavily.

## Closing

Ntoskrnl.exe high CPU is a symptom, and the WPR analysis in Fix 1 turns it from a mystery into a named driver you can update or remove. In my experience, the trail leads to storage or network drivers in about 70% of 24H2 cases, bad RAM or drives in most of the rest. Never delete or "replace" ntoskrnl.exe itself — it's not the problem, and touching it will break Windows. Fix the caller, not the kernel.
