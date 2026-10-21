---
title: "How to Fix \"Microphone Permission Denied\" in the Copilot App"
slug: copilot-microphone-permission-denied
date: 2026-10-21
categories: ["ai-pc"]
tags: ["copilot microphone permission", "mic access denied", "copilot voice input", "windows 11", "ai pc", "privacy settings"]
description: "Copilot says microphone permission denied? Restore Copilot's mic access on your Windows 11 AI PC with six fixes, from privacy toggles to device-level resets."
thumbnail: "/images/thumbs/copilot-microphone-permission-denied.webp"
faqs:
  - q: "Why does Copilot say microphone permission denied?"
    a: "Windows denied the app at the privacy layer — the system-wide microphone toggle is off, Copilot's per-app permission is blocked, or a policy (common on work PCs) disables mic access. The app cannot override that itself, so you must grant it in Settings."
  - q: "I enabled the mic but Copilot still cannot hear me. Why?"
    a: "Permission and input are different layers. If permission is granted but no audio arrives, the wrong default mic, exclusive-mode capture by another app, or a muted array is usually the cause — Fixes 4 and 5 cover those."
  - q: "Is it safe to give Copilot microphone access?"
    a: "Yes, on a personal PC. Copilot only listens while you activate voice input (press-to-talk or the mic button); it does not record in the background. On work or school devices, follow your organization's policy."
  - q: "Does reinstalling Copilot fix permission errors?"
    a: "Sometimes, because a reinstall forces Windows to re-prompt for the microphone permission. But check Settings first — a reinstall cannot fix a system-wide mic toggle that is turned off."
---

You tap the microphone button in Copilot — or hold the push-to-talk key — and get "microphone permission denied." The app wants to listen but Windows will not let it, and voice input is dead.

This is a privacy-layer block, not a broken microphone. Windows 11 gates every app's mic access through two switches: the system-wide microphone toggle and a per-app permission. If either is off — or a policy flipped them — Copilot gets denied before it ever touches the audio hardware.

These six fixes work through the permission layers in order: the Windows privacy toggles, Copilot's per-app access, the default input device, exclusive-mode conflicts, driver repair, and a clean reinstall. Work down the list.

## Why this happens

- **System-wide microphone access is off**: The master toggle under Privacy & security disables the mic for every app — Copilot gets denied at the gate.
- **Copilot's per-app permission is blocked**: The system toggle can be on while Copilot specifically is switched off in the app list.
- **Permission was denied once and remembered**: Tapping "Block" on the first prompt writes a denial Windows keeps until you manually reverse it.
- **Work or school device policy**: MDM policies can disable microphone access entirely; the toggles then appear grayed out and no app can override them.
- **Wrong default input device**: Permission is granted, but Copilot listens on a disconnected or wrong device — a dock mic, a monitor with no mic, or a disabled array.
- **Exclusive mode capture**: Another app (Teams, a recorder, a browser tab) holds the mic in exclusive mode, so Copilot is locked out even with permission granted.
- **Corrupt audio driver state**: A wedged mic driver makes Windows report the device as unavailable, which surfaces as a permission-style denial.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn on the system-wide microphone toggle

This master switch overrides everything below it. If it is off, no per-app setting can help.

1. Open **Settings > Privacy & security > Microphone**.
2. Turn **Microphone access** to **On**.
3. Also turn on **"Let apps access your microphone"** if it appears as a separate toggle.
4. Relaunch Copilot and tap the mic button. On managed devices the toggles may be grayed out — that means IT policy controls them, and only your admin can change that. (Unrelated lock-downs on Snapdragon hardware have their own quirks; see the [BitLocker issues guide for Snapdragon laptops](/articles/bitlocker-issues-snapdragon-laptop/) if your machine is enterprise-managed.)

### Fix 2: Grant Copilot its per-app microphone permission

With the master switch on, find Copilot in the app list — it is commonly the one that is off.

1. On the same **Settings > Privacy & security > Microphone** page, scroll to the app list.
2. Find **Microsoft Copilot** and switch it to **On**.
3. If Copilot is missing from the list, launch it once and use the mic button so Windows registers it, then return here.
4. Test voice input in Copilot immediately — this single toggle resolves most cases. If voice mode itself is glitchy beyond permissions, the [Copilot voice mode not working guide](/articles/copilot-voice-mode-not-working/) goes deeper.

### Fix 3: Force Windows to re-prompt by resetting the app

If the permission list looks right but Copilot still reports denied, its stored permission state may be stale. Resetting the app forces a fresh prompt.

1. Open **Settings > Apps > Installed apps**, find **Microsoft Copilot**, open **Advanced options**.
2. Click **Reset** and confirm — this clears local state, including stored permission grants.
3. Launch Copilot, tap the microphone button, and choose **Allow** when Windows prompts.
4. Recheck the per-app toggle afterward to confirm it stuck.

### Fix 4: Set the correct default microphone

Permission granted but silence means Copilot is listening to the wrong device. Point Windows at the mic you actually use. If the right device is selected and the input bar moves but Copilot still hears nothing, the fault is deeper in the Copilot+ audio path — see our guide on the [microphone not working on Copilot+ PCs](/articles/copilot-plus-pc-microphone-not-working/).

1. Open **Settings > System > Sound**, scroll to **Input**, and select the microphone you want (the laptop's array mic, not a disconnected dock or monitor device).
2. Click the arrow next to it, set **Input volume** to around 75–100, and speak — the test bar should move.
3. Disable input devices you never use (right-click > Disable in the classic Sound panel) so Windows cannot pick them.
4. Test Copilot's mic button again. Microsoft's audio troubleshooting at [Microsoft Support](https://support.microsoft.com/en-us/windows) covers hardware checks if no device shows at all.

### Fix 5: Break exclusive-mode locks and restart audio services

Another app holding the mic exclusively locks Copilot out. Clearing that hold takes seconds.

1. Open **Control Panel > Sound > Recording**, double-click your mic, go to the **Advanced** tab.
2. **Uncheck** "Allow applications to take exclusive control of this device" and click OK.
3. Close Teams, Zoom, Discord, or any recorder that might be holding the mic.
4. Press **Win + R**, type **services.msc**, restart the **Windows Audio** service, then test Copilot. On machines where NPU-driven voice features also fail, driver trouble may be underneath — compare with the [AMD NPU driver update failed guide](/articles/amd-npu-driver-update-failed/).

### Fix 6: Reinstall Copilot and repair the audio driver

When the denial survives every toggle, the app package or the mic driver is corrupt. A reinstall is quick — the package is small — and it forces Windows to show the permission prompt again, which clears denials that no toggle could reach.

1. Uninstall Microsoft Copilot from Settings > Apps, then restart the PC.
2. Open **Device Manager > Audio inputs and outputs**, right-click your microphone, choose **Uninstall device**, and restart — Windows reinstalls a fresh driver on boot.
3. Reinstall Copilot from the Microsoft Store, launch it, and tap the mic button.
4. Choose **Allow** at the fresh permission prompt and verify voice input works end to end.

## Closing

"Microphone permission denied" is Windows doing its privacy job — the fix is simply pointing the right toggles at Copilot and making sure it listens to the right device. Work from the master switch down to the app, clear exclusive-mode locks, and keep one default mic set. Once granted, the permission sticks, and Copilot's voice features stay available.
