---
title: "Runtime Broker High CPU on an ASUS Laptop: Fix Guide"
slug: how-to-fix-runtime-broker-high-cpu-on-asus-laptop
date: 2026-09-05
categories: ["performance"]
tags: ["runtime broker", "high cpu", "asus laptop", "windows 11", "troubleshooting"]
description: "RuntimeBroker.exe spiking CPU on your ASUS laptop? Learn what Runtime Broker does, why it misbehaves on ASUS machines, and how to stop it step by step."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-on-asus-laptop.webp"
faqs:
  - q: "What is Runtime Broker and is it safe to end the task?"
    a: "Runtime Broker is a legitimate Windows process that manages permissions for Microsoft Store (UWP) apps — camera, microphone, location access. Ending it in Task Manager is safe and it restarts automatically, but it's only a temporary reset: if an app is misbehaving, the broker will climb again. Use the end-task as a diagnostic step, then apply the permanent fixes in this guide."
  - q: "Why does Runtime Broker use more CPU on ASUS laptops specifically?"
    a: "ASUS laptops ship with MyASUS, Armoury Crate, and other UWP-style utilities that talk to Runtime Broker constantly for sensor and permission data. After updates to these apps, or when one hangs while requesting location or notification access, the broker can get stuck in a permission-check loop. The ASUS-specific fixes below target exactly these utilities."
  - q: "Can I permanently disable Runtime Broker?"
    a: "No — and you shouldn't try. It's a core Windows component; Store apps and several system features depend on it. Registry hacks that claim to disable it break app permissions and can destabilize the system. The correct approach is fixing the app or setting that's making the broker work overtime, which restores it to its normal near-zero idle usage."
  - q: "How much CPU should Runtime Broker normally use?"
    a: "At idle it should sit at 0–1%. Brief spikes to 10–20% when launching a Store app or changing a permission are normal and should settle within a minute. Sustained usage above 15–20% for hours, especially at idle with no Store apps open, is the problem pattern this guide fixes."
---

RuntimeBroker.exe is one of those Windows processes that should be invisible — and when it isn't, you notice fast. On ASUS laptops it has a habit of climbing to 20, 40, sometimes 60 percent CPU and staying there, spinning up the fans and chewing through battery while you do nothing more demanding than stare at the desktop. Task Manager shows the name, but gives you no clue why a "broker" needs that much processor.

The short version: Runtime Broker isn't the villain — it's the middleman. It manages permissions for Microsoft Store apps, and when one of those apps (very often an ASUS utility like MyASUS or Armoury Crate) misbehaves, the broker gets stuck doing its bidding. Fix the app or the permission, and the broker goes quiet. Here's how, in order.

## Why this happens

- **A hung Store app:** A UWP app stuck requesting permissions keeps the broker in a retry loop indefinitely.
- **ASUS utility chatter:** MyASUS, Armoury Crate, and ASUS utilities poll sensors and permissions through the broker constantly.
- **Tips and suggestions:** Windows' "suggestions" features behave like Store apps and generate broker activity.
- **Live tiles and notifications:** Apps with live tiles or heavy notification traffic keep broker threads alive.
- **Corrupted Store app data:** A damaged app package makes the broker repeatedly attempt and fail permission checks.
- **Location permission loops:** An app granted location access that can't get a fix retries through the broker.
- **Post-update Store app churn:** After Windows or ASUS app updates, apps re-register and re-request permissions en masse.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Runtime Broker is the problem and reset it

Open Task Manager, sort by CPU, and confirm RuntimeBroker.exe is genuinely the top consumer — sustained above 15 percent at idle, not a brief spike. Right-click it and choose **End task**; Windows restarts it automatically within seconds. Watch for 10 minutes: if CPU stays low, you've confirmed a stuck state rather than constant demand, and the permanent fixes below will keep it quiet. If it climbs right back, note which Store apps you had open — that's your prime suspect. The [general Runtime Broker fix guide](/articles/best-way-to-fix-runtime-broker-high-cpu/) covers the same ground for non-ASUS systems.

