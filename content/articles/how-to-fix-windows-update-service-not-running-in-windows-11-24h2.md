---
title: "Fix the Windows Update Service Not Running in Windows 11 24H2"
slug: how-to-fix-windows-update-service-not-running-in-windows-11-24h2
date: 2026-09-09
categories: ["windows-update"]
tags: ["windows update service", "wuauserv", "service not running", "windows 11 24h2"]
description: "Windows Update service not running on Windows 11 24H2? Restart and repair wuauserv, BITS, and related services with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-not-running-in-windows-11-24h2.webp"
faqs:
  - q: "Which services does Windows Update need?"
    a: "The core four are Windows Update (wuauserv), Background Intelligent Transfer Service (BITS), Cryptographic Services (cryptSvc), and Windows Installer (msiserver). All four must be present and startable; if any is Disabled or crashes on start, updates fail. You can verify all four quickly in services.msc before starting any deeper troubleshooting."
  - q: "Why does the Windows Update service keep stopping?"
    a: "Common reasons: a corrupt SoftwareDistribution database crashing the service on scan, a third-party 'optimizer' disabling it, group policy forcing it off, or damaged service registration. It rarely stops for no reason — something is acting on it. Finding that something — a tool, a policy, or corruption — is the real fix."
  - q: "Is it safe to set the Windows Update service to Automatic?"
    a: "Yes — Automatic (Delayed Start) is the healthy default on Windows 11. Setting it to Manual is also fine since the system starts it on demand. What you must avoid is Disabled, which blocks all updating including security patches. Leave it on the default and investigate anything that changes it."
  - q: "What if the service starts but stops immediately?"
    a: "That points at corruption the service trips over at startup — usually the DataStore database or the catroot2 catalogs. Resetting the SoftwareDistribution folder (covered below) resolves most start-then-stop behavior. If the behavior survives a cache reset, the service registration itself is likely damaged and needs re-registering."
---

When the Windows Update service (wuauserv) is not running, nothing else in the update pipeline matters: scans fail instantly, the Settings page shows errors, and the troubleshooter may be the only thing that even notices. On 24H2 this usually presents as error 0x80070422 or a Settings page that spins forever.

Services do not usually die on their own. Something stopped it — a corrupt database crashing it at startup, a cleanup tool disabling it, a policy forcing it off, or damaged registration. The fix sequence therefore has two halves: get the service running again now, and find what killed it so it stays running.

The steps below move from the simple restart through registration repair to the policy and corruption checks. If the service runs but scans still fail, the [update database error guide](/articles/how-to-fix-windows-update-database-error-after-windows-11-update/) covers the next layer. If the service isn't merely stopped but missing from the Services list entirely, that's a different failure — our [missing Windows Update service guide](/articles/how-to-fix-windows-update-service-missing-in-windows-11-24h2/) covers restoring a wuauserv that doesn't exist at all.

## Why this happens

- **Corrupt DataStore crashing the service:** The service reads its database at startup; a corrupt database can crash it immediately.
- **Disabled by cleanup/optimizer tools:** Third-party 'debloater' and optimizer tools routinely disable wuauserv as a 'tweak'.
- **Group policy forcing it off:** Domain or previously applied policies can set the service to Disabled and lock the setting.
- **Damaged service registration:** Corrupt registry entries for the service prevent it from starting even when set correctly.
- **Dependency failure:** If a dependency like RPC or DCOM fails, wuauserv cannot start — rare, but worth checking.
- **Antivirus blocking the service:** Overzealous security software occasionally blocks the service executable.
- **Corrupt catroot2 catalogs:** Damaged cryptographic catalogs can crash cryptSvc, which cascades into update failures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the service properly

A surprising number of cases are just a service that stopped and never restarted. Do it cleanly.

1. Press Win + R, type `services.msc`, and open the Services console.
2. Find Windows Update, double-click it, set Startup type to Automatic (or Manual), and click Start.
3. Do the same check for Background Intelligent Transfer Service, Cryptographic Services, and Windows Installer.
4. Try a manual update scan. If the service stops again immediately, continue — something is killing it.

### Fix 2: Check for group policy or tool interference

If the service is Disabled and will not stay enabled, something is enforcing that state.

1. In services.msc, if Startup type reverts to Disabled after you change it, suspect policy or a third-party tool.
2. Run `gpresult /h report.html` from a prompt and check for Windows Update service policies.
3. Uninstall or pause any 'optimizer', 'debloater', or privacy tool that manages services.
4. After removing the enforcer, set the service to Automatic again and reboot.

### Fix 3: Reset the SoftwareDistribution and catroot2 folders

The classic fix for start-then-crash behavior: remove the corrupt data the service chokes on.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver` (skip any that are already stopped).
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Run `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`, reboot, and scan.

### Fix 4: Re-register the update components

Damaged registration prevents the service from initializing. Re-registering rebuilds it.

1. Open an elevated Command Prompt.
2. Run: `regsvr32 wuapi.dll`, `regsvr32 wuaueng.dll`, `regsvr32 wups.dll`, `regsvr32 wuwebv.dll`, `regsvr32 wucltux.dll`, confirming each.
3. Also re-register BITS: `regsvr32 qmgr.dll` and `regsvr32 qmgrprxy.dll`.
4. Reboot and verify the service starts and stays running.

### Fix 5: Run the Windows Update troubleshooter

The troubleshooter automates the service-registration and permission repairs, catching anything manual steps missed.

1. Go to Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run.
2. Apply all fixes and reboot.
3. Confirm the service is running in services.msc, then scan.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents further manual reset steps if needed.

### Fix 6: Repair system files with DISM and SFC

When the service executable or its dependencies are damaged, file repair is required.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt.
2. Follow with `sfc /scannow` and reboot.
3. Verify the service starts. If it still will not start after clean DISM/SFC, the damage is likely in the service registration hive — an in-place upgrade repair is the next step.

### Fix 7: Audit what disabled it so it stays fixed

A service that keeps getting disabled will keep breaking updates. Find the culprit.

1. Check Task Scheduler for tasks that stop or disable wuauserv.
2. Review installed 'tweaker' and privacy tools — many reapply their settings on boot.
3. On managed machines, confirm with IT whether update policies are intentional.
4. Once the enforcer is removed and the service holds its Automatic setting across reboots, run one final manual scan to confirm the pipeline is healthy.

### Fix 8: Restore the service's default security descriptor

Corrupt permissions on the service itself can prevent it from starting even when its startup type is correct. The service's security descriptor lives outside normal settings, so the usual restart dance never touches it.

1. Open an elevated Command Prompt and run `sc sdshow wuauserv` to record the current descriptor for reference.
2. Run the Windows Update troubleshooter's service-repair pass first — it restores standard descriptors in most cases.
3. If the service still refuses to start, apply the documented default descriptor for wuauserv with `sc sdset` (copy it verbatim from Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) — one wrong character breaks it).
4. Reboot and verify the service starts automatically and survives a second reboot.
5. If permissions were the issue, the service now stays up permanently — nothing will silently revert it.

## Closing

A Windows Update service that is not running is a symptom with a discoverable cause: corrupt data crashing it, a tool disabling it, or damaged registration. Restart it properly, remove whatever is forcing it off, reset the cache it chokes on, and re-register its components. Verify it survives a reboot — a service that stays running is a service that is actually fixed. If scans still fail with the service healthy, the [database error repair](/articles/how-to-fix-windows-update-database-error-after-windows-11-update/) covers the next layer down.
