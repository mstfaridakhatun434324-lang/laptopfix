---
title: "KB5048667 Won't Install? A Complete Step-by-Step Repair Walkthrough"
slug: "how-to-fix-kb5048667-fails-to-install-step-by-step"
date: "2026-09-07"
categories: ["windows-update"]
tags: ["windows update", "kb5048667", "step by step", "install failure"]
description: "A meticulous step-by-step walkthrough for fixing KB5048667 installation failures on any Windows 11 laptop, from diagnosis to manual installation."
thumbnail: "/images/thumbs/how-to-fix-kb5048667-fails-to-install-step-by-step.webp"
faqs:
  - q: "What is KB5048667 and why does it keep failing?"
    a: "KB5048667 is the December 2024 cumulative update for Windows 11 version 24H2, containing security patches and quality improvements. It commonly fails because of corrupted update cache files, damaged system components, conflicting drivers, insufficient disk space, or third-party antivirus interference. The step-by-step sequence in this guide isolates each cause in order so you can identify and fix the exact problem."
  - q: "Do I need to do every step in this guide?"
    a: "No, you should stop as soon as KB5048667 installs successfully. The steps are ordered from quickest and safest to most involved, so most users resolve the problem within the first four steps. Only continue to the manual Catalog installation and component store repair if the earlier fixes do not work. Each step includes a verification point so you know whether to proceed."
  - q: "Can I skip the manual download step if automatic updates work?"
    a: "Yes, the manual Microsoft Update Catalog installation is a fallback for when the automatic Windows Update path keeps failing. If clearing the cache or running the troubleshooter gets the update installing normally, there is no need to download anything manually. Keep the Catalog method in reserve for stubborn cases where the update service itself seems broken."
  - q: "What should I do if the update fails with a specific error code?"
    a: "Write down the exact error code shown in the update history, because it points to the root cause. Code 0x80070002 usually means a corrupted download cache, while 0x80070005 points to a permissions problem. Our guides on [error 0x80070002](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/) and [error 0x80070005](/articles/how-to-fix-windows-update-error-0x80070005-after-windows-11-update/) explain each code in detail."
---
When KB5048667 refuses to install, the worst thing you can do is hammer the retry button and hope for a different result. This update, the December 2024 cumulative release for Windows 11 version 24H2, fails for specific, diagnosable reasons, and a methodical approach finds the culprit far faster than random troubleshooting. This guide gives you that method: a technician's ordered checklist where each step either fixes the problem or rules out a cause.

The approach here is simple. First, you confirm what is actually failing and gather the error details. Then you work through repairs from the least invasive to the most thorough, verifying after each one. You never skip ahead to drastic measures like resetting Windows when a two-minute cache clear would have done the job. Follow the sequence exactly, and stop the moment the update installs.

Before you begin, make sure your laptop is plugged into AC power, connected to a stable non-metered network, and has at least 10 GB of free space on the C: drive. Updates that fail halfway through because the battery died or the Wi-Fi dropped create new problems on top of the old ones. With those basics confirmed, start at step one.

## Why this happens

- **Interrupted or partial downloads:** A dropped connection or a paused update leaves a broken package in the cache that fails integrity checks on every retry.
- **Stale update service state:** The Windows Update, BITS, and cryptographic services can get stuck in a bad state, especially after a failed install attempt.
- **Corrupted component store:** Damaged files in the servicing stack prevent the update engine from assembling the new system image.
- **Driver or firmware conflicts:** Outdated chipset, storage, or BIOS firmware can trip the update's hardware readiness validation.
- **Security software blocking:** Third-party antivirus and firewall products sometimes intercept the files the installer needs to modify.
- **Disk space pressure:** Cumulative updates stage large temporary files, and low free space causes silent aborts.
- **Pending operations backlog:** A long queue of pending renames or a stuck restart can block any new update from committing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the exact failure and error code

Diagnosis comes before repair. The error code tells you which fixes are most likely to work, so do not skip this step even though it involves no actual fixing.

