---
title: "How to Fix VIDEO_TDR_FAILURE on Windows 11"
slug: how-to-fix-video-tdr-failure-on-windows-11
date: 2026-10-01
categories: ["windows-errors"]
tags: ["blue screen", "video_tdr_failure", "windows 11"]
description: "VIDEO_TDR_FAILURE on Windows 11 means the GPU driver hung and couldn't recover. Clean-reinstall the driver, cool the GPU, and stabilize it step by step."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-on-windows-11.webp"
faqs:
  - q: "What does VIDEO_TDR_FAILURE mean on Windows 11?"
    a: "TDR is Timeout Detection and Recovery. Windows 11 monitors the graphics driver, and if the GPU stops responding for more than a couple of seconds, Windows tries to reset the driver without crashing. VIDEO_TDR_FAILURE means that reset attempt failed. The root cause is usually a buggy or corrupted GPU driver, though overheating and unstable overclocks produce the identical symptom."
  - q: "Why does the error name files like nvlddmkm.sys?"
    a: "That's the actual driver that hung — nvlddmkm.sys is NVIDIA's, atikmdag.sys is AMD's, and igdkmd64.sys is Intel's integrated graphics driver. The named file confirms the crash is in the graphics stack and tells you exactly which driver to focus on. If the named file changes between crashes, suspect bad system RAM instead of the GPU driver."
  - q: "Does hardware-accelerated GPU scheduling cause TDR failures?"
    a: "It can on some driver and hardware combinations. Hardware-accelerated GPU scheduling changes how the GPU driver manages memory, and buggy implementations have triggered TDR crashes. Toggling it off in Settings > System > Display > Graphics is a quick, safe test — if crashes stop, leave it off until a newer driver arrives."
  - q: "How is this different from a regular game crash to desktop?"
    a: "A crash to desktop means the game itself failed but Windows and the driver survived. VIDEO_TDR_FAILURE means the graphics driver hung so badly that Windows' recovery mechanism failed too, forcing a full system crash. TDR blue screens always point at the driver, GPU, or system stability — never at the game's own bugs."
---

VIDEO_TDR_FAILURE on Windows 11 means your graphics driver froze and Windows couldn't restart it. You'll usually see it mid-game, during video editing, or when waking from sleep — any moment the GPU is asked to do real work.

Windows 11 adds a couple of wrinkles (hardware GPU scheduling, new driver model), but the fix order is proven: clean out the driver completely, stabilize the GPU, then rule out the supporting hardware. Let's go.

## Why this happens

- **Corrupted GPU driver installation.** Old driver remnants conflicting with the new version — the top cause.
- **Buggy driver release.** A brand-new driver with a regression for your specific card.
- **Hardware-accelerated GPU scheduling conflicts.** Windows 11's scheduling feature clashing with certain drivers.
- **Overheating GPU.** Heat-induced hangs that trip the timeout detection.
- **Unstable overclock.** Factory or manual GPU/memory overclocks failing under sustained load.
- **Multi-plane overlay (MPO) bugs.** A known source of TDR crashes on some NVIDIA/AMD driver versions.
- **Weak power delivery.** Charger or PSU issues starving the GPU at peak draw.
- **Bad system RAM.** Corrupting GPU driver data and mimicking a graphics problem.

## How to fix it

Work through these in order, from Fix 1 onward, and stop as soon as the crashes stop.

### Fix 1: Clean-reinstall the GPU driver with DDU

Don't just update over the top — wipe the driver completely and start fresh.

1. Download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) and save it without running it.
2. Download Display Driver Uninstaller (DDU).
3. Boot into Safe Mode using our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/).
4. Run DDU, select your GPU brand, and click **Clean and restart**.
5. Install the downloaded driver, choosing **Custom** and checking **Clean installation**.

### Fix 2: Turn off hardware-accelerated GPU scheduling

This Windows 11 feature is a known TDR trigger on some setups, and toggling it is harmless.

1. Open **Settings > System > Display > Graphics**.
2. Click **Change default graphics settings** at the top.
3. Turn off **Hardware-accelerated GPU scheduling**.
4. Restart the laptop.
5. Test your usual crashing workload for a few days before deciding whether to leave it off permanently.

### Fix 3: Try an older, proven driver version

If crashes started with a recent driver, the driver is the bug — go back to one that worked.

1. Download a driver from two or three months ago from the GPU maker's site.
2. Remove the current driver with DDU in Safe Mode (same process as Fix 1).
3. Install the older version.
4. In **Settings > Windows Update > Advanced options**, pause updates briefly so Windows doesn't immediately replace it.
5. Watch the GPU maker's release notes — install the fixed version when it lands.

### Fix 4: Cool the GPU and drop overclocks

Heat and unstable clocks cause the exact hangs TDR detects.

1. Reset MSI Afterburner or any overclocking tool to stock settings.
2. Monitor temperatures with HWMonitor during the workload that crashes.
3. On a laptop, sustained GPU temps above 85 to 90 degrees Celsius need attention — clean vents with compressed air and use a hard, flat surface.
4. Disable any factory "OC mode" in the laptop maker's control app (Armoury Crate, Legion Zone, Omen Hub) as a test.
5. If temperatures are fine at stock clocks, overclocking wasn't your issue — move on.

### Fix 5: Disable MPO via the registry

Multi-plane overlay bugs have caused TDR crashes on several driver generations. Disabling it is a well-known workaround.

1. Press **Win + R**, type `regedit`, and press Enter.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Dwm`.
3. Right-click, choose **New > DWORD (32-bit) Value**, and name it `OverlayTestMode`.
4. Set its value to `5` and click **OK**.
5. Restart. If this was the trigger, crashes stop immediately — and you can re-enable it after a future driver update to test.

### Fix 6: Increase the TDR delay

Giving Windows more time before declaring the driver dead helps borderline cases.

1. In `regedit`, go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a **DWORD (32-bit) Value** named `TdrDelay` and set it to `8`.
3. Optionally create `TdrDdiDelay` set to `10` as well.
4. Restart the laptop.
5. This is a bandage, not a cure — keep working the driver fixes above alongside it.

### Fix 7: Update Windows 11 and repair system files

Make sure the OS side of the graphics stack is healthy.

1. Open **Settings > Windows Update** and install everything offered.
2. Open **Terminal (Admin)** and run `sfc /scannow`.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Test your RAM with `mdsched.exe` too — bad memory mimics GPU driver crashes.
5. Restart and confirm the second SFC pass comes back clean.

### Fix 8: Verify the GPU hardware

If clean drivers, cool temps, and stock clocks still crash, test the hardware.

1. On a desktop, reseat the GPU and confirm all power connectors are firmly attached.
2. Test with the original charger on a laptop — third-party chargers cause GPU brownouts under load.
3. Try the workload on integrated graphics alone (disable the discrete GPU in Device Manager) — if it's stable, the discrete GPU is the problem.
4. Crashes in the BIOS screen or during Windows setup mean hardware failure, not drivers.
5. For a laptop discrete GPU that fails after a clean Windows install, check warranty status before anything else.

## Closing

VIDEO_TDR_FAILURE on Windows 11 is a driver problem until proven otherwise — and the DDU clean install in Fix 1 does most of the proving. Toggle the GPU scheduling feature, cool things down, and work the list patiently without skipping steps. If you're still on the older OS, the [Windows 10 version of this guide](/articles/how-to-fix-video-tdr-failure-on-windows-10/) covers the same ground, and the [gaming blue screen fixes](/articles/how-to-fix-blue-screen-while-gaming-reddit/) help when crashes only happen under load.
