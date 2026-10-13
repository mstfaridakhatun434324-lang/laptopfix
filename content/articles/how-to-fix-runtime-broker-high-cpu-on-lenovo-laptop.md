---
title: "Runtime Broker High CPU on Your Lenovo Laptop? Fix It"
slug: how-to-fix-runtime-broker-high-cpu-on-lenovo-laptop
date: 2026-09-04
categories: ["performance"]
tags: ["runtime broker high cpu", "lenovo laptop", "windows 11", "uwp apps", "cpu fix"]
description: "Runtime Broker spiking CPU on your Lenovo laptop? Understand what this middleman process does and stop the misbehaving Store app behind it."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-on-lenovo-laptop.webp"
faqs:
  - q: "What is Runtime Broker and why does it use CPU?"
    a: "Runtime Broker (RuntimeBroker.exe) is a Windows middleman process that manages permissions for Microsoft Store (UWP) apps — checking whether an app may access your location, camera, microphone, or notifications. Normally it uses negligible CPU. When it spikes, it means a Store app is repeatedly requesting permissions, live tiles are updating frantically, or a buggy app is hammering the broker with requests. The broker itself is innocent; the app behind it is the problem."
  - q: "Is it safe to end Runtime Broker in Task Manager?"
    a: "Ending it is safe in the sense that Windows restarts it automatically and nothing breaks permanently — but it is pointless as a fix, because the underlying app immediately starts hammering the fresh broker instance. Use End task only as a diagnostic: if CPU drops then climbs back within minutes, you have confirmed a persistent app-driven cause. The lasting fix is finding and taming that app, which is what the steps below do."
  - q: "Why does Runtime Broker spike on Lenovo laptops specifically?"
    a: "Lenovo preloads several Microsoft Store apps (Lenovo Vantage components, McAfee trials, utility companions) that are heavier broker users than typical Store apps. Additionally, Lenovo's utilities sometimes request location or notification permissions in tight loops when their background services misbehave after updates. The pattern — Runtime Broker spikes alongside a Lenovo utility's background activity — is common enough that checking Lenovo's preinstalled Store apps first is worthwhile."
  - q: "Can I disable Runtime Broker permanently?"
    a: "You should not. Runtime Broker is a core Windows component; disabling it breaks Store apps' permission model and can cause app crashes and Start menu issues. Registry hacks claiming to disable it cause more harm than the CPU they save. The correct approach is reducing its workload: turn off background app permissions globally or per-app, disable live tiles and tips, and remove or fix the specific Store app generating the request storm."
---

Multiple RuntimeBroker.exe entries are stacking up CPU in Task Manager on your Lenovo laptop — sometimes 10%, sometimes 30% — and ending them only helps for a few minutes before they are back. Runtime Broker is Windows' permission middleman for Store apps, and when it burns CPU, some app is abusing the permission system in a loop.

