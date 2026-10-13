---
title: "What to Do If System Interrupts Shows High CPU in Windows 11"
slug: "what-to-do-if-system-interrupts-high-cpu-windows-11"
date: "2026-09-29"
categories: ["performance"]
tags: ["system interrupts high cpu", "system interrupts 100% cpu", "deferred procedure calls", "windows 11 cpu spike", "hardware interrupts"]
description: "System Interrupts eating 10–30% CPU in Task Manager? Learn what this pseudo-process means, how to trace it to a faulty driver or device, and how to fix it."
thumbnail: "/images/thumbs/what-to-do-if-system-interrupts-high-cpu-windows-11.webp"
faqs:
  - q: "What is a normal percentage for System Interrupts?"
    a: "Between 0% and 3% is completely normal — that is the ordinary background chatter of hardware talking to the CPU. Brief spikes to 5–10% during heavy disk or network activity are also fine. It becomes a problem when System Interrupts sustains above 5–10% at idle, or above 20% during light use, indicating an interrupt storm from a faulty device or driver."
  - q: "Can System Interrupts be a virus?"
    a: "Extremely unlikely. System Interrupts is a kernel accounting category, not a process that malware can impersonate — there is no executable to replace. Malware shows up as its own processes in Task Manager instead. If your CPU is high and you suspect malware, look at the actual named processes, not System Interrupts."
  - q: "Why does it spike after waking from sleep?"
    a: "Sleep/wake transitions renegotiate power states with every device, and drivers with power-management bugs can get stuck generating interrupts during the transition — Wi-Fi and audio drivers are the usual suspects. Disabling ‘allow the computer to turn off this device’ on the network adapter (Fix 4) resolves most post-wake interrupt storms."
  - q: "Will reinstalling Windows fix System Interrupts CPU?"
    a: "Sometimes, if the cause is a corrupted driver installation — a clean install with fresh drivers can help. But if the cause is failing hardware, a BIOS bug, or a bad USB device, reinstalling changes nothing and wastes hours. Always run the LatencyMon + USB + driver investigation first; reinstall only after hardware causes are ruled out."
---

System Interrupts is not a real program — it is Task Manager's way of showing CPU time spent handling hardware interrupts and deferred procedure calls (DPCs). When it sits at 1–3%, everything is normal. When it climbs to 10%, 20%, or higher and stays there, some piece of hardware or its driver is screaming for the CPU's attention thousands of times per second, and every other process waits in line behind it.

This is a hardware/driver problem wearing a Task Manager costume, so the fix is detective work: identify which device is generating the interrupt storm, then update, reconfigure, or disable it. The steps below walk that investigation in order.

## Why this happens

- **Faulty or outdated device driver:** A buggy network, audio, or storage driver can generate interrupt storms.
- **Failing hardware:** A dying hard drive or flaky USB device retries operations endlessly, each retry an interrupt.
- **USB device misbehaving:** Bad USB devices — especially hubs, docks, and external drives — are classic interrupt storm sources.
- **Network adapter driver issues:** Wi-Fi drivers with power-management bugs interrupt constantly during sleep/wake transitions.
- **Audio driver DPC problems:** Misbehaving audio drivers (a known issue with some Realtek/Conexant versions) pile up DPC latency.
- **BIOS/firmware bugs:** Interrupt routing problems fixed in BIOS updates.
- **Overheating causing hardware retries:** Thermal stress makes marginal hardware retry operations, multiplying interrupts.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the reading and check DPC latency

First make sure the reading is real and sustained — brief System Interrupts spikes during heavy I/O are normal. LatencyMon (free) quantifies DPC latency and often names the offending driver directly.

1. Watch Task Manager for 10 minutes: is System Interrupts consistently above 5–10%?
2. Download and run LatencyMon; let it collect data for 5 minutes during the spike.
3. Check LatencyMon's Drivers tab sorted by DPC count — the top driver is your prime suspect.
4. Note the driver filename (e.g., ndis.sys, storport.sys, HDAudBus.sys).

### Fix 2: Unplug USB devices one by one

USB devices are the most common and easiest-to-test cause. A failing external drive, hub, or dock can generate thousands of interrupts per second, and the test is free: unplug and watch.

