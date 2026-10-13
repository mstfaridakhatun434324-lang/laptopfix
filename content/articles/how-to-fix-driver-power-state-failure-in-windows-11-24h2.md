---
title: "DRIVER_POWER_STATE_FAILURE on Windows 11 24H2: Fixed"
slug: how-to-fix-driver-power-state-failure-in-windows-11-24h2
date: 2026-10-09
categories: ["windows-errors"]
tags: ["windows 11", "blue screen", "power management", "drivers"]
description: "DRIVER_POWER_STATE_FAILURE crashing your Windows 11 24H2 laptop on sleep or shutdown? Here's how to find the driver that won't power down."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-in-windows-11-24h2.webp"
faqs:
  - q: "What causes DRIVER_POWER_STATE_FAILURE?"
    a: "A driver fails to complete a power-state transition — usually going to sleep or waking up — within the time Windows allows. The classic scenario: you close the lid or press sleep, a driver hangs instead of powering down, and Windows blue-screens. Wi-Fi, Bluetooth, and graphics drivers are the usual suspects."
  - q: "Why did this start after updating to Windows 11 24H2?"
    a: "The 24H2 update reworked parts of the power management stack and shipped new driver versions. A driver that handled sleep fine under 23H2 can time out under 24H2's stricter power sequencing. Updating that driver — or rolling it back — resolves most post-24H2 cases."
  - q: "Is it safe to disable Fast Startup to fix this?"
    a: "Yes, completely safe. Disabling Fast Startup just means shutdowns do a full kernel reload instead of hibernating the kernel. Boot times get a few seconds longer, but sleep/wake reliability often improves dramatically. You can re-enable it any time from Power Options."
  - q: "How do I find which driver is failing the power transition?"
    a: "Check the minidump with BlueScreenView — the faulting driver is highlighted. You can also run powercfg /energy in an elevated Command Prompt to generate a report flagging devices with power policy problems, or check Event Viewer for Kernel-Power events around the crash time."
---

DRIVER_POWER_STATE_FAILURE on Windows 11 24H2: Fixed

Here's the scene: you close your laptop lid, or hit sleep, or shut down for the night — and instead of a quiet power-down, you get a blue screen. DRIVER_POWER_STATE_FAILURE is Windows telling you that a driver refused to go to sleep (or wake up) in time, so Windows crashed rather than leave hardware in an unknown state. Since the Windows 11 24H2 update, this one has been showing up a lot, because 24H2 changed how power transitions are sequenced.

The fix is detective work with a happy ending: find the driver that can't handle the power transition, and either update it, stop Windows from power-managing it so aggressively, or both. If your crashes happen at other times rather than sleep/wake, our broader [Windows 11 blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) is worth a read too.

## Why this happens

- **A driver times out during sleep or wake.** Windows gives drivers a limited window to power down; Wi-Fi, Bluetooth, and GPU drivers that miss the deadline trigger the crash.
- **24H2 changed power sequencing.** Drivers written against older power-management behavior can stumble under 24H2's stricter ordering.
- **Fast Startup hibernates a stale driver state.** The hibernated kernel can resume drivers into a confused state that fails the next power transition.
- **USB selective suspend misbehaves.** Power-saving on USB devices (docks, external drives, receivers) can hang the USB hub driver during sleep.
- **Outdated chipset drivers.** The chipset driver orchestrates power states for the whole platform; an old one under a new Windows build is a mismatch.
- **A device is failing to idle.** A malfunctioning device that never reaches its low-power state keeps its driver from completing the transition.

## How to fix it

Work through these in order. Start with the quick power-setting changes, then go after the specific driver.

### Fix 1: Turn off Fast Startup

This single change resolves a surprising number of sleep/wake crashes.

1. Press **Win + R**, type `powercfg.cpl`, and press **Enter** to open Power Options.
2. Click **Choose what the power buttons do** in the left pane.
3. Click **Change settings that are currently unavailable**.
4. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
5. Shut down fully (not restart) once, then power on — this clears the old hibernated kernel state.

