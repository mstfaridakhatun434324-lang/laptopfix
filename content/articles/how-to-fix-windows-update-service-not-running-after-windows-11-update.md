---
title: "Windows Update Service Not Running After a Windows 11 Update? Here's the Fix"
slug: how-to-fix-windows-update-service-not-running-after-windows-11-update
date: 2026-09-07
categories: ["windows-update"]
tags: ["update service", "wuauserv", "windows 11", "update error", "services"]
description: "Windows Update fails because its service isn't running? How to restart wuauserv, fix services that won't stay started, and repair the underlying damage."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-not-running-after-windows-11-update.webp"
faqs:
  - q: "How do I know the Windows Update service isn't running?"
    a: "Open Settings > Windows Update and look for errors like 'Something went wrong' or error 0x80070422, which specifically means a required service is disabled. To confirm, press Win + R, type services.msc, and check the status of 'Windows Update' (wuauserv) — if it shows nothing under Status, it's stopped."
  - q: "The service starts but stops again immediately. Why?"
    a: "A service that won't stay running usually has corrupt dependencies — damaged files in the SoftwareDistribution folder, broken service DLL registrations, or a corrupted service configuration in the registry. The component reset and DLL re-registration steps below address exactly these causes."
  - q: "Is it safe to leave the Windows Update service disabled?"
    a: "No — not long-term. Disabling it stops all security updates, leaving known vulnerabilities unpatched indefinitely. Some 'optimization' guides recommend disabling it for performance, but the security cost far outweighs any minor resource saving. Fix the service instead of disabling it."
  - q: "What's the difference between wuauserv, BITS, and the Orchestrator service?"
    a: "Wuauserv is the main Windows Update service that scans and installs. BITS handles the background downloading. The Update Orchestrator Service manages reboot scheduling and update sessions. All three must be healthy for updates to work — a failure in any one produces different symptoms, which is why the fixes address each."
---

"We couldn't install updates because the update service isn't running" — or the more cryptic 0x80070422. The Windows Update service (wuauserv) is the engine of the whole update system, and when it's stopped or broken, nothing updates: not security patches, not drivers, not the Microsoft Store. Sometimes it just needs a restart. Sometimes it refuses to stay running, which means something underneath it is damaged. The fixes below escalate properly: restart the service, fix its dependencies, repair its registration, and rebuild what's broken.

This is also a foundational fix — many other update symptoms (failed downloads, stuck scans, troubleshooter failures) trace back to an unhealthy update service. If you've been chasing another update problem, make sure this layer is solid first. Our [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) and [metered connection guide](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/) both assume a working service underneath.

## Why this happens

- **Service set to Disabled**: By "optimization" guides, debloater scripts, or third-party tools.
- **Corrupt SoftwareDistribution data**: Damaged cache files crashing the service on startup.
- **Broken service DLL registrations**: Update engine DLLs unregistered by failed updates or registry cleaners.
- **Dependency service failures**: BITS, DCOM, or RPC issues cascading into wuauserv.
- **Corrupt service configuration**: Damaged registry entries for the service itself.
- **Antivirus blocking the service**: Security software preventing the service executable from running.
- **System file corruption**: Damaged shared components the service loads at startup.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Start the service and set it to automatic

The obvious fix first — it resolves cases where the service was simply stopped.

1. Press Win + R, type `services.msc`, press Enter.
2. Find **Windows Update** in the list and double-click it.
3. Set **Startup type** to **Automatic** (or **Manual** — Windows starts it on demand; never **Disabled**).
4. Click **Start**. If it starts cleanly, go to **Settings > Windows Update** and check for updates.
5. If it was set to Disabled and you don't know why, a "tweaking" tool did it — consider what else it changed.
6. If the service won't start or stops immediately, continue.

### Fix 2: Start the dependency services

Wuauserv depends on a chain of services. Check each link.

1. In `services.msc`, verify these are running (start them if not, set to Automatic):
   - **Background Intelligent Transfer Service (BITS)**
   - **Cryptographic Services (CryptSvc)**
   - **DCOM Server Process Launcher** and **RPC Endpoint Mapper** (these should already be running)
   - **Windows Update Medic Service (WaaSMedicSvc)** — the self-healing service for updates
   - **Update Orchestrator Service (UsoSvc)**
2. If BITS won't start, that's your real problem — note its error and continue to Fix 4.
3. After starting dependencies, try starting **Windows Update** again.

### Fix 3: Reset the update components (the service crasher)

Corrupt cache data is the top reason wuauserv dies on startup. Clearing it lets the service start clean.

1. Open **Command Prompt as administrator**.
2. Run:
   - `net stop wuauserv`
   - `net stop bits`
   - `net stop cryptsvc`
   - `net stop msiserver`
   (Some may already be stopped — that's fine.)
3. Rename the data folders:
   - `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   - `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Check `services.msc` — wuauserv should now show **Running**.
6. Run **Check for updates** to rebuild the caches.

### Fix 4: Re-register the update engine DLLs

If the service still won't stay running, its component registrations are broken.

1. Elevated Command Prompt — run each, ignoring individual errors:
   - `regsvr32 wuapi.dll`
   - `regsvr32 wuaueng.dll`
   - `regsvr32 wuaueng1.dll`
   - `regsvr32 wups.dll`
   - `regsvr32 wups2.dll`
   - `regsvr32 wuwebv.dll`
   - `regsvr32 qmgr.dll`
   - `regsvr32 qmgrprxy.dll`
2. Restart the laptop.
3. Try starting the Windows Update service again.
4. This also repairs the BITS issues from Fix 2, since they share components.

### Fix 5: Repair system files the service depends on

A service crashing at startup often loads a corrupt shared DLL. SFC and DISM repair the shared layer.

1. Elevated Command Prompt: `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and check the service status.
4. Check **Event Viewer > Windows Logs > System** for Service Control Manager errors naming wuauserv — the error text may identify the failing module.
5. If a specific DLL is named, the DISM repair should have replaced it; verify with another `sfc /scannow`.

### Fix 6: Reset the service configuration in the registry

When the service's own registry configuration is damaged — wrong image path, broken dependencies list — reset it to defaults.

1. Press Win + R, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv`.
2. Verify **Start** is `2` (Automatic) or `3` (Manual) — not `4` (Disabled).
3. Check **ImagePath** reads `%systemroot%\system32\svchost.exe -k netsvcs -p`.
4. If values look wrong and you're not comfortable editing, the safer path: run the in-place upgrade in Fix 7, which rebuilds service registrations.
5. **Back up the registry** (File > Export) before any manual change.
6. Microsoft documents service troubleshooting on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 7: In-place upgrade to rebuild the servicing infrastructure

If the service won't run after all of the above, the damage is structural. An in-place upgrade rebuilds it while keeping your data.

1. Download the Windows 11 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO, run `setup.exe`, choose **Keep personal files and apps**.
3. After completion, verify in `services.msc` that **Windows Update** is Automatic and running.
4. Run Windows Update — it should now scan and install normally.
5. Revisit whatever disabled the service originally (tweaking tools, debloaters) and don't run it again.

## Closing

The update service is the foundation everything else builds on — when wuauserv won't run, no update of any kind can succeed. The progression from simple restart through component reset, DLL re-registration, and system repair resolves virtually all cases. And the lesson for afterward: nothing that promises "performance" by disabling Windows Update is worth the unpatched vulnerabilities it leaves behind.
