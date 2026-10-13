---
title: "How to Turn Off Tips and Suggestions on Windows 10"
slug: how-to-turn-off-windows-tips-and-suggestions-on-windows-10
date: 2026-09-07
categories: ["performance"]
tags: ["windows 10", "tips and suggestions", "disable tips", "notifications", "privacy"]
description: "Stop Windows 10 tips, tricks, and suggested content. Turn off notifications, lock-screen tips, and Settings suggestions in minutes."
thumbnail: "/images/thumbs/how-to-turn-off-windows-tips-and-suggestions-on-windows-10.webp"
faqs:
  - q: "Where do I turn off tips and suggestions in Windows 10?"
    a: "The main switch is at Settings > System > Notifications & actions — uncheck 'Get tips, tricks, and suggestions as you use Windows'. For full coverage also disable 'Show me the Windows welcome experience' and 'Suggest ways I can finish setting up my device' on the same page, turn off 'Occasionally show suggestions in Start' under Settings > Personalization > Start, and disable 'Show suggestions occasionally in Settings' under Settings > Privacy > General."
  - q: "Do Windows 10 tips and suggestions slow down my computer?"
    a: "Slightly, yes. The tips system runs background Store-app activity — content downloads, notification scheduling, and telemetry — that consumes a small but constant amount of CPU, disk, and network. On modern machines it's negligible, but on older or low-end laptops with spinning hard drives, disabling tips is one of several small tweaks that add up to a noticeably snappier system, especially at startup."
  - q: "Will turning off tips break Windows Update or anything important?"
    a: "No. Tips and suggestions are purely informational overlays — disabling them affects nothing functional. Windows Update, security notifications, Defender alerts, and app notifications all continue normally. The only thing you'll lose is Microsoft's occasional pop-up advice and promotional suggestions for Store apps, which most experienced users consider noise rather than help."
  - q: "How do I disable tips for all users with Group Policy or registry?"
    a: "In Group Policy Editor (Pro editions), go to Computer Configuration > Administrative Templates > Windows Components > Cloud Content and enable 'Do not show Windows tips'. For the registry, create DWORD DisableSoftLanding set to 1 under HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\CloudContent. These machine-wide settings survive feature updates better than per-user toggles, making them ideal for shared or managed PCs."
---

Windows 10 loves to offer advice. Tips about features you didn't ask about, suggestions for apps you don't want, "did you know" popups after every update, and promotional suggestions tucked into the Start menu and Settings app. For new users some of this is genuinely helpful — for everyone else it's background noise that also costs a small but real amount of system resources.

Every tip notification involves background activity: the system downloads tip content, schedules notifications, and phones home with telemetry about what you clicked. On a modern SSD machine this is invisible. On an older laptop — especially one still running a spinning hard drive — it's one more thing competing for disk and CPU at startup and during idle. Disabling it all takes about three minutes and is fully reversible.

This guide covers every location where Windows 10 hides tips and suggestions, plus the Group Policy and registry methods that lock them off machine-wide. If you're on Windows 11, the steps differ slightly — see our [Windows 11 tips guide](/articles/how-to-turn-off-windows-tips-and-suggestions-on-windows-11/). For broader performance work, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Tips are on by default**: Every Windows 10 install enables tips, tricks, and suggestions out of the box — you have to opt out.
- **Feature updates re-enable them**: Major Windows 10 updates sometimes reset notification settings, bringing tips back.
- **Multiple independent toggles**: Microsoft spreads tip settings across Notifications, Start, Lock screen, and Privacy — one switch doesn't cover them all.
- **Cloud Content delivery**: The "Cloud Content" system pushes suggested apps and tips from Microsoft's servers, generating network and disk activity.
- **Welcome experience after updates**: Every feature update triggers the "welcome experience" full-screen tips unless disabled.
- **OEM additions**: Some manufacturers add their own tip overlays (Dell, HP, Lenovo utilities) on top of Microsoft's.
- **Telemetry coupling**: Tip engagement feeds Microsoft's telemetry; the background tasks that support it run whether you read the tips or not.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable the main tips toggle in Notifications

The big one — this stops the pop-up tips.

