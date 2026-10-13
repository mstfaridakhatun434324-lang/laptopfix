---
title: "How to Reset Windows Update Components on Windows 11 (2026 Guide)"
slug: how-to-reset-windows-update-components-on-windows-11
date: 2026-09-17
categories: ["windows-update"]
tags: ["reset", "windows update", "components", "windows 11", "softwaredistribution"]
description: "The definitive guide to resetting Windows Update components on Windows 11 — manual commands, the automated script, and when a reset is actually the right call."
thumbnail: "/images/thumbs/how-to-reset-windows-update-components-on-windows-11.webp"
faqs:
  - q: "What does resetting Windows Update components actually do?"
    a: "It stops the four update services (Windows Update, BITS, Cryptographic, MSI Installer), renames the SoftwareDistribution and catroot2 working folders so Windows rebuilds them fresh, resets BITS and network queues, and restarts everything. It clears corrupted downloads, stuck queues, and bad manifests without touching your files, apps, or installed updates."
  - q: "Will I lose my update history when I reset components?"
    a: "The Update history page may appear empty afterward because its local records lived in the renamed folders — but no installed update is removed. Your system stays exactly as patched as it was; only the pending downloads and history display reset. New history accumulates from the next check."
  - q: "How is this different from the Windows Update troubleshooter?"
    a: "The troubleshooter is a lightweight automated check that fixes service states, registry flags, and pending markers. A component reset is the heavy version: it physically rebuilds the download cache and cryptographic catalog folders. Run the troubleshooter first; reset components when it doesn't resolve the issue."
  - q: "Can resetting update components cause any harm?"
    a: "Done as documented here, no. The renamed folders (.old) remain on disk until you delete them, so the operation is reversible. The only 'cost' is that Windows re-downloads any pending updates from scratch, which uses bandwidth. Never delete the folders outright before confirming the reset worked."
---

Resetting Windows Update components is the single most powerful general-purpose fix in the Windows troubleshooting arsenal. When updates won't download, won't install, throw cryptic codes, or loop forever, the cause is corrupted state in the update machinery about half the time — and a component reset wipes that state clean and lets Windows rebuild it. It's referenced by nearly every update guide on this site because it works.

But it's also overused. A reset won't fix a missing servicing stack update, a full disk, or a driver conflict — and running it blindly before diagnosing wastes time and bandwidth. This guide covers when a reset is the right call, the full manual procedure done correctly (most online copies skip steps), and a reusable script for the future. The Windows 10 variant lives at [reset Windows Update components on Windows 10](/articles/how-to-reset-windows-update-components-on-windows-10/).

You'll need an administrator Command Prompt and about 15 minutes. Plug in the laptop and close other heavy apps first.

## Why this happens

- **Corrupted SoftwareDistribution cache**: Partial downloads and bad manifests wedge the downloader — the reset's primary target. Renaming (not deleting) the folder keeps an undo path until you are confident.
- **Damaged catroot2 catalog store**: Corrupt signature catalogs make valid updates fail verification. Windows rebuilds these catalogs automatically on the next update check.
- **Stuck BITS transfer queue**: Dead jobs clog the background transfer service the reset restarts. The bitsadmin reset command in Fix 4 clears jobs that survive folder renames.
- **Wedged service states**: Half-started update services that neither run nor stop cleanly. Stopping all four services before renaming folders is what makes the reset actually work.
- **Stale pending-operation markers**: Leftover flags from interrupted updates that block new operations. These markers are why an interrupted update poisons every attempt after it.
- **Corrupted DataStore.edb**: The update database itself can damage, breaking every scan identically. Deleting it is safe — it is a cache, and the next scan rebuilds it from scratch.
- **Post-failure compound state**: Each failed attempt layers new bad state on old — the reset clears all layers at once. This is why the fifth retry without a reset never works but the first retry after one does.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Decide a reset is actually warranted

A reset is heavy artillery — confirm the target first. A reset is heavy artillery — confirm the target first. Microsoft's [update troubleshooting guidance](https://support.microsoft.com/en-us/windows) lists the same symptom-to-cause mapping.

