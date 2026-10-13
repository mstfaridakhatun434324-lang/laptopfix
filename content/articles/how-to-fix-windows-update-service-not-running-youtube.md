---
title: "Windows Update Service Not Running? Restart It the Right Way"
slug: how-to-fix-windows-update-service-not-running-youtube
date: 2026-09-26
categories: ["windows-update"]
tags: ["wuauserv", "service not running", "windows update", "services"]
description: "Windows Update fails because its service isn't running? Learn why wuauserv stops, how to restart it properly, and how to keep it healthy."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-not-running-youtube.webp"
faqs:
  - q: "What does 'Windows Update service not running' mean?"
    a: "It means the wuauserv background service — the engine that scans for, downloads, and installs updates — is stopped or disabled. Without it, Settings shows errors like 0x80070422 and no update check can run. The service should normally start automatically whenever Windows needs it."
  - q: "Why does the Windows Update service keep stopping by itself?"
    a: "Common causes include corrupted update components that crash the service on start, third-party 'optimizer' tools that disable it, Group Policy or registry settings forcing it off, and malware that kills update services to avoid removal. Identifying which one applies determines the lasting fix."
  - q: "Is it safe to set wuauserv to Automatic startup?"
    a: "Yes — Automatic (or Automatic Delayed Start) is the healthy default. Setting it to Disabled is what breaks updates. If something keeps reverting your setting to Disabled, that's a red flag for a debloater script, a domain policy, or malware, and you should investigate rather than just re-enabling it."
  - q: "Error 0x80070422 means the service isn't running — how do I fix it?"
    a: "Error 0x80070422 is the classic symptom. Open services.msc, find Windows Update, set Startup type to Automatic, and start it. If it stops again immediately, the service is crashing on launch — work through the component reset and malware checks in this guide to fix the underlying cause."
---

# Windows Update Service Not Running? Restart It the Right Way

You click "Check for updates" and instead of the usual scan you get an error — 0x80070422, or a blunt message that the service isn't running. The Windows Update service (`wuauserv`) is the engine room of the whole update system, and when it's stopped, nothing else in the update pipeline can function. No scans, no downloads, no installs.

Restarting the service takes ten seconds. Keeping it running is the actual challenge, because a service that won't stay started is telling you something is wrong underneath — corrupted components, a policy forcing it off, or software fighting it. This guide covers both: the immediate restart done properly, and the detective work that keeps it alive.

## Why this happens

- **Corrupted update components crash the service.** Damaged DataStore or cache files can make wuauserv fail seconds after starting.
- **Third-party "optimizer" or debloater tools.** Many such tools disable wuauserv as a "tweak," breaking updates as a side effect.
- **Group Policy or registry settings.** Domain-joined PCs or old tweaks can force the service to Disabled.
- **Malware disabling updates.** Some malware kills update services deliberately to avoid being removed by security patches.
- **Failed updates leaving the service in a bad state.** An interrupted install can leave locks that prevent clean startup.
- **Dependency services stopped.** wuauserv depends on RPC and DCOM services; if those are damaged, it can't start.
- **Disk errors in the servicing areas.** Corruption in WinSxS or the update cache can crash the service during initialization.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the Service Properly via Services Console

Do the restart the right way — with the correct startup type, not just a blind start.

1. Press Win + R, type `services.msc`, and press Enter.
2. Scroll to **Windows Update**, double-click it to open properties.
3. Set **Startup type** to **Automatic** (not Manual, not Disabled).
4. Click **Start** if the service status shows Stopped, then click OK.
5. Also verify its companions: **Background Intelligent Transfer Service** (BITS) set to Automatic/Manual and running, and **Cryptographic Services** running. Then retry **Check for updates** in Settings.

### Fix 2: Start It from an Elevated Command Prompt

If the Services console gives an access error, the command line often succeeds — and it reveals useful error messages.

