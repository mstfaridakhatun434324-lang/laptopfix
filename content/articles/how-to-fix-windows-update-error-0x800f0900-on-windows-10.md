---
title: "How to Fix Windows Update Error 0x800f0900 on Windows 10"
slug: how-to-fix-windows-update-error-0x800f0900-on-windows-10
date: 2026-10-04
categories: ["windows-update"]
tags: ["windows update", "0x800f0900", "manifest", "servicing", "windows 11"]
description: "Windows 10 error 0x800f0900 signals corrupted update manifests the parser can't read. Fix the metadata with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0900-on-windows-10.webp"
faqs:
  - q: "What is a servicing manifest?"
    a: "On Windows 10, a servicing manifest is an XML document describing one system component: its files, versions, registry keys, and dependencies. The servicing stack reads these manifests to plan every update. Error 0x800f0900 means the XML parser could not read one or more of them — usually because of corruption — so the update cannot be planned or applied."
  - q: "Why does antivirus quarantine Windows servicing files?"
    a: "Heuristic scanning occasionally misidentifies servicing metadata — especially newly written manifests and catalogs during an update — as suspicious. Quarantining them breaks the parser on the next update attempt. The fix is restoring the files and excluding Windows' servicing folders in the antivirus settings, a standard and safe exclusion."
  - q: "Is CHKDSK really necessary for an update error?"
    a: "When 0x800f0900 recurs across unrelated updates, yes. Manifests are thousands of tiny files, and storage developing bad sectors corrupts them disproportionately. One `chkdsk C: /f /r` pass rules out the hardware layer definitively — skip it and you risk repairing the same corruption repeatedly without ever addressing its source."
  - q: "Can faulty RAM cause 0x800f0900?"
    a: "It can, though it is uncommon. Bad memory corrupts data as it is read from or written to disk, which can damage manifests in transit and produce parser failures that jump between different updates. If the error is random, accompanied by other crashes, and survives disk checks, run Windows Memory Diagnostic to test the RAM."
---
On Windows 10, error 0x800f0900 means the Component-Based Servicing parser hit corrupted XML manifests and gave up. Every update carries manifests describing exactly which files, registry keys, and versions it manages; when those local manifests are damaged — by a bad download, disk corruption, or overzealous security software — the parser cannot proceed and reports this code.

Think of it as a customs form that got wet: the goods are fine, but nobody can read the declaration. Reissuing the paperwork — rebuilding caches and metadata — is the entire repair strategy, and it leaves your data and installed software completely alone.

The [Windows 11 guide](/articles/how-to-fix-windows-update-error-0x800f0900-on-windows-11/) is the Windows 11 edition, and the [companion guide for 0x80073712](/articles/how-to-fix-windows-update-error-0x80073712-on-windows-10/) covers deeper component-store corruption. Rebuild the paperwork first.

## Why this happens

- **Downloaded manifests are corrupted:** Update metadata downloads alongside payloads; an interrupted or bit-damaged download corrupts the XML manifests, and the parser fails on the malformed documents.
- **Disk errors damaged the manifest store:** The servicing manifests live in WinSxS and the servicing folders — tens of thousands of small XML files where a single bad sector breaks parsing for the whole update.
- **Antivirus quarantined servicing files:** Security software occasionally flags servicing metadata as suspicious and quarantines or locks it, leaving the parser staring at missing or truncated documents.
- **A previous update left manifests half-written:** An interrupted servicing operation can leave manifest files truncated mid-write; the next update's parser trips over the incomplete documents.
- **Corrupted catroot2 breaks signature validation:** The catroot2 catalog store holds the signatures manifests are validated against. Corruption there makes valid manifests fail validation, which surfaces as a parser-level failure.
- **Third-party cleaners deleted servicing metadata:** Aggressive system cleaners that prune WinSxS or servicing folders by hand remove manifests the parser needs, manufacturing 0x800f0900 from a previously healthy system.
- **Memory faults corrupted files in transit:** Rare but real: faulty RAM can corrupt manifests as they are read or written, producing parser failures that move around randomly between updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rebuild the update caches and catalog store

This is the highest-yield fix for 0x800f0900 because the error lives in exactly these caches.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Restart the three services, then check for updates in Settings > Update & Security > Windows Update and let it rebuild before retrying.

### Fix 2: Repair the component store with DISM

Follow with SFC so the protected-file layer is verified against the newly repaired store.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for 100 percent.
3. Run `sfc /scannow` immediately afterward.
4. Restart the laptop.
5. Retry the update in Settings > Update & Security > Windows Update.

### Fix 3: Uninstall the most recent update and retry

Use update history to identify the freshest entry, and keep its KB number in case you need to reinstall it later deliberately.

1. Open Settings > Update & Security > Windows Update > Update history > Uninstall updates.
2. Sort by installed date and uninstall the most recent update.
3. Restart when prompted.
4. Run the update check again in Settings > Update & Security > Windows Update.
5. If the previously failing update now installs, reinstall the removed one afterward from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) if needed.

### Fix 4: Check the disk for file-system damage

Recurring parser failures across different updates are the signature of storage-level damage rather than download luck.

1. Open Command Prompt as administrator.
2. Run `chkdsk C: /f /r` and type Y to schedule at restart.
3. Restart and let the scan complete without interruption.
4. After booting, rebuild the caches once more (Fix 1) so manifests land on verified sectors.
5. Retry the update.

### Fix 5: Review antivirus quarantine for servicing files

This step is quick and rules out an entire class of self-inflicted parser failures.

1. Open your antivirus (including Windows Security) and review the quarantine/protection history.
2. Look for quarantined files under Windows servicing paths or with manifest/catalog extensions.
3. Restore any servicing files and add the Windows servicing folders to exclusions.
4. Restart the laptop.
5. Rebuild the caches (Fix 1) once more so clean manifests replace the quarantined ones, then retry.

### Fix 6: Perform an in-place upgrade repair

Reserve it for last, but do not fear it: it is Microsoft's designed recovery for exactly this depth of servicing damage.

1. Create the Windows 10 Media Creation Tool; Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) hosts the installation media.
2. Run setup.exe from within your running Windows.
3. Choose Keep personal files and apps.
4. Allow one to two hours across several restarts.
5. Afterward, confirm in Settings > Update & Security > Windows Update that updates parse and install cleanly. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the full repair-install walkthrough.

### Fix 7: Repair servicing offline from the Recovery Environment

When Windows 10 is running, it holds its servicing manifests open, which limits what online tools can replace. The Recovery Environment boots a separate minimal system, leaving your installation's files fully accessible. Offline DISM and SFC from there repair manifest corruption that online scans could not touch.

1. Hold Shift while clicking Start > Power > Restart to enter Recovery.
2. Go to Troubleshoot > Advanced options > Command Prompt.
3. Find your Windows drive letter using `diskpart`, then `list volume`, then `exit` (often D: in WinRE).
4. Run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`, adjusting the drive letter to match.
5. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` with the same letter.
6. Type `exit`, boot normally, and retry the update in Settings > Update & Security > Windows Update.

## Closing

On Windows 10, XML parser failures in servicing sound exotic but repair routinely: the metadata caches rebuild themselves, DISM restores the manifests, and CHKDSK protects the storage underneath. Work from the caches inward and stop at the first lasting success. The parser is picky because it has to be — it guards the integrity of every file Windows installs.
