---
title: "How to Install a KB Update Manually From the Catalog on Windows 10"
slug: how-to-install-kb-update-manually-from-catalog-on-windows-10
date: 2026-09-02
categories: ["windows-update"]
tags: ["install kb update manually", "microsoft update catalog", "windows 10 manual update", "msu installer"]
description: "Need to install a Windows 10 KB update by hand? Find the right package on the Microsoft Update Catalog, match your architecture, and install the .msu correctly."
thumbnail: "/images/thumbs/how-to-install-kb-update-manually-from-catalog-on-windows-10.webp"
faqs:
  - q: "Is it safe to download updates from the Microsoft Update Catalog?"
    a: "Yes. The Catalog at catalog.update.microsoft.com is Microsoft's official update archive, and every package is digitally signed by Microsoft. It is the same source Windows Update itself pulls from. Just avoid third-party sites offering 'update downloads' — those are unnecessary and sometimes bundled with junk."
  - q: "How do I know if I need the x64 or ARM64 version?"
    a: "Press Win + R, type msinfo32, and look at System Type. The vast majority of Windows laptops are x64-based PCs. ARM64 applies to Snapdragon/ARM laptops. Installing the wrong architecture gives a 'not applicable' error, so check before downloading. When in doubt, x64 is the safe assumption for Intel and AMD machines."
  - q: "What does 'this update is not applicable to your computer' mean?"
    a: "It means the package does not match your system: wrong architecture, wrong Windows build, the update is already installed, or a newer cumulative has superseded it. It does not mean the file is corrupt. Re-check each of those four things in order."
  - q: "Do I need to install updates in a specific order?"
    a: "Yes, when prerequisites exist. Servicing stack updates (SSUs) must be installed before the cumulative update that needs them — the KB article lists prerequisites explicitly. Monthly cumulative updates are themselves cumulative, so you only need the latest one, not every month in sequence."
---

Windows 10 users sometimes need to install an update by hand: Windows Update may be broken, a specific KB might fix a problem you have right now, or you may be updating a machine with no internet access to Microsoft's update servers. The Microsoft Update Catalog hosts every published update as a standalone .msu file, and installing one is straightforward once you know the exact KB number and the install order. [installing a KB manually on Windows 11](/articles/how-to-install-kb-update-manually-from-catalog-in-windows-11-24h2/)

The two mistakes that cause most manual-install failures: grabbing the wrong architecture (x64 vs ARM64), and installing a cumulative update before its required servicing stack update. This guide covers identifying the right file, the correct order, and what to do when the standalone installer itself throws an error.

## Why this happens

- **Wrong architecture downloaded.** x64 vs ARM64 mismatch is the most common manual-install failure. msinfo32's System Type line settles x64 vs ARM64 definitively.
- **Missing servicing stack prerequisite.** The cumulative update needs its SSU installed first. The KB article's prerequisites section names the required SSU explicitly.
- **KB does not apply to your build.** Updates are build-specific; a 24H2 KB will not install on 23H2. winver shows your build; the KB page shows its target builds.
- **Update already installed.** The installer refuses duplicates, sometimes with a confusing message. Check Installed Updates in the Control Panel for the KB number.
- **Corrupted .msu download.** Incomplete downloads fail signature validation. Re-download from the Catalog; partial downloads fail signature checks.
- **Pending restart blocking.** A previous update awaiting reboot blocks new standalone installs. A simple reboot clears most pending states.
- **Windows Update service disabled.** The standalone installer still needs the service running. The standalone installer needs wuauserv running even though it is 'standalone'.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact KB number you need

Installing the right update starts with knowing precisely which one it is. The KB number is the key to everything: find it in Settings > Windows Update > Update history, and confirm what it targets on Microsoft's support site before downloading.

1. Open Settings > Windows Update > Update history to see failed or missing updates.
2. Note the full KB number (e.g., KB5044284).
3. Check your build with winver so you match the KB to the right Windows version.
4. Search Microsoft's support site for the KB article to confirm what it fixes.
5. Write down the KB number — you will search the Catalog with it.
6. Confirm the KB appears in Settings > Windows Update > Update history as installed.

