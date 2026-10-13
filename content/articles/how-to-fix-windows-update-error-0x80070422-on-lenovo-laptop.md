---
title: "Windows Update Error 0x80070422 on a Lenovo Laptop: Fixing It"
slug: how-to-fix-windows-update-error-0x80070422-on-lenovo-laptop
date: 2026-09-23
categories: ["windows-update"]
tags: ["0x80070422", "windows update", "lenovo laptop", "service disabled"]
description: "Error 0x80070422 means a required service can't start. Restore the disabled Windows Update service on your Lenovo laptop step by step."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070422-on-lenovo-laptop.webp"
faqs:
  - q: "What does error 0x80070422 mean?"
    a: "It means 'the service cannot be started' — Windows Update tried to start a service it needs (usually the Windows Update service itself, or BITS) and the start failed because the service is disabled or its configuration is broken. The update cannot proceed without its services, so it aborts with this code."
  - q: "Why is the Windows Update service disabled on my Lenovo?"
    a: "The common causes: a third-party optimizer or 'debloat' tool disabled it, malware disabled it to block security patches, a failed update left it in a disabled state, or a group policy (common on ex-corporate machines) forces it off. Lenovo's own software does not disable it — the cause is almost always external."
  - q: "Is it safe to re-enable the service?"
    a: "Yes — the Windows Update service is a core Windows component and should be running on Automatic. Re-enabling it restores normal update behavior. The only caveat: if malware disabled it, re-enabling without removing the malware means it may get disabled again, so scan for threats if the service will not stay enabled."
  - q: "What's the difference between 0x80070422 and a service that won't start?"
    a: "They are the same problem viewed from different angles. Error 0x80070422 is what Windows Update reports when the service cannot start; a service that will not start in services.msc is the underlying condition. Our [service repair guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) covers the deep repair if the quick fixes here do not hold."
---

Error 0x80070422 is refreshingly direct: a service Windows Update needs cannot be started. In the vast majority of cases, that service is the Windows Update service itself (wuauserv), and it is disabled — its startup type set to Disabled, so every start attempt fails instantly. The update engine reports the failure with this code and stops.

The fix is conceptually simple — re-enable the service — but the follow-up question matters more: why was it disabled, and will it stay enabled? The sequence below re-enables the service, repairs it if re-enabling does not stick, and hunts the cause so the error does not return next month. For [service failures after the 24H2 update specifically](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/), that guide has migration-specific notes.

Before diving in, a quick diagnostic you can do right now: open services.msc and look at the Windows Update service's startup type. If it says Disabled, Fix 1 is your answer and you will be done in two minutes. If it says Automatic but the service still will not start, skip ahead to Fix 3 — your problem is deeper than a flipped switch, and the command-line reset plus dependency checks will find it.

## Why this happens

- **Service set to Disabled:** The startup type was changed to Disabled by software or a tweak.
- **Debloat tools:** Third-party optimizers disabling the service as part of "privacy" tweaks.
- **Malware:** Malicious software blocking updates to protect itself.
- **Group policy:** Corporate policies forcing the service off, lingering on ex-business laptops.
- **Corrupted service configuration:** Damaged registry keys preventing startup even when enabled.
- **Failed dependencies:** BITS or RPC problems cascading into the update service.
- **Antivirus blocking:** Security software preventing the service process from launching.
- **Corrupted service binaries:** Damaged files the service needs to start.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-enable the service in services.msc

The direct fix — correct the startup type and start it.

1. Press Win + R, type `services.msc`, and press Enter.
2. Double-click **Windows Update**.
3. Change **Startup type** from Disabled to **Automatic**.
4. Click **Start** — if it starts cleanly, the problem was just the setting.
5. Open Settings and run **Check for updates** to confirm.

### Fix 2: Enable the dependencies too

The update service needs its supporting cast. Microsoft documents the service model on the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. In services.msc, set **Background Intelligent Transfer Service** to Automatic (Delayed Start is fine) and start it.
2. Verify **Cryptographic Services** is running and set to Automatic.
3. Confirm **Remote Procedure Call (RPC)** and **DCOM Server Process Launcher** are running — these are system-critical.
4. Try starting the Windows Update service again.
5. Test with **Check for updates**.

### Fix 3: Reset via command line

When the GUI will not cooperate, reset the service configuration directly.

1. Open Command Prompt as administrator.
2. Run `sc config wuauserv start= auto` — note the required space after `=`.
3. Run `sc config bits start= delayed-auto`.
4. Run `net start wuauserv` and `net start bits`.
5. Verify with `sc query wuauserv` showing STATE: RUNNING.

### Fix 4: Check for group policy enforcement

Policies can force the service off and revert your manual changes.

1. Press Win + R, type `gpedit.msc`, and press Enter (Pro editions only).
2. Go to **Computer Configuration > Administrative Templates > Windows Components > Windows Update**.
3. Look for policies configuring the update service — set any disabling ones to **Not Configured**.
4. Run `gpupdate /force` in an elevated Command Prompt.
5. Re-enable the service and confirm it stays enabled after a reboot.

### Fix 5: Scan for malware and undo debloat damage

If something disabled the service deliberately, find it.

1. Run a full scan with Windows Security.
2. Run a Microsoft Defender Offline scan for persistent threats.
3. Review any optimizer, debloat, or privacy tools you have used — re-enable the update service in their settings.
4. Check Task Scheduler for tasks that stop the service.
5. Re-enable the service and verify it survives a full reboot.

### Fix 6: Repair the service registry keys

Damaged configuration prevents startup even with the right startup type.

1. Open `regedit` and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv`.
2. Export the key as a backup.
3. Set the **Start** value to `2` (Automatic).
4. Verify **ImagePath** and **Type** look sane — `Type` should be `32`.
5. Restart and test the service.

### Fix 7: Repair system files

Corrupted service binaries get replaced here.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `sfc /scannow`.
4. Restart the laptop.
5. Start the service and run **Check for updates** — the 0x80070422 error should be gone.

### Fix 8: In-place upgrade to rebuild the service stack

When the service will not stay enabled after every repair, rebuild the stack it runs on.

1. Download the Windows 11 Media Creation Tool from Microsoft.
2. Run it and choose **Upgrade this PC now**, keeping personal files and apps.
3. The repair install replaces all services — including wuauserv and its dependencies — with clean copies.
4. After completion, verify the service is Automatic and running.
5. Run **Check for updates** to confirm 0x80070422 is gone. If [downloads stall at this point](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/), that is a separate pipeline issue with its own fix path.

## Closing

Error 0x80070422 is the update engine telling you plainly that its service cannot start — and the fix is equally plain: re-enable it, repair it if it will not stay enabled, and remove whatever disabled it. The critical step most people skip is Fix 4 and Fix 5's hunt for the cause, because a service that gets re-disabled is a problem that returns. Find the disabler — the debloat tool, the policy, the malware — and the error stays fixed permanently. The service is the foundation; everything else in Windows Update is built on top of it.
