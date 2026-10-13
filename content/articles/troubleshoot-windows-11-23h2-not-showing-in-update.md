---
title: "Windows 11 23H2 Not Showing in Update? Troubleshoot It Here"
slug: troubleshoot-windows-11-23h2-not-showing-in-update
date: 2026-10-01
categories: ["windows-update"]
tags: ["windows 11 23h2", "update not showing", "feature update missing", "troubleshooting"]
description: "Windows 11 23H2 is released but not offered on your laptop? This troubleshooting guide finds why your machine is being skipped and fixes it."
thumbnail: "/images/thumbs/troubleshoot-windows-11-23h2-not-showing-in-update.webp"
faqs:
  - q: "Why is Windows 11 23H2 not showing up in Windows Update?"
    a: "Microsoft rolls out feature updates in waves and blocks machines with known compatibility issues, so not being offered 23H2 usually means a safeguard hold on your hardware or drivers. It can also mean a pending restart, corrupted update components, or a metered connection pausing the offer. The fixes below check each of these in order."
  - q: "How do I check if my laptop has a safeguard hold?"
    a: "Microsoft does not show safeguard holds directly in Settings, but you can infer one if your drivers are outdated or your hardware matches known blocked configurations. Updating all drivers from your laptop maker's support page is the practical way to clear most holds. The Installation Assistant bypasses some holds, but forcing past a genuine compatibility block risks a failed install."
  - q: "Can I install 23H2 manually if Windows Update will not offer it?"
    a: "Yes. The Windows 11 Installation Assistant and the Media Creation Tool both let you install 23H2 without waiting for the Windows Update offer. This is safe when your hardware meets the requirements and your drivers are current. Only avoid forcing it if you know your specific model has a documented compatibility problem with the update."
  - q: "Does 23H2 require TPM 2.0 and Secure Boot on my laptop?"
    a: "Yes, the standard Windows 11 requirements apply to 23H2, including TPM 2.0 and Secure Boot. If these got disabled in BIOS after a firmware update, Windows Update silently withholds the feature update. Check msinfo32 for Secure Boot state and the TPM management console to confirm both are active before troubleshooting further."
---

Your laptop runs Windows 11, version 23H2 is officially out, and Windows Update insists you are up to date. No error, no message, just silence. It feels like being skipped, and in a sense you are being skipped, but usually for a reason Microsoft considers protective rather than punitive.

Feature updates roll out in controlled waves, and machines with known driver or hardware conflicts get held back until the blockers clear. The good news is that most holds are clearable: outdated drivers, a pending restart, a metered connection, or a corrupted update pipeline. This guide walks through the checks in the order that resolves the most cases the fastest.

## Why this happens

- **Safeguard hold on your hardware:** Microsoft blocks the offer when your driver or hardware combination has a known issue with 23H2.
- **Outdated drivers:** Old graphics, Wi-Fi, or storage drivers are the most common trigger for a safeguard hold.
- **Pending restart:** An earlier update awaiting a restart can freeze the update pipeline and suppress new offers.
- **Corrupted update components:** Damaged cache or services prevent Windows Update from evaluating new feature offers.
- **Metered connection:** A connection flagged as metered pauses feature update downloads silently.
- **TPM or Secure Boot disabled:** If firmware settings changed, the machine may no longer report itself as Windows 11 eligible.
- **Insufficient disk space:** Feature updates need substantial free space before Windows Update even offers them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your current version and eligibility

1. Press **Win + R**, type `winver`, and confirm you are on Windows 11 22H2 or an earlier 23H2 build. If you already have 23H2, there is nothing to wait for.
2. Run `msinfo32` and check that Secure Boot State shows On and the BIOS mode is UEFI.
3. Open `tpm.msc` and confirm the TPM is ready for use with specification version 2.0.
4. If any requirement shows as off, reboot into BIOS and re-enable it. A firmware update sometimes resets these silently, and Windows Update withholds the offer until they are back.

### Fix 2: Clear pending restarts and paused updates

1. Open **Settings > Windows Update** and look for any pending restart prompts or paused update banners. Complete or resume them first.
2. Check **Advanced options** and make sure updates are not paused and optional updates are not being ignored.
3. Restart the laptop fully, not a hybrid shutdown, to clear any stuck pending state.
4. After restarting, click **Check for updates** and wait for the scan to complete. A surprising number of missing offers appear once the pipeline is unstuck.

### Fix 3: Update all drivers to clear safeguard holds

1. Visit your laptop maker's support page for your exact model and install the latest graphics, Wi-Fi, chipset, and storage drivers.
2. On Intel laptops, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) automates detection of outdated Intel drivers.
3. In Device Manager, check for any devices with warning icons and resolve them. A single broken device can sustain a hold.
4. Restart and check for updates again after 24 hours. Safeguard re-evaluation is not instant; Microsoft's servers need a fresh telemetry report from your machine. If the hold persists beyond 48 hours with fully updated drivers, the block is likely hardware-specific and the Installation Assistant in Fix 6 becomes the practical path forward.

### Fix 4: Check the metered connection and storage

1. Go to **Settings > Network & internet > Wi-Fi**, click your network, and make sure **Metered connection** is off.
2. Verify at least 20 GB of free space on the system drive under **Settings > System > Storage**.
3. Run Disk Cleanup as administrator to clear temporary files and old Windows installations if space is tight.
4. With the connection unmetered and space available, click **Check for updates**. Feature offers are suppressed quietly when either condition fails.

### Fix 5: Reset the Windows Update components

1. Open an admin Command Prompt and stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and restart the services with the matching `net start` commands.
3. This forces Windows Update to rebuild its catalog and re-evaluate which updates your machine qualifies for.
4. Check for updates again. If the broader pipeline is unhealthy, the [update service repair guide](/articles/windows-update-service-not-running-troubleshooting/) covers the deeper service fixes.

### Fix 6: Install 23H2 with the Installation Assistant

1. If Windows Update still will not offer 23H2 after the checks above, download the Windows 11 Installation Assistant from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it and follow the prompts. It installs the latest feature update directly, bypassing the Windows Update offer logic.
3. Keep the laptop plugged in and connected to unmetered internet for the duration.
4. This is Microsoft's own supported path and is safe when your drivers are current. If the assistant install fails with a driver error, the [0xC1900101 troubleshooting](/articles/update-fails-with-error-0xc1900101-troubleshooting/) walkthrough decodes it.

### Fix 7: Use the Media Creation Tool as the final path

1. Download the Media Creation Tool and choose **Upgrade this PC now** with **Keep personal files and apps**.
2. The tool fetches the latest Windows 11 build, which includes 23H2 and everything after it, and installs it over your current system.
3. This method also repairs any underlying servicing damage that was suppressing the offer in the first place.
4. Afterward, verify with `winver` that you are on the expected build, then confirm future updates arrive normally. For general background on update mechanics, the [Windows support hub](https://support.microsoft.com/en-us/windows) is the official reference.

## Closing

A missing 23H2 offer is almost always a safeguard hold, a pending state, or a pipeline problem rather than a broken laptop. Verify eligibility, clear pending restarts, update drivers, reset the update components, and the offer appears. When patience runs out, the Installation Assistant delivers the same update through Microsoft's supported side door.
