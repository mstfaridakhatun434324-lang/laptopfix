---
title: "How to Stop Microsoft Teams From Slowing Down Your Laptop at Startup"
slug: how-do-i-fix-teams-autostart-slowing-laptop
date: 2026-09-23
categories: ["performance"]
tags: ["teams autostart", "microsoft teams", "slow startup", "boot slow", "windows 11"]
description: "Microsoft Teams auto-starting and slowing your laptop? Stop Teams from launching at boot and reclaim your startup speed."
thumbnail: "/images/thumbs/how-do-i-fix-teams-autostart-slowing-laptop.webp"
faqs:
  - q: "Why does Microsoft Teams slow down my laptop at startup?"
    a: "Teams is built on Electron (essentially a full Chromium browser per app), so launching it at login consumes hundreds of megabytes of RAM and significant CPU while it signs in, syncs chats, and loads. On laptops with 8GB RAM or spinning-era storage habits, this contends directly with everything else starting up — antivirus, cloud sync, browser restore — stretching boot-to-usable time by a minute or more."
  - q: "How do I stop Teams from opening on startup in Windows 11?"
    a: "The reliable method: open Teams, click the three dots or your profile picture > Settings > General, and uncheck 'Auto-start Teams'. Then verify in Windows Settings > Apps > Startup (toggle Teams off) and Task Manager > Startup apps (disable it there too). Teams has a habit of re-enabling itself after updates, so check all three locations — the in-app setting alone sometimes isn't enough."
  - q: "Is it better to use Teams in the browser instead of the app?"
    a: "For occasional use, yes. The web version at teams.microsoft.com provides most functionality without any startup impact, background processes, or update churn — you just close the tab when done. The desktop app is better for heavy daily users who need notifications, calling reliability, and offline access. Match the tool to your usage: daily driver gets the app, occasional meetings get the browser."
  - q: "Why does Teams keep re-enabling auto-start after updates?"
    a: "Teams updates frequently reinstall or reset its startup registration — the installer writes the auto-start entry as part of its setup routine regardless of your previous choice. The new Teams client is better behaved than the classic one, but it can still happen. After each Teams update, glance at Settings > Apps > Startup to confirm it stayed off. Some IT-managed installs enforce auto-start via policy, which you can't override locally."
---

You press the power button, log in, and then... wait. And wait. The desktop appears but nothing responds, the fan spins up, and eventually Microsoft Teams pops open — an app you didn't ask to launch, consuming resources you need for actual work. Teams auto-start is one of the most common startup slowdowns on Windows 11 laptops, especially work machines where it was preinstalled.

Teams is heavy: the desktop client bundles an entire browser engine, syncs conversations, checks calendar, and preloads calling infrastructure. Having it fight for CPU and RAM during the critical first minutes after login is a recipe for a sluggish morning. Here's how to stop it properly — in all the places it hides — and what to do if it keeps coming back.

## Why this happens

- **Teams registered as a startup app**: The installer adds itself to Windows startup, launching at every login.
- **Heavy Electron-based client**: Teams loads a full Chromium runtime, using hundreds of MB RAM before you even use it.
- **Sign-in and sync storm**: At launch it authenticates, syncs chats/files, and checks for updates simultaneously.
- **Startup contention**: Teams competes with antivirus, OneDrive, and other startup apps for disk and CPU.
- **Re-enables after updates**: Teams installers routinely re-add the startup entry during updates.
- **Preinstalled by IT policy**: Work laptops may have Teams forced on via group policy or provisioning.
- **Background processes linger**: Even closed, Teams leaves update and notification helpers running.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable auto-start inside Teams

Start with the app's own setting — it's the most direct.

1. Open **Microsoft Teams** and sign in if needed.
2. Click the **three dots (...)** next to your profile picture (top-right) > **Settings** > **General**.
3. Uncheck **Auto-start Teams**. In the new Teams client, this is under **Settings** > **General** > **Application** > **Auto-start Teams**.
4. Also uncheck **On close, keep the application running** if you want Teams to fully exit when you close its window rather than lingering in the tray.
5. Close Teams completely (right-click its tray icon > **Quit**) and reboot to verify it doesn't launch. If it still appears, continue — Teams has more than one startup hook.

### Fix 2: Remove it from Windows startup locations

Teams registers in multiple places — clear them all.

