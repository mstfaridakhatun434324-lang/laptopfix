---
title: "How to Disable Background Apps on Windows 10 (All Methods)"
slug: "how-to-disable-background-apps-on-windows-10"
date: "2026-10-10"
categories: ["performance"]
tags: ["background apps", "windows 10", "disable background", "privacy settings", "performance"]
description: "Background apps draining your Windows 10 laptop? Disable them individually, all at once, or via Group Policy — every method explained."
thumbnail: "/images/thumbs/how-to-disable-background-apps-on-windows-10.webp"
faqs:
  - q: "Where is the background apps setting in Windows 10?"
    a: "Settings > Privacy > Background apps. That's the central page: a master toggle at the top ('Let apps run in the background') plus individual toggles for every Store app below it. Unlike Windows 11, Windows 10 keeps this global switch — turning it off disables background activity for all Store apps at once. Desktop (Win32) programs aren't governed here; those need Task Manager startup management or their own settings."
  - q: "Does disabling background apps affect notifications?"
    a: "Yes, for the apps you restrict. A mail or messaging app with background access disabled can't fetch new messages or push notifications while closed — you'll only see new items when you open the app. That's the core tradeoff. Keep background access on for the 2-3 communication apps you depend on, and disable it for everything else — games, media, utilities, and manufacturer apps don't need to whisper to the internet while you work."
  - q: "What's the difference between background apps and startup apps?"
    a: "Startup apps launch when you sign in and keep running visibly or in the tray — managed in Task Manager's Startup tab. Background apps are mostly Store apps that Windows suspends but allows to run background tasks (syncs, notifications, tile updates) — managed in Settings > Privacy > Background apps. A slow laptop usually suffers from both; fixing only one leaves half the problem. Handle startup in Task Manager and background in Privacy settings."
  - q: "Will this break Windows Update or Defender?"
    a: "No. Windows Update, Microsoft Defender, and core system services are not 'background apps' — they're system services governed separately and are completely unaffected by the Background apps toggles or the Group Policy block. You cannot accidentally disable security updates or real-time protection from the Background apps page. Those switches only affect Store apps and their background tasks."
---

Windows 10's Background apps page is one of the most useful — and most ignored — performance settings on the OS. Behind it sit dozens of Store apps with permission to run background tasks: syncing, updating tiles, fetching notifications, phoning home. Individually trivial; collectively, a constant tax on your CPU, RAM, disk, and battery.

Windows 10 actually handles this better than Windows 11 in one way: it still has the global master toggle. One switch silences every Store app's background activity at once — then you re-enable just the few you need live. Combined with startup-app management, it's the closest thing to a 'make my laptop quiet' button Windows offers.

A quick vocabulary check, because the names confuse people: 'background apps' (this guide) are Store apps allowed to run tasks while closed. 'Startup apps' are programs that launch at sign-in. 'Background processes' in Task Manager include both plus system services. You'll see all three terms in Task Manager — now you know which settings page governs which.

This guide covers all three methods — per-app, global toggle, and Group Policy — plus the related startup cleanup that completes the job. Windows 11 users should see our [Windows 11 background apps guide](/articles/how-to-disable-background-apps-on-windows-11/) for the changed settings layout.

## Why this happens

- **Default-on permissions for inbox apps** — Windows 10 grants background access to its bundled apps (news, weather, sports, games) out of the box — most users never open them, but they run tasks anyway.
- **Manufacturer bloatware tasks** — Lenovo, HP, and Dell Store apps register background tasks for update checks and telemetry that wake the system on schedules.
- **Mail/Calendar syncing constantly** — The built-in Mail app's background sync is genuinely useful — but also genuinely costly; it's the biggest legitimate background consumer for many users.
- **Skype and messaging apps** — Preinstalled Skype and similar apps maintain persistent background connections whether you use them or not.
- **Desktop apps outside this system** — Chrome, Steam, Discord, and updaters run background processes that the Background apps page can't touch — they need Task Manager and their own settings.
- **Re-enabling after updates** — Feature updates reset background permissions to defaults — your careful cleanup evaporates twice a year unless you re-check.
- **Feedback and telemetry background tasks** — Windows' own feedback notifications and telemetry uploads run as background tasks on Home and Pro — disabling background apps for system-adjacent entries quiets these too.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Method 1: The global toggle (fastest)

