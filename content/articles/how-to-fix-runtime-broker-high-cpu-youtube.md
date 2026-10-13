---
title: "How to Fix Runtime Broker High CPU Usage in Windows 11"
slug: how-to-fix-runtime-broker-high-cpu-youtube
date: 2026-09-02
categories: ["performance"]
tags: ["runtime broker", "high cpu", "windows 11", "uwp apps", "troubleshooting"]
description: "RuntimeBroker.exe spiking your CPU? Learn what Runtime Broker does, why it misbehaves, and the app-permission fixes that calm it down."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-youtube.webp"
faqs:
  - q: "What does Runtime Broker actually do?"
    a: "Runtime Broker is a Windows system process that manages permissions for Microsoft Store (UWP) apps — it checks whether an app is allowed to access your location, camera, microphone, and other sensitive resources. It launches briefly when you open a Store app and should exit when the app closes. Normal usage is near zero; sustained high CPU means a Store app is misbehaving or a permission check is looping."
  - q: "Can I disable or end Runtime Broker?"
    a: "You can end the task temporarily in Task Manager and Windows will restart it as needed — that's harmless. But you shouldn't permanently disable it, because Store apps depend on it for permission management. The correct approach is fixing the app or permission that's making the broker work overtime, which the steps below do without breaking anything."
  - q: "Why does Runtime Broker use CPU when I'm not running any Store apps?"
    a: "Because Store apps also run background tasks: live tiles updating, notifications, background sync for mail and calendar, and Cortana-era leftovers. A misbehaving background task — especially the Photos app indexing or a Store app stuck updating — keeps the broker active indefinitely. The background-permission audit in Fix 3 finds these silent consumers."
  - q: "Is RuntimeBroker.exe a virus?"
    a: "The legitimate RuntimeBroker.exe lives in C:\\Windows\\System32 and is a genuine Microsoft process. Malware occasionally impersonates the name, so verify the file location: right-click the process in Task Manager → Open file location. If it points anywhere other than System32, run a full Defender scan immediately. If it's in System32, it's the real broker with a configuration problem."
---

RuntimeBroker.exe sitting at 20–40% CPU in Task Manager looks alarming — the name sounds important, the usage looks wrong, and ending it feels risky. Here's the reassuring truth: Runtime Broker is a middleman. It manages permissions for Microsoft Store apps, and when it's burning CPU, it's because some Store app is making it work overtime. Fix the app, and the broker goes quiet.

The pattern is distinctive: Runtime Broker spikes when you open certain Store apps (Photos, Mail, Xbox), or it grinds constantly because a background Store task is stuck. This guide identifies which app is driving the broker and shuts down the misbehavior — without disabling a system process you actually need.

## Why this happens

- **Misbehaving Store app:** A buggy UWP app making repeated permission requests keeps the broker busy.
- **Stuck background task:** Live tiles, notifications, or sync tasks looping instead of completing.
- **Photos app media indexing:** The Photos app scanning large libraries triggers constant broker-mediated access checks.
- **Too many apps with background permission:** Dozens of Store apps waking for background work multiply broker activity.
- **Corrupted Store app state:** A damaged app installation causing permission-check failures and retries.
- **Tips and suggestions content:** Windows tips/notifications pulling Store content on schedules.
- **Malware impersonation:** Rare, but a fake RuntimeBroker.exe outside System32 burns CPU maliciously.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's the real broker and find the driving app

Right-click RuntimeBroker.exe in Task Manager → Open file location. It must be `C:\Windows\System32` — anything else means malware, and you should run a full Microsoft Defender scan immediately. Assuming it's legitimate, note when the spike happens: right after opening a specific Store app? Constantly? Correlate the broker's CPU with your app usage for a few minutes. If it spikes with the Photos app open, that's your driver; if it's constant with no apps open, it's a background task (Fix 3). This correlation is the diagnosis everything else builds on.

1. Verify the process location is C:\Windows\System32.
2. Run a Defender scan if the location is anywhere else.
3. Correlate broker CPU spikes with specific app usage.
4. Note whether usage is app-triggered or constant.

### Fix 2: End the task and update the offending Store app

