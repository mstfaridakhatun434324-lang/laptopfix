---
title: "Fix the Code 43 GPU Error on Windows 11 24H2"
slug: how-to-fix-code-43-gpu-error-in-windows-11-24h2
date: 2026-10-05
categories: ["drivers"]
tags: ["code 43", "gpu error", "nvidia", "amd", "windows 11 24h2"]
description: "Code 43 has stopped your GPU on Windows 11 24H2? Diagnose driver corruption, power issues, and hardware failure with this technician's repair guide."
thumbnail: "/images/thumbs/how-to-fix-code-43-gpu-error-in-windows-11-24h2.webp"
faqs:
  - q: "What does Code 43 mean for my graphics card?"
    a: "Code 43 means Windows has stopped the device because it reported a problem — the GPU driver crashed during initialization or the card failed its startup checks, so Windows disabled it to protect the system. You'll see it in Device Manager with the message Windows has stopped this device because it has reported problems. It indicates either driver corruption or a genuine hardware fault."
  - q: "Can a driver update cause Code 43?"
    a: "Absolutely — it's one of the most common triggers. A new driver that conflicts with your Windows build, a corrupted download, or leftover files from the previous driver can all make the GPU fail initialization. Rolling back the driver in Device Manager or doing a clean reinstall with DDU resolves update-caused Code 43 in most cases."
  - q: "Does Code 43 always mean my GPU is dead?"
    a: "No. Driver issues cause the majority of Code 43 errors, and those are fully fixable in software. Suspect hardware only when Code 43 survives a clean driver reinstall on a fresh Windows build, appears in the BIOS diagnostics, or is accompanied by artifacts and crashes. Don't assume a dead card until the software fixes are exhausted."
  - q: "Why did Code 43 appear after updating to Windows 11 24H2?"
    a: "Feature updates change kernel components that GPU drivers hook into. A driver that worked on the previous build can fail its initialization checks on 24H2, triggering Code 43. GPU vendors release updated drivers for new Windows builds — installing the latest driver certified for 24H2 from NVIDIA or AMD is the direct fix."
---

Open Device Manager, expand Display adapters, and there it is: a yellow triangle on your GPU and the dreaded status "Windows has stopped this device because it has reported problems. (Code 43)." Your games won't launch, hardware acceleration is gone, and the laptop may be running on basic display output. Code 43 is Windows' way of saying the GPU tried to start, failed, and got benched for safety.

The critical question is whether the failure is software or silicon. Driver corruption — from a bad update, a crashed install, or a Windows build mismatch — causes most Code 43 errors and is completely fixable. Genuine hardware failure is the minority but must be ruled in or out honestly, because the two demand opposite responses: patience and procedure for software, versus a repair quote for hardware. This guide works the software side thoroughly first, because there's no point mourning a GPU that just needs a clean driver.

## Why this happens

- **Corrupted GPU driver:** The most common cause — a damaged driver installation fails the GPU's startup sequence, and Windows stops the device with Code 43.
- **Windows 11 24H2 kernel mismatch:** The feature update changed driver-facing interfaces; older GPU drivers fail initialization on the new build until updated.
- **Leftover files from a previous driver:** Partial uninstalls leave conflicting driver components that sabotage the new driver's startup — the same debris that causes [NVIDIA installer failures](/articles/best-way-to-fix-nvidia-installer-cannot-continue/).
- **GPU power delivery problem:** On laptops, a failing charger, degraded battery, or power-management bug can starve the discrete GPU during initialization.
- **Overheating damage:** Chronic overheating can damage the GPU or its memory, producing Code 43 that persists across driver reinstalls — a hardware verdict.
- **BIOS/firmware incompatibility:** An outdated system BIOS may misconfigure the PCIe link to the discrete GPU, especially after a Windows feature update.
- **Conflicting overclock or tuning software:** MSI Afterburner profiles or manufacturer tuning utilities can push the GPU into an unstable state at boot.
- **Failing GPU hardware:** Dead memory chips, cracked solder joints (common on aging laptops), or a dying GPU core produce Code 43 that no driver can fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's really Code 43 and note the pattern

1. Open Device Manager, right-click the GPU, choose **Properties**, and confirm the status is Code 43 on the General tab.
2. Note when it started: right after a driver update, a Windows update, or randomly during use. Update-triggered means software; random with artifacts leans hardware.
3. Check Event Viewer (**Win+X > Event Viewer > Windows Logs > System**) for `nvlddmkm` or `amdkmdap` errors around the failure time — driver crashes logged here confirm the software side.

### Fix 2: Roll back the driver

1. In the GPU's Properties window, open the **Driver** tab and click **Roll Back Driver** if available.
2. Restart and check whether Code 43 clears. If it does, the new driver was the problem — stay on the older version until the vendor releases a fixed build.
3. If rollback isn't available, continue to the clean reinstall.

### Fix 3: Clean-reinstall the GPU driver with DDU

1. Download the latest driver for your GPU and Windows 11 24H2 from [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx) or [AMD's driver support page](https://www.amd.com/en/support/download/drivers.html) — pick your vendor.
2. Download Display Driver Uninstaller, boot into Safe Mode, and run DDU to remove the GPU driver completely (**Clean and restart**).
3. Install the fresh driver in normal mode and restart. This resolves the large majority of Code 43 cases, as detailed in the [clean-install walkthrough](/articles/how-to-update-nvidia-drivers-clean-install-in-windows-11-24h2/).

### Fix 4: Remove overclocking and tuning software

1. Uninstall MSI Afterburner, manufacturer control centers' overclock features, or any GPU tuning utility.
2. If your laptop has a MUX switch or GPU mode setting (in BIOS or the manufacturer's app), set it to the mode that was working before.
3. Restart and check Device Manager. An unstable overclock applied at boot is a classic Code 43 trigger that survives driver reinstalls until the tuning software is gone.

### Fix 5: Check power delivery

1. Run the laptop on its original charger (not a USB-C dock or underpowered brick) with the battery in.
2. In Windows power settings, set the power mode to **Best performance** while testing.
3. If Code 43 appears only on battery or with a weak charger, the GPU isn't getting clean power during initialization — replace the charger with the correct wattage.

### Fix 6: Update the system BIOS

1. Check your laptop manufacturer's support site for a BIOS update newer than yours (`msinfo32` shows the current version).
2. Install it with the charger connected, following the manufacturer's instructions exactly.
3. BIOS updates frequently include PCIe and power-management fixes that resolve GPU initialization failures on new Windows builds.

### Fix 7: Test for hardware failure honestly

1. Boot into the BIOS/UEFI setup — if the screen shows artifacts there, the GPU hardware is failing (no Windows driver is involved at that stage).
2. Run the manufacturer's built-in hardware diagnostics (usually F2 or F12 at boot) and run the video/GPU test.
3. If Code 43 survives DDU clean installs, BIOS updates, and proper power — and especially if artifacts appear — the GPU needs professional repair or board replacement. For an aging laptop, weigh repair cost against replacement.

## Closing

Code 43 is a symptom, not a death certificate. Work the software chain — rollback, DDU clean install, remove tuning software, verify power, update BIOS — and most GPUs come back to life, because most Code 43 errors are driver corruption wearing a scary mask. Only when every software fix fails and the symptoms point below the OS (BIOS artifacts, failed diagnostics) should you accept the hardware verdict. Diagnose honestly, and you'll either fix it or know exactly why it can't be fixed — which is far better than replacing a GPU that only needed a clean driver.
