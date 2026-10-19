---
title: "Copilot Web View Not Loading? Fix It in Minutes"
slug: copilot-web-view-not-loading
date: 2026-10-19
categories: ["ai-pc"]
tags: ["copilot", "webview2", "blank screen", "windows 11", "copilot troubleshooting"]
description: "Copilot web view not loading or showing a blank screen? Learn why Copilot's interface fails to render and how to fix it step by step."
thumbnail: "/images/thumbs/copilot-web-view-not-loading.webp"
faqs:
  - q: "Why is my Copilot window blank or white?"
    a: >
      The Copilot app draws its interface using Microsoft Edge WebView2. If that runtime is missing, outdated, or corrupted, the app opens an empty window because it cannot render any content. Reinstalling WebView2 is the definitive fix.
  - q: "Copilot shows a loading spinner forever. What does that mean?"
    a: >
      An endless spinner means the web view loaded but cannot reach Copilot's servers. This is a connectivity or sign-in problem rather than a rendering problem — check your network, VPN, and account sign-in state.
  - q: "Does this affect the Copilot website too?"
    a: >
      No. The website runs in your full browser, which has its own rendering engine. If copilot.microsoft.com works in Edge or Chrome but the app shows a blank window, the problem is isolated to the app's WebView2 runtime.
  - q: "Will reinstalling Edge fix the WebView2 issue?"
    a: >
      Not necessarily. The WebView2 runtime is a separate component from the Edge browser, even though they share technology. You need to reinstall the WebView2 runtime specifically, not just the Edge browser.
---

Copilot opens, but the window is empty — a blank white or gray rectangle where the chat interface should be. Or it shows a loading spinner that never resolves. The app is technically running, but its "web view," the embedded browser that renders everything you see, has failed.

Understanding this architecture makes the fix obvious. The Copilot app is essentially a wrapper around Microsoft Edge's WebView2 component. When WebView2 breaks, Copilot cannot draw its interface at all. This is distinct from the app not opening (covered in our [Copilot app not opening on Windows 11](/articles/copilot-app-not-opening-windows-11/) guide) and from the app ignoring input (see [Copilot not responding](/articles/copilot-not-responding/)). Here, the window exists but the content never arrives. One quick tell: if you can still interact with the window frame — resize it, minimize it — but the inside stays empty, the app shell is healthy and only the renderer has failed.

The fixes below target the rendering pipeline directly.

## Why this happens

- **Missing WebView2 runtime:** Some stripped or custom Windows installs lack the runtime entirely.
- **Corrupted WebView2 installation:** Damaged runtime files render nothing, producing the blank window.
- **Outdated runtime version:** An old WebView2 can be incompatible with the current Copilot app build.
- **GPU rendering failure:** WebView2 uses GPU acceleration; a broken graphics driver can blank the view.
- **Blocked local web traffic:** Overzealous firewalls can block the local loopback traffic the web view uses internally.
- **Corrupt app data:** Damaged Copilot cache can prevent the web view from initializing its session.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is a rendering problem, not a network problem
The treatment differs, so diagnose correctly first.

1. Open Edge or Chrome and go to copilot.microsoft.com. If it works there, rendering in your browser is fine.
2. In the Copilot app, watch carefully: a pure white/blank window means rendering failure; an endless spinner means network failure.
3. For spinner-forever cases, check your internet, disable VPN, and re-sign in — then return here only if the window is truly blank.
4. If the window is blank white, continue to Fix 2 — WebView2 is the prime suspect.
5. Note which one you have before proceeding; it saves wasted steps.

### Fix 2: Reinstall the WebView2 runtime
This is the fix that resolves most blank-window cases.

1. Open Settings > Apps > Installed apps and search for "WebView2."
2. Uninstall "Microsoft Edge WebView2 Runtime."
3. Download the latest runtime from Microsoft's official WebView2 download page. Choose the evergreen standalone installer so the runtime keeps itself updated afterward.
4. Install it, choosing the option for all users if offered. The installer registers the runtime system-wide, which is what the Copilot app expects.
5. Restart your laptop to ensure every component reloads cleanly. A restart matters here because a damaged runtime can leave zombie processes holding old files.
6. Open Copilot. If the interface now renders, the runtime was corrupt. To confirm the diagnosis for the future, note the runtime version in Settings > Apps — if the blank window ever returns, an outdated or re-corrupted runtime is the first thing to check.

### Fix 3: Repair the Copilot app's data
Corrupt app data can stop the web view from initializing even with a healthy runtime.

1. Go to Settings > Apps > Installed apps > Microsoft Copilot > Advanced options.
2. Click Repair, wait for the checkmark, and test Copilot.
3. If still blank, click Reset on the same page and confirm.
4. Reopen Copilot and sign in again.
5. If the web view loads after reset, the app's stored session data was the blocker.
6. Persistent blankness after both runtime reinstall and app reset points to graphics — continue to Fix 4.

### Fix 4: Update the GPU driver
WebView2 leans on GPU acceleration to render. A buggy graphics driver can silently blank it.

1. Open Task Manager > Performance to identify your GPU.
2. Get the latest driver from the official source: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html).
3. Install the driver and restart.
4. Open Copilot and check whether content renders now.
5. As a diagnostic alternative, you can test with hardware acceleration disabled in Edge's settings to see if the GPU path is implicated — but the driver update is the real fix.
6. If a recent GPU driver update coincided with the problem starting, roll the driver back instead.

### Fix 5: Check firewall and loopback blocking
The web view communicates over local loopback addresses, which some firewalls block.

1. Temporarily disable any third-party firewall or "internet security" suite.
2. Open Copilot and see if the interface loads.
3. If it does, re-enable the firewall and add exclusions for Copilot and WebView2 processes.
4. Check Windows Defender Firewall too: search "Allow an app through firewall" and ensure Copilot-related entries are permitted on private networks.
5. Corporate devices with strict firewall policies may need an IT exception — test on a personal network to confirm the diagnosis.
6. VPNs with aggressive filtering can also interfere; disconnect and test as in Fix 1's network check.

### Fix 6: Clean-reinstall Copilot as a last resort
When the runtime is fresh, the driver is current, and the app still shows nothing, replace the whole app package.

1. Uninstall Microsoft Copilot from Settings > Apps > Installed apps.
2. Restart the laptop.
3. Reinstall Copilot from the Microsoft Store.
4. Launch it before signing in to confirm the interface renders.
5. Sign in and test a full conversation.
6. If even a clean install shows a blank window with a fresh runtime and current GPU driver, check whether the [Copilot key opens the wrong app](/articles/copilot-key-opens-wrong-app/) — a misconfigured launch target can occasionally produce similar symptoms — or consider that a Windows feature update may be needed for compatibility.

## Closing

A blank Copilot window is the WebView2 runtime crying for help. Reinstalling that runtime fixes the clear majority of cases; the GPU driver covers most of the rest. The key insight is the architecture: Copilot is a web view in a wrapper, so when the screen is empty, always suspect the renderer before the app. Once content renders again, the assistant is back in business. If the key that launches Copilot starts opening the wrong program, see [why the Copilot key opens the wrong app](/articles/copilot-key-opens-wrong-app/). And if you decide the app is more trouble than it is worth, our guide on [uninstalling Copilot on Windows 11](/articles/uninstall-copilot-windows-11/) removes it cleanly.
