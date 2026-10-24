---
title: "How to Fix Copilot Pages Not Working on Windows 11"
slug: copilot-pages-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["copilot-pages", "microsoft-copilot", "windows-11", "copilot-not-working", "ai-pc"]
description: "Copilot Pages won't open or load on your Windows 11 laptop? This hands-on guide explains the real causes and walks you through proven, technician-tested fixes."
thumbnail: "/images/thumbs/copilot-pages-not-working.webp"
faqs:
  - q: "Why do Copilot Pages show a blank screen when I open them?"
    a: >
      A blank Pages screen is usually a sign-in or rendering problem, not lost data. The app may hold a stale account token, or its cached web components have gone bad. Signing out and back in, then updating Copilot from the Microsoft Store, fixes most blank-screen cases.
  - q: "Are Copilot Pages available on every Microsoft account?"
    a: >
      Pages are broadly available on personal Microsoft accounts, though rollout can vary by region and app version. Work or school accounts follow your organization's admin settings, so Pages may be hidden there. If Pages work on the web but not in the app, the app itself is at fault.
  - q: "Did my Copilot Pages get deleted?"
    a: >
      Almost certainly not. When Pages fail to load, the content is typically still stored in your account and reappears once the loading issue is fixed. Check the Pages panel at copilot.microsoft.com in a browser first — if your pages show there, this is purely a client-side fault.
  - q: "Does Copilot Pages require a Microsoft 365 Copilot license?"
    a: >
      No. Pages is a consumer Copilot feature that works with a free Microsoft account. If you are on a work account and Pages are missing, that is an admin policy matter — ask IT whether Copilot consumer features are enabled for your tenant.
---

Copilot Pages is one of those features you only appreciate once it stops working. You type a long, detailed prompt, Copilot turns it into a tidy editable page you can keep refining — and then one morning the Pages button is greyed out, the panel opens to a blank white screen, or every page spins forever. It feels especially annoying on a new AI PC, where you bought the hardware partly for this kind of AI workflow, and now the flagship feature will not cooperate.

Under the hood, Pages is a web-based component rendered inside the Copilot app that talks to Microsoft's servers using your account token. So a Pages failure is almost always one of three things: the app cannot prove who you are (a stale sign-in), it cannot render the page (an outdated Copilot or WebView2 component), or your account or region is not being offered the feature. The good news is that all three are fixable without reinstalling Windows.

Work through the fixes below from top to bottom, quick and common causes first. If you are also seeing wider strangeness on an Arm laptop — for example [Edge crashing repeatedly on Windows 11](/articles/edge-arm64-crashing-windows-11/) or [Hyper-V behaving oddly on an Arm machine](/articles/hyper-v-arm-laptop-issues/) — the same methodical approach of checking updates, clearing caches, and repairing components applies. And if your AI PC's troubles began right after a driver update, [stuck Intel NPU driver updates](/articles/intel-npu-driver-update-stuck/) can leave the system half-updated in ways that break app rendering.

## Why this happens

- **Stale sign-in token:** the app holds an old authentication token the server no longer accepts, so Pages requests silently fail.
- **Outdated Copilot app:** Pages ships with the app shell, and the Store sometimes lags behind on fresh Windows installs.
- **Broken WebView2 runtime:** the app renders Pages through WebView2, and a corrupted install produces blank panels.
- **Account or region restriction:** work accounts with admin-disabled features, or regions without rollout, hide Pages entirely.
- **Corrupted app cache:** stale cached page data blocks new Pages from loading, showing an endless spinner.
- **Network interference:** aggressive VPNs, proxies, or DNS filters can block Pages endpoints while chat still works.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm you are signed in with the right account

Copilot chat can work in a semi-signed-out state while Pages refuses to load, which makes this easy to miss. Open the Copilot app, click your profile avatar, and verify the exact account shown. If you have both a personal and a work account, try the personal one first, since Pages is primarily a consumer feature. A full sign-out and sign-in refreshes the token Pages depends on.

1. Open Copilot, click your profile picture, and choose Sign out.
2. Close the Copilot app completely.
3. Reopen Copilot and sign in with your personal Microsoft account.
4. Open the Pages panel and check whether it loads now.

### Fix 2: Update the Copilot app from the Microsoft Store

The Pages feature ships with the app shell itself, not with Windows, so an old Copilot version may simply lack a working Pages implementation. The Store does not always auto-update promptly, particularly on new AI PCs that sat in a warehouse with an old image. Updating takes two minutes and fixes a large share of Pages failures.

1. Open the Microsoft Store and go to your Library.
2. Click "Get updates" and wait for the scan to finish.
3. Install the Copilot update if one appears, then relaunch the app.
4. Confirm the app version is current before testing Pages again.

### Fix 3: Repair or reset the Copilot app

When an update does not help, the app's stored data is the next suspect. Windows lets you repair a Store app without losing data, and reset it when repair is not enough. Resetting clears the cached Pages content and the sign-in token, which resolves corrupted-cache cases. You will sign in again afterward, so keep your credentials handy.

1. Open Settings, then Apps, then Installed apps.
2. Find Microsoft Copilot, open its menu, and choose Advanced options.
3. Click Repair, wait for the checkmark, then test Pages.
4. If it still fails, click Reset, confirm, then reopen Copilot and sign in.

### Fix 4: Reinstall the WebView2 runtime

The Copilot app draws its Pages panel using Microsoft Edge WebView2, a shared component other apps use too. If WebView2 is damaged, you will often see blank white areas in several apps, not just Copilot. Reinstalling it from Microsoft's official source replaces the broken files without touching your data. This is especially worth trying when the problem appeared after a failed update.

1. In Installed apps, search for Microsoft Edge WebView2 Runtime and uninstall it.
2. Download the Evergreen Standalone Installer from Microsoft's official site.
3. Run the installer and restart your laptop when it finishes.
4. Open Copilot and test the Pages panel again.

### Fix 5: Test Pages on the web to isolate the fault

Before going deeper, establish whether the problem is your PC or your account. Open Edge, go to copilot.microsoft.com, sign in with the same account, and try Pages there. If Pages work in the browser, your account is fine and the fault is strictly the local app. If they fail on the web too, the issue is account-side — a region restriction, an admin policy, or a service outage — and no local repair will fix it. Also try disconnecting any VPN, since VPNs can block Pages endpoints while chat keeps working.

1. In Edge, go to copilot.microsoft.com and sign in with the same account.
2. Open the Pages panel and try creating and opening a page.
3. Working on web but broken in app means a local app fault — repeat Fix 3 and 4.
4. Broken in both places points to account, region, VPN, or service status.

## Closing

Copilot Pages failures look alarming but are rarely serious: your pages are almost always safe in your account, and the cause is usually a stale token, an old app version, or a damaged WebView2 runtime. Work the list in order and most cases resolve by Fix 4. If Pages work on the web but never in the app even after a reset, check your Windows build against the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) guidance — very old builds can ship a Copilot shell that predates stable Pages support. For anything deeper, the official [support hub](https://support.microsoft.com/en-us/windows) documents the current repair paths.
