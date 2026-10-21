---
title: "How to Fix Recall Snapshots Paused on Windows 11"
slug: recall-snapshots-paused-fix
date: 2026-10-21
categories: ["ai-pc"]
tags: ["recall snapshots paused", "recall not working", "windows recall", "snapshots stopped", "ai pc", "windows 11"]
description: "Recall snapshots paused on your Copilot+ PC? Follow step-by-step fixes to resume snapshot capture, fix storage and policy blocks, and get Recall recording."
thumbnail: "/images/thumbs/recall-snapshots-paused-fix.webp"
faqs:
  - q: "Why does Recall pause snapshots by itself?"
    a: "Recall pauses automatically when disk space runs low, when Storage Sense cleans its snapshot folder, when battery saver or a policy intervenes, or when you switch to an unsupported state like a local-only account issue. The pause banner usually names the reason."
  - q: "Does paused mean my old snapshots are deleted?"
    a: "No. Pausing only stops new captures. Your existing timeline stays searchable until snapshots age out or you delete them manually. Resume capture and the timeline simply continues from today."
  - q: "How much disk space does Recall need?"
    a: "Microsoft reserves snapshot storage based on your drive size, but Recall pauses when free space gets tight. Keeping at least 25–50 GB free on the system drive is a safe rule of thumb on Copilot+ PCs."
  - q: "Can Storage Sense delete my Recall snapshots?"
    a: "Storage Sense does not target the Recall snapshot store directly, but aggressive cleanup settings and third-party cleaners can remove the underlying data. Exclude Recall's storage from any cleaner you run."
---

Recall is supposed to quietly photograph your screen every few seconds, building a searchable timeline of everything you did. Then one day you notice the timeline has gaps — and the Recall window says snapshots are paused. Days of activity, unrecorded.

The pause is usually Recall protecting itself rather than a bug: low disk space, a settings toggle flipped by an update, a policy change, or a conflict with another app. The banner often hints at the reason, but not always, and the resume button does not always work on the first click.

This guide gives you six fixes in order: read the actual pause reason, clear the storage and settings blocks, rule out policy interference, and repair Recall itself. Work through them in sequence and check whether new snapshots start appearing after each step.

## Why this happens

- **Low disk space:** Recall pauses captures when free space drops too far, to avoid filling your drive with snapshots. This is the most common cause on 256 GB machines.
- **Snapshot saving toggled off:** A Windows update, a settings sync, or an accidental click can flip **Save snapshots** off in Recall settings — pausing looks identical to a failure.
- **Storage Sense or disk cleaners:** Aggressive cleanup tools can remove snapshot data or its storage allocation, and Recall pauses rather than record into a broken store.
- **Policy or MDM restriction:** Work or school devices managed by Intune can have Recall disabled by policy, which presents as permanently paused snapshots.
- **App conflict crashing the capture service:** If another app destabilizes the shell — the same class of problem as [Click to Do crashing File Explorer](/articles/click-to-do-crashes-file-explorer/) — the Recall capture pipeline can stall and report itself paused.
- **Corrupt snapshot store:** A damaged local database makes Recall pause new writes instead of corrupting existing history further.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the pause reason and resume from Recall settings

Recall usually tells you why it paused — the fix is often one toggle away. Do not skip this: guessing wastes the time a thirty-second check would save.

1. Open Recall and look for the pause banner or status message; note the exact reason it gives (storage, setting, policy).
2. Go to **Settings > Privacy & security > Recall & snapshots** and confirm **Save snapshots** is switched on.
3. Check the snapshot storage allocation shown on the same page — if it shows zero or an error, the store itself needs attention (Fix 4).
4. Click any **Resume** or **Turn on** control, wait a few minutes of normal PC use, then reopen Recall to see if new snapshots appear.

### Fix 2: Free up disk space on the system drive

Low free space is the number one pause trigger, and Recall will not resume until the pressure eases — toggling settings does nothing while the drive is full.

1. Open **Settings > System > Storage** and check free space on C:. Aim to free at least 25–50 GB.
2. Run **Cleanup recommendations** on the same page and remove large unused apps, old downloads, and previous Windows installations.
3. Empty the Recycle Bin and clear temporary files — quick wins that often free several gigabytes.
4. Wait 10–15 minutes after freeing space, then resume snapshots in Recall settings. The service re-checks storage on its own schedule, not instantly.

### Fix 3: Stop Storage Sense and cleaners from touching Recall

If snapshots pause again days after you fix them, something is repeatedly damaging the snapshot store — usually an overzealous cleaner.

1. Go to **Settings > System > Storage > Storage Sense** and review what it cleans automatically; turn off aggressive automatic cleanup while troubleshooting.
2. If you run third-party cleaners (CCleaner-style tools), open their settings and exclude Recall, Windows AI, and snapshot-related entries from cleaning.
3. Check the snapshot storage allocation in Recall settings again — if it shrank on its own, a cleaner is the likely culprit.
4. Resume snapshots and monitor for a few days. Stable capture after excluding cleaners confirms the diagnosis.

### Fix 4: Reset the Recall snapshot store

A corrupt local snapshot database makes Recall pause writes to protect your existing history. Resetting the store gives it a clean database to write into.

1. In **Settings > Privacy & security > Recall & snapshots**, look for the option to delete snapshots or reset Recall data.
2. Choose to delete snapshots — this clears the corrupt store. Your files and apps are untouched; only the Recall timeline resets.
3. Toggle **Save snapshots** off and back on to force Recall to reinitialize its storage.
4. Use the PC normally for 15–30 minutes, then check Recall for fresh snapshots. New captures confirm the store was the problem.

### Fix 5: Rule out policy, account, and permission blocks

On managed devices, or when permissions break, Recall pauses and no settings toggle will override it. Identify the block before fighting it.

1. Check **Settings > Privacy & security > Recall & snapshots** for any message about your organization managing the feature — that means Intune policy, and only your IT admin can change it.
2. If the microphone or screen-capture permission prompts appear broken, the [microphone permission fix](/articles/copilot-microphone-permission-denied/) covers the same permission-repair pattern for AI features.
3. Verify you are signed in with the account Recall was set up under; switching accounts can pause capture for the other profile.
4. On a personal, unmanaged PC with no policy message, continue to Fix 6 — the app itself likely needs repair.

### Fix 6: Repair Recall through Windows Update and a restart cycle

When settings, storage, and policy all check out, the Recall system component itself may be damaged — and since it ships with Windows, Windows Update is the repair path.

1. Go to **Settings > Windows Update** and install every pending update, then restart. If Windows Update itself misbehaves, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) walks through the built-in troubleshooters.
2. After restarting, open Recall settings, toggle **Save snapshots** off, restart once more, and toggle it back on — the double restart clears stuck service states.
3. If the NPU shows [zero percent usage](/articles/npu-stuck-at-zero-percent-usage/) during what should be active capture, the underlying AI pipeline may need the driver-side fixes in that guide.
4. Use the PC for 30 minutes and verify the timeline fills in. Persistent pausing after all six fixes points to a Windows repair install as the final option.

## Closing

Recall snapshots pause for protective reasons far more often than from real breakage — low disk space, a flipped toggle, or a cleaner eating the snapshot store. Free the space, exclude Recall from cleaners, reset the store if it is corrupt, and only then suspect deeper damage. Once captures resume, keep an eye on free space and the timeline will quietly keep building.
