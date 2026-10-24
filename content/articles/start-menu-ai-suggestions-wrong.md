---
title: "How to Fix Wrong AI Suggestions in the Windows 11 Start Menu"
slug: start-menu-ai-suggestions-wrong
date: 2026-10-24
categories: ["ai-pc"]
tags: ["start menu", "ai suggestions", "recommended", "copilot+ pc", "windows 11"]
description: "Start menu Recommended section showing wrong or irrelevant files and apps? Fix Windows 11 AI suggestions with these privacy, index, and personalization resets."
thumbnail: "/images/thumbs/start-menu-ai-suggestions-wrong.webp"
faqs:
  - q: "Why does the Start menu recommend files I never use?"
    a: >
      The Recommended section learns from your activity history — but it can also surface files from shared folders, synced OneDrive content, or another user's activity on a shared PC. Clearing the activity history and checking which folders are indexed usually corrects the suggestions within a day or two.
  - q: "Can I turn off AI recommendations in the Start menu completely?"
    a: >
      Yes. Go to Settings > Personalization > Start and toggle off "Show recently added apps", "Show recently opened items", and "Show recommendations for tips, shortcuts, new apps, and more". The pinned apps stay; only the Recommended section goes quiet.
  - q: "Are my Start menu suggestions sent to Microsoft?"
    a: >
      The on-device recommendation model on Copilot+ PCs processes your activity locally. However, if you have activity history syncing enabled across devices, usage data travels with your Microsoft account. You can disable that sync in Settings > Privacy & security > Activity history.
  - q: "How long does it take for suggestions to improve after a reset?"
    a: >
      After clearing history and retraining, give it 24 to 72 hours of normal use. The recommendation model needs fresh activity data to learn your patterns — judging it after an hour will always look wrong.
---

Your Start menu's Recommended section keeps suggesting a spreadsheet you opened once three months ago, a random installer from Downloads, and an app you uninstalled. Meanwhile the document you actually open every morning is nowhere to be seen. The "smart" suggestions feel like they belong to a stranger.

The Recommended section blends two things: Windows' activity tracking (recent files, frequent apps) and, on Copilot+ PCs, an on-device model that tries to predict what you want next. When the underlying data is polluted — stale history, shared-folder noise, a corrupted personalization cache, or synced activity from another device — the predictions go sideways. It is a data problem, not a broken feature.

This guide gives you six fixes in order: audit what is feeding the suggestions, clear the polluted data, fix the indexing behind it, check the AI personalization layer, reset the Start experience, and rule out cross-device contamination. Test over a day or two of normal use after the data fixes. Suggestion weirdness often travels with other shell oddities, like [lock screen widgets misbehaving](/articles/lock-screen-widgets-not-working/), since they share the same personalization backend.

## Why this happens

- **Stale activity history:** Windows keeps months of activity records; old, irrelevant entries can keep resurfacing long after your habits changed.
- **Polluted data sources:** Shared folders, OneDrive-synced libraries, and Downloads full of installers feed the model junk that looks like "recent files."
- **Synced activity from other devices:** With timeline sync on, activity from your desktop or another laptop bleeds into this PC's recommendations.
- **Corrupted personalization cache:** The Start menu's local suggestion cache can corrupt after updates, freezing recommendations on a stale snapshot.
- **Copilot+ prediction model not retrained:** The on-device model needs the AI components healthy and enough fresh data; a broken NPU driver or missing model leaves suggestions running on dumb heuristics.
- **Wrong folders indexed:** If search indexing includes folders full of installers or temp files, their contents pollute both search and recommendations.
- **Multiple users on one PC:** On shared machines, another user's activity can leak into suggestions when profiles or folder permissions blur.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Audit and trim what feeds the suggestions

Before clearing anything, look at what the model is actually eating. Most "wrong suggestion" cases are explained in thirty seconds by a Downloads folder full of installers or a shared drive in the library.

1. Open **Settings > Personalization > Start** and note which toggles are on — "recently opened items" is the main feeder.
2. Check your indexed locations in **Settings > Privacy & security > Searching Windows** — remove folders full of installers, temp files, or other noise.
3. Look at File Explorer's **Quick Access** and your **Recent** items (type `shell:recent` in the Run dialog) to see exactly what Windows thinks you use.
4. Move or delete the junk: installers you already ran, files you opened once, anything from a shared folder you do not care about.
5. Give it 24 hours of normal use — the model re-weights quickly once the noise is gone. Wi-Fi chipset quirks can also stall background learning on AI laptops, similar to [MediaTek Filogic Wi-Fi 7 issues](/articles/mediatek-filogic-wifi7-issues-laptop/).

