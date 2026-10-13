---
title: "Windows Update Error 0x800704c7, Step by Step: Stop the Cancel Loop"
slug: how-to-fix-windows-update-error-0x800704c7-step-by-step
date: 2026-10-04
categories: ["windows-update"]
tags: ["0x800704c7", "windows update error", "update keeps failing", "windows 11", "windows 10"]
description: "Error 0x800704c7 means Windows Update was cancelled mid-operation. This step-by-step walkthrough restarts the update pipeline, clears stuck downloads, and repairs the services that keep stopping."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800704c7-step-by-step.webp"
faqs:
  - q: "What causes error 0x800704c7 in Windows Update?"
    a: "The code means an operation was cancelled by the system. In practice, a Windows Update service stopped or crashed during the update, a background transfer job stalled, or security software interrupted the installer. It is a process interruption, not a corrupted file, which is why service resets fix it so reliably."
  - q: "Does 0x800704c7 mean I cancelled the update myself?"
    a: "Almost never. Users rarely trigger this code directly. It is called a cancellation because Windows frames a service crash or forced stop the same way it frames a user pressing cancel. If you did not touch anything during the update, treat it as a service or interference problem."
  - q: "Why does the error come back after a restart?"
    a: "Because the underlying trigger survives restarts — typically a stuck BITS transfer job, a service configured to start manually instead of automatically, or an antivirus rule that fires every time the updater runs. The fixes here address the persistent trigger, not just the symptom."
  - q: "Is it safe to reset the BITS queue?"
    a: "Yes. The BITS queue holds background download jobs for Windows Update and a few other services. Resetting it discards partially downloaded data that Windows will simply re-download on the next check. Nothing user-created is stored in the queue."
---

Error 0x800704c7 is Windows Update's way of saying "I stopped, but I will not tell you why." Technically the code means the operation was cancelled. Since you almost certainly did not cancel it, the real question is what pulled the plug: a service that crashed, a transfer job that jammed, or a security product that stepped in at the wrong moment. This guide treats the error as a pipeline problem and rebuilds the pipeline one section at a time, in an order that wastes none of your time.

Work through the steps sequentially. The early fixes take minutes and resolve the majority of cases; the later ones handle stubborn, recurring cancellations. Keep the laptop on AC power throughout — power-saving states that suspend background services are one of the quieter causes of this exact code, and the [HP-specific variant of this fix](/articles/how-to-fix-windows-update-error-0x800704c7-on-hp-laptop/) covers that angle in more depth for HP owners.

It helps to understand what Windows means by "cancelled" here. The update engine does not distinguish between you pressing cancel, a service crashing, and a security product killing the installer process \u2014 all three look identical from the engine's perspective, and all three produce 0x800704c7. That is why the fixes focus on the pipeline's moving parts rather than anything you did. Somewhere in the chain from download to install, a link broke, and the engine reported the break the only way it knows how.

## Why this happens

- **Windows Update service stops unexpectedly:** The wuauserv service crashes or gets stopped by another process mid-update, and the engine reports the whole operation as cancelled.
- **BITS service stalls:** Background Intelligent Transfer Service handles the actual downloading. If it hangs, the update has nothing to install and aborts.
- **Stuck BITS transfer jobs:** Damaged or orphaned download jobs clog the transfer queue. New downloads cannot proceed past them, and the operation times out as a cancellation.
- **Antivirus or firewall interference:** Security software that treats update payloads as suspicious can terminate the installer process, which Windows reads as a cancelled operation.
- **Corrupt update cache:** Partially downloaded files in the SoftwareDistribution folder confuse the installer into aborting the operation partway through.
- **Metered connection cutting the download:** If Windows decides the connection is metered mid-download, it can halt the transfer — a behavior explored further in the guide on [metered connections blocking Windows Update](/articles/how-do-i-fix-metered-connection-blocking-windows-update/).
- **Conflicting third-party updaters:** Manufacturer utilities and driver tools that run their own update routines can lock files or restart services that Windows Update depends on.
- **Damaged system files in the update stack:** Corrupted components in the servicing stack itself cause the update engine to fail its own pre-flight checks and abort.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter first

The automated tool catches the simple cases: stopped services, misconfigured settings, minor cache damage.

1. Press Win + I, then go to System, Troubleshoot, Other troubleshooters.
2. Click Run next to Windows Update.
3. Apply every fix it recommends, even if the description sounds unrelated.
4. Restart the laptop and check for updates.

### Fix 2: Restart the update services manually

If the troubleshooter did not stick, restart the services by hand so you can see their actual state.

1. Press Win + R, type `services.msc`, and press Enter.
2. Locate Windows Update. If it is not running, right-click and choose Start; if it is running, choose Restart.
3. Do the same for Background Intelligent Transfer Service.
4. Double-click each service and confirm the Startup type is Automatic (Windows Update) or Automatic/Delayed Start (BITS).
5. Retry the update from Settings.

### Fix 3: Reset the BITS transfer queue

Stuck jobs are a classic cause of recurring 0x800704c7.

1. Open an elevated Command Prompt (search "cmd", right-click, Run as administrator).
2. Run `bitsadmin /reset /allusers` and wait for confirmation.
3. Also clear per-user jobs with `bitsadmin /reset` if the first command reports jobs it could not touch.
4. Retry the update.

### Fix 4: Clear the SoftwareDistribution cache

1. In the elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Open C:\Windows\SoftwareDistribution in File Explorer and delete everything inside it.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Restart the laptop, then check for updates so Windows rebuilds a clean cache.

### Fix 5: Temporarily disable third-party security software

1. Open your antivirus or firewall suite and disable real-time protection temporarily.
2. Run Windows Update to completion.
3. Re-enable protection immediately.
4. If the update only succeeds with protection off, add Windows Update processes to the suite's exclusion list rather than disabling protection every month.

### Fix 6: Repair the update stack with SFC and DISM

1. In an elevated Command Prompt, run `sfc /scannow` and let it finish.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
3. Restart and retry the update.
4. If DISM reports it cannot find source files, rerun it while connected to a stable network — it downloads clean components from Windows Update itself.

### Fix 7: Reset Windows Update components completely, then install manually

1. Run the full component reset: stop wuauserv, bits, cryptsvc, and msiserver; rename SoftwareDistribution and catroot2 folders; restart all four services. (The `net stop` / `net start` pattern from Fix 4 applies, adding `msiserver` to the list.)
2. Restart the laptop.
3. If the error persists, identify the failing KB in Update history and install it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) as a standalone package.
4. For general update guidance and official troubleshooting paths, the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) documents these component resets as well.

### Fix 8: Check the Windows Update log for the smoking gun

When the error keeps returning, the log often names the exact failure point.

1. Open an elevated PowerShell and run `Get-WindowsUpdateLog` to generate a readable log on your desktop.
2. Open the generated file and search for 0x800704c7 or the word "cancel".
3. Look at the timestamps around the failure \u2014 the lines just before it usually identify which service stopped or which process interfered.
4. If a third-party process appears repeatedly at the failure moment, you have found your culprit; update, reconfigure, or remove it.

## Closing

The 0x800704c7 loop breaks the moment you find which part of the pipeline keeps getting interrupted \u2014 usually a crashed service or a jammed BITS queue, occasionally a background program with strong opinions. Because the fixes are cumulative and non-destructive, there is no penalty for working the whole list, including the log analysis in Fix 8: each step leaves the system cleaner than it found it. Once the update completes, watch the next Patch Tuesday cycle; if the error never returns, you have found and fixed the real trigger, not just quieted a symptom.
