---
title: "Click to Do Rewrite Text Missing? Restore It on Your Copilot+ PC"
slug: click-to-do-rewrite-missing
date: 2026-10-26
categories: ["ai-pc"]
tags: [click-to-do, rewrite-text, copilot-plus-pc, windows-11, troubleshooting, npu]
description: "Click to Do rewrite text missing from the menu? Restore the rewrite action on your Copilot+ PC by fixing settings, the model, and the NPU driver today."
thumbnail: "/images/thumbs/click-to-do-rewrite-missing.webp"
faqs:
  - q: "Why is Rewrite missing while Summarize still works?"
    a: >
      Rewrite and Summarize use different model paths, so one can fail while the other survives. A damaged rewrite component, a language mismatch, or a partially registered feature state can hide Rewrite alone, even when the rest of Click to Do looks healthy.
  - q: "Does Rewrite work in every language?"
    a: >
      No. The on-device rewrite model supports a limited set of languages, and text outside that set may show no Rewrite option at all. Testing with plain English text in Notepad is the quickest way to rule out a language problem.
  - q: "Can my selected text hide the Rewrite option?"
    a: >
      Yes. Rewrite needs editable, selectable text of a reasonable length. A single word, a password field, a protected document, or text inside an image will not offer rewriting, because the model has nothing it is allowed to transform.
  - q: "Will a Windows update bring Rewrite back?"
    a: >
      Often, yes, if the cause was a damaged component or an incomplete model download. Installing pending updates and restarting is worth trying before deeper repairs, but it will not fix a disabled toggle or a broken NPU driver on its own.
---

You open Click to Do expecting to tighten a sentence, and the Rewrite option simply is not in the list. Summarize may be there, search may be there, but the action you actually wanted has vanished without an error or an explanation. The menu looks normal in every other way, which makes the missing entry feel like a strange, personal glitch rather than a diagnosable fault.

Rewrite is a model-dependent action, like Summarize, but it follows its own path through the on-device language model, so it can disappear on its own while everything else survives. The usual causes are a disabled or half-registered feature, a language the model does not support, a selection it cannot edit, or an NPU driver that leaves the model without hardware to run on.

This guide isolates them one at a time, starting with the selection and the language, then the feature state, then the driver. If the problem turns out to be part of a wider security or sign-in fault, the [TPM attestation error on ARM](/articles/tpm-attestation-arm-error/) guide covers that side, and [Windows Hello PIN not working on AI PCs](/articles/windows-hello-pin-not-working-ai/) helps when sign-in itself is involved.

## Why this happens

- **Feature is half-registered after an update:** Windows updates can leave Click to Do in a state where the menu opens but individual model actions fail to register.
- **Selection cannot be rewritten:** Rewrite needs editable text. Password fields, protected documents, images of text, and single words do not qualify, so the option hides itself rather than failing visibly.
- **Language is unsupported:** The on-device rewrite model covers a limited set of languages. Text in an unsupported language, or a mixed-language selection, may show no Rewrite entry at all.
- **On-device model is damaged or incomplete:** If the rewrite model failed to download or was corrupted, the action cannot appear. Other actions that do not need that model keep working normally.
- **NPU driver is faulty:** Rewrite runs through the neural processor. A missing or erroring driver removes the hardware the model needs, and the action disappears silently.
- **App does not expose editable text:** Some apps render text without exposing it as editable to Windows. Click to Do opens, but it never receives text it is allowed to transform.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test Rewrite with plain English text in Notepad

Before changing any setting, prove whether Rewrite works anywhere at all, because a language or selection problem needs no system repair. Notepad supplies clean, editable, standard text with no protection or custom rendering, and a plain English sentence removes the language variable entirely.

1. Open Notepad and type a plain English sentence of ten to twenty words.
2. Select the whole sentence, not just a single word.
3. Press Win + Q or Win + Click on the selection to open Click to Do.
4. Check the full action list carefully, since Rewrite may sit below the first entries.
5. If Rewrite appears here, retest your original text and note what differs.

### Fix 2: Toggle Click to Do to re-register its actions

A half-registered feature is the most common systemic cause, and it is also the easiest to repair. The master toggle forces Windows to re-register every Click to Do action, including Rewrite, which is exactly what a damaged post-update state needs.

1. Open Settings, then Privacy and security, and select Click to Do.
2. Confirm the main toggle is on, then switch it off for about ten seconds.
3. Switch it back on and wait for the setting to settle before testing.
4. Reopen Notepad, reselect a plain English sentence, and check for Rewrite.
5. If Rewrite returns, test your original app as well to confirm the repair held.

### Fix 3: Check the selection type and the app

Rewrite is picky about its input in ways that Summarize is not, because it must return editable replacement text rather than a separate summary. A password box, a read-only document, a PDF rendered as an image, or a web form field can all suppress the option legitimately.

1. Confirm the text you selected is in an editable field or document, not a protected view.
2. Copy the same text into Notepad and test Rewrite there.
3. If Notepad succeeds, the original app or document was blocking the action.
4. Try a longer selection if you selected only one or two words.
5. Avoid password fields, secure viewers, and images of text when testing Rewrite.

### Fix 4: Update Windows, the model, and the NPU driver

When Rewrite is missing everywhere, the model or its hardware is the next suspect. Windows updates can repair a damaged model component and deliver a missing one, while the NPU driver determines whether the model has hardware to run on at all. The driver must match your exact laptop model, so your maker's support page is the right source.

1. Open Settings, then Windows Update, and install all pending and optional updates.
2. Restart the laptop and wait a few minutes after signing in for background setup.
3. Open Device Manager, expand Neural processors, and look for warning icons.
4. Update the NPU driver from your laptop maker's support page, or consult the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).
5. Retest Rewrite in Notepad with a plain English sentence before testing other apps.

### Fix 5: Repair the app where Rewrite is missing

If Rewrite works in Notepad but not in your usual app, the app itself is feeding Click to Do text it cannot rewrite, often because of a corrupted cache or a stale rendering component. Repairing the app clears that state without touching your documents, and it is a much smaller operation than reinstalling system components.

1. Close the app where Rewrite is missing and reopen it fresh.
2. Test Rewrite there with a plain, editable paragraph.
3. If it still fails, repair the app from Settings, then Apps, then Installed apps.
4. Reopen the app and test Rewrite again before trying anything else.
5. If repair fails, reset the app, then test once more with the same paragraph.

### Fix 6: Reset the feature state and verify language settings

When every earlier step leaves Rewrite missing in Notepad itself, the remaining suspects are a deeper feature-state fault and a language mismatch. Windows display language and input language both influence which on-device models activate, and a system set to an unsupported language can hide Rewrite even on fully healthy hardware.

1. Open Settings, then Time and language, and confirm your display language is supported.
2. Test Rewrite again with a plain English sentence in Notepad.
3. Toggle Click to Do off, restart the laptop, then toggle it back on.
4. Wait for background model setup to finish after signing in, then retest.
5. If Rewrite remains missing only for non-English text, the language limit is the answer.
6. For a related single-component fault pattern, see [Docker Desktop issues on ARM Windows](/articles/docker-desktop-arm-windows-issues/), where one component hides while the rest works.

## Closing

Rewrite rarely disappears for a mysterious reason: it is almost always the selection, the language, the registration, or the driver, and each of those announces itself once you test in Notepad first. Once it returns there, carry the same clean test back to your usual app, and you will know immediately whether the repair held or the app itself needs attention.
