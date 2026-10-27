---
title: "How to Fix Click to Do After the Windows 11 24H2 Update"
slug: click-to-do-not-working-after-24h2-update-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["click to do", "windows 11 24h2", "windows update", "copilot+ pc", "arm laptop", "troubleshooting"]
description: "Restore Click to Do after the Windows 11 24H2 update with step-by-step fixes for reset settings, drivers, corrupted update files, and Copilot+ repair."
thumbnail: "/images/thumbs/click-to-do-not-working-after-24h2-update-fix.webp"
faqs:
  - q: "Why did the 24H2 update break Click to Do?"
    a: "Major Windows updates can reset feature settings, replace NPU and graphics drivers with generic versions, and leave update files half-installed. Any of these can silently disable Click to Do even though the rest of Windows looks fine."
  - q: "Should I roll back the 24H2 update to get Click to Do back?"
    a: "Try the fixes in this guide first. Rolling back is a last resort because it removes security fixes, and it is only available for ten days after the update. Most Click to Do failures after 24H2 are fixed by re-enabling the feature and repairing drivers."
  - q: "Does 24H2 remove Click to Do from non-Copilot+ PCs?"
    a: "Click to Do is a Copilot+ PC feature, so on a PC without an NPU it was never fully available. If it appeared briefly before 24H2, that was likely a preview or partial rollout, and the update restored the normal behaviour."
  - q: "How long does a Click to Do repair take after 24H2?"
    a: "Most fixes take under fifteen minutes: re-enabling the feature, checking drivers, and running the update troubleshooter. A full in-place repair of Windows takes longer but is rarely needed for this one feature."
---

Click to Do worked last week, then the Windows 11 24H2 update installed overnight — and now the Windows-key-plus-click gesture does nothing. No error, no warning, just silence where the Rewrite and Summarize menu used to appear. You did not break anything; the update changed something underneath the feature.

Major Windows updates are the most common Click to Do killers. They reset feature toggles, swap validated NPU drivers for generic ones, and sometimes leave the AI components themselves in a half-updated state. The feature is still on your PC — it just needs to be reconnected.

This guide works in update-repair order: re-enable what 24H2 reset, fix what it replaced, then repair what it damaged. Test the gesture after each fix so you stop as soon as Click to Do returns.

## Why this happens

- **Feature toggle reset by the update:** 24H2 can switch Click to Do off, or reset its activation shortcut, during the upgrade — the feature looks broken when it is simply disabled.
- **Generic NPU or graphics driver installed:** The update may replace your PC maker's validated drivers with generic ones that do not expose the NPU features Click to Do needs.
- **Copilot+ components left half-updated:** If the update was interrupted by sleep, low battery, or a restart, the on-device AI packages can end up mismatched with the new Windows build.
- **Corrupted update cache or system files:** Damaged files from the upgrade process can break the service Click to Do depends on without affecting everyday apps.
- **Privacy settings reverted:** Updates sometimes restore default privacy settings, which can re-block the AI features and app permissions Click to Do uses.
- **Third-party software conflict after the update:** Security tools, clipboard managers, and overlay apps that worked before 24H2 can clash with the new build's input handling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-enable Click to Do and confirm the gesture

The first suspect after any major update is a reset setting, not a broken feature. This check takes a minute and fixes a surprising number of post-24H2 cases, so never skip it for a deeper repair.

1. Open **Settings > System > Click to Do** and confirm the feature is switched **On** — switch it off and back on if it already looks on, to force a fresh registration.
2. Confirm the activation gesture shown there, normally holding the **Windows key** and clicking selected text.
3. Open Notepad, type a sentence, select it, and try the gesture there — Notepad is the simplest test app, free of Word or browser complications.
4. If Click to Do works in Notepad but not in one app, the problem is app-specific; see [Click to Do not working in Word](/articles/click-to-do-not-working-in-word-fix/) for the Word-side version of this problem.
5. If it fails everywhere, keep working through the fixes below — the cause is system-wide, which is exactly what an update causes.

### Fix 2: Install all follow-up updates and restart properly

Checking for those updates before deeper repairs saves a lot of wasted effort.

