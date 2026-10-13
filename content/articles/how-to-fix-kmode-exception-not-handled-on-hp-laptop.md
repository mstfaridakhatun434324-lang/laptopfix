---
title: "KMODE_EXCEPTION_NOT_HANDLED on HP Laptop: Fix Guide"
slug: how-to-fix-kmode-exception-not-handled-on-hp-laptop
date: 2026-09-29
categories: ["windows-errors"]
tags: ["bsod", "hp laptop", "stop code", "drivers"]
description: "KMODE_EXCEPTION_NOT_HANDLED blue screen on your HP laptop? A kernel-mode driver threw an unhandled exception. Here's how to find and fix it."
thumbnail: "/images/thumbs/how-to-fix-kmode-exception-not-handled-on-hp-laptop.webp"
faqs:
  - q: "What does KMODE_EXCEPTION_NOT_HANDLED mean?"
    a: "A kernel-mode program — almost always a driver — generated an exception (like accessing invalid memory) that no error handler caught. Windows crashes because an unhandled exception in kernel mode means the system's integrity can't be trusted."
  - q: "Which driver causes KMODE_EXCEPTION_NOT_HANDLED on HP laptops?"
    a: "The minidump usually names it — often the network driver, storage driver, or a USB driver. On HP laptops, outdated Realtek network drivers and generic Windows Update graphics drivers are frequent offenders. Always check the dump before updating blindly."
  - q: "Can overclocking cause KMODE_EXCEPTION_NOT_HANDLED?"
    a: "Yes. Unstable CPU or RAM overclocks corrupt the data drivers operate on, producing exceptions that look like driver bugs. If you've enabled XMP or overclocked, reset to stock speeds while troubleshooting."
  - q: "Is this error related to Fast Startup?"
    a: "Sometimes. Fast Startup preserves driver state across shutdowns, so a driver that crashed once can keep crashing on every boot. Disabling Fast Startup forces clean driver initialization and resolves a real subset of these cases."
---

`KMODE_EXCEPTION_NOT_HANDLED` (stop code `0x0000001E`) is the kernel's version of an uncaught error: a driver running in kernel mode hit an exception — bad memory access, divide by zero, illegal instruction — and nothing handled it. User-mode programs crash quietly when this happens. Kernel-mode drivers take the whole system down with them, because the kernel can't trust its own state afterward.

On HP laptops, this crash has a familiar shape: it shows up after Windows Update swaps in a generic driver over HP's customized one, or after a driver update that introduced a regression. The dump file almost always names the guilty driver, which makes this one of the more solvable blue screens — if you read the evidence instead of updating everything at random.

## Why this happens

- **Faulty or incompatible driver**: The direct cause in most cases. Network, storage, and USB drivers top the list; the dump names the offender.
- **Generic Windows Update drivers over HP customizations**: Windows Update installs generic Realtek, Intel, or graphics drivers that misbehave on HP hardware tuned for customized versions.
- **Corrupt driver files**: Half-completed updates or disk errors leave driver files in an inconsistent state that throws exceptions.
- **Failing RAM**: Bad memory corrupts driver data, producing exceptions the driver didn't cause. The dump blames the driver, but the RAM is guilty.
- **Unstable overclocks or XMP**: Marginal memory/CPU settings corrupt kernel-mode operations under load.
- **Fast Startup preserving bad driver state**: A driver that crashed once gets its broken state reloaded on every "fast" boot.
- **Conflicting drivers**: Two drivers fighting over the same hardware (common with USB and audio stacks) can throw exceptions at each other.

## How to fix it

Work through these in order — read the dump first so every step after it is targeted.

### Fix 1: Read the minidump to identify the driver

This crash almost always names its culprit. Use that.

