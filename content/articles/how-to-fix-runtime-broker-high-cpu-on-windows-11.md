---
title: "Runtime Broker High CPU on Windows 11? What's Normal and What's Not"
slug: how-to-fix-runtime-broker-high-cpu-on-windows-11
date: 2026-09-02
categories: ["performance"]
tags: ["runtime broker", "high cpu", "windows 11", "uwp apps", "task manager"]
description: "RuntimeBroker.exe spiking CPU on Windows 11? Learn what this system process does, when its CPU use is normal, and how to fix it when it isn't."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-on-windows-11.webp"
faqs:
  - q: "What does Runtime Broker actually do?"
    a: "Runtime Broker (RuntimeBroker.exe) is a system process that manages permissions for Microsoft Store (UWP) apps — it brokers their access to your camera, microphone, location, files, and notifications. When you launch a Store app, Runtime Broker checks its declared permissions and enforces them. Brief CPU spikes when opening such apps are completely normal; sustained high CPU is not."
  - q: "Why are there multiple Runtime Broker processes running?"
    a: "Windows runs one Runtime Broker instance per user session plus additional instances for specific app groups — seeing two to four copies in Task Manager is normal on Windows 11. Worry only if one specific instance sustains high CPU (say, above 15%) for many minutes while you're not actively using Store apps."
  - q: "Can I disable Runtime Broker?"
    a: "No — it's a core Windows component, and disabling or deleting it breaks Microsoft Store apps, the Start menu, Settings, and parts of the shell that rely on permission brokering. The correct approach is finding which app is making Runtime Broker work overtime and fixing or removing that app, not attacking the broker itself."
  - q: "Is RuntimeBroker.exe ever malware?"
    a: "Rarely, but impersonation happens. The legitimate file is C:\\Windows\\System32\\RuntimeBroker.exe, signed by Microsoft, typically using 0% CPU at idle. Verify via Task Manager > Details > Open file location. A RuntimeBroker.exe running from anywhere else — especially a Temp or AppData folder — should be treated as malware and scanned immediately."
---

`RuntimeBroker.exe` at 25% CPU in Task Manager triggers immediate suspicion — the name sounds like bloatware, and forums are full of "just disable it" advice. Don't. Runtime Broker is a legitimate, necessary Windows process that manages permissions for Store apps. The real question isn't "how do I kill it" but "which app is making it work so hard" — because sustained high CPU from Runtime Broker always traces back to a misbehaving app.

Normal behavior: brief spikes to 10–30% when launching Store apps (Photos, Settings, Xbox app), settling to zero within seconds. Abnormal: one instance pinned above 15% for many minutes, or constant activity with no Store apps open. This guide shows how to tell the difference and fix the abnormal cases. For the broader CPU-hog landscape, see [taming SearchApp.exe](/articles/best-way-to-fix-searchapp-exe-high-cpu/); for another common broker-adjacent process, [fixing CompatTelRunner](/articles/best-way-to-fix-compattelrunner-high-cpu/).

## Why this happens

- **A Store app stuck requesting permissions**: An app repeatedly asking for location, camera, or file access keeps the broker arbitrating.
- **Photos app background indexing**: The Photos app's indexing and face-recognition passes generate sustained broker activity.
- **Live tiles / widgets polling**: News, weather, and widget content refreshing through brokered permissions.
- **Corrupt Store app**: A damaged app package throwing repeated permission errors the broker must handle.
- **Tips / "suggested content" features**: Windows' tips, suggestions, and Spotlight content polling in the background.
- **Too many brokered background apps**: Dozens of Store apps all allowed to run background tasks multiply broker load.
- **Malware impersonating the process**: Rare, but a fake RuntimeBroker.exe from a non-system location burns CPU while doing something else entirely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which app is driving the broker

Find the client before blaming the broker.

1. In Task Manager > **Details**, note which **RuntimeBroker.exe** instance has high CPU — right-click > **Analyze wait chain** to see what it's waiting on.
2. Open **Settings** > **Apps** > **Installed apps** and sort by recent activity mentally: which Store apps have you used today? Photos, Xbox Game Bar, Your Phone/Phone Link, and third-party Store apps are the usual drivers.
3. Close Store apps one by one (fully quit from the tray or Task Manager) and watch the broker instance — when CPU drops, you've found the client app.
4. Check **Settings** > **Privacy & security** > **App permissions** (Location, Camera, Microphone): an app with permission that's constantly polling (a weather app hammering location) is a prime suspect.
5. Verify legitimacy first: right-click the busy instance > **Open file location** — must be `C:\Windows\System32`. If it's elsewhere, stop here and run a full Defender scan.

### Fix 2: Tame the Photos app

The single most common Runtime Broker driver.

