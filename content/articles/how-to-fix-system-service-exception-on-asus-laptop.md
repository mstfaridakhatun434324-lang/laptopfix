---
title: "How to Fix SYSTEM_SERVICE_EXCEPTION on an Asus Laptop"
slug: how-to-fix-system-service-exception-on-asus-laptop
date: 2026-09-23
categories: ["windows-errors"]
tags: ["bsod", "drivers", "asus"]
description: "SYSTEM_SERVICE_EXCEPTION blue screen on your Asus laptop? Usually a driver failing a system call. Here's how to fix it."
thumbnail: "/images/thumbs/how-to-fix-system-service-exception-on-asus-laptop.webp"
faqs:
  - q: "What does SYSTEM_SERVICE_EXCEPTION mean?"
    a: "A system service (usually a driver) threw an exception while executing a routine — often an access violation when handling a system call (stop code 0x3B). It's a driver bug in most cases: graphics, network, webcam, or audio drivers."
  - q: "The BSOD names a .sys file. What do I do with that?"
    a: "That file is your prime suspect. Identify its device (e.g., nvlddmkm.sys = NVIDIA, rtwlane.sys = Realtek Wi-Fi), then update, roll back, or cleanly reinstall that specific driver. Don't update drivers randomly — target the named one."
  - q: "Why does it crash when I open the camera or a specific app?"
    a: "That app triggers the buggy driver. Webcam apps trigger camera drivers, games trigger GPU drivers, video calls trigger audio/network drivers. The triggering app tells you which driver family to investigate first."
  - q: "Is this related to Asus Armoury Crate or MyAsus?"
    a: "It can be — Armoury Crate and MyAsus install kernel-level drivers for fan control, lighting, and power profiles. If crashes started after an Armoury Crate update, its drivers are suspects. Update or reinstall Armoury Crate itself."
---

`SYSTEM_SERVICE_EXCEPTION` (stop code 0x3B) means a driver crashed while executing a system service routine — it tried to do something privileged, hit an exception (usually touching memory it shouldn't), and Windows stopped the system. The blue screen often names the .sys file responsible, which makes this one of the more directly diagnosable crashes.

On Asus laptops there's an extra suspect worth knowing about: Asus's own utilities — Armoury Crate, MyAsus — install kernel drivers, and their updates have a history of introducing exactly this crash. Keep them in mind alongside the usual driver suspects.

## Why this happens

- **Buggy graphics driver**: The most common cause — GPU drivers handle countless system calls, and bugs surface here.
- **Bad network/Wi-Fi driver**: Second most common, especially after Windows updates.
- **Asus utility drivers**: Armoury Crate / MyAsus kernel drivers for hardware control.
- **Webcam or audio driver**: Often implicated when crashes tie to video calls or camera apps.
- **Corrupted system files**: Damaged kernel components failing service routines.
- **Failing RAM**: Less common for this code, but bad memory corrupts the data drivers operate on.

## How to fix it

Work through these in order — identify the driver, then fix it.

### Fix 1: Read the dump and identify the driver

The .sys filename on the blue screen (or in the dump) is your shortcut.

1. Install **BlueScreenView** (NirSoft, free), open `C:\Windows\Minidump`, and check **Caused By Driver** on the latest dump.
2. Map common files: `nvlddmkm.sys` = NVIDIA, `amdkmdag.sys` = AMD, `igdkmd64.sys` = Intel graphics, `rtwlane.sys` = Realtek Wi-Fi, `Netwtw10.sys` = Intel Wi-Fi, `Asus*.sys`/`AsIO.sys` = Asus utilities.
3. Note what you were doing when it crashed — gaming (GPU), video call (camera/audio/network), or idle (background service).
4. If the dump blames `ntoskrnl.exe` generically, the real culprit corrupted kernel memory first — proceed to Driver Verifier in Fix 5.
5. Primer on dump analysis: our [SYSTEM_THREAD_EXCEPTION_NOT_HANDLED guide](/articles/system-thread-exception-not-handled-troubleshooting/) uses the same technique for a sibling stop code.

### Fix 2: Update the suspect driver cleanly

Target the identified driver — don't shotgun-update everything.

1. Download the latest driver from the authoritative source: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html), or Asus's official support site for your exact model (use only Asus's own site).
2. For GPU drivers, uninstall the old one first with **Display Driver Uninstaller (DDU)** in Safe Mode — the cleanest possible removal.
3. Install the fresh driver, choosing clean-installation options.
4. Restart and reproduce the original crash trigger (the game, the video call, the app).
5. If the newest driver still crashes, try the previous version — new releases occasionally introduce the bug.

