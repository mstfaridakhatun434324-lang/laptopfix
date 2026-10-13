---
title: "How to Fix Driver Updates Failing in Windows Update on an ASUS Laptop"
slug: "how-to-fix-driver-updates-failing-in-windows-update-on-asus-laptop"
date: 2026-09-03
categories: ["windows-update"]
tags: ["driver updates", "asus laptop", "windows update", "myasus"]
description: "Driver updates failing in Windows Update on your ASUS laptop? Six ASUS-specific fixes for MyASUS conflicts, version mismatches, and stale driver offers."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-failing-in-windows-update-on-asus-laptop.webp"
faqs:
  - q: "Should I update drivers with MyASUS or Windows Update?"
    a: "MyASUS and ASUS Live Update deliver drivers validated for your exact ASUS model, usually newer than the generic packages in Windows Update’s catalog. When both offer drivers, install ASUS’s and hide Microsoft’s conflicting offer. Letting both install drivers on overlapping schedules causes the file locks and version conflicts behind most of these failures — assign driver ownership to ASUS’s tools."
  - q: "Does Armoury Crate interfere with Windows Update drivers?"
    a: "Armoury Crate includes driver update functionality that can run on its own schedule. If it replaces driver files while Windows Update is installing the same driver, both fail. Either disable driver updates inside Armoury Crate’s settings or coordinate the schedules — and prefer MyASUS over Armoury Crate for driver management, since MyASUS is ASUS’s dedicated update tool."
  - q: "Can I download ASUS drivers manually instead?"
    a: "Yes. Search your model on ASUS’s support site and download drivers directly — chipset, graphics, audio, and network. Manual installation bypasses both the MyASUS/Windows Update conflict and any scheduling races. Install them one at a time with restarts in between, then hide the corresponding Windows Update offers with the wushowhide tool so the failures stop recurring."
  - q: "What does 0x80070103 mean on my ASUS laptop?"
    a: "It means Windows Update attempted to install a driver older than the one already on your ASUS laptop — typically because MyASUS installed a newer version first. This is not an error worth fixing by force; it is Windows Update being out of date. Hide that specific update offer and move on. Your ASUS-supplied driver stays, which is the correct outcome."
---

ASUS laptops ship with an unusually complete software ecosystem — MyASUS, ASUS Live Update, Armoury Crate — and all of it wants to manage your drivers. When Windows Update joins the party with its own older driver packages, the result is the familiar failure loop: install fails, retry, fail again. The Dell version of this brand-specific conflict is covered in the [Dell driver-update guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-on-dell-laptop/), but ASUS’s multi-tool ecosystem gives it its own flavor.

The key insight is the same: these failures are turf wars, not hardware problems. ASUS’s tools almost always have the newer, better-matched driver — Windows Update is simply offering you a downgrade your system wisely refuses.

## Why this happens

- **MyASUS installing newer drivers than Windows Update:** MyASUS and ASUS Live Update frequently deploy drivers newer than Microsoft’s catalog versions, so the older WU packages fail as downgrades.
- **ASUS-customized components with unique IDs:** ASUS uses custom hardware revisions (especially audio and network chips) that generic WU driver packages do not match.
- **Armoury Crate driver management conflicts:** Armoury Crate’s driver update feature can replace files while Windows Update is installing, failing both.
- **BIOS updates via MyASUS desyncing the catalog:** An ASUS BIOS update can re-enumerate devices, leaving Windows Update offering drivers for the old enumeration.
- **Corrupted ASUS driver staging:** Interrupted MyASUS installs leave partial driver packages that poison subsequent Windows Update attempts.
- **Windows Update offering wrong-generation drivers:** On ASUS laptops with upgraded components (e.g., replaced Wi-Fi cards), WU may offer drivers for the original factory hardware.
- **Stale catalog metadata:** The local update metadata may lag behind ASUS’s releases, offering superseded driver versions.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Let MyASUS establish the correct driver baseline

ASUS validates its drivers against your exact model, including custom hardware revisions Microsoft’s catalog does not know about. Establishing MyASUS as the driver authority resolves the version mismatches behind most WU driver failures on ASUS machines.

