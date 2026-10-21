---
title: "How to Fix Copilot App Notifications Not Working on Your AI PC"
slug: copilot-app-notifications-not-working
date: 2026-10-21
categories: ["ai-pc"]
tags: ["copilot notifications", "windows 11 notifications", "copilot app", "ai pc", "troubleshooting", "do not disturb"]
description: "Restore missing Copilot app notifications with six fixes: notification settings, Focus modes, privacy permissions, app reset, account sync, and a reinstall."
thumbnail: "/images/thumbs/copilot-app-notifications-not-working.webp"
faqs:
  - q: "Why do Copilot notifications not appear even though they are turned on?"
    a: >
      The most common cause is Windows Focus (Do Not Disturb) silently suppressing
      them, followed by Copilot's background activity being disabled in battery
      settings. Check both before assuming the app is broken — the toggles live in
      different Settings pages and are easy to miss.
  - q: "Can Copilot send notifications on the lock screen?"
    a: >
      Yes, if you allow it. Go to Settings > System > Notifications and make sure
      Copilot is permitted to show notifications on the lock screen. Note that some
      notification content may be hidden on the lock screen by your privacy settings.
  - q: "Do Copilot notifications work inside a virtual machine?"
    a: >
      Usually not. Toast notifications generally do not cross the boundary from a
      virtual machine to the host desktop. If you run Copilot inside a VM, expect to
      check the app manually rather than relying on toasts.
  - q: "Will resetting the Copilot app delete my conversations?"
    a: >
      Your conversation history is tied to your Microsoft account, not the local app
      install, so it survives a reset. You will need to sign in again and re-enable
      notification permissions afterward.
---

You set up Copilot's daily briefing and task reminders, and then... silence. No toast slides in, nothing waits in the notification center, and the lock screen stays blank. On an AI PC, where Copilot is meant to be a proactive assistant that surfaces what matters, missing notifications quietly defeats the whole point.

This affects the Copilot Windows app's toasts, notification-center entries, and lock-screen alerts — briefings, reminders, and task nudges all go missing together. The app itself usually opens and chats fine, which is exactly why the problem hides: everything looks healthy until you realize the assistant never calls out to you.

This guide gives you six fixes in technician order: Windows notification switches first, then Focus and Do Not Disturb, background activity, app repair, the notification pipeline itself, and account sync. Check each one and send yourself a test notification where you can.

## Why this happens

- **Notifications disabled for Copilot in Windows Settings**: Windows 11 manages notifications per app. Copilot can be muted there even while the in-app notification toggle is on.
- **Focus or Do Not Disturb is on**: Focus sessions, automatic rules (like "when duplicating my display"), or a stuck Do Not Disturb state suppress toasts silently.
- **Background activity turned off**: Battery-saver policies can block Copilot from running in the background, so scheduled nudges never fire.
- **Corrupt notification database**: Windows stores toasts in a local database that can corrupt after crashes, swallowing new notifications.
- **Broken sign-in session**: Copilot's cloud-scheduled briefings depend on your account session. If [Copilot's daily briefing never shows up](/articles/copilot-daily-briefing-not-showing/) either, the session is the common root cause.
- **Running inside a virtual machine**: Toasts rarely cross the VM boundary. If you use Copilot in a VM, review your [Hyper-V setup on Arm laptops](/articles/hyper-v-setup-arm-laptop/) and plan to check the app manually.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable notifications for Copilot in Windows Settings

The per-app notification switch is the first thing to verify. Windows updates and app reinstalls can flip it off without touching the in-app toggle.

1. Open **Settings > System > Notifications** and confirm the master **Notifications** toggle is on.
2. Scroll to the app list, find **Microsoft Copilot**, and turn its notifications on.
3. Expand its entry and enable **Show notification banners** and **Show notifications in notification center**.
4. Ask Copilot to set a reminder one minute out and watch for the toast.

### Fix 2: Turn off Focus and check Do Not Disturb rules

Focus is the silent killer of notifications. It can be active without any obvious indicator, especially when an automatic rule turned it on.

1. Open **Settings > System > Notifications** and check **Do not disturb** — turn it off if it is on.
2. Click **Turn on do not disturb automatically** and review every rule; disable the ones you do not want (gaming, duplicating display, full-screen apps).
3. Check **Settings > System > Focus** and end any active focus session.
4. Send the one-minute test reminder again and confirm the toast appears.

### Fix 3: Allow Copilot to run in the background

If Copilot cannot run in the background, time-based nudges and briefings never get generated on the device. Battery saver is the usual culprit on laptops.

1. Go to **Settings > Apps > Installed apps > Microsoft Copilot > Advanced options**.
2. Under **Background apps permissions**, set it to **Always** (or at least **Power optimized**, not **Never**).
3. Go to **Settings > System > Power & battery** and make sure **Battery saver** is not permanently on.
4. Keep the laptop plugged in for one test cycle to rule out aggressive power policies.

### Fix 4: Repair the Copilot app and re-grant permissions

A damaged app package can lose its notification channel registration while everything else works. Repairing re-registers it with Windows.

1. Go to **Settings > Apps > Installed apps > Microsoft Copilot > Advanced options** and click **Repair**.
2. Test notifications. If they still fail, return and click **Reset**, then sign in again.
3. After the reset, re-enable every notification toggle from Fix 1 — resets restore defaults.
4. If toasts appear but reminders arrive late or wrong, your sign-in session is suspect; sign out and back in inside the app.

### Fix 5: Restart the notification pipeline

When the Windows push-notification plumbing itself is stuck, no app's toasts arrive. A service restart plus a database rebuild clears this. [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the notification-pipeline repairs if the service will not cooperate.

1. Press **Win + R**, type `services.msc`, find **Windows Push Notifications System Service**, and restart it.
2. If that service will not start, run **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Store Apps** troubleshooter.
3. Restart the laptop (full restart, not hybrid sleep) so the notification database rebuilds cleanly.
4. Retest with the one-minute reminder. If other apps' toasts are also missing, the pipeline was the problem all along.

### Fix 6: Check account sync and quiet hours

Cloud-scheduled briefings depend on your Microsoft account being healthy and on quiet hours not eating them. If notifications crash the machine instead of staying silent, that is a different failure — see the [NPU blue-screen guide for Windows 11](/articles/npu-causes-blue-screen-windows-11/).

1. In Copilot, confirm you are signed in with the intended account and that reminders sync there.
2. Check **Settings > System > Notifications** for any quiet-hours-style rules from third-party "focus" utilities and disable them for testing.
3. On the web at your Microsoft account, verify Copilot's connected experiences are enabled.
4. Give it one full briefing cycle (usually next morning) before declaring victory — some nudges only fire on schedule.

## Closing

Copilot notification failures are almost always configuration, not breakage: a per-app toggle Windows flipped, a Focus rule you never set, background activity starved by battery saver, or a session that needs a fresh sign-in. Work the list top to bottom and the toasts come back — and once they do, leave background permissions alone, because that one toggle causes more repeat visits than all the others combined.
