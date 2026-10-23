---
title: "NPU Not Listed in MSINFO32 on Windows 11: How to Fix It"
slug: msinfo32-npu-not-listed
date: 2026-10-23
categories: ["ai-pc"]
tags: ["msinfo32", "npu missing", "system information", "npu detection", "windows 11", "troubleshooting"]
description: "Fix NPU not listed in MSINFO32 on Windows 11: verify BIOS detection, repair the NPU driver, and restore system information reporting step by step."
thumbnail: "/images/thumbs/msinfo32-npu-not-listed.webp"
faqs:
  - q: "Why doesn't my NPU show up in System Information?"
    a: "MSINFO32 lists the NPU under Components > Problem Devices only when there's an issue, or not at all on some systems — it's not a reliable NPU detector. Check Device Manager and Task Manager > Performance instead; if the NPU is missing there too, the driver or BIOS is the problem."
  - q: "Where should the NPU appear in MSINFO32?"
    a: "A healthy NPU usually doesn't appear as a separate MSINFO32 entry at all — it shows in Device Manager (System devices / Neural processors) and Task Manager > Performance. Its absence from MSINFO32 alone is not a fault."
  - q: "Does a missing NPU in MSINFO32 mean it's broken?"
    a: "Not necessarily. Confirm with Device Manager: if the NPU device is present and healthy there, everything is fine. If Device Manager also lacks it (or shows an error), then you have a real detection problem to fix."
  - q: "Can BIOS settings hide the NPU from Windows?"
    a: "Yes. Some BIOS setups have an NPU/AI accelerator toggle, and virtualization-based security settings can also affect NPU enumeration. If the NPU is missing everywhere in Windows, check the BIOS first."
---

You opened MSINFO32 (System Information) expecting to see your laptop's NPU listed, and it is nowhere to be found. Before troubleshooting, one important calibration: MSINFO32 is a poor NPU detector. A healthy NPU often has no dedicated MSINFO32 entry at all — its presence is properly confirmed in Device Manager and Task Manager.

So this guide has two jobs: first, the quick checks that confirm whether you actually have a problem, and second, the real fixes for when the NPU is genuinely missing from Windows — not just from one informational tool. Work through all six sections; the first two may save you the rest.

## Why this happens

- **MSINFO32 doesn't enumerate NPUs consistently:** System Information was designed before NPUs existed. It lists problem devices reliably but has no dedicated NPU section — absence here proves nothing by itself.
- **NPU driver not installed or failed:** If the NPU driver never loaded, Windows has no NPU device to report anywhere — Device Manager, Task Manager, and MSINFO32 all come up empty together.
- **BIOS disabled the NPU:** Some firmware includes an AI accelerator/NPU toggle. Disabled at the BIOS level, the NPU is invisible to the entire OS.
- **VBS/HVCI interfering with enumeration:** Virtualization-based Security and memory integrity change how drivers load. On some platforms they can block or hide the NPU driver — the same interference class behind [VBS/HVCI slowdowns](/articles/vbs-hvci-arm-laptop-slow/).
- **Windows Update replaced the working driver:** A generic driver update can leave the NPU in a failed state where it neither works nor reports cleanly.
- **Chipset driver missing:** The NPU depends on the platform chipset driver for enumeration. Without it, the NPU hardware is present but unreachable.
- **Actual hardware failure:** Rare, but an NPU that vanished after a drop, liquid exposure, or sudden failure across all tools with correct drivers and BIOS is a hardware problem.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify NPU presence with the right tools

MSINFO32 is the wrong witness. Check the tools that actually enumerate the NPU before concluding anything is broken.

1. Open **Device Manager** and look under **System devices** and any **Neural processors** category for the NPU (Intel AI Boost, AMD IPU Device, Qualcomm Hexagon NPU). Healthy with no warnings = no problem.
2. Open **Task Manager > Performance** and look for an **NPU** entry in the left column — its presence with utilization data is definitive proof the NPU works.
3. In MSINFO32 itself, check **Components > Problem Devices** — an NPU problem would appear here as a PNP device error. No entry here is good news.
4. If Device Manager and Task Manager both show a healthy NPU, stop here: your NPU is fine, and MSINFO32's silence is just how that tool works.
5. Only continue if the NPU is missing or erroring in Device Manager and Task Manager — that is a real detection failure.

### Fix 2: Check BIOS for NPU settings

If the NPU is invisible to all of Windows, the firmware may be hiding it. This check takes two minutes.

