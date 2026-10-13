---
title: "How to Fix the Windows Update Troubleshooter When It Won’t Run"
slug: how-to-fix-windows-update-troubleshooter-not-working-youtube
date: 2026-09-10
categories: ["windows-update"]
tags: ["windows update troubleshooter not working", "troubleshooter won't start", "diagnostic policy service", "windows 11 troubleshoot fix"]
description: "Windows Update troubleshooter won't start or crashes? Enable the diagnostic services, refresh its packages, or perform the same repairs manually."
thumbnail: "/images/thumbs/how-to-fix-windows-update-troubleshooter-not-working-youtube.webp"
faqs:
  - q: "What does 'a problem is preventing the troubleshooter from starting' mean?"
    a: "It means one of the troubleshooter's dependencies failed — usually the Diagnostic Policy Service is disabled or its diagnostic package is corrupt. Enable the diagnostic services in services.msc first; that resolves most cases immediately. The exact failing dependency is sometimes named in the System event log."
  - q: "Is the troubleshooter actually useful, or should I skip it?"
    a: "It automates the standard repairs — service restarts, cache clears, re-registration — and succeeds on simple cases. But the manual sequence in this guide does the same repairs more thoroughly. If the tool will not run, you lose nothing by going manual."
  - q: "Why would anyone disable the Diagnostic Policy Service?"
    a: "Debloat and privacy tools disable it to reduce background activity and telemetry. The side effect is breaking all troubleshooters. If you ran such a tool, its changes are the prime suspect whenever a troubleshooter refuses to start. The telemetry savings are minor compared to losing every built-in diagnostic tool."
  - q: "Can I download the troubleshooter separately?"
    a: "Microsoft retired the standalone Windows Update troubleshooter download; it is now built into Settings. The legacy Control Panel version ('View all' > Windows Update) is the closest alternative, and it uses locally cached packages that bypass download corruption. Bookmark the Control Panel path for the next time the Settings version misbehaves."
---

The Windows Update troubleshooter is supposed to be the easy button — so when it will not run, crashes, or reports 'a problem is preventing the troubleshooter from starting,' you lose the simplest repair path. The troubleshooter itself depends on the Diagnostic Policy Service, the update services, and its own downloaded diagnostic packages; a failure in any of those breaks the tool rather than the update. [the Windows Update service not running](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/)

The irony is that a broken troubleshooter usually signals the same underlying damage that is breaking your updates — corrupted servicing components or disabled diagnostic services. Fixing the troubleshooter and fixing the updates are often the same job. The steps below restore the tool first, then give you the manual equivalents for everything the tool would have done.

## Why this happens

- **Diagnostic Policy Service disabled.** The troubleshooter's core dependency, often disabled by tuners. services.msc shows it clearly; set it to Automatic.
- **Corrupted troubleshooter package.** The downloaded diagnostic CAB is damaged. Clearing SoftwareDistribution forces a fresh package download.
- **Servicing stack corruption.** The same damage breaking updates also breaks the tool. The same corruption breaking updates breaks the tool too.
- **Cryptographic Services stopped.** Needed to validate the troubleshooter's packages. Set it to Automatic in services.msc.
- **Temp folder permission issues.** The troubleshooter cannot write its working files. Clear %temp% and C:\Windows\Temp as administrator.
- **Group Policy blocking diagnostics.** Policies disabling troubleshooting on Pro editions. gpedit.msc reveals the blocking policy on Pro.
- **Corrupted system files.** Damaged binaries the troubleshooter depends on. sfc /scannow repairs the binaries it needs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable the diagnostic services

The troubleshooter cannot run without its service dependencies. The troubleshooter depends on the Diagnostic Policy Service, the Diagnostic Service Host, and the update services — a failure in any of them breaks the tool instead of the update.

