---
title: "Runtime Broker High CPU? Calm It Down on Your Windows Laptop"
slug: runtime-broker-high-cpu-troubleshooting
date: 2026-09-13
categories: ["performance"]
tags: ["runtime broker", "high cpu", "windows permissions", "task manager"]
description: "Runtime Broker eating your CPU? Learn what RuntimeBroker.exe does, why it spikes, and how to reduce its CPU usage on Windows laptops."
thumbnail: "/images/thumbs/runtime-broker-high-cpu-troubleshooting.webp"
faqs:
  - q: "What is Runtime Broker and why is it using so much CPU?"
    a: "Runtime Broker (RuntimeBroker.exe) is a legitimate Windows process that manages permissions for Microsoft Store apps — things like location, camera, and microphone access. It's supposed to use almost no CPU. When it spikes, it's almost always because a Store app (Photos, News, Tips, or a third-party UWP app) is misbehaving, stuck in a permission loop, or constantly triggering permission checks."
  - q: "Is RuntimeBroker.exe a virus?"
    a: "The genuine Runtime Broker lives in C:\\Windows\\System32 and is a core Windows component. Malware can impersonate it, so right-click the process in Task Manager and choose Open file location — if it leads anywhere other than System32, run a full antivirus scan. A real Runtime Broker at high CPU is a symptom of a misbehaving app, not an infection, in the vast majority of cases."
  - q: "Can I disable Runtime Broker?"
    a: "You shouldn't disable or delete Runtime Broker itself — Windows needs it for Store apps to function and will recreate it anyway. The correct approach is fixing what's making it work hard: disabling unnecessary background Store apps, turning off tips and suggestions, and removing misbehaving apps. Ending the task in Task Manager is safe as a temporary measure; it restarts automatically when needed."
  - q: "How much CPU should Runtime Broker normally use?"
    a: "At idle, Runtime Broker should sit at 0% CPU and only a few megabytes of memory. Brief spikes when you launch a Store app are normal. Sustained usage above 5–10% CPU — especially at idle with no apps open — is abnormal and worth investigating. If it stays elevated for hours or returns after every reboot, one of your installed Store apps is the culprit."
---

Open Task Manager and you'll find it: `RuntimeBroker.exe`, calmly burning 15%, 30%, sometimes 60% of your CPU while you do absolutely nothing. It's a real Windows component — not malware in most cases — but it has no business working that hard. Runtime Broker is a permissions middleman for Microsoft Store apps, and when one of those apps goes rogue, Runtime Broker takes the blame in the CPU column.

The good news: this is one of the more fixable high-CPU issues. The process itself is rarely broken — it's reacting to something. Your job is to find the app triggering it and shut that down. For general slowdown help beyond this one process, see our guide on [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/), and if startup is also sluggish, [trim your startup programs](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Misbehaving Microsoft Store app**: A UWP app stuck in a permission request loop makes Runtime Broker work overtime.
- **Tips, tricks, and suggestions enabled**: Windows' "helpful" notifications constantly trigger Store-app permission checks.
- **Too many background Store apps**: Dozens of preinstalled apps (News, Weather, Tips) all phoning home through the broker.
- **Corrupt app data**: A damaged Store app installation repeatedly fails and retries its permission requests.
- **Live tiles and background updates**: Apps refreshing content in the background keep the broker busy.
- **Malware impersonating Runtime Broker**: Rare, but a fake RuntimeBroker.exe running from outside System32 will mine CPU.
- **Windows spotlight and lock-screen apps**: Lock-screen apps like Cortana-era widgets trigger repeated permission checks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's the real Runtime Broker

Rule out impersonation before anything else.

1. Open **Task Manager** (Ctrl+Shift+Esc), go to the **Details** tab, and find **RuntimeBroker.exe**.
2. Right-click it and choose **Open file location** — the genuine process lives in `C:\Windows\System32`. Anything else is suspicious.
3. Check the **CPU** column: is it constantly high, or spiking? Constant high CPU at idle points to a stuck app; spikes point to a specific activity.
4. If the location is wrong, run a full scan with **Windows Security** > **Virus & threat protection** > **Scan options** > **Full scan** before doing anything else. Our [free antivirus guide](/articles/best-free-antivirus-for-windows-11-laptop/) covers extra scanning tools if you want a second opinion.
5. Also check how many RuntimeBroker.exe instances are running — one or two is normal; several chewing CPU suggests multiple troubled apps.

