---
title: "Eye Contact Effect Not Working in Studio Effects? Fix It"
slug: eye-contact-effect-not-working
date: 2026-10-19
categories: ["ai-pc"]
tags: [windows-studio-effects, eye-contact, windows-11, copilot-plus-pc, camera, troubleshooting]
description: "Eye contact effect not working in Windows Studio Effects? Fix gaze correction with our camera, lighting, environment, and driver troubleshooting steps."
thumbnail: "/images/thumbs/eye-contact-effect-not-working.webp"
faqs:
  - q: "Why does eye contact not work with my glasses on?"
    a: >
      Glasses glare hides your eyes from the gaze-correction model. Reducing screen brightness, adjusting angles, and improving lighting usually fix it — the model needs a clear view of your eyes.
  - q: "How far off-axis can eye contact correct?"
    a: >
      The correction handles natural note-reading angles near the screen. Staring far to the side exceeds the model's plausible range — keep reference material close to the display.
  - q: "Does eye contact work in all video apps?"
    a: >
      It works wherever the Windows camera stream flows, but some apps apply their own processing that can conflict. Test in the Windows camera preview first to isolate.
  - q: "Is the eye contact effect supposed to be subtle?"
    a: >
      Yes, deliberately — it should look natural, not like staring. If you cannot tell it is on, compare preview recordings with it on and off rather than judging live.
---
Eye contact is the subtlest Studio Effect — it gently corrects your gaze so you appear to look at the camera while reading notes. When it fails, there is no dramatic error; you just look like you are reading, and nobody can tell the effect is even on. It is easy to assume it never worked, when actually a specific condition is defeating it.

Gaze correction needs a clear view of your eyes, which makes it the most environmentally sensitive effect: glasses glare, looking far off-axis, and poor lighting all defeat the model. Software causes exist too, but the environment dominates here more than with any other effect.

This guide covers both sides, environment first. If Voice Focus is also failing, see [Voice Focus not working](/articles/voice-focus-not-working-windows-11/) — the NPU is the likely shared cause. If no effects work at all, start with [Windows Studio Effects not working](/articles/windows-studio-effects-not-working/). And if you are worried about the power cost of always-on AI, see [Live Captions draining battery](/articles/live-captions-draining-battery/) for the broader picture.

## Why this happens

- **Glasses glare or reflections:** Reflections hide the eyes from the gaze model — the single most common environmental cause.
- **Looking too far off-axis:** The correction has limits; staring far to the side exceeds what the model can plausibly adjust.
- **Poor or harsh lighting:** Deep shadows over the eyes or harsh side light break eye detection.
- **NPU or camera driver issues:** The standard software causes apply here too, though less often than environment.
- **Effect intensity too subtle to notice:** At low intensity the correction is deliberately subtle — users assume it is broken.
- **Conflicting app eye-contact features:** Some conferencing apps now bundle their own gaze correction that conflicts.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix the environment for eye detection
Gaze correction lives or dies on seeing your eyes clearly, which makes the environment decisive: glasses glare is the number one killer, followed by sitting far off-axis and harsh side lighting. These defeat the model before any software cause matters. A quick test with glasses off or lights adjusted tells you in seconds whether you are fighting physics or software.
1. Reduce glasses glare: adjust screen brightness and angle, or shift your seating relative to light sources.
2. Face the camera reasonably directly; keep notes near the screen, not far to the side.
3. Ensure even, frontal lighting on your face — no deep eye shadows.
4. Test with glasses off once to confirm glare was the issue.

### Fix 2: Turn up the effect and verify it is on
The effect is deliberately subtle — natural-looking correction, not a stare — and at low intensity many users cannot tell it is working. Before declaring it broken, raise the intensity if the option exists and compare preview recordings with the effect on versus off. Judging it live is unreliable; the side-by-side recording is the honest test.
1. In Settings > Bluetooth & devices > Cameras, confirm eye contact is toggled on.
2. If an intensity option exists, raise it and watch the preview.
3. Record a short preview clip looking at notes, then compare with the effect off.
4. The difference should be visible in the preview once conditions are right.

### Fix 3: Update NPU and camera drivers
Beneath the environmental causes, the standard software layer still applies: the NPU driver powers the gaze model and the camera driver feeds it. When the scene is good and the effect still does nothing, driver repair is the next step. It resolves the minority of cases that are genuinely software — worth doing, just not first.
1. Update the NPU driver from your laptop maker's support page.
2. Update the camera driver via Device Manager.
3. Restart and retest in the Windows camera preview.
4. Driver fixes resolve the minority of cases that are not environmental.

### Fix 4: Disable competing gaze correction
Conferencing apps increasingly bundle their own gaze correction, and two correctors on one stream produce uncanny results or cancel each other out. The fix is picking one pipeline: disable the app's version and keep Windows', or vice versa. Testing with the app closed in the Windows preview isolates which one was misbehaving.
1. Check your conferencing app's video settings for its own eye-contact feature and turn it off.
2. Use only the Windows Studio Effects version.
3. Test in the Windows preview with the app closed to isolate.
4. Pick one pipeline and stick with it.

### Fix 5: Check the camera feed quality
A smudged lens, a low-light fallback mode, or a compressed stream softens exactly the eye region the model needs sharp. Cleaning the lens takes five seconds and is embarrassingly often the fix. The prerequisite for every camera effect is a crisp, well-lit feed — verify the feed before blaming the effect.
1. Confirm the camera is not in a low-light or low-resolution fallback mode.
2. Clean the camera lens — smudges soften the eye region critically.
3. Close bandwidth-heavy apps if the preview looks compressed.
4. A crisp, well-lit feed is the prerequisite for every effect.

### Fix 6: Calibrate with the preview at call distance
Gaze models are tuned for typical call distances; calibrating at your actual seating position matters. Toggling the effect while watching the preview at your real distance — then adjusting seating to the model's sweet spot — turns a vague 'not working' into a tuned, working setup. Small positional changes make outsized differences here.
1. Open the camera preview and sit at your normal call distance.
2. Toggle eye contact off and on while watching the preview.
3. Move slightly closer and farther to find the model's sweet spot.
4. Adjust your seating permanently to that distance for consistent results.

### Fix 7: Update the graphics driver too
The effect pipeline composites through the GPU, and stale graphics drivers glitch it in ways people invariably blame on the camera. Updating the GPU driver — from Intel, AMD, or NVIDIA, or the laptop maker's tested build — fixes a whole class of effect glitches that have nothing to do with the NPU or the lens. It belongs in the checklist precisely because nobody suspects it.
1. Update the GPU driver from Intel, AMD, or NVIDIA directly.
2. Prefer the laptop maker's tested version if available.
3. Restart and retest eye contact in the preview.
4. Graphics driver updates fix a class of effect glitches people blame on the camera.

## Closing

Eye contact failures are environmental far more often than software: glare, angle, and lighting defeat the gaze model before drivers ever matter. Fix the scene first, then verify drivers. When the preview shows the correction working, you will know the effect was fine all along — it just could not see your eyes. See also [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for official Studio Effects guidance.
