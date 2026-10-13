---
title: "Fix Windows Update Error 0x800f0900 on Windows 11 (Update Files Corrupt)"
slug: how-to-fix-windows-update-error-0x800f0900-on-windows-11
date: 2026-10-03
categories: ["windows-update"]
tags: ["windows update", "0x800f0900", "manifest", "servicing", "windows 11"]
description: "Windows 11 error 0x800f0900 means corrupted update manifests can't be parsed. Repair the servicing metadata and install updates cleanly with these fixes."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0900-on-windows-11.webp"
faqs:
  - q: "What is a servicing manifest?"
    a: "On Windows 11, a servicing manifest is an XML document describing a single system component: its files, versions, registry keys, and dependencies. The servicing stack reads these manifests to plan every update. Error 0x800f0900 means the XML parser could not read one or more of them — usually through corruption — so the update can neither be planned nor applied."
  - q: "Why does antivirus quarantine Windows servicing files?"
    a: "Heuristic scanning occasionally mistakes servicing metadata — especially freshly written manifests and catalogs during an update — for something suspicious. Quarantining them breaks the parser on the next attempt. The remedy is restoring the files and excluding Windows' servicing folders in the antivirus settings, a standard and safe exclusion."
  - q: "Is CHKDSK really necessary for an update error?"
    a: "When 0x800f0900 recurs across unrelated updates, yes. Manifests are thousands of tiny files, and storage developing bad sectors damages them disproportionately. One `chkdsk C: /f /r` pass rules out the hardware layer conclusively — skip it and you may repair the same corruption repeatedly without ever confronting its source."
  - q: "Can faulty RAM cause 0x800f0900?"
    a: "It can, though rarely. Bad memory corrupts data moving between disk and processor, damaging manifests in transit and producing parser failures that hop between updates. If the error is random, joins other crashes, and survives disk checks, run Windows Memory Diagnostic to test the RAM."
---

Error 0x800f0900 — CBS_E_XML_PARSER_FAILURE — is the servicing stack admitting defeat at reading its own paperwork. The XML manifests that describe update components are damaged, so the parser gives up before installation even starts. On Windows 11 the damage usually comes from corrupted downloads, disk errors chewing through the manifest store, or antivirus quarantining servicing metadata. The update package itself can be flawless; it is the local description of your system that is broken.

Because the breakage sits in metadata — not in your files or your installed updates — the repairs are safe and tightly scoped: regenerate the metadata caches, heal the store, and derive fresh manifests from healthy sources. The system underneath is never touched.

When the deeper trouble on your other machine is store damage rather than metadata, [the Windows 10 edition](/articles/how-to-fix-windows-update-error-0x800f0900-on-windows-10/) covers that OS, and [the 0x80073712 store-repair guide](/articles/how-to-fix-windows-update-error-0x80073712-on-windows-11/) handles the store level. For parser failures, begin with the metadata reset.

## Why this happens

- **Manifests downloaded already broken.** Metadata travels with the payloads, so an interrupted or bit-damaged download corrupts the XML and the parser chokes on the malformed result.
- **Disk damage in the manifest store.** The manifest store holds tens of thousands of tiny XML files across WinSxS and the servicing folders — one bad sector anywhere in that sprawl breaks parsing for a whole update.
- **Servicing files swept into quarantine.** Security software periodically misreads servicing metadata as hostile, quarantining or locking it; the parser is then left facing missing or truncated documents.
- **An earlier update quit mid-write.** An interrupted servicing operation can abandon manifest files truncated halfway; the next update's parser stumbles over the incomplete documents.
- **A corrupt catroot2 undermining signature checks.** catroot2 is the catalog store whose signatures validate every manifest. When it corrupts, valid manifests fail validation — a breakdown that surfaces at the parser level.
- **Cleaner tools deleting servicing metadata.** Aggressive cleaners that hand-prune WinSxS or servicing folders remove manifests the parser needs, manufacturing 0x800f0900 on a previously healthy system.
- **Faulty RAM scrambling files in flight.** Rare but genuine — bad memory can garble manifests as they travel between disk and processor, producing parser failures that wander randomly between updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Regenerate the update caches and the catalog store

The parser reads SoftwareDistribution and validates against catroot2 — both are throwaway caches. Renaming them compels Windows to download fresh manifests and rebuild the catalog store, which cures parser failures rooted in corrupt local metadata in one stroke.

