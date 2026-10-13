---
title: "Widgets Board High CPU on Windows 11? Calm It Down"
slug: what-to-do-if-widgets-board-high-cpu-windows-11
date: 2026-10-05
categories: ["performance"]
tags: ["widgets board", "high cpu", "windows 11", "widgets.exe"]
description: "The Windows 11 Widgets board eating CPU in the background? Learn what drives Widgets.exe usage and how to tame or disable it."
thumbnail: "/images/thumbs/what-to-do-if-widgets-board-high-cpu-windows-11.webp"
faqs:
  - q: "What is the Widgets board and why does it use CPU?"
    a: "The Widgets board is the weather/news panel that slides out from the left side of the Windows 11 taskbar, powered by Widgets.exe. It uses CPU because it continuously refreshes content in the background — weather, news headlines, stocks, and MSN feed items — even when you never open it. On some systems a buggy widget or a stuck refresh loop keeps it churning at 10-30% CPU indefinitely."
  - q: "Can I just uninstall the Widgets board?"
    a: "You can remove it from the taskbar easily (right-click taskbar > Taskbar settings > Widgets > off), which stops the visible board — but Widgets.exe may still run in the background. Fully disabling it requires group policy or registry changes, or uninstalling the Windows Web Experience Pack. For most users, turning off the taskbar toggle plus disabling its background activity is enough to end the CPU usage."
  - q: "Does disabling Widgets break anything in Windows 11?"
    a: "No. Widgets are a purely optional content feature — no system function depends on them. Disabling or uninstalling the Widgets board doesn't affect the Start menu, search, notifications, or any app. The only thing you lose is the at-a-glance weather/news panel, which most users never open anyway."
  - q: "Why did Widgets suddenly start using high CPU?"
    a: "Sudden spikes usually follow a Windows update (which can reset widget settings or introduce a buggy Web Experience Pack version), a misbehaving third-party widget, or a stuck content refresh — e.g., the news feed retrying a failed connection in a tight loop. Check Task Manager's Details tab: if Widgets.exe CPU drops when you disconnect from the network, a feed refresh loop is the likely cause."
---

That little weather widget on your taskbar looks harmless, but behind it runs `Widgets.exe` — a Chromium-based process that fetches news, weather, and stocks around the clock. Most of the time it sips CPU. But when a feed gets stuck, a widget misbehaves, or an update resets its settings, it can burn 10–30% CPU permanently, warming up your laptop and draining battery for content you never look at.

The fix ranges from a simple taskbar toggle to fully removing the component. Start gentle — most cases resolve with the first two steps. If you want the per-brand variants afterward, they follow the same principles with OEM-specific paths.

## Why this happens

- **Stuck content refresh loop**: A news or weather feed failing and retrying aggressively keeps the renderer busy.
- **Buggy Web Experience Pack update**: The Widgets platform updates through the Store, and bad versions spike CPU.
- **Third-party widgets misbehaving**: Added widgets (sports, to-do, third-party) with buggy refresh logic.
- **Settings reset by Windows Update**: Updates re-enable Widgets and its background activity after you turned it off.
- **Chromium renderer overhead**: Widgets.exe is Edge/Chromium-based — each widget is effectively a background browser tab.
- **Animated taskbar widget**: The live weather animation on the taskbar itself repaints constantly on some systems.
- **Network-dependent retry storms**: On flaky connections, failed feed fetches retry in tight loops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets.exe is the actual culprit

Verify before you start disabling things.

1. Open **Task Manager** > **Processes** and look for **Widgets** or `Widgets.exe` — check both CPU and **Power usage** columns.
2. Switch to the **Details** tab, find `Widgets.exe`, right-click > **Open file location** — it should be a Microsoft-signed binary.
3. Test the network theory: disconnect Wi-Fi for 2 minutes and watch CPU — a drop points to a feed refresh loop.
4. Open the Widgets board (Win + W) and note whether CPU spikes while it's open vs. closed — spikes only when open suggest a specific widget.
5. If Widgets.exe is calm and something else is hot, stop here and chase the real process instead.

