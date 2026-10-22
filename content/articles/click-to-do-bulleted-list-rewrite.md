---
title: "How to Fix Click to Do Bulleted List Rewrite Not Working"
slug: click-to-do-bulleted-list-rewrite
date: 2026-10-22
categories: ["ai-pc"]
tags: ["click to do rewrite list", "bulleted list rewrite", "windows click to do", "rewrite not working", "copilot plus pc", "windows 11"]
description: "Click to Do mangling your bulleted lists when rewriting? Fix list-aware rewriting on your Copilot+ PC with these targeted steps. For Windows 11 24H2+."
thumbnail: "/images/thumbs/click-to-do-bulleted-list-rewrite.webp"
faqs:
  - q: "Why does Rewrite turn my bulleted list into a paragraph?"
    a: >
      The on-device model prioritized rewording over structure preservation — usually because the list was long, inconsistently formatted, or selected together with surrounding prose. Clean formatting plus smaller chunks fixes most cases.
  - q: "Can Click to Do rewrite numbered lists too?"
    a: >
      Yes, with the same caveats as bulleted lists: keep numbering simple, avoid nesting, and rewrite in chunks. Verify the numbering survived afterward — models occasionally renumber creatively.
  - q: "Is list rewriting worse than prose rewriting?"
    a: >
      It is a harder task for a small on-device model: preserving hierarchy while changing words. Expect slightly lower fidelity than prose rewriting and verify important lists manually.
  - q: "Does the NPU affect rewrite quality?"
    a: >
      Indirectly. The model runs best with adequate NPU resources; when the NPU is saturated by concurrent AI features, output quality — especially on hard tasks like list rewriting — can degrade.
---

Rewrite is brilliant on prose — select a paragraph, get a polished version. Select a bulleted list, and sometimes the result is a mess: bullets merged, hierarchy flattened, or the list rewritten as a paragraph. When Rewrite mishandles lists specifically, the problem is narrower than a broken Rewrite.

List-aware rewriting asks more of the on-device model: it must preserve structure while changing wording, a harder task than rephrasing flowing text. Failures cluster around structure preservation rather than language quality. It is the same 'harder subtask fails first' pattern as [ONNX Runtime DirectML CPU fallback](/articles/onnxruntime-directml-fallback-cpu/), where the model handles simple inference but stumbles on the complex path.

Six fixes below: formatting your source lists well, verifying the model pipeline, and working around the model's structural weaknesses. Test Rewrite on a simple 5-bullet list after each step.

## Why this happens

- **Inconsistent list formatting:** Mixed bullets, tabs, manual line breaks, and multi-paragraph bullets confuse the model's structure parsing — garbage in, flattened list out.
- **Model struggling with structure preservation:** The small on-device model is weaker at layout fidelity than a cloud model; complex nested lists exceed what it reliably preserves.
- **Selection including surrounding prose:** Selecting the list plus adjacent paragraphs gives the model mixed content, and it often 'resolves' the mix by converting everything to prose.
- **Runtime or model components degraded:** A damaged Copilot Runtime degrades the hardest tasks first — list rewriting fails while simple prose rewriting still works, mirroring [Click to Do Rewrite not working](/articles/click-to-do-rewrite-not-working/) at the general level.
- **NPU pressure from concurrent AI tasks:** Running Live Captions, Studio Effects, and Rewrite simultaneously can starve the model of NPU time, degrading output quality.
- **Overly long lists exceeding context:** Very long lists exceed the model's working context; it summarizes or truncates instead of rewriting faithfully.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Format the source list cleanly

Give the model a list it can parse. Most 'rewrite broke my list' cases start here.

1. Use real bullet formatting (Word/OneNote bullets), not manual dashes with random spacing.
2. Keep each bullet to one or two sentences; move elaboration out of the list.
3. Flatten nesting to one level where possible — nested lists are the hardest case.
4. Select only the list items, not the heading above or the paragraph below.

### Fix 2: Rewrite in smaller chunks

A five-bullet rewrite succeeds where a fifty-bullet rewrite collapses. Work with the model's limits.

1. Select 3–7 bullets at a time and rewrite each chunk separately.
2. Combine the rewritten chunks afterward — the structure survives because each chunk was small.
3. For long lists, this is consistently faster than fighting one giant rewrite.
4. Notification-style interruptions can also break focus mid-task — [silent Copilot app notifications](/articles/copilot-app-notifications-silent/) covers keeping those quiet while you work.

### Fix 3: Verify the general Rewrite pipeline

Confirm prose rewriting works — this isolates list-handling from a broken Rewrite entirely.

1. Select a plain paragraph and run Rewrite. If it works, the pipeline is healthy and lists are the specific weakness.
2. If prose Rewrite also fails, stop here and fix Rewrite generally before returning to lists.
3. Test on the same app to rule out app-specific text pipeline issues.
4. A healthy prose Rewrite plus broken list Rewrite means structure handling, not the model, is at fault.

### Fix 4: Free the NPU from concurrent AI workloads

The model rewrites better with dedicated NPU time. Close the competition.

1. Turn off Live Captions translation and Studio Effects temporarily while rewriting.
2. Close other AI-heavy apps (local model tools, AI photo editors).
3. Check **Task Manager > Performance > NPU** for saturation during the rewrite.
4. Retry the list rewrite with the NPU idle — quality often improves immediately.

### Fix 5: Repair the Copilot Runtime and model components

When even clean, short lists rewrite badly, the runtime itself may be degraded.

1. Install all pending Windows updates to refresh the runtime and model.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` elevated.
3. Restart and retest on your standard 5-bullet test list.
4. Compare against prose rewriting: if both improved, the runtime was the issue.

### Fix 6: Use structured alternatives for critical lists

For lists where structure is sacred — legal, medical, compliance — do not trust any rewrite blindly.

1. Rewrite for wording, then manually verify every bullet survived with its meaning intact.
2. Alternatively, ask for a rewrite of individual bullets rather than the whole list.
3. Keep the original list saved separately until you have verified the rewrite.
4. Treat AI rewriting as a drafting assistant for lists, never as a final authority.

## Closing

Bulleted-list rewriting fails where structure meets a small model's limits: messy source formatting, oversized selections, and NPU contention. Format lists cleanly, rewrite in small chunks, free the NPU, and repair the runtime when quality collapses broadly. And for lists where every bullet matters, let the AI draft and you verify — that division of labor plays to both strengths. If rewrite quality collapses broadly, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the runtime repair options.
