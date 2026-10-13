---
title: "Ntoskrnl High CPU on an ASUS Laptop: Fix Guide"
slug: how-to-fix-ntoskrnl-high-cpu-usage-on-asus-laptop
date: 2026-09-21
categories: ["performance"]
tags: ["ntoskrnl.exe", "system process", "asus laptop", "high cpu", "driver fix"]
description: "Ntoskrnl.exe driving CPU up on your ASUS laptop? Identify the faulty ASUS or third-party driver behind it and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-high-cpu-usage-on-asus-laptop.webp"
faqs:
  - q: "What causes ntoskrnl.exe high CPU specifically on ASUS laptops?"
    a: "The ASUS-specific triggers are Armoury Crate's kernel-level hardware monitoring drivers, MyASUS system drivers, outdated ASUS-provided Wi-Fi and audio drivers, and ASUS power management drivers mishandling sleep/wake interrupts. These all run in kernel mode, so their misbehavior shows up as System/ntoskrnl CPU. The generic causes — bad third-party drivers, USB spam, failing RAM — apply too."
  - q: "Is Armoury Crate causing my System process CPU usage?"
    a: "It can be. Armoury Crate installs low-level drivers for fan control, lighting, and hardware monitoring that operate in kernel mode; when they malfunction — often after a Crate or Windows update — they generate interrupt storms visible as ntoskrnl CPU. Test by fully exiting Armoury Crate and stopping its services: if System CPU drops, you've found it, and a clean reinstall of Crate usually fixes it."
  - q: "Should I update my ASUS BIOS to fix ntoskrnl CPU?"
    a: "If driver updates haven't helped, yes — ASUS BIOS updates frequently fix interrupt routing, power management, and ACPI issues that manifest as kernel CPU, especially on models where the problem appeared after a Windows feature update. Use the EZ Flash utility or MyASUS to update from ASUS's official BIOS for your exact model, on AC power, without interrupting it."
  - q: "How do I check if my ntoskrnl.exe is the real Microsoft file?"
    a: "In Task Manager Details, right-click the System process — you can't open its file location directly, but you can verify C:\\Windows\\System32\\ntoskrnl.exe exists, is signed by Microsoft (Properties → Digital Signatures), and matches the expected size. Rootkits mimicking the kernel are extremely rare; in virtually all cases, high System CPU is a driver issue, not a compromised kernel."
---

On ASUS laptops, a hot System process often has an ASUS accent. Armoury Crate's hardware-monitoring drivers, MyASUS system components, and ASUS's bundled Wi-Fi and audio drivers all run in kernel mode — so when any of them misbehaves, the CPU burn shows up under ntoskrnl.exe, and Task Manager gives you no hint that ASUS software is the author.

The approach is the same detective work as any ntoskrnl case — name the driver, fix the driver — with ASUS-specific suspects checked first. Here's the ordered investigation.

## Why this happens

- **Armoury Crate kernel drivers:** Hardware monitoring and fan-control drivers generating interrupt storms.
- **MyASUS system drivers:** Outdated ASUS system components misbehaving after Windows updates.
- **ASUS-bundled Wi-Fi drivers:** Older wireless drivers with DPC latency problems.
- **ASUS power management:** Sleep/wake interrupt mishandling by ASUS ACPI drivers.
- **Realtek audio drivers:** The bundled audio driver hanging on stream changes.
- **USB device spam:** Docks and peripherals flooding the kernel, ASUS laptop or not.
- **Failing memory:** RAM errors forcing expensive kernel-level handling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test the Armoury Crate hypothesis first

Before generic diagnosis, check the prime ASUS suspect. Fully exit Armoury Crate (system tray → quit), then open services.msc and stop ASUS services (Armoury Crate Service, ASUS Optimization, etc.). Watch Task Manager's System CPU for 10 minutes. If it drops, Armoury Crate's kernel drivers are the cause — uninstall Crate completely, reboot, and reinstall the latest version from ASUS or the Microsoft Store. A clean reinstall replaces the malfunctioning low-level drivers. If nothing changes, continue with general diagnosis. The [Dell ntoskrnl guide](/articles/how-to-fix-ntoskrnl-high-cpu-usage-on-dell-laptop/) shows the same test pattern for Dell's utilities.

