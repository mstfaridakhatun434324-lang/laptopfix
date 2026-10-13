---
title: "Stop Windows Tips and Suggestions From Slowing Down Your Laptop"
slug: how-to-turn-off-windows-tips-and-suggestions-on-laptop
date: 2026-09-19
categories: ["performance"]
tags: ["windows tips", "suggestions", "notifications", "windows 11", "privacy"]
description: "Windows tips, Start menu suggestions, and lock-screen 'fun facts' are all optional — and they cost attention and background resources. Here's how to switch every one of them off."
thumbnail: "/images/thumbs/how-to-turn-off-windows-tips-and-suggestions-on-laptop.webp"
faqs:
  - q: "What are Windows tips and suggestions?"
    a: "They're Microsoft's built-in prompts: pop-up tips about features ('Did you know you can snap windows?'), suggested apps in the Start menu, 'fun facts' on the lock screen, and setup suggestions in notifications. They're delivered by the Content Delivery Manager service and are on by default. They're purely informational — turning them off changes nothing about how Windows itself works."
  - q: "Do tips and suggestions slow down my laptop?"
    a: "On modern hardware the impact is small, but it's real: the Content Delivery Manager periodically downloads suggestion content, and rendering Start menu suggestions and lock-screen spotlights uses CPU, disk, and network in the background. On budget laptops with 4–8 GB of RAM and spinning hard drives, every background task matters. The bigger cost is distraction — pop-ups break focus multiple times a day."
  - q: "Where is the main toggle for tips in Windows 11?"
    a: "The main switch is at Settings > System > Notifications. Scroll to the bottom, expand 'Additional settings,' and turn off 'Get tips and suggestions when using Windows.' That stops the pop-up tips, but Start menu recommendations, lock-screen facts, and Settings suggestions each have their own separate toggles — this guide covers all of them so nothing slips through."
  - q: "Will turning off suggestions affect Windows Update or security?"
    a: "No. Tips and suggestions are a cosmetic layer — disabling them doesn't touch Windows Update, Microsoft Defender, the firewall, or any security feature. Updates still download and install on your normal schedule, and SmartScreen and Defender keep protecting you. You're only removing Microsoft's promotional and educational prompts, nothing functional."
---

Windows really wants you to discover its features. The little "Did you know?" pop-ups that slide in from the corner, the suggested apps sitting in your Start menu, the "fun facts" on the lock screen, the setup suggestions in notifications — each one is small, but together they form a constant drip of interruption on a machine you're trying to get work done on. And on budget laptops, the background service that fetches and renders all of it isn't entirely free either: Content Delivery Manager wakes up periodically to download fresh suggestion content, burning CPU cycles, disk I/O, and metered bandwidth.

The good news is that every single one of these prompts is optional. None of them is load-bearing: Windows Update, Defender, and every core feature work exactly the same with tips switched off. The bad news is that Microsoft scattered the toggles across half a dozen Settings pages, so most people turn off one or two and assume they're done — while suggestions keep appearing from the surfaces they missed. For the broader picture, see [how to speed up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); and if background load is your concern generally, start by [disabling unneeded startup programs](/articles/how-to-disable-startup-programs-windows-11/).

## Why this happens

- **Content Delivery Manager service**: the Windows component that downloads tips, suggested apps, and spotlight content in the background and injects them into Start, the lock screen, and the Settings app.
- **Defaults set during setup**: "Get tips and suggestions when using Windows" ships enabled, and the out-of-box experience never asks — so most users have never consciously turned it on.
- **Separate toggle per surface**: Start menu, lock screen, notifications, and the Settings app each have an independent suggestions switch, so disabling one leaves the others active.
- **Post-update welcome experiences**: after feature updates, Windows re-shows the "Let's finish setting up your device" flow, which re-enables several suggestion prompts.
- **Suggested apps in Start**: the "Recommended" area doubles as promotion space for Microsoft Store apps unless you switch it off.
- **Tailored experiences**: with diagnostic data enabled, Windows personalizes which tips you see — more telemetry means more prompts.
- **OEM utilities add their own**: MyASUS, Dell SupportAssist, HP Support Assistant, and Lenovo Vantage all show their own tip-style pop-ups on top of Microsoft's.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off "Get tips and suggestions when using Windows"

This is the master switch for the pop-up tips — the single toggle most people are looking for.

