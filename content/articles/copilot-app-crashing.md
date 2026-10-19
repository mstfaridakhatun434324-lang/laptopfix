---
title: "Copilot App Crashing on Windows 11? How to Stop It"
slug: copilot-app-crashing
date: 2026-10-19
categories: ["ai-pc"]
tags: ["copilot", "app crash", "windows 11", "copilot troubleshooting", "webview2"]
description: "Copilot app crashing on Windows 11? Learn what makes Copilot crash on launch or mid-chat and follow fixes to stabilize it for good."
thumbnail: "/images/thumbs/copilot-app-crashing.webp"
faqs:
  - q: "Why does Copilot crash as soon as I open it?"
    a: >
      Instant crashes on launch almost always trace to corrupted app data or a damaged WebView2 runtime. The app starts loading, hits the broken component, and Windows terminates it. A reset of the app or a WebView2 reinstall fixes the large majority of these cases.
  - q: "Copilot crashes when I send images. Is that normal?"
    a: >
      No, but it is a known weak spot. Image uploads stress the app's memory handling, and on systems with little free RAM the app can be killed by Windows. Close heavy programs before uploading images, and keep the app updated — Microsoft has patched several image-related crashes.
  - q: "Does reinstalling Copilot delete my chat history?"
    a: >
      Your chat history lives in your Microsoft account in the cloud, not in the local app package. Reinstalling the app does not delete it. You will need to sign in again, after which your history reappears.
  - q: "Can antivirus cause Copilot to crash?"
    a: >
      Yes. Some security suites flag Copilot's WebView processes as suspicious and terminate them mid-run, which looks like a random crash. If crashes started after installing or updating security software, add Copilot as an exclusion and test again.
---

There is a special annoyance to an app that crashes: it works just long enough to give you hope. Copilot opens, you start typing, and then it vanishes. Or it dies the instant you click the icon. Either way, you cannot hold a conversation with software that will not stay open.

Copilot crashes fall into two families. Launch crashes — where the app dies immediately — are almost always corrupted local data or a broken WebView2 runtime. Mid-session crashes, where it dies while you are chatting, usually involve memory pressure, a bad update, or security software killing its processes. If the app will not open at all rather than crashing, our guide on the [Copilot app not opening on Windows 11](/articles/copilot-app-not-opening-windows-11/) is the better starting point. And if it opens but ignores you, see [Copilot not responding](/articles/copilot-not-responding/).

Work through these fixes in order. The early ones are quick; the later ones dig deeper.

## Why this happens

- **Corrupted app cache or user data:** Damaged local files crash the app during startup or when loading a conversation.
- **Broken WebView2 runtime:** Copilot's entire interface runs on WebView2. A damaged runtime means instant death.
- **Bad app update:** A faulty Store update can ship a crashing build; these are usually fixed quickly by the next update.
- **Memory pressure:** With RAM exhausted, Windows kills Copilot's processes to protect the system.
- **Antivirus interference:** Security software can terminate Copilot's renderer processes, appearing as random crashes.
- **GPU driver conflicts:** Because WebView2 uses GPU acceleration, a buggy graphics driver can take the app down with it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check for a Copilot app update
If a bad update caused the crashes, the fix may already be waiting in the Store.

1. Open the Microsoft Store and click Library in the left sidebar.
2. Click "Get updates" and let it check everything.
3. If Copilot has an update, install it and wait for it to finish.
4. Launch Copilot and use it normally for a few minutes to test stability.
5. Also install any pending Windows updates in Settings > Windows Update, since app and OS updates often ship together.
6. If crashes persist on the latest version, the problem is local — continue to Fix 2.

### Fix 2: Repair, then reset the app
Windows can fix damaged app files in place, escalating to a full data wipe if needed.

1. Go to Settings > Apps > Installed apps and find Microsoft Copilot.
2. Click the three dots, choose Advanced options.
3. Click Repair first and wait for the checkmark. Test the app.
4. If it still crashes, return and click Reset, then confirm. This clears all local data.
5. Reopen Copilot and sign in again when prompted.
6. Use it for a while, including the action that used to crash it (sending an image, long chat). If it is stable now, corrupted data was the cause.

### Fix 3: Reinstall the WebView2 runtime
A damaged renderer crashes the app the moment it tries to draw anything complex.

1. In Settings > Apps > Installed apps, find "Microsoft Edge WebView2 Runtime" and uninstall it.
2. Download the latest WebView2 runtime from Microsoft's official download page.
3. Install it and restart your laptop.
4. Launch Copilot and test, especially the scenarios that crashed before.
5. If crashes are gone, the runtime was corrupt. Keep it updated going forward — it updates through Windows Update too.
6. Still crashing? The app package itself may be damaged — move to Fix 4.

### Fix 4: Clean-reinstall the Copilot app
Remove every trace of the app and start from a pristine package.

1. Uninstall Microsoft Copilot from Settings > Apps > Installed apps.
2. Restart the laptop to release any locked files.
3. Open the Microsoft Store, search "Microsoft Copilot," and install it fresh.
4. Before signing in, launch it once to confirm it opens stably.
5. Sign in and restore your normal use. Your chat history syncs back from your account.
6. If a clean install still crashes on first launch, suspect deeper system issues — continue to Fix 5.

### Fix 5: Update GPU drivers and test with hardware acceleration off
Because Copilot renders through WebView2 with GPU acceleration, graphics driver bugs can crash it.

1. Identify your GPU (Task Manager > Performance tab shows it).
2. Download the latest driver from the official source: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html).
3. Install the driver and restart.
4. Test Copilot. If crashes stop, the old graphics driver was the trigger.
5. As a diagnostic, you can also try launching Copilot right after a clean boot (msconfig > selective startup) to see if background software is involved.
6. If crashes only happen with specific content (images, long threads), note the pattern — it helps if you ever report the bug to Microsoft.

### Fix 6: Rule out memory pressure and security software
When Windows is starved of RAM, or antivirus is aggressive, Copilot becomes collateral damage.

1. Open Task Manager during normal use and watch memory. Sustained usage above 90% is a red flag.
2. Close browser tabs and heavy apps, then test Copilot alone.
3. Temporarily disable third-party antivirus and use Copilot for ten minutes. If crashes stop, add Copilot as an exclusion in the antivirus settings.
4. Check Windows Security > Protection history for any blocked Copilot components.
5. If you have less than 8 GB of RAM and crashes happen under load, memory pressure is likely — consider a RAM upgrade as the long-term fix.
6. For persistent, unexplained crashes after all of this, check whether the [Copilot web view is not loading](/articles/copilot-web-view-not-loading/) — the underlying renderer issue may need the deeper treatment there.

## Closing

App crashes feel random, but they follow patterns: launch crashes mean corrupt data or a broken runtime, mid-chat crashes mean memory or interference. The repair-reset-reinstall ladder plus a WebView2 refresh resolves the overwhelming majority. If Copilot crashes identically on a brand-new Windows user profile too, you are likely looking at a bad GPU driver or a genuinely buggy app build — update the former, and wait out the latter. If the app is not crashing but missing entirely, see [Copilot missing on your Copilot+ PC](/articles/copilot-missing-on-copilot-plus-pc/) for the restore steps.
