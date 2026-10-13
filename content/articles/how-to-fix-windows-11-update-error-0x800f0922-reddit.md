---
title: "Windows 11 Update Error 0x800f0922: The Fix Reddit Keeps Missing"
slug: how-to-fix-windows-11-update-error-0x800f0922-reddit
date: 2026-09-16
categories: ["windows-update"]
tags: ["0x800f0922", "update error", "efi partition", "windows 11", "reddit"]
description: "Error 0x800f0922 blocking your Windows 11 update? It's usually the EFI partition or .NET — here's the targeted fix sequence."
thumbnail: "/images/thumbs/how-to-fix-windows-11-update-error-0x800f0922-reddit.webp"
faqs:
  - q: "What does error 0x800f0922 actually mean?"
    a: "It's a Component-Based Servicing failure during the install phase. In practice, on Windows 11 it almost always means one of two things: the EFI system partition is too small for the update to stage boot files, or the .NET Framework servicing state is broken. The error text won't tell you which — you check both, EFI first."
  - q: "How big should the EFI partition be to avoid 0x800f0922?"
    a: "Microsoft's own guidance effectively requires around 100 MB free in the EFI partition for updates to stage. Many older installs have a 100 MB EFI partition that's nearly full. If yours shows less than ~50 MB free, that's your culprit — free space or extend it before retrying the update."
  - q: "Can 0x800f0922 be caused by .NET Framework issues?"
    a: "Yes — the second classic cause. If the .NET servicing state is corrupt, cumulative updates that include .NET payloads fail with this code. The .NET Framework repair tool and toggling the .NET Windows features off/on resolve it. Check EFI space first since it's the more common trigger, then move to .NET."
  - q: "Will fixing the EFI partition risk my ability to boot?"
    a: "Not if you only free space within it (deleting stale boot entries, old manufacturer folders) rather than resizing blindly. Don't delete the Microsoft boot folder or the partition itself. If you're extending the partition, use reputable partition tools and back up first — but most cases are solved by cleanup alone."
---

Error 0x800f0922 has a reputation on Reddit as the update error with forty different 'fixes,' most of which do nothing — because most of them target generic update corruption while 0x800f0922 is a specific failure with specific causes. The threads that actually solve it converge on two culprits: an EFI system partition too cramped to stage boot files, and a broken .NET Framework servicing state. Everything else is noise.

This guide skips the noise. You'll check the EFI partition first (five minutes, highest hit rate), then the .NET state, then the standard servicing repairs as backup. If your cumulative update is failing with a different code, the broader [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-to-install-reddit/) covers the full family.

Note the exact KB that's failing and confirm the code is really 0x800f0922 in Update history — misread codes send you down the wrong path.

## Why this happens

- **EFI partition too small or full**: The update stages boot files into the EFI partition; ~100 MB total with little free space fails the staging. Aim for at least 50 MB free; below that, staging fails deterministically.
- **Corrupt .NET servicing state**: .NET payloads inside cumulative updates fail when the Framework's servicing metadata is damaged. Microsoft's .NET Repair Tool fixes the servicing registrations this error stems from.
- **Stale manufacturer boot folders**: OEM folders in the EFI partition (old diagnostics, updaters) eat the free space updates need. Remove only folders you can positively identify as obsolete — never touch EFI\Microsoft\Boot.
- **Corrupted update cache**: A bad download can also surface as 0x800f0922 at install-time verification. If a fresh download fails identically, the cause is EFI or .NET rather than the cache.
- **Damaged component store**: WinSxS issues compound the EFI problem — the installer needs both healthy. Run DISM before retrying; a damaged store makes even a roomy EFI partition fail.
- **Pending operations blocking staging**: Leftover pending.xml entries prevent the boot-file staging phase. A cache reset plus reboot clears these stale entries in most cases.
- **Third-party disk tools interfering**: Some disk utilities lock the EFI partition or alter its layout, breaking staging. If you recently repartitioned, verify the EFI partition is still FAT32 and flagged as a system partition.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Inspect the EFI partition's free space

Diagnosis before surgery. Know your numbers. Diagnosis before surgery. Know your numbers.

