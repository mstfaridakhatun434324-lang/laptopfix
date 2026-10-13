---
title: "System Interrupts High CPU After a Windows 11 Update? Fix It"
slug: how-to-fix-system-interrupts-high-cpu-after-windows-11-update
date: 2026-10-08
categories: ["performance"]
tags: ["system interrupts", "high cpu", "windows 11 update", "driver issue"]
description: "System Interrupts spiking CPU after a Windows 11 update? Trace the interrupt storm to the updated driver or device and fix it."
thumbnail: "/images/thumbs/how-to-fix-system-interrupts-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "Why would a Windows update cause high System Interrupts?"
    a: "Updates replace drivers — storage controllers, Wi-Fi, chipset, USB — with new versions, and a buggy or mismatched driver can mishandle hardware interrupts, making a device signal the CPU thousands of times per second. Updates also change power-management behavior, and drivers that misbehave in the new power states generate interrupt storms during sleep/wake transitions. The update didn't damage hardware; it changed the software talking to it."
  - q: "How do I find which driver is causing the interrupts?"
    a: "Use LatencyMon (free): run it for 5–10 minutes during the problem and sort its Drivers tab by ISR and DPC counts — the top entries name the exact driver file (like storport.sys, ndis.sys, or a vendor driver). That filename maps to a device class: storage, network, USB, or audio. Windows Performance Recorder with Windows Performance Analyzer gives the same answer with more detail if you prefer Microsoft's own tools."
  - q: "Should I roll back the update or the driver?"
    a: "Roll back the driver first — it's targeted and preserves the update's security fixes. In Device Manager, open the suspect device's Properties > Driver tab and use Roll Back Driver if the update changed it. Only consider rolling back the Windows update itself if multiple drivers are implicated or the interrupt storm affects core chipset functions that no driver version fixes. Driver rollback solves the majority of post-update interrupt cases."
  - q: "Can System Interrupts high CPU go away on its own?"
    a: "Sometimes — if the cause is a one-time post-update activity (like a firmware update finalizing or a device re-enumerating), it settles within hours. But a driver bug doesn't heal with time; if System Interrupts is still elevated 24–48 hours after the update with no active update work happening, it's not going away alone. Diagnose it with LatencyMon rather than waiting indefinitely."
---

A Windows 11 update finishes, you reboot — and now "System Interrupts" is eating 10–25% CPU constantly in Task Manager. Nothing you can end, no program to uninstall. The update swapped drivers underneath your hardware, and one of the new drivers is mishandling interrupts: a device is now shouting at your CPU thousands of times per second, and every shout steals processing time.

