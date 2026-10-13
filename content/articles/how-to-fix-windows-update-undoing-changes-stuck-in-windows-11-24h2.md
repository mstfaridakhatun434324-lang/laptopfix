---
title: "How to Fix Windows Update Stuck on “Undoing Changes” in Windows 11 24H2"
slug: "how-to-fix-windows-update-undoing-changes-stuck-in-windows-11-24h2"
date: 2026-09-11
categories: ["windows-update"]
tags: ["undoing changes", "windows 11 24h2", "rollback", "windows update"]
description: "Windows Update stuck on “Undoing changes” in Windows 11 24H2? Six fixes for slow and stalled rollbacks, from patience budgets to WinRE recovery."
thumbnail: "/images/thumbs/how-to-fix-windows-update-undoing-changes-stuck-in-windows-11-24h2.webp"
faqs:
  - q: "How long should undoing changes take on 24H2?"
    a: "On 24H2, 45–90 minutes is normal for a rollback on an SSD, and over 2 hours on a hard drive — the checkpoint cumulative model unwinds stacked updates sequentially, which takes longer than older Windows versions. Only treat it as stuck when the screen is completely static with zero drive activity for a full hour. Most “stuck undoing changes” reports on 24H2 resolve themselves with more patience."
  - q: "Can I turn off my laptop during undoing changes?"
    a: "Strongly discouraged. The rollback is restoring thousands of system files, and interrupting it corrupts the restore journal — turning a slow-but-working rollback into a genuinely stuck one or an unbootable system. If you already interrupted it once, let the next attempt run even longer, since it now has damaged state to work around. Patience is the fix, not the power button."
  - q: "What are checkpoint updates?"
    a: "Checkpoint cumulative updates are 24H2’s new servicing model: instead of one giant monthly package, updates stack as smaller checkpoints on a baseline. It makes downloads smaller, but a rollback must unwind each checkpoint in order, which lengthens the “Undoing changes” phase compared to Windows 11 23H2 and Windows 10. The design is intentional — the extra time is the cost of smaller downloads."
  - q: "Will the update retry after rolling back?"
    a: "Yes — that is the expected flow. After the rollback completes and Windows boots, Update history shows the failed update with its error code. Use that code to target the fix: update conflicting drivers, reset the update cache, or install the update manually from the Microsoft Update Catalog. The rollback bought you a working system; the fixes ensure the next attempt succeeds instead of rolling back again."
---

Windows 11 24H2 changed the update game with checkpoint cumulative updates — smaller downloads, but rollbacks that unwind stacked checkpoints one by one. The result: “Undoing changes” screens that run far longer than they did on 23H2, and a flood of reports that the rollback is “stuck” when it is actually just slow.

There is a real stuck state too, usually caused by interrupting the first rollback or by disk problems. Telling slow from stuck is the whole skill on 24H2, and the general rollback mechanics are covered in the [undoing-changes overview](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-reddit/).

## Why this happens

- **24H2’s larger update payloads lengthening rollback:** 24H2 cumulative updates are bigger than previous versions’, so their rollbacks legitimately take longer — what looks stuck is often just slow.
- **Checkpoint update stacking:** 24H2 introduced checkpoint cumulative updates; a rollback must unwind stacked checkpoints sequentially, multiplying the time.
- **Corrupted rollback journals:** If the journal tracking what to undo is damaged, the rollback process stalls retrying unreadable entries.
- **Driver conflicts specific to the 24H2 driver model:** Drivers that worked on 23H2 can fail 24H2’s stricter install checks, triggering the rollback that then takes ages.
- **Disk space exhausted mid-rollback:** Rollbacks need working space too; a full drive can stall the undo process itself.
- **Failing storage slowing file restoration:** The rollback restores thousands of files — a marginal drive turns that into hours.
- **Interrupted first rollback corrupting the second attempt:** Powering off during “Undoing changes” damages the rollback state, making the next attempt slower or stuck.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Give 24H2’s slower rollback the time it needs

24H2’s checkpoint model makes rollbacks structurally slower than you remember from older Windows. The number-one “fix” for stuck undoing-changes on 24H2 is recalibrating expectations — the process is usually fine, just long.

