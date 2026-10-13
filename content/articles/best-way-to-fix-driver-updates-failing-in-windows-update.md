---
title: "The Best Way to Fix Driver Updates Failing in Windows Update"
slug: best-way-to-fix-driver-updates-failing-in-windows-update
date: 2026-10-05
categories: ["windows-update"]
tags: ["driver updates", "windows update", "failed drivers", "oem drivers", "device manager"]
description: "Driver updates keep failing inside Windows Update? Learn the most reliable fix order — and when to bypass Windows Update and install drivers directly."
thumbnail: "/images/thumbs/best-way-to-fix-driver-updates-failing-in-windows-update.webp"
faqs:
  - q: "Why do driver updates fail when regular Windows updates succeed?"
    a: "Driver updates go through a different path: they must match your exact hardware ID, pass driver signature verification, and migrate cleanly from the old driver. Any mismatch — a wrong hardware revision, a corrupted driver store, or an OEM customization Windows does not understand — fails the driver update while cumulative updates sail through."
  - q: "Should I let Windows Update install drivers at all?"
    a: "For basic hardware, yes — it is convenient and the drivers are tested. For critical components like graphics, Wi-Fi, and chipset on a laptop, the manufacturer's driver is usually newer and better tuned. Many technicians let Windows handle the small stuff and manually manage GPU, network, and chipset drivers."
  - q: "Can a failed driver update damage my hardware?"
    a: "No. A failed driver update leaves the old driver in place — Windows rolls back the driver installation automatically. The risk is not damage but stagnation: you stay on an old, possibly buggy driver. The fix is to install the correct driver manually rather than retrying the failing one endlessly."
  - q: "How do I stop Windows Update from retrying a bad driver?"
    a: "Use the 'Show or hide updates' troubleshooter from Microsoft to hide the specific driver update, or set a group policy to exclude drivers from Windows Update entirely. Then install the correct driver from your laptop manufacturer's support site and the bad update stops reappearing."
---

Driver updates failing inside Windows Update is a special kind of frustration: the big security updates install fine, but that one Intel graphics or Realtek audio driver fails every single time, sometimes with a cryptic error code and sometimes with no explanation at all. The good news is that there is a well-established best order for fixing this, and it works because it addresses the actual reasons driver updates fail rather than just hammering "retry."

The key insight is that Windows Update is a mediocre driver delivery service. It does not know about your laptop manufacturer's customizations, it sometimes offers drivers for the wrong hardware revision, and its driver store can get corrupted independently of the rest of the update system. The best fix is usually not to make Windows Update succeed — it is to get the right driver installed by a better route, then stop Windows from fighting you over it.

## Why this happens

- **Wrong driver for the hardware revision:** Windows Update matches on hardware ID, but similar IDs across revisions can cause it to offer a driver your specific chip revision rejects.
- **OEM customizations conflict:** Laptop makers customize reference drivers (power limits, fan curves). A generic driver from Windows Update can fail against OEM-modified firmware.
- **Corrupted driver store:** The DriverStore folder can hold damaged driver packages, and every install attempt that touches them fails the same way.
- **Driver signature enforcement:** If the offered driver has signature or catalog problems on your system, Windows blocks the install as a security measure.
- **Pending old driver locks:** The currently installed driver may be in use or locked by its own utility software, preventing replacement.
- **Insufficient permissions or policy:** Enterprise policies, or registry tweaks from "debloating" tools, can block driver installation while allowing other updates.
- **Stale device metadata:** Ghost or hidden devices in Device Manager confuse the driver matching process and cause installs to target the wrong device instance.
- **Antivirus interference:** Security software that monitors driver loading can block the new driver's installation mid-process.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly which driver is failing

Do not guess. Knowing the exact device and error code determines whether you fix Windows Update or bypass it.

1. Go to **Settings > Windows Update > Update history** and find the failed driver entry — note the device name and any error code.
2. Open **Device Manager**, find the device, right-click **Properties**, and check the **Events** tab for the failure details.
3. Note the current driver version on the **Driver** tab — you will compare this against the manufacturer's latest.

### Fix 2: Install the driver from your laptop manufacturer's site

This is the best fix in most cases and the one technicians reach for first. The OEM driver is built for your exact model.

1. Go to your manufacturer's support page — Dell, HP, or Lenovo — and enter your model or serial number.
2. Download the driver for the failing device (graphics, Wi-Fi, audio, or chipset).
3. Run the installer. Most OEM installers handle the old driver's removal automatically.
4. Restart, then verify in Device Manager that the new version is active. Windows Update usually stops offering its version once a newer driver is installed.

### Fix 3: Clean-install the driver via Device Manager

If the OEM installer fails or you prefer the component vendor's driver (Intel, NVIDIA, AMD), do a clean manual install.

1. In **Device Manager**, right-click the device and choose **Uninstall device**, ticking **Attempt to remove the driver for this device**.
2. Restart the laptop.
3. Install the fresh driver: from the vendor — [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html) — or via **Device Manager > Action > Add legacy hardware** for manual INF installs.
4. Restart again and confirm the device works.

### Fix 4: Clear the driver store of corrupted packages

A corrupted DriverStore poisons every install attempt. Cleaning it forces Windows to use only fresh packages.

1. Open **Terminal (Admin)**.
2. Run `pnputil /enum-drivers` to list third-party driver packages and note any related to the failing device.
3. Remove the bad ones with `pnputil /delete-driver oemXX.inf /uninstall` (replace oemXX.inf with the actual published name).
4. Retry the driver installation from the manufacturer package.

### Fix 5: Hide the bad update so it stops retrying

If Windows Update keeps pushing a driver version that cannot work on your hardware, hide it and manage that driver manually.

1. Download Microsoft's **Show or hide updates** troubleshooter (wushowhide.diagcab).
2. Run it, choose **Hide updates**, and select the failing driver update.
3. The update disappears from Windows Update permanently (until you unhide it).
4. Install and maintain that driver from the manufacturer going forward.

### Fix 6: Exclude drivers from Windows Update via policy

For laptops where Windows Update drivers repeatedly cause trouble, the cleanest long-term setup is to let Windows Update handle OS patches while you handle all drivers manually.

1. Press **Win + R**, type `gpedit.msc` (Windows 11/10 Pro), and go to **Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update**.
2. Enable **Do not include drivers with Windows Updates**.
3. On Home editions, set the same via Registry: create DWORD `ExcludeWUDriversInQualityUpdate` = 1 under `HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`.
4. Maintain a quarterly habit of checking your manufacturer's support page for driver updates — the same discipline that prevents [cumulative update failures](/articles/how-to-fix-monthly-cumulative-update-failed-step-by-step/) applies to drivers.

### Fix 7: Reset the Windows Update components

If driver updates fail alongside everything else, the whole update pipeline may need the standard reset: stop services, rename SoftwareDistribution and Catroot2, restart services, and retry. This is the same cache reset used for [missing-file errors](/articles/how-to-fix-windows-update-error-0x80070002-on-windows-11/), and it clears driver-package corruption as a side effect.

## Closing

The best way to fix failing driver updates is usually to stop relying on Windows Update for drivers at all: identify the failing device, install the manufacturer's driver directly, and hide or exclude the problematic update so it stops nagging you. Reserve the pipeline resets for cases where everything update-related is broken. Once you take control of drivers manually — checking quarterly, installing from the OEM — the monthly cycle of failed driver updates simply ends.
