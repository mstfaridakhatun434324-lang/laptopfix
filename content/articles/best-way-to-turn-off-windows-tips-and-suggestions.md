---
title: "The Best Way to Turn Off Windows Tips and Suggestions"
slug: best-way-to-turn-off-windows-tips-and-suggestions
date: 2026-10-10
categories: ["performance"]
tags: ["windows tips", "suggestions", "notifications", "disable tips", "windows 11"]
description: "Stop Windows tips, suggestions, and spotlight nags for good — every toggle in Settings, plus the registry and policy methods that survive updates."
thumbnail: "/images/thumbs/best-way-to-turn-off-windows-tips-and-suggestions.webp"
faqs:
  - q: "Do Windows tips and suggestions slow down my computer?"
    a: "Modestly, but measurably on low-end machines. The tips system runs background processes that fetch content, display notifications, and occasionally trigger the Runtime Broker and search components. Disabling tips will not transform a slow laptop, but it removes a constant source of background activity, popups, and CPU wake-ups — worthwhile as part of a broader cleanup."
  - q: "Why do tips keep coming back after Windows updates?"
    a: "Feature updates frequently reset notification and privacy settings to their defaults, which re-enables tips and suggestions. Microsoft also introduces new tip surfaces with each release. The registry and group policy methods in this guide are more persistent than Settings toggles and survive most updates, which is why power users prefer them."
  - q: "Will turning off suggestions break anything I need?"
    a: "No. Tips and suggestions are purely informational — tutorials, feature highlights, and Microsoft service promotions. Nothing functional depends on them. Windows Update, security features, and all applications work identically with tips disabled. You lose only the popups telling you about features."
  - q: "What's the difference between tips, suggestions, and Spotlight?"
    a: "Tips are the notification popups about Windows features. Suggestions include Start menu app suggestions and Settings suggestions. Spotlight is the rotating lock-screen imagery with fun facts. They are controlled by separate toggles in different Settings pages, which is why turning off one does not silence the others — this guide covers all three."
---

Windows loves to tell you about itself. Tips pop up about features you will never use, the Start menu suggests apps you did not ask for, Settings pages nudge you toward Microsoft services, and the lock screen cycles through Spotlight trivia. Individually these are minor; collectively they are a steady drip of interruptions — and on low-end hardware, a steady drip of background activity from the processes that fetch and display them.

Turning them all off requires visiting several Settings pages, because Microsoft scatters the toggles deliberately. This guide collects every one, in order, plus the persistent methods that survive updates.

## Why this happens

- **Scattered toggles by design:** Tips, suggestions, and Spotlight live in Notifications, Personalization, Privacy, and System settings — no single master switch exists.
- **Background content fetching:** The tips system periodically downloads content and images, waking the CPU, disk, and network for something you did not request.
- **Runtime Broker involvement:** Displaying tips and suggestions routes through Runtime Broker and notification processes, adding to their background load.
- **Update resets:** Feature updates restore many of these toggles to their defaults, so the nags return even after you silenced them.
- **New surfaces per release:** Each Windows release adds new suggestion placements — in Settings, File Explorer, or the widgets board — that default to on.
- **Sync across devices:** With settings sync enabled, a fresh install can re-import tip preferences from another PC.
- **OEM additions:** Manufacturers add their own tip and offer popups (Dell, HP, Lenovo utilities), which are separate from Microsoft's and need separate disabling.
- **Advertising-adjacent suggestions:** Some "suggestions" are effectively promotions for Microsoft services and partner apps, which is why they are so persistent.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off the main tips toggle

1. Open **Settings → System → Notifications**.
2. Scroll to the bottom and expand **Additional settings** (Windows 11) or find the tips checkboxes (Windows 10).
3. Uncheck **Get tips and suggestions when using Windows** and **Suggest ways to get the most out of Windows and finish setting up this device**.
4. This silences the largest single source of tip popups. Test for a day — most users notice the difference immediately.

### Fix 2: Remove Start menu suggestions