1. Disconnect all USB devices except keyboard/mouse (use built-in if laptop).
2. Watch System Interrupts CPU for two minutes after each removal.
3. If CPU drops after removing a device, that device (or its driver/cable) is faulty.
4. Try the suspect device in another port or with another cable to isolate further.

### Fix 3: Update the suspect driver

LatencyMon usually names the driver: ndis.sys points at the network adapter, storport.sys at storage, audio drivers at sound. Update that specific driver from the laptop manufacturer's support site — not just Windows Update. [Microsoft's support hub](https://support.microsoft.com/en-us/windows) documents driver update paths if you need the official procedure.

1. Identify your exact network/audio/storage hardware in Device Manager.
2. Download the latest driver from your laptop maker's support site.
3. Install, restart, and re-run LatencyMon for 5 minutes.
4. If the driver was the cause, DPC counts collapse immediately.

### Fix 4: Disable power management on the network adapter

Wi-Fi adapters with aggressive power saving generate interrupt storms during power-state transitions — a notorious cause of System Interrupts spikes, especially after sleep/wake.

1. Open Device Manager > Network adapters > your Wi-Fi adapter > Properties.
2. On the Power Management tab, untick ‘Allow the computer to turn off this device to save power.’
3. On the Advanced tab, disable power-saving features (e.g., set Power Saving Mode to Maximum Performance).
4. Restart and monitor System Interrupts for an hour, including a sleep/wake cycle.

### Fix 5: Test with a clean boot to rule out software triggers

Some ‘hardware’ interrupt storms are actually triggered by software hammering a device — monitoring tools, RGB controllers, and old VPN clients polling hardware constantly. A clean boot separates hardware causes from software triggers.

1. Run msconfig; on Services tab tick Hide all Microsoft services, then Disable all.
2. Disable all Startup items in Task Manager, then restart.
3. If System Interrupts calms down, re-enable in halves to find the trigger.
4. Update or remove the offending software.

### Fix 6: Update the BIOS

Interrupt routing and APIC configuration live in firmware. Manufacturers fix interrupt-storm bugs in BIOS updates more often than people expect — especially on laptops where power-state transitions are complex.

1. Check your manufacturer's support site for BIOS updates newer than yours.
2. Follow their flashing instructions exactly (AC power, charged battery, no interruptions).
3. After flashing, load BIOS defaults, then reapply any custom settings.
4. Monitor System Interrupts for a full day.

### Fix 7: Check drive health and thermals

A failing drive retrying bad sectors generates exactly this symptom, as does overheating hardware retrying operations. Both are worth ruling out before concluding it is a driver issue.

1. Run CrystalDiskInfo and check all drives' health status.
2. Monitor CPU/GPU temperatures with HWMonitor during the spike.
3. If a drive shows Caution/Bad, back up immediately and replace it.
4. Clean dust from vents; thermal retries vanish when temperatures normalize.

### Fix 8: Test in Safe Mode to isolate hardware vs software

Safe Mode loads only essential Microsoft drivers. If System Interrupts calms down in Safe Mode, a third-party driver is the cause; if it stays high, suspect hardware or firmware. This single test halves the search space. For related service-level CPU mysteries, our [Windows Update slowdown guide](/articles/windows-11-slow-after-update-how-to-fix/) covers the software side, and the [Dell-specific System Interrupts walkthrough](/articles/how-to-fix-system-interrupts-high-cpu-windows-11-on-dell-laptop/) shows the same method on Dell hardware.

1. Hold Shift while clicking Restart, then Troubleshoot > Advanced options > Startup Settings > Restart.
2. Press 4 for Safe Mode and observe System Interrupts CPU for 10 minutes.
3. Calm in Safe Mode means a third-party driver — update or remove recent driver installs.
4. Still high means hardware/firmware — focus on USB devices, BIOS, and drive health.

## Closing

System Interrupts high CPU is Windows telling you a hardware conversation has gone wrong — some device is interrupting the CPU thousands of times per second. The investigation order matters: confirm with LatencyMon, unplug USB suspects, update the named driver, tame network power management, and check BIOS and drive health. Worked patiently, the interrupt storm almost always traces to one identifiable device or driver.