1. Press **Win + I** to open Settings, then go to **System > Notifications**.
2. Scroll to the very bottom and expand **Additional settings**.
3. Toggle off **"Get tips and suggestions when using Windows"** — this stops the corner pop-ups immediately.
4. While you're here, toggle off **"Offer suggestions on how I can set up my device"** to silence setup nags.
5. Toggle off **"Show the Windows welcome experience after updates and when signed in to show what's new and suggested"** to stop the full-screen prompt after updates.

### Fix 2: Remove suggestions from the Start menu

The Start menu's "Recommended" section quietly promotes apps and tips.

1. Go to **Settings > Personalization > Start**.
2. Turn off **"Show recommendations for tips, shortcuts, new apps, and more"** — this is the big one.
3. Turn off **"Show recently added apps"** if you want a fully quiet Start menu.
4. Pin the apps you actually use; with recommendations off, the section collapses to nothing useful to Microsoft's advertisers.
5. Sign out and back in (or restart) to confirm the suggested tiles are gone for good.

### Fix 3: Kill lock-screen "fun facts" and tips

The lock screen is another suggestion surface most people forget.

1. Go to **Settings > Personalization > Lock screen**.
2. Set **"Personalize your lock screen"** to **Picture** or **Slideshow** — the tips toggle only appears for these; Windows Spotlight forces Microsoft's content.
3. Uncheck **"Get fun facts, tips, tricks, and more on your lock screen"**.
4. Press **Win + L** to lock the PC and verify the screen is clean.
5. Bonus: choosing Picture instead of Spotlight also stops the background spotlight downloads — a small bandwidth and disk win on metered connections.

### Fix 4: Disable suggested content inside the Settings app

Yes, the Settings app advertises to you too.

1. Go to **Settings > Privacy & security > General**.
2. Turn off **"Show me suggested content in the Settings app"**.
3. Turn off **"Let apps show me personalized ads by using my advertising ID"** — this cuts the ad-profile building that feeds personalized suggestions.
4. Go to **Privacy & security > Diagnostics & feedback** and turn off **"Tailored experiences"** to stop diagnostic-data-driven tips.
5. Close and reopen Settings to confirm the suggestion cards have disappeared.

### Fix 5: Lock it down with Group Policy or the registry

UI toggles sometimes get reset by feature updates. Policy and registry locks stick.

1. On Windows 11 Pro: press **Win + R**, type `gpedit.msc`, and navigate to **User Configuration > Administrative Templates > Windows Components > Cloud Content**.
2. Enable **"Do not show Windows tips"** — this is the enterprise-grade kill switch.
3. In the same folder, enable **"Turn off all Windows spotlight features"** for the full quiet treatment.
4. On Windows 11 Home (no gpedit): open `regedit` and go to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager`.
5. Set the DWORDs **SubscribedContent-338389Enabled**, **SubscribedContent-353694Enabled**, and **SubscribedContent-353696Enabled** to `0` (create them if missing), then restart — these survive updates far better than UI toggles.

### Fix 6: Silence your laptop maker's own tip pop-ups

Microsoft isn't the only one interrupting you.

1. **ASUS**: open MyASUS > Settings and turn off tips and notifications — or uninstall MyASUS entirely if you never use it.
2. **Dell**: open SupportAssist > Settings and disable recommendations and proactive alert pop-ups.
3. **HP / Lenovo**: in HP Support Assistant or Lenovo Vantage settings, turn off tips, "insights," and promotional notifications.
4. Alternative: open **Task Manager > Startup apps** and disable the OEM utility from auto-starting — no startup entry, no pop-ups.
5. Keep driver-update functionality if you rely on the vendor app; disable only the marketing and "tips" surfaces.

### Fix 7: Verify everything is quiet

Confirm the job is actually done — suggestions have a habit of creeping back.

1. Restart the laptop and use it normally for a day; no tip pop-ups should appear.
2. Open **Task Manager > Processes** and look for Content Delivery Manager activity — it should sit at or near zero.
3. If a suggestion reappears after a Windows feature update, revisit Fix 5 — updates sometimes reset UI toggles but rarely touch policy or registry locks.
4. Microsoft documents the notification settings surface at its official [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the canonical reference.
5. Pair this cleanup with [trimming your startup programs](/articles/how-to-disable-startup-programs-windows-11/) for the full quiet-and-fast treatment.

## Closing

Tips and suggestions are the easiest focus and performance win in Windows 11: about five minutes of toggles, zero functional downside, and a laptop that finally stops interrupting you. The only maintenance required is a quick check after each year's feature update, since that's the one event that occasionally flips a toggle back on.
