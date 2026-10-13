---
title: "Fix Windows Update Error 0x800f0989 on Windows 11 (Update Won't Install)"
slug: how-to-fix-windows-update-error-0x800f0989-on-windows-11
date: 2026-10-01
categories: ["windows-update"]
tags: ["windows update", "0x800f0989", "cumulative update", "servicing", "windows 11"]
description: "Error 0x800f0989 blocks Windows 11 updates when components don't match the update package. Diagnose the mismatch and repair it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0989-on-windows-11.webp"
faqs:
  - q: "What is the difference between 0x800f0989 and 0x800f0988?"
    a: "Both are PSFX servicing-mismatch errors on Windows 11 with heavily overlapping causes — language packs, store drift, interrupted updates. In practice, 0x800f0988 is most associated with language-pack mismatches, while 0x800f0989 appears more with pending operations and half-configured optional features. The repair playbook is nearly identical, which is why the fixes here mirror the sibling guide."
  - q: "What are pending servicing operations?"
    a: "They are update tasks Windows recorded in pending.xml but has not finished — usually because the required restart never happened. Until they commit or roll back, the component set sits in a transitional state that new updates cannot match, producing 0x800f0989. A proper Restart (not Shut down) lets servicing finish the pending work."
  - q: "Can optional features really break Windows Update?"
    a: "Yes. Features like .NET Framework 3.5 add components that cumulative updates must account for; a half-enabled feature leaves those components in an indeterminate state. The Windows Features dialog (`optionalfeatures`) lets you set each feature decisively on or off, which clears the indeterminate records servicing chokes on."
  - q: "How do I know the in-place upgrade is necessary?"
    a: "When every targeted fix — restart cycle, feature tidying, language removal, DISM repair, pipeline reset, and manual install — has been done properly and 0x800f0989 still appears for the same update. At that point the servicing baseline itself is the problem, and only rebuilding it via in-place upgrade (keeping files and apps) resolves the mismatch."
---
Error 0x800f0989 is the close sibling of 0x800f0988: the servicing stack cannot reconcile the update package with the components installed on your PC, so the installation aborts before changing anything. On Windows 11 it shows up with cumulative updates and occasionally with .NET rollups, and its triggers overlap its sibling's — stale language packs, store drift, half-applied updates — with extra emphasis on pending operations and optional-feature states.

Because the failure happens at the matching stage, your system is never left half-patched; every retry starts from the same safe baseline. The work is therefore pure alignment: clear pending operations, tidy optional features, repair the store, and let the update meet a system it recognizes.

If you are seeing the better-known sibling code instead, the [Windows 10 guide](/articles/how-to-fix-windows-update-error-0x800f0989-on-windows-10/) covers Windows 10 and the [companion guide for 0x800f0988](/articles/how-to-fix-windows-update-error-0x800f0988-on-windows-11/) handles 0x800f0988 directly. For 0x800f0989, begin with pending operations.

## Why this happens

- **Pending servicing operations never completed:** Operations recorded in pending.xml from an update that never got its reboot leave the component set in a transitional state that new updates cannot match.
- **Optional features sit half-enabled:** .NET Framework 3.5, Hyper-V remnants, or media features toggled incompletely leave component records in limbo, and servicing rejects packages that cannot account for them.
- **A previous update was interrupted mid-commit:** Power loss or forced shutdown during the commit phase splits component versions across the store, so the next update's expectations match neither half.
- **Stale language packs add unexpected variants:** As with its sibling error, unneeded or partially installed language packs introduce component variants the update package does not describe.
- **The component store accumulated drift:** Months of updates, cleanups, and third-party modifications gradually move WinSxS away from any clean baseline the update recognizes.
- **Corrupted update metadata misdescribes the system:** Damaged data in the servicing metadata can make the engine misread which components are installed, manufacturing a mismatch from healthy files.
- **Disk errors damaged servicing records:** Bad sectors in the servicing tree corrupt manifests and pending-operation records, producing mismatch errors from physically damaged bookkeeping.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear pending servicing operations with a proper restart cycle

