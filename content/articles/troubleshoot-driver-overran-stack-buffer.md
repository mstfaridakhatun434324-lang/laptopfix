---
title: "DRIVER_OVERRAN_STACK_BUFFER in Windows 11? Fix the Faulty Driver"
slug: troubleshoot-driver-overran-stack-buffer
date: 2026-10-04
categories: ["windows-errors"]
tags: ["driver overran stack buffer", "bsod", "windows 11", "driver error"]
description: "DRIVER_OVERRAN_STACK_BUFFER (0xF7) means a driver corrupted memory. Learn to identify the guilty driver and fix this blue screen step by step."
thumbnail: "/images/thumbs/troubleshoot-driver-overran-stack-buffer.webp"
faqs:
  - q: "What does the DRIVER_OVERRAN_STACK_BUFFER stop code mean?"
    a: "It means a driver wrote data past the end of its reserved stack memory, corrupting neighboring memory that the Windows kernel or another driver depends on. Windows stops the system with stop code 0x000000F7 to prevent that corruption from causing worse damage, such as silent data loss or security compromise."
  - q: "Which driver is causing DRIVER_OVERRAN_STACK_BUFFER on my laptop?"
    a: "The blue screen sometimes names the driver file, such as a .sys file at the bottom of the screen. If it doesn't, check the minidump in C:\\Windows\\Minidump with WinDbg, or enable Driver Verifier to stress third-party drivers until the guilty one crashes the system. Network, storage, and graphics drivers are the most frequent offenders."
  - q: "Can overclocking trigger DRIVER_OVERRAN_STACK_BUFFER?"
    a: "Yes. Overclocking the CPU or RAM destabilizes memory timing, so a driver writing to the stack can land in the wrong place when memory is unstable. Gaming laptops with XMP profiles or manual overclocks are especially prone. Restoring BIOS defaults is one of the fastest fixes if the crash started after an overclock."
  - q: "Is DRIVER_OVERRAN_STACK_BUFFER a hardware problem?"
    a: "Usually not. Roughly nine times out of ten it is a buggy, corrupt, or incompatible driver rather than failing hardware. Hardware enters the picture when RAM itself is faulty or a storage controller is dying. Rule out the driver causes first with the steps below, then test memory before suspecting the hardware."
---

Seeing **DRIVER_OVERRAN_STACK_BUFFER** on a blue screen is intimidating — it sounds like something deep inside Windows broke. In plain terms, it means one of your device drivers wrote past the end of its reserved memory "stack," stomping on memory that belongs to something else. Windows catches this corruption at the kernel level and halts the system with stop code **0x000000F7** before the damage can spread to your files.

The good news: this error almost always names a culprit, either directly on the blue screen (a `.sys` file shown near the bottom) or in the minidump file Windows saves automatically to `C:\Windows\Minidump`. In my experience, network adapter drivers, storage controller drivers, and GPU drivers account for the overwhelming majority of these crashes — especially right after a driver update, a Windows feature update, or installing "tuning" software.

Before you change anything, take a photo of the blue screen with your phone if it names a driver file. Then boot back into Windows (or Safe Mode if normal boot crashes) and work through the fixes below in order. If this started right after a Windows update, our guide to [blue screens after Windows 11 updates](/articles/how-to-fix-driver-overran-stack-buffer-after-windows-11-update/) covers the update-specific angle; and if you want a general framework for reading crash dumps, see [driver verifier violations](/articles/how-to-fix-driver-verifier-detected-violation-in-windows-11-24h2/).

## Why this happens

- **A buggy or corrupt device driver**: The classic cause. A driver with a coding bug, or one whose files were corrupted during installation, writes beyond its stack buffer and corrupts adjacent kernel memory.
- **A recent driver or Windows update**: Updates replace driver files and change kernel behavior. A driver that worked on the old build can start misbehaving on the new one.
- **Conflicting third-party software**: Antivirus filter drivers, VPN clients, firewall software, and "game booster" utilities install kernel-level drivers that fight with hardware drivers over the same resources.
- **Faulty RAM**: Bad memory cells cause the corruption Windows blames on the driver — the driver wrote correctly, but the memory itself flipped bits.
- **Overclocked CPU or memory**: Unstable overclocks and aggressive XMP profiles corrupt stack memory under load, triggering the same stop code as a buggy driver.
- **Malware and rootkits**: Kernel-level malware hooks drivers and can cause exactly this kind of memory corruption.
- **Failing storage controller or SSD**: A dying controller corrupts data in transit between the driver and the drive, which Windows reads as a driver overrunning its buffer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the guilty driver

