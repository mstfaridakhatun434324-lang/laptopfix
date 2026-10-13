---
title: "Teams Autostart Slowing Your Laptop? Take Back Your Boot Time"
slug: how-to-fix-teams-autostart-slowing-laptop
date: 2026-10-11
categories: ["performance"]
tags: ["teams autostart", "microsoft teams", "startup", "boot time", "windows 11"]
description: "Microsoft Teams launching at every boot and dragging your laptop down? Learn how to stop its autostart properly — for work and personal versions."
thumbnail: "/images/thumbs/how-to-fix-teams-autostart-slowing-laptop.webp"
faqs:
  - q: "How do I stop Microsoft Teams from opening on startup?"
    a: "Three places control it: Teams Settings, General, uncheck 'Auto-start Teams'; Task Manager, Startup apps, disable Microsoft Teams; and Settings, Apps, Startup, toggle Teams off. On work laptops, IT policy may re-enable it — check with IT if it keeps coming back. The in-app setting is the most reliable because Teams otherwise re-registers itself."
  - q: "Will disabling Teams autostart affect my meetings and notifications?"
    a: "Only while Teams isn't running — you won't get meeting reminders or chat notifications until you open it. Calendar invites still arrive by email, and browser-based Teams meeting links work without the app. If you live in meetings, consider the delayed-start compromise instead of full disable: fast boot, Teams a few minutes later."
  - q: "Why does Teams slow down my laptop so much at startup?"
    a: "Teams (especially the classic Electron-based client) is heavy: it loads a full browser engine, syncs chats, checks calendar, and preloads meeting features — all during boot's busiest window. The newer Teams 2.0 client is lighter but still significant. Its startup impact rating in Task Manager is consistently among the highest of common apps."
  - q: "What's the difference between Teams personal and work autostart settings?"
    a: "Windows 11 ships with Teams personal (the Chat icon on the taskbar) which has its own autostart in its settings, separate from Teams work/school. You may need to disable both: the Chat flyout's settings for personal, and the Teams work app's Settings, General for work. Task Manager's Startup tab usually lists them as separate entries — disable each one."
---

Microsoft Teams has one of the worst startup-impact ratings of any common app. It's a full collaboration platform — chat sync, calendar, meeting preload — firing up during boot's busiest seconds, and on many laptops it's the difference between a 45-second boot and a three-minute one. The frustration compounds because Teams is stubborn: disable it in one place and it re-enables itself from another.

This guide covers every autostart location for both Teams versions, the delayed-start compromise for meeting-heavy users, and what to do when IT policy fights you.

## Why this happens

- **Heavy client architecture:** Teams loads a full web engine plus sync services — hundreds of MB of RAM and significant CPU at launch.
- **Multiple autostart registrations:** In-app setting, Task Manager startup, Settings startup, and Registry Run keys can each launch it independently.
- **Self-healing behavior:** Teams re-registers its autostart when updated or when the in-app setting is left on.
- **Two Teams versions:** Personal (Chat) and work/school clients each autostart separately — fixing one leaves the other.
- **Boot-time resource contention:** Teams' sync workload collides with Windows, Defender, and OneDrive during the startup storm.
- **Preloaded meeting features:** Camera/mic initialization and meeting preloading add to the startup cost.
- **IT policy enforcement:** Managed devices may have autostart mandated via policy, overriding user settings.
- **Outdated classic client:** The old Electron Teams is dramatically heavier than the new client — still installed on many machines.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure Teams' actual startup impact

Task Manager → Startup apps: check Teams' startup impact rating (likely High). Then reboot and time boot-to-usable with Teams autostarting — that's your "before." Also note in Task Manager → Processes how much CPU/memory Teams consumes in the first 5 minutes. On shared/work laptops, also check whether it's Teams work, Teams personal (Chat), or both — each needs separate treatment. Numbers first: you'll want the before/after comparison to prove the fix worked. General startup tuning lives in the [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/).

1. Task Manager → Startup apps → note Teams' impact rating.
2. Identify: Teams work, Teams personal (Chat), or both.
3. Time boot-to-usable with autostart on ("before").
4. Note Teams' CPU/RAM in the first 5 minutes.

### Fix 2: Disable autostart inside Teams itself

Open Teams → Settings (gear/profile) → General → uncheck "Auto-start Teams." This is the critical one — Teams re-registers itself at update time if this stays on, overriding Task Manager changes. Do it in both clients: Teams work/school app's settings, and the personal Chat flyout's settings (Chat icon → ... → Settings). Verify the checkbox stays off after closing and reopening Teams; if it re-enables itself, an IT policy is overriding you (see Fix 7).

