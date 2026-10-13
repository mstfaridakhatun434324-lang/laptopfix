---
title: "How to Fix Driver Updates That Keep Failing in Windows Update on Windows 10"
slug: "how-to-fix-driver-updates-keep-failing-windows-update-on-windows-10"
date: 2026-10-06
categories: ["windows-update"]
tags: ["windows update", "driver updates", "windows 10", "wushowhide"]
description: "Driver updates keep failing in Windows Update on Windows 10? Six practical fixes covering error codes, manual installs, cache resets, and hiding bad updates on Windows 10."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-keep-failing-windows-update-on-windows-10.webp"
faqs:
  - q: "Where do I find optional driver updates on Windows 10?"
    a: "Open Settings, go to Update and Security, then Windows Update, and click View optional updates. Driver updates are listed there separately from quality and feature updates. Expanding the Driver updates section lets you select individual drivers to install. If a driver keeps failing, note its exact name and error code here before troubleshooting — that information drives every fix that follows."
  - q: "Does the wushowhide tool still work on Windows 10?"
    a: "Yes. Microsoft’s Show or hide updates troubleshooter (wushowhide.diagcab) still works on Windows 10 and remains the supported way to block a specific problematic update. Download it from Microsoft Support, run it, choose Hide updates, and tick the failing driver. The update will no longer be offered. You can run the tool again later and choose Show hidden updates to reverse it after a feature update."
  - q: "Why do driver updates fail more on old Windows 10 laptops?"
    a: "Older Windows 10 installs accumulate stale driver packages, registry leftovers, and cache corruption over years of updates, all of which raise the odds of a conflict. Aging hard drives add bad sectors in the driver staging area. A component reset plus a clean manual install from the manufacturer’s site resolves most of these cases, and hiding obsolete driver offers prevents the loop from restarting."
  - q: "Can a failing driver update break my working hardware?"
    a: "Almost never. A failed install rolls back to the previous driver, so your hardware keeps working with the driver it had. The risk is annoyance, not damage — the update will simply keep retrying. The exception is repeatedly force-installing mismatched drivers from unofficial sources, which is why you should use official manufacturer packages and hide Windows Update offers that conflict with them."
---

On Windows 10 the pattern is familiar: Settings > Update & Security > Windows Update shows a driver update pending, it downloads, the install bar crawls, and then it fails — sometimes with an error code, sometimes with nothing but a red “failed to install” line. Retry it tomorrow and the same thing happens, like clockwork.

Windows 10 handles drivers a little differently than Windows 11 — the screens live under Update & Security, optional drivers appear under “View optional updates,” and the old wushowhide tool remains the official way to block a bad package. If you have already moved to the newer OS, the [Windows 11 version of this guide](/articles/how-to-fix-driver-updates-keep-failing-windows-update-on-windows-11/) covers the same failures with Windows 11’s screens and paths.

## Why this happens

- **Optional driver offered against a newer installed version:** Windows 10 lists driver updates under optional updates but still auto-retries some of them; when the offered version is older than your manufacturer-installed driver, the install fails with 0x80070103.
- **Stale driver packages in the driver store:** Years of accumulated driver versions on an older Windows 10 install create conflicts where a new package trips over remnants of a half-removed old one.
- **Windows Update cache corruption:** The SoftwareDistribution cache on long-running Windows 10 systems accumulates damage from interrupted downloads, and driver packages fail the integrity check on install.
- **Group Policy or registry driver blocks:** Some Windows 10 Pro systems have “Do not include drivers with Windows Updates” enabled (or a third-party tool set it), producing confusing partial-failure behavior.
- **Antivirus quarantining driver installers:** Overzealous security software occasionally flags the temporary driver installer files Windows Update extracts, killing the install mid-process.
- **Failing disk sectors in the driver store:** On older laptops still running hard drives, bad sectors in the driver staging area cause repeatable, identical failures for the same package.
- **OEM utility conflicts:** Manufacturer update tools running their own driver schedule can replace files while Windows Update is installing, failing both attempts.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Read the update history for the exact error code

Windows 10 logs every attempt under Settings > Update & Security > Windows Update > View update history. The error code next to the failed driver is your diagnosis: 0x80070103 means a version conflict, 0x80070002 points to missing files, and 0x80240034 indicates a download that never completed.

