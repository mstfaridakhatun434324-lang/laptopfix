---
title: "Click to Do Language Support Missing? How to Restore It on Windows 11"
slug: click-to-do-language-support-missing
date: 2026-10-26
categories: ["ai-pc"]
tags: [click-to-do, windows-11, copilot-plus-pc, language-support, troubleshooting, npu]
description: "Click to Do language support missing on your Copilot+ PC? Learn why languages disappear and restore multilingual text actions with proven Windows 11 fixes."
thumbnail: "/images/thumbs/click-to-do-language-support-missing.webp"
faqs:
  - q: "Why does Click to Do only work in some languages?"
    a: >
      Click to Do relies on language packs and AI language models that Microsoft rolls out in stages. If your language model has not been downloaded or is not yet supported, the feature may work in English only or offer fewer actions.
  - q: "Do I need to change my Windows display language?"
    a: >
      Not always. Click to Do can support selected text in several languages while Windows stays in another language, but the relevant language pack and optional features must be installed for recognition and rewriting to work correctly.
  - q: "Will reinstalling language packs delete my files?"
    a: >
      No. Adding or removing a language pack only changes language resources and settings. Your documents, apps, and personal files remain untouched, though you should still restart after making language changes.
  - q: "Why did language support disappear after an update?"
    a: >
      Feature updates can reset optional features, remove a language model, or change privacy settings. Reinstalling the language pack and checking Click to Do settings usually restores support without a full reset.
---
You select text in another language, press Windows key plus click, and expect Click to Do to offer translation, rewriting, or summarising. Instead, the menu is empty, English-only, or missing the action you used yesterday. The feature itself is present, but its language support has gone missing, and that distinction matters for the fix.

Click to Do depends on more than a single toggle. It needs the right Windows build, the correct language packs, downloaded AI language models, and privacy permissions that allow text processing. If any one of those pieces is absent, Windows quietly narrows what Click to Do can do rather than showing an error. That silent narrowing is why the problem feels so confusing.

This guide walks through the full chain in order, from checking what languages are actually installed to repairing the components that power multilingual actions. If the whole feature is gone rather than just its languages, start with the fan and presence guides linked below, because shared Copilot+ components may be involved. For broader context, see how to fix [AI laptop fan curve problems](/articles/ai-laptop-fan-curve-fix/) and adjust [presence sensing privacy settings](/articles/presence-sensing-privacy-settings/) when a related AI feature misbehaves, and check the [haptic touchpad fix](/articles/haptic-touchpad-not-working-windows-11/) if touch input is also unreliable.

## Why this happens

- **Missing language pack:** Click to Do cannot recognise or rewrite text in a language whose pack is not installed, so those actions simply do not appear.
- **AI language model not downloaded:** Some languages need an on-device model that downloads separately, and a stalled download leaves support half-installed.
- **Windows build too old:** Older builds support fewer Click to Do languages, so an outdated system caps what the feature can offer.
- **Region or display language mismatch:** A language installed for typing is not the same as one enabled for AI features, and the mismatch hides actions.
- **Privacy settings blocking text access:** If Click to Do lacks permission to read selected text, language actions fail silently instead of prompting you.
- **Update reset optional features:** Feature updates sometimes remove optional language components, which explains support vanishing overnight.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check which languages Click to Do actually supports
Before changing anything, establish the facts. Open Click to Do on English text and then on text in your target language, and note exactly which actions appear in each case. That comparison tells you whether support is missing for one language or for all of them, and it stops you from reinstalling everything when only one pack is at fault. Record the language, the app you selected text in, and whether the menu appeared at all.
1. Select English text in Notepad and open Click to Do with Windows key plus click.
2. Repeat the test with text in your target language in the same app.
3. Note which actions appear for each language, or whether the menu is empty.
4. Try a second app, such as Edge, to rule out one app blocking text selection.
5. Write down the missing language so you install the right pack next.

### Fix 2: Install the full language pack, not just the keyboard
Many users install a keyboard layout and assume the language is fully installed, but Click to Do needs the broader language pack, including display and speech components where offered. Installing the complete pack gives the AI features the recognition data they need. This step alone restores support in most cases, especially after a clean install or a new user profile that only added a keyboard.
1. Open Settings, then Time and language, then Language and region.
2. Select Add a language and choose your target language from the list.
3. Tick the language features offered, including language pack and speech if shown.
4. Click Next, then Install, and wait for the download to finish completely.
5. Restart your laptop, then test Click to Do on text in that language again.

### Fix 3: Update Windows and download optional language features
An outdated build is a hard ceiling on language support, because Microsoft adds Click to Do languages through feature updates and optional components rather than small patches. Updating Windows first ensures you are not chasing a language that your build cannot offer yet. After the update, revisit optional features, since language models and handwriting components sometimes sit there waiting to be installed.
1. Go to Settings, then Windows Update, and install every available update.
2. Confirm your build under Settings, System, About, and restart if prompted.
3. Return to Settings, System, Optional features, and search for your language.
4. Install any language-related optional features that are listed as available.
5. Restart once more and retest Click to Do with the target language.

### Fix 4: Reset Click to Do permissions and privacy settings
Click to Do must be allowed to see the text you select, and a privacy change can quietly revoke that access. This is easy to overlook because the feature still opens, yet its language actions stay hidden. Checking the AI and privacy pages restores the permission without touching your files, and it also catches cases where a work or school policy changed the setting during an update.
1. Open Settings and search for Click to Do to open its settings page.
2. Confirm Click to Do is turned on and that text actions are enabled.
3. Check Settings, Privacy and security, and review any AI or text permissions.
4. If you use a work or school account, ask IT whether AI features are restricted.
5. Toggle Click to Do off and on, restart, and test the missing language again.

### Fix 5: Repair language components with system tools
When packs are installed and Windows is current but support is still missing, the underlying components may be damaged. A failed update can leave language files half-registered, which produces exactly this symptom: the language appears installed, yet Click to Do cannot use it. System File Checker and DISM repair that damage, and they are safer than removing and reinstalling Windows.
1. Open Terminal as administrator from the Start menu right-click options.
2. Run sfc /scannow and wait for it to finish before closing the window.
3. Then run DISM /Online /Cleanup-Image /RestoreHealth to repair the store.
4. Restart your laptop after both commands complete successfully.
5. Test Click to Do again, and reinstall the language pack if it still fails.

### Fix 6: Remove and reinstall the problem language cleanly
If one language stubbornly refuses to work while others are fine, its pack may be corrupt rather than missing. Removing it completely and reinstalling from scratch clears stale model files that a simple repair misses. This step takes a few minutes and a restart, but it resolves the stubborn single-language cases that survive every other fix in this guide.
1. Go to Settings, Time and language, Language and region.
2. Select the problem language, choose Remove, and restart your laptop.
3. Add the language again with all available features ticked during setup.
4. Wait for the full download, including any speech or handwriting data.
5. Restart once more and test Click to Do in that language in two apps.
6. If it still fails, check the official [Windows support pages](https://support.microsoft.com/en-us/windows) for current language availability notes.

## Closing

Missing language support in Click to Do is rarely a single broken setting. It is usually a gap in the chain of language packs, models, builds, and permissions, and working that chain in order finds the gap quickly. Once the right pack is fully installed and Windows is current, multilingual actions return, and keeping Windows updated prevents the next feature update from quietly removing them again.
