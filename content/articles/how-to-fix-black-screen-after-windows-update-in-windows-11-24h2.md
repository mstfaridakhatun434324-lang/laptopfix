---
title: "Fix a Black Screen After a Windows Update in Windows 11 24H2"
slug: how-to-fix-black-screen-after-windows-update-in-windows-11-24h2
date: 2026-09-05
categories: ["windows-errors"]
tags: ["black screen", "windows 11 24h2", "display driver", "windows update"]
description: "Black screen after updating to Windows 11 24H2? Get your display back with safe-mode driver fixes and update rollbacks."
thumbnail: "/images/thumbs/how-to-fix-black-screen-after-windows-update-in-windows-11-24h2.webp"
faqs:
  - q: "Why does the screen go black after the 24H2 update?"
    a: "The update usually replaces your graphics driver with a version that fails on your hardware, or the display driver crashes during the first boot into the new build. The system is actually running — you just can't see it. That's why remote and safe-mode fixes work."
  - q: "How do I know if it's a driver issue or a dead screen?"
    a: "If you hear the Windows login sound, the caps-lock light toggles, or an external monitor shows a picture, the panel and GPU are fine and it's a driver or display-configuration issue. Total silence with no lights suggests a deeper boot failure instead."
  - q: "Will I lose files fixing a black screen?"
    a: "No. Every fix here — safe-mode driver rollback, update uninstall, startup repair — preserves your files. A black screen is a display problem, not a data problem; your files are sitting untouched on the drive."
  - q: "The black screen has a cursor. Is that different?"
    a: "Yes, and it's good news: a visible cursor means Windows loaded and the GPU works — usually Explorer failed to start or the display driver partially loaded. The fixes below still apply, but start with the Explorer restart in Fix 2."
---
A black screen after the Windows 11 24H2 update is uniquely stressful: the laptop is clearly on — fans spin, lights glow — but there's nothing to look at. In the vast majority of cases, the machine booted fine and the display pipeline broke: the update installed a graphics driver that crashes on your hardware, or the display configuration got mangled in the upgrade. Your files are fine. The fix is getting a working picture back, then repairing the driver situation that caused it.

This guide starts with the quick checks that distinguish a driver problem from a hardware problem, then walks through the repairs in order. You don't need a second computer, but a phone flashlight and patience help.

## Why this happens

- **The update replaced your graphics driver.** 24H2 bundles driver updates; the new Intel, NVIDIA, or AMD driver crashes or fails to initialize on some hardware.
- **Display driver conflict during first boot.** Old driver remnants plus the new driver load together and the display stack collapses.
- **Wrong refresh rate or resolution pushed.** The update resets display settings to values your panel or external monitor can't show.
- **Fast Startup hibernation corruption.** The hibernation file from the old build doesn't resume cleanly on the new one, hanging the display.
- **Explorer failing to start.** Windows boots but the shell never launches — black screen with cursor.
- **BitLocker or firmware hiccups.** Rare, but TPM/firmware state changes during the update can stall the boot before the display initializes.

## How to fix it

Work through these in order. Fix 1 tells you what you're dealing with; the rest fix it.

### Fix 1: Determine whether Windows is actually running

Thirty seconds of checks that aim everything after.

1. Press **Caps Lock** — if the keyboard light toggles, Windows is alive and it's a display/driver issue.
2. Press **Win + Ctrl + Shift + B** — this restarts the graphics driver with an audible beep. If the picture returns, it was a transient driver crash.
3. Connect an **external monitor** via HDMI/USB-C. Picture on the external display means your panel config or internal display driver is at fault, not the GPU.
4. Listen for the Windows login sound after a minute. Sound plus black screen confirms a running system with a dead display path. If none of these respond, skip to Fix 7 — you have a boot problem, not a display problem. The general [black screen after update guide](/articles/windows-11-black-screen-after-update-fix/) covers the no-response variants in depth.

### Fix 2: Wake Explorer if you have a cursor

Black screen with a visible cursor is often just a dead shell.

1. Press **Ctrl + Shift + Esc**. If Task Manager appears, you're in good shape.
2. Click **Run new task**, type `explorer.exe`, and press Enter. The desktop should appear.
3. If Explorer immediately dies again, the shell is crashing — continue to Fix 3 for the driver repair, since shell crashes post-update are usually display-driver-related.

### Fix 3: Boot to Safe Mode and roll back the graphics driver

Safe Mode uses the basic display driver, which almost always gives you a picture.

1. Force WinRE: power off at the logo three times, then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > **4** (Safe Mode).
2. Open **Device Manager** (`devmgmt.msc`), expand **Display adapters**, right-click your GPU > **Properties** > **Driver** tab > **Roll Back Driver**.
3. If rollback is unavailable, **Uninstall device** (tick **Attempt to remove the driver for this device**) and reboot — Windows falls back to the Microsoft Basic Display Adapter, which will at least show a picture.
4. Once you have a stable picture, install the correct driver from your laptop maker's site or the GPU vendor: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html).

### Fix 4: Uninstall the 24H2 update from WinRE

When the driver situation is a mess, remove the update that caused it.

1. In WinRE, go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall the latest feature update** (24H2 qualifies as a feature update).
3. Let it complete and reboot. You should land back on your previous build with a working display.
4. Pause updates for a few weeks (**Settings** > **Windows Update** > **Pause updates**) while the graphics vendor ships a fixed driver.

### Fix 5: Disable Fast Startup and clear the hibernation state

Corrupted hybrid-boot state is a classic black-screen cause.

1. Once you have a picture (Safe Mode is fine), open **Control Panel** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. In **Terminal (Admin)**, run `powercfg /h off` to delete the hibernation file entirely, then `powercfg /h on` to recreate it cleanly if you use hibernation.
4. Shut down fully (not restart) and power back on. Cold boots bypass the corrupted resume path.

### Fix 6: Run Startup Repair and system file checks

If the update damaged boot or system files, repair them.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Startup Repair**. Let it run — it fixes common boot file damage automatically.
2. Then open **Command Prompt** from Advanced options and run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter if WinRE mounts Windows elsewhere — check with `diskpart` > `list volume`).
3. Reboot and test. Microsoft's support site documents the WinRE recovery options if you need the official reference.

### Fix 7: System Restore to before the update

When nothing else gives you a picture, roll the whole system back.

1. In WinRE: **Troubleshoot** > **Advanced options** > **System Restore**.
2. Pick a restore point dated before the 24H2 update and let it complete.
3. This is non-destructive to personal files — it reverses system, driver, and registry changes only.
4. After restore, immediately pause updates and update the graphics driver manually before letting 24H2 try again. Our [system restore guide](/articles/how-to-use-system-restore-on-windows-11/) covers creating restore points so you're protected next time.

## Closing

A black screen after the 24H2 update is alarming but rarely serious: the system is up, the display driver isn't. The Caps Lock test and an external monitor tell you that in under a minute, Safe Mode gives you a working picture, and from there it's a driver rollback or update uninstall away from normal. The key discipline is fixing the graphics driver properly before letting the update reinstall — otherwise you'll be staring at the same black screen next Patch Tuesday.
