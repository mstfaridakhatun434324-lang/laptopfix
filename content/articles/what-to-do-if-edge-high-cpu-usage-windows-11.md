---
title: "What to Do If Microsoft Edge Is Using High CPU on Windows 11"
slug: "what-to-do-if-edge-high-cpu-usage-windows-11"
date: "2026-09-10"
categories: ["performance"]
tags: ["edge high cpu", "microsoft edge", "browser cpu", "windows 11"]
description: "Microsoft Edge pinning your CPU at 30-50%? Identify the hungry tab or extension and calm Edge down with these fixes."
thumbnail: "/images/thumbs/what-to-do-if-edge-high-cpu-usage-windows-11.webp"
faqs:
  - q: "Why does Edge use so much CPU even with few tabs open?"
    a: "Background features are usually responsible: sleeping tabs that wake for timers, extensions running content scripts on every page, the built-in shopping and coupon assistant scanning pages, and hardware acceleration misbehaving on certain GPU drivers. Edge's own task manager, opened with Shift+Esc inside Edge, shows exactly which tab, extension, or GPU process is consuming the CPU."
  - q: "Is Edge worse than Chrome for CPU usage?"
    a: "They share the Chromium engine, so baseline usage is similar. Edge adds Microsoft-specific features like sleeping tabs, efficiency mode, and startup boost, which can make it lighter than Chrome when configured well. An unconfigured Edge with many extensions often matches or exceeds Chrome's footprint, so the difference comes down to settings and extensions rather than the browser core."
  - q: "Does hardware acceleration increase or decrease CPU usage?"
    a: "It should decrease CPU usage by offloading rendering to the GPU, and on most systems it does. But on laptops with buggy or outdated graphics drivers, hardware acceleration can backfire, causing the GPU process to spin the CPU while it waits on the driver. If Edge's GPU process shows high CPU, toggling hardware acceleration off is a worthwhile experiment."
  - q: "Will resetting Edge delete my passwords and bookmarks?"
    a: "Using Settings, Reset settings, Restore settings to their default values keeps your bookmarks, history, and saved passwords but disables extensions and clears temporary data. Signing back into your Microsoft account re-syncs anything stored in the cloud. It is a safe middle ground before the nuclear option of a full profile wipe."
---

Microsoft Edge is a good browser that occasionally behaves like a crypto miner. You notice the fans first, then Task Manager confirms it: Edge chewing through 30, 40, even 60 percent CPU with what looks like a handful of innocent tabs open. On a laptop, that translates directly into heat, noise, and battery draining visibly by the minute.

The culprits are rarely the visible tabs. Modern browsers run dozens of hidden processes: extensions injecting scripts into every page, sleeping tabs waking for background timers, the shopping assistant scanning pages for coupons, and the GPU process struggling with a cranky driver. Edge even pre-launches background processes at Windows startup through its Startup boost feature, so it can burn CPU before you ever open a window.

This guide shows how to find the exact hungry process using Edge's built-in task manager, then walks through the settings that calm it down: sleeping tabs, efficiency mode, extension triage, and hardware acceleration. No reinstall required in most cases.

## Why this happens

- **Extensions running on every page:** Ad blockers, coupon finders, and grammar tools inject scripts into each tab and can each cost several percent CPU.
- **Sleeping tabs waking repeatedly:** Tabs that should sleep keep waking for timers, notifications, or media, defeating the feature.
- **The GPU process struggling:** A mismatch between Edge and the graphics driver makes the GPU process spin CPU while waiting on rendering.
- **Startup boost preloading:** Edge preloads processes at Windows login, consuming resources even when the browser is closed.
- **Shopping and coupon assistant:** Built-in price-comparison features scan page content continuously on shopping sites.
- **Many tabs with live content:** Dashboards, chats, and auto-refreshing pages each run JavaScript timers that add up.
- **Corrupted profile data:** A damaged cache or preferences file can send renderer processes into retry loops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the hungry process with Edge's task manager

Edge ships its own task manager that breaks CPU usage down by tab, extension, and internal process. Diagnose before you change anything.

1. Open Edge and press Shift+Esc to open the browser task manager.
2. Click the CPU column to sort by usage.
3. Identify whether a tab, an extension, or the GPU process is the offender.
4. Select the worst offender and click End process to confirm the relief.
5. Note the name; the fixes below target each category.

