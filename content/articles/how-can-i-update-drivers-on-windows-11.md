---
title: "How to Update Drivers on Windows 11 the Safe Way"
slug: how-can-i-update-drivers-on-windows-11
date: 2026-09-08
categories: ["drivers"]
tags: ["update drivers", "windows 11", "device manager", "driver update"]
description: "Update drivers on Windows 11 without breaking things: the safe order, the right sources, and how to recover if an update goes wrong."
thumbnail: "/images/thumbs/how-can-i-update-drivers-on-windows-11.webp"
faqs:
  - q: "Should I update all my drivers regularly?"
    a: "No — 'if it ain't broke, don't fix it' applies to drivers. Update graphics drivers for new games, network drivers for connectivity issues, and chipset drivers occasionally. Updating every driver on a schedule invites new bugs for zero benefit. Targeted updates for a reason beat blanket updates every time."
  - q: "Is Windows Update enough for driver updates?"
    a: "For basic functionality, mostly yes — Windows Update covers common hardware with stable, certified drivers. But it's often months behind on graphics and network drivers, and occasionally installs a generic driver that breaks maker-specific features. For GPUs and Wi-Fi, the maker's or chip vendor's site is the better source."
  - q: "Are third-party driver updater tools safe?"
    a: "Generally no. Many bundle adware, install wrong drivers, or charge for what manufacturers give away free. They solve a problem you don't have — finding drivers is easy via the laptop maker or Device Manager. The rare exceptions are tools from the chip vendors themselves, like Intel's Driver & Support Assistant."
  - q: "What should I do before updating drivers?"
    a: "Create a System Restore point, note your current working driver versions, and download the new driver before uninstalling the old one — especially for network drivers, since a bad update can take you offline. For graphics drivers, choose the clean install option. These five minutes of prep turn disasters into minor inconveniences."
---

Updating drivers on Windows 11 is simple in theory and surprisingly easy to get wrong in practice. The wrong source, the wrong order, or a blind "update everything" sweep can leave you with broken Wi-Fi, silent audio, or a misbehaving GPU. This guide covers the safe method: which drivers to update, where to get them, in what order, and how to recover when something goes sideways.

The golden rule: update with a purpose. A driver update should fix a problem, add a feature you need, or close a security hole — not satisfy an urge for the newest version number. Every driver change is a small risk; take it only when there's a payoff. And always prepare a way back before you start.

## Why this happens

- **Drivers go stale:** Old drivers develop incompatibilities with new Windows builds and applications.
- **Windows Update lags behind:** Microsoft's driver catalog trails chip vendors by months on key drivers.
- **Generic drivers lack features:** Windows' built-in drivers cover basics but miss maker-specific tuning.
- **Security vulnerabilities:** Old drivers occasionally carry security flaws that updates patch.
- **New hardware needs new drivers:** Added devices need drivers Windows doesn't include.
- **Corruption accumulates:** Driver files degrade over time through disk errors and failed updates.
- **Conflicting update sources:** Mixing Windows Update, maker, and vendor drivers creates version conflicts.
- **No recovery plan:** Most driver disasters are really "no restore point" disasters.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Prepare a recovery path first

Before touching any driver, create a System Restore point: search "Create a restore point," select your system drive, and click Create. Note your current driver versions for anything you plan to update (Device Manager, device Properties, Driver tab). Download new drivers before uninstalling old ones — critical for network drivers, where a failed update leaves you offline with no way to download the fix. Our [driver backup guide](/articles/how-to-backup-drivers-before-update-in-windows-11-24h2/) covers saving working drivers for quick restoration.

1. Create a System Restore point.
2. Record current driver versions for planned updates.
3. Download new drivers before removing old ones.
4. Keep a phone or second device handy for emergency downloads.
5. Know how to boot into Safe Mode before you need it.

### Fix 2: Use Windows Update for baseline drivers

Open Settings, Windows Update, and install all available updates, then check Advanced options, Optional updates, Driver updates — Microsoft lists certified driver updates here that are safe to install. This is the right source for obscure hardware (card readers, sensors, fingerprint readers) where the maker's site is hard to navigate. Let Windows handle the long tail of minor devices; save your manual effort for the drivers that actually matter, as Microsoft's Windows support pages document for the update process.

