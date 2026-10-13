---
title: "How to Fix NVIDIA Driver Crashing on Windows 11 (8 Reliable Fixes)"
slug: how-to-fix-nvidia-driver-crashing-on-windows-11
date: 2026-09-10
categories: ["drivers"]
tags: ["nvidia driver crash", "windows 11", "gpu tdr", "nvlddmkm", "driver fix"]
description: "NVIDIA driver crashing on Windows 11? From DDU clean installs to TDR tweaks and Windows 11-specific culprits like MPO and HAGS, here are eight fixes that stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-nvidia-driver-crashing-on-windows-11.webp"
faqs:
  - q: "Why does my NVIDIA driver crash more on Windows 11 than it did on 10?"
    a: "Three Windows 11-specific factors: more aggressive automatic driver replacement via Windows Update, Multiplane Overlay (MPO) interacting badly with certain card/monitor combinations, and Hardware-Accelerated GPU Scheduling changing GPU memory behavior. Disabling MPO, testing HAGS both ways, and blocking driver updates through Windows Update resolves most of the Windows-11-only instability."
  - q: "What is MPO and why does disabling it fix black screens?"
    a: "Multiplane Overlay lets the GPU handle window composition directly instead of the CPU compositor, reducing latency and power use. On some NVIDIA card, monitor, and driver combinations the MPO path has bugs that cause black-screen flicker and TDR crashes. Disabling it via the OverlayTestMode registry value forces the classic composition path, which is thoroughly battle-tested, at negligible visual cost."
  - q: "Should Hardware-Accelerated GPU Scheduling be on or off for NVIDIA?"
    a: "There is no universal answer. HAGS generally benefits RTX 30-series and newer cards in CPU-bound scenarios, but it has caused stuttering and TDR crashes on some older cards and specific driver versions. Test your actual crashing workload with HAGS on and off — keep whichever is stable. The toggle requires a restart and lives under Settings > System > Display > Graphics."
  - q: "How do I know if my GPU is dying or if it is just a driver issue?"
    a: "A clean DDU reinstall that changes nothing, crashes accompanied by visual artifacts (checkerboard patterns, colored blocks, corrupted textures), and VRAM stress-test errors at stock clocks and safe temperatures all point to failing hardware. Pure driver issues typically resolve with a clean install, show no artifacts, and often correlate with a recent driver or Windows update."
---

On Windows 11, NVIDIA driver crashes wear the same disguise as on Windows 10 — a black flicker, a frozen game, Event ID 4101 ('Display driver nvlddmkm stopped responding'), sometimes a VIDEO_TDR_FAILURE blue screen — but Windows 11 adds its own suspects to the lineup: Multiplane Overlay (MPO), Hardware-Accelerated GPU Scheduling (HAGS), and a Windows Update system that is even more eager to replace your driver.

The fundamentals have not changed: most crashes trace back to a corrupted driver install, an unstable overclock, heat, or power delivery. What Windows 11 changes is the frequency of driver replacement and a few compositor-level features that can destabilize specific card and monitor combinations. Diagnose in the right order and you will find the cause quickly.

This guide focuses on Windows 11-specific angles. For the full clean-reinstall procedure, see [clean-installing NVIDIA drivers](/articles/best-way-to-update-nvidia-drivers-clean-install/); for the general crash playbook that applies to both Windows versions, our [Windows 10 NVIDIA crash guide](/articles/how-to-fix-nvidia-driver-crashing-on-windows-10/) covers the shared ground. If Event Viewer mentions the display driver timing out more broadly, the [display driver stopped responding guide](/articles/how-to-fix-display-driver-stopped-responding-after-windows-11-update/) is the right companion.

## Why this happens

- **Corrupted or layered driver install** — Multiple install-over-install updates leave conflicting files that crash under DirectX 12 and Vulkan workloads.
- **Windows Update replacing the NVIDIA driver** — Windows 11's driver updates are aggressive; an automatic replacement mid-week is a classic 'it worked yesterday' trigger.
- **Multiplane Overlay (MPO) instability** — MPO offloads window composition to the GPU; on some card/monitor/driver combos it causes black-screen flicker and TDR crashes.
- **Hardware-Accelerated GPU Scheduling conflicts** — HAGS changes GPU memory scheduling and can destabilize older cards or certain driver branches.
- **Unstable overclock or undervolt** — Driver updates change voltage-frequency behavior, so a previously stable tune can become crash-prone overnight.
- **Overheating or power delivery issues** — Thermal throttling and 12V rail sag produce crashes that are identical in Event Viewer to software bugs.
- **Overlay and capture software hooks** — Discord overlay, GeForce Experience overlay, OBS hooks, and some RGB utilities inject into the render path.
- **Failing GPU memory (VRAM)** — Artifacting plus crashes in specific games can indicate degrading VRAM rather than any driver issue.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean-reinstall the driver with DDU

