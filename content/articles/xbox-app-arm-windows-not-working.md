---
title: "Xbox App Not Working on Windows ARM? Here's How to Fix It"
slug: xbox-app-arm-windows-not-working
date: 2026-10-23
categories: ["ai-pc"]
tags: ["xbox app", "arm laptop", "game pass", "snapdragon", "windows 11", "troubleshooting"]
description: "Fix the Xbox app not opening, signing in, or installing games on Windows ARM laptops: service repairs, Store resets, Gaming Services fixes, and network tweaks."
thumbnail: "/images/thumbs/xbox-app-arm-windows-not-working.webp"
faqs:
  - q: "Does the Xbox app work on Snapdragon ARM laptops?"
    a: "Yes. The Xbox app ships as a native ARM64 app on Windows 11, and Game Pass works on Copilot+ PCs. When it won't open, sign in, or install games, the cause is usually Gaming Services corruption, a broken Store registration, or sign-in token issues — not the processor."
  - q: "Why does the Xbox app close immediately or show a blank screen?"
    a: "Instant closes and blank screens are typically caused by corrupted Gaming Services, a damaged app package, or stale sign-in credentials. Repairing Gaming Services and resetting the app package resolves most of these without reinstalling Windows."
  - q: "Why can't the Xbox app install games on my ARM laptop?"
    a: "Game installs go through Gaming Services and the Microsoft Store delivery pipeline. If installs stall at 0% or error out, the Gaming Services component is usually broken — reinstalling it via PowerShell is the standard fix."
  - q: "Do I need to reinstall Windows to fix the Xbox app?"
    a: "Almost never. The Xbox app's dependencies (Gaming Services, Store, Xbox identity services) can each be repaired or reinstalled individually. A Windows reinstall is the absolute last resort and rarely necessary."
---

The Xbox app on your Snapdragon laptop won't open, shows a blank green screen, refuses to sign you in, or stalls game downloads at 0% forever. Game Pass is paid for, the laptop is brand new, and the app is the one thing standing between you and your library.

On Windows 11 on ARM the Xbox app is actually native — failures come from its dependency chain: Gaming Services (handles installs), the Microsoft Store plumbing, and the Xbox identity services (sign-in). These pieces break independently, which is why symptoms vary, but the repair order is the same every time.

This guide gives you six fixes in technician order: quick app repair first, then Gaming Services surgery, then sign-in and Store repairs, then network checks, and a full reset only at the end. Test the app after each step.

## Why this happens

- **Gaming Services corruption:** This background component handles all game installs and licensing; when its package breaks, the Xbox app opens but nothing installs or launches.
- **Broken Xbox app package registration:** Windows Store apps depend on a registration entry; a damaged registration makes the tile silently do nothing.
- **Stale Xbox sign-in tokens:** Authentication tokens expire or corrupt, producing endless sign-in loops or "we couldn't sign you in" errors that look like network problems.
- **Microsoft Store cache or component damage:** The Xbox app shares delivery and licensing infrastructure with the Store — a broken Store breaks the Xbox app with it.
- **Outdated app or Gaming Services version:** The Xbox app, Gaming Services, and Windows itself must stay in sync; version skew after a partial update causes mismatched behavior.
- **Network or Teredo/Xbox networking blocks:** Multiplayer and some sign-in flows need Xbox networking (Teredo) and specific ports; strict firewalls or broken Teredo break them.
- **Conflicting overlays or "debloater" tools:** Third-party utilities that strip Windows components often remove Xbox services as "bloat," breaking the app permanently until they're restored.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Repair and reset the Xbox app package

Start with the built-in repair — fast, non-destructive, and it fixes the large category of problems caused by a damaged app package or corrupted local state.

1. Open **Settings > Apps > Installed apps**, find **Xbox**, click the three dots, and choose **Advanced options**.
2. Click **Repair** first and wait for the checkmark — then try launching the app. Repair preserves your sign-in and settings.
3. If repair doesn't help, return to the same page and click **Reset** — this clears local data and you'll need to sign in again, so have your Microsoft account credentials ready.
4. After resetting, launch the Xbox app from the Start menu (not a pinned taskbar shortcut, which can point at the old registration).
5. If the app now opens but games won't install, the app itself is fine and the problem is Gaming Services — continue to Fix 2. Similar layered breakage shows up elsewhere in Windows: [Copilot app notifications going silent](/articles/copilot-app-notifications-silent/) is another case where the app is fine but a background service isn't.

### Fix 2: Reinstall Gaming Services via PowerShell

Gaming Services is behind nearly every "won't install" and "won't launch" complaint. Reinstalling it cleanly is the highest-value repair in this guide.

