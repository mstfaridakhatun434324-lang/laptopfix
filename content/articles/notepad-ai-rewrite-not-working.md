---
title: "How to Fix Notepad AI Rewrite Not Working on Windows 11"
slug: notepad-ai-rewrite-not-working
date: 2026-10-23
categories: ["ai-pc"]
tags: ["notepad", "ai rewrite", "windows 11", "copilot+ pc", "troubleshooting"]
description: "Notepad's AI Rewrite is grayed out or failing on Windows 11? Follow step-by-step fixes for sign-in, app updates, Copilot+ eligibility, and region settings."
thumbnail: "/images/thumbs/notepad-ai-rewrite-not-working.webp"
faqs:
  - q: "Why is the Rewrite button grayed out in Notepad?"
    a: >
      The most common cause is not being signed in with a Microsoft account, or running an older Notepad version that predates the AI features. Sign in through the profile icon in Notepad and update the app from the Microsoft Store to restore the button.
  - q: "Is Notepad Rewrite free to use?"
    a: >
      On Copilot+ PCs, Rewrite uses on-device AI credits that come with the PC at no extra cost. On other Windows 11 PCs, Rewrite requires a Microsoft 365 Personal or Family subscription, or Copilot Pro, which includes a monthly allowance of AI credits.
  - q: "Why does Rewrite say 'Something went wrong' every time?"
    a: >
      This is usually a temporary cloud-service hiccup, an unsupported region or display language, or exhausted AI credits. Check your account region, make sure English (US) is your display language, verify you still have credits, and try again.
  - q: "Does Notepad Rewrite work offline?"
    a: >
      Only on Copilot+ PCs, where the on-device model can run locally once it has downloaded. On all other PCs, Rewrite sends your text to Microsoft's cloud AI service, so an active internet connection is required for it to work.
---

You highlight a sentence in Notepad, click Rewrite, and nothing happens — or the button sits grayed out no matter what you select. It worked on a friend's laptop, so you know the feature exists. The frustration is real: a simple text editor with an AI button that refuses to cooperate.

Rewrite is Microsoft's generative AI editing feature built into Notepad (version 11.2410 and newer) — it can shorten, lengthen, or rephrase text and change its tone. On Copilot+ PCs it runs on the NPU with on-device models; elsewhere it calls Microsoft's cloud AI, tied to your Microsoft account and a monthly credit allowance. That dual design is why it fails differently on different machines — sign-in, version, subscription, region, and NPU driver health all matter.

This guide gives you six fixes in technician order: sign-in and app-version checks first, then eligibility and credits, then region and language, then app repair, and finally NPU model readiness on Copilot+ hardware. Work through them in sequence and test Rewrite after each step.

## Why this happens

- **Not signed in with a Microsoft account:** Rewrite is a cloud feature tied to your Microsoft identity and AI credit balance — a local Windows account leaves the button permanently disabled.
- **Outdated Notepad version:** Rewrite arrived in Notepad 11.2410 through the Microsoft Store. Older inbox versions lack the AI menu entirely and will never gain it without an update.
- **No qualifying subscription or exhausted credits:** On non-Copilot+ PCs, Rewrite consumes monthly AI credits from Microsoft 365 Personal/Family or Copilot Pro — an expired subscription or empty credit balance silently disables the feature.
- **Unsupported region or display language:** Rewrite is English-only and limited to supported regions. A mismatched display language or account region can hide or disable the feature entirely.
- **On-device NPU model not ready:** On Copilot+ hardware the local Rewrite model downloads after setup. Until it completes, the feature stays unavailable even though everything else looks fine.
- **Corrupted app data or a policy block:** A damaged Notepad cache, or a workplace policy disabling AI features, can switch Rewrite off with no error message.
- **Temporary Microsoft service outage:** The cloud path calls Microsoft's servers. During an outage the button renders but every Rewrite attempt fails with a generic error.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Sign in with a Microsoft account inside Notepad

Rewrite checks your identity inside Notepad itself — a Windows sign-in is not enough if Notepad's own profile is signed out. This is the most common fix, especially where the sign-in prompt was skipped during setup.

1. Open Notepad and look for the profile icon in the top-right corner of the window.
2. If it shows a generic silhouette or says sign-in is needed, click it and sign in with your Microsoft account.
3. Select a sentence of text and check whether the Rewrite button (the sparkle icon) is now active.
4. If you use a work or school account, try a personal Microsoft account instead — some organizational accounts block consumer AI features.
5. Still grayed out? Move to the next fix — the account step was necessary but not sufficient. Sign-in flakiness on ARM hardware shares roots with [passkey issues on Windows 11 ARM](/articles/passkeys-not-working-windows-11-arm/).

