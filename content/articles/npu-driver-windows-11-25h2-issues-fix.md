---
title: "How to Fix NPU Driver Issues After the Windows 11 25H2 Update"
slug: npu-driver-windows-11-25h2-issues-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["npu driver", "windows 11 25h2", "copilot+ pc", "snapdragon", "ai features", "troubleshooting"]
description: "Fix NPU driver problems after the Windows 11 25H2 update with repairs for missing AI features, driver errors, and Copilot+ features that stopped working."
thumbnail: "/images/thumbs/npu-driver-windows-11-25h2-issues-fix.webp"
faqs:
  - q: "Why did my NPU stop working after the Windows 11 25H2 update?"
    a: "The 25H2 update can replace your laptop maker's validated NPU driver with a generic one, leave the old driver half-installed, or disable the AI component in Device Manager. Reinstalling the OEM driver package for your exact model is usually the fix."
  - q: "How do I know if my NPU driver is broken?"
    a: "Open Device Manager and look under System devices or Neural processors for a yellow warning icon, an unknown device, or a missing NPU entry. Task Manager showing no NPU graph, and Copilot+ features like Recall or Cocreator greyed out, are also strong signs."
  - q: "Should I use Windows Update or the maker's driver for the NPU?"
    a: "Use your laptop maker's driver package first. It is validated for your exact NPU and firmware. Windows Update drivers are a fallback, and on Copilot+ PCs they sometimes install a generic version that lacks the full AI feature set."
  - q: "Will reinstalling the NPU driver delete my files?"
    a: "No. Reinstalling a driver only replaces system software; it does not touch your documents, photos, or installed apps. Still, save open work before restarting, as the repair steps require reboots."
---

You installed the Windows 11 25H2 update, and suddenly the AI features that sold you the laptop are gone. Recall is greyed out, Cocreator refuses to open, Windows Studio Effects no longer appear in your camera settings, and Task Manager shows no NPU activity at all. The hardware did not fail overnight — the update changed the software that talks to it.

On Copilot+ PCs, the Neural Processing Unit (NPU) depends on a tightly matched set of drivers, firmware, and Windows AI components. A feature update like 25H2 can replace the maker's validated NPU driver with a generic one, leave two driver versions fighting each other, or disable the device during migration. The result looks like broken hardware, but it is almost always a driver problem.

This guide walks you through the repair in technician order: confirm the failure first, then repair the driver, then restore the Windows AI components that depend on it. Work through the fixes in sequence and test your AI features after each step.

## Why this happens

- **Generic driver replaced the OEM NPU driver:** Windows Update can swap your laptop maker's validated NPU driver for a generic version that Windows recognises but that does not expose the full AI feature set to Copilot+ apps.
- **Half-completed driver migration:** If the update restarted, lost power, or was interrupted, the old NPU driver may be partially removed and the new one partially installed, leaving the device in an error state.
- **NPU disabled during the update:** Feature updates sometimes disable devices they cannot migrate cleanly. The NPU may simply be switched off in Device Manager, invisible to every AI app.
- **Firmware and driver version mismatch:** The NPU driver expects a matching BIOS or firmware version. If 25H2 updated one side of that pairing but not the other, the driver loads and then fails.
- **Windows AI components not re-registered:** Even with a healthy driver, the Windows AI platform components that apps call can be left unregistered after a feature update, so apps report that no NPU is available.
- **Conflicting chipset or graphics driver:** The NPU shares power and driver infrastructure with the chipset and GPU on many Copilot+ designs, so a stale chipset driver installed alongside 25H2 can destabilise the NPU too.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU failure in Device Manager and Task Manager

Do not reinstall anything blind — first establish exactly what Windows sees. A missing device, a warning icon, and a silent Task Manager each point to a different repair, and two minutes of diagnosis saves you from reinstalling the wrong package.

1. Press **Windows + X** and open **Device Manager**, then expand **System devices** and **Neural processors** if present.
2. Look for an entry such as "Qualcomm Hexagon NPU" or "Intel AI Boost" — note whether it is missing entirely, or shown with a yellow warning triangle.
3. Right-click the entry, choose **Properties**, and read the **Device status** box; note any error code such as Code 31 or Code 43.
4. Open **Task Manager > Performance** and check whether an **NPU** graph appears; its absence confirms Windows cannot see the hardware.
5. Open **Settings > System > About** and note your exact laptop model, which you will need to download the correct OEM driver in the next fix.

