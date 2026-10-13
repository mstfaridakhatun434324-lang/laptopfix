---
title: "Driver Power State Failure? What to Do Step by Step"
slug: what-to-do-if-driver-power-state-failure
date: 2026-09-21
categories: ["windows-errors"]
tags: ["driver power state failure", "bsod", "sleep wake", "windows 11"]
description: "DRIVER_POWER_STATE_FAILURE strikes during sleep, wake, or shutdown. Here's what to do: update power-transition drivers, adjust power settings, and test."
thumbnail: "/images/thumbs/what-to-do-if-driver-power-state-failure.webp"
faqs:
  - q: "What does Driver Power State Failure mean?"
    a: "A driver failed to complete a power-state transition — usually sleep, wake, or shutdown — within the time Windows allows. Stop code 0x0000009F. The driver hung instead of powering down or up cleanly, so Windows stopped the system. Network, graphics, and USB drivers are the usual suspects because they manage power states constantly."
  - q: "Why does it happen when my laptop sleeps or wakes?"
    a: "Sleep and wake are the most complex power transitions, involving every device driver coordinating in sequence. A single driver that doesn't handle the transition — common after driver updates — hangs the whole chain. If your crashes cluster around closing the lid or pressing the power button, you're looking at a power-transition driver bug."
  - q: "Can I just disable sleep to avoid it?"
    a: "You can, and it stops the crashes — but it's a workaround, not a fix. Disabling sleep avoids the faulty transition without fixing the faulty driver, and the same driver can still crash during shutdown or hibernate. Use it as temporary relief while you update the real culprit, not as the permanent solution."
  - q: "Which driver is causing my power state failure?"
    a: "Check the minidump with BlueScreenView or WinDbg — parameter 1 of the bug check identifies the hanging driver, often ndis.sys (network), USB drivers, or the graphics driver. The Device Manager power-management tabs also help: devices with 'Allow the computer to turn off this device' behave differently, and disabling that option per-device is a valid diagnostic step."
---

DRIVER_POWER_STATE_FAILURE (stop code 0x0000009F) is the blue screen of bad naps. It happens when a driver fails to handle a power transition — going to sleep, waking up, shutting down, or hibernating — within the timeout Windows enforces. The driver hangs, the transition stalls, and Windows pulls the plug on everything to avoid an inconsistent power state. If your crashes cluster around closing the lid, pressing the power button, or the laptop waking itself at 3 AM, this is almost certainly your stop code.

The practical approach: identify the hanging driver from the crash dump, update the drivers that manage power states (network, graphics, USB, chipset), and adjust the power settings that trigger the faulty transition. Disabling sleep entirely is a legitimate emergency workaround, but the goal is fixing the driver. For the condensed reference, see our [Driver Power State Failure fix](/articles/driver-power-state-failure-windows-11-fix/); for the update-triggered variant, see our [post-update power failure guide](/articles/how-to-fix-driver-power-state-failure-after-windows-11-update/).

## Why this happens

- **Network driver power bugs**: Wi-Fi/Ethernet drivers hanging during sleep/wake — the top cause.
- **Graphics driver transition faults**: GPU drivers failing to suspend or resume cleanly.
- **USB device/driver issues**: External devices or their drivers blocking the power transition.
- **Outdated chipset drivers**: The chipset coordinates power states; old versions mishandle modern sleep states.
- **Fast Startup conflicts**: The hybrid shutdown interacting badly with drivers that expect full shutdowns.
- **BIOS power-management bugs**: Firmware-level sleep state (S3/Modern Standby) incompatibilities.
- **Windows Update driver swaps**: A new driver version introducing a power-transition regression.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the pattern and identify the driver

Power failures are pattern-driven — document the pattern.

1. Note exactly when crashes occur: lid close, power button, idle timeout sleep, wake from sleep, shutdown, or hibernate. Each implicates the same driver family differently.
2. Analyze the minidump: open `C:\Windows\Minidump` with BlueScreenView — the bug check parameters identify the hanging driver object, frequently pointing at `ndis.sys` (network) or USB hub drivers.
3. Open **Device Manager**, and for network adapters and USB devices, check **Properties** > **Power Management** — note which devices are allowed to wake or power down.
4. As an emergency stopgap only: **Settings** > **System** > **Power & battery** > set sleep to **Never** while you work through the real fixes.