1. Open an elevated Command Prompt (search "cmd", right-click, **Run as administrator**).
2. Run `net start wuauserv` and read the output carefully — "service started successfully" versus a specific error code changes everything.
3. If you see error 1058 (disabled), the startup type is the problem — fix it with `sc config wuauserv start= auto` (note the space after `=`).
4. If you see error 1053 or 1067, the service is crashing on launch — skip to Fix 4 for the component reset.
5. After a successful start, run `wuauclt /detectnow` on older systems or just click **Check for updates** in Settings to confirm the pipeline works.

### Fix 3: Check Group Policy and Registry Overrides

Something may be forcing the service off behind your back — find it and remove it.

1. Press Win + R, type `gpedit.msc` (Windows Pro) and navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update**.
2. Look for **Configure Automatic Updates** — if it's Disabled in a way you didn't set, a domain policy or old tweak is responsible.
3. Check the registry: open `regedit` and go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv` — the **Start** value should be `2` (Automatic) or `3` (Manual), never `4` (Disabled).
4. If a domain policy controls the PC, talk to your IT admin rather than fighting the policy locally — it will just reapply.
5. On personal PCs, remove any "disable updates" tweaks from optimizer tools before proceeding — they'll undo your fix within days otherwise.

### Fix 4: Reset Windows Update Components

A service that starts then immediately dies is crashing on corrupted data — clear the wreckage.

1. Open an elevated Command Prompt.
2. Stop everything: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Rename the data stores:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`.
5. Try **Check for updates** — with clean data stores, the service should start and stay running. Our full [component reset walkthrough](/articles/how-to-reset-windows-update-components-on-windows-10/) covers additional steps if this partial reset isn't enough.

### Fix 5: Scan for Malware That Kills Update Services

If the service was running fine and suddenly won't stay up, suspect hostile software.

1. Run a full scan with Windows Defender: **Settings > Privacy & Security > Windows Security > Virus & threat protection > Scan options > Full scan**.
2. Also run the free Microsoft Safety Scanner for a second opinion — some malware specifically targets wuauserv and hides from single-engine scans.
3. Check Task Scheduler for suspicious tasks that stop services: **Task Scheduler Library** — look for tasks running `net stop` commands you didn't create.
4. Review recently installed programs in **Settings > Apps** for anything you don't recognize, especially "optimizers" and "driver updaters."
5. After cleaning, repeat Fix 4's component reset — malware often corrupts the update stores on its way out.

### Fix 6: Repair System Files with SFC and DISM

When the service binaries or their dependencies are damaged, no restart trick will hold.

1. Open an elevated Command Prompt.
2. Run `sfc /scannow` and let it complete — it repairs protected system files including service executables.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` for component store damage SFC can't reach.
4. Restart the laptop after both complete.
5. Set wuauserv to Automatic and start it once more — on a repaired system it should now stay up. If the troubleshooter also misbehaves, our guide on [fixing the update troubleshooter itself](/articles/how-do-i-fix-windows-update-troubleshooter-not-working/) is the next stop.

### Fix 7: Check Disk Health and Event Logs

Persistent service crashes can be the first symptom of a failing drive or a deeper system problem.

1. Open **Event Viewer > Windows Logs > System** and filter for errors from the **Service Control Manager** around the times wuauserv died — the details often name the failing module.
2. Run `chkdsk C: /f` from an elevated prompt and reboot to let it check the drive.
3. If Event Viewer shows disk errors alongside service crashes, back up your data immediately — a dying drive explains everything.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has current guidance on service recovery if you need official documentation for IT.
5. As a final measure, an in-place upgrade using the [Windows 11 ISO](https://www.microsoft.com/en-us/software-download/windows11) reinstalls all system services while keeping files and apps — the definitive fix for service damage that resists repair.

## Closing

A Windows Update service that won't run is either misconfigured or damaged — rarely mysterious once you check. Set it to Automatic, clear the corrupted components it's choking on, remove whatever keeps disabling it, and verify the disk underneath is healthy. Do that, and wuauserv goes back to its quiet, reliable self.
