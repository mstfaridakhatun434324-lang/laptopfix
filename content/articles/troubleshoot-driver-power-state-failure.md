---
title: "DRIVER_POWER_STATE_FAILURE Troubleshooting: Hunt Down the Bad Driver"
slug: troubleshoot-driver-power-state-failure
date: 2026-10-02
categories: ["windows-errors"]
tags: ["driver power state failure", "0x9f", "troubleshooting", "sleep wake", "windows 11"]
description: "Troubleshoot DRIVER_POWER_STATE_FAILURE (0x9F) like a technician: read the dump, identify the blocking driver, and prove the fix with sleep/wake testing."
thumbnail: "/images/thumbs/troubleshoot-driver-power-state-failure.webp"
faqs:
  - q: "How do I identify which driver causes DRIVER_POWER_STATE_FAILURE?"
    a: "Open the crash dump in WinDbg or BlueScreenView. In a 0x9F dump, parameter 1 tells you the failure subtype and the stack usually shows the driver stuck processing a power IRP — frequently a network driver like Netwtw10.sys or a USB driver. The !irp command in WinDbg on the blocked IRP address names the exact driver. Pattern analysis helps too: crashes on wake implicate network and USB; on shutdown, storage and display."
  - q: "What does parameter 1 of the 0x9F bugcheck tell me?"
    a: "The most common value is 0x3, meaning a device object has been blocking an IRP for too long — a driver didn't finish its power transition. The parameters that follow identify the physical and functional device objects involved, which WinDbg's !analyze translates into driver names. Value 0x4 means the power transition timed out waiting on the Pnp subsystem. Either way, a driver failed to handle sleep, wake, or shutdown promptly."
  - q: "Can Driver Verifier help diagnose 0x9F crashes?"
    a: "Yes — it's one of the best uses of Verifier. Enable it for your suspect drivers (network, storage, USB), and the next power transition will crash faster with a much more precise dump naming the offender. Remember to boot into Safe Mode and run 'verifier /reset' afterward. Never leave Verifier enabled permanently; it's a diagnostic instrument, not a setting."
  - q: "Why do my 0x9F crashes only happen with my docking station connected?"
    a: "Docks are complex USB/Thunderbolt devices with their own network, audio, and display drivers — any of which can mishandle power transitions. The dock's Ethernet chip and USB controller drivers are the usual offenders. Update the dock's firmware and drivers from the dock manufacturer's site, test with the dock disconnected to confirm, and try different USB-C/Thunderbolt ports, which can behave differently."
---

DRIVER_POWER_STATE_FAILURE (0x9F) is a detective's blue screen. The stop code tells you *what* happened — a driver blocked a power transition too long — but not *which* driver. With dozens of drivers participating in every sleep/wake cycle, guessing is hopeless. This guide is the systematic hunt: read the dump to name the suspect, confirm with targeted testing, fix it, and prove the fix worked.

If you want the fix-first version — remedies in order without the forensics — our [companion repair guide](/articles/how-do-i-fix-driver-power-state-failure/) covers the same ground from the other direction. This one is for when you want to know exactly which driver is guilty and have the evidence to prove it.

## Why this happens

- **Network driver power bug**: Wi-Fi and Ethernet drivers mishandle sleep/wake handshakes — the single most common 0x9F cause on laptops.
- **USB device driver stalling suspend**: Docks, external drives, and peripherals whose drivers don't complete power-down hang the entire transition.
- **Storage driver power-state bug**: NVMe/AHCI drivers that stall during disk power-down block shutdown and sleep.
- **Graphics driver power transition hang**: GPU drivers juggling multiple power states can wedge during transitions.
- **Dock firmware/driver issues**: Thunderbolt/USB-C docks bundle several drivers; one bad one poisons every sleep cycle while connected.
- **BIOS ACPI bugs**: Firmware power-management tables that disagree with Windows cause transitions no driver can complete correctly.
- **Filter drivers delaying I/O**: Antivirus and backup filters holding I/O open during shutdown stretch transitions past the timeout.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Build your crash log and spot the pattern

Evidence first — the pattern often names the subsystem before you open a single dump.

1. For each crash, record: what power action preceded it (lid close, lid open, sleep button, shutdown, hibernate), what was connected (dock? USB devices? charger?), and the time.
2. After 3–4 crashes, look for the common thread: always on wake → network/USB/display; always on shutdown → storage; only with the dock → dock drivers/firmware.
3. Photograph one full blue screen to confirm the stop code is genuinely 0x9F every time — mixed stop codes mean a different problem.
4. This log also becomes your test plan later: you'll re-run the exact failing scenario to prove each fix.

### Fix 2: Read the dump with WinDbg's !irp

The dump usually contains the driver's name — extract it properly.

