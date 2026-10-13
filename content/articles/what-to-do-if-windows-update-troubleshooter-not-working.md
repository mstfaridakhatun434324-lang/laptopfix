---
title: "Windows Update Troubleshooter Not Working? Fix the Fixer"
slug: what-to-do-if-windows-update-troubleshooter-not-working
date: 2026-09-10
categories: ["windows-update"]
tags:
  - "windows update"
  - "troubleshooter not working"
  - "diagnostics"
  - "windows 11"
description: "When the Windows Update troubleshooter itself fails to run or finds nothing, the diagnostic layer is broken. Here is how to repair the troubleshooter and get real diagnostics back."
thumbnail: "/images/thumbs/what-to-do-if-windows-update-troubleshooter-not-working.webp"
faqs:
  - q: "Why won't the Windows Update troubleshooter even start?"
    a: "The troubleshooter depends on the Diagnostic Policy Service, Background Intelligent Transfer Service, and the msdt/diagnostics framework. If those services are disabled, or the troubleshooter's own packages are corrupted, clicking Run does nothing or throws an error immediately. Restoring those services, as shown in Fix 1, resolves most launch failures."
  - q: "What does it mean when the troubleshooter finds no problems but updates still fail?"
    a: "It means the failure mode is outside the troubleshooter's checklist — deeper servicing corruption, a poisoned download cache it cannot clear, or a policy block. The troubleshooter covers common cases, not all cases; the manual steps below pick up where it stops."
  - q: "Can I download the troubleshooter separately?"
    a: "Microsoft retired the standalone downloadable troubleshooters; the current versions live in Settings under System, then Troubleshoot. There is no official separate download anymore, so be wary of third-party sites offering troubleshooter downloads — they are often bundled with junk, so stick to the built-in Settings version rather than third-party downloads."
  - q: "Is there an alternative diagnostic when the troubleshooter is broken?"
    a: "Yes. The manual service reset, SFC/DISM scans, and the update log (via PowerShell Get-WindowsUpdateLog) all diagnose without the troubleshooter. This guide walks each of them in the order a technician would use. You are never truly without diagnostic options."
---

There is a particular irony in the tool designed to fix Windows Update being broken itself. You click Run next to Windows Update in the troubleshooters list and nothing happens — or it spins forever, or it cheerfully reports no problems while updates keep failing. Now you have two problems: the original update failure and a dead diagnostic tool.

The troubleshooter is not magic; it is a scripted package that depends on services, system files, and a diagnostics framework. When any of those are damaged, the troubleshooter fails exactly like any other program would. The fix is to repair its dependencies, then repair the troubleshooter's own packages.

This guide works bottom-up: restore the services the troubleshooter needs, repair the system files behind it, reset the update engine manually (which is what the troubleshooter would have done), and verify with alternative diagnostics. For the normal case where the troubleshooter runs fine, see our [guide to using the troubleshooter well](/articles/how-to-fix-windows-update-with-troubleshooter-on-laptop/).

## Why this happens

- **Diagnostic Policy Service disabled:** the troubleshooter framework requires this service, and optimizers love to disable it.

- **BITS not running:** the Background Intelligent Transfer Service underpins both updates and their diagnostics.

- **Corrupted troubleshooter packages:** the scripted diagnostic packages in System32 can be damaged like any system file.

- **Broken msdt associations:** the legacy diagnostic host registration can break, so the troubleshooter never launches.

- **Cryptographic Services failure:** signature validation for the diagnostic packages fails when cryptSvc is damaged.

- **Group Policy blocks:** on managed or tweaked systems, policy can disable the troubleshooting framework entirely.

- **Deeper servicing corruption:** when the component store is damaged, everything built on it — including diagnostics — misbehaves.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restore the services the troubleshooter needs

The troubleshooter cannot run on a broken foundation. These three services are its hard dependencies, and setting them back to their defaults fixes the majority of dead-troubleshooter cases.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find Diagnostic Policy Service — set Startup type to Automatic and start it.
3. Find Background Intelligent Transfer Service — set to Manual (Trigger Start) and start it.
4. Find Cryptographic Services — set to Automatic and start it.
5. Retry the Windows Update troubleshooter from Settings.

### Fix 2: Repair system files with SFC and DISM

Corrupted diagnostic packages and framework files are system files like any other. SFC restores the troubleshooter's own components, and DISM repairs the store SFC draws from.

1. Open Terminal (Admin) from the Start right-click menu.
2. Run `sfc /scannow` and wait for 100 percent completion.
3. Restart, then run `DISM /Online /Cleanup-Image /RestoreHealth` in a new admin terminal.
4. Allow up to 30 minutes, then restart again.
5. Test the troubleshooter once more before moving on.

### Fix 3: Do manually what the troubleshooter would have done

While repairing the diagnostic tool, do not let the original update problem wait. This manual reset performs the troubleshooter's core repairs directly, no diagnostic framework required.

1. In Terminal (Admin), run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Reboot and run Check for updates.
5. Many users find the original update problem resolved even before the troubleshooter is fixed.

### Fix 4: Re-register the diagnostic components

The troubleshooter's script packages register with the system like COM components. Re-registering the key diagnostic DLLs repairs launch failures where clicking Run does nothing at all.

1. Open Terminal (Admin).
2. Run `regsvr32 msdtcprx.dll` and approve the prompt (repeat for any failures).
3. Run `sfc /scannow` once more to catch stragglers the re-registration exposed.
4. Restart the laptop.
5. Open Settings, System, Troubleshoot, Other troubleshooters, and try the Run button again.

### Fix 5: Check for policy blocks on diagnostics

Tweakers and some managed setups disable scripted diagnostics via policy. If the troubleshooter option is greyed out or vanishes, policy is the prime suspect.

1. Press Win + R, type `gpedit.msc` (Windows 11 Pro), and press Enter.
2. Navigate to Computer Configuration, Administrative Templates, System, Troubleshooting and Diagnostics.
3. Ensure nothing here is set to Disabled for scripted diagnostics.
4. On Home edition, check Settings, Privacy and security for disabled diagnostic data options.
5. Undo any tweaker tool's changes to diagnostics, then retest.

### Fix 6: Use the update log as an alternative diagnostic

You do not actually need the troubleshooter to diagnose. The Windows Update log records every operation with error codes, and reading the tail of it often names the failure directly.

1. Open Terminal (Admin) and run `Get-WindowsUpdateLog` in PowerShell.
2. Open the generated WindowsUpdate.log on your Desktop.
3. Scroll to the bottom and look for error codes near the most recent timestamps.
4. Search the web for the exact code plus your symptom for targeted fixes.
5. Our [update error code reference](/articles/how-to-fix-windows-update-error-0x80070005-step-by-step/) guide helps interpret the common codes.

### Fix 7: Run an in-place upgrade as the final repair

When both the troubleshooter and the servicing stack resist repair, an in-place upgrade reinstalls Windows over itself — fixing the diagnostic framework, the update engine, and system files together while keeping your files and apps.

1. Back up important files first, even though this preserves them.
2. Download the Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Mount the ISO (double-click it) and run setup.exe.
4. Choose Keep personal files and apps when prompted.
5. Let the upgrade complete; both the troubleshooter and updates should work afterward.

## Closing

A broken troubleshooter is a dependency problem, not a mystery: restore its services, repair its files, and do its job manually in the meantime. And remember the log-file alternative — you were never truly without diagnostics. Work the list in order and both the tool and the updates it serves will be back in action.
