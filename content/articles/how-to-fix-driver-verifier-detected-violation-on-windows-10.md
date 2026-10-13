---
title: "How to Fix DRIVER_VERIFIER_DETECTED_VIOLATION on Windows 10"
slug: how-to-fix-driver-verifier-detected-violation-on-windows-10
date: 2026-10-03
categories: ["windows-errors"]
tags: ["bsod", "driver verifier", "stop code", "windows 10"]
description: "DRIVER_VERIFIER_DETECTED_VIOLATION crashing your Windows 10 laptop? Here's what the stop code means and the exact order to fix it in."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-detected-violation-on-windows-10.webp"
faqs:
  - q: "What does DRIVER_VERIFIER_DETECTED_VIOLATION mean on Windows 10?"
    a: "It means Windows' Driver Verifier — a built-in diagnostic tool — caught a driver breaking the rules, usually an illegal memory access or bad I/O call. Someone (or some troubleshooting guide) enabled Verifier, and now it's deliberately crashing the PC to expose the buggy driver."
  - q: "Should I just turn off Driver Verifier?"
    a: "Yes, as the first step. Verifier is a temporary diagnostic, not something to leave running. Run verifier /reset from an elevated Command Prompt and reboot. But don't stop there — find and fix the driver it caught, or the underlying bug remains."
  - q: "Can DRIVER_VERIFIER_DETECTED_VIOLATION damage my hardware?"
    a: "No. The blue screen is a protective stop, not damage. Verifier crashes are intentional and controlled. Your hardware is fine — the problem is a misbehaving driver that needs updating, rolling back, or removing."
  - q: "What if Windows 10 won't boot because of the Verifier crash loop?"
    a: "Boot into Safe Mode (interrupt boot three times to reach Automatic Repair, then Troubleshoot, Advanced options, Startup Settings) and run verifier /reset from there. Safe Mode loads a minimal driver set, so Verifier usually stays quiet long enough for you to disable it."
---

`DRIVER_VERIFIER_DETECTED_VIOLATION` is a blue screen with a slightly unusual story: it means a diagnostic tool called Driver Verifier did its job. Somebody — maybe you following an earlier troubleshooting guide, maybe a support tech — turned Verifier on to catch a misbehaving driver, and Verifier caught one. The problem is that Verifier was never turned back off, so now it crashes your Windows 10 laptop on purpose every time that driver misbehaves.

The fix has two halves: stop the intentional crashes by disabling Verifier, then deal with the actual buggy driver it exposed. Here's the order.

It's worth understanding why Verifier crashes feel so aggressive: unlike a normal driver bug that might only glitch occasionally, Verifier is configured to bug-check the system the instant it detects a rule violation. That's why the crashes seem to come out of nowhere and repeat so reliably. Once you internalize that the blue screen is the diagnostic working as designed — not your laptop falling apart — the fix path becomes much less stressful.

## Why this happens

- **Verifier left enabled after troubleshooting**: This is the cause in the large majority of cases. Verifier is designed to run for a short diagnostic session. Left on, it converts every minor driver misstep into a blue screen.
- **A genuinely buggy driver**: Verifier caught something real — a driver making illegal memory accesses or invalid I/O calls. Old third-party drivers for printers, USB devices, VPNs, and gaming peripherals are classic offenders on Windows 10.
- **Driver incompatible with a Windows 10 update**: A driver that passed Verifier's checks on an older build can fail them after a feature update changes kernel behavior underneath it.
- **Overclocking or unstable hardware stressing drivers**: Marginal RAM or an unstable overclock can cause driver operations to fail in ways Verifier interprets as violations.
- **Corrupted driver files**: Partially installed or damaged driver files behave unpredictably, and Verifier is specifically designed to catch exactly that unpredictability.
- **Conflicting low-level software**: Antivirus drivers, disk encryption, and virtualization tools operate at the driver level. When two of them disagree about I/O rules, Verifier flags the conflict.

## How to fix it

