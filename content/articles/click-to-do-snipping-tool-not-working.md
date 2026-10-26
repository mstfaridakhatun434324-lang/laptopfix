---
title: "Click to Do Not Working in Snipping Tool? Fix It on Your Copilot+ PC"
slug: click-to-do-snipping-tool-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags: [click-to-do, snipping-tool, copilot-plus-pc, windows-11, troubleshooting, npu]
description: "Click to Do not working inside the Snipping Tool? Fix the missing text actions, broken gesture, and NPU setup on your Copilot+ PC step by step with this guide."
thumbnail: "/images/thumbs/click-to-do-snipping-tool-not-working.webp"
faqs:
  - q: "Why does Click to Do work in Notepad but not in the Snipping Tool?"
    a: >
      The Snipping Tool captures text as part of an image, so Click to Do depends on its text-recognition step running first. If recognition fails, or the capture does not expose selectable text, the menu has nothing to act on and stays hidden.
  - q: "Do I need a Copilot+ PC for Click to Do in the Snipping Tool?"
    a: >
      Yes. Click to Do runs its text and image understanding on-device through a neural processor rated at 40 or more TOPS. On a PC without that hardware, the feature is unavailable no matter which app you open it from.
  - q: "Which gesture opens Click to Do from a Snipping Tool capture?"
    a: >
      Hold the Windows key and left-click on recognised text inside the capture, or press Win + Q while the capture is open. A plain right-click does not invoke Click to Do, and clicking on blank image space shows no text actions.
  - q: "Will reinstalling the Snipping Tool delete my screenshots?"
    a: >
      No. Reinstalling the app removes only the program itself, not the files in your Screenshots folder. Your saved captures stay on disk, although you should confirm your save location before you reset or reinstall anything.
---

You capture a screenshot, spot a phone number in the image, and try to act on it — and nothing happens. Click to Do, which works fine on selected text in Notepad, refuses to appear inside the Snipping Tool, or appears without the text actions you expected. The capture is right there on screen, yet the shortcut that should turn it into something useful stays silent.

The confusion comes from two systems having to cooperate. The Snipping Tool must first recognise the text inside your capture, and then Click to Do must read that recognised text and offer its actions.

This guide separates those two halves so you can find the real culprit. It covers the Snipping Tool's text recognition, the Click to Do gesture and toggle, the NPU driver behind the on-device models, and the updates that quietly break the chain. If the fault looks wider than one app, check [audio driver crackling on ARM laptops](/articles/audio-driver-arm-crackling/) or [HP OmniBook Ultra AI issues](/articles/hp-omnibook-ultra-ai-issues/) for a system-wide driver picture.

## Why this happens

- **Text recognition is off or failing:** The Snipping Tool must turn pixels into selectable text before Click to Do can act. If recognition stalls, there is no text for the menu to use.
- **Wrong gesture on an image:** Click to Do still needs Win + Click on recognised text, or Win + Q. A normal right-click, or a click on empty image space, produces nothing.
- **Click to Do toggle is disabled:** The feature has its own master switch under Privacy and security. Updates and new user profiles can leave it off, killing the menu everywhere.
- **NPU driver is unhealthy:** The on-device models run through the neural processor. A missing or erroring NPU driver silently disables the feature without any warning.
- **Snipping Tool is outdated or corrupted:** An old build may predate the Click to Do integration, while a corrupted install can break the hand-off between the capture window and the menu.
- **Capture quality defeats recognition:** Tiny fonts, blurry screenshots, and text over a busy background can fall below the recognition threshold, leaving Click to Do with nothing to offer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the Click to Do toggle is on

Check the feature itself before blaming the Snipping Tool, because a disabled master toggle produces the same symptom in every app. The toggle lives apart from Recall and general AI settings, and updates have a habit of leaving it off. Turning it off and on also re-registers the feature, repairing half-registered states that updates leave behind.

