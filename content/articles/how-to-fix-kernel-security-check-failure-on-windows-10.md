---
title: "KERNEL_SECURITY_CHECK_FAILURE on Windows 10: A Complete Fix Guide"
slug: how-to-fix-kernel-security-check-failure-on-windows-10
date: 2026-09-26
categories: ["windows-errors"]
tags: ["bsod", "stop code", "windows 10", "drivers"]
description: "KERNEL_SECURITY_CHECK_FAILURE blue screen on Windows 10? It's a kernel integrity check failing — usually drivers or RAM. Here's how to fix it."
thumbnail: "/images/thumbs/how-to-fix-kernel-security-check-failure-on-windows-10.webp"
faqs:
  - q: "What does KERNEL_SECURITY_CHECK_FAILURE mean?"
    a: "Windows runs integrity checks on critical kernel data structures. This stop code means one of those checks failed — a driver corrupted a protected structure, memory flipped bits in it, or a file system error damaged it. Windows crashes deliberately rather than run with compromised kernel integrity."
  - q: "Is this error caused by a virus?"
    a: "Unlikely. Despite the word 'security' in the name, this is almost always a driver bug or hardware problem, not malware. The 'security check' is Windows verifying its own internal data structures, not scanning for threats."
  - q: "Can bad RAM cause KERNEL_SECURITY_CHECK_FAILURE?"
    a: "Yes — it's one of the top causes. Failing memory corrupts the kernel structures Windows is checking, which trips the integrity check. If the crash names a different driver or file each time, test your RAM before chasing drivers."
  - q: "Should I update to Windows 11 to fix it?"
    a: "Not as a fix for this specific error. The same driver or RAM problem will usually follow you to Windows 11. Fix the root cause on Windows 10 first; upgrade later for your own reasons, not as a troubleshooting step."
---

`KERNEL_SECURITY_CHECK_FAILURE` sounds like your laptop caught a hacker, but the reality is more mundane: Windows constantly verifies the integrity of its own kernel data structures — linked lists, security tokens, pool allocations — and this blue screen means one of those checks failed. Something corrupted a structure Windows considers sacred. Nine times out of ten, that "something" is a buggy driver or failing RAM.

On Windows 10 laptops this crash is well-understood, and the fix path is methodical: check what changed recently, update the usual driver suspects, verify memory, and repair system files. Let's work through it.

## Why this happens

- **Buggy or outdated drivers**: The leading cause. A driver that corrupts kernel pool memory or mishandles linked lists trips the integrity check. Graphics and storage drivers top the list.
- **Failing RAM**: Bad memory flips bits in the kernel structures Windows is verifying. When the crash names different modules each time, memory is the prime suspect.
- **Corrupted system files**: Damage to kernel components means the structures being checked are built wrong from the start.
- **Overclocked CPU or RAM**: Unstable overclocks corrupt kernel data under load. Even "mild" overclocks or aggressive XMP profiles can do it.
- **Disk errors corrupting paged kernel data**: Bad sectors in the page file or system area corrupt kernel structures when they're paged in from disk.
- **Incompatible antivirus or system utilities**: Kernel-level security software that hasn't kept up with Windows 10 updates can corrupt the structures it hooks into.

## How to fix it

Work through these in order — driver and software causes first, hardware verification after.

### Fix 1: Check what changed before the crashes started

The most useful diagnostic question is "what's new?"

1. Open **Settings** > **Update & Security** > **Windows Update** > **View update history**. Note anything installed just before the first crash.
2. Open **Device Manager** (**Win + X**) and look for devices with yellow warnings, especially under **Display adapters** and **IDE ATA/ATAPI controllers**.
3. Think about new software: VPN clients, antivirus changes, RGB/fan utilities, virtual-machine tools — anything that installs a driver.
4. If you can identify the change, undo it first (roll back the driver, uninstall the update or program) before doing anything else.

### Fix 2: Update graphics and chipset drivers from the manufacturer

