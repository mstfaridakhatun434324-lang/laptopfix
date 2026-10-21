---
title: "How to Roll Back the Qualcomm NPU Driver in Windows 11"
slug: qualcomm-npu-driver-rollback-windows-11
date: 2026-10-21
categories: ["ai-pc"]
tags: ["qualcomm npu driver", "npu driver rollback", "snapdragon x driver", "hexagon npu", "ai pc", "windows 11"]
description: "Roll back the Qualcomm NPU driver in Windows 11 safely with six step-by-step methods covering Device Manager rollback, manual restore, and update blocking."
thumbnail: "/images/thumbs/qualcomm-npu-driver-rollback-windows-11.webp"
faqs:
  - q: "When should I roll back the Qualcomm NPU driver?"
    a: "Roll back when NPU features broke right after a driver update — Studio Effects greyed out, Recall misbehaving, live captions failing, or a new Device Manager warning. If the timing matches an update, rollback is the fastest fix."
  - q: "Will rolling back delete my files or apps?"
    a: "No. A driver rollback only swaps the NPU driver package back to its previous version. Documents, apps, Windows settings, and NPU app preferences are untouched."
  - q: "What if the Roll Back Driver button is greyed out?"
    a: "Windows kept no previous driver copy — common after clean installs or when Windows Update replaced the driver without saving one. Fixes 3 and 4 cover manual rollback with your maker's older package."
  - q: "How do I stop Windows from updating the driver again?"
    a: "Use the device-ID installation restriction in Fix 6 (Windows 11 Pro) or the 'do not include drivers' update policy. Otherwise Windows Update will eventually reinstall the same problematic driver."
---

Snapdragon X laptops live and die by their Qualcomm Hexagon NPU — the engine behind Recall, Windows Studio Effects, live captions, and Click to Do. When a driver update lands and those features break overnight, the culprit is usually obvious: the new NPU driver. Rolling back to the previous version is the fastest way to restore a working machine, and it takes about two minutes when Windows kept a copy of the old driver.

The catch: Qualcomm NPU drivers on Snapdragon machines often arrive through Windows Update rather than a Qualcomm installer. Sometimes the one-click rollback is available; sometimes Windows replaced the driver without keeping the old one, and you need the manual route through your laptop maker's support page.

This guide covers six methods in order: the quick Device Manager rollback, verifying the restore, manual rollback when no previous driver was kept, the maker's full bundle, System Restore, and blocking the bad driver from returning.

## Why this happens

- **Incompatible driver from Windows Update:** The most common trigger — a driver that passed generic validation but breaks on your specific Snapdragon X model.
- **New driver conflicts with firmware:** The updated driver may expect a BIOS revision you do not have yet, breaking Studio Effects or Recall.
- **Partial update left mixed versions:** An interrupted update can leave some Qualcomm components new and others old, producing erratic NPU behavior.
- **OEM customizations overwritten:** Your maker's tuned driver gets replaced by a generic package lacking model-specific power and thermal tuning.
- **Registration glitch:** The new package sometimes registers incorrectly, so Windows loads it in a degraded state.
- **Broken feature dependencies:** Recall and live captions depend on specific NPU driver interfaces; a driver that changed them breaks the apps without any driver warning.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Roll back from Device Manager

When Windows kept the previous driver, this is a one-minute fix. If NPU features broke within a day of a driver or Windows update, rollback is very likely the cure.

1. In Device Manager, find the Qualcomm NPU/Hexagon entry under System devices or Neural processors.
2. Right-click it, open **Properties > Driver** tab, and note the current driver date.
3. Click **Roll Back Driver** (if greyed out, skip to Fix 3), pick a reason, confirm, and restart.
4. After rebooting, confirm the driver date is older. If [Recall snapshots are paused](/articles/recall-snapshots-paused-fix/) too, the driver and Recall service may need fixing as a pair.

### Fix 2: Verify the rollback restored NPU function

A clean Device Manager does not guarantee the apps recovered — app components sometimes cache the broken state. Verify with real workloads.

1. Confirm the NPU shows "This device is working properly" with the older driver date.
2. Check that Studio Effects options like background blur are selectable again in Settings.
3. Run live captions on a short video and confirm they generate. For streaming-specific failures, see the [live captions YouTube guide](/articles/live-captions-not-working-youtube/).
4. Open Task Manager's Performance tab and confirm NPU activity during these tests.

### Fix 3: Manual rollback with the maker's older driver

When the Roll Back button is greyed out, Windows kept no previous copy. The manual route achieves the same result: remove the bad driver, install the older package.

1. On your maker's support page ([Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en), [Dell](https://www.dell.com/support)), download the previous NPU/chipset driver for your exact Snapdragon X model.
2. In Device Manager, right-click the Qualcomm NPU, choose **Uninstall device**, and check **"Attempt to remove the driver for this device"**.
3. Restart to clear the bad package from the driver store.
4. Run the older installer as administrator, restart, and verify the NPU is healthy. Compare with the general [NPU driver rollback guide](/articles/npu-driver-rollback-windows-11/) for the platform-neutral version of these steps.

### Fix 4: Reinstall the full Qualcomm driver bundle

Sometimes the NPU driver alone is not the whole story — Qualcomm's platform drivers ship as a tuned set, and rolling back one piece leaves version mismatches. The maker's full bundle restores the tested combination.

1. Download the complete driver bundle for your exact model from the maker's support page.
2. Uninstall the current NPU driver with file deletion (Fix 3, step 2) and restart.
3. Install the bundle's components in the maker's listed order (chipset first, then NPU/AI).
4. Restart and verify every Qualcomm device in Device Manager is warning-free, then retest Studio Effects, captions, and Recall.

### Fix 5: Use System Restore to undo the update

If manual driver surgery feels risky, System Restore rolls drivers, registry, and system files back to before the update while leaving personal files alone.

1. Search **"Create a restore point"**, open System Protection, and click **System Restore**.
2. Choose a restore point dated before the NPU problems started.
3. Let it complete — the machine may reboot twice.
4. Verify the NPU driver date is the older one and test your AI features.

### Fix 6: Block the bad driver from reinstalling

A rollback that Windows Update promptly undoes is no fix. Once the good driver is in place, block the problematic one.

1. In the NPU's **Properties > Details > Hardware Ids**, copy the top hardware ID.
2. On Windows 11 Pro, open **gpedit.msc** > Computer Configuration > Administrative Templates > System > Device Installation > Device Installation Restrictions.
3. Enable **"Prevent installation of devices that match any of these device IDs"** and add the NPU hardware ID.
4. On Home edition, use **Settings > Windows Update > Advanced options** to exclude drivers if offered, or set the connection as metered to gate driver downloads.

## Closing

Rolling back the Qualcomm NPU driver is the right first move whenever AI features break right after an update: try the one-click rollback, verify with real NPU workloads, go manual with the maker's older package when Windows kept no copy, and block the bad driver from returning. Keep your exact model's full driver bundle handy — on Snapdragon machines the tuned set matters more than any single driver.
