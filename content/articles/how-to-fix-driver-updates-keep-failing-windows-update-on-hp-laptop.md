---
title: "How to Fix Driver Updates That Keep Failing in Windows Update on an HP Laptop"
slug: "how-to-fix-driver-updates-keep-failing-windows-update-on-hp-laptop"
date: 2026-09-15
categories: ["windows-update"]
tags: ["driver updates", "hp laptop", "windows update", "0x80070103"]
description: "Driver updates keep failing in Windows Update on your HP laptop? Six HP-specific fixes — Support Assistant conflicts, Wolf Security, and hiding stale offers."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-keep-failing-windows-update-on-hp-laptop.webp"
faqs:
  - q: "Which driver source should win on my HP?"
    a: "HP Support Assistant, because its drivers are validated for your exact HP product number and are usually newer than Microsoft’s generic catalog packages. When Windows Update keeps failing on a driver, it is almost always offering an older version than HP already installed. Confirm HP’s driver is in place, then hide the Windows Update offer with the wushowhide tool so the failure loop ends while OS security updates continue normally."
  - q: "Should I remove third-party driver updaters from my HP?"
    a: "Uninstall it. HP laptops sometimes ship with trial driver-updater utilities, and running one alongside HP Support Assistant and Windows Update creates three-way conflicts over the same driver files. HP Support Assistant alone is the correct driver manager on an HP; remove the third-party tool through Settings, then Apps, then restart before troubleshooting further."
  - q: "What does 0x80070103 mean on HP?"
    a: "It means Windows Update tried to install a driver older than your HP’s installed version — an attempted downgrade, typically because HP Support Assistant installed a newer driver first. This is not corruption or hardware trouble. Hide that specific update offer; your HP driver remains, which is the desired outcome. Revisit only after a major Windows upgrade brings a genuinely newer package."
  - q: "Can I install HP drivers manually?"
    a: "Yes — download drivers directly from HP’s support site using your product number or serial number. Manual installation avoids scheduling races, version ambiguity, and stale catalog offers entirely. Install chipset, graphics, network, and BIOS updates with restarts between major ones, then hide the corresponding Windows Update driver offers so they stop failing."
---

HP laptops carry the same driver-turf-war DNA as other brands, with HP Support Assistant playing the role of the faster, better-informed updater. It installs model-specific drivers validated for your exact product number — and then Windows Update keeps failing to install its older generic versions, because your system correctly refuses each downgrade.

Dell owners get the same treatment from different software, detailed in the [Dell driver-update guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-on-dell-laptop/). On HP, the fix is the same shape: establish HP’s drivers, stop the races, hide the stale offers.

## Why this happens

- **HP Support Assistant deploying newer drivers:** HP’s tooling installs drivers ahead of Microsoft’s catalog; the older WU packages then fail as downgrades.
- **HP-customized hardware revisions:** HP-specific board revisions on network, audio, and biometric hardware mismatch generic WU packages.
- **Support Assistant and WU racing:** Overlapping driver install schedules cause file locks that fail both tools’ attempts.
- **Interrupted HP installs poisoning staging:** Killed Support Assistant updates leave partial driver files that Windows Update chokes on.
- **HP BIOS updates re-enumerating hardware:** A BIOS update can change device enumeration, desyncing Windows Update’s hardware matching.
- **Stale catalog metadata:** Local metadata offering superseded driver versions guarantees repeat conflict failures.
- **Third-party driver updaters adding a third racer:** An extra updater tool on an HP (often preinstalled trials) creates three-way file conflicts.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Make HP Support Assistant the driver authority

Establish HP’s drivers as the baseline first. HP validates these against your exact product number, and once they are in place, most Windows Update driver “failures” reveal themselves as outdated offers rather than real problems.

1. Open HP Support Assistant and install all its driver and firmware updates.
2. Restart the laptop.
3. Open Windows Update and note which driver failures clear.
4. The remaining failures are the stale offers to hide in Fix 6.

