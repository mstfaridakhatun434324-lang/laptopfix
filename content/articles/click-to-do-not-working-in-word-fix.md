---
title: "How to Fix Click to Do Not Working in Microsoft Word on Your AI PC"
slug: click-to-do-not-working-in-word-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["click to do", "microsoft word", "copilot+ pc", "windows 11", "arm laptop", "troubleshooting"]
description: "Fix Click to Do not working in Microsoft Word on your Copilot+ PC with complete checks for app updates, Click to Do settings, NPU features, and Office repair."
thumbnail: "/images/thumbs/click-to-do-not-working-in-word-fix.webp"
faqs:
  - q: "Why does Click to Do work in Edge but not in Word?"
    a: "Word uses its own text-selection and add-in layer, so Click to Do can fail there even when it works in the browser. An outdated Word build, a disabled Office add-in, or a Word setting that changes how text is selected is usually the cause."
  - q: "Do I need a Copilot+ PC for Click to Do in Word?"
    a: "Yes, the full Click to Do experience, including on-device AI actions, requires a Copilot+ PC with an NPU. On other PCs the feature may be missing entirely or limited to basic actions, which is normal and not a fault."
  - q: "Can an Office repair fix Click to Do in Word?"
    a: "Often, yes. A Quick Repair restores missing Office components that Click to Do hooks into, and an Online Repair rebuilds them fully. Repair is worth trying before reinstalling Word or resetting Windows."
  - q: "Will reinstalling Word delete my documents?"
    a: "No, your documents stay in OneDrive or on your PC when you reinstall Office. Sign back in with the same Microsoft account afterwards so your settings and recent files return."
---

The same gesture works fine in Edge or in a screenshot, so the feature itself is not dead. Something specific to Word is blocking it.

If one breaks, the menu stays silent with no error.

This guide walks through the Word-specific causes first, then the Windows and Copilot+ settings that support the feature. Follow the fixes in order, and test Click to Do in a plain Word document after each step so you know exactly which fix solved it.

## Why this happens

- **Outdated Word or Office build:** Click to Do hooks into newer Office text features, so an older Word build may not expose selections to Windows at all.
- **Click to Do disabled in Windows settings:** If the feature is off, or its keyboard shortcut is changed, the gesture does nothing in every app — and Word is where most people notice first.
- **Word running in compatibility or protected mode:** Documents opened in compatibility mode, or files from untrusted sources opened in Protected View, restrict the editing features Click to Do needs.
- **A conflicting add-in or COM plug-in:** Grammar tools, PDF add-ins, and older Office plug-ins can intercept text selection and swallow the Click to Do gesture.
- **NPU or Copilot+ features turned off:** If on-device AI features are disabled by policy, by a privacy setting, or after an update, Click to Do actions that need the NPU simply do not load.
- **Corrupted Office installation:** A damaged Office component can break the bridge between Word and Windows AI features without affecting normal typing and formatting.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Click to Do is on and test the right gesture

Before blaming Word, make sure the feature itself is enabled and you are using the gesture Word expects. Many "failures" turn out to be a changed shortcut or a selection made in the wrong place, and this check costs less than a minute.

1. Open **Settings > System > Click to Do** (or search for "Click to Do" in Settings) and confirm the feature is switched **On**.
2. Note the activation method shown there — by default, hold the **Windows key** and click selected text.
3. Open a new blank Word document, type a normal sentence, and select it by dragging across the words.
4. Hold the **Windows key** and click inside the highlighted text, then wait two seconds for the menu.
5. If the menu appears in the blank document, the problem is with a specific file or add-in, not with Click to Do itself — move on to Fix 3. A similar selective failure is described in [Click to Do not showing at all](/articles/click-to-do-not-showing/), where the feature is missing everywhere rather than in one app.

### Fix 2: Update Word and Windows together

Click to Do in Word needs a current Office build and a current Windows build, and an update on one side alone often is not enough. Updating both together is the cleanest way to rule out a version mismatch that leaves the menu missing.

