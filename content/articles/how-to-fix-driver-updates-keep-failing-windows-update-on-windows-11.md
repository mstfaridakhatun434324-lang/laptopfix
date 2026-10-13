---
title: "How to Fix Driver Updates That Keep Failing in Windows Update on Windows 11"
slug: "how-to-fix-driver-updates-keep-failing-windows-update-on-windows-11"
date: 2026-10-05
categories: ["windows-update"]
tags: ["windows update", "driver updates", "windows 11", "device manager"]
description: "Driver updates keep failing in Windows Update on Windows 11? Learn why optional driver installs fail and 6 fixes — from manual installs to hiding bad updates — that actually work."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-keep-failing-windows-update-on-windows-11.webp"
faqs:
  - q: "Why does Windows Update keep offering a driver I already installed?"
    a: "Windows Update checks its own catalog on a schedule and does not always detect manufacturer-installed drivers correctly. If the catalog version differs from yours — even when yours is newer — it offers the package anyway. Installing it can fail with error 0x80070103, which specifically means the driver is not needed. Hiding that update with the wushowhide tool stops the loop without affecting future updates."
  - q: "Is it safe to install drivers from Windows Update at all?"
    a: "Yes, Windows Update drivers are WHQL-tested and safe, but they are usually months older than manufacturer releases and stripped of control-panel extras. For graphics, Wi-Fi, and chipset drivers, the manufacturer’s package is the better choice. Use Windows Update drivers for obscure peripherals where no manufacturer installer exists, and hide any that repeatedly fail after you have installed the newer official version."
  - q: "What does error 0x80070103 mean on a driver update?"
    a: "Error 0x80070103 means Windows tried to install a driver that is already present or older than the installed version — essentially an attempted downgrade. It is not a system problem and does not indicate corruption. The fix is to hide that specific update so Windows Update stops offering it, rather than trying to force the installation through."
  - q: "Should I use third-party driver updater software instead?"
    a: "No. Third-party driver updaters are a frequent cause of the very conflicts described here, and some bundle unwanted software or install incorrect drivers. Stick to Windows Update, your laptop manufacturer’s support page, or the component maker’s official tool such as Intel DSA or NVIDIA’s installer. If a third-party updater is already installed, remove it before troubleshooting further."
---

You open Settings > Windows Update, see a driver update for your graphics card or Wi-Fi adapter, hit install — and it fails with an error code, or downloads forever and rolls back. You retry, and it fails again exactly the same way. Meanwhile the same driver installs fine when you grab it directly from the manufacturer, which makes the whole thing feel absurd.

This loop is one of the most common Windows 11 complaints, and it has a clear logic: Windows Update delivers generic, WHQL-signed driver packages on its own schedule, and it will stubbornly retry a package that conflicts with a newer manufacturer driver already on your system. If the same failure is happening on an older machine, the [Windows 10 version of this problem](/articles/how-to-fix-driver-updates-keep-failing-windows-update-on-windows-10/) uses slightly different screens but the same underlying causes.

## Why this happens

- **Newer manufacturer driver already installed:** If you installed a newer driver from NVIDIA, Intel, or your laptop maker, Windows Update may still offer its older packaged version, which then fails because the system refuses to downgrade.
- **Corrupted driver store entries:** Partially installed driver packages leave broken entries in the Windows driver store, and every retry trips over the same leftover files.
- **Driver signature or compatibility block:** Windows 11 enforces driver signature checks strictly; a package whose signature chain or hardware ID matching is off will fail every install attempt.
- **Third-party driver updaters interfering:** OEM utilities and third-party updater tools can lock driver files or replace them mid-install, causing Windows Update’s version check to fail.
- **Insufficient permissions on driver folders:** If the SYSTEM account lost write access to the driver store (often after a botched cleanup tool run), the installer cannot stage files and fails silently.
- **Corrupted Windows Update components:** A damaged update cache or stuck Background Intelligent Transfer Service affects driver packages just like it affects cumulative updates.
- **Metered connection blocking the download:** Driver packages are classed as optional, so a metered connection setting can starve the download mid-way and report the install as failed.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Check which driver is actually failing and its error code

Blindly retrying wastes time. Windows records the exact driver name and error code in the update history, and that code tells you whether you are dealing with a conflict, a download problem, or a permissions issue. Write both down before doing anything else.

