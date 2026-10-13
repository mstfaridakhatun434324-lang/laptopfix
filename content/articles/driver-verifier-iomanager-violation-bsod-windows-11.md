---
title: "Driver Verifier IOManager Violation BSOD on Windows 11: Fix It"
slug: driver-verifier-iomanager-violation-bsod-windows-11
date: 2026-09-17
categories: ["windows-errors"]
tags: ["bsod", "driver verifier", "windows 11"]
description: "Getting DRIVER_VERIFIER_IOMANAGER_VIOLATION on Windows 11? Here's how to escape the crash loop and fix the faulty driver."
thumbnail: "/images/thumbs/driver-verifier-iomanager-violation-bsod-windows-11.webp"
faqs:
  - q: "Why am I suddenly getting this BSOD on Windows 11?"
    a: "Driver Verifier is active on your system — either you enabled it while troubleshooting, a technician did, or it was left on from an earlier session. On Windows 11, Verifier's I/O checks are stricter, so drivers that passed on Windows 10 now get flagged."
  - q: "My PC blue-screens on every boot. How do I turn Verifier off?"
    a: "Boot into the recovery environment (interrupt boot three times), open Command Prompt from Troubleshoot > Advanced options, and run verifier /reset. That clears Verifier settings from outside Windows so you can boot normally."
  - q: "Does this BSOD mean my driver is actually broken?"
    a: "It means the driver violates I/O Manager rules that Verifier enforces — mishandled IRPs, bad completion routines, or similar. The driver may work fine in daily use, but the violation is real and worth fixing with an updated driver."
  - q: "Is it safe to just leave Driver Verifier running?"
    a: "No. Verifier is a diagnostic tool, not a protective one — it degrades performance and intentionally crashes the system when it finds violations. Always disable it after you've identified the faulty driver."
---

If your Windows 11 laptop started throwing `DRIVER_VERIFIER_IOMANAGER_VIOLATION` blue screens — possibly on every single boot — you're dealing with Driver Verifier doing its job a little too enthusiastically. Verifier is a built-in Windows tool that stress-tests drivers against kernel rules, and on Windows 11 its I/O checks catch violations that older Windows versions let slide.

The critical thing to understand: this blue screen is manufactured. Verifier found a driver breaking I/O Manager rules and crashed the system deliberately to get your attention. The fix has two parts — switching Verifier off so you can use your laptop, then dealing with the driver it flagged.

## Why this happens

- **Driver Verifier left enabled**: The overwhelmingly common cause — enabled during earlier troubleshooting and never turned off.
- **A driver genuinely violating I/O rules**: Bad IRP handling, incorrect completion routines, or double-completing requests.
- **Windows 11's stricter enforcement**: Drivers certified for Windows 10 may trip Windows 11's tighter I/O validation.
- **Outdated third-party drivers**: Old VPN, antivirus filter, or storage drivers predating current I/O requirements.
- **Verifier configured too broadly**: Checking all drivers instead of specific suspects multiplies crash opportunities.
- **Corrupted driver files**: Damaged .sys files fail checks a healthy copy would pass.

## How to fix it

Work through these in order — regain control first, then fix the driver.

### Fix 1: Disable Verifier from the recovery environment

When the BSOD hits on every boot, you can't reach Windows to turn Verifier off — so do it from outside.

1. Power on the laptop, and as soon as the manufacturer's logo appears, hold the power button to force it off. Repeat three times.
2. On the fourth boot, Windows enters the recovery environment. Click **Advanced options** > **Troubleshoot** > **Advanced options** > **Command Prompt**.
3. Type `verifier /reset` and press Enter. This wipes all Verifier settings.
4. Type `exit`, then choose **Continue** to boot Windows 11 normally.
5. The Verifier crashes stop immediately — the underlying driver issue remains, which the next fixes address.
6. If you have Windows 11 installation media, you can also boot from USB > **Repair your computer** to reach the same command prompt.

