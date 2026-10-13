---
title: "Runtime Broker High CPU: Step-by-Step Fix for Windows 11"
slug: how-to-fix-runtime-broker-high-cpu-step-by-step
date: 2026-09-26
categories: ["performance"]
tags: ["runtime broker", "high cpu", "windows 11", "microsoft store apps"]
description: "RuntimeBroker.exe spiking your CPU? Follow this step-by-step guide to diagnose which app is behind it and calm it down for good."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-step-by-step.webp"
faqs:
  - q: "What is Runtime Broker and is it a virus?"
    a: "Runtime Broker (RuntimeBroker.exe) is a legitimate Windows process that manages permissions for Microsoft Store (UWP) apps — things like camera, microphone, and location access. It is not a virus. However, malware can disguise itself with the same name, so if you see RuntimeBroker.exe running from anywhere other than C:\\Windows\\System32, or multiple copies with strange spelling, run a full Defender scan immediately."
  - q: "Why does Runtime Broker use so much CPU?"
    a: "Runtime Broker spikes when a Store app repeatedly requests permissions, when app updates are stuck, or when features like Windows tips, spotlight images, or live tiles keep waking apps in the background. A common pattern is 20-40% CPU that never settles, usually tied to one misbehaving app such as Photos, Mail, or a third-party Store app with a buggy update."
  - q: "Can I disable Runtime Broker?"
    a: "You shouldn't kill it permanently — it's a core part of how Store apps run, and ending the process just makes Windows restart it. The correct approach is fixing the app or setting that's making it work so hard. Disabling it via registry hacks breaks Microsoft Store apps entirely, so treat the cause (notifications, tips, bad app installs) rather than the broker itself."
  - q: "How do I find which app is causing Runtime Broker CPU spikes?"
    a: "Open Task Manager's Details tab, right-click RuntimeBroker.exe, and check its command line and associated app. You can also use Process Explorer from Microsoft Sysinternals to see exactly which app package the broker instance is serving. Often the timing gives it away — spikes that start when Photos indexes new pictures or when a Store app updates point straight at the culprit."
---

RuntimeBroker.exe sitting at 20% or 30% CPU in Task Manager is one of those mysteries that sends people down malware-rabbit-holes. Relax: Runtime Broker is a genuine Windows process. Its job is to babysit Microsoft Store apps — handling their permission requests for your camera, microphone, and location. When it misbehaves, it's almost always because one of those apps (or a Windows feature that uses them) is misbehaving first.

The pattern to watch for: Runtime Broker using a steady chunk of CPU even when you're doing nothing, sometimes paired with the fan ramping up on an idle laptop. If your whole system feels sluggish beyond this one process, start with [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); if the fan noise is the main complaint, see [fixing a loud fan at idle](/articles/best-way-to-fix-laptop-fan-not-working/).

## Why this happens

- **Misbehaving Store app**: A buggy UWP app (Photos, Mail, Spotify from the Store) loops permission requests through the broker.
- **Windows tips and suggestions**: The "Get tips" features constantly wake Store-backed content, keeping the broker busy.
- **Stuck app updates**: A Microsoft Store update that never completes makes the broker retry in the background.
- **Live tiles and background apps**: Apps allowed to run in the background generate steady broker activity.
- **Lock screen spotlight**: Windows Spotlight pulls new images and ads through Store-app machinery.
- **Corrupt app package**: A damaged app installation makes the broker spin trying to manage it.
- **Malware impersonation**: Rare, but fake RuntimeBroker.exe copies from non-system folders do exist — always verify the file location.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's the real Runtime Broker

Rule out malware before tweaking anything.

1. In **Task Manager**, right-click **Runtime Broker** > **Open file location** — the real one lives in `C:\Windows\System32`.
2. If the file opens anywhere else (Temp, AppData, a random folder), stop and run a full scan in **Windows Security** > **Virus & threat protection** > **Scan options** > **Full scan**.
3. Check the spelling carefully: `RuntimeBroker.exe` is real; `Runtime Brooker.exe`, `Runtime-Broker.exe`, or similar variants are fakes.
4. Note how many instances are running — one or two is normal; half a dozen all eating CPU suggests a stuck app.
5. Right-click the process > **Properties** > **Details** tab and confirm Microsoft Corporation as the publisher.

