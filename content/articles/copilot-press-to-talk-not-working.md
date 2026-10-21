---
title: "How to Fix Copilot Press to Talk Not Working on Your AI PC"
slug: copilot-press-to-talk-not-working
date: 2026-10-21
categories: ["ai-pc"]
tags: ["copilot press to talk not working", "copilot voice input broken", "copilot hold to talk", "windows 11", "ai pc", "voice control"]
description: "Copilot's press-to-talk not working? Restore voice input with six step-by-step fixes for mic permissions, app conflicts, keybinds, and driver rollbacks."
thumbnail: "/images/thumbs/copilot-press-to-talk-not-working.webp"
faqs:
  - q: "Why does Copilot's press-to-talk do nothing when I hold it?"
    a: "The voice chain has several links — the button or keybind, microphone permission, the selected input device, and the audio driver. If any link is broken, usually a revoked permission or another app holding the mic, press-to-talk silently fails while typing keeps working."
  - q: "Does press-to-talk need the NPU on a Copilot+ PC?"
    a: "Basic voice input does not — it runs through the standard audio stack and the cloud. Enhanced on-device voice features on Copilot+ PCs do use the NPU, so if those broke after a driver update, the NPU driver is worth checking."
  - q: "Why did press-to-talk stop working after a Windows update?"
    a: "Updates commonly reset privacy permissions, change the default input device, or replace audio drivers. Any of those breaks the voice chain without touching the rest of the app, which is why typing still works."
  - q: "Can I use press-to-talk offline?"
    a: "No. Voice input is transcribed in the cloud, so press-to-talk needs an active internet connection. Offline, the button will appear to do nothing even when every local setting is correct."
---

You press and hold the microphone button in Copilot — or the push-to-talk key — and nothing happens. No listening animation, no waveform, no transcribed text. Typing works perfectly, so the app is alive; only the voice path is dead.

Press-to-talk is a chain, and the app rarely tells you which link broke: the button or keybind has to reach Copilot, the microphone permission has to be granted, the right input device has to be selected, no other app can be hogging the mic, and the audio driver has to deliver clean audio. One broken link silences the whole feature.

This guide gives you six fixes in technician order: quick permission and device checks first, then mic conflicts, in-app voice settings, app repair, and driver fixes. Work through them in sequence and test the button after each step.

## Why this happens

- **Microphone permission revoked**: A Windows update or privacy reset can silently revoke Copilot's mic access. Typing is unaffected, so the failure looks like a broken button rather than a permission problem.
- **Another app holds the microphone exclusively**: Teams, Zoom, Discord, or a recorder can take exclusive control of the mic. Copilot then gets no audio stream and the talk button appears dead.
- **Push-to-talk keybind conflict**: A global hotkey in another app — a launcher, screenshot tool, or game overlay — can eat the keystroke before Copilot ever sees it.
- **Voice input disabled in Copilot's settings**: The in-app voice toggle can flip off after an update, disabling the button even though the microphone itself is fine.
- **Wrong input device selected**: Windows may be listening to a disconnected USB headset or a disabled mic array while your real microphone sits idle — Copilot hears silence.
- **Broken audio or NPU driver after an update**: Voice processing leans on the audio stack, and Copilot+ voice enhancements use the NPU. A bad driver update breaks the pipeline while the rest of the app keeps working.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify microphone permission and the default input device

Most press-to-talk failures are permission or device problems, and both take under a minute to check. Start here before suspecting anything deeper.

1. Open **Settings > Privacy & security > Microphone** and confirm both the master **Microphone access** toggle and **Microsoft Copilot** are turned **On**.
2. Go to **Settings > System > Sound**, and under **Input** select the microphone you actually use — the built-in array or your headset.
3. Speak and watch the input volume bar move. A flat bar means the wrong device is selected or the mic is muted.
4. Fully close Copilot from Task Manager, reopen it, and hold the talk button again.

### Fix 2: Free the microphone from apps holding it exclusively

