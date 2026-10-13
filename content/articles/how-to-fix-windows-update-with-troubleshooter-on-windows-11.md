---
title: "How to Fix Windows Update With the Troubleshooter on Windows 11"
slug: how-to-fix-windows-update-with-troubleshooter-on-windows-11
date: 2026-10-12
categories: ["windows-update"]
tags: ["troubleshooter", "windows update", "windows 11", "automatic fix", "repair"]
description: "Learn to use the Windows Update troubleshooter on Windows 11 properly: what it fixes, what it misses, and the manual steps to take when it is not enough."
thumbnail: "/images/thumbs/how-to-fix-windows-update-with-troubleshooter-on-windows-11.webp"
faqs:
  - q: "What does the Windows Update troubleshooter actually fix?"
    a: "It automates the standard repair sequence: restarting the Windows Update, BITS, and cryptographic services, resetting their configurations, clearing corrupted download cache data, re-registering update DLLs, and checking for pending restart blockers. It applies the fixes it finds without asking, then reports what it changed. For common stuck-update and failed-download problems, it resolves the issue outright in a few minutes."
  - q: "Where is the troubleshooter in Windows 11?"
    a: "Go to Settings > System > Troubleshoot > Other troubleshooters, then click Run next to Windows Update. On older 24H2 builds the path may appear under Settings > Update & Security > Troubleshoot instead. The troubleshooter runs as a guided wizard — it needs administrator approval to apply its deeper fixes, so approve the elevation prompt when it appears."
  - q: "What should I do when the troubleshooter cannot fix the problem?"
    a: "Treat its report as a diagnosis, not a dead end. Note exactly what it says it could not fix, then proceed manually: reset the update cache by renaming SoftwareDistribution, run DISM and SFC for image damage, update drivers, and check disk space. The troubleshooter handles the common cases; the manual sequence in this guide handles everything it misses."
  - q: "Is the troubleshooter safe to run repeatedly?"
    a: "Yes. It only resets update-related services and caches to known-good states — it does not touch personal files, installed programs, or settings. Running it multiple times is harmless, though if three runs have not helped, the cause lies outside what it covers and you should move to the manual repairs rather than running it a fourth time."
---

Buried in Windows 11's Settings is a tool most people never open until something breaks: the Windows Update troubleshooter. It is not glamorous, but it automates the exact service resets, cache clears, and re-registrations that technicians perform by hand — and for the most common update problems, it fixes them in minutes with no command line required.
The troubleshooter has limits, though, and knowing them is what separates a quick fix from a wasted afternoon. It handles service states and cache corruption well; it does not repair a damaged component store, fix broken permissions, update your drivers, or free your disk space. This guide shows you how to run it properly, how to read its report, and exactly which manual steps to take for everything it leaves behind.
Run the troubleshooter first — it is the fastest path when it works. If your update problem involves a stuck rollback, the [undoing-changes best-practice guide](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/) is the companion repair, and the [stuck-on-restarting guide](/articles/how-to-fix-windows-update-stuck-on-restarting-on-windows-11/) covers the boot-side variant. Microsoft's own [support documentation](https://support.microsoft.com/en-us/windows) describes the troubleshooter's current capabilities.

## Why this happens

- **Update services are stuck or misconfigured.** The troubleshooter's primary target: services in bad states.
- **The download cache is corrupted.** Damaged SoftwareDistribution data is the second most common automated fix.
- **Update DLLs are unregistered.** Broken COM registrations silently disable update functionality.
- **A pending restart blocks new updates.** Queued operations the troubleshooter detects and clears.
- **The troubleshooter cannot repair image damage.** Corrupted WinSxS stores are outside its scope.
- **It cannot fix permissions.** Access-denied failures need manual ACL repair.
- **It cannot update drivers or free space.** Environmental causes require your hands, not the wizard.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the troubleshooter correctly

The troubleshooter only helps if it runs with the right privileges and on a settled system. Set it up for success.

1. Save your work and close unnecessary applications.
2. Go to Settings > System > Troubleshoot > Other troubleshooters.
3. Click Run next to Windows Update and approve the administrator elevation prompt.
4. Let it complete fully — do not cancel it mid-scan even if it looks idle.

### Fix 2: Read the report and apply its fixes

The report tells you what was broken and what was fixed. Read it instead of just closing the window.

1. Review each item the troubleshooter lists as fixed — typically service restarts and cache resets.
2. Note anything it reports as 'could not fix' — that is your manual repair list.
3. Restart the laptop after the troubleshooter applies its fixes.
4. Check for updates to test whether the problem is resolved.

### Fix 3: Manually reset the update cache

When the troubleshooter's cache handling is insufficient, the full manual reset goes deeper.

1. In an elevated Command Prompt, run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands and reboot.
4. Check for updates on the fully fresh cache.

### Fix 4: Repair the component store

Image damage is the most common cause the troubleshooter cannot touch. DISM handles it.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`, allowing 15 to 30 minutes.
3. Follow with `sfc /scannow` to verify system files.
4. Restart, then run the troubleshooter once more — it often succeeds on the repaired image.

### Fix 5: Fix permissions for access-denied failures

If updates fail with 0x80070005 after the troubleshooter, broken ACLs are the cause it cannot repair.

1. Confirm the 0x80070005 code in the update history.
2. Rebuild the update folders via the cache reset above, which restores correct ownership.
3. Check the Security tab on C:\Windows\SoftwareDistribution for SYSTEM and Administrators Full control.
4. Temporarily disable third-party antivirus during the retry to rule out access blocks.

### Fix 6: Address environmental causes

The troubleshooter never touches drivers, space, or firmware. Handle these yourself.

1. Verify at least 20 GB free on C: via Settings > System > Storage.
2. Update display, storage, and network drivers from the manufacturer's support site.
3. Check for a BIOS update if cumulative updates keep failing.
4. Check [HP's support site](https://support.hp.com/us-en) or your vendor's equivalent for model-specific driver packs.

### Fix 7: Escalate to manual or in-place repair

When the troubleshooter plus all manual steps still fail, the servicing stack needs heavier repair.

1. Note the exact error code from the update history for targeted research.
2. Download the failing update's standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it directly.
3. If that fails, perform an in-place upgrade with a mounted Windows 11 ISO, keeping files and apps.
4. This final path resolves virtually all update failures the troubleshooter cannot.

### Fix 8: Make the troubleshooter part of your update routine

The troubleshooter works best as prevention, not just cure. Running it proactively catches the small corruptions before they become failed updates.

1. Run the Windows Update troubleshooter once a quarter, even when updates seem fine.
2. Run it immediately after any interrupted update — power loss, forced shutdown, or cancelled install.
3. After it reports fixes, always reboot before the next update attempt so the repairs take effect.
4. Pair it with a quick disk-space check; the two together prevent the majority of routine update failures.

## Closing

The Windows Update troubleshooter is the right first move: fast, safe, and effective for the common service and cache problems. Its report is equally valuable when it fails — it tells you exactly which manual repairs to perform next. Run it properly, read what it says, then work the manual sequence for everything it leaves behind. Between the wizard and the command line, very few update problems survive.
