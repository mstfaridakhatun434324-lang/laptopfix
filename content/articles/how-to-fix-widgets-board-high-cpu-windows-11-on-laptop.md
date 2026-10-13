---
title: "Fix the Widgets Board Eating CPU on Your Windows 11 Laptop"
slug: "how-to-fix-widgets-board-high-cpu-windows-11-on-laptop"
date: "2026-09-07"
categories: ["performance"]
tags: ["widgets board", "high cpu", "windows 11", "widgets.exe", "performance"]
description: "Widgets.exe constantly using CPU on your Windows 11 laptop? Here's how to tame or fully disable the Widgets board and get your processor back."
thumbnail: "/images/thumbs/how-to-fix-widgets-board-high-cpu-windows-11-on-laptop.webp"
faqs:
  - q: "What is Widgets.exe and why is it running?"
    a: "Widgets.exe is the background process for the Windows 11 Widgets board — the news, weather, and stocks panel that slides out from the left of the taskbar. It runs continuously to keep its content fresh, fetching updates over the network and refreshing its web-based feed, which is why it consumes CPU even when you never open the board."
  - q: "Is it safe to disable the Widgets board completely?"
    a: "Yes. Disabling Widgets removes the board and its background process but affects nothing else in Windows. The taskbar, Start menu, search, and all apps work identically. You can re-enable it at any time from taskbar settings if you change your mind."
  - q: "Why does Widgets use CPU even when I never open it?"
    a: "The board pre-loads content on a schedule so it appears instantly when opened. That means Widgets.exe wakes up regularly to download news, weather, and stock data and render its web-based cards in the background. On laptops with weaker CPUs this polling is visible as sustained few-percent CPU usage around the clock."
  - q: "Does disabling Widgets improve battery life?"
    a: "Modestly but measurably. Widgets.exe performs regular network fetches and rendering work, both of which prevent the CPU from entering deep sleep states. Removing it eliminates that baseline drain, and users typically see slightly longer idle battery life alongside the CPU savings."
---

The Windows 11 Widgets board is the panel nobody asked to keep running: slide-out news, weather, and stock cards that most laptop owners open never — yet **Widgets.exe** hums along in the background all day, fetching content and burning CPU. On a desktop with power to spare it is invisible. On a laptop, especially an ultrabook with a low-wattage processor, that constant few-percent load means warmer idle temperatures, spinning fans, and shorter battery life.

What makes Widgets particularly annoying as a CPU consumer is that it never truly sleeps. The board refreshes its feed on a timer, re-renders its web-based cards, and — on some builds — shows "dynamic" taskbar content that updates the weather widget icon continuously. Microsoft has improved its behavior across updates, but on many machines it remains a top-10 background CPU consumer for a feature nobody uses.

You have two paths: tame it (keep the board but stop the bleeding) or kill it (remove it entirely). This guide covers both, in order of increasing aggressiveness.

## Why this happens

- **Scheduled content refresh:** Widgets.exe polls Microsoft's content services on a timer to keep news and weather fresh, waking the CPU regularly.
- **Web-based rendering:** The board is essentially a hosted web view; rendering its cards costs far more CPU than a native panel would.
- **Dynamic taskbar widget:** The taskbar weather/news icon updates continuously, which keeps the process active even with the board closed.
- **Startup pre-loading:** Widgets pre-loads at login so the board opens instantly, adding permanent baseline load from boot.
- **Stuck update loop:** A corrupted Widgets cache or failed content download can send the process into a retry loop at high CPU.
- **Multiple board instances:** Bugs in some builds spawn duplicate Widgets processes that compound the load.
- **Network retries on poor connections:** On flaky Wi-Fi, failed fetches retry aggressively instead of backing off, spiking CPU.
- **Re-enabled by updates:** Feature updates frequently re-enable Widgets even after you turned it off, so the problem returns mysteriously.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets.exe is the offender

Open Task Manager, sort by CPU, and look for **Widgets** or **Windows Widgets** in the process list. Note its sustained usage over a couple of minutes — Widgets typically shows 2–8% constant load with spikes during refreshes. If it is the top background consumer on an otherwise idle system, you have confirmed the diagnosis. Also check the **Startup** tab: if Widgets-related entries are enabled, the process starts with Windows. A Dell-specific walkthrough of the same process is available in our [Widgets high CPU guide for Dell laptops](/articles/how-to-fix-widgets-board-high-cpu-windows-11-on-dell-laptop/).