1. Teams app → Settings → General → uncheck "Auto-start Teams."
2. Repeat in Teams personal (taskbar Chat icon → settings).
3. Close/reopen Teams; verify the setting holds.
4. If it re-enables itself → IT policy; see Fix 7.

### Fix 3: Disable it in Task Manager and Settings

Task Manager → Startup apps → right-click Microsoft Teams (each entry) → Disable. Then Settings → Apps → Startup → toggle off Teams entries. Belt and suspenders: the in-app setting stops Teams from re-registering, while these stop the current registrations. Reboot and verify Teams doesn't appear — check both the taskbar and Task Manager → Processes. Time your boot-to-usable again for the "after" number; most people see the single biggest boot improvement of any change from this step.

1. Task Manager → Startup apps → Disable all Teams entries.
2. Settings → Apps → Startup → toggle off Teams entries.
3. Reboot; verify Teams doesn't launch.
4. Time boot-to-usable ("after"); compare.

### Fix 4: Check the Registry Run keys

If Teams still launches: `regedit` → check `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and the machine-wide `HKLM\...\Run` for Teams entries — delete the Teams values (not the keys). Also check Task Scheduler for Teams update/launch tasks that might trigger it. This catches the stragglers that the UI toggles miss, particularly after botched updates left orphaned registrations. Be careful in the registry: delete only the Teams value entries, nothing else.

1. Regedit → HKCU...\Run → delete Teams value entries.
2. Check HKLM...\Run as well (needs admin).
3. Task Scheduler → look for Teams launch tasks; disable.
4. Reboot; verify clean startup.

### Fix 5: Upgrade from classic Teams to the new client

If you're still on the classic (Electron) Teams — recognizable by its purple icon and slowness — switch to the new Teams client: it's roughly twice as fast to launch and uses half the memory. Download it from Microsoft or let the in-app upgrade prompt handle it, then uninstall the classic client to avoid having both. Even if you keep autostart disabled, the new client matters for the times you do launch Teams manually — meetings join faster and the app idles lighter. The [24H2-specific Teams guide](/articles/how-to-fix-teams-autostart-slowing-laptop-in-windows-11-24h2/) covers version quirks.

1. Check which Teams version you're running.
2. Upgrade to the new Teams client.
3. Uninstall the classic client afterward.
4. Re-verify autostart is still disabled in the new client.

### Fix 6: Use delayed start instead of full disable

For meeting-heavy users who need Teams but hate the boot hit: keep autostart disabled everywhere, then create a Task Scheduler task launching Teams 10 minutes after logon (`%LocalAppData%\Microsoft\Teams\Update.exe --processStart Teams.exe` or the new client's path). You get a fast boot and Teams waiting when you need it. Alternatively, pin Teams to the taskbar and launch it with your morning coffee — manual launch after the boot storm is nearly as good. The delayed task is the technician's recommended compromise. Microsoft documents startup management on the [Windows support site](https://support.microsoft.com/en-us/windows).

1. Keep autostart disabled in all locations.
2. Task Scheduler → task launching Teams 10 min after logon.
3. Test: fast boot, Teams appears later automatically.
4. Or simply launch manually once settled — nearly as good.

### Fix 7: Handle IT policy enforcement

On work laptops, Teams autostart may be mandated by IT policy (Intune/SCCM) — your toggles revert within hours. Don't fight policy with hacks; instead: ask IT whether autostart is required or merely default (often it's just default and they'll exempt you), request the new lightweight Teams client if IT still deploys classic, and ask about the web version (teams.microsoft.com) as a lighter alternative for light users. If policy mandates it, the delayed-start task still helps — policy usually requires Teams to run, not to run at second zero.

1. Check if toggles revert within hours (= policy enforcement).
2. Ask IT: required or just default? Request exemption.
3. Request the new Teams client; consider the web version.
4. Use delayed start to at least move it out of the boot storm.

## Closing

Teams autostart is a multi-headed problem — in-app setting, Task Manager, Settings, registry, and two app versions — which is why single-toggle "fixes" seem to fail. Hit every location, verify with a reboot, and measure the before/after: reclaiming minutes every morning is one of the best returns on ten minutes of settings work. And if meetings rule your day, the delayed-start compromise gives you both fast boots and a ready Teams.
