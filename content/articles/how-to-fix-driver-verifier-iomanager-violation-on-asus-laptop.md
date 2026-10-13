---
title: "Fix DRIVER_VERIFIER_IOMANAGER_VIOLATION on an ASUS Laptop"
slug: how-to-fix-driver-verifier-iomanager-violation-on-asus-laptop
date: 2026-10-05
categories: ["windows-errors"]
tags: ["driver verifier iomanager violation", "asus", "blue screen"]
description: "Fix DRIVER_VERIFIER_IOMANAGER_VIOLATION on your ASUS laptop: switch off Driver Verifier, update storage and USB drivers, and end the crashes."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-iomanager-violation-on-asus-laptop.webp"
faqs:
  - q: "What is DRIVER_VERIFIER_IOMANAGER_VIOLATION?"
    a: "Stop code 0x000000C9: Driver Verifier caught a driver mishandling I/O request packets — careless IRP handling, usually in storage, USB, or file-system filter drivers. Like all Verifier crashes, this one is intentional: Verifier subjects drivers to stress and crashes the machine on purpose when one violates the rules."
  - q: "How do I stop the crash loop?"
    a: "Enter Safe Mode and execute verifier /reset from an elevated Command Prompt. Verifier deactivates immediately and the loop stops dead. Afterward, update the storage and USB drivers to fix the real violation — deactivating Verifier ends the crashes, but the underlying driver defect survives until you update it."
  - q: "Which ASUS drivers usually cause this?"
    a: "Storage controller drivers, USB drivers, and ASUS's own utility drivers — the Armoury Crate services and ASUS System Control Interface — are the typical culprits. Stale chipset drivers installed by Windows Update are frequent offenders too, especially when a generic build displaces an ASUS-tuned one and introduces I/O flaws that Verifier detects."
  - q: "Do I need Driver Verifier running normally?"
    a: "No. It is a debugging tool for developers that intentionally blue-screens your PC when it finds driver bugs. Everyday users should leave it permanently off — run verifier /reset and forget it unless you are actively debugging a driver. Verifier belongs in a lab, not in daily use; leaving it enabled invites blue screens on any system with imperfect third-party drivers."
---

If your ASUS laptop keeps blue-screening with DRIVER_VERIFIER_IOMANAGER_VIOLATION (0x000000C9), the headline is simpler than the name suggests: Driver Verifier is still switched on. Verifier is a developer utility that stress-tests drivers and intentionally crashes Windows the moment a driver mishandles an I/O request packet — precisely what this stop code records. On ASUS hardware, the drivers that usually trip it are storage, USB, or ASUS utility drivers.

The repair therefore has two halves. First, execute `verifier /reset` to halt the intentional crashes and escape the loop. Second, bring the I/O drivers Verifier was complaining about up to date, so the violation itself is repaired rather than just silenced. The complete sequence is below.

## Why this happens

- **Verifier never got switched off:** the single enabler of the whole affair. Until it is reset, Verifier keeps stress-testing drivers at every boot and crashing at each violation it finds.
- **Old storage drivers:** AHCI/NVMe and Intel RST drivers with I/O handling flaws are the classic 0xC9 trigger on ASUS machines.
- **USB driver trouble:** broken USB 3.x host drivers — or one awkward USB device such as a dock or external drive — set off I/O verification.
- **ASUS utility drivers:** the Armoury Crate services and ASUS System Control Interface install drivers that participate in I/O and power paths.
- **File-system filter drivers:** dated antivirus or disk-utility filters fumble IRPs as soon as Verifier examines them closely.
- **A generic driver swapped in by Windows Update:** a plain storage or chipset driver replacing the ASUS-tuned edition introduces I/O bugs that Verifier catches at the next boot.
- **Verifier configured too aggressively:** checking every driver with every test (instead of a targeted subset) makes violations probable on any machine carrying imperfect third-party drivers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn Driver Verifier off from Safe Mode

1. Break out of a crash loop by forcing the recovery environment: hold the power button through the Windows logo on three consecutive boots.
2. Choose **Troubleshoot, then Advanced options, then Startup Settings, then Restart**, and press **4** for Safe Mode.
3. Launch **Terminal (Admin)** from the Start right-click menu, type `verifier /reset`, and press Enter.
4. Boot normally. The loop ends at once — Verifier is off and will not fabricate further blue screens.
5. Leave Verifier off until every driver below is current — and even then, switch it on only while actively debugging something specific.

### Fix 2: Find which I/O driver Verifier flagged

