---
title: "GamingServices High CPU After a Windows 11 Update? Here's the Fix"
slug: how-to-fix-gamingservices-high-cpu-usage-after-windows-11-update
date: 2026-09-11
categories: ["performance"]
tags: ["gamingservices", "high cpu", "xbox", "windows update", "gaming"]
description: "GamingServices.exe eating CPU after a Windows 11 update? Why Xbox gaming services spike and how to repair or reset them."
thumbnail: "/images/thumbs/how-to-fix-gamingservices-high-cpu-usage-after-windows-11-update.webp"
faqs:
  - q: "What is GamingServices.exe?"
    a: "GamingServices.exe is the background service behind the Xbox app and PC Game Pass on Windows. It handles game installation, updates, licensing verification, and cloud sync for Xbox-platform games. It is supposed to be mostly idle, waking for game-related tasks. Sustained high CPU from it after a Windows update usually means it is stuck processing a corrupted game install, a broken update state, or a damaged services installation that keeps retrying failed work."
  - q: "Can I uninstall Gaming Services if I don't game?"
    a: "Yes, if you never use the Xbox app or PC Game Pass, removing Gaming Services is safe and eliminates the CPU usage entirely. Uninstall the Xbox app and Gaming Services through Settings or PowerShell, and nothing else in Windows depends on them. If you might game later, reinstalling takes a minute from the Microsoft Store. There is no reason to keep game infrastructure running on a machine that never plays games."
  - q: "Why did a Windows update break Gaming Services?"
    a: "Windows updates touch the app platform Gaming Services depends on: the Microsoft Store infrastructure, app identity services, and gaming-related system components. If the update interrupted a game download or left the Store cache inconsistent, Gaming Services can get stuck in a retry loop afterward. Updates also reset app permissions and re-register system components, any of which can leave Gaming Services in a confused half-migrated state."
  - q: "Will resetting Gaming Services delete my games?"
    a: "Repairing or resetting the Gaming Services app package does not delete your installed games — it resets the service's own configuration and cache. Your game files stay on disk, though you may need to re-verify or re-sign-in afterward. As a precaution, note which games are installed before resetting. In the worst case, the Xbox app can re-detect existing installations rather than redownloading hundreds of gigabytes."
---

`GamingServices.exe` (and its sibling `GamingServicesNet.exe`) chewing through CPU after a Windows 11 update is a special kind of annoying — you're not even gaming, yet Xbox's background plumbing is working overtime. This service exists to support the Xbox app and PC Game Pass: installing games, checking licenses, syncing saves. At rest it should be nearly invisible. When it isn't, it's almost always stuck: retrying a corrupted game operation, choking on a broken Store cache the update left behind, or running a damaged services installation in a loop.

The fix path is refreshingly concrete compared to vaguer CPU issues: repair the Store cache, reset the Gaming Services package, check for stuck game operations, and — if you don't game at all — remove the whole thing. Open **Task Manager** > **Processes**, sort by CPU, and confirm GamingServices.exe is the consumer (not the game itself). For general gaming performance, see [game stuttering after a Windows update](/articles/how-to-fix-game-stuttering-after-windows-update-in-windows-11-24h2/); for another update-triggered CPU hog, see [Windows Modules Installer high CPU](/articles/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update/).

## Why this happens

- **Corrupted Microsoft Store cache**: The update left the Store cache inconsistent; Gaming Services retries failed operations.
- **Stuck game install/update**: An interrupted game download keeps the service retrying forever.
- **Damaged Gaming Services package**: The update half-migrated the services installation.
- **License verification loops**: Broken app identity after the update causes repeated license checks.
- **Xbox app background activity**: The app itself doing post-update maintenance.
- **Corrupted game files**: A damaged installed game triggering repeated verification.
- **Permission/registry corruption**: Update-changed permissions breaking the service's normal operation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Gaming Services is the problem

Make sure of the target.

1. In **Task Manager** > **Processes** sorted by CPU, verify **Gaming Services** (GamingServices.exe) is the sustained consumer — not a game, not the Xbox app UI.
2. Check the **Details** tab for **GamingServicesNet.exe** too — the pair work together; both being hot confirms the services layer, not a single game.
3. Open the **Xbox app** and check for stuck downloads, failed installs, or games showing "installing" forever — a stuck operation is the most common trigger.
4. Note whether CPU is constant or spikes periodically — constant suggests a stuck loop; periodic suggests scheduled retry attempts.
5. If you don't recognize the Xbox app and never installed it, it likely arrived via update — removal (Fix 7) may be your whole answer.

