---
title: "Click to Do Rewrite Not Working? How to Fix It"
slug: click-to-do-rewrite-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["click to do", "rewrite", "ai writing", "troubleshooting", "ai pc", "windows 11"]
description: "Click to Do's Rewrite option greyed out or failing on your Copilot+ PC? Learn why the on-device AI text rewrite breaks and restore it with these fixes."
thumbnail: "/images/thumbs/click-to-do-rewrite-not-working.webp"
faqs:
  - q: "What does Click to Do Rewrite do?"
    a: "Rewrite is a Click to Do text action: select text anywhere in Windows, and the on-device AI model rewrites it — making it more concise, more formal, or rephrased. It runs locally on the NPU via the Phi Silica small language model, so it works offline and keeps your text private."
  - q: "Why is Rewrite greyed out in Click to Do?"
    a: "A greyed-out Rewrite usually means the Phi Silica model is not downloaded or the NPU is unavailable. Click to Do needs both: the model package from Windows Update and a working NPU to run it. Check both before assuming the feature is broken."
  - q: "Does Rewrite need an internet connection?"
    a: "No. That is the point — the Phi Silica model runs entirely on-device on your Copilot+ PC's NPU. If Rewrite fails offline, the problem is local: missing model, broken NPU driver, or the feature being disabled."
  - q: "Why does Rewrite work in some apps but not others?"
    a: "Click to Do hooks into the text selection of each app differently. Some apps (notably certain browsers and electron apps) expose selected text in ways Click to Do cannot read. If Rewrite works in Notepad but not in your app, the app compatibility — not your PC — is the limit."
---

Click to Do's Rewrite is one of those quietly magical Copilot+ features: highlight any text, and the on-device AI rephrases it instantly, no cloud round-trip. When it stops working — greyed out, spinning forever, or producing nothing — the magic dies and you are left wondering whether the feature was ever real.

Rewrite depends on a specific chain: the Click to Do feature enabled, the Phi Silica language model downloaded, and the NPU healthy enough to run it. Break any link and Rewrite fails while other Click to Do actions may still work. This guide repairs the chain link by link. If other Click to Do actions are missing too, see our guide on the [Summarize option missing](/articles/click-to-do-summarize-missing/) — the causes overlap.

Test Rewrite on a paragraph in Notepad after each fix; Notepad is the cleanest test surface.

## Why this happens

- **Phi Silica model not downloaded:** The on-device model arrives via Windows Update; without it, Rewrite has no engine.
- **NPU unavailable:** Rewrite runs on the NPU. A driver failure disables it. Snapdragon users should check our [Snapdragon X Elite NPU driver guide](/articles/snapdragon-x-elite-npu-driver-issues/) for platform-specific repairs.
- **Click to Do disabled:** The whole feature can be toggled off in Settings, greying out every action.
- **Incompatible app:** Some apps do not expose selected text to Click to Do's hooks.
- **Corrupted model files:** A partial model download leaves Rewrite spinning forever.
- **Windows build too old:** Click to Do requires a recent Windows 11 24H2-era build.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Confirm Click to Do is enabled

Rewrite cannot work if the parent feature is off. Check the master toggle before anything else.

1. Open Settings > Privacy & security > Click to Do (or search "Click to Do" in Settings).
2. Make sure the feature toggle is on.
3. Also confirm the keyboard shortcut (Windows key + click, or Windows key + Q depending on build) is enabled.
4. Select text in Notepad, invoke Click to Do, and check whether Rewrite appears.

### Fix 2: Install the Phi Silica model via Windows Update

Rewrite's engine is the Phi Silica small language model, delivered through Windows Update. Without it, the option stays greyed out.

1. Open Settings > Windows Update and check for updates.
2. Look for optional updates mentioning AI components or Phi Silica and install them.
3. Keep the laptop plugged in and connected until everything installs, then restart.
4. Test Rewrite in Notepad again.

### Fix 3: Verify the NPU is healthy

Rewrite runs on the NPU. If the AI hardware is missing or its driver crashed, the feature cannot function.

1. Open Task Manager > Performance and confirm the NPU entry exists.
2. If it is missing, work through NPU detection fixes first — the Rewrite problem will resolve with it.
3. If the NPU shows activity in other AI features but Rewrite still fails, the model (not the hardware) is the issue — continue to Fix 4.
4. Snapdragon users: NPU driver quirks are common on this platform; our [Snapdragon X Elite NPU driver guide](/articles/snapdragon-x-elite-npu-driver-issues/) covers them.

### Fix 4: Re-download the model components

A partial or corrupted Phi Silica download leaves Rewrite spinning forever. Forcing a refresh fixes it.

1. In Settings > Windows Update > Update history, look for failed AI component updates.
2. Uninstall any failed Phi Silica / AI component update, then check for updates again.
3. Alternatively, toggle Click to Do off and on in Settings to trigger a model re-check.
4. Restart and test Rewrite on a fresh Notepad paragraph.

### Fix 5: Test in a supported app

Some apps simply do not expose selected text to Click to Do. Confirm the feature works somewhere before blaming your PC.

1. Open Notepad, type a paragraph, select it, and invoke Click to Do.
2. If Rewrite works in Notepad, your PC is fine — the original app is incompatible.
3. Try the same text in Word, Edge, and other apps to map where it works.
4. For incompatible apps, copy text to Notepad, rewrite it there, and paste it back — a workable routine until app support improves.

### Fix 6: Update Windows and reset Click to Do

Click to Do is under active development; each Windows build fixes integration bugs. A reset plus update resolves stubborn cases.

1. Install all pending Windows updates and restart.
2. Toggle Click to Do off in Settings, restart, and toggle it back on.
3. Test Rewrite in Notepad with a simple sentence.
4. If other actions are missing too, our guide on the [Summarize option missing](/articles/click-to-do-summarize-missing/) covers the broader feature repair. Microsoft documents Click to Do requirements on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Rewrite fails when its chain breaks: feature disabled, model missing, NPU down, or an incompatible app. Verify the toggle, install Phi Silica, confirm the NPU, refresh the model, and test in Notepad to separate PC problems from app problems. Once the chain is intact, Rewrite becomes the fastest writing assistant on your laptop — instant, offline, and private. Brand-specific Snapdragon issues are common — see [Lenovo ThinkPad T14s Snapdragon issues](/articles/lenovo-thinkpad-t14s-snapdragon-issues/).