1. In Word, go to **File > Account > Update Options > Update Now** and let Office install any available updates, then restart Word.
2. Open **Settings > Windows Update** and install any pending updates, including optional driver updates for your Copilot+ PC.
3. Restart the PC after both updates finish — a restart is what actually registers the new Office and Windows components together.
4. Open Word again, type a fresh sentence in a blank document, select it, and try the Windows-key-plus-click gesture.
5. If an update fails repeatedly, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for the current update troubleshooting steps before trying the deeper fixes below.

### Fix 3: Open the document normally and disable suspect add-ins

Protected View and add-ins are the two Word-side traps most likely to swallow Click to Do, blocking it while everything else in Word looks normal.

1. If Word shows a yellow **Protected View** banner, click **Enable Editing**, save a copy of the file, and test Click to Do in the saved copy.
2. If the file ends in .doc rather than .docx, use **File > Save As** to save it as a modern .docx file and test in the new copy.
3. Go to **File > Options > Add-ins**, and at the bottom set **Manage** to **COM Add-ins** and click **Go**.
4. Uncheck every add-in, click **OK**, restart Word, and test Click to Do in a blank document.
5. If it works now, re-enable add-ins one at a time, testing after each, until you find the one that breaks Click to Do — then leave it disabled or update it. See also [Click to Do after the 24H2 update](/articles/click-to-do-not-working-after-24h2-update-fix/).

### Fix 4: Check Copilot+ and privacy settings for AI features

Click to Do's smarter actions run on your PC's NPU, and Windows can quietly gate them behind privacy or AI-feature settings. If those gates are closed, the menu may fail to appear in Word even though basic Windows features still work.

1. Open **Settings > Privacy & security** and review the AI-related and app-permission settings for your device.
2. Confirm that Copilot+ PC features are not disabled by a work or school policy — on a managed device, ask your IT admin whether AI features are allowed.
3. Open **Settings > System > About** and confirm the device is listed as a Copilot+ PC with an NPU; on a non-Copilot+ PC, limited Click to Do behaviour is expected.
4. Sign in to Windows with the same Microsoft account used for Office, then restart Word and test again.
5. If AI actions are missing but the basic menu appears, update your NPU driver from your PC maker's support page or from [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) if your device uses an Intel NPU.

### Fix 5: Repair Office with Quick Repair, then Online Repair

When updates and add-in checks do not help, the Office installation itself is the likely fault. A repair rebuilds the components Click to Do hooks into, without touching your documents, and it is far quicker than a full reinstall.

1. Close Word and all other Office apps completely.
2. Open **Settings > Apps > Installed apps**, find **Microsoft 365** or **Microsoft Office**, click the three dots, and choose **Modify**.
3. Choose **Quick Repair**, click **Repair**, and wait for it to finish, then restart Word and test Click to Do.
4. If Quick Repair does not help, repeat the steps and choose **Online Repair** instead — this downloads fresh Office files and takes longer, so keep the PC plugged in.
5. After Online Repair, sign back in to Office, open a blank document, and test the Windows-key-plus-click gesture on selected text.

### Fix 6: Reinstall Office and reset the Word profile

If Click to Do still refuses to appear in Word after a repair, a clean reinstall removes the last layer of corruption: damaged templates and leftover Office files that a repair leaves behind.

1. Back up custom Word templates, then uninstall Microsoft 365 from **Settings > Apps > Installed apps**.
2. Restart the PC, reinstall Office from your Microsoft account page, and sign in.
3. Open Word and test Click to Do in a brand-new blank document before opening old files.
4. If it works in the blank document but not in an old file, copy that file's text into a new document with **Paste > Keep Text Only**.
5. As a final check, test Word under a new Windows user profile; if it works there, your original profile's settings are the cause. Similar cross-app AI breakdowns are covered in [ChatGPT app issues on Windows ARM](/articles/chatgpt-app-windows-arm-issues-fix/).

## Closing

Click to Do failing only in Word is almost always a Word-side problem — an old build, Protected View, a meddling add-in, or a damaged Office install — rather than a dead Copilot+ feature. Update both Word and Windows, isolate add-ins, repair Office, and only then reinstall, and the menu should return to your documents.
