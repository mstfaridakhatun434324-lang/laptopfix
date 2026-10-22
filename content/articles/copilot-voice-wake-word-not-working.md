---
title: "How to Fix Copilot Voice Wake Word Not Working on Windows 11"
slug: copilot-voice-wake-word-not-working
date: 2026-10-22
categories: ["ai-pc"]
tags:
  - copilot
  - voice-wake-word
  - microphone
  - windows-11
  - troubleshooting
description: "Copilot won't answer its wake word on your Windows 11 laptop? Fix microphone permissions, speech settings, and app issues with this step-by-step guide."
thumbnail: "/images/thumbs/copilot-voice-wake-word-not-working.webp"
faqs:
  - q: "Why does the Copilot wake word work sometimes but not always?"
    a: >
      Intermittent wake-word detection is usually caused by background noise, a microphone that
      Windows keeps switching to a different default device, or Battery Saver throttling the always-
      listening service. Set a fixed default microphone, turn off Battery Saver while testing, and
      retrain your voice model in a quiet room to stabilize detection.
  - q: "Does the Copilot wake word work on the lock screen?"
    a: >
      By default, no. For privacy reasons Windows disables voice activation while the device is locked
      unless you explicitly allow apps to use voice activation on the lock screen. Go to Settings,
      then Privacy and security, then Voice activation, and review the lock-screen permission for the
      Copilot app.
  - q: "Can I change the Copilot wake word to a custom phrase?"
    a: >
      Currently you cannot set a fully custom wake phrase for Copilot on Windows 11. You can choose
      between the supported wake words offered in the Copilot app settings, such as Hey Copilot,
      depending on your region and app version. Third-party tools that claim custom wake words are not
      supported and may break after updates.
  - q: "Does the wake word drain my laptop battery?"
    a: >
      On Copilot+ PCs the wake-word listener can run on the low-power NPU, so the impact is minimal.
      On older laptops without an NPU the microphone stays active on the CPU, which can add noticeable
      idle drain. If battery life matters more than hands-free access, disable the wake word and use
      the Copilot key or press-to-talk instead.
---

Saying "Hey Copilot" to your laptop and getting silence in return is frustrating, especially when hands-free voice control is the whole point. The Copilot wake word depends on a chain of small things working together: an active microphone, the right app permissions, online speech recognition, and a Copilot app version that actually supports voice activation. If any link in that chain breaks, the wake word quietly stops responding with no error message to point you at the cause.

Start with the simplest checks first. Open the Copilot app and confirm that [press-to-talk still works](/articles/copilot-press-to-talk-not-working/) by holding the microphone button — if manual voice input works but the wake word does not, the problem is isolated to the always-listening service rather than your microphone hardware. On Copilot+ PCs, voice processing can be offloaded to the neural processor; if you suspect a deeper hardware issue, you can [verify your NPU is healthy and being used](/articles/npu-benchmark-tools-windows/) before blaming the app.

It also helps to rule out conflicts with other Windows AI features while you troubleshoot. If you use Click to Do alongside Copilot, note that its actions are separate from voice input — for example, when [Click to Do fails to summarize a PDF](/articles/click-to-do-summarize-pdf-not-working/) the fix lives in that feature's own settings, not in Copilot's. The steps below focus specifically on restoring the wake word, ordered from the most common causes to the rarer ones.

## Why this happens

