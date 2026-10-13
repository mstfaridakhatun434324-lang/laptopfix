---
title: "Display Driver Stopped Responding? The Definitive Fix"
slug: best-way-to-fix-display-driver-stopped-responding
date: 2026-09-22
categories: ["drivers"]
tags: ["display driver", "gpu", "tDR", "crash", "troubleshooting"]
description: "\"Display driver stopped responding and has recovered\" error? Fix GPU timeout crashes with this ordered guide — drivers, TDR settings, thermals, and hardware checks."
thumbnail: "/images/thumbs/best-way-to-fix-display-driver-stopped-responding.webp"
faqs:
  - q: "What does 'display driver stopped responding and has recovered' mean?"
    a: "It means Windows' Timeout Detection and Recovery (TDR) caught the GPU taking too long to respond — over two seconds — and restarted the graphics driver instead of blue-screening. The screen flickers or freezes briefly, then comes back. It's a protective mechanism, but repeated TDRs signal a driver, thermal, or hardware problem worth fixing."
  - q: "Is the display driver crash caused by a bad GPU?"
    a: "Not usually. Most TDR crashes come from driver bugs, overheating, unstable overclocks, or power issues — a dying GPU is actually one of the rarer causes. Work through drivers, thermals, and power before suspecting the hardware, and only consider hardware failure if crashes happen at idle with clean drivers."
  - q: "Can increasing the TDR timeout fix the crashes?"
    a: "It can stop the error message, but it's a bandage: raising the TDR delay gives a struggling GPU more time before Windows resets it. If the underlying cause is a driver bug or overheating, the freezes continue — they just last longer. Fix the root cause first and only adjust TDR as a last resort."
  - q: "Why does it only crash in one game or app?"
    a: "Different apps stress the GPU differently — one game may hammer a shader path or VRAM allocation pattern that triggers a driver bug others never touch. App-specific crashes point at the driver or the app rather than the hardware. Try the app's own graphics settings first, then the driver fixes in this guide."
---

Few errors are as annoying as "Display driver stopped responding and has recovered." Your screen freezes, goes black for a second, flickers back — and whatever you were doing stutters. Windows is actually protecting you here: its Timeout Detection and Recovery (TDR) system noticed the GPU stopped answering and restarted the driver instead of crashing the whole machine. But when it happens repeatedly, it's a symptom, not a solution.

TDR crashes have a reputation for being mysterious, but they cluster around a handful of causes: bad driver installs, overheating, aggressive overclocks or undervolts, power delivery problems, and genuinely failing hardware — roughly in that order of likelihood. The trick is working them in order instead of jumping to "my GPU is dying."

## Why this happens

- **Corrupt graphics driver install:** partial or conflicting driver files cause timeouts under load.
- **Driver version bug:** a specific release has a TDR regression for your GPU or app.
- **GPU overheating:** thermal throttling and emergency shutdowns look like driver timeouts.
- **Unstable overclock or undervolt:** factory or user overclocks push the GPU past stability.
- **Insufficient power:** the PSU or laptop power delivery can't sustain boost clocks.
- **Failing VRAM:** bad memory chips cause timeouts during heavy allocation.
- **Windows TDR timeout too aggressive:** the default 2-second limit trips on legitimate long operations.
- **Background GPU contention:** mining malware, overlays, or recorders fight the app for the GPU.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean-install the graphics driver

