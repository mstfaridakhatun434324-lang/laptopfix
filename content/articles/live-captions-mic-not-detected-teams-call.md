---
title: "How to Fix Live Captions Not Detecting Your Microphone in Teams Calls"
slug: live-captions-mic-not-detected-teams-call
date: 2026-10-28
categories: ["ai-pc"]
tags: ["live captions", "teams", "microphone", "copilot+ pc", "video calls"]
description: "Live Captions microphone not detected in Teams calls? Learn why call audio never reaches captions and how to reconnect your mic to Live Captions. with"
thumbnail: "/images/thumbs/live-captions-mic-not-detected-teams-call.webp"
faqs:
  - q: "Why does Live Captions fail like this?"
    a: >
      The most common causes are a wrong setting, an outdated driver, or a service that has not reloaded after an update. The fixes in this guide check those layers in order, starting with the simplest setting and ending with a clean repair, so you find the real cause without unnecessary reinstalls.
  - q: "Will I lose my files or settings fixing this?"
    a: >
      No. The steps in this guide preserve your files, and any reset step tells you beforehand what it clears. Back up anything important before a repair step, and test after each fix so you can stop as soon as the feature works again.
  - q: "How long does the fix usually take?"
    a: >
      Most people finish in fifteen to thirty minutes. Setting and permission fixes take minutes, while driver reinstalls and index rebuilds take longer because they need a restart and a fresh scan before you can judge the result.
  - q: "What should I do if none of the fixes work?"
    a: >
      Check for a pending Windows update and your laptop maker's latest driver, then test the feature in a clean state with other apps closed. If it still fails, the issue may be a known bug awaiting a fix, so keep Windows updated and retry after the next cumulative update.
---

Live Captions works for system audio but shows nothing during a Teams call, as if your microphone does not exist. If you have already restarted once and the problem came straight back, that actually helps narrow things down: a one-off glitch rarely survives a restart, while a setting, driver, or service fault does.

In a Teams call, Live Captions must capture your microphone through Teams' own audio pipeline, so a Teams permission, a device conflict, or an exclusive-mode setting can break that path while system captions keep working. The good news is that most of these faults are repairable without reinstalling Windows or losing your work, as long as you test in the right order instead of changing several things at once.

This guide walks through the diagnosis first and the repairs second, in the order a technician would try them. Work through the fixes in sequence, test Live Captions after each one, and stop as soon as it behaves — the fix that works tells you what was wrong, which makes the problem far less likely to return.

## Why this happens

- **Teams microphone permission off:** Teams without microphone permission cannot pass any mic audio to Live Captions.
- **Wrong input device selected:** Teams may be listening to a different microphone than the one you are speaking into.
- **Exclusive mode lock:** another app holding the microphone in exclusive mode blocks Teams from opening it.
- **Teams audio device conflict:** a headset that switches between hands-free and stereo profiles can confuse Teams' device choice.
- **Live Captions source set to system audio:** when the caption source is system audio only, microphone input is never captioned.
- **Outdated Teams or audio driver:** an old Teams build or audio driver can break the mic-to-caption handoff.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Grant Teams microphone permission

This step isolates whether the problem is a setting, a driver, or a deeper system fault. Start with the gentlest check in this section, confirm the result before moving on, and do not skip ahead — later steps assume the earlier ones are already ruled out, which keeps the repair short.

1. Open the relevant settings for Live Captions and note the current values before changing anything, so you can undo a step if needed.
2. Apply the change described for Live Captions exactly as written, without combining it with other fixes at the same time.
3. Close and reopen Teams so the new setting or repaired component loads cleanly.
4. Test Live Captions with a simple, repeatable case and note whether the symptom changed.
5. If nothing changed, undo the step and move to the next fix — do not stack untested changes.

### Fix 2: Select the correct mic in Teams settings

