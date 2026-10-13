---
title: "How to Fix VIDEO_TDR_FAILURE on a Lenovo Laptop"
slug: how-to-fix-video-tdr-failure-on-lenovo-laptop
date: 2026-09-15
categories: ["windows-errors"]
tags: ["video tdr failure", "blue screen", "graphics driver", "Lenovo", "nvlddmkm.sys"]
description: "VIDEO_TDR_FAILURE on your Lenovo laptop? It's the graphics driver timing out. Clean-install the GPU driver, fix TDR settings, stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-on-lenovo-laptop.webp"
faqs:
  - q: "What does VIDEO_TDR_FAILURE mean?"
    a: "TDR stands for Timeout, Detection, and Recovery. Windows noticed the graphics driver stopped responding, tried to reset it, and the recovery failed — so it blue-screened. The screen often names the driver file, like nvlddmkm.sys (NVIDIA), igdkmd64.sys (Intel), or atikmdag.sys (AMD)."
  - q: "Why does VIDEO_TDR_FAILURE happen on Lenovo laptops?"
    a: "Lenovo laptops with dual graphics (Intel + NVIDIA/AMD) are prone to driver conflicts between the two GPUs, and Lenovo's power management (Vantage/battery modes) can starve the GPU during transitions. Outdated or Windows-Update-installed graphics drivers are the usual trigger."
  - q: "Is VIDEO_TDR_FAILURE a dying GPU?"
    a: "Usually not — it's a driver or power issue in the large majority of cases. Suspect hardware only if it happens across multiple clean driver versions, in Safe Mode–like conditions, or alongside visual artifacts (glitchy graphics even without crashing)."
  - q: "Which driver file names point to which GPU?"
    a: "nvlddmkm.sys = NVIDIA, igdkmd64.sys / igdkmd64.sys variants = Intel, atikmdag.sys / amdkmdag.sys = AMD. The filename on the blue screen tells you exactly which GPU's driver to clean-install."
---

**VIDEO_TDR_FAILURE** is Windows' graphics watchdog giving up. Normally, when the GPU driver hangs, Windows resets it silently (that's the brief screen flicker you sometimes see). TDR failure means the reset itself failed, so Windows blue-screens instead. On Lenovo laptops — especially ThinkPads, Ideapads, and Legions with dual graphics — this is a well-trodden path with known fixes.

The blue screen usually names the driver file, which tells you which GPU is unhappy. Match your fix to that file. For the Windows 11 24H2–specific variant, see [VIDEO_TDR_FAILURE in 24H2](/articles/how-to-fix-video-tdr-failure-in-windows-11-24h2/).

## Why this happens

- **Corrupted or mismatched graphics driver:** The top cause — bad install, Windows Update driver conflicting with Lenovo's version.
- **Dual-GPU switching conflicts:** Intel iGPU + NVIDIA/AMD dGPU handoff bugs, especially on battery or during display switching.
- **GPU power starvation:** Lenovo power plans or battery-saver modes cutting GPU power mid-operation.
- **Overheating GPU:** Thermal throttling escalating into driver timeouts under gaming/rendering loads.
- **Overclocked GPU:** Factory or user overclocks (Legion models) pushing past stability.
- **Failing GPU hardware:** Rare, but possible — usually accompanied by visual artifacts.

## How to fix it

Work through these in order.

### Fix 1: Note the driver filename, then clean-install that GPU's driver

The filename on the BSOD is your roadmap. Don't skip the DDU step — TDR failures are often caused by conflicting remnants of old driver versions, and only a true clean install removes them. An update-over install preserves exactly the conflicts you're trying to eliminate.

