---
title: "DRIVER_POWER_STATE_FAILURE: How to Fix It on Windows 11"
slug: how-do-i-fix-driver-power-state-failure
date: 2026-09-26
categories: ["windows-errors"]
tags: ["driver power state failure", "bsod", "power management", "driver", "windows 11"]
description: "DRIVER_POWER_STATE_FAILURE (0x9F) means a driver mishandled a sleep/wake power transition. Here's how to fix it — driver updates, power settings, and device isolation."
thumbnail: "/images/thumbs/how-do-i-fix-driver-power-state-failure.webp"
faqs:
  - q: "What causes DRIVER_POWER_STATE_FAILURE?"
    a: "Stop code 0x9F means a driver failed to complete a power-state transition — usually sleep, hibernate, or wake — within the time Windows allows. The driver either didn't respond to the power IRP or took too long. Common offenders are network adapters (Wi-Fi and Ethernet), storage controllers, USB devices, and graphics drivers. It happens most often when the laptop sleeps, wakes, or shuts down."
  - q: "Why does it happen when my laptop wakes from sleep?"
    a: "Sleep and wake are the most complex power transitions a driver handles: every device must save state, power down, then reinitialize in the right order on wake. A driver with a power-management bug hangs during one of these steps, Windows waits, the timeout expires, and you get 0x9F. If your crashes cluster around sleep/wake, the fix is almost certainly a driver update or a power-setting change for the suspect device."
  - q: "Can I fix it by just disabling sleep?"
    a: "Disabling sleep avoids the trigger but doesn't fix the driver bug — and you'd lose one of a laptop's most useful features. It's a reasonable temporary workaround while you identify the culprit, not a solution. The proper fix is updating or replacing the offending driver, which the steps below walk you through."
  - q: "How do I find which driver caused it?"
    a: "Open the crash dump in WinDbg or BlueScreenView and look at parameter 1 and the stack: 0x9F dumps usually name the blocking driver or show it stuck in a power IRP. The !analyze output often identifies the device. Alternatively, the pattern is diagnostic — crashes on wake point at network or USB drivers; crashes on shutdown point at storage or display drivers."
---

DRIVER_POWER_STATE_FAILURE — stop code 0x9F — is the blue screen of bad power manners. It means a driver was asked to handle a power transition (sleep, wake, hibernate, shutdown) and failed to do it in time. Windows waited, the driver never finished, and the system crashed rather than continue in an inconsistent power state. On laptops, where sleep and wake happen dozens of times a day, a driver with a power-management bug turns into a daily blue screen.

The pattern is your best diagnostic tool: crashes when closing the lid, opening the lid, or shutting down point squarely at power-transition bugs. The usual suspects are Wi-Fi drivers, USB devices (especially docks and external drives), storage controllers, and graphics drivers — anything that has to save and restore hardware state. The fixes below identify the offender and fix it, in the order that resolves most cases. For the detective-style approach to the same stop code, see our [troubleshooting companion](/articles/troubleshoot-driver-power-state-failure/).

## Why this happens

- **Buggy Wi-Fi or Ethernet driver**: Network drivers are the number one cause — they mishandle the sleep/wake handshake constantly, especially after updates.
- **USB device refusing to suspend**: External drives, docks, and peripherals whose drivers don't handle power transitions hang the whole chain.
- **Outdated storage controller driver**: AHCI/NVMe drivers with power bugs stall during the disk spin-down phase of sleep.
- **Graphics driver power bug**: GPUs have elaborate power states; a buggy driver can hang when transitioning between them.
- **Fast Startup conflicts**: The hybrid shutdown interacts badly with drivers that expect clean power transitions.
- **BIOS power management bugs**: Firmware-level power handling (ACPI tables) can conflict with Windows' expectations, fixed by BIOS updates.
- **Corrupt hibernation file**: A damaged hiberfil.sys breaks resume-from-hibernate, crashing during the wake transition.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the timing pattern and the suspect

Before changing anything, characterize when it crashes.

1. Note exactly when the BSOD occurs: closing the lid, opening the lid, pressing power to sleep, shutting down, or resuming from hibernate. Write it down.
2. Disconnect all USB devices and docks, then sleep/wake the laptop several times. If crashes stop, reconnect devices one at a time to find the offender.
3. Open the latest dump in BlueScreenView (quicker than WinDbg for this) and check parameter 1 and the stack for a named driver — network drivers (`Netwtw*.sys`, `rtwlan*.sys`) are the classic find.
4. Our [dump-reading guide](/articles/how-to-read-dump-files-with-windbg-in-windows-11-24h2/) covers the deeper analysis if BlueScreenView's output is inconclusive.

