---
title: "How to Find Which App Is Draining Your Laptop Battery"
slug: how-can-i-find-which-app-is-draining-battery
date: 2026-09-03
categories: ["battery"]
tags: ["battery drain", "apps", "power usage"]
description: "Find the exact app eating your battery with Windows' built-in per-app usage stats, Task Manager, and powercfg — no guesswork."
thumbnail: "/images/thumbs/how-can-i-find-which-app-is-draining-battery.webp"
faqs:
  - q: "How do I see which apps use the most battery on Windows 11?"
    a: "Go to Settings > System > Power & battery and click Battery usage. Set the range to Last 7 days and sort by percentage. This shows exactly how much battery each app consumed, split between active use and background activity — the definitive answer to what's draining your pack."
  - q: "Why is an app I barely use showing high battery usage?"
    a: "Background activity. Many apps — mail clients, chat apps, cloud sync tools, updaters — run constantly even when you never open their window. The battery usage screen splits foreground vs. background precisely so you can spot apps burning power behind your back."
  - q: "Can a browser really drain that much battery?"
    a: "Absolutely — browsers are routinely the #1 battery consumer on laptops. Dozens of tabs, auto-playing video, and heavy sites keep the CPU and GPU busy. One bad tab (a crypto miner, an infinite-scroll page, a stuck video) can single-handedly halve battery life."
  - q: "What do I do after finding the draining app?"
    a: "Restrict its background activity in Settings > Apps > Installed apps > Advanced options, disable it in Task Manager > Startup if it launches at boot, update it (battery bugs get fixed), or replace it with a lighter alternative. Then watch the battery usage screen over the next few days to confirm the improvement."
---

When battery life tanks, the battery itself is guilty maybe half the time. The other half, it's an app — sometimes one you use constantly, sometimes one running invisibly in the background that you haven't opened in weeks. The difference matters enormously: a worn battery costs money to fix, but a rogue app costs five minutes. Windows has excellent built-in tooling for identifying the culprit; you just need to know where to look and how to read what it shows.

This guide is the full hunt: the built-in per-app battery stats, Task Manager's live power columns, the command-line backup, and what to do with each offender once identified. If you've already confirmed the battery itself is healthy via a [battery report](/articles/how-to-generate-battery-report-in-windows-11/), this is the natural next step.

## Why this happens

- **Background permissions:** Apps default to running background tasks — syncing, checking messages, updating — that burn CPU and radio power all day.
- **Startup bloat:** Apps that launch at boot tend to linger forever, each taking a small but constant sip of power.
- **Browser tab sprawl:** Modern web pages are applications; 30 tabs is 30 programs running, some of them badly behaved.
- **Updaters and sync tools:** Game launchers, cloud drives, and software updaters often scan, index, or upload aggressively in the background.
- **Stuck processes:** A crashed-but-running process can pin a CPU core at 100% indefinitely — invisible unless you look.
- **Poorly optimized apps:** Electron apps,looking at you — some desktop apps are simply power-hungry by design and have lighter alternatives.

## How to fix it

Work through these in order — identify first, then act on the evidence.

### Fix 1: Check the built-in battery usage screen

The authoritative answer, straight from Windows.

1. Open **Settings > System > Power & battery** and click **Battery usage**.
2. Change the dropdown to **Last 7 days** — a week smooths out one-off anomalies and shows real patterns.
3. Scan the sorted list: anything in double digits that surprises you is a suspect.
4. Click a suspect app to see its **In use** vs. **Background** split — heavy background share means you can restrict it without changing how you use it.
5. On Windows 10, the same screen lives at **Settings > System > Battery > See which apps are affecting your battery life**.

### Fix 2: Use Task Manager's power columns

Catch what's burning power right now.

