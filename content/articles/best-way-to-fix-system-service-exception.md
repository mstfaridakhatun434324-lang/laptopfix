---
title: "The Best Way to Fix the System Service Exception BSOD"
slug: best-way-to-fix-system-service-exception
date: 2026-09-14
categories: ["windows-errors"]
tags: ["system service exception", "bsod", "driver error", "windows 11"]
description: "The SYSTEM_SERVICE_EXCEPTION blue screen usually means a bad driver. Here's the best-practice fix order: identify the driver, update or roll back, and verify."
thumbnail: "/images/thumbs/best-way-to-fix-system-service-exception.webp"
faqs:
  - q: "What causes the System Service Exception blue screen?"
    a: "A driver or system service executed an illegal operation while running in kernel mode — typically accessing invalid memory. Stop code 0x0000003B. Graphics drivers are the most frequent offenders, followed by webcam, network, and antivirus filter drivers. The blue screen often names the guilty .sys file in parentheses after the stop code."
  - q: "How do I find which driver caused it?"
    a: "Check the blue screen itself for a filename like nvlddmkm.sys or rtwlanu.sys. If you missed it, open Event Viewer's System log for the BugCheck entry, or analyze the minidump in C:\\Windows\\Minidump with WinDbg or BlueScreenView. The named file maps directly to a device whose driver needs updating or rolling back."
  - q: "Is System Service Exception a virus?"
    a: "Almost never. It's a driver bug, not malware — though a Defender offline scan is cheap insurance and worth running once. Real causes are outdated or corrupt drivers, especially graphics drivers, and occasionally failing hardware. Treat it as a driver problem first and you'll be right the vast majority of the time."
  - q: "Will updating my graphics driver fix it?"
    a: "Very often, yes. Graphics drivers run complex kernel-mode code and are implicated in a large share of these crashes. Do a clean install of the latest driver from NVIDIA, AMD, or Intel — using the installer's clean-install option — rather than relying on Windows Update's version. If the crash started right after a driver update, roll back instead."
---

SYSTEM_SERVICE_EXCEPTION (stop code 0x0000003B) is the blue screen of driver bugs. It means a driver or system service tried to execute an illegal operation while running in kernel mode — the privileged layer where drivers live. Unlike some stop codes that point at hardware, this one points at software with unusual directness: in most cases, a single misbehaving driver, and the blue screen frequently names it in parentheses right after the stop code.

The best-practice fix order is: identify the driver, then update it (or roll it back if the crash started after an update), then verify with stress testing. Graphics drivers lead the offender list — they run enormous amounts of kernel-mode code — followed by webcam, network, Bluetooth, and antivirus filter drivers. This guide follows that order exactly. If the blue screen names a different stop code alongside this one, our [IRQL fix guide](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/) covers its closest relative, and our [dedicated System Service Exception reference](/articles/system-service-exception-windows-11-fix/) has additional driver-specific detail.

## Why this happens

- **Buggy graphics drivers**: The top cause — GPU drivers execute complex kernel code where a single bad memory access triggers the exception.
- **Outdated webcam/network drivers**: These run constantly in the background and crash when they mishandle power-state transitions.
- **Antivirus filter drivers**: Deep kernel hooks from security software can throw exceptions after their own updates.
- **Corrupt driver installations**: Partially installed or mixed-version driver files produce unpredictable kernel behavior.
- **Windows update conflicts**: An update can ship a driver or kernel change incompatible with your existing driver set.
- **Failing hardware**: Bad RAM or a dying drive can corrupt driver code in memory, producing exceptions the driver didn't cause.
- **Overclocked GPU**: Unstable graphics overclocks cause driver exceptions under load that vanish at stock clocks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the guilty driver

Everything downstream depends on this identification.

1. If the blue screen named a file (e.g., `nvlddmkm.sys`, `dxgmms2.sys`, `rtwlanu.sys`), write it down — that file belongs to a specific device driver.
2. If you missed it, open **Event Viewer** > **Windows Logs** > **System**, find the **BugCheck** error at the crash time, and note the details.
3. For deeper analysis, the minidump at `C:\Windows\Minidump` can be opened with the free BlueScreenView tool, which highlights the suspect driver in red.
4. Map the filename to hardware: `nvlddmkm.sys` = NVIDIA graphics, `atikmdag.sys`/`amdkmdag.sys` = AMD graphics, `igdkmd64.sys` = Intel graphics, `rtwlan*` = Realtek Wi-Fi, `Netwtw*` = Intel Wi-Fi.