### Fix 2: Disable Verifier from within Windows

If the crashes are intermittent and you can boot, this is quicker.

1. Press **Win + R**, type `verifier`, press Enter.
2. Select **Delete existing settings**, click **Finish**.
3. Restart. Confirm Verifier is off by reopening `verifier` — it should show the initial setup screen with no existing settings.
4. Don't skip the driver fixes below, though — Verifier flagged a real violation.

### Fix 3: Find which driver Verifier caught

The dump from the 0xC9 crash names the violator — read it before the trail goes cold.

1. Open **BlueScreenView** (NirSoft, free) and load `C:\Windows\Minidump`.
2. Find the most recent `DRIVER_VERIFIER_IOMANAGER_VIOLATION` dump and note **Caused By Driver**.
3. The dump's parameters encode which I/O rule was broken — parameter 1 values like 0x1 (IRP still has a cancel routine at completion) point to specific bug classes.
4. If the named driver is a Microsoft inbox driver, look at filter drivers layered above it — antivirus, encryption, and backup filters are the usual real culprits.
5. For the full Verifier methodology, see our [in-depth Driver Verifier IOManager violation guide](/articles/best-way-to-fix-driver-verifier-iomanager-violation/).

### Fix 4: Update the flagged driver from the manufacturer

Get the newest, cleanest copy of the violating driver.

1. Identify the device in **Device Manager** (**Win + X** > **Device Manager**).
2. Download the latest driver from the authoritative source: [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html) for Intel, [NVIDIA](https://www.nvidia.com/Download/index.aspx) / [AMD](https://www.amd.com/en/support/download/drivers.html) for GPUs, or your laptop maker — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
3. Uninstall the old driver first (**Uninstall device** + **Delete the driver software**), restart, then install the fresh download.
4. For network drivers implicated in I/O violations, prefer the laptop manufacturer's version over the chip vendor's — OEM customizations matter for I/O behavior.
5. Our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) helps if the driver resists normal-mode uninstallation.

### Fix 5: Remove problematic filter drivers

On Windows 11, filter drivers cause a disproportionate share of these violations.

1. Uninstall third-party antivirus completely — don't just disable it. Its file-system filter driver is the single most common 0xC9 trigger.
2. Remove or update VPN clients (network filter drivers), disk encryption tools, and endpoint-security agents.
3. After each removal, test stability for a day before reinstalling anything — and only reinstall versions explicitly supporting Windows 11 24H2.
4. Check **Device Manager** > **View** > **Show hidden devices** for greyed-out filter entries from uninstalled software and remove those too.

### Fix 6: Repair system and driver file corruption

Rule out damage masquerading as a driver bug.

1. Elevated Command Prompt (**Win + S** > `cmd` > right-click > **Run as administrator**).
2. `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
3. `chkdsk C: /f` to catch disk corruption damaging driver files.
4. Reinstall the flagged driver cleanly after repairs — SFC fixes inbox drivers but not third-party .sys files.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents these repair tools officially.

### Fix 7: Verify the fix with a targeted Verifier run

Confirm the violation is actually gone — briefly and narrowly.

1. Run `verifier`, choose **Create standard settings**, then **Select driver names from a list**.
2. Check only the fixed driver — not everything.
3. Restart, exercise the driver hard (large file copies for storage, heavy browsing for network, gaming for GPU) for a few hours.
4. No crash means fixed. Immediately run `verifier` again and **Delete existing settings**.
5. If it still crashes, try the previous driver version, or escalate to the vendor with the dump file — include `C:\Windows\Minidump`'s latest .dmp in your report.

## Closing

On Windows 11, DRIVER_VERIFIER_IOMANAGER_VIOLATION almost always means Verifier was left on and caught something — so the immediate fix is `verifier /reset` from the recovery prompt, and the real fix is updating or removing the flagged driver (checking filter drivers from security software first). Use Verifier as the brief, targeted diagnostic it's meant to be, then switch it off and enjoy the silence.
