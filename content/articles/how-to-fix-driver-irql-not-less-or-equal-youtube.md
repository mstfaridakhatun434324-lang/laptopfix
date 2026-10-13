---
title: "Fixing DRIVER_IRQL_NOT_LESS_OR_EQUAL Blue Screens"
slug: how-to-fix-driver-irql-not-less-or-equal-youtube
date: 2026-09-26
categories: ["windows-errors"]
tags: ["blue screen", "drivers", "windows 11"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL means a driver touched memory it shouldn't. Identify the bad driver and fix it with these proven steps."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal-youtube.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "Stop code 0x000000D1: a driver tried to access memory at an improper interrupt level. Translation — a driver bug, usually in a network, storage, or graphics driver. The blue screen often names the offending .sys file, which tells you exactly which driver to fix."
  - q: "How do I find which driver caused it?"
    a: "Read the file name on the blue screen (e.g., ndis.sys, nvlddmkm.sys). If you missed it, check C:\\Windows\\Minidump for dump files and open Event Viewer's BugCheck entries. The named file maps directly to a device or driver package."
  - q: "Will updating all my drivers fix it?"
    a: "Updating the specific faulty driver fixes it; blindly updating everything can introduce new problems. Identify the culprit first, then update or roll back just that driver from the manufacturer's official site."
  - q: "Can faulty RAM cause this error too?"
    a: "Occasionally. If no driver is ever named and crashes are random, test your RAM with Windows Memory Diagnostic. But in the majority of cases this stop code is purely a driver problem."
---
DRIVER_IRQL_NOT_LESS_OR_EQUAL (stop code 0x000000D1) is Windows catching a driver red-handed: it tried to touch memory it had no business touching, at a processor priority level where that's forbidden. The good news is that this error usually names the guilty driver right on the blue screen — a `.sys` file that tells you where to aim your fix.

If you caught the file name, you're halfway done. If not, Fix 1 shows you how to recover it. Work through the steps in order. For the closely related non-driver variant, see our [IRQL_NOT_LESS_OR_EQUAL guide](/articles/how-to-fix-irql-not-less-or-equal-on-asus-laptop/).

## Why this happens

- **Buggy device driver.** Network, Wi-Fi, graphics, and storage drivers are the classic offenders.
- **Driver updated to a bad version.** A new release introduces the bug — very common.
- **Corrupted driver files.** Disk errors or interrupted installs damage driver binaries.
- **Conflicting drivers.** Two drivers fighting over the same hardware or memory range.
- **Overclocked hardware.** Unstable clocks cause drivers to misbehave at high interrupt levels.
- **Faulty RAM.** Rare for this code, but bad memory can corrupt driver operations.
- **Malware-infected drivers.** Rootkits sometimes hook drivers and trigger these faults.

## How to fix it

Work through these in order — identify the driver first.

### Fix 1: Identify the faulty driver from the crash data

Don't guess — get the name.

1. If the blue screen named a file (like `rtwlane.sys`, `nvlddmkm.sys`, `ndis.sys`), write it down. That file identifies the driver.
2. If you missed it, boot into Safe Mode (force WinRE via 2-3 interrupted boots, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**).
3. Open **Event Viewer** (**Win + X > Event Viewer**) and go to **Windows Logs > System**.
4. Find **BugCheck** events — the details include the stop code and often the driver name.
5. Common mappings: `ndis.sys`/`netio.sys` = network stack, `nvlddmkm.sys` = NVIDIA graphics, `rtwlane.sys` = Realtek Wi-Fi, `storahci.sys`/`stornvme.sys` = storage.
6. Once you know the driver, skip straight to Fix 3 for the targeted fix.

### Fix 2: Boot into Safe Mode and run a malware scan

Rule out malicious drivers before touching legitimate ones.

1. Boot into Safe Mode with Networking (press **5** at Startup Settings).
2. Run a full scan with Windows Security: **Settings > Privacy & security > Windows Security > Virus & threat protection > Scan options > Full scan**.
3. Also run a second-opinion scan with the free Microsoft Safety Scanner if you suspect a rootkit.
4. If malware is found and removed, restart normally and monitor — infected drivers were likely the cause.
5. If the system is clean, continue to Fix 3.
6. Keep Windows Security's real-time protection on going forward; disabled protection invites driver-level malware.

### Fix 3: Update or roll back the specific driver

Targeted fix for the identified culprit.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Find the device matching your faulty driver (Network adapters for Wi-Fi drivers, Display adapters for GPU drivers).
3. Right-click it, choose **Properties > Driver**, and check the driver date and version.
4. If the crashes started after an update, click **Roll Back Driver** and follow the prompts.
5. Otherwise, click **Update driver > Search automatically for drivers**.
6. For the best result, download the driver from the manufacturer's official site — [Intel](https://www.intel.com/content/www/us/en/support/detect.html) for Intel Wi-Fi/BT or [NVIDIA](https://www.nvidia.com/Download/index.aspx) for graphics — and install it manually over the old one.

### Fix 4: Use Driver Verifier to catch the culprit (advanced)

If no driver was named, make Windows catch it in the act.

1. Press **Win + R**, type `verifier.exe`, and press **Enter**.
2. Choose **Create standard settings**, then **Automatically select all drivers installed on this computer** — or better, **Select driver names from a list** and tick only third-party drivers you suspect.
3. Click **Finish** and restart. Windows now stress-tests the selected drivers.
4. Use the laptop normally. If a driver is buggy, the system will blue-screen faster and usually name the driver this time.
5. After identifying it, boot into Safe Mode, run `verifier.exe` again, choose **Delete existing settings**, and restart to turn Verifier off.
6. Important: don't leave Driver Verifier running indefinitely — it slows the system and can cause crashes on its own. Our [Driver Verifier troubleshooting guide](/articles/troubleshoot-driver-verifier-iomanager-violation/) covers Verifier-related crashes in depth.

### Fix 5: Check for corrupted system files

System driver files can be damaged too.

1. Open an elevated terminal: right-click **Start > Terminal (Admin)**.
2. Run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
3. Then:
   `sfc /scannow`
4. Restart the laptop.
5. If SFC replaced files like `ndis.sys`, the corruption was in Windows' own drivers — monitor for stability.
6. Microsoft documents the DISM/SFC repair sequence on [support.microsoft.com](https://support.microsoft.com/en-us/windows) for reference.

### Fix 6: Test the RAM

When no driver is ever named, check the hardware.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
4. If errors are found, reseat or replace the RAM.
5. Also run `chkdsk C: /f` — disk corruption can damage driver files and mimic driver bugs.
6. Clean memory plus clean drivers means the crashes should stop; if they don't, suspect the motherboard.

### Fix 7: Reset overclocks and update the BIOS

Stability issues can masquerade as driver bugs.

1. Enter BIOS/UEFI and load optimized defaults (**F9** on most systems).
2. Disable XMP/DOCP memory profiles for testing.
3. If you use tuning utilities (Intel XTU, MSI Afterburner), reset them to defaults.
4. Check your laptop maker's support site for a BIOS update and install it with the charger connected.
5. Reinstall the suspect driver cleanly after the BIOS update.
6. Test for several days under normal use. Persistent D1 crashes after all of this point to failing hardware — usually the device whose driver keeps crashing (Wi-Fi card, SSD, or GPU).

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL is one of the more diagnosable blue screens because it usually names its culprit. Take the file name seriously, fix that specific driver, and resist the urge to update everything at once. When no driver is named, Driver Verifier plus a memory test will smoke out the cause. Keep a note of which driver version is stable for your machine — the next bad update won't catch you off guard.
