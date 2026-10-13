---
title: "How to Fix SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on Windows"
slug: how-to-fix-system-thread-exception-not-handled
date: 2026-09-03
categories: ["windows-errors"]
tags: ["blue screen", "system thread", "driver error"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED blue screen? A system thread crashed — usually a bad driver. Here's how to find it and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-system-thread-exception-not-handled.webp"
faqs:
  - q: "What does SYSTEM_THREAD_EXCEPTION_NOT_HANDLED mean?"
    a: "A Windows system thread threw an exception (error) that nothing caught, so the system crashed. In practice, it's almost always a faulty driver — the blue screen often names the culprit file (like atikmdag.sys, nvlddmkm.sys, or a network driver) right on the screen."
  - q: "How do I find which driver caused it?"
    a: "Check the blue screen itself — it usually shows 'What failed: xxx.sys'. If you missed it, open the minidump: the faulting driver is listed there. Our dump-reading guide walks through it. Event Viewer (eventvwr.msc) around the crash time also helps."
  - q: "Can this error appear in a boot loop?"
    a: "Yes — if the faulty driver loads at startup, every boot crashes. Use Safe Mode (which skips most third-party drivers) to get in, then update, roll back, or remove the offending driver from there."
  - q: "Is SYSTEM_THREAD_EXCEPTION_NOT_HANDLED a virus?"
    a: "Extremely unlikely. It's a driver or system-file problem in virtually all cases. Still, a full Windows Security scan is quick and rules out the rare rootkit scenario while you troubleshoot."
---
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED means a background Windows thread hit an error nobody handled — and nine times out of ten, a driver threw it. The silver lining: this blue screen usually names the guilty file right on the screen ("What failed: some-driver.sys"), which turns a mystery into a targeted fix.

Your first job is catching that filename. If you saw it, skip to the driver fixes. If the screen vanished too fast, [disable automatic restart after blue screens](/articles/how-can-i-disable-automatic-restart-after-bsod/) so you can read the next one. Related thread crashes are covered in our [System Service Exception guide](/articles/how-to-fix-system-service-exception-reddit/).

## Why this happens

- **Faulty graphics driver:** AMD (`atikmdag.sys`) and NVIDIA (`nvlddmkm.sys`) drivers are the most commonly named files for this stop code.
- **Bad network/Wi-Fi driver:** Network drivers running in system threads crash here frequently.
- **Corrupted driver files:** Disk corruption damaging an otherwise good driver.
- **Incompatible driver after Windows update:** Old drivers that the new build's threading model breaks.
- **Overclocked GPU/CPU:** Unstable hardware causing thread exceptions under load.
- **Damaged system files:** Corrupted Windows thread-management components.
- **Bad Windows update:** A cumulative update that shipped with a broken driver or system file — check update history against the crash timeline.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the blue screens stop appearing.

### Fix 1: Catch the faulting driver name

Everything gets easier once you know the filename.

1. If the blue screen is still happening, photograph it — note the **"What failed:"** line.
2. Can't catch it? [Disable automatic restart](/articles/how-can-i-disable-automatic-restart-after-bsod/) so the screen stays up.
3. Alternatively, read the minidump: check **C:\Windows\Minidump** for `.dmp` files and analyze them per our [WinDbg guide](/articles/how-to-read-dump-files-with-windbg-on-windows-11/). Even a single dump usually names the faulting module clearly.
4. Common names and their owners: `atikmdag.sys`/`atikmpag.sys` = AMD graphics, `nvlddmkm.sys` = NVIDIA graphics, `igdkmd64.sys` = Intel graphics, `netwtw*.sys` = Intel Wi-Fi, `rtwlanu.sys` = Realtek Wi-Fi.

### Fix 2: Boot into Safe Mode

Safe Mode loads only essential drivers, bypassing the crashing one.

1. Force recovery: power on, hold power at the Windows logo to shut down. Twice. Third boot opens **Automatic Repair**.
2. **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4**.
3. If Safe Mode is stable, the culprit is a third-party driver — proceed with the fixes below from Safe Mode.
4. If Safe Mode crashes too, the problem is a boot-critical driver or system file — jump to Fix 6.

### Fix 3: Update the identified driver

Targeted fix once you know the filename from Fix 1.

1. In **Device Manager** (**Win + X** > **Device Manager**), find the device matching the faulting driver.
2. Right-click > **Update driver** > **Search automatically for drivers**.
3. Better: download the latest from the manufacturer — GPU makers' sites for graphics, Intel Driver & Support Assistant for Intel Wi-Fi/Bluetooth/chipset.
4. For graphics crashes specifically, do a **clean install**: use Display Driver Uninstaller (DDU) in Safe Mode to wipe the old driver, then install the fresh one.
5. Restart and test with the workload that triggered crashes.

### Fix 4: Roll back the driver if crashes started after an update

New driver versions introduce regressions regularly.

1. In **Device Manager**, right-click the device > **Properties** > **Driver** tab.
2. Click **Roll Back Driver** if available, pick a reason, confirm.
3. Restart and test.
4. Block the bad version from reinstalling via Windows Update's "show or hide updates" troubleshooter.
5. Report it to the vendor — and try the next driver release in a few weeks.

### Fix 5: Remove recently added hardware/software

New devices bring new drivers — prime suspects when timelines align.

1. In Safe Mode, open **Settings** > **Apps** > **Installed apps** and remove anything installed just before crashes began.
2. Physically disconnect recently added peripherals (USB devices, docks).
3. In **Device Manager**, uninstall the device (check **Attempt to remove the driver** if offered), then restart and let Windows install its inbox driver.
4. Reintroduce hardware one piece at a time after stability returns.

### Fix 6: Repair system files and check the disk

For cases where no third-party driver is clearly at fault.

1. Open an **administrator Command Prompt**.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f` (press **Y**, restart, let it finish).
4. Restart and monitor. If a Windows system driver was faulting, this is often the fix.
5. Also run a full **Windows Security** scan to rule out malware. If crashes persist with no driver identified, the motherboard or RAM becomes suspect — run the extended memory diagnostic to be thorough.

### Fix 7: Reset overclocks and update BIOS

Stability fixes for thread exceptions under load.

1. Enter BIOS/UEFI and load **Optimized Defaults** — disable any CPU/GPU overclocking and XMP profiles.
2. Update the BIOS from your maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) on AC power.
3. In Windows, set your GPU software (GeForce Experience, AMD Adrenalin) back to stock clocks if you'd tweaked them.
4. Stress-test with your normal workload.

## Closing

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is unusually cooperative as blue screens go — it usually tells you the filename of the driver that crashed. Catch that name, update or roll back that specific driver (clean-installing graphics drivers with DDU when theyre the culprit), and most cases end there. When the screen doesn't name a file, the minidump will — learning to read it pays for itself across every future blue screen. And remember the pattern: crashes that start right after a driver or Windows update are regressions until proven otherwise, so rollback is always worth trying before deeper surgery. Keep a note of which driver version works; the next update cycle will thank you. Targeted driver fixes beat reinstalls nearly every time.
