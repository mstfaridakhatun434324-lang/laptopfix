---
title: "How to Fix Click to Do Translate Missing on Windows 11"
slug: click-to-do-translate-text-missing
date: 2026-10-22
categories: ["ai-pc"]
tags: ["click to do translate", "click to do translate missing", "windows click to do", "translate text windows 11", "copilot plus pc", "windows 11"]
description: "The Translate action vanished from Click to Do on Windows 11? Restore the missing Translate option on your Copilot+ PC with these six step-by-step fixes."
thumbnail: "/images/thumbs/click-to-do-translate-text-missing.webp"
faqs:
  - q: "Which languages does Click to Do Translate support?"
    a: >
      Support covers dozens of major languages and grows with updates. If your specific pair is missing, check for language-pack and Windows updates first — availability expands over time rather than being fixed forever.
  - q: "Does Click to Do Translate work offline?"
    a: >
      Core translation can run on-device once components are downloaded, but some language pairs and features may use online services. If offline translation matters to you, pre-install the language packs while connected.
  - q: "Why does Translate appear for some text but not other text?"
    a: >
      Language detection needs enough clean text in a recognizable script. Short fragments, heavy formatting, or mixed languages can defeat detection — select a fuller sentence and try again.
  - q: "Can I set a default target language?"
    a: >
      Click to Do generally translates into your Windows display language. Change the display language under Language & region settings if you want a different default target.
---

You select foreign-language text, trigger Click to Do, and... no Translate option. Or it is there but greyed out, or it errors the moment you pick a language. Translation is one of Click to Do's headline actions, so its absence is immediately noticeable.

Translate depends on language components that other actions do not: the source language must be detected, translation models or services must be available, and language packs may need downloading. Any gap in that chain removes or disables the action. It is the same dependency-chain fragility as [Copilot app offline mode](/articles/copilot-app-offline-mode-not-working/), where one missing offline component disables an entire feature set.

This guide walks through six fixes: confirming the trigger, installing language components, checking connectivity and region, and repairing the pipeline. Test Translate on a known foreign phrase after each step.

## Why this happens

- **Missing language packs:** Translation needs language resources for the detected source language. If the pack never downloaded, the action cannot appear — the most common cause by far.
- **Source language not detected:** Very short selections, mixed-language text, or unusual scripts can defeat language detection, leaving Translate with nothing to offer.
- **Region or language availability:** Some translation pairs and features roll out by region. A Microsoft account region mismatch can hide the action.
- **On-device model components incomplete:** Like Summarize, Translate leans on Windows Copilot Runtime components. A partial download breaks it while simpler actions survive — compare [Click to Do Rewrite not working](/articles/click-to-do-rewrite-not-working/) for the shared root cause.
- **Connectivity blocking service-backed translation:** Parts of the translation pipeline may reach Microsoft's services; aggressive firewalls, VPNs, or proxy configs can block them.
- **Corrupt Click to Do configuration:** A damaged feature configuration can drop individual actions from the menu while the rest of the feature works.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with a clean, detectable sample

Rule out detection failure before touching any settings — the action may be fine and your test text the problem.

1. Select a full sentence in a common language, e.g. a full Spanish or French sentence from a news site — not two words.
2. Trigger Click to Do with **Windows key + click** on the selection.
3. If Translate appears for the clean sample, your original text was simply not detectable — select more context next time.
4. If it is still missing, continue — the components are the suspect.

### Fix 2: Install the needed language packs

Translation cannot offer what it cannot read. Install the language resources first.

1. Go to **Settings > Time & language > Language & region** and add the source language you want to translate from.
2. Click the language's options and install the language pack plus any speech/translation-related features offered.
3. Also verify your Windows display language pack is fully installed.
4. Restart the PC after installing packs, then retest Translate on sample text.

### Fix 3: Check Windows Update for AI components

Translation models and runtime pieces arrive through Windows Update, sometimes separately from the packs.

1. Open **Settings > Windows Update** and install everything pending.
2. Click **Advanced options > Optional updates** and install any language or AI-related optional components.
3. Stay connected and plugged in for an hour so background model downloads finish.
4. Driver-level reinstalls follow the same 'get the right package' logic — [clean-installing Windows 11 AI laptop drivers](/articles/clean-install-windows-11-ai-laptop-drivers/) is a good reference for clean component installs.

### Fix 4: Verify region, network, and VPN

Service-backed pieces of translation need a clear path to Microsoft's servers from a supported region.

1. Temporarily disconnect your VPN and retest — VPNs are a classic translation breaker.
2. Check that your Microsoft account region and Windows region match under **Settings > Time & language > Language & region**.
3. If you use a proxy, test with it disabled to rule out interception.
4. Corporate firewalls may block the endpoints; on a work device, ask IT whether translation services are allowed.

### Fix 5: Reset Click to Do's configuration

When components are present but the action is still missing, the feature's own configuration may be corrupt.

1. Toggle Click to Do off and on in **Settings > Privacy & security > Click to Do** (or the equivalent Text actions page).
2. Restart the PC after toggling — the menu configuration rebuilds at startup.
3. Test Translate again on your clean sample sentence.
4. If other actions also started misbehaving, a Windows update plus `sfc /scannow` is the next escalation.

### Fix 6: Repair the shared AI runtime

Translate shares the Windows Copilot Runtime with Summarize and Rewrite — a runtime repair fixes all of them at once.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` from an elevated Command Prompt.
2. Install all pending Windows updates and restart.
3. Verify a sibling action (Summarize or Rewrite) works — if they do and Translate does not, the issue is language-specific, not runtime-wide.
4. As a final check, create a new local user account and test Translate there to rule out profile corruption.

## Closing

A missing Translate action is almost always a missing component: a language pack, an AI runtime piece, or a blocked service call. Test with clean sample text, install the packs, update Windows, check VPN and region, and reset the feature configuration. Translation is a chain — repair it link by link and the action comes back. If translation stays broken after these fixes, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the escalation paths.
