---
title: "How to Fix Copilot in Teams Not Working on Your Laptop"
slug: copilot-in-teams-not-working-laptop
date: 2026-10-24
categories: ["ai-pc"]
tags: ["copilot", "teams", "microsoft-365", "ai-assistant", "troubleshooting"]
description: "Copilot missing or not responding inside Microsoft Teams on your laptop? This guide walks through licensing, admin policy, updates, and account fixes."
thumbnail: "/images/thumbs/copilot-in-teams-not-working-laptop.webp"
faqs:
  - q: "Why is Copilot not showing up in my Teams app?"
    a: >
      The Copilot icon appears in Teams only when your account has a Microsoft 365 Copilot license assigned and your admin allows the Copilot app. If either is missing, there's simply no icon — no error. Update Teams, confirm the license assignment with IT, and check you're signed in with the work account that holds the license.
  - q: "Copilot in Teams says it can't access my meetings — why?"
    a: >
      Copilot in Teams meetings needs transcription enabled for that meeting, plus the admin policy allowing Copilot during meetings. Without a transcript it can't summarize or answer questions about the call. Ask the organizer to enable transcription in the meeting options.
  - q: "Does Copilot in Teams work with a personal Microsoft account?"
    a: >
      No. Copilot in Teams requires a work or school account with a Microsoft 365 Copilot license. Personal accounts don't get the Copilot app in Teams at all. Make sure you're signed into Teams with the correct organizational account.
  - q: "Copilot in Teams was working and suddenly stopped — what happened?"
    a: >
      Sudden failures are usually a license change (expired or reassigned), an admin policy change, or a Teams update glitch. Sign out and back in, check for Teams updates, and ask IT whether anything changed on the license or policy side. Clearing the Teams cache also resolves update-related breakage.
---

You open Teams on your laptop, look for the Copilot icon to draft a message or catch up on a chat — and it's not there. Or it's there but every prompt returns an error or spins forever. Copilot in Teams is supposed to be the always-on assistant inside your workday; when it goes missing, the meetings and chats don't get any shorter.

Copilot inside Teams covers several surfaces: the standalone Copilot app in the sidebar, Copilot in meetings (summaries, questions about the call), and Copilot in chat (catch-up, drafting). They share the same prerequisites — a Microsoft 365 Copilot license on your account, admin permission, a current Teams client — but fail in slightly different ways, which is why the guide below separates "not showing up at all" from "shows up but doesn't work."

The honest framing: most Copilot-in-Teams failures are identity and licensing issues, not laptop issues. Your laptop is usually fine — the account, the license assignment, or the tenant policy is the broken part. The fixes below verify each layer. If your machine has wider app-compatibility quirks, the same systematic method untangles things like [Chrome ARM64 issues on Windows 11](/articles/chrome-arm64-windows-11-issues/) or [Windows Sandbox not working on ARM laptops](/articles/windows-sandbox-arm-laptop-not-working/). HP AI-PC owners fighting driver-layer problems should see [HP OmniBook Ultra NPU driver issues](/articles/hp-omnibook-ultra-npu-driver-issues/).

## Why this happens

- **No Copilot license on your account:** Without an assigned Microsoft 365 Copilot license, the app simply doesn't appear.
- **Admin blocked the Copilot app:** Tenant policy can hide or disable Copilot in Teams for your group.
- **Signed in with the wrong account:** A personal account or a secondary work account without the license shows no Copilot.
- **Outdated Teams client:** Old builds predate Copilot integration or contain bugs that break it.
- **Corrupted Teams cache or identity state:** Stale tokens and cache corruption silently break Copilot's backend calls.
- **Meeting transcription disabled:** Copilot's meeting features need a transcript; without one they error or stay empty.
- **Network or conditional-access blocks:** VPNs, firewalls, or conditional access policies can block the Copilot service endpoints.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the license and the right account

