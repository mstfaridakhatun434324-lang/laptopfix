---
title: "Display Adapter Missing? A Step-by-Step Recovery Guide"
slug: how-to-fix-display-adapter-missing-step-by-step
date: 2026-10-06
categories: ["drivers"]
tags: ["display adapter", "gpu missing", "device manager", "graphics driver", "windows 11"]
description: "Display adapter vanished from Device Manager? Recover it step by step: reveal hidden devices, reinstall graphics drivers, reset BIOS, and rule out hardware failure."
thumbnail: "/images/thumbs/how-to-fix-display-adapter-missing-step-by-step.webp"
faqs:
  - q: "Why is my display adapter missing from Device Manager?"
    a: "The adapter goes missing when Windows loses its driver registration — usually after a Windows update, a failed driver install, or the device being disabled. The GPU hardware is typically still present. Less commonly, the GPU is disabled in BIOS or has suffered hardware failure. A missing adapter after an update is almost always a driver problem, not dead hardware."
  - q: "How do I get my graphics card to show up again?"
    a: "Open Device Manager, enable View > Show hidden devices, and scan for hardware changes. If the GPU appears greyed out, uninstall it and rescan. Then reinstall the graphics driver from your laptop manufacturer's site. If it's still invisible, check the BIOS for a disabled discrete GPU and run the manufacturer's hardware diagnostics to rule out failure."
  - q: "Can Windows Update make my display adapter disappear?"
    a: "Yes. Feature updates sometimes corrupt the graphics driver's registration or replace it with an incompatible build, causing the adapter to vanish from Device Manager. Reinstalling the manufacturer's graphics driver restores it. This is well documented for Windows 11 24H2, which changed enough driver-facing components to break older GPU drivers."
  - q: "What if only the Microsoft Basic Display Adapter shows up?"
    a: "That means Windows sees display hardware but has no proper driver for it — the GPU is present but running on the generic fallback. This is actually good news: the hardware is alive. Install the correct Intel, AMD, or NVIDIA driver for your model and the real adapter name will replace the generic entry after a restart."
---

Your screen works, but Device Manager shows no display adapter — or only the sad "Microsoft Basic Display Adapter" placeholder. Games won't launch, external monitors misbehave, brightness controls vanish, and everything feels sluggish because there's no GPU acceleration. The graphics hardware hasn't necessarily died; Windows has simply lost its handle on it.

This is a driver-registration problem far more often than a hardware problem. Windows updates, failed driver installs, and disabled device states all produce the same symptom: an empty Display adapters section. The recovery follows a strict order — reveal, rescan, reinstall, reconfigure — because each step addresses a deeper layer of the problem. Let's bring your GPU back into the light.

## Why this happens

- **Driver registration corrupted by an update:** Windows 11 feature updates can damage the graphics driver's registry entries, so the adapter stops enumerating — the [24H2-specific variant](/articles/how-to-fix-display-adapter-missing-in-windows-11-24h2/) documents this pattern in detail.
- **Failed driver installation:** An interrupted or incompatible graphics driver install can leave the adapter in a limbo state where Windows won't list it.
- **Device disabled:** The adapter may simply be disabled (accidentally, by software, or by a failed power transition) — invisible until re-enabled.
- **Discrete GPU disabled in BIOS:** Many laptops let the BIOS disable the NVIDIA/AMD GPU for troubleshooting; if left off, Windows never sees it.
- **Hybrid graphics driver mismatch:** On Intel+NVIDIA or AMD+Radeon laptops, a broken integrated-graphics driver can cascade into the discrete GPU disappearing too.
- **Windows running on the basic adapter:** When the real driver fails, Windows falls back to Microsoft Basic Display Adapter — functional but featureless, and a clear sign the proper driver needs reinstalling.
- **BIOS/firmware incompatibility:** An old BIOS may misconfigure the GPU's PCIe link after a Windows feature update, hiding the device.
- **Hardware failure:** A dead GPU or damaged PCIe connection removes the device at the hardware level — the diagnosis of exclusion when all software steps fail.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and rescan

