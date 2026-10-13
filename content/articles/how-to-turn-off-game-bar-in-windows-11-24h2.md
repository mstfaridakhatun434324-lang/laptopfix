---
title: "How to Turn Off Game Bar in Windows 11 24H2"
slug: how-to-turn-off-game-bar-in-windows-11-24h2
date: 2026-09-05
categories: ["performance"]
tags: ["game bar", "xbox game bar", "disable game bar", "windows 11 24h2", "gaming"]
description: "Turn off Xbox Game Bar in Windows 11 24H2 completely: Settings toggles, background processes, and registry removal for a cleaner, faster system."
thumbnail: "/images/thumbs/how-to-turn-off-game-bar-in-windows-11-24h2.webp"
faqs:
  - q: "What is Xbox Game Bar and do I need it?"
    a: "Xbox Game Bar is Microsoft's gaming overlay — press Win+G for screen recording, performance widgets, and social features. If you never record gameplay or use its widgets, you do not need it: its background processes consume CPU, RAM, and GPU resources constantly, and disabling it is safe and reversible."
  - q: "Will disabling Game Bar improve gaming performance?"
    a: "Modestly, in most cases. The bigger win is eliminating its background recording and overlay hooks, which are known stutter sources in some games. The FPS gain itself is usually small (1 to 3 percent), but the reduction in random hitches and input latency is the real benefit."
  - q: "Does turning off Game Bar break anything else?"
    a: "Only Game Bar itself and its widgets stop working — Win+G does nothing, and background game recording stops. Game Mode, the Xbox app, Game Pass, and your games all continue working normally. Screen recording alternatives like OBS or your GPU vendor's software are unaffected."
  - q: "Why does Game Bar keep coming back after updates?"
    a: "Feature updates can re-enable Game Bar and reinstall its components as part of refreshing system apps. After each major Windows update, revisit the Settings toggles to confirm they are still off. The registry and policy methods are more persistent but can also be reset by updates."
---

Xbox Game Bar — the `Win+G` overlay — runs background processes on every Windows 11 PC whether you game or not. Its recording hooks, widget services, and overlay infrastructure cost CPU cycles, memory, and in some games, cause stuttering. If you've never pressed `Win+G` on purpose, it's pure overhead.

Windows 11 24H2 changed some of the toggles' locations, so older guides point at menus that moved. This guide covers the current 24H2 paths: the Settings switches, the background-process cleanup, and the thorough removal methods for people who want it gone completely. All reversible, all safe.

## Why this happens

- **Background recording hooks**: Game Bar's capture infrastructure hooks into games even when you're not recording.
- **Always-on widget processes**: GameBar widgets run as background tasks consuming RAM persistently.
- **Overlay conflicts**: The overlay layer fights with Discord, Steam, and GPU overlays, occasionally causing stutter or crashes.
- **Re-enabled by updates**: Feature updates restore Game Bar components and reset toggles.
- **Tied to Gaming Services**: The broader Xbox service stack keeps Game Bar-adjacent processes alive.
- **Capture service overhead**: The GameDVR capture service monitors for recording hotkeys continuously.
- **Widget board integration**: Windows 11's widget infrastructure shares components with Game Bar.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off Game Bar in Settings (24H2 path)

The official toggles — start here.

1. Go to **Settings** > **Gaming** > **Xbox Game Bar** and turn it **Off** — this disables the `Win+G` overlay.
2. Go to **Settings** > **Gaming** > **Captures** and turn off **Record in the background while I'm playing a game** — this is the biggest performance win, killing background DVR.
3. Also disable **Record audio when I record a game** and any capture quality settings if you never record.
4. **Settings** > **Gaming** > **Game Mode**: leave this **On** — Game Mode is separate from Game Bar and genuinely helps; don't disable it by accident.
5. Test `Win+G` — nothing should happen now. Check Task Manager after a reboot for lingering GameBar processes.

### Fix 2: Stop Game Bar's background processes

Toggles don't always kill the background workers.

