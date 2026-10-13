---
title: "DRIVER_POWER_STATE_FAILURE: End Sleep and Shutdown Crashes"
slug: driver-power-state-failure-blue-screen-error-fix
date: 2026-10-06
categories: ["windows-errors"]
tags: ["blue screen", "power", "drivers"]
description: "DRIVER_POWER_STATE_FAILURE crashes when your laptop sleeps, wakes, or shuts down? It's a power-transition driver bug — here's how to fix it."
thumbnail: "/images/thumbs/driver-power-state-failure-blue-screen-error-fix.webp"
faqs:
  - q: "What causes DRIVER_POWER_STATE_FAILURE?"
    a: "Stop code 0x0000009F: a driver didn't complete a power-state transition (sleep, wake, shutdown) in time. The driver hung while Windows was waiting, so Windows crashed. It's overwhelmingly a driver bug, not a hardware failure."
  - q: "Why does it only happen on sleep or shutdown?"
    a: "Because that's the only time power IRPs are issued. The faulty driver handles normal operation fine but deadlocks when asked to power down or up. If your crashes cluster around sleep/wake/shutdown, this diagnosis is nearly certain."
  - q: "Which drivers usually cause it?"
    a: "Network (Wi-Fi/Ethernet), graphics, storage controller, and USB drivers are the usual suspects — anything involved in powering hardware down and back up. The minidump usually names the hanging driver."
  - q: "Will changing my power plan fix it?"
    a: "Disabling sleep is a workaround, not a fix — it just avoids triggering the bug. The real fix is updating or replacing the hanging driver. Use power-plan changes only as temporary relief while you diagnose."
---
DRIVER_POWER_STATE_FAILURE (stop code 0x0000009F) is the blue screen of power transitions: your laptop tries to sleep, wake, or shut down, a driver fails to handle the transition in time, and Windows gives up waiting. The pattern is the diagnosis — if crashes happen when closing the lid, pressing the power button, or waking up, you're in the right place.

The fix is finding the hanging driver and updating, rolling back, or replacing it. Work through these in order. There's also a same-category companion at [driver-power-state-failure-windows-11-fix](/articles/driver-power-state-failure-windows-11-fix/) with additional Windows 11-specific angles.

## Why this happens

- **Driver hangs on power IRP.** The core mechanism — a driver doesn't respond to power-down/up requests.
- **Outdated network drivers.** Wi-Fi drivers are the single most common cause.
- **Graphics driver power bugs.** GPU drivers mishandling sleep transitions.
- **USB device drivers.** External devices whose drivers block shutdown.
- **Fast Startup conflicts.** The hybrid shutdown path trips buggy drivers.
- **Corrupted power plans.** Damaged power schemes cause transition failures.
- **BIOS power-management bugs.** Firmware mishandling ACPI power states.

## How to fix it

Work through these in order — test sleep/wake after each.

### Fix 1: Identify the hanging driver from the dump

Aim your fix instead of guessing.

1. After a crash, open **Event Viewer > Windows Logs > System** and find the **BugCheck** entry (0x9F).
2. Note parameter 4 — it points to the hung power IRP, and the named driver is often in the details.
3. Check `C:\Windows\Minidump` for the dump file.
4. The blocked driver is frequently a network driver (`rtwlane.sys`, `Netwtw10.sys`), GPU driver, or USB driver.
5. If you can't read dumps, the pattern still guides you: crashes on sleep = suspect Wi-Fi and GPU drivers first.
6. Write down your suspect list — you'll work through it in the fixes below.

### Fix 2: Update the network drivers

The highest-yield single fix for 0x9F.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Expand **Network adapters**.
3. Right-click your Wi-Fi adapter, choose **Update driver > Search automatically for drivers**.
4. Better: download the latest Wi-Fi and Bluetooth drivers from your laptop maker's support site, or from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) for Intel wireless cards.
5. Do the same for the Ethernet adapter if you have one.
6. Restart, then test sleep (close the lid, wait, reopen) and shutdown several times.

### Fix 3: Update the graphics and chipset drivers

The second most common hang source.

1. Update the GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) — Intel hosts its graphics drivers on its own support detection page — clean install if possible.
2. Install the latest chipset driver from your laptop maker's support site.
3. In **Device Manager**, check **System devices** for anything with a warning icon.
4. If crashes started after a GPU driver update, roll it back via **Properties > Driver > Roll Back Driver**.
5. Test the full cycle: sleep, wake, sleep, shutdown, cold boot.
6. GPU power-transition bugs often need two or three driver generations to get fixed — if the newest still crashes, try the version before it.

### Fix 4: Disable Fast Startup

The hybrid shutdown path is a known trigger.

1. Open Control Panel > **Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)**.
4. Click **Save changes**.
5. Shut down fully and cold-boot, then test sleep/wake cycles.
6. If crashes stop, Fast Startup was provoking the buggy driver. You can leave it off permanently — boot times increase slightly, but stability wins.

### Fix 5: Disconnect USB devices and update their drivers

External hardware blocks power transitions surprisingly often.

1. Disconnect all USB devices except essentials (mouse/keyboard if needed).
2. Test sleep/wake/shutdown with nothing attached.
3. If crashes stop, reconnect devices one at a time, testing after each, to find the culprit.
4. Update that device's driver from the manufacturer's site, or replace the device.
5. In **Device Manager**, expand **Universal Serial Bus controllers** and update the USB hub and controller drivers.
6. For docks and port replicators, install the dock manufacturer's latest driver package — these are frequent 0x9F sources.

### Fix 6: Reset and repair power plans

Corrupted power schemes cause transition failures.

1. Open an elevated terminal: right-click **Start > Terminal (Admin)**.
2. Restore default power schemes:
   `powercfg /restoredefaultschemes`
3. Check for sleep issues:
   `powercfg /energy`
   Let it run 60 seconds, then open the generated report for errors.
4. Review which devices can wake the PC:
   `powercfg /devicequery wake_armed`
   Disable wake for problematic devices in **Device Manager > Properties > Power Management** (uncheck **Allow this device to wake the computer**).
5. Set **Settings > System > Power & battery > Screen and sleep** timeouts to modest values for testing.
6. Microsoft documents powercfg diagnostics on [support.microsoft.com](https://support.microsoft.com/en-us/windows) for deeper analysis.

### Fix 7: Update the BIOS and repair system files

Firmware and system-level fixes for stubborn cases.

1. Check your BIOS version (`msinfo32`) and compare with your laptop maker's support site.
2. Install any BIOS update — release notes often mention ACPI or power-management fixes. Charger connected, don't interrupt.
3. Load BIOS defaults after updating.
4. In Windows, run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
   `sfc /scannow`
5. Restart and run a full week of normal sleep/wake/shutdown cycles.
6. If 0x9F persists across updated drivers, clean power plans, no USB devices, and current BIOS, test the RAM (`mdsched.exe`) — and consider that a specific hardware device's power circuitry may be failing, which needs service. For crashes naming other drivers during power transitions, our [system service exception guide](/articles/system-service-exception-windows-11-fix/) covers the next most common stop code in this family.

## Closing

DRIVER_POWER_STATE_FAILURE is refreshingly honest: it tells you exactly when it happens (power transitions) and the dump usually tells you who did it. Start with network drivers, kill Fast Startup as a test, and isolate USB devices — that trio resolves most cases. Don't settle for "just disable sleep" as a permanent answer; a driver that can't handle power transitions will eventually cause other problems. Fix the driver, keep the sleep.
