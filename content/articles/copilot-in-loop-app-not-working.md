---
title: "How to Fix Copilot in the Loop App Not Working on Windows 11"
slug: copilot-in-loop-app-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["copilot", "loop-app", "windows-11", "microsoft-loop", "ai-pc"]
description: "Copilot in the Loop app won't load, sync, or respond on Windows 11? This technician's guide walks through the real causes and step-by-step fixes that work."
thumbnail: "/images/thumbs/copilot-in-loop-app-not-working.webp"
faqs:
  - q: "Is Copilot in the Loop app different from the Loop website?"
    a: >
      The Loop app on Windows is a native wrapper around the same Loop service that powers loop.microsoft.com. Your workspaces live in the cloud, not in the app. An app that will not open is a client problem — your content stays safe and reachable from any browser while you fix it.
  - q: "Why does the Loop app show a blank screen on my new laptop?"
    a: >
      A blank Loop app is usually a failed sign-in or a broken WebView2 rendering component. New laptops sometimes ship with an outdated WebView2 runtime or a half-completed first sign-in. Signing out fully, updating WebView2, and reinstalling Loop resolves most cases.
  - q: "Does the Loop app need a Microsoft 365 subscription?"
    a: >
      Basic Loop access works with a free Microsoft account, though some Copilot-in-Loop AI features require a Microsoft 365 Copilot license. If the app opens but AI features specifically fail, check your license. Plain sync and editing problems are almost never licensing issues.
  - q: "Can I just use Loop in the browser instead of the app?"
    a: >
      Absolutely, and it is a good diagnostic step. If loop.microsoft.com works in Edge but the app does not, you have proven the fault is local to the app. Many people use the browser version full-time, though the app offers better notifications when healthy.
---

You open the Loop app to check a workspace, and nothing happens — a white window, an endless loading shimmer, or a sign-in loop bouncing you back to the login screen. The timing always seems terrible: right before a meeting, right when you need that shared page. On a new AI PC the frustration doubles, because the machine was supposed to make AI-assisted collaboration smoother, not add another broken app.

Loop on Windows is a packaged web app: it renders the Loop service inside a native shell using WebView2, Microsoft's shared web-rendering component. So "the Loop app is not working" usually means one of three underlying faults — the sign-in token is stale, WebView2 is damaged or outdated, or the app's local data is corrupted. Your workspaces live in Microsoft's cloud, which is why the same account works fine in a browser while the app sulks.

The fixes below run from quickest to deepest: verify sign-in, update components, repair the app, and only then reinstall. The same disciplined sequence sorts out other misbehaving apps on modern laptops — the approach that steadies [Zoom on Arm64 Windows](/articles/zoom-arm64-windows-issues/) or untangles a [Rust install on Arm Windows](/articles/rust-arm-windows-install-issues/) applies here too. And if accessibility features have been acting up alongside app issues, problems like [switching live captions between multiple languages](/articles/live-captions-multiple-languages-switch/) often share the same root causes of stale components and pending updates.

## Why this happens

- **Stale sign-in session:** the app's cached credentials expired, trapping you in a login loop.
- **Outdated WebView2 runtime:** the rendering engine Loop depends on is old or corrupted, producing blank windows.
- **Corrupted app data:** the Loop app's local cache holds bad state that blocks startup.
- **Pending app update:** the installed Loop build is too old for current service endpoints.
- **Account type mismatch:** a work account whose tenant restricts Loop fails while the personal account works.
- **Network filtering:** VPNs or corporate proxies block Loop's sync endpoints while Microsoft 365 works.
- **Windows component drift:** missing cumulative updates leave system web components incompatible with the app.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out a service or account problem in the browser

Before repairing anything local, confirm your account and the Loop service are healthy. Open Edge, go to loop.microsoft.com, and sign in with the same account the app uses. If workspaces load and sync there, the service is fine and the fault is strictly the Windows app. If the browser also fails, check Microsoft's service status and try your other account type before spending time on the app.

1. In Edge, go to loop.microsoft.com and sign in with the same account.
2. Open a workspace and confirm pages load and sync.
3. If the browser works, continue with the app fixes below.
4. If both fail, check service status and try the alternate account type.

### Fix 2: Sign out fully and sign back in

The Loop app's most common failure is a half-expired sign-in: enough token left to open the shell, not enough to load content. A proper sign-out clears that token completely, unlike simply closing the window. Use the app's account menu, then close the app fully before signing back in. This two-minute step resolves the login-loop symptom in most cases.

1. In the Loop app, click your profile avatar and choose Sign out.
2. Close the app completely, checking the system tray.
3. Reopen Loop and sign in with your Microsoft account.
4. Wait for the initial sync to finish before opening a workspace.

### Fix 3: Update the Loop app from the Microsoft Store

Loop's Windows app updates through the Microsoft Store, and the Store's auto-update is notoriously lazy on new machines. An outdated Loop build may call service endpoints that no longer exist, producing the endless loading shimmer. Open the Store, force a manual update check, and make sure Loop is current before anything more drastic.

1. Open the Microsoft Store and go to Library.
2. Click "Get updates" and let the scan complete.
3. Install the Loop update if one is offered, then relaunch Loop.

### Fix 4: Repair or reset the Loop app

When updates and re-sign-ins fail, the app's local data is the likely culprit. Windows provides a Repair option that fixes the installation without touching data, and a Reset option that wipes local state clean. Since all Loop content lives in the cloud, Reset is safe — you will just sign in again and resync. Microsoft documents these app repair steps in the official [support hub](https://support.microsoft.com/en-us/windows).

1. Open Settings, then Apps, then Installed apps.
2. Find Microsoft Loop, open its menu, and choose Advanced options.
3. Click Repair, wait for completion, and test the app.
4. If it still fails, click Reset, confirm, reopen Loop, and sign in.

### Fix 5: Reinstall the WebView2 runtime

The Loop app paints everything through WebView2. If that shared component is damaged — after a failed update, an aggressive cleaner app, or a botched Windows upgrade — Loop shows a blank window while simpler apps still work. Reinstalling WebView2 replaces the broken files without affecting your documents. If several web-based apps show blank screens, this fix becomes the prime suspect.

1. In Installed apps, uninstall Microsoft Edge WebView2 Runtime.
2. Download the Evergreen Standalone Installer from Microsoft's official site.
3. Run the installer and restart your laptop.
4. Open Loop and verify workspaces render.

### Fix 6: Clean reinstall of the Loop app

If nothing above worked, do a full clean reinstall. Uninstall Loop, restart the machine (this releases locked cache files), then install fresh from the Microsoft Store. Run Windows Update afterward, since the app expects current system web components. Sign in and give the first sync several minutes on a stable connection before judging the result.

1. Uninstall Microsoft Loop from Installed apps.
2. Restart your laptop to clear locked files.
3. Reinstall Loop from the Microsoft Store.
4. Run Windows Update, sign in, and let the first sync complete.

## Closing

Loop app failures are client failures, not data failures — your workspaces are safe in the cloud the whole time. In practice the fix is almost always a fresh sign-in, a Store update, an app reset, or a WebView2 reinstall, in that order. If the browser version works but no app repair ever does, check whether a VPN or corporate proxy is filtering Loop's endpoints, since that is the one cause that survives every reinstall. Keep the Store's auto-updates on afterward, and the next Loop update will arrive quietly instead of as another Monday-morning surprise.
