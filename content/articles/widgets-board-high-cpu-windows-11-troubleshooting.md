---
title: "Widgets Board High CPU on Windows 11: Deep Troubleshooting Guide"
slug: widgets-board-high-cpu-windows-11-troubleshooting
date: 2026-09-05
categories: ["performance"]
tags: ["widgets board", "high cpu", "troubleshooting", "windows 11", "webview2"]
description: "Troubleshoot Widgets Board high CPU on Windows 11 in depth: diagnose which feed or component is responsible, fix WebView2 issues, and resolve update-triggered spikes."
thumbnail: "/images/thumbs/widgets-board-high-cpu-windows-11-troubleshooting.webp"
faqs:
  - q: "How do I find out which widget is causing high CPU?"
    a: "Remove widget cards one at a time from the board and watch Widgets.exe CPU in Task Manager after each removal, waiting several minutes between changes. News and finance cards with auto-refreshing content are the most common offenders. When CPU drops after removing a specific card, you have identified the culprit — leave it off or replace it with a lighter alternative."
  - q: "What is WebView2 and why does it matter for widgets CPU?"
    a: "WebView2 is the Chromium-based rendering engine the Widgets Board uses to display its content. Because it is essentially a browser engine, it carries browser-like overhead — JavaScript execution, rendering, and GPU compositing. A corrupted or outdated WebView2 runtime makes the entire board inefficient, so repairing it is a key troubleshooting step."
  - q: "Why did widgets CPU spike right after a Windows update?"
    a: "Updates commonly reset widget settings to defaults (re-enabling all cards and auto-play), corrupt the widget feed cache, replace the WebView2 runtime with a version that needs re-registration, or reinstall the Web Experience Pack with fresh default configuration. The spike is the board rebuilding or misbehaving on the new state — not a permanent change."
  - q: "Can antivirus software cause widgets to use more CPU?"
    a: "Indirectly, yes. Real-time antivirus scans the WebView2 cache files, downloaded feed content, and JavaScript the board executes, multiplying the CPU cost of every widget update. If widgets CPU is high and nothing else explains it, add the Web Experience Pack's cache folders to your antivirus exclusions as a diagnostic test."
---

When the Widgets Board misbehaves, "turn it off" is a valid answer — but it is not a diagnosis. Sometimes you want the weather widget and just need the runaway news feed fixed. Sometimes the board worked fine for months and suddenly spikes after an update, and you want to know why rather than amputate the feature. This guide is the diagnostic deep-dive: find the specific component, feed, or corruption behind the CPU usage, fix that, and keep what works.

Pair it with the quick-fix approach when you want speed; use this one when you want understanding.

## Why this happens

- **A single greedy widget card:** One misconfigured or data-heavy card (news with video, stocks with rapid refresh) can dominate the board's entire CPU budget.
- **Corrupted feed cache:** Damaged cached content makes the board re-fetch and re-render continuously instead of settling.
- **WebView2 runtime problems:** Outdated, corrupted, or mis-registered WebView2 forces the board to render inefficiently or fall back to software rendering.
- **Personalization pipeline overload:** The local processing that personalizes news and content can spiral when its data files corrupt.
- **Stuck authentication state:** A half-logged-in Microsoft account state makes the board retry authentication-dependent feeds in a loop.
- **GPU driver interaction:** The board's hardware-accelerated rendering can clash with buggy graphics drivers, inflating CPU as the system compensates.
- **Notification badge polling:** The taskbar badge's separate polling loop adds CPU even when the board itself is quiet.
- **Third-party widget providers:** Installed third-party widgets run with fewer constraints than Microsoft's own and are frequent culprits.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Isolate the offending widget card

