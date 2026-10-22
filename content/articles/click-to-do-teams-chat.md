---
title: "How to Use Click to Do in Microsoft Teams Chat on Windows 11"
slug: click-to-do-teams-chat
date: 2026-10-22
categories: ["ai-pc"]
tags: ["click to do teams", "click to do chat", "windows click to do", "teams text actions", "copilot plus pc", "windows 11"]
description: "Click to Do not working in Microsoft Teams chat? Learn how to trigger AI text actions on Teams messages and fix the common failures. Step-by-step guide inside."
thumbnail: "/images/thumbs/click-to-do-teams-chat.webp"
faqs:
  - q: "What is the keyboard shortcut for Click to Do in Teams?"
    a: >
      Select text in the Teams message, then hold the Windows key and left-click the selection. Win + Q with text selected is the alternative. There is no Teams-specific shortcut — it is the same system-wide gesture.
  - q: "Does Click to Do work in Teams meetings captions?"
    a: >
      Live captions in meetings are a separate pipeline. Click to Do targets selectable text like chat messages; meeting captions are handled by the Live Captions feature instead.
  - q: "Why does Click to Do work in Edge but not Teams?"
    a: >
      Edge is a native, first-party surface where text exposure is straightforward. Teams' embedded webview adds a layer that must correctly expose text to Windows — when that layer breaks, Edge keeps working while Teams goes blind.
  - q: "Can my company disable Click to Do in Teams?"
    a: >
      Yes. IT administrators can manage Click to Do through group policy or MDM, and restrictions often target work apps like Teams and Outlook first. Check with IT if the feature is missing only on your work device.
---

Click to Do promises quick AI actions on any selected text — summarize it, rewrite it, translate it. In Microsoft Teams chat, where you live half your workday, selecting a message and getting nothing is a special kind of frustration.

Teams is a complex app: messages render in a web-based surface inside a desktop shell, and Click to Do has to recognize that surface as text before it can act on it. When the handshake between Teams' rendering and Windows' text recognition breaks, selections in chat become invisible to Click to Do. The same web-surface recognition issue causes [Copilot app WebView2 runtime errors](/articles/copilot-app-webview2-runtime-error/), where embedded browser content fails to initialize.

This guide covers six fixes: the correct trigger method in Teams, Teams-specific settings, repairing the text-recognition pipeline, and workarounds when Teams itself is the blocker.

## Why this happens

- **Wrong trigger gesture in Teams:** Click to Do activates with **Windows key + click** (or **Win + Q**) on selected text — many users try right-click or double-click instead, which Teams handles itself.
- **Teams running the wrong architecture build:** On ARM Copilot+ PCs, an emulated x64 Teams build can expose its text through a layer Click to Do cannot read — the native ARM64 Teams build works far better.
- **Teams webview rendering not exposing text:** Teams renders chat in a webview; if that component is damaged or outdated, text selection exists visually but is not exposed to Windows — the same failure behind [Copilot app WebView2 runtime errors](/articles/copilot-app-webview2-runtime-error/).
- **Click to Do disabled by policy:** Work devices often manage Click to Do through policy, and Teams — as a work app — is where the restriction bites first.
- **Outdated Teams client:** Older Teams builds predate Click to Do integration refinements; the feature matrix between Teams versions and Windows builds matters.
- **GPU rendering interfering with text capture:** Hardware-accelerated rendering quirks can prevent the text-recognition layer from reading what is on screen, a problem also seen with [Dell Optimizer AI audio issues](/articles/dell-optimizer-ai-audio-issues/) when audio/video pipelines fight over resources.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the correct trigger inside Teams

Half of all 'not working' reports are a gesture problem. Learn the exact invocation first.

1. Select the message text in Teams chat by dragging across it.
2. Hold the **Windows key** and **left-click** on the selected text — the Click to Do sparkle menu should appear.
3. Alternatively, try **Win + Q** with text selected.
4. If the menu appears, you had a gesture issue, not a broken feature. If nothing appears, continue.

### Fix 2: Update Teams to the latest build

Teams ships its own updates independent of Windows, and Click to Do compatibility improves with newer clients.

1. In Teams, click your profile picture and check for updates; install any available.
2. Alternatively, update Teams through the Microsoft Store.
3. Restart Teams completely after updating — right-click its tray icon and Quit, then relaunch.
4. Retest the Windows-key-plus-click gesture on a chat message.

### Fix 3: Verify you are running native ARM64 Teams on Snapdragon

On Snapdragon Copilot+ PCs, the emulated Teams build is a common source of Click to Do blindness.

1. Open Task Manager, go to **Details**, right-click a column header, and enable the **Architecture** column.
2. Find Teams processes: **ARM64** is native, **x64** is emulated.
3. If emulated, uninstall Teams and reinstall the ARM64 build from Microsoft's site or the Store.
4. Retest Click to Do — native builds expose text far more reliably.

### Fix 4: Repair the WebView2 runtime

Teams' chat surface depends on WebView2. A damaged runtime breaks text exposure for every app that uses it.

1. Download the latest **Microsoft Edge WebView2 Runtime** installer from Microsoft.
2. Run the installer — it repairs in place without removing Teams.
3. Restart the PC to ensure all WebView2 hosts reload cleanly.
4. Test Click to Do in Teams chat again, plus in Edge, to confirm the runtime is healthy.

### Fix 5: Check policy and privacy settings

On managed devices, Click to Do may be restricted precisely where you need it most.

1. Go to **Settings > Privacy & security > Click to Do** and confirm the feature is enabled.
2. Look for any 'managed by your organization' notice — IT policy can disable Click to Do per-app.
3. The [Click to Do not working in Outlook](/articles/click-to-do-not-working-outlook/) guide covers the same policy checks for another Office app.
4. On a personal device with no policy notice, continue to Fix 6.

### Fix 6: Use workarounds while Teams is the blocker

If Teams itself will not cooperate, route around it rather than losing the feature entirely.

1. Copy the Teams message text and paste it into Notepad, then use Click to Do there.
2. Use the Teams web app in Edge — Click to Do works reliably on web pages.
3. Report the issue via **Help > Give feedback** in Teams so Microsoft's Teams and Windows teams see the pairing failure.
4. Keep Teams updated; each monthly release improves Windows AI integration.

## Closing

Click to Do in Teams chat fails at the handshake between Teams' web-based rendering and Windows' text recognition — so fix it at that handshake. Use the right gesture, update Teams, run the native ARM64 build on Snapdragon, repair WebView2, and check policy. And when Teams is simply being Teams, the copy-to-Notepad detour keeps the AI actions one paste away. If Teams-specific trouble persists, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) covers the system-side pieces.
