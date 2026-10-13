---
title: "How to Fix WHEA_UNCORRECTABLE_ERROR on Windows 10"
slug: how-to-fix-whea-uncorrectable-error-on-windows-10
date: 2026-10-13
categories: ["windows-errors"]
tags: ["blue screen", "hardware error", "windows 10"]
description: "WHEA_UNCORRECTABLE_ERROR means Windows caught a hardware fault. Learn how to tell hardware failure from driver issues and fix it."
thumbnail: "/images/thumbs/how-to-fix-whea-uncorrectable-error-on-windows-10.webp"
faqs:
  - q: "Does WHEA_UNCORRECTABLE_ERROR always mean my CPU is dying?"
    a: "No. Despite the hardware-sounding name, overclocking instability, outdated BIOS firmware, bad RAM, overheating, and even buggy chipset drivers all trigger it. A genuinely failing CPU is actually one of the less common causes — rule out everything else first."
  - q: "Can I just disable WHEA to stop the blue screens?"
    a: "Don't. WHEA is the messenger reporting real hardware faults; disabling error reporting doesn't fix the fault, it just lets corruption happen silently. You'd trade blue screens for data corruption, which is strictly worse."
  - q: "Why does it only crash when gaming?"
    a: "Gaming loads the CPU and GPU simultaneously, raising temperatures and power draw — exactly the conditions that expose unstable overclocks, weak cooling, and marginal RAM. If it's game-only, heat and overclocking jump to the top of the suspect list. Our [gaming crash guide](/articles/best-way-to-fix-blue-screen-while-gaming/) digs into this pattern."
  - q: "How do I know if it's the SSD?"
    a: "Run CrystalDiskInfo and look at the health status plus the SMART attributes — reallocated sectors and CRC errors are red flags. Also note the pattern: crashes during heavy disk activity (installs, large copies) point at storage, while crashes during CPU-heavy tasks point at CPU/RAM."
---

WHEA_UNCORRECTABLE_ERROR is the blue screen Windows shows when the hardware itself reports an unrecoverable error. That sounds terminal, but here's the thing most guides bury: drivers cause this stop code too, by misconfiguring hardware or mishandling its error reports.

So don't assume your CPU is dying. The right order is: rule out drivers and overclocks first (cheap, fast), then test the hardware properly. Our [WHEA reference](/articles/whea-uncorrectable-error-troubleshooting/) covers the theory; the steps below are the practice. None of the steps below require special tools beyond a screwdriver and a USB stick, and they're ordered from free and easy toward involved.

## Why this happens

- Overclocked or undervolted CPU becoming unstable under load.

- Failing RAM producing hardware error reports through the memory controller.

- Outdated chipset, storage, or BIOS firmware mishandling hardware error signaling.

- An overheating CPU or VRM triggering thermal hardware faults.

- A genuinely failing CPU, motherboard, or SSD — the least common but real cause.

- Corrupted drivers for the storage controller or chipset misreporting hardware state.

- A motherboard voltage regulator struggling under sustained load, especially on thin-and-light laptops with minimal cooling headroom.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Reset all overclocks to stock

Overclocking is the number one cause of this stop code on otherwise healthy hardware. Returning to stock speeds is the fastest diagnostic you have.

1. Enter BIOS/UEFI setup (**F2**, **Del**, or **Esc** during boot).

2. Disable CPU overclocks, **XMP/EXPO** memory profiles, and any undervolting.

3. Select **Load Optimized Defaults**, then **Save & Exit**.

4. Use the laptop normally for a few days. If crashes stop, your overclock was unstable — dial it back or leave it stock.

### Fix 2: Update the BIOS and chipset drivers

Motherboard makers fix hardware-error handling in BIOS updates constantly. An old BIOS misreading sensor data can throw this error on perfectly good hardware.

1. Find your exact laptop model on the manufacturer's support site.

2. Download the latest **BIOS** and **chipset** driver — for your model only.

3. Install the chipset driver first and restart.

4. Apply the BIOS update with the laptop plugged into AC power, and don't interrupt it. Dell users can start at the [Dell support site](https://www.dell.com/support).

