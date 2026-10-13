---
title: "How to Fix “We Couldn’t Complete the Updates, Undoing Changes” (Looping Rollback)"
slug: "how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-reddit"
date: 2026-09-02
categories: ["windows-update"]
tags: ["undoing changes", "windows update", "rollback", "failed update"]
description: "“We couldn’t complete the updates, undoing changes” looping on your laptop? Six fixes that stop the rollback cycle and get the update installed cleanly."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-reddit.webp"
faqs:
  - q: "What does “we couldn’t complete the updates” mean?"
    a: "It means Windows started installing an update, detected a failure partway through, and automatically reversed all changes to return your system to its previous working state. Your files are safe — the rollback is a protective mechanism, not data loss. The underlying cause is usually a conflicting driver, a corrupted download, or insufficient disk space, all fixable with the steps in this guide."
  - q: "How long should undoing changes take?"
    a: "Usually 15 to 45 minutes, but on slower drives or large feature updates it can take over an hour. The rollback is doing real work — restoring thousands of files — so interrupting it risks the exact half-updated state it is trying to prevent. Only intervene if the screen is completely static with no drive activity for over an hour, and even then prefer waiting longer on mechanical hard drives."
  - q: "Is it safe to turn off my laptop during undoing changes?"
    a: "It is safe in the sense that Windows designed the rollback to be interrupt-tolerant, but you should avoid it: powering off mid-rollback can corrupt the restore process and leave the system unbootable. If you absolutely must, hold the power button once, then boot into the recovery environment to repair. In nearly all cases, patience is the safer and ultimately faster option."
  - q: "Will the failed update try again automatically?"
    a: "Yes — that is exactly what the message indicates. After the rollback completes and Windows boots normally, open Settings, then Windows Update, then Update history. The failed update will be listed with an error code. Use that code to target your fix: update the conflicting driver, free disk space, or clear the update cache before retrying the install."
---

Few Windows messages inspire as much dread as “We couldn’t complete the updates, undoing changes.” Your laptop restarts, grinds through the rollback, boots — and the next day the same update tries again and fails again. It feels like being stuck in a loop, and in a sense you are: Windows is faithfully protecting you from a half-installed update, over and over.

The rollback itself is good news disguised as bad: it means Windows detected the failure and restored your working system instead of leaving you with a broken one. The task now is to find what keeps tripping the installer. Community threads (the “reddit” in the search) converge on the same handful of causes — and the same fixes that actually end the cycle.

## Why this happens

- **Incompatible driver staged for install:** The most common trigger: a driver or system file in the update conflicts with existing hardware drivers, so Windows aborts and rolls back.
- **Corrupted update download:** A damaged package that fails integrity checks mid-install triggers the automatic rollback as a safety measure.
- **Insufficient disk space discovered late:** The installer sometimes discovers mid-process that staging space ran out, and rolls back rather than leaving a partial system.
- **Third-party antivirus blocking file replacement:** Security software intercepting the system-file swaps forces the installer to abort and undo its changes.
- **Pending operations from a previous update:** Leftover pending file operations collide with the new update’s operations, and the installer backs out.
- **Failing system drive:** I/O errors during the file-replacement phase abort the install; the rollback is Windows protecting you from a half-written OS.
- **BIOS or firmware incompatibility:** On some laptops, outdated firmware mishandles the handoff between install phases, failing the update deterministically.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish and read the failure details

The rollback is protective, not destructive — interrupting it is the one thing that can turn a recoverable failure into an unbootable system. Let it finish, then use the failure details it leaves behind as your diagnosis.

1. Let the “Undoing changes” screen finish completely — do not power off.
2. Time it: most rollbacks complete within 45 minutes on SSDs.
3. Watch for drive activity as proof of progress.
4. Once Windows boots, open Update history and record the failed KB and error code.

### Fix 2: Remove the three most common rollback triggers

Rollbacks have repeat offenders: full disks, stale drivers, and corrupted downloads. Addressing all three before retrying breaks the cycle in the majority of cases, because the next attempt no longer trips the same trigger.

1. In Update history, identify the update that triggered the rollback.
2. Check free space: Settings > System > Storage — ensure 20+ GB free.
3. Update the most likely conflicting drivers (graphics, storage, network) from the manufacturer.
4. Clear the update cache: stop wuauserv and bits, rename SoftwareDistribution, restart services.

### Fix 3: Repair the component store the update builds on

When the component store is damaged, every update attempt assembles incorrectly and rolls back identically. DISM rebuilds the store so the installer has a sound base to build on — this fixes the “fails the same way every time” pattern.

1. Open an elevated Command Prompt.
2. Run: DISM /Online /Cleanup-Image /RestoreHealth.
3. Follow with: sfc /scannow.
4. Restart, then retry the update.

### Fix 4: Install the update manually from the Catalog

The standalone installer skips the Windows Update client’s queue, cache, and download logic — the three places rollbacks most often originate. Installing the same update manually frequently succeeds on the first try, which also confirms your system itself is healthy.

1. Download the failed update’s .msu from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) using its KB number.
2. Disconnect non-essential USB devices.
3. Temporarily disable third-party antivirus real-time protection.
4. Run the .msu installer and restart when prompted.

### Fix 5: Update BIOS and chipset drivers for deterministic rollbacks

Deterministic rollbacks — same update, same failure, every time — often trace to firmware. An outdated BIOS or storage driver can fail the phase handoff on every attempt, and no amount of cache-clearing fixes a firmware problem. Manufacturers release BIOS updates specifically addressing Windows update compatibility.

1. Check your laptop maker’s support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) for a newer BIOS than yours.
2. Update chipset and storage drivers at the same time.
3. Retry the Windows update after the firmware is current.
4. If rollbacks persist on 24H2 specifically, see the [24H2 undoing-changes guide](/articles/how-to-fix-windows-update-undoing-changes-stuck-in-windows-11-24h2/).

### Fix 6: Repair-install Windows as the definitive fix

An in-place upgrade is the definitive repair for a servicing stack that resists all targeted fixes. It preserves your files and applications while replacing every system component — after it, the update that kept rolling back installs normally.

1. If the update keeps rolling back after all repairs, download the [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11).
2. Run setup.exe from within Windows and choose “Keep personal files and apps”.
3. This reinstalls Windows over itself, rebuilding the entire servicing stack.
4. Retry the update on the repaired system.

### Fix 7: Capture the real error by disabling automatic restart on failure

The rollback screen hides the underlying error code that would tell you exactly what failed. Disabling automatic restart on system failure (via WinRE’s startup settings) lets you see stop codes instead of instant rollbacks on the worst failures, and checking the Panther setup logs after a rollback reveals the failed phase. Dell laptops have additional firmware-level logging worth checking — the [Dell undoing-changes guide](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-dell-laptop/) walks through Dell-specific diagnostics for rollback loops.

1. Boot to WinRE > Troubleshoot > Advanced options > Startup Settings > Restart, then press 9 to disable automatic restart after failure.
2. Retry the update and note any stop code shown instead of an instant rollback.
3. After any rollback, inspect C:\$WINDOWS.~BT\Sources\Panther\setupact.log for the failing phase.
4. Search the log for “0x” error codes near the end — the last errors are the operative ones.
5. Target your fix at the named phase or driver instead of retrying blindly.

## Closing

“We couldn’t complete the updates, undoing changes” is Windows doing its job — refusing to leave you with a half-updated system. The rollback is the safety net; the fixes above remove whatever kept tripping it. Clear the bad package, repair the base, update the conflicting driver or BIOS, and the next attempt completes instead of undoing.
