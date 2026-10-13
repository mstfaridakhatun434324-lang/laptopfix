---
title: "How to Fix the Windows Update Troubleshooter Not Working on Windows 10"
slug: "how-to-fix-windows-update-troubleshooter-not-working-on-windows-10"
date: 2026-09-04
categories: ["windows-update"]
tags: ["troubleshooter", "windows update", "windows 10", "not working"]
description: "Windows Update troubleshooter not working on Windows 10? Six manual fixes that replicate the troubleshooter’s repairs and restore the tool itself."
thumbnail: "/images/thumbs/how-to-fix-windows-update-troubleshooter-not-working-on-windows-10.webp"
faqs:
  - q: "Where is the troubleshooter on Windows 10?"
    a: "Open Settings, then Update and Security, then Troubleshoot, then Additional troubleshooters, and click Run the troubleshooter under Windows Update. If nothing happens or it errors immediately, the diagnostic services or the troubleshooter packages themselves need repair — the manual steps in this guide perform the same repairs the tool would attempt."
  - q: "Did a debloat script break my troubleshooter?"
    a: "Very often, yes. Windows 10 “debloat” and privacy scripts commonly disable the Diagnostic Policy Service and related services to reduce background activity, which breaks every built-in troubleshooter while leaving the rest of the system seemingly fine. Re-enabling those three diagnostic services in services.msc is the single most common fix for troubleshooters that will not run on Windows 10."
  - q: "Is there a downloadable troubleshooter for Windows 10?"
    a: "Yes — the downloadable wushowhide-independent “Windows Update Troubleshooter” diagcab is deprecated, and the MSDT platform behind the old .diagcab troubleshooters is retired. Use the built-in path under Settings, then Update and Security, then Troubleshoot. If the built-in tool fails, the manual component reset and DISM repairs here are the supported fallback."
  - q: "Will fixing Windows Update fix the troubleshooter too?"
    a: "Frequently. The corruption that breaks Windows Update often damages the troubleshooter packages too, since they share the servicing infrastructure. After a manual component reset and a DISM restore-health pass, users commonly find the troubleshooter launches and completes normally again — the repairs fix both the patient and the doctor in one pass."
---

On Windows 10 the troubleshooter lives at Settings > Update & Security > Troubleshoot > Additional troubleshooters — and on many systems it simply does nothing when you click Run. The usual suspect is not mysterious: years of “debloat” scripts and aggressive optimizers have trained a generation of Windows 10 users to disable exactly the diagnostic services the troubleshooter needs.

The Windows 11 incarnation of this problem has its own guide at the [Windows 11 troubleshooter fix](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-windows-11/). On Windows 10, though, the repair path leans harder on service restoration and the old, reliable manual component reset.

## Why this happens

- **Legacy troubleshooter components damaged:** Windows 10’s troubleshooters depend on older diagnostic packages; years of updates can leave their registrations broken.
- **Diagnostic services disabled by optimization tools:** The classic cause on Windows 10: “debloat” scripts disable the Diagnostic Policy Service, silently killing all troubleshooters.
- **Corrupted update components beyond script repair:** The troubleshooter runs fixed scripts; deep cache or store corruption they cannot handle makes the tool report failure.
- **Permissions damage blocking repairs:** ACL damage on update folders stops the troubleshooter’s repair steps with access-denied errors it cannot explain.
- **Outdated Windows 10 build with old troubleshooter:** On builds far behind on cumulative updates, the troubleshooter version predates current update mechanisms and mishandles them.
- **Security software blocking the tool’s actions:** Antivirus products may block the service restarts and file deletions the troubleshooter attempts, making it look broken.
- **Corrupted user profile:** A damaged profile can prevent the Settings-based troubleshooter page from launching the tool at all.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly how the troubleshooter fails

Pin down the failure mode first. No-launch points to disabled diagnostic services or broken tool registration; runs-but-cannot-fix points to corruption deeper than the scripts handle. The manual path replaces the tool either way.

