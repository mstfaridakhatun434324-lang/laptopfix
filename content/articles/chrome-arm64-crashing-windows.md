---
title: "How to Fix Chrome ARM64 Crashing on Windows"
slug: chrome-arm64-crashing-windows
date: 2026-10-20
categories: ["ai-pc"]
tags: ["chrome arm64", "chrome crashing", "windows 11 arm", "troubleshooting", "ai pc", "snapdragon laptop"]
description: "Chrome keeps crashing on your ARM laptop? Fix Chrome ARM64 crashes, freezes, and tab failures on Windows 11 with these troubleshooting steps that work."
thumbnail: "/images/thumbs/chrome-arm64-crashing-windows.webp"
faqs:
  - q: "Is there a native ARM64 version of Chrome for Windows?"
    a: 'Yes. Google ships a native ARM64 build of Chrome for Windows 11 on ARM, covering Snapdragon X, Intel Lunar Lake, and AMD Ryzen AI laptops. It downloads automatically from the official Chrome site on an ARM64 system. If Chrome crashes constantly, you may be running the emulated x64 build instead.'
  - q: "Why does Chrome crash on startup on my Snapdragon laptop?"
    a: 'Startup crashes are usually caused by a corrupted user profile, a misbehaving extension, or an outdated Chrome build — not the ARM chip itself. Renaming the profile folder forces Chrome to build a fresh one, which resolves most startup crashes. Hardware acceleration conflicts with the graphics driver are the next most common cause.'
  - q: "Do Chrome extensions work on ARM64 Chrome?"
    a: 'Yes. Chrome extensions are written in JavaScript and run identically on ARM64 and x64 builds. An extension can still crash tabs if it is buggy or outdated, so test with extensions disabled when diagnosing crashes. Native ARM64 Chrome handles extensions just as reliably as the Intel version.'
  - q: "Should I switch to Edge on my ARM laptop instead?"
    a: 'Microsoft Edge is also native ARM64 and well optimized for Snapdragon laptops, so it is a solid fallback while you fix Chrome. That said, native Chrome runs just as well once profile corruption or a bad extension is resolved. Fix the underlying issue rather than abandoning your synced bookmarks and passwords.'
---

Chrome crashing repeatedly is miserable on any laptop, but on a new ARM machine it feels especially wrong. Snapdragon X, Intel Lunar Lake, and AMD Ryzen AI laptops are fast and efficient, and Google ships a native ARM64 build of Chrome for Windows 11 on ARM. The browser should be rock solid.

When it is not — startup crashes, "Aw, Snap!" tab deaths, or full-window freezes — the cause is almost never the ARM processor. It is usually a corrupted profile, a rogue extension, the emulated x64 build, or a graphics driver conflict.

This guide walks you through diagnosis first, then the fixes in order. Work from the top until Chrome is stable.

## Why this happens

- **Emulated x64 Chrome build:** the x64 build running under emulation crashes more often and runs slower than native ARM64 Chrome.
- **Corrupted user profile:** a damaged profile folder causes startup crashes and tab failures that survive reinstalls.
- **Buggy or outdated extension:** one bad extension can take down every tab, especially ad blockers and password managers hooking page loads.
- **Hardware acceleration conflict:** Chrome's GPU rendering can clash with ARM graphics drivers, freezing the browser or killing tabs.
- **Outdated Chrome build:** Google fixes ARM-specific crash bugs regularly; an old build may contain a bug fixed months ago.
- **Overloaded memory:** dozens of tabs plus heavy web apps can exhaust RAM, and Chrome kills tabs to protect the system.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install native ARM64 Chrome

Chrome must be the native ARM64 build — the emulated x64 version is slower and crash-prone, as with [Adobe Photoshop on ARM laptops](/articles/adobe-photoshop-arm-laptop-issues/) and [DaVinci Resolve on ARM Windows laptops](/articles/davinci-resolve-arm-windows-laptop/). You may have the wrong build from an old offline installer. Verify it first. Every later fix assumes the native build.

1. In Chrome, open the three-dot menu > Help > About Google Chrome.
2. Check whether the build identifies as ARM64 in the version details.
3. If it is x64, uninstall Chrome from Settings > Apps (keep your data if prompted).
4. Download a fresh installer from Google's Chrome site on the laptop itself.
5. Reinstall and confirm About Chrome shows the ARM64 build.

