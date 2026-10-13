---
title: "'Undoing Changes Made to Your Computer' Stuck? Recover Your Laptop"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck
date: 2026-09-13
categories: ["windows-update"]
tags: ["undoing changes", "stuck", "update failed", "boot loop", "windows 11"]
description: "Stuck on 'Undoing changes made to your computer' for hours? Learn when the rollback is working, when it's hung, and how to recover your laptop safely."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck.webp"
faqs:
  - q: "What does 'Undoing changes made to your computer' mean?"
    a: "It means a Windows update failed to install and Windows is rolling back to the pre-update state. The rollback reverses every change the failed update made — file replacements, registry edits, driver swaps — which is why it takes a while. It is a safety mechanism working as designed."
  - q: "How long should the undoing changes screen take?"
    a: "Typically 15–45 minutes depending on how far the failed update got and your disk speed. If the spinner is animating and the drive shows activity, it is working. Beyond 2–3 hours with no animation, the rollback itself has likely hung."
  - q: "Will I lose my files during the rollback?"
    a: "No. The rollback only reverses the failed update's changes to system files, drivers, and settings — it does not touch your personal files, documents, or photos. That said, having current backups is always wise before major update operations, because a rollback that itself gets interrupted is much harder to recover from."
  - q: "What if the laptop is stuck in an undoing-changes loop?"
    a: "A loop — rollback, reboot, attempt, fail, rollback again — means the update keeps retrying and failing. Break it by booting into Safe Mode or the recovery environment, then hiding the problematic update or fixing the underlying cause so the retry succeeds or stops."
---

"Undoing changes made to your computer" is Windows doing something genuinely good: an update failed, and instead of leaving your system half-updated, Windows is carefully reversing every change. The problem is that this screen gives you no progress bar, no percentage, no reassurance — just a spinner and a sentence. After an hour, patience curdles into panic, and the urge to force a shutdown grows. This guide tells you exactly how long to wait, how to tell a working rollback from a hung one, and how to recover in each case.

The critical distinction: interrupting a working rollback can corrupt your Windows installation far worse than the failed update would have. So the waiting rules here are not suggestions — they are the safety rails.

Understanding what the rollback is actually doing makes the wait more bearable and the judgment calls sharper. Windows maintains a transaction log of everything the update changed; "undoing changes" walks that log in reverse, restoring each file, registry value, and driver to its pre-update state and verifying as it goes. That verification is why it is slow \u2014 and why interrupting it is dangerous: a half-walked reversal leaves the system neither updated nor cleanly rolled back. If the same update keeps failing and triggering rollbacks in a loop, the [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-every-time-on-laptop/) helps break the underlying cycle.

## Why this happens

- **Failed update triggering rollback:** The root event — a cumulative or feature update failed its install or post-restart verification, and Windows invoked the rollback.
- **Large update, slow rollback:** The further the failed update progressed, the more there is to undo. Big feature updates produce long rollbacks legitimately.
- **Slow disk:** Rollbacks are I/O-heavy; spinning hard drives and nearly full SSDs stretch the process dramatically.
- **Driver rollback complications:** If the failed update included driver changes, reversing them involves device re-enumeration that can stall on problematic hardware.
- **Corrupt rollback data:** The update's own uninstall/rollback metadata is damaged, so the rollback engine cannot complete its checklist.
- **Disk errors mid-rollback:** Bad sectors encountered during the reversal hang the process.
- **Interrupted first rollback attempt:** A premature forced shutdown during an earlier rollback leaves the system in a state where the next rollback also struggles.
- **Update retry loop:** Windows Update re-offering the same failing update after rollback, creating the infamous fail-rollback-retry cycle — related to the [restarting-screen hang](/articles/what-to-do-if-windows-update-stuck-on-restarting-screen/) when the failure happens at reboot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait correctly — the spinner is information

1. Confirm the spinner or dots are still animating. Animation means the rollback engine is alive.
2. Give it up to 2 hours for feature updates, 1 hour for cumulative updates. Listen for disk activity as confirmation of real work.
3. Do not touch the power button during this window. A working rollback interrupted is how unbootable systems are made.
4. Only proceed if the animation has been frozen for 30+ minutes or the wait has clearly exceeded these bounds.

### Fix 2: Forced shutdown and automatic recovery

1. Hold the power button for 10 seconds until fully off.
2. Wait 30 seconds, then power on.
3. Windows will usually resume or restart the rollback, or boot to Automatic Repair. Let whatever starts finish without interruption.
4. If Windows boots normally, immediately go to Update history to identify the failed update.

### Fix 3: Boot into the recovery environment if normal boot fails

1. Force shutdown twice during the Windows logo to trigger Automatic Repair.
2. Go to Troubleshoot, Advanced options.
3. Try Startup Repair first — it fixes boot issues the interrupted rollback may have caused.
4. If Startup Repair does not help, use System Restore to roll back to a restore point from before the update attempt.

### Fix 4: Break the retry loop from Safe Mode

1. In the recovery environment, go to Troubleshoot, Advanced options, Startup Settings, Restart, and boot into Safe Mode (option 4).
2. Open Settings, Windows Update, and pause updates for 7 days to stop the immediate retry.
3. Note the failed KB from Update history — you will address it in Fix 6.

### Fix 5: Repair the damage the failed update left behind

1. In Safe Mode (or normal mode once stable), open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
3. Clear the update cache: stop wuauserv/bits/cryptsvc, empty C:\Windows\SoftwareDistribution, restart services.
4. This cleans up both the failed update's remnants and any corruption the interrupted rollback introduced.

### Fix 6: Address the failed update itself

1. With updates paused and the system repaired, unpause and check for updates — but watch the previously failed KB.
2. If it fails again, download it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install the standalone package.
3. If the manual install also fails, use wushowhide.diagcab to hide that specific update so the loop cannot reform.
4. Update drivers (especially storage and display) from the manufacturer before the next Patch Tuesday — driver conflicts are a leading cause of update failures that trigger rollbacks.

### Fix 7: Verify stability and prepare for next time

1. Run a full update cycle and confirm everything installs cleanly.
2. Create a system restore point while healthy — it gives the next rollback a cleaner fallback.
3. Ensure 20+ GB free on the system drive; cramped drives cause both update failures and slow rollbacks.
4. For Microsoft's official rollback and recovery documentation, see the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Harden the system before the next update attempt

Make the next update attempt the last one you worry about.

1. Free at least 25 GB on the system drive \u2014 cramped drives cause both install failures and agonizingly slow rollbacks.
2. Update storage and display drivers from the manufacturer's site; driver conflicts are a leading rollback trigger.
3. Disconnect non-essential USB devices during the next update \u2014 peripherals with flaky drivers are a classic failure source.
4. Run the next update on AC power with background utilities quieted, and do not touch the laptop until it finishes. Boring precautions prevent dramatic recoveries.

## Closing

The undoing-changes screen is Windows at its most responsible and its least communicative \u2014 a careful transaction reversal with no progress bar. Respect the wait, intervene only when the evidence says the rollback has truly hung, break the retry loop at its root cause, and then harden the system so the next update does not need a rollback at all. A failed update is a bad day; an interrupted rollback is a bad week; a hardened system is a quiet Patch Tuesday. Patience here is not passivity \u2014 it is the actual fix.
