---
title: "How to Fix Widgets Board Not Working on Windows 11"
slug: widgets-board-not-working-windows-11
date: 2026-10-24
categories: ["ai-pc"]
tags: ["widgets-board", "windows-11", "taskbar-widgets", "troubleshooting", "blank-widgets"]
description: "Widgets board on Windows 11 opening blank, crashing, or missing? This step-by-step guide covers the settings, cache, and repair fixes that restore it."
thumbnail: "/images/thumbs/widgets-board-not-working-windows-11.webp"
faqs:
  - q: "Why does my Widgets board open blank on Windows 11?"
    a: >
      A blank Widgets board is most often caused by the Windows Web Experience Pack failing to load, a broken Microsoft account sign-in, or a disabled Widgets feed in settings. Updating the Web Experience Pack from the Microsoft Store and re-signing into your Microsoft account fixes the majority of cases. A corrupted icon cache or a regional feed issue can also cause it.
  - q: "How do I restart the Widgets service on Windows 11?"
    a: >
      There is no standalone Widgets service to restart; Widgets runs as part of Explorer.exe and the Windows Web Experience Pack. The practical reset is to kill Widgets.exe (if running) and restart Windows Explorer from Task Manager, or sign out and back in. You can also reinstall the Windows Web Experience Pack from the Microsoft Store library.
  - q: "Widgets button is missing from my taskbar — how do I bring it back?"
    a: >
      Right-click the taskbar, choose Taskbar settings, and turn Widgets on. If the toggle is missing or greyed out, check that Windows 11 build 22000.739 or later is installed and that your group policy or MDM policy does not hide it. On some work laptops, IT policy disables Widgets entirely.
  - q: "Do Widgets work without a Microsoft account?"
    a: >
      No. The personalized feed in the Widgets board requires signing in with a Microsoft account. The board may open but stay empty or show an error without one. Sign in under Settings > Accounts > Your info, or use the sign-in prompt inside the Widgets board itself.
---

You press Win + W or hover over that little taskbar corner, expecting your weather, calendar, news, and sports scores — and instead you get a blank panel, a board that refuses to open, or widgets showing yesterday's weather. It's a Windows 11 annoyance that isn't fatal but wears on you every day, because the Widgets board is supposed to be a quick glance, not a troubleshooting project.

The Widgets board isn't a standalone app. It runs on the Windows Web Experience Pack — a Microsoft Store component that renders web content inside a native shell, fed by your Microsoft account, region, and a background feed service. When any layer breaks, the board opens empty, freezes, or won't appear at all.

Work through the fixes below in order, from quick checks to deeper repairs. If you notice other odd behavior, the same methodical approach works for problems like [Copilot PC settings search failing to respond](/articles/copilot-pc-settings-search-not-working/) or [RTX Video Super Resolution not working](/articles/rtx-video-super-resolution-not-working/) — diagnose the layer, then act. If you use Copilot's camera features, you may also hit [Copilot Vision problems](/articles/copilot-vision-not-working-windows/) which respond to a similar account-and-settings reset.

## Why this happens

- **Broken Web Experience Pack:** The Windows Web Experience Pack renders the board. A corrupted or outdated install leaves you with a blank or crashing panel.
- **Signed out or stale Microsoft account:** The personalized feed requires an active Microsoft account sign-in. A stale token produces an empty board.
- **Widgets disabled in taskbar settings:** The taskbar toggle can be switched off by an update, a tweak tool, or group policy without you realizing it.
- **Feed or region mismatch:** Your Microsoft account region and Windows region disagreeing can block the news and weather feed from loading.
- **Corrupted Widgets cache:** Cached feed data can get into a state where the board loads the cache, fails to parse it, and never tries the network.
- **Group policy or IT restriction:** Work and school PCs often have Widgets disabled by policy — the toggle simply won't exist for you.
- **Edge WebView2 problems:** The board renders through WebView2. A broken WebView2 runtime breaks the whole board.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the taskbar toggle and sign-in state