1. Navigate to `C:\Windows\Minidump` and open the newest `.dmp` in WinDbg Preview.
2. Run `!analyze -v` and note the `IMAGE_NAME` — e.g., `rtwlanu.sys` (Realtek Wi-Fi), `ntoskrnl.exe` (often a red herring pointing at RAM), or a USB driver.
3. If the same driver appears in every dump, that's your target. If it's `ntoskrnl.exe` or varies each time, suspect RAM and jump to Fix 4 after doing Fix 2.
4. Write down the exact driver name — you'll need it for the targeted update in Fix 2.

### Fix 2: Update the named driver from HP

HP-customized drivers first, generic second.

1. Open **HP Support Assistant** (**Win + S**, type `hp support assistant`) and install all updates, or get them from [HP Support](https://support.hp.com/us-en) with your serial number.
2. If the dump blamed the network driver and HP's version is old, get the newer one from the chip maker (Realtek, Intel, MediaTek) — but keep HP's as fallback.
3. For graphics blame, uninstall in **Device Manager** (tick driver removal), restart, then install HP's graphics driver clean.
4. Intel-based HP laptops: run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch Wi-Fi, Bluetooth, and chipset updates HP hasn't packaged yet.

### Fix 3: Disable Fast Startup

Forces clean driver initialization on every boot.

1. Open **Control Panel** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and untick **Turn on fast startup**.
3. **Save changes**, then shut down fully (not restart) and power back on.
4. This alone fixes cases where a corrupted driver state was being reloaded every boot.

### Fix 4: Test your RAM

When the dump is inconclusive or blames the kernel itself, test memory.

1. Press **Win + R**, type `mdsched.exe`, press Enter, choose **Restart now and check for problems**.
2. Any error = bad RAM. For intermittent crashes, run MemTest86 overnight for the conclusive answer.
3. Also disable XMP in the BIOS (**F10** at the HP logo) while testing — unstable memory timings produce exactly these exceptions.
4. Related: the [DRIVER_OVERRAN_STACK_BUFFER guide for HP](/articles/how-to-fix-driver-overran-stack-buffer-on-hp-laptop/) covers a sibling stop code with the same driver-hunting method.

### Fix 5: Repair system files

Corruption in kernel components can throw unhandled exceptions too.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart. Quick step, real fixes.

### Fix 6: Update the BIOS

HP BIOS updates fix hardware-initialization bugs that surface as driver exceptions.

1. Check your BIOS version with `msinfo32`.
2. Download the latest for your model from [HP Support](https://support.hp.com/us-en).
3. Flash with the charger plugged in and the laptop idle.

### Fix 7: Clean-boot to isolate conflicts

Two drivers fighting over hardware produce exceptions.

1. Press **Win + R**, type `msconfig`, press Enter.
2. **Services** tab: tick **Hide all Microsoft services**, then **Disable all**. Disable all **Startup** items in Task Manager.
3. Restart and test. Re-enable in halves to find the conflict.
4. USB peripheral software, RGB controllers, and "game booster" utilities are classic finds.

### Fix 8: Reset Windows

For a driver stack too tangled to untangle.

1. Back up your files.
2. **Settings** > **System** > **Recovery** > **Reset this PC** > **Keep my files**.
3. After reset, install HP drivers from Support Assistant before Windows Update gets creative.
4. If crashes persist after a clean reset with HP drivers, it's hardware — usually RAM or the motherboard — and time for service. For power-state-flavored crashes, also see [Driver Power State Failure fix](/articles/driver-power-state-failure-windows-11-fix/).

## Closing

`KMODE_EXCEPTION_NOT_HANDLED` on an HP laptop is a detective story with the evidence handed to you: the minidump names the driver, HP's support site has the replacement, and Fast Startup plus memory tests cover the edge cases. Read the dump, update the right driver from the right source, and this particular blue screen loses its mystery — and its ability to ruin your day.

Keep the minidump habit for any future blue screen, too. Five minutes reading the blamed driver saves hours of blind updates. And once the system is stable, consider exporting your working driver set or imaging the drive — the next driver disaster becomes a restore job instead of another detective case.
