---
title: "How to Fix Copilot Memory and Personalization Not Working"
slug: copilot-memory-personalization-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags: ["copilot", "copilot-memory", "personalization", "windows-11", "troubleshooting"]
description: "Copilot memory and personalization not working? Find out why Copilot forgets your preferences and fix memory settings, account sync, and app issues quickly."
thumbnail: "/images/thumbs/copilot-memory-personalization-not-working.webp"
faqs:
  - q: "What is Copilot memory supposed to remember?"
    a: >
      Copilot memory stores preferences and facts you ask it to remember, such as your name, work style, and recurring topics, so future answers can be personalized without you repeating yourself.
  - q: "Why does Copilot forget things I told it to remember?"
    a: >
      The usual reasons are memory switched off in settings, a different account signed in, a corrupted app cache, or a privacy control blocking personalization on your PC.
  - q: "Is Copilot memory available in every region?"
    a: >
      No. Memory and personalization roll out gradually by region and account type, so the feature may simply not be enabled for your account yet even if the app is current.
  - q: "Can I delete what Copilot remembers about me?"
    a: >
      Yes. Copilot settings include a memory management page where you can view, edit, and delete individual memories, or turn memory off entirely if you prefer.
---

Copilot memory is the feature that makes the assistant feel like yours: it remembers your name, your preferences, the projects you keep returning to, and the way you like answers formatted. When it stops working, every conversation starts from zero again. Copilot forgets what you told it yesterday, stops personalizing answers, and sometimes claims it cannot remember anything at all, which turns a personal assistant back into a generic chatbot.

Memory failures are usually settings or account problems rather than a broken AI. The feature depends on memory being switched on, the right account being signed in, personalization permissions being granted, and the app syncing that state with Microsoft's servers. If any of those break, Copilot either cannot save new memories or cannot retrieve the ones it already has, and both failures look identical from the outside.

This guide diagnoses memory in order: confirm the feature is on, check the account, repair the app, and fix the deeper platform pieces. Related platform issues can masquerade as memory problems, so the [ONNX Runtime NPU error guide](/articles/onnx-runtime-npu-error/) and the [USB ports fix](/articles/ai-laptop-usb-ports-not-working/) are useful companions when the problem is wider than Copilot. On AMD hardware, the [Ryzen AI XDNA 2 NPU driver guide](/articles/amd-xdna2-npu-driver-issues/) covers the driver side that on-device features depend on.

## Why this happens

- **Memory switched off:** Copilot memory is opt-in in many builds, and a settings reset or a fresh install can leave it disabled.
- **Wrong account signed in:** Memories belong to one Microsoft account, so signing in with a different account shows an empty memory.
- **Personalization permission denied:** Windows privacy controls can block the personalization data Copilot memory needs to function.
- **Corrupted app cache:** Damaged local app data can break the sync that carries memories between your PC and the cloud.
- **Outdated Copilot app:** Memory is a newer feature, so old app builds may lack the memory controls entirely.
- **Region or account rollout:** Memory rolls out gradually, so some regions and account types simply do not have it yet.
- **Organization policy:** Work or school accounts can have memory and personalization disabled by admin policy.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm memory is switched on

Start inside Copilot's own settings, because memory is frequently off rather than broken. The toggle lives in the app, not in Windows Settings, so many users look in the wrong place and conclude the feature is missing.

1. Open the Copilot app and sign in with your usual Microsoft account.
2. Open Copilot settings and look for the **Memory** or **Personalization** section.
3. Make sure the memory toggle is switched on, and enable personalization if it is a separate control.
4. If there is no memory section at all, update the app first (Fix 2) and check again.
5. Ask Copilot to remember a simple test fact, then start a new chat and ask whether it remembers it.

### Fix 2: Update Copilot and Windows

Memory features ship in newer app builds, and an outdated Copilot may show a memory section that does nothing or hide it completely. Updating the app and Windows together removes version mismatch as a cause in one pass.

1. Open the Microsoft Store, go to **Library**, and install all updates including Copilot.
2. Go to **Settings > Windows Update** and install all pending updates.
3. Restart your PC so the new app version and components load cleanly.
4. Open Copilot, re-check the memory settings from Fix 1, and confirm the toggle stays on.
5. Test memory again with a simple remembered preference, such as your preferred answer length.

### Fix 3: Verify the right account and sync

Memories are tied to a single account, so a second account signed in somewhere is the most quietly confusing cause. Copilot can look perfectly healthy while showing another account's empty memory, and nothing is actually lost.

1. In Copilot, open your profile menu and confirm the signed-in email matches the account you used before.
2. Open **Settings > Accounts** in Windows and confirm the same Microsoft account is connected.
3. If a different account is signed in, sign out of Copilot completely and sign back in with the correct one.
4. Wait a few minutes for cloud sync to complete, especially on a slow connection.
5. Start a new chat and ask Copilot what it remembers about you to confirm the right memory loaded.

### Fix 4: Repair or reset the Copilot app

When settings and accounts check out but memory still fails, local app state is the likely culprit. A damaged cache can block the sync that saves and retrieves memories, while chat itself keeps working normally because it does not depend on that cache.

1. Open **Settings > Apps > Installed apps**, find Copilot, and open **Advanced options**.
2. Click **Repair** and wait for the confirmation checkmark.
3. Retest memory with a new remembered fact and a fresh chat.
4. If memory still fails, return to **Advanced options** and click **Reset**.
5. Sign back in with the correct account after the reset and allow a few minutes for memories to sync back.

### Fix 5: Fix privacy and personalization permissions

Copilot memory needs permission to personalize, and Windows privacy settings or third-party privacy tools can silently revoke it. This is a common aftermath of running a debloat or privacy-hardening script that touched more than intended.

1. Open **Settings > Privacy & security** and review permissions that affect personalization and app data.
2. Make sure Copilot is allowed to run in the background under its **Advanced options** page.
3. Temporarily disable third-party privacy tools and retest memory to rule them out.
4. If you use a work or school account, check with your IT admin whether personalization is restricted by policy.
5. Re-enable memory in Copilot settings after any permission change, since resets can switch it off.

### Fix 6: Check NPU drivers and platform health on AI PCs

On Copilot+ PCs, some personalization features lean on on-device components, so a broken NPU driver or missing AI model can stall them even when cloud chat works. This step matters most on AI hardware and can be skipped on older PCs.

1. Open **Device Manager > Neural processors** and confirm your NPU shows without a warning icon.
2. If it is flagged or missing, install the NPU driver from your laptop maker's support site.
3. Install all **Windows Update** optional updates, which often carry AI component downloads.
4. Leave the PC plugged in on Wi-Fi for 30 to 60 minutes so on-device models finish downloading.
5. Retest memory, and check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) if the feature is still unavailable in your region.

## Closing

Copilot memory fails when it is switched off, tied to the wrong account, blocked by a privacy setting, or broken by corrupted app data. Confirm the toggle first, update the app, verify the signed-in account, repair or reset Copilot, and check permissions and platform health. Once the chain is intact, Copilot starts remembering again and personalization returns with it.
