---
title: "How to Fix the DRIVER_VERIFIER_DETECTED_VIOLATION Blue Screen"
slug: how-do-i-fix-driver-verifier-detected-violation
date: 2026-09-16
categories: ["windows-errors"]
tags: ["bsod", "driver verifier", "driver bug", "windows 11"]
description: "Fix DRIVER_VERIFIER_DETECTED_VIOLATION — turn off Driver Verifier safely, identify the bad driver from the dump, and update or remove it in 7 steps."
thumbnail: "/images/thumbs/how-do-i-fix-driver-verifier-detected-violation.webp"
faqs:
  - q: "What is Driver Verifier and why is it crashing my PC?"
    a: "Driver Verifier is a built-in Windows stress-test tool for drivers. Someone — you, a technician, or a troubleshooting guide — turned it on to catch a bad driver, and it caught one: the blue screen means Verifier detected a driver breaking the rules. The crash is Verifier doing its job, not a new problem."
  - q: "I never turned on Driver Verifier. How did it get enabled?"
    a: "Some driver installer packages and older troubleshooting tools enable it silently. It can also be left on after a repair shop visit. If you did not enable it deliberately, just turn it off — that alone usually ends the crashes."
  - q: "Is it safe to just disable Driver Verifier?"
    a: "Yes, completely. Verifier is a diagnostic tool, not a protection feature — Windows runs fine without it. The only reason to keep it on is if you are actively hunting a specific driver bug with a plan for analyzing the results."
  - q: "How do I find which driver Verifier caught?"
    a: "The minidump from the crash usually names it. Our guide to [checking minidump files in Windows 11 24H2](/articles/how-to-check-minidump-files-in-windows-11-24h2/) shows how to read it, and our [driver verifier troubleshooting walkthrough](/articles/troubleshoot-driver-verifier-detected-violation/) goes deeper into the analysis."
---

**DRIVER_VERIFIER_DETECTED_VIOLATION** (0xC4) is a slightly unusual blue screen because it is not exactly a malfunction — it is a *diagnosis*. Windows includes a tool called **Driver Verifier** that deliberately stresses drivers to catch bugs. When it catches a driver misbehaving, it crashes the system on purpose and names the offender. So if you are seeing this stop code, Verifier is (or was) running on your machine, and it found something.

The most common situation: Verifier got turned on during some earlier troubleshooting — by you following a guide, by a repair shop, or by a driver installer — and was never turned off. Now it crashes the machine every time the buggy driver loads. The fix has two parts: turn Verifier off to stop the crashes, then deal with the driver it caught.

It is worth pausing on what Verifier actually does, because it reframes the whole problem. Normal Windows trusts drivers to follow the rules and only crashes when a violation causes real damage. Verifier does not trust anyone: it actively probes drivers with invalid inputs, tracks every memory allocation, and crashes at the *first* rule break — even one that would have been harmless in normal use. That is why Verifier crashes can feel disproportionate: the driver might have run fine for months, but under Verifier's microscope its sloppiness becomes a blue screen. The driver was always buggy; Verifier just refused to look the other way.

## Why this happens

- **Verifier was left enabled after troubleshooting.** The number one scenario. It keeps stress-testing drivers on every boot until someone turns it off.
- **A genuinely buggy driver.** Verifier caught a real bug — often in a third-party driver for USB devices, audio interfaces, VPN clients, or old peripherals.
- **An outdated driver that predates current Windows.** Drivers written for older Windows builds break rules that newer builds enforce.
- **Overclocking or unstable hardware.** Verifier's stress tests can expose marginal hardware that normal use would not trip.
- **Corrupted driver files.** A half-updated driver can fail Verifier's checks in ways neither the old nor new version would.
- **Verifier configured too aggressively.** "All drivers, all checks" will eventually crash almost any system; targeted settings are the correct way to use it.

## How to fix it

Work through these in order — disabling Verifier comes first because it stops the bleeding.

### Fix 1: Disable Driver Verifier

1. Boot into **Safe Mode** if normal boot crashes: interrupt the boot three times to reach **Automatic Repair**, then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4**.
2. Press **Win + R**, type `verifier`, and press Enter.
3. Select **Delete existing settings** and click **Finish**.
4. Alternatively, open an admin Command Prompt and run `verifier /reset`.
5. Restart normally. If the crashes stop here, Verifier was the entire problem — but still check Fix 2, because it may have been catching a real bug.

### Fix 2: Identify the driver from the crash dump

1. The minidump at `C:\Windows\Minidump` from the Verifier crash usually names the driver directly.
2. Open **Event Viewer > Windows Logs > System** and look at the bugcheck entry — it sometimes includes the driver name.
3. For the full analysis, see our guide to [checking minidump files in Windows 11 24H2](/articles/how-to-check-minidump-files-in-windows-11-24h2/).
4. Common offenders: VPN filter drivers, USB device drivers, audio drivers, and antivirus filter drivers.

### Fix 3: Update the offending driver

1. Once you know the driver name, identify its device in **Device Manager**.
2. Right-click it and choose **Update driver > Search automatically for drivers**.
3. Then check **Settings > Windows Update > Advanced options > Optional updates** for a newer version.
4. If Windows finds nothing, get the driver from the hardware maker's site — or [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel components.

### Fix 4: Remove or replace the offending software

If no updated driver exists (common with old peripherals):

1. Unplug the device the driver belongs to and uninstall its software via **Settings > Apps > Installed apps**.
2. In **Device Manager**, right-click the device and choose **Uninstall device**, checking **Attempt to remove the driver** if offered.
3. Restart. If the crashes stop, the hardware's driver is simply incompatible with your Windows build — check the maker's site for a newer version or consider replacing the device.

### Fix 5: Check for a Windows update that addresses it

1. Go to **Settings > Windows Update** and install everything pending.
2. Microsoft occasionally fixes Verifier-detected issues in the kernel itself via cumulative updates.
3. Conversely, if the crashes *started* right after an update, try **Update history > Uninstall updates** and remove the most recent one — then check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues.

### Fix 6: Test memory and disk health

Verifier crashes can occasionally be hardware faults wearing a driver costume.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. In an admin terminal, run `chkdsk C: /f` and schedule it for the next restart.
3. If either finds problems, fix the hardware first — no driver update survives bad RAM.

### Fix 7: Re-enable Verifier properly — only if you are still hunting

If you actually need Verifier for diagnosis (you are a developer or following a specific troubleshooting plan):

1. Run `verifier`, choose **Create custom settings**, and enable checks only for the **specific suspect drivers** — never "all drivers."
2. Use it for one targeted test session, capture the dump, then run `verifier /reset` immediately.
3. Verifier is a scalpel, not a lifestyle. Leaving it on indefinitely is how you got here.

## Closing

**DRIVER_VERIFIER_DETECTED_VIOLATION** means the diagnostic tool did its job and found a bad driver — your job is to turn the tool off, identify the driver from the dump, and update or remove it. In most real-world cases Verifier was simply left on by accident, and `verifier /reset` ends the saga in thirty seconds. The deeper driver hunt in Fix 2–4 is for the cases where Verifier caught something genuinely broken. If the violation names a filter driver specifically, our [Driver Verifier IOMANAGER_VIOLATION guide](/articles/how-to-fix-driver-verifier-iomanager-violation-after-windows-11-update/) covers that filter-driver failure in detail.
