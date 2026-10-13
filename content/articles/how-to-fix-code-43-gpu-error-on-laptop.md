---
title: "Code 43 GPU Error on a Laptop: Fix the Graphics Device"
slug: how-to-fix-code-43-gpu-error-on-laptop
date: 2026-09-07
categories: ["drivers"]
tags: ["code 43 gpu", "graphics device error", "nvidia amd driver", "windows 11"]
description: "GPU showing Code 43 in Device Manager? Repair the graphics driver stack and rule out hardware failure on your Windows laptop."
thumbnail: "/images/thumbs/how-to-fix-code-43-gpu-error-on-laptop.webp"
faqs:
  - q: "What does Code 43 mean on a GPU?"
    a: "Code 43 means Windows stopped the graphics device because it reported problems during startup. The driver asked the GPU to initialize and the GPU failed to respond correctly. Causes range from corrupted drivers and bad driver updates to the GPU not getting enough power, to genuine hardware failure of the graphics chip."
  - q: "Can a Windows update cause GPU Code 43?"
    a: "Yes, it's a common trigger. Feature updates can install a mismatched graphics driver, corrupt the existing installation mid-update, or change power policies that affect the discrete GPU. If Code 43 appeared right after an update, a clean reinstall of the manufacturer's graphics driver is the first fix to try."
  - q: "Is Code 43 always a dead GPU?"
    a: "No — dead GPUs are actually the minority. Most Code 43 cases resolve with a proper clean driver reinstall, a power-cycle, or disabling the conflicting driver Windows Update installed. Suspect hardware only when the error survives clean installs from the manufacturer, persists in a Linux live environment, and appears immediately on every boot."
  - q: "Why does my laptop work fine but the GPU shows Code 43?"
    a: "Because the laptop falls back to integrated graphics when the discrete GPU fails to start. Everything looks normal for office work and browsing, but games and GPU-accelerated apps will be slow or fail. Device Manager reveals the truth: the discrete GPU is stopped with Code 43 while the integrated GPU carries the load."
---

Code 43 on a GPU — "Windows has stopped this device because it has reported problems" — is alarming because it suggests the graphics chip is dead. Usually it isn't. The error means the driver couldn't initialize the GPU, and the causes span corrupted drivers, bad updates, power issues, and only occasionally actual hardware failure. This guide works from the most likely software causes toward the hardware verdict.

First, check which GPU is affected. On laptops with switchable graphics, the integrated GPU (Intel/AMD) almost never throws Code 43 — it's the discrete NVIDIA or AMD chip that does. Your laptop keeps working because the integrated GPU takes over, which is why everything seems fine until you launch a game. Confirm in Device Manager under Display adapters which device carries the yellow warning. For NVIDIA-specific driver crashes, also see [fixing NVIDIA driver crashes](/articles/best-way-to-fix-nvidia-driver-crashing/).

## Why this happens

- **Corrupted graphics driver:** The installed driver's files are damaged, so GPU initialization fails.
- **Bad driver update:** A new driver version has a bug affecting your specific GPU, or the update was interrupted.
- **Windows Update driver mismatch:** Windows installed a generic or wrong-version driver over the working one.
- **Insufficient power to the GPU:** Power management or a failing adapter starves the discrete GPU during init.
- **Driver conflict between GPUs:** Integrated and discrete driver stacks fight during the handoff.
- **Overclock/undervolt instability:** An unstable overclock causes the GPU to fail its startup self-test.
- **Failing GPU hardware:** Degraded VRAM or a dying chip fails initialization — real, but less common.
- **BIOS/firmware GPU issues:** Buggy video BIOS or system BIOS mishandles the discrete GPU at boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Power-cycle to reset the GPU hardware state

Shut down fully (Shift + Shut down to bypass Fast Startup), unplug the charger, and wait 60 seconds. For gaming laptops, also disconnect any external monitors and docks. Power on and check Device Manager. GPUs can get stuck in a bad power state that survives normal reboots, and a full power drain resets the card's firmware state. If Code 43 clears but returns after sleep, you're dealing with a power-management resume bug — note that for Fix 4.

1. Shift + Shut down for a full shutdown.
2. Unplug the charger and disconnect docks/monitors.
3. Wait 60 seconds for residual power to drain.
4. Power on and check Device Manager.
5. Note whether the error returns after sleep.

### Fix 2: Clean-reinstall the graphics driver

