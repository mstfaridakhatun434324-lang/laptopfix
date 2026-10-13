---
title: "MEMORY_MANAGEMENT Blue Screen on Windows 11: Causes and Fixes"
slug: stop-code-memory-management-bsod-windows-11
date: 2026-10-07
categories: ["windows-errors"]
tags: ["memory-management", "windows-11", "bsod"]
description: "The MEMORY_MANAGEMENT blue screen on Windows 11 usually means bad RAM or a driver corrupting memory. Here are the Windows 11-specific fixes in order."
thumbnail: "/images/thumbs/stop-code-memory-management-bsod-windows-11.webp"
faqs:
  - q: "Why does MEMORY_MANAGEMENT happen more after upgrading to Windows 11?"
    a: "Windows 11 enables memory integrity (HVCI) and other virtualization-based security features that stress the memory subsystem harder. A marginal RAM stick or sloppy driver that got away with bad behavior on Windows 10 gets caught on Windows 11 — the stricter checking exposes the weakness."
  - q: "Does Windows 11's memory integrity feature cause this BSOD?"
    a: "It can expose it, but it does not cause it. Memory integrity makes the kernel check memory operations more rigorously, so a driver that was silently corrupting memory on Windows 10 now triggers the stop code. The driver was always broken; Windows 11 just notices."
  - q: "Is this error common on new Windows 11 laptops?"
    a: "Not from the factory — new laptops with this error almost always have a genuinely defective RAM stick or SSD, which is a warranty issue. If your brand-new machine blue-screens with 0x1A, contact the manufacturer rather than spending days troubleshooting."
  - q: "Can a Windows 11 update fix MEMORY_MANAGEMENT?"
    a: "Cumulative updates sometimes include fixes for known driver conflicts, so staying updated is worthwhile. But updates cannot fix failing RAM or a third-party driver that corrupts memory — those need the hardware and driver steps below."
---
Windows 11 did not invent the MEMORY_MANAGEMENT blue screen, but its stricter memory protections mean marginal hardware and sloppy drivers get caught more often than they did on Windows 10. If this crash started after your upgrade, that is probably why. Windows 11 did not invent the MEMORY_MANAGEMENT blue screen, but its stricter memory protections mean marginal hardware and sloppy drivers get caught more often than they did on Windows 10. The stricter checking is genuinely good for stability — it just finds your weakest component sooner.

The fixes below are tuned for Windows 11 specifically — its security features, its driver model, and the places its settings live. The underlying causes are the same old ones: RAM, drivers, and corrupted files. The fixes below are tuned for Windows 11 specifically — its security features, its driver model, and where its settings live. The underlying causes are the same old ones: RAM, drivers, and corrupted files.

## Why this happens

- **Faulty RAM exposed by stricter checks.** Windows 11's memory integrity catches corruption Windows 10 let slide.
- **An incompatible driver.** Old drivers written for Windows 10 corrupt memory under Windows 11's hardened kernel.
- **Memory integrity conflicts.** The HVCI feature itself can clash with certain drivers, especially older storage and antivirus filters.
- **Corrupted system files after the upgrade.** The Windows 10-to-11 upgrade can leave damaged components behind.
- **Failing SSD.** Windows 11 leans harder on fast storage; a degrading drive corrupts cached memory pages.
- **Bad Windows 11 feature update.** A problematic 22H2/23H2/24H2 update can introduce the instability itself.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Check Memory integrity and test RAM

Windows 11's own security feature helps you triage: and the RAM test is still step one. If Memory integrity was already off and Windows names an incompatible driver, write down that driver name — it is a free suspect handed to you by the OS.

1. Press **Win + R**, type `mdsched.exe`, press **Enter**, and choose **Restart now and check for problems**.
2. While you are at it, check **Windows Security > Device security > Core isolation** — note whether **Memory integrity** is on.
3. If the RAM test finds errors, replace the stick. If it passes, try toggling Memory integrity off temporarily: if crashes stop, a driver is incompatible with HVCI — update that driver rather than leaving security off.

### Fix 2: Update every driver through Windows Update and your maker

Windows 11 driver mismatches are the top software cause. The Optional updates section is where Windows 11 hides most driver updates — the main update page alone will miss them.

1. Go to **Settings > Windows Update** and install everything, then check **Advanced options > Optional updates** for driver updates.
2. Next, visit your laptop maker's support site for Windows 11-specific chipset and graphics drivers — [Lenovo Support](https://support.lenovo.com/us/en/), [Dell Support](https://www.dell.com/support), or [HP Support](https://support.hp.com/us-en).
3. Pay special attention to storage controller and BIOS updates; both affect memory behavior on Windows 11.
4. Restart after each major driver install rather than batching them, so you know which one mattered.

### Fix 3: Run SFC and DISM

Standard corruption repair, still effective on Windows 11. On Windows 11, run these from Terminal (Admin) rather than the old Command Prompt — same tools, but Terminal is the supported path going forward.

1. Open **Terminal (Admin)** (**Win + X > Terminal (Admin)**).
2. Run `sfc /scannow` and let it complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. On upgrade-installed systems this fixes a large share of 0x1A crashes.

### Fix 4: Use Driver Verifier to catch the bad driver

When dumps keep naming different files, Verifier forces the real culprit to reveal itself. Verifier on Windows 11 with HVCI enabled can be extra crash-happy — that is expected, and it is why you turn it off the moment you have your answer.

1. Press **Win + R**, type `verifier`, and press **Enter**.
2. Select **Create standard settings**, then **Select driver names from a list**, and check all non-Microsoft drivers.
3. Restart and use the PC normally. The next crash will name the offending driver explicitly.
4. When done, run `verifier /reset` in an elevated prompt to turn it off. Read Microsoft's official guidance on Driver Verifier settings first if you have never used the tool.

### Fix 5: Check SSD health

Windows 11's memory compression and paging punish a failing SSD, and the corruption surfaces as 0x1A. Windows 11's compressed-memory feature involves the SSD in memory management far more than Windows 10 did — a marginal drive that was 'fine' before gets exposed here.

1. In an elevated **Terminal**, run `wmic diskdrive get status` — anything but OK is a red flag.
2. Run `chkdsk C: /f` and reboot to let it scan.
3. Install your SSD maker's toolbox (Samsung Magician, WD Dashboard, Crucial Storage Executive) for a detailed health read.
4. If health is below 80% or reallocated sectors are climbing, clone to a new drive — our [unexpected store exception guide](/articles/unexpected-store-exception-windows-11-fix/) covers storage-related crashes in depth.

### Fix 6: Uninstall the latest feature update if it started there

A bad 24H2-style update can be the entire story. Use the Uninstall updates page rather than System Restore for this — it targets exactly the update without rolling back your drivers and programs.

1. Go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent feature or quality update from just before the crashes began.
3. Restart and monitor for 48 hours. If stable, pause updates for two weeks while Microsoft ships a fix.
4. Reinstall drivers afterward, since rolling back an update can leave driver mismatches. For reading the resulting screens, our [guide to disabling auto-restart](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) helps you capture the stop code.

## Closing

On Windows 11, MEMORY_MANAGEMENT is usually the operating system's stricter memory policing catching hardware or drivers that were always marginal. Test the RAM, bring every driver up to Windows 11-native versions, and repair the system files — that combination ends the overwhelming majority of these crashes. Keep Memory integrity enabled once the culprit driver is updated — it is one of Windows 11's best defenses, and disabling it permanently to dodge a driver bug trades security for convenience.
