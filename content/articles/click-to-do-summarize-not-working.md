---
title: "Click to Do Summarize Text Not Working? Fix It on Your Copilot+ PC"
slug: click-to-do-summarize-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags: [click-to-do, summarize-text, copilot-plus-pc, windows-11, troubleshooting, npu]
description: "Click to Do summarize text not working on your Copilot+ PC? Fix the missing summary action, NPU driver, and settings with this complete step-by-step guide."
thumbnail: "/images/thumbs/click-to-do-summarize-not-working.webp"
faqs:
  - q: "Why is Summarize missing from Click to Do but other actions appear?"
    a: >
      Summarize depends on the on-device language model, while simpler actions do not. If that model is unavailable, corrupt, or blocked, the menu still opens but the summary action is hidden or fails, which is why the rest of Click to Do can look healthy.
  - q: "Does Summarize need an internet connection?"
    a: >
      No. On a Copilot+ PC, Click to Do summarization runs on-device through the NPU. A missing summary is therefore a local problem with the model, driver, or settings, not a network outage, although updates that repair it do need the internet.
  - q: "How much text does Summarize need to work?"
    a: >
      Summarize needs a meaningful passage, not a word or a short phrase. Selecting a single sentence or a fragment often produces no action at all, so always test with a full paragraph before assuming the feature is broken.
  - q: "Can long documents break Click to Do Summarize?"
    a: >
      Yes. Extremely long selections can exceed the model's working limit and fail silently or return nothing. If a short paragraph summarises fine but a whole page does not, split the text into smaller sections and summarise them one at a time.
---

You highlight a long paragraph, open Click to Do, and look for Summarize — and it is not there, or it spins forever, or it returns nothing. The rest of the menu may be perfectly fine: you can rewrite, search, or copy, but the one action that would save you reading the whole passage refuses to cooperate. It feels like a small failure, yet it removes the main reason many people open Click to Do.

Summarize is also the action most dependent on the on-device language model, which is why it fails alone while simpler actions survive. That model needs a healthy NPU, a compatible Windows build, enough selected text to work with, and a feature state that has not been damaged by an update.

This guide works through those pieces in diagnostic order, from the selection itself to the model and driver underneath it. If your whole system feels unstable rather than just this one action, check [BitLocker issues on ARM laptops](/articles/bitlocker-arm-laptop-issues/) for a wider driver picture, and see [Dell XPS 14 AI issues](/articles/dell-xps-14-ai-issues/) if you own that model.

## Why this happens

- **Selection is too short:** Summarize needs a real passage to condense. A word, a heading, or a single short sentence gives the model nothing to summarise, so the action hides itself.
- **Selection is too long:** At the other extreme, a huge block of text can exceed the model's working limit. The request then fails silently.
- **Language model is unavailable:** The on-device model can be missing, corrupt, or still downloading after an update. Other Click to Do actions do not need it, so they keep working.
- **NPU driver is broken:** Summarization runs through the neural processor. A driver fault starves the model of its hardware and disables the action without an error message.
- **Feature state is damaged after an update:** Windows updates can leave Click to Do half-registered, and Summarize, as the most model-dependent action, is the first to break.
- **App text is not exposed to Windows:** Some apps render text in ways Click to Do cannot read properly. The menu opens, but the summarizer never receives clean text to process.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with a proper paragraph in Notepad

The fastest way to separate a real fault from a bad test is a controlled selection, because Summarize behaves very differently with a fragment than with a full passage. Many reported failures turn out to be a two-word selection or a heading, and no repair will make those summarise. Notepad gives you clean, standard text, so a success there proves the model works.

1. Open Notepad and paste or type a paragraph of at least five full sentences.
2. Select the entire paragraph, not just the first line.
3. Press Win + Q or Win + Click on the selection to open Click to Do.
4. Look for the Summarize action and try it on this clean paragraph.
5. If it works here, your original selection was too short, too long, or incompatible.

### Fix 2: Toggle Click to Do off and on to re-register it

A half-registered feature state is invisible from the outside: the menu opens, most actions work, and only the model-dependent ones fail. Toggling the master switch forces Windows to re-register Click to Do and its model connections, which repairs exactly that kind of silent damage. It costs nothing and changes no files, so it belongs before any driver work.

1. Open Settings, then Privacy and security, and select Click to Do.
2. Switch the main toggle off and wait about ten seconds.
3. Switch it back on and wait for the setting to settle.
4. Restart the app you were summarising from, then reselect a full paragraph.
5. Test Summarize again before moving on, since this alone often restores it.

### Fix 3: Split long text and clean up the selection

When a short paragraph summarises but a long document does not, the model limit is the culprit, not your hardware. Long selections also collect hidden formatting, stray line breaks, and repeated headings that confuse the summarizer, especially when copied from web pages or PDFs.

1. Select a single paragraph of moderate length from the document.
2. Test Summarize on that paragraph alone and note whether it succeeds.
3. If it succeeds, work through the document paragraph by paragraph.
4. Paste the text into Notepad first if the original app adds heavy formatting.
5. Avoid selecting navigation bars, footers, or repeated headings with the body text.

### Fix 4: Update Windows and the NPU driver

Summarize depends on a chain of recent components: the Windows build that ships the model, and the NPU driver that runs it. An outdated build may carry an older or broken model, while a faulty driver starves the model of hardware entirely. Both are fixed by updates, but the driver must come from your laptop maker's support page, because NPU drivers are model-specific.

1. Open Settings, then Windows Update, and install every pending update.
2. Restart the laptop after the updates, even if Windows does not insist.
3. Open Device Manager, expand Neural processors, and check for warning icons.
4. Update the NPU driver from your maker's support site, or check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).
5. Retest Summarize on a clean paragraph in Notepad after the restart.

### Fix 5: Repair the app and clear the feature cache

If Summarize fails in one app but works in Notepad, the app's own state is suspect: a corrupted cache or stale text component can feed Click to Do broken text while the app itself looks normal. Repairing or resetting the app clears that state without touching your documents, and it is a safer step than reinstalling Windows components.

1. Close the app where Summarize fails and reopen it fresh.
2. If the failure persists, repair the app from Settings, then Apps, then Installed apps.
3. Test Summarize in that app again with a clean, moderate paragraph.
4. If repair fails, reset the app, then reopen it and test once more.
5. Compare the result with Notepad to confirm whether the fault was app-specific.

### Fix 6: Check model availability and sign-in state

On some systems the on-device model downloads or activates separately from the main Windows update, and Summarize stays hidden until that step completes. A paused update, a metered connection, or a fresh user profile can all leave the model half-installed, which looks exactly like a broken feature.

1. Connect to an unmetered network and open Windows Update for optional updates.
2. Install any AI component or driver updates listed, then restart the laptop.
3. Wait a few minutes after signing in for background model setup to complete.
4. Test Summarize in Notepad with a full paragraph before testing other apps.
5. If the action is still missing, note whether other model actions also fail.
6. For a related device pattern, see [Dell XPS 13 9345 Snapdragon issues](/articles/dell-xps-13-9345-snapdragon-issues/), where the same driver pattern affects summarization.

## Closing

Summarize usually returns once you give it a fair test — a real paragraph, a re-registered feature, and a healthy NPU driver — because the action itself rarely breaks in isolation. Keep your test paragraph in Notepad as a reference: if it summarises there but not elsewhere, the app or the selection is at fault, and you now know which one to fix.
