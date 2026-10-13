---
title: "Windows Update Troubleshooter Not Working on Windows 11 24H2? Try These Fixes"
slug: how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2
date: 2026-09-28
categories: ["windows-update"]
tags: ["update troubleshooter", "windows 11 24h2", "troubleshoot settings", "update errors"]
description: "The built-in Windows Update troubleshooter won't run or finds nothing on 24H2? Here's why it fails and the manual repairs that work when it doesn't."
thumbnail: "/images/thumbs/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Where is the Windows Update troubleshooter in Windows 11 24H2?"
    a: "Open Settings > System > Troubleshoot > Other troubleshooters, then click Run next to Windows Update. Microsoft has been migrating troubleshooters into the Get Help app in recent 24H2 builds, so if it's missing from Settings, search for Get Help in the Start menu and run the Windows Update troubleshooter from there."
  - q: "Why does the troubleshooter say it couldn't identify the problem?"
    a: "The built-in troubleshooter only checks a narrow set of conditions: the update service state, pending restart flags, and basic connectivity. It can't fix corrupt component stores, broken servicing stacks, or policy conflicts, so a clean bill of health from it doesn't mean your update pipeline is actually fine."
  - q: "The troubleshooter itself crashes or won't launch. What now?"
    a: "A troubleshooter that won't start usually means the diagnostic infrastructure is broken — the Troubleshooting service may be disabled, the Get Help app may be damaged, or system files are corrupt. Run the manual component resets below; they repair the same machinery the troubleshooter relies on."
  - q: "Is there a better alternative to the built-in troubleshooter?"
    a: "Yes. The manual fixes below — resetting the SoftwareDistribution folder, re-registering update DLLs, and running DISM — accomplish far more than the automated tool. Microsoft's own support engineers use these same steps when the troubleshooter fails, and they're the reliable path for stubborn 24H2 update failures."
---

The Windows Update troubleshooter is supposed to be the easy button: click Run, wait a minute, and let Windows diagnose itself. So it's a special kind of frustration when the easy button itself is broken — it crashes on launch, spins forever, or finishes with the useless verdict "couldn't identify the problem" while updates still refuse to install. You're left with a broken updater and a broken repair tool, which feels like being handed a flat tire and a broken jack.

Here's the reassuring part: the troubleshooter is a thin wrapper around a handful of scripted checks. Everything it does, you can do manually — and the manual versions go further. When the troubleshooter fails on Windows 11 24H2, it's almost always because of corrupt update components, a broken diagnostic service, or missing system files. The fixes below repair that underlying machinery directly, which usually fixes both the troubleshooter and the update problem it was supposed to solve.

## Why this happens

- **Corrupt Windows Update components**: Damaged files in the SoftwareDistribution or catroot2 folders break both updates and the tool that checks them.
- **The Diagnostic services are disabled**: The troubleshooter depends on the Diagnostic Policy Service and Diagnostic Service Host — if they're stopped, it can't run.
- **Get Help app is broken or missing**: In 24H2, troubleshooters increasingly live in the Get Help app; a damaged app means no troubleshooter at all.
- **Corrupt system files**: Damage to the servicing stack or shared DLLs that the diagnostic engine loads.
- **Pending operations block diagnosis**: A half-finished update holding locks on files the troubleshooter needs to inspect.
- **Policy restrictions**: Group Policy or MDM settings can disable troubleshooters on managed devices.
- **The troubleshooter's scripts are outdated**: Its checks were written for older failure modes and miss 24H2-specific issues like the new update orchestration service.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run it from the right place in 24H2

Microsoft moved things around. The troubleshooter you remember from Settings may have migrated, and running the current version matters because the old entry point sometimes just fails silently.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. If **Windows Update** is listed, click **Run** and let it complete.
3. If it's missing, open the **Start menu**, search for **Get Help**, and open it.
4. In Get Help, search for "Windows Update troubleshooter" and run it from there.
5. If neither location works, the diagnostic plumbing itself is broken — continue to Fix 2.

### Fix 2: Restart the diagnostic services it depends on