1. Open **Task Manager** > **Processes** and look for **Xbox Game Bar**, **GameBar**, or **Broadcast DVR server** entries.
2. Go to **Settings** > **Apps** > **Installed apps**, search **Xbox Game Bar**, click ⋯ > **Advanced options**.
3. Under **Background apps permissions**, set to **Never**.
4. Under **Terminate**, click **Terminate** to kill any running instance immediately.
5. Check **Task Scheduler** > **Microsoft** > **Windows** > **GameDVR** (or **BroadcastDVR**) — disable tasks related to background recording.

### Fix 3: Disable via Group Policy (Pro/Enterprise)

The administrative lockdown method.

1. Press `Win + R`, type `gpedit.msc`, and navigate to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Windows Game Recording and Broadcasting**.
2. Enable **Enables or disables Windows Game Recording and Broadcasting** and set it to **Disabled**.
3. This policy disables the recording and broadcasting infrastructure that Game Bar depends on.
4. Run `gpupdate /force` in a terminal, then reboot.
5. Verify: `Win+G` should do nothing, and GameDVR services should be absent from Task Manager. Microsoft documents gaming features at their [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 4: Disable via Registry (Home edition)

The same lockdown without gpedit.

1. Press `Win + R`, type `regedit`, and navigate to `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR`.
2. Set **AppCaptureEnabled** to **0** (DWORD) — disables background game capture.
3. Navigate to `HKEY_CURRENT_USER\System\GameConfigStore` and set **GameDVR_Enabled** to **0**.
4. For system-wide: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR` > create DWORD **AllowGameDVR** = **0** (create the GameDVR key if missing).
5. Reboot and verify — these registry values survive most updates better than Settings toggles.

### Fix 5: Remove the Game Bar AppX package

For those who want it fully gone.

1. Open **PowerShell as administrator**.
2. Run: `Get-AppxPackage Microsoft.XboxGamingOverlay -AllUsers | Remove-AppxPackage -AllUsers`
3. This removes the overlay package entirely — `Win+G` becomes completely inert.
4. To reinstall later (if you change your mind): open the **Microsoft Store**, search **Xbox Game Bar**, and install it fresh.
5. Note: major feature updates may reinstall it — check after each 24H2-era feature update and re-remove if desired.

### Fix 6: Quiet the surrounding Xbox service stack

Game Bar has friends that also cost resources.

1. If you don't use Game Pass or Store games, consider disabling the Xbox services: `services.msc` > **Xbox Live Auth Manager**, **Xbox Live Game Save**, **Xbox Live Networking Service** > **Disabled**.
2. See our [GamingServices guide](/articles/what-to-do-if-gamingservices-high-cpu-usage/) before touching **Gaming Services** itself — it has its own considerations.
3. **Settings** > **Gaming**: turn off anything else you don't use — some 24H2 builds add new gaming-adjacent toggles.
4. Remove the **Xbox app** itself if unused (**Settings** > **Apps** > **Installed apps** > Xbox > Uninstall) — it pulls the service stack with it.
5. After cleanup, check Task Manager's **Startup** tab for any remaining Xbox entries and disable them.

### Fix 7: Verify the performance gain and handle stutter

Confirm the removal actually helped.

1. Reboot, then check Task Manager: no GameBar, BroadcastDVR, or Xbox overlay processes should be running.
2. Test your most stutter-prone game for 15 minutes — compare against your memory of before (or better, previous 1% low measurements).
3. If stuttering persists, Game Bar wasn't your cause — work through our [game stuttering walkthrough](/articles/how-do-i-fix-windows-11-stuttering-in-games/) for the remaining suspects.
4. Keep your GPU driver updated regardless — overlay removal helps, but driver bugs cause most game stutter.
5. Document what you disabled (a quick note in a text file) so future-you can re-enable recording if you ever want to capture gameplay.

## Closing

Turning off Game Bar in Windows 11 24H2 is a small cleanup with real benefits: the Settings toggles stop the overlay and background recording, the policy/registry methods lock it down, and AppX removal takes it fully off the system. You'll reclaim a little CPU, a little RAM, and — more importantly — remove a known source of in-game stutter. If you ever take up game recording, OBS or your GPU's software does the job better anyway.