### Fix 2: Prove the downgrade with version comparison

Version comparison is the diagnosis. HP Support Assistant moves faster than Microsoft’s catalog, so the installed driver wins the comparison more often than not — and the “failure” is Windows Update being out of date.

1. Check Device Manager for the installed driver version on each failing device.
2. Compare against the Windows Update offer in Update history.
3. Newer installed version means the WU offer is a downgrade — hide it.
4. Document which offers you hid, in case a future upgrade needs revisiting.

### Fix 3: Eliminate racing installers

File locks from concurrent installers are the mechanical cause of many HP driver failures. One owner, clear lanes, no racers — the conflicts disappear without any repair work at all.

1. Set HP Support Assistant driver checks to manual or off-hours.
2. Uninstall any third-party driver updater trials.
3. Let Windows Update own OS patches only.
4. Confirm a full week with no overlapping driver installs.

### Fix 4: Clean-reinstall contested drivers from HP

Interrupted HP installs can leave staging unrecoverable by incremental means. Clean removal plus a fresh HP-sourced install is the reliable reset for a device both updaters have fought over.

1. Uninstall the device in Device Manager, ticking “Delete the driver software”.
2. Restart for the baseline driver.
3. Install the exact-model driver from [HP Support](https://support.hp.com/us-en).
4. Restart and verify the Windows Update failure is gone.

### Fix 5: Refresh the catalog cache

The local catalog cache lags HP’s releases. Refreshing it forces a current catalog query, which frequently clears phantom offers without needing to hide anything.

1. Elevated prompt: net stop wuauserv, net stop bits.
2. Rename: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
3. Restart the services.
4. Recheck Windows Update; superseded HP-conflicting offers often vanish after the refresh.

### Fix 6: Hide the stale Microsoft driver offers

When HP’s driver is correct and Microsoft’s offer is stale, hiding is the professional, permanent resolution. Security and quality updates flow untouched; only the obsolete driver offers are silenced.

1. Download wushowhide.diagcab from [Microsoft Support](https://support.microsoft.com/en-us/windows).
2. Hide each persistently failing HP-conflicting driver offer.
3. Verify Windows Update is clean of driver failures.
4. For the Dell-flavored version of this conflict, see the [Dell driver-update guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-on-dell-laptop/).

### Fix 7: Update HP BIOS and firmware alongside the drivers

Driver failures on HP laptops sometimes trace one layer deeper: the BIOS or firmware. HP’s UEFI firmware enumerates hardware for Windows, and outdated firmware can report device IDs that do not match the driver packages Windows Update offers — producing failures no driver reinstall can fix. HP Support Assistant flags BIOS updates clearly, and HP’s support site lists firmware release notes worth reading before installing. The usual precautions apply: AC power connected, battery charged, never interrupt a flash. After a BIOS update, re-run both HP Support Assistant’s driver check and Windows Update — the corrected hardware enumeration frequently resolves driver-matching failures immediately, and it is a prerequisite worth completing before hiding offers, since a firmware fix can turn a “stale offer” into a working one.

1. Open HP Support Assistant and check for BIOS/firmware updates, or find them on HP’s support site by product number.
2. Read the release notes for mentions of Windows 11, driver, or device compatibility.
3. Install the BIOS update with the charger connected and the battery above 50 percent.
4. After the flash, run HP Support Assistant’s driver check again.
5. Then check Windows Update — previously failing driver offers may now install cleanly.
6. Hide only the offers that still fail after firmware is current.

## Closing

HP’s driver-update failures in Windows Update are a coordination problem with a coordination solution: one driver owner (HP Support Assistant), current HP drivers, no racing installers, and hidden stale Microsoft offers. Set that up once and the failures stop — not because anything was repaired, but because the two systems finally stopped fighting. Lenovo owners run into the exact same coordination problem with different vendor software — our [Lenovo driver-update failure guide](/articles/how-to-fix-driver-updates-keep-failing-windows-update-on-lenovo-laptop/) is the parallel walkthrough.
