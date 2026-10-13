---
title: "Troubleshooting a Missing Display Adapter — GPU Vanished"
slug: display-adapter-missing-troubleshooting
date: 2026-10-12
categories: ["drivers"]
tags: ["display adapter missing", "gpu disappeared", "code 45", "device manager", "troubleshooting"]
description: "GPU vanished from Device Manager? Troubleshoot a missing display adapter with error-code diagnosis, from Code 43 and 45 to BIOS and hardware checks."
thumbnail: "/images/thumbs/display-adapter-missing-troubleshooting.webp"
faqs:
  - q: "What does Code 45 mean for a display adapter?"
    a: "Code 45 means 'currently, this hardware device is not connected to the computer.' For a laptop GPU, which is soldered and cannot physically disconnect, this indicates a PCIe enumeration failure — Windows tried to talk to the GPU and got no response. Common triggers are power-state bugs after sleep, corrupted chipset drivers, or a GPU stuck in a low-power state. The fix path is power-cycling the hardware state, updating chipset drivers, and reinstalling the graphics driver, in that order."
  - q: "What does Code 43 mean for a GPU?"
    a: "Code 43 means 'Windows has stopped this device because it has reported problems.' Unlike Code 45, the hardware is detected but the driver failed to start it — usually because the driver is corrupted, mismatched, or crashed during initialization. The standard fix is a clean driver reinstall with Display Driver Uninstaller. Code 43 after a driver update that previously worked often means the new driver is incompatible; rolling back to the previous version resolves it immediately."
  - q: "Why does my GPU disappear only after sleep?"
    a: "Sleep-specific disappearance is a power-state bug: the GPU fails to reinitialize when the system wakes. The usual culprits are outdated chipset drivers, buggy GPU drivers, or Windows Fast Startup preserving the broken state. Updating the chipset driver from the manufacturer is the most reliable long-term fix. As an immediate workaround, disabling Fast Startup and doing full shutdowns instead of sleep prevents the failure mode while you sort the drivers."
  - q: "How can I tell if my GPU is dead or just hidden?"
    a: "Check Device Manager with hidden devices shown: a present-but-grayed device means Windows knows the hardware exists, which rules out total hardware death. Boot a Linux live USB and check whether the GPU appears there — visible in Linux means the hardware works and Windows is the problem. The manufacturer's boot-time hardware diagnostics can also test the GPU directly. Only when the GPU is invisible everywhere, including Linux and diagnostics, should you suspect actual hardware failure."
---

A missing display adapter demands a different approach than most driver problems: you have to diagnose before you treat.

Think of it as triage. By the end of the first three sections, you will know whether you are dealing with a disabled device, a driver failure, an enumeration problem, or a firmware setting — and each diagnosis maps to a specific fix.

## Why this happens

- **Driver failure hiding the device (Code 43):** The GPU is detected but its driver crashed on load. Windows stops the device and hides it from the default view.
- **PCIe enumeration failure (Code 45):** Windows cannot communicate with the GPU at the bus level — a power-state or chipset problem rather than a graphics-driver problem.
- **Device disabled in software:** The adapter was disabled in Device Manager or by a tuning utility. It exists but is invisible in the normal view.
- **Firmware switched the GPU off:** BIOS settings (MUX, hybrid graphics, dGPU disable) or a BIOS update removed the GPU from the hardware Windows can see.
- **Windows Update driver mismatch:** An update installed an incompatible graphics driver, which fails initialization and triggers Code 43 on every boot.
- **Stuck low-power state:** Modern GPUs power-gate aggressively. A GPU stuck in a deep sleep state does not respond to enumeration — functionally identical to a disconnected device.
- **Corrupted driver store:** Partially installed or conflicting driver files from multiple install attempts create a state where no driver can load successfully.
- **Hardware failure:** Failed GPU silicon or broken solder joints. Genuinely the least common cause, diagnosed only by exclusion.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the hidden-device evidence

Your first job is gathering data, not fixing anything.

1. Open **Device Manager → View → Show hidden devices** and expand **Display adapters**. Document exactly what you see: nothing, a grayed-out GPU, or a GPU with a warning icon.
2. For a warning icon, open **Properties → General** and record the exact **Device status** code and message.
3. Check the **Events** tab in Properties — it logs driver load attempts with timestamps, showing whether the failure is consistent or intermittent.
4. Check **View → Devices by connection** and trace the GPU's PCIe path. A GPU missing from the PCIe tree points to enumeration (Fix 4); a GPU present but errored points to the driver (Fix 3).

### Fix 2: Diagnose the disabled-device case

The simplest diagnosis — and the most satisfying fix.

1. If the GPU appears grayed out in hidden view, right-click → **Properties → General** and check the status message. "Disabled" is explicit.
2. Right-click → **Enable device**, then restart. If it stays enabled and works, check what disabled it: recent utility installs, Windows updates, or accidental clicks in Device Manager.
3. If it re-disables itself after every restart, a startup program or driver policy is doing it. Check **Task Manager → Startup** for GPU utilities and the manufacturer's control software settings.
4. Some laptops disable the dGPU when on battery via power profiles — test plugged in versus on battery to catch this pattern.

