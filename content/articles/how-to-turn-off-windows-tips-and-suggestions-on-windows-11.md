---
title: "How to Disable Tips and Suggestions in Windows 11"
slug: how-to-turn-off-windows-tips-and-suggestions-on-windows-11
date: 2026-09-08
categories: ["performance"]
tags: ["windows 11", "tips and suggestions", "disable tips", "notifications", "privacy"]
description: "Turn off Windows 11 tips, tricks, and suggested content everywhere — Settings, Start menu, lock screen, and widgets — step by step."
thumbnail: "/images/thumbs/how-to-turn-off-windows-tips-and-suggestions-on-windows-11.webp"
faqs:
  - q: "Where is the tips toggle in Windows 11 Settings?"
    a: "Open Settings > System > Notifications, scroll to Additional settings, and uncheck 'Suggest ways to get the most out of Windows', 'Show me the Windows welcome experience after updates', and 'Get tips and suggestions when using Windows'. Then go to Settings > Privacy & security > General and turn off 'Show me suggested content in the Settings app' — that covers the two main locations where Windows 11 pushes tips."
  - q: "Why do Windows 11 tips keep coming back after updates?"
    a: "Feature updates (like 24H2) sometimes reset notification and personalization preferences to defaults, re-enabling tips you previously turned off. The welcome experience is also deliberately triggered after major updates to showcase new features. After every feature update, spend two minutes re-checking the toggles in Settings > System > Notifications > Additional settings and Settings > Privacy & security > General — it becomes second nature."
  - q: "Does disabling tips improve Windows 11 performance?"
    a: "Modestly. The tips system drives background Store-app activity — Runtime Broker permission checks, content downloads, and scheduled notifications — that consumes CPU, disk, and memory. Disabling tips won't transform a slow PC alone, but combined with pruning startup apps and background apps it's part of a meaningful cleanup, and it noticeably reduces background noise on lower-end laptops."
  - q: "Can I disable Windows 11 tips with the registry?"
    a: "Yes. Create DWORD values DisableSoftLanding = 1 and DisableWindowsSpotlightFeatures = 1 under HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\CloudContent to kill tips and Spotlight suggestions machine-wide. Windows 11 Pro users can instead use Group Policy: Computer Configuration > Administrative Templates > Windows Components > Cloud Content > 'Do not show Windows tips' set to Enabled — the same policy Windows 10 uses."
---

Windows 11 is chattier than it needs to be. Tips about Snap layouts, suggestions for apps in the Start menu, the full-screen "welcome experience" after every update, promotional content inside the Settings app itself, and suggested stories in the Widgets board. Each one is a small background workload — content fetches, notification scheduling, Runtime Broker activity — and together they're a constant low-grade tax on your system and your attention.

The good news: unlike some Windows behaviors, tips are fully optional and every toggle is in Settings (no registry hacking required for the basics). The bad news: Microsoft scatters them across four or five different pages, so most people turn off one switch and wonder why the tips keep coming.

This guide hits every location. If you're still on Windows 10, the menus differ — see our [Windows 10 tips guide](/articles/how-to-turn-off-windows-tips-and-suggestions-on-windows-10/). If tips are driving [Runtime Broker high CPU](/articles/how-to-fix-runtime-broker-high-cpu-after-windows-11-update/), disabling them is also part of that fix.

## Why this happens

- **On by default, everywhere**: A fresh Windows 11 install enables tips in Notifications, Start, Settings, lock screen, and Widgets simultaneously.
- **Feature updates reset toggles**: 24H2 and other major updates have been known to flip notification preferences back to defaults.
- **Welcome experience is update-triggered**: Every feature update deliberately launches the full-screen tips carousel unless you've disabled it.
- **Cloud Content pushes suggestions**: Microsoft's Cloud Content system delivers suggested apps and tips from the cloud, creating ongoing network and disk activity.
- **Widgets board suggestions**: The Widgets board mixes news, tips, and sponsored suggestions that refresh in the background.
- **OEM utilities add their own**: Dell, HP, Lenovo, and ASUS utilities layer manufacturer tips on top of Microsoft's.
- **Telemetry feedback loop**: Tip engagement data feeds the suggestion engine — the background tasks run regardless of whether you ever read a tip.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable tips in Notifications settings

The primary switch — stop the popups.