Lenovo laptops add their own wrinkle: preinstalled Store-based utilities that can become chatty after updates. The fix is identifying which app is hammering the broker and quieting it. For the Windows 11 general case beyond Lenovo, our broader [Windows 11 performance guides](/articles/laptop-running-slow-windows-11-how-to-speed-up/) apply; for trimming what runs at boot, see [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **A Store app stuck in a permission loop**: Buggy UWP apps repeatedly request location/camera/mic access, each request costing broker CPU.

- **Live tiles updating aggressively**: Tiles with real-time content (news, weather, stocks) wake the broker on every update cycle.

- **Windows tips and suggestions**: The Tips app and suggestions system generate broker-mediated notifications constantly.

- **Lenovo preinstalled Store utilities**: Lenovo Vantage modules and bundled trials can become unusually chatty after updates.

- **Background app permissions too broad**: Dozens of Store apps allowed to run in the background multiply broker workload.

- **Corrupt Store app installations**: Damaged app packages throw repeated permission errors that the broker must process.

- **Notification storms**: Apps firing excessive toast notifications route through broker-mediated channels.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Catch the app behind the broker

Runtime Broker instances group by app; Task Manager can show you which.

1. Open **Task Manager > Processes** and expand the **Runtime Broker** groupings — note which ones show CPU and their memory footprints.
2. In the **Details** tab, add the **Command line** column (right-click headers): the **-p** parameter reveals which app package each broker instance serves.
3. Alternatively, open **Settings > System > Notifications** and look for apps with excessive recent notification activity.
4. Check timing: does the spike correlate with a specific Lenovo utility running, a Store app updating, or login?
5. Write down the suspect app package name — the fixes below target it.

### Fix 2: Restrict background app permissions

The broadest fix: stop the army of Store apps from running — and brokering — in the background.

1. Go to **Settings > Apps > Installed apps**, click the **...** on each Store app you do not need live, choose **Advanced options**.
2. Under **Background apps permissions**, set it to **Never** for apps that do not need background activity (games, utilities, trials).
3. For a global approach: **Settings > Apps > Installed apps**, and bulk-restrict the obvious non-essentials first.
4. Keep background permission for apps you genuinely rely on (mail, calendar, messaging) — this is triage, not scorched earth.
5. Restart and monitor Runtime Broker CPU over an hour; background restriction is the highest-yield single change.

### Fix 3: Disable live tiles, tips, and suggestions

These Windows features are constant low-level broker customers.

1. Right-click each live tile on the Start menu > **Unpin from Start** for news, weather, and other auto-updating tiles.
2. Go to **Settings > System > Notifications** and turn off **Tips and suggestions** / **Get tips and suggestions when using Windows**.
3. In **Settings > Privacy & security**, review **App permissions** (Location, Camera, Microphone) and disable access for apps that do not need it — fewer permission checks, less broker work.
4. Turn off **Suggested content** in **Settings > Personalization > Start**.
5. These changes also modestly improve battery life, since broker wake-ups keep the CPU from sleeping deeply.

### Fix 4: Update or remove Lenovo's Store apps

On Lenovo systems, the preinstalled Store layer deserves its own audit.

1. Open the **Microsoft Store > Library** and update all apps, especially anything Lenovo-branded.
2. Open **Lenovo Vantage** (the desktop app) and install its updates; a stale Vantage with a fresh Windows build is a classic broker-noise source.
3. In **Settings > Apps > Installed apps**, review Lenovo-bundled trials and companions you never use — uninstall the obvious bloat.
4. Check **Task Manager > Startup apps** for Lenovo Store-app entries launching at boot and disable the non-essential ones.
5. If a specific Lenovo component is the confirmed broker abuser and updates do not help, uninstall it and rely on [Lenovo's support site](https://support.lenovo.com/us/en/) drivers directly instead.

### Fix 5: Repair corrupt Store apps

A damaged app package generates error loops that the broker must process endlessly.

1. For the suspect app: **Settings > Apps > Installed apps > ... > Advanced options > Repair**; if that fails, **Reset** (note: reset clears the app's data).
2. If multiple Store apps misbehave, reset the Store itself: **Settings > Apps > Installed apps > Microsoft Store > Advanced options > Reset**.
3. Re-register all Store apps in an elevated PowerShell: **Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}** (takes several minutes).
4. Run **WSReset.exe** (Win + R) to clear the Store cache.
5. Restart and verify: repaired apps stop generating the error traffic that was feeding the broker.

### Fix 6: Quiet notifications at the source

Notification storms are broker-mediated; reducing them reduces broker CPU directly.

1. Go to **Settings > System > Notifications** and turn off notifications for apps that spam (social, shopping, and game apps are typical).
2. Disable **Show notification banners** for noisy apps while keeping them in the notification center if you still want the information.
3. Turn on **Do not disturb** automatically during focus hours: **Settings > System > Notifications > Turn on do not disturb automatically**.
4. Uninstall Store apps whose only function is sending you notifications you ignore.
5. Monitor for a day: broker CPU should now sit near zero except for brief legitimate pulses.

### Fix 7: Check for the deeper causes

If broker CPU survives all app-level fixes, look one layer deeper.

1. Run **DISM /Online /Cleanup-Image /RestoreHealth** and **sfc /scannow** — corrupted Windows permission components can make the broker work overtime.
2. Create a new local user account and test there; a corrupted user profile's app data can drive per-user broker storms.
3. Check **Event Viewer > Windows Logs > Application** for repeating errors from a specific app package correlating with CPU spikes.
4. Ensure Windows is fully updated — broker efficiency fixes ship in cumulative updates; check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for known issues.
5. As a last resort, an in-place Windows 11 repair install preserves files and apps while rebuilding the app platform cleanly.

## Closing

Runtime Broker is the messenger, never the culprit: some Store app on your Lenovo laptop is hammering Windows' permission system, and the broker is just doing the paperwork. Restrict background permissions, quiet the Lenovo preloads, repair the corrupt apps — and Runtime Broker goes back to the near-zero background role it was designed for.
