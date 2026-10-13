---
title: "How to Fix Runtime Broker High CPU on Windows 10"
slug: how-to-fix-runtime-broker-high-cpu-on-windows-10
date: 2026-09-07
categories: ["performance"]
tags: ["runtime broker", "high cpu", "windows 10", "runtimebroker.exe", "cpu fix"]
description: "RuntimeBroker.exe using high CPU on Windows 10? Find the misbehaving Store app behind it and fix it with permissions, tile settings, and Store repairs."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-on-windows-10.webp"
faqs:
  - q: "Why is Runtime Broker using so much CPU on Windows 10?"
    a: "Runtime Broker manages permissions and background tasks for Microsoft Store apps. When one of those apps misbehaves — stuck in a permission loop, refreshing a live tile endlessly, or running a broken background task — the broker's CPU usage climbs. The process itself is healthy; it is overworked by an app. Finding that app is the entire fix."
  - q: "Is it safe to disable Runtime Broker on Windows 10?"
    a: "No, you should not disable it. Runtime Broker is part of the Universal Windows Platform infrastructure, and disabling it breaks Store apps and parts of the Settings app. The safe approach is identifying which app is driving it and fixing or removing that app. Think of the broker as a messenger — shooting it does not fix the message."
  - q: "Does the Photos app cause Runtime Broker high CPU?"
    a: "Frequently, yes. The Windows 10 Photos app runs background tasks for face detection, automatic albums, and OneDrive sync, all brokered through Runtime Broker. On large photo libraries these tasks can run for hours. Restricting the Photos app's background permissions or disabling its automatic features usually calms the broker immediately."
  - q: "Will this problem go away if I upgrade to Windows 11?"
    a: "Sometimes, since the upgrade reinstalls the app platform and resets app states — but it can also return, because the same misbehaving apps and permission patterns carry over. Fix the underlying app issue on Windows 10 first; the knowledge transfers, and you will know exactly what to check if it reappears after upgrading."
---

On Windows 10, RuntimeBroker.exe is a perennial Task Manager mystery: a system process you never launched, consuming CPU you never offered it, with no obvious off switch. The important thing to understand is that Runtime Broker is infrastructure — it brokers permissions (camera, location, microphone) and background activity for Microsoft Store apps. High CPU from the broker means high activity from some Store app it serves. Your job is to find the app.

Windows 10's version of this problem has its own flavor: live tiles, the older Photos app, Cortana remnants, and years of accumulated Store app cruft. Here is how to work through it.

## Why this happens

- **A Store app in a permission loop:** An app repeatedly requesting location, camera, or notification access keeps the broker mediating the same denied or stuck request.
- **Live tiles refreshing:** Windows 10's live tiles poll for content updates, and each update round-trips through the broker.
- **Photos app background analysis:** Face grouping, automatic albums, and OneDrive-linked processing run long broker-mediated background tasks.
- **Cortana and search remnants:** On builds where Cortana lingers, its background activity adds broker load even if you never invoke it.
- **Spotlight and suggestions:** Windows Spotlight lock screens and Start menu suggestions generate broker traffic on every lock, unlock, and Start open.
- **Corrupted app packages:** Damaged Store app installations cause failed permission checks that the broker retries indefinitely.
- **Groove/Movies & TV background tasks:** Legacy inbox apps with background permissions can churn quietly for years unnoticed.
- **Time broker and sync:** Time synchronization and account sync activities occasionally wedge and keep broker instances alive at high CPU.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Spot the pattern and the suspect

1. Open **Task Manager → Details**, find **RuntimeBroker.exe** instances, and note whether one or several show high CPU.
2. Correlate with your activity: does it spike on lock/unlock (Spotlight), when Photos is open (Photos app), or constantly (a background task)?
3. Open **Settings → Privacy** and scan which apps hold **Location**, **Camera**, and **Microphone** permissions — the broker mediates all of these, and the permission holders are your suspect list.
4. Write down the top suspects before changing anything. For the Windows 11 Dell-specific version of this hunt, see [Runtime Broker high CPU on Dell](/articles/how-to-fix-runtime-broker-high-cpu-on-dell-laptop/).

