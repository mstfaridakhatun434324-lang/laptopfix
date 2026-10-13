---
title: "The Best Way to Fix the Windows Update Service When It Won't Run"
slug: best-way-to-fix-windows-update-service-not-running
date: 2026-10-03
categories: ["windows-update"]
tags: ["update service fix", "wuauserv repair", "windows update", "best fix"]
description: "Skip the guesswork: this ranked guide gives you the most effective fixes first for a Windows Update service that refuses to run."
thumbnail: "/images/thumbs/best-way-to-fix-windows-update-service-not-running.webp"
faqs:
  - q: "What is the fastest fix when the Windows Update service will not start?"
    a: "The fastest reliable fix is resetting the update cache: stop the update services, rename the SoftwareDistribution folder, and restart the services. This takes about two minutes and resolves the majority of cases because a corrupted local database is the most common reason the service fails. If it does not work, the dependency and re-registration repairs below take only a few minutes more."
  - q: "Why do generic guides fail to fix the update service?"
    a: "Because they treat every case identically, usually with a single troubleshooter run. The service fails for several distinct reasons: dead dependencies, corrupted data stores, broken registration, malware, and policy locks. The best approach matches the fix to the cause, which is why this guide orders fixes by both effectiveness and diagnostic value instead of offering one magic step."
  - q: "Do I need to reinstall Windows to fix the update service?"
    a: "Almost never. The service and its supporting components are fully repairable with built-in tools: cache resets, DLL re-registration, SFC, and DISM. Reinstallation is only worth considering if the servicing stack itself is destroyed beyond DISM repair, which is rare. Work through the ranked fixes here first; reinstallation is the last resort, not the plan."
  - q: "How do I stop the problem from coming back?"
    a: "Remove the root cause, not just the symptom. Uninstall aggressive system optimizers that disable services, keep real antivirus protection instead of sketchy cleaners, and let Windows Update run on its schedule rather than blocking it for months. A machine that updates regularly almost never develops the corruption that kills the service in the first place."
---

Most guides for a dead Windows Update service give you one generic step and wish you luck. That wastes your time when the cause is one of five different things. The best way to fix the service is to work a ranked list: the highest-probability, lowest-effort repairs first, the structural repairs next, and the deep system repairs only if needed.

This is the effectiveness-ranked companion to pure diagnostics. Every fix below earns its position from how often it actually resolves the problem on real laptops. Start at the top and stop when the service stays running.

## Why this happens

- **Corrupted update database:** The most common cause by far. The SoftwareDistribution store breaks and the service cannot initialize against it.
- **Dead dependency:** BITS or Cryptographic Services failed, taking Windows Update down with them.
- **Broken COM registration:** The service's own DLLs lost their registration, so it cannot load its components.
- **Malware or optimizer damage:** Outside software disabled or corrupted the service deliberately or carelessly.
- **Policy locks:** Group policy or registry settings force the service off, common on secondhand business laptops.
- **Servicing stack corruption:** Deep damage that cache resets cannot reach, requiring DISM-level repair.
- **Permission damage:** The service account lost access to files or registry keys it needs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset the update cache (highest success rate)

1. Open an admin Command Prompt. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`, waiting for each to confirm.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`. Renaming preserves a fallback instead of deleting evidence.
3. Restart the services with `net start wuauserv`, `net start cryptSvc`, `net start bits`, and `net start msiserver`.
4. Open **Settings > Windows Update** and check for updates. This two-minute repair resolves more dead-service cases than everything else combined.

### Fix 2: Start the dependencies in the right order

1. Open `services.msc` and confirm **Background Intelligent Transfer Service** and **Cryptographic Services** are running.
2. If BITS will not start, check its own dependency, the **Remote Procedure Call** service, which should always be running.
3. Set BITS to **Manual** and Cryptographic Services to **Automatic**, then start Windows Update.
4. Services fail in chains, so fixing the bottom link restores the top. Microsoft documents this chain on the [Windows support hub](https://support.microsoft.com/en-us/windows). Test the full chain by running a manual update check after each dependency is repaired.

### Fix 3: Re-register the service components

1. In an admin Command Prompt, run `regsvr32 wuapi.dll`, `regsvr32 wuaueng.dll`, `regsvr32 wups.dll`, and `regsvr32 wuwebv.dll`.
2. Confirm each success dialog. If one fails, note which, since it identifies the damaged component. A failure on wuaueng.dll specifically points at the engine itself and usually needs the DISM repair in Fix 7 as well.
3. These registrations repair the COM plumbing the service uses to load its own code. Corruption here is common after failed updates that were interrupted mid-install.
4. Restart the laptop and verify the service starts and stays running for at least five minutes. Check the Services console twice, a few minutes apart, since some registration faults only crash the service under load.

### Fix 4: Run the update troubleshooter for automated repairs

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Windows Update**.
2. The troubleshooter applies a bundle of small repairs: service states, missing registrations, and pending operations.
3. It works best after the manual cache reset above, catching whatever that left behind.
4. Restart after it completes and test. If the troubleshooter reports it could not fix everything, continue down this list rather than rerunning it.

### Fix 5: Remove software that kills the service

1. Uninstall third-party system optimizers, registry cleaners, and driver updater tools. These are notorious for disabling services they consider unnecessary, and they rarely ask permission first.
2. Run a full scan with Windows Security to rule out malware that disables updating to protect itself. Some infections specifically target wuauserv to block the patches that would remove them.
3. Check **Task Scheduler** for tasks that stop the wuauserv service on a schedule. Look under Task Scheduler Library for entries from optimizer or tuning software you may have forgotten about.
4. After cleanup, repeat the Fix 1 cache reset so the service restarts on a clean system. For the diagnostic version of this repair, see the [service troubleshooting guide](/articles/windows-update-service-not-running-troubleshooting/).

### Fix 6: Clear policy and registry locks

1. Run `gpedit.msc`, go to **Computer Configuration > Administrative Templates > Windows Components > Windows Update**, and return configured policies to **Not Configured**.
2. Check the registry at `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` for forced values like a dead WSUS server address.
3. Delete or correct stale policy values, especially on refurbished or ex-corporate machines.
4. Restart and confirm the service now starts normally. Policy locks are invisible in the Services console, which is why this step comes after the obvious repairs.

### Fix 7: Repair the servicing foundation with DISM and SFC

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Command Prompt while connected to the internet.
2. Follow with `sfc /scannow` and restart when both finish.
3. If the service still fails, install the latest servicing stack update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
4. Verify the service runs, then complete a full update check. Should individual updates fail at this point, the [cumulative update guide](/articles/cumulative-update-fails-to-install-troubleshooting/) continues the repair sequence.

## Closing

The best fix for a dead update service is the boring one: reset the cache first, because that is the cause most of the time. Dependencies, registration, interfering software, and policy locks cover nearly everything else. Ranked this way, you spend minutes on the likely causes instead of hours on the exotic ones. Once the service is healthy, let updates install on schedule so the corruption never gets a chance to build up again.