1. Open Settings, go to Windows Update, and click Update history.
2. Find KB5048667 in the list and note the exact error code beside it.
3. Check the date and time of the last attempt to confirm it is recent.
4. Write the code down or take a photo with your phone for reference.
5. If no code appears, note whether the failure happens during download, install, or restart.

### Fix 2: Run the Windows Update troubleshooter

This automated tool detects stopped services, broken registrations, and policy misconfigurations, then applies safe repairs. It takes about five minutes and fixes a large share of update failures on its own.

1. Open Settings, then System, then Troubleshoot.
2. Select Other troubleshooters and locate Windows Update.
3. Click Run and wait for the scan to finish completely.
4. Accept every recommended fix the tool proposes.
5. Restart the laptop and check for updates again.

For background on this utility, Microsoft documents it at https://support.microsoft.com/en-us/windows.

### Fix 3: Reset the Windows Update cache cleanly

A corrupted SoftwareDistribution folder is the single most common cause of repeated KB5048667 failures. Stopping the related services, renaming the cache folders, and restarting gives Windows Update a completely fresh start.

1. Open Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the cache: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Also rename: `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Restart the services with the matching `net start` commands for each one.
6. Reboot the laptop, then run Check for updates and observe the fresh download.

### Fix 4: Free disk space and clear temporary files

If the update downloads fine but dies during installation, suspect disk space. Cumulative updates need room to stage and expand files, and Windows is not always graceful about telling you space is the problem.

1. Open Settings, go to System, then Storage, and check free space on C:.
2. Run Disk Cleanup as administrator and tick Temporary files, Delivery Optimization files, and Previous Windows installations if present.
3. Press Windows plus R, type `%temp%`, and delete everything the system allows.
4. Empty the Recycle Bin and confirm at least 10 GB is free.
5. Restart and retry the update.

### Fix 5: Update drivers and BIOS before retrying

An outdated storage controller, chipset driver, or BIOS can fail the update's readiness checks. Updating your hardware firmware first removes an entire class of failures and is good maintenance regardless.

1. Open Device Manager and check for warning icons on storage and system devices.
2. Visit your laptop maker's support site and download the latest BIOS, chipset, and storage drivers for your exact model.
3. Install the BIOS update first while on AC power, then the chipset and storage drivers.
4. Restart between the BIOS flash and the driver installs if the vendor recommends it.
5. Once everything is current, check for updates again.

### Fix 6: Install the update manually from the Microsoft Update Catalog

If the automatic pipeline is broken, bypass it. The standalone .msu package from Microsoft's official Catalog installs the identical update without involving the Windows Update service at all.

1. Visit https://www.catalog.update.microsoft.com and search for KB5048667.
2. Choose the x64 entry matching Windows 11 version 24H2.
3. Download the .msu file and double-click it to launch the installer.
4. Allow the installation to complete, which can take twenty minutes or more.
5. Restart when prompted and confirm the KB in update history.

Our companion article on [installing KB updates manually from the Catalog](/articles/how-to-install-kb-update-manually-from-catalog-in-windows-11-24h2/) covers architecture selection and verification in more detail.

### Fix 7: Repair the system image with DISM and SFC

When everything else fails, the servicing stack itself is likely damaged. DISM restores the component store to health, and SFC repairs protected system files afterward. Run them in this order for best results. This same repair sequence also resolves the broader pattern of [cumulative updates failing every time](/articles/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2/), since the underlying servicing damage is usually identical.

1. Open Command Prompt as administrator.
2. Execute `DISM /Online /Cleanup-Image /RestoreHealth` and wait for 100 percent.
3. If DISM reports it repaired the image, proceed; if it errors, retry with a stable connection.
4. Run `sfc /scannow` and wait for the verification phase to complete.
5. Restart the laptop and make one final update attempt.

## Closing

You now have a complete diagnostic-to-repair sequence for KB5048667: confirm the error, run the troubleshooter, reset the cache, free space, update firmware, install manually from the Catalog, and repair the component store as a last resort. Because the steps are ordered by effort and likelihood, you will rarely need the final two. Once the update installs, leave Windows Update on its normal schedule so future cumulative releases arrive without another round of troubleshooting.