End the RuntimeBroker.exe task in Task Manager — Windows restarts it on demand, so this is safe and often provides immediate relief if the broker was wedged. Then open the Microsoft Store → Library and update all apps, especially the one you correlated with the spike. Outdated Store apps carry the permission-handling bugs that overwork the broker. If a specific app (Photos is the classic) keeps triggering spikes after updating, reset it via **Settings → Apps → Installed apps → Advanced options → Reset**. The reset clears corrupted state without deleting your files.

1. End the Runtime Broker task for immediate relief.
2. Update all Microsoft Store apps.
3. Reset the specific app correlated with spikes.
4. Verify the broker stays quiet after the reset.

### Fix 3: Audit Store app background permissions

This is the permanent fix for constant broker activity. Go to **Settings → Apps → Installed apps** and, for every Store app you don't actively use, open Advanced options and set background permission to Never. Be thorough — weather, news, sports, and Xbox-adjacent apps all schedule background work by default. Then check **Settings → System → Notifications** and disable "Get tips and suggestions" and similar Store-content notifications. Fewer background tasks means fewer permission checks, which means an idle broker. Re-check Task Manager after an hour: constant broker CPU should be gone.

1. Set background permission to Never for unused Store apps.
2. Disable tips, suggestions, and Store-content notifications.
3. Wait an hour and check broker CPU in Task Manager.
4. Re-enable background only for apps you genuinely need live.

### Fix 4: Tame the Photos app specifically

The Photos app deserves its own fix because it's the most common broker driver: it indexes your picture library, generates People tags, and syncs with OneDrive — all broker-mediated. Open Photos → Settings and turn off People detection, OneDrive-linked folders you don't need indexed, and automatic album creation. If you don't use Photos at all, set its background permission to Never or uninstall it and use an alternative viewer. Users with large photo libraries often see broker CPU drop to zero from this fix alone. Microsoft documents Photos settings in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Photos settings and disable People detection.
2. Remove unneeded folders from the Photos library.
3. Turn off automatic album creation.
4. Set Photos background to Never if you don't use it.

### Fix 5: Repair the Store app platform

If broker CPU is high with no clear app driver, the Store platform itself may be damaged. Run `wsreset.exe` from the Run dialog (Win+R) — it clears the Store cache without touching installed apps. Then run the Windows Store Apps troubleshooter in **Settings → System → Troubleshoot → Other troubleshooters**. For deeper damage, re-register the Store platform with PowerShell: `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}` in an admin shell. This rebuilds the app registrations the broker mediates. Reboot afterward and verify.

1. Run `wsreset.exe` to clear the Store cache.
2. Run the Windows Store Apps troubleshooter.
3. Re-register app packages via admin PowerShell if needed.
4. Reboot and confirm broker idles near zero.

### Fix 6: Reduce notification and lock-screen broker work

The broker also mediates lock-screen and notification content from Store apps. In **Settings → Personalization → Lock screen**, set the lock screen status to None instead of a detailed app. In **Settings → System → Notifications**, turn off notification banners for chatty Store apps. These are small individual savings, but on systems where the broker never fully idles, they remove the last drips of background permission work. Combined with the background audit from Fix 3, the broker should now only wake briefly when you actually open a Store app — which is its correct behavior. For the broader idle-CPU picture, the [Lenovo high-CPU guide](/articles/how-to-fix-high-cpu-usage-on-lenovo-laptop/) demonstrates the same identify-then-fix method.

1. Set lock screen app status to None.
2. Disable banners for chatty Store apps.
3. Confirm the broker only spikes when opening Store apps.
4. Treat any return of constant usage as a new stuck task — repeat Fix 3.

## Closing

Runtime Broker is never the villain — it's the messenger telling you a Store app is misbehaving. Verify the process is legitimate, find the driving app, update or reset it, audit background permissions, and tame the Photos app. The broker will fade back to its proper role: briefly active, mostly invisible, near zero CPU. For the update-triggered variant of this problem, see the [post-update Runtime Broker guide](/articles/how-to-fix-runtime-broker-high-cpu-after-windows-11-update/).
