---
title: "How to Fix Live Captions Not Working With an External Microphone on Windows 11"
slug: live-captions-external-microphone-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["live captions", "external microphone", "usb microphone", "windows 11", "accessibility", "troubleshooting"]
description: "Fix Windows Live Captions not working with an external microphone by matching input devices, drivers, and caption settings that restore transcription."
thumbnail: "/images/thumbs/live-captions-external-microphone-fix.webp"
faqs:
  - q: "Do Live Captions work with a microphone at all?"
    a: "Yes, when Live Captions is set to include microphone audio. By default it captions system audio; you must enable the microphone option for it to transcribe what your mic picks up."
  - q: "Why do captions work with the built-in mic but not my USB mic?"
    a: "Windows may still be listening to the built-in microphone, or the USB mic may be muted, exclusive-mode locked, or missing its driver. Selecting the USB mic as the default input usually fixes it."
  - q: "Can a headset microphone break Live Captions?"
    a: "Yes. Bluetooth headsets often switch to a low-quality hands-free profile when the mic is active, which degrades the audio Live Captions receives and can stop transcription."
  - q: "Does Live Captions need microphone permission?"
    a: "Yes. If microphone access is turned off for the system or for the caption feature, Live Captions cannot hear your mic at all, even when the device itself works in other apps."
---

You plug in a USB microphone for a meeting, a recording, or dictation, and Windows Live Captions either stays blank or keeps captioning only the speakers — ignoring everything your new microphone hears. The microphone itself works fine in Zoom or a voice recorder, which makes the caption failure feel like a deliberate snub.

The explanation is usually a settings split. By default, Live Captions caption system audio, not microphone audio. Even when you enable the microphone option, Windows must be listening to the right input device, with permission granted and no exclusive-mode lock stealing the stream. Your USB microphone can work perfectly in one app while Live Captions listens to a different, silent input.

This guide aligns those choices in order: the caption microphone option, the Windows input device, permissions, and finally the driver layer. Speak into the external microphone after each fix to see which change makes the captions respond.

## Why this happens

- **Microphone audio not enabled in Live Captions:** The default Live Captions mode captions system audio only. Without the microphone option switched on, your mic audio is never sent to the caption engine.
- **Wrong input device selected:** Windows may keep the built-in laptop microphone as the default input after you plug in a USB microphone, so captions transcribe a silent room mic instead of your voice.
- **Microphone permission turned off:** Privacy settings can block microphone access system-wide or for specific features, leaving Live Captions deaf even though the device works elsewhere.
- **Bluetooth hands-free profile degrading audio:** A Bluetooth headset mic forces the headset into a low-bandwidth profile, and the degraded audio can be too poor for reliable transcription.
- **Exclusive mode or another app holding the mic:** A meeting app or recorder that takes exclusive control of the microphone can starve Live Captions of the same stream.
- **Missing or generic USB microphone driver:** A USB microphone running on a generic driver may record in other apps but fail to expose the format Live Captions expects.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn on microphone audio in Live Captions

This single toggle is the most missed step. Many users assume Live Captions automatically include the microphone, but the feature deliberately separates system audio from mic audio, and the mic side starts off.

1. Press **Windows + Ctrl + L** to open Live Captions.
2. Click the settings (gear) icon in the caption bar and look for the **Microphone audio** or **Include microphone audio** option.
3. Switch it **On** and confirm the caption bar acknowledges the microphone source.
4. Speak clearly into your external microphone and watch for transcription within a few seconds.
5. If captions now appear, you are done — the device was fine, and only the toggle was missing.

### Fix 2: Set the external microphone as the Windows default input

Even with the toggle on, Live Captions follow the Windows default input device. Plugging in a USB microphone does not always change that default, especially if the built-in mic was set explicitly before.

