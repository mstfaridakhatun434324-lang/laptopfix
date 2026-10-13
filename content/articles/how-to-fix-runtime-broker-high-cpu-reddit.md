---
title: "Runtime Broker High CPU: What the Reddit Fixes Actually Get Right"
slug: how-to-fix-runtime-broker-high-cpu-reddit
date: 2026-09-24
categories: ["performance"]
tags: ["runtime broker", "high cpu", "windows 11", "troubleshooting", "reddit"]
description: "RuntimeBroker.exe eating CPU on your Windows 11 laptop? This guide separates the real fixes from forum folklore, so you can diagnose and calm it down."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-reddit.webp"
faqs:
  - q: "What is RuntimeBroker.exe and why does it use so much CPU?"
    a: "Runtime Broker is a legitimate Windows process that manages permissions for Universal Windows Platform (UWP) apps — things like Photos, Settings, and Store apps. It should idle near 0% CPU. Sustained usage above 5 to 10 percent at idle usually means a misbehaving UWP app is hammering it with permission requests, or its own configuration is corrupted. It is not a virus."
  - q: "Is it safe to end the Runtime Broker task in Task Manager?"
    a: "Yes, ending RuntimeBroker.exe in Task Manager is safe; Windows restarts it automatically, and closing it only suspends the permission checks for UWP apps momentarily. If CPU drops after you end it and stays down, something a Store app was doing triggered the spike. If it climbs right back up, you have a recurring trigger — a misbehaving app, tips, or corrupted system files — that the fixes below address."
  - q: "Why does Reddit say to disable the Windows tips feature for this?"
    a: "Because it works often enough to be famous. Windows 11's Tips and Suggestions service wakes Runtime Broker repeatedly to show hints, and on some machines this turns into a constant polling loop. Disabling tips under Settings, System, Notifications removes that stimulus entirely. It is a genuine fix for one common trigger, not a cure for every Runtime Broker problem."
  - q: "Can Runtime Broker high CPU be caused by malware?"
    a: "Rarely, but it happens: malware can disguise itself as RuntimeBroker.exe by running from a folder other than System32, or a compromised UWP app can abuse the broker. Verify the genuine process path in Task Manager's Details tab. Then run a full Microsoft Defender scan before assuming it is a bug — ruling out malware first is the correct order of operations."
---

**RuntimeBroker.exe** is one of those processes that should be invisible. Its job is quiet plumbing: it brokers permissions between Universal Windows Platform apps (Photos, Settings, the Microsoft Store, widgets) and the system resources they request. At idle it should sit near 0% CPU. So when it climbs to 10, 20, or even 40% and stays there, the laptop gets hot, the fan spins up, and battery life falls off a cliff — which is exactly what brings people to Reddit looking for answers.

The problem with forum threads is that they mix real fixes, placebo tweaks, and outright dangerous advice in one comment chain. This guide is the technician's cut: which reported fixes actually work, what each one is really doing, and how to diagnose the true trigger before you change anything.

## Why this happens

- **A misbehaving UWP app hammering permission requests:** One buggy Store app asking for location, camera, or background access in a tight loop keeps the broker busy indefinitely.
- **Windows tips and suggestions polling:** The Tips service repeatedly wakes Runtime Broker to surface hints; on some systems this becomes a constant background loop.
- **Corrupted UWP app packages:** A damaged Photos, Groove, or third-party Store app can send malformed requests the broker chokes on.
- **Misconfigured privacy settings:** Conflicting app-permission settings cause repeated request/deny cycles between the app and the broker.
- **Outdated or buggy app updates:** A bad Store app update can introduce the loop; the spike often starts right after an app or OS update.
- **Corrupted system files:** Damage to the broker's own components or the UWP runtime produces persistent elevated CPU with no app to blame.
- **Malware impersonation:** A fake RuntimeBroker.exe running from a non-standard path burns CPU while hiding in plain sight.
- **Groove Music and Photos indexing loops:** These two apps are frequent offenders — Groove scanning a huge music library, Photos syncing large collections.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm which process is actually busy

Open Task Manager, go to the Details tab, right-click the column headers and add **Command line**. Find RuntimeBroker.exe and check two things: the path (genuine ones live in `C:\Windows\System32`) and which apps it is tied to. Note the CPU percentage at idle over a few minutes. This baseline matters — it tells you whether any later fix actually worked, and the path check rules out impersonating malware. For broader guidance on taming heavy system processes, see [Windows Defender high CPU fixes](/articles/how-to-fix-windows-defender-high-cpu-usage-in-windows-11-24h2/) which use the same diagnose-first method.

