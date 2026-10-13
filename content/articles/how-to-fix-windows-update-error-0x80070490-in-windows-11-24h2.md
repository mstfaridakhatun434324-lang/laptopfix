---
title: "How to Fix Windows Update Error 0x80070490 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80070490-in-windows-11-24h2
date: 2026-10-01
categories: ["windows-update"]
tags: ["windows update", "0x80070490", "error code", "windows 11", "element not found"]
description: "Error 0x80070490 (element not found) means the update engine looked for a package or registry entry that is missing. Rebuild the bookkeeping with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070490-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80070490 mean?"
    a: "ELEMENT_NOT_FOUND: the Component-Based Servicing engine went looking for a package, manifest, or registry entry the update expects — and it simply was not there. The update's bookkeeping references something missing, so the install aborts. It usually follows an interrupted update, disk damage, or an overzealous cleanup tool."
  - q: "Should I check the disk before repairing the store?"
    a: "Yes — element-not-found often means files the store expects were damaged on disk, so rule out storage trouble before repairing the OS. Run chkdsk on C: and check Event Viewer afterward for unrecoverable errors. Repairing the component store on top of a failing drive only produces fresh corruption."
  - q: "What are pending servicing operations?"
    a: "When an update stages work for the next reboot, those instructions queue as pending servicing operations. If a previous update's queue never cleared — because of a crash or forced shutdown — the stale entries collide with the new update. Clearing them lets the new installation start from a clean slate."
  - q: "The same update keeps failing after DISM. What now?"
    a: "Install the KB manually from the Microsoft Update Catalog, which bypasses the broken automatic pipeline entirely. If even the manual install fails, consider uninstalling the problematic update and starting fresh. When nothing clears it, an in-place upgrade rebuilds the servicing stack wholesale."
---

The message says "element not found," and it loves to strike a cumulative update at the worst possible point — typically once the download has finished, right when installation should start. In plain terms, the servicing engine reached for a package manifest or a registry entry the update depends on — and grasped at empty air.

A missing element always has a backstory. Maybe a previous update left its metadata half-written when power failed. Perhaps a disk fault quietly devoured servicing files. Perhaps a cleanup utility erased WinSxS content or CBS records Windows still referenced. Or the package arrived truncated — passing its first check, then failing once a referenced element came up missing.

Here is the encouraging part: damaged bookkeeping can almost always be rebuilt without touching your files. The repairs below run from identifying the culprit update to rebuilding the store itself, in escalating order — the last two are rarely needed, and each step tells you whether to continue.

## Why this happens

- **Manifests in the store are unreadable.** When the engine cannot locate a package manifest the update requires, it aborts the install.
- **A previous install left the metadata half-written.** Losing power or forcing a shutdown mid-update strands the store in an inconsistent state.
- **Storage faults ate servicing files.** Failing sectors or a dying SSD around WinSxS quietly destroy metadata that later updates depend on.
- **A cleaner wiped servicing records.** Third-party cleanup tools sometimes erase WinSxS content or CBS entries that Windows still needs.
- **The download arrived truncated.** A package that passed the first validation can still fail later once a missing element is actually referenced.
- **Old pending operations jam the queue.** Unfinished work from a previous update collides with the new install.
- **The COMPONENTS hive is damaged.** Registry data backing the store mirrors package details, and corruption there breaks lookups just the same.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Isolate the failing update first

The repair depends on what is failing — a cumulative update, a driver, or a feature enablement each point somewhere slightly different.

1. In Settings, head to Windows Update > Update history and locate the entry marked Failed with this code.
2. Write down its KB number and type — our [update history guide](/articles/how-to-check-windows-update-history-on-windows-11/) shows how to interpret these entries.
3. If retries keep producing the code, the store wants a full repair — keep going.

### Fix 2: Flush the stuck servicing queue

Unfinished queue entries from a previous update can obstruct the current install — clearing them gives the new update a clean start.

1. From an elevated Command Prompt, run `DISM /Image:C:\ /Cleanup-Image /RevertPendingActions`.
2. If it reports reverted actions, reboot at once.
3. Retry the update from the resulting clean state.

### Fix 3: Rule out disk damage before touching the OS

An element-not-found complaint frequently traces to disk damage underneath the store — fix the storage before the operating system.

1. From the elevated prompt, run `chkdsk C: /f /r` and answer Y to schedule the check.
2. Restart, and the scan will run before Windows loads — on large drives it can take quite a while.
3. Once signed in, open Event Viewer, browse to Windows Logs > Application, and verify the chkdsk entry reports no unrecoverable errors.

### Fix 4: Rebuild the store with DISM, then run SFC

With the disk exonerated, rebuild the bookkeeping itself: DISM fetches the missing manifests from Windows Update, and SFC sweeps protected system files for collateral damage.

1. Let `DISM /Online /Cleanup-Image /RestoreHealth` run to 100 percent, keeping the window open until it finishes.
2. Next, run `sfc /scannow`.
3. Reboot and attempt the failing update again.

### Fix 5: Reset the engine by rebuilding its cache folders

Store damage and engine confusion frequently overlap, so renaming the cache folders forces Windows to reconstruct its download state from scratch.

1. Power down the update services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Archive the stale folders under new names: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Power the services back up: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Run an update check and see if the error is still standing.

### Fix 6: Fetch the KB yourself and install it by hand

When the automatic channel keeps failing with 0x80070490, go around it: every cumulative and servicing-stack update lives on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), and installing by hand bypasses the broken pipeline entirely.

1. Seek the KB number from Fix 1 on the Catalog.
2. Collect the x64 Windows 11 package and launch the `.msu` file.
3. Reboot when asked, then verify the update landed in your history.

### Fix 7: Reinstall Windows when nothing else works

When every targeted repair has failed, the servicing stack is damaged past what piecemeal fixes can reach. Reinstalling Windows 11 24H2 across the existing install — files and apps retained — replaces it wholesale. Fetch the ISO from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11); third-party mirrors are strictly forbidden.

1. Expose the ISO and trigger `setup.exe`.
2. Sanction the license terms and nominate **Keep personal files and apps**.
3. Dedicate 30 to 90 minutes to the installer's several restarts, and never compel a shutdown while it works.
4. Operate Windows Update afterward to confirm the repair held.

## Closing

This code is Windows admitting its update bookkeeping is damaged, and DISM exists precisely to rebuild that bookkeeping. When the identical update fails again after a repair, [install it by hand or uninstall the problematic update](/articles/how-to-uninstall-problematic-update-on-windows-11/) and begin again. For wider update trouble, our [Windows 11 24H2 update error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) maps the related codes, and [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) carries the official documentation.
