---
title: "Fix Runtime Broker High CPU Usage in Windows 11 24H2"
slug: "how-to-fix-runtime-broker-high-cpu-in-windows-11-24h2"
date: "2026-09-24"
categories: ["performance"]
tags: ["runtime broker", "high cpu", "windows 11 24h2", "uwp apps", "performance"]
description: "Runtime Broker chewing CPU in Windows 11 24H2? Learn what it does, which app is abusing it, and how to stop the spike."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "What is Runtime Broker (RuntimeBroker.exe)?"
    a: "Runtime Broker is a Windows system process that manages permissions for Microsoft Store (UWP) apps — it brokers their access to cameras, microphones, location, and files. It is supposed to use minimal CPU, briefly spiking when you launch a Store app. Sustained high CPU means a Store app is repeatedly requesting permissions or misbehaving behind it."
  - q: "Can I disable or end Runtime Broker?"
    a: "You can end it in Task Manager and Windows restarts it automatically, but you cannot and should not disable it — Store apps depend on it for permission handling. High Runtime Broker CPU is always a symptom of a misbehaving app, so the fix is finding and fixing that app, not attacking the broker."
  - q: "Why are there multiple RuntimeBroker.exe processes?"
    a: "That is normal. Windows runs one Runtime Broker instance per logged-in user session plus instances tied to active Store apps. Seeing two or three instances is expected and harmless. Worry only when one instance sustains high CPU, which points to the specific app attached to that instance."
  - q: "Does Runtime Broker high CPU drain the battery?"
    a: "Yes — any sustained CPU usage prevents the processor from entering low-power states, which directly reduces battery life. On laptops, a Runtime Broker stuck at 15–30% CPU can shave a noticeable chunk off runtime. Fixing the underlying app restores both performance and battery life."
---

**RuntimeBroker.exe** is one of those processes that should be invisible: it manages permissions for Microsoft Store apps and typically idles at 0% CPU. When it instead sits at 15–40% indefinitely in Windows 11 24H2, something is wrong — but the broker itself is never the problem. It is doing work on behalf of a Store app that is misbehaving: hammering permission requests, stuck in a background loop, or corrupted after the 24H2 update.

The diagnostic challenge is attribution. Task Manager shows the broker's CPU, not the app causing it. This guide's core skill is tracing a hot Runtime Broker instance back to its app — via the Details tab, Event Viewer, and selective app isolation — then fixing that app. Work the sequence in order and you will find the culprit instead of stabbing in the dark.

24H2 specifically deserves mention: the update re-registers Store app packages and resets several privacy-permission defaults, which is why Runtime Broker spikes cluster after feature updates. The fixes account for that.

## Why this happens

- **Misbehaving Store app:** A buggy UWP app repeatedly requesting permissions or running a background loop.
- **Post-24H2 re-registration:** The update re-registers app packages, sometimes leaving them in a broken permission-request loop.
- **Tips and suggestions:** Windows' "Get tips" content and suggested apps generate broker activity.
- **Live Tiles/background tasks:** Store apps with background tasks (mail, news, weather) waking frequently.
- **Corrupted app package:** A damaged Store app installation causing repeated broker-mediated failures.
- **Privacy setting loops:** An app denied a permission retrying the request aggressively instead of handling denial.
- **Multiple user sessions:** Fast-user-switching sessions each running broker instances for their apps.
- **Windows Spotlight/lock screen:** Spotlight's content fetching runs through broker-mediated app activity.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which app the hot broker instance serves

Open Task Manager's **Details** tab, find the RuntimeBroker.exe with high CPU, and check its **User name** and command line (add the Command line column). Then open **Settings > Privacy & security** and review which apps recently used camera, microphone, or location — a Store app with constant recent access is your prime suspect. Also check **Settings > Apps > Installed apps**, sort by install date, and note anything updated around when the problem started (often right after 24H2). Write down 2–3 suspects before changing anything. The after-update Runtime Broker variant is covered in our [Runtime Broker after-update guide](/articles/how-to-fix-runtime-broker-high-cpu-after-windows-11-update/).

1. In Task Manager **Details**, find the high-CPU RuntimeBroker.exe.
2. Check its user and command line; note the PID.
3. Review **Privacy & security** for apps with constant recent permission use.
4. List 2–3 suspect Store apps.

### Fix 2: Disable "Show me tips" and suggested content