### Fix 2: Clear activity history and retrain the model

When the data itself is stale, trimming is not enough — you need a clean slate. Clearing activity history wipes the polluted record and forces the recommendation model to relearn from your current habits.

1. Go to **Settings > Privacy & security > Activity history** and click **Clear history**.
2. Uncheck **Store my activity history on this device** temporarily if you want the cleanest restart — you can re-enable it later.
3. Turn off **Let Windows sync my activities from this PC to the cloud** to stop other devices polluting this one.
4. In **Settings > Personalization > Start**, toggle the recommendation options off and back on to flush the cached suggestions.
5. Use the PC normally for 2–3 days before judging — the model needs fresh activity to learn. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document what activity history controls.

### Fix 3: Fix the search index behind the suggestions

Recommendations and search share the same index. A stale or damaged index feeds both bad data — files that no longer exist keep getting suggested because the index still thinks they are recent and relevant.

1. Open **Settings > Privacy & security > Searching Windows > Advanced indexing options**.
2. Click **Advanced**, then **Rebuild**, and let the index rebuild while the laptop is plugged in.
3. Confirm the indexed locations include your real working folders (Documents, Desktop) and exclude noise folders.
4. Under **File Types**, make sure your actual document types are set to index contents, not just properties.
5. After the rebuild completes, clear activity history once more (Fix 2) so the fresh index and fresh history start together.

### Fix 4: Check the Copilot+ AI personalization layer

On Copilot+ PCs, smarter suggestions come from the on-device model on the NPU. If that layer is broken, suggestions fall back to crude recency heuristics — which is exactly when they start looking random and wrong.

1. Open **Device Manager > Neural processors** and confirm the NPU has no warning icon; reinstall the driver from your maker's support page if it does.
2. Install all Windows updates including optional drivers — the AI components arrive as separate downloads.
3. Leave the PC idle, plugged in, and on Wi-Fi for an hour so background AI downloads complete.
4. Use the PC normally for a couple of days; on-device models adapt locally and improve with fresh patterns.
5. If suggestions stay random after a week, the fallback heuristics are all you have got on this build — the toggles in Fix 2's step 4 let you quiet the section entirely. Filtering failures elsewhere on Copilot+ PCs share this NPU dependency, like [Recall not filtering sensitive info](/articles/recall-not-filtering-sensitive-info/).

### Fix 5: Reset the Start menu experience

When the data is clean and the index is fresh but suggestions are still frozen on the same wrong items, the Start menu's own cache is corrupted. Re-registering the Start experience package rebuilds it.

1. Open **Settings > Apps > Installed apps** and find the Start-related system component (listed as a system component on newer builds).
2. Use **Advanced options > Repair** first, then test for a day.
3. If that fails, run in **Terminal (Admin)**: `Get-AppXPackage -AllUsers Microsoft.Windows.StartMenuExperienceHost | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
4. Restart the PC and check the Recommended section — it should start empty and rebuild.
5. Re-enable only the Start toggles you actually want in **Settings > Personalization > Start**.

### Fix 6: Stop cross-device and cross-user contamination

If suggestions keep showing files from your desktop, your old laptop, or another person, the data source is external — no amount of local clearing will stick until the sync stops.

1. On every Windows device on your Microsoft account, go to **Settings > Privacy & security > Activity history** and disable cloud sync.
2. Clear history on each device, not just this one — synced records re-upload otherwise.
3. On a shared PC, make sure other users have their own accounts and that your libraries do not include their folders.
4. Check OneDrive: files synced from another machine appear "recent" when they sync, not when you open them — pause syncing folders you do not use here.
5. After a week of clean single-device data, the suggestions should finally reflect your actual habits on this PC.

## Closing

Wrong Start menu suggestions are a data hygiene problem: stale history, noisy folders, synced contamination, or a broken on-device model feeding bad predictions. Clear the polluted inputs, fix the index, let the model relearn for a few days, and the Recommended section starts looking like your actual workday. And if the predictions never earn your trust, the toggles in Settings > Personalization > Start will silence them for good — a quiet Start menu is a valid choice.
