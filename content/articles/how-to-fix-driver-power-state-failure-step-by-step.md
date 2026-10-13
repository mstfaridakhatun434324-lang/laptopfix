---
title: "How to Fix DRIVER_POWER_STATE_FAILURE — Step by Step"
slug: how-to-fix-driver-power-state-failure-step-by-step
date: 2026-09-05
categories: ["windows-errors"]
tags: ["bsod", "drivers", "power"]
description: "DRIVER_POWER_STATE_FAILURE blue screen? Follow this step-by-step checklist to find the failing driver and fix power-transition crashes."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-step-by-step.webp"
faqs:
  - q: "What is DRIVER_POWER_STATE_FAILURE in simple terms?"
    a: "When your laptop sleeps, wakes, hibernates, or shuts down, every hardware driver must power down and back up in an orderly sequence. This stop code means one driver failed to complete its power transition in time — most often the Wi-Fi, Bluetooth, graphics, or storage driver."
  - q: "How do I know which driver is causing it?"
    a: "Check Event Viewer's BugCheck entry after a crash, or analyze the minidump in C:\\Windows\\Minidump with WinDbg Preview (!analyze -v) — it names the faulting driver. In practice, the Wi-Fi driver is the culprit often enough that it's worth checking first even before dump analysis."
  - q: "Does this error damage my laptop?"
    a: "The crash itself doesn't damage hardware, but repeated unexpected shutdowns risk file corruption and can interrupt updates mid-install. It's also a sign of an unstable driver that deserves fixing rather than ignoring — the checklist below resolves it in most cases."
  - q: "Can power settings alone fix DRIVER_POWER_STATE_FAILURE?"
    a: "Sometimes. Disabling USB selective suspend, setting the wireless adapter to Maximum Performance, and turning off Fast Startup resolve cases where the driver is fine but Windows' aggressive power management pushes devices into states the driver can't recover from. Try settings before replacing drivers."
---
DRIVER_POWER_STATE_FAILURE always strikes at the same moments: closing the lid, opening it, shutting down, or waking from sleep. That's the signature — it's a power-transition crash, which means the investigation starts with drivers that manage hardware power states and the Windows settings that control them.

This is the checklist version: work it top to bottom, checking off each step. Most people find their fix by step 4.

## Why this happens

- **Wi-Fi/Bluetooth driver failing sleep/wake** — the most common single cause.
- **Graphics driver power-management bug** — faulting during display sleep/wake.
- **Windows Update replaced a working driver** — generic version lacking proper power handling.
- **USB selective suspend** — Windows powering down USB devices their drivers expect awake.
- **Fast Startup preserving a bad driver state** — hibernation-based boot carrying corruption across restarts.
- **Aggressive PCI Express link-state power management** — power-gating the bus out from under drivers.
- **Outdated BIOS** — firmware mishandling Modern Standby transitions.
- **Failing hardware beneath the driver** — a dying Wi-Fi card or SSD that can't complete transitions.

## How to fix it

Work through these in order. After each change, deliberately test sleep/wake cycles (sleep 1 minute, wake, repeat 3–4 times).

### Fix 1: Identify the faulting driver

1. After a crash, open **Event Viewer** (**Windows + R** > `eventvwr.msc`) > **Windows Logs** > **System** and find the **BugCheck** entry — note any named driver file.
2. For the full answer, install **WinDbg Preview** from the Microsoft Store, open the newest dump in C:\\Windows\\Minidump, run `!analyze -v`, and read **MODULE_NAME**.
3. Common findings: `Netwtw*.sys` (Intel Wi-Fi), `rtwlanu.sys` (Realtek Wi-Fi), `nvlddmkm.sys` (NVIDIA), `amdkmdag.sys` (AMD), `BthA2dp.sys`/Bluetooth stack.
4. Write the name down — it focuses every step below.

### Fix 2: Update or roll back the suspect driver

