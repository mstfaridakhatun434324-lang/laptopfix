---
title: "Runtime Broker Still Spiking? The Best Way to Fix It for Good"
slug: best-way-to-fix-runtime-broker-high-cpu
date: 2026-09-25
categories: ["performance"]
tags: ["runtime broker", "high cpu", "store apps", "cpu fix"]
description: "The definitive Runtime Broker high CPU fix: identify the triggering app, kill background permissions, and keep it quiet permanently."
thumbnail: "/images/thumbs/best-way-to-fix-runtime-broker-high-cpu.webp"
faqs:
  - q: "What's the fastest way to stop Runtime Broker high CPU?"
    a: "End the task in Task Manager for instant relief, then turn off 'Get tips and suggestions when using Windows' in Settings > System > Notifications. Those two steps resolve the majority of cases within minutes. For a permanent fix, also set background app permissions to Never for preinstalled Store apps you don't use, and reset or uninstall the specific app triggering the spikes."
  - q: "Which apps usually cause Runtime Broker CPU spikes?"
    a: "The most common offenders are the Photos app (background indexing loops), News and Weather (constant background refreshes), the Tips app, and third-party Store apps with buggy background tasks. Recently updated apps are prime suspects. If spikes started after installing a particular Store app, that app is almost certainly the trigger."
  - q: "Will disabling background apps break anything?"
    a: "Setting a Store app's background permission to Never only stops it from running when you're not using it — the app still works perfectly when you open it. The only things you lose are live tile updates and background notifications from that app. For apps you rarely open, there's no downside whatsoever."
  - q: "Why does Runtime Broker come back after I end the task?"
    a: "Ending the task only stops the current instance — Windows restarts Runtime Broker automatically whenever a Store app needs a permission check, which is by design. If it immediately climbs back to high CPU, the triggering app is still active and still misbehaving. The permanent fix is addressing that app (Fix 3 and Fix 5), not repeatedly ending the broker task."
---

Ending Runtime Broker in Task Manager works — for about ten minutes. Then it's back, chewing CPU again, because you treated the symptom while the disease (a misbehaving Store app) kept going. The best way to fix Runtime Broker high CPU isn't a faster way to kill the process — it's a systematic way to find what's driving it and shut that down permanently. This guide is that sequence: quick relief first, then the permanent fix, then the verification that it stuck.

