---
title: "Microsoft 365 Copilot vs Windows Copilot: What's the Difference?"
slug: microsoft-365-copilot-vs-windows-copilot
date: 2026-10-23
categories: ["ai-pc"]
tags: ["copilot", "microsoft 365", "windows copilot", "comparison", "ai features", "windows 11"]
description: "Confused by Microsoft 365 Copilot vs Windows Copilot? Learn what each one does, which license you need, and how to get the right Copilot working on your AI PC."
thumbnail: "/images/thumbs/microsoft-365-copilot-vs-windows-copilot.webp"
faqs:
  - q: "Is Microsoft 365 Copilot the same as Windows Copilot?"
    a: "No. Microsoft 365 Copilot is a paid, cloud-powered assistant built into Word, Excel, Outlook, and Teams that works with your documents and data. Windows Copilot (the Copilot app/key on your PC) is the free system-level assistant for settings, files, and general questions."
  - q: "Do I need to pay for Copilot on my Copilot+ PC?"
    a: "No for the basics. The Copilot app, the Copilot key, Recall, Click to Do, and Studio Effects work without a subscription. You only pay if you want Microsoft 365 Copilot's deep integration inside Office apps — that requires a Copilot license on top of Microsoft 365."
  - q: "Why does Copilot act differently in Word versus the Copilot app?"
    a: "Because they are different products. The Copilot app answers general questions and tweaks Windows settings, while Microsoft 365 Copilot inside Word can read, draft, and rewrite your actual documents using your organization's data — a capability the free app does not have."
  - q: "Can I use Microsoft 365 Copilot without a Copilot+ PC?"
    a: "Yes. Microsoft 365 Copilot runs in Microsoft's cloud, not on your NPU, so any PC that runs the Office apps can use it with the right license. A Copilot+ PC only adds the on-device AI experiences like Recall and Live Captions."
---

Your new AI laptop has a dedicated Copilot key and a Copilot app — and then Word asks you to pay for "Microsoft 365 Copilot." Are these the same thing? Why won't the free Copilot summarize your document? The naming is genuinely confusing, and Microsoft has renamed these products more than once.

The short version: **Windows Copilot** (the app and key on your PC) is the free system-level assistant, while **Microsoft 365 Copilot** is the paid assistant inside Office apps with access to your files, emails, and meetings. Mixing them up leads to real problems — people buy licenses they do not need, or expect document superpowers from the free app.

This guide untangles the two: what each one does, what each costs, which one you need, and how to get the right one working. Work through the fixes in order if one of them misbehaves.

## Why this happens

- **Overlapping names, different products:** Microsoft used "Copilot" for the Windows assistant, the Office assistant, the web chatbot, and the hardware key — four different things sharing one brand, which is why searches for the difference are so common.
- **Different homes:** Windows Copilot lives in the Copilot app, taskbar, and key; Microsoft 365 Copilot lives inside Word, Excel, PowerPoint, Outlook, Teams, and OneNote.
- **Different data access:** The free Windows Copilot cannot read your Word documents or emails; Microsoft 365 Copilot is grounded in your Microsoft 365 data — files, chats, and meetings — which is what the license pays for.
- **Different price tags:** Windows Copilot is free with Windows 11; Microsoft 365 Copilot needs a paid add-on license (or Copilot Pro for personal use).
- **Different hardware stories:** Copilot+ PC exclusives like Recall, Click to Do, and Live Captions run on the NPU and belong to the Windows side — they have nothing to do with the Microsoft 365 subscription.
- **Renaming whiplash:** "Windows Copilot" became the "Copilot app" while "Copilot for Microsoft 365" became "Microsoft 365 Copilot." Old articles and UI labels keep the confusion alive.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which Copilot you are actually looking at

Before paying for anything or filing anything as broken, figure out which product is in front of you. Most "Copilot is not working" complaints turn out to be someone expecting Microsoft 365 features from the free Windows app.

1. Press the **Copilot key** (or open the Copilot app from the taskbar) — this is the free Windows-side assistant for general questions and PC settings.
2. Open Word and look for a **Copilot** button in the ribbon — that is Microsoft 365 Copilot, the paid Office-integrated product.
3. Ask the Copilot app to summarize your open Word document — it cannot, because it has no file access. That limitation is by design.
4. In Word, ask Copilot to "draft a summary of this document" — if it works, your license is active; if it prompts you to buy, you only have the free tier.
5. Decide which one you need before continuing: everyday PC help means the free app is enough; AI inside Office documents means the paid license.

### Fix 2: Get the free Windows Copilot working properly

If the Copilot app or key does nothing, the problem is on the Windows side — usually the app version, the key assignment, or a regional rollout gap rather than anything about your Microsoft 365 subscription.

