---
title: "Fixing KMODE_EXCEPTION_NOT_HANDLED on an ASUS Laptop"
slug: how-to-fix-kmode-exception-not-handled-on-asus-laptop
date: 2026-10-04
categories: ["windows-errors"]
tags: ["blue screen", "kmode exception", "asus", "windows 11", "driver crash"]
description: "KMODE_EXCEPTION_NOT_HANDLED blue screen on your ASUS laptop? Identify the faulty driver and fix it with these 7 targeted repair steps."
thumbnail: "/images/thumbs/how-to-fix-kmode-exception-not-handled-on-asus-laptop.webp"
faqs:
  - q: "What does KMODE_EXCEPTION_NOT_HANDLED mean?"
    a: "A kernel-mode driver caused an exception that Windows couldn't handle — usually an access violation or illegal instruction inside the driver. The stop code is 0x0000001E. The crash screen often names the offending driver file, like nvlddmkm.sys or netwtw10.sys, which tells you exactly where to look."
  - q: "Is KMODE_EXCEPTION_NOT_HANDLED a hardware problem?"
    a: "Usually not — it's a software problem in about 80% of cases, caused by buggy, outdated, or mismatched drivers. Failing RAM can cause it too, but start with drivers. If the blue screen names a .sys file, that driver is your prime suspect."
  - q: "Why does it happen when I play games on my ASUS laptop?"
    a: "Gaming stresses the GPU driver, network driver, and audio driver simultaneously — the three most common KMODE culprits. Update your NVIDIA or AMD graphics driver, your Wi-Fi driver, and your Realtek audio driver, and the crashes typically stop."
  - q: "Can antivirus cause KMODE_EXCEPTION_NOT_HANDLED?"
    a: "Yes. Antivirus products install kernel filter drivers, and a bad update can trigger this stop code. If crashes started after an antivirus update, uninstall it temporarily and use Microsoft Defender to test."
---

KMODE_EXCEPTION_NOT_HANDLED (stop code 0x1E) is Windows telling you that a driver did something illegal inside the kernel — accessed memory it shouldn't have, executed a bad instruction, or divided by zero — and the system had no safe way to recover. On ASUS laptops, from VivoBooks to ROG gaming machines, this almost always traces back to one misbehaving driver: graphics, Wi-Fi, or audio lead the pack.

The crash screen itself often hands you the answer by naming a `.sys` file. If you caught it, skip straight to the driver fix. If not, the steps below will help you find it and fix it.

## Why this happens

- **Buggy or outdated GPU drivers.** NVIDIA and AMD driver releases occasionally ship with kernel bugs that crash under specific games or workloads — extremely common on ROG laptops.
- **Wi-Fi driver conflicts.** Intel and MediaTek wireless drivers on ASUS models are frequent KMODE offenders, especially after Windows Update swaps them.
- **Corrupted system files.** Damage to kernel components can make even good drivers crash, since they all share the same kernel space.
- **Antivirus filter drivers.** Third-party security software hooks deep into the kernel; a bad update crashes the whole system.
- **Failing RAM.** Less common, but bad memory corrupts driver code as it loads, producing KMODE crashes that name different drivers each time.
- **Overclocked or unstable hardware.** ROG laptops with aggressive performance profiles or user overclocks can push components past stability.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Identify the faulty driver from the crash screen or dump

Knowing the exact driver saves hours of guessing.

1. The next time the blue screen appears, photograph it or note any **.sys** filename shown (e.g., `nvlddmkm.sys` = NVIDIA, `rtwlanu.sys` = Realtek Wi-Fi, `ntoskrnl.exe` = Windows kernel itself).
2. Common mappings: `nvlddmkm.sys` → GPU, `netwtw10.sys`/`Netwtw12.sys` → Intel Wi-Fi, `rtkvhd64.sys` → Realtek audio, `ntfs.sys` → storage/disk.
3. If the screen flashes too fast to read, disable automatic restart: boot to **Advanced startup > Troubleshoot > Advanced options > Startup Settings**, or see our guide on [disabling automatic restart after a blue screen](/articles/how-to-disable-automatic-restart-after-bsod-on-windows-11/).
4. Check `C:\Windows\Minidump` for dump files — even without analyzing them, the timestamps tell you when crashes happen.

