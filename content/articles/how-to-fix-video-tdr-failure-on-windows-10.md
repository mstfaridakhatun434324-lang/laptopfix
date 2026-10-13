---
title: "How to Fix VIDEO_TDR_FAILURE on Windows 10"
slug: how-to-fix-video-tdr-failure-on-windows-10
date: 2026-09-28
categories: ["windows-errors"]
tags: ["blue screen", "video_tdr_failure", "windows 10"]
description: "VIDEO_TDR_FAILURE means your graphics driver stopped responding on Windows 10. Clean-reinstall the GPU driver, check temperatures, and stabilize it."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-on-windows-10.webp"
faqs:
  - q: "What does VIDEO_TDR_FAILURE mean?"
    a: "TDR stands for Timeout Detection and Recovery. Windows watches the graphics driver, and if the GPU doesn't respond within a couple of seconds, Windows tries to reset the driver. When that reset fails, you get the VIDEO_TDR_FAILURE blue screen. It means the graphics driver hung badly enough that Windows couldn't recover it — usually a driver bug, an overheating GPU, or an unstable overclock."
  - q: "Why does the blue screen name a file like nvlddmkm.sys?"
    a: "That file is the NVIDIA graphics driver; AMD systems show atikmdag.sys instead, and Intel graphics show igdkmd64.sys. The named file tells you exactly which driver hung, which is genuinely useful — it confirms the problem is in the graphics stack rather than somewhere else. Focus your fixing on that specific GPU driver."
  - q: "Can I fix this without opening my laptop?"
    a: "Yes, most fixes are software: clean driver reinstalls, Windows updates, removing overclocks, and adjusting the TDR delay. Physical steps like cleaning vents with compressed air don't require opening anything. Only repasting or reseating components needs the case opened, and those are last resorts after software fixes fail."
  - q: "Is VIDEO_TDR_FAILURE a sign my GPU is dying?"
    a: "Not necessarily — it's a driver or stability issue far more often than dead hardware. But if you've clean-installed multiple driver versions, ruled out heat and overclocks, tested the RAM, and the crashes persist across a clean Windows install, then yes, the GPU itself becomes the prime suspect. Artifacting or crashes in the BIOS screen would confirm hardware trouble."
---

VIDEO_TDR_FAILURE is Windows telling you the graphics driver froze and couldn't be restarted. On Windows 10 this usually shows up during gaming, video editing, or even just watching video — anywhere the GPU is actually working.

The fix is almost always in the graphics driver: a clean reinstall, not just an update over the top. Let's do this properly.

## Why this happens

- **Corrupted graphics driver installation.** Leftover files from old driver versions conflict with the new one.
- **Buggy new driver release.** Sometimes the latest driver is simply broken for your card.
- **Overheating GPU.** Heat makes the GPU hang, which triggers the timeout detection.
- **Unstable GPU overclock.** Factory or manual overclocks that aren't fully stable.
- **Underpowered or failing PSU/charger.** The GPU browns out at peak draw and stops responding.
- **Conflicting software.** Overlays, recording tools, and "game boosters" hooking the graphics pipeline.
- **Corrupted Windows system files.** Damage to the components Windows uses to manage the driver reset.

## How to fix it

Work through these in order, from Fix 1 onward, and stop as soon as the crashes stop.

### Fix 1: Clean-reinstall the graphics driver with DDU

This is the fix that works most often. A normal update leaves old files behind; DDU removes everything.

1. Download the latest driver for your GPU from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) — save it, don't run it yet.
2. Download Display Driver Uninstaller (DDU).
3. Boot into Safe Mode: **Settings > Update & Security > Recovery > Advanced startup > Restart now**, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**.
4. Run DDU, select your GPU brand, and click **Clean and restart**.
5. After rebooting, install the driver you downloaded. Choose **Custom install** and check **Clean installation**.

### Fix 2: Try an older driver version

If the crashes started with a recent driver update, the new driver may be the problem, not the solution.

