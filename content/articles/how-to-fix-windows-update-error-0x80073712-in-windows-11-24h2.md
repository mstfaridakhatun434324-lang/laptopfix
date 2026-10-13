---
title: "How to Fix Windows Update Error 0x80073712 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80073712-in-windows-11-24h2
date: 2026-10-10
categories: ["windows-update"]
tags: ["windows update", "0x80073712", "error code", "windows 11", "component store"]
description: "Error 0x80073712 means the component store index references files that are missing. Rebuild the store with these repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80073712-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80073712 mean?"
    a: "CBS_E_MISSING_PACKAGE_MAPPING: the component store's index lists files that are not actually on disk. When an update reaches for one of those phantom entries, the install fails. It usually traces to a cleanup tool that carved too deeply into WinSxS, a disk fault, or an update that died midway through its own writing."
  - q: "Can a cleanup tool really cause this error?"
    a: "Yes — it is one of the leading causes. The component store's hardlinked structure fools third-party disk cleaners into deleting files that are still referenced elsewhere. Once referenced files go missing, the store's index lies about what exists, and any update needing those files fails with this code."
  - q: "What is DISM RestoreHealth actually doing?"
    a: "It measures every file in the component store against a manifest of healthy versions, then downloads genuine replacements from Windows Update for anything missing or damaged. Think of it as an inventory audit with automatic reordering. On a laptop it normally takes 15 to 30 minutes."
  - q: "Should I worry if the repair stalls at 62 percent?"
    a: "Not necessarily. RestoreHealth can appear frozen for long stretches while it processes large component groups, and slow disk or CPU activity usually explains it. Let it run for at least an hour before intervening. If it genuinely stalls, running DISM cleanup first and then retrying RestoreHealth often gets it moving."
---

Picture a library catalog that lists books which no longer sit on any shelf. Patrons keep asking for them, librarians keep searching, and everyone goes home disappointed. That is precisely what 0x80073712 reports: the component store's index references payload files that are not actually on your disk. When the update engine reaches for one and finds nothing, the install collapses.

On 24H2 laptops the usual backstories: a disk fault, a "cleanup" program that trimmed WinSxS harder than it should have, or an earlier update that perished while half-written. None of these are your fault in any meaningful sense, and all are repairable. The store's index lies in small ways too, not just catastrophic ones — a single misplaced reference is enough to fail a whole cumulative update.

The good news is that Windows ships the exact tools for this injury. The fixes below climb from a quick diagnosis to a full repair, so begin at the top and stop the moment updates install cleanly. Patience pays: most readers never reach the final fix.

## Why this happens

- **A cleaner pruned WinSxS too hard.** Hardlinked files look redundant to naive tools, so they get deleted while still referenced.
- **A disk fault silently lost files.** Bad sectors in the WinSxS region make payloads vanish without warning.
- **An earlier update died mid-write.** Half-recorded components leave the index pointing at files never finished.
- **Superseded versions cluttered the store.** Outdated component copies can choke the repair tooling itself.
- **A language pack or feature removal broke links.** Removing optional content can orphan references other components still need.
- **Antivirus quarantined a system file.** Overzealous scanners sometimes seize files the store considers its own.
- **A drive without power-loss protection lost writes.** Outages on consumer SSDs can eat files that were being recorded.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure the damage before treating it

DISM's read-only scans report on the store's condition without changing a single file, so this is always the safe first move — think of it as the X-ray before the surgery.

1. Open an administrator Command Prompt and run `DISM /Online /Cleanup-Image /CheckHealth`.
2. If CheckHealth flags corruption, run `DISM /Online /Cleanup-Image /ScanHealth` for the detailed verdict.
3. A clean ScanHealth suggests the trouble lies elsewhere — work down the list. A confirmed injury leads straight to Fix 2.

### Fix 2: Restore the missing files from Windows Update

RestoreHealth was purpose-built for exactly this wound: it audits the entire store against healthy manifests, then fetches genuine replacements for whatever is absent or broken. Expect it to take a while — 15 to 30 minutes on a typical laptop, longer on a slow disk.

1. In the same elevated prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for 100 percent — do not close the window early.
2. Follow it with `sfc /scannow` to sweep protected system files.
3. Reboot, then retry the update.

If RestoreHealth stalls, errors out, or reports it could not find the source files, our dedicated DISM RestoreHealth walkthrough covers the recovery options in full.

### Fix 3: Clear the clutter that stalls the repair

A repair pass can jam when outdated, superseded component versions crowd the store. Tidying first gives RestoreHealth room to work — a cluttered store is the single most common reason the first repair attempt stalls.

1. Run `DISM /Online /Cleanup-Image /StartComponentCleanup` from the administrator prompt.
2. Once it completes, run `DISM /Online /Cleanup-Image /RestoreHealth` again.
3. Attempt the update — the second repair pass frequently succeeds where the first one stalled.

### Fix 4: Run the built-in troubleshooter

The Windows Update troubleshooter knows the standard symptoms of store damage and applies its own safe repairs. Worth trying before the manual machinery.

1. Visit Settings > System > Troubleshoot > Other troubleshooters.
2. Activate the Windows Update entry and comply with its requests.
3. Reboot when finished and attempt the update afresh.

### Fix 5: Reset the update engine's own state

Store damage and engine confusion often travel together, and a confused engine can even refuse to retry an update that is actually repairable. This classic sequence renames the cache folders so Windows rebuilds them from nothing.

1. Bring the trio of services to a halt: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rechristen the cache directories: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Wake the services up again: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Scan for updates and see whether the error survives.

### Fix 6: Install the KB package by hand

The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) publishes every cumulative and servicing-stack release, and a manual install sidesteps the injured machinery completely.

1. Copy the KB number of the failed update from Update history.
2. On the Catalog, find that KB and grab its x64 Windows 11 package.
3. Double-click the `.msu` file and work through the installer.
4. Reboot when asked, then confirm the update in your history.

### Fix 7: Reinstall Windows atop the existing copy

When the store is wounded past what targeted tools can mend, reinstalling 24H2 over itself — files and apps preserved — replaces it wholesale. Source the ISO only from [Microsoft's Windows 11 download site](https://www.microsoft.com/en-us/software-download/windows11).

1. Attach the ISO, fire up `setup.exe`, and agree to the license terms.
2. Mark **Keep personal files and apps** when asked.
3. Reserve 30 to 90 minutes for multiple restarts; never break in mid-run.
4. Launch Windows Update after signing in to prove the repair held.

## Closing

A lying store index yields to methodical repair: measure it, restore it, clear its clutter, and it stops misleading the installer. The repair does not touch your files or programs — it only reconciles the index with reality. If the next cumulative update raises a different complaint, the [24H2 update-error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) unravels the rest of the family, and the [manual Catalog route](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) remains the dependable bypass for any stubborn KB. If DISM stalls or errors out during the repair, our [DISM RestoreHealth walkthrough for 24H2](/articles/how-to-run-dism-restore-health-in-windows-11-24h2/) covers the recovery options in full.