Most users fix this issue at this stage, because the underlying cause is usually a configuration that drifted after an update. Work through the steps carefully, test the feature after each one, and stop as soon as it works — there is no need to complete steps that no longer apply. A related feature can show the same pattern — for example, the troubleshooting steps for [obs studio npu background removal lag](/articles/obs-studio-npu-background-removal-lag/) follow the same diagnose-first order, which is worth comparing if your symptom overlaps with it.

1. Check that Teams is fully updated before judging this fix, since an old build can mask the result.
2. Make the adjustment for Live Captions in Settings, confirming each toggle actually saved.
3. Restart Teams and, if prompted, restart Windows so drivers and services reload.
4. Run the same test case you used before and compare the outcome directly.
5. Keep the change only if the test clearly improved; otherwise revert it and continue.

### Fix 3: Close apps holding the mic exclusively

If the earlier steps did not help, the fault is likely in a driver, cache, or service rather than a simple toggle. This section repairs that layer directly, so follow the order given and restart when a step asks for it — a skipped restart is the most common reason this fix appears to fail.

1. Back up anything important in Teams before repairing its data or drivers.
2. Carry out the repair for Live Captions step by step, allowing installers and scans to finish without interruption.
3. Restart Windows when the repair asks for it, even if it seems optional.
4. Test Live Captions immediately after the restart, before other apps load and compete for resources.
5. If the symptom persists, record what changed and move on — the next fix targets a different layer.

For official guidance and downloads, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 4: Set the caption source to include microphone

This step checks the account, permission, or app-data layer that quietly controls the feature. It takes a few minutes, but it separates account problems from device problems cleanly, which saves you from reinstalling software that was never at fault. The same layering applies elsewhere on Copilot+ PCs: the guide to [touchscreen pen pressure not working ai laptop](/articles/touchscreen-pen-pressure-not-working-ai-laptop/) shows how a driver or service fault can masquerade as a feature fault, and the checks there complement this fix.

1. Sign out of Teams if the fix involves your account, then sign back in with the correct Microsoft account.
2. Verify the permission or account setting for Live Captions shows the expected value after signing in.
3. Close Teams completely from Task Manager if it lingers in the background, then reopen it.
4. Test Live Captions with the same example that failed before, under the same conditions.
5. If the test passes, leave the setting as is; if not, the fault lies in another layer.

### Fix 5: Update Teams and audio drivers

When simpler fixes fail, a clean repair of the app or its data is usually what remains. This section walks through that repair safely, preserving your files and settings where possible, and tells you when a full reinstall is genuinely the faster path. If you also use other AI features on this laptop, the experience with [overwatch 2 arm laptop issues fix](/articles/overwatch-2-arm-laptop-issues-fix/) is a useful cross-check — when several features fail together, a shared driver or runtime is usually the common cause.

1. Open Device Manager or the app settings for Live Captions and confirm which driver or version is currently installed.
2. Download the correct update or repair package from the maker's official support pages, not a third-party driver site.
3. Install it as administrator and let the process complete, keeping the laptop awake and plugged in.
4. Restart, then test Live Captions before reinstalling anything else.
5. If the installer reports an error, note the exact message — it points to the next fix.

### Fix 6: Test the mic in Windows sound settings

This final repair step addresses the stubborn cases: a corrupted component, a stale driver, or a service that needs a full reset. Complete it methodically, test the feature thoroughly afterwards, and keep a note of which step worked in case the issue returns after a future update.

1. Reset or reinstall the component behind Live Captions only after the gentler fixes have been tried.
2. Follow the reset prompts in Settings, choosing to keep your files where that option is offered.
3. After the reset, set up Live Captions from scratch with default settings before customising it again.
4. Test with a basic case first, then reapply your preferred settings one at a time.
5. If the clean setup works, the old configuration was the culprit; rebuild it gradually.

## Closing

Once Live Captions is working again, keep the winning fix in mind: if the fault was a setting, check it after major updates; if it was a driver, prefer your laptop maker's driver over a generic one; and if it was a service or cache, a restart after updates is cheap insurance. That habit keeps a one-time repair from becoming a recurring chore, and it leaves your Copilot+ PC's AI features ready whenever you need them.
