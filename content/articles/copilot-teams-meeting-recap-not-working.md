---
title: "How to Fix Copilot Teams Meeting Recap Not Working"
slug: copilot-teams-meeting-recap-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["copilot", "teams", "meeting-recap", "microsoft-365", "troubleshooting"]
description: "Copilot meeting recap missing after your Teams calls? This guide covers licensing, admin policies, transcription settings, and the fixes that bring recaps back."
thumbnail: "/images/thumbs/copilot-teams-meeting-recap-not-working.webp"
faqs:
  - q: "Why is there no Copilot recap after my Teams meeting?"
    a: >
      The recap needs three things: a Microsoft 365 Copilot license assigned to you, meeting transcription or recording enabled, and your IT admin allowing Copilot in Teams. If any one is missing, no recap is generated. Also, recaps only appear for meetings where transcription actually ran — check the meeting's Recap tab.
  - q: "Does meeting recap need transcription turned on?"
    a: >
      Yes. Copilot builds the recap from the meeting transcript, so transcription (or recording, which implies transcription) must be enabled for the meeting. The organizer's meeting options control this — if transcription was off, Copilot has nothing to summarize and no recap appears.
  - q: "I have a Copilot license but recap still doesn't show — why?"
    a: >
      Check that the license is actually assigned to your account (not just purchased), that your Teams app is updated, and that your admin hasn't disabled Copilot for Teams meetings in the Teams admin center. Also confirm you're looking in the right place: the Recap tab of the meeting in Teams or Outlook.
  - q: "Can Copilot recap meetings I didn't attend?"
    a: >
      Only if the meeting was transcribed or recorded and the recap was generated — Copilot can't summarize a meeting that has no transcript. If transcription ran, you can open the meeting's Recap tab afterward and read the AI notes and action items even if you missed the call.
---

You end a Teams meeting, open it later expecting Copilot's neat summary — key points, action items, who said they'd do what — and there's nothing. No Recap tab, no AI notes, just the chat. For people who live in back-to-back meetings, the recap is the difference between staying on top and drowning.

Copilot's meeting recap isn't a single feature — it's a chain. The meeting needs transcription or recording enabled, your account needs a Microsoft 365 Copilot license actually assigned (not just purchased by the company), your IT admin needs to allow Copilot in Teams, and the Teams client needs to be current. Break any link and no recap generates, usually without explaining which link broke. The fixes below walk the chain in order.

Most "recap not working" cases turn out to be licensing or admin policy — the two things individual users can't fix alone — which is why this guide front-loads the checks that tell you whether to keep troubleshooting or go talk to IT. If your laptop has broader Teams or system oddities, the same structured approach sorts out things like [the taskbar search box not working on AI PCs](/articles/taskbar-search-box-not-working-ai-pc/) or [Docker Desktop issues on ARM Windows](/articles/docker-desktop-arm-windows-issues/). Snapdragon owners dealing with power-state quirks may also want [hibernation not working on Snapdragon laptops](/articles/hibernation-not-working-snapdragon/).

## Why this happens

- **No Copilot license assigned:** The company may own licenses that were never assigned to your specific account.
- **Transcription was off for the meeting:** Without a transcript, Copilot has nothing to summarize — no recap is generated.
- **Admin disabled Copilot for Teams:** IT can turn off Copilot in meetings via Teams admin center policy.
- **Outdated Teams client:** Older Teams builds may not render the Recap tab or call the Copilot service correctly.
- **Meeting type unsupported:** Some meeting types (certain webinars, town halls, or channel meetings with specific settings) don't generate recaps.
- **Recap still processing:** Large meetings can take a while; the recap appears after processing completes, not instantly.
- **Wrong account or tenant:** Being signed into Teams with a personal account or a different tenant that lacks the license.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm transcription actually ran for the meeting

Open the meeting in Teams or Outlook and look for the Recap tab. If there's no transcript at all, Copilot had no input — the organizer needs to enable transcription or recording in the meeting options. This single check explains a large share of missing recaps.

1. Open the meeting from your Teams calendar or Outlook.
2. Look for the **Recap** tab and check whether a transcript exists.
3. If there's no transcript, transcription was off — the organizer should enable **Transcribe** or **Record** in meeting options.
4. Join a test meeting with transcription on and verify a recap generates.

### Fix 2: Verify your Copilot license is assigned to you

A Microsoft 365 Copilot license must be assigned to your user account, not merely purchased by the organization. Ask your IT admin to check in the Microsoft 365 admin center under your user > Licenses. If it's assigned and still not working, sign out of Teams completely and sign back in — license changes sometimes need a fresh sign-in.

1. Ask your IT admin to confirm a **Microsoft 365 Copilot** license is assigned to your account.
2. In Teams, click your profile picture and **Sign out** fully, then close Teams from the system tray.
3. Sign back in with your work account.
4. Open a transcribed meeting and check for the Recap tab.

### Fix 3: Check admin policy for Copilot in Teams

Even with a license, admins can disable Copilot features per policy in the Teams admin center. This is an IT-side check: under Teams apps > setup policies or the Copilot settings, Copilot must be allowed for meetings. If you're not the admin, the specific question for IT is: "is Copilot enabled for Teams meetings in our tenant policy?"

1. Admins: open the **Teams admin center** and check Copilot / AI app policies for the user group.
2. Ensure Copilot is **allowed** for meetings, not blocked.
3. Check meeting policies for transcription or AI feature restrictions.
4. After a policy change, have the user sign out and back into Teams.

### Fix 4: Update Teams and clear its cache

An outdated Teams client can fail to show the Recap tab or fail to call the Copilot backend. Update Teams from the ... menu > Check for updates. If updating doesn't help, clear the Teams cache — corrupted local data breaks more Teams features than people expect.

1. In Teams, click **...** > **Check for updates** and install any available.
2. Fully quit Teams, then delete the cache at `%APPDATA%\Microsoft\Teams`.
3. Restart Teams and sign in again.
4. Open a transcribed meeting and verify the recap appears.

### Fix 5: Confirm you're in the right tenant and meeting type

Recaps don't generate for every meeting shape. Personal Microsoft accounts don't get Copilot recaps — you need the work/school account with the license. If you attended as a guest in another company's meeting, their tenant's policy governs the recap, not yours.

1. Confirm you're signed into Teams with your **work account**, not a personal one.
2. Check the meeting was a regular scheduled Teams meeting.
3. If you attended as a guest, the host's tenant policy controls the recap.
4. Test with an internal meeting you organize yourself, with transcription on.

### Fix 6: Wait for processing, then check the right location

Copilot recaps aren't instant — after a long meeting, processing can take tens of minutes. Also make sure you're looking in the right place: the Recap tab on the meeting event in Teams Calendar (or Outlook on the web). The AI notes, action items, and transcript search all live there, not in the meeting chat.

1. After a meeting ends, wait at least 30 minutes before concluding it's broken.
2. Open Teams **Calendar**, click the past meeting, and select the **Recap** tab.
3. Check Outlook on the web for the same meeting's recap view.
4. If the transcript exists but no AI summary, retry the sign-out/sign-in and cache steps above.

## Closing

Copilot meeting recaps fail silently because the feature is a chain — transcription, license, admin policy, client — and a broken link means no recap. Work the chain in order: usually transcription is off or the license was never assigned. If everything verifies and still no recaps, the problem is tenant-side — your IT admin must fix it in the Teams admin center. [Microsoft's support hub](https://support.microsoft.com/en-us/windows) documents the admin-side settings.
