---
title: "Windows 11 Slow Boot? Fix It Step by Step (From 3 Minutes to 30 Seconds)"
slug: "how-to-fix-windows-11-slow-boot-step-by-step"
date: "2026-09-02"
categories: ["performance"]
tags: ["slow boot", "windows 11", "boot time", "startup", "fast startup"]
description: "Windows 11 taking minutes to boot? Follow this step-by-step boot-time rescue — measure first, then trim startup, drivers, and services in order."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-boot-step-by-step.webp"
faqs:
  - q: "What is a normal boot time for Windows 11?"
    a: "On a modern SSD, Windows 11 should go from power button to usable desktop in 20-45 seconds; NVMe drives often do it in 15-25. On a mechanical HDD, 60-120 seconds is typical and anything under 2 minutes is acceptable for the hardware. If your SSD system takes over a minute, or your HDD system takes over 3 minutes, something specific is wrong — usually startup programs, a driver timeout, or Fast Startup preserving a bad state."
  - q: "Does Fast Startup make boot faster or slower?"
    a: "Both, depending on the situation. Fast Startup (hybrid shutdown) genuinely speeds up boot-from-shutdown on HDDs by hibernating the kernel session — often cutting 20-40 seconds. But it can also preserve corrupted driver states across shutdowns, causing slow or buggy boots that a true restart wouldn't have. If boots are slow and erratic, disabling Fast Startup to force true cold boots is a valid diagnostic — on SSDs the speed difference is negligible anyway."
  - q: "Why is my boot slow only sometimes?"
    a: "Intermittent slow boots trace to intermittent causes: Windows Update finishing installs on shutdown/startup, a USB device that's slow to enumerate (or a failing one retrying), network logon delays on domain machines, or antivirus doing a boot-time scan on its own schedule. Note what differs on slow days — a plugged-in external drive, pending updates, being on VPN — and the pattern names the cause."
  - q: "Will disabling startup programs break anything?"
    a: "Disabling a startup entry never uninstalls or breaks the program — it just stops it launching automatically at sign-in; you can still open it manually anytime. The only entries to leave enabled are security software and hardware utilities (audio, touchpad, graphics control panels). If you disable something and miss it, re-enable it in Task Manager's Startup tab in ten seconds. It's the safest performance tweak in Windows."
---

Three minutes from power button to a usable desktop. That's the complaint — and on a machine that used to boot in thirty seconds, it's infuriating. Slow boot has a finite set of causes, and unlike many performance problems, it's highly measurable: you can time each phase and see exactly where the seconds go.

