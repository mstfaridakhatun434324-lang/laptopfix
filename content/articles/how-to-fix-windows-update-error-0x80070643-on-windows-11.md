---
title: "Fix Windows Update Error 0x80070643 on Windows 11 (Install Failed)"
slug: how-to-fix-windows-update-error-0x80070643-on-windows-11
date: 2026-09-21
categories: ["windows-update"]
tags: ["windows update", "0x80070643", ".net framework", "defender", "windows 11"]
description: "Windows 11 error 0x80070643 means an update failed to install — often .NET Framework or Defender. Diagnose the failing update and fix it with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070643-on-windows-11.webp"
faqs:
  - q: "Why does 0x80070643 happen mostly with .NET updates?"
    a: "Because .NET cumulative updates install via the Windows Installer engine on top of the existing .NET runtime. When that runtime carries corrupted registrations or damaged assemblies — typical after interrupted updates or aggressive cleaners — the installer sees the broken baseline and aborts with ERROR_INSTALL_FAILURE. Microsoft's repair tool restores the baseline so the update can land."
  - q: "Is error 0x80070643 dangerous for my system?"
    a: "Not by itself. The code means one update failed to install — your Windows 11 system keeps running on the previous, working state. The danger is indirect: while the failed update sits uninstalled, its security fixes stay missing. Repair the failing component promptly, but treat it as a job to do, not an emergency."
  - q: "Can I just hide the failing update?"
    a: "You can, but keep hiding as a last resort, not a solution — especially for .NET and Defender updates that carry security content. Hiding is defensible as a stopgap while you set up the real repair, or when Microsoft has acknowledged a bad update and you are waiting for the corrected package."
  - q: "Why does the .NET update fail but everything else installs?"
    a: "Because only the .NET update exercises the damaged .NET runtime. Other updates touch different components and install fine — which is diagnostically handy: selective failure points squarely at the .NET installation rather than at Windows Update itself. Run the .NET Repair Tool before adjusting any servicing-wide settings."
---

Code 0x80070643 is Windows Installer's way of saying ERROR_INSTALL_FAILURE — an update's installation died partway through. Windows 11 users meet it most often with .NET Framework cumulative updates and Defender definition updates, and its most annoying trait is anonymity: the code never says which component choked. So the work always begins with detective work — finding the exact update that failed.

"Fatal" sounds terminal, but it rarely is. These failures normally surrender to targeted repairs: fixing .NET, refreshing definitions manually, or restoring a clean servicing state. Identify the failing update first, then apply the matching repair below.

When the identical fatal error appears on your other machine, [the Windows 10 edition](/articles/how-to-fix-windows-update-error-0x80070643-on-windows-10/) covers that OS; if the symptom is an installer that hangs rather than erroring, [the 0x8024200d companion guide](/articles/how-to-fix-windows-update-error-0x8024200d-on-windows-11/) is the relevant read. Start by naming the culprit.

## Why this happens

- **The .NET Framework underneath is damaged.** This code is the classic signature of .NET cumulative updates layered over a corrupt runtime. The installer recognizes the broken baseline and aborts instead of patching over damage.
- **A Defender definition update ran into a scan.** Defender intelligence updates throw this code during an active full scan, while definitions are mid-download, or when third-party AV contests Defender's update path.
- **The Installer engine is wedged from a previous run.** An interrupted MSI installation can jam the Windows Installer service, so the next update that uses the engine fails instantly and fatally.
- **Servicing folder permissions are wrong.** When SYSTEM or TrustedInstaller lose write access to servicing folders — often the aftermath of aggressive permission-tweaking utilities — installers cannot stage files and die fatally.
- **A poisoned package in the cache.** A damaged .msu or payload inside SoftwareDistribution fails at apply time rather than download time, which yields 0x80070643.
- **Third-party antivirus murdered the installer.** Suites that intercept MSI operations can terminate an update's installer mid-flight; Windows reports the kill as fatal.
- **A reboot is pending.** Some updates refuse to install while another operation awaits restart — the installer bails out fatally rather than queuing politely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Name the failing update

0x80070643 is generic, so the update's identity selects the repair: .NET updates need the .NET repair, Defender updates need the definition path, and everything else needs the servicing fixes. Guessing wastes time — look it up instead.