1. Open the **Microsoft Store**, check **Library** for Copilot app updates, and install any pending version.
2. Press the Copilot key and confirm the app launches — if nothing happens, check **Settings** for what the key is bound to (the location varies by laptop maker).
3. Sign into the Copilot app with your Microsoft account; longer conversations require sign-in.
4. Confirm Windows 11 is current via **Settings > Windows Update** — the Copilot app needs recent servicing updates.
5. If the app is missing in your region, use copilot.microsoft.com in Edge while you wait — app availability quirks are common here, as the [Xbox app's ARM issues](/articles/xbox-app-arm-windows-not-working/) show.

### Fix 3: Decide whether you need the paid Microsoft 365 Copilot

Do not buy the license reflexively. Map your actual work to what the paid tier adds over the free app, because for many home users the free Copilot plus built-in Office features is plenty.

1. List what you want AI to do: if it is "answer questions, change settings, draft casual text," the free Copilot app covers it.
2. If the list includes summarizing Word docs, drafting from your inbox, or recapping Teams meetings, that is Microsoft 365 Copilot territory — the free app cannot touch your files.
3. Check pricing for your situation: work and school accounts need the Microsoft 365 Copilot add-on; personal users can use **Copilot Pro** with a Microsoft 365 Personal or Family subscription.
4. Start with one license before buying for a team — Copilot's value varies hugely by workflow, and a month of real use beats any feature list.
5. The Copilot+ exclusives (Recall, Click to Do, Studio Effects, Live Captions) need no subscription — if those drew you to the AI PC, spend energy instead on things like [Smart charging quirks](/articles/smart-charging-not-working-windows-11/) that affect daily laptop life.

### Fix 4: Activate Microsoft 365 Copilot in the Office apps

Bought the license but Word still shows no Copilot button? Activation has three checkpoints — license assignment, app update, and sign-in — and the button appears only when all three pass.

1. Confirm the license is **assigned** to your account in the Microsoft 365 admin center (work) or shows under Subscriptions at account.microsoft.com (personal).
2. In any Office app, run **File > Account > Update Options > Update Now** — Copilot buttons need recent Current Channel builds.
3. Verify the account under **File > Account** matches the licensed account; a personal sign-in on a work-licensed machine hides the feature.
4. Restart the Office apps after updating and look for the Copilot icon in the ribbon or the side pane toggle.
5. If the button appears in Word but not Outlook or OneNote, that is normal — Copilot rolls out per app, and some apps never get it, much like how [Live Captions settings](/articles/live-captions-profanity-filter-settings/) differ across similar-looking apps.

### Fix 5: Understand what the NPU actually accelerates

Copilot+ marketing blurs the line between cloud AI and on-device AI. Knowing which Copilot features use your NPU stops you from misdiagnosing problems — a slow Copilot answer is a network issue, not an NPU failure.

1. Cloud features (free Copilot chat and Microsoft 365 Copilot alike) send prompts to Microsoft's servers — the NPU sits idle, so NPU drivers are irrelevant to them.
2. On-device features — Recall, Click to Do, Live Captions, Studio Effects, Paint Cocreator — run on the NPU and keep working offline.
3. If a cloud Copilot feature is slow or failing, troubleshoot your connection and license, not your drivers.
4. If an on-device feature like Recall fails, *that* is when NPU drivers and Windows AI components (like the Copilot Runtime) become suspects.
5. Keep both stacks healthy with Windows Update, and grab NPU drivers from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) or [AMD](https://www.amd.com/en/support/download/drivers.html) if your maker lags — they only affect the on-device side.

### Fix 6: Clean up the confusion: rename-proof your setup

Because Microsoft keeps renaming these products, future-proof your understanding with labels that survive the next rebrand — and pin the right apps so you stop opening the wrong Copilot.

1. Mentally (or literally, in a note) label them: **"PC Copilot"** = free app/key for chat and settings; **"Office Copilot"** = paid assistant inside Word, Excel, Outlook, Teams.
2. Pin the Copilot app to your taskbar for PC help, and use the ribbon buttons inside Office apps for document work — two doors, two products.
3. If a tutorial shows "Windows Copilot" working in Word, translate it: it means Microsoft 365 Copilot, whatever name it uses.
4. When asking support or IT for help, specify which one you mean — "the Copilot button in Word is missing" gets a license check, "the Copilot key does nothing" gets an app check.
5. For current naming, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows), which track renames faster than third-party tutorials.

## Closing

Windows Copilot and Microsoft 365 Copilot share a name and almost nothing else: the free assistant for your PC versus the paid assistant for your documents. Identify which one you are using, confirm it is the one you need, and most of the confusion resolves itself.