1. Start a timer when “Undoing changes” appears.
2. Allow 90 minutes on SSD, 2+ hours on HDD before judging.
3. Confirm drive activity (LED, sounds) as proof of progress.
4. Do nothing but wait while activity continues — the rollback is working.

### Fix 2: Read the rollback receipt in Update history

Every rollback leaves a receipt in Update history. Reading it turns the next attempt from a gamble into a targeted fix — the error code tells you whether drivers, space, or corruption caused the failure.

1. After the rollback completes and Windows boots, open Update history.
2. Record the failed KB and error code — this is your diagnosis.
3. Check free space (aim for 25+ GB) and update graphics, storage, and network drivers.
4. Clear the update cache before any retry.

### Fix 3: Clear the failed package and retry cleanly

The package that rolled back is still staged in damaged form; retrying without clearing it just replays the failure. A cache reset plus a manual Catalog install is the highest-success combination for updates that rolled back once.

1. Elevated Terminal: net stop wuauserv, net stop bits, net stop cryptSvc.
2. Rename: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
3. Restart the services.
4. Retry the update — or install it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) to bypass the client.

### Fix 4: Update firmware and drivers for 24H2’s stricter checks

24H2 enforces stricter driver and firmware compatibility than 23H2. Updates that rolled back on 24H2 while working elsewhere usually trace to an outdated BIOS or storage driver failing the new checks — manufacturers have released 24H2-specific updates for exactly this.

1. Update BIOS from your laptop maker ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. Update chipset and storage drivers from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) or AMD.
3. Remove third-party antivirus temporarily during the retry.
4. Retry the update with current firmware and drivers.

### Fix 5: Recover a genuinely stalled rollback via WinRE

A truly stalled rollback — no drive activity for over an hour — needs WinRE intervention. Uninstalling the partial update from recovery clears the jammed state so Windows can boot and you can repair the trigger properly.

1. If the rollback screen itself is frozen (no activity for 1+ hour), force shutdown once.
2. Boot to WinRE (interrupt boot twice) > Troubleshoot > Advanced options.
3. Use “Uninstall Updates” to remove the partially applied update, or Startup Repair.
4. Boot normally, pause updates 7 days, and apply the driver/cache fixes before retrying.

### Fix 6: Free space and verify drive health

Rollbacks restore thousands of files — they need free space and a healthy drive to do it at speed. Space and disk health are the environmental factors that turn a 45-minute rollback into a 3-hour one.

1. Free space aggressively: Disk Cleanup as admin, remove Windows.old if rollback is not needed.
2. Run chkdsk C: /f to rule out file-system damage slowing the restore.
3. If rollbacks are slow on every update, check SMART drive health.
4. For the general rollback pattern beyond 24H2, see the [undoing-changes overview](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-reddit/).

### Fix 7: Pause updates and schedule the retry deliberately

After a rollback on 24H2, the worst move is an immediate retry — the trigger (driver, cache, space) is still in place, and you will simply generate a second multi-hour rollback. Instead, pause updates for 7 days, apply every repair calmly, and then unpause for a deliberate retry at a convenient time. A scheduled retry also lets you pick the moment: charger connected, peripherals detached, no deadlines looming. Treating the retry as a planned operation rather than a background accident is what breaks the rollback-retry-rollback cycle for good.

1. After the rollback completes, open Settings > Windows Update and pause updates for 7 days.
2. Work through the driver updates, cache reset, and space freeing without time pressure.
3. Choose a retry window with at least 3 free hours and the charger connected.
4. Detach peripherals, then click “Resume updates” and install.
5. Stay nearby during the restart phase so you can distinguish slow from stuck in real time.

## Closing

On 24H2, “Undoing changes” is slower by design — bigger payloads and checkpoint stacking mean genuine rollbacks can exceed an hour. Give it that time, verify with drive activity, and only then intervene via WinRE. And once you are back in Windows, fix the trigger (drivers, cache, space) so the update installs instead of rolling back next time. If the “We couldn’t complete the updates” screen that kicks off every rollback keeps reappearing on 24H2, our [24H2 couldn’t-complete-the-updates guide](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-in-windows-11-24h2/) tackles the exact error message that starts the cycle.
