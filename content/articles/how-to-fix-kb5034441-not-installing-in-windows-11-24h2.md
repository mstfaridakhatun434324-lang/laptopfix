---
title: "KB5034441 Not Installing on Windows 11 24H2? Fix the WinRE Update Failure"
slug: how-to-fix-kb5034441-not-installing-in-windows-11-24h2
date: 2026-09-04
categories: ["windows-update"]
tags: ["kb5034441", "winre", "0x80070643", "recovery partition", "windows 11 24h2"]
description: "Fix KB5034441 failing with 0x80070643: resize the Windows Recovery Environment partition and get this security update installed."
thumbnail: "/images/thumbs/how-to-fix-kb5034441-not-installing-in-windows-11-24h2.webp"
faqs:
  - q: "What is KB5034441 and why does it keep failing?"
    a: "KB5034441 is a security update for the Windows Recovery Environment that patches a BitLocker bypass vulnerability. It fails with error 0x80070643 when the recovery partition is too small to hold the updated WinRE image, which is the case on most factory-partitioned laptops."
  - q: "Is it safe to skip KB5034441?"
    a: "Skipping leaves a known BitLocker encryption bypass unpatched in your recovery environment. It is not an emergency for most home users, but the fix is straightforward and worth doing rather than ignoring a security update indefinitely. The vulnerability it patches requires physical access to exploit, so the real-world risk for most home users is low but not zero."
  - q: "How big does the recovery partition need to be?"
    a: "Microsoft's guidance calls for at least 250 megabytes of free space inside the recovery partition for the updated WinRE image. Most failing machines have far less, which is why resizing the partition is the definitive fix. When in doubt, give it more rather than less — recovery partitions are small by nature, and extra headroom prevents the next WinRE update from failing the same way."
  - q: "Will resizing partitions delete my data?"
    a: "Shrinking the OS partition to grow the recovery partition is safe when done with built-in tools and the steps below, but any partition operation carries some risk. Back up important files first, keep the charger connected, and never interrupt the process."
---

KB5034441 is the update that refuses to die: a Windows Recovery Environment security patch that fails with error 0x80070643 on machine after machine, retrying forever. The cause is refreshingly specific — your recovery partition is too small for the new WinRE image — and the fix is equally specific: make the partition bigger. No amount of cache-clearing or troubleshooter-running will help, because the problem is geometry, not corruption.

This guide walks the exact partition-resize procedure Microsoft documents, plus the checks that confirm it worked and the fallback for machines where resizing is not practical.

## Why this happens

- **Undersized recovery partition:** Factory partitioning typically leaves the WinRE partition just big enough for the original image, with no room for the patched, larger one KB5034441 installs.
- **WinRE image growth:** The security fix adds code to winre.wim, and the installer needs roughly 250 MB of free space in the partition to stage and apply it.
- **0x80070643 on staging failure:** When staging fails for lack of space, the installer reports the generic 0x80070643 error, which sends people down the wrong troubleshooting path.
- **BitLocker-encrypted drives:** The update must work around encryption, and tight partitions leave no room for the temporary files the process needs.
- **OEM custom recovery tools:** Some makers add their own tools to the recovery partition, eating the little free space that existed.
- **Previously shrunk partitions:** Disk-management experiments that shrank the recovery partition "to gain space" come back to haunt the machine here.
- **Stale WinRE configuration:** A WinRE registered at the wrong partition or disabled entirely confuses the installer about where to apply the update.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the diagnosis with reagentc

1. Open an elevated Command Prompt and run `reagentc /info` — note the Windows RE location and confirm its status is **Enabled**.
2. Run `diskpart`, then `list disk`, `select disk 0`, `list partition` — find the Recovery partition and note its size.
3. If the recovery partition is under ~600 MB total or shows almost no free space, the diagnosis is confirmed: geometry, not corruption.
4. Run `reagentc /disable` before any partition work — never resize the partition while WinRE is registered to it.