### Fix 2: Verify your architecture and build

Download the package that matches your machine, not just your Windows version. Architecture mismatch (x64 vs ARM64) is the most common manual-install failure — verify with msinfo32's System Type line before downloading anything.

1. Press Win + R, type msinfo32, and check 'System Type'.
2. x64-based PC means you need the x64 package; ARM64 needs the ARM64 one.
3. Note the OS build number from the same screen.
4. On the Catalog, each KB lists multiple files — pick the one matching your architecture.
5. When in doubt, x64 covers the large majority of laptops.
6. Run winver and verify the build number matches the KB's documented target.

### Fix 3: Download from the Microsoft Update Catalog

The Catalog is the only source you should use. [a cumulative update that fails to install](/articles/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2/) Cumulative updates are, as the name says, cumulative: you only need the latest one for your build, not every month in sequence.

1. Go to [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) in your browser.
2. Search for the KB number (e.g., KB5044284).
3. Find the entry matching your Windows version and architecture.
4. Click Download, then click the file link in the popup window.
5. Save the .msu somewhere easy to find, like Downloads.
6. If the KB was meant to fix a specific problem, test that problem now.

### Fix 4: Install any prerequisite servicing stack update first

Order matters: the SSU goes in before the cumulative update. The servicing stack update (SSU) prerequisite is listed in the KB article; installing it first prevents the classic 'not applicable' error.

1. Check the KB article's prerequisites section for a required SSU.
2. If one is listed, download that KB from the Catalog too.
3. Install the SSU .msu first and restart if prompted.
4. Then install your main cumulative update .msu.
5. Skipping this step is the top cause of 'this update is not applicable' errors.
6. Keep the .msu file for a week before deleting it, in case a rollback needs it.

### Fix 5: Run the standalone installer

The actual install is the easy part. The Catalog lists multiple files per KB — match both the Windows version and the architecture, ignoring Server and ARM entries on a standard laptop.

1. Double-click the .msu file.
2. Click Yes on the User Account Control prompt.
3. Wait for the 'Windows Update Standalone Installer' to prepare and install.
4. Restart when prompted — do not skip the restart.
5. Verify in Settings > Windows Update > Update history that the KB shows as installed.
6. Run a normal Windows Update check afterward to confirm automatic updates still work.

### Fix 6: Handle 'not applicable to your computer'

This error means a mismatch, not a broken file. A superseded KB refuses to install because a newer cumulative already contains it; check update history for the newer KB first.

1. Re-verify the architecture: x64 vs ARM64.
2. Confirm the KB targets your Windows build (winver).
3. Check whether the update is already installed or superseded by a newer cumulative.
4. Install the prerequisite SSU if you skipped it.
5. If it truly should apply, re-download — the file may be corrupt.
6. Note the exact filename you installed; Catalog filenames encode the KB, build, and architecture.

### Fix 7: Use DISM for stubborn packages

When the GUI installer fails, the command-line path sometimes succeeds. The .msu format is just a wrapper around cabinet files; the 'Windows Update Standalone Installer' (wusa.exe) is what actually processes it.

1. Open Command Prompt as administrator.
2. Run: DISM /Online /Add-Package /PackagePath:C:\path\to\update.msu.
3. Wait for it to complete and note any error code.
4. Restart afterward even if not prompted.
5. DISM gives clearer error messages than the GUI installer.
6. If the installer reported success but the KB is missing from history, reboot and check again.

## Closing

Manual installation is a core Windows skill: identify the KB, match the architecture, respect the prerequisite order, and the .msu does the rest. Keep the Catalog bookmarked — it is the fastest bypass whenever the automatic update path breaks down. For updates that fail even when delivered manually, [the best way to install a KB manually](/articles/best-way-to-install-kb-update-manually-from-catalog/) addresses the servicing side.
