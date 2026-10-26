---
title: "How to Fix Copilot Voice Input Not Working on Windows 11"
slug: copilot-voice-input-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags:
  - copilot
  - voice-input
  - microphone
  - windows-11
  - troubleshooting
description: "Copilot voice input not working on your Windows 11 PC? Diagnose mic permission, driver, and app problems with these step-by-step fixes that restore dictation."
thumbnail: "/images/thumbs/copilot-voice-input-not-working.webp"
faqs:
  - q: "Why does Copilot say it cannot hear me even though my mic works elsewhere?"
    a: >
      Copilot needs its own microphone permission in Windows privacy settings, separate from other
      apps. If that permission is off, or Copilot is using the wrong input device, it hears nothing
      even while Teams or Zoom works fine with the same microphone.
  - q: "Does voice input need an internet connection?"
    a: >
      Yes. Copilot sends your speech to Microsoft's servers for transcription, so it needs a working
      internet connection. A weak or blocked connection produces silence, timeouts, or half-transcribed
      sentences rather than a clear error.
  - q: "Can a bad audio driver break only Copilot voice input?"
    a: >
      Yes. Copilot uses the Windows audio stack in a specific way, and a corrupted driver or a stale
      enhancement setting can break it while other apps keep working. Updating or reinstalling the
      audio driver is a common fix for exactly this pattern.
  - q: "Will resetting Copilot delete my conversations?"
    a: >
      No. Your chat history is tied to your Microsoft account and syncs back after you sign in again.
      A repair or reset only clears local app data, not your cloud conversations.
---

Talking to Copilot should feel effortless: tap the microphone, speak your question, and watch the answer appear. When voice input stops working, the whole hands-free promise collapses. You click the mic icon and nothing happens, or the app shows a listening animation that never produces a word, or it transcribes only the first syllable and then gives up. Typing still works, which proves Copilot itself is alive — the break is somewhere in the chain between your microphone and the app's speech service.

That chain has more links than most people expect. Windows must grant Copilot microphone permission, the correct input device must be selected, the audio driver must deliver clean samples, and your network must carry the audio to Microsoft's transcription service and back. On Copilot+ PCs there is one more link: the neural processing unit that accelerates on-device AI work. When [Windows ML fails to use the NPU](/articles/windows-ml-npu-not-working/), local AI features can stumble in ways that look like ordinary app bugs, and voice features are no exception.

The fixes below walk that chain from the outside in, starting with permissions and device selection — the causes behind most reports — and moving to drivers, app repair, and network checks. The same step-by-step discipline helps with other silent hardware failures; for instance, owners tracking down [HP Spectre x360 AI quirks](/articles/hp-spectre-x360-ai-issues/) often find that a single misconfigured device setting explains an apparently broken feature. Leftover driver files can cause similar ghosts, which is why [cleaning out old NPU driver leftovers](/articles/clean-driver-store-npu-leftovers/) is worth knowing about when audio and AI features misbehave together.

## Why this happens

- **Microphone permission denied for Copilot:** Windows privacy settings control mic access per app. If Copilot's toggle is off, the app cannot hear anything, no matter how good your microphone is.
- **Wrong input device selected:** With a headset, webcam mic, and built-in array all present, Windows or Copilot may listen to a silent device while your real microphone sits idle.
- **Muted or disabled microphone:** A hardware mute key, a muted input in Sound settings, or a disabled device in Device Manager silences input before any app sees it.
- **Corrupted or outdated audio driver:** A damaged driver can deliver distorted or empty audio streams that Copilot's speech service rejects, while simpler apps tolerate the same stream.
- **Network or service interruption:** Voice transcription happens in the cloud. A blocked connection, a VPN hiccup, or a temporary service issue leaves Copilot listening forever.
- **App cache or sign-in problem:** A stale Copilot cache or an expired sign-in can break the microphone session even when typing works, because voice uses a separate service token.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Allow Copilot to use the microphone

Permissions are the number one cause, and they are also the fastest to check. If this toggle is off, every other fix is wasted effort.

1. Open Settings, then Privacy and security, then Microphone.
2. Make sure "Let apps access your microphone" is turned on.
3. Scroll to Copilot in the app list and turn its toggle on.
4. If Copilot is not listed, open the app once and retry the mic so Windows registers it.
5. Test voice input again immediately after changing the permission.

### Fix 2: Select the correct input device and test it

Windows often defaults to the wrong microphone when several are attached. Confirming the active device with a live test removes all guesswork about which mic is actually being heard.

1. Open Settings, then System, then Sound, and find the Input section.
2. Select the microphone you actually use from the dropdown.
3. Speak normally and watch the input volume bar move.
4. If the bar stays flat, try each other listed device in turn.
5. Set the working microphone as the default and retest Copilot.

### Fix 3: Unmute the microphone everywhere it can be muted

Microphones can be muted in three places at once — a physical key, Windows Sound settings, and the device itself — and any one of them silences Copilot.

1. Check for a microphone mute key or switch on your laptop or headset and turn it off.
2. In Settings, then System, then Sound, open your input device's properties.
3. Make sure the input volume is above zero and the device is not muted.
4. Open Device Manager and confirm the microphone is enabled, not disabled.
5. Test the mic in Voice Recorder to prove Windows hears you before retesting Copilot.

### Fix 4: Update or reinstall the audio driver

When Windows hears you but Copilot does not, the driver is the likely translator at fault. A fresh driver gives Copilot a clean audio stream to transcribe.

1. Open Device Manager, expand Audio inputs and outputs, and right-click your microphone.
2. Choose Update driver, then Search automatically for drivers.
3. If no update is found, choose Uninstall device instead.
4. Restart the laptop so Windows reinstalls a fresh copy of the driver.
5. After restart, test voice input in Copilot again.

### Fix 5: Repair Copilot and refresh your sign-in

A damaged app cache or an expired voice-service token breaks the mic session while leaving typed chat untouched. Repairing the app and refreshing sign-in clears both problems at once.

1. Open Settings, then Apps, then Installed apps, and find Copilot.
2. Click the three dots, choose Advanced options, then click Repair.
3. If the mic still fails, sign out of Copilot and sign back in.
4. Check that your internet connection is stable before testing again.
5. For persistent sign-in trouble, [Copilot in Windows support](https://support.microsoft.com/en-us/windows) lists current service issues.

### Fix 6: Check the network path for voice traffic

Voice transcription needs a clean route to Microsoft's servers. VPNs, strict firewalls, and captive networks can all block that route while ordinary browsing keeps working.

1. Disconnect any VPN temporarily and test voice input again.
2. Try a different network, such as a phone hotspot, to rule out your Wi-Fi.
3. Restart your router if the hotspot test works but home Wi-Fi fails.
4. Make sure your firewall is not blocking the Copilot app.
5. If voice works on the hotspot only, check your router's firewall and DNS settings.

## Closing

Copilot voice input fails quietly because the break can hide in any link of a long chain — permission, device, mute state, driver, network, or app session. Checking those links in order finds the fault quickly, and most fixes take only a few minutes. Once your microphone is properly permitted, correctly selected, and clearly heard, talking to Copilot becomes the effortless shortcut it was meant to be.