Work through these in order. The first fix stops the bleeding; the rest cure the disease.

### Fix 1: Reset Driver Verifier

Always step one. This stops the deliberate crashes.

1. If Windows boots, press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Run:

   ```cmd
   verifier /reset
   ```

3. Restart. If the machine was in a crash loop, do this from Safe Mode instead: interrupt the boot three times to reach **Automatic Repair**, then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, press **4**, and run the command there.

### Fix 2: Find the driver Verifier blamed

Check the crash dump so you're not updating drivers blindly.

1. Open **File Explorer** and go to `C:\Windows\Minidump`.
2. Look at the newest `.dmp` file. You can analyze it with WinDbg, or follow the practical walkthrough in [how to check minidump files on Windows 11](/articles/how-to-check-minidump-files-on-windows-11/) — the same steps work on Windows 10.
3. Note the driver name in the crash details (something like `rzudd.sys` or `VBoxUSBMon.sys`). That's your target.

### Fix 3: Update the offending driver

A fixed driver from the vendor is the cleanest resolution.

1. Press **Win + X** and open **Device Manager**.
2. Find the device, right-click it, and choose **Update driver** > **Search automatically for drivers**.
3. If Windows finds nothing new, go to the manufacturer's website directly and download the latest Windows 10 driver for your exact model.
4. For graphics, use [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel's tool](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 4: Roll back if the driver recently updated

Sometimes the "buggy" driver is simply a bad new version.

1. In **Device Manager**, right-click the device and open **Properties**.
2. On the **Driver** tab, click **Roll Back Driver** if it's available.
3. Choose a reason and restart. If the crashes stop, stay on the older version until the vendor ships a fix.

### Fix 5: Remove the problematic software entirely

For third-party drivers (VPN clients, peripheral utilities, old printer software), removal beats updating.

1. Open **Settings** > **Apps** > **Apps & features**.
2. Uninstall the software tied to the bad driver.
3. Check the vendor's site for a removal/cleanup tool — driver leftovers are common.
4. In **Device Manager**, choose **View** > **Show hidden devices** and uninstall any grayed-out remnants of the device.

### Fix 6: Check for Windows 10 updates

Microsoft and vendors ship Verifier-related fixes in cumulative updates.

1. Go to **Settings** > **Update & Security** > **Windows Update**.
2. Click **Check for updates** and install everything, including optional driver updates.
3. Restart and monitor for a day or two.

### Fix 7: Test memory and disk health

Rule out hardware making good drivers look bad.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. In an elevated **Command Prompt**, run:

   ```cmd
   chkdsk C: /f
   ```

3. If either reports errors, address the hardware — a failing stick of RAM or dying drive will keep producing "driver" crashes until replaced.

### Fix 8: Clean-install the driver stack as a last resort

If one bad driver has contaminated the stack, start fresh.

1. Download Display Driver Uninstaller (DDU) or the vendor's clean-install utility for the device type.
2. Boot into Safe Mode and run the clean removal.
3. Reboot normally and install only the latest driver from the vendor — skip the bundled "utility suite" if it's optional.
4. Resist the urge to re-enable Driver Verifier afterwards unless you're actively diagnosing a new problem. Verifier is a tool you turn on for a session and turn off when you're done — leaving it on is how this whole mess started.

## Closing

`DRIVER_VERIFIER_DETECTED_VIOLATION` looks alarming but it's really a diagnostic doing its job too enthusiastically. Reset Verifier, identify the driver it caught, and update or remove it — that sequence ends the crashes on virtually every Windows 10 laptop. For the Windows 11 version of this problem, see [how to fix DRIVER_VERIFIER_DETECTED_VIOLATION on Windows 11](/articles/how-to-fix-driver-verifier-detected-violation-on-windows-11/), and for the I/O-specific variant read about [DRIVER_VERIFIER_IOMANAGER_VIOLATION step by step](/articles/how-to-fix-driver-verifier-iomanager-violation-step-by-step/).
