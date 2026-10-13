---
title: "REFERENCE_BY_POINTER BSOD on Windows 11: Find and Fix the Faulty Driver"
slug: reference-by-pointer-bsod-bsod-windows-11
date: 2026-10-05
categories: ["windows-errors"]
tags: ["reference_by_pointer", "bsod", "windows 11", "drivers"]
description: "REFERENCE_BY_POINTER BSOD on Windows 11? This stop code means a driver mishandled a kernel object. Here's how to find the faulty driver."
thumbnail: "/images/thumbs/reference-by-pointer-bsod-bsod-windows-11.webp"
faqs:
  - q: "Why does REFERENCE_BY_POINTER happen more after upgrading to Windows 11?"
    a: "Windows 11's kernel enforces object reference counting more strictly than Windows 10 in some paths, and its updated driver model can expose latent bugs in older drivers. A driver that worked by luck on Windows 10 may crash on Windows 11. Updating to Windows 11-native driver versions usually resolves it."
  - q: "How do I find which driver causes REFERENCE_BY_POINTER on Windows 11?"
    a: "Enable minidumps, wait for the next crash, then analyze C:\\Windows\\Minidump with WinDbg or a dump viewer. The analysis names the faulting .sys file in most cases. Alternatively, Driver Verifier stresses non-Microsoft drivers until the buggy one crashes identifiably."
  - q: "Can Windows 11's memory integrity feature cause this?"
    a: "Memory integrity (HVCI) itself rarely causes REFERENCE_BY_POINTER directly, but it changes driver behavior requirements — incompatible drivers blocked or stressed by HVCI can crash in related ways. If crashes started after enabling memory integrity, check for driver updates or temporarily disable it to test."
  - q: "Will upgrading my drivers through Windows Update fix it?"
    a: "Sometimes, but Windows Update drivers lag behind manufacturer releases and occasionally install generic versions. For the suspect driver, download directly from the hardware vendor or your laptop manufacturer's support page — those are the versions tested against your exact hardware. Manufacturer drivers are worth the extra few minutes."
---


On Windows 11, `REFERENCE_BY_POINTER` deserves special attention because the OS upgrade itself is a common trigger. Windows 11 tightened several kernel behaviors around object lifetime management, and drivers written for Windows 10 — or hastily ported — can trip the stricter checks. The result: a laptop that was stable for years starts blue-screening after the Windows 11 upgrade, with a stop code that points at no obvious hardware failure.

The mechanism is the same as on any Windows version: a driver decrements a kernel object's reference count incorrectly, the object gets freed while still in use (or its count goes negative), and the next access crashes the system. What changes on Windows 11 is *which* drivers are most likely to be at fault — older Windows 10-era drivers, drivers for hardware whose vendor was slow with Windows 11 support, and the interaction with Windows 11 features like memory integrity and virtualization-based security. For the general version of this guide, see [REFERENCE_BY_POINTER troubleshooting](/articles/reference-by-pointer-bsod-troubleshooting/), and to read your own crash evidence, [how to analyze BSOD dump files on your laptop](/articles/how-to-analyze-bsod-dump-files-on-laptop/).

## Why this happens

- **Windows 10-era drivers on Windows 11**: The top Windows 11-specific cause. Old drivers with latent reference-count bugs crash under the new kernel's stricter checks.
- **Graphics drivers not updated for Windows 11**: GPU vendors ship Windows 11-specific driver branches; running the old branch causes exactly this class of crash.
- **Third-party antivirus filter drivers**: Security software that hasn't been updated for Windows 11's driver requirements manipulates object references unsafely.
- **Memory integrity (HVCI) interactions**: Drivers incompatible with virtualization-based security can crash when HVCI is enabled, sometimes with this stop code.
- **Storage driver mismatches**: Old AHCI/NVMe drivers carried over through the upgrade corrupt object references under Windows 11's I/O paths.
- **Corrupted driver store from the upgrade**: The in-place upgrade can leave a mix of old and new driver files — a corrupted hybrid that misbehaves.
- **Failing RAM as a secondary cause**: Uncommon, but bad memory corrupts reference counts and produces this crash with random blame across dumps.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether the crashes started with the Windows 11 upgrade

Establish the timeline before touching drivers.

