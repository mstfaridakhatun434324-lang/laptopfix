---
title: "Fix TiWorker High CPU on a Lenovo Laptop"
slug: "how-to-fix-tiworker-high-cpu-on-lenovo-laptop"
date: 2026-09-17
categories: ["performance"]
tags: ["tiworker.exe", "high cpu", "lenovo laptop", "windows update", "windows modules installer"]
description: "TiWorker.exe pinning your Lenovo laptop's CPU at 100%? Learn what this Windows process does and how to stop it looping, with safe servicing-stack repairs."
thumbnail: "/images/thumbs/how-to-fix-tiworker-high-cpu-on-lenovo-laptop.webp"
faqs:
  - q: "What is TiWorker.exe and is it a virus?"
    a: "TiWorker.exe is the Windows Modules Installer Worker, a legitimate Microsoft process that installs Windows updates, enables optional features, and maintains system components. The real file lives in C:\\Windows\\WinSxS and is digitally signed by Microsoft. Malware occasionally impersonates the name, so verify the file location in Task Manager before worrying — if it runs from anywhere other than WinSxS, treat it as suspicious and scan immediately."
  - q: "How long should TiWorker.exe normally run?"
    a: "During active update installation, TiWorker can legitimately use high CPU for 20 to 60 minutes while it processes component changes, especially after a feature update. That is normal and you should let it finish. It becomes a problem when it runs at high CPU for many hours, across reboots, with no update ever completing — that pattern means the servicing stack is stuck and needs the repairs described in this guide."
  - q: "Can I just end TiWorker.exe in Task Manager?"
    a: "You can end it, but it usually restarts within minutes because the underlying update task is still queued — killing the process treats the symptom, not the cause. Worse, interrupting it mid-install can corrupt the component store and make the next attempt take even longer. The reliable approach is to let pending updates complete or to repair the servicing stack with DISM and SFC, which addresses why TiWorker is looping."
  - q: "Why is TiWorker worse on Lenovo laptops?"
    a: "It is not TiWorker itself but the context: Lenovo laptops run Lenovo Vantage, ImController services, and scheduled update tasks alongside Windows Update, so the servicing stack competes for CPU and disk with Lenovo's own background work. Outdated Lenovo system drivers can also stall the update process TiWorker is trying to complete. Updating drivers through Lenovo Vantage or the [Lenovo support site](https://support.lenovo.com/us/en/) often unblocks the loop."
---
TiWorker.exe — the Windows Modules Installer Worker — is supposed to be a behind-the-scenes process. It installs Windows updates, adds optional features, and keeps the component store healthy. But on many Lenovo laptops it gets stuck: CPU sits at 50 to 100 percent for hours, the fan never rests, and no update ever seems to finish.

The frustration is that ending the process does not help. TiWorker is launched by the TrustedInstaller service whenever the servicing stack has work queued, so it simply comes back. The loop almost always means one of three things: an update is genuinely still installing, the component store is corrupted, or a driver conflict keeps failing the installation silently.

This guide walks through the correct order of operations: verify it is legitimate, give real work time to finish, then repair the servicing stack from the least invasive method to the most. Lenovo-specific angles — Vantage, system drivers, and BIOS updates — are covered too, since they frequently unblock the loop. For the parent process behind TiWorker, see our [Windows Modules Installer guide](/articles/how-to-fix-windows-modules-installer-high-cpu-in-windows-11-24h2/).

## Why this happens

- **A feature update genuinely installing:** TiWorker legitimately uses heavy CPU for 30–60 minutes while processing a Windows 11 feature update.

- **Corrupted component store (WinSxS):** damaged servicing metadata makes TiWorker retry the same operations endlessly.

- **Stuck Windows Update queue:** a failed cumulative update leaves the servicing stack in a half-finished state that TiWorker keeps revisiting.

- **Conflicting Lenovo drivers:** outdated chipset, storage, or management engine drivers can silently fail the update TiWorker is applying.

- **Pending .NET or optional feature changes:** enabling Windows features queues servicing work that runs at high priority.

- **Interrupted previous update:** a forced shutdown during an update leaves the component store inconsistent.

- **Third-party antivirus locking system files:** aggressive real-time scanning can block TiWorker's file operations, causing retries.

- **Low disk space on C::** servicing operations need several gigabytes of scratch space; without it, they fail and loop.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it is legitimate and give real work time

Before repairing anything, confirm the process is genuine and not simply mid-installation. Interrupting a real update is the fastest way to turn a slow afternoon into a corrupted component store.

