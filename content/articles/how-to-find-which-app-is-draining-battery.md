---
title: "How to Identify the App Draining Your Laptop Battery"
slug: how-to-find-which-app-is-draining-battery
date: 2026-10-09
categories: ["battery"]
tags: ["battery usage", "background apps", "diagnostics", "windows 11"]
description: "Someone's stealing your battery — here's how to catch them. Use Windows' built-in tools to find exactly which app is draining your laptop."
thumbnail: "/images/thumbs/how-to-find-which-app-is-draining-battery.webp"
faqs:
  - q: "How do I see which app uses the most battery on Windows 11?"
    a: "Go to Settings > System > Power & battery > Battery usage. Windows shows per-app battery consumption for the last 24 hours and last 7 days, broken down by in-use vs background activity. Sort by the highest percentages to find your biggest drainers."
  - q: "Why does an app use battery in the background?"
    a: "Apps run background tasks for notifications, syncing, location updates, and keeping content fresh. Social media, messaging, cloud storage, and email apps are the usual suspects — they wake the CPU and radio periodically even when you never open them."
  - q: "What is 'System' battery usage in Windows?"
    a: "The System category covers Windows itself: the display, CPU idle overhead, Windows Update, Search indexing, and drivers. If System dominates your battery usage, the issue is usually settings (brightness, power mode), a stuck Windows process, or outdated drivers rather than a single app."
  - q: "Can a website drain my laptop battery?"
    a: "Absolutely. Browser tabs running video, animations, ads, or crypto miners can consume as much power as a desktop app. Check your browser's built-in task manager (Shift+Esc in Chrome/Edge) to find heavy tabs, and close or suspend the worst offenders."
---
Your battery was fine yesterday. Today it's evaporating — and you haven't done anything differently. Somewhere on your laptop, an app is burning through charge, and guessing which one wastes time. Windows keeps detailed receipts on exactly where your battery went. Let's read them.

This is detective work, not guesswork. In fifteen minutes you'll have a ranked list of suspects and a plan for each one.

## Why this happens

- **Background permissions pile up.** Nearly every app requests background access at install; over months, dozens of apps end up churning CPU and network while you do nothing.
- **An app update introduced a bug.** A previously well-behaved app can start draining after an update — sync loops and stuck processes are classic post-update behavior.
- **Sync and notification churn.** Mail, messaging, and cloud apps wake the system constantly to check for updates, each wake costing a little power that adds up.
- **Browser tabs are stealth apps.** A single tab with autoplaying video, heavy ads, or a stuck script can out-drain most installed programs.
- **Windows' own processes misbehave.** Search indexing after big file changes, Windows Update downloads, and antivirus scans show up under "System" and can dominate drain temporarily.
- **Startup apps multiply.** Everything in your startup list becomes a permanent background resident, each taking its small cut.

## How to fix it

Work through these in order — identify, then act, then verify.

### Fix 1: Read the Battery usage report

This is your primary evidence — start here.

1. Go to **Settings > System > Power & battery** and click **Battery usage**.
2. Set the dropdown to **Last 7 days** for the big picture, then **Last 24 hours** for recent changes.
3. Note the top apps and whether their usage is mostly **In use** or **Background** — background-heavy apps are your prime suspects.
4. Pay special attention to any app whose share jumped recently — that's your "what changed" answer.

### Fix 2: Restrict background permissions

Cut off the background drain at the source.

1. Open **Settings > Apps > Installed apps**, click the **three dots** on a suspect app, and choose **Advanced options**.
2. Under **Background apps permissions**, set it to **Never** for apps you only use deliberately (games, shopping, social), or **Power optimized** for apps you want somewhat live.
3. Repeat for every app with significant background usage in the report.
4. For the broader technique, see our guide on [turning off background apps to save battery](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/).

### Fix 3: Check the browser's task manager

Don't forget the tabs — they're apps too.

1. In **Chrome or Edge**, press **Shift + Esc** to open the browser task manager.
2. Sort by **CPU** or **Memory** and look for tabs consuming resources disproportionately.
3. Close heavy tabs, pause autoplaying video, and consider a **tab suspender extension** for tabs you keep open but rarely view.
4. If the browser itself is a top drainer, check for misbehaving extensions by testing in an **Incognito/InPrivate** window (extensions disabled).

### Fix 4: Audit startup apps

Fewer residents means less background drain.

1. Open **Task Manager** (**Ctrl + Shift + Esc**) and go to **Startup apps**.
2. Disable everything you don't need running from boot — updaters, chat clients, cloud tools you rarely use.
3. Restart and check **Battery usage** after a day to measure the improvement.

### Fix 5: Investigate "System" drain

When no single app stands out, Windows itself needs attention.

1. In **Task Manager**, sort by **CPU** and watch for system processes holding high usage: **Windows Search indexer**, **Antimalware Service Executable**, **Windows Update** components.
2. For Search indexer: let it finish (it settles after indexing), or limit indexed locations in **Settings > Privacy & security > Searching Windows**.
3. For antivirus scans: schedule full scans for when you're **plugged in**.
4. Run **Settings > Windows Update** and clear any stuck updates, then restart.

### Fix 6: Use powercfg to find sleep-time drainers

Some culprits only strike when the laptop should be sleeping.

1. Open an **admin** Command Prompt and run: `powercfg /sleepstudy` — this generates a report of what kept the system awake during sleep.
2. Open the resulting `sleepstudy-report.html` and look for apps and devices with high **% Active** time during sleep sessions.
3. Restrict or uninstall the offenders, and unplug USB devices that prevent deep sleep.

### Fix 7: Verify the fix worked

Detectives confirm their conclusions.

1. After making changes, use the laptop normally for a **full day** on battery.
2. Recheck **Settings > System > Power & battery > Battery usage** — the suspects' shares should have dropped.
3. If drain persists with no app standing out, check actual battery health with `powercfg /batteryreport` — at high wear levels, even normal app usage empties the shrunken battery fast. Our [fast-drain troubleshooting guide](/articles/laptop-battery-drains-fast-troubleshooting/) continues from there.

## Closing

Finding battery drainers is straightforward once you know where Windows keeps the evidence: Battery usage for the rankings, background permissions for the fix, and the browser task manager for the tabs everyone forgets. Do this audit twice a year — apps accumulate background permissions like dust, and a periodic cleanout keeps runtime honest. Pay particular attention after installing new software: grant background permission sparingly at install time rather than cleaning up later, since most apps ask once and never ask again. If the audit comes back clean but the battery still vanishes, the [battery report](/articles/best-way-to-use-powercfg-to-check-battery/) will tell you whether wear is the real story. Microsoft's [battery usage documentation](https://support.microsoft.com/en-us/windows) covers these screens in official detail.

One more place drainers hide: scheduled tasks. Open **Task Scheduler** and look under the Task Scheduler Library for tasks set to run frequently or wake the machine — updaters, telemetry, and manufacturer utilities love to schedule hourly work you'd never notice. You don't need to gut the scheduler, but disabling the obviously unnecessary frequent tasks (and unchecking "wake the computer" on the rest) closes a drain source that Battery usage doesn't always attribute clearly, since the work gets billed to "System" rather than the app that scheduled it.
