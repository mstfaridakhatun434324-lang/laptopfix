---
title: "Fix Edge High CPU Usage in Windows 11: A Step-by-Step Guide"
slug: "how-to-fix-edge-high-cpu-usage-windows-11-step-by-step"
date: "2026-09-06"
categories: ["performance"]
tags: ["edge high cpu", "windows 11", "browser fix", "step by step", "cpu usage"]
description: "A complete step-by-step walkthrough to stop Microsoft Edge from hogging CPU in Windows 11 — diagnose, fix, and verify, in order."
thumbnail: "/images/thumbs/how-to-fix-edge-high-cpu-usage-windows-11-step-by-step.webp"
faqs:
  - q: "How do I check which Edge tab is using the most CPU?"
    a: "Press Shift + Esc inside Edge to open its built-in browser task manager, then click the CPU column to sort. This shows per-tab, per-extension, and GPU process usage separately, which Windows Task Manager lumps together. The top entry during a spike is almost always your culprit."
  - q: "Will resetting Edge delete my bookmarks and passwords?"
    a: "Resetting settings restores defaults but keeps bookmarks, history, and saved passwords. It disables extensions and clears temporary data like cookies. If you are signed into a Microsoft account with sync enabled, your data is also backed up to the cloud, so a reset is quite safe."
  - q: "Why is Edge running in the background when I closed it?"
    a: "Edge's Startup boost pre-launches browser processes at Windows login, and the 'continue running background apps' setting keeps extensions and web apps alive after you close all windows. Both are enabled by default and add constant baseline CPU and memory load even when you are not browsing."
  - q: "Is high Edge CPU usage a virus?"
    a: "Rarely, but it is worth ruling out. Malicious or compromised extensions can mine cryptocurrency or run hidden scripts that look like ordinary browser CPU usage. If Edge is hot with no tabs open and no extensions you recognize, scan with Windows Security and remove any extension you did not deliberately install."
---

This is the methodical version of the Edge CPU fix: every step in order, nothing skipped, each one building on the last. Follow it top to bottom and you will not just reduce Edge's CPU usage — you will know exactly what was causing it, which means it will not come back as a mystery next month. The whole sequence takes about 20 minutes, and most people find the culprit by step 3.

Before starting, establish your baseline. Open Edge, use it normally for five minutes, then press **Shift + Esc** to open Edge's browser task manager and note the total CPU at the bottom. Write the number down. You will compare against it at the end — without a baseline, "it feels better" is not a diagnosis.

A quick orientation on what you will see: Edge runs as many processes — one per tab, one per extension, plus GPU and utility processes. High total CPU with a clear top offender is easy to fix. High CPU spread evenly across many tabs means you have a tab-hygiene problem rather than a bug.

## Why this happens

- **A single runaway tab:** One page running a broken script or a crypto miner can pin a core while everything else idles.
- **Extension overload:** Each installed extension is permanently running code; several heavy ones compound into constant load.
- **Sleeping tabs disabled:** Without tab sleeping, every background tab keeps its timers and scripts alive indefinitely.
- **Background processes enabled:** Startup boost and background-app continuation keep Edge processes alive 24/7.
- **Hardware acceleration mismatch:** A bad GPU driver turns acceleration from a CPU saver into a CPU waster.
- **Corrupted cache or profile data:** Damaged local data sends renderer processes into retry loops that burn CPU.
- **Outdated Edge version:** Known CPU bugs get fixed in monthly updates; a stalled updater leaves you on the buggy build.
- **Sync conflicts:** A corrupted sync state can cause Edge's sync engine to retry continuously in the background.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Record the baseline and identify the top offender

Do not change anything yet. Open Edge's browser task manager with **Shift + Esc**, sort by CPU, and watch for two minutes during your normal browsing. Note the process name and CPU percentage of the top three entries. If one tab or extension dominates, you have a targeted problem. If usage is spread across many tabs, you have a configuration problem. Either way, this reading is your "before" measurement — the entire guide is about moving this number down. For HP-specific background factors, our [HP laptop Edge guide](/articles/how-to-fix-edge-high-cpu-usage-windows-11-on-hp-laptop/) covers the manufacturer side.

1. Press **Shift + Esc** in Edge to open the browser task manager.
2. Sort by **CPU** and observe for 2 minutes.
3. Write down the top 3 consumers and the total CPU at the bottom.
4. Keep this note — you will compare at the end.

### Fix 2: Kill the runaway tab and test in a clean window

