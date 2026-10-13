---
title: "System Interrupts High CPU? Here's How to Fix It"
slug: how-to-fix-system-interrupts-high-cpu-youtube
date: 2026-09-13
categories: ["performance"]
tags: ["system interrupts", "high cpu", "drivers", "hardware", "dpc latency"]
description: "System Interrupts eating CPU in Task Manager? Learn what it really means — deferred procedure calls from drivers or hardware — and how to fix it."
thumbnail: "/images/thumbs/how-to-fix-system-interrupts-high-cpu-youtube.webp"
faqs:
  - q: "What is System Interrupts in Task Manager?"
    a: "System Interrupts isn't a real process — it's Task Manager's way of displaying CPU time spent handling hardware interrupts and Deferred Procedure Calls (DPCs). When a device needs attention (network packet arrived, disk finished a read), it interrupts the CPU; the driver then finishes the work as a DPC. High 'System Interrupts' CPU means some driver or device is generating excessive interrupts."
  - q: "Is high System Interrupts CPU dangerous?"
    a: "It's not dangerous to your data, but it's a symptom of something wrong: a misbehaving driver, a failing device, or a hardware conflict. Sustained high interrupt CPU (above 5–10%) causes audio crackling, mouse stutter, and general sluggishness because interrupt handling preempts normal processes. The underlying cause — not the interrupts themselves — is what needs fixing."
  - q: "Can a virus cause high System Interrupts?"
    a: "Extremely unlikely — malware doesn't typically manifest as interrupt storms. System Interrupts is a driver/hardware-level phenomenon, and rootkits work hard to stay invisible rather than generating obvious CPU load in Task Manager. If your interrupts are high, investigate drivers and hardware first; run a Defender offline scan for peace of mind, but don't expect it to be the cause."
  - q: "Why do System Interrupts spike when I watch YouTube?"
    a: "Video playback stresses the exact drivers most prone to interrupt issues: GPU (video decode), audio (output), and network (streaming). A marginal GPU or audio driver that behaves at idle can generate interrupt storms under the sustained load of video decode. Updating graphics and audio drivers fixes the majority of 'interrupts spike during video' cases."
---

"System Interrupts" climbing to 10%, 20%, even 100% of a CPU core in Task Manager looks terrifying — and the name gives you nothing to act on. Here's the translation: some piece of hardware (or its driver) is shouting for the CPU's attention thousands of times per second, and each shout costs CPU time. Your job is to find who's shouting.

This is a driver-and-hardware problem wearing a Task Manager disguise, so the fixes are methodical: identify the device, update or replace its driver, and check the hardware. For the step-by-step variant, see [fixing System Interrupts step by step](/articles/how-to-fix-system-interrupts-high-cpu-windows-11-step-by-step/); for the post-update variant, our [System Interrupts after update guide](/articles/how-to-fix-system-interrupts-high-cpu-after-windows-11-update/).

## Why this happens

- **Buggy or outdated drivers**: The #1 cause — network, audio, storage, and GPU drivers generating excess interrupts.
- **Failing hardware**: A dying drive, NIC, or USB device retrying operations generates interrupt storms.
- **DPC latency from bad drivers**: Drivers that do too much work at high priority stall everything.
- **USB device issues**: Faulty USB devices or controllers spamming interrupts.
- **Power management conflicts**: Devices fighting over power states generate spurious interrupts.
- **BIOS/firmware bugs**: Interrupt routing problems fixed in BIOS updates.
- **Shared IRQ conflicts**: Legacy-style conflicts on devices sharing interrupt lines.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's really interrupts (and how bad)

Baseline the problem.

1. Open **Task Manager** > **Processes**, find **System Interrupts**, and note its CPU % — under 1–2% is normal; sustained 5%+ deserves investigation; 20%+ is severe.
2. Check **Task Manager** > **Performance** > **CPU** — right-click the graph > **Change graph to** > **Logical processors** to see if one core is saturated (typical of interrupt storms).
3. Note when it spikes: at idle (failing hardware or bad driver), during video/network activity (GPU/audio/network driver), or after sleep/wake (power management).
4. Open **Resource Monitor** > **CPU** tab — the **Interrupts** pseudo-process confirms the same data from a second angle.
5. Record the pattern — "spikes to 15% when watching video" is a far more actionable diagnosis than "sometimes high."

### Fix 2: Use LatencyMon to identify the guilty driver

The definitive diagnostic tool.

1. Download **LatencyMon** (free, from Resplendence) and run it — click the play button and let it monitor for 5–10 minutes during your typical interrupt spike.
2. Check the **Drivers** tab sorted by **DPC count** and **ISR count** — the driver at the top with wildly disproportionate counts is your culprit (common names: `ndis.sys` = network, `storport.sys` = storage, `dxgkrnl.sys` = graphics, `usbport.sys` = USB, audio drivers like `rtkvhd64.sys`).
3. Note the exact driver filename — that's what you'll update, replace, or disable.
4. Also check the **Main** tab's "highest reported DPC routine execution time" — values in the milliseconds (not microseconds) indicate a seriously misbehaving driver.
5. Keep LatencyMon handy — you'll re-run it after each fix to verify the counts drop. This turns guessing into measurement.

