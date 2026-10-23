---
title: "How to Fix Copilot Not Working in Word on Windows 11"
slug: copilot-in-word-not-working
date: 2026-10-23
categories: ["ai-pc"]
tags: ["copilot", "microsoft word", "windows 11", "microsoft 365", "troubleshooting"]
description: "Copilot missing or not responding in Word on Windows 11? Full step-by-step fixes for sign-in, licenses, connected experiences, updates, and Office repair."
thumbnail: "/images/thumbs/copilot-in-word-not-working.webp"
faqs:
  - q: "Why is there no Copilot button in my Word ribbon?"
    a: >
      The most common causes are an outdated Word build, a Microsoft 365 subscription without a Copilot license, or disabled connected experiences. Update Word, verify your license includes Copilot, and check the privacy settings.
  - q: "Does Copilot in Word need a separate subscription?"
    a: >
      Yes. Copilot in Word requires a Microsoft 365 Personal, Family, or Business subscription plus a Copilot add-on license (or a plan that bundles it). A standalone Office 2021/2024 perpetual license does not include Copilot.
  - q: "Why does Copilot say it can't access my document?"
    a: >
      This usually means connected experiences are disabled in Word's privacy settings, or you are offline. Copilot needs cloud access to read and process your document, so enable connected experiences and check your internet connection.
  - q: "Copilot worked yesterday but is gone today — what happened?"
    a: >
      A license change, an expired subscription, a sign-out, or an Office update that reset privacy settings can all remove Copilot overnight. Sign back in, verify the subscription is active, and re-enable connected experiences.
---

You open Word, look for the Copilot button in the ribbon, and it is gone — or it is there but every prompt returns an error instead of a draft. Yesterday it summarized your document; today it acts like it never existed. On a laptop you bought partly for AI-assisted writing, that is more than an annoyance.

Copilot in Word is not a local feature. It is a cloud service gated by four things: a Microsoft 365 subscription with a Copilot license, a signed-in account that holds that license, an up-to-date Word build, and enabled "connected experiences" that let Word talk to Microsoft's cloud. Break any one of those and Copilot vanishes or goes silent — and Word rarely tells you which gate failed.

This guide gives you six fixes in technician order: sign-in and license checks first, then updates, then connected experiences, then credential and add-in conflicts, and finally an Office repair. Work through them in sequence and look for the Copilot button after each step.

## Why this happens

- **No Copilot license on the account:** Copilot in Word needs Microsoft 365 plus a Copilot license. A plain Microsoft 365 subscription, or a perpetual Office 2021/2024 license, shows no Copilot button at all.
- **Signed in with the wrong account:** Word may be signed in with a personal account while the Copilot license sits on a work account (or vice versa) — Copilot follows the license, not the person.
- **Outdated Word build:** Copilot requires a current Microsoft 365 build of Word. Older builds, and especially volume-licensed installs that update slowly, predate or lack the Copilot integration.
- **Connected experiences disabled:** Word's privacy setting for connected experiences gates all cloud AI. If it was turned off — by you, an update, or an admin — Copilot cannot function.
- **Expired subscription or license reassignment:** An expired Microsoft 365 subscription, or an admin removing the Copilot license, deletes the button with no warning inside Word.
- **Corrupted Office credentials or conflicting add-ins:** Stale cached credentials and third-party COM add-ins can break Copilot's cloud handshake while the rest of Word works fine.
- **Offline or blocked network:** Copilot calls Microsoft's cloud on every prompt. No internet — or a firewall/VPN blocking Microsoft 365 endpoints — makes it fail silently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Sign in with the licensed account

Copilot follows the license, and the license follows the account signed in to Word — not the Windows account. A mismatch is the most common reason the button disappears, especially on laptops shared between personal and work use.

1. In Word, click your profile picture or initials in the top-right and note which account is signed in.
2. Compare it against the account that holds your Microsoft 365 + Copilot subscription at account.microsoft.com — they must match.
3. If they differ, click the profile menu, choose **Sign out**, then sign back in with the licensed account.
4. Close Word completely and reopen it — the ribbon rebuilds its Copilot entry on launch, not mid-session.
5. If the button appears but prompts fail, the account is right and the problem is downstream. Account-license mismatches cause the same silent failures as [winget ARM packages failing to install](/articles/winget-arm-packages-not-installing/).

### Fix 2: Verify the subscription and Copilot license are active

