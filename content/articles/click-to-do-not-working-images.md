---
title: "How to Fix Click to Do Not Working on Images in Windows 11"
slug: click-to-do-not-working-images
date: 2026-10-22
categories: ["ai-pc"]
tags: ["click to do images", "click to do image actions", "windows click to do", "image text actions", "copilot plus pc", "windows 11"]
description: "Click to Do ignoring images on your Copilot+ PC? Fix image AI actions — visual search, erase, copy — with these troubleshooting steps. Six fixes inside."
thumbnail: "/images/thumbs/click-to-do-not-working-images.webp"
faqs:
  - q: "What image actions should Click to Do offer?"
    a: >
      Depending on your build: visual search with Bing, background blur or removal, erase unwanted objects, and copy/save the image region. Availability varies by build and by the image content.
  - q: "Does Click to Do work on images inside videos?"
    a: >
      Pause the video and snip the frame with Win + Shift + S, then use image actions on the snip. Direct selection inside a playing video is unreliable across apps.
  - q: "Why do image actions work in Photos but not in my game?"
    a: >
      Games render through exclusive fullscreen pipelines that do not expose frames to Windows' image-recognition layer. This is expected — use screen capture tools for game frames instead.
  - q: "Do image actions need internet?"
    a: >
      The on-device vision models work offline once downloaded. Visual search with Bing is the exception — it needs connectivity to query the web.
---

Click to Do is not just for text: select an image — or part of one — and you should get visual actions like visual search, background blur, erase objects, and copy as image. When images get no sparkle, no menu, nothing, half the feature is dark.

Image actions need the vision pipeline: the system must recognize the selection as an image, run it through on-device vision models, and offer the right actions. Text actions can work perfectly while the vision side is broken — they are separate models behind one menu. The same split-pipeline reality explains [NPU usage spikes when idle](/articles/npu-usage-spikes-idle/), where one NPU workload misbehaves while others run fine.

Six fixes below: using the right selection method, verifying the vision components, repairing the pipeline, and testing across apps. Try an image in Edge's image viewer after each step.

## Why this happens

- **Selecting images the wrong way:** Click to Do on images often needs the Snipping Tool path or a specific gesture — selecting 'around' an image in some apps does not register as an image selection at all.
- **Vision model components missing:** Image actions need vision-capable on-device models. If those downloads failed, image actions vanish while text actions survive — the core of most [Click to Do image actions missing](/articles/click-to-do-image-actions-missing/) reports.
- **App rendering images opaquely:** Apps that draw images through custom canvases (games, some editors, remote desktop) do not expose them to Windows' image pipeline.
- **NPU unavailable for vision models:** Vision models are NPU-hungry; an unhealthy NPU degrades image actions first, since they are the heaviest Click to Do workload.
- **Corrupt feature configuration:** A damaged Click to Do menu configuration can drop the image-action set while keeping text actions.
- **Image too small or too complex:** Tiny icons or extremely busy images can defeat the vision model's region detection, yielding no actions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the Snipping Tool path for images

The most reliable image trigger is not selecting in-app — it is capturing with Snipping Tool.

1. Press **Win + Shift + S** to open Snipping Tool and capture the image region.
2. In the Snipping Tool preview, look for the Click to Do / text-action affordances on the capture.
3. This path feeds Windows a clean image bitmap, bypassing app-rendering quirks entirely.
4. If image actions work on snips but not in-app selections, the app was the blocker — use snips for that app.

### Fix 2: Test on a clean, simple image

Rule out image-content issues with an ideal test case before touching settings.

1. Open a clear photo in the Photos app or Edge — good lighting, single subject.
2. Try the image gesture/selection there and check for image actions.
3. Avoid tiny thumbnails and screenshots of dense dashboards for the test.
4. Working on clean images but not your original means the content, not the feature, was the problem.

### Fix 3: Verify vision AI components downloaded

Image actions need model files that text actions do not. Confirm they arrived.

1. Install all pending Windows updates — vision components ship through Windows Update.
2. Check **Settings > Privacy & security > Click to Do** for any component-download notices.
3. Stay plugged in and online for an hour after updates; large model downloads take time.
4. Interface-level affordances matter too — [pinning the Copilot app to the taskbar](/articles/copilot-app-pin-taskbar-missing/) shows how a missing UI entry point hides a working feature.

### Fix 4: Check NPU health under vision load

Vision models stress the NPU hardest. Verify it is up to the task.

1. Open **Task Manager > Performance > NPU** and confirm the tab exists and responds.
2. Trigger an image action and watch for NPU activity — flat zero during a vision task is suspicious.
3. Check **Device Manager > Neural processors** for driver warnings.
4. Fix NPU driver issues first; vision actions typically recover as soon as the NPU does.

### Fix 5: Reset Click to Do and test across apps

A corrupt menu configuration or a single bad app can both hide image actions. Separate the two.

1. Toggle Click to Do off and on in Settings, then restart the PC.
2. Test image actions in Photos, Edge, and Paint — three different rendering pipelines.
3. If it works in two of three, the odd app out has a rendering incompatibility.
4. If it fails everywhere, continue to the system repair step.

### Fix 6: Repair Windows AI components

System-wide image-action failure after the above means the vision stack itself needs repair.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` elevated.
2. Install every pending Windows update and restart.
3. Create a new local user profile and test there to rule out profile corruption.
4. If the new profile works, migrate your data rather than fighting the old profile's damage.

## Closing

Click to Do on images fails at the vision pipeline: wrong selection method, missing model components, opaque app rendering, or a struggling NPU. Lead with the Snipping Tool path, test on clean images, confirm the vision downloads, and check NPU health. Text and image actions are siblings, not twins — fix the vision side on its own terms. System-wide vision-stack failures are documented at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
