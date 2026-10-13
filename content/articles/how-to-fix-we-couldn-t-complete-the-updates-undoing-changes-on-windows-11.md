---
title: "'We Couldn't Complete the Updates, Undoing Changes' on Windows 11 — Definitive Fix Guide"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-11
date: 2026-09-17
categories: ["windows-update"]
tags: ["windows 11", "couldn't complete updates", "undoing changes", "update loop", "windows update fix"]
description: "Windows 11 keeps saying 'We couldn't complete the updates, undoing changes'? Break the loop permanently with this definitive ordered repair guide."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-11.webp"
faqs:
  - q: "What is the difference between 'undoing changes' and a failed update?"
    a: "They are two halves of one event. The update failed — the installer hit an error it could not recover from — and 'undoing changes' is the cleanup phase where Windows reverses everything the installer did. You see the second message because the first happened silently. Fixing the loop means addressing the failure cause, not the rollback, since the rollback itself is working exactly as designed."
  - q: "Why does Windows 11 retry a failed update instead of skipping it?"
    a: "Windows Update treats most failures as transient — a busy file, a network hiccup — so it retries on the next scan. That design is correct for genuinely transient failures but creates the loop when the cause is persistent, like a corrupted cache or an incompatible driver. Hiding the specific KB with the show-or-hide updates troubleshooter breaks the retry cycle while you fix the underlying problem."
  - q: "Do I need to reinstall Windows to stop the undoing changes loop?"
    a: "Almost never. A full reinstall is the last resort, and the in-place upgrade repair — which reinstalls Windows while keeping files and apps — resolves even servicing-stack damage without one. Work through the cache reset, DISM/SFC repairs, and driver updates first. Reinstall only if the in-place upgrade itself fails, which usually indicates failing hardware rather than software."
  - q: "How do I stop this from happening with future Windows 11 updates?"
    a: "Maintain the three habits that prevent most loops: keep at least 20 GB free on C:, keep drivers current from your manufacturer's support site rather than relying on Windows Update alone, and let one update finish completely before starting another. Running Disk Cleanup's system-files option monthly keeps the component store lean, and pausing updates during critical work weeks avoids badly timed feature updates."
---

"We couldn't complete the updates, undoing changes" on Windows 11 is the operating system's most honest error message: it tells you the update failed and that it is cleaning up the mess. The frustration comes from what it does not tell you — why it failed — and from the loop that follows, where Windows retries the same doomed package on every scan. This guide is the definitive path out: diagnose the failure, repair the pipeline, and prevent the encore.

Understand the architecture and the fixes make sense. Windows installs updates as transactions against the component store. Any unrecoverable error aborts the transaction, and the "undoing changes" phase plays it backwards. Your files are never at risk during this — only the update payload is reversed. The loop persists because the cause persists: a corrupted cache, a damaged store, an incompatible driver, or too little disk space will fail the package identically every time until addressed.

Start in Update history and capture the failed KB number plus the error code. That pair is your diagnostic compass for everything below. Then work the fixes in order — each one eliminates a class of cause, and most loops break by Fix 4.

## Why this happens

- **A corrupted update cache:** staged downloads that fail integrity checks abort the transaction on every retry.
- **Component store damage:** a broken WinSxS store cannot stage new components, so every install unwinds.
- **Incompatible or outdated drivers:** drivers that fail migration checks during feature updates.
- **Insufficient free disk space:** the staged update plus rollback snapshot needs 10 to 20 GB of working room.
- **Third-party security software:** kernel-level suites locking files the installer must replace.
- **Outdated BIOS/UEFI firmware:** prerequisite failures on recent Windows 11 builds.
- **Pending servicing operations:** a previous incomplete update leaving the stack inconsistent.
- **A broken update package:** occasionally the KB itself is defective for certain hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the error code and let the rollback finish

Evidence before action. The code in Update history focuses every subsequent step.

1. If the rollback screen is showing, keep the charger connected and give it 30 to 60 minutes, watching the disk light.
2. On the desktop, open Settings, then Windows Update, then Update history.
3. Record the failed KB number and error code — 0x800f0922, 0x80070002, 0x80070003, and 0x80070103 are the common ones.
4. Search the code on Microsoft's [update support pages](https://support.microsoft.com/en-us/windows) for its documented meaning.
5. If the machine will not boot past the rollback, start with our [frozen rollback recovery guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2/).

### Fix 2: Run the Windows Update troubleshooter

The automated pass that clears stuck services, bad metadata, and misregistered components.

1. Open Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply every fix it suggests.
3. Restart the laptop.
4. Check for updates. If the troubleshooter refuses to run, the [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) has the manual procedure.

### Fix 3: Reset the SoftwareDistribution and catroot2 caches

The single most effective repair for repeat identical failures — a poisoned cache guarantees a poisoned retry.

1. Open Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the four services and reboot.
5. Run Windows Update and let it rebuild the cache from scratch.

### Fix 4: Repair the component store with DISM and SFC

When the store is damaged, nothing stages — repair the foundation before retrying.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait 10 to 30 minutes for it to complete.
3. Run `sfc /scannow` and let it verify protected system files.
4. Reboot and retry the update.
5. If DISM cannot complete, run it a second time — the first pass often repairs the servicing stack enough for the second to succeed.

### Fix 5: Update drivers and firmware from the manufacturer

Driver migration failures are the top cause of feature-update rollbacks — eliminate them at the source.

1. Visit your laptop manufacturer's support site and download current chipset, graphics, Wi-Fi, and storage drivers for your exact model.
2. Check for a BIOS/UEFI update and install it with the charger connected.
3. In Device Manager, resolve any device showing a warning icon before retrying.
4. Prefer manufacturer drivers over Windows Update's offerings for core hardware.
5. Retry the feature update after the driver stack is current.

### Fix 6: Free space and eliminate interference

Two environmental causes, minutes to rule out.

1. Confirm at least 20 GB free on C:; run Disk Cleanup as administrator with system-files options.
2. Disconnect all USB peripherals, docks, and SD cards.
3. Temporarily disable third-party antivirus (Windows Security stays on) and disconnect VPNs.
4. Retry the update in this clean state.
5. If one KB remains the sole failure, hide it with the show-or-hide updates troubleshooter.

### Fix 7: In-place upgrade repair

The definitive servicing-stack rebuild — Windows reinstalled over itself, files and apps kept.

1. Back up important files as a matter of habit.
2. Download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Mount the ISO, run setup.exe, and choose "Keep personal files and apps."
4. Allow 30 to 90 minutes for the upgrade.
5. Verify clean entries in Update history afterward.

## Closing

The undoing-changes loop on Windows 11 is almost always one of four things — cache, store, drivers, or space — and this guide addresses them in the order of likelihood. Capture the error code, work the list, and resist the urge to retry blindly between steps: every blind retry is just another rollback. Fix the cause once, and updates go back to being the boring background process they are supposed to be.
