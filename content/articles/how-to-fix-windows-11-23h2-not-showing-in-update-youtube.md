---
title: "Windows 11 23H2 Not Showing in Windows Update? How to Fix It"
slug: how-to-fix-windows-11-23h2-not-showing-in-update-youtube
date: 2026-09-12
categories: ["windows-update"]
tags: ["windows 11 23h2", "feature update", "not showing", "windows update"]
description: "Windows 11 23H2 isn't offered in Windows Update? Here's why the feature update is hidden and how to make it appear."
thumbnail: "/images/thumbs/how-to-fix-windows-11-23h2-not-showing-in-update-youtube.webp"
faqs:
  - q: "Why isn't 23H2 offered to my laptop?"
    a: "Microsoft rolls out feature updates in waves and blocks machines with known compatibility issues, called safeguard holds. If your laptop has a driver or hardware combination Microsoft has flagged, Windows Update withholds the offer until the blocker is resolved. It can also be hidden by group policy, a paused update state, or corrupted update components."
  - q: "Is it safe to force the 23H2 update?"
    a: "Generally yes if your hardware meets the requirements and you have current backups. The main risk is bypassing a safeguard hold that exists for your specific hardware, which can cause driver issues after the upgrade. Check for known issues for your model first, and use the official Installation Assistant rather than unofficial tools."
  - q: "How long do safeguard holds usually last?"
    a: "Most safeguard holds are lifted within weeks to a few months as Microsoft and hardware vendors ship fixed drivers. If 23H2 has been available for many months and still is not offered, the hold on your configuration may be long-term, and a manual upgrade path becomes the practical option."
  - q: "Will forcing the update delete my files?"
    a: "No. Both the Installation Assistant and an in-place upgrade keep your files, applications, and settings. They only replace the Windows system files. Still, back up anything irreplaceable first — any major system change carries a small risk, and a backup makes it a non-issue."
---

You know Windows 11 23H2 exists. Other laptops have it. But your Windows Update page cheerfully reports "You're up to date" with no feature update in sight. This is one of the most common Windows Update complaints, and it is usually not a malfunction at all — Microsoft deliberately withholds feature updates from machines with compatibility blocks, and a handful of settings and states can hide the offer even when no block exists.

Microsoft's rollout system works in waves for a reason. When a feature update first ships, it goes to a small set of machines with well-understood hardware; telemetry from those installs identifies problematic driver and firmware combinations, which Microsoft then adds to a safeguard hold list that blocks the offer for matching machines. Your laptop is checked against that list every time it scans. If it matches a hold — say, a particular audio driver version known to break — the offer is silently withheld until the hold is lifted. It is protection, not punishment, though it is understandably annoying when nobody tells you that you are being protected.

The trick is distinguishing "Microsoft is protecting you from a bad upgrade" from "your update pipeline is broken." This guide walks through that distinction and gives you the safe paths to 23H2 either way.

## Why this happens

- **A safeguard hold on your hardware.** Microsoft blocks the update for specific driver, firmware, or hardware combinations with known issues. This is the most common reason.
- **Staged rollout timing.** Feature updates roll out in waves over months; your machine simply may not have been offered it yet.
- **Paused or deferred updates.** An old pause setting, or a deferral policy from a previous Windows version, hides feature updates.
- **Group Policy blocking feature updates.** A "TargetReleaseVersion" policy or similar can pin the machine to its current version.
- **Corrupted update components.** A broken update engine may fail to evaluate or display the feature update offer.
- **Insufficient disk space.** Feature updates need significant free space; below the threshold, Windows Update hides the offer silently.
- **Unsupported hardware edge cases.** Machines that barely meet requirements, or that upgraded from Windows 10 on marginal hardware, can be excluded from the offer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check for a safeguard hold and known issues

Find out whether Microsoft is deliberately withholding the update from you.

1. Note your laptop's exact model, then search Microsoft's release health information for Windows 11 23H2 known issues affecting your hardware.
2. Open **Device Manager** and check for any devices with warning icons — problematic drivers are the usual trigger for holds.
3. If a hold applies to your configuration, the safest move is to wait for the fixed driver. Forcing past a hold is possible but risks the exact problem Microsoft was protecting you from.

### Fix 2: Clear pauses, deferrals, and target-version policies

Remove settings that hide feature updates.

1. In **Settings** > **Windows Update** > **Advanced options**, make sure updates are not paused and no deferral periods are set.
2. Press **Windows key + R**, type `gpedit.msc` (Pro editions), and check **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Windows Update** > **Manage updates offered from Windows Update** for any configured target version — set it to **Not configured**.
3. In the Registry, check `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` for a `TargetReleaseVersion` value and remove it if present.

### Fix 3: Free up disk space

Feature updates need room to stage.

1. Open **Settings** > **System** > **Storage** — you want at least 20 GB free, ideally more.
2. Run **Disk Cleanup** with **Clean up system files** and remove old update files and temporary data.
3. Retry **Check for updates**. The offer can appear once the space check passes.

### Fix 4: Reset the update components

A broken engine cannot evaluate the feature update offer.

1. Open an elevated Command Prompt and reset the cache:
   ```
   net stop wuauserv
   net stop bits
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   net start wuauserv
   net start bits
   ```
2. Click **Check for updates** and wait for the scan to complete fully — feature update offers can take several minutes to appear.
3. If the engine itself is the problem, [resetting the full set of update components](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) covers the deeper repair.

### Fix 5: Use the Windows 11 Installation Assistant

Microsoft's official tool bypasses the Windows Update offer mechanism.

1. Visit the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and download the **Installation Assistant**.
2. Run it and follow the prompts. It checks compatibility itself and upgrades you to the current feature version.
3. This is Microsoft's supported path for machines that are not being offered the update — far safer than registry hacks or third-party tools.

### Fix 6: Check the Lenovo-specific variant

Some Lenovo models had model-specific blocks on 23H2.

1. If you have a Lenovo laptop, compare with our guide on [23H2 not showing on Lenovo laptops](/articles/how-to-fix-windows-11-23h2-not-showing-in-update-on-lenovo-laptop/), which covers the model-specific holds.
2. Update the BIOS and chipset drivers from the manufacturer's support site before retrying — outdated firmware is a frequent hold trigger.
3. After updating firmware, run **Check for updates** again; holds tied to firmware versions can clear immediately.

### Fix 7: Do an in-place upgrade with the ISO

The final reliable path when the offer will not appear.

1. Download the Windows 11 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount it, run `setup.exe`, and choose **Keep personal files and apps**.
3. This performs the feature upgrade directly, ignoring the Windows Update offer logic entirely. It takes 30–90 minutes and leaves everything in place.

## Closing

A missing 23H2 offer is usually Microsoft's safeguard system doing its job, not a broken PC. Check for holds first, clear any policies hiding the update, and then use the Installation Assistant — Microsoft's own supported bypass — rather than fighting Windows Update. The offer mechanism is conservative by design; the Assistant gives you the same upgrade on your own schedule, once you have confirmed your hardware is ready for it.