1. Restart into UEFI/BIOS setup (F2, Del, or your maker's key during boot).
2. Look through Advanced / Devices / Security tabs for anything labeled **NPU**, **AI Boost**, **AI accelerator**, or **Neural processor** — ensure it is **Enabled**.
3. While there, note the BIOS version and compare it against the latest on your maker's support page — outdated firmware can fail to enumerate newer NPU hardware.
4. Save and exit, boot into Windows, and recheck Device Manager for the NPU device.
5. If the BIOS has no NPU toggle and no update helps, the firmware is likely fine — continue to driver repairs.

### Fix 3: Reinstall the chipset and NPU drivers

A missing NPU in Device Manager with no BIOS cause is a driver problem. The chipset platform driver (which enumerates the NPU) comes before the NPU driver itself.

1. Download the **chipset/platform driver** package for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — or from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) / [AMD](https://www.amd.com/en/support/download/drivers.html) for your platform.
2. In Device Manager, if any NPU-related entry exists with a warning, uninstall it with **"Attempt to remove the driver for this device"** checked.
3. Install the chipset package as administrator, restart, then install any separate NPU driver package the OEM provides, and restart again.
4. Recheck Device Manager — the NPU should now appear healthy — and Task Manager > Performance for the NPU entry.
5. If Windows Update immediately replaces your driver, block it with the wushowhide troubleshooter or the driver-exclusion policy documented on [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 4: Test with VBS and memory integrity toggled

Virtualization-based Security can interfere with NPU driver loading on some platforms. Testing with it off isolates the variable — you can re-enable it afterward.

1. Open **Windows Security > Device security > Core isolation** and check **Memory integrity** status.
2. Temporarily turn **Memory integrity Off** and restart when prompted.
3. Check Device Manager and Task Manager for the NPU — if it appears now, VBS/HVCI was blocking enumeration.
4. With the NPU confirmed working, update the BIOS and chipset/NPU drivers to the latest versions (newer drivers often resolve the VBS conflict), then re-enable Memory integrity and retest.
5. If the NPU works with memory integrity off but not on even after updates, you have a genuine compatibility bug — report it to your laptop maker, and decide whether the NPU or the security feature matters more for your use. Do not leave memory integrity off permanently without understanding the tradeoff.

### Fix 5: Force hardware re-enumeration

Sometimes Windows' device database holds a stale "this device failed" record that blocks re-detection even with correct drivers. Forcing re-enumeration clears it.

1. In Device Manager, click **View > Show hidden devices** and look for greyed-out NPU entries — uninstall every ghost NPU device you find.
2. Click **Action > Scan for hardware changes** and watch whether the NPU reappears.
3. If not, shut down fully (**Shift + Shut down** for a cold boot), wait 30 seconds, and power on — cold boots force firmware-level re-enumeration that restarts skip.
4. After the cold boot, reinstall the chipset driver package once more if the NPU still does not appear.
5. Check **Event Viewer > Windows Logs > System** for Kernel-PnP events about the NPU around boot time — "device not migrated" or "failed to start" entries point back to driver/firmware pairing issues.

### Fix 6: Rule out hardware failure

An NPU missing everywhere — Device Manager, Task Manager, MSINFO32 problem devices — with correct BIOS settings and fresh OEM drivers is either a deep firmware issue or dead silicon.

1. Reset the BIOS to factory defaults (a corrupted firmware setting can hide devices), then recheck.
2. Update the BIOS to the latest version even if the version looked current — reflashing can repair corrupted firmware device tables.
3. Boot a Linux live USB with a recent kernel supporting your platform and check for the NPU there (`lspci` / `lsusb` depending on how the NPU attaches) — absence in a second OS confirms hardware.
4. Run your maker's full pre-boot hardware diagnostics, including any AI accelerator or system-board tests offered.
5. If the NPU is confirmed dead, contact your maker's support — the NPU is part of the SoC, so this is a board-level repair. And keep scope honest: unrelated cosmetic issues like [an app stuck in dark mode](/articles/copilot-app-dark-mode-stuck/) or [emulator problems](/articles/android-studio-arm-windows-emulator/) are not NPU symptoms, even when they appear at the same time.

## Closing

An NPU "missing" from MSINFO32 is usually not missing at all — that tool simply does not enumerate NPUs well. Confirm with Device Manager and Task Manager first; only when the NPU is absent everywhere do the real fixes apply: BIOS toggle, chipset/NPU driver reinstall, VBS testing, and forced re-enumeration. Work the evidence, not the assumption.