- **Microphone access turned off for Copilot:** Windows 11 lets you block microphone access per app. If Copilot lost its microphone permission after an update or a privacy-settings change, the wake-word listener cannot hear anything, even though the system microphone works fine in other apps.
- **Wrong default recording device:** Laptops often have several audio inputs — the built-in mic, a headset mic, a webcam mic, and virtual devices from conferencing apps. If Windows switched the default input to a device that is unplugged or muted, the wake word appears dead.
- **Online speech recognition disabled:** Copilot's voice features rely on Microsoft's online speech services. If online speech recognition is switched off in privacy settings, the wake-word engine cannot process what it hears and stays silent.
- **Copilot app is outdated or corrupted:** Voice activation support has changed across Copilot app versions. An outdated install may lack the wake-word toggle entirely, while a corrupted install can leave the toggle visible but non-functional.
- **Battery Saver or power throttling:** The always-listening wake-word service is one of the first things Windows suspends to save power. With Battery Saver on, or on an aggressive power plan, the listener may never start.
- **Unsupported region or language:** The Copilot wake word only works in regions and display languages where Copilot voice features are enabled. A mismatched region format or an unsupported speech language silently disables it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check microphone permission for Copilot

The wake-word listener needs explicit microphone permission, and Windows updates sometimes reset it. Confirming this takes less than a minute and resolves the issue more often than any other single step.

1. Open Settings, then go to Privacy and security and select Microphone.
2. Make sure the main Microphone access toggle is turned on.
3. Scroll to the app list and confirm Copilot is allowed to access the microphone.
4. If it was off, turn it on, then fully close and reopen the Copilot app.
5. Say the wake word once to test whether detection has returned.

### Fix 2: Set the correct default microphone

When several recording devices exist, Windows does not always pick the one you are actually speaking into. Locking in the right default removes a whole class of silent failures.

1. Right-click the speaker icon in the taskbar and choose Sound settings.
2. Under Input, select the microphone you actually use, such as the built-in array mic.
3. Click the device and check the input volume meter moves when you speak.
4. If you see multiple similar entries, disable the ones you never use.
5. Retest the wake word without any headset or USB mic plugged in first.

### Fix 3: Turn on online speech recognition

Copilot's wake word depends on cloud speech services. If this privacy toggle is off, the listener has nowhere to send audio for recognition.

1. Open Settings, then Privacy and security, and select Speech.
2. Bring the Online speech recognition toggle to the On position.
3. Restart the Copilot app so it picks up the changed permission.
4. Say the wake word in a quiet room and watch for the listening indicator.
5. If it still fails, sign out and back into your Microsoft account in Copilot.

### Fix 4: Update or reinstall the Copilot app

Wake-word support lives in the Copilot app itself, not just in Windows. An old or damaged install is a common reason the toggle exists but does nothing.

1. Open the Microsoft Store, search for Copilot, and install any pending update.
2. Open Copilot settings and confirm a voice activation or wake-word option is present and enabled.
3. If the option is missing, uninstall Copilot from Settings, then Apps.
4. Reinstall Copilot fresh from the Microsoft Store and sign in again.
5. Re-enable the wake word in the app's settings and test it immediately.

### Fix 5: Disable Battery Saver and check power settings

Power-saving features suspend background listeners aggressively. This step is especially relevant on laptops running on battery when the problem appears.

1. Open Settings, then System, then Power and battery.
2. Turn off Battery Saver, or plug the laptop into AC power while testing.
3. Set the power mode to Best performance temporarily for diagnosis.
4. Restart the Copilot app and test the wake word on AC power.
5. If it works on AC but not battery, keep the wake word off on battery or adjust the power plan.

### Fix 6: Verify region and language support

A region or language mismatch disables voice features without any warning. This is worth checking if the wake word never worked on this laptop, even when new.

1. Open Settings, then Time and language, and confirm your country or region supports Copilot voice features.
2. Under Language and region, make sure the Windows display language matches a supported speech language.
3. Go to Settings, then Time and language, then Speech, and install the matching speech language pack if prompted.
4. Restart the laptop after changing language or region settings.
5. For official guidance on where Copilot features are available, see [Copilot in Windows support](https://support.microsoft.com/en-us/windows).

## Closing

The Copilot wake word is convenient when it works, but it depends on permissions, the right microphone, and a supported region all lining up. Work through the fixes above in order and test after each change — most people find the culprit in the first three steps. If nothing here restores it, the app version or your region is the likely blocker, and waiting for the next Copilot update is the sensible move.