1. Open MyASUS and run its driver update check.
2. Install all offered drivers, prioritizing chipset, graphics, and network.
3. Restart the laptop.
4. Check Windows Update — failing entries tied to those drivers should clear.

### Fix 2: Compare versions before letting Windows Update proceed

Version comparison is the whole diagnosis on ASUS laptops. MyASUS moves fast — its drivers are routinely months ahead of Microsoft’s catalog — so the “failure” is usually Windows Update losing a race it should not have entered.

1. Open Device Manager and record the current driver version for the failing device.
2. Check the version Windows Update offers in Update history.
3. If yours is newer, the WU package is a downgrade attempt — skip to hiding it (Fix 6).
4. If WU’s is newer, install it after pausing MyASUS’s auto-updates temporarily.

### Fix 3: Stop Armoury Crate and Windows Update fighting over drivers

Three ASUS-adjacent tools (MyASUS, Armoury Crate, Windows Update) all wanting to manage drivers is a recipe for file locks. Reducing it to one driver manager — MyASUS — eliminates the races.

1. Open Armoury Crate settings and disable its automatic driver updates.
2. In MyASUS, set driver checks to manual or a schedule away from Windows Update active hours.
3. Keep Windows Update for OS security patches only.
4. Verify only one tool manages drivers going forward.

### Fix 4: Clean-reinstall the ASUS driver from scratch

Interrupted ASUS updates can leave driver staging in a state neither tool can repair incrementally. A clean removal followed by a fresh ASUS-sourced install resets the device to a known-good state both tools can work with.

1. In Device Manager, uninstall the problem device, ticking “Delete the driver software”.
2. Restart and let Windows install its baseline driver.
3. Download the correct driver from ASUS support for your exact model.
4. Install it, restart, and confirm Windows Update stops failing on that device.

### Fix 5: Refresh the update cache to drop stale offers

The local catalog cache may keep offering driver versions ASUS already superseded. A cache refresh forces a new catalog query, which frequently clears phantom offers without needing the hide-updates tool.

1. Stop the services: net stop wuauserv, net stop bits (elevated Command Prompt).
2. Rename: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
3. Restart the services with net start.
4. Re-check Windows Update — stale ASUS-conflicting offers often disappear after the refresh.

### Fix 6: Hide the outdated Windows Update driver offers

When ASUS’s driver is right and Microsoft’s offer is outdated, hiding is the correct, supported resolution. It silences the failure loop permanently while OS security updates continue normally.

1. Download wushowhide.diagcab from [Microsoft Support](https://support.microsoft.com/en-us/windows).
2. Run it, choose Hide updates, and select the failing ASUS-conflicting drivers.
3. Verify they no longer appear in Windows Update.
4. Unhide only after a major Windows upgrade or ASUS BIOS update changes the hardware picture.

### Fix 7: Update the ASUS BIOS — firmware affects driver matching

An outdated ASUS BIOS can cause driver failures indirectly: Windows Update matches drivers against hardware IDs that the BIOS reports, and old firmware sometimes reports IDs that do not align with the catalog’s expectations. ASUS regularly ships BIOS updates improving Windows 11 compatibility, and the [Lenovo driver-matching guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-on-lenovo-laptop/) describes the same firmware-first principle on Lenovo hardware. Flash with care — charger connected, battery charged, no interruptions.

1. Check your current BIOS version: msinfo32 > BIOS Version/Date.
2. On ASUS support, find your exact model and compare with the latest BIOS release notes.
3. If the notes mention Windows 11, driver, or compatibility fixes, download the update.
4. Run the BIOS installer (via EZ Flash in the BIOS or the Windows utility) with AC power connected.
5. After the flash, re-run MyASUS driver checks and Windows Update — matching often improves immediately.

## Closing

ASUS laptops live in two driver worlds — ASUS’s own tooling and Microsoft’s catalog — and the failures happen where they overlap. Give ASUS’s tools ownership of your drivers, hide Microsoft’s conflicting offers, and the loop stops. Your hardware was never broken; the two updaters were just arguing over it.
