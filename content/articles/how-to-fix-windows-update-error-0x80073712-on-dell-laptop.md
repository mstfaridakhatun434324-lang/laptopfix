---
title: "How to Fix Windows Update Error 0x80073712 on a Dell Laptop"
slug: "how-to-fix-windows-update-error-0x80073712-on-dell-laptop"
date: 2026-09-23
categories: ["windows-update"]
tags: ["windows update", "0x80073712", "component store", "dism", "dell laptop"]
description: "Error 0x80073712 signals corruption in Windows’ component store on your Dell laptop. Here is how DISM, SFC, and a manual install repair it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80073712-on-dell-laptop.webp"
faqs:
  - q: "What does error 0x80073712 actually mean?"
    a: >
      It means Windows Update found the component store — the internal
      database Windows uses to assemble updates — damaged or missing
      entries it needs. The update cannot be constructed, so installation
      stops with this code rather than risking a half-applied patch.
  - q: "Will DISM /RestoreHealth delete my files?"
    a: >
      No. DISM only repairs Windows system files and the component store.
      Your documents, photos, and installed programs are untouched. It is
      one of the safest repair commands you can run on a Windows laptop.
      The tool compares your system files against known-good copies from
      Windows Update and replaces only the damaged ones, leaving
      everything personal exactly where it was.
  - q: "Why does the same update keep failing with this code?"
    a: >
      Because the damage is in the store, not the download. Windows Update
      keeps re-downloading a perfectly good update and failing at the same
      assembly step. Repairing the store with DISM breaks that loop. Until
      the component store is healthy, every attempt follows the identical
      path: download succeeds, package assembly fails, and error
      0x80073712 appears again at the same point.
  - q: "How long does DISM RestoreHealth take?"
    a: >
      Typically 15 to 45 minutes depending on your SSD speed and the
      extent of corruption. The progress bar can appear stuck at certain
      percentages — leave it alone and let it reach 100 percent before
      judging the result. On older spinning hard drives it can take over
      an hour, which is normal. Interrupting it mid-repair risks leaving
      the component store in a worse state than it started.
---

Error 0x80073712 — also reported as ERROR_SXS_COMPONENT_STORE_CORRUPT or CBS_E_MISSING_PACKAGE_MAPPING — means the update engine cannot find or trust the files it needs inside Windows’ component store (the WinSxS folder). Every update is assembled from packages mapped through this store, so when a manifest entry is missing or damaged, the installation stops before it even begins. The download itself is usually fine; the assembly step is what fails.

On Dell laptops this often follows an interrupted update — a dead battery mid-install, a forced shutdown, or a third-party ‘cleaner’ that aggressively pruned system folders. The telltale sign is that the same update fails repeatedly at the same percentage, while everything else on the machine works normally. Running the update troubleshooter alone almost never resolves it, because the troubleshooter does not rebuild the component store.

The reliable path is to repair the store itself with the DISM and SFC tools, then re-attempt the update. If the repair tools cannot fix the damage, a manual install from the Microsoft Update Catalog or an in-place upgrade will replace the broken pieces. Work through the fixes below in order. If you are dealing with a related symptom instead, see [the 0x800F0988 component-store error on Dell](/articles/how-to-fix-windows-update-error-0x800f0988-on-dell-laptop/) and [a feature update stuck at 61 percent](/articles/how-to-fix-feature-update-stuck-at-61-percent-on-dell-laptop/).

You can recognize this as a component-store failure because it strikes at the very start of the install phase and repeats identically every single time — the same update, the same point, the same code. That repeatability is genuinely useful information: it tells you the download is fine and the damage is local to your machine. This guide starts with the quick automated checks, moves through the DISM and SFC repairs that resolve most cases, and finishes with the manual and in-place options for damage that will not heal any other way.

## Why this happens

- **Corrupt component store manifests** missing or damaged WinSxS mapping files stop package assembly.

- **Interrupted update installation** a power loss or forced reboot mid-install leaves the store half-written.

- **Aggressive system cleaners** third-party tools that prune WinSxS or manifests break package mappings.

- **Disk errors on the system drive** bad sectors in the component store region corrupt stored packages.

