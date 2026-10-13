---
title: "How to Fix Display Adapter Missing in Windows 11 24H2"
slug: "how-to-fix-display-adapter-missing-in-windows-11-24h2"
date: "2026-09-22"
categories: ["drivers"]
tags: ["display adapter missing", "gpu not detected", "windows 11 24h2", "graphics driver", "device manager"]
description: "Display adapter gone from Device Manager after Windows 11 24H2? Restore your GPU with driver reinstalls, BIOS checks, hidden-device scans, and hardware tests."
thumbnail: "/images/thumbs/how-to-fix-display-adapter-missing-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my display adapter disappear after updating to Windows 11 24H2?"
    a: "The 24H2 update migrates graphics drivers aggressively and can leave the GPU in a failed state: the driver fails to load, so Windows hides the adapter instead of showing an error. It can also disable the device during the upgrade or install an incompatible driver version. Reinstalling the graphics driver cleanly — removing the old one first — restores the adapter in nearly all 24H2-related cases."
  - q: "My screen still works but the display adapter is missing. How is that possible?"
    a: "Windows falls back to the Microsoft Basic Display Adapter, which drives the screen at low resolution without hardware acceleration. Device Manager may show only this basic adapter while your real GPU (Intel, AMD, or NVIDIA) is hidden or failed. The screen working does not mean the GPU is healthy — check Device Manager with hidden devices shown to see the real state of your graphics hardware."
  - q: "Can a BIOS setting hide the display adapter?"
    a: "Yes. Many laptops have BIOS options for graphics mode — integrated, discrete, or hybrid/switchable — and a wrong or reset setting can hide one GPU from Windows. After a 24H2 update, enter the BIOS and verify the graphics configuration: hybrid or switchable mode is the safest choice. Loading BIOS defaults also clears any stale configuration the update may have left behind."
  - q: "Is a missing display adapter ever a dead GPU?"
    a: "It can be, particularly on laptops where the discrete NVIDIA or AMD GPU stops appearing even after driver reinstalls, BIOS resets, and with hidden devices shown. But rule out software first: a GPU that is invisible in Windows but appears in the BIOS or a Linux live environment is a driver problem. Truly dead GPUs are rare and usually follow overheating events or physical damage."
---

Windows 11 version 24H2 has a known habit of making display adapters vanish: after the update, Device Manager shows no Intel, AMD, or NVIDIA GPU — sometimes only the Microsoft Basic Display Adapter, sometimes nothing at all under Display adapters. The screen usually still works (at ugly low resolution), brightness control dies, and external monitors stop being detected. This guide walks through restoring the adapter, from driver surgery to BIOS checks, in the order that finds the problem fastest.

First, establish what you are dealing with: open Device Manager, click View > Show hidden devices, and expand Display adapters. Note whether your GPU appears greyed out, appears with a warning, or is completely absent. That observation determines which fixes matter most.

## Why this happens

- **24H2 driver migration failure:** The update replaces the graphics driver and the new one fails to load, so Windows hides the adapter.
- **Incompatible driver installed by the update:** 24H2 may install a graphics driver version that does not match your GPU or laptop firmware.
- **Device disabled during upgrade:** The upgrade process can leave the GPU in a disabled state that persists afterward.
- **BIOS graphics mode reset:** Firmware updates bundled with 24H2 can reset hybrid-graphics settings, hiding the discrete GPU.
- **Corrupted driver store:** Partial driver migration leaves behind file fragments that block clean reinstallation.
- **Windows Update immediately re-breaking the fix:** The bad driver gets reinstalled automatically after you fix it manually.
- **Fast Startup preserving the failed state:** The hibernation snapshot locks in the broken GPU state across reboots.
- **Actual GPU hardware failure:** Rare, but 24H2's heavy driver churn can expose a GPU that was already marginal.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and check the real state

Get the full picture before changing anything.

1. Press Win + X, open Device Manager, and click View > Show hidden devices.
2. Expand Display adapters and note everything listed: your real GPU (possibly greyed out), Microsoft Basic Display Adapter, or nothing.
3. If your GPU is greyed out, right-click it and choose Enable device — then restart and recheck.
4. If it shows a yellow warning, double-click it and record the error code from the General tab.
5. If only Microsoft Basic Display Adapter appears, your GPU's driver has failed to load — proceed to the driver fixes.
6. This inventory tells you whether you are fighting a disabled device, a broken driver, or an invisible GPU.

### Fix 2: Restart the graphics driver

A stuck graphics stack sometimes just needs a kick.

