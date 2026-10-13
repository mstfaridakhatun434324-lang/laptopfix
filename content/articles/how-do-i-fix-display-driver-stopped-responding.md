---
title: "How Do I Fix 'Display Driver Stopped Responding'?"
slug: how-do-i-fix-display-driver-stopped-responding
date: 2026-09-25
categories: ["drivers"]
tags: ["display driver", "driver stopped responding", "gpu crash", "tdr error", "nvlddmkm"]
description: "\"Display driver stopped responding and has recovered\"? Fix GPU TDR crashes with clean driver installs, TDR tweaks, and overheating checks."
thumbnail: "/images/thumbs/how-do-i-fix-display-driver-stopped-responding.webp"
faqs:
  - q: "What does 'display driver stopped responding' mean?"
    a: "It means Windows' Timeout Detection and Recovery system caught your GPU taking too long to respond and reset the driver instead of blue-screening. The screen flickers black for a few seconds, then recovers. It is Windows protecting you from a full crash, but repeated TDR events signal a driver, overheating, or hardware problem that needs fixing."
  - q: "Is a TDR error caused by a bad graphics card?"
    a: "Not necessarily. Most TDR errors are driver bugs, corrupted driver installs, or overheating — all fixable. Hardware failure is the diagnosis only after clean driver installs, temperature control, and stock clocks fail to stop the crashes. Test with the GPU at factory settings before suspecting the card itself."
  - q: "Can overclocking cause the display driver to stop responding?"
    a: "Yes, overclocking is one of the top triggers. Even factory overclocks on some cards can be marginally unstable in specific games. Reset the GPU to stock clocks with MSI Afterburner or the manufacturer's tool and retest. If crashes stop at stock, your overclock was the cause — dial it back or leave it at stock."
  - q: "Will increasing the TDR delay fix the crashes?"
    a: "Increasing the TdrDelay registry value gives the GPU more time before Windows resets it, which stops the error message but doesn't fix the underlying stall. Use it as a diagnostic step and a workaround for borderline cases, not as a permanent fix. The real fix is the driver, temperature, or stability issue making the GPU stall."
---

"Display driver stopped responding and has recovered" is Windows telling you it just saved you from a blue screen. The Timeout Detection and Recovery (TDR) system watches your GPU, and when the driver hangs for more than a couple of seconds, Windows resets it — your screen goes black briefly, then comes back. One occurrence is a fluke. Repeated TDRs are a problem demanding attention.

The causes stack up in a familiar order: bad driver installs, overheating, unstable clocks, and finally hardware. Work them in that order and you'll resolve the vast majority without touching the registry — though the TDR delay tweak is there when you need it.

## Why this happens

- **Corrupted graphics driver:** The most common cause — a bad install, a conflicting update, or driver files damaged by a crash loop.
- **GPU overheating:** Heat makes the GPU unstable; the driver hangs, TDR fires, and the cycle repeats under load.
- **Unstable overclock:** Core, memory, or factory overclocks that are marginally stable will trip TDR in demanding scenes.
- **Insufficient or failing power:** A struggling power supply or aggressive power-saving can starve the GPU mid-render, stalling the driver.
- **TDR timeout too aggressive:** The default 2-second timeout can fire on legitimate heavy workloads, especially with complex scenes or compute tasks.
- **Conflicting background software:** Overlays, recording tools, and "optimization" utilities hooking the graphics pipeline can destabilize the driver.
- **Windows update driver mismatch:** Updates installing a generic GPU driver over the tuned manufacturer version is a classic TDR trigger.
- **Failing GPU hardware:** Degrading VRAM or a dying GPU core produces TDRs that survive every software fix — the last-resort diagnosis.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do a clean reinstall of the graphics driver

1. Download the latest driver for your GPU: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html). For laptops, check the manufacturer's page first for a validated build.
2. During NVIDIA installation, choose **Custom → Perform a clean installation**. For AMD, use the **Factory Reset** option.
3. For a deeper clean, boot into Safe Mode and run Display Driver Uninstaller (DDU) to purge all traces, then install fresh.
4. Restart and stress-test with the game or app that triggered the TDRs.
5. A proper clean install — not an over-the-top update — resolves the largest share of TDR cases because it eliminates the corrupted files and conflicting remnants that cause hangs. The [dedicated TDR troubleshooting guide](/articles/troubleshoot-display-driver-stopped-responding/) covers the deep-dive version of this process.

### Fix 2: Check GPU temperatures under load

