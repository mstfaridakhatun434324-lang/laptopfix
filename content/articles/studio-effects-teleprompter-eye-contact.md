---
title: "Studio Effects Teleprompter Eye Contact Looking Fake? Fix Guide"
slug: studio-effects-teleprompter-eye-contact
date: 2026-10-22
categories: ["ai-pc"]
tags: [studio-effects, eye-contact, teleprompter, windows-11, copilot-plus-pc, camera]
description: "Studio Effects teleprompter eye contact looking unnatural on Windows 11? Fix gaze correction while reading scripts with our camera, lighting, and setup steps."
thumbnail: "/images/thumbs/studio-effects-teleprompter-eye-contact.webp"
faqs:
  - q: "Why does eye contact look strange when I read a teleprompter script?"
    a: >
      Gaze correction models have a limited plausible range. When your eyes move rapidly across script text positioned far from the camera, the corrected gaze can look jerky or artificial. Moving the script closer to the camera and slowing your reading pace usually fixes the uncanny look.
  - q: "Should I place my teleprompter text right under the camera?"
    a: >
      Yes — the closer your eyes are to the camera axis, the less correction the model has to apply. Position the script window directly beneath or beside the webcam, and keep the reading angle as narrow as possible for the most natural result.
  - q: "Does eye contact work with teleprompter hardware beam-splitter glass?"
    a: >
      It can, but beam-splitter glass reduces image clarity and can confuse gaze detection. If the effect behaves oddly through teleprompter glass, test with the effect on and off — some users get better results turning it off and relying on the hardware alone.
  - q: "Can I use eye contact and portrait blur together while presenting?"
    a: >
      Yes, both effects can run simultaneously since they use the same NPU pipeline. Just keep in mind that stacking effects increases NPU load, so make sure your NPU driver is current before relying on the combination in a live recording.
---
Reading from a teleprompter while looking engaged is exactly what Studio Effects eye contact was built for — you read your script, and the AI corrects your gaze so you appear to speak directly to the camera. When it works, the result is seamless. When it doesn't, you get the worst of both worlds: a jerky, artificial stare that distracts from everything you're saying.

The teleprompter scenario stresses gaze correction harder than anything else. Your eyes dart across lines of text and drop to the next line while the model smooths all of that into a steady, believable gaze — and when the script sits far from the camera or the lighting is poor, the correction overshoots or lags and the illusion breaks.

This guide fixes teleprompter-specific eye contact problems on Windows 11 AI PCs, starting with the setup mistakes behind most of them. If eye contact looks off even without a script, start with [Eye contact effect not working](/articles/eye-contact-effect-not-working/). If the effect stutters during recordings, the NPU may be the bottleneck — see [NPU missing after 25H2 update](/articles/npu-missing-after-25h2-update/). And if Recall's exclusions misbehave alongside your presentation workflow, [Recall app exclusions not saving](/articles/recall-app-exclusions-not-saving/) covers that fix.

## Why this happens

- **Script positioned too far from the camera:** Every inch of distance forces the model to bend your gaze further — and the faker it looks.
- **Rapid eye movement across text:** Fast scanning and line jumps exceed what the gaze model can plausibly smooth.
- **Small or dim script text:** Squinting to read tiny text changes your eye geometry and defeats detection.
- **Glasses glare from bright setup lights:** Teleprompter lighting often bounces off glasses, hiding your eyes from the model.
- **NPU throttling under stacked effects:** Eye contact plus blur plus auto-framing can overload the NPU, making correction lag.
- **Low camera resolution or tight auto-framing crops:** Heavy crops degrade the eye region the model works with.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Move the script next to the camera
Script position is the biggest lever on natural-looking gaze correction. Park the teleprompter window directly under or beside the webcam, as close to the camera axis as possible. Test before and after — most people see an immediate, obvious improvement from this single change.
1. Shrink the teleprompter window and drag it directly beneath or beside the webcam.
2. Record a 30-second test reading with the script in the new position.
3. Compare against a recording with the script in the old position.
4. If your app supports transparent overlay mode, float the text over the camera area.
5. Keep the reading angle narrow — never park the script at the screen's far edge.

### Fix 2: Make the text big, bright, and slow
Small, dim, fast-moving text makes your eyes dart and squint, which strains the correction model. Calm, predictable eye movement gives the best results: large readable text, comfortable brightness, and a scroll speed slightly below your speaking pace.
1. Increase the font size until you can read comfortably without leaning in.
2. Set scroll speed slightly slower than your natural speaking pace.
3. Use high-contrast text, such as bright text on a dark background.
4. Rehearse once before recording so fewer re-reads interrupt your flow.
5. Keep your eyes on the reading-position indicator instead of scanning ahead.

### Fix 3: Fix lighting and kill glasses glare
Eye contact needs a clean view of both eyes, so glare control matters more in teleprompter setups than in normal calls. Check the Windows camera preview while wearing your presentation glasses and reposition lights so they illuminate your face without bouncing into the lens.
1. Open the camera preview and check for reflections on your glasses in your setup lighting.
2. Angle key lights slightly to the side or above eye level to bounce glare away.
3. Reduce screen brightness a notch — the screen itself is a common glare source.
4. Test one recording with glasses off; if the effect suddenly looks natural, glare was the culprit.
5. Consider tilting glasses slightly downward for the duration of the recording.

### Fix 4: Unstack effects to free the NPU
Eye contact, background blur, and auto-framing share one NPU pipeline. Stack them and the NPU can throttle, which shows up as lagging gaze correction that trails your eyes. For teleprompter recordings, eye contact is the priority — strip the rest.
1. Turn off auto-framing for teleprompter recordings; you are stationary anyway.
2. Switch portrait blur to a plain static background, or turn it off.
3. Keep eye contact as the only active effect and re-record your test.
4. If the gaze looks smoother, you were NPU-bound — keep the stack light.
5. Update the NPU driver from your laptop maker's support page for maximum headroom.

### Fix 5: Calibrate with a real recording
Never judge eye contact from the live preview — the effect is deliberately subtle live, and you can't evaluate it while reading. Record a short paragraph of the actual script with the effect on, then the same paragraph with it off, and compare. Two minutes of calibration beats an hour of guessing.
1. With script and lighting set, open the camera preview and confirm eye contact is on.
2. Read one paragraph of the real script at presentation pace while recording.
3. Play it back and watch your eyes for smoothness, not perfection.
4. Record the same paragraph with eye contact off and compare side by side.
5. If the "on" version reads as a steady gaze at the audience, trust the recording.

### Fix 6: Test against hardware teleprompter glass
If you use a physical teleprompter with beam-splitter glass, the glass itself changes what the camera sees — reduced sharpness and faint double reflections can confuse gaze detection. Record the same script with the effect on and off through the glass; sometimes the hardware alone looks better than hardware plus AI.
1. Record one take with eye contact on through your teleprompter glass.
2. Record the same script with eye contact off.
3. Compare the two — if "off" looks more natural, the glass and model are fighting.
4. Clean the beam-splitter glass; smudges scatter light and degrade detection.
5. For current known issues with camera effects, check the [Microsoft support hub](https://support.microsoft.com/en-us/windows).

## Closing

Teleprompter eye contact fails when the setup asks the model to do too much — a distant script, tiny fast text, glare-covered glasses, stacked effects competing for NPU time. Fix the geometry first: script beside the camera, big slow text, clean lighting. Then judge the result from a recording, not the live preview.
