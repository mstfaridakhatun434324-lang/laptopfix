---
title: "NPU Disappeared After Windows Update? Bring It Back"
slug: npu-disappeared-after-windows-update
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu disappeared", "windows update", "device manager", "windows 11", "driver"]
description: "NPU disappeared after a Windows update? Learn why updates remove the Neural processors section and how to restore your AI chip step by step."
thumbnail: "/images/thumbs/npu-disappeared-after-windows-update.webp"
faqs:
  - q: "Why would Windows Update remove my NPU?"
    a: "It does not remove the hardware — it replaces the driver with one that fails to initialize the chip, so Windows drops the device entry. The NPU is still physically there; only the software handshake broke."
  - q: "Which Windows updates are known to break NPUs?"
    a: "Patch Tuesday cumulative updates and 24H2 feature-update components have both done it, particularly with early Intel Core Ultra and Ryzen AI drivers. There is no single KB to blame — it varies by machine and driver version."
  - q: "Should I avoid Windows updates on my AI laptop?"
    a: "No — skipping security updates is worse. Instead, keep a known-good OEM driver installer saved locally so you can recover in minutes when an update misbehaves, and pause updates briefly while you fix things."
  - q: "How do I know the update caused it?"
    a: "Timing is the tell: NPU working yesterday, update installed overnight, NPU gone this morning. Check Settings, Windows Update, Update history for driver updates around the failure time."
---

Everything worked yesterday. This morning, after Windows Update ran overnight, the NPU is gone — no Neural processors section, AI features dead, as if the chip was never there. This is one of the most common NPU complaints in existence, and the pattern is so consistent it has a clear playbook. The update replaced your working driver with one your machine rejects.

The good news: because the trigger is known, the fix is mechanical. Work through these in order — and if Device Manager shows the NPU with a warning instead of missing entirely, our [error code 43 guide](/articles/npu-driver-error-code-43/) may fit better. If the chip is detected but [apps are not using the NPU](/articles/npu-not-used-by-apps-windows-11/), that is a separate configuration issue with its own fixes.

## Why this happens

- **Driver replacement with a mismatch:** Windows Update installs an NPU driver built for a different chip revision or firmware level.
- **Failed mid-install:** The update downloads or installs partially, leaving no working driver at all.
- **OEM customizations wiped:** The generic update overwrites OEM-tuned driver files the NPU firmware expects.
- **Driver store corruption:** The update process itself corrupts the driver package registration.
- **Feature update component drift:** 24H2-era updates changed OS-side AI plumbing that old NPU drivers cannot talk to.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the update is the culprit

Two minutes of verification saves misdiagnosis.

1. Settings, Windows Update, Update history — look for driver updates or feature updates around the failure.
2. Note the exact KB numbers and dates; you will need them to block recurrence.
3. If no update occurred near the failure, treat this as a general [detection problem](/articles/npu-not-detected-windows-11/) instead.
4. If an update matches the timeline, proceed — you have your prime suspect.

### Fix 2: Roll back the driver

The fastest undo.

1. Device Manager — if any NPU or Unknown device entry exists, open Properties, Driver tab, "Roll Back Driver."
2. Reboot and check for the Neural processors section.
3. If no entry exists at all to roll back, skip to Fix 3 — there is nothing to revert.
4. After a successful rollback, immediately pause updates (Settings, Windows Update, Pause for 1 week).

### Fix 3: Reinstall the OEM driver cleanly

When rollback is unavailable, rebuild from the known-good package.

1. Download your maker's NPU/chipset driver: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
2. Disconnect from the internet.
3. Device Manager: uninstall any NPU-related entries, removing driver software.
4. Run the OEM installer offline, reboot, reconnect, and verify.
5. Keep that installer file saved — you will want it handy next Patch Tuesday.

### Fix 4: Block the bad update permanently

Otherwise this becomes a monthly ritual.

1. Use Microsoft's "Show or hide updates" troubleshooter to hide the offending driver update.
2. Alternatively, use Group Policy (Pro editions): gpedit.msc, Computer Configuration, Administrative Templates, Windows Components, Windows Update, "Do not include drivers with Windows Updates" — Enabled.
3. For Home edition, the registry equivalent achieves the same driver exclusion.
4. Verify over the next update cycle that the NPU survives — check Device Manager after Patch Tuesday.
5. Revisit annually: eventually a fixed driver appears and you will want updates flowing again.

### Fix 5: Check for a newer fixed driver

The update that broke you may already be superseded.

1. Check your OEM's support page for an NPU driver newer than the bad one — makers often rush out fixes.
2. Check [Intel](https://www.intel.com/content/www/us/en/support/detect.html) or [AMD](https://www.amd.com/en/support/download/drivers.html) directly for newer packages.
3. Read release notes for mentions of your symptom — "fixes NPU detection" is the phrase you want.
4. Install the fixed version with updates paused, verify, then unpause.
5. If nothing newer exists, stay on your rolled-back version and check monthly.

### Fix 6: Use System Restore as a time machine

When driver surgery is not working, rewind the whole system.

1. Win + R, `rstrui`, Enter — pick a restore point from before the update.
2. Confirm the restore; the machine will reboot and take 15-30 minutes.
3. After restore, verify the NPU is back in Device Manager.
4. Immediately pause updates and apply Fix 4's blocking so the same update does not re-break things tonight.
5. Note: System Restore does not touch personal files, only system and driver state.

## Closing

An NPU that vanishes after Windows Update is a driver-replacement problem with a driver-replacement solution: roll back, clean-install the OEM package, and block the bad update so it cannot recur. Keep a known-good installer saved locally and this entire category of failure becomes a ten-minute recovery instead of a day of panic. Make the post-update Device Manager check a habit for the first boot after every Patch Tuesday, and you will catch the next incident before it costs you any real time. If the NPU entry is present but [greyed out in Task Manager](/articles/ai-boost-greyed-out-task-manager/) rather than missing, that adjacent symptom has its own quick checks.