1. In **Device Manager**, expand **Display adapters**, right-click your GPU, and open **Properties**.
2. On the **Driver** tab, note the version and date.
3. Download a driver version from two or three months ago from the GPU maker's archive.
4. Use DDU in Safe Mode (Fix 1) to remove the current driver, then install the older one.
5. Pause driver updates in **Settings > Update & Security > Windows Update > Advanced options** so Windows doesn't "helpfully" upgrade you back.

### Fix 3: Fully update Windows 10

Microsoft ships TDR-related fixes and driver framework updates through Windows Update.

1. Open **Settings > Update & Security > Windows Update**.
2. Click **Check for updates** and install everything, including optional updates.
3. Restart even if it doesn't prompt you.
4. Check **View optional updates > Driver updates** too — install any graphics-related ones only if your manual install is older.
5. Test with the same workload that was crashing before.

### Fix 4: Remove GPU overclocks and check temperatures

An overclocked or overheating GPU hangs exactly the way TDR detects.

1. If you use MSI Afterburner or similar, reset to stock speeds and close the program.
2. Install HWMonitor and watch GPU temperatures during the workload that crashes.
3. Sustained temperatures above 85 to 90 degrees Celsius deserve action.
4. Clean the vents with compressed air and make sure the laptop sits on a hard surface.
5. On desktops, verify the GPU fans actually spin up under load — a dead fan causes exactly this.

### Fix 5: Increase the TDR delay

Giving Windows more patience before declaring the driver dead helps marginal cases, especially on slower GPUs.

1. Press **Win + R**, type `regedit`, and press Enter.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
3. Right-click in the right pane, choose **New > DWORD (32-bit) Value**, and name it `TdrDelay`.
4. Double-click it, set the value to `8` (seconds, up from the default 2), and click **OK**.
5. Restart. This doesn't fix the underlying hang, but it stops borderline cases from blue screening — combine it with the driver fixes above.

### Fix 6: Disable overlays and conflicting software

Overlays hook the graphics pipeline and are a notorious TDR trigger.

1. Turn off the Discord overlay: **Discord > Settings > Game Overlay > Enable in-game overlay** off.
2. Disable GeForce Experience or AMD Adrenalin overlays temporarily.
3. Close "game booster" utilities, screen recorders, and RGB software that hooks into games.
4. Test the crashing workload clean.
5. Re-enable them one at a time afterward to identify the offender.

### Fix 7: Repair system files and test RAM

Rule out the supporting cast — corrupted Windows files and bad memory both cause TDR crashes.

1. Open an elevated Command Prompt (**Win + X > Command Prompt (Admin)** or Windows PowerShell (Admin)).
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Test RAM with `mdsched.exe` — choose **Restart now and check for problems**.
4. Restart and confirm SFC's second pass is clean.
5. If memory errors appear, replace the faulty stick — bad RAM corrupts GPU driver data in transit.

### Fix 8: Test the GPU hardware itself

When software fixes all fail, verify the card.

1. On a desktop, reseat the GPU in its PCIe slot and check both power connectors are firmly plugged in.
2. Try the GPU in a different PCIe slot if one is available.
3. Test with a different power supply or charger — weak power causes TDR failures under load.
4. If crashes happen even in the BIOS screen or during Windows installation, the GPU hardware is failing.
5. On a laptop with a discrete GPU that keeps failing after a clean Windows install, it's a service-center repair — check your warranty first.

## Closing

VIDEO_TDR_FAILURE is a driver problem until proven otherwise, and a proper DDU clean install proves it one way or the other in most cases. Work the list top to bottom, and resist the urge to blame the hardware before the software fixes are exhausted. If you're on Windows 11 instead, the same logic applies — see our [Windows 11 VIDEO_TDR_FAILURE guide](/articles/how-to-fix-video-tdr-failure-on-windows-11/) — and for crashes that only happen in games, the [gaming blue screen fixes](/articles/how-to-fix-blue-screen-while-gaming-reddit/) go deeper on load-related causes.