1. Open Task Manager and sort by CPU to confirm RuntimeBroker.exe.
2. Right-click RuntimeBroker.exe and choose **End task**.
3. Observe for 10 minutes with no Store apps open.
4. Note whether it stays low (stuck state) or climbs back (active demand).

### Fix 2: Turn off Windows tips, tricks, and suggestions

This is the single most effective quick fix. **Settings → System → Notifications** — turn off **Get tips and suggestions when using Windows**. These suggestion features run as Store-app-like processes and are a documented Runtime Broker trigger. While there, review **Settings → Privacy & security** and disable background activity for Store apps you never use. Reboot and check Task Manager; for many ASUS users this alone drops the broker back to near zero.

1. Open **Settings → System → Notifications**.
2. Turn off **Get tips and suggestions when using Windows**.
3. Go to **Settings → Privacy & security** and limit Store app background activity.
4. Reboot and re-check Runtime Broker CPU.

### Fix 3: Update or repair MyASUS and Armoury Crate

ASUS's own utilities are the most common ASUS-specific trigger. Open the **Microsoft Store → Library** and update MyASUS, Armoury Crate, and any other ASUS app. If the broker spikes when one of these is running, reset it: **Settings → Apps → Installed apps**, find the app, open **Advanced options**, and use **Repair** first, then **Reset** if repair doesn't help. A freshly reset ASUS utility re-registers cleanly and stops hammering the broker. For ASUS utilities, the Microsoft Store versions update most reliably — use those rather than third-party download sites.

1. Open Microsoft Store → Library and update all ASUS apps.
2. Go to **Settings → Apps → Installed apps** and find MyASUS.
3. Open **Advanced options** and click **Repair**.
4. If CPU persists, use **Reset** and reconfigure the app.

### Fix 4: Audit which Store apps have background and location permissions

A single misbehaving app with location or background permission can pin the broker. Go to **Settings → Privacy & security → Location** and turn off location for apps that don't need it — or disable location services entirely as a test. Then check **Settings → Apps → Installed apps** for Store apps you don't recognize or never use; uninstall them. Pay special attention to preinstalled ASUS partner apps and trial software, which are frequent offenders. Fewer apps with permissions means fewer broker threads.

1. Open **Settings → Privacy & security → Location** and restrict access.
2. Review **Settings → Apps → Installed apps** for unused Store apps.
3. Uninstall preinstalled apps you never open.
4. Reboot and monitor Runtime Broker for an hour.

### Fix 5: Re-register Store apps with PowerShell

If the broker is stuck because of a corrupted app package, re-registering the Store apps fixes it. Open PowerShell as administrator and run the re-registration command for all users' provisioned apps. This doesn't delete your data — it re-registers the app manifests so permission checks complete instead of looping. Run it, reboot, and watch Task Manager. If a specific app was the problem, the broker settles within minutes of the reboot. Microsoft documents Store app repair steps in the [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the official reference.

1. Open PowerShell as administrator.
2. Run the app re-registration command for provisioned packages.
3. Wait for completion (ignore red errors for system packages).
4. Reboot and verify Runtime Broker stays at 0–1% at idle.

### Fix 6: Disable live tiles and background Store activity

For stubborn cases, cut the broker's workload directly. In **Settings → Apps → Installed apps**, open **Advanced options** for chatty Store apps (news, weather, social) and set **Background apps permissions** to Never. Unpin live tiles from Start for apps you don't need updating. Finally, review **Task Manager → Startup apps** and disable ASUS and third-party updaters you don't need at boot — the [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) walks through auditing these safely. Less background activity means the broker has nothing to broker.

1. Set background permissions to Never for chatty Store apps.
2. Unpin live tiles you don't need.
3. Disable unneeded startup entries in Task Manager.
4. Reboot and confirm the fix holds over a full day.

## Closing

Runtime Broker is a messenger, not the problem — on ASUS laptops the message almost always comes from an ASUS utility, a Store app permission loop, or Windows' own suggestions feature. Work the list top to bottom and you'll find the broker back at zero where it belongs. If it ever climbs again, you'll know exactly where to look first: Task Manager, the suspect app, and its permissions.
