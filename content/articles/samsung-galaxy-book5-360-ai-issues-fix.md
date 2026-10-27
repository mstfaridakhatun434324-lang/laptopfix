---
title: "How to Fix Samsung Galaxy Book5 360 AI Issues on Windows 11"
slug: samsung-galaxy-book5-360-ai-issues-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["galaxy book5 360", "samsung ai", "2-in-1 laptop", "intel core ultra", "windows 11", "troubleshooting"]
description: "Fix Samsung Galaxy Book5 360 AI issues with steps for Copilot, Galaxy AI, Intel NPU drivers, tablet-mode conflicts, and Windows AI features with clear guidance."
thumbnail: "/images/thumbs/samsung-galaxy-book5-360-ai-issues-fix.webp"
faqs:
  - q: "Why do AI features behave differently in tablet mode?"
    a: "Tablet mode changes input, sensor, and app behaviour, and some AI tools expect keyboard, camera, or pen input in a particular state. Folding the laptop or detaching input can pause a feature that worked fine in laptop mode."
  - q: "Does the 360 hinge affect AI features?"
    a: "Not directly. The hinge itself does not disable AI, but posture sensors, auto-rotate, and power profiles tied to tablet mode can change which features Windows offers. Test in laptop mode first to rule this out."
  - q: "Can an Intel driver update fix Galaxy AI problems?"
    a: "Yes, for Windows AI features. The Intel NPU driver powers on-device acceleration for Copilot, Studio Effects, and captions, so a generic driver can disable them even when normal apps run perfectly."
  - q: "Will resetting Copilot remove my notes or files?"
    a: "No. Resetting Copilot clears its local cache and sign-in state only. Your documents, photos, and Samsung data stay untouched, though you will need to sign back in."
---

Your Galaxy Book5 360 adds a twist to normal AI troubleshooting: it is a convertible, so the same AI tool can work in laptop mode and fail when you fold the screen back. Copilot may go quiet, Galaxy AI actions may vanish, or Studio Effects may stop tracking your face after you switch posture. That does not mean the hinge broke the AI — it means posture, sensors, and power profiles are part of the chain on this model.

Underneath, the chain is familiar: an Intel neural processing unit, Samsung Settings, Windows AI components, and account and language settings. A Windows update can replace the Intel driver, Samsung Update can fall behind, or a permission change can block the camera that Studio Effects need. On a 2-in-1, tablet-mode quirks sit on top of all of that.

This guide separates the two layers. First confirm AI works in laptop mode, then fix drivers and apps, then check tablet-mode and sensor settings. Work in order and test one feature after each step.

## Why this happens

- **Intel NPU driver replaced or outdated:** Windows Update can install a generic Intel driver that runs the display but hides the NPU, disabling on-device AI while everything else looks normal.
- **Samsung Settings lagging behind Windows:** Galaxy AI toggles, power profiles, and continuity features depend on Samsung's app, and an old version may not expose options a newer Windows build expects.
- **Tablet-mode and posture sensor confusion:** Auto-rotate, tent mode, and tablet posture can change input and camera behaviour, pausing or hiding AI tools that assume laptop mode.
- **Camera or microphone permission denied:** Studio Effects, voice input, and caption tools need device access. A denied permission makes them fail without a clear explanation.
- **Region, language, or account mismatch:** Copilot+ features need a supported region, display language, and Microsoft account. A local account or changed region removes them silently.
- **Power profile limiting the NPU:** Battery saver and aggressive efficiency profiles can throttle AI acceleration, making tools slow, incomplete, or unresponsive.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test AI in laptop mode first

This step isolates the convertible layer from the AI layer. If AI works flat on a desk but fails folded back, you have a posture or sensor problem, not a driver problem, and the rest of the guide changes.

1. Set the laptop flat in normal laptop mode, with the keyboard facing you and the screen open.
2. Plug in the charger to rule out battery saver, then restart the laptop.
3. Test Copilot, Studio Effects, and one Galaxy AI tool in this position and record the results.
4. Fold the screen into tablet mode and test the same three tools again, noting which ones change.
5. If only tablet mode fails, skip ahead to Fix 6 for posture settings; if both modes fail, continue with Fix 2.

