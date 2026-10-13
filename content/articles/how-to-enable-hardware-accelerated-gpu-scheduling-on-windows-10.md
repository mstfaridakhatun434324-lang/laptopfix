---
title: "How to Enable Hardware-Accelerated GPU Scheduling on Windows 10"
slug: how-to-enable-hardware-accelerated-gpu-scheduling-on-windows-10
date: 2026-09-22
categories: ["performance"]
tags: ["gpu scheduling", "hags", "windows 10 graphics", "gaming performance"]
description: "Turn on Hardware-Accelerated GPU Scheduling in Windows 10 (2004+) for lower latency and smoother gaming — steps, requirements, and fixes."
thumbnail: "/images/thumbs/how-to-enable-hardware-accelerated-gpu-scheduling-on-windows-10.webp"
faqs:
  - q: "Does Windows 10 support Hardware-Accelerated GPU Scheduling?"
    a: "Yes, but only on version 2004 (May 2020 update) and later. HAGS was introduced with that release alongside the WDDM 2.7 driver model. If you're on an older Windows 10 build — 1909 or earlier — the option doesn't exist at all. Check your version with Win + R > winver; if you're behind, update through Settings > Update & Security > Windows Update before trying anything else."
  - q: "Is HAGS as good on Windows 10 as on Windows 11?"
    a: "Functionally it's the same feature, but Windows 11's implementation is more mature — its WDDM 3.x driver model handles hardware scheduling more robustly, and driver support is broader. On Windows 10 you can still see the same 1–5% FPS gains and smoother frame pacing, but you're slightly more likely to hit driver quirks. Keeping drivers current matters even more on Windows 10."
  - q: "Why don't I see the GPU scheduling option in Windows 10 settings?"
    a: "Three usual reasons: your Windows 10 build is older than 2004, your GPU predates hardware-scheduler support (older than NVIDIA GTX 10-series or AMD RX 5600/5700), or your graphics driver is too old to report WDDM 2.7. Update Windows first, then the GPU driver from NVIDIA, AMD, or Intel. If all three are current and the toggle is still missing, your GPU simply lacks the hardware."
  - q: "Can enabling HAGS cause problems on Windows 10?"
    a: "Occasionally. The earliest HAGS-capable drivers had bugs causing stutter or crashes in specific games, and Windows 10 gets fewer driver refinements now that development focus is on Windows 11. If you enable it and a particular game misbehaves, turn it back off and retest — per-game issues were the most common complaint. The toggle is fully reversible, so there's no risk in trying."
---

Windows 10 users sometimes assume Hardware-Accelerated GPU Scheduling is a Windows 11 exclusive — it isn't. Microsoft shipped it in the May 2020 Update (version 2004), and it works the same way: instead of the CPU managing GPU memory scheduling, the graphics card's own scheduler takes over, cutting latency and smoothing out frame delivery. The gains are modest but free — typically a few percent better frame rates and noticeably steadier frame pacing.

The Windows 10 path differs slightly from Windows 11's: the Settings location is different, the version requirement is strict (2004+), and driver maturity lags behind. This guide covers the Windows 10-specific steps, requirements, and the quirks to watch for. For the Windows 11 version of this guide, the process is nearly identical but lives under a different Settings path; for wider gaming tune-ups, see [fixing game stuttering after a Windows update](/articles/how-to-fix-game-stuttering-after-windows-update-on-dell-laptop/).

## Why this happens

- **Default scheduling routes through the CPU**: Every GPU memory decision waits on the CPU, adding latency to each frame.
- **CPU bottlenecks starve the GPU**: When the processor is saturated, GPU scheduling queues up — the micro-stutter HAGS removes.
- **WDDM 2.7 enabled the hardware path**: The May 2020 Update's driver model is what makes GPU-side scheduling possible at all.
- **Draw-call-heavy games pay the most tax**: Open-world and strategy titles issuing thousands of draw calls benefit most.
- **Older drivers can't expose the toggle**: The option only appears when the driver reports WDDM 2.7 or newer.
- **Windows 10 driver development has slowed**: Vendors prioritize Windows 11, so HAGS-related fixes land on 10 later or not at all.
- **Background CPU load amplifies the benefit**: Streaming, Discord, and browser tabs competing for CPU make hardware scheduling more valuable.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify Windows 10 version 2004 or later

