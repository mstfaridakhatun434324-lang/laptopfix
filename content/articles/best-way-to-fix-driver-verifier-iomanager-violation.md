---
title: "Best Way to Fix DRIVER_VERIFIER_IOMANAGER_VIOLATION"
slug: best-way-to-fix-driver-verifier-iomanager-violation
date: 2026-09-12
categories: ["windows-errors"]
tags: ["bsod", "driver verifier", "drivers"]
description: "DRIVER_VERIFIER_IOMANAGER_VIOLATION blue screen? Driver Verifier caught a driver breaking I/O rules. Here's how to fix it properly."
thumbnail: "/images/thumbs/best-way-to-fix-driver-verifier-iomanager-violation.webp"
faqs:
  - q: "What does DRIVER_VERIFIER_IOMANAGER_VIOLATION mean?"
    a: "Driver Verifier — Windows' built-in driver stress-testing tool — caught a driver violating I/O Manager rules (stop code 0xC9). This crash only happens when Verifier is actively running. The named driver in the dump is the one breaking the rules."
  - q: "I didn't turn on Driver Verifier. Why am I getting this?"
    a: "Someone or something did — a technician, a troubleshooting guide you followed earlier, or rarely, malware. The fix is the same: boot into Safe Mode, run verifier, choose 'Delete existing settings,' and restart. Then address the named driver."
  - q: "Should I just turn off Driver Verifier and ignore it?"
    a: "Turning it off stops the crashes, but the underlying driver bug remains — Verifier was doing its job by exposing it. The right move is to identify the driver from the dump, update or replace it, then disable Verifier."
  - q: "Can Driver Verifier cause a boot loop?"
    a: "Yes, and it's common: Verifier crashes the system during boot before you can log in. Boot into Safe Mode (Verifier doesn't apply its checks there the same way) or use the recovery command prompt to delete Verifier settings with verifier /reset."
---

`DRIVER_VERIFIER_IOMANAGER_VIOLATION` (stop code 0xC9) is a special blue screen: it only exists because Driver Verifier is running. Verifier is a Windows tool that deliberately stresses drivers, checking they follow kernel rules — and when a driver breaks I/O Manager rules, Verifier crashes the system on purpose, naming the offender in the dump.

So this crash is actually good news disguised as bad: Verifier did exactly what it was built to do and handed you the guilty driver's name. The work now is (1) escaping Verifier's crash loop if you're stuck in one, and (2) fixing the named driver.

## Why this happens

- **Driver Verifier is enabled and stressing drivers**: The prerequisite — without Verifier running, this stop code cannot occur.
- **A driver violates I/O Manager rules**: Mishandled IRPs, incorrect completion routines, or invalid I/O patterns the driver got away with until Verifier checked.
- **Outdated or buggy third-party driver**: Old drivers written before current I/O rules were enforced.
- **Verifier left on after earlier troubleshooting**: The most common real-world scenario — someone enabled it following a guide, fixed nothing, and forgot it.
- **Overly broad Verifier settings**: Verifying every driver including Microsoft's own can cause crashes unrelated to any real bug.
- **Corrupted driver binaries**: Damaged .sys files fail Verifier's checks even if the driver version is fine.

## How to fix it

Work through these in order — escape Verifier first, then fix the driver.

### Fix 1: Turn off Driver Verifier (Safe Mode method)

If you can reach Safe Mode, this takes two minutes.

1. Boot into Safe Mode: force-power-off three times during the Windows logo to reach Automatic Repair, then **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4**.
2. Once in Safe Mode, press **Win + R**, type `verifier`, press Enter.
3. Select **Delete existing settings** and click **Finish**.
4. Restart normally. The Verifier-induced crashes stop immediately.
5. If you can boot normally already (crashes are intermittent), just run `verifier` from a normal session and delete settings — no Safe Mode needed.
6. Our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers alternate ways in if the triple-power-off method doesn't trigger recovery.

### Fix 2: Turn off Driver Verifier (recovery command prompt method)

