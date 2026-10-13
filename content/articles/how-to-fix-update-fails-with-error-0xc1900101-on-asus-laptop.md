---
title: "How to Fix Update Error 0xC1900101 on an ASUS Laptop"
slug: how-to-fix-update-fails-with-error-0xc1900101-on-asus-laptop
date: 2026-09-15
categories: ["windows-update"]
tags: ["0xc1900101 fix", "asus windows update error", "feature update rollback", "windows 11 upgrade failed"]
description: "Feature update keeps rolling back with 0xC1900101 on your ASUS laptop? Track the crashing driver in setuperr.log, refresh the BIOS, and finish the upgrade."
thumbnail: "/images/thumbs/how-to-fix-update-fails-with-error-0xc1900101-on-asus-laptop.webp"
faqs:
  - q: "Should I disconnect my second internal drive?"
    a: "When 0xC1900101 persists past the driver updates, yes — give it a try. Extra drives complicate the installer's drive mapping, and an unstable secondary drive can halt migration completely. Unplug it for the upgrade attempt and reconnect afterward. Label the cables first so reassembly is foolproof."
  - q: "Does 0xC1900101 mean my laptop is too old for Windows 11?"
    a: "Not necessarily. The code speaks to driver compatibility, not the age of the machine. Many five-plus-year-old ASUS laptops upgrade cleanly once the storage driver and BIOS are current. Treat age as the verdict only when ASUS lists your model as incompatible with the new build."
  - q: "What does 0xC1900101 mean in plain English?"
    a: "A driver crashed or stalled the Windows upgrade, so Windows gave up and rolled back. The system restores itself for safety, then shows this code. The code never identifies the driver — that is what the setup logs are for, and reading them is the fastest path to the fix."
  - q: "Which drivers cause 0xC1900101 most often?"
    a: "Storage drivers (Intel RST, NVMe), display drivers, and third-party antivirus filter drivers are the usual culprits. Peripheral drivers for docks, printers, and USB devices follow behind. Refreshing the BIOS, chipset, and storage drivers from ASUS support covers the most likely offenders."
---

An ASUS laptop that begins a Windows 11 feature update, retreats, and leaves 0xC1900101 behind is caught in a deterministic loop: the same driver will crash the same way on every attempt until it is updated, removed, or unplugged. Pressing Retry without changing anything changes nothing. [the same failure on Lenovo hardware](/articles/how-to-fix-update-fails-with-error-0xc1900101-on-lenovo-laptop/)

The ASUS-specific wrinkle: MyASUS driver bundles sometimes ship storage or chipset drivers that predate what the new Windows build requires. Updating ASUS's own drivers first — BIOS, chipset, and Intel RST above all — clears a disproportionate share of these failures before any log file gets opened.

## Why this happens

- **Overclocks or undervolts that cannot survive setup.** CPU and memory tweaks stable in daily use fall apart under installer load. Restore BIOS defaults to test; custom settings can return later.
- **MyASUS bundles older than the new build.** Bundled ASUS drivers predating what the upgrade expects. Cross-check MyASUS's versions against the latest on ASUS support.
- **A damaged system image.** Component-store corruption that SFC and DISM should fix before the installer runs. Both tools surface this ahead of time.
- **Extra drives scrambling the mapping.** Secondary disks confuse drive-letter and driver mapping; a failing second drive can stall migration. Detach it for the attempt.
- **An obsolete storage driver.** Aging Intel RST or NVMe drivers die during migration — the single biggest cause, with Intel RST and Samsung NVMe drivers filling the logs.
- **Antivirus filter drivers crashing mid-upgrade.** Kernel filters belonging to third-party security suites are a classic 0xC1900101 source. The vendor's removal tool — not the plain uninstaller — strips filter drivers completely.
- **A BIOS predating the new build.** ASUS firmware releases routinely carry the compatibility fixes new Windows builds demand; changelogs frequently mention upgrade compatibility outright.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean broken packages out of the driver store

Corrupt driver packages in the store sabotage migration. The rollback preserves everything, so a failed attempt costs only time — but an unchanged repeat costs time and teaches nothing.

