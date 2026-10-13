---
title: "Cumulative Update Fails Every Time? Full Troubleshooting Guide"
slug: "cumulative-update-fails-every-time-troubleshooting"
date: "2026-09-14"
categories: ["windows-update"]
tags: ["windows update", "cumulative update", "troubleshooting", "error codes"]
description: "A complete troubleshooting walkthrough for laptops where every cumulative update fails. Diagnose the root cause with logs and error codes, then apply targeted fixes."
thumbnail: "/images/thumbs/cumulative-update-fails-every-time-troubleshooting.webp"
faqs:
  - q: "How do I find the real error code when updates fail?"
    a: "Open Settings, go to Windows Update, and click Update history to see the exact error code next to each failed update. For deeper detail, open Event Viewer, navigate to Windows Logs then System and Setup, and filter for events from the Windows Update Client around the failure time. The CBS.log file in C colon backslash Windows backslash Logs backslash CBS also records servicing failures with specific error codes."
  - q: "What do the most common update error codes mean?"
    a: "Code 0x80070002 means the update files are missing or corrupted, usually fixed by clearing the cache. Code 0x80070005 is an access denied error pointing to permissions problems. Code 0x800f0900 indicates component store corruption needing DISM repair. Code 0x80240034 means the download was interrupted. Each code narrows the diagnosis, which is why recording it before troubleshooting matters."
  - q: "Can a failing hard drive cause every update to fail?"
    a: "Yes, a deteriorating SSD or hard drive with bad sectors can corrupt update files as they are written, causing every cumulative update to fail verification. If you also see random file corruption, crashes, or extremely slow disk performance, check the drive health with your manufacturer's diagnostic or the command wmic diskdrive get status. Replace a failing drive before continuing update troubleshooting."
  - q: "Should I use the Update Assistant or Media Creation Tool instead?"
    a: "The Windows 11 Installation Assistant and Media Creation Tool from https://www.microsoft.com/en-us/software-download/windows11 can install feature updates when Windows Update fails, but they are less useful for monthly cumulative updates. For cumulative updates, the Microsoft Update Catalog standalone packages are the better bypass. Use the Assistant or Media Creation Tool when feature updates specifically refuse to install."
---
Troubleshooting a laptop where every cumulative update fails requires a different mindset than fixing a single bad patch. A single failure might be a flaky download; a repeating pattern means the update subsystem itself is unhealthy. This guide teaches you to diagnose like a technician: gather the error codes, read the logs, identify the failure phase, and then apply the fix that matches your diagnosis instead of guessing.

The diagnostic discipline matters because the fixes differ. A cache problem needs a cache reset, a permissions problem needs permission repair, and component store corruption needs DISM. Applying the wrong fix wastes an hour and teaches you nothing. Spend ten minutes on diagnosis first, and the repair usually becomes obvious.

We will start by capturing exactly what is failing and where, using update history, Event Viewer, and log files. Then we will map common error codes to their meanings and work through targeted repairs in order. If you prefer a straight fix list without the diagnostic depth, our [best-way repair sequence](/articles/best-way-to-fix-cumulative-update-fails-every-time/) covers the same ground in action order.

## Why this happens

- **Persistent cache corruption:** The SoftwareDistribution folder accumulates damage across months of failed attempts.
- **Component store degradation:** The servicing stack deteriorates over time, breaking every cumulative image assembly.
- **Broken service configuration:** Update-related services stuck in disabled or error states halt all progress.
- **Permission drift:** Access control changes on system folders block the installer from writing files.
- **Failing storage hardware:** Bad sectors corrupt update payloads as they are staged.
- **Driver and firmware staleness:** Outdated low-level drivers fail each new build's readiness checks.
- **Policy or registry interference:** Misconfigured group policies or tweaking tools can paralyze the update engine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the error code and failure phase

Good troubleshooting starts with evidence. Record exactly what fails and when before changing anything.

