---
title: "Windows Update Service Not Running? Step-by-Step Repair Guide"
slug: how-to-fix-windows-update-service-not-running-step-by-step
date: 2026-10-06
categories: ["windows-update"]
tags: ["wuauserv", "update service", "services.msc", "error 0x80070422", "windows 11"]
description: "Getting 'Windows Update service is not running' or error 0x80070422? Follow this step-by-step repair to restart the service and fix what keeps stopping it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-not-running-step-by-step.webp"
faqs:
  - q: "What does 'Windows Update service is not running' mean?"
    a: "It means the wuauserv service — the engine behind Windows Update — is stopped, disabled, or crashing on start. Without it, Settings can't check for, download, or install updates, and you'll see error 0x80070422. The service can be stopped by failed updates, aggressive 'debloating' tools, group policies, or corrupted service registration."
  - q: "Why does the service stop again after I start it?"
    a: "If wuauserv dies shortly after you start it, something is actively killing it: a corrupted update cache it chokes on at startup, a group policy forcing it disabled, a third-party 'privacy' tool disabling it on a schedule, or damaged system files. The steps below address each of these in order."
  - q: "Can a virus disable Windows Update?"
    a: "Some malware disables wuauserv to prevent security patches from removing it, so a mysteriously disabled update service is worth a full Microsoft Defender offline scan. But in most cases the cause is mundane — a tweaking utility, a managed-device policy, or a failed update — not malware."
  - q: "Is it safe to set the service to Automatic?"
    a: "Yes — Automatic (Delayed Start) is the correct default for wuauserv on a normal home laptop. If some guide told you to disable it to 'stop forced updates,' use the proper pause-updates setting instead; a disabled update service leaves you without security patches."
---

"Something went wrong. Try to reopen Settings later" — or the blunter "Windows Update cannot currently check for updates because the service is not running." Error code 0x80070422 often comes along for the ride. This message means the engine behind Windows Update, a background service called **wuauserv**, is stopped, disabled, or crashing every time it tries to start. No service, no updates — and no security patches until it is fixed.

The good news: this is one of the most mechanical problems in Windows troubleshooting. The service either needs restarting, needs its startup type fixed, or is being killed by something you can find and remove. This guide walks through it step by step, from the two-minute fix to the deep repairs. If your update service is not just stopped but entirely missing from the services list, our [missing-service recovery guide](/articles/how-to-fix-windows-update-service-missing-on-lenovo-laptop/) covers that rarer case.

A quick note on the error codes you'll see: 0x80070422 is the classic "service disabled" code and points straight at Fix 1 or Fix 3. If Settings shows "Something went wrong" with no code, the service is more likely crashing than disabled — jump to Fix 4. And if the service starts fine but updates still fail, the service was never your problem; the issue is downstream in the cache or component store, and our [cumulative-update install guide](/articles/how-to-fix-cumulative-update-fails-to-install-step-by-step/) picks up from there.

## Why this happens

- **Service set to Disabled**: A tweaking utility, "debloat" script, or old guide disabled wuauserv to block updates.
- **Corrupt update cache**: wuauserv crashes at startup when it tries to read a damaged SoftwareDistribution database.
- **Group Policy enforcement**: On work or school laptops, an administrator policy forces the service off.
- **Third-party "privacy" tools**: Utilities that promise to stop Windows telemetry often disable the update service as a side effect.
- **Damaged service registration**: Failed updates or disk errors can corrupt the service's registry entries so it cannot start.
- **Conflicting security software**: Some third-party antivirus products pause update services during their own operations and fail to resume them.
- **Corrupt system files**: Damage to the servicing stack files that wuauserv depends on prevents startup.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Start the service and set it to Automatic

The two-minute fix that solves most cases.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Update** in the list, right-click it, and choose **Properties**.
3. Set **Startup type** to **Automatic (Delayed Start)** — not Disabled, not Manual.
4. Click **Start**. If it starts and stays running, open Settings > Windows Update and check for updates. Done.
5. If it stops again within minutes or refuses to start, continue below.

### Fix 2: Check the dependency services

wuauserv depends on other services; if they are down, it cannot run.

1. In `services.msc`, also verify these are running and set to Automatic or Manual: **Background Intelligent Transfer Service (BITS)**, **Cryptographic Services**, **DCOM Server Process Launcher**, and **RPC Endpoint Mapper**.
2. Start any that are stopped, then try starting Windows Update again.
3. If a dependency refuses to start, note its name and error — that is your real problem, and the [Microsoft update support hub](https://support.microsoft.com/en-us/windows) documents dependency repairs.

### Fix 3: Remove the group policy or tool that keeps disabling it

If the service re-disables itself, something is enforcing it.

1. Press **Win + R**, type `gpedit.msc` (Pro editions) and check **Computer Configuration > Administrative Templates > Windows Components > Windows Update** for policies that disable the service.
2. Check for third-party tools: search installed apps for anything with "debloater," "privacy," "telemetry," or "update blocker" in the name, and uninstall or reconfigure them.
3. In **Task Scheduler**, look for tasks that run scripts at startup targeting wuauserv and disable them.

### Fix 4: Clear the cache the service chokes on

A corrupt SoftwareDistribution database crashes wuauserv at startup.

1. Stop the service: in elevated Terminal, run `net stop wuauserv` and `net stop bits`.
2. Rename the folder: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
3. Start the service: `net start wuauserv`. It rebuilds a clean database on start.
4. Check for updates — a fresh database usually lets the service stay alive.

### Fix 5: Re-register the update DLLs

Damaged service registration can prevent startup even with a clean cache.

1. In elevated Terminal, run: `regsvr32 wuapi.dll`, `regsvr32 wuaueng.dll`, `regsvr32 wups.dll`, `regsvr32 wups2.dll`, `regsvr32 wuwebv.dll`, `regsvr32 qmgr.dll`, `regsvr32 jscript.dll` — confirming each dialog.
2. Restart the laptop and try starting the Windows Update service again.

### Fix 6: Repair system files with DISM and SFC

When the servicing stack itself is damaged, nothing else sticks.

1. In elevated Terminal: `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then: `sfc /scannow`. Restart when finished.
3. Verify the Windows Update service starts and remains running, then run a check for updates.

### Fix 7: Reset Windows Update components with the official script approach

The full reset, done manually so you see every step.

1. In elevated Terminal, stop: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename both `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` with `.old` suffixes.
3. Restart all four services, reboot, and confirm the service holds steady. Persistent failures after this point suggest deeper OS damage — consider an in-place upgrade using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

## Closing

A "service not running" error looks alarming but is usually a configuration problem, not a broken Windows: restart the service, set it to Automatic, and remove whatever keeps killing it. Once wuauserv holds steady, updates flow again and the error disappears for good. If you used any tool that promised to "stop Windows updates forever," uninstall it — that is the culprit more often than anything else.

One final habit worth building: after any major Windows update, glance at `services.msc` and confirm Windows Update is still set to Automatic (Delayed Start) and running. Major updates occasionally reset service configurations, and catching a re-disabled service early saves you from discovering it months later when you're already behind on security patches. A thirty-second check twice a year is cheap insurance for the entire update pipeline.
