---
title: "Display Driver Stopped Responding on Windows 11? Stop the Freezes"
slug: how-to-fix-display-driver-stopped-responding-on-windows-11
date: 2026-09-30
categories: ["drivers"]
tags: ["display driver", "tdr", "windows 11", "gpu crash"]
description: "Fix display driver stopped responding errors on Windows 11: end TDR crashes with clean driver reinstalls, thermal fixes, and timeout tuning."
thumbnail: "/images/thumbs/how-to-fix-display-driver-stopped-responding-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 keep restarting my display driver?"
    a: "Windows 11 uses Timeout Detection and Recovery: when the GPU stops responding within its timeout window, the OS restarts the graphics driver instead of blue-screening. Repeated restarts mean the GPU keeps hanging — most commonly from a corrupted graphics driver, overheating, or an unstable overclock. The notification is the symptom; the hang is the disease."
  - q: "Did a Windows 11 update cause my TDR crashes?"
    a: "It is a common trigger. Feature and cumulative updates migrate graphics drivers, and a bad migration produces exactly this pattern: crashes that begin within days of the update on a previously stable machine. A clean reinstall of the current vendor driver, rather than the migrated one, is the fix."
  - q: "Should I increase the TDR delay in the registry?"
    a: "As a diagnostic step, yes — raising TdrDelay gives a slow-but-healthy GPU more time before Windows declares it hung. As a permanent fix, be cautious: it masks the underlying problem. If crashes persist even with a generous timeout, the cause is heat, power, or failing hardware, and the timeout is just hiding it."
  - q: "How hot is too hot for a laptop GPU?"
    a: "Sustained temperatures above 90C under load deserve attention, and anything approaching 100C is actively causing instability on most laptop GPUs. Brief spikes are normal; a GPU that lives at high temperatures during ordinary gaming needs better cooling — cleaned vents, a cooling pad, or a professional repaste on older machines."
---

On Windows 11 the TDR crash has a familiar choreography: the screen freezes mid-game or mid-scroll, everything goes black for a few seconds, and the desktop returns with a notification that the display driver stopped responding and has recovered. Windows restarted your graphics driver to dodge a blue screen. When it happens once a month, it is a hiccup. When it happens daily, something is wrong with the driver, the thermals, or the hardware — and the notification will keep coming until the cause is fixed.

Windows 11 adds its own flavor to this classic failure. Feature updates migrate graphics drivers behind the scenes, and a bad migration is the most common birthday of a new TDR problem. The OS is also more aggressive about GPU power management on laptops, and the handoff between power states is exactly where marginal drivers stumble. The good news is that the diagnostic sequence is well established and resolves the large majority of cases without new hardware.

Work through the steps below in order: clean driver reinstallation, timeout diagnostics, thermal remediation, power and clock checks, and finally the stress tests that render a verdict on the GPU itself.

## Why this happens

- **Bad driver migration during a Windows update:** The update's replacement graphics driver may be mismatched or corrupted. TDR crashes that start within days of an update point here first.
- **Corrupted driver installation:** Partial installs and conflicting remnants make the driver mishandle commands, hanging the GPU under load.
- **GPU overheating:** Heat-soaked laptop GPUs throttle, then hang. Clogged vents and aged thermal paste are the physical root of many TDR patterns.
- **Aggressive GPU power-state transitions:** Windows 11's laptop power management switches GPU power states frequently. Marginal drivers crash during the transitions, especially on battery or hybrid graphics.
- **Unstable factory or user overclock:** Gaming laptops ship with aggressive GPU tuning. Silicon that was borderline at the factory degrades into TDR crashes over time.
- **Unstable system RAM or VRAM:** Memory errors corrupt the driver's command stream. TDR crashes paired with occasional blue screens suggest memory rather than the GPU core.
- **Failing GPU hardware:** A dying GPU produces TDR crashes that survive drivers, cooling, and stock clocks — and they get worse month over month.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean-reinstall the graphics driver with DDU

