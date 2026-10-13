---
title: "Laptop Slow After the Windows 11 24H2 Update? Do This First"
slug: "what-to-do-if-laptop-slow-after-windows-11-24h2-update"
date: "2026-09-04"
categories: ["performance"]
tags: ["windows 11 24h2", "slow after update", "laptop slow", "performance fix", "windows update"]
description: "Your laptop crawls after installing Windows 11 24H2? These are the first things a technician checks — from post-update settling to driver mismatches."
thumbnail: "/images/thumbs/what-to-do-if-laptop-slow-after-windows-11-24h2-update.webp"
faqs:
  - q: "How long should I wait after the 24H2 update before troubleshooting?"
    a: "Give the laptop 24 to 48 hours of normal use, including at least one full shutdown and cold boot. Post-update tasks like search reindexing, .NET optimization, and driver re-detection run in the background and finish on their own. If the machine is still slow after two days of regular use, the slowdown is real and the fixes in this guide apply."
  - q: "Can I uninstall the 24H2 update to get my speed back?"
    a: "Yes, within 10 days of installation via Settings > System > Recovery > Go back. This restores the previous build with your files intact. It is a reasonable fallback if a driver or firmware conflict is clearly tied to 24H2, but try the driver and service fixes first, since rolling back is temporary and the update will eventually be required."
  - q: "Why would a Windows update make my laptop slower?"
    a: "Feature updates reset drivers to generic versions, re-enable disabled services, rebuild the search index, and sometimes introduce new background components like Recall or Copilot hooks on supported hardware. Any one of these can add sustained CPU, disk, or memory load until it is identified and tamed."
  - q: "Will 24H2 slow down older laptops permanently?"
    a: "Not inherently. 24H2's system requirements are the same as Windows 11's, and on healthy hardware with current drivers it performs comparably to 23H2. Persistent slowness after an update is almost always a fixable driver, service, or indexing issue rather than the new build being fundamentally heavier."
---

A major Windows feature update like 24H2 replaces huge parts of the operating system in one shot — drivers, services, the search index, power plans — and any one of them can come back misconfigured. The result is the classic complaint: the laptop was fine on Tuesday, 24H2 installed overnight, and now everything takes twice as long. Before you assume the update itself is bad, understand that most post-update slowdowns are transitional or come from one reverted setting.

The single most important thing to know is that a feature update needs a settling period. For 24 to 48 hours after installation, Windows runs reindexing, .NET native image regeneration, compatibility telemetry, and driver re-detection in the background. During that window the machine will feel slower, and no amount of tweaking shortens it — the work has to finish. Only after that window should you start the diagnostic sequence below.

This guide is ordered the way I triage post-update machines: first verify the settling is done, then check what the update changed (drivers, services, power), then fix the specific offender. Work it in order and you will find the cause instead of guessing.

## Why this happens

- **Background post-update tasks:** Search reindexing, .NET optimization (ngen), and compatibility appraiser runs consume CPU and disk for up to 48 hours after a feature update.
- **Generic drivers replacing vendor drivers:** 24H2 frequently swaps manufacturer-tuned storage, chipset, and GPU drivers for Microsoft's generic versions, which can be measurably slower.
- **Re-enabled services and features:** Services you previously disabled — SysMain, telemetry, Widgets, Copilot hooks — often come back enabled after a feature update.
- **Corrupted update staging:** If the update installed over a damaged component store, the resulting system can exhibit persistent high CPU from servicing processes.
- **Power plan reset:** Feature updates sometimes revert a custom or manufacturer power plan to Balanced, throttling performance on battery and even on AC.
- **Old BIOS/firmware mismatch:** Newer builds expect newer firmware; an outdated BIOS on some laptops causes interrupt storms or broken power management after updating.
- **Antivirus re-registration:** Security products re-register their filters after a build upgrade, sometimes triggering a full re-scan of the drive.
- **Storage driver mode changes:** Rarely, the update flips the storage controller configuration, dropping the SSD out of its optimal mode until the driver is reinstalled.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the settling period is actually over

Do not troubleshoot a machine that is still legitimately busy. Open Task Manager, sort by CPU and Disk, and look for SearchIndexer, .NET Runtime Optimization Service, CompatTelRunner, or TiWorker running hot. If those are active, the update is still settling — let it finish, preferably plugged in and idle overnight. Only proceed when sustained background load has dropped and the laptop is still slow during normal use. Our [post-update troubleshooting checklist](/articles/troubleshoot-laptop-slow-after-windows-11-24h2-update/) covers this waiting game in more depth.

