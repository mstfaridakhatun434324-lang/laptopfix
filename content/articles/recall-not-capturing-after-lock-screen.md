---
title: "How to Fix Recall Not Capturing After the Lock Screen on Windows 11"
slug: recall-not-capturing-after-lock-screen
date: 2026-10-22
categories: ["ai-pc"]
tags: ["recall lock screen", "recall not capturing", "windows recall pause", "recall resume capture", "copilot plus pc", "windows 11"]
description: "Recall stops capturing every time you lock your PC? Fix Recall's failure to resume after the lock screen with these six targeted troubleshooting steps."
thumbnail: "/images/thumbs/recall-not-capturing-after-lock-screen.webp"
faqs:
  - q: "Is it normal for Recall to pause while the screen is locked?"
    a: >
      Yes — pausing during lock is by design, since there is nothing meaningful to capture. The bug is only when capture fails to resume after you unlock and start working again.
  - q: "How can I tell if Recall is currently capturing?"
    a: >
      Open Recall and check for very recent snapshots in the timeline. There is no persistent 'recording' indicator by design — the timeline itself is the status display.
  - q: "Does this affect snapshots from before the lock?"
    a: >
      No. Snapshots taken before locking remain in the timeline. Only the post-unlock period goes missing when the resume fails.
  - q: "Will disabling the lock screen fix it?"
    a: >
      Disabling the lock screen avoids the trigger but creates a security problem and does not fix the underlying resume bug. Fix the handshake instead — and keep locking your PC.
---

You lock your PC for lunch, unlock it, work all afternoon — then discover Recall captured nothing after the unlock. The timeline has a clean gap exactly matching the locked period plus everything after it, until something eventually jolts capture back to life.

This is a resume failure: Recall correctly pauses capture while the screen is locked (there is nothing useful to snapshot), but the wake-up handshake that should restart it sometimes never completes. The capture service stays in its 'locked' state while you happily work in an uncaptured session. It is the same class of resume bug as [Copilot key double-press problems](/articles/copilot-key-double-press-issue/), where a key press after sleep goes into a void instead of waking its feature.

Six fixes below: confirming the pattern, checking the obvious toggles, repairing the resume handshake, and stabilizing the underlying services. Lock and unlock deliberately to test after each one.

## Why this happens

- **Capture service not resuming after unlock:** The background service that takes snapshots fails to transition from locked to active state — the core bug, and the reason gaps extend long past the unlock moment.
- **Fast Startup interfering with service state:** Hybrid shutdown/startup can leave services in a half-initialized limbo where unlock events are missed — a cousin of the [Recall snapshots paused](/articles/recall-snapshots-paused-fix/) problem where the service state and the UI disagree.
- **Power settings suspending background work:** Aggressive power plans can keep the capture pipeline suspended after unlock to 'save battery,' never releasing it back to full operation.
- **Windows Hello or sign-in delays:** If sign-in options stall or the unlock handshake is slow, Recall may miss the resume signal entirely.
- **Corrupt snapshot store blocking new writes:** Sometimes capture does resume but writes fail against a damaged store — indistinguishable from not capturing without checking the store health.
- **Third-party lock-screen or security software:** Custom lock screens, privacy filters, or security tools can intercept the unlock event before Recall sees it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the exact gap pattern

Verify the gaps align precisely with lock/unlock cycles — this distinguishes a resume bug from general capture failure.

1. Lock the PC with **Win + L**, wait 2 minutes, unlock, and work for 10 minutes.
2. Open Recall and check whether snapshots exist for the post-unlock period.
3. Repeat the test once more to confirm it is reproducible, not a one-off.
4. Note whether capture eventually resumes on its own (after minutes? hours? only after reboot?) — that timing hints at the cause.

### Fix 2: Check the save-snapshots toggle and filters

Rule out the mundane before chasing the exotic: a flipped toggle produces identical symptoms.

1. Open **Settings > Privacy & security > Recall & snapshots** and confirm **Save snapshots** is on.
2. Check that the current app is not in the exclusion list — you might be testing with an excluded app.
3. Verify the sensitive-information filter is not aggressively hiding the test snapshots.
4. If all toggles are correct, the resume handshake is the real suspect — continue.

### Fix 3: Disable Fast Startup

Fast Startup's hybrid state is a notorious source of missed wake/unlock events across Windows features.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully (not restart), power on, and run the lock/unlock test again.
4. If capture now resumes reliably, Fast Startup was swallowing the unlock signal.

### Fix 4: Reset the capture service state

Force the capture pipeline through a clean stop/start cycle to clear whatever wedged state the missed resume left behind.

1. Turn **Save snapshots** off in Recall settings.
2. Restart the PC — a full restart, not just sign-out.
3. Turn **Save snapshots** back on and wait 5 minutes of active use.
4. Run the lock/unlock test. A clean service state usually restores the resume handshake.

### Fix 5: Check power and sleep settings

Over-aggressive power management can keep background capture throttled after unlock.

1. Go to **Settings > System > Power & battery** and review the power mode — **Best power efficiency** is the most aggressive.
2. Switch to **Balanced** while testing to rule out power throttling.
3. Check **Screen, sleep, & hibernate timeouts** for unusually aggressive values.
4. Brand-specific power tools can also interfere — [Lenovo Vantage AI features](/articles/lenovo-vantage-ai-features-not-working/) covers how vendor utilities meddle with Windows power behavior.

### Fix 6: Repair Windows if the resume stays broken

A resume handshake that survives all the above is likely damaged at the OS service level.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` elevated.
2. Install all pending Windows updates, since the capture service ships with the OS.
3. Test with third-party security or lock-screen tools temporarily disabled to rule out interception.
4. If it persists, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the repair-install path as the final escalation.

## Closing

Recall pausing on lock is correct; failing to resume is not. Confirm the gap pattern, check the toggles, disable Fast Startup, reset the capture service, and review power settings — in that order. The resume handshake is delicate, but it is repairable, and once it is healthy your timeline will bridge every unlock without missing a beat.