If another app has claimed the mic in exclusive mode, Copilot's talk button gets no audio no matter what you press. This is especially common when Teams or Zoom was recently in a call.

1. Close **Teams, Zoom, Discord**, and any voice recorder completely — check Task Manager for lingering background processes.
2. Open **Control Panel > Sound > Recording**, double-click your microphone, and open the **Advanced** tab.
3. Uncheck **"Allow applications to take exclusive control of this device"** and click OK.
4. Retest press-to-talk. If Teams itself is unstable on your machine, note that an unstable Teams can hold the mic hostage even after its window closes — see our guide to [Teams crashing on Snapdragon laptops](/articles/teams-crashing-snapdragon-laptop/) for that separate repair.

### Fix 3: Re-enable voice input and check the keybind in Copilot

The app's own voice toggle and shortcut binding are the next suspects — updates flip them more often than anyone admits.

1. In Copilot, open **Settings** and look for **Voice input**, **Voice mode**, or a microphone toggle — make sure it is enabled.
2. If Copilot offers a push-to-talk shortcut setting, confirm the key shown matches the one you are pressing, and reassign it if it looks wrong.
3. Test with the on-screen microphone button instead of the keyboard shortcut — if the button works, the problem is the keybind, not the mic.
4. If a keybind conflict is confirmed, check other apps for the same global hotkey: close launchers, screenshot tools, and overlays one by one until the key reaches Copilot.

### Fix 4: Repair the Copilot app to re-register voice handlers

When the button does nothing at all — no error, no animation — Copilot's voice registration with Windows may be corrupt. The built-in repair re-registers it cleanly.

1. Open **Settings > Apps > Installed apps**, find **Microsoft Copilot**, and open **Advanced options**.
2. Click **Repair** first, then test the talk button. This keeps your data while fixing broken app wiring.
3. If the button is still dead, click **Reset** to clear the app's local state, then sign back in.
4. Note the distinction: if Copilot ignores clicks entirely — not just the talk button — the whole app is wedged rather than the voice path. For that, see [Copilot not responding](/articles/copilot-not-responding/) instead.

### Fix 5: Roll back or update the audio and NPU drivers

A driver update that landed just before press-to-talk died is the prime suspect. Rolling it back — or replacing a corrupt one — restores the voice pipeline.

1. Open **Device Manager**, expand **Audio inputs and outputs**, right-click your microphone, choose **Properties > Driver**, and use **Roll Back Driver** if it is available.
2. Do the same under **Sound, video and game controllers** for your audio device.
3. On Snapdragon X machines, voice features have broken specifically after NPU driver updates — the [Qualcomm NPU driver rollback walkthrough](/articles/qualcomm-npu-driver-rollback-windows-11/) reverses exactly that scenario step by step.
4. Restart after any driver change and retest press-to-talk before changing anything else.

### Fix 6: Clean-boot to find the conflicting software

If every setting and driver checks out, some background program is intercepting the button or the mic. A clean boot isolates it by starting Windows with only essential services.

1. Press **Win + R**, type **msconfig**, and on the **Services** tab check **Hide all Microsoft services**, then **Disable all**.
2. On the **Startup** tab (or Task Manager > Startup apps), disable everything, then restart.
3. Test press-to-talk in the clean state. If it works, re-enable services and startup apps in halves until the culprit returns.
4. Common offenders: voice changers, audio enhancement suites, macro tools, and aggressive antivirus shields — keep the offender disabled or add an exception for Copilot.

## Closing

Press-to-talk fails silently because it depends on a whole chain — permission, device, exclusivity, keybind, app registration, driver — and Copilot shows you none of it. Work the chain from the top: toggles and device first, then mic conflicts, then the app, then drivers. One of these six fixes restores the button in nearly every case, and the clean boot catches the rare software conflict. Microsoft's voice-input basics are documented on the official [Windows support page](https://support.microsoft.com/en-us/windows).