If one tab dominates, close it and watch CPU collapse — that confirms the page, not the browser, is the problem. Common offenders include webmail with a stuck sync, news sites with aggressive video ads, and web apps left open overnight. Then open a single blank tab and check idle CPU: a healthy Edge idles near 0–2%. If a blank tab still shows high CPU, the problem is in Edge's configuration or extensions, not any website.

1. In the browser task manager, select the top tab and click **End process**.
2. Close all tabs except one blank new-tab page.
3. Wait 60 seconds and note idle CPU.
4. If idle is still high, continue — the issue is systemic.

### Fix 3: Disable all extensions and reintroduce them one by one

This is the step that solves the majority of cases. Extensions run with broad privileges and several popular categories — coupon finders, "free VPN" tools, shopping assistants — are notorious CPU hogs. Disable everything, restart Edge, and re-check your baseline. Then re-enable extensions individually with a minute of observation between each. When CPU jumps, you have found it: remove that extension permanently and find an alternative.

1. Navigate to **edge://extensions/**.
2. Disable every extension with its toggle.
3. Restart Edge, wait 2 minutes, and compare CPU to baseline.
4. Re-enable one at a time, observing CPU for 60 seconds each.

### Fix 4: Enable efficiency mode and sleeping tabs

With extensions ruled out, turn on Edge's built-in resource savers. Efficiency mode reduces background tab activity and visual effects; sleeping tabs unloads tabs you have not looked at recently, freeing both CPU and RAM. Set the sleep timeout aggressively (5 minutes) — you lose nothing, since sleeping tabs reload instantly when clicked. These two settings compound: efficiency mode throttles what is awake, sleeping tabs reduces what is awake at all.

1. Open **Settings > System and performance**.
2. Enable **Efficiency mode** (set to Balanced or Always).
3. Enable **Save resources with sleeping tabs** with a 5-minute timeout.
4. Browse normally for 15 minutes, then re-check the browser task manager.

### Fix 5: Disable Startup boost and background continuation

Edge's Startup boost launches browser processes at Windows login so Edge opens faster — at the cost of permanent background CPU and memory. The background-apps setting keeps extensions running after you close Edge. Unless you open Edge dozens of times a day and cannot tolerate a one-second slower launch, turn both off. This also reduces the "Edge is using CPU but I closed it" confusion. Fewer autostarting components also helps overall boot speed, as covered in our [startup disk usage guide](/articles/how-to-fix-windows-11-high-disk-usage-on-startup-on-lenovo-laptop/).

1. In **Settings > System and performance**, turn off **Startup boost**.
2. Turn off **Continue running background extensions and apps when Microsoft Edge is closed**.
3. Restart Windows (not just Edge) to clear already-running background processes.
4. Verify in Windows Task Manager that no Edge processes remain after closing the browser.

### Fix 6: Reset Edge settings

If CPU is still high with no extensions, no heavy tabs, and background features off, the browser's configuration is likely corrupted. Resetting restores all settings to defaults while preserving bookmarks, history, and passwords — it is far more effective than reinstalling, because a reinstall keeps the same broken profile. After the reset, re-apply only the settings from Fixes 4 and 5, and reinstall extensions only as needed.

1. Go to **Settings > Reset settings**.
2. Click **Restore settings to their default values** and confirm.
3. Restart Edge and check CPU before reinstalling any extension.
4. Re-enable efficiency mode and sleeping tabs (reset turns them off).

### Fix 7: Update Edge, then update the GPU driver

Finish by eliminating known bugs. First force an Edge update at **edge://settings/help** — monthly releases regularly fix CPU regressions. Then update the graphics driver from your manufacturer's support site (not just Windows Update), because hardware acceleration behavior depends on it; a stale GPU driver is a classic cause of the GPU Process entry burning CPU in the browser task manager. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the update process if the built-in updater stalls.

1. Visit **edge://settings/help** and install any pending update.
2. Download the latest GPU driver from your laptop manufacturer's support site.
3. Install the driver and restart.
4. Compare final CPU against your baseline note from Fix 1.

## Closing

The step-by-step discipline matters here: baseline, isolate, fix, verify. Most Edge CPU problems surrender at the extension step or the efficiency-mode step, but by working the full sequence you also clean up the background processes and stale drivers that would have caused the next spike. Compare your final reading to the baseline — if it is not dramatically lower, something outside Edge (like a system-wide CPU hog) deserves investigation.