The hard requirement everything else depends on.

1. Press Win + R, type `winver`, and press Enter — check the version number.
2. You need **version 2004** (OS build 19041) or newer. Anything older (1909, 1903…) has no HAGS support whatsoever.
3. If you're behind, go to **Settings** > **Update & Security** > **Windows Update** > **Check for updates** and install everything offered.
4. If Windows Update doesn't offer a newer build, use Microsoft's Update Assistant — search Microsoft Support for "Windows 10 Update Assistant" to get the official tool.
5. Re-run `winver` after updating to confirm you're on 2004+ before continuing.

### Fix 2: Confirm GPU compatibility

No hardware scheduler, no feature.

1. Press Win + R, type `dxdiag`, open the **Display** tab, and note the GPU model and **Driver Model** (must read WDDM 2.7+).
2. NVIDIA: GTX 10-series (Pascal) or newer. AMD: RX 5600/5700-series or newer. Intel: 11th-gen Core iGPU or newer, or Arc.
3. Laptop check: many Windows 10 laptops run older iGPUs — if the Intel integrated graphics predates 11th-gen, the toggle won't appear even with a supported discrete GPU in some hybrid configurations.
4. If the GPU is too old, HAGS is impossible — focus instead on driver updates and background-load reduction for gaming smoothness.
5. If the GPU qualifies, move on — the missing toggle is a software problem.

### Fix 3: Update the graphics driver to a WDDM 2.7+ driver

The fix for most missing toggles.

1. Get the latest driver for your card: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html).
2. Choose **clean installation** (NVIDIA custom install) or the factory-reset option (AMD) to clear old driver remnants.
3. Restart, then re-check `dxdiag` — **Driver Model** should now read WDDM 2.7 or higher.
4. On laptops, if the vendor driver breaks things, fall back to the manufacturer's driver (Dell, HP, Lenovo support pages) — but vendor-first usually has the newer WDDM.
5. Recheck the Settings toggle location in Fix 4 after the driver update.

### Fix 4: Enable it in Windows 10 Settings

The Windows 10-specific path.

1. Open **Settings** > **System** > **Display**.
2. Scroll down and click **Graphics settings** (the link beneath the Multiple displays section — this is the Windows 10 location; Windows 11 moved it).
3. Toggle on **Hardware-accelerated GPU scheduling**.
4. Restart your PC — mandatory; the setting does nothing until reboot.
5. Return to the same page after rebooting to confirm the toggle held (on some driver versions it silently reverts — if so, update the driver again).

### Fix 5: Force it via Registry if the toggle is missing

When hardware qualifies but Settings won't show the switch.

1. Press Win + R, type `regedit`, navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Set the **HwSchMode** DWORD to `2` (create it as a 32-bit DWORD if absent). Back up the key first via right-click > Export.
3. Restart the PC.
4. Verify with a tool like GPU-Z or by observing the Settings toggle state.
5. If you get crashes or worse stuttering, set it back to `1` and reboot — early Windows 10 HAGS drivers were buggier than current ones.

### Fix 6: Test per-game and roll back selectively

Windows 10's older driver stack means more per-game quirks.

1. Test HAGS with your most-played games individually, using built-in benchmarks or an FPS overlay, watching 1% lows and frame-time consistency.
2. If one specific game stutters or crashes with HAGS on while others are fine, that's a known pattern — disable HAGS for now rather than fighting the game.
3. Check the game's forums: some titles received patches addressing HAGS conflicts, so a game update may resolve it.
4. Keep a note of which driver version you tested with; re-test after each driver update since behavior changes.
5. Consider whether upgrading to Windows 11 is worthwhile — its more mature HAGS implementation and ongoing driver focus make it the better platform for this feature long-term. For broader gaming smoothness on either OS, see [how to speed up a Windows 11 laptop](/articles/how-to-speed-up-windows-11-laptop/).

## Closing

On Windows 10, Hardware-Accelerated GPU Scheduling is absolutely available — you just need version 2004+, a supported GPU, and a WDDM 2.7+ driver, toggled via Settings > System > Display > Graphics settings. Expect the same modest latency and smoothness gains as Windows 11, with a slightly higher chance of per-game quirks on the older driver stack. Verify with real games, and don't hesitate to roll back if a specific title objects.
