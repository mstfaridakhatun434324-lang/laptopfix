---
title: "System Interrupts High CPU on Windows 11? Diagnose and Fix It"
slug: how-to-fix-system-interrupts-high-cpu-windows-11-on-laptop
date: 2026-09-13
categories: ["performance"]
tags: ["system interrupts", "high cpu", "deferred procedure calls", "drivers", "hardware"]
description: "System Interrupts eating CPU on Windows 11? Learn what deferred procedure calls are, find the faulty driver or hardware, and fix it."
thumbnail: "/images/thumbs/how-to-fix-system-interrupts-high-cpu-windows-11-on-laptop.webp"
faqs:
  - q: "What is the System Interrupts process in Windows 11?"
    a: "System Interrupts isn't a real process — it's a placeholder Task Manager shows for CPU time spent handling hardware interrupts and Deferred Procedure Calls (DPCs). When hardware (network card, USB device, GPU, storage controller) needs the CPU's attention, it raises an interrupt; the CPU stops what it's doing to service it. High 'System Interrupts' CPU means some hardware or its driver is interrupting the CPU excessively — thousands of times per second instead of the normal trickle."
  - q: "Is high System Interrupts CPU dangerous?"
    a: "Not directly dangerous, but it's a symptom worth investigating. Sustained high interrupt activity steals CPU from your applications, causes audio stuttering, mouse lag, and general sluggishness, and on laptops it prevents the CPU from entering low-power states — draining battery and generating heat. The underlying cause is usually a buggy driver or misbehaving USB device rather than failing hardware, and both are fixable."
  - q: "Can I end the System Interrupts process?"
    a: "No — there's nothing to end. System Interrupts has no executable and no process to kill; it's Task Manager's accounting label for kernel interrupt-handling time. Anyone telling you to 'disable System Interrupts' is mistaken. The fix is always finding which driver or device is generating the interrupt storm and updating, reconfiguring, or replacing it — the work happens in Device Manager, not Task Manager."
  - q: "What is a DPC latency checker and do I need one?"
    a: "DPC latency tools (like LatencyMon or Windows Performance Analyzer) measure how long Deferred Procedure Calls take to execute — high DPC latency from a bad driver causes audio dropouts and stutter even when overall CPU looks fine. If your symptom is stuttering audio or laggy mouse rather than just a high Task Manager number, running LatencyMon for a few minutes will name the exact driver file (like ndis.sys or storport.sys) responsible, which is far more precise than guessing."
---

**System Interrupts** sitting at 10%, 20%, or even 30% CPU in Task Manager is uniquely confusing because there's nothing to kill, nothing to uninstall, and no .exe to Google. That's because System Interrupts isn't a program at all — it's Task Manager's label for time the CPU spends servicing hardware interrupts. Something plugged into (or inside) your laptop is shouting for the CPU's attention thousands of times per second, and every shout steals cycles from your actual work.

The symptoms go beyond the Task Manager number: crackling or stuttering audio, a mouse that lags, DPC-induced micro-freezes, worse battery life (the CPU can't sleep when it's constantly interrupted), and extra heat. The cause is almost always a driver — network, USB, storage, or audio drivers are the usual suspects — or a misbehaving external device. This guide shows you how to identify the exact driver with free tools and fix it. For driver-adjacent CPU issues, see [Windows Modules Installer high CPU](/articles/how-to-fix-windows-modules-installer-high-cpu-step-by-step/); for general slowness, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Buggy network driver**: Wi-Fi and Ethernet drivers are the #1 cause of interrupt storms — especially after Windows updates replace OEM drivers.
- **USB device misbehaving**: A flaky external drive, hub, dock, or peripheral spams interrupts.
- **Storage controller driver issues**: Outdated AHCI/NVMe drivers generate excessive interrupts during disk I/O.
- **Audio driver DPC spikes**: Bad audio drivers cause high DPC latency — the classic "crackling audio" scenario.
- **Failing hardware**: A dying Wi-Fi card, SSD, or USB controller retries operations endlessly, each retry an interrupt.
- **BIOS/firmware bugs**: Power management firmware that mishandles device sleep states causes wake-interrupt loops.
- **IRQ conflicts from docks**: USB-C docks and port replicators multiplexing many devices can overwhelm the interrupt controller.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the offending driver with LatencyMon

Stop guessing — measure.

1. Download **LatencyMon** (free, from Resplendence) and run it as administrator.
2. Click the play button and let it monitor for 5–10 minutes while the System Interrupts CPU is high.
3. Check the **Drivers** tab sorted by **DPC count** or **Highest execution** — the driver at the top (e.g., `ndis.sys`, `storport.sys`, `USBPORT.SYS`, `HDAudBus.sys`) is your culprit.
4. Note the exact `.sys` filename — you'll target this driver in the following fixes.
5. If LatencyMon reports "your system appears suitable" but Task Manager still shows high interrupts, the issue may be hardware-level (Fix 6) rather than a single driver.

