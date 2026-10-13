---
title: "Best Way to Fix 'Windows Update Says Undoing Changes Made to Your Computer'"
slug: best-way-to-fix-windows-update-says-undoing-changes-made-to-your-computer
date: 2026-09-18
categories: ["windows-update"]
tags: ["undoing changes", "windows update fix", "best fix", "update rollback", "windows 11"]
description: "Looking for the best, most reliable way to fix the 'Undoing changes made to your computer' loop? Here is the technician-approved sequence that works."
thumbnail: "/images/thumbs/best-way-to-fix-windows-update-says-undoing-changes-made-to-your-computer.webp"
faqs:
  - q: "What is the single best fix for the undoing changes loop?"
    a: "There is no single fix, because the loop has several distinct causes — but the highest-yield sequence is: let the rollback finish, reset the SoftwareDistribution cache, repair the store with DISM and SFC, and update drivers from the manufacturer. That four-step run resolves the overwhelming majority of cases. Skipping straight to drastic measures like reinstalling Windows wastes time when the cause is usually a corrupt cache."
  - q: "How long should I try fixes before giving up and reinstalling?"
    a: "Work the full ordered sequence first — it takes about two hours including the DISM scan and an in-place upgrade repair. Only consider a clean reinstall if the in-place upgrade itself fails, which points to hardware trouble rather than software. Most people who jump to reinstalling discover the loop was a 15-minute cache reset away from fixed."
  - q: "Why do forum fixes for this error contradict each other?"
    a: "Because different causes produce the identical screen. A cache reset fixes corrupted downloads but does nothing for a driver conflict; a driver update fixes migration failures but not store damage. Contradictory advice usually means each poster fixed their own distinct cause. The ordered sequence in this guide works because it eliminates causes by likelihood instead of guessing."
  - q: "Is the undoing changes loop a sign my laptop is too old?"
    a: "Not necessarily, but age raises the odds. Older laptops accumulate WinSxS bloat, vendors stop updating their drivers, and aging drives develop errors — all rollback triggers. If the loop recurs after a full repair sequence, check drive health with SMART data before blaming age. A fresh SSD in an old laptop often ends update troubles permanently."
---

Everyone wants the single best fix for "Windows Update says undoing changes made to your computer." Here is the honest technician's answer: the best fix is not a trick — it is a sequence. The screen is identical for half a dozen different causes, so the method that actually works is eliminating those causes in order of likelihood, verifying after each step, and stopping the moment updates flow again. This guide is that sequence, refined to the minimum steps that resolve the maximum cases.

The logic is simple. Roughly half of these loops are a corrupted update cache. Of the remainder, most are component-store damage, driver migration failures, or disk space. The sequence below attacks them in exactly that order, which means the average case resolves in under an hour without ever touching the drastic options. Each fix includes a verification step so you know when to stop.

Before starting: if the rollback screen is currently showing, give it 30 to 60 minutes on AC power with an eye on the disk light. A working rollback needs no fix at all — only a frozen one does.

## Why this happens

- **Corrupted update cache (most common):** bad staged downloads failing integrity checks on every retry.
- **Damaged component store:** WinSxS corruption preventing any package from staging.
- **Driver migration conflicts:** OEM or outdated drivers failing the update's migration checks.
- **Insufficient disk space:** the update plus its rollback snapshot needs 10 to 20 GB.
- **Security software interference:** kernel-level suites locking files during installation.
- **Outdated firmware:** BIOS prerequisites silently failing on newer Windows builds.
- **A defective update package:** occasionally Microsoft's own KB is broken for specific hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the failure details and finish the rollback

The best sequence starts with information, not action.

1. Let any in-progress rollback finish — 30 to 60 minutes on AC power, disk light as your guide.
2. On the desktop, open Update history and record the failed KB and error code.
3. Look up the code on Microsoft's [update support pages](https://support.microsoft.com/en-us/windows) — it often names the cause directly.
4. If the machine is frozen on the rollback screen, begin with the [frozen rollback recovery guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2/) instead.
5. Do not retry the update yet — blind retries just produce blind rollbacks.

### Fix 2: Reset the update cache — the highest-yield single step

This one fix resolves more undoing-changes loops than everything else combined. Do it first among the active repairs.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the four services with `net start` and reboot.
5. Run Windows Update and check: if the previously failing package now installs, you are done — stop here.

### Fix 3: Repair the component store with DISM and SFC

If the loop survived the cache reset, the store itself is the next most likely culprit.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait 10 to 30 minutes — do not interrupt it.
3. Run `sfc /scannow` and let verification complete.
4. Reboot, then retry Windows Update.
5. Verify in Update history. If the troubleshooter side of things also looks broken, see the [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/).

### Fix 4: Update drivers and BIOS from the manufacturer

Driver migration failures are the leading cause of feature-update rollbacks specifically.

1. Download current chipset, graphics, Wi-Fi, and storage drivers from your laptop manufacturer's support site for your exact model.
2. Install any available BIOS/UEFI update with the charger connected.
3. Clear any yellow warning icons in Device Manager before retrying.
4. Retry the Windows update.
5. If a single driver package from Windows Update keeps failing, hide it with the show-or-hide updates troubleshooter.

### Fix 5: Free disk space and remove interference

The quick environmental sweep that costs minutes and fixes a real share of cases.

1. Ensure at least 20 GB free on C: via Disk Cleanup's system-files options.
2. Disconnect USB peripherals and docks.
3. Temporarily disable third-party antivirus and disconnect VPNs.
4. Retry the update in this clean state.
5. Re-enable security software afterward.

### Fix 6: Run the Windows Update troubleshooter as a verification pass

By this point the troubleshooter serves as a second opinion — catching anything the manual steps missed.

1. Go to Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its findings.
3. Restart and check for updates one more time.
4. A clean troubleshooter run plus a clean manual sequence means the pipeline is healthy.

### Fix 7: In-place upgrade repair — the definitive reset

When every targeted repair fails, rebuild the servicing stack wholesale while keeping everything.

1. Download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO, run setup.exe, choose "Keep personal files and apps."
3. Allow 30 to 90 minutes.
4. Confirm clean Update history afterward.
5. If even this fails, check drive health — persistent failure past this point is a hardware signal, per our [drive-health guidance](/articles/what-to-do-if-windows-update-says-undoing-changes-made-to-your-computer/).

## Closing

The "best way" to fix the undoing-changes loop was never a secret registry key — it is discipline: diagnose with the error code, reset the cache, repair the store, refresh the drivers, and verify at each step. That sequence fixes the vast majority of cases in about an hour, and it tells you exactly when you have reached the point where hardware, not software, is the answer. Boring, methodical, effective — the way all good repairs work.