For the diagnostic-first walkthrough, see our [Runtime Broker troubleshooting guide](/articles/runtime-broker-high-cpu-troubleshooting/); for broader performance work, [speeding up Windows 11](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **One rogue Store app in a permission loop**: A single buggy app generates endless permission checks through the broker.
- **Windows tips and suggestions**: The "helpful hints" engine constantly wakes Store apps in the background.
- **Photos app indexing storms**: The Photos app's background media indexing is a notorious broker trigger.
- **Dozens of preinstalled apps with background rights**: Every preinstalled app with background permission is a potential trigger.
- **Corrupt app installations**: Damaged Store apps fail and retry their permission requests in a loop.
- **Live tiles refreshing**: Apps updating tiles pull the broker into constant background activity.
- **Windows Spotlight churn**: Lock-screen content apps triggering repeated checks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Get immediate relief (end the task)

Stop the bleeding while you work on the cure.

1. Open **Task Manager** (Ctrl+Shift+Esc) > **Processes**, find **Runtime Broker**, right-click > **End task**.
2. CPU drops instantly — enjoy the quiet, but know it's temporary.
3. Keep Task Manager open and watch: note exactly how long until it climbs again, and which apps are running when it does.
4. If it stays quiet for hours, a transient glitch was the cause and you're likely done — skip to Fix 7's verification.
5. If it returns within minutes, proceed — you have an active trigger to hunt.

### Fix 2: Kill tips, tricks, and suggestions

The quickest permanent-ish win.

1. **Settings** > **System** > **Notifications** > expand **Additional settings**.
2. Uncheck **Get tips and suggestions when using Windows** — this single toggle fixes a huge share of cases.
3. Also uncheck **Suggest ways I can finish setting up my device** and **Show the Windows welcome experience**.
4. **Settings** > **Personalization** > **Start** > turn off **Show suggestions for tips, shortcuts, new apps, and more**.
5. Restart and monitor for an hour — for many users, the broker never misbehaves again after this.

### Fix 3: Identify the triggering app

Find the actual culprit instead of guessing.

1. With Runtime Broker ended (Fix 1), open your Store apps one at a time — Photos, News, Weather, Mail — watching Task Manager after each.
2. The app that makes Runtime Broker spike within a minute or two is your trigger.
3. Check **Settings** > **Apps** > **Installed apps** sorted by recent — apps updated in the last few days are suspects.
4. Don't forget third-party Store apps (Spotify, Netflix, etc.) — their background tasks go through the broker too.
5. Write down the culprit — Fixes 4 and 5 target it directly.

### Fix 4: Revoke background permissions broadly

Starve the triggers of background activity.

1. **Settings** > **Apps** > **Installed apps** — for every preinstalled app you don't use, click **...** > **Advanced options** > set **Background apps permissions** to **Never**.
2. Prioritize: Tips, News, Weather, Clipchamp, Solitaire collection, and any manufacturer bloatware.
3. For the culprit app from Fix 3, definitely set it to Never — or uninstall it if you don't need it.
4. This doesn't break the apps — they work fine when opened; they just can't wake up behind your back.
5. Restart and verify: Runtime Broker should sit at 0% at idle.

### Fix 5: Repair, reset, or remove the culprit app

Fix the app instead of working around it.

1. **Settings** > **Apps** > **Installed apps** > culprit app > **...** > **Advanced options** > **Repair** — test afterward.
2. If Repair fails, use **Reset** — wipes the app's data, clearing the corrupt state causing the loop.
3. For the **Photos** app specifically, Reset is remarkably effective against its indexing loops.
4. If you don't use the app, **Uninstall** it — the cleanest possible fix.
5. Reinstall from the Microsoft Store only if you actually need it — fresh installs rarely inherit the corrupt state.

### Fix 6: Reset the Store cache and update everything

Clear the systemic rot.

1. Press **Win+R**, run `wsreset.exe` — clears the Microsoft Store cache (blank window, then Store opens).
2. Open **Microsoft Store** > **Library** > **Get updates** — install all pending app updates; outdated apps misbehave more.
3. **Settings** > **Windows Update** — install all pending Windows updates; broker bugs get patched in cumulative updates.
4. Restart after everything is updated.
5. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents Store reset procedures if you need the official flow.

### Fix 7: Verify it stays fixed

Prove the fix, don't assume it.

1. After all fixes, restart and let the laptop idle for 30 minutes with Task Manager's **Processes** tab visible.
2. Runtime Broker should appear at 0% CPU — brief flickers when opening Store apps are fine.
3. Use the laptop normally for 2–3 days, glancing at Task Manager occasionally — sustained spikes mean a trigger survived.
4. If spikes return, repeat Fix 3's identification — a different app may have taken over as the trigger.
5. For ongoing monitoring, **Settings** > **System** > **Power & battery** > **Battery usage** shows which apps burn background power — a proxy for broker-triggering behavior. Pair with our [startup trim guide](/articles/how-to-disable-startup-programs-windows-11/) for full background hygiene.

## Closing

The best way to fix Runtime Broker high CPU is to stop thinking of it as a Runtime Broker problem. It's an app problem wearing a broker costume. Kill the tips, revoke the background permissions, fix the triggering app, and the broker does what it was designed to do: sit at 0%, invisible, handling the occasional permission check like a professional. If you ever see it spike again in the future, you'll know exactly where to look — the last Store app you installed or updated is always suspect number one.
