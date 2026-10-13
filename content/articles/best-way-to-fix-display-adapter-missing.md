---
title: "The Best Way to Fix a Missing Display Adapter in Device Manager"
slug: best-way-to-fix-display-adapter-missing
date: 2026-10-10
categories: ["drivers"]
tags: ["display adapter missing", "gpu not detected", "device manager", "graphics driver", "code 45"]
description: "Display adapter missing from Device Manager? Recover a vanished GPU with the correct sequence — from hidden devices to BIOS checks to clean driver installs."
thumbnail: "/images/thumbs/best-way-to-fix-display-adapter-missing.webp"
faqs:
  - q: "Why did my NVIDIA or AMD GPU disappear from Device Manager?"
    a: "The most common reason is a failed driver update that left the GPU in an error state, causing Windows to hide it or list it under hidden devices. The second most common is the GPU being disabled — in Device Manager, in BIOS, or by the laptop's MUX/power management. Actual GPU hardware death is rare on laptops; in the vast majority of cases the chip is fine and the problem is driver or configuration state."
  - q: "Should I be worried if only the Microsoft Basic Display Adapter shows?"
    a: "Not immediately. Microsoft Basic Display Adapter is Windows' fallback when no proper GPU driver is loaded — it means Windows sees display hardware but has no driver for it. This is actually good news: the GPU is physically detected. Installing the correct driver from the manufacturer or from NVIDIA/AMD will replace the fallback entry with the real adapter. Worry only if no display adapter of any kind appears, even after showing hidden devices."
  - q: "Can a BIOS update make the display adapter disappear?"
    a: "Yes. BIOS updates can reset graphics settings — switching from discrete to integrated graphics, disabling the dGPU, or changing PCIe enumeration — which makes the adapter vanish from Windows. If the disappearance followed a BIOS update, enter setup and check the graphics configuration first. Some updates also require a matching driver update afterward. When in doubt, reinstall the graphics driver after any BIOS update that touches display settings."
  - q: "Is DDU safe to use on a laptop?"
    a: "Yes, Display Driver Uninstaller is safe on laptops when used correctly — it is the standard tool technicians use for corrupted graphics drivers. Run it from Safe Mode, choose the GPU manufacturer, and use the 'Clean and restart' option. The main caution on laptops is to reinstall the manufacturer's graphics driver afterward rather than the generic NVIDIA/AMD package, because laptop GPUs often need OEM customizations for power management and MUX switching to work properly."
---

Opening Device Manager to find the Display adapters section empty — or containing only "Microsoft Basic Display Adapter" where your NVIDIA or AMD GPU used to be — is alarming. Games will not launch, external monitors misbehave, and everything feels sluggish. But a missing display adapter is usually a software state problem, not a dead GPU. The chip is almost certainly still on the board; Windows has just lost track of it.

The best way to fix it follows a strict order: reveal hidden devices, check for disabled states, clean out the corrupted driver, and reinstall the correct one. Each step is quick, and the sequence matters — jumping straight to driver reinstalls without checking the earlier steps is why many people fix this three times.

## Why this happens

- **Failed graphics driver update:** An interrupted or incompatible driver install leaves the GPU in an error state. Windows hides errored devices from the default Device Manager view.
- **GPU disabled in Device Manager:** Accidentally or by a utility, the adapter gets disabled. Disabled devices vanish from the normal view but remain present.
- **BIOS graphics settings changed:** A BIOS update or settings change can disable the discrete GPU or switch the laptop to integrated-only mode, hiding the dGPU from Windows entirely.
- **Driver corruption after Windows update:** Major Windows updates can invalidate the installed graphics driver, leaving the adapter undetectable until the driver is reinstalled.
- **PCIe enumeration failure:** The GPU is a PCIe device. Power-state bugs — especially around sleep and hibernation — can cause enumeration to fail, producing Code 45 "device not connected" errors.
- **Laptop MUX/power management conflict:** MUX switches and OEM power utilities manage which GPU is active. A stuck state can hide the discrete GPU from the OS.
- **Windows installed the wrong driver:** Occasionally Windows Update installs a desktop GPU driver on a laptop GPU (or vice versa), which fails to initialize and hides the adapter.
- **Actual hardware failure:** The least common cause — a dead GPU or failed solder joint. Suspect this only after every software avenue is exhausted.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden and disabled devices

Half of all "missing adapter" cases end right here.

1. Open **Device Manager**, click **View → Show hidden devices**, and expand **Display adapters** again.
2. If the GPU appears grayed out, right-click it and choose **Enable device**. Restart and check whether it stays enabled.
3. If it appears with a yellow warning icon, note the error code: **Code 43** means the driver failed, **Code 45** means Windows thinks the hardware is disconnected.
4. If the adapter is truly absent even as hidden, continue — the problem is deeper than a disabled device. Our diagnostic-focused companion guide on [missing display adapters](/articles/display-adapter-missing-troubleshooting/) covers error-code interpretation in depth.

