---
title: "Troubleshooting System Interrupts High CPU: The Diagnostic Playbook"
slug: troubleshoot-system-interrupts-high-cpu-windows-11
date: 2026-10-09
categories: ["performance"]
tags: ["system interrupts troubleshoot", "dpc latency", "interrupt storm", "driver diagnosis"]
description: "A technician's diagnostic playbook for System Interrupts high CPU in Windows 11: measure with the right tools, isolate the faulty driver or device, and fix it."
thumbnail: "/images/thumbs/troubleshoot-system-interrupts-high-cpu-windows-11.webp"
faqs:
  - q: "What's the difference between interrupts and DPCs?"
    a: "Hardware interrupts (ISRs) are the CPU's immediate response to hardware signals; deferred procedure calls (DPCs) are the follow-up work Windows schedules to finish later. Task Manager's System Interrupts number combines both. High ISRs point at chatty or failing hardware; high DPCs point at drivers doing too much work per interrupt. Tools like LatencyMon and Windows Performance Analyzer split them so you know which you're fighting."
  - q: "Which tool is best for diagnosing interrupt issues?"
    a: "For most users, LatencyMon — it's free, simple, and names the offending driver within minutes. For deep analysis, Windows Performance Analyzer (part of the Windows ADK) with the DPC/ISR trace gives the full picture professionals use. Start with LatencyMon; escalate to WPA only if LatencyMon's answer is inconclusive."
  - q: "How do I use Windows Performance Recorder for this?"
    a: "Install the Windows Performance Toolkit from the ADK, run wpr.exe -start DPCISR (or use the GUI recorder with the DPC/ISR profile), reproduce the high CPU for a few minutes, then wpr.exe -stop trace.etl. Open the trace in Windows Performance Analyzer and examine the DPC/ISR Duration by Module table — the modules with the highest durations are your culprits."
  - q: "Can Windows 11 itself cause interrupt storms, or is it always drivers?"
    a: "It's almost always drivers or hardware, not the OS core — Windows' own interrupt handling is well-tested. What can look like a Windows cause: a Windows update delivering a bad driver version, or a power-management policy change altering interrupt moderation. In those cases the trigger was Windows Update, but the faulty component is still the driver. Rolling back that driver usually resolves it."
---

Yesterday's guide answered 'how do I fix it' — this one answers 'how do I find it.' Troubleshooting System Interrupts is a measurement discipline: you quantify the problem, isolate the subsystem, identify the exact driver or device, and only then act. Guessing wastes hours; measuring takes minutes. This is the playbook technicians follow, adapted for anyone comfortable installing a free tool and reading a sorted list.

You'll work in three phases: establish the baseline, narrow the subsystem (USB? network? storage? audio?), then name the driver. Each phase has a clear pass/fail signal telling you when to move on. If you want the fix-first version of this topic, see [how to fix System Interrupts high CPU](/articles/how-do-i-fix-system-interrupts-high-cpu-windows-11/); for ordinary process-level CPU hogs, [high CPU usage in Windows 11](/articles/how-to-fix-high-cpu-usage-on-windows-11/) is the companion.

Phase one takes five minutes and needs only Task Manager.

## Why this happens

- **Unmeasured 'high CPU' that's actually normal**: Brief interrupt spikes during heavy I/O are healthy — the first diagnostic step is proving the problem is real and sustained.
- **USB subsystem storms**: Failing USB devices or hubs generate interrupt floods; isolating the USB tree is a distinct diagnostic phase.
- **Network driver DPC overload**: NDIS drivers with interrupt moderation disabled drown the CPU during transfers — measurable per-driver.
- **Storage driver ISR issues**: storport and AHCI driver problems show as interrupt load correlated with disk activity.
- **Audio driver DPC latency**: Audio drivers run at high priority; buggy ones stall the system measurably in DPC traces.
- **Firmware power-management bugs**: C-state and power-transition bugs cause interrupt storms that no driver update fixes — only BIOS updates do.
- **Failing hardware signaling distress**: Dying components generate error interrupts; the pattern is load that survives OS reinstalls or appears in live-USB tests.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Phase 1: Establish the baseline

Prove the problem is real, sustained, and quantified before touching anything.

