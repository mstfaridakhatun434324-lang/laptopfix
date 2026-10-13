---
title: "APC_INDEX_MISMATCH on a Lenovo Laptop: How to Fix It"
slug: how-to-fix-apc-index-mismatch-on-lenovo-laptop
date: 2026-09-05
categories: ["windows-errors"]
tags: ["blue screen", "apc index mismatch", "lenovo laptop"]
description: "APC_INDEX_MISMATCH blue screen on your Lenovo laptop? Usually a Realtek audio or graphics driver issue. Here's how to fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-apc-index-mismatch-on-lenovo-laptop.webp"
faqs:
  - q: "What causes APC_INDEX_MISMATCH on Lenovo laptops?"
    a: "The most common cause is the Realtek HD audio driver — certain versions are notorious for this exact stop code on Lenovo machines. Outdated graphics drivers, corrupted system files, and mismatched kernel drivers after Windows updates are the other usual suspects."
  - q: "Why does it happen most often with Realtek audio drivers?"
    a: "Realtek's driver makes asynchronous procedure calls (APCs) in a way that mismatches what the Windows kernel expects in certain builds. Lenovo ships specific Realtek versions tuned for their hardware; the generic Windows Update version sometimes isn't one of them, which is why the Lenovo-provided driver usually fixes it."
  - q: "Can I just disable the Realtek audio device to stop the crashes?"
    a: "As a temporary test, yes — disabling the device in Device Manager stops its driver from loading. But you'll lose sound, so it's only diagnostic. The real fix is installing the correct Lenovo-provided Realtek driver version."
  - q: "Does APC_INDEX_MISMATCH mean my RAM is bad?"
    a: "Rarely. Despite involving kernel calls, this stop code is driver-related in the overwhelming majority of cases. Only consider RAM testing if driver fixes fail completely — and even then, check the minidump first, which usually names the audio or graphics driver."
---
APC_INDEX_MISMATCH is a driver synchronization error — a driver made kernel calls in the wrong order, and Windows crashed rather than risk corruption. On Lenovo laptops, this stop code has a famous prime suspect: the Realtek audio driver. If your crashes mention `rtkvhd64.sys` or happen during audio use, you're likely one driver update away from fixed.

Work through these in order. For the Windows 10 variant, see [APC index mismatch on Windows 10](/articles/how-to-fix-apc-index-mismatch-on-windows-10/); if it started after an update, see [APC index mismatch after a Windows 11 update](/articles/fix-apc-index-mismatch-after-windows-11-update/).

## Why this happens

- **Realtek HD audio driver bug:** The classic Lenovo trigger — mismatched APC calls in certain driver versions.
- **Outdated graphics driver:** Intel/NVIDIA/AMD graphics drivers with similar kernel-call issues.
- **Wrong driver from Windows Update:** Generic Realtek driver replacing Lenovo's tuned version.
- **Corrupted system files:** Damaged kernel components after failed updates.
- **Third-party audio software:** Equalizers, virtual audio cables, and audio enhancers hooking the audio stack.
- **USB audio and DisplayLink drivers:** External docks and USB headsets install their own audio drivers that can trigger the same mismatch — disconnect them as a test.
- **BIOS/firmware mismatch:** Old Lenovo BIOS with newer Windows builds.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the blue screens stop appearing.

### Fix 1: Update the Realtek audio driver from Lenovo

The number-one fix for this stop code on Lenovo hardware.

