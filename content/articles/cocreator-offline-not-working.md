---
title: "Cocreator Not Working Offline? How to Fix It on Windows 11"
slug: cocreator-offline-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags: [cocreator, paint, windows-11, copilot-plus-pc, offline, troubleshooting]
description: "Cocreator not working offline in Paint on Windows 11? Learn why offline generation fails and restore on-device image creation on your Copilot+ PC today."
thumbnail: "/images/thumbs/cocreator-offline-not-working.webp"
faqs:
  - q: "Does Cocreator really work without internet?"
    a: >
      On Copilot+ PCs, Cocreator can generate images on-device using the NPU, so it should work offline once the required models are downloaded. Without those models, it may show an error or ask you to connect.
  - q: "Why does Cocreator ask for internet on a Copilot+ PC?"
    a: >
      It usually needs to download a model, verify the app, or update Paint first. After that one-time download, offline generation should work, provided the model files remain installed.
  - q: "Will offline Cocreator work on a non-Copilot+ PC?"
    a: >
      No. Offline generation requires the NPU and on-device models found on Copilot+ PCs. Other PCs may need an internet connection or may not offer Cocreator at all.
  - q: "Do I lose my drawings if I reset Paint?"
    a: >
      Resetting Paint clears its settings but does not delete image files you saved to a folder. Save any unsaved work first, because open canvases are not preserved by a reset.
---
You open Paint, switch to Cocreator, draw a rough sketch, and expect an AI image to appear even without Wi-Fi. Instead, you get a spinner, an error about connection, or a greyed-out generate button. On a Copilot+ PC, that should not happen, because Cocreator is designed to run on-device, and the offline failure points to a missing model or a broken app state.

Offline generation is not magic. It depends on the NPU being recognised, the Cocreator models being downloaded and intact, Paint being up to date, and Windows allowing on-device AI processing. If you have never used Cocreator while online, the models may never have downloaded. If an update removed them, the feature falls back to asking for the internet.

This guide fixes offline Cocreator step by step, starting with the one-time online setup that makes offline use possible. Related display and camera faults can share the same driver causes, so also check the [screen flickering fix](/articles/ai-laptop-screen-flickering-fix/) and the [Teams camera fix](/articles/ai-laptop-camera-teams-not-working/) if other AI features misbehave. For driver gaps, see the [human presence detection driver fix](/articles/human-presence-detection-driver-missing/) as a related example.

## Why this happens

- **Models never downloaded:** Cocreator needs on-device models that download on first use, so a PC that has never run it online has nothing to run offline.
- **NPU not recognised:** If Windows cannot see the NPU, Paint cannot offer on-device generation and falls back to an online request.
- **Paint out of date:** Older Paint versions lack offline Cocreator or contain bugs that block generation without a connection.
- **Models damaged by an update:** Feature updates can remove or corrupt model files, leaving Cocreator asking for the internet again.
- **Privacy or AI settings blocking on-device processing:** If on-device AI is restricted, Cocreator cannot run locally even when the models exist.
- **Corrupt Paint app data:** Damaged app settings or cache can break generation while the rest of Paint still opens normally.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your PC qualifies and the NPU is visible
Offline Cocreator is a Copilot+ feature, so the first check is hardware, not Paint settings. Open Task Manager and look for the NPU entry under Performance, and confirm you have at least 16 GB of RAM. If the NPU is missing, no Paint setting will enable offline generation, and the real fix is a driver or system repair rather than reinstalling Paint.
1. Open Task Manager and select Performance to look for an NPU entry.
2. Confirm your laptop is marketed as a Copilot+ PC with a 40+ TOPS NPU.
3. Check Settings, System, About, for RAM and Windows 11 version details.
4. If the NPU is absent, update drivers from your laptop maker first.
5. Restart and recheck Task Manager before moving to Paint fixes.

### Fix 2: Run Cocreator once while online to download models
This is the step most offline failures skip. Cocreator cannot generate offline until its models are downloaded, and that download only happens when you use it with an internet connection. Connect to Wi-Fi, open Cocreator, and generate at least one image successfully. That first success proves the models are in place and gives offline mode something to use.
1. Connect your laptop to a stable Wi-Fi network.
2. Open Paint, select Cocreator, and draw a simple sketch.
3. Enter a short prompt and generate an image while still online.
4. Wait for generation to complete fully before closing Paint.
5. Disconnect Wi-Fi and try the same prompt again to test offline mode.

### Fix 3: Update Paint and Windows to the Cocreator build
An outdated Paint or Windows build can block offline generation even on qualifying hardware, because offline support arrived and improved through updates. Updating both removes that ceiling and often restores models that an older build mishandled. Use the Microsoft Store for Paint and Windows Update for the system, then restart before testing again.
1. Open the Microsoft Store and check for Paint updates, then install them.
2. Go to Settings, Windows Update, and install all available updates.
3. Restart your laptop after both updates complete.
4. Open Paint and confirm Cocreator is still present in the toolbar.
5. Test offline generation with Wi-Fi off and a simple prompt.

### Fix 4: Check on-device AI and privacy permissions
Windows can restrict on-device AI processing through privacy settings, and a restriction there stops Cocreator from running locally even with models installed. This produces a confusing symptom: Paint opens, Cocreator appears, but generation fails offline while online generation works. Reviewing the AI and privacy pages restores local processing without changing your drawings or files.
1. Open Settings and search for AI or Copilot+ feature settings.
2. Confirm that on-device AI features are allowed on this device.
3. Check Settings, Privacy and security, for any blocked AI permissions.
4. If this is a work or school device, ask IT whether local AI is restricted.
5. Toggle the relevant setting off and on, restart, and test offline again.

### Fix 5: Repair Paint and system components
If models are downloaded and permissions are correct but offline generation still fails, Paint or its system components may be damaged. Repairing Paint through Settings is safe and keeps your saved files, while system file tools fix deeper damage that a Paint repair cannot reach. Run them in order and test after each stage so you know which one worked.
1. Go to Settings, Apps, Installed apps, and find Paint.
2. Select Advanced options, then Repair, and wait for it to finish.
3. If repair fails, open Terminal as administrator and run sfc /scannow.
4. Then run DISM /Online /Cleanup-Image /RestoreHealth to fix the store.
5. Restart, open Cocreator online once, then test offline generation again.

### Fix 6: Reset Paint and redownload the models cleanly
When repair does not help, a full reset clears corrupt Paint data and forces a clean model download. Save your work first, because open canvases will not survive the reset. After resetting, use Cocreator once while online so the models download fresh, then disconnect and confirm offline generation works before calling the job done.
1. Save any open Paint work to a folder before resetting the app.
2. Go to Settings, Apps, Installed apps, Paint, Advanced options.
3. Select Reset to clear Paint data, then restart your laptop.
4. Connect to Wi-Fi, open Cocreator, and generate an image online.
5. Disconnect Wi-Fi and generate the same prompt offline to confirm.
6. For driver help, use the official [Intel Driver Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) if your laptop uses Intel hardware.

## Closing

Offline Cocreator fails for a simple reason in most cases: the on-device models were never downloaded, were removed by an update, or cannot run because the NPU or permissions are missing. Running Cocreator once online, updating Paint and Windows, and repairing the app restores offline generation. After that, test offline mode before you travel, so you discover any missing model while you still have Wi-Fi to fix it.