1. Symptoms that warrant it: updates stuck downloading for hours, repeated identical error codes, troubleshooter failing to fix, or failures that began after an interrupted update.
2. Symptoms that don't: single transient error that clears on retry, metered-connection blocks, or 'not applicable' messages (those are eligibility, not corruption).
3. Run the built-in troubleshooter first (Settings → System → Troubleshoot → Other troubleshooters → Windows Update).
4. If it fails or the problem returns within a day, proceed — the reset is justified.
5. If you are unsure, run the troubleshooter twice — the second pass sometimes catches what the first missed.

### Fix 2: Fix 2: Stop the four update services

Services must be stopped before their folders can be renamed — skipping this is the most common botched reset. Services must be stopped before their folders can be renamed — skipping this is the most common botched reset.

1. Open Command Prompt **as administrator** (right-click Start → Terminal (Admin)).
2. Run each: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Confirm each reports stopped successfully; if one hangs, wait 60 seconds and retry once.
4. Don't proceed until all four are stopped — renaming in-use folders fails or corrupts further.
5. If a service refuses to stop, check Task Manager for a hung TiWorker.exe and end it first.

### Fix 3: Fix 3: Rename the SoftwareDistribution and catroot2 folders

Rename, don't delete — the .old folders are your undo button. Rename, do not delete — the .old folders are your undo button.

1. In the same admin prompt, run: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
2. Then: `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Verify both renames succeeded (`dir C:\Windows` should show the .old names).
4. If a rename fails with 'access denied,' a service is still running — return to Fix 2.
5. After renaming, glance at the folder timestamps later — fresh timestamps confirm the rebuild happened.

### Fix 4: Fix 4: Reset BITS and network service state

The step most guides skip. BITS keeps its own queue state that survives folder renames. The step most guides skip. BITS keeps its own queue state that survives folder renames.

1. Still in the admin prompt, run: `bitsadmin /reset /allusers` to clear all BITS jobs.
2. Re-register the update DLLs only if you're on an older build with registration issues (Windows 11 rarely needs this).
3. Reset the network stack's update-relevant state: `netsh winsock reset` (requires reboot after).
4. These clear the transfer-layer state that folder renames alone miss.
5. The winsock reset requires the reboot in Fix 5 — do not skip it or the reset is incomplete.

### Fix 5: Fix 5: Restart the services and verify

Bring the stack back up and confirm it's healthy before updating. Bring the stack back up and confirm it is healthy before updating.

1. Run: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
2. Confirm each starts successfully.
3. Win + R → `services.msc` → verify Windows Update shows **Manual** startup (not Disabled).
4. Restart the laptop to let the winsock reset take effect.
5. If any service fails to start, note the exact error — it points at deeper system damage.

### Fix 6: Fix 6: Run one clean update check

The first post-reset check rebuilds everything — give it room. The first post-reset check rebuilds everything — give it room.

1. Settings → Windows Update → **Check for updates**.
2. Expect the first scan to take longer (10–20 minutes) as the datastore rebuilds.
3. Let all offered updates download and install; reboot as prompted.
4. Verify Update history shows the new successes. If the original error returns identically, the cause wasn't cache corruption — investigate servicing stack, drivers, or disk space next.
5. Resist the urge to retry mid-scan; interrupting the rebuild recreates the corruption you just cleared.

### Fix 7: Fix 7: Clean up the .old folders (after a week)

Don't delete them immediately — keep your undo button until you're sure. Do not delete them immediately — keep your undo button until you are sure.

1. Use the laptop normally for a week; confirm updates keep working.
2. Then delete `C:\Windows\SoftwareDistribution.old` and `C:\Windows\System32\catroot2.old` to reclaim disk space.
3. You'll need admin permission; use File Explorer with UAC approval.
4. Future resets: save the commands from Fixes 2–5 as a .bat file (run as admin) for one-click reuse.
5. Set a calendar reminder for the deletion so the .old folders do not sit consuming gigabytes indefinitely.

## Closing

A proper component reset — four services stopped, both folders renamed, BITS queue cleared, everything restarted — resolves the majority of 'updates are just broken' situations on Windows 11. Use it when the symptoms point at corrupted state, keep the .old folders for a week, and save the command sequence for next time. It's the closest thing Windows troubleshooting has to a reset button that actually works. Related guides: [reset Windows Update components on Windows 10](/articles/how-to-reset-windows-update-components-on-windows-10/) and [Windows Update troubleshooter](/articles/how-to-fix-cumulative-update-fails-to-install-reddit/).