Open Teams and check which account you're signed in with — it must be the work/school account holding the Microsoft 365 Copilot license. Then have your IT admin verify the license is assigned to that exact account in the Microsoft 365 admin center. "We bought licenses" and "you have a license" are different things, and this mismatch is the top cause.

1. In Teams, click your profile picture and verify the signed-in work account.
2. Ask IT to confirm **Microsoft 365 Copilot** is assigned to that account.
3. Sign out of Teams fully, close it from the system tray, and sign back in.
4. Check the Teams sidebar for the Copilot app icon.

### Fix 2: Check admin policy for the Copilot app

Admins control Copilot's availability in the Teams admin center — app setup policies decide who sees the Copilot app, and meeting policies control Copilot during calls. If the icon is missing for your whole team, it's almost certainly policy. The specific question for IT: "Is the Copilot app allowed in our Teams app setup policy, and is Copilot enabled for meetings?"

1. Admins: open the **Teams admin center** > Teams apps > Setup policies.
2. Confirm the **Copilot** app is allowed and pinned for the user's policy.
3. Check meeting policies for Copilot / AI feature restrictions.
4. After changes, the user must sign out and back into Teams (allow up to 24 hours for propagation).

### Fix 3: Update Teams to the current version

Copilot integration is actively developed — older Teams clients may lack the app entirely or hit long-fixed bugs. Update from the ... menu, or via the Microsoft Store for the Store version. After updating, quit Teams completely from the system tray rather than just closing the window.

1. In Teams, click **...** > **Check for updates** and install any available.
2. Right-click the Teams tray icon and choose **Quit**.
3. Reopen Teams and sign in.
4. Look for the Copilot icon in the left sidebar.

### Fix 4: Clear the Teams cache and refresh identity

Corrupted cache and stale authentication tokens are the classic "it worked last week" cause. Clearing the Teams cache forces a clean re-authentication and re-download of app definitions, which restores the Copilot app entry in most update-related breakages.

1. Fully quit Teams (system tray > Quit).
2. Delete the contents of `%APPDATA%\Microsoft\Teams` (and `%LOCALAPPDATA%\Microsoft\Teams` if present).
3. Restart Teams and sign in with your work account.
4. Verify the Copilot app appears and responds to a test prompt.

### Fix 5: Test Copilot's individual surfaces separately

Don't treat "Copilot in Teams" as one thing — test each surface. Ask the standalone Copilot app a simple question; check whether Copilot appears in a meeting with transcription on; try the chat catch-up feature. If the app works but meeting Copilot doesn't, the problem is transcription or meeting policy, not your license. This isolation saves you from reinstalling things that were never broken.

1. Open the **Copilot** app in the Teams sidebar and ask a simple question.
2. Join a test meeting with **transcription enabled** and check for Copilot options.
3. Try Copilot in a Teams chat (drafting or catch-up).
4. Note exactly which surfaces fail — report this precisely to IT.

### Fix 6: Rule out network and conditional access interference

Copilot calls cloud endpoints that VPNs, strict firewalls, and conditional-access policies can block — sometimes producing vague errors rather than clear "blocked" messages. Test with the VPN disconnected and on a different network if possible. If Copilot works off-VPN but not on it, your network team needs to allowlist the Microsoft 365 endpoints.

1. Disconnect any VPN and test Copilot in Teams again.
2. Try a different network (mobile hotspot) to isolate the office network.
3. Ask IT whether conditional access policies restrict Copilot or AI apps.
4. If it works off-network, escalate to the network team with that evidence.

## Closing

Copilot in Teams is an account-and-policy feature wearing a laptop-app costume — the laptop is rarely the problem. Walk the identity chain: right account, assigned license, admin policy allowing it, current client, clean cache. That sequence resolves the overwhelming majority of cases, and when it doesn't, you'll have the precise diagnostic ("license assigned, policy allows, app works but meetings don't") that lets IT fix it in minutes. [Microsoft's support hub](https://support.microsoft.com/en-us/windows) documents the Teams repair procedures if a reinstall becomes necessary.
