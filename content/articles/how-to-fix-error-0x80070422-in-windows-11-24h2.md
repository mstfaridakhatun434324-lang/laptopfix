---
title: "How to Fix Windows 11 Update Error 0x80070422 (24H2)"
slug: how-to-fix-error-0x80070422-in-windows-11-24h2
date: 2026-09-28
categories: ["windows-errors"]
tags: ["update error", "0x80070422", "Windows 11 24H2"]
description: "Error 0x80070422 stopping Windows 11 24H2 updates? Re-enable the disabled services behind it with this guide."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070422-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80070422 mean?"
    a: "It means 'the service cannot be started' — Windows Update tried to use a required background service (usually the Windows Update service itself or BITS) and found it disabled. The update can't proceed without its own engine running."
  - q: "Why would the Windows Update service be disabled?"
    a: "Common reasons: third-party 'privacy' or 'debloating' tools that disable it deliberately, a previous troubleshooting session that stopped it and never restarted it, group policies on work laptops, or malware trying to prevent security updates from installing."
  - q: "Is it safe to re-enable the Windows Update service?"
    a: "Yes — it's a core Windows component meant to run. Re-enabling it restores normal update function and doesn't change anything else. The only exception is a work laptop managed by IT, where you should check with your administrator before changing service settings."
  - q: "What if the service won't stay enabled?"
    a: "Something is actively disabling it — usually a third-party utility running at startup, a scheduled task, or group policy. Check Task Scheduler and your installed 'optimizer' tools, and scan for malware, since blocking updates is classic malware behavior."
---
Error 0x80070422 is refreshingly honest as Windows errors go: it means a service Windows Update needs is disabled and can't start. No cryptic corruption, no missing files — just an engine that someone (or something) switched off. The fix is correspondingly direct: find the disabled service, switch it back on, and updates flow again.

This error also shows up in the Microsoft Store and a few other places, but the Windows Update context is by far the most common on 24H2. The steps below cover the services, the registry keys that control them, and the tools that keep turning them off — because the real fix isn't just enabling the service once, it's stopping whatever disabled it.

## Why this happens

- **A "debloating" or "privacy" tool disabled it.** Third-party utilities that promise to stop Windows "spying" routinely disable the Windows Update service as part of their script. This is the number-one cause I see.
- **A previous troubleshooting session left it off.** The standard advice for stuck updates includes stopping the update services — and plenty of people (and scripts) stop them without restarting them.
- **Group Policy on managed machines.** Work or school laptops may have update services controlled by IT policy. The service shows as disabled and your changes get reverted.
- **Malware blocking updates.** Preventing security updates is standard malware tradecraft. If the service keeps disabling itself and you didn't install any tweaking tools, suspect infection.
- **Corrupted service configuration.** Rare, but the service's registry configuration can be damaged such that it can't start even when set to Automatic — usually after a bad update or disk corruption.
- **Dependency services disabled.** Windows Update depends on other services (BITS, RPC). If a dependency is disabled, the update service fails to start and you get the same error code.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Enable the Windows Update service

The direct fix — check the service and set it correctly.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Update** in the list and double-click it.
3. Set **Startup type** to **Automatic**. If **Service status** shows Stopped, click **Start**.
4. Click **OK**, then go to **Settings > Windows Update > Check for updates**. If updates now work, you're done — but read Fix 5 to stop it happening again.

### Fix 2: Enable the dependency services

Windows Update doesn't work alone — check its supporting cast.

1. In **services.msc**, find each of these and set **Startup type** to **Automatic** (or **Manual** where noted), starting any that are stopped:
   - **Background Intelligent Transfer Service** → Automatic
   - **Cryptographic Services** → Automatic
   - **DCOM Server Process Launcher** → Automatic
   - **RPC Endpoint Mapper** → Automatic
   - **Windows Installer** → Manual
2. Restart the laptop after changing several services — some only pick up the new configuration on boot.
3. Retry Windows Update. A single disabled dependency produces the identical 0x80070422, so don't skip this check. Dependency issues also lurk behind sibling errors like [0x80240034](/articles/how-to-fix-error-0x80240034-in-windows-11-24h2/), where BITS misbehavior breaks downloads.

### Fix 3: Fix it via the registry

If the Services console won't let you change the startup type (greyed out), the registry is the back door.

1. Press **Win + R**, type `regedit`, and press Enter. Approve the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv`.
3. Double-click the **Start** value and set it to `2` (Automatic). The values mean: 2 = Automatic, 3 = Manual, 4 = Disabled.
4. Do the same for the `BITS` key (Background Intelligent Transfer Service) — set its **Start** to `2` or `3`.
5. Close the editor and restart. Verify in **services.msc** that the services now show the correct startup types.

### Fix 4: Run the Windows Update troubleshooter

Let Microsoft's automated tool verify the service configuration.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. The troubleshooter checks service states among other things and will restart misconfigured services itself.
4. Restart the laptop and retry the update. This is a good sanity check even after manual fixes — it catches anything you missed.

### Fix 5: Find and remove whatever keeps disabling it

Enabling the service once is pointless if something switches it off again tonight.

1. Think about what you've installed: "privacy tools," "Windows debloaters," "update blockers," "game optimizers" — uninstall anything in this family via **Settings > Apps > Installed apps**.
2. Check **Task Scheduler** (**Win + R**, `taskschd.msc`) for tasks that stop or disable update services — look under **Task Scheduler Library** for unfamiliar entries and disable the suspicious ones.
3. Check **Startup apps** in Task Manager for tweaking utilities that reapply their "optimizations" on every boot.
4. If you're on a work or school laptop and the service reverts after every change, stop fighting it and talk to your IT department — Group Policy will override local changes every time, and that's by design.

### Fix 6: Scan for malware

A service that disables itself repeatedly is a red flag.

1. Open **Windows Security** from the Start menu, go to **Virus & threat protection > Scan options**, and run a **Full scan**.
2. For a second opinion, run the **Microsoft Safety Scanner** (free download from [Microsoft support](https://support.microsoft.com/en-us/windows)) — it's a standalone on-demand scanner that doesn't conflict with anything.
3. If malware is found and removed, re-enable the services (Fix 1) and run Windows Update immediately to catch up on the security patches the malware was blocking.
4. After cleanup, change important passwords from a clean device — malware that blocks updates often does worse things too.

### Fix 7: Repair the service registration

When the service configuration itself is corrupted and won't start even when enabled.

1. In **Terminal (Admin)** (**Win + X**), re-register the update engine components:
   `regsvr32 /s wuapi.dll`
   `regsvr32 /s wuaueng.dll`
   `regsvr32 /s wups.dll`
2. Then reset the service configuration to defaults:
   `sc config wuauserv start= auto`
   `sc config bits start= auto`
   `net start wuauserv`
   `net start bits`
   (Note the space after `start=` — it's required.)
3. Restart and test. If the services now start and stay running, the corruption is resolved.
4. As a final fallback, an in-place upgrade with the 24H2 ISO (from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping files and apps) rebuilds all service registrations cleanly.

## Closing

Error 0x80070422 is one of the most satisfying errors to fix because the cause-and-effect is so clean: service off, updates fail; service on, updates work. Once updates flow again, if a *different* update error appears — the download-failure [0x800f0922](/articles/how-to-fix-error-0x800f0922-in-windows-11-24h2/) is the next most common — that guide picks up where this one leaves off. The only trap is stopping at Fix 1 without doing Fix 5 — if a debloating tool or scheduled task keeps killing the service, you'll be back here next month wondering why updates broke "again." Find the thing that turned it off, remove it, and this error becomes a one-time story.
