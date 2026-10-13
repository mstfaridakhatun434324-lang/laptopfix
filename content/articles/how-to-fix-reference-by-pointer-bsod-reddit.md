---
title: "REFERENCE_BY_POINTER Blue Screen in Windows 11: Causes and Fixes"
slug: how-to-fix-reference-by-pointer-bsod-reddit
date: 2026-09-06
categories: ["windows-errors"]
tags: ["blue screen", "reference by pointer", "stop code 0x18", "driver bug", "windows 11"]
description: "REFERENCE_BY_POINTER (0x18) crashing your Windows 11 laptop? Learn what this driver reference-count bug means and fix it in 7 steps."
thumbnail: "/images/thumbs/how-to-fix-reference-by-pointer-bsod-reddit.webp"
faqs:
  - q: "What does REFERENCE_BY_POINTER mean?"
    a: "It's stop code 0x00000018. Windows keeps a reference count on internal driver objects, and when a driver decrements that count below zero (or otherwise makes it illegal), the system crashes immediately. In plain terms: a buggy driver mishandled a kernel object, and Windows stopped everything rather than risk corruption."
  - q: "Is REFERENCE_BY_POINTER caused by bad RAM?"
    a: "Rarely, but it happens. Faulty memory can corrupt the object headers Windows uses for reference counting, which looks identical to a driver bug. If updated drivers don't stop the crashes, run mdsched.exe to test your RAM before buying replacements."
  - q: "Can overclocking cause this blue screen?"
    a: "Yes. Overclocked CPU or RAM introduces timing errors that corrupt driver data structures, including reference counts. If you overclocked anything, restore stock clocks first — many 0x18 crashes vanish the moment you do."
  - q: "How do I find which driver caused it?"
    a: "Check the blue screen itself for a .sys filename, or open C:\\Windows\\Minidump and analyze the newest .dmp file with WinDbg or BlueScreenView. The named driver is your prime suspect — update it, roll it back, or remove its device."
---

REFERENCE_BY_POINTER (stop code 0x00000018) is one of the more cryptic blue screens you'll run into. The name sounds like a programmer's inside joke, but the underlying idea is simple: Windows tracks how many parts of the system are "using" each internal object with a reference count. When a driver messes that count up — dropping it below zero, for example — Windows can't trust its own bookkeeping anymore, so it crashes rather than risk silent corruption.

The good news is that this is almost always a software problem, which means it's fixable without buying anything. Drivers are the culprit in the overwhelming majority of cases, with memory and overclocking as the runners-up.

## Why this happens

- **A buggy device driver decrements an object reference illegally.** This is the textbook 0x18 cause — a driver bug in how it opens and closes kernel objects.
- **Outdated or beta drivers.** Drivers written for older Windows builds mishandle object lifetimes on Windows 11, especially after a feature update.
- **Antivirus and filter drivers.** Kernel-level security, backup, and disk-encryption drivers hook deep into object management and are frequent 0x18 offenders.
- **Faulty RAM corrupting object headers.** Bad memory flips bits in the reference-count fields, producing crashes that blame innocent drivers.
- **Overclocked CPU or memory.** Unstable overclocks cause exactly the kind of timing corruption that mangles reference counts.
- **Corrupted system files.** Damage to core Windows files can break the reference-counting machinery itself.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Identify the crashing driver from the dump file

Don't guess; find out which driver Windows blamed.

1. If the blue screen showed a filename like `drivername.sys`, write it down — that's your suspect.
2. Open **File Explorer** and navigate to `C:\Windows\Minidump` to confirm crash dumps are being saved.
3. Download and run BlueScreenView (or WinDbg from the Microsoft Store) and open the newest `.dmp` file.
4. Look at the **Caused By Driver** column — that module gets updated or removed first.
5. If every crash blames a *different* driver, suspect RAM instead of drivers and jump to Fix 5.

Knowing the exact driver saves hours. For the update-triggered variant of this crash, see our guide on [REFERENCE_BY_POINTER after a Windows 11 update](/articles/how-to-fix-reference-by-pointer-bsod-after-windows-11-update/).