### Fix 2: Run a power efficiency report to name the culprit

Windows can audit its own power behavior and point at problem devices.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `powercfg /energy` and wait 60 seconds while it observes your system.
3. Open the generated report — the command prints its path, usually `C:\Windows\System32\energy-report.html` — in your browser.
4. Look for red errors about devices not entering suspend or drivers with power policy issues. Note the device names.
5. You can also run `powercfg /devicequery wake_armed` to see which devices are allowed to wake the laptop — a misbehaving wake device is a prime suspect.

### Fix 3: Update the suspect drivers

Power-transition bugs get fixed in driver updates constantly.

1. Open **Device Manager** and update the devices flagged in Fix 2 — typically under **Network adapters**, **Bluetooth**, and **Display adapters**.
2. Right-click each, choose **Update driver > Search automatically for drivers**.
3. Then get the chipset driver from your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — since Windows Update often lags on chipset releases.
4. Intel-based laptops can also use Intel's Driver & Support Assistant tool to catch Wi-Fi and Bluetooth driver updates.

### Fix 4: Stop Windows from power-managing the network adapter

Aggressive power saving on Wi-Fi adapters is a classic trigger.

1. In **Device Manager**, expand **Network adapters**, right-click your Wi-Fi adapter, and choose **Properties**.
2. On the **Power Management** tab, uncheck **Allow the computer to turn off this device to save power**.
3. On the **Advanced** tab, look for power-saving properties (names vary: **Power Saving Mode**, **Sleep on WoWLAN disconnect**) and set them to **Maximum Performance** or disabled.
4. Repeat for your **Bluetooth** adapter. Reboot and test sleep/wake several times.

### Fix 5: Disable USB selective suspend

USB power saving hangs sleep on docks and external devices.

1. Open **Power Options** (`powercfg.cpl`), click **Change plan settings** on your active plan, then **Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set both **On battery** and **Plugged in** to **Disabled**.
3. Expand **PCI Express > Link State Power Management** and set it to **Moderate power savings** (not Maximum) — maximum can starve devices during transitions.
4. Click **OK**, then test sleep and wake a few times.

### Fix 6: Check the crash dump to confirm the driver

If crashes persist, let the dump file confirm your suspect.

1. Run BlueScreenView against `C:\Windows\Minidump` and find the `DRIVER_POWER_STATE_FAILURE` entries (stop code `0x0000009F`).
2. The highlighted driver plus the parameters tell the story: parameter 1 = `0x3` means a device object blocked an IRP too long; `0x4` points at the power transition thread.
3. If the dump names a driver you haven't updated yet, target it specifically — download the newest version from the hardware vendor (Realtek, Intel, NVIDIA) rather than relying on Windows Update.
4. Related sleep-adjacent crashes like [IRQL_NOT_LESS_OR_EQUAL after updates](/articles/how-to-fix-irql-not-less-or-equal-after-windows-11-update/) sometimes share the same faulty driver, so compare notes.

### Fix 7: Reset the power plans to defaults

A corrupted or overly aggressive custom power plan can cause transition failures.

1. Open an elevated **Command Prompt** and run `powercfg -restoredefaultschemes` to reset all power plans.
2. Then run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` to repair any damaged power-management components.
3. Reboot, leave the balanced plan active, and retest sleep/wake.
4. As a last resort, check for a BIOS update from your laptop maker that mentions power, sleep, or S3/modern standby fixes — install only on AC power. Microsoft's Windows support site documents power troubleshooting in more depth.

## Closing

DRIVER_POWER_STATE_FAILURE is almost always one driver failing to handle sleep gracefully under 24H2's new sequencing. Turn off Fast Startup, find the offender with the energy report or the dump file, update it, and tame the aggressive power-saving settings — and your laptop will go to sleep and wake up like it's supposed to.
