---
title: "Fixing Windows Update Error 0x800F020B on a Lenovo Laptop"
slug: how-to-fix-windows-update-error-0x800f020b-on-lenovo-laptop
date: 2026-09-08
categories: ["windows-update"]
tags: ["0x800f020b", "windows update", "lenovo", "update error"]
description: "Windows Update error 0x800F020B on your Lenovo laptop means an optional or driver component failed to install. Here is the exact order to clear it and get updates flowing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f020b-on-lenovo-laptop.webp"
faqs:
  - q: "What does Windows Update error 0x800F020B mean?"
    a: "Error 0x800F020B means Windows Update tried to install an optional component or device driver package and the installation was rejected. On Lenovo laptops this usually involves a Lenovo-published driver, a .NET Framework optional feature, or a firmware package that does not match your exact model."
  - q: "Will error 0x800F020B stop all my Windows updates?"
    a: "No. The error applies only to the specific component that failed, but it blocks the whole update batch from reporting success. Your cumulative security updates may still be waiting behind it, which is why you should clear the failed item rather than ignore the error."
  - q: "Should I download the driver from Lenovo instead?"
    a: "Yes, when the failing item is a Lenovo driver. Lenovo Vantage or the Lenovo support site offers the same driver packaged for your exact model, and it installs cleanly where the generic Windows Update package fails. This resolves most 0x800F020B cases on ThinkPad, IdeaPad, and Legion machines."
  - q: "Can I just hide the failing update?"
    a: "You can, as a last resort, by hiding the specific optional update with the wushowhide troubleshooter package. But first try the fixes in this guide, because hiding a driver update can leave hardware running on an older, less stable driver than the one Lenovo intended."
---

Error 0x800F020B shows up in Windows Update history with a terse message and no useful explanation: the update failed to install, and retrying changes nothing. On Lenovo laptops this code almost always traces back to the same thing — Windows Update attempting to install a driver or optional component package that your specific machine rejects. The download completes fine; the installation itself is refused.

I have seen this most often with Lenovo-published drivers for the chipset, power management, or fingerprint reader, and occasionally with .NET Framework optional features that fail their applicability check. The good news is that the error is narrow: it is about one package, not about Windows Update being broken. Work through the fixes below and you will either get the package installed properly or get it cleanly out of the way.

## Why this happens

- **A Lenovo driver package that fails its applicability check.** Windows Update offers a driver whose hardware ID or version does not match your machine, and the installer refuses it with 0x800F020B.
- **Corrupted component store.** Damage in the WinSxS store means optional components cannot be staged, so any feature-based update package fails at install time.
- **A stuck or partial download in the update cache.** The SoftwareDistribution cache holds a truncated copy of the package; Windows keeps retrying the same broken file.
- **Conflicting Lenovo Vantage driver installs.** Lenovo Vantage or Lenovo System Update installed the same driver separately, and the two packages now conflict during installation.
- **Disabled or damaged optional Windows features.** .NET Framework 3.5 or similar optional features with missing source files fail when the update tries to enable or patch them.
- **Third-party antivirus interfering with the installer.** Security software quarantines or blocks a driver installer mid-flight, producing a cryptic hex error instead of a clear message.
- **A pending restart from an earlier update.** An unfinished previous update holds a lock on the component store, so the new package cannot complete its transaction.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly which update is failing

Before fixing anything, confirm which package carries the 0x800F020B error so you treat the right thing.

1. Open **Settings** > **Windows Update** > **Update history** and look for the entry marked failed with error 0x800F020B.
1. Note whether it is a driver (it will name a device), a .NET Framework update, or a Lenovo firmware item.
1. If it is a driver, open **Device Manager** and check that device for a warning icon.
1. Write down the exact update name; you will need it in Fix 5.

### Fix 2: Run the Windows Update troubleshooter

The built-in troubleshooter resets the update pipeline and often clears a one-off 0x800F020B without further work.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
1. Run **Windows Update** and apply every fix it suggests.
1. Restart the laptop even if it does not ask you to.
1. Check for updates again and see whether the error repeats.

### Fix 3: Clear the SoftwareDistribution cache

A corrupted cached copy of the package is one of the most common causes, and clearing the cache forces a fresh download.

1. Open an elevated Command Prompt and run `net stop wuauserv` and `net stop bits`.
1. Rename `C:\Windows\SoftwareDistribution` to `C:\Windows\SoftwareDistribution.old`.
1. Run `net start wuauserv` and `net start bits`.
1. Run **Check for updates** and let the failed item download again from scratch.

### Fix 4: Repair the component store with DISM and SFC

If the failing package is an optional component, the store itself may need repair before anything will install.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to finish.
1. Then run `sfc /scannow` and restart when it completes.
1. Retry the update. Component-store errors such as [invalid package failures](/articles/how-to-fix-0x800f0900-update-error-after-windows-11-update/) often clear after this repair.
1. If DISM fails, the same repair logic applies before retrying.

### Fix 5: Install the driver from Lenovo instead

When the failing item is a Lenovo driver, the manufacturer's own package installs cleanly where the Windows Update copy fails.

1. Open **Lenovo Vantage** (install it from the Microsoft Store if missing) and check for driver updates.
1. Install any driver matching the failed update's device, then restart.
1. If Vantage does not offer it, get the driver from [Lenovo support](https://support.lenovo.com/us/en/) by entering your serial number.
1. After installing manually, Windows Update will see the driver as current and stop offering the broken package.

### Fix 6: Enable the .NET Framework source if that is the failing item

0x800F020B on a .NET Framework update usually means the optional feature cannot find its source files.

1. Open **Control Panel** > **Programs** > **Turn Windows features on or off**.
1. Check **.NET Framework 3.5 (includes .NET 2.0 and 3.0)** and click OK, letting Windows download the files.
1. If it fails, retry the Windows Update package afterward — the feature enablement was the blocker.
1. For persistent failures, an in-place repair install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) refreshes the feature store.

### Fix 7: Hide the update as a last resort

If one stubborn optional package keeps failing after every repair, hiding it lets the rest of your updates proceed normally.

1. Download the official wushowhide troubleshooter package from [Microsoft support](https://support.microsoft.com/en-us/windows).
1. Run it, choose **Hide updates**, and select the 0x800F020B item.
1. Confirm in **Update history** that no new failure is recorded.
1. Revisit the hidden update in a month — a revised package often appears. Related: [driver updates failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-reddit/).

## Closing

Error 0x800F020B looks alarming because of the hex code, but on a Lenovo laptop it is almost always one rejected driver or optional component, not a broken update system. Identify the failing package, clear the cache, repair the component store, and prefer Lenovo's own driver package when Windows Update's copy will not install. Once the offending item is resolved or hidden, your cumulative updates will install normally again.
