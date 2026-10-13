---
title: "How to Fix Windows Update Error 0x8007000D Step by Step"
slug: how-to-fix-windows-update-error-0x8007000d-step-by-step
date: 2026-10-09
categories: ["windows-update"]
tags: ["windows update", "0x8007000d", "corrupt data", "windows 11"]
description: "Error 0x8007000D means Windows Update found invalid data. Follow this step-by-step guide — SFC, DISM, cache reset, and clean-boot — to repair it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x8007000d-step-by-step.webp"
faqs:
  - q: "What does Windows Update error 0x8007000D mean?"
    a: "It is ERROR_INVALID_DATA: the update package or the system files it depends on failed integrity validation. Causes range from a corrupted download and a damaged component store to antivirus software quarantining update files or disk errors altering stored data. Windows correctly refuses to install unverifiable data, so the fix is about restoring integrity, not forcing the install."
  - q: "Should I run SFC or DISM first?"
    a: "Run SFC first because it is quicker and fixes protected system files directly. If SFC reports unfixable damage or the error persists, run DISM, which repairs the component store that SFC draws from, then run SFC again. This order — SFC, DISM, SFC — is Microsoft's recommended sequence and avoids wasting a long DISM run when a quick SFC would have sufficed."
  - q: "Can a clean boot really fix an update error?"
    a: "Yes, when the cause is interference rather than corruption. Third-party cleaners, aggressive antivirus, and system utilities can delete, quarantine, or lock files while the updater is working, producing invalid-data failures. A clean boot removes those actors; if the update succeeds there, you know to hunt the interfering program instead of repairing the system further."
  - q: "How do I know if my disk is causing the corruption?"
    a: "Suspect the disk when corruption recurs across unrelated files — documents failing to open, apps crashing, plus repeated update validation failures. Run chkdsk C: /f /r from an administrator Command Prompt and review its report. A healthy disk with one bad download points at the network or cache; widespread errors point at failing storage that needs replacing."
---

Error 0x8007000D means ERROR_INVALID_DATA: somewhere between Microsoft's servers and your system, the update data became something Windows can't trust. It might be a download corrupted in transit, a component store with damaged files, or a security tool that "cleaned" a file the installer needed. Windows stops rather than install questionable data — annoying, but the safe choice.

The repair logic is straightforward: verify what's on the system, rebuild what's damaged, clear what's stale, and remove whatever keeps corrupting it. Each step targets one layer of the integrity chain, in the order that resolves most cases with the least effort.

An important distinction guides the whole sequence: "invalid data" can mean the files on your disk are damaged, or it can mean the downloads arriving are damaged. SFC and DISM fix the first; the cache reset and clean boot address the second. If you only do one half — say, repairing the store but never clearing the poisoned cache — the error will keep returning, because fresh repairs get validated against stale, broken downloads. Do both halves and the error has nowhere left to hide. That two-front approach is also why the fixes are ordered the way they are: verify and rebuild the on-disk data first, then clear the cache and remove interference, so each layer is trustworthy before the next one is tested.

## Why this happens

- **Corrupted downloads.** Transfers damaged by interruptions or proxies fail validation.
- **Damaged component store.** WinSxS files the installer checks against are themselves corrupt.
- **Stale cache fragments.** Old partial downloads get reused and fail checks.
- **Antivirus quarantine.** Security software removing pieces of update packages.
- **Disk-level errors.** Bad sectors altering stored files silently.
- **Cleaner utilities.** Third-party tools deleting files mid-update.
- **Interrupted previous updates.** Half-written files left behind by crashes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note which package fails validation

A little diagnosis focuses the repair.

1. Open **Settings > Windows Update > Update history**; record the KB number and type of the 0x8007000D failure.
2. Check whether every update fails or just one — universal failure suggests store or disk damage; a single package suggests a bad download.
3. Note the pattern; you'll use it to judge whether each fix is working.

### Fix 2: Run SFC to repair system files

The quickest integrity check.

1. Open an administrator Command Prompt and run `sfc /scannow`.
2. Wait for 100 percent completion without using the machine heavily.
3. Restart if repairs were made, then retry the update.
4. If SFC couldn't fix everything, don't loop it — proceed to DISM, which repairs SFC's own source.

### Fix 3: Repair the component store with DISM

Rebuild the reference data the installer validates against.

1. In the elevated prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and let it finish downloading clean components.
2. Run `sfc /scannow` once more to confirm consistency.
3. Restart the laptop.
4. Retry the update; the SFC-DISM-SFC sequence clears the corruption variant of this error.

### Fix 4: Reset the update cache

Even a healthy store fails if the download fragments are bad.

1. In an administrator Command Prompt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Check for updates — all packages download fresh and validate cleanly.

### Fix 5: Clean boot to find interference

Isolate software that's damaging files during installation.

1. Run `msconfig`, go to the **Services** tab, check **Hide all Microsoft services**, and click **Disable all**.
2. Disable all **Startup apps** in Task Manager, then restart.
3. Retry the failing update in the clean state.
4. If it works, re-enable services in halves to identify the culprit, then update, replace, or remove that program.

### Fix 6: Manual install and disk verification

Cover the remaining possibilities.

1. Download the failing KB as an x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install it standalone.
2. If it still fails validation, run `chkdsk C: /f /r` from an administrator Command Prompt and reboot to let it scan.
3. Review the chkdsk report for bad sectors or file-system errors.
4. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) covers these integrity tools in depth.

### Fix 7: Re-register the Windows Update DLLs

Misregistered updater components fail validation even when every file is healthy.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Re-register the core libraries: `regsvr32 atl.dll`, `regsvr32 urlmon.dll`, `regsvr32 mshtml.dll`, `regsvr32 shdocvw.dll`, `regsvr32 browseui.dll`, `regsvr32 jscript.dll`, `regsvr32 vbscript.dll`, `regsvr32 scrrun.dll`, `regsvr32 msxml.dll`, `regsvr32 wuapi.dll`, `regsvr32 wuaueng.dll`, `regsvr32 wups.dll` — confirm each dialog.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Retry the update; properly registered components validate packages correctly.

### Fix 8: Perform an in-place upgrade as the final repair

When integrity failures survive every targeted fix, reinstall Windows over itself.

1. Download the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it with a double-click.
2. Run `setup.exe`, accept the license terms, and choose **Keep personal files and apps**.
3. Let the upgrade finish — 30 to 90 minutes, several restarts, charger connected.
4. After signing in, check for updates; the pristine system validates and installs packages cleanly.

## Closing

Error 0x8007000D is an integrity refusal, and the verify-rebuild-clear sequence above restores trustworthy update data on the vast majority of laptops. For HP-specific angles like Support Assistant driver conflicts, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x8007000d-on-hp-laptop/), and if your error is a locked-file conflict rather than invalid data, the [0x80070020 step-by-step guide](/articles/how-to-fix-windows-update-error-0x80070020-step-by-step/) handles that distinct case.