1. Open the Widgets Board and note every card currently displayed.
2. Remove cards one at a time (each card's **…** menu → remove/hide), waiting 3–5 minutes between removals while watching Widgets.exe in Task Manager.
3. When CPU drops meaningfully after a removal, you have found the offender — news/video cards and rapidly refreshing finance cards are the usual winners.
4. Leave the culprit removed. If you need its function, look for a lighter alternative card or check the information in a browser instead. For the quick-disable path, see [best way to fix widgets board high CPU](/articles/best-way-to-fix-widgets-board-high-cpu-windows-11/).

### Fix 2: Clear the board's caches and reset its state

1. Go to **Settings → Apps → Installed apps → Windows Web Experience Pack → Advanced options**.
2. Click **Repair** first and test for an hour — this fixes corrupted state while preserving your card layout.
3. If no improvement, click **Reset** — this wipes configuration and caches, forcing the board to rebuild cleanly.
4. Re-add only the cards you actually use, one at a time, watching CPU after each. A clean rebuild with minimal cards is often dramatically lighter than the accumulated cruft of months.

### Fix 3: Repair the WebView2 runtime

1. Go to **Settings → Apps → Installed apps** and find **Microsoft Edge WebView2 Runtime**.
2. If a **Modify/Repair** option is available, run it. Otherwise, download the latest WebView2 runtime installer from Microsoft's official distribution page and reinstall it.
3. Restart the laptop — WebView2 changes require a restart to fully take effect for all host apps.
4. Retest widgets CPU. Because the board is essentially a WebView2 application, runtime corruption punishes it disproportionately — this fix resolves the mysterious "board suddenly heavy for no reason" cases.

### Fix 4: Fix the Microsoft account authentication loop

1. Open the Widgets Board settings and check the account state — sign out and sign back into your Microsoft account within the board if it looks stuck.
2. Alternatively, go to **Settings → Accounts** and verify your account shows no "verify" or error states.
3. Authentication-dependent feeds (personalized news, calendar) retry aggressively when auth is half-broken, and each retry costs CPU.
4. If you do not need personalized content, using the board signed out eliminates this entire failure class.

### Fix 5: Audit third-party widgets

1. Review the board for any widgets not made by Microsoft — third-party providers' widgets are the least tested and most frequent CPU offenders.
2. Remove them one at a time with the Task Manager test from Fix 1.
3. Check whether the third-party widget has its own settings for refresh intervals and lengthen them, or disable auto-refresh entirely.
4. Prefer Microsoft's first-party cards or no card over a misbehaving third-party one — the information is available elsewhere.

### Fix 6: Update the graphics driver for the rendering path

1. The board uses GPU-accelerated rendering through WebView2; a buggy graphics driver makes every card expensive to draw.
2. Clean-install the current driver: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html) as appropriate for your hardware.
3. As a diagnostic test, temporarily disable hardware acceleration effects: **Settings → Accessibility → Visual effects → Animation effects Off**, and see if widgets CPU drops.
4. If it drops, the rendering path was the problem — keep animations off or keep the updated driver; either resolves it.

### Fix 7: Investigate the update-triggered spike specifically

1. If the spike began with a Windows update, check **Settings → Windows Update → Update history** for the KB number and search it alongside "widgets CPU" — known issues get documented fast.
2. Verify the update did not reset your widget configuration: open the board and check for re-enabled cards, badges, and auto-play you had turned off.
3. Re-apply your minimal configuration, then run the **Repair** from Fix 2 — updates frequently leave the Web Experience Pack in a half-migrated state that Repair resolves.
4. If the spike matches a known update issue, the fix may simply be the next cumulative update — pause optional updates meanwhile rather than fighting it.

### Fix 8: Decide the board's fate based on evidence

1. After the diagnostics above, you know specifically what was wrong — a greedy card, corrupted cache, bad runtime, or auth loop.
2. If the board now idles quietly with your chosen cards, keep it — the diagnosis paid off and you kept the feature.
3. If CPU remains stubbornly high with minimal cards and a healthy runtime, the board's cost exceeds its value on your hardware — disable it via policy/registry as described in our [widgets board fix guide](/articles/best-way-to-fix-widgets-board-high-cpu-windows-11/).
4. Document what you found (which card, which fix) — widget issues recur with updates, and your notes make the next round a five-minute job.

## Closing

Deep troubleshooting the Widgets Board means treating it like what it is — a small web application with feeds, caches, a rendering engine, and an authentication layer, any of which can fail independently. Isolate the card, repair the runtime, fix the auth state, and check the update history. When you find the specific broken piece, the fix is precise and the board earns its place back on the taskbar — quiet this time. A 24H2 caveat: the Widgets.exe process behaves differently in that build, so if the board-side fixes here don't move the needle, the [24H2 Widgets.exe guide](/articles/how-to-fix-widgets-exe-high-cpu-in-windows-11-24h2/) targets the process itself.
