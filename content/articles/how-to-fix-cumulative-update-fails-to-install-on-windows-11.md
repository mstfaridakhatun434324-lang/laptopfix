---
title: "Cumulative Update Refuses to Install on Windows 11: Fixes That Work"
slug: how-to-fix-cumulative-update-fails-to-install-on-windows-11
date: 2026-09-05
categories: ["windows-update"]
tags: ["cumulative update", "windows 11", "install failed", "kb update"]
description: "A cumulative update that fails every month needs a systematic fix. Diagnose why Windows 11 cumulative updates fail and apply the repairs that actually resolve them."
thumbnail: "/images/thumbs/how-to-fix-cumulative-update-fails-to-install-on-windows-11.webp"
faqs:
  - q: "Why does the same cumulative update fail every month?"
    a: "Because the underlying blocker never changes. Cumulative updates are monthly and large, so the same corrupted cache, conflicting driver, or damaged system file trips the installer every single time. Fixing the root cause once ends the monthly cycle — the fixes in this article are designed to find exactly that root cause."
  - q: "Is it safe to skip a failed cumulative update?"
    a: "Temporarily, yes — your system keeps working. But cumulative updates bundle security patches, so skipping them repeatedly leaves known vulnerabilities unpatched. Do not treat skipping as a solution; treat it as a pause while you work through the fixes. Microsoft details update contents on its support site."
  - q: "How much free space does a cumulative update need?"
    a: "Plan on at least 10 to 20 GB of free space on the system drive. The update downloads a large package, stages it, and keeps rollback data until the install succeeds. Laptops with small SSDs hit this wall often, and the installer does not always report space as the reason it failed."
  - q: "Should I pause updates while fixing this?"
    a: "A short pause of one to two weeks is reasonable — it stops the failing update from retrying while you repair the system. Do not leave updates paused indefinitely. Unpause and retry once you have worked through the fixes, so you confirm the repair actually worked."
---

Cumulative updates are the monthly heartbeat of Windows 11 — security patches, reliability fixes, and small improvements bundled into one package. When the same cumulative update fails to install month after month, it stops being an annoyance and starts being a security problem, because every skipped update is a stack of unpatched vulnerabilities.

The failure pattern matters. If the update downloads and then fails at install, you are looking at corruption, conflicts, or space. If it will not even download, the problem is upstream — services, network, or the update engine itself. The sequence below covers both patterns in diagnostic order. For [download-stuck cases specifically](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/), start there; otherwise begin with Fix 1.

## Why this happens

- **Corrupted SoftwareDistribution cache:** The downloaded package is damaged, so verification fails at install time.
- **Low disk space:** Staging plus rollback data exceeds available space, and the installer aborts.
- **Conflicting third-party software:** Security suites and system utilities block installer operations.
- **Damaged system files:** Pre-existing corruption fails the installer's integrity checks.
- **Stuck update services:** wuauserv or BITS in a bad state prevents proper staging of the package.
- **Driver incompatibility:** A driver the cumulative update tries to replace resists or conflicts.
- **Metered connection limits:** Windows holds back large downloads on connections marked as metered.
- **Corrupted Catroot2 signatures:** The signature catalog that validates update packages is damaged.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Free disk space and retry

The fastest win — cumulative updates are large, and space is the number one silent killer.

1. Open **Settings > System > Storage** and check free space on the system drive.
2. Run Disk Cleanup: search for it, select the system drive, and check every safe category including **Windows Update Cleanup**.
3. Uninstall programs you no longer use and move large media files to external storage.
4. Aim for at least 20 GB free before retrying.
5. Run Windows Update again and watch whether the install proceeds further than before.

### Fix 2: Run the Windows Update troubleshooter

Let the automated tool take a pass — it handles service restarts and cache flags well.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to Windows Update.
3. Apply all recommended fixes.
4. Restart the laptop.
5. Retry the cumulative update.

### Fix 3: Reset the update components

The definitive cache repair. This resolves most failures that survive the troubleshooter.

1. Open Command Prompt as administrator.
2. Stop the services:
   ```
   net stop wuauserv
   net stop bits
   net stop cryptsvc
   net stop msiserver
   ```
3. Rename both cache folders:
   ```
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   ```
4. Restart all four services with `net start` for each.
5. Restart the laptop and check for updates — the package downloads fresh.

### Fix 4: Check the update services

If the [update service itself will not stay running](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/), every download attempt is doomed regardless of cache state.

1. Press Win + R, type `services.msc`, and press Enter.
2. Verify **Windows Update**, **Background Intelligent Transfer Service**, and **Cryptographic Services** are all set to **Automatic** (BITS can be Manual).
3. If any are stopped, start them and watch for immediate error messages.
4. Check the **Recovery** tab of each service — set first and second failures to **Restart the Service**.
5. Retry the update.

### Fix 5: Repair with DISM and SFC

Installer integrity checks fail on damaged system files; repair the image first.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for completion.
3. Run `sfc /scannow` next.
4. Restart the laptop.
5. Retry the cumulative update — the checks that failed before now pass.

### Fix 6: Disable metered connection and third-party blocks

Make sure nothing upstream is throttling or blocking the download.

1. Go to **Settings > Network & internet > Wi-Fi** (or Ethernet), open your connection, and turn off **Metered connection**.
2. Temporarily disable third-party antivirus real-time protection.
3. Disconnect from any VPN — some VPNs interfere with the update delivery network.
4. Retry the update on a stable, unmetered connection.
5. Re-enable your security software immediately after.

### Fix 7: Install from the Microsoft Update Catalog

When the automatic engine keeps failing, the standalone installer bypasses it entirely. Microsoft hosts every cumulative update on the [Update Catalog](https://www.catalog.update.microsoft.com/), and the [Windows support hub](https://support.microsoft.com/en-us/windows) documents manual installation.

1. Find the KB number in **Settings > Windows Update > Update history**.
2. Search the Update Catalog for that KB and download the x64 package.
3. Close all applications and run the installer.
4. Restart when prompted.
5. Confirm the KB shows as installed in update history.

### Fix 8: Check for a hidden driver block

Some cumulative updates fail because of a driver that Windows Update keeps trying to bundle with the package. Isolating the driver side often unblocks the cumulative update itself.

1. Open **Settings > Windows Update > Advanced options > Optional updates**.
2. Look at the driver updates section — note any that have been failing repeatedly.
3. Temporarily hide the problematic driver update (right-click the device in Device Manager and disable it during the update window).
4. Retry the cumulative update with the driver out of the picture.
5. Re-enable the device afterward and install its driver separately from the manufacturer's site.

## Closing

A cumulative update that fails repeatedly is telling you something specific about your system — corrupted cache, cramped disk, damaged files, or a blocking program. The sequence above finds it: space and the troubleshooter clear the easy cases, the component reset and DISM handle the stubborn ones, and the manual catalog install is the reliable last resort. Fix it once, properly, and next month's cumulative update will install the way it is supposed to — quietly, in the background, without drama. Keep a monthly habit of checking update history after Patch Tuesday so any new failure gets caught early while it is still easy to fix.
