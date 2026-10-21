---
title: "How to Fix Click to Do Not Working in Outlook on AI PCs"
slug: click-to-do-not-working-outlook
date: 2026-10-21
categories: ["ai-pc"]
tags: ["click to do not working", "click to do outlook", "copilot+ pc", "click to do email", "windows 11", "ai actions"]
description: "Fix Click to Do not working in Outlook on your AI PC with six step-by-step methods covering app support, text selection, NPU state, and Outlook configuration."
thumbnail: "/images/thumbs/click-to-do-not-working-outlook.webp"
faqs:
  - q: "Why does Click to Do work elsewhere but not in Outlook?"
    a: "Click to Do hooks into Outlook's reading pane through accessibility interfaces. If hardware acceleration is off, an add-in interferes, or you use legacy Outlook or Windows Mail, the hooks fail only inside Outlook."
  - q: "Does Click to Do work in new Outlook and classic Outlook?"
    a: "Click to Do is designed for the new Outlook for Windows. Classic Outlook (Win32) and the old Windows Mail app have limited or no support — switching to the new Outlook usually fixes it."
  - q: "Can I use Click to Do actions on email addresses in Outlook?"
    a: "Yes — select an email address in a message and Click to Do offers to send an email or add a contact. If that menu never appears, work through the selection and app-support fixes below."
  - q: "Does Click to Do need the NPU to work in Outlook?"
    a: "Yes. Click to Do's text analysis runs on the NPU, so if the neural processor is disabled or [never engaged by apps](/articles/npu-not-used-by-apps-windows-11/), the overlay may not appear anywhere, including Outlook."
---

Click to Do is one of the most practical Copilot+ features: highlight text anywhere, and a small menu offers to summarize it, rewrite it, or act on it. In Outlook it should be especially useful — select an email address to send a message, select a meeting time to create an event. So when the menu never appears inside Outlook, the feature feels half-broken.

Often Click to Do works fine in Edge or Notepad while staying silent in Outlook. That pattern points at Outlook-specific integration, not a broken Click to Do.

This guide runs through six fixes in order: verifying the right Outlook client, correcting how you invoke the feature, fixing selection behavior, repairing the NPU layer, and rebuilding Outlook's configuration.

## Why this happens

- **You are using classic Outlook or Windows Mail:** Click to Do targets the new Outlook for Windows. Legacy Win32 Outlook and the retired Windows Mail app do not expose the accessibility hooks it needs.
- **Wrong invocation method:** Click to Do appears after selecting text and pressing **Win + click** on the selection, or via the right-click menu on newer builds. Just selecting text and waiting shows nothing — by design.
- **Outlook hardware graphics acceleration is disabled:** The overlay relies on Outlook's normal composition path. With hardware acceleration off, it cannot anchor to the message window — a cousin of the [Studio Effects video flickering](/articles/studio-effects-flickering-video-fix/) problem.
- **An add-in is intercepting selection or context menus:** Third-party Outlook add-ins (security scanners, CRM plugins, grammar tools) can swallow the selection events or context-menu entries Click to Do depends on.
- **NPU is not being used by apps:** Click to Do's text actions are processed on-device by the NPU. If apps never engage the neural processor, the feature cannot initialize anywhere.
- **High refresh-rate display quirks on ARM laptops:** On Snapdragon Copilot+ PCs, overlay UI can misbehave at nonstandard refresh rates. If the menu flickers and vanishes, [missing 120 Hz options](/articles/120hz-refresh-rate-missing-arm-laptop/) can signal the same display-stack instability.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Switch to the new Outlook for Windows

Click to Do support follows the app, not just Windows. Microsoft built the integration for the new Outlook for Windows. On classic Outlook, Click to Do has nothing to hook into, and no setting changes that.

1. Open the Microsoft Store, search **Outlook**, and install **Outlook for Windows** if it is not present.
2. Or open classic Outlook and toggle **Try the new Outlook** in the top-right, then let it migrate your accounts.
3. Open an email in the new Outlook, select a sentence, and press **Win + left-click** on the selection.
4. If the Click to Do menu appears, the old client was the whole problem.
5. Keep the new Outlook as your default mail app so the integration stays available.

### Fix 2: Use the correct Click to Do invocation in Outlook

Many "not working" reports are really "invoked wrong." Click to Do does not pop up automatically on text selection in most builds — you must select text first, then explicitly summon it.

1. In an Outlook message, click-drag to select the text (an email address is a good test).
2. With the text selected, hold the **Windows key and left-click** directly on the highlight.
3. If nothing appears, right-click the selection instead — on newer builds Click to Do lives in the context menu.
4. Test the same gesture in Notepad; if it works there, the problem is Outlook-specific.
5. Check **Settings > Privacy & security > Click to Do** and confirm the feature toggle is on.

### Fix 3: Re-enable hardware graphics acceleration in Outlook

The new Outlook's rendering settings can break overlay features when hardware acceleration is turned off — commonly disabled as a troubleshooting step for other display issues, then forgotten.

1. In the new Outlook, click the gear icon, go to **Settings**, and search for a hardware acceleration toggle — make sure it is **on**.
2. In classic Outlook, check **File > Options > Advanced** and clear **"Disable hardware graphics acceleration"** if checked.
3. Restart Outlook completely (confirm no Outlook process remains in Task Manager).
4. Select text in a message and invoke Click to Do again.

### Fix 4: Disable interfering Outlook add-ins

Add-ins that modify the reading pane or replace the context menu are prime suspects when Click to Do works everywhere except Outlook. Security and compliance add-ins are the usual culprits.

1. In Outlook, go to **File > Options > Add-ins** (classic) or **Settings > General > Manage add-ins** (new Outlook).
2. Disable all third-party add-ins — especially antivirus email scanners, CRM integrations, and grammar tools.
3. Restart Outlook and test Click to Do on a selected email address.
4. If it works, re-enable add-ins one at a time until the menu breaks again, then leave that one off or update it.

### Fix 5: Verify the NPU is active and used by apps

Click to Do's text understanding runs on the neural processor. If the NPU driver failed or is disabled, Click to Do cannot initialize — and Outlook is often where you notice first. Check Task Manager's Performance tab for the NPU entry.

1. Open Task Manager (**Ctrl + Shift + Esc**) > **Performance** and confirm an **NPU** entry exists.
2. Trigger a Click to Do action in Notepad and watch for an NPU usage spike — no spike means apps are not engaging it.
3. In Device Manager, check the NPU has no warning icon; reinstall the driver from your laptop maker's support page if it does.
4. Install all Windows updates via **Settings > Windows Update** ([official Windows 11 download info](https://www.microsoft.com/en-us/software-download/windows11)).
5. Restart and retest in Outlook.

### Fix 6: Repair or reinstall the Outlook app package

If Click to Do works in every other app and every Outlook setting looks right, the Outlook installation itself may be damaged — particularly the WebView2-based rendering layer. Repairing replaces those components without touching your accounts.

1. Go to **Settings > Apps > Installed apps**, find **Outlook for Windows**, and open **Advanced options**.
2. Click **Repair**, let it complete, then test Click to Do.
3. If repair does not help, click **Reset** — you will sign back into your accounts afterward.
4. As a last resort, uninstall Outlook for Windows, restart, and reinstall it from the Microsoft Store.
5. After reinstall, invoke Click to Do with Win + click on selected text to confirm the integration is back.

## Closing

Click to Do failing only in Outlook is almost always an app-support issue: the wrong Outlook client, the wrong gesture, a disabled graphics path, or a meddling add-in. Work from the client version down through the NPU layer.