1. Press Win + Ctrl + Shift + B — the screen will flash black briefly as the driver restarts.
2. Wait ten seconds, then reopen Device Manager and check whether the adapter reappeared.
3. If it appears but vanishes again after sleep or reboot, the driver still needs the clean reinstall below.
4. This shortcut is safe and does not close applications — use it freely as a diagnostic.

### Fix 3: Clean-reinstall the graphics driver with DDU

For 24H2 breakage, a normal reinstall often is not enough — purge the driver store properly.

1. Download Display Driver Uninstaller (DDU) and the latest graphics driver for your GPU and laptop model on another device if needed.
2. Boot into Safe Mode (Shift + Restart > Troubleshoot > Advanced options > Startup Settings).
3. Run DDU, select your GPU brand, and choose "Clean and restart" — this removes every trace of the old driver.
4. After rebooting into normal Windows, install the fresh driver package you downloaded.
5. Restart once more and verify the adapter appears correctly in Device Manager.
6. For NVIDIA GPUs, get the driver from [NVIDIA's official download page](https://www.nvidia.com/Download/index.aspx); for Intel/AMD, prefer your laptop maker's package.

### Fix 4: Install the laptop manufacturer's graphics driver

Laptop GPUs need the manufacturer's tuned driver more often than desktop cards do.

1. Find your exact model on the manufacturer's support site and download its graphics driver — even if the version looks older than the component maker's.
2. If DDU already cleaned the system, simply run the manufacturer's installer.
3. For switchable-graphics laptops (Intel + NVIDIA or AMD + AMD), install the integrated GPU driver first, then the discrete one.
4. Restart and confirm both adapters appear in Device Manager without warnings.
5. Test brightness control and external monitor detection — both depend on the GPU driver loading properly, as covered in our [brightness fix guide](/articles/how-to-fix-display-brightness-not-working-on-windows-11/).

### Fix 5: Check BIOS graphics settings

24H2-related firmware updates can reset the graphics mode and hide a GPU.

1. Restart into the BIOS setup (F2, F10, Del, or the manufacturer key).
2. Look for graphics, display, or video settings — options like Integrated, Discrete, Hybrid, or Switchable.
3. Set it to Hybrid or Switchable (not Discrete-only or Integrated-only) so Windows sees all GPUs.
4. Confirm the primary display device is set correctly for a laptop (usually the integrated GPU or Auto).
5. Save, exit, and check Device Manager after booting.
6. If the BIOS shows no graphics options, load setup defaults — this alone clears stale configurations.

### Fix 6: Disable Fast Startup and reset the GPU power state

Fast Startup can preserve the failed GPU state indefinitely across reboots.

1. Open Control Panel > Power Options > Choose what the power buttons do.
2. Click "Change settings that are currently unavailable" and uncheck "Turn on fast startup".
3. Shut down completely, unplug the laptop, and hold the power button for 15 seconds.
4. Power on fresh and check Device Manager — GPUs stuck in failed power states often reappear here.
5. Microsoft documents startup and recovery behavior on their [Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Block Windows Update from reinstalling the bad driver

The cruelest 24H2 loop: you fix the driver, and Windows Update breaks it again overnight.

1. After getting a working driver installed, open System Properties (Win + R > `sysdm.cpl`) > Hardware tab > Device Installation Settings.
2. Select "No" to stop automatic driver downloads.
3. For a stronger block, use Group Policy or the registry method in our [disable driver updates guide](/articles/how-to-disable-automatic-driver-updates-on-windows-11/).
4. Monitor Windows Update history for a few days to confirm no graphics driver sneaks back in.
5. Recheck these settings after each future Windows feature update, which can reset them.

### Fix 8: Test the GPU outside Windows

If the adapter remains invisible after all software steps, verify the hardware.

1. Enter the BIOS — many BIOS screens report detected graphics hardware.
2. Boot an Ubuntu live USB and check its system info or run `lspci | grep -i vga` in a terminal.
3. GPU visible in Linux but not Windows: a Windows-side problem — consider a repair install of Windows 11.
4. GPU invisible everywhere: the GPU or its connection has likely failed — contact the manufacturer for service.
5. Note that a missing discrete GPU also breaks [external monitor detection](/articles/how-to-fix-external-monitor-not-detected-on-hp-laptop/) on laptops where the HDMI port is wired to it.

## Closing

A missing display adapter in Windows 11 24H2 is almost always a driver-migration casualty, and the DDU clean reinstall in Fix 3 resolves the large majority of cases. The critical follow-up is Fix 7 — blocking Windows Update from reinstalling the offending driver — because without it, the problem returns like clockwork. Work the list in order, and only conclude hardware failure after the Linux test in Fix 8 says so.
