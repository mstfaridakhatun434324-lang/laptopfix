---
title: "Fixing APC_INDEX_MISMATCH on Windows 10"
slug: how-to-fix-apc-index-mismatch-on-windows-10
date: 2026-09-18
categories: ["windows-errors"]
tags: ["blue screen", "apc index mismatch", "stop code 0x1", "driver bug", "windows 10"]
description: "APC_INDEX_MISMATCH (0x1) blue screening your Windows 10 laptop? Fix this driver APC-state bug in 7 steps, newest drivers first."
thumbnail: "/images/thumbs/how-to-fix-apc-index-mismatch-on-windows-10.webp"
faqs:
  - q: "What does APC_INDEX_MISMATCH mean?"
    a: "It's stop code 0x00000001. APCs (Asynchronous Procedure Calls) are queued work items in the kernel, and each thread tracks whether APCs are enabled or disabled. When a driver changes that state inconsistently — disabling and enabling an unequal number of times — Windows crashes. It's almost always a driver bug."
  - q: "Which drivers cause APC_INDEX_MISMATCH?"
    a: "Graphics drivers are the classic offenders (the win32k path is heavily APC-dependent), followed by audio drivers — Realtek audio drivers have a long history with this stop code — and antivirus filter drivers. The named .sys file on the crash screen identifies yours."
  - q: "Can RAM cause this error?"
    a: "Uncommonly. This stop code is one of the most purely driver-caused crashes in Windows. Only consider RAM if the blamed driver changes every crash and driver fixes fail — even then, drivers remain the likelier story."
  - q: "Is this error specific to Windows 10?"
    a: "No — it exists on Windows 11 too, with the same causes and fixes. If you've upgraded, our [Windows 11 APC_INDEX_MISMATCH guide](/articles/how-to-fix-apc-index-mismatch-on-windows-11/) covers the same ground with Windows 11 specifics."
---

APC_INDEX_MISMATCH (0x1) is Windows catching a driver in a bookkeeping lie. Drivers must carefully balance disabling and re-enabling Asynchronous Procedure Calls around critical sections; when a driver gets the count wrong, the kernel's internal state no longer adds up, and Windows crashes rather than continue with corrupted scheduling state. It's a driver bug essentially every time.

The good news: because the cause is so consistent, the fix list is short and effective.

## Why this happens

- **Buggy graphics driver.** The win32k graphics path is APC-heavy, making display drivers the number-one trigger.
- **Realtek or other audio driver bugs.** Audio drivers have a notorious history with APC mismatches.
- **Antivirus filter drivers.** Kernel hooks that disable APCs and fail to restore them properly.
- **Corrupted driver installation.** A half-updated driver with mismatched components miscounts APC state.
- **Windows 10 update changed kernel behavior.** An update tightens APC validation, exposing bugs in older drivers that previously "worked."
- **Overclocking-induced corruption.** Unstable clocks corrupting driver execution state mid-APC-sequence.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Identify the named driver from the crash

The blue screen usually hands you the answer.

1. Note any `.sys` filename on the crash screen (common ones: `win32kfull.sys`, `rtkvhd64.sys`, `nvlddmkm.sys`).
2. If it flashes by too fast, analyze `C:\Windows\Minidump` with BlueScreenView after rebooting.
3. The named driver (or its device category) becomes your Fix 2 target.
4. If `win32kfull.sys` is named, the real culprit is usually the graphics driver feeding it bad calls.
5. Write it down — you'll need it in the next step.

### Fix 2: Clean-reinstall the graphics driver

Graphics drivers are suspect number one.

1. Download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) for your GPU.
2. Boot into Safe Mode and run Display Driver Uninstaller (DDU) to remove the old driver completely.
3. Restart and install the fresh driver with **Clean installation** selected.
4. For Intel integrated graphics, use [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) to get the correct build.
5. Test with the activity that crashed before — video calls and gaming are common triggers.

### Fix 3: Update or reinstall the audio driver

Realtek audio drivers are the runner-up cause.

1. Open **Device Manager**, expand **Sound, video and game controllers**.
2. Right-click your audio device and choose **Update driver**.
3. If crashes started after an audio driver update, use **Properties > Driver > Roll Back Driver** instead.
4. For a thorough fix, uninstall the audio device in Device Manager (tick "delete driver" if you have the replacement ready), restart, and install the driver from your laptop manufacturer's support page.
5. Test audio playback and calls — the triggers for this driver path.

### Fix 4: Remove third-party antivirus and system utilities

Filter drivers miscount APCs.

1. Open **Settings > Apps** and uninstall third-party antivirus, "driver updaters," and system optimizers.
2. Restart — Windows Defender takes over automatically.
3. Use the laptop normally for a day or two.
4. If stability returns, the removed product's kernel driver was the cause.
5. Only reinstall security software from the vendor's latest version, and watch for crash recurrence. Broader driver-crash techniques are in our [SYSTEM_SERVICE_EXCEPTION guide](/articles/how-to-fix-system-service-exception-youtube/).

### Fix 5: Repair system files

Rule out corruption in Windows' own APC machinery.

1. Open an elevated Command Prompt or **Terminal (Admin)**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for completion.
3. Then run `sfc /scannow` and restart.
4. If SFC finds and fixes corruption, monitor for a few days — recurring corruption hints at a failing drive.
5. Retest the original crash trigger.

### Fix 6: Reset overclocks and check memory

Cover the hardware-adjacent causes.

1. Enter BIOS/UEFI, disable XMP/EXPO and any CPU overclock or undervolt, and load optimized defaults.
2. Press **Windows + R**, type `mdsched.exe`, and run the memory diagnostic.
3. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
4. Test at stock settings for a couple of days.
5. APC mismatches surviving all driver fixes plus clean memory are rare — at that point, suspect the specific device's hardware.

### Fix 7: Update Windows 10 fully and consider the upgrade path

Finish with the OS layer.

1. Go to **Settings > Update & Security > Windows Update** and install everything pending, including optional driver updates.
2. Some APC bugs are fixed by Windows updates themselves — an outdated Windows 10 build may simply contain the bug.
3. If your laptop supports it, consider upgrading to Windows 11 via Microsoft's download page — newer kernel builds handle edge cases better.
4. Before upgrading, back up your files and confirm driver availability for Windows 11 on your model.
5. Microsoft's Windows support hub documents update-related troubleshooting.

### Fix 8: Use System Restore to roll back the system

When the crash has a clear start date, time-travel beats troubleshooting.

1. Press **Windows + R**, type `rstrui`, and press Enter to open System Restore.
2. Choose a restore point dated before the APC crashes began.
3. Let it complete — this reverts drivers, updates, and system files without touching your personal files.
4. After the restore, immediately pause Windows driver updates for a week (**Settings > Windows Update**) so the bad driver doesn't reinstall overnight.
5. Then manually install the known-good graphics and audio drivers from your manufacturer's support page.
6. If no restore points exist, enable System Protection afterward (**System Properties > System Protection > Configure**) so this safety net exists next time.

## Closing

APC_INDEX_MISMATCH is refreshingly straightforward: it's a driver bug, usually graphics or audio, and clean-reinstalling those two drivers resolves the vast majority of cases. Don't let the cryptic name intimidate you — the fix is mundane, quick, and free. Note which driver was named so that if it ever recurs, you go straight to the culprit. The version-neutral walkthrough of this same stop code — [APC Index Mismatch blue screen fix](/articles/apc-index-mismatch-blue-screen-error-fix/) — is a good reference if the Windows 10 menus here do not match your screen.
