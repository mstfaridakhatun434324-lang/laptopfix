---
title: "Runtime Broker High CPU After Windows 11 Update? Fix It Fast"
slug: how-to-fix-runtime-broker-high-cpu-after-windows-11-update
date: 2026-09-06
categories: ["performance"]
tags: ["runtime broker", "high cpu", "windows 11 update", "universal apps"]
description: "RuntimeBroker.exe eating CPU after a Windows 11 update? Learn what it does, why updates trigger it, and 7 fixes to calm it down."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-after-windows-11-update.webp"
faqs:
  - q: "What is Runtime Broker and why is it using so much CPU?"
    a: "Runtime Broker (RuntimeBroker.exe) is a legitimate Windows process that manages permissions for Microsoft Store apps — things like location, camera, and microphone access. After a Windows 11 update it often spikes because the system is re-checking app permissions, re-registering Store apps, and running background maintenance. Sustained high CPU beyond a day or two usually means a misbehaving Store app is stuck requesting permissions in a loop."
  - q: "Can I end Runtime Broker in Task Manager?"
    a: "Yes, you can safely end Runtime Broker — Windows restarts it automatically when a Store app needs it. Ending the task is a fine temporary relief measure and stops the CPU spike immediately. However, if a broken app is the root cause, Runtime Broker will spin back up and the high CPU will return, so treat ending the task as a diagnostic step, not a permanent fix — find and fix the underlying app."
  - q: "Why does Runtime Broker use high memory along with high CPU?"
    a: "Runtime Broker typically uses only 20–40 MB of RAM, so if you're seeing hundreds of megabytes alongside high CPU, something is genuinely wrong — usually a Store app leaking handles or a corrupted app package forcing repeated permission checks. The combination of high CPU and high memory points strongly to a specific app rather than normal background activity, and reinstalling or resetting that app is usually the cure."
  - q: "How long should I wait after an update before worrying?"
    a: "Give it 24–48 hours of normal use. Windows runs post-update maintenance — app re-registration, permission audits, search reindexing — that legitimately keeps Runtime Broker busy. If CPU is still pinned after two days, or if Runtime Broker is constantly above 20–30% CPU with no update in progress, stop waiting and work through the fixes: disable the tips suggestions that feed it, and identify the offending Store app."
---

RuntimeBroker.exe suddenly sitting at 20–40% CPU in Task Manager right after a Windows 11 update is one of those things that looks alarming but is usually explainable. Runtime Broker is the middleman between Microsoft Store (UWP) apps and your system — every time a Store app wants your location, camera, or notifications, Runtime Broker brokers that permission. Updates reshuffle all of those permissions, re-register apps, and trigger background maintenance, so a CPU spike in the first day or two is normal.

The problem starts when it doesn't stop. If Runtime Broker is still chewing CPU days after the update, something is stuck: a Store app hammering permission requests in a loop, a corrupted app package, or the infamous "tips and suggestions" background activity that keeps Universal apps busy. The good news is the fixes are straightforward and none of them risk your system.

This guide walks through diagnosing which scenario you're in and fixing it in order — from the quick temporary relief to the permanent cure. For general post-update slowness, also see [fixing File Explorer high CPU after a Windows 11 update](/articles/how-to-fix-file-explorer-high-cpu-after-windows-11-update/); for broader slowdowns, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Post-update app re-registration**: Windows re-registers every Store app after a feature update, and Runtime Broker audits each one's permissions — heavy for a day or two.
- **A Store app stuck in a permission loop**: A buggy or half-updated app (Photos, Groove, Cortana remnants) repeatedly requests access, and Runtime Broker services each request.
- **Windows tips and suggestions**: The "Show me tips" and "Suggested content" features generate background Store-app activity that keeps Runtime Broker awake.
- **Live Tiles and notification churn**: Apps with live tiles constantly updating (news, weather) generate permission and notification traffic.
- **Corrupted app package**: A damaged UWP app installation makes Runtime Broker retry operations endlessly.
- **Background app permissions too broad**: Too many Store apps allowed to run in the background multiplies Runtime Broker's workload.
- **Pending Store updates stuck**: The Microsoft Store trying and failing to update an app creates repeated broker activity.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's actually Runtime Broker and wait it out (briefly)

First, make sure you're looking at the right process and the right timeframe.

1. Open **Task Manager** > **Processes**, sort by CPU — confirm it's **Runtime Broker** (RuntimeBroker.exe), not a similarly-named process.
2. Check **Settings** > **Windows Update** — if an update finished within the last 48 hours, some elevated activity is expected.
3. Right-click Runtime Broker > **End task** — this is safe; Windows restarts it on demand. If CPU drops and stays low for hours, it may have just needed a reset.
4. If CPU climbs right back up within minutes, you have a persistent trigger — move to Fix 2.
5. Don't end it repeatedly as a "solution" — that's treating the symptom. The goal is finding which app is keeping it busy.

