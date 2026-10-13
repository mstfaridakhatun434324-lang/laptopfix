---
title: "How to Fix Runtime Broker High CPU on a Dell Laptop"
slug: how-to-fix-runtime-broker-high-cpu-on-dell-laptop
date: 2026-10-07
categories: ["performance"]
tags: ["runtime broker", "high cpu", "dell laptop", "windows 11", "cpu fix"]
description: "RuntimeBroker.exe pinning your Dell laptop's CPU? Learn what Runtime Broker does, which app is making it misbehave, and the step-by-step fixes that calm it down."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-on-dell-laptop.webp"
faqs:
  - q: "What is Runtime Broker and is it safe to end the task?"
    a: "Runtime Broker is a legitimate Windows process that manages permissions for Microsoft Store apps — things like location, camera, and microphone access. Ending the task in Task Manager is safe; Windows restarts it automatically when needed. However, ending it only treats the symptom. If it immediately spikes again, a specific Store app is misbehaving, and you need to find which one."
  - q: "Why does Runtime Broker use so much CPU on Dell laptops?"
    a: "Dell laptops ship with many preinstalled Store apps — Dell utilities, partner apps, and trials — and each one can trigger Runtime Broker activity when it requests permissions or runs background tasks. A single misbehaving app, often one you never open, can keep Runtime Broker churning constantly. The process itself is rarely broken; it is reacting to an app."
  - q: "Can I disable Runtime Broker permanently?"
    a: "You should not. Runtime Broker is a core part of the Store app permission system, and disabling it breaks Microsoft Store apps. The correct approach is finding and fixing the app that is overworking it — usually by changing that app's background permissions or uninstalling it. Disabling the broker is like removing a smoke detector because of a noisy alarm."
  - q: "Does Runtime Broker high CPU drain the battery?"
    a: "Yes, significantly. Sustained high CPU usage keeps the processor from entering low-power states, which drains the battery faster and generates heat that spins up the fans. Fixing a runaway Runtime Broker often produces a noticeable improvement in both battery life and how quiet the laptop runs."
---

Few Task Manager mysteries are as persistent as RuntimeBroker.exe sitting at 20, 40, or even 80 percent CPU while you do nothing. On Dell laptops it is especially common, because Dell preloads a small army of Microsoft Store apps — utilities, partner offers, trials — and Runtime Broker is the process that manages permissions and background activity for every one of them. When one of those apps misbehaves, Runtime Broker takes the blame in Task Manager while the real culprit hides.

The key insight: Runtime Broker is almost never broken itself. It is overworked. The fix is finding which app is overworking it.

## Why this happens

- **A misbehaving Store app:** One preinstalled or third-party Store app stuck in a permission-request or background-task loop drives Runtime Broker's CPU usage.
- **Dell's preload multiplying the suspects:** More preinstalled Store apps means more candidates for the misbehaving one — Dell machines simply have more lottery tickets.
- **Live tiles and background refresh:** Apps with live tiles or background refresh constantly wake Runtime Broker to update content and check permissions.
- **Stuck "Get tips" and system apps:** Windows' own tips, suggestions, and spotlight features can loop on corrupted state and hammer the broker.
- **Corrupted Store app installations:** Damaged app packages cause repeated failed permission checks, each one costing broker CPU time.
- **Photos app background processing:** The Photos app's face detection and indexing runs through broker-mediated background tasks and can spike for hours on large libraries.
- **Location and notification permission churn:** Apps repeatedly requesting location or notification access — especially after updates reset permissions — keep the broker busy.
- **Windows Spotlight lock screen:** The rotating lock-screen images and suggestions involve broker activity on every lock/unlock cycle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the app behind the broker

1. Open **Task Manager → Details** tab, find **RuntimeBroker.exe** — note there may be several instances, each serving different apps.
2. Right-click the high-CPU instance → the **User name** and associated app can sometimes be inferred; alternatively use **Process Explorer** (Microsoft Sysinternals) to see exactly which app each broker instance serves.
3. Simpler method: open **Settings → Apps → Installed apps** and look at recently updated or preinstalled Dell/partner Store apps — the culprit is usually one you never intentionally installed.
4. Note your suspects before changing anything; targeted removal beats blanket changes.