1. Open **Settings > System > Sound** and scroll to the **Input** section.
2. Select your external microphone from the input device list — look for its brand name, not "Microphone Array".
3. Speak into it and watch the **Input volume** bar move; no movement means the wrong device or a muted mic.
4. Click the device's properties and make sure its volume is at a healthy level, not zero, and that it is not muted.
5. Return to Live Captions, speak again, and check for transcription. This device-matching step is the same one that fixes [live captions for Phone Link calls](/articles/live-captions-phone-link-calls-fix/), where the call audio device and the caption device diverge.

### Fix 3: Grant microphone permission and check privacy settings

Windows privacy controls can silently block the caption feature while leaving other apps untouched. If the permission is off, no device selection or driver update will help until it is restored.

1. Open **Settings > Privacy & security > Microphone**.
2. Make sure **Microphone access** is **On**, and **Let apps access your microphone** is also on.
3. Scroll the app list and confirm nothing relevant is individually blocked.
4. If the PC is managed by work or school, look for a notice that microphone access is controlled by policy.
5. Restart Live Captions with **Windows + Ctrl + L** (off, then on) and test the external microphone again.

### Fix 4: Avoid the Bluetooth hands-free trap

Bluetooth headsets are the worst offenders for caption quality. The moment the microphone activates, many headsets drop from high-quality stereo audio to a narrow hands-free profile, and the muffled result transcribes badly or not at all.

1. If you use a Bluetooth headset, disconnect it for the test and use a wired USB microphone instead.
2. If you must use Bluetooth, open **Settings > System > Sound** and check which profile Windows selected for the headset.
3. In **Settings > Bluetooth & devices > Devices**, remove and re-pair the headset to clear a stuck profile.
4. Speak at normal volume close to the mic and check whether captions improve with the wired microphone.
5. For important meetings, prefer the wired USB microphone — it gives Live Captions the cleanest signal, and it also avoids the sync problems seen with [Phone Link on AI laptops](/articles/phone-link-ai-laptop-not-syncing-fix/) when Bluetooth profiles switch mid-call.

### Fix 5: Release exclusive mode and close competing mic apps

One app holding the microphone exclusively can leave Live Captions with nothing to transcribe. Meeting apps, recorders, and voice changers are the usual holders, and closing them for a test quickly proves the point.

1. Close Zoom, Teams, voice recorders, and any voice-effect software completely.
2. Open **Settings > System > Sound**, select your external microphone, and open its properties.
3. Under **Advanced**, uncheck **Allow applications to take exclusive control of this device**.
4. Reopen Live Captions, enable microphone audio again, and speak into the mic.
5. If captions return, reopen your meeting app one at a time to find which one was grabbing the mic; adjust that app's audio settings rather than leaving exclusive mode off for everything.

### Fix 6: Update the microphone driver and test on another port

A generic or stale USB audio driver can record acceptably in one app while failing the caption pipeline. Updating it, and ruling out a faulty port or cable, closes the hardware side of the problem.

1. Open **Device Manager > Audio inputs and outputs**, right-click your external microphone, and choose **Update driver**.
2. If Windows finds nothing newer, download the driver from the microphone maker's site, or check your laptop maker's support page — [Dell](https://www.dell.com/support) or [Lenovo](https://support.lenovo.com/us/en/) — for the USB audio chipset driver.
3. Try a different USB port, preferably a direct port on the laptop rather than a hub, and avoid USB-C adapters for the test.
4. In an elevated terminal, run `sfc /scannow` if other audio devices also behave oddly, to rule out system-file damage.
5. Test Live Captions once more; if the mic works everywhere except captions, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for current Live Captions microphone advisories. A similar driver-first approach also resolves [Copilot voice input](/articles/copilot-voice-input-not-working/) failures, where the mic path matters more than the app setting.

## Closing

Live Captions ignore an external microphone most often because they were never told to listen to it — the mic-audio toggle, the default input device, or a permission stands between your voice and the caption engine. Align those three, avoid the Bluetooth profile trap, and the captions usually start following your microphone immediately.
