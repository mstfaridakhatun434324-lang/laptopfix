---
title: "How to Fix Windows Update Error 0x800f0989 on Windows 10"
slug: how-to-fix-windows-update-error-0x800f0989-on-windows-10
date: 2026-10-02
categories: ["windows-update"]
tags: ["windows update", "0x800f0989", "cumulative update", "servicing", "windows 11"]
description: "Error 0x800f0989 on Windows 10 signals a servicing mismatch between the update package and installed components. Clear it with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0989-on-windows-10.webp"
faqs:
  - q: "What is the difference between 0x800f0989 and 0x800f0988?"
    a: "Both are PSFX mismatch errors on Windows 10 with largely shared causes — language packs, store drift, interrupted updates. In practice 0x800f0988 tracks most closely to language-pack problems, while 0x800f0989 shows up more with unfinished operations and half-configured optional features. The repair sequence is nearly identical, which is why these steps mirror the sibling guide."
  - q: "What are pending servicing operations?"
    a: "They are update tasks recorded in pending.xml that Windows has not yet completed — usually because the machine was never properly restarted. Until they finish or roll back, components sit in a transitional state new updates cannot match, yielding 0x800f0989. A genuine Restart (not Shut down) lets servicing complete the outstanding work."
  - q: "Can optional features really break Windows Update?"
    a: "Yes. Features like .NET Framework 3.5 add components each cumulative update must reckon with; a half-enabled feature leaves those components in an indeterminate state. The Windows Features dialog (`optionalfeatures`) lets you set every feature firmly on or off, clearing the ambiguous records servicing chokes on."
  - q: "How do I know the in-place upgrade is necessary?"
    a: "When the restart cycle, feature tidying, language removal, DISM repair, pipeline reset, and manual install have all been performed correctly, and 0x800f0989 still blocks the same update. Then the servicing baseline itself is at fault, and only rebuilding it through an in-place upgrade (keeping files and apps) ends the mismatch."
---
Windows 10 raises error 0x800f0989 when the servicing stack examines an update package and finds it incompatible with the components installed on your machine. The package itself is fine, and your installation is fine — they simply disagree, usually because an earlier operation never finished, an optional feature sits half-configured, or the component store shifted after an interrupted update.

The comforting part is atomicity: servicing validates before committing, so a rejected update changes nothing at all. Your task is to eliminate whatever makes your system look foreign to the update — unfinished work, orphaned features, store damage — in the order below.

The [Windows 11 edition](/articles/how-to-fix-windows-update-error-0x800f0989-on-windows-11/) covers this error on Windows 11, and the [sibling guide for 0x800f0988](/articles/how-to-fix-windows-update-error-0x800f0988-on-windows-10/) handles the closely related code. Start by clearing out anything pending.

## Why this happens

- **Servicing operations never finished:** entries recorded in pending.xml from an update that never got its reboot leave components in a transitional state new updates cannot match.
- **Optional features are stuck halfway:** .NET Framework 3.5, leftover Hyper-V pieces, or media features toggled incompletely leave component records in limbo that servicing rejects packages over.
- **A prior update was cut off mid-commit:** power loss or a forced shutdown during the commit phase splits component versions across the store, so the next update matches neither half.
- **Stale language packs add surprise variants:** like its sibling error, unneeded or partially installed language packs introduce component variants the package does not describe.
- **The store has accumulated drift:** months of updates, cleanups, and third-party tweaks gradually push WinSxS away from any baseline the update recognizes.
- **Servicing metadata is corrupted:** damaged metadata can make the engine misread which components exist, manufacturing a mismatch out of healthy files.
- **Disk faults damaged servicing records:** bad sectors in the servicing tree corrupt manifests and pending-operation records, producing mismatch errors rooted in physically damaged bookkeeping.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Finish pending work with a proper restart cycle

Check update history first: an entry demanding a restart is your smoking gun.

1. Open Settings > Update & Security > Windows Update > Update history and look for updates awaiting a restart.
2. Choose Start > Power > Restart — skip Shut down, since Fast Startup would bypass the commit.
3. After the reboot, give background servicing five minutes to settle.
4. Reopen Settings > Update & Security > Windows Update and confirm the pending state cleared.
5. Attempt the failed update again only once the restart cycle is done.

### Fix 2: Put optional Windows features in a decisive state

Pay extra attention to .NET Framework 3.5 — many installers toggle it during their own setups.

1. Press Win + R, enter `optionalfeatures`, and hit Enter.
2. Fully uncheck each feature you do not need and click OK.
3. If .NET Framework 3.5 shows a partial state, turn it completely on, restart, then turn it completely off and restart again.
4. Wait for Windows to apply the changes — several minutes is normal.
5. Reboot once more, then attempt the update again via Settings > Update & Security > Windows Update.

### Fix 3: Remove surplus language packs

This pairs well with the feature cleanup above: both shrink the system to the configuration updates are actually built against.

1. Head to Settings > Time & language > Language.
2. Remove every preferred language except your display language.
3. Restart so servicing registers the simplified configuration.
4. Try the cumulative update once more from Settings > Update & Security > Windows Update.
5. Reinstall a language later only if you truly need it — each one reintroduces matching surface.

### Fix 4: Repair the component store with DISM

This is the deep-clean step for accumulated drift the tidying fixes cannot reach.

1. Start an administrator Command Prompt.
2. Run `DISM /Online /Cleanup-Image /StartComponentCleanup`.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` until it finishes.
4. Follow that with `sfc /scannow` to cover the protected-file layer.
5. Restart and attempt the update again.

### Fix 5: Reset the pipeline and its metadata

Fresh metadata combined with a repaired store gives the update a truthful, accurate picture of your machine.

1. Open a Command Prompt with admin rights.
2. Halt the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the three services with `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Check for updates in Settings > Update & Security > Windows Update and let the metadata rebuild before retrying.

### Fix 6: Try the manual install, then repair in place if needed

Most 0x800f0989 cases resolve at one stage or the other — very few make it past both.

1. Locate the KB number in Settings > Update & Security > Windows Update > Update history.
2. Fetch the matching package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and run it.
3. If the same mismatch appears, create the Windows 10 Media Creation Tool.
4. Launch setup.exe, select Keep personal files and apps, and finish the in-place upgrade.
5. Afterward, cumulative updates target the rebuilt baseline. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the repair-install process if you want a walkthrough.

### Fix 7: Attempt the update in Safe Mode with Networking

Safe Mode with Networking loads only essential drivers and services while keeping downloads working. In this minimal state, servicing sidesteps the feature and filter-driver conditions that trigger 0x800f0989, matching the update against the cleanest component set available.

1. Hold down Shift while clicking Start > Power > Restart.
2. Select Troubleshoot > Advanced options > Startup Settings > Restart.
3. Hit 5 to enter Safe Mode with Networking.
4. Open Settings > Update & Security > Windows Update and run the pending update.
5. Restart normally afterward and confirm the update stuck.

## Closing

On Windows 10, this PSFX sibling yields to the same discipline: finish what is pending, settle what is half-configured, repair what has drifted. Neither the update nor your system is broken — they just need to agree on the inventory. Work the list, and agreement follows.
