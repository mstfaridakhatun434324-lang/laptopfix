---
title: "Windows Update Error 0x800f020b on Laptop: Driver Update Fix"
slug: how-to-fix-windows-update-error-0x800f020b-on-laptop
date: 2026-09-27
categories: ["windows-update"]
tags: ["windows update error 0x800f020b", "driver update failed", "no applicable package", "hide windows update"]
description: "Error 0x800f020b means a driver update doesn't apply to your hardware. Hide the bad update and install the right driver from the maker."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f020b-on-laptop.webp"
faqs:
  - q: "What does error 0x800f020b mean?"
    a: "It means the update package does not apply to your system. Most often it is a driver update offered to hardware that does not match, for example a driver for a device variant you do not have, so the installer correctly refuses it and reports this code."
  - q: "Should I force-install a driver that gives 0x800f020b?"
    a: "No. The code means the package genuinely does not match your hardware. Forcing it risks installing the wrong driver and creating new problems. Get the correct driver from your laptop manufacturer's support page instead, matched to your exact model. The ten minutes this takes beats hours of failed retries."
  - q: "How do I stop Windows Update from retrying the bad driver?"
    a: "Use Microsoft's Show or Hide Updates troubleshooter to hide that specific update. Once hidden, Windows Update skips it permanently and the error stops reappearing in your update history on every check. The troubleshooter is small, safe, and reversible if you change your mind."
  - q: "Can 0x800f020b mean my device is failing?"
    a: "Sometimes. If the driver targets a device Windows can no longer detect properly, the mismatch can reflect a hardware problem, such as a failing Wi-Fi card presenting the wrong ID. But usually it is just a wrongly offered update."
---

Error 0x800f020b is Windows Update offering you the wrong driver and then failing to install it — which, to be fair, is the correct behavior. The package's applicability rules say it does not match your hardware, the installer agrees, and the attempt ends with this code instead of a wrong driver on your system.

This happens more than it should. Update catalogs occasionally mis-target driver packages, offering a variant for hardware you do not have or a revision your device IDs do not match. The result is a persistent failure that retries forever, because Windows Update never reconsiders its targeting.

The fix has two parts: silence the wrongly offered update so it stops failing, and install the right driver from the source that actually knows your hardware — the manufacturer.

There is something almost polite about 0x800f020b: Windows Update is refusing to install a driver it knows does not fit, rather than forcing it and breaking your hardware. The annoyance is that it keeps asking. The fixes below teach it to stop asking — by hiding the misfit update — and get you the driver that actually fits from the people who built the laptop.

If your machine is on 24H2 specifically, the [24H2-specific version of this fix](/articles/how-to-fix-windows-update-error-0x800f020b-in-windows-11-24h2/) adds the build-specific wrinkles — ghost devices, the Intel Driver & Support Assistant path, and how to block driver updates via policy for good.

## Why this happens

- **Mis-targeted driver package.** The update catalog offered a driver variant that does not match your device IDs.

- **Device IDs misreported.** A struggling device can present wrong hardware IDs, attracting the wrong driver.

- **Superseded driver still offered.** An outdated driver entry lingering in the catalog keeps being offered despite a newer driver installed.

- **Third-party driver already installed.** A manufacturer driver newer than the offered one makes the package inapplicable.

- **Corrupt driver store entry.** Damaged driver store data confuses the applicability check.

- **Device disabled in BIOS or Device Manager.** A disabled device may still attract its driver update while failing the applicability check.

- **OEM hardware variants.** Same-model laptops with different component revisions get each other's drivers offered.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Hide the bad update

The single most effective step. Microsoft's Show or Hide Updates troubleshooter lets you block the specific offending update so it never retries. The hide tool lists updates by title; match it carefully to the failed entry in update history, since hiding the wrong update solves nothing.

1. Download the Show or Hide Updates troubleshooter (wushowhide.diagcab) from Microsoft.
2. Run it, choose Hide updates, and select the failing driver update from the list.
3. Confirm it is hidden, then check for updates to verify the error is gone.

### Fix 2: Fix 2: Install the correct driver from the manufacturer

The manufacturer knows your exact hardware revision. Their driver is the one that actually applies, and it usually supersedes the bad offering. Manufacturer driver pages often list drivers by device category; if you are unsure which download matches, the hardware ID from Device Manager's Details tab settles it.

1. Find your exact model on the manufacturer's support site, Dell, HP, or Lenovo.
2. Download the driver for the device in question, install it, and restart.
3. Windows Update typically stops offering the wrong package once the correct driver is in place.

### Fix 3: Fix 3: Identify the device in Device Manager

Knowing which device the failed update targets focuses the whole repair. The update history names the driver, and Device Manager shows the device's health. A yellow warning icon on the device strengthens the case for a hardware problem; a clean device with this error points squarely at catalog mis-targeting.

1. Press Win + X and open Device Manager.
2. Look for the device matching the failed driver, and check for warning icons.
3. If the device shows an error, troubleshoot the device itself; a failing device explains the mismatch.

### Fix 4: Fix 4: Uninstall the device and reinstall its driver

A corrupted driver installation can fail applicability checks. Removing the device and letting Windows rediscover it rebuilds the driver stack cleanly. After the restart, wait for Windows to finish its automatic driver detection before installing the manufacturer's package; racing it can produce a driver conflict.

1. In Device Manager, right-click the device and choose Uninstall device.
2. If offered, check Delete the driver software for this device.
3. Restart and let Windows reinstall the driver, or install the manufacturer's driver manually.

### Fix 5: Fix 5: Pause driver updates via policy

If wrong drivers keep arriving, you can tell Windows Update to leave drivers alone entirely and manage them yourself from manufacturer sources. This policy affects all driver updates, so commit to checking the manufacturer's page periodically yourself; you are trading convenience for correctness.

1. Press Win + R, type `gpedit.msc`, and go to Computer Configuration, Administrative Templates, Windows Components, Windows Update, Manage updates offered from Windows Update.
2. Enable Do not include drivers with Windows Updates.
3. Run `gpupdate /force`. Manage drivers manually from then on.

### Fix 6: Fix 6: Reset the update cache

A stale cache can keep re-offering a driver that no longer applies. Clearing it forces a fresh applicability evaluation. The applicability evaluation happens during the metadata sync, so a cleared cache re-evaluates every offered driver against your actual hardware IDs.

1. In an administrator Terminal, run `net stop wuauserv` and `net stop bits`.
2. Delete everything in C:\Windows\SoftwareDistribution\Download and the DataStore folder.
3. Restart the services and check for updates.

### Fix 7: Fix 7: Check for a failing device

When the mismatch persists across everything, consider that the hardware itself is misreporting. A Wi-Fi card or SSD presenting wrong IDs will keep attracting wrong drivers. Manufacturer diagnostics usually include a component test for network and storage devices; run the specific test for the device attracting the wrong driver.

1. In Device Manager, check the device's Details tab, then Hardware Ids, against the manufacturer's specs.
2. Run the manufacturer's hardware diagnostics from their support page.
3. Replace the failing component if diagnostics confirm it. For general driver maintenance, our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/) keeps the stack healthy, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the hide-updates tool.

## Closing

Error 0x800f020b is Windows correctly refusing the wrong driver — the real problem is that it keeps being offered. Hide the bad update, install the manufacturer's correct driver, and the loop ends. Keep your driver stack maintained with our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official hide-updates troubleshooter.
