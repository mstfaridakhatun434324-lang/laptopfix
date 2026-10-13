---
title: "Fix Driver Updates Failing in Windows Update, Step by Step"
slug: how-to-fix-driver-updates-failing-in-windows-update-step-by-step
date: 2026-09-10
categories: ["windows-update"]
tags: ["driver updates failing", "windows update", "step by step", "driver install error"]
description: "Driver updates failing in Windows Update? Follow this systematic step-by-step repair, from hiding bad offers to clean driver reinstalls."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-failing-in-windows-update-step-by-step.webp"
faqs:
  - q: "Why do driver updates fail while Windows updates succeed?"
    a: "They use different install paths. Windows patches install through the servicing stack, which is robust; driver updates install through the driver installer and PnP stack, which is pickier about signatures, version conflicts, and device state. A healthy update client can still fail driver installs."
  - q: "What do driver update error codes mean?"
    a: "0x80070103 means the offered driver is older than or identical to the installed one. 0x800f020b means the driver package is damaged or mismatched. 0x80240061 relates to isolation issues. Each points at a different fix, which is why noting the code matters."
  - q: "Should I let Windows Update install drivers at all?"
    a: "For peripherals and minor devices, yes — it is convenient and safe. For core drivers (graphics, chipset, network, storage), prefer the manufacturer's site or tool. You can also let Windows Update handle everything and intervene only when a specific driver repeatedly fails."
  - q: "Can a failed driver update damage my hardware?"
    a: "No. A failed driver install leaves the previous working driver in place — that is why the device keeps working despite the error. The failure is an installation rejection, not a partial flash. Firmware updates are the exception; treat those with extra care."
---

Driver updates failing in Windows Update is a special kind of annoyance: Windows itself patches fine, but one printer, audio, or graphics driver fails on every cycle, turning every Patch Tuesday into a red error badge. The codes — 0x80070103, 0x800f020b — are terse, and retrying never helps because the failure is deterministic: the same wrong package meets the same rejection every time.

The fix is systematic, not magical. Identify the failing driver and its code, decide whether Windows Update should even be offering it, then either hide the offer, supply the correct package manually, or clean-reinstall the driver. This guide gives you that decision tree in order.

If the failing driver is on an HP laptop specifically, the [HP driver update guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-on-hp-laptop/) adds vendor-specific steps. For the general case on any brand, continue here.

## Why this happens

- **Offered driver older than installed:** Windows Update's catalog lags the manufacturer's; it offers a driver you already beat, and the installer rejects it (0x80070103).
- **Corrupt driver package in cache:** A half-downloaded driver payload fails signature or hash verification on every attempt.
- **Device-specific customization mismatch:** Laptop vendors customize reference drivers; the generic package does not match the customized hardware ID.
- **Driver installer blocked by running software:** Audio or peripheral utilities holding the device open prevent driver replacement.
- **Pending reboot deadlock:** A previous installation awaiting reboot blocks all subsequent driver installs.
- **Wrong hardware revision targeting:** The offered driver targets a different revision of the same model line.
- **Third-party driver updater conflicts:** External updater tools install versions that fight Windows Update's offers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failing driver and error code

Precision here prevents wasted effort. Know exactly what is failing before touching anything.

1. Open Settings → Windows Update → Update history → Driver updates and find the failed entry.
2. Note the device name, driver version offered, and error code.
3. Open Device Manager, find the device, and note the currently installed driver version (Properties → Driver tab).
4. If the offered version is older than installed, you are looking at a 0x80070103-style stale offer — skip to Fix 3.

### Fix 2: Reboot and retry once

Clear the trivial causes before doing surgery.

1. Perform a full restart (not sleep/shutdown hybrid).
2. Run Windows Update once more.
3. If the same driver fails with the same code, the cause is systemic — continue.

### Fix 3: Hide the bad driver offer

When Windows Update insists on a driver your system does not want, remove the offer from the queue.

1. Download Microsoft's wushowhide.diagcab ('Show or hide updates' troubleshooter).
2. Run it, select Hide updates, and check the failing driver.
3. Confirm the error no longer appears on the next scan.
4. Remember: hiding is triage. You still need a working driver — obtain it in Fix 4 or 5.

### Fix 4: Install the correct driver from the manufacturer

The vendor's package matches your exact hardware, including customizations Windows Update does not know about.

1. Identify your exact model and hardware revision.
2. Download the driver from the manufacturer's support site (Dell, HP, Lenovo) or use their update tool.
3. For Intel graphics/chipset/network, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects and installs the right packages.
4. For NVIDIA or AMD graphics, use [NVIDIA's driver download](https://www.nvidia.com/Download/index.aspx) or [AMD's driver support page](https://www.amd.com/en/support/download/drivers.html).
5. Install, reboot, and verify the version in Device Manager.

### Fix 5: Clean-reinstall a corrupted driver

When the installed driver package itself is damaged, no update will apply over it — remove it first.

1. In Device Manager, right-click the device → Uninstall device; tick 'Attempt to remove the driver for this device' if offered.
2. Reboot and let Windows load its inbox driver.
3. Install the manufacturer's package from Fix 4 on the clean slate.
4. Verify in Device Manager that the new version stuck.

### Fix 6: Reset the update cache for corrupt downloads

If the driver package downloads damaged every time, the cache is the culprit.

1. Open an elevated Command Prompt; run `net stop wuauserv` and `net stop bits`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
3. Run `net start wuauserv` and `net start bits`, reboot, and retry the scan.
4. A fresh download that still fails points back at package mismatch, not corruption — return to Fix 4.

### Fix 7: Decide the long-term driver strategy

Stop the cycle from repeating by choosing who supplies drivers for this machine.

1. Option A: Let Windows Update handle drivers, and hide individual bad offers as they appear.
2. Option B: Get core drivers from the manufacturer and use the group policy/device-installation setting to prevent Windows Update from offering drivers at all.
3. For most laptop users, the hybrid works best: manufacturer packages for graphics/chipset/network/BIOS, Windows Update for everything else.
4. Document which driver you hid and why — future-you will thank present-you when the offer reappears after a feature update.

### Fix 8: Use driver rollback as a diagnostic tool

When a device worked before a recent driver change and fails after, rolling back confirms the new driver is the problem. This turns a vague 'driver update fails' into a confirmed bad package you can then block deliberately.

1. In Device Manager, right-click the device → Properties → Driver tab → Roll Back Driver (available only if a previous version exists).
2. Test the device thoroughly — if it works, the newer driver was the problem, not your system.
3. Hide the offending driver offer with wushowhide.diagcab so Windows Update stops pushing it.
4. Check the manufacturer's site for a fixed revision; install it manually when available.
5. Report the bad driver to the manufacturer — you are likely not the only one hit by it.

## Closing

Driver updates failing in Windows Update is a deterministic problem with a systematic fix: identify the driver and code, hide the stale offer, install the manufacturer's correct package, and clean-reinstall when the installed driver is damaged. Choose a long-term driver strategy afterward so the same failure does not return with the next feature update. If the whole update client seems broken rather than just drivers, run through the [Windows Update troubleshooter guide](/articles/how-to-fix-windows-update-with-troubleshooter-in-windows-11-24h2/) first.
