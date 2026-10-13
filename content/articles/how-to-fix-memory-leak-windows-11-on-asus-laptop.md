---
title: "Windows 11 Memory Leak on an ASUS Laptop? Find the Culprit"
slug: how-to-fix-memory-leak-windows-11-on-asus-laptop
date: 2026-09-20
categories: ["performance"]
tags: ["memory leak", "windows 11", "asus laptop", "high ram usage", "armoury crate"]
description: "RAM filling up on your ASUS laptop with no explanation? Track the leaking ASUS service or driver with Task Manager and PoolMon, then stop it."
thumbnail: "/images/thumbs/how-to-fix-memory-leak-windows-11-on-asus-laptop.webp"
faqs:
  - q: "Which ASUS software is known to leak memory?"
    a: "The usual suspects are Armoury Crate (especially its background services and lighting control), ASUS System Control Interface components, MyASUS background tasks, and older versions of ASUS Precision Touchpad or audio drivers. Armoury Crate is the most frequently reported: its service processes have shown slow user-mode leaks in several versions, where memory climbs a few megabytes per hour until the system feels sluggish. Updating Armoury Crate or removing it entirely resolves most ASUS-specific cases."
  - q: "Should I just uninstall Armoury Crate?"
    a: "If you don't use its features — fan profiles, RGB lighting, game profiles — uninstalling is the cleanest fix and many users report immediate stability. But Armoury Crate also controls fan curves and power profiles on ROG and TUF models, so removing it can leave fans on default behavior. A middle path: update to the latest version first and disable its background extras (in-app lighting, news feeds); uninstall only if the leak persists or you genuinely don't need it."
  - q: "How can I tell a real leak from Windows just using RAM?"
    a: "Windows 11 uses free RAM for caching and releases it on demand, so high usage alone proves nothing. The leak test: reboot, record Task Manager's committed memory and non-paged pool size, then use the laptop normally for a few hours without opening new programs. If committed memory climbs steadily and never returns — particularly the non-paged pool growing into gigabytes — that's a genuine leak. Stable-but-high usage is just caching."
  - q: "Do ASUS BIOS updates fix memory leaks?"
    a: "Sometimes. ASUS BIOS/UEFI updates have fixed firmware-level issues that manifest as kernel memory growth — particularly around USB power management, the embedded controller, and sleep/wake handling. If your leak correlates with sleep cycles or involves the non-paged pool growing after resumes, a BIOS update is worth trying. Always update BIOS from ASUS support for your exact model, on AC power, without interrupting the process."
---

ASUS laptops — especially ROG and TUF gaming lines — ship with one of the heaviest factory software stacks in the industry. Armoury Crate, MyASUS, ASUS System Control Interface, lighting services, update checkers: it's a lot of background machinery, and when any piece of it leaks memory, your RAM graph becomes a slow uphill climb that ends in stutters, frozen apps, and eventually a forced reboot. The pattern is unmistakable: fine after boot, worse every hour, fixed (temporarily) by restarting.

The diagnostic approach is the same as any memory leak — confirm growth over time, identify whether it's user-mode or kernel-mode, then name the process — but the suspect list is ASUS-flavored. Armoury Crate services, ASUS update components, and the occasional ASUS audio or touchpad driver top it. Let's work through it.

Start with the leak test: reboot, note Task Manager > **Performance** > **Memory** > **Committed** and **Non-paged pool**, then check again after 2–3 hours of normal use. Growing pool means a driver; growing committed with a stable pool means an app or service. For the Dell-flavored version of this hunt, see our [Dell memory leak guide](/articles/how-to-fix-memory-leak-windows-11-on-dell-laptop/); if kernel CPU is spiking too, the [ntoskrnl walkthrough](/articles/how-to-fix-ntoskrnl-high-cpu-usage-on-windows-11/) pairs well.

## Why this happens

- **Armoury Crate service leaks**: Background services (ArmouryCrate.Service, lighting control) slowly growing over hours.
- **MyASUS background tasks**: Update checkers and telemetry tasks with unbounded memory growth in some versions.
- **ASUS System Control Interface**: The driver bridging ASUS hotkeys/fan control, occasionally leaking kernel pool.
- **Sonic Studio / audio drivers**: ASUS audio enhancements leaking per-stream allocations.
- **Aura lighting services**: RGB control services polling hardware in a leaky loop.
- **Generic Windows culprits**: SysMain over-caching, stuck Search indexer, third-party antivirus filters — ASUS machines get these too.
- **Browser/extension leaks**: Unrelated to ASUS but the most common user-mode leaker on any laptop.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the leak and classify it

Evidence first, uninstalls later.

1. Reboot, open **Task Manager** > **Performance** > **Memory**, and record **Committed** and **Non-paged pool** values.
2. Use the laptop normally for 2–3 hours, then compare. Growing non-paged pool = kernel/driver leak (go to Fix 5). Growing committed with stable pool = user-mode leak (continue here).
3. In **Processes**, sort by Memory and watch for the steady climber — note whether it's an ASUS process (ArmouryCrate, ASUSOptimization, MyASUS) or something else.
4. Check the **Details** tab with the **Handles** column added — leaking handles alongside memory confirms the suspect.
5. Screenshot the numbers; you'll need the before/after to prove each fix worked.