### Fix 2: Shrink the OS partition to make room

1. Still in diskpart (as admin), run `list volume`, identify the OS volume (usually C:), then `select volume C` — or use the volume number shown.
2. Run `shrink desired=250 minimum=250` to carve 250 MB of unallocated space after the OS partition.
3. If shrink fails for lack of movable space, run Disk Cleanup and defragment-adjacent steps first: delete temp files, empty the recycle bin, and disable hibernation temporarily with `powercfg /h off`.
4. Verify with `list partition` that unallocated space now exists immediately after the OS partition.

### Fix 3: Delete and recreate a larger recovery partition

1. In diskpart, `select` the old recovery partition and run `delete partition override` — this is safe because you disabled WinRE in Fix 1.
2. Create the new one: `create partition primary`, then `format quick fs=ntfs label="Windows RE tools"`.
3. Set its identity: `set id=de94bba4-06d1-4d40-a16a-bfd50179d6ac` and `gpt attributes=0x8000000000000001`.
4. Run `list partition` to confirm the new recovery partition is roughly 250 MB larger than the old one.

### Fix 4: Re-enable WinRE on the new partition

1. Run `reagentc /enable` in the elevated prompt — this copies the WinRE image into the new, roomier partition.
2. Run `reagentc /info` again and confirm status is **Enabled** with the new partition's location.
3. If enable fails, your winre.wim may be damaged — extract a fresh copy from Windows installation media and retry.
4. Only proceed when `reagentc /info` shows a healthy, enabled recovery environment.

### Fix 5: Install KB5034441 fresh

1. Open **Settings > Windows Update** and click **Check for updates** — KB5034441 should now download and install without 0x80070643.
2. If Windows Update still offers a stale failed state, clear it: stop the update services, rename SoftwareDistribution, restart services, and check again.
3. For a direct approach, download KB5034441 from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install the standalone package.
4. Confirm success in **Update history** — the entry should show "Successfully installed."

### Fix 6: Verify the recovery environment still works

1. After the update, run `reagentc /info` one final time to confirm WinRE remains enabled.
2. Test booting to recovery: **Settings > System > Recovery > Advanced startup > Restart now**, and confirm the recovery menu appears.
3. If recovery does not boot, re-run `reagentc /disable` then `reagentc /enable` to re-register the image.
4. A working recovery environment is the whole point of this update — verify it, since a [broken recovery path](/articles/best-way-to-fix-windows-update-troubleshooter-not-working/) undermines every other repair tool.

### Fix 7: The fallback — scripted resize for repeat attempts

1. If manual diskpart work feels risky, Microsoft published a sample script that automates the shrink-and-recreate procedure — run it from an elevated prompt exactly as documented.
2. The script handles the reagentc disable/enable dance automatically, reducing the chance of sequencing mistakes.
3. After the script completes, retry KB5034441 via Windows Update before trying anything else.
4. Keep your drivers current afterward — a healthy update pipeline matters, and our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/) covers the vendor-first approach that avoids future conflicts.

### Fix 8: Hide the update when resizing is not practical

1. If the laptop uses BitLocker with no recovery key available, or the disk layout cannot safely be resized, hiding KB5034441 is the pragmatic fallback.
2. Download Microsoft's **Show or Hide Updates** troubleshooter (wushowhide.diagcab), run it, choose **Hide updates**, and select KB5034441.
3. Understand the tradeoff: the WinRE BitLocker-bypass vulnerability stays unpatched, so treat physical security of the laptop more carefully.
4. Revisit the decision every six months — a future Windows build may enlarge the recovery partition automatically during upgrade, at which point unhide the update and install it.

## Closing

KB5034441 fails for one reason — a recovery partition too small for the patched image — and the fix is one procedure: disable WinRE, shrink the OS volume, recreate the recovery partition larger, re-enable WinRE, install the update. It is partition surgery, so back up first and follow the sequence exactly. Do it once and this particular 0x80070643 will never darken your update history again.