Download the latest driver for your exact GPU — [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) for GeForce, [AMD's driver support](https://www.amd.com/en/support/download/drivers.html) for Radeon. During installation, choose Custom/Advanced and tick "Perform a clean installation" (NVIDIA) or use the Factory Reset option (AMD). This wipes the old driver completely instead of layering over it. Reboot and verify the GPU starts. If the newest driver caused the problem, install the previous known-good version instead — driver regressions are real.

1. Download the driver for your exact GPU model.
2. Choose Custom install with clean installation ticked.
3. If the newest driver caused it, install the older working version.
4. Reboot after installation.
5. Verify the GPU starts in Device Manager.

### Fix 3: Use the laptop maker's graphics driver

Laptop GPUs are not desktop cards — they have custom power and thermal profiles, and the maker's driver is tuned for them. If the GPU maker's reference driver throws Code 43, try the graphics driver from your laptop manufacturer's support page ([Dell](https://www.dell.com/support), for example) for your exact model. Uninstall the current driver with Display Driver Uninstaller (DDU) in Safe Mode first for the cleanest possible slate, then install the maker's package. This resolves a large share of persistent Code 43 cases on gaming laptops.

1. Download DDU and the maker's graphics driver.
2. Boot into Safe Mode and run DDU to remove the GPU driver.
3. Reboot normally.
4. Install the laptop maker's graphics driver package.
5. Reboot and verify the GPU initializes.

### Fix 4: Fix GPU power management

In the NVIDIA Control Panel or AMD Software, set the power management mode to "Prefer maximum performance" (NVIDIA) or disable deep sleep states (AMD) as a test. In Windows Power Options, set PCI Express Link State Power Management to Off. Also test with the charger connected and the Windows power mode set to Best performance — if Code 43 only appears on battery, the GPU isn't getting the power it needs to initialize. A failing or underrated charger can cause exactly this on gaming laptops.

1. Set GPU power mode to maximum performance in its control panel.
2. Disable PCIe Link State Power Management in Power Options.
3. Test with the original high-wattage charger connected.
4. Set Windows power mode to Best performance.
5. Note whether the error is battery-only.

### Fix 5: Remove overclocks and undervolts

If you've overclocked or undervolted the GPU with MSI Afterburner or similar, reset everything to stock — an unstable tune causes the GPU to fail its power-on self-test, which Windows reports as Code 43. Uninstall the tuning software entirely for the test, since profiles can reapply at boot. Also reset any BIOS-level performance tweaks. If the GPU starts cleanly at stock settings, your tune was the problem; re-tune conservatively if you must. Microsoft's support pages cover Safe Mode booting if driver crashes prevent normal startup.

1. Reset all GPU overclocks and undervolts to stock.
2. Uninstall tuning software like Afterburner for the test.
3. Reset BIOS performance tweaks to defaults.
4. Reboot and check Device Manager.
5. Re-tune conservatively only after stability is confirmed.

### Fix 6: Check for Windows Update interference

If Code 43 appeared after a Windows update, the update likely replaced your driver. Roll back the display driver in Device Manager (Driver tab, Roll Back Driver), then use Group Policy or the "show or hide updates" troubleshooter to block driver updates from Windows Update. Reinstall your known-good driver afterward. Also check whether the update changed the BIOS-adjacent firmware — some updates bundle firmware that affects GPU initialization. For the broader pattern, see [display driver stopped responding](/articles/how-to-fix-display-driver-stopped-responding-after-windows-11-update/).

1. Roll back the display driver in Device Manager.
2. Block driver updates from Windows Update.
3. Reinstall your known-good graphics driver.
4. Check update history for bundled firmware updates.
5. Pause updates while you stabilize the driver.

### Fix 7: Verify hardware with independent tests

Boot a Linux live USB and check whether the discrete GPU initializes there (`lspci` should show it without errors, and GPU tools should detect it). If Linux also fails, the GPU hardware is likely dying — on most laptops the GPU is soldered, meaning motherboard-level repair. Also run the laptop maker's built-in hardware diagnostics (Dell SupportAssist, HP PC Hardware Diagnostics, Lenovo Diagnostics) which include GPU tests. Artifacting, crashes under load, or Code 43 across all operating systems is the hardware verdict.

1. Boot a Linux live USB and check GPU detection.
2. Run the maker's built-in hardware diagnostics.
3. Note artifacting or crashes under GPU load.
4. Code 43 in every OS means hardware failure.
5. Get a board-level repair quote — laptop GPUs are usually soldered.

## Closing

Code 43 on a laptop GPU is a driver problem until proven otherwise, and the proof comes from clean reinstalls — first the GPU maker's driver, then the laptop maker's tuned package via DDU. Power management and bad updates account for most of the rest. When the error survives every driver, every OS, and every power configuration, you've done the software due diligence and it's time to talk hardware repair.
