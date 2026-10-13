---
title: "Error 0x800f0922 on Windows 11? The Step-by-Step Fix"
slug: how-to-fix-windows-11-update-error-0x800f0922-step-by-step
date: 2026-10-09
categories: ["windows-update"]
tags: ["0x800f0922", "update error", "step by step", ".net framework", "windows 11"]
description: "Stuck on Windows 11 update error 0x800f0922? This condensed step-by-step checklist takes you from diagnosis to a working update in under an hour."
thumbnail: "/images/thumbs/how-to-fix-windows-11-update-error-0x800f0922-step-by-step.webp"
faqs:
  - q: "How is this different from the full 0x800f0922 guide?"
    a: "This is the condensed checklist version — same fixes, stripped to the essential steps in the order that resolves the error fastest. If you want the full explanations of why each fix works, plus HP-specific angles, see our complete 0x800f0922 guide. Use this page when you just want to get it done."
  - q: "Which fix resolves 0x800f0922 most often?"
    a: "Repairing the .NET Framework 3.5 feature state. In the majority of cases we've seen, the update fails while trying to service a half-enabled or damaged .NET 3.5 installation. Toggling the feature off and on — or reinstalling it from installation media — clears the error."
  - q: "Can I skip straight to the manual install?"
    a: "You can, and it sometimes works, but if the underlying cause is a full EFI partition or broken .NET state, the manual installer will fail with the same code. The checklist order exists because the quick diagnostic steps take five minutes and save you from a wasted manual attempt."
  - q: "Does this error mean my Windows installation is damaged?"
    a: "Not necessarily. 0x800f0922 is a servicing prerequisite failure, not a verdict on your whole OS. The component store repair step (DISM/SFC) addresses the cases where servicing itself is damaged, and only if that reports unrepairable corruption should you consider bigger measures."
---

You want the fix, not the lecture. Error 0x800f0922, Windows 11 update failing, here is the checklist in the order that works. Each step takes a few minutes; most people are done by step 3. If a step's one-line context does not apply to you, skip it — but do not reorder them, because each step eliminates a cause the later steps assume is gone.

Quick orientation: 0x800f0922 means a servicing operation failed — usually .NET Framework 3.5 state, a full EFI/recovery partition, or a corrupt payload. The checklist below hunts those three. For the deep-dive version with full explanations, see our [complete 0x800f0922 guide](/articles/how-to-fix-windows-11-update-error-0x800f0922-on-hp-laptop/).

Estimated time for the full checklist: 30–60 minutes, most of it waiting on DISM and downloads. Have your Windows 11 installation media (or ISO download link) handy before you start — Fix 2's offline .NET repair needs it, and hunting for it mid-repair breaks your momentum. Keep the charger plugged in throughout; servicing operations interrupted by power loss create exactly the kind of damage you're here to fix.

## Why this happens

- **Broken .NET Framework 3.5 state**: The top cause — servicing trips over a half-enabled .NET 3.5.
- **Full EFI system partition**: No room to write boot files during servicing.
- **Full recovery partition**: WinRE staging fails for lack of space.
- **Corrupt update payload**: Damaged download fails verification mid-install.
- **Antivirus filter drivers**: Third-party AV aborting servicing operations.
- **Damaged component store**: WinSxS corruption failing every servicing call.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failing component in the CBS log

Two minutes of diagnosis saves twenty of guessing.

1. Open `C:\Windows\Logs\CBS\CBS.log`, search for `0x800f0922`. The log is huge — use Ctrl+F and start from the most recent match, since old entries from months ago will mislead you.
2. Read the lines above the match: `NetFx3` mentions mean .NET trouble (go to Fix 2); partition or staging errors mean space trouble (go to Fix 3). If the log names a specific package (like a KB number), note it — you'll need it for the manual install in Fix 7 if it comes to that.
3. Can't find the code in the log at all? Then the failure happened before servicing even started — check the Windows Update log via Event Viewer (**Windows Logs > System**, source "WindowsUpdateClient") for the download or scan failure instead.

### Fix 2: Reset the .NET Framework 3.5 feature

The fix that resolves most 0x800f0922 cases.

1. Open **Control Panel > Programs > Turn Windows features on or off**.
2. Uncheck **.NET Framework 3.5 (includes .NET 2.0 and 3.0)**, restart, re-check it, restart again.
3. If the online enable fails, mount a Windows 11 ISO and run in elevated Terminal: `DISM /Online /Enable-Feature /FeatureName:NetFx3 /All /Source:X:\sources\sxs /LimitAccess` (X: = mounted ISO).
4. Retry the update.

### Fix 3: Check EFI and recovery partition space

Servicing fails silently when these are full.

1. In elevated Terminal: `mountvol Y: /s`, then check Y:'s free space in File Explorer. A healthy EFI partition usually has tens of megabytes free; single digits is a red flag.
2. Clean stale boot entries if full: `bcdedit /enum firmware` lists them, and orphaned entries from long-removed OS installs are safe to delete. Check the recovery partition in Disk Management too — if it's at 0 bytes free, the update cannot stage its WinRE changes.
3. Microsoft's partition-space guidance for failed updates is at the [Windows update support hub](https://support.microsoft.com/en-us/windows).
4. Retry the update once both have breathing room. If the EFI partition refills quickly, something is writing boot files repeatedly — investigate before the next Patch Tuesday rather than after it fails.

### Fix 4: Get a clean payload

Rule out the corrupt download.

1. Elevated Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` → `SoftwareDistribution.old`; rename `catroot2` similarly.
3. Restart the services; check for updates for a fresh download.

### Fix 5: Remove antivirus interference

Filter drivers are a known servicing-killer.

1. Temporarily **uninstall** third-party antivirus (disabling often isn't enough).
2. Verify Microsoft Defender is active.
3. Retry the update; reinstall your AV after success.

### Fix 6: Repair the component store

For when servicing itself is damaged.

1. Elevated Terminal: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. Restart and retry the update.
3. After the repair, check `C:\Windows\Logs\CBS\CBS.log` for fresh `0x800f0922` entries — there should be none. If the update installs now, the repair was the fix; only continue to Fix 7 if the same code returns, which proves the package path is the problem rather than your system.

### Fix 7: Install the KB manually

The bypass when the automatic path is the problem.

1. Copy the KB number from **Update history**.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and run the `.msu` with peripherals disconnected.

## Closing

That is the whole checklist: log, .NET, partitions, cache, AV, component store, manual install. Error 0x800f0922 looks intimidating but it is a prerequisite problem, and prerequisites are fixable. Work it once, note which step fixed it, and you will recognize it instantly if it ever returns.

Keep this page bookmarked rather than memorizing it — 0x800f0922 is uncommon enough that you'll forget the details between encounters, and the checklist order matters more than any single step. Each encounter also teaches you something about your machine's servicing health: which prerequisite failed, and why. That knowledge compounds, turning an intimidating hex code into a familiar, solvable maintenance task. Next time it appears, you'll go straight to the CBS log, identify the failing prerequisite in two minutes, and fix it in twenty. That's the difference between troubleshooting and flailing: a written procedure, followed in order. Print it, bookmark it, or just remember the sequence — log, .NET, partitions, cache, AV, repair, manual — and this error loses its power to ruin your afternoon. And if a failed attempt ever strands you in the endless "undoing changes" loop instead of a clean rollback, our [undoing-changes recovery guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/) picks up exactly there.
