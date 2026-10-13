---
title: "How to Fix a BSOD That Hits at Startup on Windows 11"
slug: how-to-fix-bsod-on-startup-windows-11-reddit
date: 2026-09-21
categories: ["windows-errors"]
tags: ["blue screen", "startup", "windows 11"]
description: "Blue screen every time Windows 11 starts? Use Safe Mode, driver removal, and startup repair to break the crash-at-boot cycle."
thumbnail: "/images/thumbs/how-to-fix-bsod-on-startup-windows-11-reddit.webp"
faqs:
  - q: "Why does the blue screen only happen during startup?"
    a: "Startup loads every driver and service at once, so a single bad driver, corrupt boot file, or failing drive sector in the boot path crashes the system before the desktop appears. Once running, that same component may never be stressed the same way — which is why the crash is startup-specific."
  - q: "How do I get into Safe Mode if Windows keeps crashing?"
    a: "Interrupt the boot three times (hold power during the Windows logo) to force the Automatic Repair screen, then Troubleshoot > Advanced options > Startup Settings > Restart, and press 4 for Safe Mode. Safe Mode skips most third-party drivers, so it usually boots when normal mode cannot."
  - q: "Will Safe Mode let me fix the problem permanently?"
    a: "Yes — Safe Mode is a working Windows environment where you can uninstall bad drivers, roll back updates, run SFC and DISM, and use System Restore. Most startup-BSOD causes are fully fixable from Safe Mode without reinstalling anything."
  - q: "What if even Safe Mode blue-screens?"
    a: "Then the problem is in the core boot path: corrupt boot configuration, damaged system files, or failing hardware (drive or RAM). Use the recovery environment's Startup Repair, Command Prompt boot rebuilds, and hardware diagnostics — Safe Mode failing is itself a useful diagnostic clue."
---
A blue screen that strikes **during startup** — before you ever see the desktop — is uniquely frustrating because your normal troubleshooting tools are on the other side of the crash. But Windows gives you a back door: the recovery environment and Safe Mode, both reachable without a working desktop.

The strategy is simple: get into an environment that boots, find what is crashing the normal boot, remove or repair it, and boot normally again.

## Why this happens

- **Bad driver loading at boot:** A newly installed or updated driver that crashes during initialization — the most common cause.
- **Corrupt Boot Configuration Data:** Damaged boot instructions from disk errors or failed updates.
- **Damaged system files in the boot path:** Corruption in the kernel or boot-start drivers.
- **Failing drive sectors:** Bad sectors exactly where boot files live, failing consistently at the same point.
- **Bad Windows update:** An update that installed halfway or included an incompatible driver.
- **Fast Startup corruption:** A damaged hibernation file breaking every hybrid boot.
- **Hardware faults:** Failing RAM or an overheating component that fails under the startup load burst.

## How to fix it

Work through these in order.

### Fix 1: Force the recovery environment

Three interrupted boots trigger Automatic Repair.

1. Power on the laptop, and as soon as the Windows logo or spinner appears, hold the power button until it shuts off.
2. Repeat twice more. On the next power-on, Windows enters **Automatic Repair** instead of the normal boot.
3. If you see **Preparing Automatic Repair**, you are in. From here: **Advanced options** gives you Startup Repair, Safe Mode (via Startup Settings), Command Prompt, System Restore, and more.

### Fix 2: Boot into Safe Mode

Safe Mode loads a minimal driver set — if the crash is driver-caused, Safe Mode boots fine.

1. From the recovery screen: **Troubleshoot > Advanced options > Startup Settings > Restart**.
2. Press **4** for Safe Mode (or **5** for Safe Mode with Networking if you need internet for driver downloads).
3. If Safe Mode boots, the core system is intact and a third-party driver or startup item is the crasher. If Safe Mode also blue-screens, skip to Fix 5 — the problem is deeper.

### Fix 3: Remove the crashing driver or update

In Safe Mode, undo whatever changed before the crashes began.

1. Open **Device Manager** (**Win + X**) and check for warning icons. Right-click any suspect device (especially anything updated recently) and choose **Uninstall device**, ticking **Attempt to remove the driver for this device**.
2. Go to **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent update if crashes started after it.
3. Reboot normally. If the desktop appears, install the correct driver from your manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) rather than letting Windows Update pick one.

### Fix 4: Disable Fast Startup and clean-boot

Fast Startup corruption and startup-program conflicts both cause boot-time crashes.

1. In Safe Mode, open **Control Panel > Power Options > Choose what the power buttons do > Change settings that are currently unavailable**, and uncheck **Turn on fast startup**.
2. Press **Win + R**, type `msconfig`, go to the **Services** tab, tick **Hide all Microsoft services**, and click **Disable all**.
3. In **Task Manager > Startup apps**, disable non-Microsoft entries. Reboot normally; if it boots, re-enable items in halves to find the culprit.

### Fix 5: Run Startup Repair and rebuild the boot files

For crashes that defeat Safe Mode, repair the boot chain itself.

1. From recovery: **Troubleshoot > Advanced options > Startup Repair**. Let it attempt the automatic fix.
2. If it fails, open **Command Prompt** from the same menu and run:
   - `bootrec /fixmbr`
   - `bootrec /fixboot`
   - `bootrec /rebuildbcd`
   - If needed: `bcdboot C:\Windows` (verify the drive letter with `diskpart` > `list volume` first)
3. Choose **Continue** and test the boot. Startup-repair-specific failures are covered in our [SrtTrail.txt guide](/articles/what-to-do-if-srttrail-txt-blue-screen-error/).

### Fix 6: Repair system files and scan the disk offline

Corrupt boot-path files and disk errors need the offline tools.

1. In the recovery Command Prompt, run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter to match your Windows partition).
2. Run `chkdsk C: /f /r` and let the full scan complete — startup crashes at the same point every boot often mean bad sectors in the boot path.
3. Reboot and test. If chkdsk finds many bad sectors, the drive is failing — back up from recovery before doing anything else.

### Fix 7: Use System Restore, then test hardware

Two remaining avenues before a reset.

1. From recovery: **Troubleshoot > Advanced options > System Restore**, and pick a point before the crashes began. This is non-destructive to personal files.
2. If restore points do not exist or do not help, test hardware: run `mdsched.exe` from Safe Mode or recovery for RAM, and your manufacturer's boot-time diagnostics (**F12**/**Esc** at power-on) for the drive.
3. Crashes at the same boot moment with clean software and failing diagnostics mean hardware — replace the faulty part rather than fighting the software.

### Fix 8: Reset Windows keeping files

The final software option when the boot chain resists repair.

1. From recovery: **Troubleshoot > Reset this PC > Keep my files**, with **Cloud download** if network is available in the recovery environment. Plug in the charger and let the reset complete without interruption.
2. Afterward, install manufacturer drivers first, then Windows updates, then applications gradually. Our full reset walkthrough is [how to reset Windows 11 without losing files](/articles/how-to-reset-windows-11-without-losing-files/).
3. If the reset fails, suspect the drive — check SMART health and consider replacement plus a clean install from Microsoft installation media.

## Closing

A startup BSOD is a locked door with the key under the mat: three interrupted boots open the recovery environment, Safe Mode bypasses the crashing driver, and the boot-rebuild commands fix the boot chain. Work from Safe Mode outward, and the crash-at-boot cycle breaks without costing you your files.
