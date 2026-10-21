---
title: "How to Fix Click to Do Not Working on Screenshots in Windows 11"
slug: click-to-do-not-working-on-screenshots
date: 2026-10-21
categories: ["ai-pc"]
tags: ["click to do screenshots", "screenshot ai actions", "snipping tool", "copilot+ pc", "windows 11", "visual search"]
description: "Fix Click to Do not working on screenshots on your AI PC with six step-by-step methods covering Snipping Tool, image detection, NPU state, and permissions."
thumbnail: "/images/thumbs/click-to-do-not-working-on-screenshots.webp"
faqs:
  - q: "How is Click to Do supposed to work on screenshots?"
    a: "Capture with Win + Shift + S or the Snipping Tool, then invoke Click to Do (Win + Q or Win + click) on the captured image. It should offer visual search, copying text from the image, and other image actions."
  - q: "Why does Click to Do work on photos but not screenshots?"
    a: "Screenshots flow through the Snipping Tool overlay and clipboard, adding handoff steps that plain image files skip. A broken Snipping Tool integration or clipboard issue affects screenshots while photos open normally."
  - q: "Do screenshots need to be saved before Click to Do sees them?"
    a: "No — Click to Do works on the Snipping Tool capture overlay and pasted screenshots. But if the overlay handoff is broken, saving the screenshot as a file and opening it is a reliable workaround."
  - q: "Can DRM or protected content block Click to Do on screenshots?"
    a: "Yes. Screenshots of DRM-protected video may capture as black, and Click to Do cannot analyze a black image. That is expected behavior, not a bug."
---

Screenshots are where Click to Do should shine: snap a region, then immediately visual-search it or copy text out of it — no saving files. When that flow breaks, the fast path that makes the feature useful is gone.

The screenshot path needs three apps cooperating: the capture tool, the clipboard or overlay holding the image, and Click to Do detecting it. Photos skip all of that — they are just files. So "works on photos, fails on screenshots" points at the capture-and-handoff chain.

This guide covers six fixes in order: the correct screenshot-to-Click-to-Do flow, Snipping Tool repair, clipboard and overlay issues, image-action prerequisites, NPU state, and permission checks.

## Why this happens

- **Invoking Click to Do on the wrong surface:** After Win + Shift + S, Click to Do must be invoked on the captured image (or the Snipping Tool markup window) — not on the dimmed screen behind the overlay.
- **Snipping Tool integration is broken:** If the capture never reaches a surface Click to Do recognizes — notification missing, markup window never opens — the actions never trigger.
- **Clipboard handoff failure:** Screenshotting to the clipboard and pasting into an app is the fastest path. If clipboard history or image-format handling is damaged, the pasted image is not a real image to Click to Do.
- **Image actions are missing entirely:** If the image-action set never loaded (vision model, NPU, power policy), screenshots get the same stunted menu as photos — the [Copilot key driver guide](/articles/copilot-key-driver-reinstall/) covers the same enablement failure class.
- **NPU not engaging for vision workloads:** Screenshot analysis is a vision workload on the NPU. Capture-related AI features share imaging plumbing — when the [Copilot+ camera pipeline](/articles/copilot-plus-pc-camera-not-working/) misbehaves, screenshot AI often wobbles for the same reason.
- **Screen-capture permission or DRM:** Some apps and protected video block capture; Click to Do cannot act on a black capture. [Discord screen sharing](/articles/discord-screen-share-arm-laptop/) hits the same protected-surface limits on ARM laptops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the correct screenshot-to-Click-to-Do flow

Most "not working" reports come from invoking Click to Do at the wrong moment in the capture flow. Establish a working baseline with the two reliable paths before changing settings.

1. Press **Win + Shift + S**, drag a region over some text (a webpage paragraph is ideal).
2. Click the Snipping Tool notification to open the capture in the markup window.
3. In the markup window, press **Win + Q** or select part of the image and **Win + click**.
4. Check for image actions: visual search, copy text from image. If they appear, your flow was the problem.
5. Alternative path: save the capture as PNG in the Snipping Tool, open it in Photos, and invoke Click to Do there.

### Fix 2: Repair the Snipping Tool app

When the Snipping Tool is damaged — capture works but the notification never appears or captures vanish — Click to Do never gets a proper image surface. Repairing the app package fixes the handoff.

1. Go to **Settings > Apps > Installed apps**, find **Snipping Tool**, and open **Advanced options**.
2. Click **Repair**, wait for completion, then test Win + Shift + S again.
3. If the notification still does not appear, click **Reset** on the same page.
4. Check **Settings > System > Notifications** and confirm Snipping Tool notifications are allowed.
5. Retest: capture, open the notification, Win + Q on the image.

### Fix 3: Fix the clipboard image handoff

The clipboard path — screenshot to clipboard, paste into Paint, then Click to Do — breaks when clipboard history or image-format handling is corrupt. It is the fastest way to get a screenshot under Click to Do without saving files.

1. Open **Settings > System > Clipboard** and toggle **Clipboard history** off and back on.
2. Press **Win + V** and click **Clear all** to purge stale entries.
3. Press **Print Screen**, open **Paint**, paste (**Ctrl + V**), and confirm the image pastes correctly.
4. Select a region in Paint and **Win + click** to invoke Click to Do.
5. If pasting fails, run `sfc /scannow` in an elevated Command Prompt — clipboard format handlers are system components.

### Fix 4: Make sure Click to Do image actions are actually available

If the screenshot flow is right but the menu shows only text actions, the problem is not screenshots at all — the image-action set is missing system-wide. Screenshots are just where you noticed.

1. Open any photo in the **Photos** app and invoke Click to Do (**Win + Q**).
2. If image actions are missing on the photo too, the screenshot flow is innocent — check the vision-model download, NPU state, and battery saver.
3. Confirm the NPU shows activity in Task Manager when you invoke Click to Do on the photo.
4. Keep the laptop plugged in with Battery saver off while testing — vision models are power-gated.
5. Once image actions appear on photos, retest on a screenshot.

### Fix 5: Check screen-capture permissions and protected content

If Click to Do works on screenshots of documents but not of videos or certain apps, you are hitting capture protection, not a Click to Do bug. DRM-protected video captures as black, and no fix makes Click to Do analyze a black rectangle.

1. Test on a plainly capturable surface: a Notepad window or a webpage with text.
2. If that works but video screenshots fail, the content is DRM-protected — expected behavior.
3. Check **Settings > Privacy & security** for any denied screen-capture permissions (wording varies by build).
4. For game captures, verify **Settings > Gaming > Captures** is enabled.
5. Stick to capturable content for AI actions; protection boundaries are by design.

### Fix 6: Update graphics and NPU drivers for the capture pipeline

The screenshot path leans on the graphics driver's capture APIs and the NPU's vision pipeline together. A Windows Update driver replacing your OEM one classically degrades capture-adjacent AI features.

1. Download the latest graphics and NPU/chipset drivers for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. Install both as administrator, restarting when prompted.
3. Take a test screenshot with Win + Shift + S and open it in the Snipping Tool markup window.
4. Invoke Click to Do on the image and confirm the full image-action menu appears.
5. If a specific driver version breaks capture AI, roll back in Device Manager until the maker updates it.

## Closing

Click to Do failing on screenshots is usually a handoff problem: the capture, the clipboard, or the overlay surface between you and the AI. Establish the working flow first — capture, markup window, Win + Q — then repair the broken link.
