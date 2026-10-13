---
title: "How to Fix Windows Update Error 0x80070422 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80070422-in-windows-11-24h2
date: 2026-09-30
categories: ["windows-update"]
tags: ["windows update", "0x80070422", "error code", "windows 11", "services"]
description: "Error 0x80070422 means the Windows Update service is disabled and cannot start. Re-enable wuauserv and its dependencies with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070422-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80070422 mean?"
    a: "In technical terms, a service Windows Update depends on — usually wuauserv itself — is disabled or prevented from launching, so every update attempt dies before it begins. It appears the instant you press Check for updates: Windows reaches for its own update service, finds it switched off, and gives up."
  - q: "How did the service get disabled without my knowledge?"
    a: "The most common trigger is a debloat script, third-party optimizer, or tweak utility that turned background services off — frequently right after a fresh install. Leftover group policies on ex-corporate laptops and some malware infections also disable wuauserv deliberately."
  - q: "The service keeps flipping back to Disabled. Why?"
    a: "If the service reverts to Disabled after a restart, or services.msc refuses the change, a registry value or group policy is enforcing it. Check the Start DWORD under the wuauserv registry key — a value of 4 means Disabled — and inspect group policy for update-related settings that re-apply the change."
  - q: "Which other services does Windows Update need?"
    a: "Background Intelligent Transfer Service, Cryptographic Services, DCOM Server Process Launcher, and RPC Endpoint Mapper all support the update pipeline. Windows Update cannot start if BITS or Cryptographic Services is disabled, even when wuauserv itself looks fine — so verify the dependencies too."
---

It is the simplest error on this list to understand, and one of the most annoying to meet. You press Check for updates, and Windows immediately surrenders: the service it needs to perform the check has been switched off. Not broken, not corrupted — just disabled, like a lamp unplugged from the wall.

With Windows 11 24H2, it often turns up right after a "debloat" script runs, a third-party optimizer does its thing, or a fresh install where a tweak utility silenced background services. Ex-corporate laptops carry another classic cause: a leftover policy that keeps forcing the service off on what is now a personal machine.

The fix is correspondingly direct: switch the service back on, make sure it stays on, and confirm its supporting services are alive. The steps below walk that path in order — most readers are done by Fix 2, with the later steps reserved for services that refuse to stay enabled.

## Why this happens

- **Someone set the service to Disabled.** Usually wuauserv's startup type was flipped to Disabled inside services.msc or by a script.
- **A registry tweak altered the startup value.** Debloat and privacy scripts often write 4 (Disabled) into the Start DWORD under the wuauserv key.
- **An optimizer took over service management.** Tools that promise a faster Windows occasionally disable wuauserv within an aggressive preset.
- **Group Policy holds the service down.** On ex-corporate or school machines, a residual policy may keep forcing the service off.
- **Malware silenced updates for self-preservation.** Certain infections deliberately halt wuauserv so that security patches cannot eliminate them.
- **Service registration damaged.** A faulty update or disk fault can injure the registration, making the service report as disabled despite correct configuration.
- **A dependency service is disabled.** BITS or Cryptographic Services being off stops the update service from starting.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether the service is actually disabled

Before altering anything, confirm the actual state — Disabled, stuck on Manual, and failing-to-start each want a different remedy.

1. Press Win + R, enter `services.msc`, and hit Enter.
2. Scroll down to Windows Update, double-click the entry, and inspect the Startup type and Service status fields.
3. If Startup type shows Disabled, continue to Fix 2. If it shows Manual or Automatic but the service will not start, skip to Fix 4.

### Fix 2: Switch the service back to Automatic

This is the core fix: return wuauserv to its proper startup type and start it.

1. In the Windows Update properties window, change Startup type to Automatic.
2. Click Start under Service status, then wait for it to report Running.
3. Hit Apply, then OK, and reboot the PC so the change takes hold.
4. Head to Settings > Windows Update and run a check — the error should have vanished.

### Fix 3: Correct the startup value in the registry

When the service reverts to Disabled after rebooting, or services.msc rejects the change, some registry value or policy is enforcing it.

1. Press Win + R, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv`.
2. Open the Start value and change it to 2 (Automatic) — 4 means Disabled.
3. Restart the PC and verify the service stays Automatic.
4. If it still reverts, a group policy is re-applying it — check `gpedit.msc` under Windows Update policies.

### Fix 4: Revive the services it depends on

BITS or Cryptographic Services being disabled stops Windows Update from starting, even if wuauserv itself appears healthy. Reviving the dependencies resolves situations where the main service starts, then immediately dies.

1. In services.msc, open the Background Intelligent Transfer Service entry, change Startup type to Automatic (Delayed Start), then start the service.
2. Do the same for Cryptographic Services, DCOM Server Process Launcher, and RPC Endpoint Mapper.
3. Go back to the Windows Update entry, choose Automatic, and press Start.
4. Retry the update check.

### Fix 5: Let the troubleshooter have a go

The troubleshooter detects disabled services and broken registrations, repairing them automatically.

1. Slide into Settings > System > Troubleshoot > Other troubleshooters.
2. Deploy the Windows Update entry and track its prompts.
3. Reboot the PC and verify the service runs.

### Fix 6: Reset the update components completely

If the service starts but updates still fail, the engine's cache may be corrupt. A full reset clears it — this is worth trying before concluding the service itself is broken, since cache corruption mimics service failure.

1. Switch the services off: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Box the folders up with new names: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Switch the services back on: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Verify updates arrive and confirm the error is gone.

### Fix 7: Reinstall Windows as the final fallback

When the service cannot be revived by any means, its registration or the surrounding infrastructure is damaged beyond repair. Reinstalling 24H2 over the existing install rebuilds it. Pull the ISO only from [Microsoft's official Windows 11 download site](https://www.microsoft.com/en-us/software-download/windows11).

1. Mount the ISO and kindle `setup.exe`.
2. Welcome the license terms, then anoint **Keep personal files and apps**.
3. Bestow 30–90 minutes across several restarts upon the installer, and forbid interruption.
4. Evince that the update service runs normally afterward.

## Closing

Nine times out of ten, this error is a service that someone — or some script — switched off, and switching it back on ends the story. The tenth time, a policy or registry value is fighting you, and Fix 3 exists for exactly that battle. If updates then fail with a different code, the [24H2 update-error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) explains the rest, and the [troubleshooter guide](/articles/best-way-to-fix-windows-update-with-troubleshooter/) automates the service checks. Service configuration is documented in [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
