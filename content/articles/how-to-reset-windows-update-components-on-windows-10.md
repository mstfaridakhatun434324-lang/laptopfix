---
title: "How to Reset Windows Update Components on Windows 10"
slug: how-to-reset-windows-update-components-on-windows-10
date: 2026-09-22
categories: ["windows-update"]
tags: ["reset", "windows update", "components", "windows 10", "softwaredistribution"]
description: "Windows 10 updates stuck or failing? Reset the update components with the correct Windows 10 procedure — commands, script, and verification."
thumbnail: "/images/thumbs/how-to-reset-windows-update-components-on-windows-10.webp"
faqs:
  - q: "Does the Windows 10 reset procedure differ from Windows 11?"
    a: "The core is identical: stop the same four services, rename SoftwareDistribution and catroot2, clear BITS, restart. Differences are cosmetic — Windows 10 uses the classic Control Panel troubleshooters and 'Settings → Update & Security' paths instead of Windows 11's reorganized Settings. The commands themselves are the same."
  - q: "Will resetting components delete my installed Windows 10 updates?"
    a: "No. Installed updates stay installed and remain in Update history. The reset only clears pending downloads, the download cache, and local history display data. Your patch level doesn't move backward — you're cleaning the workshop, not uninstalling anything. If you need the old history for your records, screenshot it before resetting."
  - q: "Should I use the automated troubleshooter or the manual reset on Windows 10?"
    a: "Always try the automated route first: Settings → Update & Security → Troubleshoot → Additional troubleshooters → Windows Update. It's faster and fixes the common cases. Use the manual command-line reset when the troubleshooter fails, the same error returns, or corruption is clearly deep (repeated identical failures)."
  - q: "How often is it safe to reset Windows Update components?"
    a: "As often as needed — the operation is non-destructive. That said, if you're resetting monthly, something upstream is wrong (failing drive, bad RAM corrupting downloads, aggressive antivirus). Treat frequent resets as a symptom to investigate, not a maintenance routine. Two resets a year for genuine stalls is normal; two a month is a red flag pointing at deeper trouble."
---

Windows 10's update machinery is the same battle-tested stack Windows 11 inherited — and it corrupts in the same ways: wedged downloads, poisoned caches, stuck services, cryptic error codes that survive reboots. The component reset is the definitive fix for all of it, and on Windows 10 the procedure is essentially the same as its newer sibling, with Windows 10's own Settings paths. The procedure below is the same one Microsoft support engineers run, adapted to Windows 10's menus and service names.

If you've already read the Windows 11 version of this procedure, the commands below will look familiar — that's intentional. The value here is the Windows 10-specific navigation (Update & Security, the classic troubleshooters) and the Windows 10 quirks worth knowing, like the older servicing stack behaviors on long-unpatched machines. The Windows 11 guide is at [reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/).

Budget 15 minutes, an administrator Command Prompt, and AC power. Let's rebuild the update stack properly. On machines that have not been serviced in months, expect the first post-reset update pass to be large — that is backlog, not a problem.

## Why this happens

- **Corrupted SoftwareDistribution cache**: Partial downloads and bad manifests — the reset's main target, same as Windows 11. The .old rename keeps your undo option until the reset proves itself.
- **Damaged catroot2 signature catalogs**: Corrupt catalogs fail verification of legitimate updates. Fresh catalogs rebuild automatically on the next update check.
- **Stuck BITS queue**: Dead transfer jobs clogging the background service. The bitsadmin reset clears the queue state that folder renames do not touch.
- **Wedged wuauserv/cryptSvc states**: Services half-started after failed updates or bad shutdowns. All four services must be stopped before renaming — in-use folders will not rename.
- **Stale pending markers**: Interrupted updates leaving flags that block new operations. One interrupted update can poison every subsequent attempt until cleared.
- **Corrupted DataStore.edb**: The update database breaking every scan identically. It is a rebuildable cache — the next scan regenerates it from scratch.
- **Years of layered failed attempts**: Old Windows 10 machines accumulate compound bad state across many Patch Tuesdays. If you are resetting monthly, investigate the drive and RAM — frequent corruption has a hardware cause.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Run the Windows 10 troubleshooter first

