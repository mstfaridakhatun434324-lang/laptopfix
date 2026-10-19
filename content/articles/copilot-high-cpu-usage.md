---
title: "Copilot High CPU Usage? How to Calm It Down"
slug: copilot-high-cpu-usage
date: 2026-10-19
categories: ["ai-pc"]
tags: ["copilot", "high cpu", "performance", "windows 11", "task manager"]
description: "Copilot using too much CPU on Windows 11? Learn what makes Copilot spike processor usage and how to bring it back to normal."
thumbnail: "/images/thumbs/copilot-high-cpu-usage.webp"
faqs:
  - q: "Why is Copilot using 30% CPU when I am not even using it?"
    a: >
      Background Copilot processes sometimes get stuck in a loop — indexing, syncing, or retrying a failed network call. Ending the stuck process in Task Manager usually drops usage to zero instantly. If it keeps recurring, a corrupted cache or outdated app is the deeper cause.
  - q: "Is high CPU from Copilot a sign of malware?"
    a: >
      Genuine Copilot processes run from Microsoft's app folders. If Task Manager shows a "Copilot" process running from a strange location or with a misspelled name, that is suspicious. Right-click it, open the file location, and verify it points to a legitimate Microsoft path.
  - q: "Does Copilot use the NPU or CPU for its work?"
    a: >
      On Copilot+ PCs, some on-device AI tasks run on the NPU, but the app's interface, networking, and background sync still use the CPU. High CPU with low NPU usage usually means the app is stuck on non-AI work like syncing or retrying connections.
  - q: "Will limiting Copilot break Windows?"
    a: >
      No. Copilot is not a core Windows component. Restricting its background activity, disabling its startup entry, or even uninstalling it does not affect system stability.
---

You glance at Task Manager and there it is: Copilot, an app you barely opened today, chewing through 25, 40, even 70 percent of your CPU. Your fan spins up, your battery drains, and everything feels sluggish — all courtesy of an assistant that was supposed to be helping.

High CPU from Copilot is almost never "normal AI work." When Copilot is genuinely answering a question, a brief spike is expected. But sustained high usage, especially when you are not interacting with it, means something is stuck: a looping background sync, a failed network retry, a corrupted cache, or a runaway renderer process. If the app is also misbehaving in other ways, our [Copilot app crashing](/articles/copilot-app-crashing/) guide covers the stability side; for launch problems see [Copilot not available in your region](/articles/copilot-not-available-in-my-region/) only if region blocks are involved.

Here is how to find the culprit process and calm it down.

## Why this happens

- **Stuck background sync:** A failed sync or network retry can loop forever, pinning a CPU core.
- **Corrupted cache:** Damaged local data makes the app thrash instead of working smoothly.
- **Runaway WebView renderer:** The embedded browser process sometimes spins out of control.
- **Outdated app version:** Older builds had known CPU bugs that updates fixed.
- **Startup bloat:** Copilot launching at boot and doing background work you never asked for.
- **Malware impersonation:** Rare, but fake "Copilot" processes from shady locations are a real threat vector.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact offending process
Not all CPU usage labeled "Copilot" is the same. Find precisely what is burning cycles.

1. Open Task Manager with Ctrl + Shift + Esc and go to the Processes tab.
2. Click the CPU column to sort by usage, highest first.
3. Expand the Copilot entry to see its child processes — note which one (renderer, GPU process, utility) is the hog.
4. Right-click the hogging process, choose "Open file location," and verify it is a legitimate Microsoft path.
5. If the location looks wrong or the name is misspelled, treat it as malware: run a full Windows Security scan immediately.
6. For a legitimate process, note its name — you will target it in the next fixes.

### Fix 2: End the stuck process and watch for recurrence
A one-time stuck process is fixed in seconds. Recurrence means a deeper problem.

1. In Task Manager, right-click the high-CPU Copilot process and choose End task.
2. Watch the CPU column for a minute. If usage drops to normal and stays there, it was a transient stuck process.
3. Reopen Copilot and use it normally. If CPU spikes again immediately, the trigger is reproducible — continue to Fix 3.
4. If it stays calm for hours then spikes later, something periodic (a sync job, an update check) is the trigger.
5. Make a note of when spikes happen — patterns like "every hour" or "on wake from sleep" are diagnostic gold.

### Fix 3: Disable Copilot at startup
If you do not use Copilot constantly, there is no reason for it to run from boot.

1. In Task Manager, go to the Startup apps tab.
2. Find Microsoft Copilot in the list. If its status is Enabled, right-click and choose Disable.
3. Restart your laptop and check Task Manager — Copilot should no longer appear until you launch it manually.
4. Use Copilot only when needed, then close it fully (right-click tray icon > Quit) instead of leaving it running.
5. This alone eliminates most "mystery CPU while idle" complaints.
6. If you later want it back at startup, re-enable it in the same tab.

### Fix 4: Repair, reset, and update the app
Corrupted data and old builds are the two most common persistent causes.

1. Go to Settings > Apps > Installed apps > Microsoft Copilot > Advanced options.
2. Click Repair, wait for the checkmark, and monitor CPU for a while.
3. If usage is still high, click Reset on the same page and confirm, then sign in again.
4. Open the Microsoft Store > Library > Get updates and install any Copilot update.
5. Also install pending Windows updates — app and OS fixes often ship together.
6. After updating, run Copilot for a full day of normal use before declaring victory; some spikes only appear under specific conditions.

### Fix 5: Check power settings and background permissions
Windows may be letting Copilot run wild in the background.

1. Go to Settings > Apps > Installed apps > Microsoft Copilot > Advanced options.
2. Under "Background apps permissions," change it from "Power optimized" to "Never" if you only use Copilot on demand.
3. Open Settings > System > Power & battery and confirm you are on Balanced, not Best performance, for daily use.
4. In Task Manager's Details tab, right-click the Copilot process > Set priority, and ensure it is Normal, not Above normal or High.
5. If you use a "game booster" or optimizer that raises app priorities, exclude Copilot from it.
6. These changes cap how aggressively Copilot can consume resources without affecting its functionality when you actually use it.

### Fix 6: Scan for impersonators and consider removal
If nothing else explains it, verify the process is genuine — then decide if Copilot earns its place.

1. In Task Manager, right-click the Copilot process > Properties and check the digital signature. Genuine Microsoft processes are signed by Microsoft.
2. Run a full scan with Windows Security (Virus & threat protection > Scan options > Full scan).
3. Check Task Scheduler for suspicious Copilot-named tasks you did not create.
4. If the process is genuine but you simply never use Copilot, the ultimate CPU fix is uninstalling it — see our guide on [how to check if your laptop is a Copilot+ PC](/articles/how-to-check-if-laptop-is-copilot-plus-pc/) first if you are unsure what you would lose.
5. After uninstalling, confirm in Task Manager that no Copilot processes remain.
6. Remember: on a healthy system, an idle Copilot should use essentially 0% CPU. Anything sustained above 5% at idle deserves investigation.

## Closing

Copilot has no business burning your CPU while you are not talking to it. The pattern is almost always the same: find the stuck process, end it, then fix the underlying cause — usually cache corruption, an old build, or an over-permissive startup entry. And if you catch a fake Copilot process running from a shady folder, you have found something far more important than a performance bug.