### Fix 2: Identify the app behind the spike

Find out which Store app is driving the broker.

1. Open **Settings** > **Apps** > **Installed apps** and sort by install date — recently updated or installed Store apps are prime suspects.
2. Think about timing: does the spike start when you open Photos, when Mail syncs, or right after a Store update?
3. Open **Microsoft Store** > **Library** and check for apps stuck on "Updating" or "Pending" — a stalled update is a classic trigger.
4. Temporarily uninstall recently added Store apps one at a time, watching Task Manager after each removal.
5. For a precise answer, download **Process Explorer** from Microsoft Sysinternals, hover over the RuntimeBroker.exe instance, and read which app package it serves.

### Fix 3: Turn off Windows tips and suggestions

This single toggle fixes a surprising number of cases.

1. Open **Settings** > **System** > **Notifications**.
2. Scroll down and turn off **Offer suggestions on how I can set up my device** and **Get tips and suggestions when using Windows**.
3. Go to **Settings** > **Privacy & security** > **General** and turn off **Let apps show me personalized ads** and **Show me suggested content in the Settings app**.
4. Restart the laptop and watch Runtime Broker for 10 minutes — these content feeds were waking Store machinery constantly.
5. If CPU settles, you've found it; leave those toggles off permanently.

### Fix 4: Kill live tiles and background app activity

Stop Store apps from working when you're not using them.

1. Open **Settings** > **Apps** > **Installed apps**, pick a Store app you rarely use, click **...** > **Advanced options**.
2. Under **Background apps permissions**, set it to **Never** for apps that don't need to run in the background.
3. Repeat for the usual suspects: Photos, Mail and Calendar, Cortana remnants, Xbox Game Bar (if unused), and any preinstalled bloatware apps.
4. Go to **Settings** > **Personalization** > **Lock screen** and set the background to **Picture** or **Slideshow** instead of **Windows spotlight**.
5. Restart and confirm Runtime Broker drops to near-zero at idle.

### Fix 5: Reset or repair the offending Store app

When one app is clearly the trigger, give it a fresh start.

1. In **Settings** > **Apps** > **Installed apps**, find the suspect app > **...** > **Advanced options**.
2. Click **Repair** first — this reinstalls the app's files without touching your data; test CPU usage after.
3. If Repair doesn't help, click **Reset** — this wipes the app's data, so back up anything important inside it first.
4. Alternatively, uninstall the app entirely and reinstall it fresh from the **Microsoft Store**.
5. For system apps you can't uninstall (like Photos), use Reset, or switch to a desktop alternative and set background permissions to Never.

### Fix 6: Clear stuck Store updates and cache

A jammed update pipeline keeps the broker churning.

1. Open **Microsoft Store** > **Library** > **Get updates** and let everything finish — cancel anything stuck, then retry.
2. Press **Win + R**, type `wsreset.exe`, and press Enter — a blank Store window opens and closes, clearing the Store cache.
3. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** and run the **Windows Store Apps** troubleshooter.
4. Check **Settings** > **Windows Update** and install pending updates — Store and broker fixes ship in cumulative updates; Microsoft documents update troubleshooting at [Microsoft support](https://support.microsoft.com/en-us/windows).
5. Reboot and re-check: a clean update pipeline usually drops Runtime Broker back to idle.

### Fix 7: Create a fresh user profile (last resort)

If the broker misbehaves for every app, the user profile's app data may be corrupt.

1. Open **Settings** > **Accounts** > **Other users** > **Add account** and create a new local administrator account.
2. Sign into the new account, leave it idle for 15 minutes, and check Task Manager for Runtime Broker CPU.
3. If it's calm in the new profile, your old profile's Store-app data is corrupt — migrate your files over.
4. Move documents, desktop, and browser data to the new profile; reinstall Store apps fresh rather than copying app data.
5. Once settled, you can remove the old profile from **Settings** > **Accounts** > **Other users**.

## Closing

Runtime Broker is the messenger, not the problem — high CPU from it always traces back to a Store app, a stuck update, or a chatty Windows feature. Verify the process is genuine, find the app behind it, and quiet the background chatter with the toggles above. Done in order, these steps resolve nearly every Runtime Broker spike without resorting to dangerous hacks.