1. Open Settings > Windows Update > Update history and find the entry flagged Failed with 0x80070643.
2. Classify it: .NET Framework update, Defender intelligence update, or something else.
3. Launch `perfmon /rel` from Win + R and study Reliability Monitor for the matching critical event with its full details.
4. Copy the KB number somewhere safe — the manual-install fallback needs it.
5. Continue with the repair that matches your culprit.

### Fix 2: Repair the .NET Framework

A failing .NET rollup usually means the runtime beneath it is damaged. Microsoft's .NET Framework Repair Tool detects and fixes the standard corruptions — missing registrations, broken policies, damaged assemblies — and afterward the cumulative update installs normally.

1. Fetch the Microsoft .NET Framework Repair Tool; [the Windows support hub](https://support.microsoft.com/en-us/windows) guidance pages point to it.
2. Launch it, accept the license, and let it examine the installed .NET versions.
3. Apply every recommended repair, rebooting when asked.
4. Go back to Settings > Windows Update and retry — install the .NET update alone first to confirm.
5. Still failing? Remove the newest .NET update via Update history, restart, and try again.

### Fix 3: Update Defender definitions by hand

For the Defender flavor, sidestep the stalled automatic path: pull a definition update directly from Windows Security or via the MpCmdRun command-line tool. A manual definition refresh dodges whatever servicing state the automatic attempt tripped on.

1. In Windows Security, open Virus & threat protection > Protection updates and select Check for updates.
2. If that fails, launch an administrator Command Prompt.
3. The command-line alternative is `"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -SignatureUpdate`.
4. Wait for the success message, then restart.
5. Verify under Protection updates that the intelligence version is current.

### Fix 4: Flush pending operations and rebuild the cache

Fatal install errors sometimes come from leftover debris: pending.xml operations waiting on a reboot, or a poisoned package sitting in SoftwareDistribution. Clearing both gives the next attempt a clean runway instead of the previous attempt's wreckage.

1. Reboot the laptop (Start > Power > Restart) to drain simple pending operations.
2. Launch an administrator Command Prompt.
3. Halt the services: `net stop wuauserv`, then `net stop bits`.
4. Rename the cache with `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`, then start both services again.
5. Retry the failed update from Settings > Windows Update.

### Fix 5: Retry from a clean boot

When third-party software ambushes installers mid-flight, a clean boot removes the ambusher. This shines for the .NET flavor of 0x80070643, where antivirus filters and utilities interfere with the MSI engine's file work.

1. Press Win + R, enter `msconfig`, and hit Enter.
2. Under the Services tab, tick Hide all Microsoft services and choose Disable all.
3. Turn off all startup items via Task Manager's Startup tab.
4. Restart, then install the update through Settings > Windows Update.
5. Use `msconfig` to restore normal startup afterward, then reboot once more.

### Fix 6: Install the KB yourself

The ultimate bypass: download the exact KB package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and run it personally. The standalone installer ignores the automatic pipeline's state completely, so it wins in many cases where Windows Update keeps failing with 0x80070643.

1. Enter your KB number in the search box on [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Download the build matching your architecture and OS version.
3. Shut down other programs, then double-click the .msu to install.
4. Reboot when prompted.
5. Run a standard update check to confirm the failure vanished from history.

### Fix 7: Rebuild the Windows Installer registration

Sometimes the engine — not the update — is at fault: a corrupt msiexec registration makes every MSI-based update fail identically. Unregistering and re-registering reconstructs its configuration and clears the wedged state. This pays off most when several unrelated updates fail with 0x80070643.

1. Launch an elevated Command Prompt.
2. Execute `msiexec /unregister`; it returns silently.
3. Execute `msiexec /regserver` to reconstruct the registration.
4. Restart so the fresh registration loads.
5. Attempt the failed update again from Settings > Windows Update.

## Closing

0x80070643 rewards investigation: name the failing update, repair that one component — the .NET runtime, the Defender definitions, or the servicing state — and the fatal error usually gives up. Hold the manual Catalog install in reserve for the stubborn cases. On Windows 11, a healthy underlying runtime brings back the silent background rollups — which is how updates should behave.