The automated pass fixes the easy cases in minutes. The automated pass fixes the easy cases in minutes.

1. Settings → **Update & Security** → **Troubleshoot** → **Additional troubleshooters**.
2. Select **Windows Update** → Run the troubleshooter; apply all recommended fixes.
3. Restart when prompted, then test with **Check for updates**.
4. Only proceed to the manual reset if problems persist — don't skip the easy win.
5. Run it with nothing else heavy going — the troubleshooter's service restarts conflict with active installs.

### Fix 2: Fix 2: Stop the four update services

Identical to Windows 11 — services must be down before folder renames. Identical to Windows 11 — services must be down before folder renames.

1. Right-click Start → **Command Prompt (Admin)** or Windows PowerShell (Admin).
2. Run: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Verify each reports stopped; retry once after 60 seconds if one hangs.
4. All four down before continuing — no exceptions.
5. On Windows 10, also stop the Delivery Optimization service (DoSvc) if it exists — it can hold handles on the Download folder.

### Fix 3: Fix 3: Rename SoftwareDistribution and catroot2

Rename preserves your undo option; the .old folders stay until you delete them. Rename preserves your undo option; the .old folders stay until you delete them.

1. `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
2. `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Confirm with `dir C:\Windows` — both .old entries should be listed.
4. 'Access denied' means a service is still running — back to Fix 2.
5. Windows 10 rebuilds these folders slightly slower than 11 — allow extra time on the first post-reset check.

### Fix 4: Fix 4: Clear BITS jobs and reset Winsock

The transfer-layer state that folder renames don't touch. The transfer-layer state that folder renames do not touch.

1. `bitsadmin /reset /allusers` — clears every queued BITS job.
2. `netsh winsock reset` — resets the network socket catalog (needs the reboot in Fix 5).
3. On very old Windows 10 builds, also re-register update DLLs per Microsoft's legacy guidance — modern builds don't need this.
4. These two commands resolve the 'reset didn't help' cases where the queue was the real culprit.
5. Microsoft's [update fix guidance](https://support.microsoft.com/en-us/windows) confirms this BITS-and-Winsock step for stubborn cases.

### Fix 5: Fix 5: Restart services and reboot

Bring the stack back up cleanly. Bring the stack back up cleanly.

1. `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
2. Confirm all four start successfully.
3. Restart the laptop (applies the Winsock reset).
4. After boot, verify in `services.msc` that Windows Update is set to Manual/running properly.
5. Verify in services.msc that startup types are correct — some tools set Windows Update to Disabled and forget to restore it.

### Fix 6: Fix 6: Run a clean update check and verify

The first post-reset scan rebuilds the datastore — let it finish. The first post-reset scan rebuilds the datastore — let it finish.

1. Settings → Update & Security → Windows Update → **Check for updates**.
2. Allow 10–20 minutes for the initial scan; then install everything offered.
3. Reboot as prompted; confirm Update history shows successes.
4. Identical error returning means non-cache causes — check servicing stack updates, disk space, and drivers next.
5. If the scan finds nothing for 20 minutes, that is normal on old machines — the catalog comparison is slow, not stuck.

### Fix 7: Fix 7: Save a reusable reset script

You'll use this again — make it one click. You will use this again — make it one click.

1. Open Notepad, paste the stop/rename/start command sequence from Fixes 2–5.
2. Save as `ResetWU.bat` on your desktop (or a tools folder).
3. Right-click → **Run as administrator** whenever updates wedge in the future.
4. After a week of healthy updating, delete the .old folders to reclaim space.
5. Store the script outside the desktop — a dedicated tools folder survives desktop cleanups.

## Closing

Windows 10's component reset is the same proven sequence as Windows 11's: stop four services, rename two folders, clear BITS, restart everything. Keep the troubleshooter as your first try, the manual reset as your heavy fix, and the saved .bat as your permanent shortcut. Corrupted update state doesn't stand a chance. Old Windows 10 machines reward this maintenance most: years of layered update state compress into one clean rebuild, and the saved script turns future stalls into a two-minute task. Related guides: [reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/) and [stop an update in progress on Windows 10](/articles/how-to-stop-windows-update-in-progress-on-windows-10/).