If Verifier crashes the system even in Safe Mode, use the recovery environment.

1. Boot to the recovery environment (installation USB > **Repair your computer**, or Automatic Repair > **Advanced options**).
2. Go to **Troubleshoot** > **Advanced options** > **Command Prompt**.
3. Type `verifier /reset` and press Enter — this clears all Verifier settings from outside Windows.
4. Type `wpeutil reboot` and let the laptop start normally.
5. Confirm Verifier is off by running `verifier` in Windows and checking it shows no existing settings.

### Fix 3: Identify the named driver from the dump

Before or after disabling Verifier, capture which driver it caught.

1. Open the latest minidump in **BlueScreenView** (`C:\Windows\Minidump`) — look at **Caused By Driver**.
2. The 0xC9 crash names the violating driver directly, often with the specific rule broken in the dump's parameter codes.
3. Map the filename to its device: network drivers (`ndis.sys`, `Netwtw10.sys`), storage (`storport.sys`, `stornvme.sys`), or a third-party .sys.
4. If the dump names a Windows inbox driver, the real culprit is often a filter driver stacked above it (antivirus, encryption) — investigate those.
5. Background on dump reading: our [DRIVER_IRQL_NOT_LESS_OR_EQUAL guide](/articles/driver-irql-not-less-or-equal-blue-screen-error-fix/) uses the same technique.

### Fix 4: Update or replace the violating driver

Now fix the actual bug Verifier exposed.

1. In **Device Manager** (**Win + X** > **Device Manager**), find the device for the named driver.
2. Download the latest driver from the manufacturer: [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or your laptop maker ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
3. Uninstall the old driver first (check **Delete the driver software**), restart, then install the new one fresh.
4. If the newest driver still violates, try the previous version — and report the bug to the vendor with the dump attached.
5. Retest by re-enabling Verifier briefly on just that driver to confirm the violation is gone, then disable Verifier again.

### Fix 5: Remove filter drivers that violate I/O rules

Antivirus, encryption, and backup filter drivers are frequent 0xC9 offenders.

1. If the dump implicates a filter driver (or an inbox driver with filters stacked on it), uninstall the parent software completely.
2. Third-party antivirus first — its file system filter is the classic case. Defender takes over automatically.
3. Then VPN clients with network filters, disk encryption tools, and backup software with volume filters.
4. Reinstall only the latest versions explicitly supporting your Windows build.
5. Microsoft documents filter driver behavior on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Repair corrupted driver files

Sometimes the driver version is fine but its files are damaged.

1. Open an elevated Command Prompt (**Win + S**, type `cmd`, right-click > **Run as administrator**).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`.
3. Reinstall the driver cleanly afterward — SFC repairs system files but not third-party .sys files.
4. Check the drive with `chkdsk C: /f` too — disk corruption damages driver files and produces Verifier failures that look like bugs.

### Fix 7: Re-enable Verifier narrowly to confirm the fix

Use Verifier as the verification tool it is — briefly and precisely.

1. Press **Win + R**, type `verifier`, choose **Create standard settings**.
2. This time, **select driver names from a list** and check only the fixed driver.
3. Restart and use the laptop for a few hours of normal workload.
4. No crash = the driver is fixed. Immediately run `verifier` again and **Delete existing settings**.
5. Never leave Verifier running unattended — it's a diagnostic instrument, not a background service. Our [24H2 hypervisor error guide](/articles/how-to-fix-hypervisor-error-bsod-in-windows-11-24h2/) covers another Verifier-adjacent crash if you're troubleshooting virtualization too.

## Closing

DRIVER_VERIFIER_IOMANAGER_VIOLATION means Verifier caught a driver red-handed — which is the tool working as designed, not a new problem. Disable Verifier to stop the intentional crashes, read the dump for the driver's name, update or remove that driver (checking filter drivers from AV and encryption tools), and confirm with a brief targeted Verifier run. Then turn Verifier off and get back to a quiet, stable system.
