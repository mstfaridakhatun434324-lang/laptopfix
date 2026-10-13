---
title: "How Do I Fix 'We Couldn't Complete the Updates, Undoing Changes'?"
slug: how-do-i-fix-we-couldn-t-complete-the-updates-undoing-changes
date: 2026-09-26
categories: ["windows-update"]
tags: ["couldn't complete updates", "undoing changes fix", "update loop"]
description: "Asking 'how do I fix we couldn't complete the updates, undoing changes'? Here's the plain-English answer: escape the loop, find the cause, fix it once."
thumbnail: "/images/thumbs/how-do-i-fix-we-couldn-t-complete-the-updates-undoing-changes.webp"
faqs:
  - q: "How long does the 'undoing changes' screen normally last?"
    a: "Between 15 minutes and 2 hours depending on your drive and the update size. SSDs usually finish inside an hour; hard drives can take two. Only treat it as stuck after those windows pass with zero drive activity. Interrupting a working rollback is the main way this becomes a serious problem."
  - q: "Will I lose my documents during the rollback?"
    a: "No. The rollback only reverses system files, drivers, and the update packages themselves. Your personal files, photos, and documents are not part of what gets undone. Installed programs also survive in nearly all cases. Backups are still wise before major updates, but the rollback itself is not the thing that threatens your data."
  - q: "Why does it happen again every time I restart?"
    a: "Because Windows keeps retrying the failed update. Until the underlying blocker — bad driver, corrupt cache, full disk — is fixed, each attempt fails the same way and triggers the same rollback. Pausing updates while you repair the cause breaks the cycle."
  - q: "Is this error dangerous for my laptop?"
    a: "The rollback itself is protective, not dangerous — it is Windows choosing safety over a broken install. The danger comes from interrupting it: forced shutdowns mid-rollback can corrupt boot files. Let it finish, then fix the root cause calmly. Once the rollback completes, the system is exactly as stable as it was before the update attempt — no worse, which is the whole point of the safety mechanism."
---

Short answer: let the rollback finish, pause updates so it stops retrying, find the actual error code, fix the underlying cause (usually a driver, a corrupt cache, or a full disk), and then let the update try again. That is the whole strategy. Everything below is the detailed version of those five moves, in the order a technician would perform them.

This message appears when Windows installs an update, checks its own work, finds the result invalid, and reverses everything automatically. It is frustrating because the screen gives you no code and no reason — but the reason exists, logged in your update history, and it is fixable. For the deeper technical walkthrough, see [troubleshooting the undoing-changes loop](/articles/troubleshoot-we-couldn-t-complete-the-updates-undoing-changes/); the Dell-specific version is [undoing changes stuck on Dell](/articles/how-to-fix-windows-update-undoing-changes-stuck-on-dell-laptop/).

Here is a question that helps you calibrate everything that follows: did this update ever work on this laptop? If previous months' updates installed fine and only this one fails, the cause is probably specific to this package — a corrupted download or a one-off conflict — and the lighter fixes will likely do. If updates have been failing for months, the cause is structural — servicing damage, chronic driver staleness, a dying drive — and you should plan on the full sequence including the repair install. Knowing which situation you are in saves you from under-fixing a structural problem or over-fixing a transient one.

## Why this happens

- **The installed update failed its own validation:** Windows checks the result after installing; a mismatch triggers the automatic rollback you are watching.
- **A driver refused to cooperate:** The most common specific cause — an existing driver incompatible with what the update changed.
- **The download was corrupted:** A damaged package that installs incorrectly and fails checks.
- **Your disk is too full:** The install or rollback runs out of working space partway through.
- **Antivirus interfered:** Security software modifying files during the install window, invalidating the result.
- **The servicing stack is damaged:** The install engine itself producing bad installs from good packages. This is the "every update fails the same way" signature — and the DISM repair in Fix 6 is its specific antidote.
- **A previous failed update left debris:** Pending operations from an earlier attempt colliding with the new one.
- **Hardware faults:** Bad RAM or dying storage corrupting data during the heavy install workload.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish — do not interrupt it

1. When you see "Undoing changes," leave the laptop alone with the charger connected.
2. Allow up to **2 hours** (hard drive) or **1 hour** (SSD) — the screen gives no progress bar, which is normal.
3. Watch for drive activity as your progress indicator.
4. Interrupting the rollback mid-stream is the single biggest cause of unbootable systems after this error. Patience is the fix here.

### Fix 2: Pause updates to stop the retry loop

1. Once you are back in Windows: **Settings → Windows Update → Pause updates** for 1–2 weeks.
2. This stops Windows from immediately re-attempting the failed update on the next restart.
3. You now have a stable system to work from — the loop is broken.

### Fix 3: Find the real error code

1. **Settings → Windows Update → Update history** — find the failed update and note its **KB number** and error code.
2. Common codes: 0x80070002 (missing files), 0x80070005 (permissions), 0x800f0922 (framework issues), 0xC1900101 (driver failure).
3. The code tells you which of the fixes below matters most — but the general sequence fixes most cases regardless. Take a photo of the error screen with your phone — codes are easy to mistype from memory.

### Fix 4: Free disk space and update drivers

1. Free at least **15 GB** on C: using Storage Sense and Disk Cleanup (admin → Windows Update Cleanup). Do this before the driver updates, not after — a full disk can corrupt driver installations too, and you want the driver refresh landing on a healthy filesystem.
2. Update your drivers from the manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — focusing on chipset, storage, and graphics.
3. Driver conflicts are the top cause of validation failures; this step removes them.

### Fix 5: Clear the update cache

1. Elevated Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` with `.old` suffixes.
3. Restart the three services and reboot. Fresh cache, fresh metadata, no debris from the failed attempt.

### Fix 6: Repair the servicing stack

1. Elevated Terminal: `DISM /Online /Cleanup-Image /RestoreHealth`, wait for completion.
2. Then `sfc /scannow`, then reboot.
3. This repairs the install engine itself — the fix when the same update fails validation repeatedly.

### Fix 7: Retry surgically, with a fallback ready

1. Unpause updates and install the specific update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) using the KB number.
2. If it succeeds, you are done — resume normal updates.
3. If it fails identically, run an in-place repair install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) ISO (keep files and apps) — the definitive fix for stubborn validation failures. Identical failure after the full sequence is the repair install's cue — do not loop the earlier fixes again.

## Closing

So: let it finish, pause the loop, read the code, fix the cause, retry once. That five-move sequence resolves this error in the overwhelming majority of cases because it addresses the actual failure instead of fighting the rollback screen. The screen is Windows protecting you; the repair is you returning the favor by removing whatever made the protection necessary. Next time the message appears — and on a long-lived laptop, it eventually will — you will know exactly what to do before the rollback even finishes. Share the five moves with anyone you help — they are the same on every brand and every build.
