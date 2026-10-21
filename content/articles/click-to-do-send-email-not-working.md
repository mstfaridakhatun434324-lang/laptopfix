---
title: "How to Fix Click to Do Send Email Not Working on AI PCs"
slug: click-to-do-send-email-not-working
date: 2026-10-21
categories: ["ai-pc"]
tags: ["click to do send email", "click to do email action", "copilot+ pc", "default mail app", "windows 11", "mailto"]
description: "Fix Click to Do Send Email not working on your AI PC with six step-by-step methods covering default mail apps, mailto handling, Outlook setup, and permissions."
thumbnail: "/images/thumbs/click-to-do-send-email-not-working.webp"
faqs:
  - q: "What is the Click to Do Send Email action supposed to do?"
    a: "When you select an email address and invoke Click to Do, the Send Email action opens a new message addressed to that contact in your default mail app. If nothing opens, the mail handoff is broken."
  - q: "Why does Send Email open the wrong app?"
    a: "Click to Do hands the address to Windows' default mail app via the mailto protocol. If your default mail app is set to something unexpected — or the mailto association is broken — the wrong app opens or nothing happens."
  - q: "Does Send Email need Outlook installed?"
    a: "No. It needs any working default mail app — the new Outlook for Windows, Thunderbird, or another mail client registered for mailto. With no mail app set as default, the action silently fails."
  - q: "Can I make Send Email use Gmail in the browser instead?"
    a: "Only indirectly. Click to Do opens the system default mail handler. Set your browser as the mailto handler with a Gmail mailto extension, and Send Email opens Gmail in the browser."
---

Select any email address on screen, invoke Click to Do, hit **Send Email**, and a compose window opens with the address filled in. When that action does nothing, you are back to copying addresses by hand.

The Send Email action is a handoff, not a mail client. Click to Do detects the address, then asks Windows to open it with your default mail app through the `mailto:` protocol. That chain has three links — detection, the mailto association, and the mail app itself — and a break in any one produces the same symptom: nothing happens.

This guide runs through six fixes in order: verifying the action appears, repairing the default mail app, fixing the mailto association, configuring Outlook, checking permissions, and the browser-mailto case.

## Why this happens

- **No default mail app is set:** Without a configured mail client, the mailto protocol has nowhere to go, and Click to Do fires the handoff into the void.
- **Broken mailto protocol association:** The registry association linking `mailto:` to your mail app can be damaged by uninstalls or failed updates. The action then fails silently.
- **Wrong default mail app:** If mailto points at an app you never use, the compose window opens somewhere you do not notice — looking like nothing happened.
- **Outlook not fully configured:** With Outlook as default but no account signed in, the compose window may flash and vanish. When [Teams is crashing](/articles/teams-crashing-snapdragon-laptop/) too, the Microsoft 365 sign-in state is often the shared root cause.
- **Click to Do lacks permission to launch apps:** Privacy settings that block Click to Do from opening other apps neuter every "act on it" action, Send Email included.
- **Old protocol-handler leftovers:** Retired communication apps sometimes leave competing protocol handlers behind. If [Skype's AI features are also misbehaving](/articles/studio-effects-not-available-in-skype/), leftover registrations from that era can be part of the same mess.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the Send Email action appears and triggers

First confirm which link is broken: does the Send Email action show up when you select an email address, and what happens when you click it? A missing action is a Click to Do problem; a dead click is a mail-handoff problem.

1. Open Notepad, type `test@example.com`, and select it.
2. **Win + click** the selection to open Click to Do and look for the **Send Email** action.
3. If the action is missing, check the Click to Do toggles in **Settings > Privacy & security > Click to Do**.
4. If the action appears but clicking it does nothing, continue — the mail handoff is broken.
5. Note exactly what happens (nothing, wrong app, flash-and-close) for the steps below.

### Fix 2: Set a proper default mail app

The most common cause is having no usable default mail app. Windows needs one registered `mailto:` handler — without it, Send Email has no destination.

1. Go to **Settings > Apps > Default apps** and search for your preferred mail app.
2. Select it and set it as default for **MAILTO** (and email file types while you are there).
3. Or scroll to the **mailto** protocol entry in the Default apps list and assign your mail app directly.
4. Install the new **Outlook for Windows** from the Microsoft Store if no mail app is present.
5. Retest: select the test address in Notepad, invoke Click to Do, and click **Send Email**.

### Fix 3: Repair the mailto protocol association in the registry

If a default app is set but Send Email still does nothing, the mailto association is likely corrupt — pointing at an uninstalled app. Rebuilding it forces Windows to re-resolve the handler.

1. In **Settings > Apps > Default apps**, change the **MAILTO** handler to a different app, then change it back — this rewrites the association.
2. If that fails, open **regedit** and inspect `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\Shell\Associations\UrlAssociations\mailto\UserChoice` for a stale ProgId.
3. Delete the `UserChoice` key for mailto (Windows rebuilds it), then re-set your default mail app.
4. Test mailto directly: press **Win + R**, type `mailto:test@example.com`, and press Enter — the compose window should open.
5. If the Run dialog test works, Click to Do's Send Email will work too.

### Fix 4: Sign in and configure your Outlook account fully

When Outlook is the default but has no working account, the compose window cannot initialize — it may flash and vanish. This is common after a Windows reset that kept the app but dropped the sign-in. A [misbehaving Copilot+ microphone](/articles/copilot-plus-pc-microphone-not-working/) alongside can indicate the same unhealthy Microsoft 365 sign-in state.

1. Open Outlook directly and check you are signed in with a working account.
2. Send a test email from inside Outlook to confirm the account works.
3. If sign-in loops, remove the account in **Settings > Accounts > Email & accounts** and add it fresh.
4. In Outlook settings, confirm a default **From** account is selected for new messages.
5. Retest Click to Do's Send Email — with a healthy Outlook, the compose window opens addressed correctly.

### Fix 5: Allow Click to Do to launch other apps

Click to Do's "act on it" actions require permission to launch other applications. If that permission was denied during setup or by a privacy script, every launch action silently fails.

1. Open **Settings > Privacy & security > Click to Do** and enable anything related to launching apps or actions.
2. Check **Settings > Privacy & security > App permissions** for denied Click to Do entries.
3. Sign out and back in so permission changes take effect.
4. Retest Send Email from the Notepad test address.

### Fix 6: Route mailto through the browser for webmail workflows

If you live in Gmail or Outlook on the web with no desktop mail app, register the browser as the mailto handler. Send Email then opens a web compose window instead of failing.

1. In Chrome or Edge, install a mailto-handler extension for Gmail (or use Edge's protocol handler settings for Outlook web).
2. Register the browser for **mailto** links (Chrome: Privacy and security > Site settings > Protocol handlers).
3. In **Settings > Apps > Default apps**, set your browser as the **MAILTO** handler.
4. Test with **Win + R** → `mailto:test@example.com` — a browser compose tab should open. Microsoft documents protocol handlers in the [Windows support hub](https://support.microsoft.com/en-us/windows).
5. Retest Click to Do's Send Email; it now flows through the browser.

## Closing

Click to Do's Send Email is only as healthy as the mailto chain beneath it: detection, protocol association, and a configured default mail app. Usually the fix is setting a real default mail app or repairing the mailto association.