### Fix 2: Update Samsung apps and Windows together

AI breaks when Samsung and Microsoft updates drift apart, because each side expects features the other has not yet delivered. Updating both together closes that gap before you touch drivers.

1. Open **Samsung Update** and install every Samsung driver and app update, especially Samsung Settings.
2. Open the **Microsoft Store**, go to **Library**, and update Copilot and Samsung companion apps.
3. Open **Settings > Windows Update**, install all pending updates, and restart.
4. Reopen Samsung Settings and check whether missing AI toggles have returned.
5. If an update fails, restart and retry that update alone instead of repeating a batch of failed installs.

### Fix 3: Repair the Intel NPU driver

When AI tools stall in both laptop and tablet mode, the Intel driver is the prime suspect. A validated reinstall restores NPU access and often fixes several AI features at once, which is why it comes before app resets.

1. Open **Device Manager > Neural processors** and look for warnings on the Intel AI Boost entry.
2. Use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to scan this laptop and install the recommended graphics and NPU package.
3. Restart when prompted, then check Device Manager again for warning icons.
4. Run Samsung Update once more for any model-specific driver variant Samsung provides.
5. Open **Task Manager > Performance**, confirm the NPU appears, and test background blur to prove it is active.

### Fix 4: Reset Copilot and check account settings

A healthy NPU with a broken Copilot app still produces blank answers, so check the app layer next. This fix also re-checks the account and region settings that quietly gate Copilot+ features.

1. Open **Settings > Accounts** and confirm you are signed in with a Microsoft account, not a local account.
2. Check **Settings > Time & language > Language & region** for a supported country and display language.
3. Open **Settings > Apps > Installed apps**, find **Copilot**, open **Advanced options**, and click **Repair**.
4. Test Copilot, and click **Reset** only if repair fails, then sign back in and wait a minute for sync.
5. If you need help with Windows settings after this step, see [Microsoft Windows support](https://support.microsoft.com/en-us/windows) for current Copilot+ guidance.

### Fix 5: Fix microphone, camera, and caption AI tools

Caption, voice, and Studio Effects tools depend on device access and language packs, so they deserve their own check. A general Copilot repair will not fix a microphone permission, and a microphone fault does not mean the NPU is broken.

1. Open **Settings > Privacy & security > Camera** and **Microphone** and allow access for the apps using AI.
2. Open **Settings > Time & language > Language** and install any missing language packs for captions or translation.
3. Open **Settings > Accessibility > Captions**, toggle live captions off and on, and test with a recorded video first.
4. Test the external microphone separately from the built-in one, switching the input in **Settings > System > Sound**.
5. If captions fail only with an external mic, follow the dedicated guide for [live captions with an external microphone](/articles/live-captions-external-microphone-fix/).

### Fix 6: Fix tablet-mode, rotation, and sensor settings

If laptop-mode AI works but tablet mode does not, posture and sensor settings are the remaining suspects. These settings are easy to overlook because they sit outside the AI menus, yet they decide how Windows presents tools when folded.

1. Open **Settings > System > Display** and check rotation lock and display orientation in tablet mode.
2. Open **Settings > Bluetooth & devices** and confirm pen, touch, and sensor devices show no warnings.
3. In Samsung Settings, check power and device posture options, and set the laptop to **Best performance** while testing.
4. Test AI tools in tablet mode again after each change, rather than changing several settings at once.
5. Compare the behaviour with the [Lenovo ThinkPad X9 Aura AI guide](/articles/lenovo-thinkpad-x9-aura-ai-issues-fix/) for another Intel AI laptop, and if Cocreator-style offline AI also fails, check [Cocreator offline not working](/articles/cocreator-offline-not-working/).

## Closing

On the Galaxy Book5 360, always test AI in laptop mode before blaming drivers, because posture and sensors add a layer other laptops do not have. Once laptop-mode AI is proven, Samsung updates, Intel driver repair, and permission checks will usually restore the rest in both modes.