1. Open Device Manager (**Win+X > Device Manager**).
2. Click **View > Show hidden devices**. A greyed-out display adapter means it's present but disabled or disconnected — right-click it and choose **Uninstall device**, then continue.
3. Click **Action > Scan for hardware changes** and watch the Display adapters section.
4. If the adapter appears with a warning icon instead of vanishing, you've moved the problem forward — note the error code (Code 43 and friends have their own fixes).

### Fix 2: Check for the Microsoft Basic Display Adapter

1. If Display adapters shows only **Microsoft Basic Display Adapter**, the GPU hardware is detected but driverless — this is a pure driver problem.
2. Right-click it and choose **Update driver > Search automatically for drivers** as a first attempt.
3. Regardless of the result, proceed to install the manufacturer's driver in Fix 3 — Windows' automatic driver is a stopgap, not the solution.

### Fix 3: Reinstall the graphics driver from the manufacturer

1. Identify your GPU: check your laptop's specifications or look at the basic adapter's **Properties > Details > Hardware Ids** for VEN/DEV codes.
2. Download the graphics driver from your laptop manufacturer's support site for your exact model — OEM drivers handle laptop GPU wiring correctly.
3. If the installer refuses because it can't find the hardware, extract the package and install via Device Manager's **Browse my computer for drivers** pointed at the extracted folder.
4. Restart and verify the real adapter name appears. [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can identify the right Intel graphics driver automatically. If the adapter appears but immediately shows an error code after installation, the [post-update display adapter guide](/articles/how-to-fix-display-adapter-missing-after-windows-11-update/) covers error-specific recovery for that exact situation.

### Fix 4: Clean out corrupted driver remnants

1. If the adapter still won't appear, download Display Driver Uninstaller (DDU).
2. Boot into Safe Mode and run DDU to remove all graphics drivers (**Clean and restart**).
3. After reboot, install the manufacturer's driver fresh. Corrupted remnants are a leading cause of adapters that stay missing through normal reinstalls.

### Fix 5: Check the BIOS for a disabled GPU

1. Restart and enter the BIOS/UEFI setup (usually **F2** or **Del**).
2. Look for graphics options: **Discrete GPU**, **Dedicated graphics**, **Switchable graphics**, or **MUX switch** settings.
3. Make sure the discrete GPU is **Enabled** (not forced to integrated-only), save, and exit.
4. If your laptop has a MUX switch set to iGPU-only mode, the NVIDIA/AMD adapter legitimately won't appear in Windows — that's by design, not a fault.

### Fix 6: Reset BIOS to defaults and update it

1. In the BIOS, choose **Load Optimized Defaults** (or similar), save, and exit — a misconfigured firmware setting can hide the GPU.
2. Check the manufacturer's support site for a BIOS update and install it with the charger connected.
3. After the update, recheck Device Manager. BIOS updates regularly include PCIe enumeration fixes that restore missing GPUs.

### Fix 7: Rule out hardware failure

1. Run the manufacturer's built-in diagnostics (F2/F12 at boot on most brands) and execute the video/GPU test.
2. Boot from a Linux live USB — if the GPU is invisible there too, it's a hardware problem, not a Windows problem.
3. If the GPU is confirmed dead on an older laptop, an external GPU enclosure (for Thunderbolt models) or a replacement machine are the practical options. Document the diagnostics result for any warranty or repair claim.

## Closing

A missing display adapter is Windows losing track of hardware it can usually find again. Reveal hidden devices, rescan, reinstall the manufacturer's driver cleanly, and check the BIOS GPU settings — that sequence restores the adapter in nearly every software-caused case. The Microsoft Basic Display Adapter placeholder is actually encouraging: it proves the hardware is alive and just waiting for its proper driver. Only when the GPU is invisible to the BIOS, diagnostics, and a live USB should you conclude it's gone for good.
