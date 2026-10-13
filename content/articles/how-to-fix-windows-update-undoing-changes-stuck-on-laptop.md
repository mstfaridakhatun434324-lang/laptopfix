---
title: "How to Fix Windows Update ‘Undoing Changes’ Stuck on a Laptop"
slug: "how-to-fix-windows-update-undoing-changes-stuck-on-laptop"
date: 2026-09-02
categories: ["windows-update"]
tags: ["windows update", "undoing changes", "rollback loop", "stuck", "laptop"]
description: "Stuck on ‘Undoing changes made to your computer’? Learn how long to wait, how to break the loop safely, and how to fix the failed update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-undoing-changes-stuck-on-laptop.webp"
faqs:
  - q: "How long is too long for ‘Undoing changes’?"
    a: >
      Up to 2–3 hours can be normal, especially for feature updates on
      hard drives or full SSDs. Beyond 4 hours with no disk activity or
      screen changes, it is reasonable to treat it as stuck. Keep the
      charger plugged in throughout — a dead battery mid-rollback is one
      of the few things that turns a slow recovery into a real problem.
  - q: "Is it safe to turn off my laptop during the rollback?"
    a: >
      It is risky — interrupting a rollback can leave Windows in an
      unbootable half-state. That is why waiting is the first fix. If you
      must intervene after many hours, do it once and be prepared to use
      the Recovery Environment.
  - q: "Why did the update fail in the first place?"
    a: >
      Common reasons: incompatible drivers, insufficient disk space,
      corrupt update cache, or peripheral interference. The update history
      page shows the specific error code, which points at the real cause.
      Each failed update logs its code in Settings > Windows Update >
      Update history — that code is your roadmap. Fix the specific failure
      it names, and the retry succeeds instead of triggering another
      rollback.
  - q: "Will this happen every time I update?"
    a: >
      Not if you fix the root cause. The rollback loop repeats only when
      the same failure recurs — address the error code from update
      history, and the next attempt installs normally. Rollbacks are not
      random; they are Windows responding to the same unresolved problem.
      Update the offending driver, free the needed disk space, or clear
      the corrupt cache, and the cycle ends with the next successful
      install.
---

The ‘Undoing changes made to your computer’ screen means Windows Update tried to install something, failed, and is now rolling back to the previous state. That rollback is a safety feature — it is Windows protecting you from a half-installed update. The problem is when the rollback itself gets stuck, sometimes for hours, leaving the laptop in limbo between the failed update and the working system.

Here is the reassuring part: the rollback is almost always still working even when it looks frozen. Undoing changes involves reversing file operations across thousands of system files, and on slower drives it can legitimately take 30 minutes to several hours. The dangerous move is interrupting it — a forced shutdown mid-rollback is how machines end up unbootable, because the system is then neither the old version nor the new one.

So the rule is: wait generously first, intervene carefully second, and then fix the underlying failed update so the loop does not repeat. That is exactly the order below. If you are dealing with a related symptom instead, see [the best way to fix a stuck restarting screen](/articles/best-way-to-fix-windows-update-stuck-on-restarting-screen/) and [Windows Update stuck on restarting on Dell](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-dell-laptop/).

Seeing ‘Undoing changes made to your computer’ means Windows already tried the update, failed, and is now protecting you by rolling back — the safety feature is working as designed. The anxiety comes when the rollback itself seems frozen, sometimes for hours. Here is the reassuring reality: rolling back thousands of file operations is genuinely slow work, and most ‘stuck’ rollbacks are just unfinished ones. Wait generously first, intervene carefully second, and fix the underlying failure third.

## Why this happens

- **Legitimately slow rollback** reversing thousands of file operations takes a long time on slow storage.

- **Failed update left inconsistent state** the rollback has more damage to unwind than expected.

- **Driver conflict caused the original failure** the same bad driver complicates the rollback.

- **Low disk space** rollback needs working space too.

- **Corrupt servicing state** the rollback engine trips over damaged metadata.

- **Peripheral interference** devices complicate the driver rollback phase.

- **Interrupted previous rollback** an earlier forced shutdown made the current rollback harder.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait — longer than you think

Most ‘stuck’ rollbacks are just slow. Plug in the charger and walk away; hovering over the screen does not speed up file operations, and impatience is what turns slow rollbacks into broken ones. Set a timer for three hours rather than watching the screen; the rollback needs no supervision, and watching it only feeds the urge to intervene early.

1. Plug in the charger and leave the laptop completely alone.

2. Give it at least 2–3 hours; large feature-update rollbacks can take longer on HDDs.

3. Watch for any change — disk activity, brief screen flickers.

4. Only treat it as stuck after 4+ hours with zero signs of life.

### Fix 2: Force a restart only as a last resort

Interrupting a rollback carries real risk — do it once, carefully. If Windows resumes the rollback on its own after the forced restart, let it run to completion this time — do not interrupt it a second time.

1. Hold the power button 10 seconds to power off.

2. Unplug all USB peripherals.

3. Wait 30 seconds and power on.

4. Windows will attempt to resume or complete the rollback.

### Fix 3: Boot into Safe Mode

If normal boot returns to the loop, Safe Mode often breaks it. Safe Mode loads a minimal driver set, which is often enough to let a driver-blocked rollback finish what normal mode could not.

1. Trigger WinRE with two interrupted boots.

2. Troubleshoot > Advanced options > Startup Settings > Restart, press 4.

3. In Safe Mode, let any pending rollback finish.

4. Restart normally afterward.

### Fix 4: Use System Restore from WinRE

Rolls the system back cleanly past the failed update. Pick the most recent restore point predating the update attempt; older points work too but undo more of your recent system changes.

1. In WinRE: Troubleshoot > Advanced options > System Restore.

2. Pick a restore point from before the update attempt.

3. Complete the restore and boot normally.

### Fix 5: Clear the failed update’s cache

Prevents Windows from immediately retrying the same failure. Pausing updates for a week after recovery gives you breathing room to fix the root cause instead of immediately re-triggering the same failure.

1. Once booted, open an elevated Command Prompt.

2. net stop wuauserv, net stop bits; clear C:\Windows\SoftwareDistribution\Download; net start both.

3. Pause updates for 7 days (Settings > Windows Update) to stabilize.

### Fix 6: Fix the underlying failure before retrying

The rollback happened for a reason — find it. The error code in update history is your roadmap — searching it will usually land you on the exact fix instead of generic advice.

1. Check Settings > Windows Update > Update history for the failed KB and its error code.

2. Address that specific code (driver updates, disk space, DISM repairs as appropriate).

3. Disconnect USB peripherals before the next attempt.

4. Unpause updates and retry once the cause is fixed.

### Fix 7: Uninstall the problematic update if it partially installed

Sometimes the rollback leaves a half-present update. After uninstalling, run DISM and SFC to clean up any servicing debris the partial install left behind before attempting the update again.

1. Settings > Windows Update > Update history > Uninstall updates.

2. Remove the partially installed KB if listed.

3. Restart, then run DISM /Online /Cleanup-Image /RestoreHealth and sfc /scannow.

4. Retry the update afterward.

## Closing

The ‘Undoing changes’ screen is Windows doing the safe thing, and patience is the fix more often than people expect. Wait it out, break the loop carefully only if you must, then fix whatever made the update fail — the rollback will not need to happen twice. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