1. Open Settings > Update & Security > Windows Update > View update history.
2. Expand Driver Updates and record the driver name, offered version, and error code.
3. In Device Manager, check the device’s current driver version for comparison.
4. If the installed driver is newer, skip to Fix 6 (hide the update) — forcing it is pointless.

### Fix 2: Install the manufacturer’s driver package directly

The driver on your laptop maker’s support page or the chip maker’s site is newer, includes the full feature set, and installs with its own tested installer. Once it is in place, Windows 10 usually withdraws the older optional offer automatically.

1. Note your exact laptop model and the device in question.
2. Download the driver from the official source: your laptop maker’s support site, [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html).
3. Uninstall the current device driver from Device Manager first if versions are close, ticking delete-driver-software.
4. Install the downloaded package, restart, and re-check Windows Update.

### Fix 3: Remove the broken driver and let Windows rediscover the device

A clean removal clears the corrupted staging that repeated retries keep tripping on. Windows 10’s plug-and-play will reinstall a baseline driver on the next boot, giving the update a clean target.

1. Open Device Manager (Win + X > Device Manager).
2. Right-click the device > Uninstall device, and tick “Delete the driver software for this device”.
3. Restart the laptop; Windows installs its inbox driver automatically.
4. Go to Windows Update > Check for updates and let the driver offer come back fresh.

### Fix 4: Reset Windows Update components the Windows 10 way

The classic component reset still works on Windows 10 and fixes the cache corruption behind a large share of repeat driver failures. Stopping the services first is essential — renaming folders while they are in use does nothing.

1. Run Command Prompt as administrator.
2. Stop services: net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver.
3. Rename the caches: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart all four services with net start, then run Check for updates.

### Fix 5: Check the driver-related policies and optional-updates view

Windows 10 Pro systems sometimes carry a policy that partially blocks driver delivery, and the optional-updates screen itself can hold a stuck selection. Verifying both removes a whole class of silent failures.

1. Open “View optional updates” under Windows Update > Advanced options and clear any stuck driver selections.
2. Press Win + R, type gpedit.msc, and check Computer Configuration > Administrative Templates > Windows Components > Windows Update for driver-exclusion policies.
3. If “Do not include drivers with Windows Updates” is Enabled and you want drivers from WU, set it to Not Configured.
4. Run gpupdate /force in an elevated prompt, then check for updates again.

### Fix 6: Hide the failing update with wushowhide

When the package is simply wrong for your hardware — an older version, a mismatched hardware ID — the professional fix is to block it. Microsoft’s Show or hide updates troubleshooter was built for exactly this on Windows 10 and remains available.

1. Download wushowhide.diagcab from [Microsoft Support](https://support.microsoft.com/en-us/windows).
2. Run it, click Next, choose Hide updates, and select the failing driver.
3. Verify the driver no longer appears under Check for updates.
4. Unhide it only after a Windows 10 feature update, which may ship a genuinely newer driver package.

### Fix 7: Block driver delivery with Group Policy on Windows 10 Pro

When hiding individual updates feels like whack-a-mole — a new bad driver offer every month — Windows 10 Pro offers a structural fix: a Group Policy that stops Windows Update from delivering drivers at all. With this set, you manage drivers entirely through manufacturer installers (the approach the [Dell driver guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-on-dell-laptop/) recommends for Dell hardware), and Windows Update handles only OS patches. It is the cleanest long-term answer for systems where WU drivers chronically conflict.

1. Press Win + R, type gpedit.msc, and press Enter.
2. Navigate to Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update.
3. Open “Do not include drivers with Windows Updates” and set it to Enabled.
4. Run gpupdate /force in an elevated Command Prompt, then restart.
5. From now on, source every driver from your laptop maker or the chip manufacturer — Windows Update will no longer offer (or fail on) any.

## Closing

On Windows 10, a driver update that fails twice will fail forever until the underlying conflict is removed — retrying without changes is the definition of this particular insanity. Read the error code, install the manufacturer’s package when it is newer, reset the cache when downloads are corrupt, and hide the update when Windows is offering you something your machine does not need.