1. From an elevated Command Prompt, list third-party drivers with pnputil /enum-drivers, then delete stale entries via pnputil /delete-driver oemXX.inf /uninstall (replace XX) — prioritizing hardware you no longer own.
2. Restart and retry the update.
3. Reinstall antivirus only after the upgrade completes and the system proves stable.

### Fix 2: Heal the image before the installer runs

Repair the component store before the installer leans on it. ASUS BIOS notes mentioning "Windows 11 compatibility" are often 0xC1900101 fixes in disguise.

1. In an elevated Command Prompt, run sfc /scannow, then DISM /Online /Cleanup-Image /RestoreHealth, and restart when both finish.
2. Retry the feature update.
3. DISM damage that refuses to clear points deeper — the in-place upgrade comes next. After a successful upgrade, restore BIOS customizations (XMP, undervolts) one at a time.

### Fix 3: Try the Installation Assistant instead

A different installation route sometimes walks around the crashing driver entirely. Virtualization-based security and memory integrity can also fight old drivers mid-upgrade; the logs usually say so plainly.

1. Download the Windows 11 Installation Assistant ([Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)) and run it with peripherals disconnected and antivirus removed, keeping files and apps.
2. Let it run to completion without interruption.
3. An identical failure means the driver needs the log-driven identification in Fix 5. After upgrading, run Windows Update fully so the new build collects the drivers it wants.

### Fix 4: Upgrade in place from the newest ISO

The last resort: the latest ISO carries the latest inbox drivers, which may already include the fix. Once the guilty driver is known, updating that driver — not reinstalling Windows — settles the vast majority of cases.

1. Fetch the newest Windows 11 ISO via [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), mount the image, and launch setup.exe — choosing "Keep personal files and apps" with peripherals unplugged first.
2. The newer inbox drivers often win where the older update stack failed.
3. Afterward, refresh ASUS drivers via [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows), and archive a copy of the failed attempt's setuperr.log in case the issue returns next feature update.

### Fix 5: Make the setup logs name the driver

The logs identify the failing driver with precision, and five minutes of reading can save hours of blind guessing. The decisive file is C:\$Windows.~BT\Sources\Panther\setuperr.log — search near the failure timestamp for .sys filenames.

1. Open C:\$Windows.~BT\Sources\Panther\setuperr.log in Notepad and search for "driver" or ".sys" near the end; note any driver file recurring around the failure time. Also inspect C:\Windows\Logs\MoSetup\ for BlueBox logs on newer builds.
2. Search the web for the filename to identify its device, then update or remove that device's driver.
3. After retrying, re-read setuperr.log to confirm the previously failing driver is gone.

### Fix 6: Unplug everything nonessential

Eliminate the whole peripheral-driver category in one stroke. With 0xC1900101, extend code 0x20017 signals a failed boot-critical driver while 0x30018 points at a driver in the specialize phase — the extend code narrows the search.

1. Unplug every USB device except a keyboard and mouse if needed; disconnect external hard drives, docks, printers, and SD cards. If a second internal drive can sit out the upgrade, disconnect that too.
2. Retry the update with only the charger attached.
3. Confirm in msinfo32 that the reported BIOS version matches the one you meant to flash.

### Fix 7: Modernize BIOS, chipset, and storage drivers

The highest-value blind repair: drag ASUS's core drivers into the present. [The 24H2 0xc1900101 guide](/articles/how-to-fix-error-0xc1900101-in-windows-11-24h2/) notes that Intel RST drivers older than version 18.x are the most common single trigger — check yours in Device Manager under Storage controllers.

1. On ASUS support, enter your model or serial number, then flash the newest BIOS first with the charger connected and zero interruptions.
2. Install the latest chipset and Intel RST / storage drivers, restarting between each major driver.
3. Retry the feature update once the stack is current, after scanning Device Manager for lingering yellow warnings.

## Closing

0xC1900101 always means a driver has declared it cannot survive the upgrade — identify the driver and the fix is yours. The setup logs name it directly for precision; the blind sequence of unplugging peripherals, refreshing ASUS drivers, and stripping antivirus covers the cases where you skip the logs. For other upgrade-failure codes, [the Windows 10 version of this error](/articles/how-to-fix-error-0xc1900101-on-windows-10/) applies identical detective work.
