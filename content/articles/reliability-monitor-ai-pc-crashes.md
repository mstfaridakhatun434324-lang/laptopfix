---
title: "Using Reliability Monitor to Diagnose AI PC Crashes"
slug: reliability-monitor-ai-pc-crashes
date: 2026-10-23
categories: ["ai-pc"]
tags: ["reliability monitor", "crash diagnosis", "ai pc", "windows 11", "stability", "troubleshooting"]
description: "Diagnose AI PC crashes with Reliability Monitor: read the stability timeline, identify failing apps and drivers, and fix repeat crashes step by step."
thumbnail: "/images/thumbs/reliability-monitor-ai-pc-crashes.webp"
faqs:
  - q: "What is Reliability Monitor and where do I find it?"
    a: "It's a built-in Windows tool that charts your system's stability over time, marking app crashes, driver failures, and Windows failures on a timeline. Open it by typing 'reliability' in Start or running perfmon /rel."
  - q: "How is it different from Event Viewer?"
    a: "Reliability Monitor is the friendly summary — a visual timeline with plain-language failure descriptions. Event Viewer is the raw log underneath. Start with Reliability Monitor to spot patterns, then dig into Event Viewer for details."
  - q: "What does a dropping stability index mean?"
    a: "The 1-10 stability index falls with each failure and recovers slowly during clean days. A steady decline means something is repeatedly crashing; a sudden cliff points to a specific change (update, new app, new driver)."
  - q: "Can Reliability Monitor show hardware problems?"
    a: "Indirectly — it shows Windows hardware-error reports (like WHEA errors) and the driver crashes that hardware faults cause. Repeated identical driver crashes at the same workload strongly suggest a hardware issue."
---

When your AI PC crashes — apps vanishing, the system freezing, blue screens — the most valuable diagnostic is not any single error message but the pattern across days. Reliability Monitor gives you exactly that: a timeline of every failure, what caused it, and when it started. It is the first tool a technician opens, and it takes five minutes to read.

This guide teaches you to read the timeline, identify the failure patterns specific to AI PCs (NPU drivers, AI services, ARM app crashes), and convert each pattern into the right repair. Six sections, in diagnostic order.

## Why this happens

- **Crash patterns are invisible without history:** A single crash tells you nothing; the same module crashing daily tells you everything. Memory of "it crashed recently" is unreliable — the timeline is not.
- **AI PC failures cluster in specific components:** NPU drivers, AI platform services (Recall, Studio Effects hosts), and ARM-translated apps fail in recognizable repeat patterns that the timeline makes obvious.
- **Updates are the most common inflection point:** The timeline's cliff edges almost always align with a Windows update, driver update, or new app install — the "what changed" question answered visually.
- **Background services crash silently:** AI indexing and NPU services can crash repeatedly without any visible symptom except slowness. Reliability Monitor surfaces these invisible failures.
- **Cascading failures mislead:** One root crash (a driver) spawns app crashes that look like app bugs. The timeline's chronological order reveals which failure came first.
- **Intermittent issues need long baselines:** A crash every three days is undiagnosable from memory but obvious on a 28-day timeline — the same long-view principle behind [memory integrity conflict diagnosis](/articles/memory-integrity-npu-driver-conflict/).
- **Users misattribute the cause:** "The browser crashes" when the timeline shows the graphics driver crashing underneath the browser. The timeline corrects the blame to the right layer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Open Reliability Monitor and read the timeline

Before changing anything, spend five minutes learning what your system has been doing. The timeline often names the culprit outright.

1. Press **Win + R**, type `perfmon /rel`, and press Enter — or search Start for "View reliability history".
2. Look at the stability index graph (1-10 scale) over the last weeks: note any cliffs (sudden drops) and their dates — each cliff is a failure event worth investigating.
3. Click any day column to see that day's detail list below: application failures, Windows failures, driver failures, and informational events (installs, updates).
4. Click **View technical details** on any failure for the faulting module name, exception code, and app version — record these for the worst offenders.
5. Identify the single most frequent failure: sort mentally by repetition. The thing that crashes most often is your prime suspect — everything else is secondary until it is fixed.

### Fix 2: Correlate cliffs with changes (updates, installs, drivers)

A cliff on the timeline is a "what changed" marker. Match each cliff to its cause using the informational events on the same day.

