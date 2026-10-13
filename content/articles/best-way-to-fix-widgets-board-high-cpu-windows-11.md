---
title: "The Best Way to Fix Widgets Board High CPU on Windows 11"
slug: best-way-to-fix-widgets-board-high-cpu-windows-11
date: 2026-09-04
categories: ["performance"]
tags: ["widgets board", "high cpu", "windows 11", "widgets.exe", "cpu fix"]
description: "Widgets.exe driving up CPU on Windows 11? Fix the Widgets Board's high CPU usage with this best-practice sequence — feed settings, background permissions, and full disable."
thumbnail: "/images/thumbs/best-way-to-fix-widgets-board-high-cpu-windows-11.webp"
faqs:
  - q: "What is the Widgets Board and why does it use CPU?"
    a: "The Widgets Board is the slide-out panel (opened from the taskbar weather icon) showing news, weather, stocks, and calendar. Its process, Widgets.exe, runs continuously in the background fetching fresh content, updating feeds, and rendering the board — even when you never open it. That constant content pipeline is what consumes CPU, disk, and network."
  - q: "Is it safe to disable the Widgets Board completely?"
    a: "Yes, completely safe. The Widgets Board is an optional shell feature — disabling it removes the taskbar icon and the panel, and nothing else in Windows depends on it. The Start menu, notifications, and all apps work identically. Most users who disable it report lower idle CPU usage and never miss it."
  - q: "Why does Widgets.exe use CPU even when I never open the board?"
    a: "Because the board pre-fetches content in the background so it appears instantly when opened. It polls news feeds, weather services, and stock data on a schedule regardless of whether you look at it. Disabling background content updates — or the board entirely — is the only way to stop the polling."
  - q: "Will disabling widgets improve battery life?"
    a: "Modestly, yes. The widgets process wakes the CPU on a schedule to fetch content, and each wake-up prevents the processor from staying in its deepest sleep states. On laptops where every watt counts, removing a scheduled waker produces a small but real battery improvement, plus a quieter idle."
---

The Widgets Board is the panel that slides out when you click the weather widget on the taskbar — news headlines, weather, stocks, sports scores. It looks harmless. But behind it runs Widgets.exe, a process that fetches fresh content on a schedule all day long, whether you ever open the board or not. On many Windows 11 laptops it shows up in Task Manager consuming a steady few percent of CPU — and on some, far more, especially after updates corrupt its feed state.

The best-practice fix is a short escalation: calm the feeds first, restrict the background activity second, and disable the board entirely third.

## Why this happens

- **Scheduled content polling:** The board fetches news, weather, and stocks on timers throughout the day, each poll waking the CPU and network.
- **Corrupted feed state:** Damaged widget configurations or feed caches can send the update loop into overdrive, multiplying normal CPU usage.
- **Animated and rich content:** Auto-playing videos, animated weather, and rich media cards cost far more to render and update than static text.
- **MSN content pipeline weight:** The feeds come through Microsoft's content services, and heavy personalization processing happens locally.
- **Background running by default:** The widgets process starts with Windows and runs permanently — there is no "only when opened" mode.
- **Update-triggered resurgence:** Windows updates frequently re-enable widgets and reset their settings even after you disabled them.
- **WebView2 rendering overhead:** The board renders through WebView2 (Chromium-based), which carries browser-engine overhead for what is essentially a news panel.
- **Notification badges:** Widget notification badges on the taskbar require additional background checks beyond the board's own polling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets.exe is the problem

1. Open **Task Manager** and look for **Widgets.exe** (or **Windows Widgets**) in the Processes list, sorted by CPU.
2. Note its sustained usage over several minutes — occasional spikes during feed refresh are normal; constant multi-percent usage is not.
3. Check whether usage correlates with network activity in the **Performance** tab — heavy network alongside widgets CPU confirms feed polling as the driver.
4. If widgets CPU is trivial and something else dominates, stop here — the board is not your problem. Our [general high-CPU guidance](/articles/antimalware-service-executable-high-cpu-windows-11/) covers the other usual suspects.