This remains the highest-yield fix on Windows 11 too. A truly clean slate eliminates the layered-install corruption that causes most TDR crashes.

1. Download DDU and the latest NVIDIA driver from [NVIDIA's official driver download page](https://www.nvidia.com/Download/index.aspx).
2. Disconnect from the internet to block Windows Update interference.
3. Boot into Safe Mode via Settings > System > Recovery > Advanced startup.
4. Run DDU (GPU / NVIDIA / Clean and restart).
5. Install the downloaded driver using Custom > **Perform a clean installation**, then reconnect and test.

### Fix 2: Disable MPO via the registry

Microsoft and NVIDIA both acknowledge MPO-related black screens on certain configurations. NVIDIA even ships an official MPO-disable registry key, which tells you how real this is.

1. Download the official 'Disable MPO' .reg file from NVIDIA support (search 'MPO disable NVIDIA') or create it manually.
2. Manual method: in regedit, go to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Dwm` and create DWORD **OverlayTestMode** = `5`.
3. Restart the PC.
4. If flicker and crashes stop, leave it disabled — the visual difference is negligible on most setups.

### Fix 3: Toggle Hardware-Accelerated GPU Scheduling

HAGS helps on modern cards but hurts on some older ones. Testing both states takes two minutes.

1. Open Settings > System > Display > Graphics > Change default graphics settings.
2. Toggle **Hardware-accelerated GPU scheduling** to the opposite of its current state.
3. Restart when prompted.
4. Stress-test with your crashing game. Keep whichever setting is stable — there is no universally correct value.

### Fix 4: Block Windows Update driver replacements

On Windows 11 this step is nearly mandatory after a clean install, or the OS will eventually undo your work.

1. Open Settings > Windows Update > Advanced options > Optional updates — uncheck any NVIDIA driver offered there.
2. For Pro editions: gpedit.msc > Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update > enable **Do not include drivers with Windows Updates**.
3. Restart and verify your driver version survives the next update cycle.

### Fix 5: Reset clocks, check thermals and power

Hardware causes do not care which Windows version you run. Rule them out before chasing software ghosts.

1. Reset any GPU overclock/undervolt to stock and close tuning utilities.
2. Monitor GPU temperature under load — sustained 86°C+ means clean the cooler and check fans.
3. On desktops, use separate PCIe power cables per connector, not daisy-chained splitters.
4. On laptops, test plugged in on the **Best performance** power mode; also see Microsoft's [Windows 11 support hub](https://support.microsoft.com/en-us/windows) for power-plan guidance.

### Fix 6: Disable overlays and background injectors

Windows 11's compositor plus an overlay hook is a known crash cocktail during mode changes and alt-tabs.

1. Turn off the GeForce Experience in-game overlay (Settings > General).
2. Disable Discord's game overlay and close any FPS/RTSS overlays.
3. Temporarily exit RGB control software (iCUE, Armoury Crate lighting services) that hooks into games.
4. Retest for at least an hour of the previously crashing workload.

### Fix 7: Run a VRAM stress test

If crashes come with visual artifacts — checkerboards, colored blocks, texture corruption — the memory on the card may be failing, and no driver will fix that.

1. Download OCCT or FurMark and run the VRAM/GPU memory test for 20–30 minutes.
2. Watch for artifacts or errors in the test log.
3. If errors appear at stock clocks and normal temperatures, the card is likely failing — check warranty/RMA options.
4. If the test is clean, your crashes are software-side; revisit Fixes 1–4.

### Fix 8: Try a previous stable driver version

When a specific Game Ready driver introduced the crashes, rolling back is rational troubleshooting, not defeat.

1. Identify a driver version that was stable for your card (community forums and release notes help).
2. DDU-clean the current driver in Safe Mode.
3. Install the older driver with the clean-install option.
4. Disable automatic driver updates in GeForce Experience until a fixed release is confirmed.

## Closing

Windows 11 adds MPO and HAGS to the NVIDIA crash suspect list, but the diagnostic order stays the same: clean reinstall, stop Windows Update from replacing it, test the Windows 11-specific toggles, then rule out clocks, heat, power, and VRAM. Most systems are stable by Fix 4; the later fixes catch the hardware and edge cases that software alone cannot explain.
