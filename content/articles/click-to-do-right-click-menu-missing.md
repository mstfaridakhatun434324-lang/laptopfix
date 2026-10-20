---
title: "Click to Do Missing From Right-Click Menu? Fix It Here"
slug: click-to-do-right-click-menu-missing
date: 2026-10-20
categories: ["ai-pc"]
tags: ["click to do", "right click menu", "context menu", "troubleshooting", "ai pc", "windows 11"]
description: "Click to Do not appearing in your right-click menu on Windows 11? Learn why the AI actions vanish from context menus and restore them with these steps."
thumbnail: "/images/thumbs/click-to-do-right-click-menu-missing.webp"
faqs:
  - q: "How do I open Click to Do?"
    a: "The standard methods are pressing the Windows key while clicking selected text, or using the keyboard shortcut Windows key + Q on supported builds. It can also appear in the right-click context menu when text is selected. If none of these work, the feature itself may be disabled."
  - q: "Why did Click to Do disappear after a Windows update?"
    a: "Updates sometimes reset the feature toggle or break the shell extension that injects Click to Do into context menus. Re-enabling the feature in Settings and restarting Explorer usually restores it. This is a settings regression, not a removal of the feature."
  - q: "Does Click to Do appear in every app's right-click menu?"
    a: "No. Click to Do integrates with apps that expose selected text through standard Windows text APIs. It works reliably in Notepad, Word, Edge, and most native apps, but some third-party apps with custom text rendering never show it."
  - q: "Is Click to Do only on Copilot+ PCs?"
    a: "The full on-device AI version with Rewrite and Summarize requires a Copilot+ PC with an NPU. Some basic Click to Do actions may appear on other Windows 11 machines, but the NPU-powered features are Copilot+ exclusives — which is why NPU health matters, as covered in our [NPU not used by apps guide](/articles/npu-not-used-by-apps-windows-11/)."
---

Right-clicking selected text used to offer Click to Do's AI actions — Rewrite, Summarize, and more — and now the menu shows none of them. The feature has not been removed; its shell integration broke, its toggle got reset, or you are testing in an app that never supported it. This guide separates those cases fast.

The key diagnostic is Notepad. If Click to Do appears there but not in your app, the app is the limit. If it appears nowhere, the Windows integration needs repair. Either way the fixes below are ordered from quickest to deepest.

Related action-level problems have their own guides: [Rewrite not working](/articles/click-to-do-rewrite-not-working/) and [Summarize missing](/articles/click-to-do-summarize-missing/). Start with the toggle and Explorer checks below — most users find the menu back within minutes.

## Why this happens

- **Feature toggle reset:** A Windows update turned Click to Do off in Settings.
- **Shell extension failed to load:** The context-menu integration crashed or failed to register.
- **Explorer needs a restart:** The menu cache holds a stale state without the Click to Do entry.
- **Testing in an unsupported app:** Custom text rendering in some apps never triggers the menu.
- **No text actually selected:** Click to Do text actions require an active selection; an empty right-click shows nothing.
- **Group policy or registry disable:** Enterprise policies or tweaking tools can suppress the feature.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Verify the feature toggle

Start in Settings. If the master switch is off, no menu integration can work.

1. Open Settings > Privacy & security > Click to Do.
2. Turn the feature on if it is off.
3. Confirm the activation shortcut is enabled.
4. Select text in Notepad and test both the shortcut and the right-click menu.

### Fix 2: Restart Windows Explorer

The context menu is rendered by Explorer. A restart reloads the shell extensions, including Click to Do's.

1. Open Task Manager, find "Windows Explorer" under Processes.
2. Right-click it and choose Restart — your screen will flicker briefly.
3. After the desktop returns, select text in Notepad and right-click.
4. Check whether the Click to Do entry has returned.

### Fix 3: Test in Notepad to isolate the app

If the menu works in Notepad but not your app, the app never supported the integration — and no Windows fix will add it.

1. Open Notepad, type a sentence, select it, and right-click.
2. If Click to Do appears here, your Windows integration is healthy.
3. Test the same selection in your target app to confirm the limitation.
4. For unsupported apps, use the keyboard shortcut instead of the menu — the shortcut path sometimes works where the menu does not.

### Fix 4: Re-register the shell integration

When the menu is missing everywhere including Notepad, the shell registration is broken. Toggling the feature forces re-registration.

1. Turn Click to Do off in Settings, then restart the laptop.
2. Turn Click to Do back on.
3. Restart Windows Explorer via Task Manager (Fix 2).
4. Test in Notepad again.

### Fix 5: Check for policy or tweaker interference

Enterprise policies and "debloater" scripts sometimes disable AI features. If you ran any tweaking tool, it may be the culprit.

1. Think back to any privacy/debloat scripts run on this PC.
2. Check Settings > Privacy & security for any greyed-out (policy-locked) Click to Do toggle.
3. On work machines, ask IT whether AI features are disabled by policy.
4. Undo the relevant tweak or policy if you control the machine, then restart.

### Fix 6: Update Windows and repair system files

A corrupted shell component or an outdated build can permanently suppress the menu entry until repaired.

1. Install all pending Windows updates and restart.
2. Run `sfc /scannow` and then `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt.
3. Restart once more and test in Notepad.
4. If voice features are also acting up, our [voice mode fix](/articles/copilot-voice-mode-not-working/) covers the related permission layer, and Microsoft documents the feature on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

A missing right-click entry is almost always the toggle, the Explorer cache, or an unsupported app — not a dead feature. Verify the switch, restart Explorer, isolate with Notepad, re-register the integration, check for policy interference, and repair the system files. One of these restores the menu, and once it is back it tends to stay back. Brand-specific Copilot+ issues are common — see [Dell Latitude 7455 Copilot+ issues](/articles/dell-latitude-7455-copilot-issues/).