### Fix 2: Turn off background activity for suspect apps

1. Go to **Settings → Apps → Installed apps**, click the **…** on a suspect app → **Advanced options**.
2. Under **Background apps permissions**, set it to **Never**.
3. Under **App permissions**, toggle off **Location**, **Camera**, and **Microphone** for apps that have no business needing them.
4. Repeat for each Dell preload and partner app you do not use. Watch Task Manager after each change — when the broker calms down, you found it.

### Fix 3: Disable Windows tips, suggestions, and Spotlight

1. Go to **Settings → System → Notifications** and turn off **Get tips and suggestions when using Windows**.
2. Go to **Settings → Personalization → Lock screen** and change the background from **Windows spotlight** to **Picture**.
3. In **Settings → Privacy & security**, review app permissions broadly and revoke what is unnecessary.
4. These system features are frequent broker irritants, and disabling them costs nothing in real functionality. For the full tips-removal walkthrough, see our guide on [turning off Windows tips and suggestions](/articles/best-way-to-turn-off-windows-tips-and-suggestions/).

### Fix 4: Uninstall the offending preinstalled apps

1. In **Settings → Apps → Installed apps**, uninstall Dell partner apps, trials, and games you never use.
2. For stubborn preinstalled apps that lack an uninstall button, right-click them in the **Start menu** and choose Uninstall from there.
3. Keep Dell utilities you actually use (SupportAssist, power management) — the goal is removing the unknown ones, not gutting the system.
4. After removals, restart and verify broker CPU stays low for a full day of normal use. For the broader autostart cleanup, see [how to disable startup programs](/articles/how-to-disable-startup-programs-windows-11/).

### Fix 5: Repair or reset the Windows Store app platform

1. Open an **admin Terminal** and run `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}` to re-register all Store apps.
2. Alternatively, go to **Settings → System → Troubleshoot → Other troubleshooters** and run the **Windows Store Apps** troubleshooter.
3. Corrupted app packages are a classic cause of broker loops, and re-registration fixes them without data loss.
4. Restart after the repair and recheck. Microsoft documents Store repairs at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 6: Tame the Photos app specifically

1. Open the **Photos app → Settings** and turn off anything related to automatic enhancement, face grouping, or OneDrive-linked processing if you do not use those features.
2. In the app's **Advanced options** (Settings → Apps → Installed apps → Microsoft Photos → Advanced options), set **Background apps permissions** to **Never** if you only open Photos manually.
3. For very large photo libraries, consider a lighter third-party viewer for browsing — the Photos app's background analysis is disproportionate on huge collections.
4. This single app is responsible for a surprising share of broker complaints.

### Fix 7: Check for the issue after updates

1. If broker spikes began right after a Windows update, the update may have re-enabled background permissions or reinstalled removed apps.
2. Re-run Fix 2's permission audit — updates are notorious for resetting app permissions to defaults.
3. Check **Settings → Apps → Installed apps** sorted by install date for anything the update re-added, and remove it again.
4. Keep Dell and Windows drivers current via [Dell's official support site](https://www.dell.com/support) — firmware-level fixes occasionally address the underlying app behavior.

### Fix 8: Create a clean test profile

1. Create a new local user account (**Settings → Accounts → Other users → Add account**) and log into it.
2. If Runtime Broker behaves normally in the new profile, your main profile's app data or permissions database is corrupt — the problem is environmental, not systemic.
3. Migrate to the new profile (copy Documents, Desktop, browser data) rather than fighting the corruption.
4. If the broker misbehaves in the new profile too, a Windows repair install from [official media](https://www.microsoft.com/en-us/software-download/windows11) is the final step.

## Closing

Runtime Broker high CPU is a whodunit, not a hardware failure — some Store app is making the broker work overtime, and Dell's generous preload means there are plenty of suspects. Audit background permissions, silence the tips and Spotlight features, remove the apps you never asked for, and repair the Store platform if needed. Find the app behind the broker, and the CPU graph goes quiet.
