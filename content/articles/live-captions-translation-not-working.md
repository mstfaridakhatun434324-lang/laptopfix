---
title: "Live Captions Translation Not Working? Fix It on Windows 11"
slug: live-captions-translation-not-working
date: 2026-10-19
categories: ["ai-pc"]
tags: [live-captions, translation, windows-11, copilot-plus-pc, npu, troubleshooting]
description: "Live Captions translation not working on Windows 11? Fix on-device translation with our NPU, driver, language pair, region, and Copilot+ PC checks today."
thumbnail: "/images/thumbs/live-captions-translation-not-working.webp"
faqs:
  - q: "Why is the translate option greyed out in Live Captions?"
    a: >
      Almost always hardware: translation needs a Copilot+ PC with a 40+ TOPS NPU. On other machines the option is unavailable by design.
  - q: "Which languages does Live Captions translation support?"
    a: >
      The supported list grows with Windows updates and currently covers major languages. Check the translation language dropdown in settings — if your pair is not listed, it is not supported yet.
  - q: "Does Live Captions translation work offline?"
    a: >
      Yes, once the translation models are downloaded. The models run on-device via the NPU, so no internet is needed during actual translation.
  - q: "Translation worked before an update and stopped. Why?"
    a: >
      Updates can replace the NPU driver or reset the translation toggle. Reinstall the OEM NPU driver, re-enable translation, and let the models re-download.
---
Base Live Captions work — English speech becomes English text — but the translation feature that turns foreign audio into your language just will not engage. The translate toggle is greyed out, or translations never appear. This is a distinct problem from captions themselves failing, with its own steeper requirements.

Translation is the premium tier of Live Captions: unlike basic captioning, it needs a Copilot+ PC with a working NPU, because the translation models run on-device through the neural processor. That single requirement explains most failures.

This guide covers the translation-specific chain: hardware, NPU driver, language support, and settings. If effects are greyed out too, see [Studio Effects greyed out](/articles/studio-effects-greyed-out/) — the NPU is the likely common cause. For the full effects suite, see [Windows Studio Effects not working](/articles/windows-studio-effects-not-working/). If basic captions do not work either, start with [Live Captions not working](/articles/live-captions-not-working-windows-11/).

## Why this happens

- **Not a Copilot+ PC:** Translation needs 40+ TOPS NPU. On lesser hardware the feature is unavailable by design.
- **NPU driver broken or outdated:** The translation models run on the neural processor; a bad driver silently disables translation.
- **Translation language unsupported:** Only certain language pairs are supported for on-device translation. Unsupported pairs show no translation option.
- **Translation models not downloaded:** The models download separately from the base caption pack, and the download can stall.
- **Feature toggle off:** Translation has its own sub-toggle inside Live Captions settings.
- **Outdated Windows build:** Translation support expanded across updates; older builds may lack your language pair.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Copilot+ eligibility
Translation is the gated tier of Live Captions: unlike base captioning, it requires a 40+ TOPS NPU and therefore a Copilot+ PC. On lesser hardware the translate option is unavailable by design — not broken, just absent. Checking Task Manager for the NPU entry settles it instantly and prevents wasted effort on a feature the machine was never meant to run.
1. Check Task Manager > Performance for an NPU entry at 40+ TOPS.
2. Verify Copilot+ status with our [Copilot+ PC check](/articles/how-to-check-if-laptop-is-copilot-plus-pc/).
3. On ineligible hardware, translation will never activate — base captions remain available.
4. Do not chase workarounds; the NPU requirement is architectural.

### Fix 2: Fix the NPU driver
The translation models execute on the neural processor, so a broken NPU driver kills translation while leaving base captions untouched — a confusing split symptom. Device Manager reveals it, and the OEM driver restores it; translation typically reappears immediately after the driver fix without any further settings changes.
1. Open Device Manager > Neural processors; look for warning icons.
2. Install the NPU driver from your laptop maker's support page.
3. Restart and reopen Live Captions to see if the translate option activates.
4. If the NPU was the blocker, translation appears immediately after the driver fix.

### Fix 3: Check language pair support
On-device translation covers a growing but finite list of language pairs. If yours is not on it, no toggle, driver, or update will conjure it — the models for that pair simply do not exist locally yet. Checking the supported list first saves the frustration of troubleshooting a limitation, and the list expands with Windows updates.
1. In Live Captions settings, open the translation language list.
2. Confirm both your source and target languages are listed and downloaded.
3. If your pair is missing, translation is unavailable for it — no setting changes that.
4. Check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for the current supported-language list.

### Fix 4: Force the translation model download
The translation models download separately from the base caption pack, and that download stalls quietly — no progress bar, no error. Toggling translation off and on retriggers it, and an uninterrupted half hour on stable Wi-Fi lets it finish. Most 'translation just stopped' cases are really 'translation models never finished downloading.'
1. Ensure you are on stable, unmetered Wi-Fi.
2. Toggle translation off and on in Live Captions settings to retrigger the download.
3. Leave the laptop idle and plugged in for 30 minutes to let it complete.
4. Test with a supported language pair afterward.

### Fix 5: Update Windows fully
Translation language support is one of the fastest-moving parts of Windows 11 — each major update widens it. An older build may simply predate your language pair. Staying current is disproportionately important for this feature, more so than for base captioning, which has been stable far longer.
1. Install all pending Windows updates and restart.
2. Confirm you are on 24H2 or later.
3. Re-check the translation toggle after updating.
4. Microsoft expands on-device translation support regularly — staying current matters more here than for base captions.

### Fix 6: Verify the NPU is actually doing the work
Watch the NPU graph during a translation attempt: activity means the request reaches the neural processor, silence means it dies upstream. This single observation splits the diagnostic tree cleanly — driver and toggle issues on one side, language-pair limitations on the other — and takes ten seconds in Task Manager.
1. Open Task Manager > Performance > NPU during a translation attempt.
2. You should see NPU activity spike as translation runs.
3. No activity with translation toggled on means the request never reaches the NPU.
4. That points back at drivers or the feature toggle, not the language pair.

### Fix 7: Test translation with the simplest pair
Strip the test to the simplest supported pair — English to Spanish, say — with clear, slow speech. If that works, your original pair is the limitation and everything else is healthy. If even the simplest pair fails, the problem is systemic and the driver-toggle-models chain needs the full treatment.
1. Set source to English and target to Spanish (or your region's best-supported pair).
2. Play clear, slow speech audio.
3. If the simple pair works, your original pair is the limitation.
4. If even the simple pair fails, the problem is systemic — driver, toggle, or models.

## Closing

Live Captions translation fails for three reasons in practice: no qualifying NPU, a broken NPU driver, or an unsupported language pair. Check them in that order. Base captioning remains available on far more hardware, so even when translation is out of reach, you are not without captions entirely.
