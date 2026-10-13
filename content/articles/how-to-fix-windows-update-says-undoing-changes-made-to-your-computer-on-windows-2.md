---
title: "Windows 10 'Undoing Changes Made to Your Computer': Fix the Update Loop"
slug: how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-windows-2
date: 2026-10-12
categories: ["windows-update"]
tags: ["undoing changes windows 10", "windows 10 update failed", "undoing changes", "update rollback", "windows 10"]
description: "Stuck on 'Undoing changes made to your computer' in Windows 10? Fix the rollback loop with these Windows 10-specific steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-windows-2.webp"
faqs:
  - q: "Is Windows 10 still getting updates that can cause this?"
    a: "Yes — Windows 10 continues receiving monthly security updates, and those cumulative updates can fail and roll back exactly like on Windows 11. The servicing stack, update cache, and driver-migration mechanics are the same. Every fix in this guide applies to the current Windows 10 update pipeline."
  - q: "Should I just upgrade to Windows 11 instead of fixing this?"
    a: "If your hardware qualifies and you have been considering it, a persistent update loop is a reasonable nudge — the in-place upgrade to Windows 11 also repairs the broken update state as a side effect. But do not upgrade to escape diagnosis: fix the trigger first, or the same driver or corruption issue can follow you to Windows 11."
  - q: "Does the Windows 10 troubleshooter actually help here?"
    a: "More often than its reputation suggests. The Windows Update troubleshooter on Windows 10 resets the update services, re-registers DLLs, and clears common stuck states — it resolves the simple cache/service cases in minutes. Run it first; it costs nothing and works often enough to earn the first slot."
  - q: "Can I block a specific update that keeps failing on Windows 10?"
    a: "Yes, with the official 'Show or hide updates' troubleshooter (wushowhide) from Microsoft, which lets you hide a specific KB so Windows stops offering it. Use this for a genuinely problematic update while you fix the underlying cause — not as a permanent strategy, since hiding security updates indefinitely leaves you exposed."
---

Windows 10 may be the older sibling, but its update engine fails in exactly the same way: an update does not complete, the PC announces **"Undoing changes made to your computer,"** and you wait — sometimes through a loop that repeats every month. The mechanics (update cache, servicing stack, driver migration) are shared with Windows 11, but the tools and menus have Windows 10 specifics worth getting right.

This guide is written for Windows 10 paths: the classic Control Panel troubleshooters, the wushowhide tool for blocking bad updates, and the servicing commands as they behave on Windows 10. The fix order mirrors the Windows 11 guides — escape, classify, clear, repair — with the Windows 10 details filled in.

If you are on Windows 11, use the [Windows 11 complete undoing-changes guide](/articles/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-windows/) instead; the steps overlap but the menus differ. The core diagnostic — read the error code first — is identical on both.

## Why this happens

- **Corrupted update cache:** Damaged downloads in SoftwareDistribution failing integrity checks.
- **Servicing stack corruption:** Damaged component store failing every cumulative update identically.
- **Driver migration failures:** Old drivers (especially storage and chipset) that the update cannot migrate.
- **Disk space exhaustion:** Small-SSD Windows 10 machines hitting the update space wall.
- **Stuck update services:** wuauserv or BITS wedged, poisoning every attempt.
- **Third-party antivirus interference:** Legacy AV products intercepting update file operations.
- **A specifically bad KB:** Occasionally Microsoft ships an update with a genuine defect affecting certain hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Escape the rollback and note the code

Same rule as Windows 11: under two hours, wait plugged in; past three hours with no activity, force off and reboot. At the desktop, open Settings → Update & Security → Windows Update → View update history, expand the failed update, and copy the KB number and error code. On Windows 10 the history page shows the same code families — 0xC1900101 (drivers), 0x800F0922 (servicing), 0x80070070 (space) — and the code picks your fix.

1. Wait out rollbacks under two hours; force only the truly stuck.
2. Open View update history; expand the failed entry.
3. Copy the KB number and full error code.
4. Classify: driver / servicing / space / download / bad KB.

