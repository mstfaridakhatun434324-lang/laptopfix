---
title: "VIDEO_TDR_FAILURE on ASUS Laptops: A Complete Fix Guide"
slug: how-to-fix-video-tdr-failure-on-asus-laptop
date: 2026-09-14
categories: ["windows-errors"]
tags: ["blue screen", "video tdr failure", "asus laptop", "gpu timeout", "nvlddmkm.sys"]
description: "VIDEO_TDR_FAILURE blue screening your ASUS laptop? Fix GPU timeout crashes in 8 steps — drivers, TDR settings, heat, and power."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-on-asus-laptop.webp"
faqs:
  - q: "What does VIDEO_TDR_FAILURE mean?"
    a: "TDR stands for Timeout Detection and Recovery. Windows gives the GPU 2 seconds to respond; if it doesn't, Windows tries to reset the graphics driver, and if that fails, you get this blue screen (0x116). It means the GPU stopped answering — usually due to a driver bug, overheating, or unstable clocks."
  - q: "Is VIDEO_TDR_FAILURE a dead GPU?"
    a: "Usually not. Most TDR failures are driver or heat issues. Suspect hardware only if clean driver installs, stock clocks, and good temperatures don't help — or if you see visual artifacts (checkerboards, colored lines) even in the BIOS screen, which points firmly at the GPU."
  - q: "Why does it happen on ASUS laptops specifically?"
    a: "ASUS gaming laptops (ROG, TUF) push GPUs hard with factory overclocks and aggressive power profiles via Armoury Crate. Those profiles can be marginally unstable, and ASUS-customized drivers sometimes lag behind. Resetting Armoury Crate to stock profiles fixes many cases."
  - q: "Can I just increase the TDR timeout?"
    a: "You can raise the TdrDelay registry value, and it sometimes masks the crash — but it treats the symptom. A GPU that regularly needs more than 2 seconds to respond has an underlying problem (driver, heat, or clocks) that you should fix instead of hiding."
---

VIDEO_TDR_FAILURE (0x116) is Windows' way of saying "the graphics card stopped talking to me." TDR — Timeout Detection and Recovery — is supposed to reset a hung GPU gracefully, but when the reset itself fails, you get the blue screen. On ASUS laptops, especially ROG and TUF gaming models, this usually traces back to GPU drivers, Armoury Crate's aggressive tuning, or heat.

The fix sequence goes from software to hardware, cheapest first.

## Why this happens

- **Buggy or corrupted GPU driver.** The driver hangs the GPU and can't recover it — the most common cause.
- **Overheating GPU.** Heat-induced errors make the GPU stop responding, especially in thin ASUS models with dust-clogged cooling.
- **Unstable factory overclock.** ASUS performance profiles push GPU clocks that aren't stable on every individual chip.
- **Insufficient power.** A failing charger or power-plan issue starves the GPU during load spikes.
- **Conflicting overlays and capture software.** Anything hooking the graphics pipeline can hang the driver.
- **Failing GPU hardware.** The last resort diagnosis — usually announced by visual artifacts.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Reset Armoury Crate to stock settings

ASUS's own tuning software is suspect number one on ASUS laptops.

1. Open **Armoury Crate** and go to the system configuration/performance section.
2. Switch from **Turbo** or **Manual** mode to **Performance** or **Silent** — avoid Manual overclocks for now.
3. If you set a manual GPU overclock, reset it to defaults.
4. Disable any "GPU overclock" or "memory overclock" toggles.
5. Restart and test the game or workload that crashed. Many TDR failures vanish right here.

### Fix 2: Clean-reinstall the GPU driver

Wipe the driver completely and start fresh.

1. Download the latest GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
2. Boot into Safe Mode and run Display Driver Uninstaller (DDU) to remove all traces of the old driver.
3. Restart normally and install the fresh driver with the **Clean installation** option ticked.
4. Try the Studio/stable driver branch instead of Game Ready if crashes persist — it's validated longer.
5. If the generic driver misbehaves on your specific model, check the ASUS official support site for your exact model's driver package instead.

