---
title: "Fix Windows Update Error 0x80070422 on Windows 11: Service Won't Start"
slug: how-to-fix-windows-update-error-0x80070422-on-windows-11
date: 2026-10-12
categories: ["windows-update"]
tags: ["windows 11", "windows update", "error 0x80070422", "update service", "services"]
description: "Error 0x80070422 means the Windows Update service can't start. Learn to re-enable it, repair its dependencies, and undo what disabled it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070422-on-windows-11.webp"
faqs:
  - q: "What does error 0x80070422 mean?"
    a: "It means 'the service cannot be started' — Windows Update tried to run, but its service (or a service it depends on) is disabled or failing to start. The cause is usually a disabled service, corrupted service registration, or a third-party tool that turned updates off."
  - q: "Why would the Windows Update service be disabled on my laptop?"
    a: "Common reasons: 'debloating' or privacy utilities that disable updates, old update-blocker tools, enterprise policies from a previous workplace or school, malware, or a user manually disabling the service and forgetting. Windows itself does not disable this service on consumer machines."
  - q: "Is it safe to re-enable the Windows Update service?"
    a: "Yes. The service is designed to run and is required for security patches. Re-enabling it restores normal update behavior. If a tool keeps disabling it, remove the tool rather than fighting it — security updates are not optional, and a machine that cannot update is a machine drifting toward vulnerability."
  - q: "What if the service starts but the error persists?"
    a: "Then the problem is in a dependency: BITS, Cryptographic Services, or DCOM/RPC. Check each dependency's status in services.msc, verify the service's logon account is still Local System, and repair corrupted service registrations with the DLL re-registration steps covered later in this guide."
---

Error 0x80070422 is refreshingly honest as Windows errors go: "the service cannot be started." When you see it in Windows Update on Windows 11, it means the update engine tried to do its job but the Windows Update service — or something it depends on — refused to start. Unlike the cryptic cache errors, this one points at a specific layer: services. And services can be inspected, restarted, and repaired with precision.

The detective question is always *why* the service is disabled. Windows 11 does not disable its own update service. Something did it: a debloating script, an update-blocker utility, a group policy from a managed environment, or occasionally malware. Fixing the error means both re-enabling the service and dealing with whatever disabled it, or the error will return.

## Why this happens

- **Service set to Disabled:** The Windows Update service (wuauserv) startup type was changed to Disabled, so it cannot start on demand.
- **Debloating/privacy tools:** Third-party scripts that promise to "remove bloat" commonly disable update services as a side effect.
- **Update-blocker utilities:** Tools designed to stop Windows updates do it by breaking the services, and their changes persist after the tool is removed.
- **Group Policy restrictions:** Machines that were ever domain-joined or managed may carry policies disabling update services.
- **Corrupted service registration:** The service's registry entries can be damaged, so the Service Control Manager cannot start it even when configured correctly.
- **Failed dependencies:** wuauserv depends on RPC and DCOM; BITS has its own dependency chain. If a dependency fails, the update service fails with it.
- **Wrong service logon account:** If the service's logon credentials were changed from the defaults, it cannot start.
- **Malware:** Some malware disables update services deliberately to prevent security patches from removing it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-enable the Windows Update service

The direct fix: set the service back to its proper configuration and start it.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Double-click **Windows Update**.
3. Set **Startup type** to **Automatic**, click **Apply**, then click **Start**.
4. Click OK, then go to **Settings > Windows Update** and check for updates.

### Fix 2: Check the dependency services

The update service does not work alone. Verify its supporting cast.

1. In `services.msc`, confirm these are running: **Background Intelligent Transfer Service** (Manual), **Cryptographic Services** (Automatic), **DCOM Server Process Launcher** (Automatic), **RPC Endpoint Mapper** (Automatic).
2. Start any that are stopped and set their startup types as listed.
3. In the Windows Update service's **Properties > Dependencies** tab, confirm the listed dependencies match and are running.
4. Retry Windows Update.

### Fix 3: Verify the service logon account

A changed logon account silently prevents the service from starting.

1. In `services.msc`, double-click **Windows Update** and open the **Log On** tab.
2. It should be set to **Local System account** with **Allow service to interact with desktop** unchecked.
3. If it was changed, restore it to Local System, click Apply, and try starting the service.
4. Do the same check for BITS and Cryptographic Services.

### Fix 4: Remove or undo update-blocking tools

If a tool disabled the service, it will do it again. Find and neutralize it.

1. Check **Settings > Apps > Installed apps** for update blockers, "Windows update disablers," debloating tools, or aggressive privacy utilities — uninstall them.
2. Check **Task Scheduler** (**taskschd.msc**) for tasks that disable update services on a schedule, and disable those tasks.
3. Re-enable the services per Fix 1 and Fix 2, restart, and confirm they stay enabled after a reboot.
4. If a workplace or school policy is the cause and the laptop is yours now, remove the management enrollment under **Settings > Accounts > Access work or school**.

### Fix 5: Reset the service registration via Command Prompt

If the service is configured correctly but still will not start, its registration may be corrupted. Re-register the update DLLs.

1. Open **Terminal (Admin)**.
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Re-register core DLLs: run `regsvr32 /s wuapi.dll`, `regsvr32 /s wuaueng.dll`, `regsvr32 /s wups.dll`, `regsvr32 /s wups2.dll`, `regsvr32 /s wuwebv.dll`, `regsvr32 /s atl.dll`.
4. Start the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, then check for updates.

### Fix 6: Scan for malware

Because malware deliberately disables update services, a 0x80070422 with no other explanation deserves a security scan.

1. Open **Windows Security > Virus & threat protection** and run a **Full scan** (not just quick).
2. If you use third-party antivirus, run its full scan too.
3. Remove anything found, restart, re-enable the services, and retry updates.
4. Persistent reinfection signs (service re-disables itself within hours) warrant an offline scan via **Windows Security > Scan options > Microsoft Defender Offline scan**.

### Fix 7: Repair system files and reset the update components

As the final software-level repair, fix any underlying corruption and reset the whole update stack.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. Reset the cache: stop the three services, rename `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` with `.old` suffixes, and restart the services.
3. Restart the laptop and check for updates — the same comprehensive reset that clears [stuck update downloads](/articles/how-to-fix-windows-update-stuck-downloading-step-by-step/) applies here.
4. For reference on normal update service behavior, see the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows).

A word on persistence: group policy is the most stubborn source of this error because policies reapply at every reboot and policy refresh. If Fix 1 works but the service is disabled again the next morning, run rsop.msc (Resultant Set of Policy) to see which policies apply to your machine and where they come from. Ex-domain laptops often carry these as tattooed registry policies that survive even after leaving the domain. For the Windows 10 incarnation of this problem, including the legacy update-blocker tools common on that OS, see our [Windows 10 0x80070422 guide](/articles/how-to-fix-windows-update-error-0x80070422-on-windows-10/). Removing the policy source beats re-enabling the service every week.

## Closing

Error 0x80070422 is a service problem with a service answer: re-enable Windows Update and its dependencies, fix the logon account, and — critically — find and remove whatever disabled them in the first place. Debloaters and update blockers are the usual culprits, and uninstalling them prevents the endless re-disable cycle. Once the services start cleanly and stay started, Windows Update simply works again.
