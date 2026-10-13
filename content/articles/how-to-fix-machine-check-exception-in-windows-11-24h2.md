---
title: "MACHINE_CHECK_EXCEPTION in Windows 11 24H2: What It Means and How to Fix It"
slug: how-to-fix-machine-check-exception-in-windows-11-24h2
date: 2026-09-08
categories: ["windows-errors"]
tags: ["bsod", "machine-check-exception", "windows-11-24h2"]
description: "MACHINE_CHECK_EXCEPTION in Windows 11 24H2 signals a hardware fault your CPU detected. Here's how to find the failing part and fix it."
thumbnail: "/images/thumbs/how-to-fix-machine-check-exception-in-windows-11-24h2.webp"
faqs:
  - q: "What does MACHINE_CHECK_EXCEPTION mean?"
    a: "It is a blue screen stop code (0x0000009C) raised when the CPU itself detects a hardware error — a fault in the processor, memory bus, cache, or connected hardware. Unlike most blue screens, this one points at hardware first, software second."
  - q: "Why does it happen more after the 24H2 update?"
    a: "The 24H2 update changed power management and driver models in ways that expose marginal hardware. A slightly unstable CPU or borderline RAM that worked under 23H2 can start throwing machine checks under 24H2's different voltage and scheduling behavior."
  - q: "Can a software fix resolve a machine check?"
    a: "Sometimes. Updating the BIOS, chipset drivers, and resetting overclocks resolve many cases, because the 'hardware fault' is really firmware or configuration marginality. Persistent machine checks after that, though, usually mean a genuinely failing component."
  - q: "Is my data at risk?"
    a: "The crash itself does not delete data, but the underlying hardware fault — especially a failing SSD — can. Back up your important files now, before you finish troubleshooting, so a dying drive does not take them with it."
---

`MACHINE_CHECK_EXCEPTION` — stop code `0x0000009C` — is the blue screen you get when your CPU catches a hardware fault and tells Windows about it. Unlike most blue screens, which blame drivers or system files, this one starts with the assumption that a physical component misbehaved: the processor, its cache, the memory bus, or something attached to it.

Seeing it spike after the Windows 11 24H2 update is common, and it does not necessarily mean your hardware died overnight. 24H2 changed power management and driver behavior enough to expose hardware that was already living on the edge. Here is how to sort out what is really failing.

## Why this happens

- **Unstable CPU or cache.** The processor detects an internal error — often from marginal silicon, heat, or voltage problems — and raises the machine check.
- **Failing or mismatched RAM.** Memory bus errors are the single most common machine-check source on laptops.
- **Outdated BIOS or microcode.** Old firmware lacks the CPU microcode updates that fix known errata on newer Windows builds.
- **Overclocking or aggressive undervolting.** 24H2's scheduler stresses cores differently; an undervolt that was stable before can now throw machine checks.
- **Overheating.** Thermal faults trigger machine checks when the CPU protects itself under extreme heat.
- **Failing motherboard components.** Voltage regulators and capacitors degrading with age cause intermittent machine checks that worsen over time.
- **Corrupt 24H2-specific drivers.** The chipset and storage drivers shipped for 24H2 can misbehave on hardware that skipped vendor driver updates.

## How to fix it

Work through these in order, from least to most invasive. Back up your data before you start — this is a hardware-first error.

### Fix 1: Back up your data right now

Before anything else, protect yourself against the worst case — a failing drive behind these crashes.

1. Plug in an external drive or confirm your cloud backup is current.
2. Copy your documents, photos, and anything irreplaceable — do not rely on "I will do it later."
3. If the crashes are frequent, boot into Safe Mode to copy files without triggering another blue screen.
4. Only after your backup is verified should you continue troubleshooting.

### Fix 2: Reset all overclocking and undervolting

If you tuned voltages or clocks at any point, this is the first suspect under 24H2.

1. Open whatever tool you used — Intel XTU, Throttlestop, Ryzen Master, or the BIOS itself.
2. Reset every setting to default or stock values.
3. In the BIOS, choose **Load Optimized Defaults** to be thorough.
4. Save, reboot, and use the laptop normally for a few days. Many post-24H2 machine checks vanish right here.
5. If you must undervolt later, redo it from scratch and stability-test each step — old profiles are not trustworthy under 24H2.

### Fix 3: Update the BIOS and chipset drivers

Firmware updates carry CPU microcode fixes that specifically address machine-check errata.

1. Visit your laptop manufacturer's support page and download the latest **BIOS/UEFI** and **chipset** drivers for your exact model.
2. Install the chipset package first, then flash the BIOS with the charger plugged in.
3. Do not interrupt the flash — a power loss here can brick the board.
4. After flashing, load BIOS defaults and reconfigure only what you need.
5. Intel users can also check for the latest platform drivers with the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 4: Test the memory thoroughly

The memory bus is the most common machine-check source, so test RAM properly — one quick pass is not enough.

1. Press `Win + R`, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**, then press **F1** and select **Extended** test with more passes.
3. If any errors appear, test sticks individually to isolate the bad one.
4. For a deeper test, run MemTest86 from a USB drive overnight — eight full passes is the gold standard.
5. Replace any stick that errors. Our [MEMORY_MANAGEMENT stop code guide](/articles/how-to-fix-stop-code-memory-management-on-dell-laptop/) covers RAM diagnosis step by step if you need it.

### Fix 5: Check temperatures and cooling

Thermal machine checks happen when the CPU overheats faster than throttling can respond.

1. Install HWMonitor or Core Temp and log temperatures during normal use and under load.
2. Sustained CPU temps above 95°C under load, or idle temps above 60°C, indicate a cooling problem.
3. Blow dust from the vents with compressed air and use the laptop on a hard surface.
4. On laptops older than two years, consider a repaste at a repair shop if temps stay high.
5. Set the power plan to **Balanced** instead of **Best performance** while troubleshooting.

### Fix 6: Scan the drive and repair system files

Rule out storage faults and 24H2 file corruption in one pass.

1. Open an elevated Command Prompt and run `chkdsk C: /f /r` — type **Y** and restart to run it.
2. Then run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Check the drive's SMART health with CrystalDiskInfo — reallocated sectors plus machine checks means the SSD is dying.
4. Replace a failing drive and reinstall Windows fresh; cloning a dying drive just moves the problem.

### Fix 7: Roll back or clean-install if it started with 24H2

If the machine checks began immediately after the 24H2 update and nothing above helped, the update itself may be the trigger.

1. Go to **Settings** > **System** > **Recovery** > **Go back** (available for 10 days after the update) to return to 23H2.
2. If the rollback window expired, download the [Windows 11 Installation Assistant](https://www.microsoft.com/en-us/software-download/windows11) and reinstall 24H2 cleanly — an in-place upgrade over itself fixes corrupted update state.
3. Back up first: a clean install wipes the drive.
4. If machine checks persist on a clean install with updated BIOS and tested RAM, the hardware fault is real — take it to a repair shop.

## Closing

`MACHINE_CHECK_EXCEPTION` is your CPU telling you something physical went wrong, but "physical" often turns out to be fixable: a bad undervolt, stale BIOS microcode, or a failing RAM stick. Back up first, reset your tuning, update firmware, and test the memory. Work it in that order and you will know exactly what you are dealing with instead of guessing. If the machine checks began right after a feature update, our [blue screen after Windows 11 update guide](/articles/how-to-fix-blue-screen-after-windows-11-update-reddit/) covers the rollback path in detail.