1. Open Disk Management (Win + X → Disk Management) and identify the EFI System Partition (usually 100 MB, FAT32).
2. Admin Command Prompt: `mountvol y: /s` to mount it, then `dir y:` to see contents and `fsutil volume diskfree y:` for free space.
3. If free space is under ~50 MB, you've found it — proceed to Fix 2.
4. If space looks fine, skip to Fix 3 (.NET) — don't touch the EFI partition unnecessarily. When done inspecting, `mountvol y: /d` to unmount.
5. Write down the exact free-space figure — you will compare it after cleanup to confirm progress.

### Fix 2: Free space inside the EFI partition safely

Cleanup, not resizing, solves most cases. Cleanup, not resizing, solves most cases.

1. With the partition mounted (Fix 1), look in `y:\EFI` for stale OEM folders — old manufacturer diagnostics, updater remnants — and delete only what you can positively identify as obsolete.
2. Never touch `y:\EFI\Microsoft\Boot` — that's your actual bootloader.
3. Aim for 50+ MB free; unmount with `mountvol y: /d`.
4. Retry the update. If cleanup can't free enough, extending the partition is the next step (back up first).
5. When in doubt about a folder's purpose, leave it — deleting the wrong EFI entry breaks booting.

### Fix 3: Repair the .NET Framework servicing state

The second classic 0x800f0922 cause. The second classic 0x800f0922 cause.

1. Download Microsoft's .NET Framework Repair Tool and run it (it fixes servicing registrations).
2. Alternatively: Control Panel → Programs → Turn Windows features on/off → uncheck **.NET Framework 3.5** and **4.8 Advanced Services** → reboot → re-check them → reboot.
3. Retry the cumulative update.
4. If .NET was the cause, the install proceeds past the point where it previously failed.
5. Run the repair tool twice if the first pass reports fixes — .NET repairs sometimes need two passes.

### Fix 4: Reset the update cache

Rule out the corrupted-download variant of this error. Rule out the corrupted-download variant of this error.

1. Admin Command Prompt: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`; `ren C:\Windows\System32\catroot2 catroot2.old`.
3. `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
4. Re-download and retry the update. Full procedure: [reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/).
5. A fresh download that fails identically points firmly at EFI or .NET rather than the cache.

### Fix 5: Run DISM and SFC for the servicing layer

Backup repair for when EFI and .NET both check out. Backup repair for when EFI and .NET both check out.

1. Admin Command Prompt: `DISM /Online /Cleanup-Image /RestoreHealth`.
2. `sfc /scannow`; restart.
3. Retry the update.
4. Persistent 0x800f0922 after clean EFI + healthy store is rare — note it for escalation.
5. If SFC finds unfixable corruption, the component store needs an ISO-sourced repair before updates can proceed.

### Fix 6: Install the KB manually from the Update Catalog

Bypass the pipeline to isolate the cause. Bypass the pipeline to isolate the cause.

1. Find the failing KB on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Install the x64 .msu as administrator; reboot.
3. If manual install hits the same 0x800f0922, the cause is systemic (EFI/.NET/store) — keep working Fixes 2–5.
4. If it succeeds, the pipeline was contributing — monitor next month's update.
5. A manual install that throws the same code is valuable evidence, not a wasted attempt — it narrows the field.

### Fix 7: Extend the EFI partition (last resort)

Only if cleanup can't free enough space and everything else is healthy. Only if cleanup cannot free enough space and everything else is healthy.

1. Back up the entire system (system image or reliable third-party backup).
2. Use a reputable partition manager to extend the EFI partition to 260+ MB, or follow Microsoft's documented procedure for this error.
3. Verify the system still boots before attempting the update.
4. Retry the update — with room to stage, 0x800f0922 clears.
5. After extending, boot twice normally before attempting the update — confirm stability first.

## Closing

0x800f0922 looks cryptic but it's one of the most diagnosable update errors: check EFI free space, clean it safely, repair .NET, then fall back to the standard servicing repairs. The Reddit threads eventually get there — this guide just starts there. Related guides: [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-to-install-reddit/) and [reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/).
