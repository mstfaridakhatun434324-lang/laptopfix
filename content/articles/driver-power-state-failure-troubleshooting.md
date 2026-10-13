---
title: "Driver Power State Failure Troubleshooting: Find the Exact Cause"
slug: driver-power-state-failure-troubleshooting
date: 2026-09-06
categories: ["windows-errors"]
tags: ["driver power state failure", "troubleshooting", "power management", "bsod"]
description: "Still getting DRIVER_POWER_STATE_FAILURE after the basic fixes? This deep troubleshooting guide isolates the exact driver or device causing it."
thumbnail: "/images/thumbs/driver-power-state-failure-troubleshooting.webp"
faqs:
  - q: "How do I find which driver causes DRIVER_POWER_STATE_FAILURE?"
    a: "Use a clean boot to isolate it: disable all non-Microsoft services and startup items, test sleep/wake, then re-enable in halves until the crash returns. For a faster technical answer, analyze the minidump with WinDbg or BlueScreenView — the faulting driver is usually named. Event Viewer also logs Kernel-Power event 41 and driver timeout warnings before the crash."
  - q: "What does Event Viewer show before this blue screen?"
    a: "Look in Windows Logs > System for warnings from sources like Kernel-Power, ndis, or storahci in the minutes before the crash. You may also see event ID 41 (Kernel-Power) recording the unexpected shutdown. These entries often name the device that failed to respond to the power transition, giving you a head start before clean-boot isolation."
  - q: "Can USB devices cause DRIVER_POWER_STATE_FAILURE?"
    a: "Absolutely — USB docks, external drives, and wireless dongles are frequent culprits because their drivers must handle suspend and resume. If crashes started after adding a USB device, unplug it for a few days as a test. Also disable USB selective suspend in the advanced power settings to see if the crashes stop."
  - q: "Why does this error only happen on battery power?"
    a: "On battery, Windows uses more aggressive power-saving: deeper PCIe link states, USB selective suspend, and faster device sleep. A driver that handles the gentle AC power transitions fine can fail the aggressive battery ones. Testing on AC vs battery narrows it down, and relaxing the battery power plan settings often resolves it."
---
The basic fixes for DRIVER_POWER_STATE_FAILURE — Fast Startup off, driver updates, PCIe settings — resolve most cases. But when the blue screen keeps coming back, you need to stop treating it generically and find the specific driver or device that's hanging the power transition. This guide is the deep-dive companion to the [main Driver Power State Failure fix guide](/articles/driver-power-state-failure-bsod-windows-11/); start there if you haven't.

Troubleshooting this error is detective work: the crash means a driver didn't answer a power request in time, so your job is to figure out which one.

## Why this happens

- **A specific driver hangs on power IRPs.** Some driver fails to complete the power request packet Windows sends during sleep/wake.
- **USB device drivers mishandle suspend.** Docks, hubs, and dongles with buggy drivers stall the whole transition.
- **Firmware-level power bugs.** The BIOS/UEFI power tables (ACPI) can contain errors that only certain OS versions trip over.
- **Conflicting power policies.** OEM utilities and Windows fighting over power plans create transitions no driver expects.
- **A device that never wakes.** A failing Wi-Fi card or SSD may simply not respond to resume commands.
- **Corrupted hibernation file.** A damaged hiberfil.sys replays bad state on every resume from hibernate.
- **Docking station firmware.** Older dock firmware mishandles the sleep handshake with the laptop, hanging the whole transition.

## How to fix it

Work through these in order, from diagnostic to definitive.

### Fix 1: Read the minidump and Event Viewer

Gather evidence before changing anything.

1. Install BlueScreenView and open the latest crash — note the faulting `.sys` file and the bug check parameters.
2. Open **Event Viewer > Windows Logs > System** and filter the hour before the crash for **Warning** and **Error** entries.
3. Look for Kernel-Power event 41 plus any driver-specific warnings naming a device.
4. Write down the suspect driver/device names — you'll target them in the steps below instead of guessing.

