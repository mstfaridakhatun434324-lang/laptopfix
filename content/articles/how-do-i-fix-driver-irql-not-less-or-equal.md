---
title: "How to Fix DRIVER_IRQL_NOT_LESS_OR_EQUAL"
slug: how-do-i-fix-driver-irql-not-less-or-equal
date: 2026-09-30
categories: ["windows-errors"]
tags: ["blue screen", "driver_irql", "drivers"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL means a driver touched memory it shouldn't have. Identify the driver, update or remove it, and end the crashes."
thumbnail: "/images/thumbs/how-do-i-fix-driver-irql-not-less-or-equal.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "Windows drivers run at different privilege levels called IRQLs. This stop code means a driver tried to access memory at an IRQL where that access isn't allowed — essentially a driver reaching for memory it had no business touching. It's one of the most common blue screens in existence, and it's almost always a specific buggy driver rather than a Windows problem."
  - q: "Which drivers cause this error most often?"
    a: "Network drivers are the classic offenders — the error very often names ndis.sys, which is Windows' network driver interface, meaning the real culprit is your Wi-Fi or Ethernet driver. Graphics drivers, storage drivers, and antivirus filter drivers round out the usual suspects. The file named on the blue screen tells you exactly where to look."
  - q: "Can faulty RAM cause DRIVER_IRQL_NOT_LESS_OR_EQUAL?"
    a: "Yes, though it's less common than a bad driver. Defective memory can corrupt a driver's data, making a healthy driver crash as if it were buggy. The telltale sign is the named file changing from crash to crash — if it's a different driver every time, test the RAM before chasing drivers. Consistent naming means it's really that driver."
  - q: "Why does it happen when I connect to Wi-Fi or plug in USB?"
    a: "Because that's when the relevant driver activates. A Wi-Fi driver with a bug in its power-state handling crashes the moment it tries to connect; a USB driver bug triggers when a device enumerates. If you can tie crashes to a specific action like that, you've essentially identified the driver — update or reinstall that device's driver first."
---

DRIVER_IRQL_NOT_LESS_OR_EQUAL is the blue screen most Windows users will meet at least once. The name is pure jargon, but the meaning is simple: a driver tried to touch memory it wasn't allowed to touch, and Windows stopped it cold.

The best part about this error is that the blue screen usually names the guilty file. That turns a vague crash into a targeted repair job. Here's how to read the clue and fix it.

## Why this happens

- **Buggy network driver.** Wi-Fi and Ethernet drivers are the number one cause; ndis.sys on the screen means "look at your network driver."
- **Outdated graphics or storage driver.** These run at high privilege and crash hard when buggy.
- **Antivirus or VPN filter drivers.** Deep hooks that mishandle memory access.
- **Corrupted driver files.** A bad install or disk error damaging a driver that used to work.
- **Bad RAM.** Corrupting driver data so healthy drivers crash.
- **Recent driver update.** A new version introducing a regression.
- **Overclocking.** Unstable clocks corrupting driver operations.

## How to fix it

Work through these in order, from Fix 1 onward, and stop as soon as the crashes stop.

### Fix 1: Read the file name on the blue screen

This is the whole game for this stop code — the file name is your diagnosis.

1. Next time it crashes, note the file in parentheses, e.g. `DRIVER_IRQL_NOT_LESS_OR_EQUAL (ndis.sys)`.
2. Common translations: `ndis.sys` means your network driver, `nvlddmkm.sys`/`atikmdag.sys` mean GPU driver, `ntfs.sys` points at storage or the file system.
3. Search the exact file name if you don't recognize it — driver file names are well documented.
4. If the file is different every crash, skip to Fix 5 (RAM test) — that's the bad-memory pattern.
5. If it's consistent, that device's driver is your target for Fix 2.

### Fix 2: Update the identified driver

Go straight at the driver the blue screen named.

1. Press **Win + X** and open **Device Manager**.
2. Find the device matching the file: network adapters for ndis.sys, display adapters for GPU files, storage controllers for storport-related names.
3. Right-click, choose **Update driver > Search automatically for drivers**.
4. If Windows finds nothing, download the latest from the device maker's site — for network chips, [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) is handy.
5. Restart and test the exact scenario that was crashing (connecting to Wi-Fi, gaming, etc.).

### Fix 3: Roll back if an update started it

A driver that worked for months and broke after an update should simply be reverted.

1. In **Device Manager**, right-click the device and open **Properties**.
2. On the **Driver** tab, click **Roll Back Driver** if available.
3. Restart and test.
4. If Roll Back is greyed out, uninstall the device (checking **Attempt to remove the driver**), restart, and let Windows install its older built-in driver.
5. Pause driver updates temporarily so the bad version doesn't reinstall itself overnight.

### Fix 4: Remove VPN, firewall, and antivirus filters

These install network filter drivers that are notorious for IRQL crashes.

1. Uninstall any third-party VPN client completely.
2. If you run a third-party firewall or antivirus, update it first and test — then uninstall it with the vendor's removal tool if crashes continue.
3. Windows Security and the built-in firewall cover you during testing.
4. Run for several days without the third-party software.
5. If stable, reinstall only the latest versions from scratch, one at a time, to identify the offender.

### Fix 5: Test your RAM

Especially important if the named file keeps changing between crashes.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Let the full test finish.
3. Check results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
4. Disable XMP/DOCP in the BIOS and retest if the quick test passes but you still suspect memory.
5. Replace any failing stick — see the [MEMORY_MANAGEMENT guide](/articles/memory-management-bsod-windows-11-fix/) for the full memory troubleshooting path.

### Fix 6: Repair system files

Corrupted Windows driver-framework files can make good drivers crash.

1. Open **Terminal (Admin)** from the **Win + X** menu.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart.
4. Run SFC once more to confirm a clean second pass.
5. If SFC repeatedly finds corruption it can't fix, the drive may be damaging files — run `chkdsk C: /f` as well.

### Fix 7: Update the BIOS and chipset drivers

Firmware-level bugs in interrupt handling cause IRQL crashes that no driver update fixes.

1. Check your BIOS version with `msinfo32`.
2. Visit your laptop maker's support page for updates to BIOS and chipset drivers.
3. Flash the BIOS with the charger connected and everything closed.
4. Install the chipset package after the BIOS update.
5. Load BIOS defaults afterward if you'd previously changed interrupt or power-related settings.

### Fix 8: Clean install the driver stack via reset

When multiple drivers seem implicated, start the software side over.

1. Back up your files.
2. Go to **Settings > System > Recovery > Reset PC**, choose **Keep my files**, and use **Cloud download**.
3. After setup, install drivers in this order: chipset, storage, network, graphics — all from the laptop maker's site.
4. Test stability before installing VPN, antivirus, or utility software.
5. Add third-party software back one program per day so any returning crash points straight at the culprit.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL is one of the friendliest blue screens to troubleshoot because it usually tells you exactly which driver to fix. Read the file name, update or roll back that driver, and clear out filter software — that resolves the vast majority. For crashes where the blame shifts between drivers, suspect the RAM and follow the [SYSTEM_SERVICE_EXCEPTION guide](/articles/how-to-fix-system-service-exception-reddit/), which covers the same driver-hunting technique in more depth.