### Fix 2: Disable live tiles

1. Open the **Start menu**, right-click each live tile, and choose **More → Turn live tile off**.
2. Prioritize news, weather, finance, and third-party tiles — the ones that fetch remote content on a schedule.
3. Alternatively, unpin tiles you never look at — a tile you do not see should not be polling.
4. Live tiles are the most Windows-10-specific broker driver; silencing them resolves a large share of cases on this OS.

### Fix 3: Restrict background apps globally

1. Go to **Settings → Privacy → Background apps**.
2. Toggle off **Let apps run in the background** entirely, or leave the master on and disable it per-app for everything you do not need live.
3. Be selective about what keeps background access: messaging apps you rely on can stay; games, trials, and utilities you rarely open should not.
4. Restart and watch the broker for a day. Background restriction is the broadest single lever against broker CPU.

### Fix 4: Tame the Photos app

1. Open **Photos → Settings** and disable automatic album creation, face grouping, and any OneDrive-linked features you do not use.
2. Go to **Settings → Privacy → Background apps** and turn off background access for **Microsoft Photos** if you only open it manually.
3. For very large libraries, consider whether the Photos app's analysis is worth its cost — a simpler viewer avoids the background tasks entirely.
4. The Photos app is the single most common broker offender on Windows 10; this step alone fixes many cases.

### Fix 5: Silence Spotlight, tips, and suggestions

1. Go to **Settings → Personalization → Lock screen** and change from **Windows spotlight** to **Picture**.
2. Go to **Settings → System → Notifications & actions** and uncheck **Get tips, tricks, and suggestions as you use Windows**.
3. In **Settings → Privacy → General**, turn off **Show me suggested content in the Settings app**.
4. These Windows 10 features are constant low-grade broker irritants; disabling them is pure win. Our [tips and suggestions guide](/articles/best-way-to-turn-off-windows-tips-and-suggestions/) covers the complete silencing.

### Fix 6: Repair the Store app platform

1. Open **Settings → Update & Security → Troubleshoot → Additional troubleshooters → Windows Store Apps → Run the troubleshooter**.
2. For a deeper repair, open **PowerShell as administrator** and re-register app packages: `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
3. Corrupted packages cause the broker's retry loops; re-registration gives every app a clean manifest.
4. Restart afterward and monitor. Microsoft documents Store troubleshooting at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Remove or reset the offending app

1. Once you have identified the suspect app (Fix 1), try **Settings → Apps → select the app → Advanced options → Reset** first — this clears its corrupted state while keeping it installed.
2. If Reset does not help, **uninstall** it. Inbox apps that resist normal uninstall can often be removed via right-click in the Start menu.
3. For apps you need but which misbehave, check the Microsoft Store for updates — the misbehavior is sometimes a known bug fixed in a newer version.
4. Reinstall only if you actually use the app; otherwise let it stay gone.

### Fix 8: Verify with a clean profile test

1. Create a new local user (**Settings → Accounts → Family & other users → Add someone else to this PC → I don't have this person's sign-in information → Add a user without a Microsoft account**).
2. Log into the new profile and observe broker CPU for an hour of normal use.
3. Quiet in the new profile means your main profile's app data or permissions store is corrupt — migrate to the new profile rather than fighting it.
4. Noisy in both profiles means system-level corruption — run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` from an admin prompt, and consider a repair install. Keep drivers current via the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update is not offering them.

## Closing

Runtime Broker high CPU on Windows 10 is almost always one app's bad behavior amplified through system infrastructure — live tiles polling, the Photos app analyzing, or a corrupted package retrying. Find the app via permissions and patterns, restrict its background life, repair the platform, and remove what you do not need. The broker goes quiet not because you silenced it, but because nothing is shouting at it anymore.