### Fix 2: Check BIOS graphics settings

Firmware-level settings override everything Windows tries to do.

1. Restart and enter BIOS/UEFI setup (usually **F2** or **Del**).
2. Look for graphics options: **Graphics Device**, **Display Mode**, **Hybrid Graphics**, or **MUX switch** settings. Ensure the discrete GPU is enabled — options like "Integrated only" or "iGPU mode" hide the dGPU from Windows by design.
3. If you recently updated the BIOS, choose **Load Optimized Defaults**, then reconfigure the graphics setting the way you want it.
4. Save, exit, and check Device Manager again. A GPU that reappears after a BIOS change was never broken — it was just switched off at the firmware level.

### Fix 3: Scan for hardware changes and reset the PCIe bus

For Code 45 and enumeration failures, force Windows to rediscover the hardware.

1. In Device Manager, click **Action → Scan for hardware changes**. Watch the Display adapters section during the scan.
2. If the GPU appears briefly then vanishes, or appears with Code 45, do a full power cycle: shut down completely, unplug the charger, hold the power button 30 seconds, then boot.
3. Disable **Fast Startup** (**Control Panel → Power Options → Choose what the power buttons do**) — it preserves hardware state across shutdowns, which preserves enumeration failures too.
4. Test sleep/wake behavior afterward. If the GPU vanishes specifically after sleep, the problem is a power-state bug, and the chipset driver update in Fix 6 is the long-term cure.

### Fix 4: Clean the graphics driver with DDU

Corrupted driver state is the most common deep cause. Display Driver Uninstaller removes what normal uninstalls leave behind.

1. Download **Display Driver Uninstaller (DDU)** and the correct graphics driver for your exact laptop model from the manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. Boot into **Safe Mode** (**Settings → Recovery → Advanced startup → Startup Settings**).
3. Run DDU, select your GPU manufacturer (NVIDIA/AMD/Intel), and choose **Clean and restart**. Do not use the shutdown option — you want the immediate restart.
4. After reboot, install the downloaded manufacturer driver before Windows Update can install its own. For discrete GPUs you can also use the official NVIDIA or AMD driver packages, but prefer the laptop maker's version for MUX-equipped machines.

### Fix 5: Install the chipset and management engine drivers

The GPU depends on chipset infrastructure to enumerate on the PCIe bus.

1. Download the **chipset driver** and **Intel Management Engine** (or AMD chipset) package from the laptop manufacturer's support page.
2. Install the chipset driver first, restart, then the management engine driver, restart again.
3. Check Device Manager → **System devices** for any remaining yellow warnings — unresolved chipset devices can keep the GPU hidden.
4. This step is especially important after motherboard-affecting changes: BIOS updates, Windows feature updates, or any repair work. General driver-update principles are covered in our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/).

### Fix 6: Block the driver that keeps breaking it

If the GPU vanishes after every Windows update, stop the cycle.

1. After a working driver is installed, open **Device Manager → Display adapters → GPU → Properties → Driver** and note the exact working version.
2. On Windows Pro, enable **Do not include drivers with Windows Updates** via Group Policy (**gpedit.msc → Computer Configuration → Administrative Templates → Windows Components → Windows Update → Manage updates offered from Windows Update**).
3. Alternatively, use the **Show or hide updates** troubleshooter to hide the specific graphics driver update.
4. Keep the known-good driver installer saved locally. If a future update breaks things again, DDU plus the saved installer restores you in fifteen minutes.

### Fix 7: Test for hardware failure

Only reach this step after all software avenues are exhausted.

1. Boot from a Linux live USB. If the GPU appears there (check with `lspci`), the hardware is fine and the problem is Windows-specific — revisit the driver steps.
2. Run the manufacturer's built-in hardware diagnostics (usually accessible from the boot menu, e.g., **F12** on Dell, **F2** on Lenovo) and run the video/GPU tests.
3. Check for physical symptoms: artifacting before the disappearance, crashes under load, or the GPU vanishing specifically when hot all point to hardware.
4. If hardware failure is confirmed, the options are professional board repair or an eGPU/USB-C dock workaround for external displays — the integrated GPU still handles everyday tasks fine.

## Closing

A missing display adapter is a detection problem far more often than a hardware problem. Show hidden devices, check the BIOS switch, clean the driver with DDU, and reinstall the manufacturer's package — that sequence recovers the overwhelming majority of vanished GPUs. Note which step brought it back, because that tells you exactly what to guard against next time an update comes knocking.