1. Go to Settings > Update & Security > Troubleshoot > Additional troubleshooters.
2. Click Windows Update, then Run the troubleshooter, and observe precisely: no launch, instant error, or runs-but-fails.
3. Record any error text — it narrows the failing layer.
4. Continue with manual repairs regardless of the outcome.

### Fix 2: Re-enable the diagnostic services (the classic fix)

This is the number-one fix on Windows 10, full stop. Optimization scripts disable these services aggressively, and without them no troubleshooter can run. Restoring them takes two minutes and resolves the majority of “troubleshooter won’t start” cases.

1. Press Win + R, type services.msc, and press Enter.
2. Locate Diagnostic Policy Service, Diagnostic Service Host, and Diagnostic System Host.
3. Set each Startup type to Automatic and start any that are stopped.
4. Retry the troubleshooter immediately.

### Fix 3: Perform the troubleshooter’s repair manually

This manual sequence is the heart of what the Windows Update troubleshooter does. Performing it by hand bypasses the broken tool entirely and delivers the identical repair — it is the most honest “troubleshooter replacement” available.

1. Run Command Prompt as administrator.
2. Stop: net stop wuauserv, net stop bits, net stop cryptSvc, net stop msiserver.
3. Rename: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart all four services with net start.

### Fix 4: Repair the layers beneath with DISM and SFC

When corruption runs deeper than the cache — damaged manifests, broken system files — the troubleshooter’s scripts fail and the tool reports defeat. DISM and SFC repair the layers beneath the scripts, which is exactly what the tool cannot do for itself.

1. Open an elevated Command Prompt.
2. Run: DISM /Online /Cleanup-Image /RestoreHealth until it completes.
3. Run: sfc /scannow.
4. Restart and test both the updates and the troubleshooter.

### Fix 5: Test from a new user profile

Profile corruption can block the Settings-hosted troubleshooter from initializing. A fresh-profile test takes five minutes and cleanly separates a profile problem (migrate) from a system problem (repair the system).

1. Create a new local administrator: Settings > Accounts > Family & other users > Add someone else.
2. Sign in as the new user.
3. Launch the troubleshooter from the new profile.
4. If it works there, migrate to the new profile; repairing the old one is rarely worth the effort.

### Fix 6: Update the build or repair-install Windows

Ancient builds carry ancient troubleshooters. Bringing the build current updates the troubleshooter packages themselves, and an in-place upgrade rebuilds the entire diagnostic platform when nothing else works.

1. Check for pending cumulative updates and install them — newer builds carry fixed troubleshooter packages.
2. If updates will not run at all, install the latest cumulative manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. As a last resort, run an in-place upgrade using Windows 10 installation media to rebuild all system tooling.
4. Verify the troubleshooter runs on the repaired system.

### Fix 7: Repair the Settings app that hosts the troubleshooter

On Windows 10 the troubleshooter runs inside the Settings app’s infrastructure; if the Settings app package itself is damaged, the troubleshooter cannot launch no matter how healthy the diagnostic services are. Symptoms include Settings pages that crash or the Troubleshoot page showing blank. Re-registering the Settings-related packages — the same class of fix described for Dell systems in the [Dell troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-dell-laptop/) — restores the host the tool needs.

1. Open PowerShell as administrator.
2. Re-register the immersive control panel: Get-AppxPackage -AllUsers *immersivecontrolpanel* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}.
3. Restart the laptop.
4. Open Settings > Update & Security > Troubleshoot and confirm the page loads fully.
5. Run the Windows Update troubleshooter from the repaired host.

## Closing

On Windows 10, a non-working troubleshooter is usually collateral damage from the same optimization scripts and corruption behind the update failure itself. Re-enable the diagnostic services, perform the component reset by hand, and repair the servicing base — you will have done everything the troubleshooter would have done, and it will likely work again afterward.
