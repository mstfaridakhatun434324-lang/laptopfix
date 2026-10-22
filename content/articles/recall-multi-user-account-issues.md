---
title: "Recall on Shared Laptops: Fix Multi-User Snapshot and Account Issues"
slug: recall-multi-user-account-issues
date: 2026-10-22
categories: ["ai-pc"]
tags: ["recall", "user-accounts", "windows-11", "ai-pc", "privacy", "troubleshooting"]
description: "Sharing a Copilot+ laptop between users? Learn how Recall keeps each person's snapshots separate and fix multi-user sign-in and storage problems quickly."
thumbnail: "/images/thumbs/recall-multi-user-account-issues.webp"
faqs:
  - q: "Can other users on the same laptop see my Recall snapshots?"
    a: >
      No. Recall stores snapshots per user profile, encrypted with that user's own
      Windows Hello identity. Another person signing in with their account cannot
      open, search, or even see that your snapshots exist.
  - q: "Does each user need their own Windows Hello PIN for Recall?"
    a: >
      Yes. Because snapshots are encrypted per identity, every user who wants
      Recall must enroll their own Hello PIN, face, or fingerprint under their own
      profile. One user's Hello setup does not cover anyone else.
  - q: "Why is Recall on for one user but missing for another?"
    a: >
      Recall is a per-user setting, and each profile also needs a Microsoft
      account sign-in plus Hello enrollment. A local account or a profile without
      Hello will not show Recall as available until those are set up.
  - q: "Can an administrator disable Recall for all users at once?"
    a: >
      Yes. Admins can turn Recall off device-wide through Settings or policy, which
      overrides individual user toggles. On managed or family devices, check with
      whoever administers the laptop before troubleshooting a missing Recall.
---

Copilot+ laptops are expensive, so they get shared: a family machine with a profile for each person, or a household laptop where everyone has their own sign-in. Recall was designed for exactly this situation, with snapshots encrypted per user and invisible across profiles. In practice, though, multi-user setups produce a special class of problems: Recall works for one person and not another, snapshots seem to vanish after switching users, storage fills twice as fast, or an administrator's setting silently overrides everyone.

The root of most of these issues is that Recall's identity model is per profile, not per device. Each user's snapshots are encrypted with their own Hello identity, each user has their own toggle, and each user's capture history is independent. That isolation is good for privacy, but it means every troubleshooting step has to be performed inside the affected user's session. Fixes applied as the wrong user simply do nothing. If Recall was disabled deliberately rather than broken, our guide to [Recall disabled by organization policy](/articles/recall-disabled-by-organization/) explains the managed-device side.

Before changing anything, sort out who administers the laptop. On family devices, parental controls or a well-meaning admin can disable Recall device-wide, which no per-user fix will override. Our walkthrough of [Recall on managed devices](/articles/recall-enterprise-managed-device/) covers how to recognize that situation. Below, we fix the genuine multi-user problems: per-profile setup, sign-in mix-ups, storage pressure, and admin overrides.

## Why this happens

- **Recall is per user, not per device:** enabling Recall under one profile does nothing for the others. Each person must turn it on, enroll Hello, and build their own snapshot history independently.
- **Snapshots are encrypted per identity:** a snapshot captured by one user cannot be decrypted by another, even an administrator. Switching users and expecting continuity will always disappoint.
- **Local accounts lack Recall requirements:** Recall needs a Microsoft account-backed profile with Hello enrolled. Family members signed in with local accounts will find Recall missing or non-functional.
- **Storage multiplies with users:** each active user accumulates their own snapshot store. On a 256 GB drive shared by three people, Recall data can quietly consume a surprising share of disk space.
- **Administrator settings override users:** a device-wide Recall disable, whether through Settings or policy, beats every per-user toggle. Standard users cannot re-enable what an admin turned off.
- **Fast user switching confuses capture:** Recall captures the active session. Rapid switching between users can produce gaps or misattributed snapshots when the service does not track the switch cleanly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set up Recall separately inside each user's profile

The most common "multi-user issue" is not a bug at all: only one person ever enabled Recall. Each profile needs its own complete setup before its timeline exists.

