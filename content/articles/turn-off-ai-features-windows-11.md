---
title: "How to Turn Off AI Features in Windows 11 (Complete Guide)"
slug: turn-off-ai-features-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: ["disable ai", "copilot", "recall", "windows 11", "privacy"]
description: "How to turn off AI features in Windows 11: disable Recall, Copilot, Studio Effects, and Live Captions step by step, with Group Policy options included."
thumbnail: "/images/thumbs/turn-off-ai-features-windows-11.webp"
faqs:
  - q: "Can I completely remove AI from Windows 11?"
    a: >
      You can disable every user-facing AI feature — Recall, Copilot, Studio Effects, Live Captions, AI search — but you can't strip the underlying AI platform out of Windows entirely. Disabling the features stops their activity, battery drain, and data collection, which is what most people actually want.
  - q: "Does disabling Copilot break anything else in Windows?"
    a: >
      No. Copilot is a standalone app; removing or disabling it doesn't affect Settings, search (basic file search still works), or system stability. Some context-menu entries may linger — they're harmless.
  - q: "Will Windows updates turn AI features back on?"
    a: >
      Sometimes, yes — feature updates have re-enabled Recall and reset search settings in the past. After every major update, spend two minutes re-checking Privacy & security settings. This guide's checklist makes that audit fast.
  - q: "Is there a single master switch for all AI?"
    a: >
      Unfortunately no. Microsoft spreads AI toggles across Settings, Group Policy, and individual apps. This guide collects them all in one place — work top to bottom and you'll cover everything.
---

Maybe you don't want Recall screenshotting your day. Maybe Copilot's constant presence annoys you. Maybe you just want your battery back — or your laptop runs hot with everything enabled (see [Copilot+ PC overheating](/articles/copilot-plus-pc-overheating/) if thermals are the issue). Whatever the reason, Windows 11 doesn't make it obvious how to turn its AI features off — the toggles are scattered across half a dozen settings pages, and some only exist in Group Policy. This guide gathers every switch in one place.

The good news: everything here is reversible, and nothing breaks Windows. Disabling AI features doesn't affect updates, security, or stability — you simply lose those specific conveniences. If you're on the fence, our guides on [AI features draining laptop battery](/articles/ai-features-draining-laptop-battery/) and [laptop slow when AI features are on](/articles/laptop-slow-when-ai-features-on/) help you decide which features are actually costing you. And if Task Manager shows the NPU itself working overtime, [NPU usage high at idle](/articles/npu-usage-high-idle/) is the deeper dive.

Work through the sections below in order. Each is independent — disable what you don't want, keep what you do. For managed or shared PCs, the Group Policy section at the end locks things down properly.

## Why this happens

- **AI is opt-out, not opt-in:** Microsoft enables Recall, Copilot, and AI search by default on capable hardware — you have to hunt down each toggle.
- **Toggles live in different places:** Recall is under Privacy & security, Copilot is an app, Studio Effects are in camera settings, search AI is under Searching Windows.
- **Updates reset your choices:** Feature updates have re-enabled AI features users previously disabled, so this isn't a one-time job.
- **Some switches need Pro:** The most thorough disables (Group Policy) require Windows 11 Pro — Home users get Settings-only options.
- **"Off" sometimes means "paused":** A few features stop their visible activity but leave background services installed — the Services section covers full shutdown.
- **Enterprise needs differ:** Personal preference is one thing; compliance requirements are another — hence the Group Policy lockdown path.

## How to fix it

Work through these in order — disable what you don't want, keep the rest.

### Fix 1: Disable Windows Recall

Recall is the most invasive AI feature — continuous screenshots analyzed by AI. Turning it off is the highest-impact single change.

1. Open Settings > Privacy & security > Recall & snapshots.
2. Toggle "Save snapshots" to Off.
3. Click "Delete snapshots" and confirm to wipe existing data.
4. If the toggle is managed by policy, use Group Policy (Fix 6) instead.
5. Verify in Task Manager that Recall-related processes stop within a few minutes.

### Fix 2: Remove or disable Copilot

Copilot is now a regular app, which makes it easy to remove — but its background services need separate attention.

1. Open Settings > Apps > Installed apps, find Microsoft Copilot, and Uninstall it.
2. In Task Manager > Startup, disable any remaining Copilot entries.
3. To keep the app but silence it: open Copilot's settings and disable autostart, notifications, and file context.
4. If your keyboard has a Copilot key, remap it: Settings > Personalization > Text input or your OEM's keyboard utility.
5. Restart and confirm no Copilot processes run in Task Manager.

### Fix 3: Turn off Studio Effects and Live Captions

These are per-device features that are easy to miss because they activate contextually (during calls).

1. Go to Settings > Bluetooth & devices > Cameras, select your camera, and turn off all Studio Effects (background blur, eye contact, auto framing).
2. Press Win + Ctrl + L to toggle Live Captions off, then open Settings > Accessibility > Live captions and disable "start automatically."
3. In Teams/Zoom, disable their own AI effects too — they run independently of Windows'.
4. Check Quick Settings panel for any AI effect tiles left enabled.
5. Test with a call — video should now be plain, with no background processing.

### Fix 4: Calm AI search and indexing

Windows AI search is useful but hungry. You can keep basic search while dropping the AI-enhanced layer.

1. Go to Settings > Privacy & security > Searching Windows.
2. Switch from "Enhanced" to "Classic" indexing mode.
3. Exclude folders you don't need searched (media archives, VMs, game libraries).
4. Turn off "Search highlights" and cloud search integrations you don't use.
5. If search feels broken afterward, rebuild the index once: Indexing Options > Advanced > Rebuild.

### Fix 5: Disable AI background services

Some AI components run as Windows services even with the features "off." For a thorough shutdown, manage the services directly.

1. Press Win + R, type `services.msc`, and press Enter.
2. Look for AI-related services (names vary by Windows build — search for "AI," "Recall," or "Copilot" in the list).
3. Double-click a service > set Startup type to "Disabled" (not just "Manual") for ones you're sure about.
4. Be conservative: disable only services clearly tied to features you turned off above.
5. Reboot and verify in Task Manager > Services that they show as Stopped. For a deeper service-level cleanup, see [disable Windows AI services](/articles/disable-windows-ai-services/).

### Fix 6: Lock it down with Group Policy (Pro/Enterprise)

Settings toggles can be flipped by updates; Group Policy is the durable, admin-grade off switch.

1. Press Win + R, type `gpedit.msc`, and press Enter (Windows 11 Pro required).
2. Navigate to Computer Configuration > Administrative Templates > Windows Components.
3. Find Windows AI / Copilot / Recall policies (exact names vary by build — search "copilot" and "recall" in the policy list).
4. Set "Turn off Windows Copilot" and "Disable Recall" policies to Enabled (Enabled = the feature is off).
5. Run `gpupdate /force` in an elevated Command Prompt and reboot.

## Closing

Windows 11's AI features are all optional, but Microsoft makes you work to opt out — toggles scattered across Settings, apps, services, and Group Policy. Work this guide top to bottom once, and you'll have a quiet, AI-free system that still updates and runs perfectly. The only ongoing cost is the two-minute post-update audit, because feature updates love to "helpfully" re-enable things. Keep this page bookmarked for that. If you later miss a specific feature, every step here is reversible — turn it back on the same way you turned it off.