### Fix 2: Turn off the Widgets taskbar entry and board

The quick win that fixes most cases.

1. Right-click the taskbar > **Taskbar settings** > toggle **Widgets** to **Off**.
2. Restart the laptop and check Task Manager — on many systems this alone stops Widgets.exe from running.
3. If Widgets.exe still appears, open the board once with **Win + W** (it can still open via shortcut), click your profile icon > sign out of the Widgets account to stop personalized feed syncing.
4. Remove any third-party widgets from the board before closing it — click **...** on each widget > **Remove widget**.
5. Monitor for a day; if CPU stays flat, you're done — the board was the entire problem.

### Fix 3: Disable Widgets background activity

Stop it from working when the board is closed.

1. Open **Settings** > **Apps** > **Installed apps** and find **Windows Web Experience Pack**.
2. Click **...** > **Advanced options** > set **Background apps permissions** to **Never**.
3. Under **Settings** > **Personalization** > **Taskbar**, confirm Widgets stays **Off**.
4. Open **Task Manager** > **Startup apps** and disable anything widget/feed related.
5. Reboot and verify Widgets.exe no longer appears in Task Manager at idle.

### Fix 4: Update or reinstall the Web Experience Pack

Fix a buggy Widgets platform version.

1. Open the **Microsoft Store** > **Library** > **Get updates** and install any update for **Windows Web Experience Pack**.
2. If no update is offered and CPU is still high, uninstall it: **Settings** > **Apps** > **Installed apps** > **Windows Web Experience Pack** > **Uninstall**.
3. Reboot — Windows will either run fine without it or reinstall a fresh copy via the Store.
4. If you want it back, search the Microsoft Store for **Windows Web Experience Pack** and reinstall.
5. Test CPU for a day after reinstall — a fresh platform copy resolves version-specific CPU bugs.

### Fix 5: Disable Widgets via Group Policy or registry

The permanent, enterprise-grade off switch.

1. For Pro/Enterprise: press **Win + R**, type `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > enable **Allow widgets** set to **Disabled**.
2. For Home edition: open **regedit** and go to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh`.
3. Create a DWORD (32-bit) named **AllowNewsAndInterests** set to `0` (create the Dsh key if missing).
4. Reboot — the Widgets toggle disappears from Taskbar settings and Widgets.exe stays dead.
5. To reverse, delete the value or set the policy back to **Not Configured**; Microsoft documents policy behavior at [Microsoft support](https://support.microsoft.com/en-us/windows).

### Fix 6: Address the underlying feed/network issue

Fix the refresh loop instead of just silencing it.

1. If disconnecting from the network calmed Widgets.exe, the issue is a feed endpoint — check for proxy/VPN interference with MSN feed domains.
2. Temporarily disable your VPN and test — some VPNs break the widget feed's connections, causing retry storms.
3. In **Settings** > **Network & internet**, check for metered-connection weirdness — set your connection as metered temporarily to throttle background feeds as a test.
4. Clear the Edge/WebView cache: Widgets render through WebView2 — open **Settings** > **Apps** > **Installed apps** > **Microsoft Edge WebView2 Runtime** and repair it.
5. Re-enable Widgets after the network fix and confirm CPU stays normal — you get the feature back without the cost.

### Fix 7: Reduce overall background content load

Lower the ambient churn that feeds widget-like processes.

1. Open **Settings** > **System** > **Notifications** and disable **suggestions** and promotional notification types.
2. Set lock screen background away from **Windows spotlight** (**Settings** > **Personalization** > **Lock screen** > **Picture**).
3. In **Task Manager** > **Startup apps**, disable feed-adjacent apps (news apps, weather apps you don't use).
4. For the full background cleanup, work through [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).
5. If general slowness persists beyond Widgets, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Closing

Widgets.exe is a background browser tab wearing a taskbar costume — when its feeds misbehave, it burns CPU for nothing. The taskbar toggle plus background-permission cutoff resolves most cases in under two minutes; the policy/registry switch makes it permanent. Either way, you lose nothing Windows actually needs.
