---
title: "Copilot Not Responding on Windows 11? Fixes That Work"
slug: copilot-not-responding
date: 2026-10-19
categories: ["ai-pc"]
tags: ["copilot", "not responding", "windows 11", "copilot troubleshooting", "ai assistant"]
description: "Copilot not responding on Windows 11? Find out why Copilot freezes or ignores input and follow step-by-step fixes to get answers again."
thumbnail: "/images/thumbs/copilot-not-responding.webp"
faqs:
  - q: "Why does Copilot open but never answer my questions?"
    a: >
      The app window loads but the backend service never connects. This is usually a network or account issue: Copilot cannot reach Microsoft's servers, or your sign-in token expired. Checking connectivity and re-signing in resolves most of these cases.
  - q: "Is Copilot down or is it my laptop?"
    a: >
      Check quickly by opening Copilot in a web browser at copilot.microsoft.com. If it works there, the problem is your app or PC. If it fails there too, Microsoft's service itself is having issues and you just need to wait.
  - q: "Does Copilot need the internet to respond?"
    a: >
      Yes, for full responses. Copilot processes queries on Microsoft's servers, so without a working connection it can open its window but cannot generate answers. Some on-device features exist on Copilot+ PCs, but conversational replies need the cloud.
  - q: "Why does Copilot freeze when I paste long text?"
    a: >
      Very long inputs can overwhelm the app's input handling, especially on machines with limited RAM. Try shorter prompts first. If short prompts also freeze, the issue is the app or connection, not your input length.
---

Copilot opens fine, you type a question, hit enter — and nothing. The typing indicator spins forever, or the app just sits there ignoring you. It is a special kind of frustration: the assistant is right there on screen, looking ready, but completely unresponsive.

When Copilot does not respond, the problem is rarely the app window itself. The window is just a shell; the actual answering happens on Microsoft's servers. So an unresponsive Copilot almost always means one of three things: it cannot reach the servers, your sign-in session broke, or a local component (like the WebView renderer) is stuck. If the app will not even open, start with our guide on the [Copilot app not opening on Windows 11](/articles/copilot-app-not-opening-windows-11/) instead — but if it opens and then ignores you, you are in the right place.

The fixes below move from fastest to deepest. Most people find the answer by Fix 3.

## Why this happens

- **No working internet path to Copilot servers:** The app opens offline but cannot fetch answers without connectivity to Microsoft's endpoints.
- **Expired or corrupt sign-in token:** Your Microsoft account session inside Copilot silently expired, so requests are rejected.
- **WebView2 renderer stuck:** The embedded browser component froze, so the interface cannot send or display anything.
- **VPN or proxy interference:** Some VPNs and corporate proxies block or reroute the domains Copilot needs.
- **Corrupt app cache:** Damaged local data can leave the app in a half-loaded state where the UI works but messaging does not.
- **Microsoft service outage:** Occasionally the problem is on Microsoft's side and no local fix will help until it passes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether Copilot's service is up
Before touching your laptop, rule out a Microsoft-side outage in thirty seconds.

1. Open your browser and go to copilot.microsoft.com.
2. Sign in with the same Microsoft account and ask a simple question.
3. If it answers normally, the service is fine and the problem is local to your app — continue to Fix 2.
4. If the website also fails to respond, check Microsoft's service status page or a downtime tracker for reported Copilot issues.
5. During a confirmed outage, just wait. No amount of reinstalling will fix a server-side problem.

### Fix 2: Sign out and back into Copilot
An expired authentication token is one of the most common causes of a Copilot that opens but never answers.

1. In the Copilot app, open the profile or settings menu (usually your avatar in the corner).
2. Sign out of your Microsoft account completely.
3. Close the Copilot app fully — right-click its taskbar icon and choose Quit, or end it in Task Manager.
4. Reopen Copilot and sign back in with your Microsoft account.
5. Ask a test question. A fresh token resolves the silent-rejection problem in most cases.
6. If there is no visible sign-out option, use Fix 4's reset, which also clears the stored credentials.

### Fix 3: Test your connection and disable VPN temporarily
Copilot needs a clean path to Microsoft's servers. VPNs, proxies, and strict firewalls are frequent silent blockers.

1. Open a browser and confirm general internet works, then specifically try copilot.microsoft.com.
2. If you use a VPN, disconnect it completely and test Copilot again.
3. If Copilot responds without the VPN, the VPN is the blocker — check its settings for split tunneling or allowlist Microsoft's domains.
4. Try switching networks (phone hotspot versus home Wi-Fi) to rule out ISP or router-level blocking.
5. Corporate or school networks often block AI services at the firewall — test on a personal network to confirm.
6. If a different network fixes it, the issue is network policy, not your laptop.

### Fix 4: Clear Copilot's cache with a reset
Damaged local data can leave Copilot stuck in a state where the UI renders but messaging never completes.

1. Open Settings > Apps > Installed apps and find Microsoft Copilot.
2. Click the three dots, choose Advanced options.
3. Click Repair first, wait for the checkmark, and test.
4. If still unresponsive, click Reset on the same page and confirm. This clears cache and sign-in state.
5. Reopen Copilot, sign in again, and test with a simple question.
6. If the app now responds, the cache was corrupt. If it is still silent, continue to Fix 5.

### Fix 5: Reinstall WebView2 and the Copilot app
When the embedded renderer is damaged, the app can display its interface but never actually communicate.

1. In Settings > Apps > Installed apps, uninstall "Microsoft Edge WebView2 Runtime" if present.
2. Download a fresh WebView2 runtime from Microsoft's official site and install it.
3. Next, uninstall the Copilot app itself from Installed apps.
4. Restart your laptop to clear any locked components.
5. Reinstall Copilot from the Microsoft Store and launch it.
6. Sign in and test. If it responds now, the damaged renderer was the cause. If it still hangs, see our guide on [Copilot web view not loading](/articles/copilot-web-view-not-loading/) for deeper WebView diagnostics.

### Fix 6: Check for resource exhaustion and conflicting software
On machines with little free RAM, or with aggressive "optimizer" software, Copilot's processes can be starved or killed.

1. Open Task Manager (Ctrl + Shift + Esc) and check memory usage. If you are above 90% with Copilot open, close heavy apps and test again.
2. Look for Copilot-related processes in Task Manager. If they repeatedly appear and vanish, something is killing them — check your antivirus quarantine.
3. Temporarily disable third-party antivirus and test Copilot. If it responds, add an exclusion for the Copilot app.
4. Disable any "game booster" or RAM-cleaner utilities, which are notorious for killing background app processes.
5. As a final isolation test, try Copilot in a new local Windows user account. If it works there, your main profile has a software conflict to hunt down.

## Closing

A Copilot that opens but never answers is almost always a connectivity, sign-in, or renderer problem — not a dead app. The thirty-second website test tells you immediately whether to blame Microsoft or your machine, and the sign-out/sign-in plus cache reset resolves the majority of local cases. If the app also crashes outright, work through [Copilot app crashing](/articles/copilot-app-crashing/); and if you would rather silence the whole thing, here is how to [disable the Copilot key](/articles/disable-copilot-key/). If Copilot works in the browser but never in the app despite everything here, keep the web version bookmarked as your fallback while Microsoft sorts the app out.
