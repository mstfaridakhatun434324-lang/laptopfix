---
title: "How Do I Fix Windows 11 23H2 Not Showing in Update?"
slug: how-do-i-fix-windows-11-23h2-not-showing-in-update
date: 2026-10-04
categories: ["windows-update"]
tags: ["windows 11 23h2", "update missing", "feature update", "fix guide"]
description: "A practical, step-by-step answer: get the missing Windows 11 23H2 update offered on your laptop, or install it directly with Microsoft's own tools."
thumbnail: "/images/thumbs/how-do-i-fix-windows-11-23h2-not-showing-in-update.webp"
faqs:
  - q: "I checked for updates and 23H2 is still missing. What now?"
    a: "Work through the pipeline: restart to clear pending states, update all drivers from your laptop maker's site, reset the Windows Update cache, and check for updates again. If the offer still does not appear after 24 hours, use the Windows 11 Installation Assistant from Microsoft's download page, which installs 23H2 directly without waiting for the Windows Update offer."
  - q: "Is it safe to force the 23H2 install with the Installation Assistant?"
    a: "Yes, when your hardware meets Windows 11 requirements and your drivers are current. The Installation Assistant is Microsoft's own supported tool, not a hack. The only situation to avoid forcing is a known documented incompatibility with your specific model. For everyone else, it delivers exactly the same update Windows Update would eventually offer."
  - q: "How do I know if Microsoft is blocking 23H2 for my laptop?"
    a: "You cannot see the block directly, but the pattern is recognizable: everything else updates fine, drivers are current, the pipeline is healthy, and only the 23H2 offer is missing. Outdated graphics, Wi-Fi, or storage drivers cause most blocks, so updating those from the manufacturer is the practical way to lift them. Give it 24 to 48 hours after driver updates for re-evaluation."
  - q: "Will I lose anything installing 23H2 through the assistant?"
    a: "No. The Installation Assistant performs an in-place upgrade that keeps your files, apps, and settings. It downloads the update, verifies it, and installs it like a normal feature update. Keep the laptop plugged in and avoid interrupting it, and the process completes with everything intact."
---

You open Windows Update, click Check for updates, and get told you are up to date. But you know 23H2 exists, your friend's laptop got it weeks ago, and yours sits on 22H2 with no explanation. It is a frustrating, silent problem: no error code to search, just an absence.

This is the practical fix-it version of the problem. No theory about rollout waves beyond what matters: a checklist that gets the offer to appear, and when the offer refuses to appear, the supported tools that install 23H2 anyway. Follow it top to bottom.

## Why this happens

- **Safeguard hold:** Microsoft withholds the update from hardware with known driver conflicts until they are resolved.
- **Stale drivers:** Outdated graphics, network, or storage drivers are the usual reason for the hold.
- **Pending update state:** An unfinished earlier update blocks new feature offers from being evaluated.
- **Damaged update cache:** Corrupted local data prevents Windows Update from seeing available features.
- **Metered connection flag:** Windows quietly skips feature downloads on metered networks.
- **Disabled TPM or Secure Boot:** Firmware changes can silently disqualify the machine from the offer.
- **Low disk space:** The offer is suppressed when there is not enough room to stage the update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and check properly

1. Save your work and do a full restart from the Start menu, not a shutdown, to clear any pending update states.
2. After rebooting, open **Settings > Windows Update** and click **Check for updates**. Wait for the scan to fully complete.
3. Look carefully at the results page. Sometimes the feature update appears under optional updates or as a small banner that is easy to miss.
4. If it is genuinely absent, continue. This basic step resolves the cases where a stuck pending state was suppressing the offer.

### Fix 2: Update your drivers from the manufacturer

1. Go to your laptop maker's support site, enter your exact model, and download the latest graphics, Wi-Fi, Bluetooth, chipset, and storage drivers.
2. Install them one by one, restarting when prompted. Do not rely on Windows Update's driver versions for this task, since the hold exists precisely because Microsoft considers those versions suspect.
3. Intel laptop owners can use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to automate the Intel-side updates.
4. After all drivers are current, check for updates again. If the offer does not appear immediately, wait 24 hours for Microsoft's servers to re-evaluate your machine with fresh telemetry. Graphics drivers are the single most common hold trigger, so prioritize those if you are short on time.

### Fix 3: Free space and unmeter the connection

1. Open **Settings > System > Storage** and confirm at least 20 GB free on the system drive.
2. Run Disk Cleanup as administrator and remove temporary files, delivery optimization files, and previous Windows installations you no longer need.
3. Go to **Settings > Network & internet**, open your connection properties, and turn off **Metered connection** if it is on.
4. Check for updates once more. Both low space and metered flags suppress the offer without any warning message.

### Fix 4: Reset the Windows Update cache

1. Open an admin Command Prompt and run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`, then restart the services with the matching `net start` commands.
3. This forces Windows Update to rebuild its catalog and re-check which feature updates your machine qualifies for. The old folder stays as a backup until you are confident everything works.
4. Click **Check for updates** and let the fresh scan complete, which can take several minutes on a rebuilt cache. For deeper service-level problems, the [update service troubleshooting](/articles/windows-update-service-not-running-troubleshooting/) guide covers the full repair.

### Fix 5: Verify firmware requirements are still met

1. Press **Win + R**, type `msinfo32`, and confirm Secure Boot State is On and BIOS Mode is UEFI.
2. Run `tpm.msc` and verify the TPM reports ready for use at specification version 2.0.
3. If either got disabled, perhaps by a BIOS update resetting defaults, reboot into firmware settings and re-enable them.
4. After re-enabling, boot into Windows and check for updates. Eligibility is re-evaluated on each scan, so the offer can appear immediately.

### Fix 6: Install 23H2 with the Installation Assistant

1. Go to the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and download the **Windows 11 Installation Assistant**.
2. Run it and follow the prompts. It downloads and installs the latest feature update directly, keeping your files and apps.
3. Keep the laptop on AC power with a stable, unmetered connection for the whole process.
4. When it finishes, run `winver` to confirm the new build. This is Microsoft's supported path and works even when Windows Update never makes the offer.

### Fix 7: Use the Media Creation Tool for a full refresh

1. If the assistant also struggles, download the Media Creation Tool from the same Windows 11 download page linked above.
2. Choose **Upgrade this PC now** and select **Keep personal files and apps**.
3. The tool installs the newest Windows 11 build with all updates integrated, which also repairs any servicing damage that was hiding the offer.
4. Afterward, updates should flow normally. For background on how Microsoft stages these releases, the [Windows support hub](https://support.microsoft.com/en-us/windows) has the official documentation. The diagnostic angle on missing offers is covered in the [23H2 troubleshooting guide](/articles/troubleshoot-windows-11-23h2-not-showing-in-update/).

## Closing

Getting 23H2 onto your laptop is a checklist problem, not a mystery. Restart, update drivers, free space, reset the cache, verify firmware, and the offer usually appears. When it does not, the Installation Assistant installs the same update through the front door Microsoft built for exactly this situation. Either way, you end up on the current build with updates flowing normally again.