Boot time breaks into phases: firmware/POST (your laptop's logo screen), the Windows loading phase, and the sign-in-to-usable-desktop phase where startup programs pile on. Each phase has different culprits — BIOS settings, driver timeouts, and startup bloat respectively. Timing which phase is slow tells you where to work, which is why this guide starts with measurement, not tweaks.

Work it step by step, timing as you go — most slow boots are fixed by Step 3. If apps are slow after boot completes (a different problem), our [slow app launch guide](/articles/how-to-fix-apps-opening-slowly-on-windows-11/) takes over where this one ends.

## Why this happens

- **Startup program pile-up** — The dominant cause of slow sign-in-to-desktop: dozens of auto-starting apps (updaters, launchers, chat clients) serializing their launches — each adding seconds.
- **Fast Startup preserving bad state** — Hybrid shutdown hibernates driver state; corrupted preserved state makes every 'shutdown' boot slow until a true restart clears it.
- **Driver/service timeouts** — A driver waiting on a timeout (network, storage, disconnected device) stalls the boot sequence — visible as a long black screen or spinning dots.
- **Slow USB device enumeration** — External drives, docks, and even failing flash drives delay POST and Windows device enumeration — unplug to test in seconds.
- **Mechanical HDD** — Boot is random-read heavy; HDDs simply take 2-4x longer than SSDs through every boot phase — the hardware baseline.
- **Bloated user profile** — Enormous desktops (thousands of icons/files), huge Startup folders, and corrupted profile hives slow the sign-in phase specifically.
- **Pending updates finishing** — 'Working on updates' boots are one-time costs — but a stuck update retrying every boot is a recurring one.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Step 1: Time your boot phases

You can't fix what you don't measure.

1. Time a full boot with your phone: power button to login screen (Phase 1+2), then login to usable desktop (Phase 3).
1. Phase 1+2 slow (long logo/spinning dots) = firmware or driver issue — focus on Steps 5-6. Phase 3 slow (desktop appears but unusable) = startup bloat — Step 2 is your fix.
1. Check **Task Manager > Startup apps > Last BIOS time** — the firmware duration in seconds; over 20s suggests BIOS-level delays.
1. Write down your baseline — you'll compare after each fix.

### Fix 2: Step 2: Gut the startup list

The highest-yield boot fix for Phase-3 slowness.

1. Open Task Manager (**Ctrl + Shift + Esc**) > **Startup apps**, sort by **Startup impact**.
1. **Disable** everything High/Medium impact except security software and hardware utilities (audio, touchpad, graphics).
1. Check the hidden **Startup** folders too: `shell:startup` (your user) and `shell:common startup` — remove shortcuts you don't need.
1. Restart and re-time Phase 3 — most users cut it by half or more here.

### Fix 3: Step 3: Toggle Fast Startup deliberately

Test both states — the right answer depends on your machine.

1. **Control Panel > Power Options > Choose what the power buttons do > Change settings that are currently unavailable**.
1. If Fast Startup is ON: turn it OFF, shut down fully, cold boot, and time it — on SSDs this is often as fast and far more reliable.
1. If it was OFF: turn it ON and compare — on HDDs it genuinely saves 20-40 seconds per boot.
1. Keep whichever is faster AND stable on your hardware; retest after major updates since updates reset it.

### Fix 4: Step 4: Unplug USB devices and test

The 30-second diagnostic everyone skips.

1. Shut down, unplug everything USB except keyboard/mouse (docks, external drives, hubs, printers), and boot.
1. If boot is dramatically faster, one of those devices is stalling enumeration — reconnect one at a time to find it.
1. A failing external drive is the classic: it retries reads during boot and Windows waits.
1. Update the dock's firmware/drivers if a dock is the culprit — or leave it unplugged until after boot.

### Fix 5: Step 5: Update BIOS and chipset drivers

For slow Phase 1+2 (logo screen, spinning dots).

1. Check **Last BIOS time** in Task Manager — if it's high, enter BIOS/UEFI and disable: **network boot (PXE)**, **USB legacy boot** ordering before SSD, and unused **SATA ports**.
1. Update the BIOS from your maker's support page ([Dell](https://www.dell.com/support), HP, or [Lenovo](https://support.lenovo.com/us/en/)) — changelogs often mention boot-time improvements.
1. Update the chipset driver from the same page — boot driver timeouts often trace to old chipset drivers.
1. Each change: re-time the boot. BIOS tweaks are the lever for logo-screen slowness.

### Fix 6: Step 6: Clean up the profile and check the drive

For slow sign-in with a clean startup list.

1. Declutter the desktop to a handful of shortcuts — thousands of desktop items measurably slow sign-in.
1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` to fix corrupted profile/system hives.
1. Check drive health (CrystalDiskInfo) — a struggling drive slows every boot phase; our [100% disk guide](/articles/best-way-to-fix-disk-active-time-100-percent/) covers the disk side.
1. If the boot drive is an HDD, the SSD upgrade in that guide is the permanent fix — boot times typically drop 60-70%.

### Fix 7: Step 7: Reset or clean-install (last resort)

When the software stack is the problem and nothing else worked.

1. First try **Settings > System > Recovery > Reset this PC** (keep files) — faster than a full reinstall and fixes most software-caused slow boots.
1. If the reset doesn't help, clean-install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — the definitive software answer.
1. Time the clean install's boot before reinstalling apps — that's your hardware's true baseline; add apps back gradually.
1. Microsoft's Windows support hub walks through recovery options officially.

## Closing

Slow boot is a measurement problem first: time the phases, then fix the slow one — startup bloat for Phase 3, drivers and BIOS for Phases 1-2. Most boots are rescued by Step 2 alone. And if the drive is mechanical, know that every software fix is fighting the hardware — the SSD is the finish line.
