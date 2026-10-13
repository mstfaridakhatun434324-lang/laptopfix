---
title: "How to Fix Widgets Board High CPU Usage on Windows 11"
slug: "how-to-fix-widgets-board-high-cpu-windows-11"
date: "2026-09-13"
categories: ["performance"]
tags: ["widgets board", "high cpu", "windows 11", "widgets.exe"]
description: "Widgets.exe or Widgets Board burning CPU in the background? Calm the Windows 11 widgets feed with these targeted fixes."
thumbnail: "/images/thumbs/how-to-fix-widgets-board-high-cpu-windows-11.webp"
faqs:
  - q: "What is the Widgets Board process in Task Manager?"
    a: "The Widgets Board runs as Widgets.exe and powers the slide-out panel you open with Win+W or the weather widget on the taskbar. It continuously refreshes news, weather, stocks, and sports content in the background so the panel feels instant when opened. That background refreshing is what shows up as CPU and network usage even when you never open the board."
  - q: "Is it safe to disable the Widgets Board completely?"
    a: "Yes. Disabling widgets removes the taskbar weather icon and the Win+W panel, but nothing else in Windows depends on them. Your news apps, browser bookmarks, and weather apps all keep working independently. If you later miss the glanceable weather, re-enabling takes ten seconds in Settings under Personalization and Taskbar."
  - q: "Why does Widgets.exe use CPU when I never open it?"
    a: "The board pre-fetches and updates its content on a schedule regardless of whether you open it, similar to how a phone refreshes widgets overnight. On some systems a stuck feed or a corrupted board cache makes it refresh far more aggressively than designed. Clearing the cache or disabling the feature entirely stops the background churn."
  - q: "Does disabling widgets improve battery life?"
    a: "Modestly. The widgets service wakes the network stack and CPU on its refresh schedule, which works against sleep efficiency. On battery-conscious laptops, disabling widgets alongside other background consumers like [Teams autostart](/articles/what-to-do-if-teams-autostart-slowing-laptop/) produces a measurable improvement in idle drain over a full day."
---

The Windows 11 Widgets Board is the panel that slides out when you press Win+W, full of news headlines, weather, stocks, and sports scores. It is powered by a background process called Widgets.exe, and on some laptops that process develops an unhealthy appetite, consuming 10 to 25 percent CPU around the clock even if you have never opened the board in your life.

The mechanism is simple: the board refreshes its content on a schedule so it feels instant when opened. When a feed gets stuck or the board's cache corrupts, that polite scheduled refresh turns into a frantic loop. Because the taskbar weather widget keeps the service alive, the CPU burn continues through your entire session, warming the laptop and draining the battery.

The fixes range from a simple cache clear to removing the taskbar widget to disabling the board entirely. Start with the lightest option and escalate only if CPU stays high.

## Why this happens

- **A stuck news or weather feed:** A feed that fails to complete its refresh retries aggressively, looping CPU usage.
- **Corrupted widgets cache:** Damaged cached content makes the board re-download and re-render continuously.
- **Taskbar weather widget keeping it alive:** The taskbar widget pins the Widgets.exe process in memory for the whole session.
- **Too many pinned widgets:** Each pinned widget adds its own refresh timer and rendering cost.
- **WebView2 rendering issues:** The board renders in Edge's WebView2 runtime; a broken runtime install causes excessive CPU.
- **Aggressive refresh after sleep:** Waking from sleep can trigger a backlog of missed refreshes all firing at once.
- **Personalized content churn:** Tailored news and ads refresh more frequently than a static weather widget would.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets.exe is the offender

Verify the process name and its CPU pattern before changing settings, so you know the fix actually worked.

1. Press Ctrl+Shift+Esc to open Task Manager.
2. Sort by CPU and look for Widgets.exe near the top.
3. Watch for three minutes; the board should be mostly idle between refreshes.
4. If it sustains double-digit CPU, proceed with the fixes below.
5. Note the baseline so you can compare after each change.

### Fix 2: Remove the taskbar widgets button

