---
title: "Fix Runtime Broker High CPU on an HP Laptop"
slug: how-to-fix-runtime-broker-high-cpu-on-hp-laptop
date: 2026-09-15
categories: ["performance"]
tags: ["runtime broker", "high cpu", "hp laptop", "uwp apps"]
description: "Runtime Broker spiking CPU on your HP laptop? Find which Store app is misbehaving and fix it — from permissions to clean reinstalls."
thumbnail: "/images/thumbs/how-to-fix-runtime-broker-high-cpu-on-hp-laptop.webp"
faqs:
  - q: "What does Runtime Broker actually do?"
    a: "Runtime Broker is the middleman between Universal Windows Platform (Store) apps and the system permissions they request — location, microphone, camera, notifications, and background execution. Every time a Store app checks a permission, Runtime Broker handles it. Brief CPU use during app launches is normal; sustained high CPU means an app is hammering it with repeated permission requests."
  - q: "Why does Runtime Broker use more CPU on HP laptops?"
    a: "HP preloads several Store apps — utilities, support tools, and partner apps — that request permissions aggressively in the background. More preinstalled Store apps means more permission traffic through the broker. Auditing which HP apps are installed and removing the ones you never open typically quiets the broker significantly."
  - q: "Is it safe to end Runtime Broker in Task Manager?"
    a: "Yes, temporarily. Ending it stops the CPU spike immediately, and Windows restarts it automatically when a Store app next needs a permission check. It is a safe relief valve, not a fix — the misbehaving app will drive CPU up again until you address it with the steps in this guide."
  - q: "Can I disable Runtime Broker permanently?"
    a: "You should not. Disabling it breaks Store apps' ability to request permissions, causing crashes and malfunctioning apps across the system. It is a core OS component. The correct fix is always finding and fixing the app that is abusing it, which leaves the broker itself idling at near-zero CPU as designed."
---

Runtime Broker is one of those processes that should be invisible. It sits between Store apps and your system permissions, quietly approving location checks and notification requests, using essentially zero CPU. When it instead parks itself at 20–40% CPU indefinitely, something on the other side of that counter is misbehaving — usually a preinstalled Store app stuck in a permission-request loop.

HP laptops are frequent victims because HP's factory image includes a stack of Store apps that all want background permissions. This guide shows you how to identify the offending app, fix its permissions, and — when the app is junk — remove it entirely.

## Why this happens

- **A Store app stuck in a permission loop:** An app repeatedly requesting location, microphone, or background access keeps the broker permanently busy.
- **HP's preinstalled Store apps:** HP utilities and partner apps request background permissions aggressively, multiplying broker traffic.
- **Live Tiles and notification spam:** Apps with live tiles or frequent notifications generate constant broker-mediated updates.
- **Corrupted app installations:** A damaged Store app can fail its permission checks and retry endlessly.
- **Background app permissions too broad:** Apps allowed to run background tasks they do not need create steady broker load.
- **Photos app indexing:** The Microsoft Photos app's background face/object indexing hammers the broker on large libraries.
- **Windows tips and suggestions:** The tips system itself is a Store-app surface that generates broker traffic.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the pattern and get immediate relief

1. Open Task Manager (**Ctrl + Shift + Esc**) and verify **Runtime Broker** holds sustained high CPU (not just a spike during an app launch).
2. Right-click it → **End task**. Windows restarts it on demand — note how long the calm lasts before CPU climbs again.
3. If CPU climbs back within minutes with no apps visibly open, a background Store app is the driver — continue.
4. If it stays calm for hours, the spike may have been a one-off (an app updating); monitor before changing anything.

### Fix 2: Audit which Store apps are installed

1. Open **Settings → Apps → Installed apps** and scan for Store apps you never use — especially HP utilities, preinstalled games, and partner apps.
2. Uninstall the obvious junk first; each removed app is one less permission-requester.
3. Pay special attention to apps with background behavior: news, weather, and "assistant" style apps are the classic broker abusers.
4. Keep a list of what you removed in case you need to reinstall something from the Microsoft Store later.

### Fix 3: Restrict background app permissions

1. Go to **Settings → Apps → Installed apps**, click **...** on a suspicious app → **Advanced options**.
2. Under **Background apps permissions**, set it to **Never** for anything that does not need background activity.
3. Go to **Settings → Privacy & security** and review **Location**, **Microphone**, and **Notifications** — turn off access for apps that have no business asking.
4. Fewer permission grants means fewer broker transactions — this is the highest-leverage settings pass in the guide.

### Fix 4: Reset or repair the misbehaving app

1. If you suspect a specific app (often Photos, or an HP utility), go to its **Advanced options** and click **Repair** first, then **Reset** if repair does not help.
2. Resetting clears the app's data and permission state — you will need to sign in again where applicable.
3. For the Photos app specifically, also open it → **Settings** and turn off background indexing features you do not use.
4. Retest Runtime Broker CPU for an hour after each reset — fix one app at a time so you know which one was guilty.

### Fix 5: Turn off Live Tiles and suggestion surfaces

1. Right-click tiles in the Start menu → **More → Turn live tile off** for news, weather, and other chattering apps.
2. Go to **Settings → System → Notifications → Additional settings** and uncheck **Get tips and suggestions when I use Windows**.
3. Our full [tips and suggestions shutdown](/articles/how-can-i-turn-off-windows-tips-and-suggestions/) covers every promo surface that generates broker traffic.
4. These surfaces are constant low-grade broker load even when "nothing" is running.

### Fix 6: Re-register Store apps if the broker itself is corrupt

1. Open an elevated PowerShell and run: `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
2. This re-registers every Store app package, fixing corrupted registrations that cause permission-check loops.
3. Restart the laptop and observe. This is a broad hammer — use it only after Fixes 2–5 did not isolate a single app.
4. If PowerShell reports errors for specific packages, those are likely the corrupted ones — consider uninstalling and reinstalling just those from the Store. General app troubleshooting background is on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 7: Check HP-specific background agents

1. Open **Task Manager → Startup apps** and disable HP agents you do not need at boot.
2. In **Settings → Apps → Installed apps**, evaluate remaining HP software against actual use — keep driver/update tools, remove marketing and "experience" apps.
3. Check [HP's support page](https://support.hp.com/us-en) for updated versions of the HP apps you keep — HP does fix broker-abusing bugs in their Store apps over time.
4. As a final isolation test, boot into **Safe Mode** — Runtime Broker should be nearly idle there, confirming a third-party Store app (not Windows itself) is the cause.

## Closing

Runtime Broker high CPU is always a symptom of an app, never the broker's own fault. Audit the Store apps, revoke the background permissions they do not need, reset the one that is looping, and the broker drops back to the near-zero background hum it was designed for — taking your fan noise and battery drain with it.

Going forward, treat every new Store app install as a small decision: does it need background permission, location access, or notification rights? Granting the minimum at install time prevents the next broker spike before it starts. And if Runtime Broker ever misbehaves again, the [Windows 11 24H2 edition of this fix](/articles/how-to-fix-runtime-broker-high-cpu-in-windows-11-24h2/) covers the same ground with version-specific screenshots and settings paths.