1. Install HWiNFO64 or HWMonitor and log GPU temperature while reproducing the crash.
2. Sustained temperatures above **85–90°C** on most GPUs invite instability; thermal throttling plus TDR together strongly suggest heat.
3. Clean dust from vents and fans with compressed air, and ensure the laptop sits on a hard flat surface.
4. Elevate the rear of the laptop or use a cooling pad — even a 5°C drop can end TDRs on thermally marginal machines.
5. If the laptop is several years old and runs hot at idle, dried thermal paste is likely — a repaste by a competent shop restores thermal headroom. Heat-related instability also affects [general driver crashes](/articles/best-way-to-fix-display-driver-stopped-responding/).

### Fix 3: Reset to stock clocks

1. Open MSI Afterburner or your GPU vendor's tool and reset all overclock settings to stock (the reset button or a fresh profile).
2. If you never overclocked manually, check whether the card runs a factory overclock and consider a slight **underclock** (-50 MHz core) as a stability test.
3. Disable any "OC mode" or "Turbo" toggle in the laptop's control software (Armoury Crate, Legion Zone, etc.).
4. Retest the crashing workload. Stability at stock clocks proves the overclock was the trigger.
5. Leave clocks at stock unless you enjoy re-tuning — marginal overclocks cause exactly this intermittent TDR pattern.

### Fix 4: Increase the TDR delay

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a new **QWORD (64-bit) Value** named `TdrDelay` and set it to **8** (decimal) — up from the default 2 seconds.
3. Optionally create `TdrDdiDelay` set to **10** as well.
4. Restart and test. The longer delay lets the GPU finish heavy work instead of being reset mid-render.
5. Treat this as a workaround, not a cure — if TDRs continue even at 8 seconds, the GPU is genuinely hanging and needs the driver/heat/hardware fixes. Back up the registry key before editing.

### Fix 5: Set maximum performance power settings

1. Open **NVIDIA Control Panel → Manage 3D settings → Power management mode** and set it to **Prefer maximum performance** (NVIDIA), or the AMD equivalent in Adrenalin.
2. In **Windows Power Options → Advanced**, set **PCI Express → Link State Power Management** to **Off**.
3. Set the Windows power mode to **Best performance** while testing.
4. Unstable power-state transitions — the GPU ramping up and down — are a known TDR trigger, and locking performance states eliminates that variable.
5. If crashes stop on maximum performance, your GPU's power management is implicated; keep the setting or investigate firmware updates.

### Fix 6: Disable overlays and background hooks

1. Turn off the Steam overlay, Discord overlay, GeForce Experience overlay, and Xbox Game Bar capture for the crashing game.
2. Close recording software (OBS, etc.) during testing — reintroduce one at a time afterward.
3. Uninstall "game booster" and "system optimizer" utilities; they hook the graphics pipeline and cause exactly these hangs.
4. Test the workload clean. Overlays injecting into the render path are a frequent hidden cause of driver hangs.
5. Re-enable overlays individually after stability returns to identify the offender.

### Fix 7: Test with a different driver version

1. If TDRs started with a specific driver update, the new driver itself may be buggy for your GPU.
2. Use DDU in Safe Mode to remove the current driver, then install the previous known-good version from the vendor's archive.
3. For NVIDIA, the Studio driver (vs. Game Ready) is sometimes more stable on laptops.
4. Block automatic driver updates temporarily so Windows doesn't "helpfully" reinstall the problematic version.
5. Report the regression to the vendor — driver bugs affecting popular GPUs do get fixed when reported with details.

### Fix 8: Stress-test to isolate hardware failure

1. Run a GPU stress test (FurMark or 3DMark) while monitoring temperatures and watching for TDRs or artifacts.
2. Run a VRAM test (OCCT's VRAM test) — VRAM faults cause TDR-pattern crashes that look like driver issues.
3. If crashes occur in Safe Mode, in Linux, and across multiple driver versions, the GPU hardware is failing.
4. On laptops, GPU failure usually means motherboard-level repair or replacement — get a professional diagnosis before spending money.
5. As a last software resort, a clean Windows reinstall eliminates any OS-level corruption — but only pursue this after hardware testing, since reinstalling Windows won't fix a dying GPU.

## Closing

TDR errors are Windows doing its job — catching a hung GPU before it takes the system down. Your job is to find why the GPU hangs: usually a corrupted driver (clean install), heat (cooling), or clocks (stock settings). The registry delay buys headroom but doesn't fix root causes. When TDRs survive clean drivers, cool temperatures, and stock clocks across operating systems, the hardware verdict is earned.