1. Open **Settings → Personalization → Start**.
2. Toggle off **Show suggestions for tips, shortcuts, new apps, and more** (wording varies slightly by Windows version).
3. While here, toggle off **Show recently added apps** and **Show most used apps** if you want a fully static, distraction-free Start menu.
4. Right-click any suggested app tile still showing and choose **Unpin** — leftovers from before the toggle need manual removal.

### Fix 3: Silence Settings and lock-screen suggestions

1. Open **Settings → Privacy & security → General** and toggle off **Show me suggested content in the Settings app**.
2. Go to **Settings → Personalization → Lock screen** and change the background from **Windows spotlight** to **Picture** or **Slideshow**.
3. If a **"Get fun facts, tips, tricks, and more on your lock screen"** checkbox appears, uncheck it.
4. These two pages cover the suggestions most guides miss — the Settings app nudges and the lock-screen trivia.

### Fix 4: Disable Spotlight and widgets-board suggestions

1. In **Settings → Personalization → Background**, avoid **Windows spotlight** as the desktop background — it phones home for new images.
2. Open the **Widgets board**, click the settings gear, and turn off suggested content and notification badges for widgets you do not use — or disable the board entirely from **Taskbar settings**.
3. In **File Explorer → View → Options**, check for suggestion or sync-provider notifications and disable them.
4. Each of these is a small content pipeline you did not ask for; closing them reduces both interruptions and background network activity.

### Fix 5: Lock it with the registry (persistent method)

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager`.
2. Set these DWORD values to **0**: **SubscribedContent-338389Enabled** (tips), **SubscribedContent-353698Enabled** (suggestions), and **RotatingLockScreenEnabled** (Spotlight).
3. Also set **SystemPaneSuggestionsEnabled** to 0 to block Settings-app suggestions at the source.
4. Export the key first as backup. Registry-level changes survive the feature updates that reset Settings toggles.

### Fix 6: Use group policy on Pro editions

1. Press **Win + R**, type `gpedit.msc`, and navigate to **Computer Configuration → Administrative Templates → Windows Components → Cloud Content**.
2. Enable **Do not show Windows tips** and **Turn off all Windows spotlight features**.
3. Also check **User Configuration → Administrative Templates → Start Menu and Taskbar** for suggestion-related policies.
4. Run `gpupdate /force` in an admin prompt and restart. Policy-level disabling is the most durable method available — Microsoft documents these policies at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Silence manufacturer popups separately

1. Open your manufacturer's utility (Dell SupportAssist, HP Support Assistant, Lenovo Vantage, MyASUS) and find its **notifications/offers** settings.
2. Disable promotional notifications, "tips," and offer popups — these are independent of Microsoft's toggles.
3. Check **Task Manager → Startup apps** for manufacturer marketing agents and disable them.
4. Uninstall manufacturer "welcome" or "jumpstart" apps entirely if you never use them — they exist largely to show you offers.

### Fix 8: Verify the silence and measure the benefit

1. Use the laptop normally for two days and note the absence of popups — check the notification center (**Win + N**) for anything that slipped through.
2. In Task Manager, compare background CPU usage before and after — the gains are modest but real, especially from disabling Spotlight and content delivery.
3. If tips return after a Windows update, re-verify Fix 1's toggles first, then confirm your registry values from Fix 5 are intact.
4. For the broader background-cleanup this belongs to, see our guides on [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) and calming [Runtime Broker high CPU](/articles/how-to-fix-runtime-broker-high-cpu-on-dell-laptop/) — tips often feed both.

## Closing

Windows tips and suggestions are death by a thousand toggles — no single switch, persistent across updates, scattered through half a dozen Settings pages. Worked through in order, though, they stay off: Settings toggles for the immediate silence, registry or policy for permanence, and manufacturer utilities for the OEM layer. The result is a quieter system, fewer interruptions, and a small but real reduction in the background churn your laptop performs on Microsoft's behalf rather than yours.
