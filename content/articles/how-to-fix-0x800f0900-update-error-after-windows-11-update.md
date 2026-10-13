---
title: "How to Fix the 0x800F0900 Update Error After a Windows 11 Update"
slug: how-to-fix-0x800f0900-update-error-after-windows-11-update
date: 2026-09-16
categories: ["windows-update"]
tags: ["0x800f0900", "windows update", "windows 11", "update error"]
description: "Error 0x800F0900 after a Windows 11 update means the update manifest failed to parse. Clear the cache, repair the store, and reinstall cleanly with this guide."
thumbnail: "/images/thumbs/how-to-fix-0x800f0900-update-error-after-windows-11-update.webp"
faqs:
  - q: "What does error 0x800F0900 mean?"
    a: "It is CBS_E_XML_PARSER_FAILURE: the servicing stack could not parse the update's XML manifest. The manifest describes every file in the update, so a manifest Windows cannot read means the update cannot be validated or installed. Think of the manifest as the update's packing list — if Windows cannot read the list, it cannot unpack the box."
  - q: "Why did 0x800F0900 appear right after a Windows 11 update?"
    a: "Usually because the downloaded package was truncated or corrupted, or because the previous update left the component store in a state where the new manifest cannot be processed. The timing points at the download or the store, not at your hardware."
  - q: "Can a bad hard drive cause 0x800F0900?"
    a: "Yes. Disk corruption can damage the cached manifest between download and install, producing exactly this parser error. If the error survives cache clears and DISM repairs, checking the drive with chkdsk is the logical next step. Mechanical drives developing bad sectors are the usual suspects; SSDs fail this way far less often."
  - q: "Is the manual Catalog install safe for this error?"
    a: "Yes. Installing the same KB from the Microsoft Update Catalog bypasses the damaged Windows Update download path entirely, and the standalone installer validates the package independently. It is one of the most reliable workarounds for 0x800F0900. The Catalog is Microsoft's own distribution point, so the package is identical to what Windows Update would deliver."
---

Error 0x800F0900 has a habit of appearing right when an update should be finishing. The download completes, the install begins, and then Windows Update reports failure with this code and no helpful context. Under the hood, the meaning is precise: the servicing stack tried to read the update's XML manifest — the file that inventories every component in the package — and the parse failed. No manifest, no install.

On Windows 11 this almost always comes down to two culprits: a corrupted download sitting in the update cache, or damage in the component store that prevents manifest processing. Both are repairable without drastic measures. The sequence below starts with the cache, moves through store repair, and ends with the manual install that sidesteps the whole problem.

Every Windows update carries a manifest — an XML document inventorying each file, its hash, and where it belongs. The servicing stack parses this manifest before touching a single system file, because installing from an unreadable manifest risks an inconsistent system. Error 0x800F0900 means that parse failed: truncated XML from an interrupted download, a manifest altered by disk corruption, or a store too damaged to validate against. The stack did exactly the right thing by refusing. Your job is to give it a manifest it can read.

## Why this happens

- **A truncated manifest in the update cache.** An interrupted download leaves an XML manifest that ends mid-file, which the parser rejects immediately.
- **Component store corruption.** Damage in WinSxS breaks the baseline the manifest is validated against, failing the parse.
- **Disk errors altering cached files.** Bad sectors or file-system damage silently corrupt the manifest after a successful download.
- **A mismatched or superseded package.** Stale metadata serves a manifest that does not match the actual package revision.
- **Antivirus quarantining part of the package.** Security software removing a staged file leaves the manifest referencing something that no longer exists.
- **Servicing stack too old for the package format.** An outdated stack cannot parse manifests from newer update revisions.
- **Concurrent update operations colliding.** Two update processes staging packages simultaneously can corrupt each other's manifests.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failing KB and clear the update cache

The corrupted manifest lives in the cache — remove it first.

1. Open **Settings** > **Windows Update** > **Update history** and note the KB number behind the 0x800F0900 error.
1. In an elevated Command Prompt, stop wuauserv, cryptSvc, bits, and msiserver.
1. Rename `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` with `.old` suffixes.
1. Restart the services and check for updates, letting the KB download completely fresh.

### Fix 2: Run the Windows Update troubleshooter

Covers the registration and service faults that can accompany a manifest failure.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
1. Run **Windows Update**, apply all fixes, and restart.
1. Retry the update once on the clean cache.
1. If 0x800F0900 returns for the same KB, the problem is deeper than the cache.

### Fix 3: Repair the component store with DISM

Manifest parsing depends on a healthy store — repair it directly.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt.
1. Wait for full completion; do not interrupt it.
1. Follow with `sfc /scannow` and restart.
1. Retry the update. This resolves the related [invalid package error 0x800F080A](/articles/how-to-fix-windows-update-error-0x800f080a-on-lenovo-laptop/) by the same mechanism.

### Fix 4: Check the disk for corruption

If fresh downloads keep producing unparseable manifests, suspect the storage.

1. Run `chkdsk C: /f` from an elevated Command Prompt and reboot to scan.
1. Check **Event Viewer** > **Windows Logs** > **Application** (Wininit source) for the results.
1. Clear the update cache once more after any repairs.
1. Retry the download — a healthy disk plus a clean cache should yield a valid manifest.

### Fix 5: Install the KB manually from the Update Catalog

Bypass the Windows Update download path entirely.

1. Find the exact KB number from your update history.
1. Download the x64 package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
1. Run the .msu installer and restart when prompted.
1. The standalone installer parses the manifest independently of the damaged cache. If it succeeds, your update pipeline needed only a clean package.

### Fix 6: Update the servicing stack first if the KB is new

An old stack chokes on new manifests — update the stack, then the KB.

1. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for the latest servicing stack update for your build.
1. Install the SSU, restart, then install the cumulative KB manually.
1. Alternatively, let Windows Update pull the SSU naturally after the cache clear, then retry the KB.
1. Stack-first ordering prevents a whole class of manifest errors.

### Fix 7: In-place upgrade repair for persistent failures

When 0x800F0900 survives every targeted repair, rebuild the servicing infrastructure.

1. Download the Media Creation Tool from Microsoft's official Windows 11 download site.
1. Run setup.exe inside Windows and choose **Keep personal files and apps**.
1. Complete the repair install (30 to 90 minutes).
1. Run Windows Update afterward — with a rebuilt store and stack, manifests parse normally. For the full repeat-failure playbook, see [cumulative update fails every time on Windows 11](/articles/how-to-fix-cumulative-update-fails-every-time-on-windows-11/).

### Fix 8: Run an offline DISM repair with ISO source

When online DISM cannot repair the store, give it clean source files.

1. Download the Windows 11 ISO from Microsoft's official site and mount it (double-click).
1. Note the drive letter, then run `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:X:\Sources\Install.wim:1` with your letter.
1. Wait for completion — the local source bypasses download problems entirely.
1. Follow with `sfc /scannow`, restart, and retry the update against the repaired store.

## Closing

Error 0x800F0900 is the servicing stack telling you it cannot read the update's manifest — a data problem, not a system death sentence. Fresh downloads, a repaired component store, and a healthy disk resolve it in nearly every case, and the manual Catalog install routes around the damaged path when Windows Update cannot. Once the KB installs cleanly, the parser error is gone for good.