### Fix 2: Turn off Windows tips, tricks, and suggested content

This is the single most effective fix and resolves a large share of persistent Runtime Broker CPU issues.

1. Go to **Settings** > **System** > **Notifications** > **Additional settings** (or scroll down) and uncheck **Show me the Windows welcome experience**, **Suggest ways to get the most out of Windows**, and **Get tips and suggestions when using Windows**.
2. Go to **Settings** > **Privacy & security** > **General** and turn off **Show me suggested content in the Settings app**.
3. Go to **Settings** > **Personalization** > **Start** and turn off **Show suggestions for tips, shortcuts, new apps, and more**.
4. These settings drive background Store-app activity — disabling them starves the permission loop of its fuel. (Our dedicated guides cover [Windows 10](/articles/how-to-turn-off-windows-tips-and-suggestions-on-windows-10/) and [Windows 11](/articles/how-to-turn-off-windows-tips-and-suggestions-on-windows-11/) in more detail.)
5. End Runtime Broker in Task Manager once more, then watch CPU for 10–15 minutes — for many users this alone ends the saga.

### Fix 3: Limit which Store apps can run in the background

Fewer background apps means less broker traffic.

1. Go to **Settings** > **Apps** > **Installed apps**.
2. Click the **…** menu on each preinstalled app you don't use (Clipchamp, Spotify, TikTok, news apps) > **Advanced options**.
3. Under **Background apps permissions**, set it to **Never** for apps you don't need running.
4. Pay special attention to apps with live tiles or frequent notifications — each update cycle involves Runtime Broker.
5. You don't need to nuke everything — just the apps you never open. Fifteen minutes of pruning here pays off permanently. See Microsoft's app guidance at [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 4: Update or reset the misbehaving Store app

If one specific app is the culprit, updating or resetting it breaks the loop.

1. Open the **Microsoft Store** > **Library** > **Get updates** — install everything pending. A half-updated app is a prime suspect.
2. If Runtime Broker spikes when you open a particular app (commonly Photos, Mail, or Xbox Game Bar), that's your culprit.
3. Go to **Settings** > **Apps** > **Installed apps**, find the suspect app > **…** > **Advanced options** > **Repair** first.
4. If Repair doesn't help, use **Reset** — this clears the app's data and permission state, which is exactly what breaks the loop.
5. For apps you never use, just **Uninstall** them — fewer Store apps, less broker work.

### Fix 5: Re-register all Store apps with PowerShell

For system-wide corruption after a botched update.

1. Open Terminal as administrator.
2. Run: `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. This re-registers every Store app package — it takes several minutes and will show red errors for system packages that can't be re-registered; that's normal, ignore them.
4. Restart your laptop when it finishes.
5. Check Task Manager after the reboot — Runtime Broker should settle to near-zero when idle.

### Fix 6: Check for a stuck Windows Update component

Sometimes the update itself never fully finished, keeping maintenance tasks looping.

1. Go to **Settings** > **Windows Update** and install anything pending — then restart even if it doesn't ask.
2. Run the Windows Update troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
3. In an elevated Terminal, run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` to repair update-damaged system files.
4. Check **Task Scheduler** > **Microsoft** > **Windows** > **UpdateOrchestrator** for tasks stuck in a running state — a wedged update task keeps broker-adjacent services busy.
5. If updates repeatedly fail, download the failing KB manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — a clean manual install often succeeds where the automatic one loops.

### Fix 7: Create a fresh user profile (last resort)

If Runtime Broker misbehaves only in your profile, the profile's app-permission database is corrupt.

1. Go to **Settings** > **Accounts** > **Other users** > **Add account** and create a new local administrator account.
2. Sign into the new account and watch Task Manager for an hour of normal use.
3. If Runtime Broker is calm in the new profile, your old profile's Store app data is corrupt — migrate your files over rather than fighting it.
4. This is rare but definitive — a corrupt per-user app repository can't be fixed by any of the above.
5. Before doing this, it's worth one full in-place upgrade repair (via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)) which refreshes system files while keeping everything.

## Closing

Runtime Broker high CPU after a Windows 11 update is almost always transient maintenance or one noisy Store app — rarely anything sinister. Disable the tips and suggestions background churn, prune background apps, and reset the offending app, and Runtime Broker goes back to being the quiet background process it's supposed to be.
