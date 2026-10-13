---
title: "Win32kfull.sys BSOD After a Windows 11 Update: How to Fix It"
slug: how-to-fix-win32kfull-sys-bsod-after-windows-11-update
date: 2026-10-07
categories: ["windows-errors"]
tags: ["bsod", "stop code", "windows update", "graphics"]
description: "Blue screen naming win32kfull.sys after a Windows 11 update? It's the graphics subsystem crashing. Here's the fix, step by step."
thumbnail: "/images/thumbs/how-to-fix-win32kfull-sys-bsod-after-windows-11-update.webp"
faqs:
  - q: "What is win32kfull.sys?"
    a: "It's a core Windows system file that handles the graphical subsystem — window management, graphics rendering calls, and user interface drawing. When a blue screen names it, the crash happened inside Windows' graphics handling, usually triggered by a faulty graphics driver."
  - q: "Why did this start after a Windows update?"
    a: "Updates replace graphics drivers with new versions — sometimes generic Microsoft ones that don't play well with your specific GPU or laptop. The update can also change graphics subsystem behavior that an older driver wasn't written for."
  - q: "Is win32kfull.sys a virus?"
    a: "No. It's a legitimate, critical Windows system file in C:\\Windows\\System32. Malware sometimes uses similar names, but a blue screen naming the real win32kfull.sys is a driver or system-file problem, not an infection."
  - q: "Can I just delete or replace win32kfull.sys?"
    a: "Never delete it — Windows won't boot without it. If the file itself is corrupt, SFC and DISM repair it safely from clean sources. Manual replacement from the internet risks introducing mismatched or malicious files."
---

When the blue screen names `win32kfull.sys`, Windows is telling you the crash happened in its graphics subsystem — the part of the kernel that draws windows, handles display calls, and talks to your GPU driver. And when that crash starts right after a Windows 11 update, the story is almost always the same: the update changed something in the graphics stack, and the driver (or the file itself) didn't survive the transition intact.

The fix targets the graphics pipeline specifically: get the right driver back in place, repair the system file if it's damaged, and undo the update if it's the trigger.

## Why this happens

- **The update replaced your GPU driver with a problematic version**: Windows Update's driver versions lag behind — or differ from — manufacturer releases, and the mismatch crashes the graphics subsystem.
- **Old GPU driver incompatible with updated system files**: The update refreshed `win32kfull.sys` itself; a driver written against the old version can now crash against the new one.
- **Corrupted win32kfull.sys from an interrupted update**: If the update was interrupted, the file can be left partially written — and it's loaded on every boot.
- **Conflicting display software**: Screen recorders, overlays, color-calibration tools, and remote-desktop apps hook the graphics subsystem; an update can break those hooks.
- **Corrupt font or theme caches**: Less common, but damaged font caches have been known to crash the window manager in ways that blame `win32kfull.sys`.
- **Failing GPU or VRAM**: If the crashes happen during graphically intense moments rather than correlating with the update, hardware enters the picture.

## How to fix it

Work through these in order — graphics driver first, since that's the cause 90% of the time.

### Fix 1: Clean-install the correct GPU driver

The update's driver is the prime suspect. Replace it completely.

1. Identify your GPU: **Device Manager** (**Win + X**) > **Display adapters**.
2. Download the proper driver: [NVIDIA](https://www.nvidia.com/Download/index.aspx) (choose **Custom** > **Clean install**), AMD via its official driver support page (factory reset option), or Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. For a truly clean slate, use DDU (Display Driver Uninstaller) in Safe Mode first — it removes every trace of the old driver, including the one the update installed.
4. Install the fresh driver, restart, and test for a few days. If crashes began with the update and end with this driver, case closed.

### Fix 2: Repair win32kfull.sys with SFC and DISM

If the system file itself was damaged by the update, repair it from clean sources.

1. Open **Terminal (Admin)** (**Win + X**).
2. Run `sfc /scannow` — this specifically checks and replaces corrupted protected files including `win32kfull.sys`.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to fix the repair source.
4. Restart. If `sfc` reported fixing files, test stability before doing anything else.

### Fix 3: Uninstall the update that triggered it

When the timeline is unambiguous, undo the trigger.

1. Go to **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Remove the update installed just before the crashes began.
3. Restart and observe for several days.
4. If the system is stable, the update was the trigger — but don't just block updates forever. Reinstall it later after updating your GPU driver first (Fix 1), which often resolves the underlying incompatibility.

The general [blue screen after Windows 11 update guide for Lenovo](/articles/how-to-fix-blue-screen-after-windows-11-update-on-lenovo-laptop/) covers the broader post-update crash landscape.

### Fix 4: Disable or update display-hooking software

Overlays and recorders hook exactly the subsystem that's crashing.

1. Temporarily disable: Discord overlay, GeForce Experience/AMD Software overlay, Steam overlay, Xbox Game Bar (**Settings** > **Gaming** > **Xbox Game Bar** > Off), screen recorders, and color-calibration loaders.
2. Update any you actually need to their latest versions — vendors patch update incompatibilities quickly.
3. Re-enable one at a time over several days. If crashes return with one specific app, you've found a contributing factor.

### Fix 5: Clear font and thumbnail caches

Corrupt caches occasionally crash the window manager.

1. Press **Win + R**, type `services.msc`, stop the **Windows Font Cache Service**.
2. Delete the contents of `C:\Windows\ServiceProfiles\LocalService\AppData\Local\FontCache` (show hidden files first).
3. Run **Disk Cleanup** (**Win + S** > `cleanmgr`), check **Thumbnails**, and clean them.
4. Restart — Windows rebuilds both caches fresh.

### Fix 6: Test the GPU hardware

If crashes correlate with graphical load rather than the update timeline, test the hardware.

1. Run a GPU stress test (FurMark or 3DMark) for 20 minutes while monitoring temperatures with HWMonitor.
2. Artifacts, driver crashes, or blue screens under load point at the GPU or its VRAM.
3. Also run `mdsched.exe` (**Win + R**) memory diagnostic — system RAM errors can corrupt graphics operations.
4. On laptops with switchable graphics, try forcing the integrated GPU for a day (in NVIDIA Control Panel or AMD Software: prefer integrated graphics) — if crashes stop, the discrete GPU is suspect.

Related driver-verification crashes are covered in the [Driver Verifier detected violation guide](/articles/how-to-fix-driver-verifier-detected-violation-on-windows-11/).

### Fix 7: In-place repair install

When the graphics stack is too tangled for targeted fixes, reinstall Windows over itself.

1. Download Windows 11 media from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run setup from within Windows and choose **Keep personal files and apps**.
3. This reinstalls every system file — including `win32kfull.sys` — with clean copies while preserving your data.
4. After the repair install, install your GPU driver from the manufacturer *before* running Windows Update, so the update doesn't reinstall its problematic version first.

## Closing

A blue screen naming `win32kfull.sys` after an update is the graphics subsystem telling you the update broke its contract with your GPU driver. The fix is correspondingly focused: get the manufacturer's clean driver in place, repair the system file, and the crash goes away. It's one of the more precisely-diagnosed blue screens you'll encounter — the filename does half the troubleshooting for you.
