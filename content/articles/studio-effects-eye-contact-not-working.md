---
title: "Studio Effects Eye Contact Not Working? Fix It Step by Step"
slug: studio-effects-eye-contact-not-working
date: 2026-10-25
categories: ["ai-pc"]
tags: ["Studio Effects", "eye contact", "Copilot+ PC", "Windows 11", "webcam"]
description: "Studio Effects eye contact not working? Learn why gaze correction fails and how to restore natural eye contact on your Copilot+ PC webcam."
thumbnail: "/images/thumbs/studio-effects-eye-contact-not-working.webp"
faqs:
  - q: "What does Studio Effects eye contact do?"
    a: >
      Eye contact uses the NPU to adjust your gaze in video calls so you
      appear to look at the camera even when you are reading the screen.
      It makes video calls feel more natural without you changing how you
      sit or work.
  - q: "Why is eye contact greyed out or missing?"
    a: >
      Eye contact requires a Copilot+ PC with a supported NPU, a compatible
      camera, and up-to-date Windows and drivers. If any of those are
      missing, the option is hidden or greyed out rather than broken.
  - q: "Does eye contact work in all video apps?"
    a: >
      Eye contact works at the system camera level, so it applies in most
      video apps once enabled in Windows Studio Effects settings. Some apps
      with their own camera processing may interact with it differently.
  - q: "Can eye contact look unnatural?"
    a: >
      If the effect is too strong or the camera angle is extreme, gaze
      correction can look slightly artificial. Sitting at a normal distance
      with the camera at eye level gives the most natural result.
---

Eye contact is the subtlest Studio Effect and, when it works, the most impressive: you read your notes on screen, and everyone on the call sees you looking right at them. When it fails — greyed out, having no visible effect, or making your gaze look strange — video calls lose that natural feel, and the setting becomes a source of frustration rather than polish. Most eye contact failures are about hardware support, drivers, or camera setup, not about the effect itself being broken.

The first split is availability versus function. If the option is missing entirely, your hardware or Windows build does not support it yet. If the option is present but does nothing, the camera, driver, or NPU pipeline is at fault. Those are different problems with different fixes, and the guide below addresses them in order.

Wake and presence features share the same camera and NPU pipeline, so check them for clues. If [wake on approach is not working](/articles/wake-on-approach-not-working/) or [Snipping Tool background blur is missing](/articles/snipping-tool-blur-background-not-working/), the camera pipeline itself may be the issue. And if captions behave oddly at boot, our guide to [live captions auto-start on boot](/articles/live-captions-auto-start-boot/) covers the related startup layer.

## Why this happens

- **Hardware not supported:** Eye contact needs a Copilot+ NPU; non-Copilot+ PCs do not offer it.
- **Outdated Windows build:** Older builds lack Studio Effects or the eye contact option.
- **Camera driver problem:** A faulty camera driver breaks the video pipeline eye contact depends on.
- **NPU driver problem:** A missing or broken NPU driver prevents the effect from processing.
- **Effect not enabled:** Eye contact can be toggled off in Studio Effects settings without any warning.
- **Camera angle too extreme:** A camera far above or below eye level makes gaze correction unreliable or unnatural.
- **App overriding camera processing:** Some video apps apply their own effects that conflict with Studio Effects.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm eye contact is supported and enabled

Before troubleshooting function, confirm availability. Check your PC type, Windows build, and the Studio Effects settings to see whether eye contact should even be present.

1. Confirm your PC is a Copilot+ PC with an NPU.
2. Open Settings, go to System, then About, and note your Windows build.
3. Open Settings, go to Bluetooth & devices, then Cameras, and open Studio Effects.
4. Check whether eye contact appears and is toggled on.
5. If absent, update Windows — the feature may arrive with a newer build.
6. If present but off, turn it on and test in a video call.

### Fix 2: Update Windows and camera drivers

Studio Effects depend on current OS components and camera drivers. Updating both is the highest-yield fix for effects that are present but non-functional.

1. Open Settings, go to Windows Update, and install all pending updates.
2. Restart when prompted.
3. Open Device Manager, expand Cameras, and update the camera driver.
4. Also update the NPU driver under Neural processors.
5. Restart again after driver updates.
6. Re-enable eye contact in Studio Effects and test.

### Fix 3: Test the camera itself first

If the camera feed is broken, eye contact cannot work on top of it. Testing the camera in the Camera app isolates camera faults from effect faults cleanly.

1. Open the Windows Camera app.
2. Confirm the video feed is clear and smooth.
3. If the feed is black, frozen, or missing, fix the camera first.
4. Check for a physical privacy shutter and open it.
5. Confirm camera permission is granted to the Camera app.
6. Once the feed is healthy, retest eye contact.

### Fix 4: Fix the NPU pipeline

Eye contact runs on the NPU, so an NPU problem stops it even when the camera is fine. A Device Manager check and driver refresh restores the processing path.

1. Press Windows + X and open Device Manager.
2. Expand Neural processors and check for warnings.
3. Right-click the NPU and choose Update driver.
4. If updating fails, uninstall the device and restart for reinstallation.
5. Confirm the NPU shows healthy with no warnings.
6. Re-enable eye contact and test in a call.

### Fix 5: Improve camera position and lighting

Gaze correction works best within a normal geometry: camera near eye level, reasonable distance, decent lighting. Extreme angles and dark rooms make the effect unreliable or artificial, which looks like failure.

1. Position the camera at or near eye level.
2. Sit at a normal laptop distance, not extremely close or far.
3. Ensure your face is well lit from the front.
4. Avoid strong backlight that silhouettes your face.
5. Test eye contact in a call and ask the other person how it looks.
6. Adjust position until the effect looks natural.

### Fix 6: Disable conflicting app effects

Video apps with their own background or gaze features can fight Studio Effects. Turning off the app's own processing lets Windows' eye contact work cleanly.

1. Open your video app's camera or effects settings.
2. Turn off its own eye contact, gaze, or background effects.
3. Keep only Windows Studio Effects enabled.
4. Restart the video app.
5. Test eye contact again.
6. If the app has no such settings, test eye contact in a different app to isolate the conflict.

### Fix 7: Reset Studio Effects settings

When everything else checks out but eye contact still does nothing, resetting the effects clears hidden misconfiguration. Toggle all effects off, restart, and re-enable them one by one, testing eye contact last.

1. Open Studio Effects settings.
2. Turn off all effects, including eye contact.
3. Restart your PC.
4. Turn eye contact back on alone.
5. Test in a video call.
6. Re-enable other effects one at a time.
7. For persistent problems, see the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

Studio Effects eye contact fails for understandable reasons: unsupported hardware, outdated drivers, a broken camera feed, or bad geometry. Work through support, drivers, and camera health before concluding the effect is broken — in most cases one of those layers is the real culprit. Once it works, it quietly transforms video calls, letting you read, think, and glance at notes while still appearing fully present.