1. Identify your exact model: press **Win + R**, type `msinfo32`, and note **System Model**.
2. Go to [Lenovo Support](https://support.lenovo.com/us/en/), enter your model or serial number.
3. Download the latest **Audio** driver (Realtek HD Audio) listed for your machine.
4. Open **Device Manager** (**Win + X** > **Device Manager**), expand **Sound, video and game controllers**.
5. Right-click **Realtek(R) Audio** > **Update driver** > **Browse my computer for drivers** and point it at the downloaded Lenovo driver. Or run Lenovo's installer directly.
6. Restart and test — especially with audio playing, since that's the trigger.

### Fix 2: Roll back the Realtek driver if crashes just started

If a recent driver update introduced the problem, reverse it.

1. In **Device Manager**, right-click **Realtek(R) Audio** > **Properties** > **Driver** tab.
2. Click **Roll Back Driver**, choose a reason, and confirm.
3. Restart and test.
4. Prevent Windows Update from reinstalling the bad version using the "show or hide updates" troubleshooter.
5. Check Lenovo Support periodically for a fixed driver release.

### Fix 3: Update graphics and chipset drivers

The secondary suspects — update them while you're at it.

1. In **Device Manager**, update **Display adapters** and **System devices**.
2. Install Lenovo's tested **chipset** and **graphics** drivers from [Lenovo Support](https://support.lenovo.com/us/en/).
3. Intel graphics users can also use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Restart and monitor for a day of normal use.

### Fix 4: Remove third-party audio software

Audio enhancers hook the same stack Realtek uses — conflicts are common.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Uninstall equalizers, virtual audio devices, audio "boosters," and old VoIP tools with their own audio drivers.
3. In **Device Manager**, under **Sound, video and game controllers**, uninstall any non-Realtek, non-Intel audio devices you don't use (right-click > **Uninstall device**).
4. Restart and test audio playback.

### Fix 5: Run SFC and DISM

Repairs kernel and system file damage that can manifest as APC mismatches.

1. Open an **administrator Command Prompt**.
2. Run `sfc /scannow` and wait.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and test.

### Fix 6: Update Lenovo BIOS and run Lenovo diagnostics

Firmware-level fix plus a hardware sanity check.

1. On [Lenovo Support](https://support.lenovo.com/us/en/), download the latest **BIOS** for your model.
2. Connect AC power and run the updater — don't interrupt it.
3. After updating, run **Lenovo Diagnostics** (via the Lenovo Vantage app or F10 at boot on many models) to rule out hardware.
4. Retest for stability.

### Fix 7: Disable the audio device as a diagnostic (temporary)

Confirms the audio driver is the culprit when nothing else is conclusive.

1. In **Device Manager**, right-click **Realtek(R) Audio** > **Disable device**.
2. Use the laptop (without sound) for a day.
3. No crashes? The Realtek driver is confirmed — re-enable it and focus on finding the right driver version (Fix 1), trying older Lenovo releases if the newest still crashes.
4. Crashes continue? Re-enable and investigate graphics/chipset drivers instead.

### Fix 8: Confirm with the minidump and try Lenovo's older driver

When the newest driver still crashes, the dump plus Lenovo's driver archive usually ends it.

1. Check **C:\Windows\Minidump** for recent `.dmp` files — confirm the faulting module is the audio driver (`rtkvhd64.sys`) and not something else masquerading as this stop code.
2. On [Lenovo Support](https://support.lenovo.com/us/en/), look beyond the latest audio driver: Lenovo keeps previous versions available for most models.
3. In **Device Manager**, uninstall the current Realtek driver (check **Attempt to remove the driver for this device**), restart, then install the older Lenovo version.
4. Block Windows Update from "upgrading" it again with the show/hide updates troubleshooter.
5. If two different Lenovo driver versions both crash, run the extended memory diagnostic (`mdsched.exe`) to rule out RAM before suspecting the motherboard.

## Closing

APC_INDEX_MISMATCH on a Lenovo is a driver-sync problem with a usual suspect, and that suspect is the Realtek audio driver. Installing Lenovo's version — not the generic one Windows Update prefers — ends most cases at Fix 1. If the newest Lenovo driver still crashes, don't assume the hardware is broken: try the previous release, since Realtek regressions are common and Lenovo's archive usually has older versions. Work the list in order, keep audio software minimal, and update the BIOS while you're at it. This stop code looks exotic but it's one of the most fixable blue screens there is — and once the right driver is in place, it stays fixed.