1. Open Settings > Windows Update > Update history and expand Driver updates.
2. Note the driver name, version offered, and the error code (for example, 0x80070103 means a driver conflict).
3. Open Device Manager, find the device, and compare its current driver version with the one Windows Update offers.
4. If your installed version is newer, the correct fix is to hide the update (Fix 6), not to force the older one in.

### Fix 2: Install the driver manually from the official source

The manufacturer package is almost always newer and more complete than the Windows Update repackaging. Installing it directly resolves the device’s actual need, after which Windows Update usually stops offering the older package. Use only official sources — never random driver-download sites.

1. Identify your hardware: GPU, Wi-Fi chip, or laptop model and service tag.
2. Download from the official page: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or your laptop maker’s support site.
3. Run the installer, choosing “Clean install” if the option exists for graphics drivers.
4. Restart, then check Windows Update — the failed driver entry should disappear or succeed.

### Fix 3: Clean out the broken driver package with Device Manager

When a partial install has poisoned the driver store, removing the device’s driver package completely gives Windows a clean slate. The “delete the driver software” checkbox is the key part most people skip — without it, Windows just reinstalls the same broken files.

1. Open Device Manager, right-click the problem device, and choose Uninstall device.
2. Tick “Attempt to remove the driver for this device” (or “Delete the driver software”) before confirming.
3. Restart the laptop and let Windows install its built-in baseline driver.
4. Return to Windows Update and retry the driver update on the clean baseline.

### Fix 4: Reset the Windows Update components

Driver packages download through the same pipeline as system updates, so a corrupted cache produces identical failures. Resetting the services and renaming the cache folders forces a fresh download of the driver package metadata and files.

1. Open an elevated Command Prompt.
2. Run these four commands: net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver.
3. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the four services with net start, then check for updates again.

### Fix 5: Rule out metered connection and third-party interference

Because driver updates ship as optional content, Windows quietly skips or truncates them on metered networks. Third-party driver utilities can also fight Windows Update for control of the same device. Eliminate both variables before concluding the package itself is broken.

1. Go to Settings > Network & internet > Wi-Fi (or Ethernet), open your connection, and turn off Metered connection.
2. Temporarily uninstall or disable any third-party driver updater tools.
3. Pause and unpause Windows Update once to refresh the download queue.
4. Retry the driver install and watch whether it now completes.

### Fix 6: Hide the bad update so it stops retrying

When the offered driver is simply wrong for your hardware — older than what you have, or mismatched — the correct outcome is not a successful install but a stopped one. Microsoft’s “Show or hide updates” troubleshooter lets you block a specific update package permanently.

1. Download the “Show or hide updates” troubleshooter (wushowhide.diagcab) from [Microsoft Support](https://support.microsoft.com/en-us/windows).
2. Run it, choose Hide updates, and tick the failing driver package.
3. Confirm it no longer appears in Windows Update.
4. Revisit this only after a major Windows version upgrade, which can legitimately bring a newer driver package.

### Fix 7: Roll back a driver that installed but misbehaves

Sometimes the failure runs in reverse: a Windows Update driver installs “successfully” and then the device misbehaves — Wi-Fi drops, audio crackles, the screen flickers. Windows 11 keeps the previous driver available for exactly this situation, and rolling back is faster than any reinstall. On 24H2 systems the driver model is stricter, so a marginal driver that worked on 23H2 can start failing after the upgrade — the [24H2 driver-failure guide](/articles/how-to-fix-driver-updates-keep-failing-windows-update-in-windows-11-24h2/) covers those version-specific quirks in detail.

1. Open Device Manager, right-click the misbehaving device, and choose Properties.
2. Open the Driver tab and click “Roll Back Driver” — if the button is greyed out, no previous driver was kept.
3. Choose a reason (the previous driver worked better) and confirm; restart the laptop.
4. After rolling back, hide the problematic driver offer with wushowhide so Windows Update does not reinstall it.
5. Then install the manufacturer’s known-good driver version directly to stay current without the bad package.

## Closing

Driver update failures in Windows 11 are rarely a sign of broken hardware — they are almost always version conflicts, stale cache, or a package that was wrong for your machine to begin with. Diagnose with the error code first, install the manufacturer’s driver directly when you can, and hide the update when Windows is simply offering you a downgrade you do not need.
