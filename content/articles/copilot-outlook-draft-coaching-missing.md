---
title: "How to Fix Missing Copilot Draft Coaching in Outlook on Windows 11"
slug: copilot-outlook-draft-coaching-missing
date: 2026-10-23
categories: ["ai-pc"]
tags: ["copilot", "outlook", "draft coaching", "microsoft 365", "email", "troubleshooting"]
description: "Restore missing Copilot draft coaching in Outlook on Windows 11 with step-by-step fixes for licensing, app version, account setup, and admin policy blocks."
thumbnail: "/images/thumbs/copilot-outlook-draft-coaching-missing.webp"
faqs:
  - q: "Why is Copilot draft coaching missing from my Outlook?"
    a: "The most common reasons are a missing or unassigned Microsoft 365 Copilot license, using the classic Outlook desktop app instead of the new Outlook for Windows, or an admin policy that disabled Copilot features. Verify your license and app version first."
  - q: "Does draft coaching work in classic Outlook?"
    a: "No. Copilot's draft coaching and rewriting features require the new Outlook for Windows or Outlook on the web. If you are still on the classic Win32 Outlook, switch to the new Outlook to access these AI writing features."
  - q: "Can my IT admin block Copilot in Outlook?"
    a: "Yes. Microsoft 365 administrators can disable Copilot experiences through admin center policies. If your license is active and the button still does not appear, ask your IT admin whether Copilot has been turned off for your organization."
  - q: "Is draft coaching an NPU feature on Copilot+ PCs?"
    a: "No. Draft coaching is a cloud-powered Microsoft 365 feature, not an on-device NPU workload, so it behaves the same on Copilot+ PCs and regular PCs. Licensing and the Outlook app version are what matter, not your chip."
---

You open a new email in Outlook, write a rough draft, and look for the Copilot button that is supposed to offer coaching on tone, clarity, and length — but it is not there. No ribbon icon, no "Coaching by Copilot" prompt, nothing. The feature was announced for your plan, your colleague sees it, yet your Outlook acts like it does not exist.

Copilot in Outlook is not an on-device NPU feature — it is a cloud service gated by your Microsoft 365 license, the exact Outlook app you are running, and your organization's admin policies. Any one of those three can silently remove the button.

This guide walks you through six checks in technician order: license and account first, then the Outlook app version, then settings and policy blocks. Work through them in sequence and look for the Copilot icon after each step.

## Why this happens

- **No Microsoft 365 Copilot license assigned:** Draft coaching requires a Copilot for Microsoft 365 license (or Copilot Pro for personal accounts). Without it, Outlook simply hides the feature — there is no error message.
- **Using classic Outlook instead of the new Outlook:** The classic Win32 Outlook desktop app does not support Copilot draft coaching. The feature only exists in the new Outlook for Windows and Outlook on the web.
- **Signed in with the wrong account:** If Outlook is signed in with a personal Microsoft account while your Copilot license sits on your work account (or vice versa), the feature will not appear.
- **Admin policy disabling Copilot:** Microsoft 365 admins can turn off Copilot experiences for the whole organization or specific users. The button vanishes with no local indication of why.
- **Outdated Outlook build:** Copilot features roll out in specific Outlook builds. An outdated new-Outlook client can predate the draft coaching rollout for your update channel.
- **Offline or restricted network:** Draft coaching calls Microsoft's cloud on every use. A VPN, proxy, or firewall rule that blocks the Copilot endpoints removes the feature as if it were never licensed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your Copilot license is active and assigned

Everything else is pointless without the license, so verify it first. Draft coaching is a licensed Microsoft 365 feature, and the most common cause of a missing button is simply that the license was never assigned to your account.

1. Go to account.microsoft.com and sign in with the same account you use in Outlook, then check **Subscriptions** for an active **Microsoft 365 Copilot** or **Copilot Pro** license.
2. For work accounts, ask your IT admin to confirm the Copilot license is **assigned** to you in the admin center — assigned, not merely purchased.
3. In Outlook, go to **File > Office Account** (classic) or **Settings > General > About** (new Outlook) and confirm the signed-in account matches the licensed one.
4. If the accounts differ, sign out and back in with the licensed account, then restart Outlook.
5. Wait a few minutes after any license change — Microsoft 365 license provisioning can take up to 24 hours to reach the Outlook client.

### Fix 2: Switch to the new Outlook for Windows

If you are running the classic Outlook desktop app, no amount of license checking will help — Copilot draft coaching does not exist there. This is the second most common cause, and the fix is a one-click switch.