### Fix 3: Test the RAM

The memory controller reports through WHEA, so bad RAM shows up here. Test before suspecting the CPU.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.

2. For a definitive test, boot **MemTest86** from USB and run at least 2 passes.

3. Test sticks individually if errors appear.

4. Replace faulty sticks — memory errors here are hardware, full stop.

### Fix 4: Check temperatures and cooling

Thermal faults are real hardware errors. A laptop that only crashes under load is telling you about heat, not a dying CPU.

1. Install **HWiNFO** and log CPU temperatures during a stress test or heavy game.

2. Sustained readings above **95-100°C** indicate a cooling problem.

3. Blow out vents with compressed air and ensure the laptop sits on a hard surface.

4. If it thermal-throttles constantly, the heatsink may need repasting — a shop job if you're not comfortable opening the laptop.

### Fix 5: Run system file and disk checks

Corrupted drivers and disk errors can generate spurious hardware error reports. Rule them out cheaply.

1. Open **Command Prompt (Admin)** and run `sfc /scannow`.

2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.

3. Then run `chkdsk C: /f /r` (schedule it with **Y** and restart).

4. If chkdsk finds extensive bad sectors, suspect the SSD — check its SMART health next.

### Fix 6: Reinstall storage and chipset drivers cleanly

The storage controller driver talks directly to the hardware WHEA monitors. A clean reinstall eliminates driver-level false alarms.

1. In **Device Manager**, expand **Storage controllers** and **IDE ATA/ATAPI controllers**.

2. Uninstall each controller driver (don't worry — Windows reinstalls basics on reboot).

3. Restart, then install the latest chipset and storage drivers from the laptop maker's site.

4. Monitor for a few days before declaring victory.

### Fix 7: Check the SSD health

A dying SSD throws hardware errors that WHEA dutifully reports. This check takes two minutes and can save hours of misdiagnosis.

1. Install **CrystalDiskInfo** and check the drive's health status.

2. **Caution** or **Bad** means replace the drive soon — back up first.

3. Also check the manufacturer's own SSD toolbox for firmware updates.

4. If the drive is healthy and crashes persist after all fixes above, the CPU or motherboard is the remaining suspect — time for professional diagnosis.

### Fix 8: Reseat the SSD and memory

Laptops live in backpacks, and vibration loosens things. A slightly unseated M.2 SSD or RAM stick throws intermittent hardware errors that WHEA reports faithfully — reseating both is quick preventive medicine.

1. Shut down, unplug, and remove the battery if it's removable.

2. Open the bottom panel (you'll need a small Phillips screwdriver).

3. Remove the single screw holding the **M.2 SSD**, lift it slightly, reseat it firmly, and re-tighten.

4. Release, remove, and firmly reseat each **RAM stick** until the clips click.

5. While inside, check for obvious issues: dust packed around components or a swollen battery.

6. Reassemble and test under load for a few days.

## Closing

WHEA_UNCORRECTABLE_ERROR deserves respect — it can mean real hardware trouble — but the statistics favor fixable causes: unstable overclocks, old BIOS firmware, bad RAM, and heat. Work the list from cheap to expensive and you'll usually find the answer before spending money. If every test passes and it still crashes at stock settings with good cooling, that's when you take it to a repair shop with your test results in hand; you've already done half their diagnostic work. While the panel is open, look for the obvious: a swollen battery pressing on components, dust packed around the SSD, or a loose heatsink screw. Physical issues cause a real share of WHEA errors. If you'd rather not open the machine yourself, a shop will do the reseat and inspection cheaply — it's quick work with the right screwdrivers. You now know more about your machine's health than most owners ever will — temperatures, memory integrity, drive health, firmware age. That knowledge pays off the next time anything acts up, not just with this stop code. If the WHEA error showed up after a Windows 11 update on another machine, the [post-update WHEA guide](/articles/how-to-fix-whea-uncorrectable-error-after-windows-11-update/) sorts out update-triggered driver faults from real hardware.
