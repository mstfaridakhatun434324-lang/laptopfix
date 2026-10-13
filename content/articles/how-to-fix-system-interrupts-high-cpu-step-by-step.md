---
title: "System Interrupts High CPU? A Step-by-Step Diagnosis"
slug: how-to-fix-system-interrupts-high-cpu-step-by-step
date: 2026-09-10
categories: ["performance"]
tags: ["system interrupts", "high cpu", "diagnosis", "drivers", "latencymon"]
description: "System Interrupts consuming your CPU? Follow this methodical step-by-step diagnosis to find the exact driver or device causing the interrupt storm."
thumbnail: "/images/thumbs/how-to-fix-system-interrupts-high-cpu-step-by-step.webp"
faqs:
  - q: "What is a safe/normal level for System Interrupts CPU?"
    a: "At idle, System Interrupts should sit between 0% and 2% — occasionally spiking to 5% during heavy I/O is fine. Sustained readings above 5% at idle warrant investigation; above 10% you'll feel the sluggishness; above 20% and the system is seriously impacted. These thresholds apply at idle with no apps running — during gaming or file copies, higher transient values are normal."
  - q: "How do I use LatencyMon to find the problem driver?"
    a: "Download and run LatencyMon as administrator, click the play button, and let it monitor for 5–10 minutes during typical use. Then open the Drivers tab and sort by ISR count — the driver with an overwhelmingly high count is generating the interrupt storm. The reported filename (like storport.sys or a Wi-Fi driver) tells you exactly which device subsystem to fix. Also check the Main tab's verdict on real-time audio suitability, which summarizes overall interrupt health."
  - q: "Can Windows Update cause System Interrupts to spike?"
    a: "Yes — it's one of the most common triggers. Windows Update replaces drivers, and the new driver (often a generic Microsoft version replacing the manufacturer's tuned one) can generate interrupt storms immediately. If the spike started within a day of updates installing, check Settings > Windows Update > Update history, identify driver updates, and roll back the suspect in Device Manager or reinstall the manufacturer's version."
  - q: "Should I worry if System Interrupts is high only when a USB device is plugged in?"
    a: "No need to worry about the system — but you've found your culprit. A specific USB device (or the port/hub it's on) generating interrupt storms points to a faulty device, a bad cable, or an incompatible USB 3 device on a USB 2 port (or vice versa). Try a different port, a different cable, and the device on another computer. If it misbehaves everywhere, replace the device."
---

`System Interrupts` high CPU is uniquely frustrating because there's nothing to kill, nothing to uninstall, and no error message — just a phantom entry in Task Manager consuming your processor. Most guides respond with a grab-bag of "try updating drivers," which is fine advice but terrible diagnosis. This guide is different: it's a strict step-by-step diagnostic sequence. Each step either identifies the culprit or eliminates a category, so you always know what to do next.

You'll need about an hour and one free tool (LatencyMon). By the end, you'll know exactly which driver or device is generating the interrupt storm — not a guess, a measurement. Let's begin.

For the HP-specific variant of this problem, see [System Interrupts high CPU on HP laptops](/articles/how-to-fix-system-interrupts-high-cpu-on-hp-laptop/). For general driver health, [updating drivers on Windows 11](/articles/how-to-update-drivers-on-windows-11-laptop/) is useful background.

## Why this happens

- **A driver generating spurious interrupts**: One misbehaving driver firing thousands of excess interrupts per second.
- **Failing hardware retrying operations**: Dying drives or flaky devices generating error interrupts.
- **USB device spamming the controller**: Faulty peripherals overwhelming the USB interrupt handler.
- **Network adapter power-state bugs**: Wi-Fi/Ethernet drivers mishandling sleep/wake transitions.
- **Outdated BIOS or chipset drivers**: Platform-level interrupt routing problems.
- **Thermal interrupt storms**: Overheating components generating excessive management interrupts.
- **Driver replaced by Windows Update**: A generic driver swapped in over the manufacturer's version.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Establish the baseline measurement

You can't fix what you haven't measured.

1. Close all applications and let the system sit for 5 minutes — note the **System Interrupts** CPU percentage in Task Manager's **Details** tab. This is your baseline.
2. Record three numbers: idle percentage, percentage with your normal apps open, and percentage during a file copy. This tells you whether it's constant (driver/hardware) or load-triggered (specific subsystem).
3. Check **Performance** > **CPU** and note whether the interrupts correlate with disk, network, or GPU activity — the correlation hints at the subsystem.
4. Take a screenshot of Task Manager sorted by CPU — you'll compare against this after each fix.
5. Define your target: sustained idle under 2%. Anything above 5% at true idle is abnormal and worth the full diagnosis below.

### Fix 2: The Safe Mode elimination test

Determine whether it's a third-party driver or something deeper.