### Fix 2: Update or roll back the suspect driver

Driver bugs cause the vast majority of 0x18 crashes.

1. Open **Device Manager** (press **Windows + X** and select it).
2. Find the device matching the suspect driver — GPU, network adapter, or storage controller are the usual ones.
3. Right-click it, choose **Properties > Driver**, and try **Roll Back Driver** if the crashes started after an update.
4. If rollback isn't available, choose **Update driver > Search automatically for drivers**.
5. For graphics drivers, do a clean reinstall from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) using their clean-install option.
6. Restart and use the laptop normally to confirm the crashes are gone.

### Fix 3: Run Driver Verifier to catch the guilty driver

If dumps are inconclusive, Driver Verifier stresses drivers until the bad one reveals itself.

1. Press **Windows + R**, type `verifier`, and press Enter.
2. Select **Create standard settings**, then **Automatically select unsigned drivers** — or choose **Select driver names from a list** and tick recently updated third-party drivers.
3. Click **Finish** and restart when prompted.
4. Use the laptop normally; Verifier will blue-screen *faster* when the faulty driver misbehaves, and this time the dump will name it clearly.
5. After identifying the driver, boot into Safe Mode, run `verifier /reset`, and restart to turn Verifier off.

Leave Verifier running only until you catch the culprit — it intentionally makes crashes more likely while active.

### Fix 4: Remove problematic filter and security drivers

Antivirus, VPN, and backup tools install kernel drivers that are classic 0x18 sources.

1. Open **Settings > Apps > Installed apps** and look for third-party antivirus, VPN clients, or disk utilities installed around the time crashes began.
2. Uninstall them one at a time, restarting after each, and test for stability.
3. Windows Defender activates automatically when third-party antivirus is removed, so you're never unprotected.
4. If a specific product is confirmed as the cause, check the vendor's site for an updated version before reinstalling.
5. For persistent cases, also check **Device Manager > View > Show hidden devices** for leftover ghost drivers from uninstalled software and remove them.

General blue-screen troubleshooting steps that complement this approach are covered in our [complete Windows 11 blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 5: Test your RAM

When dumps blame different drivers each time, memory is the likely villain.

1. Press **Windows + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**.
3. Let the full test complete — don't interrupt it.
4. After reboot, open **Event Viewer > Windows Logs > System** and look for **MemoryDiagnostics-Results** entries.
5. If errors are found, reseat the RAM modules; if errors persist, replace the faulty stick.

### Fix 6: Reset any overclocking to stock

Overclocks are a silent cause of reference-count corruption.

1. Restart and enter your BIOS/UEFI (usually **Del**, **F2**, or **F10** at boot).
2. Disable XMP/EXPO memory profiles and any CPU overclock or undervolt.
3. Select **Load Optimized Defaults** (or **Load Setup Defaults**) and save.
4. Boot into Windows and test for a day or two.
5. Only re-enable performance profiles after the system proves stable at stock settings.

### Fix 7: Repair system files and refresh Windows

If nothing else works, the OS itself may be damaged.

1. Open **Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. When that finishes, run `sfc /scannow` and restart.
3. If crashes continue, open **Settings > System > Recovery** and use **Reset this PC** with the **Keep my files** option.
4. Reinstall drivers one at a time from your manufacturer's support page, testing between each — if the crash returns after a specific driver, you've found it.
5. Microsoft's own [blue screen troubleshooting guide](https://support.microsoft.com/en-us/windows) covers additional recovery options if the reset doesn't finish.

## Closing

REFERENCE_BY_POINTER looks intimidating, but the fix path is mechanical: identify the driver from the dump, update or remove it, and only then suspect hardware. Most people solve it at Fix 2 or Fix 4 without spending a rupee. The one thing you shouldn't do is ignore it — a driver that's corrupting kernel objects today can take your data with it tomorrow, so work the list and get it resolved.
