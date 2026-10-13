---
title: "'We Couldn't Complete the Updates, Undoing Changes' — Troubleshooting"
slug: we-couldn-t-complete-the-updates-undoing-changes-troubleshooting
date: 2026-09-08
categories: ["windows-update"]
tags: ["undoing changes", "couldn't complete updates", "update rollback", "windows 11"]
description: "Stuck on 'We couldn't complete the updates, undoing changes'? Understand the rollback and fix the underlying failure so the next update succeeds."
thumbnail: "/images/thumbs/we-couldn-t-complete-the-updates-undoing-changes-troubleshooting.webp"
faqs:
  - q: "What does 'We couldn't complete the updates, undoing changes' mean?"
    a: "Windows attempted to install updates, hit a failure it could not recover from, and is now rolling back to the pre-update state. It is a safety mechanism, not a crash — the system is restoring the last known-good configuration."
  - q: "How long does 'undoing changes' take?"
    a: "Typically 15–45 minutes, sometimes longer on slow drives. The rollback has to reverse everything the update staged. Let it finish uninterrupted — powering off during the rollback is the main way this turns into a real problem. Patience during the rollback is the cheapest insurance in all of Windows troubleshooting."
  - q: "Will I lose files during 'undoing changes'?"
    a: "No. The rollback only reverses system files, drivers, and update payloads. Personal files, installed apps, and settings are preserved. It restores the system state, not a blank slate. The rollback touches only the Windows system directories and the driver store, leaving your user profile completely alone."
  - q: "Why does it happen on every update?"
    a: "A recurring rollback means a persistent blocker: a driver that fails migration every time, a corrupt component store, or a hardware issue like a failing drive. The rollback protects you each time, but the underlying cause needs fixing or every update will roll back."
---

'We couldn't complete the updates, undoing changes' is Windows at its most protective — and its most frustrating. The update failed, Windows caught the failure, and now it is carefully reversing everything it did. The good news hidden in the annoyance: your system is intact. The rollback exists precisely so a bad update cannot strand you.

The critical mistake is treating the rollback as the problem. It is the symptom. Something — a driver, a corrupt store, a disk error — made the update uninstallable, and until that cause is fixed, every future update will take the same round trip: attempt, fail, undo.

This guide covers surviving the rollback safely, then diagnosing the underlying failure so the next attempt succeeds. If you want the condensed best-practice sequence rather than the full diagnostic, see the [best way to fix undoing changes](/articles/best-way-to-fix-we-couldn-t-complete-the-updates-undoing-changes/).

## Why this happens

- **Driver migration failure:** A driver that cannot migrate to the new build aborts the install; the rollback then restores the old driver set.
- **Component store corruption:** Damage in WinSxS prevents the update from staging, failing the install before it meaningfully starts.
- **Third-party antivirus interference:** AV products hooking system files can cause the update's file operations to fail validation.
- **Disk errors:** Bad sectors in the update staging area corrupt payloads, failing integrity checks mid-install.
- **Insufficient disk space:** The update needs room for both the new files and the rollback data; without it, the install aborts.
- **Corrupt update cache:** A damaged download fails verification during installation, triggering the rollback.
- **Firmware or BIOS incompatibility:** Outdated firmware failing the new build's hardware checks during the install phase.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish — do not interrupt it

The single most important step. An interrupted rollback is how machines end up unbootable.

1. Leave the machine plugged in and walk away for up to an hour.
2. Do not hold the power button, do not unplug, do not 'fix' it mid-rollback.
3. When it finishes, the machine boots to the previous Windows normally — that is success, not failure.

### Fix 2: Identify which update rolled back and why

The rollback erases its own evidence quickly, so capture the details now.

1. Go to Settings → Windows Update → Update history and find the failed update with its error code.
2. Note the KB number and whether it was a quality (cumulative) or feature update.
3. Check Reliability Monitor (search 'reliability') for the failure timestamp and any driver failures logged alongside it.

### Fix 3: Clear the corrupt cache that caused the failure

A damaged download is the most common rollback trigger and the easiest to eliminate.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
4. Restart the services, reboot, and retry the update.

### Fix 4: Repair the component store

When rollbacks recur, the store is the prime suspect. Fix it before the next attempt.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt.
2. Follow with `sfc /scannow` and reboot.
3. Retry the update. If DISM fails, the store damage is severe — consider the manual Catalog install path.

### Fix 5: Remove the usual blockers before retrying

Drivers and security software cause a large share of rollbacks. Strip them for the retry.

1. Uninstall third-party antivirus temporarily (Windows Security takes over).
2. Disconnect peripherals: docks, printers, USB drives, SD cards.
3. Update BIOS, chipset, and storage drivers from the manufacturer's support site.
4. Retry the update in this clean state.

### Fix 6: Install the update manually from the Catalog

Manual installation bypasses the Windows Update client's state, which is sometimes the actual problem.

1. Find the KB number from Fix 2.
2. Download the matching package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Install the MSU directly and reboot.
4. If the manual install also rolls back, the problem is in the system (store, driver, disk) rather than the update client — keep diagnosing rather than retrying.

### Fix 7: Check drive health when rollbacks keep recurring

A failing drive corrupts staged payloads, producing identical rollbacks on every attempt.

1. Run `chkdsk C: /f /r` and reboot to let it complete.
2. Check SMART data with the manufacturer's diagnostics.
3. If the drive is failing, replace it before fighting updates further — no software fix survives bad sectors.
4. For the deeper service-level repair sequence, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official escalation path.

### Fix 8: Read the rollback logs to name the failing component

The rollback leaves detailed logs identifying what failed and when. Reading them converts the next attempt from hopeful guessing into a targeted strike on the actual culprit.

1. Enable hidden files, then open `C:\$WINDOWS.~BT\Sources\Panther\setuperr.log` and read the final errors before the rollback began.
2. Note any .sys driver files, package names, or phase codes (like 0x20017) in those entries.
3. Open `setupact.log` in the same folder and search for 'rollback' to find the exact trigger point and the operation that failed.
4. Address the named component directly — update or uninstall its driver, or clear the named package — then retry.
5. Save copies of both logs; if the next attempt fails differently, comparing the two proves you are making progress rather than looping.

## Closing

'Undoing changes' is Windows protecting you from a failed update — let the rollback finish, then fix the cause instead of dreading the message. Clear the cache, repair the component store, strip the blockers, and check the drive if rollbacks recur. The message disappears permanently once the underlying failure is resolved, because there is nothing left to roll back from. For the condensed highest-yield order, the [best-way fix sequence](/articles/best-way-to-fix-we-couldn-t-complete-the-updates-undoing-changes/) distills this guide to its essentials. If the rollback itself never finishes and the machine just sits on the 'Undoing changes' screen, the [stuck rollback guide](/articles/windows-update-undoing-changes-stuck-troubleshooting/) is built for that exact jam.