- **Failed cumulative update layering** a skipped or partially installed update leaves gaps later updates expect.

- **Antivirus quarantining system files** overzealous real-time protection can lock files mid-write.

- **Incomplete servicing stack update** the update engine itself is damaged and misreads the store.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter first

It is a quick first pass that can clear simple blockers before you move to store repair. The whole check takes about five minutes, and it occasionally clears a stuck update state that merely mimics store corruption — worth ruling out before the heavier repairs.

1. Open Settings > System > Troubleshoot > Other troubleshooters.

2. Click Run next to Windows Update.

3. Apply any fixes it suggests and restart the laptop.

4. Try the update once more — if 0x80073712 returns, continue below.

### Fix 2: Repair the component store with DISM

DISM’s RestoreHealth operation downloads clean copies of corrupted store files and is the primary fix for this error. If RestoreHealth complains it cannot find source files, point it at a Windows ISO with the /Source option, or simply move on to the manual install fix below.

1. Open Command Prompt or Terminal as administrator.

2. Run: DISM /Online /Cleanup-Image /ScanHealth and note what it reports.

3. Run: DISM /Online /Cleanup-Image /RestoreHealth.

4. Wait for it to reach 100% — this can take 15–30 minutes.

5. Restart the laptop, then run Windows Update again.

### Fix 3: Follow up with System File Checker

After DISM repairs the store, SFC replaces corrupted protected system files using the now-healthy store as its source. Make it a habit to run SFC after every DISM repair: DISM heals the store, SFC heals the files, and Microsoft designed the two tools to be used in exactly that order.

1. In the same elevated Command Prompt, run: sfc /scannow.

2. Let it complete to 100% without closing the window.

3. If it reports it fixed files, restart the laptop.

4. Re-run Windows Update and check whether 0x80073712 is gone.

### Fix 4: Reset the Windows Update components

Stale update metadata can keep pointing at the broken mappings even after the store is repaired, so resetting the components forces a clean state. Renaming instead of deleting keeps a safety net — if anything behaves oddly afterward, you can restore the .old folders and return to the previous state.

1. Open Command Prompt as administrator.

2. Run: net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver.

3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old and C:\Windows\System32\catroot2 to catroot2.old.

4. Run: net start wuauserv, net start cryptSvc, net start bits, net start msiserver.

5. Retry the update.

### Fix 5: Install the update manually from the Catalog

A manual install bypasses the damaged automatic pipeline and often succeeds where Windows Update keeps failing. If the standalone installer also fails, it writes detailed output to the CBS logs, giving you a concrete next clue instead of another bare error code.

1. Note the KB number of the failing update in Settings > Windows Update > Update history.

2. Go to [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for that KB number.

3. Download the x64 package matching your Windows version.

4. Double-click the .msu file and follow the installer prompts.

5. Restart when prompted and verify the KB appears in update history.

### Fix 6: Check the drive for errors

Because store corruption can come from a failing SSD sector, ruling out disk problems prevents the error from recurring. Schedule this for a time you can leave the laptop alone, since the /r surface scan on a large drive can easily take an hour or more.

1. Open Command Prompt as administrator.

2. Run: chkdsk C: /f /r and confirm the scan at next restart.

3. Restart the laptop and let the disk check complete.

4. Afterward, run DISM /Online /Cleanup-Image /RestoreHealth once more.

5. Retry Windows Update.

### Fix 7: Perform an in-place upgrade as the last resort

An in-place upgrade reinstalls Windows over itself, rebuilding the entire component store while keeping your files and apps. Expect the upgrade to take 30 to 90 minutes with several restarts; keep the laptop on AC power and do not interrupt it.

1. Back up important files first.

2. Download the Windows 11 installation media from [Microsoft’s software download page](https://www.microsoft.com/en-us/software-download/windows11).

3. Run setup.exe from the mounted ISO and choose ‘Keep personal files and apps’.

4. Complete the upgrade, then run Windows Update normally.

## Closing

The 0x80073712 error looks intimidating, but it is one of the most fixable update failures because DISM was designed for exactly this damage. Most Dell laptops are back to updating normally after a RestoreHealth pass — and if not, the manual Catalog install or in-place upgrade finishes the job without losing your data. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