1. Open Task Manager and sort by **CPU**, then by **Disk**.
2. Note any of: SearchIndexer, ngen/MSCorSvc, CompatTelRunner, TiWorker.
3. If they are active, leave the laptop plugged in and idle for several hours.
4. Reassess only after background load has been quiet for a full day of use.

### Fix 2: Check what the update did to your drivers

The most common real cause of post-24H2 slowness is driver regression. Open Device Manager and look for warning icons, then compare driver dates on the storage controller, display adapter, and chipset against what the manufacturer offers. Pay special attention to the GPU: 24H2 is known to replace vendor GPU drivers with older Microsoft ones on some laptops. Reinstall the manufacturer's driver pack from the official support site for your exact model.

1. Press **Win + X** and open **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers**, **Display adapters**, and **System devices**; note any yellow warnings.
3. Download the latest chipset, storage, and GPU drivers from your manufacturer's support site.
4. Install them, restart, and compare responsiveness.

### Fix 3: Re-disable the services the update re-enabled

Feature updates are notorious for resurrecting services users had disabled. Check SysMain, Windows Search (if you had it off), and the Widgets/ Copilot background components. On many machines, simply re-applying the pre-update service configuration restores the old performance. If SysMain is the offender, our [SysMain high disk usage guide](/articles/how-to-fix-sysmain-high-disk-usage-in-windows-11-24h2/) has the full disable sequence.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Check **SysMain**, **Windows Search**, and any telemetry services you previously disabled.
3. Set offenders back to **Disabled** and stop them.
4. Restart and measure the difference.

### Fix 4: Verify your power plan survived the update

24H2 sometimes resets power plans, and a laptop dropped to Power Saver — or a Balanced plan with aggressive processor throttling — feels dramatically slower. Open **Settings > System > Power & battery** and confirm the power mode is **Best performance** while you test. On gaming and workstation laptops, also check the manufacturer's control app (Lenovo Vantage, HP OMEN Hub, Dell Power Manager), which the update may have reset to a quiet/eco profile.

1. Open **Settings > System > Power & battery**.
2. Set **Power mode** to **Best performance** (plugged in).
3. Open your manufacturer's control app and check its thermal/performance profile.
4. Retest with the charger connected.

### Fix 5: Run the update troubleshooter and repair the component store

If servicing processes (TiWorker, TrustedInstaller) never settle, the component store may be damaged. Run DISM to repair it and SFC to fix protected files — this resolves the class of problems where the update installed "successfully" but left the servicing stack in a loop. Microsoft documents these repair tools on the official [Windows support hub](https://support.microsoft.com/en-us/windows). If the troubleshooter finds and fixes update errors, let Windows Update run a full check afterward.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Windows Update**.
2. Open **Command Prompt as administrator** and run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Follow with `sfc /scannow` and restart.
4. Check Task Manager to confirm servicing processes have settled.

### Fix 6: Update the BIOS and firmware

When everything else checks out but the machine still drags, firmware is the next suspect. 24H2 changed low-level power and security interfaces, and vendors released BIOS updates to match. An outdated BIOS can cause exactly the vague, system-wide sluggishness people blame on the update itself. Check your manufacturer's support page for a BIOS newer than your current version — and read the release notes for mentions of 24H2 or Windows 11 compatibility.

1. Check your current BIOS version with `msinfo32` (System Information).
2. Compare it against the latest on your manufacturer's support site.
3. Apply the BIOS update with the charger connected and the battery charged.
4. Reset BIOS to optimized defaults afterward if behavior is odd.

### Fix 7: Roll back as a last resort

If you have identified nothing fixable and the 10-day rollback window is still open, going back to the previous build is legitimate triage — it tells you definitively whether 24H2 is the trigger. Use **Settings > System > Recovery > Go back**. Before you do, create a full backup, because while rollback preserves files, things can go wrong. Note the rollback is temporary: Windows will eventually require the newer build, so use the time to research the specific incompatibility.

1. Back up important files to external storage.
2. Go to **Settings > System > Recovery > Go back** and follow the prompts.
3. Confirm performance returns on the old build.
4. Research the incompatibility (usually a driver) before allowing the update again.

## Closing

Post-24H2 slowness is frustrating precisely because the trigger is obvious but the cause is not — and in most cases the cause is something the update changed rather than the update itself. Give it the settling period it needs, then work the list: drivers, re-enabled services, power plans, and firmware. One of those is almost always the answer.