1. Press **Ctrl + Shift + Esc** and sort by **CPU**.
2. Find **Widgets** / **Windows Widgets** and note sustained usage.
3. Check the **Startup** tab for Widgets entries.
4. If it is a top idle consumer, proceed with taming or disabling.

### Fix 2: Turn off the Widgets taskbar entry point

The least invasive fix: remove Widgets from the taskbar so the dynamic icon stops updating. This does not kill the background process, but it stops the constant taskbar refreshes, which account for a surprising share of the CPU. Right-click the taskbar, open taskbar settings, and toggle Widgets off. Many users find this alone drops Widgets.exe to near-zero because the dynamic content pipeline shuts down.

1. Right-click the taskbar and choose **Taskbar settings**.
2. Toggle **Widgets** to **Off**.
3. Wait 5 minutes and check Widgets.exe CPU in Task Manager.
4. If usage persists, continue to the next fix.

### Fix 3: Sign out of the Widgets board to stop personalization

The Widgets board personalizes content using your Microsoft account, and the sync/personalization pipeline is a meaningful part of its background work. Opening the board, going to its settings, and signing out (or disabling personalized content) reduces the fetch frequency. This is a middle-ground fix for people who occasionally glance at the weather widget but do not need a live news feed burning CPU all day.

1. Open the Widgets board (**Win + W**).
2. Click the profile/settings icon in the board.
3. Sign out or disable personalized content options.
4. Close the board and monitor CPU over the next hour.

### Fix 4: End the task and disable its startup entry

If taming is not enough, stop the process from auto-starting. End Widgets.exe in Task Manager, then disable any Widgets startup entries so it does not return at next login. Note that Windows may still launch it on demand if something triggers the board — this fix targets the always-running background instance, which is the CPU problem. Verify after a full restart that Widgets.exe is not running without you opening the board.

1. In Task Manager, select **Widgets** and click **End task**.
2. Open the **Startup apps** tab and disable any Widgets entry.
3. Restart Windows and check that Widgets.exe is absent from processes.
4. Confirm CPU baseline improved on the idle desktop.

### Fix 5: Uninstall the Windows Web Experience Pack

The Widgets board is delivered as a Microsoft Store package called **Windows Web Experience Pack**. Uninstalling it removes Widgets.exe entirely — the most thorough software-level fix short of policy. The board simply stops existing: **Win + W** does nothing. This is reversible through the Microsoft Store if you ever want it back. This is the fix I recommend for laptops where every watt and every CPU cycle counts.

1. Open **Settings > Apps > Installed apps**.
2. Search for **Windows Web Experience Pack**.
3. Click the three dots and choose **Uninstall**, then confirm.
4. Restart and verify Widgets.exe no longer appears in Task Manager.

### Fix 6: Disable Widgets via Group Policy or Registry

For a permanent, update-resistant disable — ideal if feature updates keep resurrecting Widgets — use policy. On Pro editions, the Group Policy Editor has a dedicated Widgets setting; on Home, the equivalent registry value works identically. This is the enterprise-grade fix: it survives updates that would otherwise re-enable the board. Back up the registry key before editing, as always.

1. On Pro: press **Win + R**, type `gpedit.msc`, and go to **Computer Configuration > Administrative Templates > Windows Components > Widgets**; enable **Allow widgets** = Disabled.
2. On Home: open regedit and go to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh`.
3. Create DWORD **AllowNewsAndInterests** = **0** (create the Dsh key if missing).
4. Restart; the Widgets toggle disappears from taskbar settings.

### Fix 7: Repair the Web Experience Pack if you want to keep Widgets

If you actually use the board but it is stuck in a high-CPU loop, the installation may be corrupted rather than merely greedy. Repair or reset the package instead of removing it: this clears the corrupted cache that causes retry loops while keeping the feature. After the repair, re-apply Fix 2's taskbar toggle if you want the board available on demand without the dynamic icon. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) if the Store repair options are missing.

1. Go to **Settings > Apps > Installed apps > Windows Web Experience Pack**.
2. Click the three dots, choose **Advanced options**.
3. Click **Repair**; if CPU is still high, use **Reset**.
4. Reopen the board once to confirm it works, then monitor CPU.

## Closing

Widgets.exe is a perfect example of a feature tax: a panel most people never open, billing CPU and battery around the clock. Whether you tame it with the taskbar toggle or remove it entirely via the Web Experience Pack uninstall, the fix takes minutes and the reclaimed idle headroom is permanent. If other background processes still burn CPU after Widgets is gone, our [Runtime Broker CPU guide](/articles/how-to-fix-runtime-broker-high-cpu-after-windows-11-update/) covers the next most common silent consumer.