1. Open Task Manager (Ctrl+Shift+Esc) → Details tab.
2. Add the Command line column; verify RuntimeBroker.exe runs from System32.
3. Record its CPU at idle for 3–5 minutes as your baseline.
4. Proceed only if sustained idle usage is clearly abnormal (several percent or more).

### Fix 2: End the task and watch what happens

Right-click RuntimeBroker.exe and choose End task. Windows restarts it automatically — this is safe and only briefly pauses UWP permission checks. Now watch: if CPU stays low, the trigger was a one-off event and you're done. If it climbs back within minutes, a recurring trigger exists and you continue. Note which apps you had open when it returns; the Photos app, Groove Music, or the Widgets board are classic suspects worth closing one at a time to test.

1. End RuntimeBroker.exe in Task Manager.
2. Wait 10 minutes with normal light use; watch CPU.
3. If it stays low: trigger was transient — nothing further needed.
4. If it returns: note which apps were open and continue to Fix 3.

### Fix 3: Disable Windows tips and suggestions

Settings → System → Notifications → Additional settings, and uncheck both "Show the Windows welcome experience" and "Get tips and suggestions when using Windows." This kills the Tips service's polling of the broker. Restart and recheck idle CPU. This single toggle resolves a large share of reported cases — it's the Reddit fix that survives scrutiny — but if your CPU is unchanged after a reboot, the trigger is an app or corruption, not tips.

1. Open Settings → System → Notifications.
2. Expand Additional settings.
3. Uncheck "Show the Windows welcome experience" and "Get tips and suggestions when using Windows."
4. Restart and recheck idle CPU.

### Fix 4: Isolate the offending UWP app

Open Settings → Apps → Installed apps and sort by install date; if the spike started after a Store app update, start there. For each suspect (Photos, Groove Music, Mail, Widgets-linked apps): open its Advanced options, terminate it, reset it, and — for Groove especially — remove huge libraries from its scan scope. Test idle CPU after each change so you know which app was the trigger. Once identified, either keep it reset, limit its background permissions, or uninstall it.

1. Settings → Apps → Installed apps → pick a suspect app.
2. Open Advanced options → Terminate, then Repair; if that fails, Reset.
3. For Groove: remove large music folders from its library scope.
4. Recheck idle CPU after each app change.

### Fix 5: Tighten app permissions and background access

Settings → Privacy & security: review Location, Camera, and Microphone permissions — revoke access for apps that don't need them, since denied-but-retrying requests keep the broker busy. Then go to Apps → Installed apps → each suspect's Advanced options → Background apps permissions → set to Never for apps you don't need running behind the scenes. Fewer background apps means fewer permission requests for the broker to service. This is also a good moment to trim general slowdowns using a [broader speed-up pass](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

1. Settings → Privacy & security → revoke Location/Camera/Mic for unneeded apps.
2. For each suspect app → Advanced options → Background apps permissions → Never.
3. Restart and verify idle CPU.

### Fix 6: Repair UWP packages and system files

Open Terminal as administrator and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`. These repair the UWP runtime and the broker's own files. Also re-register the Store app packages with the standard PowerShell command documented on the [Microsoft support site](https://support.microsoft.com/en-us/windows) if Photos or other in-box apps are the suspects. Reboot, then recheck. If corruption was the cause, idle CPU should now be near zero; persistent elevation after clean SFC/DISM points to a third-party app or a deeper issue.

1. Admin Terminal: run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`; reboot.
3. Recheck idle CPU; continue if still elevated.

### Fix 7: Rule out malware with a full scan

If nothing above helped, run a full scan in Windows Security → Virus & threat protection → Scan options → Full scan. Malware masquerading as system processes is uncommon but exactly the kind of thing that survives all the legitimate fixes above. If the scan is clean and CPU is still high, an in-place upgrade repair (reinstalling Windows 11 while keeping files and apps, via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)) is the last resort before a clean install.

1. Windows Security → Virus & threat protection → Scan options → Full scan.
2. Remove anything found; reboot and recheck.
3. If clean but still broken: consider an in-place upgrade repair.

## Closing

Runtime Broker high CPU is almost always a trigger problem, not a broker problem — a chatty app, the tips service, or corrupted packages keeping a quiet process artificially busy. Work the list in order, measure idle CPU after each change, and you'll find the real trigger instead of collecting forum tweaks. Once the broker is back near zero at idle, your fan noise and battery drain usually resolve themselves along with it.
