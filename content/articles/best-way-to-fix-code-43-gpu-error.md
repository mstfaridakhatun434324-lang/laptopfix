---
title: "Code 43 GPU Error: The Best Way to Fix It on a Laptop"
slug: best-way-to-fix-code-43-gpu-error
date: 2026-09-19
categories: ["drivers"]
tags: ["code 43", "gpu error", "device manager", "nvidia", "amd"]
description: "Device Manager reports 'Windows has stopped this device (Code 43)' on your GPU? Here's the ordered fix sequence that resolves it."
thumbnail: "/images/thumbs/best-way-to-fix-code-43-gpu-error.webp"
faqs:
  - q: "What does Code 43 mean on a GPU?"
    a: "Code 43 means Windows stopped the device because it reported a problem — the GPU's driver told Windows something failed during initialization, so Windows halted the device to protect the system. It's a generic flag, not a specific diagnosis: the underlying cause ranges from driver corruption (most common) through power and thermal issues to actual hardware failure (least common but real)."
  - q: "Can a driver update cause Code 43?"
    a: "Yes — it's one of the top triggers. A new GPU driver that doesn't initialize properly on your specific card, or Windows Update installing a mismatched driver version over your manufacturer's driver, frequently produces Code 43. Rolling back the driver or clean-installing the previous known-good version resolves update-caused Code 43 in most cases."
  - q: "Is Code 43 always a hardware failure?"
    a: "No — despite what forums claim, Code 43 is a software/driver problem more often than hardware. Work the software sequence first: power-drain, driver rollback, DDU clean install, and BIOS check. Only suspect hardware after all software fixes fail, especially if the error survives a clean driver install and appears in other operating systems too."
  - q: "Why does Code 43 keep coming back after I fix it?"
    a: "Recurring Code 43 usually means Windows Update is reinstalling the problematic driver version after each of your fixes. After fixing it, hide the driver update with Microsoft's Show or hide updates troubleshooter so the bad version can't return. If it recurs without any update involved, suspect thermal or power issues — or developing hardware failure."
---

Code 43 is Windows' way of saying "this device told me it's broken, so I stopped it" — specifically, *Windows has stopped this device because it has reported problems. (Code 43)*. On a GPU it means the graphics card failed to initialize properly, and Windows halted it rather than risk a crash. Your screen still works (the integrated GPU or basic display driver takes over), but anything needing the discrete GPU doesn't.

The good news: Code 43 is a driver or power problem far more often than a dead card. The sequence that works is: power-drain the hardware, roll back or clean-install the driver, block the bad version, then check thermals and BIOS. For NVIDIA-specific crash variants, see [fixing NVIDIA driver crashes](/articles/how-to-fix-nvidia-driver-crashing/); for installer failures, [NVIDIA installer cannot continue](/articles/how-to-fix-nvidia-installer-cannot-continue-after-windows-11-update/).

## Why this happens

- **Corrupted GPU driver installation**: Layered updates or interrupted installs leave the driver unable to initialize the card.
- **Windows Update driver mismatch**: Microsoft's driver version conflicts with the installed GPU software stack.
- **GPU not getting clean power**: On laptops, a weak/failing power brick or battery issue can starve the discrete GPU at initialization.
- **Overheating at boot**: A dust-choked GPU cooler causes initialization-time thermal faults.
- **BIOS/firmware issue**: GPU-related BIOS bugs, or a BIOS update that changed power/PCIe behavior.
- **Loose GPU (desktop MXM, rare on laptops)**: Mostly a desktop concern; laptop GPUs are soldered, but eGPU connections can cause it.
- **Actual GPU hardware failure**: Failed VRAM, power phases, or the GPU die itself — the last resort diagnosis.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Power-drain and cold boot

Clear the hardware state before touching software.

1. Shut the laptop down completely, unplug the AC adapter, and disconnect all peripherals (especially eGPUs, docks, and external monitors).
2. Hold the power button for 30 seconds to drain residual power.
3. Reconnect only the original AC adapter — not a third-party charger — and power on.
4. Open **Device Manager** > **Display adapters** and check whether the Code 43 is gone. Power-state glitches cause a surprising share of Code 43 reports.
5. If you use an eGPU, reconnect it only after the internal GPU is clean, and test with the eGPU disconnected first to isolate.

### Fix 2: Roll back the GPU driver

Fastest fix when the timeline matches an update.