### Fix 2: Turn off the taskbar widgets entry point

1. Right-click the taskbar → **Taskbar settings**.
2. Toggle **Widgets** to **Off** — this removes the taskbar icon and prevents accidental board opens.
3. Note this does not stop the background process; it only hides the entry point. It is step one, not the whole fix.
4. Monitor Task Manager — if Widgets.exe calms down significantly, the board's rendering (triggered by hover previews) was part of the cost.

### Fix 3: Quiet the board's content and notifications

1. Open the Widgets Board (Win + W), click the **settings gear** or your profile icon → **Widget settings**.
2. Turn off **notification badges**, **announcements**, and any auto-playing content options.
3. Remove widget cards you do not use — each card is its own polling feed. Keep only weather, or nothing at all.
4. Fewer cards means fewer feeds, fewer polls, and less CPU. This is the highest-value tweak short of disabling the board.

### Fix 4: Restrict the widgets app's background permissions

1. Go to **Settings → Apps → Installed apps** and find **Windows Web Experience Pack** (the widgets host app).
2. Click **… → Advanced options** and set **Background apps permissions** to **Never** — or to **Power optimized** as a middle ground.
3. Toggle off **Location** permission if the weather widget does not need precise location.
4. Restart and observe Widgets.exe behavior over an hour — restricted background permissions often cut its CPU dramatically.

### Fix 5: Repair or reset the Web Experience Pack

1. In the same **Advanced options** page for Windows Web Experience Pack, use **Repair** first — this fixes corrupted feed state without losing configuration.
2. If Repair does not help, use **Reset** — this clears the widget configuration and feed caches entirely, forcing a clean rebuild.
3. Reconfigure minimally afterward: fewer cards, no auto-play, no badges.
4. Corrupted widget state after Windows updates is a classic cause of sudden widgets CPU spikes, and Reset is its direct cure.

### Fix 6: Disable the Widgets Board via group policy or registry

1. For a durable disable: open `gpedit.msc` → **Computer Configuration → Administrative Templates → Windows Components → Widgets** → enable **Allow widgets** set to **Disabled**.
2. On Home edition (no gpedit), use the registry: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh`, create DWORD **AllowNewsAndInterests** set to **0** (create the Dsh key if missing).
3. Restart — the taskbar toggle disappears and Widgets.exe should no longer run at startup.
4. Back up the registry key before editing. This survives the updates that re-enable the Settings-level toggle.

### Fix 7: Uninstall the Web Experience Pack (if available)

1. In **Settings → Apps → Installed apps**, check whether **Windows Web Experience Pack** offers an **Uninstall** option — on some builds it does.
2. Alternatively, in an **admin Terminal**, run `winget uninstall "Windows Web Experience Pack"` and confirm.
3. Verify Widgets.exe is gone from Task Manager after restart.
4. If the package cannot be uninstalled on your build, the policy/registry disable from Fix 6 achieves the same practical result.

### Fix 8: Verify the gain and lock it in

1. Compare idle CPU in Task Manager before and after — note the difference over a full hour, not just a minute.
2. Check battery estimates during light use; the removal of a scheduled waker shows up as modestly longer projected runtime.
3. After each Windows feature update, verify the board has not returned — re-apply Fix 6 if it has.
4. For the broader background-process cleanup this belongs to, see our guides on [turning off Windows tips](/articles/best-way-to-turn-off-windows-tips-and-suggestions/) and [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/). Microsoft documents widgets behavior at [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

The Widgets Board is a content pipeline disguised as a taskbar icon — polling, rendering, and waking your CPU all day for headlines you never read. The best fix escalates cleanly: quiet the feeds, restrict the background permissions, repair the corrupted state, and disable the board entirely if you never use it. Each step is reversible, each step is measurable, and the last one gives you the quiet idle your laptop was supposed to have.
