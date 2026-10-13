---
title: "\"We Couldn't Complete the Updates, Undoing Changes\": What to Do Now"
slug: what-to-do-if-we-couldn-t-complete-the-updates-undoing-changes
date: 2026-09-03
categories: ["windows-update"]
tags: ["undoing changes", "update failed", "rollback", "couldn't complete", "recovery"]
description: "Stuck on 'We couldn't complete the updates, undoing changes'? Understand what's happening and what to do when the rollback finishes — or doesn't."
thumbnail: "/images/thumbs/what-to-do-if-we-couldn-t-complete-the-updates-undoing-changes.webp"
faqs:
  - q: "How long does 'undoing changes' normally take?"
    a: "Typically 15 minutes to an hour, depending on how far the update got before failing and your drive speed. Feature-update rollbacks take longer than cumulative ones. If the screen shows animation and occasional disk activity, it's working — let it finish. Only worry if it's completely frozen with no activity for over two hours."
  - q: "Are my files safe during the undoing changes process?"
    a: "Yes. The rollback restores system files to their pre-update state; it doesn't touch your personal files, documents, or photos. That's the entire point of the rollback mechanism — returning the system to a known-good state. Interrupting the rollback is the main thing that could cause problems, so let it complete."
  - q: "Why does the same update keep failing and undoing changes?"
    a: "Because the blocking condition hasn't changed. Windows retries the update, hits the same driver conflict, disk-space limit, or corrupted download, and rolls back again. Each cycle is identical until you fix the root cause. Note the error code in Update history after the rollback, fix the underlying issue, then allow the retry — don't just let it loop."
  - q: "What if 'undoing changes' itself gets stuck?"
    a: "Give it two hours of no activity before acting. If truly frozen, force shutdown once — Windows usually resumes or completes the rollback on the next boot. If it loops, boot into the Recovery Environment (interrupt boot three times) and use 'Uninstall latest quality/feature update' to clear it manually. Your files remain safe through all of this."
---

"We couldn't complete the updates. Undoing changes. Don't turn off your computer." It is actually good news wearing a scary message: Windows tried to install an update, something failed safely, and now it is putting everything back the way it was. The rollback is the safety net working as designed.

What you do next depends on where you are in the process. If "undoing changes" is currently on screen, the job is patience. If it finished and you are back at your desktop, the job is diagnosis — because the update will try again, fail again, and undo again until the underlying cause is fixed.

This guide covers both phases: surviving the rollback, then breaking the fail-and-undo loop. Work through these in order — diagnose first, then act.

## Why this happens

- **Driver conflict during install.** A driver failing migration triggers the automatic rollback.
- **Corrupted update download.** A damaged package failing integrity checks mid-install.
- **Insufficient disk space.** The installer running out of working room partway through.
- **Third-party software interference.** Antivirus or utilities blocking servicing operations.
- **Damaged servicing stack.** Component store corruption failing the install's checks.
- **Hardware-level stalls.** Disk errors or failing storage interrupting file operations.
- **Incompatible update for the configuration.** Microsoft occasionally ships updates with undiscovered conflicts.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish — do not interrupt it

If "Undoing changes" is on screen now: leave it alone. The rollback is restoring system files, and interrupting it is the single most dangerous thing you can do in this situation — it can leave the system in a half-rolled-back state that is much harder to recover.

Watch for signs of life: the spinning animation, occasional disk activity. Give it up to two hours. Only if there is zero activity for two full hours should you consider a force shutdown — and even then, Windows usually resumes the rollback on the next boot. Patience is the fix for this phase.

### Fix 2: After the rollback — capture the error code

Once you are back at the desktop, go to Settings, Windows Update, Update history. Find the failed update and note its exact error code. Common ones: 0x800F0922 (package/servicing), 0xC1900101 (driver rollback), 0x80070070 (disk space).

This code is the entire diagnosis. Do not let Windows retry the update yet — pause updates for 7 days (Settings, Windows Update, "Pause updates") so you can fix the cause first. Every blind retry is another hour-long fail-and-undo cycle. The dedicated [0x800F0922 fix guide](/articles/how-to-fix-windows-11-update-error-0x800f0922-on-lenovo-laptop/) decodes one of the most common rollback codes in detail.

### Fix 3: Free disk space and clear the corrupted download

Rollbacks frequently trace to space or bad packages. Free 15+ GB on C: with Storage Sense and temp-file cleanup. Then purge the failed package so the retry downloads fresh:

1. Open Command Prompt as administrator.
2. Run: `net stop wuauserv`, then `net stop bits`
3. Delete everything inside `C:\Windows\SoftwareDistribution\Download`.
4. Run: `net start bits`, then `net start wuauserv`

A clean download plus adequate space eliminates the two most common rollback triggers in one pass. Do not unpause updates until the remaining fixes are done.

### Fix 4: Update drivers and firmware via the manufacturer

Driver-caused rollbacks are extremely common. Open your manufacturer's utility — Dell SupportAssist, Lenovo Vantage, HP Support Assistant, MyASUS — and install all pending BIOS and driver updates. Keep the charger connected during any BIOS flash.

Outdated storage and chipset drivers are the classic rollback triggers because the update's file operations depend on them. The [Dell support site](https://www.dell.com/support) and [Lenovo support](https://support.lenovo.com/us/en/) serve model-specific updates if you prefer the web. Restart after updating and confirm everything is current before proceeding.

### Fix 5: Remove antivirus interference

Uninstall third-party antivirus with its removal tool — not just disable, since filter drivers stay loaded when merely disabled. Windows Security takes over automatically.

Antivirus products that hook servicing operations are a documented cause of install failures that end in "undoing changes." Retry behavior changes dramatically with them gone: if the next attempt succeeds, you found the blocker. Reinstall antivirus afterward only with a current version. If driver updates are tangled up in your failures, the [driver update failure loop guide](/articles/how-to-fix-driver-updates-keep-failing-windows-update-on-laptop/) untangles that side.

### Fix 6: Repair the servicing stack

When rollbacks recur across different updates, the servicing infrastructure is suspect:

1. Open Command Prompt as administrator.
2. Run: `DISM /Online /Cleanup-Image /RestoreHealth` (10-30 minutes, internet required).
3. Run: `sfc /scannow`.
4. Restart.

These repair the component store and protected system files the update installer validates against. If SFC reports repaired corruption, that was likely aborting your installs. Microsoft's Windows support documentation covers both tools. Retry the update only after both complete cleanly.

### Fix 7: Manual install or hide the problem update

Unpause updates and try once more with all fixes in place. If the same update fails and rolls back again, take the KB number from Update history to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install the .msu manually — the manual path bypasses the pipeline where the failure lived.

If even the manual install rolls back, check whether Microsoft has acknowledged issues with that KB — sometimes the update itself is broken and the correct action is hiding it with the "Show or hide updates" troubleshooter and waiting for the revised release. Not every rollback is your system's fault; occasionally the package is simply bad.

## Closing

"We couldn't complete the updates, undoing changes" is Windows protecting you — the rollback is the safety net, not the problem. Let it finish, capture the error code, then break the loop: fresh download, free space, current drivers and firmware, no antivirus interference, repaired servicing stack. And remember that cumulative updates supersede each other — if one specific KB is cursed, the next month's package usually installs cleanly over it.
