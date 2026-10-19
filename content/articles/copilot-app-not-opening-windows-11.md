---
title: "Copilot App Not Opening on Windows 11? How to Fix It"
slug: copilot-app-not-opening-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: ["copilot app", "windows 11", "app won't open", "copilot troubleshooting", "microsoft copilot"]
description: "Copilot app not opening on Windows 11? Discover why the app won't launch and follow proven steps to get Microsoft Copilot running again."
thumbnail: "/images/thumbs/copilot-app-not-opening-windows-11.webp"
faqs:
  - q: "Why does Copilot open and immediately close?"
    a: >
      This usually means the app's cached data or its WebView runtime is corrupted. The app starts, hits the damaged component, and crashes before the window renders. Clearing the app cache or repairing the WebView2 runtime fixes it in most cases.
  - q: "Is Copilot a separate app or part of Windows 11?"
    a: >
      Microsoft moved Copilot from a built-in sidebar to a standalone app distributed through the Microsoft Store. That is why it can be uninstalled, fail to update, or go missing entirely — it behaves like any other Store app now, with the same failure modes.
  - q: "Do I need a Microsoft account for Copilot to open?"
    a: >
      The app itself should open without one, but signing in unlocks full functionality and sync. If the app refuses to launch until you sign in, that is abnormal — try the repair steps below rather than assuming an account is mandatory.
  - q: "Can a Windows update break the Copilot app?"
    a: >
      Yes. Feature updates sometimes replace the Copilot app package with a stub or leave mismatched versions of its dependencies. If Copilot broke right after an update, reinstalling the app from the Store is the fastest fix.
---

You click the Copilot icon, the cursor spins for a second, and then... nothing. No window, no error message, no sign the app even tried. Or maybe it flashes open and vanishes instantly. Either way, Microsoft's AI assistant is refusing to start, and that shiny Copilot key on your keyboard is suddenly decorative.

Copilot on Windows 11 is now a standalone Store app, which means it inherits all the classic Store-app failure modes: corrupted cache, broken updates, damaged dependencies, and region blocks. The good news is that these are well-understood problems with reliable fixes. If your [Copilot key is not working on your laptop](/articles/copilot-key-not-working-laptop/) either, fixing the app first often resolves both issues at once, since the key simply launches this app.

Work through the fixes below from top to bottom. Start with the quick checks — most people are back up and running by Fix 3.

## Why this happens

- **Corrupted app cache:** Damaged temporary files can crash the app during startup before any window appears.
- **Broken WebView2 runtime:** Copilot renders its interface through Microsoft Edge WebView2. If that runtime is damaged, the app cannot draw its window.
- **Incomplete Store update:** A half-finished update can leave the app package in a broken state that will not launch.
- **Region restriction:** In unsupported regions, the app may install but refuse to open.
- **Conflicting security software:** Overzealous antivirus or firewall rules can block the app's launch or its network calls.
- **Corrupt user profile data:** Damaged per-user app data can prevent launch for one account while the app works fine for another.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Store Apps troubleshooter
Windows has a built-in troubleshooter that detects and repairs common Store app launch failures automatically.

1. Open Settings with Win + I and go to System > Troubleshoot > Other troubleshooters.
2. Find "Windows Store Apps" in the list and click Run.
3. Let the troubleshooter scan. Apply any fixes it recommends.
4. When it finishes, try launching Copilot again.
5. If the troubleshooter reports it could not fix the issue, continue to Fix 2 — you have at least ruled out the simple causes.

### Fix 2: Repair and reset the Copilot app
Windows can repair the app's files without touching your data, and reset it completely if repair is not enough.

1. Open Settings > Apps > Installed apps and find "Microsoft Copilot" in the list.
2. Click the three dots next to it and choose Advanced options.
3. Under the Reset section, first click Repair and wait for the checkmark to appear.
4. Try launching Copilot. If it still will not open, return to the same page and click Reset, then confirm.
5. Launch Copilot again. A reset clears sign-in state, so you may need to sign back in — that is normal.
6. If the app is not listed in Installed apps at all, skip ahead to Fix 4 to reinstall it.

### Fix 3: Reinstall Microsoft Edge WebView2
Copilot's window is rendered by the WebView2 runtime. Reinstalling it fixes a whole class of instant-crash-on-launch problems.

1. Open Settings > Apps > Installed apps and search for "WebView2".
2. If "Microsoft Edge WebView2 Runtime" is listed, click its three dots and uninstall it.
3. Visit the official [Microsoft Support](https://support.microsoft.com/en-us/windows) site and search for the WebView2 runtime download, or get it from Microsoft's developer download page.
4. Install the runtime and restart your laptop when prompted.
5. Try launching Copilot again. If the app now opens, the runtime was the culprit.
6. If Copilot still crashes, the problem lies elsewhere — continue to Fix 4.

### Fix 4: Reinstall Copilot from the Microsoft Store
When repair and reset fail, a clean reinstall replaces every file in the app package.

1. Open Settings > Apps > Installed apps, find Microsoft Copilot, click the three dots, and choose Uninstall. Confirm.
2. Restart your laptop to clear any locked files from the old installation.
3. Open the Microsoft Store, search for "Microsoft Copilot," and install it fresh.
4. Launch Copilot from the Start menu (not the taskbar pin yet) to test.
5. If it opens, right-click the taskbar icon and pin it again for convenience.
6. Still failing? The issue may be account-level — create a new local Windows user account temporarily and test Copilot there to isolate profile corruption.

### Fix 5: Check region availability and network blocks
If you are in a region where Copilot is not offered, or your firewall blocks its endpoints, the app may refuse to open silently.

1. Check Microsoft's documentation for the current list of regions where Copilot is available.
2. If your region is unsupported, the app may never open properly — see our guide on [Copilot not available in your region](/articles/copilot-not-available-in-my-region/) for workarounds.
3. Temporarily disable any third-party antivirus or firewall and try launching Copilot. If it opens, add Copilot as an allowed app in that software's settings.
4. Try a different network (phone hotspot, for example) to rule out ISP or corporate network blocking.
5. If the app opens on another network, the block is network-level — check your router or VPN settings.

### Fix 6: Update Windows and check system file health
A damaged system component underneath the app can prevent any Store app from launching correctly.

1. Open Settings > Windows Update and install all pending updates, then restart.
2. After restarting, open Command Prompt as administrator (search "cmd", right-click, Run as administrator).
3. Run `sfc /scannow` and wait for it to complete. This repairs protected system files.
4. If SFC found and fixed errors, restart once more and test Copilot.
5. As a deeper check, run `DISM /Online /Cleanup-Image /RestoreHealth` in the same admin prompt, then restart and test again.
6. If Copilot still will not open after all of this, check whether the [Copilot app is crashing](/articles/copilot-app-crashing/) with a visible error — that guide covers the next layer of diagnostics.

## Closing

A Copilot app that will not open is annoying, but it is rarely mysterious — corrupted cache, a broken WebView2 runtime, or a bad update covers nearly every case. The repair-reset-reinstall ladder above resolves the large majority of them. If the app opens for a different Windows user but not for you, your user profile is the problem, and migrating to a fresh profile is cleaner than endless repairs. If the app opens but ignores your questions, see [Copilot not responding](/articles/copilot-not-responding/); and if you would rather the key launched something else entirely, learn how to [remap the Copilot key](/articles/remap-copilot-key-windows-11/).