1. Download the latest driver from your GPU vendor — [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel via the [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. During installation, choose **Custom** and check **Clean installation** (NVIDIA) or **Factory Reset** (AMD). This removes conflicting leftovers.
3. For a deeper clean, use Display Driver Uninstaller (DDU) in Safe Mode — the nuclear option for driver corruption.
4. Reboot and test with the app that crashed before. Most TDR clusters are fixed right here.
5. If the crashes *started* with a driver update, install the previous known-good version instead of the latest.

### Fix 2: Check GPU temperatures

1. Install HWiNFO64 or HWMonitor and watch GPU temperature during the workload that crashes.
2. Sustained temperatures above 85–90°C on a laptop GPU (or 80°C+ on desktop) point at thermal trouble.
3. Clean dust from vents and fans with compressed air — laptops collect shocking amounts of dust.
4. Replace dried thermal paste if the laptop is more than 2–3 years old and runs hot; this is the single most effective thermal fix.
5. Use a cooling pad and ensure vents aren't blocked — gaming on a bed is a classic TDR trigger.
6. If temperatures are fine at crash time, thermals aren't your cause; move on.

### Fix 3: Remove overclocks and reset to stock

1. Open MSI Afterburner, your vendor's utility, or the GPU control panel and reset all clocks, voltages, and power limits to default.
2. Disable any "OC mode," "Turbo," or "Game Boost" profiles in the laptop's control software — factory overclocks can be unstable too.
3. If you undervolted the GPU, restore stock voltage; an undervolt that's stable in one game can TDR in another.
4. Test for a full day at stock settings. Stability at stock proves the overclock was the problem.
5. Re-apply overclocks gradually only after confirming stability — and stress-test each step.

### Fix 4: Rule out power delivery problems

1. On laptops, always test with the original charger connected — many GPUs throttle or crash on battery or underpowered chargers.
2. Check that the charger's wattage matches the laptop's requirement; a 65W charger on a 130W gaming laptop causes exactly these symptoms.
3. On desktops, verify PCIe power cables are fully seated and the PSU wattage covers the GPU's transient spikes (which exceed rated TDP).
4. Try a different wall outlet and skip power strips with a dozen devices on them during testing.
5. Power-related TDRs often happen at the *start* of heavy load, when the GPU spikes hardest.

### Fix 5: Adjust the Windows TDR timeout

1. This is a workaround, not a fix — use it only after the steps above, or to buy stability while you investigate.
2. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
3. Create a DWORD (32-bit) value named **TdrDelay** and set it to `8` (seconds, up from the default 2).
4. Optionally add **TdrDdiDelay** set to `8` as well for good measure.
5. Reboot. Longer timeouts let legitimate long GPU operations finish instead of triggering a reset.
6. If crashes persist even with an 8-second timeout, the GPU is genuinely hanging — that's a hardware-level problem.

### Fix 6: Eliminate background GPU contention

1. Open Task Manager's Performance tab and watch GPU usage at idle — anything above a few percent is suspicious.
2. Disable overlays: Discord, GeForce Experience, Xbox Game Bar, and screen recorders all inject into the GPU pipeline.
3. Check for cryptominers or malware with a full scan — unauthorized GPU load causes exactly these timeouts.
4. In **Settings > System > Display > Graphics**, check per-app GPU assignment on multi-GPU laptops; forcing the wrong GPU causes conflicts.
5. Close browsers with hardware acceleration during testing — dozens of Chrome tabs with video can destabilize a marginal GPU.

### Fix 7: Test the hardware itself

1. Run a GPU stress test (FurMark or 3DMark) and watch for crashes, artifacts, or driver resets.
2. Crashes within minutes at stock settings and normal temperatures suggest VRAM or core degradation.
3. Test with the laptop's integrated graphics only (disable the discrete GPU in Device Manager) — stability on iGPU points at the discrete GPU.
4. If the GPU is failing, check warranty status before opening anything — vendors cover this.
5. Related display-driver problems like a [missing display adapter in Device Manager](/articles/how-to-fix-display-adapter-missing-on-windows-11/) share some of these diagnostic steps if the GPU vanishes entirely instead of just timing out.

## Closing

The "display driver stopped responding" error looks scary but is usually mundane: a botched driver install, dust-clogged cooling, or an overclock that isn't as stable as you thought. The order matters — clean drivers first, thermals second, clocks third — because each step is cheaper than the next and the statistics favor the early steps. Reserve hardware suspicion for last, and only after you've seen crashes at stock settings, normal temperatures, and clean drivers. Most TDR stories end at Fix 1 or Fix 2, with a GPU that was never dying at all. If the GPU disappears from Device Manager entirely instead of just timing out, work through [display adapter missing on Windows 10](/articles/how-to-fix-display-adapter-missing-on-windows-10/) — the diagnostic fork between driver and hardware is the same.