1. Launch a Command Prompt with administrator rights.
2. Stop the three services — wuauserv (`net stop wuauserv`), BITS (`net stop bits`), cryptsvc (`net stop cryptsvc`).
3. Rename the download cache: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Rename the catalog store: `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Start the three services again, open Settings > Windows Update, check for updates, and let the rebuild finish before retrying.

### Fix 2: Heal the component store

When pristine metadata still refuses to parse, the rot goes deeper — into the WinSxS manifests themselves. DISM RestoreHealth scans the store and trades damaged manifests for known-good copies, fixing the documents that trip the parser at their source.

1. Open an administrator Command Prompt.
2. Execute `DISM /Online /Cleanup-Image /RestoreHealth` and let the progress bar reach 100 percent.
3. Immediately follow with `sfc /scannow`.
4. Reboot the laptop.
5. Attempt the update from Settings > Windows Update.

### Fix 3: Roll back the newest update

Occasionally the parser failure originates in the last installed update's own manifests — a single bad cumulative update can poison the metadata for its successor. Removing the newest update takes those manifests away, and the retry parses cleanly.

1. Open the uninstall list at Settings > Windows Update > Update history > Uninstall updates.
2. Order by install date and remove the newest entry.
3. Reboot when prompted.
4. Check for updates once more in Settings > Windows Update.
5. If the previously failing update now installs, re-fetch the removed one afterward from [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com) when needed.

### Fix 4: Rule out disk damage

Manifests are minuscule files scattered across the servicing tree — sitting ducks for bad sectors and file-system corruption. CHKDSK repairs the file system and quarantines bad sectors so manifests stop landing on dying storage.

1. Start an administrator Command Prompt.
2. Schedule `chkdsk C: /f /r` by typing Y at the prompt.
3. Reboot and allow the scan to finish uninterrupted.
4. After booting, regenerate the caches again (Fix 1) so fresh manifests settle onto verified sectors.
5. Retry the update.

### Fix 5: Free servicing files from quarantine

If your suite quarantined servicing metadata, each repair rebuilds files that get re-quarantined — an invisible loop. Spotting recently flagged system or servicing files in quarantine, restoring them, and excluding them breaks the cycle for good.

1. Open your antivirus — Windows Security included — and review quarantine alongside protection history.
2. Search for quarantined items under Windows servicing paths or with manifest/catalog extensions.
3. Restore discovered servicing files and exclude the Windows servicing folders.
4. Reboot.
5. Regenerate the caches (Fix 1) once more so clean manifests take the quarantined ones' place, then retry.

### Fix 6: Reinstall Windows over itself

The definitive rebuild: an in-place upgrade lays Windows down over itself from clean media, regenerating every manifest, catalog, and servicing record while keeping files, apps, and settings. Parser failures that survive cache rebuilds, DISM, and disk checks are systemic by definition — and this is the systemic answer.

1. Prepare Windows 11 installation media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Launch setup.exe while Windows is still running.
3. Keep personal files and apps.
4. Budget one to two hours across several restarts.
5. Afterward, verify in Settings > Windows Update that updates parse and install cleanly. The full repair-install walkthrough is on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Repair the store offline in WinRE

Parser failures that outlive every online repair usually involve manifests locked by the running system. Entering the Windows Recovery Environment takes the installed Windows offline, unlocking every servicing file so DISM and SFC can rebuild manifests without contention — the strongest option short of a reinstall.

1. Enter Recovery by holding Shift while clicking Start > Power > Restart.
2. Choose Troubleshoot > Advanced options > Command Prompt.
3. Pin down the Windows drive letter with `diskpart`, then `list volume`, then `exit` (WinRE often calls it D:, not C:).
4. Execute `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`, substituting the right letter.
5. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`, substituting the same letter.
6. Type `exit`, pick Continue for a normal boot, and attempt the update in Settings > Windows Update.

## Closing

0x800f0900 is illegible paperwork: the manifests describing your system were damaged, and the servicing parser will not plan an update from documents it cannot read. Regenerate the caches, heal the store, check the disk, and new paperwork gets issued. On Windows 11 the cache-and-catalog rebuild alone closes most cases — servicing metadata is built to be disposable, so regenerating it is maintenance, not a workaround.
