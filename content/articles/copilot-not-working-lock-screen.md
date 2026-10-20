---
title: "Copilot Not Working on the Lock Screen? Here's the Fix"
slug: copilot-not-working-lock-screen
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot", "lock screen", "windows hello", "troubleshooting", "ai pc", "windows 11"]
description: "Copilot not responding on the Windows 11 lock screen? Learn why lock-screen Copilot fails to start and enable it properly with these step-by-step fixes."
thumbnail: "/images/thumbs/copilot-not-working-lock-screen.webp"
faqs:
  - q: "Can Copilot work on the lock screen?"
    a: "Yes, Windows 11 supports invoking Copilot from the lock screen on capable devices, primarily for quick voice queries. It is an opt-in feature — you must enable lock-screen Copilot in Settings, and it works best with voice since typing is limited on the lock screen."
  - q: "Why is there no Copilot button on my lock screen?"
    a: "The lock-screen Copilot entry point appears only when the feature is enabled in Settings and your build supports it. If the toggle is missing entirely, your Windows build predates the feature or your region does not have it yet."
  - q: "Is lock-screen Copilot a security risk?"
    a: "Microsoft designed it for limited queries without unlocking — it cannot open your files or apps. If the limitation frustrates you, that is the security boundary working as intended. You can disable the feature entirely if you prefer no assistant on the lock screen."
  - q: "Does lock-screen Copilot need the NPU?"
    a: "Voice queries from the lock screen use the same cloud Copilot as usual, so the NPU is not required. But general Copilot+ PC health matters for the surrounding features — if AI hardware is missing, our [NPU detection guide](/articles/npu-not-detected-windows-11/) is the place to start."
---

You press the Copilot key on the lock screen and nothing happens — no overlay, no listening chime, just the lock screen staring back. Lock-screen Copilot is an opt-in convenience feature, and when it fails the cause is almost always a disabled toggle, a missing build component, or a microphone permission that does not extend to the lock screen.

This is a narrow feature with narrow fixes, which makes troubleshooting fast: verify the toggle exists and is on, verify the build supports it, then check the lock-screen-specific permissions. This guide does that in order.

If Copilot misbehaves inside Windows too, the [Edge sidebar fix](/articles/copilot-edge-sidebar-not-working/) covers the in-OS integration layer. Lock the screen with Windows key + L to test after each fix below.

## Why this happens

- **Feature toggle is off:** Lock-screen Copilot defaults to off and must be enabled in Settings.
- **Windows build too old:** The feature arrived in newer Windows 11 builds; older installs lack it.
- **Microphone not available on lock screen:** Privacy settings can deny mic access before sign-in.
- **Region rollout:** Availability varies by region.
- **Corrupted lock screen components:** A broken Spotlight or lock-screen app cache interferes.
- **Group policy disabled it:** Enterprise machines often suppress lock-screen assistants.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Enable lock-screen Copilot in Settings

The feature is opt-in. If you never turned it on, nothing is broken.

1. Open Settings > Personalization > Lock screen (or search "Copilot lock screen" in Settings).
2. Find the Copilot on lock screen toggle and turn it on.
3. Lock your PC (Windows key + L) and test the Copilot key or voice invocation.
4. If the toggle does not exist, your build lacks the feature — continue to Fix 2.

### Fix 2: Update Windows to a supporting build

Lock-screen Copilot arrived in newer Windows 11 builds. An outdated install simply does not have it.

1. Open Settings > Windows Update and install all pending updates.
2. Restart and check for the lock-screen Copilot toggle again.
3. If it appears, enable it and test on the lock screen.
4. Microsoft documents feature availability on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 3: Allow microphone access on the lock screen

Voice invocation needs mic access before sign-in, which is a separate permission consideration from in-session mic access.

1. Open Settings > Privacy & security > Microphone and confirm access is on.
2. Test voice features inside Windows first (see our [voice mode fix](/articles/copilot-voice-mode-not-working/)) — if voice fails there too, fix that first.
3. Lock the screen and try a voice query: "Hey Copilot" or the Copilot key.
4. If voice works in-session but not on the lock screen, the lock-screen path specifically is restricted — continue to Fix 5.

### Fix 4: Check region availability

If the toggle exists but does nothing, or never appeared despite updates, region rollout may be the answer.

1. Confirm your region in Settings > Time & language > Language & region.
2. Compare with Microsoft's published availability for lock-screen Copilot.
3. Do not change regions just for this — the feature will arrive with the rollout.
4. Use in-session Copilot meanwhile; it has the full feature set.

### Fix 5: Repair lock screen components

A corrupted lock-screen cache can suppress the Copilot entry point even when the feature is enabled.

1. In Settings > Personalization > Lock screen, switch the background to a different option and back.
2. Disable and re-enable the lock-screen Copilot toggle.
3. Run `sfc /scannow` in an elevated Command Prompt to repair system files.
4. Restart and test on the lock screen again.

### Fix 6: Check group policy (managed PCs)

Enterprise policy commonly disables lock-screen assistants. On a work laptop, this is likely intentional.

1. Ask IT whether lock-screen Copilot is allowed by policy.
2. On a personal PC, check for tweaking tools that may have disabled lock-screen features and undo them.
3. If policy blocks it, no local fix overrides it — use Copilot after sign-in.
4. For general Copilot health on AI hardware, our [NPU detection guide](/articles/npu-not-detected-windows-11/) confirms the underlying platform. Edge-side integration is covered in [Copilot Edge sidebar not working](/articles/copilot-edge-sidebar-not-working/).

## Closing

Lock-screen Copilot is a small, opt-in convenience, and its failures are equally small: toggle off, build too old, mic unavailable pre-sign-in, or policy-blocked. Enable it in Settings, update Windows, verify the mic path, and accept the security boundary for what it is — quick queries without unlocking, nothing more. If you need the full assistant, sign in; that is where Copilot does its best work anyway. Surface Pro users hit device-specific issues too — see [Surface Pro 11 pen not working](/articles/surface-pro-11-pen-not-working/).
