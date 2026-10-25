---
title: "Copilot Hey Copilot Wake Word Not Working? Fix It Step by Step"
slug: copilot-hey-copilot-wake-not-working
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Copilot", "voice", "Copilot+ PC", "Windows 11", "wake word"]
description: "'Hey Copilot' wake word not responding? Learn why voice activation fails and how to restore hands-free Copilot on your Copilot+ PC laptop."
thumbnail: "/images/thumbs/copilot-hey-copilot-wake-not-working.webp"
faqs:
  - q: "Why doesn't 'Hey Copilot' wake Copilot?"
    a: >
      The usual causes are the wake word being disabled, microphone
      permissions denied, the wrong input device selected, or the feature not
      yet being available in your region or app version. Background noise and
      a muted microphone cause many false reports too.
  - q: "Does Hey Copilot listen all the time?"
    a: >
      When enabled, the device listens locally for the wake phrase, similar
      to other voice assistants. Audio is only sent for processing after the
      wake word is detected, and you can disable the feature entirely in
      Copilot settings.
  - q: "Do I need a Copilot+ PC for the wake word?"
    a: >
      Hands-free wake word support is tied to newer Copilot app versions and
      hardware capabilities. On older hardware or older app versions the
      option may be absent even though push-to-talk Copilot works fine.
  - q: "Can I use a different wake phrase?"
    a: >
      No. The supported wake phrase is fixed as "Hey Copilot." Custom wake
      phrases are not supported, so the feature only responds to that exact
      phrase spoken clearly.
---

Saying "Hey Copilot" and getting silence is a strange kind of failure — the feature is supposed to be effortless, and when it does not respond you are left wondering whether it is deaf, disabled, or simply not there. Wake word problems are usually settings or microphone issues, not AI failures, which is good news: they are fixable with ordinary checks.

The diagnostic split is simple. First, confirm the feature is actually available and enabled on your PC. Then confirm the microphone works and is the one Copilot is listening to. Most reports resolve in one of those two steps; the rest involve app updates, permissions, or environment noise, each with its own fix below.

Battery and sleep behaviour can also interfere, since wake listening interacts with power states. If your machine drains overnight, see our guide to [Copilot+ PC sleep battery drain](/articles/copilot-pc-sleep-battery-drain/), and HP users should check [HP EliteBook X G1i AI issues](/articles/hp-elitebook-x-g1i-ai-issues/). If you run containers or heavy tools on the same machine, our guide to [Docker Desktop on ARM Windows](/articles/docker-desktop-arm-windows/) covers the resource contention that can starve voice services.

## Why this happens

- **Wake word disabled:** The feature is off by default in some versions or was switched off during setup.
- **Microphone permission denied:** Copilot cannot listen without microphone access, and a denied permission blocks it silently.
- **Wrong microphone selected:** A headset, dock, or external mic may be selected while you speak into the laptop's built-in array.
- **Microphone muted or too quiet:** Hardware mute keys, low gain, or privacy shutters block input before Copilot ever hears it.
- **Feature not yet available:** Wake word support rolls out by region and app version, so it may be absent on your PC.
- **Background noise or distance:** Loud environments and speaking from across the room reduce detection reliability.
- **App not running in the background:** If Copilot is fully closed, it cannot listen for the wake phrase.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the wake word is enabled

Start with the setting itself. If the toggle is off, nothing else matters, and turning it on is a ten-second fix.

1. Open the Copilot app and go to Settings.
2. Find the voice or wake word section.
3. Confirm "Hey Copilot" or voice activation is turned on.
4. If the option is missing, the feature may not have reached your app version — update Copilot from the Store.
5. Toggle it off and back on to clear any stale state.
6. Say "Hey Copilot" clearly and check for a response.

### Fix 2: Test the microphone itself

If the setting is on but nothing happens, the microphone is the next suspect. A quick test in Windows sound settings tells you whether input is reaching the system at all.

1. Open Settings, go to System, then Sound.
2. Under Input, select your microphone and speak.
3. Watch the input volume bar — it should move as you speak.
4. If it does not move, check the hardware mute key and privacy shutter.
5. Try a different microphone, such as a headset, to isolate the fault.
6. Set the working microphone as the default input device.

### Fix 3: Grant microphone permission to Copilot

Windows privacy settings can block Copilot's microphone access even when the mic works elsewhere. Confirming the permission removes a silent blocker that produces exactly this symptom.

1. Open Settings, go to Privacy & security, then Microphone.
2. Confirm microphone access is allowed for the device.
3. Scroll to Copilot and confirm its permission is on.
4. If it was off, turn it on and restart Copilot.
5. Say "Hey Copilot" and check for a response.
6. If permission keeps reverting, check for a work or school policy controlling it.

### Fix 4: Make sure Copilot is running in the background

Wake word listening requires Copilot to be alive in the background. If it is fully closed or blocked from background activity, there is nothing listening for the phrase.

1. Open Copilot and leave it running, minimised rather than closed.
2. Check Task Manager to confirm Copilot's background process is present.
3. Open Settings, go to Apps, then Copilot's advanced options.
4. Confirm background app permissions allow it to run.
5. Add Copilot to startup if you want wake word available after boot.
6. Test the wake phrase with Copilot minimised.

### Fix 5: Update the Copilot app and Windows

Wake word support improves with app updates, and older versions may lack it entirely or have detection bugs. Updating both the app and Windows aligns the feature with its latest fixes.

1. Open the Microsoft Store and update Copilot.
2. Open Settings, go to Windows Update, and install pending updates.
3. Restart after updating.
4. Recheck the wake word setting — it may appear only after the update.
5. Enable it and test with a clear "Hey Copilot."
6. For persistent issues, see the official [Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 6: Improve the listening environment

Detection is a signal problem as much as a software problem. Speaking clearly, closer to the mic, and in a quieter room can turn an unreliable wake word into a reliable one without changing any setting.

1. Move within a couple of metres of the laptop.
2. Reduce background noise from fans, music, and TV.
3. Speak the phrase clearly, at normal volume, without rushing it.
4. Face the laptop's microphone array directly.
5. Test several times to distinguish random misses from total failure.
6. If detection works close up but not at distance, that is normal range behaviour.

### Fix 7: Reset the Copilot app

When settings, permissions, and hardware all check out but the wake word still fails, the app's own state may be corrupt. A repair or reset clears it without affecting your files.

1. Open Settings, go to Apps, then Installed apps.
2. Find Copilot and open Advanced options.
3. Choose Repair and test the wake word.
4. If Repair fails, choose Reset.
5. Sign back into Copilot and re-enable the wake word.
6. Test again in a quiet room, close to the microphone.

## Closing

"Hey Copilot" silence is almost always a setting, a permission, or a microphone — in that order. Enable the feature, prove the mic works, grant permission, and keep Copilot running, and hands-free activation usually returns. If it works close up but not across the room, that is the normal limit of far-field detection, not a fault worth chasing further.
