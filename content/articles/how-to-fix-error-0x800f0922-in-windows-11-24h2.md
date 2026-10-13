---
title: "How to Fix Windows 11 Update Error 0x800f0922 (24H2)"
slug: how-to-fix-error-0x800f0922-in-windows-11-24h2
date: 2026-09-14
categories: ["windows-errors"]
tags: ["update error", "0x800f0922", "Windows 11 24H2"]
description: "Windows 11 24H2 failing with error 0x800f0922? Here's what causes it and the exact steps to get the update installed."
thumbnail: "/images/thumbs/how-to-fix-error-0x800f0922-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x800f0922 mean?"
    a: "It means a Windows update — very often a .NET Framework update or a 24H2 feature update — failed during installation. The two classic triggers are a full System Reserved partition (the update needs free space there to write boot files) and a broken .NET Framework 3.5 component."
  - q: "How much free space does the System Reserved partition need?"
    a: "Microsoft's guidance is at least 50 MB free on the System Reserved partition for the update to stage its boot files. If it's packed with old boot files and fonts, the update fails with 0x800f0922 every time until you clear space."
  - q: "Will these fixes delete my personal files?"
    a: "No. The troubleshooter, partition cleanup, SFC/DISM scans, and update-component reset only touch Windows system files and the update cache. Your documents and programs are safe through every step here."
  - q: "What if 0x800f0922 keeps failing after all these fixes?"
    a: "Download the update manually from the Microsoft Update Catalog and install the .msu file directly — this bypasses the broken Windows Update pipeline entirely. If even that fails, an in-place upgrade with the 24H2 ISO repairs the component store while keeping everything."
---
Error 0x800f0922 is one of those codes that tells you almost nothing — "something went wrong installing the update," thanks, Windows. But after seeing it on plenty of laptops, I can tell you it has two favorite causes on Windows 11 24H2: a System Reserved partition that's too full for the update to use, and .NET Framework components in a broken state. Both are fixable without drama.

This error usually appears when installing cumulative updates or .NET updates, and it fails at a high percentage (often around 90%+) which makes it extra annoying — you wait through the whole download and install, then get the error. Let's fix the actual causes instead of just retrying and hoping.

## Why this happens

- **The System Reserved partition is full.** Windows needs free space on this small hidden partition to stage boot files during the update. Years of accumulated boot files can fill it, and the update fails at the final step. This is the number-one cause of 0x800f0922.
- **Broken .NET Framework 3.5.** Many updates touch .NET components. If the .NET 3.5 feature is in a half-enabled or corrupted state, the update's .NET payload can't install and the whole update rolls back with this code.
- **Corrupted Windows Update cache.** Stale or half-downloaded files in the SoftwareDistribution folder make the installer choke, especially on the large 24H2 payloads.
- **Third-party antivirus blocking the install.** Security suites that hook into system file operations sometimes block the update from writing to protected locations like the System Reserved partition.
- **Secure Boot / firmware quirks.** On some laptops, Secure Boot settings interact badly with the boot-file staging step. It's rarer, but worth knowing if nothing else works.
- **General component store corruption.** If the underlying Windows component store (the "parts bin" Windows builds updates from) is damaged, any update touching those components fails.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Run the Windows Update troubleshooter

It's the obvious first step because it automatically resets the common failure points.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Find **Windows Update** and click **Run**.
3. Let it complete and apply any fixes it suggests, then restart the laptop.
4. Try the update again via **Settings > Windows Update > Check for updates**. If it fails with 0x800f0922 again, continue — the troubleshooter rarely fixes the partition issue, which is next.

### Fix 2: Free space on the System Reserved partition

This is the fix that resolves most 0x800f0922 cases. You'll assign the hidden partition a drive letter, clean out unneeded files, then remove the letter.

1. Press **Win + X**, choose **Terminal (Admin)**, and approve the prompt.
2. Type `diskpart` and press Enter, then type `list volume` and press Enter.
3. Find the volume labeled **System Reserved** (usually around 100–500 MB, FAT32). Note its volume number, then type `select volume N` (replace N) and `assign letter=Z:`.
4. Type `exit` to leave diskpart. Now in the same admin terminal, run:
   `takeown /f Z:\ /r /d Y`
   `icacls Z:\ /grant administrators:F /t`
5. Open **File Explorer**, go to **Z:**, and look in the **EFI\Microsoft\Boot\Fonts** folder — delete unneeded language font files you clearly don't use, and remove any obviously stale `.ttf` files. Don't touch anything else.
6. Back in the terminal, run `diskpart`, then `select volume N`, then `remove letter=Z:` to hide the partition again. Restart and retry the update.

### Fix 3: Repair .NET Framework 3.5

A broken .NET 3.5 feature blocks the update's .NET payload.

1. Press **Win + R**, type `optionalfeatures.exe`, and press Enter to open **Windows Features**.
2. Expand **.NET Framework 3.5 (includes .NET 2.0 and 3.0)**. If it's ticked, untick it, click **OK**, and restart. Then reopen the same dialog, tick it again, click **OK**, and let Windows reinstall it cleanly.
3. If it's unticked, tick it and let it install — the update may simply have needed the feature present.
4. Retry the Windows update. If .NET repair was the issue, the update should now sail through.

### Fix 4: Reset the Windows Update components

This clears the corrupted download cache and restarts the update machinery fresh.

1. Open **Terminal (Admin)** via **Win + X**.
2. Stop the update services:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
3. Rename the cache folders so Windows rebuilds them:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services:
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
   `net start msiserver`
5. Restart the laptop and check for updates again. This same reset also helps with the download-failure cousin [error 0x80240034](/articles/how-to-fix-error-0x80240034-in-windows-11-24h2/).

### Fix 5: Run SFC and DISM

These repair the component store the update builds on.

1. In **Terminal (Admin)**, run `sfc /scannow` and wait for it to finish.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` — this downloads clean component files from Windows Update, so stay online.
3. Restart and retry the update. If DISM itself errors out, that's a strong signal the component store needs the in-place upgrade in Fix 7. For the general approach to update failures, our [Windows 11 installation troubleshooting guide](/articles/windows-11-installation-failed-troubleshooting/) covers overlapping ground.

### Fix 6: Install the update manually from the Microsoft Update Catalog

Bypass the broken automatic pipeline entirely.

1. In **Settings > Windows Update > Update history**, note the **KB number** of the failing update (it looks like KB5037771).
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search for that KB number, and download the version matching your system (x64 for most laptops — check **Settings > System > About > System type** if unsure).
3. Double-click the downloaded `.msu` file and follow the installer. This uses a completely separate install path from Windows Update.
4. Restart when prompted. Manual installs succeed surprisingly often where the automatic route kept failing.

### Fix 7: Do an in-place upgrade with the 24H2 ISO

This reinstalls Windows 11 24H2 over itself, repairing the component store while keeping files, apps, and settings.

1. Download the Windows 11 24H2 ISO from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Double-click the ISO to mount it, then run **setup.exe** from the mounted drive.
3. Choose **Keep personal files and apps** when asked, and let the upgrade run — it takes 30–60 minutes.
4. After it's done, run Windows Update once more. The previously failing update should now install cleanly on the repaired system.

## Closing

Error 0x800f0922 is annoying precisely because it fails late in the process, but it's also one of the more "honest" errors — it's almost always the System Reserved partition or .NET, and both have clean fixes. My practical advice: after you get past it, keep an eye on that little partition. It fills up silently over the years, and a two-minute cleanup now saves you from meeting 0x800f0922 again at the next big update.