1. In Task Manager's Details tab, right-click TiWorker.exe and choose Open file location.
2. Confirm it opens inside C:\Windows\WinSxS — anything else is malware until proven otherwise.
3. Check Settings > Windows Update: if an update shows as installing, give it up to 90 minutes on AC power.
4. Make sure the laptop is plugged in and set to never sleep during this window (Settings > System > Power & battery).
5. Only proceed to repairs if TiWorker is still burning CPU hours later with no update progressing.

### Fix 2: Run the Windows Update troubleshooter

The built-in troubleshooter resets the update pipeline's state — clearing stuck download jobs and re-registering components — which is often enough to let TiWorker finish and exit. Microsoft documents this flow on its [Windows support site](https://support.microsoft.com/en-us/windows).

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Click Run next to Windows Update and let it complete fully.
3. Apply every repair it offers, even if the descriptions sound generic.
4. Restart the laptop when prompted, then check for updates again.
5. Watch Task Manager for 20 minutes: TiWorker should spike briefly during real work, then settle.

### Fix 3: Repair the component store with DISM

DISM repairs the servicing stack itself — the exact machinery TiWorker runs on. When the component store is corrupted, this is the definitive fix, and it is safer than any registry edit.

1. Open Command Prompt as administrator (search cmd, right-click, Run as administrator).
2. Run DISM /Online /Cleanup-Image /ScanHealth first to check for damage without changing anything.
3. If it reports corruption, run DISM /Online /Cleanup-Image /RestoreHealth and wait — this takes 10–30 minutes.
4. Do not close the window or shut down while it runs; interrupted DISM can worsen corruption.
5. When it completes successfully, restart and observe whether TiWorker stays quiet.

### Fix 4: Follow up with System File Checker

DISM repairs the store that SFC draws from, so running SFC afterward catches protected system files that TiWorker may have damaged during its looping. The two tools are designed to be used as a pair.

1. In the same elevated Command Prompt, run sfc /scannow.
2. Wait for the verification to reach 100 percent — typically 10–20 minutes on a laptop SSD.
3. If it reports that it repaired files, restart the laptop.
4. If it reports corruption it could not fix, repeat the DISM RestoreHealth step, then run SFC once more.
5. Check Task Manager after the reboot to confirm TiWorker is idle.

### Fix 5: Reset the Windows Update components manually

When the update queue itself is wedged, clearing the SoftwareDistribution and catroot2 caches forces Windows to rebuild them cleanly. This stops TiWorker from re-reading the same broken queue on every boot.

1. Open Command Prompt as administrator.
2. Stop the services: net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver (one per line).
3. Rename the caches: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the services with net start wuauserv, net start cryptSvc, net start bits, net start msiserver.
5. Restart the laptop, check for updates, and let the fresh queue process normally.

### Fix 6: Update Lenovo system drivers and BIOS

Lenovo-specific stalls are common: an outdated storage or chipset driver can fail the very update TiWorker is trying to install, creating the loop. Lenovo Vantage or the official support site has the correct packages for your exact model.

1. Open Lenovo Vantage and run a system update check, installing all critical driver updates.
2. Pay special attention to chipset, storage (IRST/RST), and Intel Management Engine drivers.
3. Check for a BIOS update in Vantage as well — apply it only on AC power with the battery above 50 percent.
4. Alternatively, download drivers for your serial number from the [Lenovo support site](https://support.lenovo.com/us/en/).
5. Restart after driver updates and give Windows Update one clean attempt to finish.

### Fix 7: Free disk space and check drive health

Servicing operations need working room — several gigabytes on C: — and a failing drive can make every TiWorker operation time out and retry. Both are quick to rule out.

1. Open Settings > System > Storage and ensure at least 15–20 GB is free on C:; run Cleanup recommendations if not.
2. Empty the Recycle Bin and remove the Windows.old folder if a previous upgrade left one behind.
3. Open Command Prompt as administrator and run chkdsk C: /scan to check the file system online.
4. Check the SSD's health in Lenovo Vantage or your SSD vendor's toolbox app.
5. If the drive reports warnings, back up immediately — no servicing repair can fix failing hardware.

## Closing

TiWorker high CPU is the servicing stack telling you it cannot finish its job — not a process to kill, but a queue to clear. Verify it is legitimate, let genuine updates complete, then repair with DISM and SFC, reset the update components, and bring Lenovo drivers current. Worked through in order, these steps resolve the loop on the overwhelming majority of Lenovo laptops without ever touching a clean install. If update problems keep recurring more broadly, our [post-24H2 update repair guide](/articles/how-to-fix-windows-11-slow-after-24h2-update-on-lenovo-laptop/) covers the wider update-failure playbook.