1. Click the day of the steepest recent drop and read the **informational events** — Windows Update installs, driver updates, and new software appear here with timestamps.
2. If a Windows update or driver update precedes the cliff by hours, that update is the prime suspect: roll back the driver (Device Manager > Roll Back Driver) or uninstall the update (**Settings > Windows Update > Update history > Uninstall updates**).
3. If a new app install precedes the cliff, uninstall that app as a test — particularly ARM-translated apps or system utilities, which are overrepresented in AI PC crash timelines (the same install-friction class as [Visual Studio ARM64 installer issues](/articles/visual-studio-arm64-installer-issues/)).
4. If no change is visible before the cliff, look one to two days earlier — some updates stage before activating, and driver updates can take effect on the next boot.
5. After the rollback/uninstall, watch the timeline for 2-3 days: the stability index should stop falling and begin recovering. No recovery means the correlation was wrong — keep investigating.

### Fix 3: Address the top repeating application failure

The most frequent app crash deserves direct attention. The technical details tell you whether it is the app, its runtime, or something underneath.

1. In the day detail, find the most repeated **Application failure** and open its technical details — note the **faulting module** (the DLL that actually crashed) and the **exception code**.
2. If the faulting module belongs to the app itself: update the app, reset it (**Settings > Apps > Installed apps > Advanced options > Reset**), or reinstall it cleanly.
3. If the faulting module is a system runtime (like WebView2, .NET, or a graphics driver DLL), the app is the victim — update the runtime or driver instead. WebView2 issues specifically have their own [repair path](/articles/copilot-app-webview2-runtime-error/).
4. If the exception code indicates an access violation (0xc0000005) in the same module repeatedly, check for corrupted app data: rename the app's `%appdata%`/`%localappdata%` folder (back it up first) and let the app rebuild it.
5. Re-check the timeline after the fix: that specific failure should disappear from new days. If a different module now crashes in the same app, you fixed one layer and exposed the next — continue.

### Fix 4: Address driver and Windows failures

Driver failures and Windows (bugcheck/blue screen) failures are more serious than app crashes — they affect the whole system and often implicate hardware.

1. For **Windows hardware errors** or bugchecks, note the stop code in technical details and check whether they cluster under load, after sleep, or randomly — load-clustered suggests thermals/power, sleep-clustered suggests driver power management.
2. For repeated **driver failures** naming one driver file, clean-reinstall that driver from the OEM: uninstall with driver removal in Device Manager, restart, install the OEM package.
3. Run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Terminal — Windows failures with no clear driver often trace to system file corruption.
4. Check thermals and memory: run Windows Memory Diagnostic (`mdsched.exe`) and monitor temperatures under load — hardware faults produce the "same crash, no software change" pattern.
5. If bugchecks persist with clean drivers, clean system files, and healthy thermals, back up and contact your maker's support with the timeline screenshots — you have done the software triage they would ask for.

### Fix 5: Hunt the silent background crashes

Some of the most damaging failures never show a dialog — AI services and updaters crashing in the background, each one dragging the stability index down and degrading performance.

1. In Reliability Monitor, expand days and look specifically for failures in services and background processes: search indexing, AI/Recall services, NPU-related hosts, and updater services.
2. A background service crashing hourly is a real problem even if you never see it — it usually means corrupted service data or a broken update.
3. For Windows services: check **Services** (`services.msc`) for the failing service's status, and look at its dependencies — a dependency failing first is the actual root cause.
4. Reinstall or repair the component owning the service (Windows features via DISM, or the app's repair option), rather than just restarting the service — restarts treat the symptom.
5. After repair, the timeline should show the background failures stopping. Persistent background crashes in security-adjacent services may also relate to [memory integrity / HVCI conflicts](/articles/memory-integrity-npu-driver-conflict/) — check that angle if the crashing service is security-related.

### Fix 6: Establish a clean baseline and monitor

Diagnosis is a loop, not a single pass. After repairs, use the timeline as your verification instrument.

1. After each repair, mark the date (a sticky note works) and watch the next 3-7 days of the timeline for that specific failure's return.
2. A failure that never returns is fixed — move to the next most frequent issue on the timeline.
3. If the stability index climbs back toward 10 and holds, the system is healthy — the timeline is now your early-warning system for future problems.
4. Make checking Reliability Monitor a monthly habit (it takes two minutes) — catching a new cliff early means rolling back one change instead of untangling months of compounding issues.
5. Export or screenshot the timeline before major changes (feature updates, driver overhauls) so you always have a "before" picture. The timeline's memory is better than yours — let it do the remembering.

## Closing

Reliability Monitor converts crashes from anecdotes into evidence: read the timeline oldest-to-newest, match cliffs to changes, fix the most frequent failure first, and verify by watching the index recover. On AI PCs the usual suspects are NPU drivers, AI services, and ARM app translations — the timeline will point at whichever one is actually guilty on your machine.