The troubleshooter is useless without its backend services. This is the single most common reason it won't launch at all, and it takes thirty seconds to check.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Diagnostic Policy Service** — set **Startup type** to **Automatic** and click **Start** if it's stopped.
3. Do the same for **Diagnostic Service Host** and **Diagnostic System Host**.
4. Try the troubleshooter again from **Settings > System > Troubleshoot**.
5. If the services refuse to start with an error, note the error code — it usually points at corrupt system files, which Fix 5 addresses.

### Fix 3: Reset the Windows Update components manually

This is what the troubleshooter tries to do and often fails at. Doing it by hand — stopping services, clearing the download caches, restarting — fixes the majority of update failures on 24H2. If the update service itself seems dead, our guide to [the update service not running](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/) goes deeper.

1. Open **Command Prompt as administrator** (search cmd, right-click, Run as administrator).
2. Stop the services:
   - `net stop wuauserv`
   - `net stop bits`
   - `net stop cryptsvc`
   - `net stop msiserver`
3. Rename the cache folders so Windows rebuilds them fresh:
   - `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   - `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services with `net start` for each of the four above.
5. Run **Check for updates** — Windows rebuilds clean caches and retries.

### Fix 4: Repair or reinstall the Get Help app

On 24H2 builds where troubleshooters live in Get Help, a damaged app means every troubleshooter fails. Reinstalling it from the Store restores the whole diagnostic front end.

1. Open **Settings > Apps > Installed apps**.
2. Search for **Get Help**, click the three dots, and choose **Advanced options**.
3. Click **Repair** first and test the troubleshooter.
4. If it still fails, click **Reset** (this clears the app's data).
5. As a last resort, uninstall Get Help and reinstall it from the **Microsoft Store**.
6. Microsoft documents the troubleshooter locations on the [Windows support site](https://support.microsoft.com/en-us/windows) if the UI has moved again in your build.

### Fix 5: Repair corrupt system files with SFC and DISM

When the troubleshooter crashes on launch, the cause is often damaged system files in the servicing stack. SFC and DISM repair exactly that layer.

1. Open **Command Prompt as administrator**.
2. Run `sfc /scannow` and wait for it to finish (10–20 minutes).
3. If it reports unfixable corruption, run:
   - `DISM /Online /Cleanup-Image /RestoreHealth`
4. Wait for DISM to complete — it downloads clean copies from Windows Update, so you need working internet.
5. Restart the laptop and run `sfc /scannow` once more to confirm.
6. Try the troubleshooter again; it should now launch and complete.

### Fix 6: Re-register the update engine DLLs

The troubleshooter and the update service share a set of DLLs. If their registrations are broken — common after a failed cumulative update — re-registering them restores both.

1. Open **Command Prompt as administrator**.
2. Run these one at a time, ignoring any individual errors:
   - `regsvr32 wuapi.dll`
   - `regsvr32 wuaueng.dll`
   - `regsvr32 wups.dll`
   - `regsvr32 wups2.dll`
   - `regsvr32 wuwebv.dll`
   - `regsvr32 qmgr.dll`
3. Restart the laptop.
4. Run the troubleshooter — with fresh registrations it can usually complete its checks.

### Fix 7: Check for policy blocks and run the standalone diagnostic

If you're on a work or school laptop, policy may simply forbid troubleshooters. And if all else fails, Microsoft offers the standalone "Windows Update" diagnostic as a downloadable package.

1. Press **Win + R**, type `gpedit.msc`, and check **Computer Configuration > Administrative Templates > System > Troubleshooting and Diagnostics** for disabled scripted diagnostics.
2. On Home edition (no gpedit), check **Settings > Privacy & security** for any MDM enrollment notice.
3. Download the latest Windows Update troubleshooter package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) by searching "Windows Update troubleshooter".
4. Run the downloaded `.diagcab` file — the standalone version bypasses the broken Settings/Get Help integration.
5. If even the standalone tool fails, the servicing stack needs an in-place repair install (see our [clean install update error guide](/articles/how-to-fix-windows-update-error-after-clean-install-in-windows-11-24h2/) for the repair-install walkthrough).

## Closing

A broken troubleshooter feels like a dead end, but it's really just a sign that the manual path is needed — and the manual path is more thorough anyway. Resetting the update components, repairing system files, and re-registering the update DLLs resolve the vast majority of 24H2 cases where the automated tool gives up. Once updates flow again, the troubleshooter usually starts working too, since both depend on the same healthy machinery underneath.
