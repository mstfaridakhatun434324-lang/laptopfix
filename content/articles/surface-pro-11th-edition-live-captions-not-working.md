---
title: "How to Fix Surface Pro 11th Edition Live Captions Not Working"
slug: surface-pro-11th-edition-live-captions-not-working
date: 2026-10-28
categories: ["ai-pc"]
tags: ["Surface Pro 11", "Live Captions", "accessibility", "AI laptop", "Windows 11"]
description: "Live Captions on your Surface Pro 11 should transcribe any audio in real time. Learn why captions stop and how to get them back today. Fix it. Fix it."
thumbnail: "/images/thumbs/surface-pro-11th-edition-live-captions-not-working.webp"
faqs:
  - q: "Why are Live Captions not working on my Surface Pro 11?"
    a: >
      The usual causes are a missing language pack, a disabled microphone or audio setting, a driver issue, or Live Captions being turned off in accessibility settings.
  - q: "Do Live Captions need internet to work?"
    a: >
      No. Live Captions run on-device using the NPU on Copilot+ PCs like the Surface Pro 11, so they work offline once the language pack is installed.
  - q: "Why do captions work for videos but not for calls?"
    a: >
      Live Captions capture system audio by default. Calls may need the microphone audio option enabled, or the call app may route audio in a way captions cannot capture.
  - q: "Can a Windows update break Live Captions?"
    a: >
      Yes. Updates can remove or corrupt language packs, reset accessibility settings, or replace audio drivers, any of which can stop captions.
---

Live Captions are one of the most genuinely useful accessibility features in Windows: a small floating bar that transcribes any audio playing on your PC, in real time, without needing the internet. On the Surface Pro 11th Edition, the NPU handles that transcription on-device, so captions are fast and private. When the captions stop — the bar is empty, it never appears, or it shows an error — the loss is felt immediately by anyone who relies on them for calls, videos, or meetings.

The cause is usually a missing piece rather than a broken feature. Live Captions need a language pack, an audio source, and the right accessibility toggle, and a Windows update can disturb any of those quietly. The NPU path matters too: on a Copilot+ PC, captions use the NPU, so an NPU driver problem can stop captions even when everything else looks fine.

This guide checks each piece in order: the toggle, the language pack, the audio source, and the drivers, so captions return quickly.

## Why this happens

- **Language pack missing or corrupted:** Live Captions need a speech language pack for your language, and without it captions cannot start.
- **Live Captions turned off:** An update or a settings reset can turn the feature off in accessibility settings.
- **Microphone or audio source issue:** If captions are set to include microphone audio and the mic is blocked, captions may fail or stay empty.
- **Audio driver problem:** A driver that mishandles system audio capture can leave Live Captions with nothing to transcribe.
- **NPU driver fault:** On-device captioning on the Surface Pro 11 uses the NPU, so an NPU driver error can stop captions.
- **App audio routing:** Some apps route audio in ways that bypass system audio capture, so captions work for some apps and not others.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn Live Captions on properly

Confirm the feature itself is enabled before chasing deeper causes.

1. Press Windows + Ctrl + L to toggle Live Captions, and watch for the caption bar to appear.
2. Open Settings, go to Accessibility, then Captions, and confirm Live Captions is switched on.
3. Check the caption style and position settings to make sure the bar is not hidden off-screen.
4. Play a video with clear speech and watch whether any text appears within a few seconds.
5. If the bar appears but stays empty, the problem is audio capture or language, not the toggle.

### Fix 2: Install or repair the language pack

A missing language pack is the most common reason captions refuse to start.

1. Open Settings, go to Accessibility, then Captions, and check the caption language setting.
2. If the language shows a download prompt or an error, download and install the speech pack for your language.
3. Open Settings, go to Time and language, then Language, and confirm speech recognition is installed for your language.
4. Restart the laptop after installing the language pack, then toggle Live Captions on again.
5. Test captions with a video in the installed language to confirm transcription works.

A similar language-pack fix resolves [Clipchamp Autocompose crashes](/articles/clipchamp-autocompose-crashes-snapdragon/) when a media component is missing, and the same component-check logic applies when [facial recognition fails in low light](/articles/facial-recognition-hello-fails-low-light-ai-pc/) because a sensor path is incomplete. For a related backup check, see [Windows Backup restore problems](/articles/windows-backup-ai-pc-restore-fix/).

### Fix 3: Check the audio source and microphone settings

Captions need audio to transcribe, and the wrong source means silence.

1. In Live Captions settings, check whether "Include microphone audio" is on or off, and test both settings.
2. Open Settings, go to System, then Sound, and confirm the correct output device is selected and producing sound.
3. If microphone audio is enabled, confirm the microphone is allowed in Privacy and security, then Microphone settings.
4. Play system audio loudly enough for capture, since very quiet audio may not trigger transcription.
5. Test captions with a loud video first, then with a call, to separate system-audio capture from microphone capture.

### Fix 4: Update audio and NPU drivers

Drivers control both the audio capture path and the on-device transcription engine.

1. Open Device Manager, expand Sound, video and game controllers, and update the audio driver.
2. Expand Neural processors and check the NPU for warnings or errors.
3. Visit Microsoft's Surface support site and install the latest driver and firmware pack for the Surface Pro 11th Edition.
4. Restart and toggle Live Captions on again, testing with a video.
5. If captions return but lag badly, the NPU driver may still be at fault, and a fresh driver install is worth trying.

### Fix 5: Reset Live Captions settings

Corrupted caption settings can block the feature even when every component is healthy.

1. Open Settings, go to Accessibility, then Captions, and turn Live Captions off.
2. Restart the laptop, then turn Live Captions back on.
3. Reset the caption style to default in case a custom style is rendering text invisibly.
4. Test captions with a video, checking both the bar's visibility and its text.
5. If the bar appears but text is invisible, the style or color settings are the culprit, not the transcription engine.

### Fix 6: Repair Windows accessibility components

If every piece checks out but captions still fail, Windows components may need repair.

1. Run the System File Checker from an administrator Command Prompt to repair system files.
2. Check for Windows updates, since Live Captions fixes arrive through Windows Update.
3. Check Microsoft's official Live Captions guidance at [Microsoft Support](https://support.microsoft.com/en-us/windows) for language and configuration requirements.
4. Test captions in a new user profile to rule out a profile-specific settings corruption.
5. If captions fail in every profile after repair, contact Microsoft support with your build number and language pack status.

## Closing

Live Captions failing on the Surface Pro 11 is usually a toggle, a language pack, or an audio source that quietly changed — not a broken NPU or a dead feature. Turn the feature on, install the language pack, check the audio source, and update the drivers, and captions typically return to their fast, on-device transcription. If they stay silent after every fix, a Windows repair is the final step before a support case.
