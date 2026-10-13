---
title: "What to Do If Chrome Uses High CPU on Windows 11"
slug: what-to-do-if-chrome-high-cpu-windows-11
date: 2026-09-24
categories: ["performance"]
tags: ["chrome", "high cpu", "browser", "windows 11", "extensions"]
description: "Chrome pushing your laptop's CPU to 50-100%? From rogue tabs and extensions to hardware acceleration, here's exactly what to check and fix."
thumbnail: "/images/thumbs/what-to-do-if-chrome-high-cpu-windows-11.webp"
faqs:
  - q: "Why does Chrome use so much CPU?"
    a: "Chrome runs each tab and extension as a separate process, which is great for stability but means resource usage adds up fast. Heavy web apps (video calls, streaming, crypto miners on shady sites), misbehaving extensions, dozens of open tabs, and software rendering when hardware acceleration fails are the main drivers of high CPU."
  - q: "How many tabs is too many in Chrome?"
    a: "There's no fixed number — it depends on what the tabs contain. Ten static article pages are trivial; ten tabs with auto-playing video, live dashboards, or web apps can saturate a CPU. Chrome's Memory Saver feature helps by sleeping inactive tabs, but CPU-heavy background tabs (video calls, miners, animations) need to be closed, not just slept."
  - q: "Should I turn hardware acceleration on or off?"
    a: "On, normally — it offloads rendering to the GPU and reduces CPU usage significantly. Turn it off only as a diagnostic step: if disabling it fixes high CPU, your graphics driver is the real problem and needs updating. Leaving it off permanently just shifts rendering work onto the CPU."
  - q: "Will resetting Chrome delete my bookmarks?"
    a: "No. Chrome's 'Restore settings to their original defaults' keeps bookmarks, history, and saved passwords — it only disables extensions, clears temporary data, and resets settings. It's a safe troubleshooting step. (Uninstalling Chrome entirely is different — choose to keep data if prompted.)"
---

Chrome is the most popular browser on Windows laptops and also one of the most common sources of high CPU usage. It's not unusual to see Chrome consuming 40, 60, or even 100 percent of CPU — the fan screaming, the battery draining, everything else slowing down — while you're "just browsing." The multiprocess architecture means every tab, extension, and plugin gets its own process, so usage adds up in ways that are hard to see from the main window.

The good news: Chrome gives you excellent built-in tools to find exactly which tab or extension is responsible, and most high-CPU causes have straightforward fixes. This guide starts with Chrome's own task manager (which most users don't know exists), then works through the extension, settings, and system-level fixes in order of likelihood.

Before starting, make sure Chrome is updated — Google ships performance and efficiency fixes constantly, and an outdated browser is the simplest explanation. Also note whether the high CPU happens constantly or only on specific sites: constant usage points to extensions or settings, while site-specific spikes point to heavy pages you can simply avoid.

## Why this happens

- **CPU-heavy tabs**: Video calls, streaming, browser games, live dashboards, and crypto miners on malicious sites can each consume massive CPU.
- **Misbehaving extensions**: Ad blockers, coupon finders, and poorly-coded extensions run on every page and can spike CPU badly.
- **Too many active tabs**: Each tab is a process; dozens of media-heavy tabs multiply the load, especially without Memory Saver.
- **Hardware acceleration failures**: When GPU acceleration breaks (usually a driver issue), Chrome falls back to software rendering, hammering the CPU.
- **Background Chrome processes**: Chrome keeps running background apps, updaters, and notification services even with no window open.
- **Corrupted profile data**: Damaged cache or profile files cause excessive processing and repeated failed operations.
- **Outdated Chrome version**: Older builds lack efficiency improvements and may have known CPU bugs.
- **Conflicting software**: Some antivirus and "PC optimizer" tools inject into Chrome and cause high CPU.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use Chrome's built-in Task Manager