### Fix 2: Update or tame Armoury Crate

The number-one ASUS suspect gets attention first.

1. Open **Armoury Crate** > **Settings** > **About** > **Check for updates** — install every pending Armoury Crate, ASUS System Control Interface, and firmware update it offers.
2. Inside Armoury Crate, disable extras you don't use: **Aura Sync** lighting effects (set to static or off), news/content feeds, and game library scanning.
3. Test for a few hours. If the leak persists, do a clean reinstall: uninstall Armoury Crate via **Settings** > **Apps**, reboot, then install the latest version from ASUS's official support site for your exact model.
4. After reinstalling, re-test for half a day before deciding — a fresh install with updated components resolves most residual leaks.
5. If you don't need fan profiles or RGB at all, uninstall Armoury Crate and skip to Fix 4's alternative fan control — many users never look back.

### Fix 3: Audit MyASUS and ASUS background tasks

Trim the factory background fleet.

1. Open **MyASUS** > check for updates, then review its settings — disable **automatic checkups**, promotional notifications, and background optimization features you don't use.
2. Open **Task Scheduler** (`taskschd.msc`) > **Task Scheduler Library** > **ASUS** and review the tasks: update checkers and telemetry tasks running hourly are candidates to disable.
3. Disable (don't delete) tasks one at a time — right-click > **Disable** — and observe memory over a few hours between changes.
4. In **Settings** > **Apps** > **Installed apps**, review ASUS entries: **ASUS Product Registration**, **ASUS Smart Display Control**, promo apps — uninstall what you never open.
5. Keep **ASUS System Control Interface** and chipset drivers; remove only the user-facing utilities.

### Fix 4: Replace Armoury Crate fan control if you uninstall it

Don't lose thermal control when removing the leaker.

1. Before uninstalling Armoury Crate, note your current fan profile — after removal, fans fall back to BIOS-controlled curves, which are safe but less aggressive.
2. Check your BIOS (F2/Del at boot) for **fan curve** or **thermal policy** settings — many ASUS BIOSes let you set performance/silent profiles directly.
3. For granular control without Armoury Crate, **G-Helper** (open-source, lightweight) replaces fan control, power profiles, and keyboard backlight on ASUS laptops with a fraction of the footprint.
4. Monitor temperatures with **HWiNFO64** for a day after switching to confirm cooling is adequate under load.
5. If temperatures are fine, you've traded a leaky 500MB suite for a 10MB tool — a clear win.

### Fix 5: Use PoolMon for kernel-mode leaks

When the non-paged pool grows, find the driver.

1. Install **PoolMon** from the Windows Driver Kit/SDK and run `poolmon.exe -b` from an elevated prompt, sorted by bytes.
2. Watch for a climbing **Tag** — note it and search the tag to identify the driver (ASUS audio, network, and USB drivers have all appeared here).
3. Update the identified driver from ASUS support for your exact model — not from Windows Update, which may serve an older build.
4. For ASUS audio leaks specifically, also try disabling audio enhancements: speaker icon > **Sound settings** > device > **Audio enhancements** off.
5. Re-observe the pool for 2–3 hours to confirm stability.

### Fix 6: Tame Windows' own memory consumers

ASUS machines suffer the generic Windows leaks too.

1. Disable **SysMain** temporarily (`services.msc` > Disabled) and observe — a corrupt prefetch cache can mimic a leak.
2. Rebuild the search index (**Indexing Options** > **Advanced** > **Rebuild**) if SearchIndexer.exe is the grower.
3. Check third-party antivirus: update it, or test with real-time protection briefly disabled (offline) to see if its filter driver is the leaker.
4. Audit browser extensions in groups — disable all, then re-enable one group per day to find the leaky one.
5. Use **RAMMap** (Sysinternals) to see exactly where memory is going when Task Manager's totals don't add up.

### Fix 7: Update BIOS and repair Windows

Firmware and system corruption are the last suspects.

1. Check ASUS support for a **BIOS update** for your exact model — install on AC power, don't interrupt. Firmware fixes for EC and USB power management have resolved pool leaks.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt.
3. Install all pending Windows updates — cumulative updates have patched several Windows 11 memory leaks; grab specific KBs from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update stalls.
4. Do a **clean boot** (`msconfig`, hide Microsoft services, disable all) and bisect startup items to isolate any remaining user-mode leaker definitively.
5. If the clean boot is stable for 48 hours, the leaker is in your startup set — keep bisecting until it's named, then update or remove it.

## Closing

On ASUS laptops, memory leaks usually have the ASUS logo on them — Armoury Crate's background services are suspect number one, followed by MyASUS tasks and ASUS drivers. Confirm the leak with the before/after pool test, update or remove the ASUS component responsible, and don't forget the generic Windows culprits that affect every brand. Your RAM should stay flat across a full day of use; anything else means something is still leaking, and now you know how to catch it.