### Fix 2: Test with a clean profile

A corrupted profile is the most common cause of Chrome crashing on startup. Profiles get damaged by forced shutdowns or interrupted updates. Reinstalling Chrome does not fix it because the profile folder survives uninstalls.

1. Close Chrome completely, including background processes in Task Manager.
2. Press Win + R, type `%LOCALAPPDATA%\Google\Chrome\User Data`, and press Enter.
3. Rename the `Default` folder to `Default-Backup`.
4. Launch Chrome and test for several minutes with the fresh profile.
5. If stable, sign in to sync to restore bookmarks, or copy files from the backup selectively.

### Fix 3: Disable extensions and hardware acceleration

Extensions and GPU rendering are the two biggest runtime crash sources after the profile. A single outdated extension can crash every tab, while hardware acceleration conflicts with some ARM graphics drivers cause full-browser freezes. Disabling both is a quick test that splits the problem in half. If Chrome stabilizes, re-enable items one at a time to find the culprit.

1. Open `chrome://extensions` and toggle off every extension.
2. Go to Settings > System and turn off "Use hardware acceleration when available".
3. Restart Chrome and browse normally for a while.
4. If stable, re-enable extensions one by one, testing between each.
5. Leave hardware acceleration off if freezes return when it is enabled.

### Fix 4: Update Chrome, Windows, and graphics drivers

Google ships ARM-specific stability fixes in nearly every Chrome release, and Windows 11 updates include platform fixes Chrome depends on. Running old versions leaves known crash bugs on the table. Graphics drivers matter too, since Chrome leans on the GPU for rendering — and our guide on [how to check NPU TOPS in Windows 11](/articles/how-to-check-npu-tops-windows-11/) helps confirm your AI-PC driver stack is healthy overall. Check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update seems stuck, and see [Microsoft support](https://support.microsoft.com/en-us/windows) for update troubleshooting steps.

1. In Chrome, go to Help > About Google Chrome and let it update, then relaunch.
2. Open Settings > Windows Update and install all pending updates.
3. Update the graphics driver from your laptop maker's support page.
4. Restart the laptop after all updates complete.
5. Test Chrome with your normal tabs and extensions.

### Fix 5: Reduce memory pressure

Chrome is famously hungry for RAM, and with many tabs open it can exhaust memory, killing tabs to protect the system. ARM laptops often ship with 16 GB, which is plenty normally but not for a hundred tabs plus web apps. Chrome's built-in memory saver helps, but closing what you do not need helps more. This is worth checking before assuming a deeper problem, especially if crashes happen only with many tabs open.

1. Open Task Manager (Shift + Esc inside Chrome) and sort by memory.
2. Close the heaviest tabs and extensions you are not actively using.
3. In Settings > Performance, make sure Memory Saver is on.
4. Add your most important sites to the "Always keep these sites active" list.
5. Restart Chrome and confirm tab crashes have stopped.

### Fix 6: Reset Chrome settings as a last resort

When nothing else explains the crashes, corrupted settings or policies may be at fault. The built-in reset restores defaults while keeping bookmarks, history, and passwords. That makes it safer than a full reinstall. If crashes persist on a clean profile after a reset, the cause is likely system-level — a deeper Windows or driver problem.

1. Go to Settings > Reset settings > Restore settings to their original defaults.
2. Confirm the reset and wait for Chrome to restart.
3. Test with a few tabs before reinstalling any extensions.
4. Reinstall extensions one at a time from the Web Store.
5. If crashes continue, compare behavior in Edge to isolate a Chrome-specific versus system issue.

## Closing

Chrome crashes on ARM laptops are rarely about the chip — they come from the wrong build, a corrupted profile, a bad extension, or a driver conflict. Work through the native-build check, profile reset, and extension triage, and Chrome should be as stable as on any Intel machine. If you are comparing hardware while troubleshooting, our [Intel Lunar Lake vs AMD Strix Point](/articles/intel-lunar-lake-vs-amd-strix-point/) breakdown covers how the different AI-PC chips handle everyday software.