1. Open **Settings > Windows Update** and click **Check for updates**, installing everything offered, including optional updates.
2. Look under **Advanced options > Optional updates** for driver updates for your NPU and graphics, and install those too.
3. Restart from **Start > Power > Restart** — do not just close the lid or use Sleep, which does not complete pending update work.
4. After the restart, wait two minutes for background services to settle, then test Click to Do in Notepad.
5. If Windows Update itself errors out, run the built-in troubleshooter at **Settings > System > Troubleshoot > Other troubleshooters > Windows Update** before moving on. A related missing-action problem after updates is covered in [Click to Do text actions missing](/articles/click-to-do-text-actions-missing/), which helps narrow down whether the whole feature or just one action set broke.

### Fix 3: Restore the correct NPU and graphics drivers

If 24H2 replaced your drivers, Click to Do loses the hardware it runs on.

1. Open **Device Manager** and expand **Neural processors** and **Display adapters**, noting the driver names and dates.
2. If either shows a generic Microsoft driver, or a date from the 24H2 install day, download the latest drivers from your PC maker's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Install the NPU driver first, then the graphics driver, restarting when each installer asks.
4. After both restarts, test Click to Do in Notepad and in an image, since image actions stress the NPU more than text actions.
5. If your PC maker has no newer driver yet, roll back just that driver in Device Manager via Properties > Driver > Roll Back Driver.

### Fix 4: Repair update damage with system file checks

A 24H2 upgrade that was interrupted, or that hit a disk error, can leave system files damaged in ways that only affect features like Click to Do. The built-in repair tools scan and rebuild those files without touching your personal data.

1. Right-click **Start**, choose **Terminal (Admin)**, and confirm the permission prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to finish — this can take ten to twenty minutes, so keep the PC plugged in.
3. When DISM finishes, run `sfc /scannow` in the same window and wait for its result.
4. Restart the PC, then test Click to Do again in Notepad.
5. If either tool reports damage it could not repair, an in-place repair install of Windows 11 (using the installer from Microsoft's Windows 11 download page and choosing **Keep personal files and apps**) is the next step.

### Fix 5: Check privacy settings and clean-boot for conflicts

Updates can revert privacy defaults, and older third-party tools can clash with the new build. A clean boot separates a Windows problem from a third-party one in minutes.

1. Open **Settings > Privacy & security** and review the settings for AI features, clipboard, and app permissions that Click to Do relies on.
2. Press **Windows + R**, type `msconfig`, and on the **Services** tab check **Hide all Microsoft services**, then click **Disable all**.
3. On the **Startup** tab, open Task Manager and disable all startup items, then restart the PC.
4. Test Click to Do in this clean state. If it works, re-enable services and startup items in small groups, restarting and testing after each group, until the culprit returns.
5. Once you identify the conflicting app — often a clipboard manager, overlay, or security tool — update it to a 24H2-compatible version or leave it disabled. The same conflict-hunting approach helps with other missing Click to Do pieces, such as [Click to Do Create image missing](/articles/click-to-do-create-image-missing-fix/), where one action set vanishes while the rest survive.

### Fix 6: Roll back 24H2 as a last resort

If every repair fails and Click to Do worked before 24H2, rollback is a legitimate last resort — but only within ten days of the update, and only after the fixes above, because it also removes 24H2 security improvements.

1. Open **Settings > System > Recovery** and look for **Go back** under Previous version of Windows.
2. If **Go back** is present, click it, choose a reason, and follow the prompts — the PC will restart several times.
3. After rollback, test Click to Do immediately, before installing other updates, to confirm the update was the cause.
4. If **Go back** is missing, the ten-day window has passed; stay on 24H2 and repeat Fix 4's in-place repair instead.
5. If rollback restores Click to Do, pause Windows updates for a week so 24H2 does not reinstall before a fix ships. Broader post-update AI instability is discussed in [Notion AI issues on ARM laptops](/articles/notion-ai-arm-laptop-issues-fix/).

## Closing

A Click to Do failure that starts the morning after 24H2 is almost never permanent damage — it is a reset toggle, a swapped driver, or a half-finished update component. Re-enable the feature, restore the maker's drivers, repair system files, and only consider rollback when every repair has failed.
