---
title: "Windows Update Service Not Running on Windows 11: Restoring It"
slug: how-to-fix-windows-update-service-not-running-on-windows-11
date: 2026-09-14
categories: ["windows-update"]
tags: ["update service", "wuauserv", "windows 11", "service fix"]
description: "The Windows Update service won't stay running on Windows 11? Diagnose why wuauserv keeps stopping and restore reliable updates."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-not-running-on-windows-11.webp"
faqs:
  - q: "Why does the Windows Update service keep stopping on Windows 11?"
    a: "On Windows 11 the most common reasons are a crashed dependency (BITS or the RPC service), corrupted service registry keys after a feature update, third-party debloat tools that disable it, or the service hitting an error during startup and giving up. Check Event Viewer > Windows Logs > System for the service control manager entries — they usually name the exact failure."
  - q: "Is it normal for the service to stop when not updating?"
    a: "Yes, partially. Windows 11 stops wuauserv when it is idle to save resources — that is normal behavior, not a problem. The problem is when the service will not start on demand: Settings shows an error, updates never check, and manual starts fail immediately. Idle-stopped is fine; broken is not."
  - q: "Can I set the service to Automatic Delayed Start?"
    a: "You can, but Automatic is the safer choice while troubleshooting. Delayed start postpones the service at boot, which is fine on a healthy system but can mask startup-order problems. Once everything works reliably, either setting is acceptable — Windows manages the service lifecycle itself either way."
  - q: "Does this affect Microsoft Store updates too?"
    a: "Sometimes. The Store uses its own delivery mechanism, but it shares some underlying components (BITS, cryptographic services) with Windows Update. A broken wuauserv alone usually does not stop Store updates, but if the shared dependencies are the real problem, both pipelines suffer. Fix the dependencies and both recover."
---

On Windows 11, the Windows Update service (wuauserv) is designed to stop when idle — so the first thing to establish is whether your service is healthily idle or genuinely broken. The test is simple: open Settings, go to Windows Update, and click **Check for updates**. If the service spins up and the check runs, nothing is wrong. If you get an error, the service refuses to start, or it starts and dies within seconds, you have a real problem — and this guide fixes it.

Windows 11 adds a few wrinkles over Windows 10: feature updates like 24H2 can damage the service's registry configuration during migration, and the OS is more aggressive about stopping idle services, which confuses diagnosis. The sequence below accounts for both. For [post-24H2 service failures specifically](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/), that guide has migration-specific notes.

## Why this happens

- **Idle-stop confusion:** The service stopped normally when idle, and the real issue is elsewhere.
- **24H2 migration damage:** The feature update corrupted the service's registry keys.
- **Failed dependencies:** BITS, RPC, or DCOM launcher problems cascade into wuauserv.
- **Debloat tools:** Third-party optimizers disable the service and sometimes break its configuration.
- **Corrupted service binaries:** The wuauserv host files damaged by disk errors or interrupted updates.
- **Permission drift:** The service logon account lost required privileges.
- **Antivirus blocking:** Security software preventing the service process from launching.
- **Stuck in a crash loop:** The service starts, hits an error, stops, and Windows gives up restarting it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it is actually broken

Do not repair a healthy idle service.

1. Open **Settings > Windows Update** and click **Check for updates**.
2. Open Task Manager's Services tab and watch for wuauserv while the check runs.
3. If the check completes, the service is fine — your update problem lies elsewhere, such as [stuck downloads](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/).
4. If you get an error like "something went wrong," proceed — the service is genuinely broken.
5. Note the exact error message; it guides the later fixes.

### Fix 2: Start the service and set Automatic

The basic reset — effective more often than you would expect.

1. Press Win + R, type `services.msc`, and press Enter.
2. Double-click **Windows Update**, set **Startup type** to **Automatic**.
3. Click **Start** and observe: clean start, immediate error, or start-then-stop.
4. On the **Recovery** tab, set all three failure actions to **Restart the Service** with a one-minute delay.
5. Test with **Check for updates** in Settings.

### Fix 3: Repair the dependencies

A service is only as healthy as what it depends on. Microsoft documents the dependency chain on the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. In the service properties, open the **Dependencies** tab and note every listed service.
2. Confirm **Remote Procedure Call (RPC)** and **DCOM Server Process Launcher** are running — Windows cannot function without them, so their failure indicates deeper trouble.
3. Start **Background Intelligent Transfer Service** if it is stopped.
4. Check **Cryptographic Services** as well — the update engine needs it for signature validation.
5. Retry starting the Windows Update service.

### Fix 4: Reset via command line

Bypass any GUI weirdness with direct service control commands.

1. Open Command Prompt as administrator.
2. Run `sc config wuauserv start= auto` — the space after `=` is mandatory.
3. Run `sc failure wuauserv reset= 86400 actions= restart/60000/restart/60000/restart/60000` to configure auto-restart on failure.
4. Run `net start wuauserv`.
5. Verify with `sc query wuauserv` — look for STATE: RUNNING.

### Fix 5: Check the registry configuration

Feature updates sometimes leave the service key damaged.

1. Open `regedit` and go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv`.
2. Export the key as a backup before touching anything.
3. Verify **Start** equals `2`; set it to `2` if it shows `4`.
4. Verify **Type** is `32` (shared process) — if it is anything else, the key is corrupt.
5. If the key is corrupt beyond simple values, continue to Fix 6 rather than guessing.

### Fix 6: Repair system files

Damaged host binaries get replaced here.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait.
3. Run `sfc /scannow`.
4. Restart the laptop.
5. Start the service and run **Check for updates**.

### Fix 7: Rule out interference

Something may be actively killing the service.

1. Check any debloat, privacy, or optimizer tools you have run — re-enable the update service in their settings.
2. Run a full Windows Security scan, plus an offline scan for persistent malware.
3. Open Task Scheduler and look for non-Microsoft tasks that stop services.
4. Temporarily disable third-party antivirus and test the service start.
5. Once the service survives a full reboot cycle untouched, the interference is gone.

### Fix 8: In-place upgrade to rebuild the service stack

When the service will not start after every targeted repair, the service stack itself needs rebuilding.

1. Download the Windows 11 Media Creation Tool from Microsoft.
2. Run it and choose **Upgrade this PC now**, keeping personal files and apps.
3. The repair install replaces all system services, including wuauserv and its dependencies, with clean copies.
4. After completion, verify the service starts and survives reboots.
5. Run **Check for updates** to confirm the full pipeline works end to end.

## Closing

On Windows 11, half of all "service not running" reports turn out to be the healthy idle behavior — which is why Fix 1's verification matters. For the genuinely broken half, the cause is almost always in the short list: startup type, dependencies, or registry damage from a feature update. Work the sequence, verify with a real update check after each fix, and the service will be back to its quiet, mostly-invisible self — which is exactly how it should be. If you manage multiple machines, the dependency check in Fix 3 is the fastest triage step to teach others.