Chrome has its own task manager that shows per-tab and per-extension CPU — far more useful than Windows Task Manager for this problem.

1. In Chrome, press **Shift + Esc** to open Chrome's Task Manager.
2. Click the **CPU** column to sort by usage.
3. Identify the top consumers — note whether they're tabs (page titles), extensions, or the GPU process.
4. Select the worst offender and click **End process** to kill just that tab/extension.
5. If killing a specific tab fixes it, that page is the problem — avoid it or find what's heavy on it (auto-play video, miners).

### Fix 2: Audit and remove extensions

Extensions are the most common persistent cause. Test ruthlessly.

1. Go to **chrome://extensions**.
2. Toggle off all extensions, then check CPU usage for 10 minutes.
3. If it's fixed, re-enable extensions one at a time, testing after each.
4. Permanently remove any extension that spikes CPU — especially coupon/shopping extensions, "free VPN" extensions, and anything you don't remember installing.
5. Prefer fewer, well-maintained extensions from known developers.

### Fix 3: Enable Memory Saver and Energy Saver

Chrome's built-in efficiency features automatically tame background tabs.

1. Go to **Settings > Performance**.
2. Turn on **Memory Saver** — inactive tabs get slept automatically, freeing CPU and RAM.
3. Turn on **Energy Saver** — limits background activity and visual effects when on battery or when enabled.
4. Add sites you need always-active (like music streaming) to the Memory Saver exclusions if needed.

### Fix 4: Check hardware acceleration and update GPU drivers

If Chrome's GPU process shows high CPU, acceleration is likely broken.

1. Go to **Settings > System** and check **Use hardware acceleration when available** — it should be ON.
2. If it's on and CPU is still high, toggle it OFF temporarily as a test. If CPU drops, your graphics driver is the real culprit.
3. Update the driver: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html).
4. After updating, turn hardware acceleration back ON and retest.

### Fix 5: Clear browsing data and reset settings

Corrupted cache and bad settings accumulate over time.

1. Go to **Settings > Privacy and security > Delete browsing data**.
2. Clear **Cached images and files** (keep passwords and history unless you want a full clean).
3. If problems persist, go to **Settings > Reset settings > Restore settings to their original defaults**.
4. This disables extensions and clears temporary data but keeps bookmarks, history, and passwords.

### Fix 6: Stop Chrome running in the background

Chrome's background persistence means it can burn CPU with no window open.

1. Go to **Settings > System**.
2. Turn off **Continue running background apps when Google Chrome is closed** if you don't need Chrome notifications/updates while closed.
3. In Windows Task Manager's **Startup apps** tab, disable Chrome if you don't want it preloading at boot.
4. Check for multiple Chrome updaters in Task Scheduler and disable the extras.

### Fix 7: Scan for malware and conflicting software

Browser hijackers and miners are real, and some "security" tools fight Chrome.

1. Run Chrome's built-in cleanup: **Settings > Reset settings > Clean up computer > Find** (if available in your region).
2. Run a full Windows Security scan.
3. Check **chrome://conflicts** for software injecting into Chrome — incompatible applications are listed here.
4. Remove or update any conflicting software, especially old antivirus or "PC boosters."
5. Check your extensions once more after cleanup — malware sometimes installs rogue extensions that survive other fixes. Anything you don't recognize in chrome://extensions should be removed immediately.

If Chrome's memory (not CPU) is the issue, see our guide on [fixing Chrome high memory usage](/articles/how-to-fix-chrome-using-too-much-ram-laptop-in-windows-11-24h2/). For system-wide browser-independent slowness, see [how to speed up a Windows 11 laptop](/articles/how-to-speed-up-windows-11-laptop/).

## Closing

Chrome high CPU is almost always one specific thing: a heavy tab, a bad extension, or broken hardware acceleration. Chrome's own task manager names the culprit in seconds — use it first, fix what it points at, and your laptop goes back to quiet, cool browsing.