One switch for everything. Best starting point.

1. Open **Settings > Privacy > Background apps**.
1. Turn off **Let apps run in the background** at the top — every Store app loses background permission instantly.
1. Use the laptop normally for a day. Miss notifications from a specific app? Return here and flip just that app back on (requires the master toggle on, then per-app control).
1. This is the 30-second version of the whole guide — surprisingly sufficient for most people.

### Fix 2: Method 2: Per-app surgical control

Keep the master on; silence apps individually.

1. On the same **Settings > Privacy > Background apps** page, leave the master toggle on.
1. Scroll the app list and turn off everything you don't need live: games, news, weather, sports, manufacturer apps, Skype (if unused).
1. Keep on: Mail/Calendar (if you rely on notifications), messaging apps you actually use, and any 2FA/authenticator apps.
1. Pay attention to **Your Phone / Phone Link** if it's listed — it syncs constantly; restrict it unless you actively use the phone integration.
1. The rule: if you'd open the app manually to check it, it doesn't need background access.

### Fix 3: Method 3: Group Policy (durable, Pro/Enterprise)

Survives updates and reinstalls — the administrator's option.

1. Press **Win + R**, type `gpedit.msc` > **Computer Configuration > Administrative Templates > Windows Components > App Privacy**.
1. Open **Let Windows apps run in the background** > **Enabled** > select **Deny** in the options dropdown > OK.
1. This enforces the block system-wide; users can't override it in Settings (the toggles grey out).
1. To allow exceptions later, switch the policy to **Not Configured** and manage per-app again.

### Fix 4: Clean up startup apps too (the other half)

Background settings don't cover desktop programs — Task Manager does.

1. Open Task Manager (**Ctrl + Shift + Esc**) > **Startup** tab.
1. **Disable** everything with High startup impact you don't need within seconds of login: updaters, launchers, chat clients.
1. Sort the **Processes** tab by CPU to spot desktop background hogs (Chrome, Steam, Discord helpers) — configure each app's own 'run in background' setting.
1. Both halves done = the full quiet-laptop treatment.

### Fix 5: Handle the special cases

A few apps need individual attention.

1. **Mail app too chatty?** Settings inside the Mail app > manage sync frequency per account, or restrict its background access and open it manually.
1. **Skype preinstalled but unused?** Uninstall it outright (**Settings > Apps**) rather than merely restricting it.
1. **Cortana remnants?** Our [Cortana/SearchHost guide](/articles/how-to-fix-cortana-high-cpu-on-lenovo-laptop/) covers silencing those background tasks.
1. **News and Interests eating CPU?** That taskbar weather widget refreshes on its own schedule — right-click the taskbar > **News and interests > Turn off** removes it entirely, feed and all.
1. **Widgets-like features?** Windows 10's News and Interests (taskbar weather widget) can be turned off: right-click taskbar > **News and interests > Turn off**.

### Fix 6: Re-check after feature updates

Twice a year, Windows resets your work. Reclaim it in two minutes.

1. After each feature update, revisit **Settings > Privacy > Background apps** and confirm your toggles held.
1. Re-disable anything the update re-enabled or newly installed.
1. Consider the Group Policy method (Fix 3) if you're tired of redoing it — policy survives updates.
1. Put a recurring reminder for the week after Patch Tuesday feature updates land.

## Closing

Windows 10 gives you the master switch Windows 11 took away — use it. Global toggle off, a handful of essentials back on, startup cleaned in Task Manager: that's the whole recipe for a laptop that idles quietly and holds its charge. Two minutes after every feature update keeps it that way. The official description of these settings lives in Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).
