---
title: "Windows Update Installing the Wrong NPU Driver: How to Fix It"
slug: windows-update-driver-ranking-npu
date: 2026-10-23
categories: ["ai-pc"]
tags: ["windows update", "npu driver", "driver ranking", "driver issue", "ai pc", "troubleshooting"]
description: "Stop Windows Update from installing the wrong NPU driver: block bad driver updates, rank the OEM driver first, and restore NPU function step by step."
thumbnail: "/images/thumbs/windows-update-driver-ranking-npu.webp"
faqs:
  - q: "Why does Windows Update keep replacing my working NPU driver?"
    a: "Windows Update ranks drivers by date, version, and signature — not by whether they actually work on your hardware. A newer-dated generic NPU driver can outrank your laptop maker's validated driver, so Windows 'upgrades' you into a broken state."
  - q: "How do I stop Windows Update from updating a specific driver?"
    a: "Microsoft's official method uses the 'Show or hide updates' troubleshooter or a Group Policy / registry setting to block driver updates for a device. Rolling back the driver alone isn't enough — you must block the bad update or it returns."
  - q: "Will blocking driver updates break security updates?"
    a: "No. Blocking driver updates only affects driver packages — Windows quality and security updates continue normally. You can still update drivers manually from your laptop maker's support page."
  - q: "How do I know which NPU driver is correct for my laptop?"
    a: "The correct driver comes from your laptop maker's support page for your exact model, matched to your NPU (Intel AI Boost, AMD Ryzen AI/XDNA, or Qualcomm Hexagon). Check Device Manager's driver date and provider after installing to confirm it stuck."
---

Your NPU was working — Studio Effects ran, Recall indexed, local AI apps saw the accelerator — and then a routine Windows Update quietly replaced the driver with a version that broke everything. The NPU vanishes from Task Manager, AI features error out, and reinstalling the right driver only helps until the next update cycle.

This is Windows Update's driver ranking doing exactly what it was designed to do, just with the wrong outcome. It picks the "best" driver by its own scoring rules, and those rules do not know that your laptop maker's older driver is the one that actually works.

This guide fixes it permanently: restore the correct driver, then block the bad one so the cycle ends. Six fixes in order.

## Why this happens

- **Ranking favors newer dates over working drivers:** Windows Update scores drivers by version/date and signature. A generic NPU driver with a newer date outranks the OEM's validated-but-older driver, so Windows installs the generic one.
- **Generic drivers lack OEM customizations:** NPU drivers from Intel, AMD, and Qualcomm are customized per laptop for power management, firmware pairing, and feature enablement. The generic package lacks these and misbehaves.
- **Rollback doesn't block reinstallation:** Rolling back the driver in Device Manager restores the old driver temporarily — but Windows Update re-offers the "better-ranked" driver at the next scan, usually within days.
- **Feature updates reset driver blocks:** Major Windows updates (like 25H2) can clear previously set driver blocks and reinstall the whole driver set, resurrecting the problem — the same update-breakage pattern as [Recall breaking after 25H2](/articles/recall-broken-after-25h2-update/).
- **Multiple NPU driver sources conflict:** Intel DSA, AMD Adrenalin, Windows Update, and the OEM installer can each push NPU drivers. Competing sources install over each other unpredictably.
- **Firmware/driver version pairing:** NPU firmware and drivers are version-paired. A driver newer than the firmware expects — or vice versa — produces "device cannot start" errors that look like hardware failure.
- **Driver store corruption:** A corrupted driver store can cause Windows to mis-rank or mis-install drivers repeatedly, making the problem recur even with blocks in place.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the wrong driver and roll back

First confirm the diagnosis: check what driver is actually loaded and whether it changed recently.

1. Open **Device Manager**, find the NPU (under **System devices** or **Neural processors** — names vary: "Intel AI Boost", "AMD IPU Device", or "Qualcomm Hexagon NPU").
2. Right-click, open **Properties > Driver**, and note the **Driver Provider**, **Driver Date**, and **Driver Version**. A Microsoft provider or a very recent date right after an update is the smoking gun.
3. If **Roll Back Driver** is available, click it and choose a reason — this restores the previous driver immediately for testing.
4. Check **Task Manager > Performance** — the NPU entry should reappear once the correct driver loads. Test an NPU feature (Studio Effects, or an app that uses the NPU) to confirm function.
5. Important: the rollback is temporary. Windows Update will re-offer the bad driver — continue to Fix 2 to block it permanently.

### Fix 2: Block the bad driver update with Microsoft's tool