1. From an elevated Command Prompt, run `verifier /query` to list the drivers that were under verification when the crashes occurred.
2. Open **Event Viewer, then Windows Logs, then System** and locate the **BugCheck** entries matching your crash times — the details commonly name the offending `.sys` file.
3. Names seen often on ASUS machines: `stornvme.sys`, `storahci.sys`, `iaStorAC.sys` for storage, `USBXHCI.sys` for the USB host, plus ASUS utility drivers.
4. Write the exact filename down. Pinpointing the component focuses the driver work ahead and keeps you from updating blindly.

### Fix 3: Refresh the chipset and storage drivers

1. Open **MyASUS**, head to **System Update**, and install every offered driver update — **chipset** and **storage** take priority.
2. When MyASUS lacks them, pull chipset drivers for your exact model from the ASUS support site.
3. On Intel-based ASUS laptops, [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html) can provide current chipset and RST drivers if ASUS's builds are behind.
4. Reboot after installing. The storage and chipset drivers own the I/O paths Verifier was testing — current versions resolve most 0xC9 violations outright.
5. Stress-test afterward with disk-heavy work (big file copies, game installs), since that loads the I/O path hardest.

### Fix 4: Refresh USB drivers and quarantine suspect devices

1. Open **Device Manager** and expand **Universal Serial Bus controllers**.
2. Right-click every **USB Root Hub** and **USB 3.x eXtensible Host Controller** entry and update its driver.
3. Unplug USB docks, external drives, adapters, and hubs, then run the laptop bare for a while.
4. Plug devices back in one at a time, testing after each, to catch the one whose driver triggers the violation.
5. Get an updated driver for that device from its manufacturer — or retire the device if none exists. A single badly behaved USB device driver can keep 0xC9 recurring indefinitely.

### Fix 5: Update the ASUS utilities

1. Open the **Microsoft Store, then Library**, and bring **Armoury Crate** up to the latest release.
2. In **MyASUS, then System Update**, verify **ASUS System Control Interface** is current.
3. Reboot after updating. Outdated ASUS utility drivers are a documented 0xC9 source because they hook into power and device I/O paths.
4. If crashes started right after an ASUS utility updated, remove that utility temporarily as a diagnostic — reinstall once the system is steady.
5. Verifier crashes of the non-I/O variety are covered in our [Driver Verifier violation guide](/articles/fix-driver-verifier-detected-violation-after-windows-11-update/).

### Fix 6: Strip out stale filter drivers

1. Open **Settings, then Apps, then Installed apps** and uninstall third-party antivirus products, disk utilities, or old VPN clients you no longer need.
2. In **Device Manager**, switch on **View, then Show hidden devices**, and uninstall greyed-out remnants of removed software.
3. Launch **Terminal (Admin)** and run `sfc /scannow` to fix system file damage.
4. Reboot. File-system filter drivers intercept every file operation, so outdated ones fail I/O verification relentlessly — removing them eliminates a whole class of violations.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents Safe Mode and recovery-environment access if you struggle to reach these tools.

### Fix 7: Verify the drive is healthy

1. From **Terminal (Admin)**, run `chkdsk C: /f /r` — answer **Y** to schedule it, restart, and allow the full scan to finish.
2. Review your SSD's SMART health in the drive maker's toolbox software.
3. If the drive shows warnings, reallocated sectors, or a failing health percentage, back up important files immediately — dying storage hardware creates I/O errors no driver update can repair.
4. A healthy drive plus current drivers closes out the hardware side of the investigation.

### Fix 8: Prove stability and leave Verifier off

1. With Verifier off and drivers refreshed, run the laptop normally for several days — work in sleep/wake cycles, USB plug/unplug events, and large file operations.
2. For proof the violation is gone, you may briefly re-enable targeted I/O verification on the suspect driver alone, test a few hours, then immediately run `verifier /reset`.
3. Never keep Verifier enabled as a standing setting — it is a lab instrument for driver developers, not protection for daily use.
4. Let MyASUS System Update run periodically so storage, chipset, and USB drivers never drift far behind again — stale I/O drivers are what started this whole episode. The identical I/O verification failures on Acer hardware appear in our [Acer I/O violation guide](/articles/how-to-fix-driver-verifier-iomanager-violation-on-acer-laptop/).

## Closing

DRIVER_VERIFIER_IOMANAGER_VIOLATION on ASUS machines is Verifier performing exactly as designed — exposing I/O driver bugs, usually in storage, USB, or an ASUS utility driver — on a laptop where somebody forgot to disable it. Run `verifier /reset` to stop the intentional crashes, refresh those drivers through MyASUS (Intel direct when needed), and test USB devices individually. It presents as a deep system failure; underneath it is a driver-refresh checklist with a dramatic name, and it ends the instant Verifier is off and the drivers are fresh.
