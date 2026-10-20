---
title: "How to Fix Super Resolution Not Working in Windows Photos"
slug: super-resolution-photos-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["super resolution", "photos app", "troubleshooting", "ai pc", "enhance image", "windows 11"]
description: "Super Resolution missing or failing in Windows Photos? Learn the Copilot+ PC requirements and follow proven fixes for the NPU, app, and Windows settings."
thumbnail: "/images/thumbs/super-resolution-photos-not-working.webp"
faqs:
  - q: "Why is Super Resolution missing from my Photos app?"
    a: "Super Resolution only appears on Copilot+ PCs with a 40+ TOPS NPU and a recent Photos app version. If your hardware qualifies but the option is gone, update Photos from the Microsoft Store and install the latest Windows 11 updates. A broken NPU driver can also hide the feature."
  - q: "Does Super Resolution in Photos use the NPU or the GPU?"
    a: "It uses the NPU. Microsoft designed the Photos Super Resolution model to run on the neural processor so upscaling stays fast and power-efficient. If your NPU driver is missing or outdated, the feature disappears rather than falling back to the GPU, which is why driver health matters so much here."
  - q: "Super Resolution starts but produces a blurry result. Is it broken?"
    a: "Not necessarily. The tool works best on moderately low-resolution originals; extremely tiny or heavily compressed images give the model little to work with. If results are suddenly worse than before, though, update your NPU driver — a driver regression can silently degrade inference quality."
  - q: "Can I use Super Resolution on photos stored on an external drive?"
    a: "Yes, the feature works on any image Photos can open, regardless of where it is stored. If the option is unavailable for external files but works for local ones, the issue is usually file permissions or a corrupted Photos cache, not the drive itself. Repairing the app normally resolves it."
---

Super Resolution in the Microsoft Photos app upscales your pictures using an on-device AI model, sharpening details without the blocky artifacts of old-fashioned resizing. It is part of the same wave of NPU-powered editing tools as Generative Erase, and it shares on-device AI plumbing with gaming features like [Auto Super Resolution](/articles/auto-super-resolution-games-not-working/).

The failure modes look familiar: the Enhance or Super Resolution button is missing from the editor, it is grayed out, or clicking it does nothing at all. Sometimes the upscale runs but crawls, or it finishes with an image that looks no better than the original. Each symptom points at a different layer — the app, Windows, or the NPU driver.

This guide covers the full repair path. You will verify the hardware requirements, update Photos and Windows, fix the NPU driver stack, and reset the app if needed, stopping as soon as Super Resolution works again.

## Why this happens

- **No qualifying NPU:** Super Resolution needs a Copilot+ PC with a 40+ TOPS NPU; weaker hardware never gets the option.
- **Outdated Photos app:** the upscaler ships in newer Photos releases delivered through the Microsoft Store.
- **Windows build too old:** the NPU inference plumbing the feature needs arrived in recent Windows 11 releases.
- **Faulty NPU driver:** a present-but-broken driver makes the model fail silently or vanish from the UI.
- **Corrupted Photos cache:** damaged app data can disable editing features after an update.
- **Insufficient memory:** very large upscales on systems with little free RAM can stall or abort mid-process.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify your PC qualifies for the feature

Super Resolution is gated behind Copilot+ PC hardware, so confirm the requirement before troubleshooting software. Open Task Manager with Ctrl + Shift + Esc, go to the Performance tab, and look for the NPU tile showing TOPS and driver information. If the NPU is absent entirely, you are likely dealing with [an NPU that Windows cannot detect](/articles/npu-not-detected-windows-11/) rather than a Photos problem. Also confirm Windows 11 in Settings, then System, then About, since the feature needs a recent build.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Open the Performance tab and look for the NPU tile.
3. Click it to confirm the TOPS rating and driver version.
4. Check Settings, then System, then About for your Windows 11 build.
5. If no NPU appears, troubleshoot NPU detection first.

### Fix 2: Update Microsoft Photos from the Store

The upscaler lives inside the Photos app, so an outdated app is the most common reason the button never appears. Microsoft pushes Photos updates through the Store on its own schedule, independent of Windows Update, and many users run a months-old Photos build on a fully patched OS. Open the Store, visit your Library, and install every pending update for Photos. Relaunch the app and open any photo in the editor to see whether Super Resolution has returned.

1. Open the Microsoft Store from the Start menu.
2. Click Library in the lower-left corner.
3. Click Get updates and let the scan complete.
4. Install the Microsoft Photos update when offered.
5. Reopen Photos and check the editor toolbar.

### Fix 3: Bring Windows 11 fully up to date

Photos calls into NPU runtime components that ship with Windows 11 itself, and an older build may not expose what the newest Photos expects. Feature updates in particular carry the DirectML and neural execution updates that on-device AI tools depend on. Head to Settings, then Windows Update, install everything including optional driver updates, and reboot. After the restart, open Photos and test the upscale on a low-resolution image to confirm the pipeline works end to end.

1. Open Settings and select Windows Update.
2. Click Check for updates and install all of them.
3. Install optional driver updates under Advanced options.
4. Restart the laptop when prompted.
5. Test Super Resolution on a small photo in the Photos editor.

### Fix 4: Repair the NPU driver stack

When the app and OS are current but Super Resolution still fails or runs abnormally slowly, suspect the NPU driver. The model may fail to load onto the neural processor, in which case Photos quietly disables the button instead of showing an error. Update the driver through Device Manager, or grab the newest release from your laptop maker's support page or the chip vendor. Similar NPU execution failures show up as an [ONNX Runtime NPU execution provider error](/articles/onnx-runtime-npu-execution-provider-error/) in other AI apps, so the same driver repair helps both.

1. Open Device Manager and expand Neural processors.
2. Right-click the NPU and choose Update driver.
3. If Windows finds nothing, download the driver from the vendor's site.
4. For stubborn cases, uninstall the device and restart to reinstall it.
5. Confirm the NPU tile looks healthy in Task Manager afterward.

### Fix 5: Repair or reset the Photos app

If everything underneath is healthy and the feature is still missing or crashes on use, the Photos installation itself is the prime suspect. A quick repair through Settings fixes most corruption without touching your pictures. When repair is not enough, resetting the app clears its cache and restores defaults, which also fixes cases where Super Resolution vanished after a bad update. Note that sibling AI editing tools share this failure pattern — if object removal broke too, see our guide to [Generative Erase not working](/articles/generative-erase-photos-not-working/).

1. Open Settings, then Apps, then Installed apps.
2. Locate Microsoft Photos and open its three-dot menu.
3. Choose Advanced options.
4. Click Repair, wait for the checkmark, and retest.
5. If it still fails, click Reset and reopen the app.

## Closing

Super Resolution depends on three things lining up — qualifying NPU hardware, a current Photos app, and a healthy driver — and the fix is usually whichever of those three you updated least recently. Start at the top of this list and you will have the upscaler back without reinstalling Windows. Microsoft documents the full feature requirements on the [Windows support site](https://support.microsoft.com/en-us/windows), which is worth checking after every major update.
