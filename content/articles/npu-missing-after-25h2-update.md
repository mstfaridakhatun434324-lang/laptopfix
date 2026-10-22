---
title: "NPU Missing After Windows 11 25H2 Update? Restore It Now"
slug: npu-missing-after-25h2-update
date: 2026-10-22
categories: ["ai-pc"]
tags: ["npu", "windows-11-25h2", "windows-update", "device-manager", "ai-pc", "troubleshooting"]
description: "NPU vanished after the Windows 11 25H2 update? Learn why feature updates hide the Neural processors section and how to bring your NPU back step by step."
thumbnail: "/images/thumbs/npu-missing-after-25h2-update.webp"
faqs:
  - q: "Why do Windows feature updates break the NPU?"
    a: >
      Feature updates reinstall large parts of the driver stack and
      sometimes substitute a generic driver that does not match your NPU
      revision. The Neural processors section then disappears from Device
      Manager. It is a software mismatch, not hardware damage, and it is
      fixable by reinstalling the correct driver.
  - q: "Will the NPU come back on its own after 25H2?"
    a: >
      Occasionally a follow-up cumulative update restores it, but you
      should not wait. Every day without the NPU means Copilot+ features
      like Recall, Live Captions translation, and Studio Effects stay
      disabled. The manual driver reinstall below takes about fifteen
      minutes.
  - q: "Can I roll back the 25H2 update to get my NPU back?"
    a: >
      Yes, within ten days of installing it, via Settings > System >
      Recovery > Go back. But rollback is a blunt tool — it undoes
      security fixes too. Try the driver fixes first; rollback is only
      worth it if no driver version works on 25H2.
  - q: "How do I stop Windows Update from breaking the NPU again?"
    a: >
      After fixing it, pause driver updates via Group Policy or the
      registry (Device Installation Settings > No), and install NPU
      drivers only from your laptop maker. That keeps Windows Update from
      silently swapping your working driver again.
---

You installed the Windows 11 25H2 feature update, everything looked fine — and then you noticed Copilot+ features were greyed out. A quick check of Device Manager confirms the worst: the entire "Neural processors" section is gone, as if your AI PC never had an NPU at all.

Feature updates are the classic NPU killer. Unlike monthly patches, they reinstall huge portions of the Windows driver stack, and the NPU — with its young, fast-moving drivers — is often the casualty. This exact pattern has played out with every recent feature update, which is why we already have a guide for the [NPU disappearing after a Windows update](/articles/npu-disappeared-after-windows-update/) in general; 25H2 brings its own specific quirks on top. Similar "update ate my feature" reports are hitting other AI components too, like [Click to Do losing its Open-with-app option](/articles/click-to-do-open-with-app-missing/) after updates.

The good news: your NPU hardware is almost certainly fine. The chip does not get damaged by a Windows update — it is just invisible to the OS because the driver binding broke. The fixes below rebuild that binding from the simplest driver refresh to a clean reinstall, and most people get the NPU back without touching their files.

## Why this happens

- **Generic driver substitution:** 25H2 can replace your OEM NPU driver with a newer-but-incompatible inbox driver, which fails to start and hides the device.
- **Driver signature enforcement changes:** Feature updates sometimes tighten driver signing rules, blocking older NPU drivers that worked on the previous build.
- **Corrupted driver migration:** The update's driver migration step can leave half of the old driver and half of the new one, producing a device that will not enumerate.
- **BIOS/firmware mismatch:** Newer Windows builds occasionally require a minimum firmware version for NPU enumeration, and older BIOS releases stop exposing it.
- **Disabled by the update's hardware scan:** The 25H2 hardware re-detection can mark the NPU as a failed device and hide it behind "show hidden devices."
- **OEM utility conflicts:** Laptop-maker AI utilities written for the older Windows build can fight the new driver for control of the NPU at boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check for a hidden or failed NPU device

The NPU may still be present but flagged as failed, which hides it from the normal Device Manager view.

1. Open Device Manager (Win + X > Device Manager).
2. Click View > Show hidden devices.
3. Look under Neural processors and also under "Other devices" for anything with a yellow warning triangle or labelled Unknown device.
4. If you find the NPU greyed out, right-click it and choose Uninstall device, ticking "Attempt to remove the driver" if offered.
5. Restart Windows and check whether the Neural processors section reappears with a fresh driver attempt.

