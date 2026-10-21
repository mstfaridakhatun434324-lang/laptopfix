---
title: "How to Manually Install the Intel NPU Driver Using the INF File"
slug: manually-install-intel-npu-driver-inf
date: 2026-10-21
categories: ["ai-pc"]
tags: ["intel npu driver", "inf install", "manual driver install", "ai boost", "device manager", "troubleshooting"]
description: "Intel NPU driver installer failing? Learn to manually install the Intel NPU driver from its INF file with this safe, step-by-step technician's method."
thumbnail: "/images/thumbs/manually-install-intel-npu-driver-inf.webp"
faqs:
  - q: "When should I install the driver from the INF instead of the setup.exe?"
    a: >
      When the vendor's installer fails, rolls back, or refuses your system — but the driver package itself is fine. The INF method bypasses the installer's version checks and bundled extras, installing just the driver. It's also the standard fix when an update fails halfway and leaves the NPU broken.
  - q: "Is manual INF installation safe?"
    a: >
      Yes, when the INF comes from Intel or your laptop maker. You're using Windows' own driver installation mechanism with a properly signed package — no different from what the setup program does, just without the installer's wrapper and extra software.
  - q: "Do I need to uninstall the old driver first?"
    a: >
      Usually yes. Installing over a corrupt driver can inherit the corruption. Uninstall the existing NPU driver with driver-file deletion first, reboot, then install from the INF onto the clean device entry.
  - q: "The INF install says the driver isn't intended for this platform. What now?"
    a: >
      Stop — that message means the package doesn't match your hardware (wrong NPU generation or wrong Windows build). Forcing it can cause code 10 or code 28 errors. Download the package for your exact processor and Windows 11 build instead.
---

Intel's NPU driver installer usually just works — until it doesn't. The setup program fails with a cryptic error, rolls back halfway, or insists your system isn't supported even though Device Manager clearly shows an Intel AI Boost NPU waiting for a driver. When the installer gives up, manual INF installation is the technician's way forward.

An INF file is simply the instruction sheet Windows uses to install a driver: which files to copy, which registry entries to create, which hardware IDs it supports. The setup.exe is just a wrapper around this process, plus version checks and bundled utilities. Going straight to the INF skips the wrapper — and its failure modes.

This guide walks through the full manual process in order: get the right package, extract the INF, clean out the old driver, install, and verify. Follow it exactly and the NPU comes up cleanly even when every installer failed.

## Why this happens

- **The installer fails its own pre-checks:** Setup programs verify OS build, existing driver versions, and bundled components. Any mismatch aborts the install even though the core driver would work fine — a common story when [an Intel NPU driver update fails](/articles/intel-npu-driver-update-failed/) midway.
- **Corrupt previous install blocks the updater:** The installer detects the broken driver state and won't proceed rather than repairing it. Manual INF installation sidesteps the detection logic entirely.
- **Bundled software conflicts:** Intel's package sometimes includes management utilities that clash with your OEM's versions. The INF method installs only the driver, avoiding the conflict.
- **Windows Update keeps interfering:** The installer and Windows Update race to own the device, and the install fails mid-write. Doing it manually in a controlled sequence avoids the race.
- **Wrong installer for your NPU generation:** Intel ships different packages for different Core Ultra generations. Grabbing the wrong setup.exe produces misleading "not supported" errors the INF's hardware-ID check would have caught cleanly.
- **Permissions or policy blocks:** Enterprise policies or overzealous security software can block setup.exe while still allowing Windows' own driver install path.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Download the correct Intel NPU driver package

Everything downstream depends on this step — a wrong package wastes the whole exercise, so verify before you download.

1. Identify your exact processor: **Settings > System > About** shows the chip (e.g., Core Ultra 7 155H), and Device Manager's NPU entry shows the hardware ID.
2. Get the driver from [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) or your laptop maker's support page — never from third-party driver sites.
3. If the download is a ZIP, extract it to a folder like `C:\Drivers\IntelNPU`. If it's an .exe that won't run properly, extract it with 7-Zip — many Intel installers are self-extracting archives.
4. Confirm the extracted folder contains .inf files with matching .sys and .cat files. No INF, no manual install — re-download.

### Fix 2: Uninstall the existing broken driver completely

Installing fresh files over a corrupt driver state is how corrupt driver states get new files. Clear the decks first.

1. In Device Manager, expand **Neural processors**, right-click the Intel NPU, and choose **Uninstall device**.
2. Check **"Attempt to remove the driver for this device"** and confirm.
3. Restart. The NPU should now appear as an unknown device or under "Other devices" — that clean slate is what you want.
4. If it still shows the old driver name, the uninstall didn't take; repeat in Safe Mode.

### Fix 3: Install the driver from the INF via Device Manager

This is the core technique: point Windows at the INF and let its own driver machinery do the install — no setup.exe involved.

1. In Device Manager, right-click the NPU (or unknown device) and choose **Update driver**.
2. Select **Browse my computer for drivers**, then **Let me pick from a list of available drivers on my computer**.
3. Click **Have Disk**, then **Browse**, navigate to your extracted folder, select the .inf file, and click Open.
4. Choose the matching Intel NPU / AI Boost model from the list, click Next, and approve the installation. Restart when prompted.

### Fix 4: Use pnputil for a command-line install

When Device Manager's wizard misbehaves — or you want a scriptable, verifiable install — pnputil does the same job from an elevated terminal with exact feedback.

1. Open **Terminal (Admin)** and navigate to your extracted driver folder.
2. Run `pnputil /add-driver *.inf /install` — Windows stages the package into the Driver Store and installs it onto matching hardware.
3. Read the output: it names the published oemNN.inf and reports success or a specific error.
4. Restart and check Device Manager. If pnputil reports the driver is already present, add `/force` — but only when the existing copy is certainly the corrupt one.

### Fix 5: Verify the installation actually took

A silent install isn't a successful install — confirm the driver is loaded, signed, and functional before declaring victory.

1. In Device Manager, open the NPU's **Properties > Driver**: the provider should read Intel, with a sensible date and version.
2. Check the **Details** tab's Digital Signer property — a proper Intel signature means Windows trusts the package.
3. Confirm no yellow warning remains. If you see code 28, the INF didn't match your hardware ID — wrong package; go back to Fix 1.
4. Test a real workload: enable background blur in your camera app or check that [Quick Settings shows your Studio Effects toggles](/articles/studio-effects-settings-missing-quick-settings/) — a working feature proves the driver, not just the entry.

### Fix 6: Stop Windows Update from undoing your manual install

Manual installs are especially vulnerable to being "upgraded" by Windows Update into a broken state again — the classic loop where [the snapshot viewer or other AI features](/articles/recall-snapshot-viewer-not-opening/) break a week after your fix.

1. Note your working driver version from **Properties > Driver**.
2. Copy the NPU's hardware ID from **Properties > Details > Hardware Ids**.
3. In **gpedit.msc**, go to Computer Configuration > Administrative Templates > System > Device Installation > Device Installation Restrictions, enable **"Prevent installation of devices that match any of these device IDs"**, and add the ID.
4. After the next Patch Tuesday, verify your manually installed version is still in place.

## Closing

Manual INF installation isn't a hack — it's the same driver install minus the installer program that kept failing. Get the right package from Intel or your laptop maker, clear the broken driver, install via Device Manager or pnputil, and verify with a real AI workload. Once the driver is installed and guarded from Windows Update, the NPU behaves exactly as if setup.exe had worked the first time.
