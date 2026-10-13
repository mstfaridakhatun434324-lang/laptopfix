---
title: "Driver Updates Failing in Windows Update? Diagnose and Fix Them"
slug: troubleshoot-driver-updates-failing-in-windows-update
date: 2026-09-29
categories: ["windows-update"]
tags: ["driver updates", "windows update", "troubleshoot", "drivers"]
description: "Driver updates keep failing inside Windows Update? Learn how to diagnose which driver is stuck, clear the failure, and get the right driver installed."
thumbnail: "/images/thumbs/troubleshoot-driver-updates-failing-in-windows-update.webp"
faqs:
  - q: "Why do driver updates fail in Windows Update?"
    a: "Driver updates fail for different reasons than regular updates: the driver may be incompatible with your exact hardware revision, a newer manufacturer driver may already be installed (causing a version conflict), the driver package may be corrupted in the cache, or Windows may lack permissions to replace a driver currently in use."
  - q: "Should I let Windows Update install drivers at all?"
    a: "For most users, yes — Windows Update drivers are tested and safe. But enthusiasts and gamers often prefer manufacturer drivers for GPUs and chipsets. A practical middle ground: let Windows handle routine drivers, but install GPU, chipset, and Wi-Fi drivers manually from the manufacturer for the latest fixes."
  - q: "How do I see which driver update failed?"
    a: "Go to Settings > Windows Update > Update history and expand Driver Updates. Each entry shows the device name, driver version, and failure code. That device name is your starting point — it tells you exactly which hardware's driver to fetch manually from the manufacturer."
  - q: "Can a failed driver update cause blue screens?"
    a: "A failed update itself usually can't — if it failed, it didn't install. The danger is a partially installed driver, which can cause instability. If crashes started around a driver update attempt, roll the device driver back in Device Manager and install the manufacturer's version instead."
---

# Driver Updates Failing in Windows Update? Diagnose and Fix Them

There's a special frustration reserved for driver updates that fail inside Windows Update. Regular updates either install or they don't — but driver updates fail with cryptic codes, retry forever, and sometimes leave a device in a half-updated limbo. Meanwhile Windows keeps offering the same failing driver like nothing's wrong.

The key insight: driver updates are a negotiation between Windows Update and your exact hardware, and the negotiation breaks down in predictable ways. This guide treats it as a diagnosis problem first — identify which driver, why it's failing, and whether Windows Update is even the right delivery method — then fixes it accordingly.

## Why this happens

- **Hardware revision mismatch.** Windows Update offers a driver for a hardware revision slightly different from yours; it fails applicability checks.
- **A newer driver already installed.** If the manufacturer's driver is newer than Windows Update's offering, the install conflicts and fails.
- **Corrupted driver package in the cache.** A damaged download fails signature or integrity checks every retry.
- **The device is in use.** Drivers for active devices (GPU, network) can fail when Windows can't safely unload the old driver.
- **Third-party driver utilities competing.** Manufacturer update tools installing the same driver simultaneously corrupt the attempt.
- **Insufficient permissions on driver store.** Damaged ACLs on the DriverStore block the staging of new drivers.
- **The device itself is failing.** A dying Wi-Fi card or SSD can fail driver installs repeatedly — the driver isn't the problem.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the Exact Failing Driver

Never troubleshoot "driver updates" generically — name the device first.

1. Go to **Settings > Windows Update > Update history** and expand the **Driver Updates** section.
2. Note each failed entry: the device name, the driver version offered, and the error code.
3. Open **Device Manager**, find that device, right-click **Properties > Driver** tab, and note the currently installed version and date.
4. Compare: if your installed driver is NEWER than the offered one, Windows Update is offering a downgrade — that's your answer, and Fix 6 (hiding it) is your fix.
5. If the versions differ in the other direction, the offered driver is legitimately newer and something is blocking it — continue below.

### Fix 2: Install the Driver Manually from the Manufacturer

The most reliable fix for a failing Windows Update driver: bypass Windows Update entirely.

