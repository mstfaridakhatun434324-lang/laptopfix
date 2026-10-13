---
title: "Best Way to Fix 'We Couldn't Complete the Updates, Undoing Changes'"
slug: best-way-to-fix-we-couldn-t-complete-the-updates-undoing-changes
date: 2026-09-11
categories: ["windows-update"]
tags: ["undoing changes fix", "best way", "update rollback", "windows 11"]
description: "The best-practice sequence for 'We couldn't complete the updates, undoing changes' — the most reliable order of fixes, distilled from technician workflows."
thumbnail: "/images/thumbs/best-way-to-fix-we-couldn-t-complete-the-updates-undoing-changes.webp"
faqs:
  - q: "What is the single most effective fix for 'undoing changes' loops?"
    a: "Clearing the SoftwareDistribution cache combined with a DISM component-store repair resolves the majority of recurring rollbacks. The cache clear removes the corrupt payload; DISM fixes the store damage that made the install fail. Do both before retrying. This combination has the highest success rate of any rollback repair."
  - q: "How is this different from the full troubleshooting guide?"
    a: "This is the distilled best-practice sequence — the order an experienced technician would work in, with the highest-yield steps first. The full [undoing changes troubleshooting guide](/articles/we-couldn-t-complete-the-updates-undoing-changes-troubleshooting/) covers the same ground with deeper diagnostics for unusual cases."
  - q: "Should I try the update again right after the rollback?"
    a: "Not immediately. Retrying without changing anything reproduces the same failure. Work at least the cache clear and blocker removal first, then retry. Each blind retry costs you another 30–60 minute rollback cycle. Use the waiting time productively: update drivers and free disk space before the next attempt."
  - q: "When should I stop trying and reinstall?"
    a: "When you have cleared the cache, repaired the store with DISM/SFC, removed blockers, tried the manual Catalog install, and checked drive health — and the rollback still recurs identically. At that point an in-place upgrade repair is faster than further diagnosis."
---

When 'We couldn't complete the updates, undoing changes' appears, most people do the worst possible thing: click 'retry' and hope. Hope is not a troubleshooting strategy. The rollback happened for a specific reason, and the best way to fix it is a specific sequence — highest-probability fixes first, each one eliminating a class of cause before you spend another hour on a doomed retry.

This guide is the distilled version: the order a technician works in when the clock is ticking. No exhaustive diagnostics, no theory — just the sequence that resolves the most cases in the fewest steps. If you want the deeper diagnostic version with log analysis, the [full undoing-changes troubleshooting guide](/articles/we-couldn-t-complete-the-updates-undoing-changes-troubleshooting/) has it.

One rule governs everything below: never retry the update until you have changed something. Every step here changes something.

## Why this happens

- **Corrupt update payload:** The most common cause — a damaged download that fails verification during install, triggering rollback.
- **Component store damage:** The second most common — WinSxS corruption the installer cannot work around.
- **Driver migration failure:** A driver that will not migrate aborts the install late, after significant time invested.
- **Third-party security software:** Filter drivers interfering with the file operations of the install.
- **Disk-level corruption:** Bad sectors or file system errors in the staging area.
- **Insufficient space:** Too little room for the install plus its rollback data.
- **Firmware incompatibility:** Outdated BIOS failing the new build's checks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback complete fully

The best sequence starts with discipline: never interrupt the rollback.

1. Stay plugged in and let 'Undoing changes' finish — 15 to 60 minutes.
2. Do not force shutdowns during the rollback; that is how boot damage happens.
3. Boot to the desktop normally before doing anything else.

### Fix 2: Clear the update cache

Highest-yield step. Eliminates the corrupt payload class of causes in five minutes.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
4. Restart the four services, then reboot.

### Fix 3: Repair the component store

Second-highest yield. Fixes the store damage behind most recurring rollbacks.

1. From the elevated prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow`.
3. Reboot. Do not skip the reboot — the repairs finalize at startup.

### Fix 4: Strip the blockers

Remove the external factors before the retry, not after another failure.

1. Uninstall third-party antivirus temporarily.
2. Disconnect all peripherals except the charger.
3. Update BIOS, chipset, and storage drivers from the manufacturer's site.
4. Free at least 20 GB on C: with Disk Cleanup.

### Fix 5: Retry the update — once, properly

Now the retry has a reason to succeed. Do it under the best conditions.

1. Run Windows Update with peripherals disconnected and the charger attached.
2. Set the machine to never sleep during the attempt.
3. If it is a feature update failing repeatedly, use the Installation Assistant from Microsoft's [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) instead of Windows Update. For repeat failures of the same package, the [cumulative update repeat-failure repair](/articles/how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2/) breaks the cycle.
4. One careful retry. If it rolls back again, continue — do not loop.

### Fix 6: Install manually from the Update Catalog

Bypass the Windows Update client entirely for the stubborn cases.

1. Note the KB number from Update history.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Install the MSU directly, reboot, and verify.
4. A manual install that also rolls back proves the problem is systemic (store, driver, disk) — which you then address rather than retrying.

### Fix 7: Check the drive and escalate deliberately

The last step before the nuclear options: verify the hardware, then choose the repair.

1. Run `chkdsk C: /f /r` and check SMART health.
2. If the drive is healthy and rollbacks persist, perform an in-place upgrade repair (ISO setup, keep files and apps).
3. If the drive is failing, replace it — no software sequence fixes bad sectors.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the in-place repair procedure officially.

### Fix 8: Perform the in-place upgrade repair

When the entire sequence fails, the servicing environment itself is damaged beyond targeted repair. The in-place upgrade reinstalls Windows over itself while keeping your files, apps, and settings — rebuilding the update pipeline, the component store, and the driver stack in a single pass. It takes one to two hours and resolves the cases nothing else touches. Think of it as the controlled demolition option: everything above the foundation is rebuilt while the foundation — your files, apps, and settings — stays exactly where it is. It is slower than the targeted fixes, but its success rate on stubborn rollback loops is unmatched, because it replaces every damaged component at once rather than hunting them individually.

1. Back up your important files to an external drive or cloud storage — the process is safe, but backups are non-negotiable before OS-level surgery.
2. Download the Windows 11 ISO matching your edition from Microsoft and mount it (double-click the ISO).
3. Run setup.exe, choose 'Keep personal files and apps', and disconnect all peripherals with the charger attached.
4. Let it run to completion without interrupting — the machine reboots several times and the progress bar moves slowly near the end.
5. Afterward, open Settings → Windows Update and install — the update that kept rolling back now installs cleanly.
6. Reinstall any third-party antivirus you removed, re-enable your services, and create a fresh restore point to mark the healthy state.

## Closing

The best way to fix 'undoing changes' is order, not effort: let the rollback finish, clear the cache, repair the store, strip blockers, then retry once under ideal conditions. Escalate to manual installation and drive checks only when the sequence fails. Most cases resolve by step five — because most cases were a corrupt payload or a damaged store all along.