The good news about post-update interrupt storms: the cause is software, it started at a known moment, and the prime suspect list is short — whatever drivers the update touched. This guide shows how to identify the offending driver, roll it back or update past the bug, and verify the fix. (For the Dell-specific version with vendor tools, that's a separate guide.) For other post-update CPU issues, see [Windows Modules Installer high CPU](/articles/how-to-fix-windows-modules-installer-high-cpu-on-lenovo-laptop/); for general CPU hogs, [Antimalware Service Executable](/articles/antimalware-service-executable-high-cpu-windows-11/).

## Why this happens

- **Buggy replacement driver**: The update installed a driver version with an interrupt-handling bug.
- **Driver/OS power-state mismatch**: New power management behavior triggers interrupt storms in drivers not updated for it.
- **Firmware/driver version skew**: Updated driver talking to old firmware (or vice versa) miscommunicates via interrupts.
- **Device re-enumeration loops**: The update's hardware rescan leaves a device in a re-enumeration loop.
- **DPC latency from storage drivers**: New StorPort/miniport drivers with DPC bugs show up as System Interrupts.
- **USB host controller driver changes**: Updated USB drivers mishandling connected devices' interrupts.
- **Coincidental hardware failure**: Rare — but updates stress hardware (reboots, firmware flashes), occasionally exposing a device that was about to fail.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the timing and rule out active update work

Make sure the update is truly done.

1. **Settings** > **Windows Update** — confirm no update is downloading, installing, or pending restart. Active setup work raises interrupts legitimately.
2. Note when the interrupts started versus when the update installed (**Update history** timestamps) — same-day onset strongly implicates the update.
3. Watch **System Interrupts** in Task Manager for 5 minutes: constant elevation vs. spikes tied to activity (mouse movement, network use, disk access).
4. If it's been less than 24 hours since the update, give it one overnight plugged-in idle session — finalization activity can elevate interrupts temporarily.
5. Persistent beyond 48 hours with no update activity = diagnose the driver (Fix 2).

### Fix 2: Identify the offending driver with LatencyMon

Get the exact filename.

1. Download and run **LatencyMon** (free from Resplendence) for 5–10 minutes while interrupts are high.
2. Open the **Drivers** tab, sort by **ISR count** (and check **DPC count**) — the top driver is your storm source.
3. Map the filename: `storport.sys`/vendor storage driver = storage; `ndis.sys`/Wi-Fi vendor driver = network; `usbport.sys`/`usbxhci.sys` = USB; `HDAudBus.sys` = audio.
4. Note the driver version — you'll compare against available versions in Fix 3/4.
5. If LatencyMon shows no clear leader, use **Windows Performance Recorder** (`wpr -start CPU -start DPC`) for a 60-second trace and analyze DPC/ISR summary tables.

### Fix 3: Roll back the driver the update changed

The most targeted fix.

1. Open **Device Manager**, find the device class from Fix 2 (e.g., Network adapters for a Wi-Fi storm).
2. Right-click the device > **Properties** > **Driver** tab — check the driver date: if it matches the update day, this is almost certainly it.
3. Click **Roll Back Driver**, choose a reason, and confirm — this restores the pre-update driver.
4. Reboot and watch System Interrupts for 15 minutes — rollback fixes the majority of these cases immediately.
5. Then block the bad driver from reinstalling: **Settings** > **Windows Update** > pause updates briefly, or use the "Show or hide updates" troubleshooter to hide that driver update.

### Fix 4: Update past the bug (when rollback isn't available)

Sometimes forward is the only way.

1. If Roll Back is grayed out, get the newest driver: vendor sites ([Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html)) or your laptop manufacturer's support page.
2. Storage-controller storms: update chipset + Intel RST/AMD chipset drivers from the laptop maker.
3. Wi-Fi storms: Intel cards via Intel DSA; others via the laptop manufacturer's page (Wi-Fi drivers are often model-specific).
4. USB storms: update chipset drivers; disconnect all USB devices first to confirm the storm stops without them.
5. BIOS/firmware: check the manufacturer's support page for updates mentioning interrupt, power, or device-stability fixes — install per their instructions.

### Fix 5: Test hardware by elimination

Rule out the coincidental-failure case.

1. Disconnect all USB devices and docks — if interrupts normalize, reconnect one at a time to find the trigger device.
2. If Wi-Fi is implicated, test with Wi-Fi off (airplane mode) vs. on — and test Ethernet if available.
3. Boot into **Safe Mode** (minimal drivers): if interrupts are normal there, it's definitively a third-party/normal-mode driver, not hardware.
4. Run the manufacturer's built-in diagnostics (F2/F12 at boot on Dell/HP/Lenovo) for a hardware sanity check.
5. Replace the specific failing device (cable, dock, USB peripheral) when elimination points at hardware — interrupt storms from hardware don't respond to software.

### Fix 6: Adjust power management as a workaround

When the storm is power-state-triggered.

1. **Settings** > **System** > **Power & battery** > **Power mode** — test **Best performance**; some interrupt bugs only trigger in low-power states.
2. **Device Manager** > the suspect device > **Properties** > **Power Management** tab — uncheck **Allow the computer to turn off this device to save power** as a test.
3. In **Power Options** > **advanced settings**, disable **USB selective suspend** and set **PCI Express Link State Power Management** to **Off** (plugged in) as diagnostics.
4. If these calm the storm, you've confirmed a power-state driver bug — keep the workaround while reporting it, and retest after each driver update.
5. These are workarounds, not cures — the real fix remains a corrected driver.

### Fix 7: Uninstall the problematic update (last resort)

When the update itself is fundamentally incompatible.

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the KB that started it.
2. First search the KB number + "system interrupts" — if it's a known-bad update with widespread reports, rollback is justified; if you're the only report, prefer driver fixes.
3. Pause updates for 2–3 weeks after uninstalling to avoid immediate reinstallation.
4. Report via **Feedback Hub** with LatencyMon data attached — driver/update regression reports with data get attention.
5. Reinstall once a superseding cumulative update ships; staying unpatched long-term trades one problem for security exposure.

## Closing

Post-update System Interrupts storms are driver regressions with a known birthday: identify the driver with LatencyMon, roll it back (or update past the bug), and verify with the hardware-elimination tests. The update changed the software, not your hardware — so the fix lives in the driver stack, not in a repair shop. And when you find the guilty driver version, blocking its reinstall is as important as the rollback itself.
