---
title: "How to Fix Click to Do Image Actions Missing on Copilot+ PCs"
slug: click-to-do-image-actions-missing
date: 2026-10-21
categories: ["ai-pc"]
tags: ["click to do image actions", "click to do missing", "copilot+ pc", "visual search", "windows 11", "ai features"]
description: "Fix Click to Do image actions missing on your Copilot+ PC with six step-by-step methods covering visual search, NPU load, app support, and feature toggles."
thumbnail: "/images/thumbs/click-to-do-image-actions-missing.webp"
faqs:
  - q: "What are Click to Do image actions?"
    a: "When you invoke Click to Do on an image, it should offer visual search with Bing, copying text from the image, blurring the background, or removing objects. If only text actions appear on images, the image-action set is missing."
  - q: "Why do text actions work but image actions do not?"
    a: "Text and image actions use different on-device models. The image model is larger, needs more NPU memory, and downloads separately. Text actions can work while the image model is missing, blocked, or failing to load."
  - q: "Do Click to Do image actions need the internet?"
    a: "The analysis runs on-device, but actions like visual search with Bing open a browser and need connectivity. The menu itself should appear offline; if it does not, the problem is local."
  - q: "Can battery saver remove Click to Do image actions?"
    a: "Yes. Aggressive power policies can prevent the image model from loading on the NPU, removing image actions while text actions keep working — one reason to check your power plan."
---

Click to Do has two halves: text actions (summarize, rewrite, search) and image actions (visual search, copy text from images, background blur). Many Copilot+ owners find the text half working perfectly while the image half is simply absent — invoking Click to Do on a photo shows a stunted menu or nothing at all.

Image actions depend on a separate, heavier on-device vision model than text actions. That model has to download, fit into NPU memory, and pass stricter hardware checks. Any failure along that chain silently drops the image actions while text actions sail on.

This guide covers six fixes in order, from confirming you are invoking it on a real image through model downloads, NPU state, and the power settings that can starve the vision model.

## Why this happens

- **The vision model has not downloaded yet:** Image actions need an extra on-device model that Windows fetches after setup. On a fresh install or a metered connection, the download may never complete.
- **NPU is idle or unavailable:** Vision models are the most NPU-hungry part of Click to Do. If the neural processor is [stuck at zero percent usage](/articles/npu-stuck-at-zero-percent-usage/) or disabled, the image pipeline cannot start.
- **Invoking on a non-image surface:** Image actions trigger on actual images — photos, screenshots, image files. Video frames, canvas elements, and DRM-protected surfaces yield no image actions.
- **Battery saver or power policy blocks the model:** Loading the vision model is power-intensive, so battery saver can suppress it — the same trade-off behind [sleep battery drain](/articles/battery-drain-in-sleep-snapdragon-laptop/) on Snapdragon laptops.
- **Click to Do image actions disabled in Settings:** The image-action toggles can be off while text actions stay on, especially after a privacy-hardening script ran.
- **Feature flags out of sync:** When Windows feature rollouts are incomplete, related AI surfaces misbehave together — if your [Quick Settings are also missing AI entries](/articles/studio-effects-settings-missing-quick-settings/), the underlying feature enablement is likely the culprit.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Invoke Click to Do on a genuine image the right way

Before changing anything, confirm the problem is real and not an invocation issue. Image actions only appear when Click to Do detects an image under the cursor. Test on a known-good image like a photo in the Photos app.

1. Open the **Photos** app and open any photo (a real image file, not a video).
2. Press **Win + Q**, or select part of the image and **Win + click**.
3. Check whether image actions (visual search, copy text from image, blur background) appear.
4. Try a screenshot: press **Win + Shift + S**, capture a region, then invoke Click to Do on it.
5. If image actions appear on photos but not in your target app, the app surface is the limitation.

### Fix 2: Confirm the vision model has downloaded

Windows downloads Click to Do's image model separately, and it is easy to miss. A metered connection, paused updates, or a fresh install can leave the download incomplete indefinitely — with no error in the menu itself.

1. Go to **Settings > Windows Update**, install every pending update, and restart.
2. Set your network as non-metered: **Settings > Network & internet > Wi-Fi > your network**, toggle **Metered connection** off.
3. Leave the laptop plugged in and idle for 30–60 minutes so background model downloads complete.
4. Check **Settings > Privacy & security > Click to Do** for any model-download status or error.
5. Retest on a photo in the Photos app after the wait.

### Fix 3: Check that the NPU is active and actually working

The vision model runs on the NPU, and image actions are the first casualty when the neural processor is down. If the NPU entry is missing or permanently idle in Task Manager, fix that before anything else.

1. Open Task Manager (**Ctrl + Shift + Esc**) > **Performance** and look for the **NPU** entry.
2. Invoke Click to Do on an image and watch for NPU activity; if it sits at zero, see [why the NPU can be stuck idle](/articles/npu-stuck-at-zero-percent-usage/).
3. In Device Manager, verify the NPU has no warning icon; reinstall the driver from your laptop maker's support page if needed.
4. Confirm you are on a Copilot+ PC with a 40+ TOPS NPU — image actions require the full Copilot+ hardware bar.
5. Restart and retest.

### Fix 4: Turn off battery saver and check the power plan

Battery saver trims background AI workloads, and the vision model is one of the first things cut. If image actions appear when plugged in but vanish on battery, power policy is your answer.

1. Turn **Battery saver** off in **Settings > System > Power & battery**.
2. Set the power mode to **Best performance** or **Balanced** while testing.
3. Plug in the charger and retest Click to Do on an image.
4. If actions return on AC power, test AI features plugged in, then tune the battery plan afterward.
5. Check your laptop maker's power utility (Lenovo Vantage, MyASUS, Dell Optimizer) for an AI/NPU power toggle and allow AI workloads.

### Fix 5: Verify the Click to Do toggles in Settings

Click to Do's settings page has separate controls, and the image-related ones can be off while text actions run fine. Privacy scripts and enterprise baselines disable exactly these toggles.

1. Open **Settings > Privacy & security > Click to Do** and confirm the main toggle is on.
2. Enable any image or visual-related toggles (wording varies by build).
3. Check **Settings > Privacy & security > General** for disabled AI options the feature depends on ([Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the current layout).
4. Sign out and back in, then retest on a photo.

### Fix 6: Repair Windows' AI components with an in-place upgrade

If the model is downloaded, the NPU works, power is fine, and toggles are on — yet image actions are still missing — a Windows component is likely corrupt. An in-place upgrade refreshes every system component, including the AI stack, while keeping files and apps.

1. Download the latest Windows 11 ISO from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO, run **setup.exe**, and choose **Keep personal files and apps**.
3. Let the repair install complete (30–60 minutes), then install all Windows Updates.
4. Leave the machine idle and plugged in for an hour so AI models re-download.
5. Test Click to Do image actions on a photo — the full action set should now appear.

## Closing

Missing Click to Do image actions almost always trace to the vision model's chain of dependencies: the download, the NPU, the power policy, or the toggles. Text actions working is a useful clue — it proves Click to Do itself is fine and narrows the hunt to the image pipeline.