### Fix 2: Update the culprit driver from the right source

Driver source matters enormously here.

1. Open **Device Manager**, find the device matching the bad driver (Network adapters for ndis.sys, Storage controllers for storport.sys, Sound for audio drivers).
2. Right-click > **Update driver** > **Search automatically** is the weakest option — it rarely finds the newest driver.
3. Better: get the driver from your laptop maker's support page (Dell, HP, Lenovo, or ASUS) — OEM drivers are validated for your exact hardware and power management.
4. For Intel Wi-Fi/Bluetooth: use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) — Intel's Wi-Fi drivers are frequently newer than OEM bundles.
5. For NVIDIA/AMD GPUs: [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx) / AMD's official driver download page.

### Fix 3: Roll back the driver if the problem started with an update

Newer isn't always better — Windows Update loves replacing good OEM drivers with generic ones.

1. In **Device Manager**, right-click the suspect device > **Properties** > **Driver** tab.
2. If **Roll Back Driver** is clickable, use it — this restores the previous version that presumably worked.
3. To stop Windows Update from "upgrading" it again: **Settings** > **Windows Update** > **Advanced options** > turn off **Receive updates for other Microsoft products**, and consider the Group Policy "Do not include drivers with Windows Updates" (Pro) or the registry equivalent.
4. If rollback isn't available, manually download the older OEM driver version from the manufacturer's support archive.
5. This single fix resolves a huge fraction of post-update System Interrupts cases — the generic Microsoft driver for a Wi-Fi card is a classic offender.

### Fix 4: Disconnect and isolate external devices

USB peripherals are silent interrupt spammers.

1. Unplug ALL USB devices — docks, hubs, external drives, printers, webcams, even the mouse (use the touchpad temporarily).
2. Watch Task Manager for 2–3 minutes. Interrupts drop? Plug devices back one at a time, waiting a minute between each, until the spike returns.
3. Common offenders: USB-C docks (firmware bugs), external HDDs with aggressive power management, cheap USB hubs, and USB audio interfaces with bad drivers.
4. For the guilty device: update its firmware/drivers, try a different port (USB 2.0 ports generate fewer interrupts than USB 3.x for low-bandwidth devices), or replace it.
5. Laptop docks especially: check the dock manufacturer's site for firmware updates — dock firmware bugs are a notorious DPC source.

### Fix 5: Tune network adapter power management

For ndis.sys / Wi-Fi driver culprits.

1. In **Device Manager** > **Network adapters**, right-click your Wi-Fi adapter > **Properties** > **Power Management** tab — uncheck **Allow the computer to turn off this device to save power** (counterintuitive, but power-state transitions generate interrupt storms on buggy drivers).
2. On the **Advanced** tab, look for power-saving properties (e.g., "Power Saving Mode," "U-APSD support") and set them to **Maximum Performance** as a test.
3. Disable unused network adapters entirely (right-click > **Disable device**) — Bluetooth PAN, virtual adapters from VPNs, and old Ethernet controllers you never use.
4. If you use a VPN, test with it disconnected — VPN virtual adapters are frequent DPC contributors.
5. Re-enable power saving after confirming the fix if battery life matters — but only after updating to a driver that handles it properly.

### Fix 6: Update BIOS/firmware and check hardware health

When it's below the OS level.

1. Check your manufacturer's support page for **BIOS updates** — firmware changelogs often mention "fixes high CPU/interrupt" or "improves device power management."
2. Update SSD firmware via the drive maker's tool (Samsung Magician, Crucial Storage Executive, WD Dashboard) — storage firmware bugs cause storport.sys interrupt storms.
3. Run the manufacturer's hardware diagnostics (Dell SupportAssist, Lenovo Vantage, HP PC Hardware Diagnostics) — a failing Wi-Fi card or SSD shows up here.
4. Listen for the pattern: interrupts that spike during disk activity point at storage; during network activity, the Wi-Fi card; constant regardless, deeper hardware or BIOS.
5. If diagnostics flag a component and the laptop is under warranty, that's a repair ticket — interrupt storms from failing hardware only get worse.

### Fix 7: Clean Windows reinstall for the truly stubborn cases

When drivers, firmware, and isolation all fail.

1. Back up your data — this is the nuclear option.
2. Do a clean install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) (not a reset — a true clean install from USB media).
3. Install drivers ONLY from the laptop manufacturer's support page, in their recommended order (chipset first).
4. Test System Interrupts before installing any third-party software — if it's clean, add programs back gradually.
5. If interrupts are high even on a pristine install with OEM drivers, it's hardware — take it to service.

## Closing

System Interrupts high CPU is your laptop telling you a driver or device is misbehaving at the hardware level — Task Manager can't name it, but LatencyMon can. Identify the .sys file, update or roll back that specific driver from the right source, unplug suspects one by one, and the interrupt storm almost always has a concrete, fixable cause. It's detective work, but it's deterministic detective work.
