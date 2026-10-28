---
title: "How to Fix the Dell Pro 14 AI Copilot App Crashing on Your Laptop"
slug: dell-pro-14-ai-copilot-app-crashes
date: 2026-10-28
categories: ["ai-pc"]
tags: ["Dell Pro 14", "Copilot app", "crashing", "AI laptop", "Windows 11"]
description: "Copilot keeps crashing on your Dell Pro 14 AI? Learn why the app closes on launch and how to make it stable again step by step. Do it now. Fix it today."
thumbnail: "/images/thumbs/dell-pro-14-ai-copilot-app-crashes.webp"
faqs:
  - q: "Why does the Copilot app crash on my Dell Pro 14 AI?"
    a: >
      The usual causes are a corrupted app install, a failed update, a sign-in problem, a conflicting service, or a system component that Copilot depends on being broken.
  - q: "Is the crash caused by the Dell hardware?"
    a: >
      Almost never. Copilot crashes are software problems — app data, updates, or Windows components — and they are fixable without touching the hardware.
  - q: "Will reinstalling Copilot delete my chats?"
    a: >
      Copilot chats are tied to your Microsoft account and stored online, so reinstalling the app does not delete your conversation history.
  - q: "Can I use Copilot in the browser while the app is broken?"
    a: >
      Yes. Copilot on the web offers the same AI chat while you fix the app, so you lose no functionality during troubleshooting.
---

Copilot crashing on launch is a special kind of annoyance: you click the icon, the window flashes, and then it is gone — or it opens, lets you type one message, and closes without warning. On the Dell Pro 14 AI, where Copilot is meant to be a core part of the experience, a crashing app feels like a core feature has been taken away. The good news is that the hardware is almost never involved; Copilot crashes are app and system problems, and they follow a predictable fix order.

The crash usually comes from one of a few sources: corrupted app data after a failed update, a sign-in token that has gone stale, a Windows component that Copilot depends on being damaged, or a conflicting background service. Each has a fix, and working through them in order — repair, reset, reinstall, then system repair — restores the app in most cases.

This guide takes you through that order, with a browser workaround so you can keep using Copilot while you fix the app.

## Why this happens

- **Corrupted app data:** A failed or interrupted Copilot update can leave app data in a state that crashes the app on every launch.
- **Stale sign-in token:** An expired or invalid Microsoft account token can crash Copilot during its startup sign-in check.
- **Missing Windows component:** Copilot depends on WebView2 and other Windows components, and a damaged component can crash the app.
- **Conflicting background service:** Security software, a VPN, or a proxy can block Copilot's startup network check and cause a crash.
- **Outdated app version:** An old Copilot build may be incompatible with a newer Windows build, crashing on launch.
- **Corrupt user profile data:** A damaged user profile or app cache can make Copilot crash for one user while it works for another.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the browser workaround and confirm the service is up

First, confirm Copilot itself is working, so you know the problem is the app, not the service.

1. Open a browser and sign into Copilot on the web to confirm your account and the service work.
2. Note whether the app crashes instantly on launch, after a delay, or when you send a message, since the timing points to different causes.
3. Try launching Copilot from the Start menu, the taskbar, and the Copilot key separately to see whether the crash follows all launch methods.
4. If the web version works but every app launch crashes, the app installation or its local data is the problem.
5. Keep using the web version while you apply the fixes below.

### Fix 2: Repair and reset the Copilot app

Repair and reset are the fastest app-level fixes and they preserve nothing you need to worry about.

1. Open Settings, go to Apps, then Installed apps, and find Microsoft Copilot.
2. Click Advanced options, then Repair, and test the app.
3. If repair does not help, return to Advanced options and click Reset, which clears local app data.
4. Launch Copilot after reset and sign in again with your Microsoft account.
5. If the app still crashes, move to a full reinstall rather than repeating repair.

A similar repair-first fix resolves [Notepad Rewrite greyed out](/articles/notepad-rewrite-ai-feature-greyed-out/) when an AI feature's app data is stale, and the same logic applies when [VirtualBox guests crash](/articles/virtualbox-arm64-guest-crashes-windows-11/) because a component is corrupted. For a related app check, see [Automatic1111 install problems](/articles/automatic1111-arm-windows-install-fix/).

### Fix 3: Reinstall Copilot and update WebView2

A clean reinstall removes corrupted files that repair cannot reach, and WebView2 is Copilot's rendering engine.

1. Open Settings, go to Apps, then Installed apps, find Microsoft Copilot, and uninstall it.
2. Restart the laptop, then reinstall Copilot from the Microsoft Store.
3. Check the Microsoft Store for a WebView2 Runtime update and install it if offered.
4. Alternatively, download the WebView2 Runtime from Microsoft's official site and install it.
5. Launch Copilot and sign in, testing it for several minutes before declaring it fixed.

### Fix 4: Check sign-in, network, and security software

Sign-in and network blocks can crash Copilot during its startup check.

1. Sign out of your Microsoft account in Windows Settings and sign back in to refresh the account token.
2. Temporarily disable your VPN or proxy and test Copilot, since network interception can break its startup check.
3. Check your security software for a Copilot or WebView2 block, and add an exception if one exists.
4. Test Copilot on a different network, such as a phone hotspot, to rule out a network-level block.
5. If Copilot works on another network, the problem is your network's filtering, not the laptop.

### Fix 5: Update Windows and Dell drivers

System-level incompatibilities between an old app build and a new Windows build cause crashes too.

1. Open Windows Update and install all available updates, including optional driver updates.
2. Visit the official Dell support site for the Pro 14 AI and install the latest chipset and system drivers.
3. Restart and launch Copilot, testing it for several minutes.
4. If a recent Windows update started the crashes, check for a newer Copilot update in the Store that fixes the incompatibility.
5. Keep both Windows and Copilot current, since their versions are designed to move together.

### Fix 6: Test a new user profile and repair Windows

If Copilot crashes for one user but works for another, the user profile is the problem.

1. Create a new local user account and sign into it, then launch Copilot there.
2. If Copilot works in the new profile, your original profile's app data is corrupt, and migrating to a new profile is the cleanest fix.
3. If Copilot crashes in every profile, run the System File Checker from an administrator Command Prompt to repair system components.
4. Check Microsoft's official Copilot troubleshooting guidance at [Microsoft Support](https://support.microsoft.com/en-us/windows) for further steps.
5. If system repair does not help, a Windows repair install using Windows Update preserves your files while refreshing system components.

## Closing

Copilot crashing on the Dell Pro 14 AI is a software problem with a clear fix order: repair, reset, reinstall, then check sign-in and system components. Most crashes end at the repair or reinstall step, and the browser version keeps you working in the meantime. If the app crashes in every user profile after a system repair, a Windows repair install is the final step — and it almost always ends the crashing for good.
