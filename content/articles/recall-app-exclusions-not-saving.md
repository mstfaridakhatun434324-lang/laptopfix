---
title: "How to Fix Recall App Exclusions Not Saving on Windows 11"
slug: recall-app-exclusions-not-saving
date: 2026-10-22
categories: ["ai-pc"]
tags: ["recall app exclusions", "recall exclusions not saving", "windows recall", "recall settings bug", "copilot plus pc", "windows 11"]
description: "Recall keeps forgetting your app exclusions on Windows 11? Fix exclusions that won't save on your Copilot+ PC with these six proven troubleshooting steps."
thumbnail: "/images/thumbs/recall-app-exclusions-not-saving.webp"
faqs:
  - q: "Why do my Recall exclusions keep disappearing?"
    a: >
      The usual causes are a corrupt Recall settings store, a policy override on managed devices, editing exclusions under the wrong user account, or settings sync overwriting your changes. Work through the fixes above in order.
  - q: "Do app exclusions also block websites in that app's browser?"
    a: >
      App exclusions block capture of the whole app, including its browser windows. For finer control, use Recall's website exclusion list for specific sites instead of excluding the entire browser.
  - q: "How many apps can I exclude from Recall?"
    a: >
      There is no documented hard limit — exclude as many as you need. A long exclusion list does not noticeably slow Recall down.
  - q: "Will excluding an app delete its old snapshots?"
    a: >
      No. Excluding an app only stops future capture. Snapshots already taken remain in the timeline until they age out or you delete them manually.
---

Recall's app exclusion list is its most important privacy control: add an app, and Recall never snapshots it. So when exclusions refuse to save — you add an app, close settings, and it is gone again — the privacy promise quietly breaks.

Exclusions that will not stick usually point to a settings-storage problem rather than a Recall capture problem. The list lives in the same settings database as the rest of Recall's configuration, and when writes to that database fail, exclusions are the most visible casualty. A parallel settings-write failure causes [the missing per-app Studio Effects toggle](/articles/studio-effects-per-app-toggle-missing/), where a toggle flips back the moment you leave the page.

This guide walks through six fixes: verifying the failure, ruling out account and policy blocks, repairing the settings database, and confirming exclusions hold. Test by re-adding one app after each step.

## Why this happens

- **Settings database write failure:** If Recall's configuration store is corrupt or locked, exclusion changes silently fail to persist — the UI accepts them, but nothing is written to disk.
- **Policy or MDM overriding exclusions:** On work or school devices, management policy can control Recall's behavior and discard user-made exclusion changes.
- **Wrong user account context:** Exclusions are per-user. Adding them under one account while checking under another makes it look like they did not save.
- **App identity changes after updates:** When an excluded app updates, its package identity can change enough that Recall no longer matches it — the entry saves, but stops applying, which mimics the [Recall not recording specific apps](/articles/recall-not-recording-specific-apps/) symptom.
- **Settings sync conflicts:** If Windows settings sync is fighting between devices, exclusion changes can be overwritten by an older synced state.
- **Recall component needing repair:** A damaged Recall system component can lose the ability to persist any settings, with exclusions as the most noticeable loss.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the failure precisely

Confirm what is actually happening before repairing: is the entry vanishing, or is it saved but not applied?

1. Open **Settings > Privacy & security > Recall & snapshots** and add a single test app to exclusions.
2. Close Settings completely, reopen it, and check whether the entry is still listed.
3. If it vanished, the save itself is failing — continue below. If it is listed but the app is still captured, skip to Fix 4.
4. Take a screenshot of the exclusion list now so you can compare after each fix.

### Fix 2: Check account and policy blocks

Exclusions cannot save if policy forbids them or if you are editing the wrong profile's settings.

1. Confirm you are signed in as the account that uses Recall — exclusions are per-user, not per-device.
2. Look for any 'managed by your organization' message in Recall settings; MDM policy can block exclusion changes.
3. If the device is personal and unmanaged, continue — policy is not your problem.
4. On a work device, ask IT whether Recall exclusions are centrally managed before fighting the UI.

### Fix 3: Toggle and restart to unstick the settings UI

Sometimes the settings page itself is in a bad state and needs a clean reload to write properly.

1. Remove all exclusion entries, close Settings, and restart the PC.
2. Reopen Recall settings and add one app. Close and reopen Settings to verify it stuck.
3. If it sticks now, re-add your full list one app at a time, verifying each.
4. Similar stuck-UI behavior affects other on-device AI features — [audio interfaces on ARM laptops](/articles/audio-interface-not-working-arm-laptop/) covers a parallel case with audio device settings.

### Fix 4: Re-add apps after they update

An exclusion that 'stopped working' after an app update usually needs to be removed and re-added against the new app identity.

1. Remove the non-working exclusion entry completely.
2. Launch the app once so Windows registers its current identity.
3. Re-add it to the exclusion list while it is running — running apps are easier for the picker to identify correctly.
4. Test by using the app for a few minutes, then confirm no new snapshots of it appear in the timeline.

### Fix 5: Reset Recall's configuration

When no exclusion will save, the configuration store itself is likely corrupt. Resetting it restores write ability.

1. In Recall settings, turn **Save snapshots** off.
2. Delete existing snapshots to clear the store, which shares infrastructure with the settings database.
3. Restart the PC, turn snapshot saving back on, and try adding an exclusion again.
4. If exclusions now persist, rebuild your list. If they still fail, continue to Fix 6.

### Fix 6: Repair Windows and reinstall Recall components

Persistent failure across resets means the Recall system component or the settings platform underneath is damaged.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt.
2. Install every pending Windows update — Recall ships with the OS, so updates are its repair channel.
3. If the settings platform is broadly broken, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) covers repair-install options.
4. After repair, verify exclusions save and survive a reboot before calling it fixed.

## Closing

Exclusions that will not save are a settings-storage problem, not a capture problem — and they are fixable. Verify the exact failure, rule out account and policy issues, re-add apps after updates, reset Recall's configuration, and repair Windows if needed. Once exclusions stick and survive a reboot, your privacy boundaries are back where you set them.
