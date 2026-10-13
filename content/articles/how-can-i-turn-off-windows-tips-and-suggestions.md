---
title: "How to Turn Off Windows Tips and Suggestions"
slug: how-can-i-turn-off-windows-tips-and-suggestions
date: 2026-09-13
categories: ["performance"]
tags: ["tips", "suggestions", "notifications", "windows 11"]
description: "Annoyed by Windows tips, suggestions, and ads? Turn them all off — Settings, Lock screen, Start menu, and File Explorer — in minutes."
thumbnail: "/images/thumbs/how-can-i-turn-off-windows-tips-and-suggestions.webp"
faqs:
  - q: "What are Windows tips and suggestions exactly?"
    a: "They are Microsoft's built-in prompts: 'tips' teach you features, 'suggestions' recommend apps and settings, and together they include what most people experience as ads — for Microsoft 365, OneDrive, Edge, and Store apps. They appear as notifications, on the Lock screen, in the Start menu's Recommended section, and inside File Explorer."
  - q: "Will turning off suggestions break anything in Windows?"
    a: "No. These are purely promotional and educational surfaces — disabling them removes notifications and recommendations but changes no functionality. Windows Update, security features, and all apps keep working exactly as before. You are only silencing the marketing layer, not any system capability."
  - q: "Why do suggestions keep coming back after Windows updates?"
    a: "Feature updates sometimes reset notification and personalization settings to Microsoft's defaults, re-enabling suggestions you previously turned off. It is worth re-checking the toggles in this guide after each annual feature update. Cumulative monthly updates rarely reset them, so this is mostly a once-a-year chore."
  - q: "Is there a difference between tips and the 'suggested' apps in Start?"
    a: "Yes. Tips are the notification-style popups, while Start menu suggestions are app promotions in the Recommended section. They are controlled by separate toggles, which is why turning off one does not silence the other. This guide covers both, plus the Lock screen and File Explorer variants most guides miss."
---

Windows has a lot to say. Tips about features you will never use. Suggestions for apps you will never install. Lock screen "fun facts" that are advertisements. Start menu recommendations for software you did not ask about. Individually they are minor; collectively they are a constant low-grade interruption — and on lower-end laptops, the background content fetching behind them is not free either.

The good news: every one of these surfaces has an off switch. The bad news: Microsoft scattered them across four different settings areas, so most people only find half of them. This guide gets all of them — notifications, Lock screen, Start menu, and File Explorer — in one pass.

## Why this happens

- **Microsoft's engagement strategy:** Tips and suggestions are a deliberate channel for promoting Microsoft services — they are on by default because most users never look for the switches.
- **Settings are scattered:** The toggles live in Notifications, Personalization, and Folder Options separately, so partial fixes feel like the problem persists.
- **Feature updates reset toggles:** Annual Windows updates restore defaults, silently re-enabling suggestions you turned off months ago.
- **"Suggestions" is several features:** Notification tips, Lock screen spotlight content, Start recommendations, and Explorer sync-provider notifications are independent systems.
- **OEM additions:** Laptop manufacturers add their own tip and promo utilities on top of Microsoft's, doubling the noise on factory images.
- **Background content downloads:** Suggestion tiles and spotlight images download in the background, costing bandwidth and a little CPU on metered or slow connections.
- **New-user defaults:** Every new user account starts with all of these enabled, so shared laptops re-expose the noise per profile.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Silence notification tips and suggestions

1. Open **Settings → System → Notifications**.
2. Scroll to the bottom and expand **Additional settings** (Windows 11 24H2) — or look for the checkboxes on older builds.
3. Uncheck **Show the Windows welcome experience after updates**, **Suggest ways I can finish setting up my device**, and **Get tips and suggestions when I use Windows**.
4. These three toggles kill the notification-style tips, the post-update nag screens, and the "suggested" popups in one move.

### Fix 2: Clean up the Lock screen

1. Go to **Settings → Personalization → Lock screen**.
2. If **Personalize your lock screen** is set to **Windows spotlight**, the rotating images and "fun facts" are ad-adjacent content — switch it to **Picture** or **Slideshow** with your own images.
3. Uncheck **Get fun facts, tips, tricks, and more on your lock screen**.
4. The Lock screen is now just a lock screen — no promotions, no background content downloads. This also helps slightly on metered connections.

### Fix 3: Remove Start menu suggestions

1. Go to **Settings → Personalization → Start**.
2. Turn off **Show recommendations for tips, shortcuts, new apps, and more**.
3. If your build shows **Show suggested content in Settings** under **Privacy & security**, turn that off too.
4. The Start menu's Recommended section now shows only your actual recent files — or nothing, if you also disable recent items. Either way, no more app ads.

### Fix 4: Stop File Explorer's sync-provider notifications

1. Open File Explorer, click the **...** menu → **Options** → **View** tab.
2. Uncheck **Show sync provider notifications** and click **OK**.
3. These are the OneDrive upsell banners inside Explorer windows — the most ad-like of all the suggestion surfaces.
4. While you are here, uncheck **Show notifications for** anything else promotional your build lists. Explorer-specific annoyances pair well with our [slow Explorer fixes](/articles/how-to-fix-windows-11-slow-after-update-youtube/) if the app itself is sluggish too.

### Fix 5: Remove manufacturer tip and promo utilities

1. Open **Settings → Apps → Installed apps** and look for your laptop maker's "experience," "welcome," or "support" apps that push tips.
2. Uninstall or disable the ones that nag — keep only genuine driver/update utilities you use.
3. Check **Task Manager → Startup apps** for promo agents and disable them.
4. Dell, HP, and Lenovo each document their utilities on their support sites — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — if you are unsure which tool does what before removing it.

### Fix 6: Lock it down with Group Policy or Registry (Pro and persistent)

1. On Windows 11 Pro: press **Win + R**, type `gpedit.msc`, and go to **Computer Configuration → Administrative Templates → Windows Components → Cloud Content**.
2. Enable **Turn off all Windows spotlight features** and **Do not show Windows tips**.
3. On Home edition, the Settings toggles from Fixes 1–4 are sufficient — the policy route just makes them harder for updates to revert.
4. Re-check these after each annual feature update, since that is when Microsoft is most likely to reset them.

### Fix 7: Quiet the remaining background noise

1. In **Settings → Privacy & security → General**, turn off **Let apps show me personalized ads by using my advertising ID** and **Show me suggested content in the Settings app**.
2. In **Settings → Apps → Installed apps**, uninstall preinstalled third-party apps that push their own notifications (trial games, shopping apps).
3. Review **Settings → System → Notifications** per-app list and disable notification permission for anything you do not want hearing from.
4. For the broader project of trimming background activity that costs performance as well as attention, our [startup-trimming steps](/articles/how-do-i-fix-windows-11-using-too-much-ram-idle/) in the RAM guide double as a notification-hygiene pass.

## Closing

Windows tips and suggestions are not one setting but five, scattered across Notifications, Personalization, Explorer options, and Privacy. Work through all of them once, re-check after annual updates, and Windows finally shuts up — leaving you with an operating system instead of a billboard.

There is a pleasant side effect beyond the silence: fewer suggestion surfaces means less background downloading of spotlight images, ad tiles, and tip content. On metered connections and older hardware, that translates to real bandwidth and a small but measurable reduction in background activity. A quieter Windows is, in a small way, a faster Windows too.