1. Open **Photos** > **Settings** (gear icon) — turn off **People** (face grouping) if you don't use it; its background analysis is broker-intensive.
2. In Photos settings, check for options about OneDrive/iCloud integration — disable auto-indexing of cloud libraries you don't browse in Photos.
3. **Settings** > **Apps** > **Installed apps** > **Microsoft Photos** > **Advanced options** > **Background apps permissions** > set to **Never** if you don't need Photos doing background work.
4. Still in Advanced options: use **Repair** first, then **Reset** if CPU persists — a corrupt Photos database causes endless brokered retry loops.
5. If you rarely use Photos, consider setting a different default image viewer and leaving Photos' background permissions off permanently.

### Fix 3: Quiet live content and suggestions

Stop Windows' background chatter.

1. **Settings** > **Personalization** > **Start** — turn off **Show suggestions**, **Show recently added apps**, and similar content feeds that poll through the broker.
2. **Settings** > **Privacy & security** > **General** — turn off **Let apps show me personalized ads**, **Show me suggested content in the Settings app**, and **Get tips and suggestions**.
3. For widgets: **Settings** > **Personalization** > **Taskbar** > toggle **Widgets** off if you don't use the board — its news/weather polling is broker-mediated. (Dedicated widget issues: [Widgets.exe high CPU](/articles/best-way-to-fix-widgets-board-high-cpu-windows-11/).)
4. **Settings** > **System** > **Notifications** — disable notifications for apps you don't care about; each notification passes through brokered channels.
5. Restart and observe for an hour — suggestion/tip polling is a slow burn, so the improvement shows over time, not instantly.

### Fix 4: Restrict background apps permissions

Fewer background clients, less broker work.

1. **Settings** > **Apps** > **Installed apps** — for each Store app you don't need running in the background, open **Advanced options** > **Background apps permissions** > **Never**.
2. Prioritize: social apps, shopping apps, games, and anything with live tiles you never look at.
3. Keep background permissions for apps you rely on (mail, messaging, authenticator) — this is pruning, not scorched earth.
4. Also check **Settings** > **Privacy & security** > **Background apps** (on builds that have the global page) for the master list.
5. After pruning, the broker should show 0% at idle — verify in Task Manager after 10 minutes of not touching Store apps.

### Fix 5: Repair or remove the misbehaving app

When one specific app is the driver.

1. Once Fix 1 identifies the app: **Settings** > **Apps** > **Installed apps** > the app > **Advanced options** > **Repair**. Test for a day.
2. If Repair doesn't help, use **Reset** (same page) — this clears the app's data and permission state, ending corrupt-state loops.
3. For third-party Store apps you don't need: **Uninstall**. The Microsoft Store will happily reinstall them later if you change your mind.
4. For built-in apps you can't uninstall normally (via **Advanced options** or PowerShell `Remove-AppxPackage`), resetting plus background-permission denial usually suffices.
5. Reinstall from the **Microsoft Store** if you removed something you actually want — a fresh package often behaves better than the migrated one. Store issues are documented on Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Check location and notification permission loops

Two permission types cause the most broker churn.

1. **Settings** > **Privacy & security** > **Location** — review **Let apps access your location** list. Turn off location for apps that don't need it (games, utilities, readers).
2. If **Location services** itself is stuck (icon constantly active), toggle the master **Location services** off and on — this resets the location broker state.
3. **Settings** > **System** > **Notifications** > turn off **Show notification banners** for chatty apps — each banner is brokered work.
4. Disable **Focus assist** automatic rules temporarily as a test — its state evaluation involves brokered app queries.
5. Watch Task Manager for 30 minutes after these changes — permission-loop CPU drops quickly once the polling app is denied.

### Fix 7: System-level repair for persistent broker CPU

When no single app explains it.

1. Run the **Windows Store Apps troubleshooter**: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Store Apps** > **Run**.
2. Clear the Store cache: **Win+R** > `wsreset.exe` — a blank Store window opens and closes; this fixes corrupt Store states that agitate the broker.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an elevated terminal — the broker is a system component and these repairs cover it.
4. Check for pending Windows updates — broker and app-platform fixes ship in cumulative updates regularly.
5. As a last resort, create a fresh local user profile and test there — a corrupt user profile's app-permission database can keep the broker spinning, and a new profile confirms it. For general high-CPU triage beyond the broker, see [fixing System Interrupts](/articles/best-way-to-fix-system-interrupts-high-cpu/).

## Closing

Runtime Broker high CPU is a messenger problem — the broker is working hard because some app keeps knocking on its door. Find the app (usually Photos, a location-hungry utility, or a corrupt Store package), calm it down or remove it, and the broker returns to its natural state: invisible, at 0% CPU, doing the quiet permission work Windows needs. Never kill the messenger; fix whatever's shouting at it.