1. Open the latest minidump in WinDbg Preview (symbols configured — see our [dump-reading guide](/articles/how-to-read-dump-files-with-windbg-in-windows-11-24h2/)).
2. Run `!analyze -v`. For 0x9F with parameter 1 = 0x3, note the device object addresses in the parameters.
3. Run `!irp <address>` on the blocked IRP — the output names the driver holding it. That's your prime suspect, caught red-handed.
4. Run `lmvm <drivername>` to get its version and timestamp. A driver from 2019 handling power transitions on Windows 11 24H2 is a strong update candidate.

### Fix 3: Confirm with the disconnect test

Prove the suspect before changing software — isolation beats assumption.

1. Disconnect all USB devices, docks, and external displays. Run your failing scenario (e.g., five sleep/wake cycles) with nothing attached.
2. If crashes stop, reconnect devices one at a time, testing the scenario after each. The crash's return identifies the device.
3. For internal suspects (Wi-Fi), disable the device in Device Manager instead of disconnecting, then test.
4. If crashes continue with everything disconnected and Wi-Fi disabled, the suspect is an internal driver — storage, chipset, or graphics. Proceed to Fix 4.

### Fix 4: Update the identified driver from the right source

Precision update — the exact driver, from the manufacturer, not Windows Update's generic.

1. Download the driver for your exact model from the laptop manufacturer's support page — [Dell](https://www.dell.com/support), HP, Lenovo. For Intel Wi-Fi, [Intel's assistant](https://www.intel.com/content/www/us/en/support/detect.html) is authoritative.
2. For a truly clean update of network drivers: uninstall the old driver in Device Manager (tick "delete driver software"), reboot, then install the fresh download.
3. For docks, update the dock firmware from the dock maker's site — firmware fixes resolve 0x9F cases that driver updates don't.
4. Re-run your failing scenario five times. Stable across all five is a confirmed fix, not luck.

### Fix 5: Neuter the device's power management

When the driver can't be fixed, stop it from participating badly.

1. In Device Manager, open the suspect device's **Properties** > **Power Management** tab and untick **Allow the computer to turn off this device to save power**.
2. In **Settings** > **System** > **Power & battery**, check whether crashes correlate with specific power modes — test on Best Performance vs. Balanced.
3. For USB suspects: in Device Manager under **Universal Serial Bus controllers**, disable **USB selective suspend** via Power Options > **Change plan settings** > **Change advanced power settings** > **USB settings**.
4. These are workarounds that confirm the diagnosis while you wait for a proper driver fix — legitimate, but keep pushing the vendor for an update.

### Fix 6: Deploy Driver Verifier against the suspects

When dumps are inconclusive, make the culprit crash louder.

1. Run `verifier`, choose **Create standard settings** > **Select driver names from a list**, and tick your suspect drivers.
2. Reproduce the scenario. Verifier stresses the drivers — the crash comes faster and the dump is far more precise about the offender.
3. Analyze the new dump: Verifier-instrumented crashes name names clearly.
4. Boot to Safe Mode and run `verifier /reset` immediately after. Leaving Verifier on degrades performance and can cause crashes on its own — it's a lab instrument.

### Fix 7: Check BIOS and the hibernation path

Widen to firmware when drivers check out.

1. Compare your BIOS version against the manufacturer's latest; flash if behind, reading release notes for ACPI/power mentions.
2. In an admin terminal, run `powercfg /h off`, reboot, then `powercfg /h on` — this rebuilds hiberfil.sys, eliminating corrupt hibernation state as a variable.
3. Disable Fast Startup (**Power Options** > **Choose what the power buttons do**) and retest — hybrid shutdown interacts with power-transition bugs.
4. Check **Event Viewer** > **System** for Kernel-Power events around crash times — event 41s and driver warnings there corroborate your dump findings.

### Fix 8: Document, report, and monitor

Close the loop like a professional.

1. Write down: the guilty driver (name + version), the fix applied, and the test results (e.g., "10 sleep/wake cycles, 0 crashes").
2. Report the buggy driver to the vendor with your dump attached — vendors fix what gets reported with evidence.
3. Keep the crash log going for two weeks post-fix. 0x9F bugs love to return with the next driver update — if they do, you'll catch the regression immediately instead of wondering.
4. If no driver can be proven guilty after all this, consider that the issue may be OS-level: check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for known 0x9F issues in your Windows build, and our [general fix guide](/articles/driver-power-state-failure-windows-11-fix/) for the remedy-ordered approach.

## Closing

Troubleshooting 0x9F is a solved problem once you stop guessing: log the pattern, read the dump with `!irp`, confirm with the disconnect test, update precisely, and verify with repeated scenario runs. The methodology matters more than any single fix because power-transition bugs are slippery — they hide behind "it worked fine yesterday" and return with driver updates. A technician's crash log and five deliberate sleep/wake cycles after every change turn this from a haunting into a closed case. Name the driver, prove it, fix it, verify it.
