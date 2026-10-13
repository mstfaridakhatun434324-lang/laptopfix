---
title: "Fix Error 0x80080005 on Windows 10: When the Update Service Will Not Start"
slug: how-to-fix-windows-update-error-0x80080005-on-windows-10
date: 2026-10-10
categories: ["windows-update"]
tags: ["windows update", "0x80080005", "windows 10", "update service", "server execution failed"]
description: "Windows 10 update error 0x80080005 means the update engine failed to launch. Here is the ordered repair, from service restarts to a full in-place refresh."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80080005-on-windows-10.webp"
faqs:
  - q: "What is Windows Update error 0x80080005 on Windows 10?"
    a: "It means the COM-based update engine failed to start — server execution failed. The causes are local: wedged services, broken DLL registrations, corrupted system files, or interference from third-party software, not your internet connection. Because the fault is local, every effective fix in this guide runs on your machine."
  - q: "Why does Windows Update show the error immediately?"
    a: "Because the failure happens at engine startup, before any download begins. Windows tries to activate the update components, activation fails, and the error surfaces right away instead of after a long download. That immediacy is actually helpful: it points straight at services and registrations."
  - q: "Should I disable my antivirus to fix 0x80080005?"
    a: "Temporarily disabling it for testing is reasonable, since some suites hook the update components. But do not leave protection off — if disabling helps, update or replace the suite rather than running unprotected. Note the exact suite version too, since only certain builds hook the update engine."
  - q: "The troubleshooter did not fix it. What next?"
    a: "Move to the manual steps: force-restart the services, re-register the update DLLs, clear the SoftwareDistribution cache, and run DISM plus SFC. Our [Windows 11 version of this fix](/articles/how-to-fix-windows-update-error-0x80080005-on-windows-11/) follows the same logic with Windows 11 menu paths."
---

There is something almost honest about error 0x80080005: Windows 10 does not waste your time pretending to download. The moment you ask for updates, it reports that the update engine itself could not start. Server execution failed is the technical phrasing, and it tells you exactly where to look — inside the laptop, at the services and registrations that make up the update machinery.

The repair follows the machine's own startup sequence in reverse. First make sure the services can actually run, then make sure their COM registrations are intact, then clear any corrupt state they choke on, and finally repair the system files underneath. It is methodical work, but each step takes only minutes, and the fix rate is high because the failure is so localized. If driver updates specifically are the ones failing on this machine, our [driver update failure guide](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) addresses that narrower problem.

Test Windows Update after each fix. Stop as soon as the page scans normally — there is no prize for running the whole list.

## Why this happens

- **Services stuck mid-transition**: wuauserv caught between stopping and stopped blocks every new launch attempt.
- **Unregistered update DLLs**: Lost COM registrations after crashes, bad shutdowns, or overzealous cleaning tools.
- **Corrupt service executables or dependencies**: Damaged files the engine loads at startup.
- **Third-party hooks**: Driver utilities and security tools that inject into system services.
- **Destroyed update cache**: A SoftwareDistribution folder damaged badly enough to crash initialization.
- **Low disk space**: Staging-space checks failing at engine startup.
- **Pending reboot deadlocks**: A reboot pending for weeks can leave the servicing stack in a state that refuses new sessions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter

Begin with automation. On Windows 10 the troubleshooter specifically probes whether the update services start correctly, and its repairs cover the most common wedged states.

1. Go to Settings > Update & Security > Troubleshoot > Additional troubleshooters.
2. Run the Windows Update troubleshooter and apply everything it recommends.
3. Restart the laptop fully — use Restart, not Shut down, to clear fast-startup state.
4. Open Windows Update and check whether the error is gone.

### Fix 2: Force-restart the stuck services

The Services console sometimes cannot stop a wedged service because the control request itself hangs. The command line can kill the underlying process and start fresh, which breaks the deadlock.

