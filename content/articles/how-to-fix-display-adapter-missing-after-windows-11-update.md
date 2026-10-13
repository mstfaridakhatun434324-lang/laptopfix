---
title: "Display Adapter Missing After a Windows 11 Update? Recover the GPU"
slug: how-to-fix-display-adapter-missing-after-windows-11-update
date: 2026-09-23
categories: ["drivers"]
tags: ["display adapter", "gpu missing", "windows 11 update", "device manager"]
description: "Fix a missing display adapter after a Windows 11 update: reveal hidden GPUs in Device Manager, reinstall graphics drivers, and fix BIOS detection issues."
thumbnail: "/images/thumbs/how-to-fix-display-adapter-missing-after-windows-11-update.webp"
faqs:
  - q: "Why did my NVIDIA or AMD GPU disappear after a Windows 11 update?"
    a: "The update's driver migration can complete with a graphics driver the GPU cannot start, so Windows hides the adapter instead of showing a broken one. In other cases the update disables the discrete GPU's driver while leaving the integrated graphics running, which looks like the dedicated GPU vanished. A clean driver reinstall restores it."
  - q: "What is the difference between a missing and a disabled display adapter?"
    a: "A disabled adapter appears in Device Manager grayed out and can be re-enabled with a right-click. A missing adapter does not appear at all — even the category may be absent — which means Windows cannot enumerate the hardware, pointing to driver, BIOS, or firmware causes. Check with hidden devices shown before deciding which case you have."
  - q: "Can a Windows update physically damage my GPU?"
    a: "No. Updates cannot damage the silicon. What they can do is leave the driver stack in a state where the GPU will not initialize, which looks identical to hardware death from the user's perspective. The BIOS-level tests in this guide distinguish the two definitively."
  - q: "Why does my laptop work fine on integrated graphics but the NVIDIA GPU is gone?"
    a: "The integrated GPU has a simpler driver path that usually survives updates intact, while the discrete GPU's more complex driver is what breaks. This is actually good news: it means Windows is healthy and only the discrete GPU's driver stack needs repair, which the steps below address."
---

A Windows 11 update finishes, the laptop reboots, and something is subtly wrong: games stutter, the NVIDIA Control Panel is gone, and Device Manager shows only the Intel or AMD integrated graphics where two adapters used to be. The discrete GPU has vanished — not error-flagged, not disabled, just absent. The laptop still works because the integrated graphics carry the display, which makes the problem easy to misread as a performance quirk rather than a missing device.

This disappearance is almost always a driver migration failure. Windows updates replace the graphics driver during installation, and if the new driver cannot initialize the discrete GPU, Windows hides the adapter rather than displaying a broken one. Less commonly, the update exposes a BIOS setting change or a firmware sequencing issue that prevents the GPU from enumerating at boot.

Recovery follows a clear order: reveal what Windows can see, force re-enumeration, reinstall the graphics driver cleanly, check the BIOS-level GPU settings, and verify with hardware tests. Genuine GPU death is possible but uncommon — rule out everything else first.

## Why this happens

- **Failed graphics driver migration:** The update installs a GPU driver that cannot initialize the discrete card. Windows responds by hiding the adapter instead of showing it with an error.
- **Discrete GPU driver disabled during migration:** The migration can leave the discrete GPU's driver in a disabled state while integrated graphics take over silently.
- **Driver store corruption:** A half-written driver package poisons automatic reinstalls — every attempt pulls the same broken files until the package is deleted.
- **BIOS GPU mode changed:** Some updates flip BIOS graphics settings between switchable, discrete, and integrated modes, hiding the dGPU from the OS.
- **Fast startup caching a bad device state:** Fast startup hibernates the kernel device state. A bad GPU state gets faithfully restored on every boot until fast startup is disabled and a full shutdown clears it.
- **Chipset driver mismatch:** The discrete GPU enumerates through the PCIe bus managed by the chipset driver. An outdated chipset driver can fail to present the GPU to Windows after an OS update.
- **Actual GPU hardware failure:** The least common cause, but real: a GPU that never appears in the BIOS, in any OS, or after driver repair has likely failed physically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and check the true state

Start by seeing what Windows actually knows. A grayed-out adapter is a very different problem from a truly absent one.

1. Open Device Manager, click View, then Show hidden devices.
1. Expand Display adapters and look for grayed-out NVIDIA, AMD, or Intel discrete entries.
1. A grayed entry means re-enable or reinstall the driver; a completely absent entry means working through the steps below.

### Fix 2: Disable fast startup and cold boot

Fast startup can preserve a broken GPU device state across reboots indefinitely. A true cold boot clears it.

1. Open Control Panel, then Power Options, then Choose what the power buttons do.
1. Click Change settings that are currently unavailable and uncheck Turn on fast startup.
1. Shut down fully, wait thirty seconds, and power on. Check Device Manager for the adapter's return.

### Fix 3: Scan for hardware changes and re-enable

Force Windows to re-enumerate the PCIe bus. This catches GPUs that are present but were skipped during a hurried boot.

1. In Device Manager, click Action, then Scan for hardware changes.
1. If the adapter appears grayed out, right-click and choose Enable device.
1. If it appears with a warning, note the error code — Code 43 points squarely at the driver reinstall next.

### Fix 4: Clean-reinstall the graphics driver

This is the definitive fix for migration-broken GPU drivers. Remove the broken package completely so it cannot be resurrected.

1. Download the newest driver for your GPU from NVIDIA, AMD, or Intel — [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) and [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) cover discrete cards, Intel's DSA the integrated ones.
1. In Device Manager, uninstall the display adapter (or the unknown device standing in for it), checking Delete the driver software.
1. Install the downloaded driver and restart. Verify both adapters appear in Device Manager. If the GPU appears but then crashes under load, the [NVIDIA crashing-driver guide](/articles/nvidia-driver-keeps-crashing-windows-11/) picks up from there.

### Fix 5: Update the chipset driver

The GPU reaches Windows through the chipset's PCIe implementation. An outdated chipset driver after an OS update can silently drop the discrete GPU from enumeration.

1. Download the chipset driver for your exact laptop model from the vendor's support site.
1. Install it and restart, then rescan for hardware changes in Device Manager.
1. This step disproportionately helps AMD-based laptops, where the chipset driver owns more of the PCIe bring-up.

### Fix 6: Check BIOS graphics settings

Look below the OS for firmware-level GPU configuration that an update may have altered.

1. Enter the BIOS and find graphics, display, or video settings.
1. If there is a switchable/discrete/integrated selector, set it to Switchable or Discrete — not Integrated only.
1. Save, exit, and check Device Manager after booting. If the GPU flickers or shows artifacts rather than vanishing, the [display driver crash guide](/articles/how-to-fix-display-driver-stopped-responding-after-windows-11-update/) addresses that adjacent failure.

### Fix 7: Verify at the hardware level

If the GPU still will not appear, determine whether the hardware itself is visible to the firmware.

1. Check the BIOS system information page for any mention of the discrete GPU.
1. Boot a live Linux USB and check whether the GPU enumerates there.
1. A GPU invisible in the BIOS and in Linux after all driver repairs points to hardware failure and a service visit. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the built-in hardware troubleshooters as a final software check.

## Closing

A display adapter that vanishes after a Windows 11 update is a driver migration casualty in the great majority of cases — the GPU is still on the board, waiting for a driver that can initialize it. Reveal hidden devices, cold-boot past fast startup's cached state, and reinstall the graphics and chipset drivers cleanly. Only when the firmware itself cannot see the card is it time to talk about hardware.