### Fix 3: Update the implicated driver

The fix for most LatencyMon findings.

1. Map the driver filename to its device: `ndis.sys` → network adapter driver; `storport`/`iaStor` → storage/chipset; `dxgkrnl` → GPU; audio `.sys` → audio driver.
2. Get the update from the right source: GPU drivers from NVIDIA's, AMD's, or [Intel's](https://www.intel.com/content/www/us/en/support/detect.html) official driver pages; everything else from your laptop manufacturer's support page first.
3. For network drivers specifically, try both the manufacturer's version and the chipset maker's (Intel/Realtek/Qualcomm) — interrupt behavior varies between them.
4. Install, reboot, and re-run LatencyMon under the same workload — the DPC/ISR counts for that driver should collapse.
5. If the newest driver is worse (it happens), roll back: **Device Manager** > device > **Properties** > **Driver** > **Roll Back Driver**.

### Fix 4: Disconnect suspect USB and external devices

USB is a frequent silent offender.

1. Unplug **all** USB devices except keyboard/mouse — docks, external drives, webcams, audio interfaces, USB Wi-Fi adapters.
2. Watch System Interrupts for 10 minutes — if it drops, reconnect devices one at a time, waiting several minutes each, until the spike returns.
3. The guilty device gets: a different USB port, a driver/firmware update from its maker, or replacement if it's failing.
4. Pay special attention to **USB hubs and docks** — a marginal hub generates interrupts for every device behind it.
5. In **Device Manager** > **Universal Serial Bus controllers**, check for warning icons — and try disabling **USB selective suspend** (**Power Options** > advanced > **USB settings**) as a test, since suspend/wake cycles generate interrupt bursts.

### Fix 5: Update BIOS and chipset drivers

Interrupt routing lives in firmware.

1. Check your current BIOS version (**msinfo32** > **BIOS Version/Date**) against the latest on your manufacturer's support site.
2. BIOS updates frequently fix interrupt routing, ACPI power-state, and device-compatibility issues that manifest as interrupt storms — this is especially true after Windows feature updates.
3. Update the **chipset driver** alongside the BIOS — the chipset driver tells Windows how to talk to the interrupt controller.
4. Follow the manufacturer's BIOS update instructions exactly: plugged in, no interruptions, don't touch the machine during the flash.
5. Re-run LatencyMon after the update — firmware-level fixes show up as across-the-board DPC reductions, not just one driver improving.

### Fix 6: Disable or replace the problem device

When the driver can't be fixed.

1. If LatencyMon consistently fingers one device's driver and no update helps, consider disabling the device: **Device Manager** > right-click > **Disable device** (obviously not for essential devices).
2. Common candidates for disabling: unused network adapters (disable Wi-Fi if you use Ethernet or vice versa), old audio enhancements, unused SD card readers.
3. For essential devices with no good driver, a hardware replacement may be the answer — e.g., a USB Wi-Fi adapter replacing a flaky internal one, or a USB sound card replacing crackling onboard audio.
4. In **Device Manager**, also try **uninstalling** the device (checking "delete driver software") and letting Windows install its inbox driver — sometimes the inbox driver behaves better than the manufacturer's.
5. Check [Microsoft Support](https://support.microsoft.com/en-us/windows) and the [Update Catalog](https://www.catalog.update.microsoft.com/) for driver versions Windows Update hasn't offered you yet.

### Fix 7: Check for failing hardware

The uncomfortable final possibility.

1. If interrupts are high at idle with no driver standing out in LatencyMon, suspect hardware: run your manufacturer's diagnostics (Dell/Lenovo/HP all have boot-time component tests).
2. Check drive health (**CrystalDiskInfo**) — a failing drive's retry storms are a classic interrupt source.
3. Monitor temperatures — overheating components (especially chipsets and SSDs) generate error interrupts before they fail outright.
4. Test with a **Linux live USB** — if interrupts/DPC-equivalent load is high there too, it's definitively hardware, not a Windows driver problem.
5. For laptops under warranty, the manufacturer's diagnostic results are your ticket to a repair — document the LatencyMon findings and the idle-interrupt percentages to make the case. Broader hardware-vs-software triage is in our [slow laptop guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Closing

System Interrupts high CPU is always a who, not a what: some driver or device generating a storm of interrupts. LatencyMon names the driver, the right update (or BIOS, or unplugged USB device) quiets it, and verification is built into the process. It's the most technical-looking Task Manager entry and one of the most satisfying to fix — because once you see the guilty driver name, the mystery is over.