1. Open **Settings** > **System** > **Notifications**.
2. Scroll down and expand **Additional settings**.
3. Uncheck **Get tips and suggestions when using Windows**.
4. Uncheck **Suggest ways to get the most out of Windows and finish setting up this device**.
5. Uncheck **Show me the Windows welcome experience after updates and when signed in to show what's new and suggested** — this kills the post-update full-screen carousel.

### Fix 2: Remove suggested content from Settings and Start

The in-app suggestions most people miss.

1. Open **Settings** > **Privacy & security** > **General**.
2. Turn off **Show me suggested content in the Settings app** — this removes the promotional cards Microsoft injects into Settings pages.
3. Open **Settings** > **Personalization** > **Start**.
4. Turn off **Show recommendations for tips, app promotions, and more** (wording varies by build — on some it's **Show suggestions for tips, shortcuts, new apps, and more**).
5. This also stops Windows from auto-installing suggested Store apps into your Start menu. Microsoft documents these options at [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 3: Silence the Widgets board and lock screen

Two more suggestion surfaces.

1. Open the **Widgets board** (Win + W), click the **…** or settings, and turn off suggested stories / personalized content you don't want — or disable Widgets entirely: **Settings** > **Personalization** > **Taskbar** > turn off **Widgets**.
2. For the lock screen: **Settings** > **Personalization** > **Lock screen** — if using **Windows spotlight**, uncheck **Get fun facts, tips, tricks, and more on your lock screen**, or switch to **Picture**.
3. Spotlight content downloads new images and tips regularly — disabling it saves both bandwidth and background activity.
4. If you actually like the rotating wallpapers, keep Spotlight but know it's one of the background content-fetch tasks.
5. Check **Settings** > **System** > **Notifications** for **Widgets** as a notification sender and disable it if you don't want widget notifications.

### Fix 4: Prune notification senders broadly

Tips aren't the only background noise.

1. In **Settings** > **System** > **Notifications**, scroll through the per-app sender list.
2. Turn off notifications for apps you never use — preinstalled games, trial apps, manufacturer bloat.
3. Each enabled sender can wake background tasks; each disabled one is a small saving.
4. Use **Do not disturb** scheduling (same page) to automatically silence everything during focus hours or overnight.
5. Keep notifications on for things that matter (security, calendar, messaging) — this is about pruning, not scorched earth.

### Fix 5: Disable tips via Group Policy (Pro)

The method that survives feature updates.

1. Press **Win + R**, type `gpedit.msc`, press Enter.
2. Go to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Cloud Content**.
3. Enable **Do not show Windows tips**.
4. Optionally enable **Turn off all Windows spotlight features** in the same folder.
5. Run `gpupdate /force` in an elevated terminal or restart. Machine-wide policies aren't reset by feature updates the way per-user toggles can be.

### Fix 6: Disable tips via Registry (Home)

For Windows 11 Home without Group Policy.

1. Press **Win + R**, type `regedit`, approve the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\` and create a **CloudContent** key if missing (right-click > New > Key).
3. Add DWORD `DisableSoftLanding` = `1` and DWORD `DisableWindowsSpotlightFeatures` = `1`.
4. Also consider per-user: `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager` — set `SubscribedContent-338389Enabled`, `SubscribedContent-353698Enabled`, and `SystemPaneSuggestionsEnabled` to `0` to kill Start and Settings suggestions at the user level.
5. Export the key (File > Export) before editing, then restart.

### Fix 7: Quiet the OEM utilities

Manufacturer popups are separate from Windows tips.

1. **Dell**: MyDell/SupportAssist > settings > disable promotional notifications ([Dell Support](https://www.dell.com/support)).
2. **HP**: HP Support Assistant > settings > turn off offers and recommendations (see HP's support site for your model).
3. **Lenovo**: Lenovo Vantage > settings > reduce notifications to critical only ([Lenovo Support](https://support.lenovo.com/us/en/)).
4. **ASUS**: Armoury Crate / MyASUS > settings > disable news and offers.
5. Keep driver-update notifications on — just kill the marketing.

## Closing

Windows 11 buries its tip toggles across half a dozen pages precisely because Microsoft would prefer you leave them on. Ten minutes of turning them all off buys you a quieter, slightly faster machine — and unlike most performance tweaks, you'll notice this one every single day in the absence of interruptions.