### Fix 3: Check GPU temperatures and clean cooling

Heat hangs GPUs.

1. Install HWiNFO or HWMonitor and log GPU temperature during the crashing workload.
2. Sustained temperatures above 87–90°C on the GPU are a red flag.
3. Power off, then blow compressed air through the intake and exhaust vents in short bursts (hold the fans still with a toothpick to avoid overspinning).
4. Elevate the rear of the laptop or use a cooling pad — even 3–5°C helps stability.
5. On laptops more than two years old, consider a professional repaste of the GPU/CPU thermal compound.

### Fix 4: Verify power delivery

TDR failures love marginal power.

1. Game and stress-test only with the original ASUS charger plugged in — check its wattage matches what the laptop shipped with.
2. Inspect the charger cable and DC jack for damage or looseness.
3. In **Settings > System > Power & battery**, set power mode to **Best performance** while plugged in (counterintuitively, some "balanced" plans cause voltage swings).
4. Disable USB selective suspend and PCIe link-state power management in the advanced power plan settings while testing.
5. If crashes correlate with battery-only use or a swollen battery, replace the battery.

### Fix 5: Disable overlays and background graphics hooks

Remove software that hangs the graphics pipeline.

1. Disable the Discord overlay, GeForce Experience/AMD Software overlay, and Xbox Game Bar (**Settings > Gaming**).
2. Turn off screen recording and instant-replay features while testing.
3. Close MSI Afterburner, RivaTuner, and similar tools — they hook the driver directly.
4. Test the crashing workload clean.
5. Reintroduce tools one at a time afterward. For broader crash context, our [blue screen while gaming guide](/articles/how-to-fix-blue-screen-while-gaming-youtube/) covers the full load-related picture.

### Fix 6: Adjust the TDR timeout (carefully)

Give the GPU more time before Windows declares it dead — a diagnostic step, not a permanent fix.

1. Press **Windows + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a new **DWORD (32-bit) Value** named `TdrDelay` and set it to `10` (decimal — 10 seconds).
3. Optionally add `TdrDdiDelay` set to `20`.
4. Restart and test. If crashes stop, the GPU was *slow*, not dead — still investigate heat and drivers.
5. If crashes continue even with a 10-second timeout, the GPU is genuinely hanging; revert the values and continue below. Power-related GPU crashes are also covered in our [DRIVER_POWER_STATE_FAILURE guide](/articles/driver-power-state-failure-windows-11-fix/).

### Fix 7: Test with the integrated GPU and update firmware

Isolate whether the discrete GPU is the problem.

1. In **Armoury Crate** or **NVIDIA Control Panel**, force the crashing app to use the integrated GPU and test.
2. If the iGPU is stable, the discrete GPU or its driver path is confirmed as the fault zone.
3. Update the BIOS/UEFI from ASUS's support site — firmware updates fix GPU power-management bugs.
4. Also update the chipset drivers from ASUS or AMD/Intel as appropriate.
5. Run `sfc /scannow` in **Terminal (Admin)** to rule out system-file corruption.

### Fix 8: Evaluate the GPU hardware

When software is exhausted, face the hardware question.

1. Boot into BIOS/UEFI and look at the screen for several minutes — artifacts here mean hardware, since no Windows driver is loaded.
2. Run a FurMark stress test and watch for artifacts, checkerboarding, or colored lines.
3. If artifacts appear even at stock clocks and good temperatures, the GPU is failing.
4. On laptops with soldered GPUs, this means motherboard-level repair — get a quote from ASUS service or a board-repair shop.
5. Microsoft's [blue screen troubleshooting hub](https://support.microsoft.com/en-us/windows) documents the official recovery paths if you need them.

## Closing

VIDEO_TDR_FAILURE on ASUS laptops is a driver-and-tuning problem far more often than a dead GPU. Reset Armoury Crate, clean-install the driver, and check your temperatures — that trio resolves the overwhelming majority of cases. Only start worrying about hardware when clean software and cool temperatures still produce hangs, and even then, artifacts are the real tell.
