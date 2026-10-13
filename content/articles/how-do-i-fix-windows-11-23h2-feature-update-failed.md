---
title: "How Do I Fix the Windows 11 23H2 Feature Update Failed Error?"
slug: how-do-i-fix-windows-11-23h2-feature-update-failed
date: 2026-10-06
categories: ["windows-update"]
tags: ["23h2 failed", "feature update error", "windows 11", "fix guide"]
description: "The Windows 11 23H2 feature update failed on your laptop? Follow this step-by-step fix sequence to get it installed successfully."
thumbnail: "/images/thumbs/how-do-i-fix-windows-11-23h2-feature-update-failed.webp"
faqs:
  - q: "What should I do first when the 23H2 feature update fails?"
    a: "Write down the exact error code from Settings, Windows Update, Update history before anything else. Then run the Windows Update troubleshooter, clear the update cache, and update your graphics and chipset drivers. This opening sequence resolves most 23H2 failures because they are usually caused by corrupted downloads or outdated drivers rather than anything exotic."
  - q: "Can I retry the 23H2 update immediately after it fails?"
    a: "You can, but retrying without changing anything usually produces the same failure. Take ten minutes first to clear the SoftwareDistribution cache, disconnect USB peripherals, and temporarily uninstall third-party antivirus. A retry after those steps has dramatically better odds than an immediate blind retry, which just wastes another download cycle."
  - q: "How much free space does the 23H2 feature update need?"
    a: "Plan for at least 20 GB of free space on the system drive, and more is better. The update stages gigabytes of files, keeps a rollback copy of your current installation, and needs working room during the install. If your drive is nearly full, use Disk Cleanup as administrator to remove temporary files and old Windows installations before retrying."
  - q: "Will the 23H2 update delete my files if it fails again?"
    a: "No. A failed feature update rolls back to your previous Windows version automatically, and your personal files, apps, and settings survive the rollback intact. The only thing you lose is time. That safety net is exactly why you should fix the underlying cause and retry rather than avoiding the update out of fear."
---

The 23H2 feature update downloads, installs partway, fails, and rolls back. Then Windows offers it again, and the cycle repeats. Each attempt costs an hour or more and ends in the same disappointment. It is tempting to just ignore the update, but failed feature updates do not fix themselves, and the underlying problem usually blocks future updates too.

This is the direct fix-it guide: what to do, in what order, to get 23H2 installed on your laptop. No log forensics, no theory. Just the sequence that works, starting with the fastest wins and ending with the guaranteed paths.

## Why this happens

- **Corrupted download:** The feature update package downloaded with errors, and every retry reuses the damaged files.
- **Outdated drivers:** Graphics, storage, or chipset drivers incompatible with 23H2 abort the install mid-flight.
- **Antivirus interference:** Third-party security software blocks file operations the installer needs.
- **Insufficient disk space:** The staging and rollback copies need far more room than the download size suggests.
- **Peripheral conflicts:** USB devices and docks introduce driver failures during the offline install phase.
- **Broken servicing stack:** Corruption in the update infrastructure fails every large install while small patches still work.
- **BIOS too old:** Firmware that predates 23H2's expectations can halt the install during hardware initialization.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Record the error code, then run the troubleshooter

1. Open **Settings > Windows Update > Update history**, find the failed 23H2 entry, and write down the full error code.
2. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Update** troubleshooter.
3. Restart the laptop after the troubleshooter finishes, even if it claims it found nothing.
4. Try the update once more. If it fails with the same code, continue down this list instead of looping the troubleshooter, since repetition without changes never helps.

### Fix 2: Clear the update cache completely

1. Open an admin Command Prompt and stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
3. Restart all four services with the matching `net start` commands.
4. Check for updates and let 23H2 download fresh. A clean cache eliminates the corrupted-package failures that cause most repeat failures.

### Fix 3: Update graphics and chipset drivers

1. Identify your exact laptop model and download the latest graphics driver from the GPU maker and the chipset driver from your laptop maker's support page.
2. For Intel graphics, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the right version automatically. NVIDIA users should visit NVIDIA's driver download page.
3. Choose clean installation options where offered to remove old driver remnants.
4. Restart and retry the update. Driver incompatibility is the leading cause of 23H2 failures that survive a cache clear.

### Fix 4: Remove antivirus and disconnect peripherals

1. Uninstall third-party antivirus fully through **Settings > Apps**, then run the vendor's removal tool to clear leftover filter drivers.
2. Unplug all USB devices: external drives, printers, hubs, docks, and adapters. Keep only the power cable.
3. Turn off Bluetooth so no wireless device drivers load during the install.
4. Retry the feature update in this minimal state. You can reinstall your antivirus and reconnect everything after 23H2 is running.

### Fix 5: Free disk space aggressively

1. Confirm at least 20 GB free on the system drive under **Settings > System > Storage**. Aim for 30 GB for comfort, since the installer also keeps a full rollback copy of your current Windows.
2. Run Disk Cleanup as administrator. Check every safe category, especially temporary files, delivery optimization files, and previous Windows installations, which alone can free tens of gigabytes.
3. Move large personal files to external storage temporarily if the drive is still tight. Videos and game installers are the usual space hogs on laptops.
4. Retry the update with real breathing room. Space-related failures are embarrassing to repeat, so be generous here. An update that fails at 80 percent with a disk-full error wastes the entire download and install time.

### Fix 6: Repair the servicing stack

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Command Prompt while connected to the internet. This downloads healthy component store files to replace damaged ones.
2. Follow with `sfc /scannow` and restart when both complete. SFC repairs protected system files using the store that DISM just fixed, which is why the order matters.
3. If 23H2 still fails, download the standalone installer from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) using the KB number from update history. Choose the x64 package for standard laptops.
4. Manual installation bypasses the servicing problems that block the automatic path. If the failure shows a driver error code instead, the [0xC1900101 guide](/articles/best-way-to-fix-update-fails-with-error-0xc1900101/) targets that family.

### Fix 7: Use the Installation Assistant for a clean run

1. Download the Windows 11 Installation Assistant from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it with peripherals disconnected and antivirus removed, keeping the laptop on AC power.
3. The assistant uses a separate, more robust install pipeline than Windows Update and succeeds in most cases where the standard path keeps failing.
4. After installation, verify with `winver` and confirm updates flow normally. For the diagnostic approach to recurring failures, the [23H2 failure troubleshooting](/articles/troubleshoot-windows-11-23h2-feature-update-failed/) guide digs into root causes.

## Closing

Fixing a failed 23H2 update is about removing every obstacle before the retry: clear the cache, update the drivers, remove the antivirus, disconnect the peripherals, free the space. Each step raises the odds, and the Installation Assistant provides the clean final path. Worked in order, 23H2 installs instead of failing, and your laptop is back on the supported update track with future releases arriving normally. Do not skip the driver updates even when you are tempted to jump straight to the assistant.
