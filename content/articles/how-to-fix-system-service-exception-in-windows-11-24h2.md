---
title: "SYSTEM_SERVICE_EXCEPTION in Windows 11 24H2: How to Fix It"
slug: how-to-fix-system-service-exception-in-windows-11-24h2
date: 2026-09-24
categories: ["windows-errors"]
tags: ["bsod", "stop code", "24h2", "drivers"]
description: "SYSTEM_SERVICE_EXCEPTION blue screen on Windows 11 24H2? Usually a bad driver or corrupt system files. Here's the exact fix order that works."
thumbnail: "/images/thumbs/how-to-fix-system-service-exception-in-windows-11-24h2.webp"
faqs:
  - q: "What causes SYSTEM_SERVICE_EXCEPTION on Windows 11 24H2?"
    a: "Almost always a driver passing bad data to the Windows kernel, or corrupted system files. On 24H2 specifically, older graphics, Wi-Fi, and webcam drivers that predate the update are the usual offenders, along with third-party antivirus drivers that hook deep into the system."
  - q: "Is SYSTEM_SERVICE_EXCEPTION a virus?"
    a: "Very rarely. The stop code means a system service threw an exception it couldn't handle — that's a software bug pattern, not a malware pattern. Still, run a quick Windows Security scan to be thorough, since rootkits can destabilize kernel services."
  - q: "Why did this start after updating to 24H2?"
    a: "Major Windows builds change kernel interfaces. Drivers written for 23H2 or earlier sometimes make calls that 24H2 handles differently, triggering the exception. Updating those drivers to 24H2-aware versions from the manufacturer usually ends it."
  - q: "Do I need to reinstall Windows to fix it?"
    a: "Almost never. Driver updates, SFC/DISM repairs, and removing the offending software resolve the vast majority of cases. Reinstallation is only warranted if the crash persists after every driver is current and system files verify clean."
---

`SYSTEM_SERVICE_EXCEPTION` is one of the most common blue screens on Windows 11 24H2, and it has a refreshingly straightforward meaning: a piece of code running in the kernel — usually a driver — did something illegal, and Windows crashed to protect itself. The stop code sometimes names a file on the blue screen (like `nvlddmkm.sys` or `ntfs.sys`), and that filename is a direct clue to the culprit.

On 24H2 this error spiked because the update changed enough under the hood that older drivers started misbehaving. The fix is almost always driver-side, and there's a logical order that gets you there without guesswork.

## Why this happens

- **Outdated drivers incompatible with 24H2**: Graphics, Wi-Fi, Bluetooth, and webcam drivers written for older builds make kernel calls that 24H2 rejects or handles differently, triggering the exception.
- **Third-party antivirus or VPN drivers**: These hook deep into the kernel's network and file stacks. After a major build update, those hooks are a leading cause of this exact stop code.
- **Corrupted system files**: Damage to kernel-mode components means even correct driver calls can throw exceptions when the underlying service is broken.
- **Faulty RAM corrupting kernel data**: Bad memory can corrupt the data structures system services rely on, producing exceptions that look like driver bugs.
- **Overclocking or unstable hardware**: CPU/RAM overclocks that were borderline-stable can push kernel operations over the edge, especially under the slightly different scheduling of a new build.
- **Conflicting software that installs drivers**: RGB control apps, fan utilities, virtual-drive tools, and Android emulators all install kernel drivers that can clash with each other.

## How to fix it

Work through these in order — the blue screen's filename clue (if shown) tells you where to focus.

### Fix 1: Identify the culprit file from the crash

Don't skip the detective work — it saves hours.

1. The next time it blue-screens, look for a filename in parentheses after the stop code, e.g. `SYSTEM_SERVICE_EXCEPTION (nvlddmkm.sys)`.
2. Common mappings: `nvlddmkm.sys` = NVIDIA graphics, `atikmdag.sys`/`amdkmdag.sys` = AMD graphics, `ntfs.sys` = storage/file system, `netio.sys`/`tcpip.sys` = network drivers or VPN software, `win32kfull.sys` = graphics/display subsystem.
3. No filename? Open **Event Viewer** (**Win + X** > **Event Viewer**) > **Windows Logs** > **System** and look for BugCheck entries around the crash time — they often name the faulting module.
4. You can also install the free BlueScreenView utility to read the minidump at `C:\Windows\Minidump` in plain English.