### Fix 2: Run the Windows 10 update troubleshooter

Settings → Update & Security → Troubleshoot → Additional troubleshooters → Windows Update → Run the troubleshooter. On Windows 10 this tool is relatively thorough: it restarts services, re-registers update DLLs, and repairs common stuck states. Apply everything it suggests, restart, and check for updates. It resolves the simple service/cache cases outright — always worth the three minutes before manual surgery.

1. Run the Windows Update troubleshooter; apply all fixes.
2. Restart the PC.
3. Check for updates and note the result.
4. If it fails again, proceed — you have ruled out the simple cases.

### Fix 3: Reset the update components manually

The thorough Windows 10 reset: stop the wuauserv, cryptSvc, BITS, and msiserver services; rename `C:\Windows\SoftwareDistribution` to SoftwareDistribution.old and `C:\Windows\System32\catroot2` to catroot2.old; restart the services. This discards the entire local update state — cache, history, pending operations — and forces Windows to rebuild it cleanly. It is the definitive fix for corrupted-cache and wedged-service failures.

1. Stop wuauserv, cryptSvc, BITS, and msiserver (admin prompt: `net stop`).
2. Rename SoftwareDistribution and catroot2 folders to .old.
3. Restart the four services (`net start`).
4. Check for updates; the re-download starts fresh.

### Fix 4: Repair servicing and free disk space

Elevated Command Prompt: `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`. On Windows 10 these behave the same as Windows 11 and fix the same corruption family. Pair with Disk Cleanup (clean up system files) to secure 20 GB+ free — Windows 10 machines tend to be older with smaller SSDs, so space is a more common trigger here than on new Windows 11 laptops. Microsoft documents the servicing tools in [Windows support](https://support.microsoft.com/en-us/windows).

1. Run elevated DISM restore-health, then SFC.
2. Run Disk Cleanup → Clean up system files; target old installations.
3. Confirm 20 GB+ free on C:.
4. Retry the update once.

### Fix 5: Update drivers and hide the bad KB if needed

For driver-family codes, update chipset, storage, and graphics drivers from your laptop maker. If one specific KB fails repeatedly while others succeed, use Microsoft wushowhide troubleshooter to hide that KB — stopping the monthly retry loop while you wait for a revised update or fix the underlying driver. Hiding is a pause button, not a solution: revisit it after the next driver update, and never hide security updates indefinitely.

1. Update maker drivers for driver-family error codes.
2. If one KB always fails: run wushowhide and hide it.
3. Fix the underlying driver issue in the meantime.
4. Unhide and retry after the next driver/update cycle.

### Fix 6: Install the update manually from the catalog

Download the failing KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install the .msu by hand. On Windows 10, manual installs are especially useful because they bypass the older automatic pipeline quirks. If the manual install succeeds, the delivery mechanism was at fault; if it fails identically, your system state needs the repair in the next step.

1. Get the KB number from update history.
2. Download the .msu from the Update Catalog.
3. Install manually; record the exact outcome.
4. Identical failure: proceed to repair install.

### Fix 7: Repair install or upgrade to Windows 11

Two endgame options. A Windows 10 repair install (mount the Windows 10 ISO, run setup, keep files and apps) rebuilds the update engine in place. Or, if the hardware qualifies, upgrade to Windows 11 via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — the upgrade repairs the broken update state as a side effect and moves you to the supported platform. Either way: back up first, stay plugged in, and verify the failing update installs afterward.

1. Back up personal files.
2. Option A: Windows 10 ISO → setup → keep files and apps.
3. Option B: upgrade to Windows 11 if hardware qualifies.
4. Verify the previously failing update now completes.

## Closing

Windows 10 rollback loops yield to the same discipline as Windows 11: escape safely, read the code, run the troubleshooter, reset the update components, repair servicing, update drivers, hide only the truly bad KB temporarily, and finish with a repair install or the Windows 11 upgrade. The update engine is fixable — and staying on working updates matters more with every passing month. If the failure message names the update explicitly, the [could-not-complete repair guide](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-after-windows-11-upd/) covers the error-code families in depth.
