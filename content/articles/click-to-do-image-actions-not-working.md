---
title: "Click to Do Image Actions Not Working? How to Fix Them"
slug: click-to-do-image-actions-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags: ["click to do", "image actions", "copilot plus pc", "windows 11", "visual search", "ai features"]
description: "Click to Do image actions not working on your Copilot+ PC? Learn why visual search and editing fail and follow steps to restore image actions in Windows 11."
thumbnail: "/images/thumbs/click-to-do-image-actions-not-working.webp"
faqs:
  - q: "Why does Click to Do show text actions but no image actions?"
    a: >
      Text and image actions use different on-device models, so image actions can fail while text actions work perfectly. If the image model is missing, the image is protected, or the app blocks image extraction, Click to Do falls back to text-only or empty results. Testing with a plain photo in a browser usually separates a model problem from an app problem.
  - q: "Do image actions work on screenshots and photos?"
    a: >
      Yes, Click to Do image actions are designed for photos, screenshots, and images on web pages, provided the image is large and clear enough to analyse. Very small thumbnails, heavily compressed images, and images inside protected video players may not offer actions, because the model cannot extract enough detail.
  - q: "Does Click to Do image search need the internet?"
    a: >
      Local actions such as removing a background run on the device's neural processing unit, while visual web search needs an internet connection to look up similar images online. If local actions work but web search does not, check your connection and browser rather than reinstalling the AI components.
  - q: "Why is background removal greyed out in Click to Do?"
    a: >
      Background removal needs a clear foreground subject and a supported image format, and it stays greyed out when the model cannot separate the subject cleanly. Try a larger, sharper photo with a distinct subject, and make sure your Windows build and AI components are fully updated.
---

You click on a photo, expecting visual search, background removal, or an image edit — and Click to Do either shows nothing for the image or offers actions that fail when you tap them. Text actions may work fine on the same screen, which makes the image failure feel oddly specific. It is specific, though: image actions run on different models, need different permissions, and face different app restrictions than text actions.

Images also fail for reasons text never encounters. A photo can be too small, too compressed, protected by a video player, or rendered by an app that never hands Click to Do the actual image data. Add in missing image models, outdated drivers, and settings that limit visual features, and you have several quiet failure points that produce no error message at all.

This guide separates those failure points. You will test with an ideal photo first, then check app and protection issues, then repair the image models and drivers. If Copilot Pro features are also refusing to activate on the same device, the guide on [Copilot Pro features not activating](/articles/copilot-pro-features-not-activating/) may share a licensing or account root cause worth checking alongside this one.

## Why this happens

- **Image model missing or not ready:** Image actions need their own on-device models, which download separately from text models and may still be installing after setup or an update.
- **Image too small or low quality:** Tiny thumbnails and heavily compressed images give the model too little detail to analyse, so actions stay hidden or fail.
- **Protected or app-rendered content:** Video players, secure apps, and apps that draw images themselves can block Click to Do from accessing the image data.
- **Wrong click target:** Clicking near an image, on its caption, or on an overlaid button may register as a text click instead of an image click.
- **Outdated Windows build or drivers:** Image AI features depend on current Windows components and graphics drivers, so an old build can break them silently.
- **Visual features disabled:** Settings or organisation policy can disable image actions specifically while leaving text actions enabled.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with a large, clear photo in a browser

Start with ideal image content so you can tell whether image actions work at all.

1. Open a normal website in your browser and find a large, sharp photograph, not a thumbnail.
2. Hold the Windows key and click directly on the centre of the photograph, not its caption.
3. Wait a few seconds, since image analysis takes longer than text recognition to load actions.
4. Note exactly which actions appear, and which ones fail if you tap them.
5. Try a second large photo on a different site to rule out one page's unusual image handling.

### Fix 2: Check the click target and image size

Many image failures are simply clicks that landed on the wrong element.

1. Zoom the browser page in so the photo fills more of the screen before clicking it.
2. Click the main subject of the photo, avoiding borders, captions, and overlaid play buttons.
3. Avoid images inside video players, carousels with overlays, and password-protected galleries for testing.
4. Download the photo and open it in the Photos app, then test Click to Do on the local copy.
5. If the local copy works but the web version does not, the website's image handling is the barrier.

### Fix 3: Update Windows, AI components, and graphics drivers

Image features are sensitive to build and driver versions, so bring everything current before deeper repairs.

1. Open Settings, go to Windows Update, and install every pending update, including optional ones.
2. Restart your laptop and wait for background AI setup to settle before testing again.
3. Check your graphics driver version and update it from the manufacturer's official source if it is old.
4. For Intel, NVIDIA, or AMD graphics, use only the official driver pages linked from Microsoft support guidance.
5. Retest Click to Do on the same large browser photo after updating and restarting.

### Fix 4: Re-enable visual features and test app isolation

A disabled visual toggle or a blocking app can hide image actions while text actions continue normally.

1. Open Windows Settings and confirm that Click to Do and its image or visual features are enabled.
2. Look for any sub-option that limits image actions and switch those actions back on.
3. Test image actions in a browser, then in the Photos app, then in the app where they failed.
4. If the browser and Photos app work but another app does not, that app blocks image extraction by design.
5. Update the blocking app, and use a supported app for image actions when you need them urgently.

### Fix 5: Repair system components and reset the AI state

Damaged components can break image models while leaving text models untouched, so a repair targets that split.

1. Open an administrator terminal and run the system file checker to repair damaged Windows files.
2. Restart your laptop after the scan, then leave it connected and idle for a few minutes.
3. Open Settings, check Windows Update again, and install any follow-up AI component update.
4. Test Click to Do image actions on a large browser photo, waiting fully for actions to load.
5. If only web visual search fails while local actions work, check your internet connection and default browser settings next.

### Fix 6: Test on a fresh user account to isolate profile damage

A damaged profile can suppress image actions that work fine for another user on the same hardware.

1. Create a temporary local user account in Windows Settings, with no organisation policy attached.
2. Sign into the new account, wait for setup to finish, and open a browser photo page.
3. Hold the Windows key, click the photo, and compare the image actions with your main account.
4. If the new account shows full image actions, your main profile's AI data or settings are damaged.
5. Repair or migrate the profile as needed, then retest image actions on your main account before closing the case.

## Closing

Image actions fail for narrower reasons than text actions: a missing image model, a tiny or protected image, a wrong click target, or an app that never shares the image data. Test with a large browser photo first, update Windows and drivers second, and isolate the app and profile before repairing the system — that order finds the fault without wasted reinstalls. Similar platform-level limits affect other peripherals too, from a [game controller ARM Windows issue](/articles/game-controller-arm-windows-issues/) where driver support varies by device to a [Lenovo Yoga Slim 7x AI problem](/articles/lenovo-yoga-slim-7x-ai-problems/) where model-specific updates restore AI features. For official feature and driver guidance, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) is the safest starting point.