### Fix 2: Strip all USB devices and test

USB drivers are the most common specific culprits.

1. Unplug every USB device except keyboard/mouse: docks, hubs, external drives, printers, dongles.
2. Test sleep/wake cycles for a day. If crashes stop, reconnect devices one per day until the crash returns.
3. For the guilty device, update its driver from the manufacturer's site or replace it.
4. Also disable **USB selective suspend** in **Power Options > Change advanced power settings > USB settings** as a general stabilizer.

### Fix 3: Disable hibernation and rebuild hiberfil.sys

A corrupted hibernation file poisons every resume.

1. Open **Terminal (Admin)** and run `powercfg /hibernate off` — this deletes hiberfil.sys.
2. Restart the laptop.
3. Run `powercfg /hibernate on` to recreate a fresh hibernation file.
4. Test hibernate/resume cycles. If crashes only happened on hibernate resume, this often ends them.

### Fix 4: Methodical clean boot isolation

The definitive way to name the culprit when dumps are inconclusive.

1. Press **Win + R**, type `msconfig`; on the **Services** tab, check **Hide all Microsoft services** and click **Disable all**.
2. In Task Manager's **Startup apps**, disable everything. Restart.
3. Test sleep/wake thoroughly. If stable, re-enable half the services, restart, and retest.
4. Keep halving until the crash returns with a minimal set enabled — the last-added item is your culprit. Update, reconfigure, or uninstall it.

### Fix 5: Test AC vs battery to isolate power-plan triggers

Determine whether aggressive battery power saving is the trigger.

1. Run the laptop on AC power only for two days, testing sleep/wake each day.
2. Then run on battery only for two days with the same tests.
3. If crashes happen only on battery, open the advanced power settings for the battery plan and relax them: PCIe Link State to Off, USB selective suspend Disabled, wireless adapter to Maximum Performance.
4. If crashes happen on both, the trigger isn't plan-specific — continue to firmware.

### Fix 6: Update BIOS and reset ACPI-related settings

Firmware power tables are the layer below drivers.

1. Check your BIOS version against your laptop maker's latest on their support site — read changelogs for sleep/power fixes.
2. Update with the charger connected, then enter the BIOS and **Load Optimized Defaults**.
3. Look for settings like **USB Wake Support**, **Deep Sleep Control**, or **Block Sleep** — set them to sensible defaults (wake support on, deep sleep off for testing).
4. Save, boot, and test. Firmware fixes resolve the cases where every driver is current but crashes persist.

### Fix 7: Replace or disable the suspect hardware

When one device is proven guilty and no driver fixes it.

1. If isolation points to the Wi-Fi card, try the latest driver from Intel/Realtek/Qualcomm directly, not just the laptop maker's package.
2. If the card still fails, replace it — Wi-Fi cards are inexpensive and usually socketed, or use a USB adapter as a workaround.
3. If storage is implicated, check SMART health and clone to a new SSD at the first warning sign.
4. For anything else, take your isolation notes to a repair shop — "the crash stops when X is disabled, here are the dumps" gets you a fast, accurate repair. Keep [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) bookmarked for the official power-troubleshooting references.

## Closing

Deep troubleshooting of this error is about narrowing: dumps and logs name suspects, USB stripping and clean boot confirm them, AC/battery testing characterizes the trigger, and firmware updates fix what drivers can't.

The discipline that matters most is changing one thing at a time and testing sleep/wake cycles between changes — otherwise you'll never know which fix actually worked, and the crash will be back the next time that driver updates. Keep a simple log as you go: date, change made, result. It takes thirty seconds per entry and turns a confusing week of intermittent crashes into a clear record. When you do find the culprit, consider reporting it to the device manufacturer — driver power bugs get fixed when users report them with specifics, and your report helps the next person with the same hardware. If your crashes began specifically after the 24H2 update, the [24H2-specific driver power state failure guide](/articles/how-to-fix-driver-power-state-failure-in-windows-11-24h2/) covers update-triggered variants in more depth.