1. Open **Settings** > **Apps** > **Startup** and toggle **Microsoft Teams** to **Off**.
2. Open **Task Manager** (Ctrl + Shift + Esc) > **Startup apps** tab, find **Microsoft Teams**, right-click > **Disable**. Check the **Startup impact** column — Teams is often rated High.
3. Press **Win + R**, type `shell:startup`, and press Enter — if a Teams shortcut sits in your personal Startup folder, delete it.
4. Also check `shell:common startup` (the all-users Startup folder) for a Teams entry, though this needs admin rights to modify.
5. Reboot and confirm: no Teams window, no Teams tray icon, and Task Manager's Startup tab still shows it Disabled. Our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) covers hunting stubborn entries.

### Fix 3: Stop the re-enable cycle after updates

Teams updates are notorious for resurrecting auto-start — break the cycle.

1. After every Teams update, re-check **Settings** > **Apps** > **Startup** — make verifying this part of your routine for a few update cycles until you're confident it sticks.
2. In the new Teams client, ensure you're signed into the **work/school account** properly — sign-in state confusion sometimes triggers the app to "repair" its startup registration.
3. If your laptop is IT-managed, check with your administrator: group policies like "prevent Teams autostart" exist, but so do policies that *enforce* it. You can't win a fight against enforced policy locally.
4. Consider switching to the **new Teams client** if you're still on classic — the new client is lighter, starts faster, and respects the auto-start toggle more reliably.
5. As a last resort for personal machines, uninstall Teams entirely if you only join occasional meetings — the web app at teams.microsoft.com in Edge or Chrome covers meetings with zero startup footprint.

### Fix 4: Reduce Teams' resource footprint (if you keep it)

If you need Teams daily, make it lighter rather than banishing it.

1. In Teams **Settings** > **General**, enable **Enable GPU hardware acceleration** only if your GPU handles it well — on weak integrated graphics, disabling it can actually reduce stutter.
2. Turn off **Register Teams as the chat app for Office** if you don't use Office integration — it adds background hooks.
3. In **Settings** > **Notifications**, disable notifications for channels and teams you don't actively follow — each notification wakes the app.
4. Close Teams fully (tray icon > Quit) when you're done for the day instead of leaving it running overnight — it accumulates memory over long sessions.
5. Keep Teams updated: **...** > **Check for updates**. Performance fixes ship regularly, and an outdated client is often heavier than the current one.

### Fix 5: Speed up overall startup so Teams matters less

Even with Teams tamed, a lean startup helps everything.

1. Audit **all** startup apps in Task Manager > Startup apps — disable updaters, game launchers, chat apps, and utilities you don't need instantly at login.
2. Open **Settings** > **Apps** > **Startup** and be aggressive: if you can launch it manually in 5 seconds when needed, it doesn't need to auto-start.
3. Check for **OneDrive** and other sync clients starting at boot — stagger heavyweights so they don't all hammer the disk simultaneously.
4. Run **Task Manager** > **Performance** during boot (open it quickly after login) to see whether CPU, disk, or memory is the bottleneck — disk at 100% points to too many simultaneous starters.
5. For the full startup-optimization walkthrough, see [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) and [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

### Fix 6: Handle IT-managed and preinstalled Teams

Work laptops play by different rules — know your options.

1. Check whether Teams was installed per-user or machine-wide: **Settings** > **Apps** > **Installed apps** — machine-wide installs (in Program Files) are typically IT-managed.
2. Look for a company portal or software center app — IT often provides an approved removal or configuration path there.
3. If policy enforces auto-start, the pragmatic compromise: let it start, but delay its impact by setting Teams to start **minimized** and disabling its most expensive features (video previews, GIF autoplay in Settings > Appearance).
4. Ask IT about the **Teams autostart policy** — many admins will exempt users who request it, since forced autostart generates helpdesk complaints.
5. Document the business case if needed: measure your boot-to-usable time with and without Teams autostart (use Task Manager's **Last BIOS time** plus a stopwatch) — numbers persuade IT faster than complaints. Microsoft documents Teams deployment options at [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

Teams autostart is a solvable annoyance: disable it in the app, in Windows startup, and in the Startup folder, then guard against update resurrection. Your laptop boots to a usable desktop in seconds instead of minutes — and Teams is there when *you* choose to open it, not when it chooses to open itself.