A lapsed Microsoft 365 subscription or a removed Copilot license deletes the Word integration without any in-app warning — Word just looks like the version from before Copilot existed. Check the license before touching the software.

1. Go to account.microsoft.com, sign in, and open **Subscriptions** — confirm Microsoft 365 shows as active and paid up.
2. On a work or school account, ask your admin to confirm the Copilot license is still assigned to you in the Microsoft 365 admin center.
3. Check you are not over your device-install limit — an over-limit install drops into reduced functionality mode, which hides Copilot.
4. If anything was renewed or reassigned, sign out of Word, wait five minutes for the license to propagate, and sign back in.
5. Reopen Word and check the ribbon. If the license is confirmed active but Copilot is still missing, the issue is in Word itself — keep going.

### Fix 3: Update Word to the current Microsoft 365 build

Copilot integration lives in recent Word builds, and an update can quietly roll it back on a deferred channel. An outdated or stuck build is a frequent culprit on laptops that have not updated Office in months.

1. In Word, go to **File > Account > Update Options > Update Now** and install everything offered.
2. After updating, check **File > Account > About Word** — Copilot needs a current Microsoft 365 (Click-to-Run) build, not an old MSI install.
3. If updates say you are current but the build number looks months old, your install may be on the Semi-Annual channel — ask your admin about moving to Current Channel if Copilot is required.
4. Restart the PC after a major Office update so all Office services re-register cleanly.
5. Open Word and look for the Copilot button in the **Home** tab. Microsoft's [Windows and Office support pages](https://support.microsoft.com/en-us/windows) document which update channels carry the Copilot features.

### Fix 4: Enable connected experiences in Word's privacy settings

Copilot is a connected experience — Word literally cannot call the AI service if connected experiences are disabled. This toggle gets flipped by privacy-conscious users, by some updates, and by admin policy, and Word gives no hint that it is the blocker.

1. In Word, go to **File > Account > Manage Settings** (under Account Privacy).
2. Make sure **Enable connected experiences** is turned **on** — this is the master switch Copilot depends on.
3. Also enable **optional connected experiences** if prompted; some Copilot drafting features use them.
4. Close Word fully and reopen it so the setting takes effect.
5. Test Copilot with a simple prompt like "Summarize this document." On a managed work laptop, this setting may be locked by your admin — if the toggle is grayed out, only IT can change it, and no local fix will help.

### Fix 5: Clear cached credentials and disable conflicting add-ins

Stale Office credentials and third-party COM add-ins can break Copilot's authentication handshake while everything else in Word works perfectly — the classic "Word is fine, Copilot is dead" pattern. Both are quick to rule out.

1. Close all Office apps, open **Credential Manager** in Windows, and under **Windows Credentials** remove entries starting with **MicrosoftOffice**.
2. Reopen Word and sign in fresh when prompted — this forces a clean token for the Copilot service.
3. If Copilot still fails, go to **File > Options > Add-ins**, set **Manage** to **COM Add-ins**, click **Go**, and uncheck all third-party add-ins.
4. Restart Word and test Copilot again with add-ins disabled.
5. Re-enable add-ins one at a time — the one that breaks Copilot is your culprit. Credential staleness misleads diagnostics the same way misread power data skews a [battery report on NPU power usage](/articles/battery-report-npu-power-usage/).

### Fix 6: Repair the Office installation

When sign-in, license, updates, settings, and add-ins are all correct, the Office installation itself is usually damaged — a broken Click-to-Run component can disable just the Copilot integration while Word otherwise runs. An Online Repair reinstalls Office cleanly without losing your documents.

1. Open **Settings > Apps > Installed apps**, find **Microsoft 365**, click the three dots, and choose **Modify**.
2. Select **Online Repair** (not Quick Repair — the online variant actually reinstalls the bits) and let it run; it takes 15–30 minutes on a fast connection.
3. Restart the PC when the repair finishes.
4. Open Word, sign in with your licensed account, and confirm connected experiences are still enabled after the repair.
5. Check for the Copilot button and test a prompt. If a repair does not restore it, fully uninstall and reinstall from your Microsoft account portal — and keep the [Intel NPU driver healthy with a clean install](/articles/intel-npu-driver-clean-install-ddu/) so on-device AI paths do not compound the problem.

## Closing

Copilot in Word fails at one of four gates — license, account, build, or connected experiences — plus credentials, add-ins, or a damaged install. Verify the licensed account and active subscription first, update Word second, and flip connected experiences back on before assuming anything deeper is broken.
