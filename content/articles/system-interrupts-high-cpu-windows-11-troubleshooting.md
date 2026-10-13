---
title: "System Interrupts Eating CPU on Windows 11? Troubleshoot It"
slug: system-interrupts-high-cpu-windows-11-troubleshooting
date: 2026-10-07
categories: ["performance"]
tags: ["system interrupts", "cpu usage", "troubleshooting", "driver conflict", "windows 11"]
description: "Troubleshoot System Interrupts high CPU on Windows 11: identify the faulty driver or device with the right tools and stop the interrupt storm."
thumbnail: "/images/thumbs/system-interrupts-high-cpu-windows-11-troubleshooting.webp"
faqs:
  - q: "How do I find which driver causes high System Interrupts?"
    a: "Use LatencyMon (free) — run it for several minutes, then sort its Drivers tab by DPC count or total execution time. The driver at the top is generating the interrupt load. Common names: ndis.sys points to network drivers, storport.sys or stornvme.sys to storage, usbport.sys to USB. Then update or roll back that specific device's driver."
  - q: "Can Windows Update cause System Interrupts spikes?"
    a: "Yes. Feature updates replace drivers with generic Microsoft versions that may handle interrupts poorly on your hardware, and they can also re-enable devices you'd disabled. If the spike started right after an update, check Device Manager for driver dates matching the update, and roll back or replace the affected drivers with the laptop maker's versions."
  - q: "Does disabling devices in Device Manager help?"
    a: "As a diagnostic, absolutely — disabling a suspect device and watching System Interrupts drop confirms the culprit. As a permanent fix, only for non-essential devices like fingerprint readers or SD card readers. For essential devices (network, storage), disabling is just confirmation; the real fix is a corrected driver or repaired hardware."
  - q: "When should I suspect hardware instead of drivers?"
    a: "When drivers, BIOS, and a clean Windows install don't help; when maker's hardware diagnostics report errors; when the problem persists in a Linux live environment; or when the spike correlates with physical events like heat, movement, or plugging in a specific port. Failing drives and flaky USB controllers are the most common hardware causes."
---

Task Manager shows `System Interrupts` consuming a steady 10–30% of your CPU. There's no End Task button that works, no program to uninstall, and most "fixes" online are random registry tweaks that do nothing. Time for actual troubleshooting: a systematic process that identifies the interrupting device and fixes it.

System Interrupts is Windows accounting for kernel time spent servicing hardware requests. High values mean a device or driver is demanding attention far too often. This guide is the diagnostic workflow — measure, isolate, identify, fix. For a fix-ordered walkthrough of the same problem, see our companion guide to [fixing System Interrupts](/articles/best-way-to-fix-system-interrupts-high-cpu-windows-11/).

## Why this happens

- **Driver interrupt mishandling**: A buggy driver requests or mishandles interrupts excessively — the #1 cause.
- **Device generating spurious interrupts**: Failing hardware signals the CPU repeatedly as it errors.
- **Interrupt conflicts after updates**: New Windows builds reassign resources or replace tuned drivers with generic ones.
- **USB device malfunction**: A bad peripheral floods the USB controller with interrupt requests.
- **Storage subsystem errors**: A struggling drive's retries surface as interrupt load during I/O.
- **Network driver polling bugs**: Wi-Fi drivers stuck in aggressive polling or power-state flapping.
- **Firmware interrupt routing bugs**: BIOS misconfiguring how device interrupts reach the CPU.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure properly with the right tools

Task Manager's number is a hint, not a diagnosis.

1. Download **LatencyMon** (Resplendence, free) and **Process Explorer** (Microsoft Sysinternals) — both are standard technician tools.
2. Close unnecessary apps, then run LatencyMon for at least 5 minutes while the system idles. Click the **Drivers** tab and sort by **DPC count** — the leader is your suspect.
3. Also check the **ISR count** column — high ISR counts point to hardware-level interrupt flooding rather than driver deferred work.
4. Write down the top 2–3 drivers with their counts. Typical mappings: `ndis.sys` → network stack, `tcpip.sys` → network, `storport.sys`/`stornvme.sys` → storage controller, `USBPORT.SYS`/`usbxhci.sys` → USB, `dxgkrnl.sys` → graphics.
5. Re-run the measurement after each fix below — you want to see the counts drop, not just Task Manager's percentage wobble. Objective numbers beat vibes.

### Fix 2: Correlate with activity and devices

Narrow the suspect list before changing anything.

