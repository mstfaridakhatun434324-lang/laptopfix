---
title: "How to Fix IRQL Not Less or Equal Blue Screen on Windows 11"
slug: irql-not-less-or-equal-windows-11-fix
date: 2026-09-19
categories: ["windows-errors"]
tags: ["bsod", "irql-not-less-or-equal", "windows-11"]
description: "IRQL_NOT_LESS_OR_EQUAL on Windows 11 is a driver or RAM issue in disguise. Use these steps to pin down the cause and end the crashes."
thumbnail: "/images/thumbs/irql-not-less-or-equal-windows-11-fix.webp"
faqs:
  - q: "What does IRQL_NOT_LESS_OR_EQUAL mean in plain English?"
    a: "It's a blue screen (stop code 0x0000000A) that happens when a driver or system process tries to access memory at an interrupt level that's too high — basically, a driver reached for memory it wasn't allowed to touch right then. Faulty drivers cause it most often, followed by bad RAM."
  - q: "The blue screen names a driver file. What should I do?"
    a: "Write down the exact .sys filename. Then update, roll back, or reinstall that specific driver — Fix 3 below walks through it. Files like nvlddmkm.sys (NVIDIA), Netwtw10.sys (Intel Wi-Fi), and rtwlane.sys (Realtek) are the usual repeat offenders."
  - q: "Why does it happen mostly when I play games?"
    a: "Gaming stresses the GPU driver, network driver, and RAM simultaneously — the three most common triggers. An unstable GPU driver or a marginal RAM stick that survives light use will crash under gaming load. Update the graphics driver and test your RAM."
  - q: "Can overclocking cause IRQL_NOT_LESS_OR_EQUAL?"
    a: "Absolutely. Overclocked RAM (XMP profiles included), CPU, or GPU can all produce this stop code when the overclock isn't fully stable. Reset everything to stock speeds as a diagnostic step — if the crashes stop, your tuning was the problem."
---
IRQL_NOT_LESS_OR_EQUAL (stop code 0x0000000A) is one of the most frequently seen blue screens on Windows 11, and its name hides a simple story: a driver tried to touch memory it had no right to touch at that moment. The kernel caught it and crashed the system rather than let corruption spread.

On laptops, the culprits are almost always a misbehaving driver — graphics and Wi-Fi drivers lead the pack — or RAM that's starting to fail. The fixes below will help you tell the two apart and fix whichever one you've got.

## Why this happens

- **Faulty or incompatible drivers.** Graphics, Wi-Fi, and storage drivers that access memory incorrectly are the number one cause, especially after a driver or Windows update.
- **Failing RAM.** Bad memory returns wrong data when drivers read it, which the kernel interprets as an illegal access.
- **Corrupted system files.** Damage to Windows' own kernel components can trigger the error from legitimate operations.
- **Overclocking or unstable XMP profiles.** RAM running beyond its stable limits produces exactly this kind of intermittent illegal access.
- **Malware.** Rootkits and other kernel-level malware perform the same illegal memory accesses this stop code detects.
- **Hardware conflicts after an upgrade.** A newly installed SSD, RAM stick, or dock can introduce driver or resource conflicts.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once the crashes stop.

### Fix 1: Identify the driver from the blue screen

The crash screen often hands you the answer directly.

1. Next time it blue-screens, look for the **"What failed:"** line near the bottom and note the exact `.sys` filename — photograph it with your phone if it's gone too fast.
2. Common offenders: `nvlddmkm.sys` (NVIDIA graphics), `Netwtw10.sys` / `Netwtw12.sys` (Intel Wi-Fi), `rtwlane.sys` (Realtek Wi-Fi), `storport.sys` (storage).
3. If a file is named, jump to Fix 3 and target that driver specifically. If no file is named, continue in order — the pattern still matters, as our [IRQL troubleshooting deep-dive](/articles/irql-not-less-or-equal-troubleshooting/) explains.

### Fix 2: Boot into Safe Mode to confirm it's a third-party driver

A quick isolation test before you change anything.

1. Interrupt the boot three times (hold the power button at the logo screen) to reach the **Windows Recovery Environment**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **5** for **Safe Mode with Networking**.
3. Use the laptop for a while in Safe Mode. If it's stable here, a third-party driver is definitely the cause — Safe Mode doesn't load them.

### Fix 3: Update, roll back, or reinstall the problem driver

This resolves the majority of IRQL crashes.

1. Press **Win + X** and open **Device Manager**.
2. For the device matching your suspect driver (**Display adapters** for GPU files, **Network adapters** for Wi-Fi files), right-click and choose **Update driver > Search automatically for drivers**.
3. If the crashes started after a recent update, open **Properties > Driver tab** and click **Roll Back Driver** instead.
4. For the cleanest result, download the driver from the source: your laptop maker's support page, [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) for NVIDIA GPUs, or [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel Wi-Fi and chipset.
5. For NVIDIA specifically, choose **Custom install** and check **Perform a clean installation** to wipe the old driver's remnants.
6. Restart and test under the conditions that used to crash it.

### Fix 4: Run a malware scan

Kernel-level malware causes this exact stop code.

1. Open **Windows Security > Virus & threat protection > Scan options**.
2. Select **Microsoft Defender Offline scan** and click **Scan now**. The laptop reboots into a pre-Windows environment that catches rootkits hiding from normal scans.
3. Remove anything found. If you use third-party antivirus, fully uninstall it temporarily too — its own kernel driver is a candidate cause.

### Fix 5: Repair system files

Fix corruption in Windows' own components.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow` — allow 10–15 minutes.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. These tools also fix sibling errors like the ones covered in our guide to the [best way to fix IRQL errors](/articles/best-way-to-fix-irql-not-less-or-equal/).

### Fix 6: Test and reseat your RAM

Do this if the crashes name different files each time or happen randomly.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. If errors are reported, power off, open the RAM compartment, and reseat the sticks firmly.
3. With two sticks, test one at a time to find the bad one, and replace it with matching specs.
4. If you enabled XMP or any memory overclock in the BIOS, disable it — unstable memory tuning is a classic cause of this stop code.
5. For a definitive test, run MemTest86 from a USB drive for two full passes.

### Fix 7: Check for overheating and reset the system if needed

Heat-induced instability and deep system corruption are the remaining suspects.

1. Monitor CPU/GPU temperatures under load with HWMonitor — sustained temps above 95°C cause exactly these crashes. Clean vents and fans with compressed air.
2. If everything else failed, go to **Settings > System > Recovery > Reset PC**, choose **Remove everything** with **Cloud download**, and reinstall drivers from the manufacturer before anything else.
3. Crashes on a clean install with passing RAM tests point to a motherboard fault — get professional diagnosis. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the full reset documentation.

## Closing

IRQL_NOT_LESS_OR_EQUAL looks technical, but your job is simple: find whether it's a driver or the RAM. The blue screen often names the driver file outright — update or roll back that driver and you're done. When it doesn't, the pattern tells the story: same trigger every time means driver, random chaos means RAM. Work the list in order and you'll land on the right answer without guessing.