Windows' tips, tricks, and suggested apps generate surprising broker activity — the Tips app and suggestions pipeline are Store-app components that poll regularly. Turn off **Get tips and suggestions when using Windows** (Settings > System > Notifications) and disable **Suggested content** in Settings. This is the quickest, safest first intervention, and on many machines it alone drops Runtime Broker to zero because the suggestions engine was the app hammering it.

1. Go to **Settings > System > Notifications**.
2. Turn off **Get tips and suggestions when using Windows**.
3. Disable suggested content/start suggestions in Personalization.
4. Wait 10 minutes and check Runtime Broker CPU.

### Fix 3: Restrict background activity for suspect apps

If tips were not the cause, throttle the suspects from Fix 1. For each suspect Store app, open **Settings > Apps > Installed apps > ··· > Advanced options** and set **Background apps permissions** to **Never**. This stops their background tasks — the usual source of broker loops — while leaving the apps fully usable when opened manually. Apply to one suspect at a time, waiting 10 minutes between each, so you can identify the exact offender by the CPU drop. This binary-search approach beats disabling everything blindly.

1. Open each suspect app's **Advanced options**.
2. Set **Background apps permissions** to **Never**.
3. Do one app at a time; wait 10 minutes and check CPU.
4. The app whose restriction drops CPU is the culprit.

### Fix 4: Repair or reset the culprit app

Once identified, fix the app rather than just silencing it. On its **Advanced options** page, click **Repair** first — this fixes damaged files while keeping data. If CPU remains high, click **Reset**, which clears the app's data and returns it to fresh-install state (you may need to sign in again). For inbox apps like Photos, Mail, or Cortana/Search components, reset is safe and routinely fixes post-24H2 broker loops caused by corrupted re-registration. Re-test background permissions afterward.

1. On the culprit app's **Advanced options** page, click **Repair**.
2. Check Runtime Broker CPU for 15 minutes.
3. If still high, click **Reset** and reconfigure the app.
4. Re-verify CPU with background permissions as desired.

### Fix 5: Re-register all Store apps (24H2 corruption repair)

When no single app stands out — or several broker instances are hot — the 24H2 re-registration itself may be corrupt across packages. Re-register the built-in app packages with PowerShell: `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`. This re-lays every manifest cleanly, fixing the broken registrations 24H2 sometimes leaves. It takes several minutes and shows red errors for system packages that cannot re-register — those are normal and safe to ignore. Microsoft documents app re-registration on the official [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open **PowerShell as administrator**.
2. Run the Get-AppXPackage re-registration command above.
3. Ignore expected red errors for system packages.
4. Restart and check Runtime Broker CPU.

### Fix 6: Audit privacy permissions for looping apps

A common loop pattern: an app denied camera/microphone/location access retries the request aggressively instead of accepting denial, and each attempt goes through the broker. Review **Settings > Privacy & security** permission pages (Camera, Microphone, Location) and either grant access to the legitimate app that keeps asking or uninstall it if you do not trust it. Also check **App diagnostics** and **Background apps** master toggles. The goal is no app in a permanent request-deny-retry cycle — every permission decision should be final.

1. Review Camera/Microphone/Location permission pages.
2. Grant or uninstall for each repeatedly-requesting app.
3. Check **Background apps** master toggle state.
4. Confirm no app is stuck in a permission loop.

### Fix 7: Uninstall the offender if it's non-essential

If the culprit is a preinstalled Store app you never use — news, sports, trial games, vendor bloat delivered via the Store — remove it. Uninstalling from **Settings > Apps** eliminates its broker traffic permanently. For inbox apps that cannot be uninstalled normally, PowerShell removal (`Get-AppxPackage *name* | Remove-AppxPackage`) works; be conservative and only remove apps you recognize as non-essential. After removal, verify the hot broker instance is gone and stays gone across a reboot. A related Lenovo-nuisance cleanup is our [Widgets CPU guide](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-dell-laptop/) — different process, same principle of removing what you never use.

1. Uninstall the culprit via **Settings > Apps** (or PowerShell for inbox apps).
2. Restart the laptop.
3. Confirm no RuntimeBroker.exe sustains high CPU.
4. Reinstall from the Store later only if needed.

## Closing

Runtime Broker high CPU is a whodunit with a reliable detective method: find the hot instance, list the suspect apps, silence them one by one until the CPU drops, then repair or remove the offender. The broker was never guilty — it was just the process where a misbehaving Store app's bad manners showed up. Identify the app, and the case closes.
