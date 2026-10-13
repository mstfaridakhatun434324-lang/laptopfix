---
title: "Windows Update Service Not Running: Troubleshooting Guide"
slug: windows-update-service-not-running-troubleshooting
date: 2026-10-02
categories: ["windows-update"]
tags: ["update service", "wuauserv", "service not running", "troubleshooting"]
description: "Windows Update fails because its service won't run? This troubleshooting guide repairs the service, its dependencies, and the corruption behind it."
thumbnail: "/images/thumbs/windows-update-service-not-running-troubleshooting.webp"
faqs:
  - q: "Why does the Windows Update service keep stopping by itself?"
    a: "The service stops when one of its dependencies fails, when its registry configuration is corrupted, or when third-party software interferes with it. Malware, aggressive system optimizers, and broken updates can all damage the service registration. If it stops repeatedly after you start it manually, the cause is structural, and the dependency and corruption checks below will find it."
  - q: "Is it safe to reset the Windows Update service and its cache?"
    a: "Yes. Stopping the service, renaming the SoftwareDistribution folder, and restarting only clears downloaded update files and the local update database. Your personal files, installed programs, and settings are completely unaffected. Windows rebuilds everything it needs on the next update check, which is exactly why this repair is so reliable."
  - q: "What are the dependencies of the Windows Update service?"
    a: "The key dependencies are the Background Intelligent Transfer Service (BITS), the Cryptographic Services, and the Remote Procedure Call service. If BITS or Cryptographic Services fail to start, Windows Update cannot function. The Services console shows the dependency tree, and repairing those underlying services usually restores Windows Update automatically."
  - q: "Can a virus disable the Windows Update service?"
    a: "Yes, some malware deliberately disables Windows Update to prevent security patches from removing it. If the service will not stay running and you find unfamiliar programs or browser redirects, run a full scan with Windows Security and then a second-opinion scan. Clean the infection first, because repairing the service on an infected machine rarely holds."
---

When the Windows Update service refuses to run, everything downstream breaks at once: no update checks, no downloads, no installs, and a collection of vague error codes that all trace back to one silent service. You click Check for updates and get an error instead of a scan. The troubleshooter may even tell you the service is not running, as if that were news.

The service itself is rarely the real problem. It stops because something it depends on is broken, because its configuration is corrupted, or because outside software is interfering. Fixing it means working outward from the service to its dependencies, its data stores, and the system around it. This guide does exactly that, in dependency order.

## Why this happens

- **Corrupted service registration:** The service's registry entries are damaged, so it cannot start or stops immediately.
- **Failed dependency service:** BITS or Cryptographic Services will not run, and Windows Update cannot function without them.
- **Corrupted SoftwareDistribution database:** The local update data store is damaged, crashing the service when it tries to read it.
- **Third-party interference:** System optimizers, aggressive antivirus, or malware disable or break the service deliberately.
- **Broken permissions:** The service account lost the file or registry permissions it needs to operate.
- **Pending update corruption:** A half-applied update left the servicing stack in a state the service cannot initialize.
- **Group policy restrictions:** A policy disables the service or blocks update behavior, common on ex-corporate laptops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Start the service manually and watch what happens

1. Press **Win + R**, type `services.msc`, and find **Windows Update** in the list.
2. Double-click it, set **Startup type** to **Manual**, and click **Start**. Note exactly what happens: does it start cleanly, throw an error, or start and then stop?
3. An immediate error code like 1053 or 1083 points at dependencies or registration. Starting then stopping points at data corruption.
4. Write down the behavior. This thirty-second test directs everything that follows, so do not skip it.

### Fix 2: Check and repair the dependency services

1. In the Windows Update properties window, open the **Dependencies** tab and note the listed services.
2. In the Services list, verify **Background Intelligent Transfer Service** and **Cryptographic Services** are running. Start any that are stopped.
3. Set BITS startup type to **Manual** and Cryptographic Services to **Automatic**, which are their healthy defaults.
4. Try starting Windows Update again. When a dependency was the blocker, the service now starts cleanly. Microsoft documents these relationships on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 3: Reset the SoftwareDistribution data store

1. In an admin Command Prompt, run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`. This removes the corrupted database that may be crashing the service on startup.
3. Restart the services with `net start wuauserv`, `net start cryptSvc`, `net start bits`, and `net start msiserver`.
4. Open **Settings > Windows Update** and check for updates. The service rebuilds its data store from scratch and usually behaves from here on.

### Fix 4: Re-register the update DLLs

1. If the service still misbehaves, its component registration may be broken. In an admin Command Prompt, re-register the core DLLs one by one.
2. Run `regsvr32 wuapi.dll`, `regsvr32 wuaueng.dll`, `regsvr32 wups.dll`, and `regsvr32 wuwebv.dll`, confirming each success dialog.
3. These commands repair the COM registration that lets the service load its own components.
4. Restart the laptop and test the service again. This fix targets the exact failure where the service starts and immediately stops.

### Fix 5: Scan for malware and remove interfering software

1. Run a full scan with **Windows Security > Virus & threat protection > Scan options > Full scan**.
2. Uninstall any third-party system optimizers, driver updaters, or aggressive antivirus suites that might be disabling the service.
3. Check **Task Scheduler** for unfamiliar tasks that stop services, and check the Services list for unknown entries set to Disabled that relate to updating.
4. After cleaning, repeat Fix 3 to give the service a fresh data store on a clean system. A repaired service on an infected machine will break again.

### Fix 6: Check group policy and registry locks

1. Run `gpedit.msc` and navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update**. Set any configured policies back to **Not Configured** unless you know they are intentional.
2. In the registry, check `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` for forced settings like a disabled service or a dead WSUS server.
3. Ex-corporate or refurbished laptops often carry these policies long after leaving the company network.
4. Remove or correct the policies, restart, and verify the service starts. For the prioritized repair sequence once the service runs, see the [best-way service fix guide](/articles/best-way-to-fix-windows-update-service-not-running/).

### Fix 7: Repair system files and reset the pipeline

1. Run `sfc /scannow` in an admin Command Prompt to repair protected system files the service depends on.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store. This command downloads healthy replacements from Windows Update, so keep the machine online while it runs.
3. As a final measure, download the standalone servicing stack update for your build from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install it manually. The servicing stack is the foundation the update service builds on, and refreshing it resolves failures that survive every other repair.
4. Restart and confirm the service starts and stays running, then run a full update check. If individual updates now fail, the [cumulative update troubleshooting](/articles/cumulative-update-fails-to-install-troubleshooting/) picks up from here.

## Closing

A non-running Windows Update service is a symptom of dependency failure, data corruption, or outside interference, not a mystery. Start it manually to observe the failure, repair the dependencies, reset the data store, and clear policy locks. Worked in this order, the service comes back and stays back.