1. In **Device Manager** > **Display adapters**, right-click the flagged GPU > **Properties** > **Driver** tab.
2. Click **Roll Back Driver** if available, select a reason, and restart.
3. Check whether Code 43 clears. If it does, the update was the cause — proceed to Fix 4 to block it permanently.
4. If rollback is greyed out, note the current driver version and date for comparison in the next fix.
5. Also check **Settings** > **Windows Update** > **Update history** to confirm a driver update coincides with the error's appearance.

### Fix 3: DDU clean install of the GPU driver

The definitive driver repair when rollback isn't available or doesn't stick.

1. Download **Display Driver Uninstaller (DDU)** plus the driver: NVIDIA users get it from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx); AMD users from [AMD's driver page](https://www.amd.com/en/support/download/drivers.html). Pick the last version that worked, or one version older than the crashing one.
2. Disconnect from the internet, boot into **Safe Mode** (**Settings** > **System** > **Recovery** > **Advanced startup**).
3. Run DDU: select your GPU brand, **Clean and restart**.
4. After restart (still offline), run the manufacturer's installer with **Custom** > **clean installation** checked.
5. Reconnect to the internet and verify in Device Manager that Code 43 is gone and the driver version is the one you installed.

### Fix 4: Block the bad driver version permanently

Stop Windows Update from re-breaking it.

1. Download the **Show or hide updates** troubleshooter and hide the GPU driver update that caused Code 43.
2. In **System Properties** (**sysdm.cpl**) > **Hardware** > **Device Installation Settings**, select **No** to stop automatic manufacturer driver installs generally.
3. Verify the driver version in Device Manager survives a Windows Update cycle.
4. Revisit only when you deliberately want a newer GPU driver — install it manually via DDU-clean procedure.
5. Document which version works (a sticky note in the laptop bag is low-tech and effective) so future-you doesn't "update" into the problem again.

### Fix 5: Address thermals and power delivery

Code 43 at initialization is sometimes the GPU failing its own power-on self-check due to heat or power.

1. Clean the vents and fans with compressed air — short bursts into the exhaust, can upright.
2. Always use the original power brick, plugged directly into the wall (not a power strip shared with heavy loads) for testing.
3. Remove the battery if it's removable, and test on AC alone — a failing battery can drag down the power rail the GPU needs.
4. Check GPU temperature at idle with HWMonitor — idle temps above 65–70°C suggest the cooler isn't making contact or is fully clogged.
5. If Code 43 appears only when hot (after gaming) but not on cold boot, thermals are the cause — repaste if the machine is old, and stop using it on soft surfaces.

### Fix 6: Update or reset the BIOS

Firmware-level GPU initialization issues.

1. Check your manufacturer's support page for BIOS release notes mentioning GPU, display, or PCIe fixes — [Dell's support page](https://www.dell.com/support) (or HP's or Lenovo's).
2. If a newer BIOS addresses GPU issues, update following the manufacturer's instructions exactly: plugged in, battery charged, no interruptions.
3. If Code 43 *started* with a BIOS update, check whether the manufacturer offers a BIOS rollback — some do, some don't.
4. In BIOS, use **Load Optimized Defaults** to clear any scrambled PCIe/power settings.
5. After any BIOS change, cold-boot (full shutdown, not restart) and recheck Device Manager.

### Fix 7: Confirm hardware failure properly

Only after everything software has failed.

1. Boot a Linux live USB (Ubuntu) and check whether the GPU initializes there (`lspci` should list it without errors). Failing in both OSes = hardware.
2. Run a GPU stress test if the card initializes at all — artifacts (blocks, lines, wrong colors) during the test confirm VRAM/GPU failure.
3. On laptops with hybrid graphics, force everything to the integrated GPU in Windows graphics settings — if the system is fully stable without the discrete GPU, the discrete GPU or its power circuit is the problem.
4. Check Event Viewer for Code 43 paired with **WHEA** hardware errors — that combination is the strongest software-visible signal of real hardware failure.
5. Laptop GPU repair is motherboard-level work — get a repair quote, and weigh it against the machine's age and value. A USB-free workaround doesn't exist for a dead internal GPU, but integrated graphics keep the laptop usable for non-GPU tasks.

## Closing

Code 43 looks scary because Windows "stopped" your hardware, but it's usually Windows protecting you from a bad driver rather than reporting a dead card. Power-drain, roll back, DDU-clean, block the bad version — that sequence resolves the large majority. Reserve the hardware verdict for Code 43 that survives a clean driver install in two operating systems.