1. Open **Settings** > **Windows Update** > **Update history** and find the Windows 11 feature update date.
2. Compare against your first REFERENCE_BY_POINTER crash (Event Viewer > Windows Logs > System, filter **BugCheck**). If crashes began within days of the upgrade, you're dealing with driver compatibility, not sudden hardware failure.
3. Note any driver names in the bug check details — a consistent name across crashes is your target.
4. If the laptop was upgraded long ago and crashes just started, treat it as a normal driver bug and still work the sequence below.

### Fix 2: Update the graphics driver to the Windows 11 branch

The most common individual fix.

1. Identify your GPU (**Win + X** > **Device Manager** > **Display adapters**).
2. Download the current Windows 11 driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) — make sure you select Windows 11 as the OS, not Windows 10.
3. Choose a clean installation during setup to remove the old branch's remnants.
4. For laptops, also check your manufacturer's support page (Dell, HP, Lenovo) — OEM-customized GPU drivers sometimes differ from vendor generics.

### Fix 3: Replace third-party security software temporarily

Windows 11's security stack conflicts with outdated filter drivers.

1. Uninstall third-party antivirus/firewall/VPN software using the vendor's removal tool — filter drivers frequently survive normal uninstalls.
2. Enable Microsoft Defender and use the laptop normally for several days.
3. If crashes stop, the old security driver was incompatible with Windows 11. Only reinstall the latest version explicitly marked Windows 11-compatible.
4. Check **Windows Security** > **Device security** > **Core isolation** > **Memory integrity** — if it's on and crashes correlate, try toggling it off temporarily as a test (leave it on long-term if possible; it's valuable protection).

### Fix 4: Update chipset and storage drivers for Windows 11

The upgrade often leaves these behind.

1. Visit your laptop manufacturer's support page, select your exact model and **Windows 11** as the OS.
2. Install the latest **chipset** driver package, restart, then the **storage/IRST/NVMe** driver, restart again.
3. If the manufacturer offers a "driver update utility," use it once for the full sweep — then uninstall the utility itself so it doesn't cause future conflicts.
4. Do not install storage drivers from Windows Update's optional section during diagnosis — use the manufacturer's versions.

### Fix 5: Analyze the minidump for the exact driver

Stop guessing and read the evidence.

1. Verify dumps: `sysdm.cpl` > **Advanced** > **Startup and Recovery** > **Settings** — **Small memory dump** selected, path `%SystemRoot%\Minidump`.
2. After the next crash, analyze the newest dump in `C:\Windows\Minidump` using our [dump analysis guide](/articles/how-to-analyze-bsod-dump-files-on-laptop/).
3. The faulting module name (a `.sys` file) identifies the driver — look it up to find its software package.
4. Deal with that specific driver: update from the vendor, roll back if recently updated, or uninstall the parent software if you don't need it.

### Fix 6: Run Driver Verifier against third-party drivers

Force the buggy driver to crash identifiably.

1. **Win + R** > `verifier` > **Create standard settings** > **Select driver names from a list** > check all non-Microsoft drivers.
2. Restart and use the laptop. Verifier adds overhead and the faulty driver will usually crash quickly — with its name on the stop screen this time.
3. Boot into Safe Mode, run `verifier /reset`, restart normally.
4. Fix the identified driver per the earlier steps. Never leave Verifier running as a permanent setting.

### Fix 7: Repair the driver store and finish updates

Clean up upgrade debris and get current.

1. Elevated prompt: `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — this repairs corrupted driver store components.
2. Install every pending Windows update, then check **Advanced options** > **Optional updates** for driver updates matching your hardware.
3. If crashes persist after all driver work, run `mdsched.exe` memory diagnostics — random blame across dumps after driver fixes points to RAM.
4. As a last resort before hardware suspicion, an in-place upgrade repair from the Windows 11 ISO (keeping files and apps) rebuilds the driver store cleanly.

## Closing

REFERENCE_BY_POINTER after moving to Windows 11 is a compatibility story, not a hardware obituary — old drivers meeting a stricter kernel. The fix is bringing the driver stack up to the Windows 11 branch: GPU, chipset, storage, and security software, in that order of suspicion. Do that methodically, verify with dumps, and the stop code disappears with the last outdated driver.
