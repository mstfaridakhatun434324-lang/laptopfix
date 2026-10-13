---
title: "How to Fix Windows Update Error 0x800f0988 on Windows 10"
slug: how-to-fix-windows-update-error-0x800f0988-on-windows-10
date: 2026-09-30
categories: ["windows-update"]
tags: ["windows update", "0x800f0988", "cumulative update", "language pack", "windows 11"]
description: "Error 0x800f0988 on Windows 10 means a cumulative update can't find matching component versions. Resolve the PSFX mismatch with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0988-on-windows-10.webp"
faqs:
  - q: "What does PSFX_E_MATCHING_COMPONENT_NOT_FOUND mean?"
    a: "The cumulative update's servicing logic (PSFX) searched your Windows 10 machine for a particular component version and found no match. The typical cause is a surplus language pack or a partially removed optional feature leaving components in an unforeseen state. Removing the extras and running DISM store repairs clears it."
  - q: "Why do language packs break cumulative updates?"
    a: "Each extra language adds localized copies of system components, and the update must include matching data for every copy present. Old or half-installed packs create copies the package never anticipated, so servicing halts with 0x800f0988 instead of patching the wrong baseline. Fewer languages means fewer conflicts."
  - q: "Should I install the servicing stack update separately?"
    a: "Yes, when the error persists. The servicing stack is the engine that applies cumulative updates, and newer updates sometimes rely on engine capabilities only the latest SSU provides. Installing the SSU first — from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) if needed — is a quick, low-risk step that unblocks otherwise stubborn failures."
  - q: "Will an in-place upgrade delete my files?"
    a: "No, provided you choose Keep personal files and apps: documents, installed programs, and settings survive while Windows rebuilds its servicing layer. Back up irreplaceable data first as routine prudence, but the process is designed to be non-destructive and is Microsoft's recommended cure for deep servicing corruption."
---
Error 0x800f0988 on Windows 10 appears when a cumulative update's expectations about your system's components do not match reality. Somewhere on the machine — an extra language pack, a half-removed optional feature, a store that drifted after an interrupted update — the inventory disagrees with the update package, so servicing refuses to proceed rather than patch the wrong thing.

The reassuring part is that the failure is clean: servicing validates everything before changing anything, so a rejected update leaves no debris and causes no instability. Your job is reconciliation — trim what should not be there, mend the store, freshen the servicing engine, and rebuild the baseline only as a last resort. None of this threatens your files or installed programs. Think of it as tidying a library so the catalog matches the shelves: once the inventory agrees, the update that kept bouncing will install without complaint.

The [Windows 11 edition](/articles/how-to-fix-windows-update-error-0x800f0988-on-windows-11/) covers the same error on Windows 11, while the [sibling 0x800f0989 guide](/articles/how-to-fix-windows-update-error-0x800f0989-on-windows-10/) addresses the related PSFX failure. Begin by auditing which extras are installed.

## Why this happens

- **Surplus language packs introduce variant mismatches:** each pack adds localized component variants the cumulative update must cover. Stale, partial, or unnecessary packs create versions the package never described — the classic 0x800f0988 trigger.
- **The component store drifted off-script:** interrupted updates and overzealous cleanup utilities leave WinSxS holding components no known servicing baseline recognizes.
- **An earlier cumulative update stalled halfway:** with some components moved to the new level and the rest left at the old one, the next cumulative update cannot reconcile the split.
- **The servicing stack lags behind:** the SSU is the engine that installs cumulative updates; an outdated engine can misjudge component states that a current one reads correctly.
- **Optional features were removed incompletely:** .NET builds, media features, and similar components deleted halfway leave orphaned records the update cannot account for.
- **Cleanup tools erased servicing metadata:** utilities promising a slimmer Windows sometimes strip manifests and payloads the engine needs to compute the update, manufacturing the mismatch.
- **Disk damage corrupted component records:** bad sectors inside the WinSxS tree garble the records the engine matches against, fabricating mismatches from nowhere.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Strip unneeded language packs

Fewer languages means fewer component variants for the update to reconcile — this single cleanup resolves a large share of 0x800f0988 cases on its own.

1. Open Settings > Time & language > Language.
2. Under Preferred languages, select each language you never use and choose Remove.
3. Restart the laptop afterward.
4. Retry the cumulative update via Settings > Update & Security > Windows Update.
5. If it installs, the language packs were the problem — keep them off.

### Fix 2: Clean up and repair the component store

Trim the store first, then repair it — the repair runs faster and more reliably on a smaller, tidier store, and you reclaim disk space as a bonus.

1. Launch an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /StartComponentCleanup`.
3. Once it finishes, run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Finish with `sfc /scannow` to verify protected files.
5. Restart and attempt the update again in Settings > Update & Security > Windows Update.

### Fix 3: Apply the newest servicing stack update on its own

SSUs are quick, need at most one restart, and give the update engine the capabilities newer cumulative updates assume — do this even if you believe your stack is current. A stale stack is one of the quietest causes of repeat 0x800f0988 failures.

1. Check your build with Win + R > `winver`.
2. Find the latest servicing stack update for that build on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Install the SSU package and restart.
4. Go back to Settings > Update & Security > Windows Update and attempt the cumulative update again.
5. If even the SSU fails, reset the update components first (next fix) and try again.

### Fix 4: Reset the Windows Update components

Do this after the store work so each layer — languages, store, pipeline — is verified clean in sequence.

1. Open a Command Prompt with administrator rights.
2. Execute `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Execute `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Bring the three services back with the matching `net start` commands.
5. Give the cumulative update another try from Settings > Update & Security > Windows Update.

### Fix 5: Clean up half-removed optional features

Features stranded between on and off leave component records servicing cannot place — pay special attention to .NET Framework 3.5 and media features.

1. Press Win + R, enter `optionalfeatures`, and hit Enter.
2. Uncheck anything you do not need — particularly half-configured entries — and click OK.
3. For a feature you genuinely need that looks broken: turn it fully on, restart, then turn it fully off and restart again.
4. Allow the dialog to apply its changes, then restart once more.
5. Try the update again in Settings > Update & Security > Windows Update.

### Fix 6: Repair with an in-place upgrade

The heavyweight but decisive option — rebuilds the entire servicing baseline while keeping your files and apps. Reserve it for when everything above has been performed properly.

1. Obtain the Windows 10 Media Creation Tool — via Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).
2. Run setup.exe from inside your current Windows installation.
3. Select Keep personal files and apps.
4. Allow one to two hours across several restarts.
5. Afterward, cumulative updates install against a coherent baseline.

## Closing

On Windows 10, PSFX mismatch errors surrender to tidiness: remove what does not belong, mend the store, refresh the servicing engine, and rebuild the baseline when all else fails. Move from the gentlest intervention to the most drastic and stop at the first success. Keep spare language packs off the machine afterward — they are the most frequent repeat offender — and cumulative updates return to their quiet monthly rhythm.