1. Identify your exact laptop model and the device (e.g., "Intel Wi-Fi 6 AX201").
2. Download the driver from the manufacturer: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — or go straight to the chip maker (Intel, NVIDIA, or AMD) for component-level drivers.
3. Run the manufacturer's installer — these handle the unload/replace sequence more robustly than Windows Update.
4. Reboot when prompted, even if the installer doesn't insist.
5. Return to Windows Update and **Check for updates** — with the newer driver installed, the failing entry should disappear or show as successful.

### Fix 3: Clear the Corrupted Driver Package from the Cache

If the manual install isn't an option yet, purge the damaged package Windows Update keeps retrying.

1. Open an elevated Command Prompt.
2. Stop the services: `net stop wuauserv` and `net stop bits`.
3. Rename the cache: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Restart the services: `net start wuauserv` and `net start bits`.
5. Run **Check for updates** — Windows re-downloads a fresh copy of the driver package, which resolves corruption-induced failures. For a deeper rebuild of the whole pipeline, see [how to reset Windows Update components](/articles/how-to-reset-windows-update-components-on-windows-10/).

### Fix 4: Update the Driver via Device Manager

Device Manager uses a slightly different install path that sometimes succeeds where Windows Update fails.

1. Open **Device Manager**, right-click the problem device, and choose **Update driver**.
2. Select **Search automatically for drivers** — this queries the same catalog but installs immediately without the update pipeline.
3. If that fails, choose **Browse my computer for drivers** and point it at a driver folder you downloaded from the manufacturer.
4. For stubborn cases, first choose **Uninstall device** (checking **Delete the driver software** if offered), reboot, then install fresh — this clears a corrupted existing driver that blocks the update.
5. Verify in the device's **Properties > Driver** tab that the new version is active.

### Fix 5: Pause Competing Driver Tools During the Update

Manufacturer utilities and Windows Update installing the same driver simultaneously is a classic failure recipe.

1. Close or pause manufacturer update tools (Dell Update, HP Support Assistant, Lenovo Vantage, Intel DSA) before running Windows Update.
2. Pick ONE driver delivery channel per device: either the manufacturer tool or Windows Update, not both.
3. If you prefer manufacturer tools, hide the Windows Update driver offering using Microsoft's "Show or hide updates" troubleshooter.
4. Never run two driver installers at once — queue them sequentially.
5. After a successful install via one channel, the other channel stops offering that driver automatically.

### Fix 6: Hide the Problematic Driver Update

Sometimes the right answer is telling Windows Update to stop offering a driver you don't want.

1. Download Microsoft's "Show or hide updates" troubleshooter package.
2. Run it, choose **Hide updates**, and select the failing driver from the list.
3. Confirm in **Update history** that Windows no longer retries it.
4. Install the driver you actually want via the manufacturer instead (Fix 2).
5. Revisit hidden updates every few months — a future driver version may be worth unhiding. This is also the technique for [feature experience pack failures](/articles/how-do-i-fix-feature-experience-pack-failed-to-install/) that behave the same way.

### Fix 7: Check Whether the Hardware Is Failing

A driver that fails across every install method — Windows Update, Device Manager, manufacturer installer — points at hardware.

1. Try the manufacturer installer: if it fails with a device error rather than a software error, suspect the hardware.
2. Check **Device Manager** for the device disappearing and reappearing — intermittent detection means a loose or dying component.
3. For Wi-Fi/Bluetooth failures, test with a USB adapter: if the USB adapter works fine, the internal card is likely bad.
4. Run the manufacturer's hardware diagnostics (Dell, HP, and Lenovo all include boot-time diagnostics).
5. If hardware is confirmed bad, no driver will ever install — replace the component. For laptops with soldered parts, this means a repair shop visit, but at least you'll stop chasing a software ghost.

## Closing

Failing driver updates in Windows Update are a diagnosis-first problem: name the device, check the versions, then choose the right channel. Most resolve with a manual manufacturer install or a cache clear; the stubborn ones get hidden; the truly unfixable ones are hardware telling you the truth. Either way, you stop watching the same driver fail forever.