Pending operations are the most overlooked trigger of 0x800f0989: an update that installed but never got its completing reboot leaves the system mid-transaction. A full restart — not shutdown — lets servicing commit or roll back the pending work and return the component set to a matchable state.

1. Open Settings > Windows Update > Update history and look for updates marked as needing a restart.
2. Click Start > Power > Restart (avoid Shut down so Fast Startup does not skip the commit).
3. After rebooting, wait five minutes for background servicing to settle.
4. Open Settings > Windows Update and check whether the pending state cleared.
5. Retry the failed update only after the restart cycle completes.

### Fix 2: Tidy optional Windows features

Half-configured optional features are a classic 0x800f0989 trigger because their component records sit between states. Opening the Windows Features dialog and decisively enabling or disabling each questionable entry — no maybes — removes the limbo states servicing chokes on.

1. Press Win + R, type `optionalfeatures`, and press Enter.
2. For each feature you do not need, uncheck it fully and click OK.
3. If .NET Framework 3.5 shows a partial state, check it on completely, restart, then uncheck it and restart again.
4. Let Windows apply the changes — this can take several minutes.
5. Restart once more, then retry the update in Settings > Windows Update.

### Fix 3: Remove unneeded language packs

Language packs multiply the component variants servicing must reconcile, and stale packs are a documented trigger for the whole 0x800f098x family. Windows 10 keeps per-language component data long after you stop using a language, so packs you added years ago still complicate today's cumulative updates. Stripping every language you do not read or type in shrinks the matching problem to the update's expected baseline, and reinstalling a language later takes only minutes if you ever need it back.

1. Open Settings > Time & language > Language.
2. Remove every preferred language except your active display language.
3. Restart the laptop to let servicing notice the simplified configuration.
4. Retry the cumulative update in Settings > Windows Update.
5. Reinstall a language later only if you genuinely need it — each one re-adds matching surface.

### Fix 4: Repair the component store with DISM

With pending work cleared and extras removed, repair whatever drift and corruption remains in the store itself. DISM's RestoreHealth reconciles WinSxS against known-good sources, and StartComponentCleanup removes the superseded versions that complicate matching.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /StartComponentCleanup`.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to completion.
4. Follow with `sfc /scannow` for the protected-file layer.
5. Restart and retry the update.

### Fix 5: Reset the update pipeline and its metadata

Corrupted servicing metadata — the engine's map of what is installed — can report mismatches that do not really exist. Renaming SoftwareDistribution and catroot2 forces Windows to rebuild both the download cache and the cryptographic catalog the engine matches against.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the three services.
5. Check for updates in Settings > Windows Update and let it rebuild its metadata before retrying.

### Fix 6: Install the update manually, then repair in place if needed

Two-stage fallback: first try the standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), which bypasses the automatic pipeline's matching path. If even the manual install reports the mismatch, escalate to an in-place upgrade that rebuilds the entire servicing baseline while keeping your files and apps.

1. Find the KB number in Settings > Windows Update > Update history.
2. Download the matching package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and run it.
3. If it fails with the same mismatch, create the Windows 11 installation media.
4. Run setup.exe, choose Keep personal files and apps, and complete the in-place upgrade.
5. Afterward, cumulative updates install against the rebuilt baseline. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the repair-install process if you need a walkthrough.

### Fix 7: Install the update in Safe Mode with Networking

Safe Mode starts Windows with a minimal driver and service set, which strips away the third-party filters and half-configured features that confuse the servicing matcher. If the update installs cleanly in Safe Mode, the mismatch was environmental rather than structural — and you can then hunt the interfering program at leisure.

1. Hold Shift while clicking Start > Power > Restart.
2. Choose Troubleshoot > Advanced options > Startup Settings > Restart.
3. Press 5 for Safe Mode with Networking.
4. Open Settings > Windows Update and install the pending update.
5. Restart normally afterward and verify the update persisted.

## Closing

Error 0x800f0989 is a disagreement between the update and your system's component inventory — pending operations, half-toggled features, and stale language packs are the usual points of contention. Settle each one decisively and servicing finds the familiar baseline it needs. On Windows 11, the restart cycle plus feature tidying resolves most cases long before the in-place upgrade becomes necessary.