1. Open **Device Manager** (**Windows + X** > **Device Manager**).
2. Find the device matching your suspect driver (Network adapters for Wi-Fi, Display adapters for GPU, Bluetooth for wireless audio).
3. **Properties** > **Driver** tab: check the **Driver Date**. If crashes started right after a driver change, click **Roll Back Driver**. Otherwise, **Update driver** > **Search automatically for drivers**.
4. Best source: your laptop maker's support site for your exact model — manufacturer wireless and graphics drivers include power-management fixes generics lack.
5. For Intel Wi-Fi/Bluetooth, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) supplies current stable versions.
6. Restart and run your sleep/wake test cycle.

### Fix 3: Adjust the advanced power settings

1. **Control Panel** > **Hardware and Sound** > **Power Options** > **Change plan settings** > **Change advanced power settings**.
2. **Wireless Adapter Settings** > **Power Saving Mode**: set both **On battery** and **Plugged in** to **Maximum Performance**.
3. **USB settings** > **USB selective suspend setting**: set both to **Disabled**.
4. **PCI Express** > **Link State Power Management**: set to **Moderate power savings** or **Off** (test both; Off is the stronger test).
5. **Sleep** > **Allow hybrid sleep**: set to **Off** for testing.
6. Click **Apply** > **OK**, then run the sleep/wake test cycle.

### Fix 4: Disable Fast Startup

1. **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup (recommended)** > **Save changes**.
3. Shut down completely (not Restart), power back on, and test.
4. Alternatively, from an admin Command Prompt: `powercfg /h off` disables hibernation and Fast Startup together.

### Fix 5: Fix USB device power management

1. In **Device Manager**, expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub** and **Generic USB Hub**: right-click > **Properties** > **Power Management** tab > uncheck **Allow the computer to turn off this device to save power**.
3. Do the same for devices under **Human Interface Devices** that stay plugged in (receivers, docks).
4. If you use a USB docking station, check the dock maker's site for firmware updates — dock power quirks cause this stop code too.

### Fix 6: Update the BIOS

1. Check your BIOS version: **Windows + R** > `msinfo32` > **BIOS Version/Date**.
2. Compare against your laptop maker's support site for your exact model; download and install any newer BIOS with the AC adapter plugged in — do not interrupt it.
3. BIOS updates frequently fix Modern Standby and device power-transition bugs behind this stop code.
4. After updating, re-run the sleep/wake test cycle before changing anything else.

### Fix 7: Run the Power troubleshooter and reset power schemes

1. **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > run **Power**.
2. Apply its recommendations and restart.
3. If settings have been heavily customized over time, reset them cleanly: admin Terminal > `powercfg -restoredefaultschemes` > restart.
4. Reapply only the Fix 3 changes you need, testing sleep/wake after each one.

### Fix 8: Check for failing hardware

When software steps all pass but crashes continue.

1. Pay attention to which device the dump blames repeatedly — a Wi-Fi card blamed across many driver versions may itself be failing.
2. Test with the suspect device disabled: in **Device Manager**, right-click the Wi-Fi adapter > **Disable device**, use Ethernet or USB tethering for a day, and see if crashes stop.
3. Run your manufacturer's UEFI hardware diagnostics (F2/Del/Esc at boot) for a full system scan.
4. A device that fails diagnostics or crashes across every driver version needs replacement — on most laptops the Wi-Fi card is a small, inexpensive M.2 module a shop can swap quickly.

## Closing

DRIVER_POWER_STATE_FAILURE is a checklist problem: name the driver from the dump, get the manufacturer's proper version, tame the power settings, kill Fast Startup, and update the BIOS. Taken in that order, the sleep/wake crashes stop — and you'll know exactly which step did it. For the HP-specific version of this repair, see [DRIVER_POWER_STATE_FAILURE on HP](/articles/how-to-fix-driver-power-state-failure-on-hp-laptop/), and for the Lenovo angle, [driver power state failure on Lenovo](/articles/how-to-fix-driver-power-state-failure-on-lenovo-laptop/) covers that brand's driver paths. Microsoft's [power troubleshooting guidance](https://support.microsoft.com/en-us/windows) covers the official settings reference.
