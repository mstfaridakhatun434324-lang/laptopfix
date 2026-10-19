---
title: "Click to Do Missing on Windows 11? How to Get It Back"
slug: click-to-do-missing
date: 2026-10-19
categories: ["ai-pc"]
tags: [click-to-do, windows-11, copilot-plus-pc, missing-feature, troubleshooting, npu]
description: "Click to Do missing entirely from Windows 11? Learn why the Copilot+ feature disappears and restore it on eligible laptops with our step-by-step guide."
thumbnail: "/images/thumbs/click-to-do-missing.webp"
faqs:
  - q: "Should Click to Do appear on non-Copilot+ PCs?"
    a: >
      No. It requires a 40+ TOPS NPU and Copilot+ certification. On other hardware the feature is not installed at all, which is why there is no toggle to enable.
  - q: "Which Windows 11 version includes Click to Do?"
    a: >
      Click to Do arrived with Windows 11 24H2-era builds. If you are on 23H2 or older, updating is the fix — the feature literally does not exist on earlier builds.
  - q: "Why did Click to Do disappear after an update?"
    a: >
      Updates can unregister the feature's components or re-run eligibility checks that temporarily fail. Repairing system files and restarting usually restores it.
  - q: "Is Click to Do available in all regions?"
    a: >
      Availability has varied by region during rollout. If hardware and build both qualify, check Microsoft's current availability notes for your market.
---
Not broken — gone. No toggle in Settings, no response to Win + Click, no mention of Click to Do anywhere on the system. When the feature is entirely missing rather than malfunctioning, the cause is almost always eligibility or a Windows build issue rather than a settings problem.

Click to Do only exists on Copilot+ PCs running a new enough Windows 11. If any link in that chain is missing — hardware, build, or component registration — Windows does not show a disabled feature; it shows nothing at all. That absence is itself the diagnostic clue.

This guide traces the chain and restores the feature where it should exist. If captions are also broken, see [Live Captions not working](/articles/live-captions-not-working-windows-11/) — shared AI components may be damaged. For translation-specific issues, see [Live Captions translation not working](/articles/live-captions-translation-not-working/). To verify your hardware first, read [how to check if your laptop is a Copilot+ PC](/articles/how-to-check-if-laptop-is-copilot-plus-pc/).

## Why this happens

- **Hardware does not qualify:** Without a 40+ TOPS NPU and Copilot+ certification, Click to Do is not installed — there is nothing to restore.
- **Windows 11 build too old:** Click to Do arrived with specific 24H2-era builds. Older builds have no trace of it.
- **Feature update removed or hid it:** Major updates have, on occasion, left the feature unregistered until re-enabled.
- **Wrong Windows edition or region:** Availability varies; some editions and regions did not get Click to Do in early rollouts.
- **Corrupt component registration:** The feature's system components can unregister during a failed update, hiding it from Settings.
- **New user profile:** Click to Do settings are per-user; a fresh profile may not have it enabled even when the system does.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your PC is a Copilot+ PC
A missing feature is Windows telling you the eligibility chain is broken, and hardware is the first link. Without a 40+ TOPS NPU and Copilot+ certification, Click to Do is not installed at all — there is no hidden toggle to unearth. Confirming this takes two minutes in Task Manager and our eligibility guide, and it converts an anxious mystery into a plain answer.
1. Follow our [Copilot+ PC check guide](/articles/how-to-check-if-laptop-is-copilot-plus-pc/) step by step.
2. You need 40+ TOPS NPU, 16GB RAM, 256GB storage.
3. Check Task Manager > Performance for the NPU entry.
4. Ineligible hardware will never show Click to Do — consider this the answer, not a bug.

### Fix 2: Update Windows to a Click to Do build
Click to Do did not exist before the 24H2 era, so no update, toggle, or hack can conjure it on older builds. The fix is gloriously mundane: update Windows until the build that contains the feature is installed. Microsoft's standalone installer covers machines where Windows Update is reluctant, and a restart afterward is non-negotiable.
1. Go to Settings > Windows Update and install everything offered.
2. Confirm you are on 24H2 or later via Settings > System > About.
3. If Update does not offer 24H2+, use the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
4. After updating and restarting, search Settings for 'Click to Do' again.

### Fix 3: Re-register the feature components
Even on qualifying builds, the feature's system components can unregister during a failed update — present in theory, invisible in practice. System File Checker plus DISM repairs exactly this class of damage: the component store and the registered components it deploys. It is the right tool when the build qualifies and the hardware qualifies but Settings shows nothing.
1. Run sfc /scannow in an elevated terminal to repair system components.
2. Then run DISM /Online /Cleanup-Image /RestoreHealth for the component store.
3. Restart and check Settings for the Click to Do page.
4. These commands fix the registration damage failed updates leave behind.

### Fix 4: Check region, edition, and policies
After hardware and build, the remaining gates are administrative: region availability, Windows edition, and group policy on managed devices. These explain the frustrating cases where two identical laptops differ — one on a managed update ring, one not. Home users can largely skip this; enterprise users should ask IT before burning hours on technical fixes.
1. Verify your region settings did not change; availability has varied by market.
2. On work devices, ask IT whether Click to Do is disabled by policy.
3. Ensure you are on a full Windows 11 edition with AI features enabled.
4. Home users: this is rarely the cause — focus on build and hardware first.

### Fix 5: Try a fresh user profile test
Click to Do settings live per-user, so a fresh profile is the perfect control experiment. If the feature appears for a new local account, your main profile's configuration is corrupt — migrate or reset it. If it is missing there too, the problem is system-level and you have eliminated an entire branch of possibilities with one test.
1. Create a new local user account and sign in.
2. Search Settings for Click to Do in the new profile.
3. If it appears there, your main profile's settings are corrupt — migrate or reset them.
4. If it is missing there too, the issue is system-level: build, hardware, or components.

### Fix 6: Verify the feature pack via optional features
Click to Do arrives as part of Windows' AI feature set, and the underlying optional components can be absent even when the build is new enough. Checking Optional Features for the AI entries takes a minute and occasionally reveals the gap. Installing what is missing plus a restart is a small fix for a confusing symptom.
1. Go to Settings > System > Optional features.
2. Look for AI-related feature entries and confirm they are installed.
3. Use 'Add an optional feature' if anything relevant is missing.
4. Restart after adding components, then search Settings for Click to Do again.

### Fix 7: Check enrollment in the right update channel
Update channels quietly determine which features exist on a machine: Insider rings, managed update rings, and deferred channels can all lag or skip AI features. When hardware and build both check out, the channel is the next suspect — and on work devices, the answer may simply be that IT's ring does not include it yet.
1. Go to Settings > Windows Update > Windows Insider Program and note enrollment.
2. Release Preview and Beta channels may differ in Click to Do availability.
3. On work devices, confirm with IT that the update ring includes AI features.
4. Mismatch between channel and expectation explains several 'missing feature' cases.

## Closing

A missing Click to Do is Windows telling you the eligibility chain is broken somewhere: hardware, build, registration, or policy. Walk the chain in that order and you will find the break. On genuinely qualifying hardware with a current build, the repair commands plus a restart bring it back in the large majority of cases.