### Fix 2: Install the OEM NPU driver for 25H2

Your laptop maker's driver package is matched to your exact machine and is the most reliable fix after a feature update.

1. Go to your maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and enter your exact model or serial number.
2. Look for a Neural Processing Unit, NPU, Intel AI Boost, AMD NPU, or Qualcomm Hexagon driver marked compatible with Windows 11 25H2.
3. Download and install it, choosing a clean install option if the installer offers one.
4. Restart the laptop, then verify the Neural processors section is back in Device Manager.
5. Confirm Task Manager's Performance tab shows the NPU entry again.
6. If the maker has no 25H2-specific package yet, install their newest Windows 11 driver anyway — it usually works, and you can report the gap to their support.

### Fix 3: Force the correct driver through Device Manager

When the right driver files are on disk but Windows picked the wrong one, you can point it at the correct driver manually.

1. In Device Manager, right-click the NPU (or Unknown device) and choose Update driver > Browse my computer for drivers.
2. Click "Let me pick from a list of available drivers on my computer."
3. Untick "Show compatible hardware" only if you know exactly which driver matches your chip; otherwise leave it ticked.
4. Select the proper Intel AI Boost, AMD NPU, or Qualcomm Hexagon driver and install it.
5. Restart and verify. If Windows immediately "updates" it back to the broken one, move to Fix 5 to block driver updates. This manual rebinding also helps when [Studio Effects loses its per-app toggle](/articles/studio-effects-per-app-toggle-missing/) after an update, since that symptom shares the same driver-layer root cause.

### Fix 4: Update BIOS/UEFI firmware

If 25H2 raised the bar for NPU enumeration, an old BIOS can leave the chip invisible no matter what driver you install.

1. Check your current BIOS version with `msinfo32` (look at the BIOS Version/Date line).
2. On your laptop maker's support page, compare it with the latest release and read the changelog for NPU, AI, or 25H2 mentions.
3. Download the BIOS update and install it with the laptop plugged into AC power — never on battery.
4. Enter BIOS setup after the update and confirm any NPU / AI Boost / AI Accelerator option is Enabled.
5. Boot into Windows and recheck Device Manager; install the OEM NPU driver again if the section reappears but shows a warning.

### Fix 5: Block Windows Update from replacing the working driver

Fixing the NPU once is pointless if the next update swaps the driver again — this step protects the repair.

1. Press Win + R, type `sysdm.cpl`, go to the Hardware tab, and click Device Installation Settings.
2. Choose "No (your device might not work as expected)" to stop automatic driver downloads — you will now update drivers manually.
3. Alternatively, on Pro editions, open gpedit.msc and enable "Do not include drivers with Windows Updates" under Windows Update policies.
4. Reinstall your known-good OEM NPU driver one final time so the pinned version is the correct one.
5. Check Windows Update history afterward to confirm no driver updates are being offered for the NPU. Microsoft documents driver-update behavior on the [Microsoft support site](https://support.microsoft.com/en-us/windows) if you want the full background.

### Fix 6: Repair the Windows component store

If the driver stack itself was damaged during the 25H2 upgrade, repairing Windows' core files can unstick enumeration.

1. Install every pending update from Settings > Windows Update, including optional driver updates EXCEPT any NPU driver (keep your working one).
2. Open an administrator terminal and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
3. Restart, then uninstall and reinstall the OEM NPU driver once more on the repaired system.
4. If the NPU is still missing, use Settings > System > Recovery > "Fix problems using Windows Update" to reinstall Windows while keeping your files — this rebuilds the driver migration cleanly without a full wipe.

## Closing

A missing NPU after the 25H2 update is frustrating but very rarely permanent — it is a driver binding problem, and the OEM driver package plus a block on automatic driver replacement resolves it for most laptops. Once the Neural processors section is back, leave driver updates for the NPU in your own hands rather than Windows Update's. If the whole machine feels sluggish after the upgrade and not just the NPU, see our guide on [AI PCs running slow after Windows updates](/articles/ai-pc-slow-after-windows-update/) too. And if the ten-day rollback window is still open and nothing else works, rolling back remains a valid last resort while you wait for your maker to publish a 25H2-ready driver.