1. Open an elevated Command Prompt.
2. Run sc queryex wuauserv to find the PID if it is stuck, then taskkill /f /pid <PID>, or simply taskkill /f /fi "SERVICES eq wuauserv".
3. Run net stop bits and net stop cryptSvc, then net start wuauserv, net start bits, and net start cryptSvc.
4. Test Windows Update immediately.

### Fix 3: Delete the damaged download cache

A cache corrupted at the structural level can crash the service during its startup scan. Renaming the folder is safe and forces a clean rebuild.

1. In an elevated Command Prompt, run net stop wuauserv and net stop bits.
2. Run ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
3. Run net start wuauserv and net start bits.
4. Reboot, then open Windows Update — the first scan will take several minutes.

### Fix 4: Re-register the update components

This is the core fix for server execution failures. The update engine's DLLs must be registered for COM activation; re-registering them rebuilds those entries from scratch.

1. In an elevated Command Prompt, run regsvr32 wuapi.dll, regsvr32 wuaueng.dll, regsvr32 wups.dll, regsvr32 wups2.dll, and regsvr32 wuwebv.dll one by one.
2. Add regsvr32 msxml3.dll, regsvr32 jscript.dll, and regsvr32 qmgr.dll for the helper libraries.
3. Reboot the laptop.
4. Check for updates again.

### Fix 5: Run DISM and SFC repairs

If registrations keep breaking or the engine still will not start, the underlying files are likely damaged. DISM repairs the component store, SFC repairs protected system files against it.

1. Run DISM /Online /Cleanup-Image /RestoreHealth in an elevated Command Prompt.
2. When it completes, run sfc /scannow.
3. Restart the laptop after both finish.
4. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) afterward for any servicing stack update you might have missed, and install it.

### Fix 6: Test in a clean boot

Third-party software that loads at startup can intercept the update engine's launch. A clean boot removes all non-Microsoft services from the equation and tells you definitively whether something external is interfering.

1. Press Windows + R, type msconfig, go to the Services tab, tick Hide all Microsoft services, and click Disable all.
2. Restart into the clean-boot state and test Windows Update.
3. If the error is gone, re-enable services in groups to find the culprit.
4. Update, reconfigure, or uninstall the offending program, then return msconfig to normal startup.

### Fix 7: Clear the pending-reboot deadlock

A reboot that has been pending for weeks — from an old update, an installer, or a driver — can leave the servicing stack refusing to start new engine sessions. Clearing the pending state breaks the deadlock without the risks of forcing anything.

1. Check for a pending reboot: in regedit, look at HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager for PendingFileRenameOperations.
2. Simply restart the laptop properly (Start > Power > Restart) and let it fully settle for ten minutes.
3. If the pending state survives reboots, run dism /online /cleanup-image /startcomponentcleanup to resolve stuck servicing operations.
4. Reboot once more, then test Windows Update.
### Fix 8: Do an in-place upgrade repair

The last resort for an engine that will not start is refreshing the Windows installation itself. An in-place upgrade keeps your files, apps, and settings while replacing every system file, which rebuilds the update stack completely.

1. Download the Windows 10 ISO from Microsoft on the laptop itself.
2. Mount the ISO and run setup.exe.
3. Select Keep personal files and apps at the prompt.
4. Let the repair complete (usually 30 to 90 minutes), then verify Windows Update scans cleanly.

## Closing

On Windows 10, 0x80080005 is a startup problem wearing an update code's clothing, and startup problems answer to restarts, registrations, and repairs — in that order. Most machines are fixed by the forced service restart or the DLL re-registration; the deeper file repairs exist for the ones that are not. Whatever fixed it, finish with a full successful update cycle before declaring victory, because an engine that starts but cannot complete still needs attention. The same engine-startup repair for Windows 11 is in our [0x80080005 Windows 11 guide](/articles/how-to-fix-windows-update-error-0x80080005-on-windows-11/).