1. Open Settings, then Privacy and security, and select Click to Do.
2. Confirm the main toggle is switched on, not greyed out.
3. Switch it off, wait ten seconds, then switch it back on.
4. Test Click to Do at once on selected text in Notepad.
5. If Notepad works but the Snipping Tool does not, the fault is capture-specific.

### Fix 2: Use the correct gesture on recognised text

The gesture is the most common trap here, because a screenshot invites a normal right-click, and a normal right-click does nothing. Click to Do needs the Windows key held down while you left-click directly on recognised text, or the Win + Q shortcut. Clicking on a photo, a logo, or blank space will not summon text actions.

1. Take a fresh capture with a clear line of large, high-contrast text.
2. Wait a moment for the capture window to finish processing the image.
3. Hold the Windows key and left-click directly on a word in the capture.
4. If nothing appears, press Win + Q while the capture window is focused.
5. Note whether any menu appears at all, even without text actions.

### Fix 3: Turn on text recognition in the Snipping Tool

Click to Do cannot act on a picture of text until the Snipping Tool has turned that picture into text. A capture of a clean document should show selectable words once recognition has run; if you cannot select any text from the capture, Click to Do has nothing to work with, and no toggling of its own settings will help.

1. Open the Snipping Tool and capture a page of plain printed text.
2. Look for the text actions or copy-text option in the capture toolbar.
3. Try selecting a word to see whether it highlights as real text.
4. If no text is selectable, update the Snipping Tool from the Microsoft Store.
5. Retest with a larger font, since tiny text often fails recognition.

### Fix 4: Repair the Snipping Tool app

When recognition and the gesture check out elsewhere but the Snipping Tool still refuses to cooperate, the app itself is the prime suspect. A corrupted cache or half-updated install can break the hand-off between the capture window and the menu while ordinary screenshots keep working, which is why this failure is so misleading. Repair keeps your settings and screenshots intact.

1. Open Settings, then Apps, then Installed apps, and find Snipping Tool.
2. Open its advanced options and choose Repair, then wait for it to finish.
3. Take a new capture and test Win + Click on its recognised text.
4. If repair changes nothing, return to the same screen and choose Reset.
5. After a reset, retake a capture and test the gesture again.

### Fix 5: Check the NPU driver and Windows build

The on-device models behind Click to Do run through your laptop's neural processor, so a sick NPU kills the feature silently in every app, with no error message pointing at the driver. Device Manager reveals the truth in seconds, and the driver matched to your exact laptop model fixes this far more often than any Windows setting.

1. Open Device Manager and expand Neural processors to look for warning icons.
2. Update the driver from your laptop maker's support site, such as [HP support](https://support.hp.com/us-en).
3. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) for current build guidance.
4. Open Settings, then Windows Update, and install every pending update.
5. Restart the laptop after any driver update, since NPU changes need a reboot.

### Fix 6: Improve capture quality and retest cleanly

If every setting and driver checks out, the capture itself may be the problem. Recognition models have real limits: small fonts, low contrast, motion blur, and busy backgrounds all push text below the threshold, and a scaled or compressed capture makes it worse. A clean, deliberate test capture separates a genuine system fault from a recognition limit, and it costs nothing to try.

1. Capture a full-screen view of a plain document at 100 percent zoom.
2. Choose dark text on a plain light background, avoiding glare.
3. Wait for the capture to finish processing before invoking Click to Do.
4. Test Win + Click on the largest, clearest word in the capture first.
5. If the clean capture works, recapture your original screenshots larger.
6. For a shortcut that avoids the gesture entirely, [customise the Click to Do keyboard shortcut](/articles/customize-click-to-do-keyboard-shortcut/) to suit your keyboard.

## Closing

Work through the chain in order — toggle, gesture, recognition, app repair, driver, capture quality — and the faulty link usually reveals itself quickly, because each test rules out a whole category at once. When Click to Do returns inside the Snipping Tool, test it on a couple of ordinary captures before calling the job done.