Rolling back without blocking is mowing the lawn without pulling weeds. Microsoft provides an official way to hide a specific driver update.

1. Download Microsoft's **"Show or hide updates" troubleshooter** (wushowhide) — Microsoft documents this approach on [Windows support](https://support.microsoft.com/en-us/windows).
2. Run it, choose **Hide updates**, and select the NPU driver update from the list. This blocks that specific driver version from installing.
3. Verify the block: run **Windows Update > Check for updates** and confirm the NPU driver no longer appears as an available update.
4. Note the limitation: hiding blocks that specific version. If Microsoft publishes a newer bad version later, you may need to hide it again — check after each Patch Tuesday if the problem historically recurs.
5. For a more durable block, continue to Fix 3 (Group Policy/registry), which blocks driver updates by device rather than by version.

### Fix 3: Exclude drivers from Windows Update entirely

The strongest protection: tell Windows Update to never include drivers. You then update drivers manually from trusted sources only.

1. Open **Group Policy Editor** (`gpedit.msc`) — on Pro/Enterprise editions — and go to **Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update**.
2. Enable **"Do not include drivers with Windows Updates"**, then run `gpupdate /force` in an admin Terminal.
3. On Home edition (no gpedit), set the registry instead: in admin Terminal run `reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v ExcludeWUDriversInQualityUpdate /t REG_DWORD /d 1 /f`.
4. Restart, then check Windows Update — driver updates should no longer be offered at all.
5. Take ownership of driver updates going forward: check your maker's support page monthly, and use Intel DSA / AMD Adrenalin / Qualcomm's channels for NPU drivers specifically. Manual updating is slightly more work but ends the surprise-breakage cycle.

### Fix 4: Clean-install the correct OEM NPU driver

With updates blocked, install the known-good driver cleanly so no remnants of the bad one linger in the driver store.

1. Download the NPU/chipset driver package for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — or the NPU driver from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) / [AMD](https://www.amd.com/en/support/download/drivers.html) for your platform.
2. In Device Manager, right-click the NPU, choose **Uninstall device**, and check **"Attempt to remove the driver for this device"** — repeat until Device Manager shows no NPU driver (it may appear as an unknown device).
3. Restart, then run the OEM/chipset installer as administrator and restart again when prompted.
4. Verify in **Device Manager > Properties > Driver** that the provider and version match the OEM package, and confirm the NPU appears in Task Manager.
5. Run Windows Update once more to confirm the NPU driver is not re-offered — if it is, your block from Fix 2/3 did not apply; revisit those steps.

### Fix 5: Clean the driver store of the bad driver package

If the wrong driver keeps returning despite blocks, its package may be staged in the driver store where Windows keeps "helpfully" reinstalling it.

1. Open admin Terminal and run `pnputil /enum-drivers` to list all third-party driver packages in the store.
2. Identify the bad NPU driver package by provider and date (compare against the version you blocked).
3. Remove it with `pnputil /delete-driver oemXX.inf /uninstall /force`, replacing oemXX.inf with the actual published name — the /force flag is needed if the driver is currently staged.
4. Run `pnputil /enum-drivers` again to confirm it is gone.
5. Restart and verify the correct driver is still loaded and the NPU works. Cleaning the store is the step that finally ends "it came back again" loops.

### Fix 6: Handle feature-update resets and verify long-term

Major Windows updates can undo your blocks and reinstall drivers wholesale. Plan for it rather than being surprised by it.

1. After every feature update (25H2 and beyond), check **Device Manager > NPU > Driver** to confirm your OEM driver survived — do this before assuming AI features are broken for new reasons.
2. Re-apply the wushowhide block (Fix 2) if the bad driver version reappears in Windows Update after the feature update.
3. Verify the Group Policy/registry exclusion (Fix 3) is still in place — feature updates occasionally reset policies.
4. Keep a note (a text file on the desktop works) of your known-good NPU driver version and the block steps, so the next occurrence is a 10-minute fix instead of a research project.
5. If NPU problems persist even with the correct driver pinned, the issue is no longer ranking — investigate the app layer, like [provisioning failures](/articles/autopilot-arm-laptop-provisioning-failed/) on managed devices or [app-specific GPU issues](/articles/after-effects-arm-laptop-not-working/), rather than the driver.

## Closing

Windows Update installs the wrong NPU driver because its ranking rewards newness over correctness — and rollback alone never sticks. Restore the OEM driver, block the bad update with wushowhide or the driver-exclusion policy, clean the driver store, and re-verify after every feature update. Do it once, properly, and the cycle ends.