1. Open **Task Manager** (Ctrl + Shift + Esc), go to **Processes**, and if you don't see them, right-click the column headers and enable **Power usage** and **Power usage trend**.
2. Sort by **Power usage trend** — this shows sustained consumption rather than momentary spikes.
3. Look for anything marked **Very high** that shouldn't be: updaters, installers stuck mid-task, browser sub-processes, or unfamiliar names.
4. For a stuck process, right-click > **End task** and watch whether battery drain visibly improves over the next hour.
5. If the same process keeps coming back, it's a startup item or service — note its name for Fix 4.

### Fix 3: Audit your browser specifically

Browsers deserve their own investigation — they're usually #1.

1. Open your browser's built-in task manager (**Shift + Esc** in Chrome/Edge) to see per-tab CPU and memory usage — kill the worst tabs.
2. Look for tabs with auto-playing video, infinite scroll, or heavy animations; these are disproportionate battery killers.
3. Disable or remove extensions you don't actively use — each one runs code on every page you visit.
4. Turn on the browser's efficiency features: Edge has **Efficiency mode** in Settings > System and performance; Chrome has **Memory Saver** and **Energy Saver**.
5. Consider whether you need 40 tabs open — bookmark and close; your battery will notice the difference immediately.

### Fix 4: Tame startup apps and background permissions

Stop the drain from ever starting.

1. In **Task Manager > Startup apps**, disable everything you don't need within seconds of booting — game launchers, chat apps, updaters, cloud tools.
2. For Microsoft Store apps: **Settings > Apps > Installed apps**, click an app's **... > Advanced options**, and set **Background apps permissions** to **Never** for anything that doesn't need live updates.
3. For desktop apps, the lever is usually inside the app's own settings — look for "launch at startup," "run in background," or "start minimized" and turn them off.
4. In **Settings > Privacy & security > Background apps** (Windows 11), you can also globally restrict background activity.
5. Reboot and re-check Task Manager after 10 minutes of idle — the process list should be noticeably shorter.

### Fix 5: Update or replace the worst offenders

Sometimes the app is just buggy.

1. Check the worst offender for updates — battery-drain bugs are common and commonly fixed; check the Microsoft Store, the app's site, or its built-in updater.
2. Search "[app name] high battery usage" — if it's a known issue with a known workaround, you'll find it fast.
3. Consider lighter alternatives for chronic offenders: a native app instead of an Electron one, a lighter browser, or the web version instead of a desktop client.
4. For cloud sync tools (OneDrive, Dropbox, etc.), check sync settings — pausing sync on battery or limiting it to Wi-Fi can cut drain dramatically.
5. After making changes, give it 2-3 days, then revisit the **Battery usage** screen to confirm the numbers moved.

### Fix 6: Check for malware and miners

Rule out the malicious explanation.

1. If an unfamiliar process shows very high power usage trend and you can't identify it, treat it as suspicious.
2. Run a full scan with **Windows Security > Virus & threat protection > Scan options > Full scan**.
3. Browser-based crypto miners show up as a browser tab or process burning a full CPU core — the browser task manager from Fix 3 exposes them.
4. Check **Task Manager > Startup** and **Task Scheduler** for entries you don't recognize that launch at boot or on schedules.
5. A machine that's hot and draining at idle with no visible cause deserves a second-opinion scan with a reputable on-demand scanner.

### Fix 7: Confirm the fix with before-and-after data

Prove it worked instead of hoping.

1. Before making changes, screenshot the **Battery usage** screen and note your typical hours-per-charge.
2. After the fixes, use the laptop normally for 3-7 days on the same kind of workload.
3. Revisit **Battery usage** (Last 7 days) and compare — the offender's share should have collapsed.
4. If total battery life is still poor despite no app standing out, the battery itself is the story — run the [full Windows 11 diagnostic sequence](/articles/how-to-run-battery-diagnostics-on-windows-11/) to check wear.
5. Microsoft's official battery-saving guidance is at [Microsoft Support](https://support.microsoft.com/en-us/windows).

## Closing

Battery drain is a whodunit, and Windows hands you the detective's toolkit for free. Check the usage screen, sort Task Manager by power trend, interrogate the browser, and put the offenders on a diet. Most "my battery is dying" complaints end here — with an app restricted, not a battery replaced.
