---
title: "How to Fix NPU Error Code 28: Drivers Not Installed on Your AI PC"
slug: npu-error-code-28-drivers-not-installed
date: 2026-10-20
categories: ["ai-pc"]
tags: ["npu error code 28", "drivers not installed", "npu driver missing", "troubleshooting", "ai pc", "device manager"]
description: "Fix NPU error code 28 'drivers not installed' on your AI PC laptop — install the right NPU driver manually, fix Windows Update blocks, and restore AI features."
thumbnail: "/images/thumbs/npu-error-code-28-drivers-not-installed.webp"
faqs:
  - q: "What does NPU error code 28 mean?"
    a: "Code 28 means Windows recognizes the NPU hardware but has no driver installed for it. The hardware is fine — the driver is simply missing or was never installed. Installing the correct OEM driver almost always resolves it."
  - q: "Why did my NPU driver disappear after a Windows update?"
    a: "Windows Update sometimes removes or replaces the NPU driver during a feature update, especially if the new build deems the old driver incompatible. The fix is to reinstall the driver from your laptop maker's support page rather than waiting for Windows Update to sort itself out."
  - q: "Can I use the generic driver Windows finds automatically?"
    a: "Sometimes, but the generic driver may lack features like AI Boost or Studio Effects acceleration. The OEM driver from Dell, HP, or Lenovo is validated for your exact model and is the safer long-term choice."
  - q: "How do I know the NPU driver installed correctly?"
    a: "Device Manager should show the NPU under Neural processors or System devices with no warning icon, and Task Manager's Performance tab should list the NPU. Test an AI feature like background blur as a final check."
---

Code 28 is one of the more straightforward NPU errors: Device Manager sees the neural processor but reports "The drivers for this device are not installed." Windows simply has nothing to load, so your AI features sit idle and apps fall back to the CPU.

This state is common after a fresh Windows install, after a feature update stripped the old driver, or after you uninstalled a corrupt driver package — which is progress, since the broken files are gone. The path forward: get the right driver onto the machine and ensure nothing blocks it.

This guide covers six methods, from the quick automatic attempts to a fully manual driver installation. Work through them in order and check Device Manager after each one.

## Why this happens

- **Driver removed by a Windows feature update:** Major Windows builds sometimes discard drivers they consider incompatible, leaving the NPU driverless on first boot into the new build.
- **Fresh Windows install without OEM drivers:** Clean installs from Microsoft media include generic drivers only. NPU drivers for Intel AI Boost, AMD Ryzen AI, or Snapdragon X need the OEM package.
- **Corrupt driver uninstalled (on purpose):** If you purged a broken NPU driver to fix another error, code 28 is the expected intermediate state — the old package is gone and nothing has replaced it yet.
- **Windows Update driver search blocked:** Metered connections, paused updates, or group policies can prevent Windows from fetching the driver automatically.
- **Wrong driver architecture:** Installing an x64 NPU package on an ARM-based Snapdragon X laptop (or vice versa) fails silently, leaving code 28 in place.
- **Disabled device installation:** Device installation restrictions or a disabled Windows Update medic service can block even a correct manual install from completing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let Windows Update find the driver automatically

Before doing anything manual, give Windows one chance to fetch the driver itself. This works when the only problem is a missing package and your update pipeline is healthy.

1. Open **Settings > Windows Update** and click **Check for updates**, then install everything offered, including optional updates.
2. Expand **Advanced options > Optional updates > Driver updates** and look for anything mentioning NPU, neural processor, AI Boost, or your chip vendor, then install what you find and restart.
3. Check Device Manager — if the NPU now appears without warnings, confirm in Task Manager's Performance tab that the NPU is listed.
4. If nothing NPU-related was offered, move to Fix 2 — your update catalog simply does not carry the driver.

### Fix 2: Scan for hardware changes and update the driver manually

If Windows Update found nothing, force Device Manager to re-detect the device and point it at Windows' own driver store. This catches cases where driver files exist on disk but were never bound to the device.

1. In Device Manager, click **Action > Scan for hardware changes** and wait for the scan to finish.
2. Right-click the NPU entry, choose **Update driver**, then **Search automatically for drivers**.
3. If Windows reports the best driver is already installed yet code 28 remains, choose **Browse my computer for drivers > Let me pick from a list** and try any compatible NPU entry shown.
4. Restart and recheck. If the NPU still shows code 28, the driver genuinely is not on the machine — move to Fix 3.

### Fix 3: Install the OEM NPU driver package

The reliable fix for code 28 is the driver package from your laptop maker, validated for your exact model. Double-check the architecture — x64 for Intel/AMD laptops, ARM64 for Snapdragon X machines.

1. Find your exact model in **Settings > System > About**, then open your maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. Download the latest chipset/NPU/AI Boost driver for Windows 11, confirming the architecture matches your machine.
3. Right-click the installer, choose **Run as administrator**, and let it complete without interruption.
4. Restart when prompted, then verify in Device Manager that code 28 is gone and the NPU entry is clean.

### Fix 4: Install the driver from the extracted INF directly

Some OEM packages fail at the installer stage but contain perfectly good driver files. Pointing Device Manager at the extracted INF bypasses the installer entirely — a favorite technician trick for stubborn code 28.

1. Run the OEM installer once; if it errors out, note the temporary extraction folder (often under `C:\Drivers` or `%TEMP%`), or extract the installer with 7-Zip into `C:\NPU_Driver`.
2. In Device Manager, right-click the NPU, choose **Update driver > Browse my computer for drivers**, and point it at that folder with **Include subfolders** checked.
3. Let Windows install from the INF and restart. If the device shows as an [unknown device](/articles/npu-unknown-device-in-device-manager/) instead, the INF did not match — recheck the architecture.
4. Confirm the NPU initializes cleanly and appears in Task Manager.

### Fix 5: Unblock Windows Update and device installation

If manual installs keep failing or Windows cannot fetch anything, something may be blocking the pipeline — a metered connection flag, paused updates, or a device-installation restriction left over from troubleshooting.

1. Open **Settings > Windows Update** and make sure updates are not paused; resume them if they are.
2. Go to **Settings > Network & internet > Wi-Fi** (or Ethernet), open your connection properties, and turn **Metered connection** off.
3. Open **gpedit.msc** (Windows 11 Pro) and check Computer Configuration > Administrative Templates > System > Device Installation > Device Installation Restrictions for any enabled block policies; disable ones you added during earlier troubleshooting.
4. Retry Fix 1 or Fix 3. If a language-dependent AI feature also broke recently, check the [live captions language pack download fix](/articles/live-captions-language-pack-download-failed/) — the same blocked pipeline is often behind both.

### Fix 6: Reset the driver store with a clean reinstall

When every install attempt fails identically, the local driver store itself may be damaged. Removing all NPU-related OEM packages with `pnputil` and starting over clears state Device Manager cannot reach.

1. Open Terminal as administrator and run `pnputil /enum-drivers` to list third-party driver packages.
2. Identify entries mentioning NPU, neural, AI Boost, or your chip vendor, and remove each with `pnputil /delete-driver oemXX.inf /uninstall`.
3. Restart the laptop, then run the Fix 3 OEM installer fresh.
4. Verify in Device Manager and Task Manager. If the NPU is still not detected at all, work through the [NPU not detected in Windows 11 guide](/articles/npu-not-detected-windows-11/) — the issue may be enumeration rather than drivers.

## Closing

Code 28 is refreshingly honest as errors go: the driver is simply missing, and installing the right one fixes it. Get the OEM package for your exact model and architecture, keep Windows Update unblocked, and verify with a real AI workload — not just a clean Device Manager.