Removing the taskbar entry stops the always-on widget host that keeps Widgets.exe running all session.

1. Right-click an empty area of the taskbar and choose Taskbar settings.
2. Find the Widgets toggle near the top of the list.
3. Switch Widgets to Off.
4. The weather icon disappears from the taskbar immediately.
5. Check Task Manager to see if Widgets.exe exits or calms down.

### Fix 3: Clear the widgets board cache

A corrupted cache is a common cause of refresh loops. Clearing it forces the board to rebuild cleanly.

1. Close the widgets board if it is open with Win+W toggling.
2. Press Win+R, type %localappdata%\Microsoft\Windows, and press Enter.
3. Look for widgets-related cache folders and rename rather than delete them as a safety step.
4. Alternatively, sign out and back in, which clears in-memory board state.
5. Re-check CPU after 15 minutes of normal use.

### Fix 4: Repair the WebView2 runtime

The board renders its content through Microsoft Edge WebView2. A damaged runtime makes rendering far more CPU-intensive than it should be.

1. Open Settings, Apps, Installed apps.
2. Search for Microsoft Edge WebView2 Runtime.
3. Click the three dots and choose Modify, then Repair.
4. Let the repair complete and restart the laptop.
5. Test Widgets.exe CPU with the board both closed and open.

### Fix 5: Disable the Widgets Board with Group Policy

On Windows 11 Pro, Group Policy can disable the board entirely, which is cleaner than just hiding the taskbar button.

1. Press Win+R, type gpedit.msc, and press Enter.
2. Navigate to Computer Configuration, Administrative Templates, Windows Components, Widgets.
3. Double-click Allow widgets and set it to Disabled.
4. Click Apply and OK, then restart.
5. Widgets.exe should no longer launch at all.

### Fix 6: Uninstall the Web Experience Pack

The Widgets Board ships as the Windows Web Experience Pack. Removing it is the most thorough option on any edition.

1. Open Terminal as administrator with Win+X.
2. Type winget list web experience to confirm the package name.
3. Run winget uninstall MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy carefully.
4. Restart the laptop after removal.
5. Verify Widgets.exe no longer appears in Task Manager.

### Fix 7: Reinstall the Web Experience Pack

When repair does not help, a clean reinstall of the package that hosts the board replaces every corrupted file. Your pinned widgets reset to defaults, which is a small price for a quiet CPU.

1. Open Terminal as administrator with Win+X.
2. Run winget uninstall MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy to remove it.
3. Restart the laptop after removal.
4. Run winget install MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy to reinstall.
5. Open the board once with Win+W, close it, and monitor CPU for an hour.

### Fix 8: Reinstall the Web Experience Pack

When repair does not help, a clean reinstall of the package that hosts the board replaces every corrupted file. Your pinned widgets reset to defaults, which is a small price for a quiet CPU.

1. Open Terminal as administrator with Win+X.
2. Run winget uninstall MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy to remove it.
3. Restart the laptop after removal.
4. Run winget install MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy to reinstall.
5. Open the board once with Win+W, close it, and monitor CPU for an hour.

## Closing

The Widgets Board is a nice-to-have that should never cost you double-digit CPU. For most people, removing the taskbar button or repairing WebView2 settles it; for those who never glance at widgets anyway, disabling the board entirely is the clean answer. Either way, verify with Task Manager that Widgets.exe is actually quiet afterward. Background CPU hogs rarely travel alone, so if the fans are still busy, check whether [Teams autostart](/articles/what-to-do-if-teams-autostart-slowing-laptop/) is also dragging down your boot. Background refresh loops rarely travel alone, so if the fans stay busy, audit your other startup consumers too. Microsoft documents background app controls in its [Windows support hub](https://support.microsoft.com/en-us/windows). Background refresh loops rarely travel alone, so if the fans stay busy, audit your other startup consumers too. Microsoft documents background app controls in its [Windows support hub](https://support.microsoft.com/en-us/windows). If the board is quiet but boot is still slow, [disabling unnecessary startup apps](/articles/how-to-disable-startup-apps-on-windows-11/) is the next step worth taking.