### Fix 2: Update the network drivers

The highest-probability fix — do this first regardless.

1. Identify your Wi-Fi adapter in **Device Manager** > **Network adapters**.
2. Download the latest driver from your laptop manufacturer's support page (Dell, HP, Lenovo) — or from [Intel's assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel Wi-Fi.
3. Install it, restart, and test sleep/wake cycles deliberately: sleep and wake the laptop five times in a row.
4. Update the Ethernet driver too if you use wired connections or a USB-C dock with Ethernet — dock network chips are frequent 0x9F offenders.

### Fix 3: Stop devices from misbehaving during power transitions

Prevent the suspect devices from participating in power management badly.

1. In **Device Manager**, right-click your Wi-Fi adapter > **Properties** > **Power Management** tab, and untick **Allow the computer to turn off this device to save power**.
2. Do the same for USB Root Hubs under **Universal Serial Bus controllers** if USB devices are implicated.
3. In **Settings** > **System** > **Power & battery**, set **Screen and sleep** timeouts sanely, and under **Power mode** avoid aggressive battery-saver settings that force deeper sleep states.
4. Retest. If crashes stop, you've confirmed a device power-management bug — keep the setting, and report it to the driver vendor.

### Fix 4: Update storage and chipset drivers

The second tier of suspects after networking.

1. Update the chipset driver from your manufacturer's support page or the [Intel](https://www.intel.com/content/www/us/en/support/detect.html)/AMD driver pages.
2. Update the storage controller driver (Intel RST / VMD, AMD NVMe) the same way — never rely on the generic Microsoft storage driver for a laptop with a vendor-specific controller.
3. Update the graphics driver with a clean install — [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, or Intel.
4. Restart and run your sleep/wake test cycle again.

### Fix 5: Disable Fast Startup and rebuild the hibernation file

Eliminate the hybrid-shutdown variables.

1. Open **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**, and untick **Turn on fast startup**.
2. Open **Windows Terminal (Admin)** and run `powercfg /h off` — this deletes hiberfil.sys entirely. Restart.
3. If you use hibernate, re-enable it with `powercfg /h on` — this creates a fresh, uncorrupted hibernation file.
4. Test shutdown and sleep cycles. Fast Startup conflicts alone account for a meaningful share of 0x9F crashes.

### Fix 6: Update the BIOS

Firmware-level ACPI bugs cause power-transition crashes no driver update can fix.

1. Check your current BIOS version in **System Information** (`msinfo32`).
2. Visit your manufacturer's support page and compare — if yours is old, download the update and read the release notes for power/ACPI/stability mentions.
3. Flash with the charger connected and don't interrupt the process.
4. Retest sleep/wake thoroughly — BIOS updates frequently resolve 0x9F on specific laptop models where the ACPI tables were buggy.

### Fix 7: Run Driver Verifier on the suspects

If the dump won't name names, force the issue.

1. Press **Windows + R**, type `verifier`, choose **Create standard settings**, then **Select driver names from a list**.
2. Select the network, storage, and USB drivers you suspect. Restart — Verifier will crash the system faster and the dump will pinpoint the offender.
3. After capturing the dump, boot into Safe Mode and run `verifier /reset` to disable it.
4. Never leave Verifier on permanently — it slows the system and is purely a diagnostic tool.

### Fix 8: Clean-boot to isolate software interference

Some crashes come from software that hooks power transitions.

1. Run `msconfig`, hide all Microsoft services, disable the rest; disable non-Microsoft startup apps in Task Manager; restart.
2. Test sleep/wake cycles. If stable, re-enable in halves to find the culprit — VPN clients, backup tools, and "optimizer" utilities are common interferers.
3. Once found, update or remove the offending software.
4. For persistent cases across all software fixes, check Microsoft's support hub for known 0x9F issues with your Windows build — some are OS bugs fixed by cumulative updates.

## Closing

DRIVER_POWER_STATE_FAILURE is almost never mysterious once you watch the pattern: it crashes around sleep, wake, or shutdown because a driver fumbles the power transition. Update the network drivers first — they're the cause more often than everything else combined — then work through storage, chipset, and graphics drivers, and don't forget the BIOS. The sleep/wake test cycle (five deliberate cycles after each change) is what turns guessing into diagnosis. Fix the driver, keep the laptop's sleep working, and the 0x9F screens stop for good.
