---
title: "Fixing APC_INDEX_MISMATCH on Windows 11"
slug: how-to-fix-apc-index-mismatch-on-windows-11
date: 2026-09-30
categories: ["windows-errors"]
tags: ["blue screen", "apc index mismatch", "stop code 0x1", "graphics driver", "windows 11"]
description: "APC_INDEX_MISMATCH (0x1) blue screening Windows 11? Fix this driver APC bookkeeping bug in 7 steps — graphics and audio drivers first."
thumbnail: "/images/thumbs/how-to-fix-apc-index-mismatch-on-windows-11.webp"
faqs:
  - q: "What does APC_INDEX_MISMATCH mean?"
    a: "It's stop code 0x00000001. Drivers must balance disabling and re-enabling Asynchronous Procedure Calls; when a driver gets the count wrong, kernel scheduling state becomes inconsistent and Windows crashes. It's a driver bug in essentially every case."
  - q: "Why did this start after upgrading to Windows 11?"
    a: "Windows 11 validates APC state more strictly in some paths, and drivers written for Windows 10 may trip the new checks. Updating those drivers to Windows 11-specific versions from your manufacturer's support page usually resolves it."
  - q: "Which driver should I update first?"
    a: "The graphics driver — it's the most common trigger because the graphics subsystem is APC-heavy. Audio drivers (especially Realtek) are second. The .sys file named on the crash screen tells you exactly which one."
  - q: "How is this different from the Windows 10 version of the error?"
    a: "The cause and fixes are nearly identical; only the driver versions and settings locations differ slightly. If you're still on Windows 10, our [Windows 10 APC_INDEX_MISMATCH guide](/articles/how-to-fix-apc-index-mismatch-on-windows-10/) covers that side."
---

APC_INDEX_MISMATCH (0x1) on Windows 11 is the same driver bookkeeping bug as on Windows 10: a driver disabled and re-enabled Asynchronous Procedure Calls an unequal number of times, leaving the kernel's internal state inconsistent. Windows 11's stricter validation just catches it more reliably — which is why many people first meet this crash after upgrading.

The fix is refreshingly direct: find the driver, fix the driver.

## Why this happens

- **Outdated graphics driver.** The win32k graphics path is APC-intensive — display drivers are the top trigger.
- **Windows 10-era drivers on Windows 11.** Old drivers tripping new validation after an upgrade.
- **Realtek audio driver bugs.** Audio drivers have a long, documented history with this stop code.
- **Antivirus filter drivers.** Kernel hooks mismanaging APC state.
- **Corrupted driver installations.** Partial updates leaving mismatched driver components.
- **Feature update changed kernel behavior.** A Windows 11 update exposing latent driver bugs.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Read the crash screen for the driver name

Get the clue before it disappears.

1. Note any `.sys` filename on the blue screen — `win32kfull.sys` points at the graphics stack, `rtkvhd64.sys` at Realtek audio.
2. Photograph the screen if it's too fast to read.
3. After rebooting, confirm with BlueScreenView against `C:\Windows\Minidump`.
4. The named driver (or its device family) is your Fix 2 target.
5. If the blamed driver varies, suspect a deeper issue and keep reading — but that's uncommon for this code.

### Fix 2: Clean-reinstall the graphics driver

The highest-probability fix.

1. Download the current driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
2. Boot into Safe Mode, run Display Driver Uninstaller (DDU) to wipe the old driver fully.
3. Restart normally and install fresh, selecting **Clean installation**.
4. For Intel integrated graphics, use [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for the correct Windows 11 build.
5. Test video playback, calls, and gaming — the common APC-heavy triggers.

### Fix 3: Update the audio driver

The runner-up cause, especially Realtek.

1. Open **Device Manager > Sound, video and game controllers**.
2. Right-click the audio device: **Update driver** — or **Roll Back Driver** if crashes started after an audio update.
3. For a clean fix, uninstall the audio device (keep a downloaded replacement driver ready), restart, and install the manufacturer's Windows 11 audio package.
4. Get the driver from your laptop maker's support page rather than Windows Update for the best-matched version.
5. Test with audio playback and video calls.

### Fix 4: Remove third-party security and utility software

Filter drivers are frequent APC-mismanagers.

1. Uninstall third-party antivirus, "driver updaters," and system optimizers via **Settings > Apps > Installed apps**.
2. Restart — Windows Defender activates automatically.
3. Test for a couple of days of normal use.
4. If crashes stop, the removed software's kernel driver was the cause; only reinstall updated versions.
5. Similar driver-level crashes and their hunt are detailed in our [DRIVER_IRQL_NOT_LESS_OR_EQUAL guide](/articles/what-to-do-if-driver-irql-not-less-or-equal/).

### Fix 5: Install all Windows 11 updates

The OS itself sometimes contains the fix.

1. Go to **Settings > Windows Update** and install everything, including optional updates.
2. Check **Advanced options > Optional updates** for driver updates Microsoft has validated for Windows 11.
3. Some APC bugs are fixed in cumulative updates — an outdated build may simply contain the bug.
4. Restart after updates and retest.
5. If a specific update triggered the crashes, uninstall it (**Update history > Uninstall updates**) and pause updates briefly.

### Fix 6: Reset clocks and verify system files

Cover the secondary causes.

1. Enter BIOS/UEFI, disable XMP/EXPO and any overclocking, load optimized defaults.
2. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`.
3. Press **Windows + R**, type `mdsched.exe`, and run the memory diagnostic for completeness.
4. Test at stock settings.
5. APC mismatches surviving all of this are rare — re-examine which driver is named, since the answer is almost always there.

### Fix 7: Refresh the driver stack via reset

When the driver tangle is beyond manual repair.

1. Back up your files.
2. **Settings > System > Recovery > Reset PC**, **Keep my files**, **Cloud download**.
3. After reset, install Windows 11-specific drivers from your manufacturer's support page — chipset, graphics, audio, network, in that order.
4. Let Windows Update finish fully before installing third-party software.
5. Microsoft's Windows support hub has additional guided troubleshooting.

### Fix 8: Perform an in-place upgrade repair

Refresh Windows while keeping everything intact.

1. Download the **Media Creation Tool** from Microsoft's Windows 11 download page and create installation media.
2. Run `setup.exe` from the USB while booted into your current Windows (not booting from the USB).
3. Choose **Keep personal files and apps** when prompted.
4. Let the repair install complete — it replaces all system files and the driver store with fresh copies.
5. Afterward, reinstall only the drivers from your manufacturer's support page and test the crashing scenario before restoring anything else.

## Closing

APC_INDEX_MISMATCH on Windows 11 is one of the most straightforward blue screens you'll encounter: a driver miscounted, and clean-reinstalling the graphics and audio drivers fixes it the vast majority of the time. The upgrade angle just means you should prefer Windows 11-specific driver packages over whatever carried over. Note the named driver, fix it, and move on — this one rarely comes back once properly addressed. If it does return, check Windows Update history first — a re-offered bad driver is the usual repeat offender, and hiding that specific update buys lasting peace. Keep a record of the working driver versions somewhere safe; when Windows Update inevitably offers a replacement months from now, you'll know exactly which versions to protect. APC crashes reward this kind of record-keeping because the same few drivers cause them again and again. If you're seeing this same stop code on a setup where the Windows 11 specifics don't apply, our [APC Index Mismatch blue screen guide](/articles/apc-index-mismatch-blue-screen-error-fix/) runs the identical diagnosis in version-neutral form.
