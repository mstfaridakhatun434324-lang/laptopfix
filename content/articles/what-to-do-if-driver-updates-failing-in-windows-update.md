---
title: "Driver Updates Keep Failing in Windows Update? Fix Them for Good"
slug: what-to-do-if-driver-updates-failing-in-windows-update
date: 2026-10-11
categories: ["windows-update"]
tags: ["driver updates", "windows update", "device manager", "windows 11 24h2", "troubleshooting"]
description: "Stop driver updates from failing in Windows Update: isolate the conflicting driver, clean-install the right version, and prevent bad updates from reinstalling."
thumbnail: "/images/thumbs/what-to-do-if-driver-updates-failing-in-windows-update.webp"
faqs:
  - q: "Why do driver updates fail while other updates install fine?"
    a: "Drivers install through a different pipeline than cumulative updates: they must match your exact hardware ID and pass signature checks. A mismatched, unsigned, or vendor-blocked driver fails even when the rest of Windows Update works perfectly. Treating driver failures as a separate pipeline keeps you from wasting time on cumulative-update repairs that cannot help."
  - q: "Should I let Windows Update install drivers at all?"
    a: "For most laptops, yes for chipset, network, and input drivers, but get graphics and audio drivers from the manufacturer when possible. Vendor drivers are tested against your exact model, while Windows Update sometimes pushes generic versions that conflict. A hybrid policy — Windows Update for basics, vendor drivers for graphics and audio — gives the best reliability on most laptops."
  - q: "How do I stop a bad driver update from reinstalling?"
    a: "Use Microsoft's Show or Hide Updates troubleshooter package to hide the specific driver update after rolling it back. Alternatively, use Group Policy or the registry to block driver updates from Windows Update while still receiving security patches. The hide only lasts until a feature update refreshes the list, so re-check after each major Windows upgrade."
  - q: "Can a failing driver update damage my laptop?"
    a: "Rarely. Failed driver installs roll back automatically. The real risk is a partially installed graphics or storage driver causing blue screens or boot loops, which is why you should back up and create a restore point before forcing driver updates."
---

When Windows Update sails through its cumulative patches but chokes every time on driver updates, you are dealing with a different beast than ordinary update failure. Drivers are hardware-specific, signature-checked, and version-sensitive — and Windows Update's driver catalog sometimes offers your laptop a driver that was never meant for it. The result: endless "failed to install" entries, optional updates that never complete, and occasionally a driver that installs and promptly blue-screens the machine.

This guide treats failing driver updates as a driver-management problem first and an update problem second. You will identify exactly which driver is failing, decide whether Windows Update should even be delivering it, and install the correct version from the right source — then block the bad one from coming back.

## Why this happens

- **Wrong driver for the hardware:** Windows Update matches on hardware IDs, and similar-but-different laptop variants sometimes receive each other's drivers, which fail signature or compatibility checks mid-install.
- **Vendor blocks and holds:** Laptop makers can place compatibility holds on specific driver versions; Windows Update keeps offering the update but the installer refuses it.
- **Newer driver already installed:** If you manually installed a newer vendor driver, Windows Update may still offer its older catalog version, which fails because Windows will not downgrade silently.
- **Corrupted driver store:** The DriverStore folder accumulates stale and half-installed driver packages; corruption there makes every new driver install fail the same way.
- **Signature enforcement failures:** Damaged catalog files or disabled driver signature checks cause signed-driver validation to fail during installation.
- **Conflicting third-party driver tools:** "Driver updater" utilities install their own versions and lock files, so the Windows Update installer cannot replace them.
- **Insufficient permissions or pending reboot:** Driver installation needs a clean servicing state; pending operations from a previous install block the next one.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly which driver is failing

1. Open **Settings > Windows Update > Update history** and expand **Driver Updates** — note the exact driver name, version, and error code.
2. Open **Device Manager**, find the device, right-click **Properties > Driver**, and compare the installed version to the offered one.
3. If the offered version is older than what is installed, Windows Update is trying to downgrade — skip to Fix 6 to block it.
4. Write down the error code (0x80070103 means "a better driver is already installed," which is informational, not a real failure).

### Fix 2: Install the vendor driver directly and let it win

1. Go to your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and enter your exact model or serial number.
2. Download the driver for the failing device (graphics, Wi-Fi, audio, or chipset) and install it manually, choosing **Clean install** if the installer offers it.
3. For Intel graphics or Wi-Fi, the Intel Driver and Support Assistant finds the correct build automatically.
4. After the vendor driver installs, Windows Update usually stops offering its version — the correct driver "wins" the version comparison. This is also the approach in our [driver update walkthrough](/articles/best-way-to-update-drivers-on-windows-11/).

### Fix 3: Roll back a driver that installed badly

1. In **Device Manager**, right-click the device and choose **Properties > Driver > Roll Back Driver** if the button is available.
2. Pick the reason "previous version worked better" and restart when prompted.
3. If rollback is greyed out, uninstall the device (tick **Attempt to remove the driver**), restart, and let Windows install its inbox driver.
4. Detailed rollback steps are covered in our guide to [rolling back a driver update](/articles/best-way-to-rollback-driver-update/) — follow it before the bad driver causes a boot loop.

### Fix 4: Clean the driver store of stale packages

1. Open an elevated Command Prompt and run `pnputil /enum-drivers` to list third-party driver packages.
2. Identify stale versions of the failing driver and remove them with `pnputil /delete-driver oemXX.inf /uninstall` (replace oemXX.inf with the actual name).
3. Never delete the currently working driver — only older or duplicate versions of the same device.
4. Retry the Windows Update driver install; a clean store removes the conflicts that caused the failure.

### Fix 5: Reset Windows Update components to clear the failed state

1. The standard component reset (stop services, rename SoftwareDistribution and Catroot2, restart services) clears the "failed" flag Windows Update remembers.
2. After the reset, check for updates again — the driver offer should reappear fresh instead of instantly failing.
3. If the [update troubleshooter itself misbehaves](/articles/best-way-to-fix-windows-update-troubleshooter-not-working/), do the manual reset described in that guide rather than relying on the tool.
4. Install any pending cumulative updates first; a healthy servicing stack makes driver installs far more reliable.

### Fix 6: Hide the bad driver update so it stops retrying

1. Download Microsoft's **Show or Hide Updates** troubleshooter package (wushowhide.diagcab) from the official Windows support pages.
2. Run it, choose **Hide updates**, and select the specific failing driver from the list.
3. Hidden updates never download or attempt installation again, ending the failure loop permanently.
4. Revisit the hide list after major Windows upgrades, since feature updates can unhide previously hidden drivers.

### Fix 7: Decide your long-term driver strategy

1. For graphics drivers on gaming or creator laptops, prefer the vendor: NVIDIA or AMD directly, and consider blocking GPU drivers from Windows Update via Group Policy.
2. For Wi-Fi, Bluetooth, and chipset drivers, Windows Update is usually fine once the vendor baseline is installed.
3. Uninstall any third-party "driver updater" utility — they cause more conflicts than they solve and fight Windows Update for control.
4. [Back up your working drivers](/articles/best-way-to-backup-drivers-before-update/) now, so the next failure is a ten-minute restore instead of a troubleshooting session.

## Closing

Failing driver updates are Windows Update telling you it does not have the right package for your hardware — so stop letting it guess. Identify the driver, install the vendor's version, hide the bad offer, and set a deliberate driver policy for the machine. Done once, properly, this ends the cycle of red "failed" entries and the blue screens that sometimes follow them.