Before anything else, confirm Widgets is actually enabled and you're signed in. Right-click the taskbar, select Taskbar settings, and make sure Widgets is turned on. Then open Settings > Accounts > Your info and verify you're signed in with a Microsoft account — a local account or pending identity verification is a classic blank-board cause.

1. Right-click the taskbar and open **Taskbar settings**.
2. Set the **Widgets** toggle to On.
3. Open Settings > Accounts > Your info and confirm a Microsoft account sign-in.
4. Complete any pending identity verification, then press Win + W to test.

### Fix 2: Update the Windows Web Experience Pack

The board's rendering engine lives in a Store component that updates separately from Windows. Open the Microsoft Store, go to Library, and check for updates — if the Windows Web Experience Pack is pending, install it. A version mismatch after a feature update is one of the most common causes of a blank board.

1. Open the **Microsoft Store** app.
2. Click **Library** in the left sidebar, then **Get updates**.
3. Restart your PC once the update completes.
4. Open the Widgets board and confirm it renders.

### Fix 3: Restart Explorer and clear the Widgets cache

If the pack is current, the next layer is runtime state. Restarting Windows Explorer flushes the Widgets host process, and clearing the Web Experience Pack's cache forces a fresh feed pull. Do this after any setting change — cached state is stubborn.

1. Press Ctrl + Shift + Esc to open **Task Manager**.
2. Right-click **Windows Explorer** and choose **Restart** (the taskbar will blink — normal).
3. Press Win + R, type `%LOCALAPPDATA%\Microsoft\Windows\WebCache` and delete its contents.
4. Open the Widgets board to test.

### Fix 4: Repair or reset the Web Experience Pack

When restarts don't help, the component itself may be damaged. Windows lets you repair or reset Store apps without reinstalling the OS. Repair keeps your data; reset clears it. Try repair first, then reset.

1. Open Settings > Apps > **Installed apps** and search for **Windows Web Experience Pack**.
2. Click the three dots and choose **Advanced options**.
3. Click **Repair**, wait, and test the board.
4. If it still fails, return and click **Reset**, then test again.

### Fix 5: Check region, feed, and WebView2

Feed loading depends on your region agreeing across the board, and on the WebView2 runtime being healthy. Open Settings > Time & language > Language & region and make sure your region matches your Microsoft account's region. Then install or repair the Microsoft Edge WebView2 Runtime — the board shares it with many Microsoft apps. The runtime download is linked from [Microsoft's support hub](https://support.microsoft.com/en-us/windows), and keeping Windows current via [the official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) resolves update-related feed breaks.

1. Open Settings > Time & language > **Language & region** and set your region correctly.
2. Install or repair the **Microsoft Edge WebView2 Runtime**.
3. Make sure Windows 11 is on a recent build (Settings > Windows Update).
4. Sign out of Windows and sign back in, then open the board.

### Fix 6: Rule out policy and third-party interference

If the Widgets toggle is missing from taskbar settings entirely, a policy is likely hiding it. On Pro, check gpedit: Computer Configuration > Administrative Templates > Windows Components > Widgets — "Allow widgets" should be Not configured or Enabled. Also temporarily disable third-party taskbar tweakers (Start11, ExplorerPatcher, windhawk mods), which are notorious for breaking the board.

1. On Pro, open gpedit.msc and check the **Widgets** policy state.
2. On Home, check `HKLM\SOFTWARE\Policies\Microsoft\Dsh` — remove `AllowNewsAndInterests` if set to 0.
3. Close any taskbar customization tools and restart Explorer.
4. Re-check whether the Widgets toggle reappears in Taskbar settings.

## Closing

A dead Widgets board is almost always one of three things: the Web Experience Pack is stale or broken, your Microsoft account sign-in has gone stale, or a policy or tweak tool is standing in the way. Fix 2 and Fix 3 resolve the vast majority of reports in under ten minutes. If the board still fails after the policy check, run System File Checker — or use the in-place upgrade from the official Windows 11 media to repair the OS while keeping files and apps.