### Fix 2: Clean-install the latest graphics driver

The highest-yield single fix for this stop code.

1. Download the newest driver for your exact GPU from the manufacturer: [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx), [AMD's driver support](https://www.amd.com/en/support/download/drivers.html), or Intel's driver assistant for Intel graphics.
2. During installation, choose **Custom** and tick **Clean installation** (NVIDIA) or **Factory reset** (AMD) — this removes the old driver completely instead of layering over it.
3. Restart and test with the workload that previously crashed (the game, the video call, the external monitor).
4. If crashes persist on the newest driver, try one version older — occasionally the latest release is itself the bug, and vendors pull or patch it within days.

### Fix 3: Roll back if the crash followed an update

When timing implicates a specific update, reverse it.

1. Open **Device Manager**, find the device for the suspect driver, right-click > **Properties** > **Driver** tab > **Roll Back Driver**.
2. If the crash followed a Windows update rather than a driver update, go to **Settings** > **Windows Update** > **Update history** > **Uninstall updates** and remove the recent one.
3. Test for several days before re-applying — and when you do, install the driver manually from the vendor rather than letting Windows Update choose the version.

### Fix 4: Update the remaining high-risk drivers

Don't stop at graphics — the other usual suspects deserve fresh drivers too.

1. In **Device Manager**, update (or reinstall from vendor sites): network adapters (Wi-Fi and Ethernet), webcam/imaging devices, Bluetooth, and chipset drivers.
2. For laptops, prefer the laptop manufacturer's driver page over the chip vendor's — OEMs sometimes customize these drivers, and generic versions can misbehave.
3. If you run third-party antivirus, update it or temporarily uninstall it with the vendor's removal tool to test — filter driver bugs are a known source of this exact exception.
4. Restart after each driver change and test; changing one thing at a time is how you confirm which one mattered.

### Fix 5: Run Driver Verifier to catch the culprit (advanced)

When the guilty driver won't reveal itself, force it to confess.

1. Press **Windows + R**, type `verifier.exe`, and press Enter.
2. Choose **Create standard settings** > **Select driver names from a list**, and tick only non-Microsoft drivers you suspect (graphics, network, webcam).
3. Restart — Verifier stresses those drivers, and the guilty one will blue-screen faster with a more informative stop code like DRIVER_VERIFIER_DETECTED_VIOLATION naming it.
4. **Important**: after identifying the driver (or after 24–48 hours), run `verifier /reset` and restart — never leave Verifier running permanently, as it slows the system and can cause crashes on its own.

### Fix 6: Repair system files and scan for malware

Cover the non-driver possibilities.

1. Open **Terminal (Admin)**, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then SFC again.
2. Run a **Microsoft Defender Offline scan** (**Settings** > **Privacy & security** > **Windows Security** > **Virus & threat protection** > **Scan options**) to rule out malware hooking kernel functions.
3. If SFC/DISM find and fix corruption and crashes stop, a damaged system file was amplifying or causing the exceptions.

### Fix 7: Test hardware and reset overclocks

When software is exhausted, verify the silicon.

1. Run Windows Memory Diagnostic (`mdsched.exe`) — bad RAM corrupts driver code in memory and produces exceptions no driver update fixes.
2. Run `chkdsk C: /f /r` to rule out storage corruption of driver files.
3. Reset any GPU overclock to stock clocks in your tuning utility, and disable XMP memory profiles in the BIOS — unstable clocks are a classic source of driver exceptions under load.
4. Monitor temperatures during the crashing workload; thermal throttling combined with aggressive clocks destabilizes drivers.

## Closing

SYSTEM_SERVICE_EXCEPTION rewards methodical driver work: identify the file, clean-install or roll back the driver, verify under load. The temptation is to shotgun-update every driver at once, but that destroys your ability to know what fixed it — and knowing matters, because the same bad driver version will try to reinstall itself through Windows Update. Pin the working version, block the bad one if needed, and keep the crash dump from the incident; if the exception ever returns, comparing dumps tells you in seconds whether it's the same driver or a new offender. For the full reference on this stop code including vendor-specific driver notes, see our [System Service Exception deep-dive](/articles/system-service-exception-windows-11-fix/).