1. Sign in as the user who is missing Recall; do not attempt this from another account.
2. Go to Settings, Accounts, Your info, and confirm the profile uses a Microsoft account, converting from a local account if needed.
3. Go to Accounts, Sign-in options, and enroll a Windows Hello PIN for this specific user.
4. Open Settings, Privacy and security, Recall and snapshots, and turn Recall on.
5. Use the laptop under that profile for a while, then open Recall to confirm snapshots are capturing.

### Fix 2: Stop sharing a single Windows profile

If the whole household uses one Windows account, Recall cannot separate anyone's history, and the encryption model collapses into a single shared store. Separate profiles are the intended design.

1. As an administrator, go to Settings, Accounts, Other users, and add a Microsoft account for each person.
2. Have each person sign in once and complete the first-run setup, including their own Hello PIN.
3. Enable Recall individually inside each new profile using Fix 1.
4. Migrate personal files to the correct profiles so daily work happens under the right identity.
5. Reserve the old shared profile for guests only, or remove it once migration is complete.

### Fix 3: Reclaim disk space from multiple snapshot stores

When several users run Recall on a small SSD, storage pressure causes failures that look like Recall bugs: capture stops, search degrades, or updates fail for lack of space. Managing each store fixes it.

1. Check free space in Settings, System, Storage; if the drive is nearly full, Recall stores are a likely contributor.
2. Sign in as each user in turn and open Settings, Privacy and security, Recall and snapshots.
3. Use Delete snapshots for users who do not need a long history, or reduce how far back each timeline is kept where the option exists.
4. Consider turning Recall off entirely for light-use profiles that gain little from it.
5. Re-check free space after cleaning all profiles; Recall needs comfortable headroom to capture reliably.

### Fix 4: Resolve administrator and policy overrides

When no user can enable Recall, or the toggle is greyed out for everyone, the block is device-wide. Standard-user troubleshooting cannot fix this; the admin layer has to be addressed first.

1. Sign in as an administrator and open Settings, Privacy and security, Recall and snapshots.
2. If Recall is disabled here, enabling it lifts the block for all users at once.
3. On family devices, check the Microsoft Family Safety settings for any app or feature restrictions affecting Recall.
4. If the toggle is greyed out even as admin, a policy is in play; our guide to [group policy disabling Recall](/articles/recall-group-policy-keeps-disabling/) covers that repair.
5. Once the device-wide block is lifted, each user still enables Recall individually per Fix 1.

### Fix 5: Fix sign-in mix-ups after fast user switching

Rapid switching can leave Recall capturing under the wrong session or paused entirely. A clean sign-out cycle restores correct per-user capture without touching any data.

1. Save work and sign out completely instead of using Switch user for the next changeover.
2. Sign in as the intended user and wait a minute for background services to settle.
3. Open Recall and confirm the timeline shows that user's own snapshots, not someone else's.
4. If capture seems paused, toggle Recall off and on inside that user's settings.
5. Make full sign-outs the household habit when handing the laptop over; it avoids the whole class of switching glitches.

### Fix 6: Audit privacy so each user's history stays theirs

On a shared laptop, trust matters as much as function. Verifying the isolation actually holds gives everyone confidence, and it catches the one dangerous misconfiguration: two people unknowingly using the same profile.

1. As each user, open Recall and confirm the timeline contains only that person's activity.
2. Verify every active profile has its own Hello PIN enrolled, so no one can open another's session without their credential.
3. Turn off automatic sign-in if it is enabled, since it defeats per-user isolation entirely.
4. Review each profile's Recall exclusion list for sensitive apps that should never be captured.
5. If any timeline shows another person's content, stop and split the profiles using Fix 2 before continuing.

## Closing

Multi-user Recall problems almost always trace back to the per-profile design: each person needs their own Microsoft account, their own Hello enrollment, and their own toggle, and no fix applied as the wrong user will ever work. Set up the profiles properly, keep an eye on multiplied storage, and respect the admin layer when a device-wide block is in force. Done right, a shared Copilot+ laptop gives everyone a private, searchable timeline with no cross-contamination. While tuning shared machines, two unrelated fixes often come in handy: adjusting [Studio Effects blur strength](/articles/studio-effects-blur-strength-adjustment/) per user for video calls, and choosing [native ARM versus x64 VS Code](/articles/vscode-arm-native-vs-x64/) on Snapdragon laptops.
