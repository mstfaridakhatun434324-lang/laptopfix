---
title: "KB5048667 Fails to Install on Your HP Laptop? Here's the Fix"
slug: "how-to-fix-kb5048667-fails-to-install-on-hp-laptop"
date: "2026-09-06"
categories: ["windows-update"]
tags: ["windows update", "kb5048667", "hp laptop", "cumulative update"]
description: "KB5048667 keeps failing to install on your HP laptop? This technician's guide explains why HP machines struggle with this update and walks you through seven ordered fixes."
thumbnail: "/images/thumbs/how-to-fix-kb5048667-fails-to-install-on-hp-laptop.webp"
faqs:
  - q: "Why does KB5048667 fail specifically on HP laptops?"
    a: "HP laptops often fail this update because of HP-specific software conflicts, such as HP Support Assistant holding locks on driver files, outdated HP BIOS versions that conflict with firmware checks, or preinstalled utilities interfering with servicing components. Corrupted Windows Update cache files and third-party antivirus tools are also common causes on HP hardware, and each of these can be resolved with the ordered fixes in this guide."
  - q: "Is it safe to install KB5048667 manually from the Microsoft Update Catalog?"
    a: "Yes, installing from the Microsoft Update Catalog is completely safe as long as you download the correct package for your system architecture, which is x64 for nearly all modern HP laptops. The Catalog is Microsoft's official distribution channel for standalone update packages. Manual installation bypasses Windows Update service issues and often succeeds where automatic installation repeatedly fails on HP machines."
  - q: "Will clearing the SoftwareDistribution folder delete my files?"
    a: "No, clearing the SoftwareDistribution folder is completely safe and will not delete any of your personal files, documents, or installed programs. That folder only stores temporary Windows Update download and installation files. Windows rebuilds it automatically the next time you check for updates. This is one of the most reliable first fixes for a stubborn cumulative update."
  - q: "How long should I wait before trying a different fix?"
    a: "Give each fix one full attempt, including a restart and a fresh check for updates, before moving to the next one. A single update attempt can take ten to thirty minutes, so be patient. If Windows Update fails again with the same error code after a fix, move on to the next step. Most HP laptops are resolved by the fourth fix in this sequence."
---
Seeing KB5048667 fail to install on your HP laptop is frustrating, especially when Windows Update keeps retrying the same download only to roll it back again. KB5048667 is the December 2024 cumulative security update for Windows 11 version 24H2, and it bundles security fixes, quality improvements, and servicing stack changes that your system needs to stay protected. When it refuses to install, your laptop can sit for weeks without critical patches, which is a real problem for a machine you rely on every day.

HP laptops have a few quirks that make this specific update more likely to fail. HP Support Assistant and preinstalled HP drivers can hold locks on files the updater needs to replace, older HP BIOS versions can conflict with the update's firmware checks, and third-party antivirus tools sometimes quarantine servicing components mid-install. The good news is that nearly every KB5048667 installation failure on HP hardware traces back to a small set of causes, and each one has a reliable fix that you can apply yourself in under an hour.

Below I will walk you through why this update fails on HP laptops and give you a technician's ordered repair sequence. We will start with quick checks, then move through cache resets, manual installation from the Microsoft Update Catalog, and component store repair. Follow the fixes in order and stop as soon as the update installs successfully. If you run into a broader pattern where every cumulative update fails, our guide on [fixing cumulative updates that fail every time](/articles/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2/) covers the underlying causes in more depth.

## Why this happens

- **Corrupted Windows Update cache:** Partially downloaded or damaged files in the SoftwareDistribution folder confuse the installer, so it fails the integrity check and rolls back every attempt.
- **HP Support Assistant conflicts:** HP's own update utility can lock driver and firmware files that KB5048667 needs to replace, causing the installation to abort midway.
- **Outdated HP BIOS or chipset drivers:** Older firmware on HP machines can fail the update's hardware readiness checks, especially when Secure Boot or TPM measurements are involved.
- **Third-party antivirus interference:** Security suites from vendors other than Microsoft sometimes quarantine or block servicing components while the update is being applied.
- **Insufficient disk space:** Cumulative updates need several gigabytes of free space for staging, and a nearly full drive or a cramped recovery partition will halt the install.
- **Servicing stack or component store corruption:** Damaged system files in the component store prevent the update engine from assembling the new image correctly.
- **Metered connection or paused updates:** A metered network setting or a paused update state can interrupt the download, leaving a broken package that fails on install.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter

The built-in troubleshooter is the fastest way to catch common problems like stopped services, misconfigured policies, or a stalled download queue. It runs a scripted diagnostic and applies safe automatic repairs, which resolves a surprising number of update failures without any manual work.

1. Open Settings, then go to System and select Troubleshoot.
2. Click Other troubleshooters and find Windows Update in the list.
3. Click Run and let the diagnostic complete without interrupting it.
4. Apply any recommended repairs, then restart your laptop.
5. Open Windows Update and click Check for updates to retry KB5048667.

If the troubleshooter itself misbehaves, see our guide on [fixing a broken Windows Update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/). Microsoft also documents this tool at https://support.microsoft.com/en-us/windows.

### Fix 2: Clear the SoftwareDistribution and catroot2 cache

When cached files are corrupted, Windows Update keeps failing on the same broken package. Deleting the cache forces a clean re-download. This is safe and only removes temporary update files, never your personal data.

1. Open Command Prompt as administrator from the Start menu.
2. Run these commands one at a time: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the folders with: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Restart the laptop, then check for updates again.

### Fix 3: Free up disk space and check the recovery partition

Cumulative updates stage several gigabytes of files before installing. If your C: drive is nearly full or the hidden recovery partition is cramped, the installer aborts. Aim for at least 10 GB of free space on the system drive.

1. Open Settings, go to System, then Storage, and review what is using space.
2. Run Disk Cleanup as administrator and select system files, including old Windows Update files.
3. Delete the contents of your Temp folder by typing `%temp%` in the Run dialog.
4. Uninstall large programs or move media files to external storage if needed.
5. Restart and retry the update once you have comfortable free space.

### Fix 4: Update your HP BIOS, chipset, and drivers first

Outdated HP firmware is a leading cause of KB failures on HP hardware. Bring your drivers current before retrying, because the update's readiness checks often pass once firmware is fresh.

1. Open HP Support Assistant and run a full check for BIOS, driver, and firmware updates.
2. Install everything it offers, allowing the laptop to restart as required.
3. If Support Assistant finds nothing, visit https://support.hp.com/us-en, enter your model, and check manually.
4. Pay special attention to BIOS, chipset, and storage controller updates.
5. After all HP updates are installed, retry KB5048667 in Windows Update.

### Fix 5: Temporarily disable third-party antivirus

Antivirus products can block the servicing stack from replacing protected files. Temporarily disabling real-time protection during the update window removes this variable. Windows Defender stays active as a fallback, so you are not unprotected.

1. Open your antivirus program and find the real-time protection or shield controls.
2. Disable protection for one hour or until the next restart, whichever the program offers.
3. Disconnect from public Wi-Fi during the update if you want extra caution.
4. Run Windows Update and let KB5048667 install without interruption.
5. Re-enable your antivirus immediately after the update completes.

### Fix 6: Install KB5048667 manually from the Microsoft Update Catalog

When the Windows Update service itself is the problem, sideloading the standalone package bypasses it entirely. Manual installation has a very high success rate for stubborn cumulative updates on HP laptops.

1. Go to https://www.catalog.update.microsoft.com and search for KB5048667.
2. Download the x64 package for Windows 11 version 24H2.
3. Double-click the downloaded .msu file to start the standalone installer.
4. Follow the prompts and let the installation finish, then restart.
5. Verify the update in Settings, then Windows Update, then Update history.

### Fix 7: Repair the component store with DISM and SFC

If system image corruption is the root cause, no amount of cache clearing will help. DISM repairs the component store using Windows Update as a source, and SFC then fixes protected system files. Run both before your final retry.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to reach 100 percent.
3. When DISM finishes, run `sfc /scannow` and wait for the verification to complete.
4. Restart the laptop even if no integrity violations were reported.
5. Check for updates one final time and confirm KB5048667 installs.

## Closing

KB5048667 failures on HP laptops almost always come down to cache corruption, HP software conflicts, outdated firmware, or a damaged component store, and the seven fixes above address them in the order a technician would actually try them. Start with the troubleshooter and cache reset, bring your HP drivers current, and use the manual Catalog install if the automatic path keeps failing. Once the update lands, your laptop will be current on security patches again, and future cumulative updates should flow through normally.