### Fix 2: Update Notepad from the Microsoft Store

The inbox Notepad does not always carry AI features — Rewrite arrives through Store updates, and a stalled update leaves you on a version without it. This takes a minute and rules out the version variable.

1. Open the Microsoft Store and go to **Library**, then click **Get updates**.
2. Wait for Notepad to finish updating — you need version 11.2410 or newer.
3. Fully close Notepad (check the taskbar overflow to make sure no window lingers) and reopen it.
4. Select text and open the **Rewrite** menu to see if the options now appear.
5. If the Store shows no update, your Windows build may be too old — install all pending updates via **Settings > Windows Update**, then check the Store again. Stalled updates on ARM share roots with [Terminal crashes on ARM64](/articles/windows-terminal-arm64-crashing/).

### Fix 3: Verify Copilot+ eligibility or subscription credits

Rewrite's billing splits by hardware: Copilot+ PCs get on-device AI credits with the machine; everyone else needs a paid subscription with monthly credits. On the wrong side of that split — or with exhausted credits — the button dies quietly.

1. Check whether your PC is a Copilot+ PC: open **Settings > System > About** and look for the Copilot+ branding or an NPU entry under the processor details.
2. If it is NOT a Copilot+ PC, confirm you have an active Microsoft 365 Personal/Family or Copilot Pro subscription at account.microsoft.com.
3. Check your AI credit balance in your Microsoft account — Rewrite fails when monthly credits are exhausted; they reset on your billing date.
4. If your subscription lapsed, renew it and wait a few minutes for the entitlement to sync, then restart Notepad.
5. On a Copilot+ PC with the button still dead, the problem is the on-device model, not credits — skip to Fix 6 after Fix 4.

### Fix 4: Set the region and display language correctly

Rewrite is English-only and region-gated. A non-English display language or a Microsoft account in an unsupported region can hide the feature even when everything else is perfect — with no on-screen explanation.

1. Open **Settings > Time & language > Language & region** and confirm **Windows display language** is set to **English (United States)**.
2. In the same page, set **Country or region** to **United States** (or another supported region) — mismatches here are a known trigger.
3. Sign out of Windows and sign back in so the language change fully applies.
4. Reopen Notepad, sign in again if prompted, and test Rewrite on a plain-English sentence.
5. You can switch back to another display language after confirming Rewrite works — but the feature follows the language setting. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document current AI language availability.

### Fix 5: Repair or reset the Notepad app

When sign-in, version, credits, and region are all correct, the app's cache is usually corrupt — damaged local state can disable just the AI path while editing works fine. Repair preserves settings; reset is the heavier hammer.

1. Open **Settings > Apps > Installed apps**, find **Notepad**, and click the three dots, then **Advanced options**.
2. Click **Repair** and wait for the checkmark, then test Rewrite.
3. If repair changes nothing, click **Reset** on the same page — this clears Notepad's local data (your .txt files are untouched).
4. Reopen Notepad, sign in with your Microsoft account again, and test Rewrite on fresh text.
5. As a last resort on this layer, uninstall Notepad from the same Advanced options page and reinstall it from the Microsoft Store — a clean install rules out every local-state cause at once.

### Fix 6: Check the NPU driver and let the on-device model download

On Copilot+ PCs, Rewrite's local model needs a healthy NPU driver — a broken or generic one means the on-device AI runtime never initializes and Rewrite silently fails. It is the same NPU stack behind [driver error code 39](/articles/npu-driver-error-code-39-fix/), so treat it as a driver problem first.

1. Open **Device Manager > Neural processors** and confirm your NPU appears without a warning icon — a yellow triangle means the driver is broken.
2. If flagged, reinstall the NPU driver from your laptop maker's support page (Dell, HP, or Lenovo) rather than relying on the generic Windows driver.
3. Open **Settings > Windows Update** and install all optional driver updates — the Copilot+ AI models often arrive as a separate downloadable component.
4. Leave the PC idle, plugged in, and on Wi-Fi for 30–60 minutes after setup or a major update; the on-device model downloads in the background.
5. Reopen Notepad and test Rewrite — on a healthy Copilot+ PC it now works even with Wi-Fi off, confirming the local model is live.

## Closing

Notepad Rewrite fails for checkable reasons: a missing sign-in, an old app version, exhausted credits, a wrong language, a corrupt cache, or an NPU driver that never loaded the on-device model. Walk the list in order and the button comes back — the feature was never broken, just blocked at one of six gates.