1. Note the `.sys` file: **nvlddmkm.sys** → NVIDIA, **igdkmd64.sys** → Intel, **atikmdag.sys/amdkmdag.sys** → AMD.
2. Download **DDU (Display Driver Uninstaller)** and the correct driver: for Lenovo laptops, start with the graphics driver from [Lenovo Support](https://support.lenovo.com/us/en/) for your exact model (it's validated for your dual-GPU setup).
3. Boot into **Safe Mode** (Shift + Restart > **Troubleshoot > Advanced options > Startup Settings**).
4. Run DDU, choose **Clean and restart**.
5. Install the Lenovo-provided driver. Only try the GPU vendor's latest (NVIDIA/AMD/Intel direct) if Lenovo's version still crashes.

### Fix 2: Fix Lenovo Vantage power and graphics settings

Lenovo's own software is a frequent contributor.

1. Open **Lenovo Vantage** and check **Device > Power** — if you're on an aggressive battery-saver profile while gaming or doing GPU work, switch to **Best Performance** (plugged in).
2. In Vantage's **GPU settings** (Legion/Ideapad Gaming), try switching between **Hybrid** and **Discrete GPU only** modes — whichever you're on, test the other.
3. Disable **Panel Self-Refresh** and aggressive display power-saving in **Intel Graphics Command Center** if present.
4. Update **Lenovo Vantage** itself and the **Lenovo System Update** drivers.

### Fix 3: Adjust the TDR timeout in the registry

If the GPU just needs more time (common with heavy workloads), give it more time. The default 2-second timeout is aggressive for complex scenes or compute workloads; 10 seconds lets legitimate work complete without Windows panicking. This is a safe, reversible tweak.

1. Press **Win + R**, type `regedit`, press Enter (back up the registry first: **File > Export**).
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
3. Create a new **DWORD (32-bit) Value** named `TdrDelay`, set its value to `10` (decimal) — this gives the GPU 10 seconds instead of the default 2 before Windows declares a timeout.
4. Optionally add `TdrDdiDelay` with value `20` as well.
5. Restart and test. If crashes stop, the GPU was just slow, not broken.

### Fix 4: Disable GPU overclocking and check thermals

1. Reset any overclocks in **Lenovo Legion Toolkit**, **MSI Afterburner**, or Vantage performance modes — return to stock clocks.
2. Monitor GPU temperature with **HWiNFO64** under load. Sustained temps near 90°C+ on the GPU plus TDR crashes = cooling problem.
3. Clean vents and fans with compressed air; elevate the rear of the laptop for airflow.
4. On older machines, dried thermal paste may need professional replacement.

### Fix 5: Update the Intel iGPU driver too

On dual-GPU Lenovos, the Intel driver matters as much as the discrete one.

1. In **Device Manager > Display adapters**, you'll see both GPUs.
2. Update the **Intel UHD/Iris Xe** driver from [Lenovo Support](https://support.lenovo.com/us/en/) (or Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)).
3. Mismatched Intel + NVIDIA driver generations cause handoff crashes — keep both current and from the same era.

### Fix 6: Test with the discrete GPU disabled

Isolate which GPU is at fault.

1. In **Device Manager > Display adapters**, right-click the discrete GPU (NVIDIA/AMD) and choose **Disable device**.
2. Use the laptop on Intel graphics for a day. No crashes → the dGPU driver (or dGPU) is the problem.
3. Re-enable and focus your driver efforts there. If crashes happen on Intel graphics alone too, it's likely the Intel driver or a system-level issue — run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth`.

### Fix 7: Check Windows Update for the real culprit

1. **Settings > Windows Update > Update history** — if a graphics driver update coincides with the crashes, roll it back in **Device Manager** (**Properties > Driver > Roll Back Driver**).
2. Consider pausing driver updates via Windows Update: **System > About > Advanced system settings > Hardware tab > Device Installation Settings > No** — then manage GPU drivers manually.
3. Install pending cumulative updates too — Microsoft ships TDR-related fixes. If the TDR failures began after a Windows update, see [fix VIDEO_TDR_FAILURE after Windows 11 update](/articles/fix-video-tdr-failure-after-windows-11-update/).

### Fix 8: Hardware verification as the last step

If multiple clean driver versions all crash identically:

1. Run **Lenovo Diagnostics** (boot menu or Vantage > Device > Diagnostics) — full GPU test.
2. Look for visual artifacts (checkerboards, lines, color corruption) outside of crashes — those indicate GPU hardware failure.
3. Artifacts + failed diagnostics = warranty claim or repair shop. No driver will fix a dying GPU.

## Closing

VIDEO_TDR_FAILURE on Lenovo laptops is a driver-and-power problem far more often than a hardware problem: clean-install the right GPU driver (Lenovo's version first), sort out Vantage's power/GPU modes, and consider the TdrDelay tweak for slow-but-healthy GPUs. The driver filename on the blue screen tells you which GPU to focus on — use it. Only when clean drivers, stock clocks, and good thermals all fail should the GPU hardware itself become the suspect.