### Fix 2: End the task and watch what comes back

A quick reset that often reveals the culprit.

1. In **Task Manager** > **Processes**, find **Runtime Broker**, right-click, and choose **End task**. It's safe — Windows restarts it automatically when needed.
2. Watch Task Manager for a few minutes: if CPU stays low, something transient was stuck and the reset cleared it.
3. If Runtime Broker climbs again within minutes, note which apps are also active — the one launching alongside the spike is your suspect.
4. Open **Settings** > **Apps** > **Installed apps** and sort by install date; recently updated or installed Store apps are prime suspects.
5. Repeat the end-task test after closing each suspect app to narrow it down, then move to Fix 3 to deal with the app itself.

### Fix 3: Disable background apps you don't need

Fewer apps running in the background means fewer permission checks.

1. Go to **Settings** > **Apps** > **Installed apps** and click the three dots on each preinstalled app you never use (News, Weather, Tips, Clipchamp, etc.).
2. Choose **Advanced options** and set **Background apps permissions** to **Never** for each one.
3. Pay special attention to **Photos**, **Microsoft Store**, and **News** — these are the most common Runtime Broker triggers.
4. For a global approach on Windows 11: **Settings** > **System** > **Power & battery** > **Battery usage** — apps listed here with background activity can be restricted individually.
5. After disabling, restart and check Task Manager — Runtime Broker should drop to near zero at idle.

### Fix 4: Turn off tips, tricks, and suggestions

Windows' helpful hints are a surprisingly common trigger.

1. Go to **Settings** > **System** > **Notifications** > **Additional settings** (or scroll down on Windows 10 under Notifications & actions).
2. Uncheck **Get tips and suggestions when using Windows** — this alone fixes many Runtime Broker CPU cases.
3. Also uncheck **Suggest ways I can finish setting up my device** and **Show me the Windows welcome experience**.
4. In **Settings** > **Personalization** > **Start**, turn off **Show suggestions for tips, shortcuts, new apps, and more**.
5. Restart the laptop and verify — these suggestion engines trigger Store-app permission checks in the background constantly.

### Fix 5: Repair or reset the offending Store app

If you've identified a specific app, fix it rather than fighting the broker.

1. Go to **Settings** > **Apps** > **Installed apps**, find the suspect app, click the three dots > **Advanced options**.
2. Click **Repair** first — this fixes the app without deleting its data. Check Task Manager afterward.
3. If Repair doesn't help, click **Reset** — this wipes the app's data and settings, which clears corrupt states causing permission loops.
4. For the **Photos** app specifically (a frequent offender), resetting often resolves its background indexing loops that hammer Runtime Broker.
5. If the app is one you never use, just **Uninstall** it — the cleanest fix. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the repair and reset options for Store apps.

### Fix 6: Reset the Microsoft Store cache

A corrupt Store cache can cascade into every Store app misbehaving.

1. Press **Win+R**, type `wsreset.exe`, and press Enter — a blank command window appears for a few seconds, then the Store opens. That's the cache being cleared.
2. Restart your laptop after the reset completes.
3. Open the **Microsoft Store** > **Library** and install any pending app updates — outdated Store apps are more likely to misbehave.
4. Check **Settings** > **Windows Update** and install pending updates too — Runtime Broker bugs get fixed in cumulative updates.
5. Monitor Task Manager for a day; if the spikes are gone, the corrupt cache was the root cause.

### Fix 7: Create a new user profile (last resort)

A corrupted user profile can cause persistent broker issues no app-level fix resolves.

1. Go to **Settings** > **Accounts** > **Other users** > **Add account** and create a new local user.
2. Log into the new account and check Task Manager at idle — if Runtime Broker is calm there, your original profile is corrupt.
3. Migrate your files to the new profile (Documents, Desktop, Downloads) and reinstall your apps gradually, watching for the culprit to return.
4. This is drastic, so only do it if Fixes 1–6 all failed and the high CPU has persisted for weeks.
5. Before this step, consider one full Windows repair: run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an elevated terminal — it fixes system-component corruption that profile issues mimic.

## Closing

Runtime Broker high CPU is almost never a broken Windows component — it's a symptom of a Store app misbehaving, and the fix is finding and calming that app. Disable background permissions for apps you don't use, kill the tips and suggestions, and reset the offenders. The broker will fade back to its usual 0%, where it belongs.