1. Open Settings, Windows Update, Update history, and note each failed KB with its error code.
2. Observe whether failures happen during download, installation, or the restart phase.
3. Check if the failure percentage is consistent, which hints at a specific file or phase.
4. Write down the codes; 0x80070002, 0x80070005, and 0x800f0900 are the most common.
5. Note any pattern across months, such as failures starting after a specific date.

### Fix 2: Read the Event Viewer and CBS logs

Logs turn a vague failure into a specific cause. The update client logs its errors with useful detail.

1. Open Event Viewer and go to Windows Logs, System.
2. Filter for Source equal to Microsoft-Windows-WindowsUpdateClient around failure times.
3. Check Windows Logs, Setup for servicing errors during the install phase.
4. Open C:\Windows\Logs\CBS\CBS.log and search for "Failed" near the failure timestamp.
5. Match what you find to the error code meanings to pick your repair.

### Fix 3: Run the Windows Update troubleshooter

With diagnosis in hand, start repairs with the automated tool. It fixes service states, registrations, and common misconfigurations quickly.

1. Go to Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply all fixes.
3. Restart the laptop.
4. Retry the update and compare the result to your baseline.

### Fix 4: Reset the update components and clear the cache

Eliminate cache corruption and wedged services in one thorough reset.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Restart the services with `net start` and reboot.
6. Check for updates and watch whether the failure phase changes.

### Fix 5: Check disk health and free space

Rule out storage as the systemic cause, since bad sectors and full drives break every update identically.

1. Run `wmic diskdrive get status` in Command Prompt and confirm all drives report OK.
2. Check free space on C: in Settings, System, Storage.
3. Run Disk Cleanup as administrator and clear update and temporary files.
4. Ensure at least 15 GB is free before retrying.
5. If the drive reports errors, run your manufacturer's full diagnostic.

### Fix 6: Repair permissions and the component store

Address access-denied errors and servicing corruption with the heavyweight repairs.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` to 100 percent.
3. Run `sfc /scannow` and wait for verification to finish.
4. Restart the laptop.
5. Retry the cumulative update and check the logs for a clean run.

For error-specific guidance, see our articles on [0x80070005](/articles/how-to-fix-windows-update-error-0x80070005-after-windows-11-update/) and [0x80070002](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/).

### Fix 7: Install manually from the Catalog as a bypass

If the service path remains broken after repairs, sideload the update to confirm the system itself is healthy.

1. Identify the failing KB number from update history.
2. Download the x64 .msu from https://www.catalog.update.microsoft.com.
3. Install it by double-clicking and restart when prompted.
4. Verify success in Update history.
5. If manual install works but automatic keeps failing, the service configuration needs deeper repair.

### Fix 8: Generate and analyze the WindowsUpdate.log

The readable update log often reveals the precise failure that generic troubleshooting misses. PowerShell can convert Windows 11's internal update telemetry into a plain-text log on your desktop in under a minute. Searching it for your failure timestamps shows which phase aborted and frequently names the responsible file or driver. This turns the final stretch of troubleshooting from guesswork into evidence-based repair, which is exactly what you need when the standard fixes have all been tried.

1. Open PowerShell as administrator.
2. Run `Get-WindowsUpdateLog` and wait for the desktop log file to appear.
3. Open WindowsUpdate.log and search for "error" or "failed" near your last attempt time.
4. Identify the failing component, file path, or driver name in those entries.
5. Take targeted action: update the named driver, repair the named file, or research the exact error.
6. Retry the update and generate a fresh log to confirm a clean run.

## Closing

Systematic troubleshooting beats random fix attempts every time: capture the error code, read the logs, identify the failure phase, and apply the matching repair. Most repeating cumulative update failures resolve at the cache reset or the DISM repair stage once you know which one your evidence points to. Keep an eye on update history going forward so the next problem gets caught at the first failure instead of the tenth.