1. Open Task Manager, Details tab, and record System Interrupts CPU at idle for five minutes — note the average, not the peak.
2. Record context: on battery or AC, Wi-Fi on/off, USB devices connected, audio playing or silent.
3. Sustained 10%+ at true idle is actionable; under 5% with spikes is usually normal.
4. Write the numbers down — you'll compare every later test against this baseline.

### Fix 2: Phase 2: Isolate the subsystem

Narrow from 'something' to 'USB vs network vs storage vs audio' with binary tests.

1. Disconnect all USB devices and re-measure for two minutes — a drop implicates USB.
2. Disable Wi-Fi/Ethernet (airplane mode) and re-measure — a drop implicates the network driver.
3. Stop all disk activity and re-measure — load that vanishes at disk-idle implicates storage.
4. Mute/stop all audio and re-measure — audio DPC issues vanish when the audio stack idles.
5. The subsystem whose removal drops the number is where your culprit lives.

### Fix 3: Phase 3: Name the driver with LatencyMon

Turn the subsystem suspicion into a driver filename.

1. Download and run LatencyMon as administrator for 5-10 minutes during the problem.
2. Open the Drivers tab, sort by DPC count and by total execution time.
3. The top one or two .sys files are your culprits — note exact filenames.
4. Cross-reference: ndis.sys/wdiwifi.sys means network, storport.sys/storahci means storage, portcls.sys means audio.

### Fix 4: Verify with a clean-boot confirmation

Confirm the suspect before changing drivers — correlation isn't causation.

1. Run msconfig, choose Selective startup, and disable all non-Microsoft services.
2. Restart and re-measure: if interrupts drop, a third-party driver/service is confirmed guilty.
3. Re-enable in halves (binary search) to pinpoint the exact one.
4. This takes time but gives certainty — worth it before BIOS updates or hardware replacement.

### Fix 5: Fix the identified driver

Now — and only now — change something, targeting the named culprit.

1. Update the specific driver from the manufacturer (not Windows Update's generic version).
2. If the problem started with a driver update, roll it back in Device Manager instead.
3. For network culprits, check adapter advanced properties for interrupt moderation settings.
4. Re-measure with LatencyMon after the change — the DPC counts should collapse.

### Fix 6: Escalate to firmware and hardware tests

When no driver is guilty, the problem is below the OS.

1. Update BIOS — firmware interrupt bugs are fixed only in firmware.
2. Run manufacturer hardware diagnostics from boot.
3. Boot a Linux live USB and check interrupt/CPU behavior there — hardware faults reproduce across OSes.
4. Intel's driver resources at [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) and Microsoft's docs at [Microsoft's Windows support site](https://support.microsoft.com/en-us/windows) support the process.

### Fix 7: Document and monitor

Close the loop so the problem stays fixed and you recognize recurrence.

1. Record the culprit driver/device and the fix applied.
2. Set a calendar reminder to re-check after the next feature update — driver regressions recur.
3. Keep LatencyMon installed; a two-minute run is the fastest re-diagnosis.
4. If the same device fails again within months, replace it — repeat offenders are dying, not glitchy.

### Fix 8: Confirm with a selective-startup binary search

When LatencyMon names a third-party driver but you're not certain it's causal, a binary search through startup services gives definitive proof before you change drivers.

1. Open msconfig, choose Selective startup, and on the Services tab hide all Microsoft services.
2. Disable the top half of the remaining services, restart, and re-measure System Interrupts.
3. If the problem persists, the culprit is in the enabled half; if it vanishes, it's in the disabled half.
4. Repeat, halving the suspect group each round — five rounds isolate one service out of thirty-two.
5. Once identified, update, reconfigure, or uninstall the owning software.
6. Return msconfig to Normal startup when done.
7. This method is slow but gives certainty — use it when the stakes are high, like before replacing hardware.

## Closing

Troubleshooting System Interrupts is measurement, not guesswork: baseline it, isolate the subsystem with binary tests, name the driver with LatencyMon, confirm with a clean boot, then fix precisely. Most technicians solve these cases in under an hour following this playbook. The interrupts are just the messenger — this method finds who sent the message.