### Fix 2: Reinstall the OEM NPU driver package

The single most effective repair is a clean reinstall of the driver package from your laptop maker, not from a generic driver site. The OEM package contains the NPU driver matched to your firmware, plus any chipset components it depends on. The same OEM-first rule applies when [NPU temperature monitoring stops showing](/articles/npu-temperature-monitoring-fix/), because a generic driver often hides sensor data too.

1. Visit your maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and search for your exact model from Fix 1.
2. Download the latest **NPU, chipset, or AI driver package** for Windows 11 25H2, not an older Windows 11 24H2 build.
3. In Device Manager, right-click the NPU entry and choose **Uninstall device**, ticking **"Attempt to remove the driver for this device"** if offered.
4. Run the downloaded OEM installer as administrator and let it finish completely without putting the laptop to sleep.
5. Restart when prompted, then recheck Device Manager and Task Manager — the warning should be gone and the NPU graph should return.

### Fix 3: Update Windows and repair the AI platform components

If the OEM driver is healthy but Copilot+ features still report no NPU, the Windows side of the stack needs repair. The 25H2 update can leave AI components unregistered, and a cumulative update plus a component reset usually restores them. This step also helps when an app-level problem is masquerading as a driver fault, much like the app-specific behaviour covered in [Steam client slowdowns on ARM laptops](/articles/steam-client-arm-laptop-slow-fix/).

1. Open **Settings > Windows Update** and install every pending update, then restart — do not skip optional driver updates listed there on the first pass.
2. Open **Settings > System > Optional features** and confirm the AI-related features for your Copilot+ PC are installed, not pending.
3. Open Terminal as administrator and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, waiting for each to complete.
4. Restart the laptop and open an AI feature such as Windows Studio Effects or Cocreator to test whether the NPU is now recognised.
5. If the feature still fails, run **Settings > System > Troubleshoot > Other troubleshooters** and use the Windows Update troubleshooter before moving on.

### Fix 4: Update BIOS and firmware to match the 25H2 driver

A driver that keeps failing after a clean reinstall usually points at firmware. NPU drivers are validated against specific BIOS versions, and 25H2-era drivers may refuse to load properly on older firmware. This is a careful step, but on a plugged-in laptop it is routine maintenance.

1. On your maker's support page for your model, check the latest **BIOS / firmware** version and compare it with yours in **Settings > System > About** or the BIOS setup screen.
2. Download the BIOS update only from the maker's official support page — never from a third-party driver site.
3. Plug in the charger, close all apps, and save your work; never update BIOS on battery power.
4. Run the BIOS updater and do not touch the keyboard, power button, or lid until the laptop restarts itself completely.
5. After booting into Windows, recheck Device Manager and test a Copilot+ feature; firmware-matched drivers usually load cleanly on the first boot.

### Fix 5: Check power settings and BIOS options for the NPU

Some laptops gate the NPU behind a power or BIOS setting, and a feature update can reset those settings to defaults that keep the NPU powered down. This is easy to miss because Device Manager may show the device as working while it never actually activates under load.

1. Open **Settings > System > Power & battery** and set **Power mode** to **Balanced** or **Best performance** for testing.
2. Open **Settings > System > Power & battery > Battery saver** and make sure it is off while you test.
3. Restart into BIOS setup (usually **F2**, **F12**, or **Del** at boot) and look for an **NPU**, **AI accelerator**, or **Neural processor** toggle under Advanced or Configuration.
4. If the NPU is disabled there, enable it, save, and exit — Windows will enumerate the device on the next boot.
5. If you also use AI camera effects, test them now; a related camera-side failure is covered in [AI background blur not working](/articles/photos-background-blur-ai-not-working/) if blur specifically still fails.

## Closing

An NPU that stops working after 25H2 is frustrating precisely because the hardware is fine — the update simply broke the driver handshake. Confirm the failure, reinstall the OEM driver, repair the Windows AI components, and match your firmware, and in most cases the Copilot+ features return without any hardware work at all.