Generic or outdated graphics drivers are the single most common trigger.

1. For NVIDIA laptops, download the latest driver from [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx) and choose **Custom install** > **Clean install**.
2. For AMD graphics, get the latest Adrenalin driver from AMD's official support site rather than Windows Update.
3. For Intel graphics and chipset, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Restart and use the laptop normally for a day or two before declaring victory — these crashes can be intermittent.

### Fix 3: Run the built-in hardware troubleshooters and memory test

Rule out the hardware suspects with the tools Windows already has.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. Let both memory passes complete. Any error — even a single one — means the RAM needs replacing.
3. Back in Windows, open **Terminal (Admin)** and run `chkdsk C: /f /r`. Type **Y** when asked to schedule it, then restart — this checks the disk for bad sectors that could be corrupting paged kernel data. It can take an hour or more on large drives.

The [24H2 KERNEL_SECURITY_CHECK_FAILURE guide](/articles/how-to-fix-kernel-security-check-failure-in-windows-11-24h2/) covers the same crash on newer builds if you've since upgraded.

### Fix 4: Repair system files with SFC and DISM

Corrupted kernel files fail their own integrity checks — repair them.

1. Open an elevated Command Prompt: **Win + X** > **Command Prompt (Admin)** or **Windows PowerShell (Admin)**.
2. Run `sfc /scannow` and wait for completion.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. If `sfc` reported it fixed corrupt files, there's a good chance your crashes are done.

### Fix 5: Remove or update kernel-level third-party software

Antivirus, VPNs, and system utilities hook the kernel — and outdated hooks corrupt what they touch.

1. Update your antivirus to the latest version. If crashes persist, temporarily uninstall it (**Settings** > **Apps**) and rely on Windows Defender for a few days as a test.
2. Do the same test with VPN clients and any "system optimizer" or driver-updater utilities.
3. Check **Device Manager** > **View** > **Show hidden devices** for leftover grayed-out devices from uninstalled software and remove them.

### Fix 6: Reset overclocks and memory settings to stock

Unstable clocks corrupt kernel structures under load — the textbook cause of intermittent instances of this stop code.

1. If you use any overclocking utility (Intel XTU, Ryzen Master, MSI Afterburner with CPU tweaks), reset everything to defaults.
2. Restart into BIOS/UEFI (**F2** or **Del** at the manufacturer's splash screen).
3. Disable **XMP**/**DOCP** memory profiles and set memory to **Auto**.
4. If the BIOS has a "Load Optimized Defaults" option, use it, then save and exit (**F10**).
5. Test for several days at stock settings.

A related buffer-overflow crash with a similar fix path is [DRIVER_OVERRAN_STACK_BUFFER](/articles/how-to-fix-driver-overran-stack-buffer-after-windows-11-update/) — worth checking if your dumps mention stack corruption.

### Fix 7: Update Windows 10 fully, then consider a repair install

An out-of-date Windows 10 can have known kernel bugs that newer cumulative updates fixed.

1. Go to **Settings** > **Update & Security** > **Windows Update** and install everything offered, including optional driver updates — then reboot.
2. Check Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) for any known issues with your specific build.
3. If crashes persist on a fully updated system with current drivers and clean memory tests, do an in-place repair install: download the Windows 10 Media Creation Tool, run it, and choose **Upgrade this PC now**. It reinstalls Windows while keeping files and apps.
4. If even that fails, the evidence points to hardware — RAM first, then the motherboard — and it's time for a repair shop or warranty claim.

## Closing

`KERNEL_SECURITY_CHECK_FAILURE` is Windows catching corruption in its own most-trusted data — which is actually good news, because it means the protection worked and the cause is finite: a driver, the RAM, or damaged system files. Work the list top to bottom, resist the urge to reinstall Windows before Fix 4, and give each change a couple of days of real use. Most Windows 10 laptops are stable again by Fix 4 or Fix 5, with nothing lost but the crashing.