Don't guess — the evidence is already on your system.

1. Open **File Explorer** and navigate to `C:\Windows\Minidump`. If the folder doesn't exist, crashes haven't been configured to save dumps (rare on Windows 11).
2. Install **WinDbg Preview** from the Microsoft Store, open it, and load the newest `.dmp` file.
3. Run the command `!analyze -v` and look for the `IMAGE_NAME` and `MODULE_NAME` lines — that's the crashing driver, e.g. `rtwlanu.sys` (Realtek Wi-Fi) or `nvlddmkm.sys` (NVIDIA).
4. If WinDbg feels like too much, check **Event Viewer** > **Windows Logs** > **System** for the BugCheck event with code 0xF7 — it often lists the driver name in the details.

### Fix 2: Update or roll back the faulty driver

Once you know the driver name, target it directly.

1. Press **Win + X** and open **Device Manager**. Find the device (e.g. Network adapters for a Wi-Fi driver).
2. Right-click it and choose **Update driver** > **Search automatically for drivers**.
3. If the crash started right after an update, choose **Properties** > **Driver** tab > **Roll Back Driver** instead, and confirm.
4. Restart and use the laptop normally for a day. If crashes stop, you're done — don't update that driver again until a newer, stable version is available.

### Fix 3: Run Driver Verifier to catch the bad driver

When you can't identify the driver, let Windows stress-test them.

1. Press **Win + R**, type `verifier`, and press Enter.
2. Select **Create standard settings** > **Next** > **Select driver names from a list**.
3. Check only **non-Microsoft** drivers (third-party ones) — never verify all drivers at once or the system may become unusable.
4. Click **Finish** and restart. Use the laptop normally; Driver Verifier will force a blue screen naming the misbehaving driver. Then boot into Safe Mode, run `verifier /reset`, and replace that driver.
5. Warning: Driver Verifier intentionally makes the system slower and more crash-prone. Always reset it (`verifier /reset`) after you've found the culprit.

### Fix 4: Repair system and driver files with SFC and DISM

Corrupted shared system files can make a healthy driver crash.

1. Open **Terminal (Admin)** or **Command Prompt (Admin)**.
2. Run `sfc /scannow` and let it complete — this repairs protected Windows files.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store SFC draws from.
4. Restart. If SFC reported that it fixed corruption, test the laptop before moving on — file repair alone often resolves 0xF7.

### Fix 5: Test your RAM

Memory faults produce identical stop codes, so rule them out early.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The laptop will reboot into the Windows Memory Diagnostic.
3. Let the standard test finish (about 15–30 minutes). Any red errors mean at least one RAM stick is faulty.
4. On laptops with removable RAM, reseat or replace the faulty module. On ultrabooks with soldered RAM, a failed test means a motherboard repair — back up your data first.

### Fix 6: Reset overclocking and BIOS settings to defaults

Unstable clocks corrupt memory under load.

1. Restart and enter the **BIOS/UEFI** (usually **F2**, **Del**, or **Esc** during the manufacturer's logo).
2. Find the option to **Load Optimized Defaults** or **Restore Defaults** and apply it.
3. If you enabled XMP/DOCP memory profiles or manual CPU overclocks (including Intel XTU or Ryzen Master changes in Windows), disable them.
4. Save and exit, then test. If the crashes stop, your overclock was the cause — keep it at stock for stability.

### Fix 7: Do a clean install of the driver from the manufacturer

Windows Update drivers are generic; the manufacturer's build is the real fix.

1. Identify your laptop model and download the latest driver for the suspect device from your manufacturer's support site (Dell, HP, or Lenovo) — or from [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html) for GPU/chipset drivers.
2. In **Device Manager**, right-click the device and choose **Uninstall device**, ticking **Attempt to remove the driver for this device** if offered.
3. Restart, then install the downloaded driver package manually.
4. For NVIDIA/AMD GPUs, choose the **Custom (Clean Install)** option during setup to remove all leftover files.

## Closing

DRIVER_OVERRAN_STACK_BUFFER looks scary but it's one of the most fixable blue screens — in the vast majority of cases it's a single bad driver, and the steps above will identify and replace it. If you've worked through every fix and the crashes continue with different drivers named each time, that's the classic signature of failing RAM or a dying motherboard component, and it's time to back up your data and involve the manufacturer's service center.
