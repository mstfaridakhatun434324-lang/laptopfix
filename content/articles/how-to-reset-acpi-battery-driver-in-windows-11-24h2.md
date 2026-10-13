---
title: "How to Reset the ACPI Battery Driver in Windows 11 24H2"
slug: how-to-reset-acpi-battery-driver-in-windows-11-24h2
date: 2026-10-13
categories: ["battery"]
tags: ["ACPI", "battery driver", "Device Manager", "Windows 11"]
description: "Battery stuck, not charging, or showing wrong percentages? Resetting the ACPI battery driver in Windows 11 24H2 fixes it in minutes."
thumbnail: "/images/thumbs/how-to-reset-acpi-battery-driver-in-windows-11-24h2.webp"
faqs:
  - q: "What does the ACPI battery driver do?"
    a: "The Microsoft ACPI-Compliant Control Method Battery driver is the translator between Windows and your laptop's battery hardware. It reports charge percentage, charging state, and capacity. When it corrupts — often after Windows updates — Windows shows wrong percentages, 'plugged in not charging,' or no battery at all."
  - q: "Is it safe to uninstall the ACPI battery driver?"
    a: "Yes. It's a standard system driver that Windows reinstalls automatically on the next boot. Uninstalling it doesn't touch your files or settings — it just forces Windows to rebuild the driver stack cleanly, which clears corrupted state."
  - q: "Will resetting the driver delete my battery calibration?"
    a: "No. Calibration reference points live in the battery controller's firmware, not in the Windows driver. The reset only clears the software-side communication state, so your calibration survives intact."
  - q: "What if the battery still misbehaves after resetting the driver?"
    a: "Then the problem is deeper: try the Microsoft AC Adapter driver too, update the BIOS and chipset drivers, check for a charge limit in the manufacturer's app, and generate a battery report to check for genuine wear. Persistent issues after a clean driver point to hardware."
---

The ACPI battery driver is one of those invisible pieces that only matters when it breaks — and when it breaks, the symptoms look like a dead battery. Wrong percentages, charging that never starts, a battery that vanishes from Windows entirely. It's the translator between Windows and your laptop's battery controller chip, and when the translation goes wrong, every reading Windows shows you is suspect — including the taskbar icon you trust every day. Before you buy hardware, spend five minutes resetting this driver. It resolves a surprising share of battery weirdness, especially after Windows 11 24H2 updates.

## Why this happens

- **Update corruption:** Feature updates sometimes migrate the driver stack badly, leaving stale or mismatched driver state behind.
- **Stuck embedded controller state:** The driver caches communication with the battery controller; a glitch there persists across reboots.
- **Conflicting manufacturer drivers:** Some OEM battery utilities install filter drivers that clash with the Microsoft ACPI driver after updates.
- **Hibernation residue:** A corrupted hibernation file can restore bad driver state on every boot.
- **Firmware mismatch:** A BIOS update can change the battery controller's interface while Windows keeps talking to it the old way.
- **Duplicate or ghost devices:** Sometimes Device Manager shows two battery entries after an update, and Windows reads from the stale one.

## How to fix it

### Fix 1: Uninstall the ACPI battery driver

1. Press **Win + X** and open **Device Manager**.
2. Expand the **Batteries** category.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**.
4. If prompted about deleting driver software, leave the box **unchecked** — you want Windows to reinstall its own driver.
5. Don't reboot yet; continue to Fix 2 for the full reset sequence.

### Fix 2: Do the full power-drain reset

1. After uninstalling, **shut down** the laptop completely (hold Shift while clicking Shut down to bypass Fast Startup).
2. Unplug the charger and, if the battery is removable, take it out.
3. Press and hold the **power button for 30 seconds** to drain residual power from the capacitors.
4. Reinsert the battery (if removed), plug in the charger, and power on.
5. Windows detects the battery hardware and reinstalls the ACPI driver automatically — check Device Manager to confirm it's back with no warning icon.

### Fix 3: Reset the Microsoft AC Adapter driver too

1. In **Device Manager > Batteries**, right-click **Microsoft AC Adapter** and **Uninstall device**.
2. Do the same shutdown-and-drain sequence from Fix 2.
3. This clears the charging-side driver state, which fixes "plugged in, not charging" cases the battery driver reset alone misses.
4. If your charger issues persist, also verify you're using the right wattage — see [how to fix a laptop battery that drains while plugged in](/articles/how-do-i-fix-laptop-battery-drains-while-plugged-in/).

### Fix 4: Update chipset and BIOS drivers

1. Visit your manufacturer's support site and install the latest **chipset drivers** — these include the platform power management components the ACPI driver depends on.
2. Check for a **BIOS update**; release notes mentioning "battery," "charging," or "power" are directly relevant.
3. Install the BIOS update on AC power with the battery in place, and don't interrupt it.
4. After updating, the ACPI driver renegotiates with the new firmware cleanly.

### Fix 5: Clear hibernation state

1. Open **Terminal (Admin)** and run `powercfg /h off` to delete the hibernation file.
2. Shut down fully, then boot and test the battery behavior.
3. If fixed, re-enable hibernation with `powercfg /h on` if you use it.
4. A corrupted hiberfil.sys restoring bad driver state on every boot is rarer than people think, but this rules it out definitively.

### Fix 6: Check for a charge limit masking the problem

1. Open your manufacturer's app (**Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, HP BIOS settings).
2. Look for charge thresholds or conservation modes that stop charging at 60-80 percent.
3. Sometimes what looks like a driver failure ("won't charge past 80%") is actually this feature working correctly.
4. Temporarily set it to full charge and retest before concluding the driver is at fault.

### Fix 7: Verify with a battery report

1. Run `powercfg /batteryreport` in an admin terminal.
2. Confirm the report now shows sensible **Design Capacity** and **Full Charge Capacity** values.
3. Use the laptop on battery and confirm the percentage drops smoothly.
4. If the gauge is still erratic after a clean driver, run a [full battery calibration](/articles/how-do-i-fix-laptop-battery-calibration-not-working/) — the controller's reference points may have drifted.

### Fix 8: Scan for driver updates through Windows Update

1. After the manual reset, open **Settings > Windows Update > Advanced options > Optional updates**.
2. Expand **Driver updates** and install anything related to batteries, chipset, or system firmware.
3. Restart and retest — Microsoft occasionally ships fixed ACPI driver builds through this channel after problematic updates.
4. If Windows Update offers a battery driver newer than what auto-installed, take it; if the problem started right after a driver update, use **Device Manager > Batteries > Properties > Driver > Roll Back Driver** instead.

## Closing

The ACPI driver reset is the closest thing battery troubleshooting has to "turn it off and on again" — quick, safe, and effective far more often than its simplicity suggests. Make it your first move whenever battery symptoms appear after a Windows update, and your go-to sanity check before spending money on parts. Keep this procedure in your back pocket: driver stacks corrupt again over time, and knowing the 30-second power-drain sequence saves you a support call every single time it happens. If a clean driver, updated firmware, and no charge limits still leave you with a misbehaving battery, the evidence points to the battery itself, and a report-backed replacement decision is the honest next step.

Microsoft documents driver management at the [Windows support hub](https://support.microsoft.com/en-us/windows). For the general no-charge walkthrough, see [how to fix a laptop battery not charging step by step](/articles/how-to-fix-laptop-battery-not-charging-step-by-step/).