1. Hold **Shift** while clicking **Restart**, then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4** for Safe Mode.
2. In Safe Mode, open Task Manager and check System Interrupts at idle for 5 minutes.
3. **Normal in Safe Mode** → a third-party driver or startup service is the cause. Continue to Fix 3.
4. **Still high in Safe Mode** → the cause is a core Windows driver, BIOS-level issue, or hardware fault. Skip to Fix 5 (hardware isolation) and Fix 6 (BIOS/platform).
5. Restart normally afterward — Safe Mode was diagnostic only.

### Fix 3: The USB and peripheral isolation sweep

The fastest physical test in the sequence.

1. With the system running normally, disconnect **every** USB device: mouse (use the touchpad), external drives, printers, docks, USB hubs, even the charger if it's USB-C (test on battery briefly).
2. Watch System Interrupts for 2–3 minutes after each removal — note any drop.
3. If removing a specific device fixes it, you've found it: try the device in a different port, with a different cable, and on another computer to determine whether it's the device, cable, or port.
4. Pay special attention to USB docks and hubs — they're the most common USB interrupt offenders, especially with outdated firmware.
5. If USB isolation changes nothing, reconnect everything and continue — you've eliminated an entire category in five minutes.

### Fix 4: Identify the exact driver with LatencyMon

The precision instrument step.

1. Download **LatencyMon** from Resplendence (free) and run it as administrator.
2. Click the green **Play** button and let it collect data for 5–10 minutes while the system exhibits the problem (don't run heavy apps — you want the interrupt baseline).
3. Open the **Drivers** tab, click the **ISR count** column header to sort descending — the top driver is your prime suspect. Also check **DPC count** sorting for confirmation.
4. Interpret the filename: `storport.sys`/`stornvme.sys` = storage; `ndis.sys` + your Wi-Fi driver's .sys = network; `usbport.sys`/`usbxhci.sys` = USB; `HDAudBus.sys` = audio; `nvlddmkm.sys`/`amdkmdag.sys` = GPU.
5. Write down the exact filename — Fix 5 targets it directly. If counts are spread evenly with no clear leader, the issue is platform-level (BIOS/chipset) rather than one driver.

### Fix 5: Fix the identified driver

Surgical strike on the culprit.

1. Open **Device Manager** and locate the device corresponding to the LatencyMon-identified driver.
2. **If the problem started recently**: right-click > **Properties** > **Driver** > **Roll Back Driver** — then block Windows from "updating" it again via the manufacturer's version below.
3. **Otherwise**: install the manufacturer's latest driver — get it from your laptop maker's support site (not just Windows Update). For Intel/AMD/NVIDIA components, use [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA's download page, or AMD's driver page.
4. For network adapters: additionally disable power management (**Properties** > **Power Management** > uncheck **Allow the computer to turn off this device**) — power-state transition bugs are a top network interrupt source.
5. Restart, re-measure your baseline from Fix 1, and re-run LatencyMon briefly to confirm the ISR counts normalized.

### Fix 6: Update BIOS, chipset, and storage platform drivers

For platform-level interrupt issues.

1. Visit your laptop manufacturer's support site and install the latest **BIOS**, **chipset**, and **storage (Intel RST/AMD)** drivers, in that order, restarting between each.
2. BIOS updates fix interrupt routing (APIC/ACPI) bugs — keep the laptop plugged in and don't interrupt the flash.
3. After updating, load BIOS defaults (or optimized defaults) — custom BIOS tweaks to power management or virtualization can alter interrupt behavior.
4. Re-run the LatencyMon test — platform updates often resolve the "no single driver stands out" cases from Fix 4.
5. Check Microsoft's official [Windows support page](https://support.microsoft.com/en-us/windows) for any known interrupt-handling issues with your specific Windows build.

### Fix 7: Hardware isolation and the final verdict

When software fixes are exhausted.

1. Run your manufacturer's built-in hardware diagnostics (HP: F2 at boot; Dell: F12 > Diagnostics; Lenovo: F10 or Lenovo Vantage) — run the full storage and motherboard tests.
2. Check SMART data with CrystalDiskInfo — look for **Caution** or **Bad** status, reallocated sectors, or CRC errors. A dying drive is a classic interrupt storm source.
3. Test RAM with `mdsched.exe` — memory errors generate machine-check interrupts that inflate the counter.
4. Monitor temperatures (HWiNFO64) under load — if the CPU is thermal-throttling, the throttling machinery itself generates interrupts; clean the cooling system.
5. Final decision tree: diagnostics point to a component → replace it (drives and RAM are user-replaceable on many laptops; motherboards mean professional repair). Diagnostics clean + still high in Safe Mode → consider a clean Windows reinstall, since something is corrupt below the driver level.

## Closing

System Interrupts isn't a mystery — it's a measurement, and measurements can be traced. Baseline it, eliminate Safe Mode and USB categories quickly, identify the exact driver with LatencyMon, and fix that driver. That methodical sequence resolves the overwhelming majority of cases in under an hour, replacing guesswork with evidence at every step.