1. Fully exit Armoury Crate from the system tray.
2. Stop ASUS services in services.msc.
3. Watch System CPU for 10 minutes.
4. If it drops: clean-reinstall Armoury Crate.

### Fix 2: Identify the driver with LatencyMon

If Crate wasn't it, get scientific. Download LatencyMon, run as administrator, and monitor 10–15 minutes during high CPU. The Drivers tab names the worst DPC offender explicitly — write down the .sys filename. On ASUS machines the answer is frequently an ASUS-branded .sys, a Realtek audio driver, or the Wi-Fi driver. This named target focuses every step below; without it you're guessing. The [Acer ntoskrnl troubleshooting guide](/articles/how-to-fix-ntoskrnl-high-cpu-usage-on-acer-laptop/) uses the same tool-first approach.

1. Run LatencyMon as administrator for 10–15 minutes.
2. Read the Drivers tab for the top offender.
3. Record the exact .sys filename.
4. Map it to its hardware vendor.

### Fix 3: Update ASUS drivers from ASUS, not Windows Update

Get drivers from ASUS's official support site for your exact model: chipset, ATK package, audio, Wi-Fi, and the ASUS System Control Interface. ASUS tunes these for your hardware; Windows Update's generic versions are a common source of the DPC problems you're seeing. Install chipset first, reboot, then the rest one by one, re-checking System CPU after each. For Intel-based ASUS laptops, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) fills gaps in chipset and wireless drivers.

1. Download model-specific drivers from ASUS official support.
2. Install chipset first, reboot, then the rest one by one.
3. Re-check System CPU after each install.
4. Use Intel DSA for Intel chipset/wireless gaps.

### Fix 4: Update the ASUS BIOS

ASUS BIOS updates regularly fix the ACPI and interrupt-routing bugs that present as ntoskrnl CPU — particularly when the problem started after a Windows feature update changed how the OS talks to firmware. Download the BIOS for your exact model from ASUS support, update via EZ Flash in the BIOS (on AC power, laptop plugged in, do not interrupt), and load optimized defaults afterward. This is safe when done by the book, and it resolves a class of kernel CPU issues no driver update can touch.

1. Download the correct BIOS for your exact ASUS model.
2. Update via EZ Flash on AC power without interruption.
3. Load optimized defaults after the update.
4. Verify System CPU at idle.

### Fix 5: Isolate USB devices and test RAM

Unplug everything USB — docks, hubs, external drives, adapters — and watch System CPU for 10 minutes. ASUS laptops with USB-C docks are prime candidates for interrupt spam from marginal dock hardware; reconnect one device at a time to find it. Separately, run **Windows Memory Diagnostic** with a full pass: failing RAM forces the kernel's memory manager into expensive error handling that looks exactly like driver DPC load. Replace faulty sticks. Microsoft documents both diagnostics in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Unplug all USB devices; observe for 10 minutes.
2. Reconnect one at a time, watching for the spammer.
3. Run Windows Memory Diagnostic, full pass.
4. Replace any failing RAM.

### Fix 6: Clean-boot and repair system files

Last sweep: clean-boot via **msconfig** (hide Microsoft services, disable the rest) to catch third-party kernel filter drivers — VPN clients, antivirus, disk tools — generating the load. Re-enable in halves if it fixes things. Then run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow` elevated to repair corrupted system components, since damaged kernel-adjacent files cause retry loops indistinguishable from driver storms. Reboot, re-run LatencyMon, and confirm DPC latency is back to normal.

1. Clean-boot to isolate filter drivers.
2. Re-enable in halves if successful.
3. Run DISM and SFC repairs elevated.
4. Confirm with LatencyMon.

## Closing

On ASUS laptops, ntoskrnl CPU usually speaks with an ASUS accent — Armoury Crate drivers, ASUS system components, or bundled Wi-Fi/audio drivers. Test Crate first, name the driver with LatencyMon, update from ASUS directly, and don't forget the BIOS. The kernel is just the messenger; once the driver behaves, the message stops. Keep LatencyMon's results saved with the date — if the problem ever returns after an update, you'll know within minutes whether it's the same driver or a new one.
