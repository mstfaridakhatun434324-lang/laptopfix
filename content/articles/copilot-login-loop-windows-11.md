---
title: "Copilot Stuck in a Login Loop on Windows 11? How to Fix It"
slug: copilot-login-loop-windows-11
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot login loop", "copilot sign in problem", "troubleshooting", "ai pc", "microsoft account", "windows 11"]
description: "Fix Copilot stuck in a login loop on Windows 11 — endless sign-in prompts, expired tokens, and account conflicts on your AI PC, resolved step by step."
thumbnail: "/images/thumbs/copilot-login-loop-windows-11.webp"
faqs:
  - q: "Why does Copilot ask me to sign in every time I open it?"
    a: 'The app usually cannot save its sign-in token due to corrupted app data or a Credential Manager problem. Repair Copilot and clear stale credentials. If it happens on one network only, a firewall may block the token refresh.'
  - q: "Can I use Copilot without signing in to a Microsoft account?"
    a: 'You can use a limited anonymous mode, but you lose history, personalization, Designer boosts, and Pro features. The Windows 11 app strongly prefers a signed-in account and will keep prompting you.'
  - q: "Why does sign-in work in my browser but not in the Copilot app?"
    a: 'The app signs in through Microsoft Edge WebView2, separate from your browser — a working browser login does not guarantee a working app login. Repairing WebView2 usually resolves this; corrupted Credential Manager entries are the other common cause.'
  - q: "Will resetting the Copilot app delete my chat history?"
    a: 'No — history is stored in your Microsoft account in the cloud, not just the app. Resetting clears local data and forces a fresh sign-in, then history syncs back. Anonymous-session content is not saved.'
---

You click Sign in, a login window flashes, you enter your password — and you're back at the sign-in screen. Again and again. The Copilot login loop is maddening because every attempt looks like it should work, yet nothing sticks.

The loop happens when Copilot can't finish authentication's final step: saving the sign-in token. Expired cached tokens, personal-versus-work account conflicts, a broken WebView2 runtime, or corrupted Credential Manager entries can all trap you — even a wrong system clock breaks validation.

This guide breaks the loop step by step, from clearing stale sign-in state to repairing the authentication components. Work through the fixes in order, attempting a normal sign-in after each one. The loop always has a cause, and one of these steps removes it.

## Why this happens

- **Expired tokens stuck in the cache:** Copilot tries to refresh a dead token instead of starting clean, and the refresh keeps failing silently.
- **Personal and work accounts conflict:** Windows holds credentials for both, and Copilot can't decide which identity to complete.
- **Broken Edge WebView2 runtime:** the sign-in window runs on WebView2, so a damaged runtime breaks authentication while Windows otherwise works.
- **Corrupted Credential Manager entries:** stale Copilot credentials cause each new login to fail validation.
- **Wrong system date and time:** tokens are time-sensitive, and a clock off by minutes invalidates every one of them.
- **VPN or firewall intercepting login traffic:** security software and proxies can block or alter the authentication handshake mid-flight.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the sign-in state completely

The loop persists because Copilot retries with the same broken sign-in state instead of starting fresh. Sign out everywhere — the app, the system tray instance, and the browser — so no stale session resurrects itself. Many skip the tray step, but Copilot keeps running there holding old tokens.

1. In the Copilot app, open Settings and choose Sign out.
2. Right-click the Copilot icon in the system tray and select Quit.
3. Open your browser, go to copilot.microsoft.com, and sign out.
4. Also sign out at account.microsoft.com to clear the web session.
5. Restart the Copilot app and try signing in fresh.

### Fix 2: Delete stale credentials from Credential Manager

Windows stores Copilot's tokens in Credential Manager, where entries can corrupt beyond the app's ability to repair. The damaged credential fails validation on every launch, throwing you back to the login screen. Removing the Copilot entries forces Windows to create clean ones — a minute's work that fixes loops surviving reinstalls.

1. Press the Windows key, type Credential Manager, and open it.
2. Open Windows Credentials and find entries mentioning Copilot or SSO.
3. Remove the Copilot-related entries, leaving unrelated ones alone.
4. Close Credential Manager and restart your laptop.
5. Open Copilot and sign in — Windows stores fresh credentials.

### Fix 3: Repair Microsoft Edge WebView2

The Copilot login window is rendered by Microsoft Edge WebView2, which can break independently of Edge. When damaged, sign-in loads just far enough to look normal, then fails at the token handoff — the classic loop. On Snapdragon ARM laptops, also check your [Prism emulator settings on Windows 11](/articles/prism-emulator-settings-windows-11/). Repairing WebView2 restores login for Copilot and every app using it.

1. Open Settings > Apps > Installed apps.
2. Find Microsoft Edge WebView2 Runtime in the list.
3. Click the three dots, choose Modify, then Repair.
4. Wait for the repair to finish and restart your laptop.
5. Open Copilot and attempt to sign in again.

### Fix 4: Fix the system clock and resolve account conflicts

Tokens carry timestamps — if your clock disagrees with Microsoft's servers by minutes, every token is rejected, creating an instant loop with no useful error. Personal and work accounts on one machine also confuse Copilot's identity choice. Microsoft covers both fixes on the [official Windows support page](https://support.microsoft.com/en-us/windows).

1. Open Settings > Time and language > Date and time.
2. Turn on Set time automatically and Set time zone automatically.
3. Click Sync now and confirm the displayed time is correct.
4. Go to Settings > Accounts > Email and accounts and review each account.
5. Remove duplicates, keeping the account you use for Copilot.

### Fix 5: Rule out interfering software and drivers

Security suites and firewalls sometimes intercept the login handshake and silently break it — if the loop started after installing one, disable it for a single sign-in attempt as a diagnostic. On AI PCs, a malfunctioning NPU driver can also destabilize AI apps, so test with the NPU [disabled in Device Manager](/articles/how-to-disable-npu-device-manager/). Re-enable everything except the culprit.

1. Temporarily disable third-party antivirus or firewall software.
2. Disconnect from any VPN and try signing in on a plain connection.
3. If the loop persists, disable the NPU in Device Manager as a test.
4. Attempt sign-in with each change to identify the culprit.
5. Re-enable everything except the component causing the loop.

### Fix 6: Reset the Copilot app and re-register it

When targeted fixes fail, the installation is damaged beyond repair's reach. A full reset wipes local state — settings, cache, token storage — returning the app to just-installed condition; cloud history survives. After a successful sign-in, verify local AI features engage the hardware by checking whether the [NPU is being used by apps](/articles/npu-not-used-by-apps-windows-11/).

1. Open Settings > Apps > Installed apps and find Microsoft Copilot.
2. Open Advanced options and click Repair first, then test sign-in.
3. If the loop continues, return to the same page and click Reset.
4. Restart the laptop, open Copilot, and sign in.
5. Confirm you stay signed in after closing and reopening the app.

## Closing

A login loop is always concrete: a stale token, a corrupted credential, a broken WebView2, a wrong clock, or software intercepting the handshake. Clear the sign-in state first, then work through the deeper layers. Once you stay signed in across restarts, the loop is broken.