1. Open **Settings** > **System** > **Notifications & actions**.
2. Uncheck **Get tips, tricks, and suggestions as you use Windows**.
3. On the same page, uncheck **Show me the Windows welcome experience after updates and occasionally when I sign in** — this kills the full-screen tip carousel after updates.
4. Also uncheck **Suggest ways I can finish setting up my device to get the most out of Windows** — this stops the nagging setup suggestions.
5. While you're here, review the **Get notifications from these senders** list and disable any app whose notifications you never read — fewer notifications, less background work.

### Fix 2: Remove suggestions from the Start menu

Stop the "Suggested" app promotions in Start.

1. Open **Settings** > **Personalization** > **Start**.
2. Turn off **Occasionally show suggestions in Start**.
3. This stops Windows from installing suggested Store apps (Candy Crush, etc.) into your Start menu — which also saves the disk and network activity of those silent installs.
4. Right-click any already-installed suggested apps in Start and **Uninstall** them.
5. Note: this setting sometimes returns after feature updates — check it again after each major update. Microsoft's own documentation on personalization is at [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 3: Disable lock-screen tips and Settings suggestions

The two spots most people miss.

1. Open **Settings** > **Personalization** > **Lock screen**.
2. If **Background** is set to **Windows spotlight**, either uncheck **Get fun facts, tips, tricks, and more on your lock screen** or switch Background to **Picture** or **Slideshow** — Spotlight is the delivery vehicle for lock-screen tips and ads.
3. Open **Settings** > **Privacy** > **General**.
4. Turn off **Show suggested content in the Settings app** — this removes the promotional suggestions Microsoft injects into Settings pages.
5. On the same Privacy > General page, review **Let apps use advertising ID** and **Let Windows track app launches** — disabling these reduces the telemetry that powers "personalized" suggestions.

### Fix 4: Turn off Timeline and activity suggestions

Lesser-known suggestion surfaces.

1. Open **Settings** > **Privacy** > **Activity history**.
2. Uncheck **Store my activity history on this device** and **Send my activity history to Microsoft**, then click **Clear** under Clear activity history.
3. This stops the Timeline suggestions and the cross-device "pick up where you left off" prompts.
4. Open **Settings** > **System** > **Multitasking** and turn off **Show suggestions in your timeline** if present (older builds).
5. These changes also modestly reduce background disk writes — activity history is constantly logged.

### Fix 5: Disable tips via Group Policy (Pro/Enterprise)

The enterprise-grade method that survives updates.

1. Press **Win + R**, type `gpedit.msc`, press Enter.
2. Navigate to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Cloud Content**.
3. Double-click **Do not show Windows tips** > set to **Enabled** > OK.
4. In the same folder, enable **Turn off all Windows spotlight features** if you want the lock-screen suggestions gone machine-wide too.
5. Run `gpupdate /force` in an elevated Command Prompt, or just restart — the policy applies to all users on the machine.

### Fix 6: Disable tips via Registry (Home edition)

For Windows 10 Home, which lacks Group Policy Editor.

1. Press **Win + R**, type `regedit`, press Enter (approve the UAC prompt).
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\` — if there's no **CloudContent** key, right-click **Windows** > **New** > **Key** and name it `CloudContent`.
3. Inside CloudContent, right-click > **New** > **DWORD (32-bit) Value**, name it `DisableSoftLanding`, set its value to `1`.
4. Optionally add DWORD `DisableWindowsSpotlightFeatures` set to `1` in the same key to kill Spotlight suggestions.
5. Restart your PC. Back up the registry (File > Export) before editing — standard precaution.

### Fix 7: Silence OEM tip overlays

Manufacturer utilities have their own "helpful" popups.

1. **Dell**: Open Dell SupportAssist or MyDell > Settings > turn off **notifications and recommendations**. See [Dell Support](https://www.dell.com/support) for your model's app.
2. **HP**: HP Support Assistant > Settings > disable **recommendations and offers**.
3. **Lenovo**: Lenovo Vantage > settings gear > turn off **notifications** you don't want (keep critical hardware alerts on).
4. These OEM tips are separate from Windows tips — disabling Microsoft's toggles won't silence them.
5. Don't disable the OEM utility entirely — just its marketing notifications. The driver-update functionality is worth keeping.

## Closing

Windows 10's tips and suggestions are a death-by-a-thousand-cuts kind of slowdown — each one trivial, all of them together a constant low-grade drain on attention and system resources. Three minutes in Settings (or one Group Policy) silences them all, and unlike most performance tweaks, this one also makes the machine simply less annoying to use.