### Fix 2: Update the suspect driver from the manufacturer

Generic Windows drivers are the most common source of this crash on 24H2.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. If graphics is the suspect: for NVIDIA, download the latest driver from [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx); for AMD, use AMD's official driver download page; for Intel graphics, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. Do a **clean install** when the installer offers it — this wipes the old driver's remnants instead of layering over them. AMD users should grab theirs from AMD's official driver page rather than relying on Windows Update's version.
4. If a network driver is implicated, get the Wi-Fi/Ethernet driver from your laptop manufacturer's support site rather than Windows Update, since OEMs customize these.

The broader [SYSTEM_SERVICE_EXCEPTION fix guide](/articles/system-service-exception-windows-11-fix/) covers additional driver scenarios if the manufacturer's update doesn't resolve it.

### Fix 3: Remove or update antivirus and VPN software

Kernel-hooking security software is a top-3 cause of this stop code after build updates.

1. If you run third-party antivirus, update it to the latest version first — vendors patch kernel hooks for new Windows builds quickly.
2. If crashes continue, temporarily uninstall it (**Settings** > **Apps** > **Installed apps**) and let Windows Defender take over for a few days as a test.
3. Do the same for VPN clients, which install network filter drivers — update first, remove as a test second.
4. If the crashes stop, reinstall the latest version of the security software; the fresh install gets the 24H2-compatible drivers.

### Fix 4: Repair system files with SFC and DISM

Corrupted kernel services throw exceptions even when drivers are innocent.

1. Open **Terminal (Admin)** (**Win + X**).
2. Run `sfc /scannow` and wait for it to complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the source files `sfc` uses.
4. Restart. These two commands fix a surprising share of `SYSTEM_SERVICE_EXCEPTION` cases where no single driver is obviously at fault.

### Fix 5: Run Windows Memory Diagnostic

When the crash names different files each time, suspect RAM rather than any one driver.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. Let both passes finish. Any error means bad memory — and bad memory corrupts kernel data structures in ways that produce exactly this stop code.
3. For a definitive test, run MemTest86 overnight from a USB stick (4+ passes).

A related crash with a similar driver-first fix path is [SYSTEM_THREAD_EXCEPTION_NOT_HANDLED](/articles/how-to-fix-system-thread-exception-not-handled-in-windows-11-24h2/) — worth a look if your dumps point at thread-handling modules.

### Fix 6: Uninstall recently added driver-installing software

RGB controllers, fan utilities, virtual drives, and emulators all ship kernel drivers that can conflict.

1. Open **Settings** > **Apps** > **Installed apps**, sort by install date.
2. Uninstall anything installed around the time crashes began — especially hardware utilities, overclocking tools, and virtual-device software.
3. Check **Device Manager** > **View** > **Show hidden devices** afterward and remove any grayed-out remnants of the uninstalled software's devices.
4. Restart and observe for a few days.

### Fix 7: Roll back the 24H2 update as a last resort

If the crashes began the day 24H2 installed and nothing else helps, the build itself may be the problem on your hardware.

1. Go to **Settings** > **System** > **Recovery** > **Go back** (available for 10 days after the update).
2. If that window has passed, download fresh 24H2 media from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and do an in-place upgrade — it reinstalls Windows while keeping files and apps, replacing all system files with clean copies.
3. After the repair install, update drivers from the manufacturer before letting Windows Update run wild.

For crashes that specifically started right after a cumulative update rather than the 24H2 build itself, see the [post-update SYSTEM_SERVICE_EXCEPTION guide](/articles/how-to-fix-system-service-exception-after-windows-11-update/).

## Closing

`SYSTEM_SERVICE_EXCEPTION` on 24H2 is overwhelmingly a driver-compatibility problem, not a dying laptop. The filename on the blue screen usually points straight at the offender, and a manufacturer-supplied driver update ends the story in most cases. Work the list in order, give each change a day or two of normal use before judging it, and you'll almost always find the crashes gone by Fix 4 — with your files, apps, and sanity intact.