A standard reinstall often preserves the corruption. DDU from Safe Mode removes the driver completely before the fresh install.

1. Download the latest driver for your GPU from the vendor.
1. Boot to Safe Mode and run Display Driver Uninstaller with Clean and restart.
1. Install the fresh driver in normal Windows and restart. Test with the workload that crashed most often.

### Fix 2: Check whether the crashes track a Windows update

Timing is diagnostic. Crashes that began right after an update have a different prime suspect than crashes on a long-stable system.

1. Open Settings, then Windows Update, then Update history, and compare dates with when crashes started.
1. If they correlate, the migrated driver is the suspect — the DDU reinstall above is the fix, not a driver rollback alone.
1. Consider pausing driver delivery afterward so the bad driver is not reinstalled; the [24H2 TDR notes](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/) cover version-specific patterns.

### Fix 3: Tune the TDR timeout diagnostically

A longer timeout separates slow GPUs from broken ones. Treat the result as information, not necessarily as the permanent fix.

1. In Registry Editor, go to HKEY_LOCAL_MACHINE, SYSTEM, CurrentControlSet, Control, GraphicsDrivers.
1. Create QWORD values TdrDelay set to 8 and TdrDdiDelay set to 10.
1. Restart and test. If crashes vanish, the GPU needed more time — still address thermals and drivers, since healthy GPUs rarely need this.

### Fix 4: Fix laptop thermals

Sustained heat is the most common non-driver cause. Laptop cooling needs active maintenance.

1. Monitor GPU temperatures under load; sustained readings over 90C need action.
1. Clean vents with compressed air and use the laptop on a hard surface.
1. Add a cooling pad for gaming sessions. On machines older than three years, consider professional repasting. Retest after each improvement.

### Fix 5: Stabilize clocks and power

Remove the variables of overclocking and power droop before judging the hardware.

1. Reset GPU clocks to stock in the vendor utility or Afterburner.
1. Set the Windows power plan to Best performance while testing, and use the original charger.
1. Disable variable refresh and overlay software temporarily to isolate the driver path. If the driver installs but immediately crashes instead, the [crashing NVIDIA driver guide](/articles/nvidia-driver-keeps-crashing-windows-11/) addresses that adjacent failure.

### Fix 6: Test system memory

When TDR crashes come with occasional blue screens or application crashes, suspect RAM.

1. Run Windows Memory Diagnostic from the Start menu and let the extended test complete.
1. If errors appear, test sticks individually where the design allows.
1. Replace faulty memory — it is cheaper than a GPU and a common hidden cause. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the memory diagnostic tool.

### Fix 7: Stress-test for the hardware verdict

Exhausted software leaves one question: is the GPU itself failing?

1. Run a sustained GPU stress test while logging temperatures.
1. Crashes at safe temperatures, or visual artifacts during the test, indicate hardware failure.
1. A GPU that passes an hour of stress testing at sane temperatures is healthy — revisit drivers and background software instead of shopping for repairs.

### Fix 8: Reinstall the chipset driver to stabilize the GPU bus

The discrete GPU communicates through the chipset's PCIe implementation, and an outdated or corrupted chipset driver can cause the hangs that TDR blames on the graphics driver. This is an underappreciated cause on both Intel and AMD laptops, particularly after Windows updates that migrate the chipset driver badly. Refreshing it costs little and rules out a whole layer.

1. Download the chipset driver for your exact model from the laptop vendor's support page.
1. Install it and restart, even if the installer claims the current version is fine.
1. Retest the crashing workload before touching graphics drivers again, so you know which change helped.

## Closing

Windows 11 TDR crashes are solvable in the great majority of cases: a DDU-clean driver, a bad update migration undone, or thermals restored to sanity. The registry timeout is a useful diagnostic, not a cure — let it tell you whether the GPU is slow or broken, then fix the actual cause. The freezes stop when the driver, the cooling, and the clocks all agree, and that agreement is achievable without replacing the machine.
