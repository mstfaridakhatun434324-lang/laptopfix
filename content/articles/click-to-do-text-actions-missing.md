---
title: "Click to Do Text Actions Missing? How to Restore Them"
slug: click-to-do-text-actions-missing
date: 2026-10-26
categories: ["ai-pc"]
tags: ["click to do", "text actions", "copilot plus pc", "windows 11", "ai features", "summarize"]
description: "Click to Do text actions missing on your Copilot+ PC? Learn why copy, summarize and rewrite vanish and follow steps to restore text actions in Windows 11 today."
thumbnail: "/images/thumbs/click-to-do-text-actions-missing.webp"
faqs:
  - q: "Why does Click to Do open but show no text actions?"
    a: >
      The overlay can appear while its text actions fail to load if the text itself cannot be read, the AI models are not ready, or a setting limits the available actions. Click to Do first needs to recognise selectable text, then it loads the matching actions, so a failure at either stage leaves an empty or partial menu.
  - q: "Do text actions need an internet connection?"
    a: >
      Most Click to Do text actions, including summarise and rewrite, run on the device's neural processing unit and do not need the internet. However, the feature still needs Windows to be activated and its AI components installed, so an offline device that has never completed setup may show fewer actions.
  - q: "Why are some text actions available but not others?"
    a: >
      Different actions depend on different models and content types. Summarise needs a longer passage, rewrite needs editable-style text, and web search actions need a browser context. Short selections, headings, or text inside an image will naturally offer a smaller set of actions.
  - q: "Can a language setting hide text actions?"
    a: >
      Yes. Text actions are trained for specific languages, and content in an unsupported language may show only basic actions such as copy. If your text is in a supported language but actions are still missing, check that your Windows display language and region settings match the language of the content.
---

Click to Do opens, you click on a paragraph, and the menu appears — but the useful actions are gone. No summarise, no rewrite, no copy as plain text, sometimes not even a basic copy option. The overlay is technically working, yet it offers nothing worth using, which is almost more frustrating than it not opening at all.

Text actions depend on a chain of conditions that the overlay alone does not guarantee. Click to Do must first recognise the clicked content as real text, then load the right AI models, then match actions to the selection length, language, and app context. Break any link — unreadable text, unready models, an unsupported language, or a restrictive app — and the menu shrinks or empties. The fix is to find which link broke.

This guide isolates that link step by step. You will test with ideal text first, then check language and app context, then repair the AI components. If Click to Do does not open at all, start instead with the overlay guide, and if fingerprint sign-in is also failing on the same device, see [Copilot+ PC fingerprint not working](/articles/copilot-plus-pc-fingerprint-not-working/) for the related hardware check.

## Why this happens

- **Text not recognised as selectable text:** Clicking on an image of text, a scanned document, or a custom-rendered control gives Click to Do nothing it can treat as text.
- **Selection too short or too long:** Some actions need a minimum passage length, so a single word or a whole page may offer far fewer actions than a paragraph.
- **AI models not installed or ready:** On-device text models download and initialise after setup, and actions stay hidden until that process finishes.
- **Unsupported language:** Text actions are language-specific, so content in an unsupported language naturally shows only the most basic options.
- **App blocking text extraction:** Secure apps, protected windows, and apps with custom text rendering can prevent Click to Do from reading the selection.
- **Feature or action toggles disabled:** Individual AI actions can be limited by settings or organisation policy even when the Click to Do overlay itself remains enabled.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with ideal, selectable paragraph text

Start with the easiest possible content so you know whether text actions work at all.

1. Open a normal website in your browser and find a plain paragraph of at least three sentences.
2. Hold the Windows key, click inside the paragraph, and watch which actions the menu offers.
3. Select a longer passage if the first click shows few actions, since length changes the available set.
4. Try a second paragraph on a different website to rule out one page's unusual formatting.
5. If ideal text shows full actions, your original content was the problem, not Click to Do itself.

### Fix 2: Check the language and selection type

Language and content type quietly filter the action list, even when everything else is healthy.

1. Confirm the text you clicked is in a language supported by Windows AI features.
2. Check that your Windows display language matches the language of the content you are testing.
3. Avoid headings, buttons, and navigation labels for testing, since they offer fewer actions than body text.
4. Try clicking on body copy rather than a caption or a table cell, which may be treated differently.
5. If actions appear for English body text but not for other-language text, language support is the limiting factor.

### Fix 3: Give on-device AI models time and updates

Text actions cannot appear before their models are installed, and a fresh or recently updated PC may still be finishing that work.

1. Connect your laptop to power and a stable internet connection, then leave it idle for a while.
2. Open Settings, go to Windows Update, and install every pending update, including optional ones.
3. Restart your laptop after updating, since AI components often initialise only after a reboot.
4. Wait several minutes after signing in before testing, to allow background model setup to complete.
5. Test Click to Do again on ideal paragraph text, and repeat the update check if actions are still absent.

### Fix 4: Test in a different app to isolate blocking

If one app hides actions while a browser shows them, the app is restricting text extraction.

1. Test Click to Do text actions in a browser first, and note the full list of actions shown.
2. Then test the same gesture in the app where actions were missing, using similar paragraph text.
3. Try pasting that text into a plain text editor or word processor and testing there as well.
4. If the browser and editor show actions but the original app does not, that app blocks extraction by design.
5. Update the blocking app, and consider copying text into a supported app when you need text actions urgently.

### Fix 5: Re-enable AI features and repair system components

Disabled toggles and damaged components can suppress actions while leaving the overlay visible.

1. Open Windows Settings and confirm that Click to Do and its AI features are fully enabled.
2. Look for any sub-option that limits text actions and turn those actions back on.
3. Open an administrator terminal and run the system file checker to repair damaged Windows components.
4. Restart your laptop after the scan, then test Click to Do on ideal browser text again.
5. If actions return only briefly, check Windows Update again for a follow-up fix to the AI components.

### Fix 6: Test on a fresh user account to isolate profile damage

A damaged user profile can hide actions that work perfectly for another account on the same machine.

1. Create a temporary local user account in Windows Settings, with no organisation policy attached.
2. Sign into the new account, wait for setup to finish, and open a browser page.
3. Hold the Windows key, click on paragraph text, and compare the actions with your main account.
4. If the new account shows full text actions, your main profile's AI settings or data are damaged.
5. Migrate to a repaired profile if needed, or reset the AI feature state on the original account and retest.

## Closing

Missing text actions rarely mean Click to Do is broken — they usually mean the clicked text was unreadable, too short, in an unsupported language, or in an app that blocks extraction. Test with ideal paragraph text first, then work through language, model readiness, and app isolation before repairing anything. The same isolation logic helps with other input problems, from a [fingerprint reader ARM not working](/articles/fingerprint-reader-arm-not-working/) fault that blocks sign-in to a [Surface Pro 11 AI issue](/articles/surface-pro-11-ai-issues/) where model-specific drivers limit on-device AI. For official guidance, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) is the reliable place to confirm feature requirements and rollout status.