1. With LatencyMon running, test scenarios one at a time: idle, Wi-Fi heavy download, USB device plugged in, external monitor connected, on battery vs. plugged in.
2. Note which scenario spikes the counts — Wi-Fi activity implicating `ndis.sys` means the wireless driver; USB insertion spiking `usbxhci.sys` means USB subsystem.
3. Unplug all USB devices and re-measure — a dramatic drop immediately convicts a peripheral or the USB driver.
4. Toggle Wi-Fi off (airplane mode) for 5 minutes — if interrupts vanish, the wireless driver is the problem child.
5. Disconnect external monitors/docks — display-link and dock drivers are frequent offenders on office setups.
6. Document the trigger precisely: "ndis.sys DPC count explodes during Wi-Fi downloads, calm on Ethernet" is a diagnosis a support tech can act on.

### Fix 3: Update or roll back the implicated driver

Aim the fix at the measured culprit.

1. Open **Device Manager**, find the device behind the suspect driver (Network adapters for ndis.sys, Storage controllers for storport, etc.).
2. First try the laptop maker's driver for your exact model — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — makers tune drivers for their hardware's interrupt behavior.
3. For Intel wireless, also try the newest from the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), which often carries interrupt-handling fixes ahead of OEM packages.
4. If the problem started after a driver update: Properties > **Driver** > **Roll Back Driver** — then block that driver version from reinstalling via Windows Update's optional updates.
5. Re-measure with LatencyMon after every driver change. A fixed driver shows an immediate, dramatic count reduction — no reboot-and-hope needed beyond the required restart.

### Fix 4: Use Device Manager disable as a diagnostic scalpel

Confirm the device before committing to a fix.

1. In Device Manager, right-click the suspect device > **Disable device**. (Pick non-critical ones for longer tests: Bluetooth, fingerprint reader, SD reader, secondary adapters.)
2. Watch LatencyMon/Task Manager for 5 minutes. Interrupts collapse? Confirmed — the device or its driver is the source.
3. Re-enable and apply the real fix (driver update, firmware, replacement).
4. For USB root hubs: disable hubs one at a time — internal devices (webcam, card reader) hang off these, and one bad internal device can flood the whole controller.
5. Never leave critical devices disabled as a "fix" — it's a diagnostic step. The exception: a broken fingerprint reader you never use can stay disabled indefinitely with zero downside.

### Fix 5: Update BIOS and reset firmware settings

Interrupt routing is firmware's territory.

1. Note your BIOS version (`msinfo32`), then check the maker's support site for updates mentioning stability, device compatibility, or power management.
2. Flash per instructions with AC power connected — interrupted flashes brick machines.
3. After updating, also **load BIOS defaults** (or "optimized defaults") once — years of toggled settings can leave interrupt routing in a bad state; reconfigure only what you need afterward.
4. Update the **chipset driver** package alongside — BIOS and chipset drivers cooperate on interrupt delivery.
5. Re-measure. Firmware-level interrupt fixes are real and common; this step closes cases that driver updates couldn't.

### Fix 6: Rule out hardware failure

The remaining cases are usually physical.

1. Run the maker's full hardware diagnostics — Dell SupportAssist, HP Hardware Diagnostics, Lenovo Vantage — with the extended storage and motherboard tests.
2. Check drive health with the SSD maker's toolbox; run `chkdsk C: /scan` for file-system integrity.
3. Monitor temperatures (HWiNFO): overheating components generate errors, and errors generate interrupts. Clean vents and fans.
4. The Linux live-USB test: boot Ubuntu from USB, open a system monitor, and watch CPU. High interrupt-like load in Linux = hardware, definitively. Calm in Linux = a Windows driver you haven't found — revisit Fix 3 with different driver versions.
5. If hardware is implicated and under warranty, contact support with specifics: "LatencyMon shows stornvme.sys at 40,000 DPCs/sec, diagnostics report drive errors" — evidence accelerates RMAs.

### Fix 7: Clean up the software environment

Reduce the interrupt load from the software side.

1. [Perform a clean boot](/articles/how-to-perform-clean-boot-windows-11-on-laptop/) and re-measure — if interrupts are calm, a third-party driver or service is agitating the hardware. Re-enable in halves to find it.
2. Uninstall unused VPN clients, virtual network adapters, and USB device software — each installs filter drivers that add interrupt-path overhead.
3. Keep Windows updated — Microsoft ships interrupt and DPC fixes in cumulative updates; check the [Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update is behind.
4. As a last software resort, an in-place repair install refreshes the kernel and driver stack while keeping files and apps.
5. Set a baseline: record healthy LatencyMon numbers after fixing, so future regressions are obvious in one 5-minute test.

## Closing

Troubleshooting System Interrupts is detective work, not guesswork: measure with LatencyMon, correlate with activity, isolate with unplugging and Device Manager disables, then fix the convicted driver or device. The interrupt storm always has a source — this process finds it instead of hoping a random tweak does.