1. Press Win + R, type services.msc, and press Enter.
2. Set 'Diagnostic Policy Service' to Automatic and start it.
3. Set 'Diagnostic Service Host' to Manual and start it.
4. Set 'Diagnostic System Host' to Manual as well.
5. Retry the troubleshooter from Settings > System > Troubleshoot.
6. Relaunch the troubleshooter from Settings > System > Troubleshoot and confirm it now starts.

### Fix 2: Run the troubleshooter from the legacy Control Panel

The old troubleshooting framework sometimes works when the Settings version does not. Debloat and privacy tools routinely disable the Diagnostic Policy Service, which is why 'troubleshooter won't start' so often follows a debloating session.

1. Open Control Panel > Troubleshooting > View all.
2. Run 'Windows Update' from the classic list.
3. If the classic one runs, apply its fixes.
4. The classic framework uses locally cached packages instead of downloads.
5. This bypasses corrupted downloaded diagnostic packages.
6. If it runs, apply every fix it suggests and note what it found.

### Fix 3: Re-download the troubleshooter package

Clear the cached diagnostic packages so fresh ones download. [the troubleshooter on other brands](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-dell-laptop/) The Settings-based troubleshooter downloads fresh diagnostic packages, while the legacy Control Panel version uses cached ones — when one fails, try the other.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits, net stop cryptsvc.
3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old.
4. Restart the services.
5. Retry the troubleshooter — it downloads a fresh diagnostic package.
6. Try the legacy Control Panel > Troubleshooting > View all version as a cross-check.

### Fix 4: Check Cryptographic Services

Package validation fails silently when this service is down. Error 0x80070005 from the troubleshooter means access denied, usually a permissions problem in the temp folders it uses for working files.

1. In services.msc, find 'Cryptographic Services'.
2. Set it to Automatic and start it.
3. Retry the troubleshooter.
4. If it was disabled by a tuner, undo the tuner's changes.
5. This service is also required for Windows Update itself.
6. Confirm the Diagnostic Policy Service stays running after a reboot.

### Fix 5: Clear the temp folders

Permission or corruption issues in temp locations break the troubleshooter's working files. The troubleshooter is a wrapper around standard repairs — service restarts, cache clears, DLL re-registration — so its failure never blocks you from doing those repairs manually.

1. Press Win + R, type %temp%, and delete everything Windows allows.
2. Also clear C:\Windows\Temp (as administrator).
3. Restart the laptop.
4. Retry the troubleshooter.
5. Skip files Windows says are in use — those are fine.
6. Run the Windows Update troubleshooter specifically, since that is the one you need.

### Fix 6: Undo debloat tool changes

Tuners that disable diagnostics break the troubleshooter by design. Cryptographic Services must be running for the troubleshooter to validate its diagnostic packages; its failure mode is a silent troubleshooter crash.

1. Re-run any debloat or privacy tool and restore defaults.
2. Manually re-enable the diagnostic services listed above.
3. Restart and retry.
4. Avoid tools that disable the Diagnostic Policy Service.
5. The troubleshooter is exactly the kind of thing those tools sacrifice.
6. If the tool works in the new profile but not the old one, plan a profile migration.

### Fix 7: Run SFC and DISM

Repair the binaries the troubleshooter depends on. Corrupted packages in the download cache break the Settings troubleshooter specifically, which is why clearing SoftwareDistribution also fixes the tool.

1. Open Command Prompt as administrator and run: sfc /scannow.
2. Then: DISM /Online /Cleanup-Image /RestoreHealth.
3. Restart when finished.
4. Retry the troubleshooter.
5. If it still fails, the manual sequence below replaces it entirely.
6. Re-run any debloat tool's restore function and verify it no longer disables diagnostics.

## Closing

A troubleshooter that will not run is just the servicing stack telling on itself — fix the diagnostic services and you often fix the updates too. And when the wrapper will not cooperate, the manual sequence does the same repairs more thoroughly anyway. For the update problems underneath it all, [Windows 11 update failures in general](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-11/) is the main guide. For Microsoft's own documentation on these repairs, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).
