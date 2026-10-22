---
title: "How to Fix Click to Do Privacy Settings on Windows 11"
slug: click-to-do-privacy-settings-fix
date: 2026-10-22
categories: ["ai-pc"]
tags: ["click to do privacy", "click to do settings", "windows click to do", "ai privacy windows 11", "copilot plus pc", "windows 11"]
description: "Uneasy about Click to Do privacy on Windows 11? Learn exactly what data it uses, how to lock down its privacy settings, and fix settings that won't apply."
thumbnail: "/images/thumbs/click-to-do-privacy-settings-fix.webp"
faqs:
  - q: "Does Click to Do send my selected text to Microsoft?"
    a: >
      Text actions run on-device using the local AI model and your NPU — selections are not uploaded. The exception is explicitly web-backed actions like visual search with Bing, which sends the image to perform the search.
  - q: "Can my employer see what I use Click to Do on?"
    a: >
      Click to Do itself does not report your selections to anyone. On a managed work device, IT can control whether the feature is enabled, but that is policy enforcement, not surveillance of your selections.
  - q: "Should I turn off Click to Do for privacy?"
    a: >
      For most personal use, the on-device design makes it one of the more private AI features in Windows. If you are still uncomfortable, turning it off is one toggle and fully reversible — no data cleanup needed.
  - q: "Do Click to Do privacy settings sync across my PCs?"
    a: >
      Some Windows settings sync via your Microsoft account; feature-specific AI toggles may or may not roam. Verify the settings on each PC rather than assuming they carried over.
---

Click to Do reads your screen's text and images to offer AI actions — which naturally raises the question of where that data goes. The privacy story is actually reassuring, but the settings that control it are scattered and occasionally fail to apply.

The key fact: Click to Do's text actions run on-device using the local Phi Silica model. Your selections are processed on your PC's NPU, not shipped to the cloud — with narrow exceptions like visual search, which explicitly queries the web. Understanding that boundary tells you which settings actually matter. The same on-device-versus-cloud distinction underlies [Firefox on ARM64 Windows](/articles/firefox-arm64-windows-issues/), where knowing what runs locally changes the whole troubleshooting picture.

This guide covers six areas: what Click to Do does with your data, the privacy settings to review, fixing settings that will not stick, and policy considerations on work PCs.

## Why this happens

- **Misunderstanding on-device vs cloud processing:** Most privacy anxiety comes from assuming selections upload to Microsoft. Text actions are on-device; only explicitly web-backed actions (visual search) leave the PC.
- **Privacy toggles not applying:** Settings that revert or silently fail leave users unsure what is actually enforced — the 'will not stick' class of bug.
- **Scattered settings locations:** Click to Do privacy touches Settings privacy pages, the feature's own page, and Windows diagnostics settings — no single dashboard.
- **Work policy overriding user choices:** On managed devices, IT policy can enforce settings the user cannot change, causing confusion when toggles appear locked — see [Click to Do disabled by group policy](/articles/click-to-do-disabled-group-policy/) for the managed-device picture.
- **Diagnostic data settings conflated with feature data:** Windows diagnostic data is a separate pipeline from Click to Do's on-device processing; users often conflate the two.
- **Outdated builds with older privacy controls:** Privacy controls refined across builds; older builds offer coarser options.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Understand what Click to Do does with selections

Base your settings on facts, not fears.

1. Text actions (summarize, rewrite, translate, copy as table) run on-device via the local model and NPU.
2. Visual search with Bing sends the image region to the web — it is the clearly-labeled exception.
3. No Microsoft account sign-in is required for the on-device actions.
4. If any of this changes in future builds, Microsoft documents it in the feature's privacy supplement — check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for current statements.

### Fix 2: Review the Click to Do settings page

Audit the feature's own controls first.

1. Open **Settings > Privacy & security > Click to Do** (or Text actions on your build).
2. Review every toggle: feature on/off, and any data/model-related options shown.
3. Turn off individual capabilities you do not want rather than the whole feature if you still want basic actions.
4. Note the current state with a screenshot before changing anything.

### Fix 3: Fix privacy toggles that will not stick

A toggle that reverts is not protecting you. Make it stick.

1. Change the toggle, close Settings completely, reopen, and verify.
2. If it reverted, check for 'managed by your organization' text — policy overrides user toggles silently.
3. Try toggling with settings sync paused: **Settings > Accounts > Windows backup**.
4. If it still will not stick on a personal, unmanaged PC, repair system files with `sfc /scannow` — the settings platform itself may be damaged.

### Fix 4: Separate diagnostics from feature behavior

Do not fight the wrong setting. Windows diagnostic data and Click to Do processing are different things.

1. Review **Settings > Privacy & security > Diagnostics & feedback** separately.
2. Setting diagnostics to **Required only** does not change Click to Do's on-device behavior — and does not need to.
3. Tailored experiences and advertising ID settings are likewise separate pipelines.
4. After major updates like [NPU missing after the 25H2 update](/articles/npu-missing-after-25h2-update/), re-verify these pages — updates occasionally reset privacy-adjacent defaults.

### Fix 5: Handle work and school devices correctly

Managed devices play by IT's rules. Know where you stand.

1. Check for organization-management notices across the privacy settings pages.
2. Ask IT what Click to Do policies apply — some orgs disable web-backed actions but allow on-device ones.
3. Do not attempt to bypass management controls; it can violate acceptable-use policy.
4. For personal tasks on a work PC, prefer your personal device where you control the settings.

### Fix 6: Disable Click to Do entirely if you prefer

The ultimate privacy control is off. It is a legitimate choice, and reversible.

1. Turn the master toggle off in **Settings > Privacy & security > Click to Do**.
2. Verify no sparkle icon appears on text selection afterward.
3. Your other AI features (Live Captions, Studio Effects) are controlled separately — disabling Click to Do does not affect them.
4. Re-enable anytime; your preference persists across updates on a healthy system.

## Closing

Click to Do's privacy story is strong by design — on-device models, local NPU processing, no account required — with visual search as the clearly-marked cloud exception. Audit the settings page, make sure your toggles actually stick, keep diagnostics and feature behavior conceptually separate, and respect IT policy on work devices. Informed settings beat anxious guessing every time.
