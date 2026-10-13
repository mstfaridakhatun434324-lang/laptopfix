---
title: "Windows Update Error 0x80070422 on HP Laptops: Service Disabled Fix"
slug: how-to-fix-windows-update-error-0x80070422-on-hp-laptop
date: 2026-09-24
categories: ["windows-update"]
tags:
  - "error 0x80070422"
  - "hp laptop"
  - "windows update"
  - "service disabled"
description: "Error 0x80070422 means the Windows Update service is disabled or cannot start. On HP laptops, optimizers and security tools often cause it — here is the full repair."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070422-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x80070422 mean?"
    a: "It means a required service is disabled or failed to start — for Windows Update, almost always the Windows Update service (wuauserv) itself. The update engine cannot run without its service, so every check and install fails with this code until the service is restored."
  - q: "Why would the Windows Update service be disabled on my HP laptop?"
    a: "Common culprits: system optimizer or debloater tools that disable services aggressively, HP or third-party utilities changing service states, malware, or a previous repair that stopped the service and never restarted it afterward. It is never disabled by Windows itself under normal conditions."
  - q: "Is it safe to re-enable the Windows Update service?"
    a: "Yes — it is supposed to run. Setting wuauserv back to its default restores normal behavior; you are undoing someone else's change, not hacking the system. Setting wuauserv back to its default (Manual Trigger Start on Windows 11, Automatic on Windows 10) restores normal behavior. You are undoing someone else's change, not hacking the system."
  - q: "What if the service won't stay running after I start it?"
    a: "A service that immediately stops again points at deeper damage: corrupted service binaries, dependency failures, or malware. The DISM and SFC repairs plus the full malware scan in this guide address those underlying causes methodically, in that order. Start with the malware scan since an infection will undo the other repairs."
---

Error 0x80070422 is refreshingly honest as Windows errors go: it means the service cannot start because it is disabled. No cryptic parameters, no missing files — just an update engine with its ignition switched off. On HP laptops this happens more than it should, usually courtesy of an optimizer tool, an overzealous debloater, or a security suite that got too ambitious.

The fix is conceptually simple — turn the service back on — but doing it properly means checking the service's dependencies, its startup type, the policies that might be forcing it off, and whatever turned it off in the first place. Otherwise you will be back here next month.

This HP-aware guide covers the full repair: the service itself, its dependencies, the common disablers on HP machines, and the deeper fixes for services that refuse to stay running. If your code is different, our [0x80070005 repair guide](/articles/how-to-fix-windows-update-error-0x80070005-step-by-step/) addresses the access-denied variant.

## Why this happens

- **wuauserv disabled:** the Windows Update service set to Disabled by an optimizer, debloater, or manual tweak.

- **Dependency services disabled:** BITS, DCOM, and RPC dependencies turned off, so wuauserv cannot start even when enabled.

- **Group Policy forcing it off:** policy settings (from tweakers or managed setups) overriding the service configuration.

- **Corrupted service registration:** the service's registry entries damaged, so it fails to start with 0x80070422.

- **HP utility interference:** some HP and third-party utilities manage services aggressively during their own updates.

- **Malware:** malicious software disabling update services to avoid removal — worth ruling out.

- **Damaged service binaries:** corrupted system files behind the service itself.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-enable the Windows Update service

The direct fix: open the Services console and restore wuauserv to its proper startup type. This alone resolves most 0x80070422 cases, so it is always worth trying before the deeper dependency and policy checks.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find Windows Update in the list and double-click it.
3. Set Startup type to Manual (Windows 11 default) or Automatic.
4. Click Start to start the service now, then Apply and OK.
5. Run Check for updates to confirm the error is gone.

### Fix 2: Check the dependency services

wuauserv depends on other services. If any dependency is disabled, the update service fails to start with the same code — so verify the whole chain.

1. In services.msc, find Background Intelligent Transfer Service — set to Manual and start it.
2. Verify DCOM Server Process Launcher and RPC Endpoint Mapper are Running and Automatic.
3. Check Cryptographic Services — set to Automatic and start it.
4. Return to Windows Update and try starting it again.
5. Retest with Check for updates.

### Fix 3: Remove whatever keeps disabling it

A service that was disabled once will be disabled again unless you find the cause. Audit the usual suspects on HP laptops before considering the job done.

1. Check installed optimizers, debloaters, and privacy tools — undo their service tweaks or uninstall them.
2. Review Task Manager Startup apps for aggressive system utilities and disable them.
3. Check HP utilities for service-management features and set them to non-aggressive modes.
4. On Pro editions, check gpedit.msc under Windows Update policies for forced service states.
5. Monitor for a week: if the service disables itself again, the culprit is still installed.

### Fix 4: Scan for malware

Malware disabling update services is a classic persistence technique. With the service restored, a full scan rules out the malicious cause definitively.

1. Update Microsoft Defender definitions (Settings, Privacy and security, Windows Security).
2. Run a Full scan — not the quick scan — and let it complete.
3. For a second opinion, run the Microsoft Safety Scanner from [Microsoft's support site](https://support.microsoft.com/en-us/windows).
4. Remove anything found and restart.
5. Confirm the Windows Update service is still running afterward.

### Fix 5: Repair the service registration and files

If the service is enabled but still throws 0x80070422 when starting, its registration or binaries are damaged. Re-registering components and repairing system files addresses this layer.

1. Open Terminal (Admin).
2. Re-register update DLLs: `regsvr32 wuaueng.dll`, `regsvr32 wuapi.dll`, `regsvr32 wups.dll`.
3. Run `sfc /scannow` to completion.
4. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then restart.
5. Try starting the Windows Update service again from services.msc.

### Fix 6: Reset the update components around the service

A corrupted cache can prevent the freshly started service from functioning, producing confusing follow-on errors. Resetting the components gives the revived service clean state to work with.

1. In Terminal (Admin), run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with `net start` commands.
4. Reboot the HP laptop.
5. Run Check for updates and confirm normal operation.

### Fix 7: Refresh HP drivers and lock in the fix

Finish the HP-specific picture: current drivers reduce the need for the utilities that meddle with services, and a final check confirms everything holds.

1. Visit [HP's support site](https://support.hp.com/us-en) and install current chipset drivers for your model.
2. Run HP Support Assistant's tune-up once.
3. Verify the Windows Update service shows the correct startup type in services.msc.
4. Run one final Check for updates successfully.
5. Avoid optimizer tools going forward — they caused this.

## Closing

Error 0x80070422 is the update engine with its service switched off, and the repair is to switch it back on properly: the service, its dependencies, the policy or tool that disabled it, and the deeper repairs if it will not stay running. Find the disabler as well as the disabled, and this code will not return. If downloads themselves are being throttled by connection settings, our [metered-connection guide](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/) covers that side of the problem.
