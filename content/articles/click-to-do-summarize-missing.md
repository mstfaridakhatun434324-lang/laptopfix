---
title: "Click to Do Summarize Option Missing? How to Get It Back"
slug: click-to-do-summarize-missing
date: 2026-10-20
categories: ["ai-pc"]
tags: ["click to do", "summarize", "ai features", "troubleshooting", "ai pc", "windows 11"]
description: "Click to Do's Summarize option missing on your Copilot+ PC? Learn why the on-device AI summary action disappears and bring it back with these proven fixes."
thumbnail: "/images/thumbs/click-to-do-summarize-missing.webp"
faqs:
  - q: "What does Click to Do Summarize do?"
    a: "Summarize is a Click to Do text action that condenses selected text into a short summary using the on-device Phi Silica language model. Select a long paragraph or article, invoke Click to Do, and choose Summarize to get the key points — all processed locally on the NPU."
  - q: "Why is Summarize missing but Rewrite works?"
    a: "The two actions can depend on different model components or feature flags. Rewrite working proves the NPU and base model are fine; Summarize missing usually means its specific action definition failed to register — often fixed by a Windows update or toggling Click to Do off and on."
  - q: "Does Summarize need a minimum amount of text?"
    a: "Yes, in practice. Summarize typically appears only when you select a meaningful chunk of text — a sentence or two may not trigger it, while a paragraph will. If it never appears regardless of selection length, the problem is configuration, not selection size."
  - q: "Is Summarize available in all regions?"
    a: "Click to Do availability varies by region and language, and some actions roll out gradually. If your region only recently got Click to Do, Summarize may arrive in a later update. Check that your Windows display language is a supported one."
---

You select a long article, invoke Click to Do, and expect the Summarize option — but it is nowhere in the menu. Rewrite is there, other actions are there, just not Summarize. This selective disappearance is a configuration problem, not a hardware one: the action failed to register, the model component is incomplete, or the selection did not qualify.

Summarize shares most of its machinery with Rewrite — the Phi Silica model, the NPU, the Click to Do framework — so when Rewrite works and Summarize does not, you can skip the deep hardware checks and focus on the action layer. This guide does exactly that. If Rewrite is also broken, fix that first with our [Click to Do Rewrite guide](/articles/click-to-do-rewrite-not-working/); if the whole menu is gone, see [Click to Do missing from the right-click menu](/articles/click-to-do-right-click-menu-missing/).

Test with a full paragraph selected in Notepad after each fix.

## Why this happens

- **Action failed to register:** The Summarize action definition did not load, even though the framework runs.
- **Selection too short:** Summarize hides itself for tiny selections that are not worth summarizing.
- **Incomplete model components:** Part of the AI stack installed but the Summarize path did not.
- **Feature flag not enabled:** Microsoft rolls actions out gradually; your build may not have the flag yet.
- **Unsupported app context:** Some apps expose text in ways that suppress certain actions.
- **Stale Click to Do cache:** The action menu cached an old definition list.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Select enough text

Summarize hides for short selections. Rule out the trivial cause first.

1. Open Notepad and paste or type a full paragraph (5+ sentences).
2. Select the entire paragraph.
3. Invoke Click to Do (Windows key + click on the selection).
4. Check whether Summarize now appears — if it does, your original selection was simply too short.

### Fix 2: Toggle Click to Do off and on

This forces the action definitions to reload, which restores actions that failed to register.

1. Open Settings > Privacy & security > Click to Do and turn the feature off.
2. Restart the laptop.
3. Turn Click to Do back on.
4. Test Summarize with a long paragraph in Notepad.

### Fix 3: Install pending Windows updates

Missing actions often arrive in the next cumulative or feature update. An outdated build is the most common real cause.

1. Open Settings > Windows Update and install everything pending.
2. Check optional updates for AI component packages and install those too.
3. Restart and test Summarize again.
4. If Rewrite broke too along the way, our [Rewrite fix guide](/articles/click-to-do-rewrite-not-working/) repairs the shared model layer.

### Fix 4: Clear the Click to Do action cache

A stale cache can hold an old action list without Summarize. Clearing it forces a fresh registration.

1. Close all apps and sign out of Windows, then sign back in (this clears per-session caches).
2. Alternatively, restart the laptop for a full cache reset.
3. Invoke Click to Do on a long selection in Notepad.
4. Check the full action list — Summarize should now be present.

### Fix 5: Verify region and language support

If your region or display language is not in the rollout, Summarize may legitimately be unavailable — and no local fix will conjure it.

1. Check Settings > Time & language > Language & region for your country and display language.
2. Compare against Microsoft's published Click to Do availability (see the [Windows support hub](https://support.microsoft.com/en-us/windows)).
3. If unsupported, switching region is not recommended — wait for the rollout instead.
4. If supported, continue to Fix 6; the problem is local.

### Fix 6: Repair the AI components

When the action is still missing on a supported configuration, the model components need repair.

1. Confirm the NPU is healthy — some actions need on-device inference; our [NPU BIOS enable guide](/articles/how-to-enable-npu-in-bios/) covers firmware-level checks.
2. In Windows Update history, look for failed AI component updates and reinstall them.
3. Run `sfc /scannow` in an elevated Command Prompt to repair system files.
4. Restart, then test Summarize on a long selection in both Notepad and Edge.

## Closing

A missing Summarize is an action-registration problem, not a broken laptop. Select enough text, reload the feature, update Windows, clear the cache, verify your region, and repair the AI components — in that order. When Summarize reappears, it is worth the effort: instant on-device summaries of anything you read, with no data leaving your PC. Brand-specific AI PC issues overlap — see [HP EliteBook Ultra AI PC problems](/articles/hp-elitebook-ultra-ai-pc-problems/).
