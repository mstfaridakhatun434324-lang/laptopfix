---
title: "How to Fix Click to Do Summarize Not Working on PDFs in Windows 11"
slug: click-to-do-summarize-pdf-not-working
date: 2026-10-22
categories: ["ai-pc"]
tags: ["click to do summarize pdf", "click to do pdf", "windows click to do", "summarize pdf windows 11", "copilot plus pc", "windows 11"]
description: "Click to Do won't summarize your PDF on Windows 11? Fix the missing or broken Summarize action on PDFs with these six troubleshooting steps for Copilot+ PCs."
thumbnail: "/images/thumbs/click-to-do-summarize-pdf-not-working.webp"
faqs:
  - q: "Does Click to Do Summarize work offline?"
    a: >
      Yes — summarization runs on the on-device Phi Silica model, so it works without an internet connection once the model components have downloaded. That is also why a missing model download breaks it completely.
  - q: "Why is Summarize missing but Rewrite works?"
    a: >
      Rewrite and Summarize use different model capabilities. A partial model download or a struggling NPU can leave one working while the other fails — updating Windows and checking NPU health usually restores both.
  - q: "Can Click to Do summarize a scanned PDF?"
    a: >
      Not directly. Scanned PDFs contain images, not text. Run OCR on the file first to add a text layer; afterward, Click to Do treats it like any other text PDF.
  - q: "Is there a length limit for Summarize?"
    a: >
      Very long selections can exceed the on-device model's context window and fail. Summarize in section-sized chunks for long documents — it is faster and the summaries are better anyway.
---

Select a wall of text in a PDF, trigger Click to Do, and the Summarize action should distill it in seconds using the on-device Phi Silica model. When Summarize is missing, greyed out, or errors on PDFs specifically, the feature feels half-built.

PDF summarization has more moving parts than plain-text actions: the PDF reader must expose real text (not a scanned image), the text must reach the on-device model, and the model components must be present and healthy. A break at any link kills Summarize while simpler actions like copy keep working. The same multi-link fragility shows up in [Copilot app work account sign-in](/articles/copilot-app-work-account-sign-in/), where one expired token breaks an entire sign-in chain.

Six fixes below: verifying the PDF has real text, checking the model components, repairing the pipeline, and choosing the right PDF reader. Test Summarize after each step.

## Why this happens

- **Scanned-image PDFs have no text to summarize:** A scanned PDF is pictures of pages, not text. Click to Do cannot summarize what the reader itself cannot select as text — the most common 'failure' is actually correct behavior.
- **On-device model components missing:** Summarize runs on the Phi Silica small language model via Windows Copilot Runtime. If those components failed to download, the action cannot run — the deeper cause behind many [Click to Do Summarize option missing](/articles/click-to-do-summarize-missing/) reports.
- **PDF reader not exposing selected text:** Some third-party PDF readers render text through custom engines that do not expose selections to Windows' text pipeline.
- **NPU unavailable for the model:** Phi Silica prefers the NPU; if the NPU driver is broken, the model may fail to initialize even though simpler Click to Do actions work.
- **Document too long or too short:** Extremely long selections can exceed the model's context window, and tiny selections give it nothing to summarize — both present as a failed or missing action.
- **Corrupt Windows Copilot Runtime:** The shared runtime that hosts the model can itself be damaged, breaking every AI action that depends on it while leaving basic text actions intact.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the PDF contains real selectable text

Do not troubleshoot the AI before confirming there is text for it to read.

1. Try selecting text in the PDF with the mouse. If you cannot select individual words — only drag a rectangle — it is a scanned image.
2. For scanned PDFs, run OCR first (many free tools do this) to create a text layer, then retry Summarize.
3. Test Summarize on a known-good text PDF, like a Microsoft documentation page saved as PDF.
4. If text PDFs summarize fine, your original file was the problem all along.

### Fix 2: Check that the on-device AI components are present

Summarize needs the local model; without it, the action silently degrades.

1. Go to **Settings > Windows Update** and install all pending updates — model components arrive through Windows Update.
2. Check **Settings > Privacy & security > Click to Do** (or Text actions) for any notice about required components downloading.
3. Keep the PC plugged in and connected for an hour after updating so background downloads complete.
4. Audio-pipeline AI features share these components — [MyASUS AI noise cancellation](/articles/myasus-ai-noise-cancellation-problems/) shows how the same downloads affect other on-device AI.

### Fix 3: Switch to Edge as your PDF reader for the test

Edge's PDF reader has the deepest Click to Do integration. Isolate whether the reader or the system is at fault.

1. Right-click the PDF, choose **Open with > Microsoft Edge**.
2. Select text in Edge's reader and trigger Click to Do with **Windows key + click**.
3. If Summarize works in Edge but not your usual reader, the reader was the blocker — consider switching readers.
4. If it fails in Edge too, the problem is system-wide — continue below.

### Fix 4: Verify the NPU is healthy

The summarization model leans on the NPU. A sick NPU starves it.

1. Open **Task Manager > Performance** and confirm the NPU tab exists and shows activity.
2. Open **Device Manager > Neural processors** and confirm no warning icons.
3. If the NPU is missing or errored, fix the NPU driver first — AI actions will follow.
4. Retest Summarize after the NPU is healthy; model initialization often starts working immediately.

### Fix 5: Repair Windows Copilot Runtime

When the shared AI runtime is corrupt, every model-backed action fails together.

1. Install all pending Windows updates and restart — the runtime ships with the OS.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt.
3. Test a different model-backed action (like Rewrite on plain text) to see if the whole runtime or just PDF handling is broken.
4. Account-related AI failures have a different signature — [Copilot app work account sign-in](/articles/copilot-app-work-account-sign-in/) helps distinguish them.

### Fix 6: Right-size your selection and retry

Sometimes the feature works and the input does not. Selections at the extremes confuse the model.

1. Select a moderate chunk — a few paragraphs, not the entire 200-page document.
2. Avoid selecting headers, footers, and page numbers mixed with body text.
3. For very long documents, summarize section by section and combine the results.
4. If moderate selections summarize reliably, adopt chunking as your workflow rather than fighting the limit.

## Closing

Click to Do Summarize on PDFs fails for concrete reasons: image-only PDFs, missing model components, an incompatible reader, or a sick NPU. Check the text layer first, confirm the on-device model is downloaded, test in Edge, and verify NPU health. Work through the chain methodically and the Summarize button stops being decorative. For deeper system repairs beyond these steps, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) is the authoritative next stop.
