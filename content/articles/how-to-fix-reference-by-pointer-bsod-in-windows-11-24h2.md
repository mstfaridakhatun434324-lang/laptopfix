---
title: "How to Fix the REFERENCE_BY_POINTER BSOD in Windows 11 24H2"
slug: how-to-fix-reference-by-pointer-bsod-in-windows-11-24h2
date: 2026-09-21
categories: ["windows-errors"]
tags: ["reference by pointer", "bsod", "0x18", "windows 11 24h2", "driver crash"]
description: "REFERENCE_BY_POINTER blue screen on Windows 11 24H2? This stop code 0x18 crash is usually a driver bug — here's how to find and fix it."
thumbnail: "/images/thumbs/how-to-fix-reference-by-pointer-bsod-in-windows-11-24h2.webp"
faqs:
  - q: "What does REFERENCE_BY_POINTER mean?"
    a: "It is stop code 0x00000018, and it means an object's reference count became invalid — usually because a driver freed the same memory object twice or mishandled a kernel object. Windows detects the inconsistency and crashes deliberately to prevent further corruption. In plain terms, a driver made a bookkeeping error with system memory."
  - q: "Is this error specific to Windows 11 24H2?"
    a: "No, the stop code exists in all modern Windows versions, but 24H2 changed enough driver behavior that older drivers which used to get away with sloppy reference counting now crash. If the blue screens started right after upgrading to 24H2, an outdated third-party driver is the overwhelmingly likely cause."
  - q: "Can RAM cause REFERENCE_BY_POINTER?"
    a: "Faulty RAM can cause almost any blue screen, including this one, but it is a less common cause than drivers for this specific code. Still worth testing with Windows Memory Diagnostic since it is free and takes under an hour. If the memory test passes clean, focus your energy on drivers."
  - q: "How do I find which driver caused it?"
    a: "Open the minidump in C:\\Windows\\Minidump with BlueScreenView or WinDbg. The 'caused by driver' field usually names the culprit directly — often a network, storage, or antivirus filter driver. Once you have the file name, you know exactly which device's driver to update or roll back."
---
REFERENCE_BY_POINTER (stop code 0x18) is one of the more cryptic blue screens Windows throws. The name sounds like a programming lecture, and honestly, it kind of is one — it means a driver messed up its internal bookkeeping of a system memory object. But you do not need to understand kernel reference counting to fix it. You just need to find the bad driver.

On Windows 11 24H2 this error has become more common because the update tightened driver behavior, exposing bugs in older drivers that previously flew under the radar. Here's the practical path to a stable system.

## Why this happens

- **An outdated third-party driver:** The classic cause — a driver written for older Windows mishandles object references under 24H2's stricter rules.
- **Network adapter drivers:** Wi-Fi and Ethernet drivers are frequent offenders for this specific stop code, especially Realtek, Intel, and Killer/Qualcomm adapters.
- **Antivirus or firewall filter drivers:** Security software hooks deep into the kernel, and older versions are notorious for reference-count bugs.
- **Recently updated drivers with regressions:** A brand-new driver version can introduce the bug — "latest" does not always mean "most stable."
- **Corrupted driver files on disk:** Partially updated or disk-damaged driver binaries behave unpredictably.
- **Faulty RAM:** Less common for this code, but bad memory cells can corrupt the reference counts Windows maintains.
- **Overclocked or unstable system:** Marginal CPU/RAM stability produces erratic driver behavior that surfaces as reference-count violations.

## How to fix it

Work through these in order, starting at Fix 1. Identifying the driver first saves you from updating things blindly.

### Fix 1: Identify the crashing driver from the minidump

Don't guess — read the crash dump and let Windows tell you which driver failed.

1. After a crash, boot back into Windows (use Safe Mode if normal boot blue-screens: interrupt startup three times to reach recovery).
2. Press **Win + R**, type `%SystemRoot%\Minidump`, and press Enter.
3. Open the newest `.dmp` file with BlueScreenView (free from NirSoft) — the lower pane highlights the driver, e.g. `Netwtw10.sys` (Intel Wi-Fi) or `rtwlane.sys` (Realtek).
4. Write down the exact file name. If the dump names `ntoskrnl.exe` only, the real culprit is hiding — proceed to Fix 5 for driver verification techniques.