### Fix 3: Update or reinstall Asus utilities

Asus's own software is a legitimate suspect on Asus hardware.

1. If crashes started after an Armoury Crate or MyAsus update, uninstall it (**Settings** > **Apps** > **Installed apps**), restart, and test.
2. If crashes stop, reinstall the latest version from Asus's official support site — or from the Microsoft Store (Armoury Crate is distributed there).
3. Also update **Asus System Control Interface** — the underlying driver package Asus utilities depend on. An outdated SCI with a new Armoury Crate (or vice versa) is a known crash combination.
4. If you don't use Armoury Crate's features, leaving it uninstalled is a valid permanent fix — Windows handles fans and power plans fine without it.

### Fix 4: Roll back recent driver updates

If the crash timeline matches a driver update, revert it.

1. **Device Manager** (**Win + X**) > right-click the suspect device > **Properties** > **Driver** tab > **Roll Back Driver**.
2. If greyed out, uninstall the device (check **Delete the driver software**), restart, and install the previous known-good version.
3. Block the bad version with Microsoft's **Show or hide updates** troubleshooter.
4. Check **Settings** > **Windows Update** > **Update history** — if Windows Update delivered the driver, hiding it there prevents reinstallation.
5. Our [blue screen after Windows 11 update guide](/articles/blue-screen-after-windows-11-update-troubleshooting/) covers update-driven crashes broadly.

### Fix 5: Run Driver Verifier on suspects

When dumps are inconclusive, Verifier forces the culprit to identify itself.

1. **Win + R** > `verifier` > **Create standard settings** > **Select driver names from a list**.
2. Check third-party drivers related to your crash pattern (GPU, network, Asus utility drivers).
3. **Finish**, restart, and use the laptop until it crashes — Verifier's dump names the violator.
4. Boot into Safe Mode, run `verifier`, **Delete existing settings**, then fix the named driver.
5. If Verifier causes a boot loop, see our [Driver Verifier IOManager violation guide](/articles/best-way-to-fix-driver-verifier-iomanager-violation/) for the escape procedure.

### Fix 6: Repair system files

Corrupted kernel components fail service routines too.

1. Elevated Command Prompt (**Win + S** > `cmd` > right-click > **Run as administrator**).
2. `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
3. Restart and retest with the original trigger.
4. If SFC finds unfixable corruption, an in-place upgrade from [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) replaces all system files while keeping your data and apps.

### Fix 7: Test RAM as the final hardware check

If software fixes fail and dumps keep blaming the kernel, test memory.

1. `mdsched.exe` (**Win + R**) > **Restart now and check for problems**.
2. Confirm with MemTest86 overnight for intermittent faults.
3. Reseat RAM if accessible; replace faulty sticks with matching specs.
4. Also update the BIOS from Asus's support site — firmware fixes for system-call handling appear in changelogs.
5. Microsoft documents bug check troubleshooting on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

SYSTEM_SERVICE_EXCEPTION on an Asus laptop is a driver crashing mid-system-call — and the dump usually names it. Read the .sys filename, clean-install that driver, and don't forget Asus's own utilities (Armoury Crate, System Control Interface) as suspects. Target the named driver instead of updating everything blindly, and the crashes stop as suddenly as they started.