### Fix 2: Update the graphics driver cleanly

The GPU driver is suspect number one on ASUS gaming laptops.

1. Get the latest driver for your exact GPU from [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html).
2. Boot into **Safe Mode** (interrupt startup three times for Automatic Repair, then **Troubleshoot > Advanced options > Startup Settings**).
3. Open **Device Manager**, expand **Display adapters**, right-click your GPU, and choose **Uninstall device**, ticking **Attempt to remove the driver**.
4. Restart normally and install the fresh driver you downloaded — choose **Custom install** and tick **Perform a clean installation** on NVIDIA.
5. Avoid "Game Ready" beta drivers if stability matters more than day-one game support; the **Studio** driver branch is often more stable.

### Fix 3: Update Wi-Fi and Bluetooth drivers from ASUS

Wireless drivers are the second most common cause.

1. Identify your Wi-Fi chip in **Device Manager > Network adapters** (Intel, MediaTek, or Realtek).
2. Download the latest driver package for your exact ASUS model — ASUS bundles Wi-Fi, Bluetooth, and chipset drivers together, which avoids version mismatches.
3. In **Device Manager**, right-click the Wi-Fi adapter and choose **Uninstall device** (tick the driver removal box).
4. Install the downloaded package and restart.
5. If crashes persist, try the driver directly from Intel via [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) — sometimes newer than ASUS's repackaged version.

### Fix 4: Uninstall third-party antivirus temporarily

Kernel-level security drivers are a documented KMODE trigger.

1. Open **Settings > Apps > Installed apps** and uninstall your third-party antivirus.
2. Use the vendor's official removal tool if offered (Norton, McAfee, and Avast all ship one) — the standard uninstall often leaves kernel drivers behind.
3. Restart and rely on **Microsoft Defender** for a few days.
4. If crashes stop, the antivirus was guilty — reinstall the latest version or stay with Defender.

### Fix 5: Run SFC, DISM, and a memory test

Rule out corrupted system files and bad RAM in one pass.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` again.
3. Press **Windows + R**, type `mdsched.exe`, choose **Restart now and check for problems**, and let the memory test finish.
4. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
5. If the blue screen names a different driver every time, suspect RAM first — that randomness is the classic signature of bad memory.

### Fix 6: Disable overclocking and reset performance profiles

ROG laptops with tweaked settings crash more.

1. Open **Armoury Crate** (ASUS's utility) and set the operating mode back to **Silent** or **Balanced** instead of **Turbo**.
2. If you enabled any manual GPU overclock (MSI Afterburner or similar), reset it to defaults.
3. Enter the BIOS and choose **Load Optimized Defaults** if you changed anything there.
4. Restart and test under the workload that used to crash.

### Fix 7: Use Driver Verifier to catch the culprit (advanced)

If you still don't know which driver is guilty, make Windows tell you.

1. Press **Windows + R**, type `verifier.exe`, and press Enter.
2. Choose **Create standard settings**, then **Automatically select all drivers installed on this computer** — or select unsigned/suspicious drivers only.
3. Restart. Driver Verifier stresses drivers; the guilty one will crash faster, and the blue screen will name it.
4. Once identified, boot into **Safe Mode**, run `verifier /reset` in an admin Command Prompt, and fix or remove that driver.
5. Do not leave Verifier running permanently — it slows the system and can cause crashes on its own.

For crashes with a similar driver-blame pattern, our [UNEXPECTED_KERNEL_MODE_TRAP guide](/articles/how-to-fix-unexpected-kernel-mode-trap-after-windows-11-update/) covers a closely related stop code.

## Closing

KMODE_EXCEPTION_NOT_HANDLED is a driver problem until proven otherwise, and on ASUS laptops the investigation usually ends at the GPU or Wi-Fi driver. Identify the named `.sys` file, do a clean reinstall of that driver, and you're done in most cases. The deeper tools — memory tests, Driver Verifier — are there for the stubborn remainder, but you likely won't need them.