1. Install all regular Windows Updates first.
2. Check Optional updates, Driver updates.
3. Install certified drivers for minor hardware.
4. Reboot after the batch.
5. Verify everything still works before continuing.

### Fix 3: Get graphics drivers from the GPU maker

Graphics drivers deserve special treatment — they're the most impactful and most frequently updated. Use [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) for GeForce or [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics (AMD owners should use AMD's driver support page). Always choose the clean install option to wipe the old driver completely. For laptops, check the maker's support page first — some models need the tuned maker driver rather than the reference one.

1. Identify your exact GPU in Device Manager.
2. Download from the GPU maker's official page.
3. Choose clean/custom install, not express.
4. Check the laptop maker's page for tuned variants.
5. Reboot and verify with a quick graphics test.

### Fix 4: Get network and chipset drivers from the laptop maker

Wi-Fi, Bluetooth, and chipset drivers are the ones most likely to break when sourced wrong. Download these from your laptop manufacturer's support page for your exact model — [Dell](https://www.dell.com/support), for example; HP and Lenovo offer equivalent per-model downloads. Install chipset first, then network, then Bluetooth, rebooting between major ones. These maker packages include the correct firmware pairings and power profiles that generic drivers miss.

1. Download chipset, Wi-Fi, and Bluetooth packages for your model.
2. Install the chipset driver first and reboot.
3. Install Wi-Fi, then Bluetooth, rebooting after each.
4. Verify connectivity before moving on.
5. Keep the installers saved for future reinstalls.

### Fix 5: Update remaining devices via Device Manager

For anything left — audio, camera, touchpad, card reader — right-click the device in Device Manager and choose "Update driver," then "Search automatically." If Windows finds nothing but you know an update exists, use "Browse my computer" and point it at a driver you downloaded from the maker. Don't force updates on devices that work fine; the automatic search is conservative by design. If a device shows a warning icon, that's your signal it actually needs attention — see our [ELAN touchpad guide](/articles/how-do-i-fix-elan-touchpad-not-working/) for a worked example.

1. Right-click the device, Update driver, Search automatically.
2. Or browse to a manually downloaded driver.
3. Skip devices that already work correctly.
4. Prioritize devices showing warning icons.
5. Reboot after updating input or audio devices.

### Fix 6: Avoid driver updater utilities

Uninstall any third-party "driver booster" or "driver updater" tools — they routinely install wrong drivers, bundle unwanted software, and charge for free updates. The only semi-exceptions are vendor tools like Intel DSA or NVIDIA GeForce Experience, which come from the chip maker itself. If a sketchy updater already ran, check Device Manager for devices with new warning icons and roll back the drivers it changed (Driver tab, Roll Back Driver). Then create that restore point you skipped and do it properly.

1. Uninstall third-party driver updater tools.
2. Check Device Manager for new warning icons.
3. Roll back any drivers the tool changed.
4. Use a restore point if rollback isn't available.
5. Stick to maker and vendor sources going forward.

### Fix 7: Recover from a bad driver update

If an update breaks something, act quickly: in Device Manager, open the device's Properties, Driver tab, and click Roll Back Driver. If that's grayed out, uninstall the device with "Attempt to remove the driver for this device" ticked, then install your saved working version. If Windows won't boot properly, use Safe Mode (Shift+Restart, Troubleshoot, Startup Settings) and roll back from there. As a last resort, use System Restore to return to the point you created in Fix 1 — this is why you created it.

1. Try Roll Back Driver in the device's Driver tab.
2. Or uninstall with driver removed and reinstall the old version.
3. Boot into Safe Mode if normal boot is broken.
4. Use System Restore as the final fallback.
5. Block the bad driver version from reinstalling via Windows Update.

## Closing

Safe driver updating is 90% preparation and source discipline: restore point first, maker and vendor sources only, targeted updates with a reason, and a tested way back. Do that and driver updates become routine maintenance instead of Russian roulette. The drivers that matter most — graphics, Wi-Fi, chipset — reward the extra care; everything else can ride along with Windows Update.
