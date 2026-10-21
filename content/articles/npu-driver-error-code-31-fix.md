---
title: "How to Fix NPU Driver Error Code 31 on Your AI PC"
slug: npu-driver-error-code-31-fix
date: 2026-10-21
categories: ["ai-pc"]
tags: ["npu error code 31", "npu driver fix", "device manager error", "npu troubleshooting", "ai pc", "windows 11"]
description: "Fix NPU driver error code 31 on your AI PC laptop with seven step-by-step methods covering rollback, clean driver reinstall, Windows repair, and BIOS."
thumbnail: "/images/thumbs/npu-driver-error-code-31-fix.webp"
faqs:
  - q: "What does NPU error code 31 mean in Device Manager?"
    a: "Code 31 means Windows cannot load the NPU driver at all. Unlike code 10, where the driver loads but fails to start, code 31 is a load failure — usually a corrupt, mismatched, or badly registered driver package rather than dead hardware."
  - q: "Will fixing error code 31 delete my files?"
    a: "No. Everything here touches only the NPU driver stack. Rolling back, reinstalling, and repairing drivers never touches your documents, apps, or Windows settings."
  - q: "Why did code 31 appear right after a Windows update?"
    a: "Windows Update sometimes replaces your working OEM NPU driver with an incompatible one, or interrupts the install mid-way. Rolling back to the previous driver is the fastest cure when the timing matches an update."
  - q: "How do I know the fix actually worked?"
    a: "The yellow warning disappears and the NPU shows 'This device is working properly.' Then test a real NPU feature — background blur or live captions — because a clean icon alone does not prove the chip is doing work."
---

Seeing "This device is not working properly because Windows cannot load the drivers required for this device (Code 31)" on your NPU is unsettling on an AI PC laptop. The neural processor runs Windows Studio Effects, live captions, and Copilot+ features — when its driver cannot load, those features vanish from Settings or silently fall back to the CPU, draining your battery faster.

Code 31 is a driver-loading failure: Windows found the NPU hardware but failed to load its driver into memory. That differs from code 10, where the driver loads and then crashes at startup. In practice, code 31 traces back to a corrupt, half-installed, mismatched, or improperly registered driver package — not broken hardware.

This guide gives you seven fixes in technician order: quick state resets first, then rollback, a true clean reinstall, Windows-level repair, and firmware checks. Recheck Device Manager after each fix.

## Why this happens

- **Interrupted driver update:** A forced shutdown or conflicting Windows Update mid-install leaves driver files and registry registration out of sync, so Windows cannot load the package.
- **Wrong driver package:** An Intel AI Boost driver on AMD Ryzen AI hardware (or vice versa) is a driver Windows refuses to bind to the real chip.
- **Windows Update replacement:** Windows Update occasionally pushes a newer-but-incompatible NPU driver over a working OEM one, and code 31 appears overnight.
- **Corrupt driver registration:** Even with intact files, a damaged INF registration means Windows cannot assemble the driver at load time.
- **Leftover fragments:** Uninstalling without deleting driver software leaves stale files, so the new install mixes old and new components that fail together.
- **Damaged system files:** If Windows' own driver-loading components are corrupt, every reinstall of a good NPU driver fails the same way until the system is repaired.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Cold boot and rescan for hardware changes

Sometimes code 31 is a one-time registration hiccup from a single bad boot, and Windows cached the failure. A true cold boot plus a hardware rescan forces Windows to retry the driver load from scratch.

1. Hold **Shift** and click **Shut down** for a full shutdown instead of hybrid sleep.
2. Unplug the charger and USB devices, hold the power button 15 seconds, wait 30 seconds, then power on.
3. In Device Manager, right-click your computer name and choose **Scan for hardware changes**.
4. If the warning cleared, the failure was transient — you are done.

### Fix 2: Roll back to the previous NPU driver

When code 31 appeared right after a driver or Windows update, the previous driver worked and the new one is the problem. Rollback restores it in under a minute.

1. In Device Manager, right-click the NPU, open **Properties**, and go to the **Driver** tab.
2. Click **Roll Back Driver** (if greyed out, Windows kept no previous version — skip to Fix 3).
3. Choose a reason, confirm, and restart when prompted.
4. Verify the warning is gone and test an NPU feature. If [Click to Do stopped working on screenshots](/articles/click-to-do-not-working-on-screenshots/) at the same time, the same bad update likely caused both.

### Fix 3: Uninstall the NPU driver and delete its files

A plain uninstall leaves the driver package in the driver store, so Windows reinstalls the same broken copy and code 31 returns. Deleting the driver software breaks that loop.

1. Right-click the NPU, choose **Uninstall device**, and check **"Attempt to remove the driver for this device"**.
2. Restart immediately — part of the cleanup finishes during boot.
3. Reopen Device Manager and run **Scan for hardware changes** so Windows installs a baseline driver.
4. If the NPU works now, install the proper OEM driver in Fix 4; if code 31 persists, continue to Fix 5.

### Fix 4: Install the correct OEM driver for your exact model

Mismatched packages are a leading cause of code 31. Your laptop maker's support page lists the driver validated against your exact model, BIOS, and power firmware.

1. Find your exact model in **Settings > System > About**, then search it on [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
2. Download the latest chipset/NPU package for Windows 11 for that exact model.
3. Run the installer as administrator without interruption, then restart.
4. Confirm the NPU shows "This device is working properly." For a different error code, compare with the [code 10 NPU guide](/articles/npu-error-code-10-device-cannot-start/) — the two share root causes but need different fixes.

### Fix 5: Repair Windows system files and the driver store

If every reinstall fails with code 31, the fault may sit in Windows itself — corrupt system files or a damaged driver store break the load of even a perfect driver. SFC and DISM repair this without reinstalling Windows.

1. Open **Terminal (Admin)** and run `sfc /scannow`; restart if it repaired files.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to fix the component store.
3. Reinstall the OEM NPU driver from Fix 4 once more and restart.
4. If code 31 still appears, check whether [Windows Copilot runtime components are missing](/articles/windows-copilot-runtime-components-missing/) — broken AI runtimes and broken NPU drivers often arrive together after a bad update.

### Fix 6: Update the BIOS/UEFI firmware

The BIOS describes the NPU to Windows at boot, and outdated firmware can hand Windows a device description the driver cannot bind to — surfacing as code 31. Check this when the error followed a Windows feature update.

1. Press **Win + R**, type `msinfo32`, and note your BIOS Version/Date.
2. On your manufacturer's support page, download a newer BIOS for your exact model.
3. Close all programs, keep the charger plugged in, and run the updater — a black screen for several minutes is normal; never interrupt it.
4. After Windows loads, verify the NPU and test an AI feature.

### Fix 7: Block Windows Update from reinstalling the bad driver

If the NPU heals but code 31 returns after Patch Tuesday, Windows Update is pushing the incompatible driver over your working one again. Block it so the fix sticks.

1. In the NPU's **Properties > Details > Hardware Ids**, copy the top ID.
2. Open **gpedit.msc** (Windows 11 Pro) and go to Computer Configuration > Administrative Templates > System > Device Installation > Device Installation Restrictions.
3. Enable **"Prevent installation of devices that match any of these device IDs"** and add the NPU hardware ID.
4. Restart and confirm the NPU stays healthy past the next update cycle.

## Closing

Code 31 means Windows cannot load the NPU driver — and the fix is almost always a rollback, a true clean reinstall with driver files deleted, or the correct OEM package for your exact model. Repair system files when reinstalls keep failing identically, keep the BIOS reasonably current, and block Windows Update from overwriting a driver that works.
