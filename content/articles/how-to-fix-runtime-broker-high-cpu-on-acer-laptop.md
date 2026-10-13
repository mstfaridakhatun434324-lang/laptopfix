---
title: "Runtime Broker High CPU on an Acer Laptop: How to Fix It"
slug: how-to-fix-runtime-broker-high-cpu-on-acer-laptop
date: 2026-09-14
categories: ["performance"]
tags: ["runtime broker", "high cpu", "acer laptop", "windows 11", "store apps"]
description: "RuntimeBroker.exe spiking on your Acer laptop? Find the Store app or permission loop behind it and apply these ordered fixes to silence it."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-on-acer-laptop.webp"
faqs:
  - q: "What does Runtime Broker actually do on my Acer laptop?"
    a: "Runtime Broker manages permissions for Microsoft Store apps — granting camera, microphone, location, and notification access — and handles communication between those apps and Windows. It's a lightweight middleman by design. When it uses significant CPU, a Store app is abusing it: usually one stuck in a permission-request loop or an Acer utility polling through it constantly."
  - q: "Why is Runtime Broker worse on budget Acer laptops?"
    a: "Budget Acer machines have less CPU headroom, so a broker stuck at 15% is far more noticeable than on a powerful machine where it blends into background noise. Acer's preinstalled utilities and partner apps also add Store-app activity that feeds the broker. The fixes are the same as on any Windows machine, but the relief is more dramatic here."
  - q: "Can I disable Runtime Broker with a registry tweak I found online?"
    a: "Don't. Registry tweaks claiming to disable Runtime Broker break Store app permissions, cause app crashes, and can destabilize Windows features that depend on it. Microsoft designed it as a required system component. Every legitimate fix targets the app or setting driving the broker's workload — which restores normal near-zero usage without breaking anything."
  - q: "Which Acer apps commonly trigger Runtime Broker CPU spikes?"
    a: "Acer Care Center, Acer Quick Access, and Acer's update utilities are the frequent offenders, especially after their Store updates. Preinstalled partner apps and trials that came with the machine also generate broker traffic. Updating these apps, resetting the misbehaving one, or uninstalling the ones you never open resolves most Acer-specific cases."
---

RuntimeBroker.exe shouldn't be a name you ever notice. It's Windows' permission middleman for Store apps — a process that should idle at zero and spike for seconds at most. So when Task Manager shows it holding 15, 25, or 40 percent CPU on your Acer laptop for hours, something is leaning on that middleman hard, and your battery and fans are paying for it.

On Acer machines the cause is usually in the preinstalled software stack: Acer utilities and partner apps generating constant permission traffic, or a Store app stuck in a request loop. This guide finds the driver of the load and quiets it, in order.

## Why this happens

- **Acer utility polling:** Acer Care Center and Quick Access constantly query sensors and permissions through the broker.
- **Hung Store app:** A Store app stuck requesting location, camera, or notification access loops forever.
- **Windows tips and suggestions:** These run as Store-like processes and are a documented broker trigger.
- **Preinstalled partner apps:** Trial and partner software phoning home through broker-mediated permissions.
- **Live tiles and notifications:** Chatty tiles keep broker threads alive around the clock.
- **Corrupted app packages:** Damaged Store app manifests cause repeated failed permission checks.
- **Post-update re-registration:** After Windows or app updates, apps re-request permissions en masse.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm and reset the broker

Open Task Manager, sort by CPU, and verify RuntimeBroker.exe is genuinely sustained above 10–15% at idle — ignore brief spikes when opening Store apps. Right-click it and choose **End task**; it restarts automatically. If CPU stays low for the next 10 minutes, it was a stuck state and the permanent fixes below keep it that way. If it climbs straight back, note which apps were open — the culprit is among them. The [best-practice Runtime Broker guide](/articles/best-way-to-fix-runtime-broker-high-cpu/) covers this same diagnostic in condensed form.

1. Verify sustained RuntimeBroker.exe CPU at idle in Task Manager.
2. End the task and let Windows restart it.
3. Observe for 10 minutes with Store apps closed.
4. Note which apps correlate with any rebound.

### Fix 2: Disable Windows tips and suggestions

The highest-yield quick fix: **Settings → System → Notifications** → turn off **Get tips and suggestions when using Windows**. These suggestion engines behave like Store apps and hammer the broker. While in Settings, go to **Privacy & security** and revoke background and location permissions from Store apps you never use. Reboot and check — this single change resolves a large share of broker cases on all brands, Acer included.

1. Turn off tips and suggestions in Notification settings.
2. Revoke background permissions from unused Store apps.
3. Restrict location access to apps that genuinely need it.
4. Reboot and verify broker CPU.

### Fix 3: Update, repair, or remove Acer utilities

Acer's own software is the prime Acer-specific suspect. Update Acer Care Center, Quick Access, and all Acer apps via **Microsoft Store → Library**. If the broker spikes alongside a specific Acer utility, reset it: **Settings → Apps → Installed apps → Advanced options → Repair**, then **Reset** if needed. For Acer utilities you never open, uninstall them outright — fewer broker clients, fewer problems. Keep only what you actually use; most users need none of them day-to-day. Check for driver-level Acer tools separately, since those aren't Store apps.

1. Update all Acer apps through the Microsoft Store.
2. Repair, then reset, any Acer app tied to the spikes.
3. Uninstall Acer utilities you never open.
4. Reboot and monitor for several hours.

### Fix 4: Purge preinstalled partner apps

The trial antivirus, shopping apps, and partner utilities that came with the machine generate broker traffic for permissions and notifications you'll never want. Go through **Settings → Apps → Installed apps** and uninstall everything you didn't choose to install — be thorough but avoid removing drivers and hardware utilities. Each removed app is one fewer permission-client hammering the broker. The [bloatware removal guide](/articles/how-to-remove-bloatware-from-windows-11-laptop/) walks through identifying safe removals brand by brand.

1. List apps in Settings → Apps → Installed apps.
2. Uninstall partner apps, trials, and software you didn't choose.
3. Keep drivers and genuine hardware utilities.
4. Reboot and check broker CPU at idle.

### Fix 5: Re-register Store apps and quiet notifications

If a corrupted app package is crash-looping through the broker, re-register: open PowerShell as administrator and re-register the provisioned Store app packages, then reboot. Separately, cut notification noise: **Settings → System → Notifications** — turn off notifications for chatty apps you don't need alerts from, and unpin live tiles from Start. Notifications and tiles are broker-mediated, so quieting them directly reduces broker threads. Microsoft documents Store app repair in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Re-register Store app packages in elevated PowerShell.
2. Disable notifications for apps you don't need alerts from.
3. Unpin live tiles from the Start menu.
4. Reboot and verify over a full day.

### Fix 6: Lock down startup and background activity

Final sweep: **Task Manager → Startup apps** — disable Acer updaters and third-party launchers you don't need at boot (the [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) shows the safe way to audit). In **Settings → Apps → Installed apps → Advanced options**, set **Background apps permissions** to Never for remaining chatty Store apps. With startup lean and background activity restricted, the broker has almost nothing to mediate — which is exactly its healthy state.

1. Disable unneeded startup entries in Task Manager.
2. Set background permissions to Never for chatty Store apps.
3. Reboot and confirm the fix holds for 48 hours.
4. Revisit if a future app update re-triggers it.

## Closing

On Acer laptops, Runtime Broker noise almost always traces to the preinstalled software stack — Acer utilities, partner apps, or Windows' own suggestions — rather than anything you did. Update or remove the offenders, quiet the notifications, and the broker returns to its proper role: a process you never think about.