### Fix 2: Reset the Microsoft Store cache

Clear the foundation Gaming Services stands on.

1. Press **Win + R**, type `wsreset.exe`, and press Enter — a blank Command Prompt window appears, the Store opens when the reset completes. Don't close it early.
2. After the reset, open the **Microsoft Store** > **Library** and install any pending Store app updates — Gaming Services depends on current Store infrastructure.
3. Reboot, then check Task Manager — a corrupted cache was the cause if GamingServices.exe settles within 15 minutes.
4. If the Store itself misbehaves (won't open, errors), repair it: **Settings** > **Apps** > **Installed apps** > **Microsoft Store** > **Advanced options** > **Repair**, then **Reset** if repair doesn't help.
5. Microsoft's [Store troubleshooting guidance](https://support.microsoft.com/en-us/windows) covers deeper Store repair if wsreset isn't enough.

### Fix 3: Repair and reset the Gaming Services package

Fix the service installation itself.

1. Open **Settings** > **Apps** > **Installed apps**, search for **Gaming Services**.
2. Click **...** > **Advanced options** > **Repair** — wait for it to complete, then check Task Manager.
3. If repair doesn't help, use **Reset** in the same panel — this reinstalls the service package cleanly without touching your game files.
4. Also repair the **Xbox app** the same way (Repair, then Reset if needed) — the app and services are tightly coupled.
5. Reboot after resetting and observe for 30 minutes — a damaged package was the cause if CPU normalizes.

### Fix 4: Clear stuck game operations

Remove the job it's choking on.

1. Open the **Xbox app** > check every game's status — cancel or pause any stuck, failed, or endlessly "installing" items.
2. For a corrupted installed game: Xbox app > game > **...** > **Manage** > **Files** > **Verify and repair** — let it complete.
3. Check **Settings** > **Apps** > **Installed apps** for partially-installed games (often showing odd sizes) and uninstall the broken ones cleanly, then reinstall if wanted.
4. Clear the Xbox app's local cache: the app's **Advanced options** > **Reset** also clears its download state.
5. After clearing stuck operations, GamingServices.exe should stand down — it was the retry loop, not the service itself.

### Fix 5: Reinstall Gaming Services via PowerShell

The clean-slate reinstall.

1. Open **PowerShell as administrator**.
2. Remove the package: `Get-AppxPackage *gamingservices* -AllUsers | Remove-AppxPackage -AllUsers`
3. Also remove the Xbox app if it's misbehaving: `Get-AppxPackage *xboxapp* -AllUsers | Remove-AppxPackage -AllUsers`
4. Reboot, then reinstall from the **Microsoft Store**: search **Xbox** app and install it — Gaming Services comes along as its dependency.
5. Sign back into the Xbox app, let it detect your existing game installs (it usually finds them without redownloading), and verify CPU is calm.

### Fix 6: Check for deeper system corruption

When the services layer keeps breaking.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an elevated terminal — app-platform corruption causes recurring Gaming Services failures.
2. Install all pending **Windows Update** items — follow-up patches fix update-introduced app platform bugs.
3. Create a new local user account and test Gaming Services there — a calm service on the new account means your profile's app data is corrupted (migrate or reset the app data).
4. Check **Event Viewer** > **Windows Logs** > **Application** for GamingServices errors — specific error codes point to the failing component.
5. If corruption recurs after every update, consider the broader Windows repair path — chronic app-platform breakage suggests servicing issues.

### Fix 7: Remove it entirely (for non-gamers)

The definitive fix if you never game.

1. Uninstall the **Xbox app**: **Settings** > **Apps** > **Installed apps** > **Xbox** > **Uninstall**.
2. Remove Gaming Services via PowerShell (admin): `Get-AppxPackage *gamingservices* -AllUsers | Remove-AppxPackage -AllUsers`
3. Also remove **Xbox Game Bar** if unused: **Settings** > **Gaming** > **Xbox Game Bar** > off, plus uninstall the Game Bar app.
4. Verify in Task Manager that GamingServices.exe is gone entirely — no process, no CPU, problem eliminated at the root.
5. If you game later, reinstalling the Xbox app from the Store restores everything in minutes — this decision is fully reversible.

## Closing

GamingServices high CPU after a Windows 11 update is a stuck-service problem, not a hardware problem: corrupted Store cache, a wedged game operation, or a half-migrated services package looping its retries. Reset the cache, repair the package, clear the stuck jobs — or remove the whole Xbox stack if you never game. Either way, background gaming plumbing has no business burning your CPU while you work.
