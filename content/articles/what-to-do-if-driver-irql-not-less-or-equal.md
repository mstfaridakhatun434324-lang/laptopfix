---
title: "DRIVER_IRQL_NOT_LESS_OR_EQUAL: What to Do Right Now"
slug: what-to-do-if-driver-irql-not-less-or-equal
date: 2026-09-22
categories: ["windows-errors"]
tags: ["blue screen", "driver irql", "stop code 0xd1", "driver crash", "windows 11"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL (0xD1) just crashed your laptop? Do these 7 things right now — identify the driver and stop the crashes."
thumbnail: "/images/thumbs/what-to-do-if-driver-irql-not-less-or-equal.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "It's stop code 0x000000D1. A driver tried to access memory at an improper IRQL (interrupt request level) — essentially, it touched pageable memory while running at a priority where only non-pageable memory is allowed. The named .sys file is the driver that broke the rule."
  - q: "What should I do immediately after this blue screen?"
    a: "First, note any .sys filename on the crash screen. Then boot up and check what changed recently — a driver or Windows update is the usual trigger. Don't keep pushing through repeated crashes; each one risks file corruption. Work the driver fixes below before using the laptop heavily."
  - q: "Is this caused by overclocking?"
    a: "It can be. Overclocked RAM especially causes drivers to read corrupted addresses, which manifests as IRQL errors blaming innocent drivers. If you've enabled XMP/EXPO or overclocked anything, reset to stock early in your troubleshooting."
  - q: "Can faulty RAM cause IRQL_NOT_LESS_OR_EQUAL?"
    a: "Yes — bad RAM corrupts the addresses drivers work with, producing IRQL crashes that blame random drivers each time. If the blamed driver changes with every crash, test your memory with mdsched.exe rather than chasing drivers."
---

DRIVER_IRQL_NOT_LESS_OR_EQUAL (0xD1) is the blue screen most likely to interrupt you mid-task with no warning. A driver accessed memory it had no business touching at its current privilege level, and Windows pulled the plug. The crash screen usually names the offender, which makes this one of the more actionable stop codes — if you act on the clue instead of just rebooting and hoping.

Here's what to do right now, in priority order.

## Why this happens

- **Faulty or outdated device driver.** The named `.sys` file broke IRQL rules — network and storage drivers are frequent offenders.
- **Recently updated driver with a bug.** Windows Update or manual updates install driver versions with IRQL mishandling.
- **Corrupted driver files.** Disk errors or interrupted updates damage driver binaries.
- **Faulty RAM corrupting driver addresses.** Bad memory makes good drivers touch bad addresses.
- **Overclocked memory destabilizing drivers.** XMP/EXPO instability shows up as IRQL errors.
- **Antivirus filter drivers.** Kernel-level security drivers operating at high IRQL are classic triggers.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Capture the culprit from the crash

Do this before the memory of the crash fades.

1. If the blue screen named a `.sys` file (e.g., `Netwtw10.sys`, `rt640x64.sys`, `nvlddmkm.sys`), write it down — that's your target.
2. After rebooting, open `C:\Windows\Minidump` with BlueScreenView to confirm the blamed driver across multiple crashes.
3. Consistent blame = guilty driver. Changing blame each time = suspect RAM (jump to Fix 5).
4. Note what you were doing — Wi-Fi activity implicates network drivers, gaming implicates GPU.
5. For the post-update pattern, see [DRIVER_IRQL_NOT_LESS_OR_EQUAL after a Windows 11 update](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/).

### Fix 2: Roll back or update the named driver

Strike at the identified driver immediately.

1. Open **Device Manager** (**Windows + X**), find the device, and open **Properties > Driver**.
2. If the crashes started recently, click **Roll Back Driver** — this is the fastest fix when a bad update caused it.
3. Otherwise, click **Update driver > Search automatically for drivers**.
4. For network drivers, get the latest from your laptop manufacturer's support page — Windows Update's versions lag.
5. Restart and test the exact activity that crashed. Broader driver-crash methodology is in our [SYSTEM_SERVICE_EXCEPTION guide](/articles/how-to-fix-system-service-exception-youtube/).

### Fix 3: Clean-reinstall network and storage drivers

These two categories cause most 0xD1 crashes.

1. In **Device Manager**, expand **Network adapters**, right-click your Wi-Fi adapter, and choose **Uninstall device**.
2. Restart — Windows reinstalls a fresh copy. If it doesn't, install the manufacturer's driver manually.
3. Do the same for storage controllers under **Storage controllers** and **IDE ATA/ATAPI controllers**.
4. Avoid "driver updater" utilities — they install mismatched versions that cause exactly this crash.
5. Test with heavy network and disk activity (large downloads, file copies).

### Fix 4: Remove third-party security and VPN software

Filter drivers run at the IRQL levels where this crash lives.

1. Uninstall third-party antivirus, firewall, and VPN clients via **Settings > Apps > Installed apps**.
2. Restart and let Windows Defender activate.
3. Test for a day of normal use.
4. If crashes stop, the removed product's driver was at fault — only reinstall an updated version.
5. Pay special attention to "network protection" features in security suites; they're frequent 0xD1 sources.

### Fix 5: Test RAM and reset memory clocks

Rule out memory as the hidden cause.

1. Press **Windows + R**, type `mdsched.exe`, and run the diagnostic (Extended mode via **F1**).
2. Enter BIOS/UEFI and disable XMP/EXPO profiles — test at stock memory speeds.
3. Check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
4. If errors appear, reseat or replace the faulty stick.
5. Retest the crashing scenario at stock clocks before declaring drivers guilty.

### Fix 6: Run Driver Verifier on suspect drivers

Catch the driver red-handed when dumps are ambiguous.

1. Press **Windows + R**, type `verifier`, and press Enter.
2. Choose **Create standard settings**, then **Select driver names from a list**.
3. Tick the suspect third-party drivers (network, storage, audio).
4. Restart and use the laptop — Verifier forces an immediate, clearly-labeled crash when the driver misbehaves.
5. Analyze the dump, fix the driver, then boot to Safe Mode and run `verifier /reset`.

### Fix 7: Repair system files and update everything

Finish with the OS layer.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. Install all pending Windows updates via **Settings > Windows Update**.
3. Update the BIOS/UEFI from the manufacturer's support page.
4. As a last resort, **Settings > System > Recovery > Reset PC** with **Keep my files**.
5. Microsoft's [blue screen troubleshooting hub](https://support.microsoft.com/en-us/windows) documents further recovery steps.

### Fix 8: Disconnect suspect USB peripherals during crashes

External devices cause more 0xD1 crashes than people expect.

1. Unplug all non-essential USB devices — docks, external drives, webcams, USB audio interfaces, and exotic peripherals.
2. Test the crashing scenario with only the charger and built-in devices.
3. If crashes stop, reconnect devices one at a time, testing between each, until the culprit returns.
4. Update that device's driver from the manufacturer's site, or replace the device if no updated driver exists.
5. Pay special attention to USB Wi-Fi adapters and docking stations — their drivers run at exactly the IRQL levels where this crash occurs.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL gives you everything you need on the crash screen itself — the driver's name. Act on it: roll back or update that driver first, clear out filter drivers second, and only then look at RAM. Most people fix this in under half an hour because the clue is right there. The only wrong move is rebooting repeatedly and hoping it was a fluke. Write the driver's name down once you've found it — future you will be grateful the next time an update brings it back.