### Fix 2: Enable sleeping tabs and efficiency mode

Sleeping tabs freeze inactive tabs after a period, and efficiency mode caps background resource use. Together they are Edge's biggest built-in savings.

1. In Edge, go to Settings, then System and performance.
2. Turn on Save resources with sleeping tabs.
3. Set Fade sleeping tabs and choose a short timeout like 5 minutes.
4. Turn on Efficiency mode and set it to Maximum savings or Balanced.
5. Restart Edge and monitor CPU over the next hour.

### Fix 3: Triage your extensions

Extensions are the most common hidden CPU hog. The browser task manager from Fix 1 tells you exactly which ones to suspect.

1. In Edge, open the Extensions page via the puzzle-piece menu.
2. Disable every extension you do not actively use.
3. For the rest, click Details and restrict Site access to On click or specific sites.
4. Re-enable them one per day to identify the hog if CPU was high.
5. Prefer extensions with small user bases and recent updates over abandoned ones.

### Fix 4: Toggle hardware acceleration

Hardware acceleration normally helps, but on laptops with problematic GPU drivers it can be the entire problem. Testing both states takes a minute.

1. Go to Edge Settings, System and performance.
2. Find Use hardware acceleration when available.
3. If it is on, turn it off, restart Edge, and check CPU for 15 minutes.
4. If it is off and CPU is high, try turning it on instead.
5. Keep whichever setting gives lower CPU in the browser task manager.

### Fix 5: Disable Startup boost and background running

If Edge processes appear in Task Manager before you open the browser, these two settings are responsible.

1. In Edge Settings, System and performance, turn off Startup boost.
2. Turn off Continue running background extensions and apps when Microsoft Edge is closed.
3. Open Windows Task Manager, Startup apps tab.
4. Disable Microsoft Edge there as well.
5. Restart Windows and confirm no Edge processes run before launch.

### Fix 6: Reset Edge settings

When configuration corruption is suspected, a settings reset clears the cruft while preserving bookmarks and passwords.

1. Open Edge Settings and go to Reset settings.
2. Click Restore settings to their default values and confirm.
3. Re-enable only the extensions you verified as safe.
4. Reconfigure sleeping tabs and efficiency mode, since the reset turns them off.
5. Sign back into sync if prompted and verify CPU stays calm.

### Fix 7: Create a fresh Edge profile

A corrupted profile can keep renderer processes spinning no matter what settings you change. Testing with a brand-new profile isolates profile corruption in two minutes.

1. Click your profile icon in Edge and choose Add profile.
2. Set up the new profile without signing in or installing extensions.
3. Browse normally for 30 minutes and watch CPU in the browser task manager.
4. If the new profile is calm, migrate bookmarks to it gradually.
5. Delete the old profile once the new one is fully working.

### Fix 8: Create a fresh Edge profile

A corrupted profile can keep renderer processes spinning no matter what settings you change. Testing with a brand-new profile isolates profile corruption in two minutes.

1. Click your profile icon in Edge and choose Add profile.
2. Set up the new profile without signing in or installing extensions.
3. Browse normally for 30 minutes and watch CPU in the browser task manager.
4. If the new profile is calm, migrate bookmarks to it gradually.
5. Delete the old profile once the new one is fully working.

## Closing

Edge high CPU is a diagnosis-first problem: the browser's own task manager tells you in seconds whether to blame a tab, an extension, or the GPU process, and each has a targeted fix. For most users, sleeping tabs plus efficiency mode plus an extension audit returns Edge to a quiet background citizen. If the whole system still feels heavy, remember the browser is only one consumer; our guide to [disabling startup apps](/articles/how-to-disable-startup-apps-on-windows-11/) covers the rest of the usual suspects. If a specific extension keeps misbehaving, our [Edge CPU troubleshooting walkthrough](/articles/best-way-to-fix-edge-high-cpu-usage-windows-11/) goes deeper, and Microsoft documents browser performance in its [Windows support hub](https://support.microsoft.com/en-us/windows). If a specific extension keeps misbehaving, our [Edge CPU troubleshooting walkthrough](/articles/best-way-to-fix-edge-high-cpu-usage-windows-11/) goes deeper, and Microsoft documents browser performance in its [Windows support hub](https://support.microsoft.com/en-us/windows).
