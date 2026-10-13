---
title: "DRIVER_VERIFIER_IOMANAGER_VIOLATION: Troubleshooting Guide"
slug: driver-verifier-iomanager-violation-troubleshooting
date: 2026-09-30
categories: ["windows-errors"]
tags: ["bsod", "driver verifier", "stop code", "drivers"]
description: "DRIVER_VERIFIER_IOMANAGER_VIOLATION blue screen? Driver Verifier caught a driver mishandling I/O. Here's how to identify it and fix the crash."
thumbnail: "/images/thumbs/driver-verifier-iomanager-violation-troubleshooting.webp"
faqs:
  - q: "What is DRIVER_VERIFIER_IOMANAGER_VIOLATION?"
    a: "Driver Verifier — Windows' built-in driver stress-testing tool — caught a driver violating I/O manager rules, such as completing the same I/O request twice or passing invalid parameters. The violation means the driver has a real bug that could corrupt data or crash the system."
  - q: "Did Driver Verifier cause this blue screen?"
    a: "In a sense, yes — but it exposed a genuine bug rather than creating one. Verifier deliberately stresses drivers so bugs surface as immediate crashes instead of silent corruption. The driver was broken before Verifier ran; Verifier just proved it."
  - q: "Should I turn off Driver Verifier after fixing the driver?"
    a: "Absolutely. Verifier is a diagnostic tool, not a permanent setting. Leaving it on degrades performance and can cause crashes on its own. Run verifier /reset in an elevated prompt once you've identified and fixed the bad driver."
  - q: "Can this error appear if I never enabled Driver Verifier?"
    a: "Sometimes — certain Windows builds and debugging tools enable Verifier silently, and some driver installers do it too. If you see this stop code unexpectedly, check whether Verifier is running with the verifier /query command."
---

`DRIVER_VERIFIER_IOMANAGER_VIOLATION` (stop code `0x000000C9`) is a special blue screen: it means Driver Verifier was running, and it caught a driver breaking the I/O manager's rules. Maybe the driver completed an I/O request packet twice. Maybe it passed a garbage parameter. Whatever the specifics, Verifier proved the driver has a genuine bug — one that, without Verifier, would have manifested as silent data corruption or a mysterious crash weeks later.

The good news: Verifier hands you the guilty driver's name on a platter. The fix is almost always "replace that driver." The trap to avoid is leaving Verifier enabled after you're done, which turns your laptop into a crash-prone stress-test machine permanently. Troubleshoot, fix, then turn Verifier off.

## Why this happens

- **Buggy third-party driver**: The core cause. Storage filter drivers, antivirus filters, virtual disk tools, and USB drivers are the most common violators of I/O manager rules.
- **Driver Verifier left enabled**: Someone (or some installer) turned Verifier on and never turned it off. The system then crashes on driver bugs that would otherwise go unnoticed.
- **Outdated driver vs. new Windows build**: A driver written for older I/O manager behavior violates rules that newer Windows enforces more strictly.
- **Corrupt driver files**: Half-updated drivers can violate I/O rules the original never did.
- **Conflicting filter drivers**: Two filters in the storage stack mishandling the same I/O request packets — antivirus plus backup software is the classic pair.
- **Failing storage hardware**: A dying drive returning garbage to the storage driver can make a correct driver look like it's violating rules.
- **Overclocked system instability**: Marginal overclocks corrupting I/O operations in flight, though this is rare for this specific code.

## How to fix it

Work through these in order — confirm Verifier's status first, then fix the driver it names.

### Fix 1: Check whether Driver Verifier is running

Know what you're dealing with before changing anything.

1. Open **Terminal (Admin)** (**Win + X** > **Terminal (Admin)**).
2. Run `verifier /query`. If it lists drivers under verification, Verifier is active.
3. If you didn't enable it deliberately, some debugging tool or driver installer did — note which drivers are listed, because those are the suspects.
4. Don't disable it yet — you want one more crash with Verifier on to capture the guilty driver's name in the dump (Fix 2). If the system is unusably unstable, skip to Fix 3 and disable it now.

### Fix 2: Identify the violating driver from the dump

Verifier crashes name names. Read them.

1. After a Verifier-induced crash, open the newest dump in `C:\Windows\Minidump` with WinDbg Preview.
2. Run `!analyze -v`. The output names the driver that committed the violation — often with the specific rule broken.
3. Write down the driver name and its provider. Third-party storage filters, antivirus drivers, and virtual-disk drivers are the usual entries.
4. This is the single most valuable step in the whole guide — everything after it is targeted.

### Fix 3: Disable Driver Verifier

Once you have the driver's name (or if the system won't stay up), turn Verifier off.

1. Open **Terminal (Admin)** and run `verifier /reset`.
2. Restart the laptop.
3. Confirm with `verifier /query` — it should report that no drivers are being verified.
4. Your system is now out of stress-test mode. The underlying driver bug still exists, but it will no longer crash deliberately — fix it in the next steps before it corrupts something quietly.

### Fix 4: Update or replace the violating driver

Targeted fix for the named driver.

1. Identify the driver from Fix 2. If it's tied to a program (antivirus, backup tool, virtual drive software), update that program to the latest version first.
2. If it's a hardware driver, get the replacement from the manufacturer: chipset/storage from your laptop maker, or run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel storage and chipset drivers.
3. If the latest version still violates, roll back to the previous version — newer isn't always more correct for I/O manager compliance.
4. As a last resort for a non-essential driver, uninstall the owning software entirely.

### Fix 5: Remove conflicting filter drivers

When two filters fight over I/O requests, both can look guilty.

1. Open **Settings** > **Apps** > **Installed apps** and look for overlapping tools: two antivirus products, antivirus plus backup software with its own filter, disk utilities.
2. Uninstall all but one of each category. Use vendor removal tools for antivirus so filter drivers are fully removed.
3. Restart and test. Filter conflicts are a top cause of I/O manager violations that no single driver update fixes.
4. Microsoft documents filter-driver troubleshooting approaches at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Repair system files

Corruption in the I/O manager's own components.

1. In **Terminal (Admin)**, run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart. This eliminates OS-side corruption as a contributor.

### Fix 7: Test storage hardware and memory

Rule out the physical layer.

1. Check drive health with CrystalDiskInfo or the manufacturer's tool — a dying drive makes good drivers look guilty.
2. Run `mdsched.exe` for a quick RAM check.
3. If hardware is clean and the violation was consistent, you're back to the driver from Fix 2 — it's genuinely buggy, and replacing or removing its software is the answer.
4. For the broader blue screen playbook, see [how to fix the blue screen of death on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/), and for the post-update variant of this code, [Driver Verifier IOManager violation after a Windows 11 update](/articles/how-to-fix-driver-verifier-iomanager-violation-after-windows-11-update/).

## Closing

`DRIVER_VERIFIER_IOMANAGER_VIOLATION` is actually good news disguised as a blue screen: Verifier caught a real driver bug and told you exactly which driver. Read the dump, fix or remove that driver, then turn Verifier off with `verifier /reset`. The only way this goes wrong is ignoring the evidence — updating random drivers while the named violator stays installed, or leaving Verifier on until it crashes something else. Name it, fix it, disable Verifier, move on.
