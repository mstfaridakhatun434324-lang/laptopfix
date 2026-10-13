---
title: "How to Fix the System Service Exception BSOD on Windows 11"
slug: system-service-exception-windows-11-fix
date: 2026-09-16
categories: ["windows-errors"]
tags: ["bsod", "system-service-exception", "windows-11"]
description: "SYSTEM_SERVICE_EXCEPTION blue screens on Windows 11 are usually driver-related. Here's how to identify the culprit and stop the crashes."
thumbnail: "/images/thumbs/system-service-exception-windows-11-fix.webp"
faqs:
  - q: "What does SYSTEM_SERVICE_EXCEPTION mean?"
    a: "It's a blue screen (stop code 0x0000003B) that fires when a system service or driver tries to execute an illegal operation — like accessing memory it shouldn't. The most common triggers are buggy third-party drivers (especially graphics and network), corrupted system files, or malware interfering with system services."
  - q: "The blue screen names a .sys file. What do I do with that?"
    a: "That filename is the single most useful clue you have. Note it down exactly — common ones include nvlddmkm.sys (NVIDIA), Netwtw10.sys (Intel Wi-Fi), and rtwlane.sys (Realtek Wi-Fi). Update, roll back, or reinstall the software that owns that driver, as described in Fix 3 below."
  - q: "Can antivirus software cause SYSTEM_SERVICE_EXCEPTION?"
    a: "Yes. Third-party antivirus products run kernel-level drivers, and a buggy or outdated one can trigger this exact stop code — particularly right after a Windows feature update. Fully uninstalling the antivirus temporarily (not just disabling it) is a legitimate diagnostic step."
  - q: "Is this error a sign my RAM is failing?"
    a: "Occasionally, but drivers are far more likely. If the crashes name different .sys files each time, or happen with no clear pattern, then yes — test your RAM with mdsched.exe as described in Fix 6."
---
SYSTEM_SERVICE_EXCEPTION is a classic Windows blue screen that shows up when a driver or system service attempts something the kernel won't allow — usually touching memory it has no business touching. On Windows 11 laptops, the trigger is a misbehaving third-party driver in the vast majority of cases.

The good news: the blue screen often names the offending `.sys` file right on the screen, which hands you the culprit on a plate. Even when it doesn't, the fixes below will systematically eliminate the usual suspects.

## Why this happens

- **Buggy third-party drivers.** Graphics, Wi-Fi, and audio drivers from NVIDIA, Intel, Realtek, and others are the most frequent cause — a single bad release can crash the kernel.
- **A Windows update broke driver compatibility.** Feature updates change kernel internals, and drivers that worked fine before can start misbehaving afterward.
- **Corrupted system files.** Damaged Windows components can cause legitimate system services to execute invalid operations.
- **Malware or rootkits.** Malicious kernel-level code triggers exactly the kind of illegal operations this stop code reports.
- **Failing RAM.** Intermittent memory corruption makes drivers and services read garbage, producing crashes that name a different file every time.
- **Overclocking or unstable hardware.** Aggressive GPU or CPU settings on gaming laptops can destabilize drivers under load.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once the crashes stop.

### Fix 1: Note the .sys file on the blue screen

This takes no effort and can shortcut the whole process.

1. The next time the blue screen appears, look at the small text near the bottom — it often says something like **"What failed: nvlddmkm.sys"**.
2. Photograph the screen with your phone or write the filename down exactly.
3. Search the web for that filename to identify its owner. `nvlddmkm.sys` is NVIDIA graphics, `Netwtw10.sys` is Intel Wi-Fi, `rtwlane.sys` is Realtek Wi-Fi, `atikmdag.sys` is AMD graphics.
4. Skip straight to Fix 3 and target that specific driver first.

### Fix 2: Boot into Safe Mode if the crashes block normal use

If you can't stay in Windows long enough to troubleshoot, stabilize first.

1. Interrupt the boot three times (hold the power button at the logo screen) to reach the **Windows Recovery Environment**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **5** for **Safe Mode with Networking**.
3. Safe Mode loads only Microsoft's own drivers, so if the crashes stop here, you've confirmed a third-party driver is the cause.

### Fix 3: Update or roll back the suspect driver

This is the fix that resolves most SYSTEM_SERVICE_EXCEPTION crashes.

1. Press **Win + X** and open **Device Manager**.
2. If you identified a `.sys` file in Fix 1, find the matching device: **Display adapters** for GPU files, **Network adapters** for Wi-Fi files.
3. Right-click it and choose **Update driver > Search automatically for drivers**.
4. If the crashes started right after a driver or Windows update, go to **Properties > Driver tab** and click **Roll Back Driver** instead.
5. For the most reliable result, download the driver from the manufacturer's site — [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) for NVIDIA GPUs, or your laptop maker's support page for everything else — and install it over the current one.
6. Restart and use the laptop normally. Related driver crashes like [IRQL_NOT_LESS_OR_EQUAL](/articles/irql-not-less-or-equal-troubleshooting/) respond to the same treatment.

### Fix 4: Run a full malware scan

Rule out malicious kernel-level code before going deeper.

1. Open **Windows Security** from the Start menu.
2. Go to **Virus & threat protection > Scan options** and choose **Microsoft Defender Offline scan**.
3. Click **Scan now**. The laptop will restart into a special environment and scan before Windows loads — this catches rootkits that hide from normal scans.
4. Remove anything it finds and restart. If you run a third-party antivirus, consider fully uninstalling it temporarily as well — its own kernel driver could be the trigger.

### Fix 5: Repair corrupted system files

Clean up any damage to Windows' own components.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow` and let it finish (10–15 minutes).
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` — needs an internet connection.
4. Restart. If SFC found and fixed corruption, that may have been your entire problem. Kernel-level corruption like this is closely related to errors such as [kernel mode heap corruption](/articles/how-to-fix-kernel-mode-heap-corruption/), which the same repair tools address.

### Fix 6: Test your RAM

Do this especially if the blue screens name a different file each time.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Let the Windows Memory Diagnostic complete. If it reports errors, reseat your RAM sticks (if removable) and test again; a stick that consistently fails needs replacing.
4. For a definitive test, run MemTest86 from a USB drive for at least two full passes.

### Fix 7: Reset or clean-install Windows

When every driver is current, the files are clean, the RAM passes, and it still crashes, the installation itself is suspect.

1. Back up your files.
2. Go to **Settings > System > Recovery > Reset PC**, choose **Remove everything**, and pick **Cloud download**.
3. After setup, install drivers from the laptop manufacturer's site before anything else, and test stability before reinstalling third-party apps one by one. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the reset options in full if you need guidance.

## Closing

SYSTEM_SERVICE_EXCEPTION is almost always a driver telling the kernel to do something illegal — and the blue screen frequently names the guilty `.sys` file, which makes your job much easier. Update or roll back that driver, scan for malware, repair system files, and test the RAM, in that order. One of those steps fixes it for nearly everyone; the trick is not skipping the easy wins before reaching for the nuclear options.
