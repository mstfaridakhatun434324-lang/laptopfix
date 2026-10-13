---
title: "Cortana Using CPU in Windows 11 24H2? Shut It Down"
slug: how-to-fix-cortana-high-cpu-in-windows-11-24h2
date: 2026-09-23
categories: ["performance"]
tags: ["cortana", "high cpu", "windows 11 24h2", "background process", "disable cortana"]
description: "Cortana still burning CPU in Windows 11 24H2? Learn why the deprecated assistant lingers and how to fully disable it."
thumbnail: "/images/thumbs/how-to-fix-cortana-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "Is Cortana still part of Windows 11 24H2?"
    a: "Not as a supported feature — Microsoft deprecated the Cortana app and ended support for it. What remains on 24H2 systems are leftover components: background tasks, partial AppX packages, and search hooks from the gradual removal. These remnants serve no user-facing purpose, which is why disabling or removing them is safe and has no effect on anything you actually use."
  - q: "Will removing Cortana break Windows Search?"
    a: "No. Modern Windows Search (SearchHost.exe) is a separate component from Cortana, even though they were historically intertwined. Removing the Cortana AppX package does not affect the Start menu search box, file search, or the search indexer. If search misbehaves afterward, it is a SearchHost issue to fix on its own terms — not a Cortana dependency."
  - q: "Why does Cortana come back after updates?"
    a: "Feature updates reinstall a fresh Windows image that can include the Cortana package components again, undoing your removal. The registry policy in Fix 6 (AllowCortana = 0) tells Windows not to enable Cortana, which survives most updates. After each annual feature update, it is worth a quick check in Task Manager to confirm the remnants stayed gone."
  - q: "Does Cortana listen to me if its process is running?"
    a: "The leftover background processes are not actively recording — they are typically crashed-looping or idle maintenance tasks, and voice activation requires explicit permission that is off by default. Still, if the idea bothers you, disabling voice activation (Fix 4) and removing the package (Fix 5) eliminates the components entirely rather than leaving you to trust their idle state."
---

Cortana was deprecated years ago, yet on many Windows 11 24H2 systems its remnants still show up in Task Manager — sometimes idling quietly, sometimes spiking CPU during login or search. Users who never asked for a voice assistant find a Cortana process consuming resources and wonder why it exists at all. It is digital vestigial structure: present, purposeless, occasionally painful.

The leftovers persist because deprecation was gradual: Microsoft removed the app but left background components, search integrations, and scheduled tasks that can still wake up. On 24H2 specifically, some upgrade paths leave the Cortana package in a half-removed state where its background task crashes and restarts in a loop — which is exactly the CPU pattern people report. A crash loop is expensive because every restart repeats the costly initialization.

There is no reason to keep any of it. The steps below disable Cortana's background activity, remove its scheduled tasks, and — for those who want it gone entirely — uninstall the package. For other background CPU drains, see the [Service Host high CPU guide](/articles/how-to-fix-service-host-high-cpu-on-windows-11/). None of these steps affect anything you actually use.

## Why this happens

- **Half-removed Cortana package**: the 24H2 upgrade leaves components that crash-restart in a loop.
- **Background task triggers**: scheduled tasks still wake Cortana processes periodically.
- **Search integration hooks**: leftover search hooks invoke Cortana code paths during queries.
- **Voice activation listening**: voice activation services keep audio pipelines warm.
- **Corrupted package state**: a damaged AppX package retries initialization forever.
- **Startup entries**: Cortana-related entries still launch at boot on some systems.
- **Windows reinstalling it**: feature updates occasionally restore the package.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Cortana is the CPU user

Make sure you are looking at the right process before disabling things. Screenshot the process list during a spike for reference. Note the exact process name — SearchApp, SearchHost, and Cortana are different components with different fixes.

1. Open Task Manager and look for Cortana or SearchUI-related entries during the spike.
2. In the Details tab, verify the process path is a Windows system location.
3. Note when it spikes — at login points to startup entries; during search points to integration hooks.

### Fix 2: Disable Cortana in Settings

The supported toggle stops its background activity. The toggle may be missing on systems where the app is already uninstalled.

1. Open Settings > Apps > Installed apps and search for Cortana.
2. If present, open its Advanced options and set Background apps permissions to Never.
3. Turn off any Let this app run at login option, then end the process in Task Manager.
4. If Cortana reappears after a feature update, repeat the removal — updates sometimes restore the package.

### Fix 3: Remove Cortana's scheduled tasks

Leftover tasks are the most common reason it keeps waking up. Export the task list first if you want a rollback path.

1. Open Task Scheduler (taskschd.msc) and navigate the Microsoft > Windows tree.
2. Find any Cortana-related tasks, right-click each, and choose Disable.
3. Reboot and verify no Cortana process appears in Task Manager.
4. Also check the Task Scheduler Library root for generically named tasks that launch Cortana components.

### Fix 4: Disable voice activation

Voice activation keeps audio and assistant pipelines active in the background. Voice activation is off by default, but upgrades sometimes re-enable it.

1. Open Settings > Privacy & security > Voice activation.
2. Turn off Let apps use voice activation and the Cortana-specific toggle if present.
3. Restart and confirm the related background activity is gone.

### Fix 5: Uninstall the Cortana package

Full removal ends the loop permanently. It is reversible via the Store. The -AllUsers flag matters on shared machines.

1. Open an admin PowerShell and run: Get-AppxPackage -AllUsers *Cortana* | Remove-AppxPackage -AllUsers.
2. If the package resists, try: winget uninstall Cortana.
3. Reboot and confirm Task Manager stays Cortana-free.
4. After removal, check the Store library to make sure it does not show as pending reinstall.

### Fix 6: Block reinstall via registry

Feature updates sometimes restore Cortana. This policy stops that. Group Policy (gpedit.msc) offers the same setting with a friendlier UI on Pro editions. On Home editions without gpedit, the registry method is the only option.

1. Open regedit and go to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search.
2. Create a DWORD named AllowCortana and set it to 0.
3. Reboot; Windows will no longer re-enable Cortana components. See [Microsoft's Windows help](https://support.microsoft.com/en-us/windows) for policy documentation.

### Fix 7: Verify search still works

After removal, confirm you did not break Start menu search. Test both typed queries and voice-free Start menu browsing.

1. Press the Windows key and type a test query.
2. Confirm apps and files appear normally.
3. If search broke, re-register the SearchHost package rather than reinstalling Cortana.
4. Test searching for a Control Panel item and a document to cover both search backends.

### Fix 8: Repair system files to fix the half-removed state

When Cortana's package is half-removed and crash-looping, the underlying cause is often corrupted component store state that SFC and DISM can repair. Fixing the component store lets Windows either complete the removal cleanly or stabilize the remnants, either of which ends the CPU loop.

1. Open an admin Command Prompt and run DISM /Online /Cleanup-Image /RestoreHealth.
2. When it finishes, run sfc /scannow.
3. Reboot and check Task Manager for Cortana activity.
4. If the loop persists, proceed to the package uninstall in Fix 5.

## Closing

Cortana on 24H2 is a ghost — deprecated but not fully exorcised, and on some systems its remnants loop badly enough to cost real CPU. Disable its background permissions, kill its scheduled tasks, and uninstall the package if you want it gone for good. Nothing you actually use depends on it. Exorcise the ghost, and the CPU graph goes quiet. If search itself is the CPU hog rather than Cortana, see [SearchApp high CPU](/articles/how-to-fix-searchapp-exe-high-cpu-step-by-step/).