1. Open **PowerShell as administrator** — this must be elevated, or the removal will fail silently.
2. Run `get-appxpackage Microsoft.GamingServices | remove-appxpackage -allusers` to strip the broken component completely.
3. Restart the laptop — this clears the service registration so the reinstall starts clean.
4. Open the **Microsoft Store**, search for **Gaming Services**, and install it fresh from the Store listing.
5. Launch the Xbox app and attempt a small game install to verify the pipeline works end to end. If your laptop's Wi-Fi has been unreliable during large downloads, rule that out as a separate issue — [Intel BE200 Wi-Fi problems on AI laptops](/articles/intel-be200-wifi-issues-ai-laptop/) covers the network side.

### Fix 3: Fix Xbox sign-in and identity issues

When the app opens but traps you in sign-in loops, the identity stack needs attention — credential and token hygiene, not a reinstall problem.

1. In the Xbox app, click your profile picture and **Sign out**, then close the app completely.
2. Open **Settings > Accounts > Email & accounts** and remove any duplicate or stale Microsoft account entries — duplicates confuse the Xbox identity provider.
3. Open **Credential Manager > Windows Credentials** and delete entries starting with `Xbl|` or `XboxLive` to clear corrupted tokens.
4. Reopen the Xbox app and sign in fresh with the account that owns your Game Pass subscription — double-check you're not signing into a different Microsoft account than the one with the subscription.
5. If sign-in still fails, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for current guidance on account and Store sign-in repairs, since the identity backend changes periodically.

### Fix 4: Repair the Microsoft Store and its cache

The Xbox app leans on Store infrastructure for licensing and delivery. A damaged Store produces Xbox symptoms — even when the Store itself seems fine.

1. Press **Win + R**, type `wsreset.exe`, and press Enter — a blank Store window opens and closes; that's the cache clearing, not an error.
2. Open **Settings > Apps > Installed apps > Microsoft Store > Advanced options** and use **Repair**, then **Reset** if needed.
3. In the Store app, click your profile and check **Downloads and updates** — install every pending update, including Gaming Services and Xbox app updates.
4. Run the Store apps troubleshooter: **Settings > System > Troubleshoot > Other troubleshooters > Windows Store Apps > Run**.
5. Relaunch the Xbox app and test both sign-in and a game install. When background sync services misbehave more broadly, the pattern resembles other service-level issues — for instance, [Copilot's Outlook draft coaching going missing](/articles/copilot-outlook-draft-coaching-missing/) is likewise a service entitlement problem rather than an app bug.

### Fix 5: Check Xbox networking, firewall, and date/time

Multiplayer, cloud gaming, and some sign-in flows need working Xbox networking. Teredo breaks quietly, and a wrong system clock breaks certificate validation — both produce confusing errors.

1. Open the Xbox app, go to **Settings > Network**, and check the NAT type and server connectivity status it reports.
2. If Teredo shows blocked, open an administrator terminal and run `netsh interface teredo set state type=default`, then restart and recheck.
3. In **Windows Security > Firewall**, confirm the Xbox app and Gaming Services are allowed — third-party firewalls should have explicit allow rules for both.
4. Verify **Settings > Time & language > Date & time** has **Set time automatically** on — a clock skewed by even a few minutes breaks Xbox Live certificate checks.
5. Test with a wired connection or a different network if possible; some public and corporate networks block the ports Xbox Live needs regardless of your laptop's configuration.

### Fix 6: Full reset of the Xbox gaming stack

When individual repairs failed, reset the whole stack at once: app, Gaming Services, and identity state. Still far short of reinstalling Windows, and it catches multi-component breakage piecemeal repairs miss.

1. Uninstall the **Xbox app**, **Xbox Game Bar**, and **Xbox Identity Provider** from **Settings > Apps** (keep Game Bar if you use it — reinstall it after).
2. Remove Gaming Services with the PowerShell command from Fix 2, then restart.
3. Reinstall in order from the Microsoft Store: **Gaming Services** first, then the **Xbox app**, then sign in fresh.
4. Undo any "debloater" or optimizer tool changes — if you ever ran a script that removed Xbox components as bloat, its undo/restore function is mandatory here, because those tools delete packages the Store can't always restore.
5. Launch the app, sign in, and install a small game as the final verification. If even the full-stack reset fails identically, broaden the diagnosis before blaming Windows: on Snapdragon machines, check whether other Qualcomm-dependent components are healthy — [Qualcomm AI Hub models failing to run](/articles/qualcomm-ai-hub-models-not-running/) would point to a deeper platform or driver issue rather than anything Xbox-specific. If the platform is otherwise healthy, an in-place upgrade via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) (keeping files and apps) is the last step before considering a reset.

## Closing

Xbox app failures on ARM laptops are dependency failures, not ARM failures — the app is native, but Gaming Services, Store plumbing, and sign-in tokens each break in their own way. Repair the app package, reinstall Gaming Services via PowerShell, clear stale tokens, and fix the Store cache before contemplating a Windows reinstall. That order resolves the overwhelming majority of cases.