1. Open classic Outlook and look for the **Try the new Outlook** toggle in the top-right corner of the window.
2. Flip the toggle on and let Outlook migrate your accounts and settings — this usually takes a few minutes.
3. Once the new Outlook opens, compose a new email and look for the **Copilot** icon in the message ribbon or toolbar.
4. If you do not see the toggle, your organization may have blocked the migration — check with IT, or use Outlook on the web at outlook.com as an alternative, since Copilot works there too.
5. On a Copilot+ PC the new Outlook also benefits from on-device features like [Click to Do in Teams chat](/articles/click-to-do-teams-chat/), which is a separate NPU-powered experience worth exploring once your cloud Copilot is working.

### Fix 3: Update Outlook to the latest build

Copilot draft coaching arrived in specific Outlook builds and keeps gaining refinements. If your new Outlook is months behind, you may be running a build that predates the feature or has a broken implementation.

1. In the new Outlook, go to **Settings > General > About Outlook** and note your version and build number.
2. Open the **Microsoft Store**, go to **Library**, and install any pending Outlook updates.
3. Alternatively, in classic Outlook go to **File > Office Account > Update Options > Update Now** to pull the latest Microsoft 365 Apps build.
4. After updating, restart Outlook and compose a test email — the Copilot button often appears immediately.
5. If you are on the Semi-Annual Enterprise channel, ask IT about Current Channel, where Copilot features land months earlier — the same version-lag problem affects [Roblox on ARM Windows laptops](/articles/roblox-arm-windows-laptop-issues/).

### Fix 4: Check admin policies and connected experiences

In a work or school tenant, your admin can disable Copilot with a policy — and there is also a privacy setting on your own machine that can suppress it. Check both before assuming the feature is broken.

1. In the new Outlook, open **Settings > General > Privacy and data** and make sure connected experiences are enabled — disabling them can remove Copilot.
2. Ask your Microsoft 365 admin to check the **Microsoft 365 admin center > Settings > Org settings > Copilot** page for any policy disabling Copilot in Outlook.
3. Have the admin verify the **Microsoft 365 Copilot** service plan is enabled for your license in **Users > Licenses** — individual service plans can be toggled off even when the license is assigned.
4. If a policy was blocking you, sign out of Outlook and back in after the admin change so the new policy downloads.
5. Personal-account users: check account.microsoft.com privacy settings for anything disabling AI or connected experiences on your Microsoft account.

### Fix 5: Repair the network path to Copilot's cloud endpoints

Draft coaching is useless without a working connection to Microsoft's Copilot services. VPNs, corporate proxies, and aggressive firewalls commonly break it — and the symptom is a silently missing button rather than an error.

1. Disconnect your VPN temporarily and restart Outlook, then check whether the Copilot button appears.
2. If you are on a corporate network, ask IT whether traffic to Microsoft 365 Copilot endpoints is allowed — some proxies strip the required authentication headers.
3. Check **Settings > Network & internet** in Windows 11 and confirm you have a working connection with no captive-portal warning.
4. Temporarily disable third-party firewall or DNS-filtering software and retest; re-enable it afterward and add an exception if that was the cause.
5. Keep your laptop on AC power while troubleshooting so battery-saver throttling does not muddy the results — if charging itself is flaky, see [USB-C PD charging fixes for AI laptops](/articles/usb-c-pd-charging-not-working-ai-laptop/).

### Fix 6: Reset Outlook's local state and reinstall if needed

When the license, app, policy, and network are all correct but the button still will not show, corrupted local Outlook state is the last suspect. A reset clears cached feature flags without touching your mailbox data.

1. Close Outlook completely, then open **Settings > Apps > Installed apps**, find **Outlook (new)**, and choose **Advanced options > Reset**.
2. Reopen Outlook, sign in again, and compose a test message to check for the Copilot icon.
3. If the reset did not help, uninstall the new Outlook from Installed apps, restart the PC, and reinstall it fresh from the Microsoft Store.
4. After reinstalling, give the app a few minutes on first launch to download its configuration before judging the result.
5. As a final cross-check, open Outlook on the web — if Copilot appears there but not in the desktop app, the problem is local to your Windows installation, and [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) cover deeper repairs like an in-place upgrade.

## Closing

A missing draft-coaching button is almost never a broken PC — it is a missing license, the wrong Outlook app, or a policy in the way. Confirm the license on your signed-in account, switch to the new Outlook, and check admin policies before reinstalling anything.