### Fix 3: Diagnose and fix the Code 43 driver failure

Code 43 means the hardware is there but the driver cannot start it.

1. Confirm the timeline: did Code 43 appear right after a driver update or Windows update? If yes, the new driver is the prime suspect.
2. First try **Driver → Roll Back Driver** in the GPU's properties. If the previous driver loads successfully, you have confirmed a bad update — then block it from reinstalling.
3. If rollback is unavailable, perform a clean reinstall: download the manufacturer's graphics driver, run **Display Driver Uninstaller (DDU)** in Safe Mode, restart, and install the fresh driver.
4. Check **Event Viewer → Windows Logs → System** for `nvlddmkm` or `amdkmdap` errors around boot time. Repeated TDR (Timeout Detection and Recovery) errors before the Code 43 suggest the driver crashes during initialization — sometimes fixed by a slightly older driver version rather than the newest. General driver troubleshooting principles are in our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/).

### Fix 4: Diagnose and fix the Code 45 enumeration failure

Code 45 is a bus-level problem — the graphics driver is not even in play yet.

1. Confirm the pattern: does the GPU vanish specifically after sleep/hibernate, or is it gone from a cold boot too? Sleep-only disappearance is a power-state bug; cold-boot absence is more serious.
2. Do a true power cycle: full shutdown, unplug the charger, hold power 30 seconds, reboot. This resets the PCIe bus and GPU power states.
3. Update the **chipset driver** from the laptop manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). The chipset driver owns PCIe enumeration, and this is the highest-success fix for Code 45.
4. Disable **Fast Startup** and test sleep/wake cycles. If the GPU survives with Fast Startup off, you have both a diagnosis and a workaround while pursuing driver updates.

### Fix 5: Rule out firmware-level causes

When the GPU is invisible even in hidden devices and in the PCIe tree, look below the OS.

1. Enter BIOS/UEFI setup and find graphics settings. Look for **Discrete GPU**, **dGPU**, **MUX**, **Hybrid Graphics**, or **Switchable Graphics** options and make sure the discrete GPU is enabled.
2. If a BIOS update preceded the disappearance, check the manufacturer's site for a newer BIOS — early releases sometimes break GPU enumeration, and the fix is literally the next BIOS version.
3. **Load Optimized Defaults** in BIOS, then reconfigure. Corrupted BIOS settings from a failed update can hide devices in ways that look exactly like hardware failure.
4. Check whether the manufacturer's control software (Lenovo Legion Toolkit, ASUS Armoury Crate, Dell Alienware Command Center) has a GPU mode setting — these can switch the dGPU off at a level Windows cannot override. For the ordered recovery sequence once diagnosis is done, see our [missing display adapter repair guide](/articles/best-way-to-fix-display-adapter-missing/).

### Fix 6: Clean the driver store of conflicting remnants

For cases where multiple install attempts have left the driver state tangled.

1. Run DDU in Safe Mode as in Fix 3, but this time also use its option to remove **GeForce Experience** / **AMD Software** remnants if present.
2. After DDU, before installing anything, check Device Manager: the GPU should appear as **Microsoft Basic Display Adapter** or under **Other devices**. If it does not appear at all, return to Fix 4 and 5 — the problem is enumeration, not the driver store.
3. Install only the manufacturer's graphics driver — not the NVIDIA/AMD generic package, not a Windows Update driver. One clean, correct driver.
4. Verify stability over several days including sleep cycles before declaring victory. Intermittent reappearance means the root cause (usually chipset/power) is still lurking.

### Fix 7: Confirm or rule out hardware failure

The diagnosis of exclusion — only valid after the software steps.

1. Boot a Linux live USB and run `lspci | grep -i vga`. GPU visible in Linux but not Windows is definitive proof of a Windows-side problem — do not let a repair shop tell you the GPU is dead.
2. Run the manufacturer's boot-time diagnostics (Dell ePSA, Lenovo UEFI diagnostics, HP PC Hardware Diagnostics) and execute the video tests specifically.
3. Look for the hardware-failure pattern: artifacting, crashes under 3D load, or the GPU disappearing when hot and reappearing when cold. Thermal-dependent behavior is the hallmark of failing solder joints.
4. If hardware failure is confirmed on a laptop, weigh board-level repair cost against the machine's value — and remember the integrated GPU still runs the laptop fine for non-gaming use, with USB-C docks covering external displays.

## Closing

Troubleshooting a missing display adapter is an exercise in reading evidence: hidden-device status, error codes, timing patterns, and cross-OS visibility each narrow the field. Most cases resolve to a disabled device, a bad driver update, or a chipset enumeration bug — all fixable in software. The diagnostic discipline matters because it stops you from reinstalling drivers for a firmware problem or mourning a GPU that is merely asleep.