Driver-caused crashes often travel together; if you also see IRQL errors, our [IRQL_NOT_LESS_OR_EQUAL guide](/articles/irql-not-less-or-equal-windows-11-fix/) covers the sibling stop code.

### Fix 2: Update the identified driver

Once you know the culprit, replace it with a current, clean version.

1. Open **Device Manager** (**Win + X > Device Manager**) and locate the device.
2. Right-click it and choose **Update driver > Search automatically for drivers**.
3. If Windows finds nothing newer, download the driver manually: for Intel hardware use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html); for your laptop model, check the manufacturer's support page for 24H2-certified drivers.
4. Install, restart, and use the laptop normally for a couple of days to confirm the crashes stop.

### Fix 3: Roll back if a recent driver update triggered it

If the blue screens started within days of a driver or Windows update, the new driver is guilty until proven innocent.

1. In **Device Manager**, right-click the device, open **Properties**, and go to the **Driver** tab.
2. Click **Roll Back Driver**, select a reason, and confirm.
3. Restart and monitor. Keep the older driver until the vendor releases a fixed version.
4. To prevent Windows Update from pushing the bad driver again, check **Settings > Windows Update > Advanced options > Optional updates** and skip that driver version.

### Fix 4: Remove or update third-party antivirus and VPN clients

Filter drivers from security software are disproportionately represented in 0x18 crashes.

1. Go to **Settings > Apps > Installed apps**.
2. Uninstall your third-party antivirus and any VPN client temporarily. Windows Security (Defender) activates automatically and protects you meanwhile.
3. Restart and test for 24-48 hours of normal use.
4. If the crashes stop, download the absolute latest version of that software from the vendor's official site and reinstall — do not reinstall the old installer you had lying around.

### Fix 5: Run Driver Verifier to catch the culprit (advanced)

If dumps only blame `ntoskrnl.exe`, use Driver Verifier briefly to force the real offender to reveal itself.

1. Press **Win + R**, type `verifier`, and press Enter.
2. Choose **Create standard settings**, then **Select driver names from a list**.
3. Select only third-party (non-Microsoft) drivers related to your suspects — network, storage, antivirus.
4. Click **Finish** and restart. Use the laptop normally; Verifier will blue-screen on the violating driver and name it in the dump.
5. **Important:** After identifying the driver, boot into Safe Mode and run `verifier /reset` to turn Verifier off. Never leave it running permanently — see our [Driver Verifier violation guide](/articles/driver-verifier-detected-violation-blue-screen-error-fix/) for why.

### Fix 6: Test memory and repair system files

Rule out hardware and corruption as contributing factors.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. After Windows boots, open **Terminal (Admin)** (**Win + X > Terminal (Admin)**) and run `sfc /scannow`.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` if SFC finds damage it cannot fix.
4. If the memory test reports errors, reseat or replace the RAM — no driver update will fix physically bad memory.

### Fix 7: Update the BIOS/UEFI firmware

On 24H2, outdated firmware can cause driver-hardware miscommunication that manifests as reference-count crashes.

1. Check your current BIOS version: press **Win + R**, type `msinfo32`, press Enter, and note **BIOS Version/Date**.
2. Visit your laptop manufacturer's support page, compare with the latest release, and read the changelog for stability or 24H2 compatibility fixes.
3. Follow the manufacturer's flashing instructions exactly — keep the charger plugged in and do not interrupt the process.
4. After the BIOS update, retest for several days.

## Closing

REFERENCE_BY_POINTER looks intimidating, but it is almost always one misbehaving driver — and the minidump usually names it outright. Read the dump, update or roll back that specific driver, and clear out old antivirus filter drivers, and the 0x18 crashes stop. On Windows 11 24H2 specifically, make sure every driver you install is certified for 24H2 rather than carried over from an older build, because that version gap is where most of these crashes are born.