### Fix 2: Update network and chipset drivers

The highest-yield driver updates for this stop code.

1. Download the latest Wi-Fi/Ethernet drivers from your laptop manufacturer's support page (OEM-customized versions matter here). For Intel adapters, [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) pinpoints the right package.
2. Update the chipset driver from the laptop vendor — it orchestrates the power states all other drivers follow.
3. In **Device Manager**, for each network adapter: **Properties** > **Power Management** > experiment with unchecking **Allow the computer to turn off this device to save power** — if crashes stop, that driver's power handling is the bug, and the updated driver should resolve it properly.
4. Restart and run deliberate sleep/wake cycles (lid close, power button, idle timeout) to test — don't wait for crashes to come to you.

### Fix 3: Update the graphics driver

GPUs are deeply involved in sleep/wake.

1. Clean-install the latest GPU driver from the vendor (NVIDIA/AMD/Intel) using the clean-install/factory-reset option.
2. If crashes started after a GPU driver update, roll back to the previous version instead.
3. Disable hardware-accelerated GPU scheduling temporarily (**Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings**) as a test — it changes the driver's power behavior.
4. For laptops with dual GPUs, update both the integrated and discrete graphics drivers — the handoff between them during sleep is a known crash point.

### Fix 4: Disable Fast Startup

The hybrid shutdown is a frequent accomplice.

1. Open **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**.
2. Untick **Turn on fast startup (recommended)** and save.
3. Fast Startup's hybrid shutdown keeps drivers in a suspended state between boots; drivers with power bugs then misbehave on the next cycle. A full shutdown sidesteps this entirely.
4. Test shutdown/startup cycles for a few days. If crashes stop, leave Fast Startup off permanently — the boot-time cost on an SSD is negligible.

### Fix 5: Audit USB devices and their drivers

External devices hang power transitions more than people expect.

1. Disconnect all USB devices except essentials and test sleep/wake cycles. If crashes stop, reconnect one at a time to find the offender.
2. Update USB/chipset drivers from the laptop vendor; in **Device Manager** > **Universal Serial Bus controllers**, check **Power Management** tabs for hubs.
3. Disable **USB selective suspend**: **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings** > **USB settings** > **USB selective suspend setting** > **Disabled**.
4. Check [Microsoft's power troubleshooting guidance](https://support.microsoft.com/en-us/windows) for the sleep-study report (`powercfg /sleepstudy`) — it logs exactly which devices block sleep.

### Fix 6: Update the BIOS and check sleep states

Firmware-level power management matters.

1. Check the laptop manufacturer's support page for a BIOS update — changelogs frequently mention sleep/wake and Modern Standby fixes.
2. In the BIOS, look for sleep-related options (Sleep state, Modern Standby vs. S3, USB wake support) and try the alternative setting if crashes persist.
3. Run `powercfg /a` in an elevated terminal to see which sleep states your system supports — missing S3 with forced Modern Standby is a known laptop crash source.
4. After a BIOS update, re-test the full sleep/wake/shutdown cycle suite before declaring victory.

### Fix 7: Repair system files and reset the power plan

Clean up the OS layer and power configuration.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated terminal.
2. Reset power plans to defaults: `powercfg /restoredefaultschemes` in an elevated terminal — years of tweaked settings can produce contradictory power behavior.
3. Reconfigure only the settings you actually need afterward, testing sleep/wake after each change.
4. If crashes persist through everything, the minidump analysis from Fix 1 becomes the definitive guide — consider posting the analyzed dump (not the raw file) to a tech forum with your exact laptop model for driver-specific advice.

## Closing

DRIVER_POWER_STATE_FAILURE is a transition problem, so the fix is about transitions: which driver hangs, during which power change, and what update introduced it. The emergency sleep-disable buys you stability while you work; the real fix is the driver update (or rollback) that lets the transition complete. Keep a log of which power actions you've tested after each change — this crash is intermittent by nature, and "it hasn't crashed in three days" only counts if those three days included the lid closes, idle sleeps, and shutdowns that used to trigger it. For the quick-reference version, our [power state failure fix](/articles/driver-power-state-failure-windows-11-fix/) is the bookmarkable companion.
