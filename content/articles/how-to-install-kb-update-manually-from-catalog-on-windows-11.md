---
title: "How to Install a KB Update Manually From the Catalog on Windows 11"
slug: how-to-install-kb-update-manually-from-catalog-on-windows-11
date: 2026-09-03
categories: ["windows-update"]
tags: ["install kb update manually", "microsoft update catalog", "windows 11 manual update", "msu installer"]
description: "Need to install a Windows 11 KB update manually? Get the right .msu from the Microsoft Update Catalog, handle prerequisites, and verify the installation with this guide."
thumbnail: "/images/thumbs/how-to-install-kb-update-manually-from-catalog-on-windows-11.webp"
faqs:
  - q: "What does 'this update is not applicable to your computer' mean?"
    a: "The package does not match your system: wrong architecture, wrong Windows build, the update already installed, or a newer cumulative that superseded it. It does not mean the file is corrupt. Recheck those four items in order before assuming the download is bad."
  - q: "Do I need to install updates in a specific order?"
    a: "Yes, where prerequisites exist. Servicing stack updates (SSUs) must precede the cumulative update that needs them — the KB article lists prerequisites explicitly. Monthly cumulative updates are themselves cumulative, so you need only the latest one, not every month in sequence."
  - q: "Can I install a Windows 11 KB on Windows 10?"
    a: "No. Updates target specific Windows versions, and a Windows 11 package refuses to install on Windows 10 with a 'not applicable' error. Always match the KB to your installed version, which you can confirm by running winver from the Run dialog."
  - q: "Will a manual install break future automatic updates?"
    a: "No. A manually installed update registers in update history just like an automatic one, and Windows Update continues normally afterward. The system state is identical regardless of delivery path — manual installation is fully supported by Microsoft. Mix manual and automatic installs freely going forward."
---

Installing a KB update by hand from the Microsoft Update Catalog is one of the most useful troubleshooting skills on Windows 11. It routes around a broken Windows Update engine, lets you grab the exact fix Microsoft published for your problem, and works even where policy blocks automatic updates. The Catalog is Microsoft's official archive — every file is signed and safe. [the best way to install a KB manually](/articles/best-way-to-install-kb-update-manually-from-catalog/)

Where people stumble is rarely the installation itself but the groundwork: identifying the right KB, matching it to your build and architecture, and satisfying prerequisites. Nail those and the .msu installs in minutes. The walkthrough below covers the full process, including the standalone installer's error messages and what each one signifies.

## Why this happens

- **Update already installed.** The installer rejects duplicates, sometimes confusingly. Check Installed Updates in Control Panel for the KB number.
- **Corrupted .msu download.** Incomplete downloads fail signature checks. Re-download from the Catalog; partial files never validate.
- **Pending restart in the way.** A previous update awaiting reboot blocks new standalone installs. One reboot clears most pending states.
- **Windows Update service disabled.** The standalone installer still needs wuauserv running, despite the 'standalone' name.
- **Superseded update.** A newer cumulative already includes this KB, so it refuses. Check update history for the newer cumulative first.
- **Language pack mismatch.** Uncommon, but some updates target specific languages. Most consumer updates are language-neutral; confirm on the KB page.
- **Not enough disk space.** The .msu expands to several times its download size while staging. Free room before installing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the prerequisite servicing stack update first

Order matters: the SSU goes in before the cumulative. The KB article's prerequisites section names the required SSU, and installing it first avoids the classic 'not applicable' error.

1. Read the KB article's prerequisites section for a required SSU.
2. If one is listed, download that KB from the Catalog as well.
3. Install the SSU .msu first, restarting if prompted.
4. Then install your main cumulative .msu.
5. Skipping this step is the leading cause of 'this update is not applicable' errors.
6. Hold onto the .msu for a week before removing it, in case a rollback needs it.

### Fix 2: Run the standalone installer

The install itself is the easy part. The Catalog lists several files per KB — match the Windows version and the architecture, skipping Server and ARM entries on a standard laptop.

1. Double-click the .msu.
2. Click Yes at the User Account Control prompt.
3. Wait while the 'Windows Update Standalone Installer' prepares and installs.
4. Reboot when prompted — do not skip the restart.
5. Confirm the KB appears in Settings > Windows Update > Update history.
6. Run a normal Windows Update check afterward to verify automatic updates still work.

### Fix 3: Resolve 'not applicable to your computer'

This signals a mismatch, not a broken file. A superseded KB refuses because a newer cumulative already contains it — check history for the newer KB first.

1. Re-verify the architecture: x64 versus ARM64.
2. Verify the KB targets your Windows build (winver).
3. Check whether it is already installed or superseded by a newer cumulative.
4. Install the prerequisite SSU if you skipped it earlier.
5. If it genuinely should apply, re-download — the file may be damaged.
6. Note the exact filename; Catalog filenames encode the KB, build, and architecture.

### Fix 4: Use DISM for stubborn packages

When the GUI installer fails, the command line sometimes succeeds. The .msu is a wrapper around cabinet files; wusa.exe is what actually processes it.

1. Open an elevated Command Prompt.
2. Execute `DISM /Online /Add-Package /PackagePath:C:\path\to\update.msu`.
3. Wait for it to finish and note any error code.
4. Restart afterward even if you are not prompted.
5. DISM reports clearer errors than the GUI installer.
6. If it claimed success but the KB is missing from history, reboot and check again.

### Fix 5: Clear a pending restart first

A machine awaiting reboot from a previous update blocks new installs. On Windows 11, winver shows the exact build the KB must match — close does not count for applicability.

1. Look for C:\Windows\WinSxS\pending.xml.
2. Simply reboot the laptop — most pending states clear on restart.
3. After rebooting, run the .msu again before doing anything else.
4. If pending.xml survives reboots, investigate the stuck update first.
5. Never delete pending.xml casually; rebooting is the safe clearance.
6. Verify the file's digital signature (right-click > Properties > Digital Signatures) if the download seems suspect.

### Fix 6: Confirm the installation actually landed

Verify the KB is present and active. Keep downloaded .msu files until the system is stable — they serve as your offline reinstall path if the update rolls back.

1. Go to Settings > Windows Update > Update history.
2. Verify the KB number appears under quality updates.
3. Run winver and check the build matches the KB's target.
4. If the issue the KB was meant to fix persists, it may not have been the right KB.
5. Keep the .msu file until everything is stable.
6. Remove partial or failed downloads from the Downloads folder to avoid later confusion.

### Fix 7: Recognize when manual install is not the answer

Manual installs bypass delivery problems, not servicing corruption. DISM /Online /Add-Package accepts .msu paths directly and gives clearer errors than the GUI installer when something is wrong.

1. If the .msu fails with servicing errors, repair the component store first.
2. Run SFC and DISM before retrying the install.
3. If several manual installs fail identically, perform an in-place upgrade repair.
4. Manual installation bypasses delivery problems; it does not fix corruption.
5. Restore servicing health first, then deliver updates however you like.
6. Record the KB and the reason you installed it manually for future reference.

## Closing

After your first manual KB install, Windows Update loses much of its mystery — same payload, different door. Check update history, hold onto the .msu until you are stable, and see [a cumulative update that fails to install](/articles/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2/) if the engine underneath needs mending. For Microsoft's own documentation on these repairs, consult [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).
