---
title: "KB5034441 Won't Install on Your Lenovo? Fix the Recovery Partition"
slug: how-to-fix-kb5034441-not-installing-on-lenovo-laptop
date: 2026-10-08
categories: ["windows-update"]
tags: ["kb5034441", "lenovo", "winre", "0x80070643", "windows update"]
description: "Fix KB5034441 failing with 0x80070643 on a Lenovo laptop: resize the WinRE recovery partition step by step and let the security update install."
thumbnail: "/images/thumbs/how-to-fix-kb5034441-not-installing-on-lenovo-laptop.webp"
faqs:
  - q: "Why does KB5034441 fail with error 0x80070643?"
    a: "KB5034441 updates the Windows Recovery Environment, and it needs at least 250 MB of free space in the recovery partition. Most factory partitions are too small, so the update fails with 0x80070643 every time. The fix is enlarging the WinRE partition, not retrying the download."
  - q: "Is it safe to resize the recovery partition myself?"
    a: "Yes, if you follow the diskpart sequence carefully and back up first. You are shrinking the main Windows partition slightly and giving that space to a new, larger recovery partition. Thousands of users have done this successfully, but a typo in diskpart can delete the wrong partition."
  - q: "Can I just hide KB5034441 and skip it?"
    a: "You can hide it with Microsoft's show/hide troubleshooter, and your laptop will work fine. But you lose the WinRE security fix, so resizing the partition is the better long-term answer. Hiding is a reasonable stopgap while you prepare."
  - q: "How do I check my WinRE partition size on a Lenovo?"
    a: "Open an elevated Command Prompt and run reagentc /info to see the recovery location and status, then open diskmgmt.msc to view partition sizes graphically. If the recovery partition shows under 500 MB total or nearly zero free space, it is almost certainly too small for KB5034441 to install."
---

KB5034441 is a special kind of headache. It is a security update for the Windows Recovery Environment (WinRE), and on Lenovo laptops it fails again and again with error 0x80070643. Retrying the download changes nothing, because the download is fine — the problem is that your recovery partition is physically too small to hold the updated recovery image.

This is one of the few update failures with a single, well-understood cause. Microsoft's own guidance is to resize the WinRE partition, and that is exactly what we will do: disable WinRE, shrink the Windows partition slightly, build a bigger recovery partition, re-enable WinRE, and install the update.

## Why this happens

- **Undersized factory recovery partition:** Lenovo's factory WinRE partitions are often 500 MB or less, but KB5034441 needs roughly 250 MB of *free* space inside it.
- **WinRE image growth:** The update adds patched components to winre.wim, and the image has grown past what the old partition layout allows.
- **No automatic resizing:** Windows Update cannot resize partitions on its own, so the install fails instead of making room.
- **BitLocker interplay:** On encrypted systems, partition operations need the recovery key handy, and WinRE must be disabled before diskpart touches anything.
- **Multiple recovery partitions:** Some Lenovos carry leftover recovery partitions from factory resets, confusing the reagentc location mapping.
- **The 0x80070643 misdirection:** The error code suggests a fatal install error, sending users down generic troubleshooting paths that cannot help. Unlike generic [update install failures](/articles/how-to-fix-windows-update-error-after-clean-install-on-lenovo-laptop/), this one is purely a space problem.
- **Staged update retries:** Each failed attempt re-downloads and re-stages the package, wasting time and disk space without ever addressing the partition.
- **OEM custom WinRE images:** Lenovo's customized recovery image can be larger than stock, leaving even less headroom than on other brands.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the diagnosis with reagentc

1. Open an elevated Command Prompt and run `reagentc /info` — note the Windows RE location and whether it is enabled.
2. Open **Disk Management** (`diskmgmt.msc`) and find the Recovery partition; check its size.
3. If it is under about 650 MB total, or shows nearly full, the diagnosis is confirmed: KB5034441 cannot fit.
4. Also run `reagentc /info` output to disk or a photo — you will want the original location for reference.

### Fix 2: Back up and prepare

1. Back up your personal files to an external drive or cloud storage. Partition work is low-risk when done right, but backups are non-negotiable.
2. If BitLocker is on, save your recovery key from your Microsoft account before touching partitions.
3. Plug in the charger — a power loss during partition changes is the one thing that can genuinely break the system.
4. Download nothing yet; the update itself will come from Windows Update once the partition is ready.

### Fix 3: Disable WinRE and shrink the OS partition

1. In the elevated Command Prompt, run `reagentc /disable` to take WinRE offline.
2. Type `diskpart`, then `list disk`, `select disk 0` (your system disk), and `list partition`.
3. Select the Windows OS partition (`select partition N`) and run `shrink desired=750 minimum=750` to free 750 MB.
4. Type `exit` to leave diskpart. You now have unallocated space sitting after the Windows partition.

### Fix 4: Remove the old WinRE partition and create a larger one

1. Back in diskpart, `list partition` and `select partition N` for the old Recovery partition.
2. Run `delete partition override` to remove it — this is the point of no return, so double-check the selection.
3. Create the new one: `create partition primary id=de94dbba-06d1-4d40-a16a-bfd50179d6ac` followed by `gpt attributes=0x8000000000000001`.
4. Format it with `format quick fs=ntfs label="Windows RE tools"` and `exit` diskpart.

### Fix 5: Re-enable WinRE on the new partition

1. In the elevated Command Prompt, run `reagentc /enable`.
2. Run `reagentc /info` again and confirm the location now points at the new, larger partition and status shows Enabled.
3. If it fails, the partition ID or attributes are wrong — repeat Fix 4 carefully.
4. Lenovo's support site documents WinRE behavior for ThinkPad and IdeaPad models at the [Lenovo support portal](https://support.lenovo.com/us/en/) if your layout differs.

### Fix 6: Install KB5034441 from Windows Update

1. Open **Settings → Windows Update** and click **Check for updates**.
2. KB5034441 should now download and install without the 0x80070643 error.
3. Reboot when prompted and verify in **Update history** that it shows as successfully installed.
4. If it still fails, re-check free space with `reagentc /info` — some systems need the partition closer to 1 GB.

### Fix 7: Hide the update as a last resort

1. If partition resizing is not possible on your disk layout, download Microsoft's "Show or hide updates" troubleshooter from the [Windows support hub](https://support.microsoft.com/en-us/windows).
2. Run it, choose **Hide updates**, and select KB5034441.
3. This stops the endless fail-retry cycle while keeping everything else updating normally.
4. Revisit the partition fix later when you have time — the security update is worth installing properly. If other updates fail with different codes in the meantime, the [0x800f0831 repair guide](/articles/how-to-fix-windows-update-error-0x800f0831-in-windows-11-24h2/) covers the next most common install error.

### Fix 8: Verify WinRE actually works after the resize

1. After KB5034441 installs, test recovery: hold **Shift** while clicking **Restart** to boot into WinRE.
2. Confirm the recovery menus load and offer **Troubleshoot** options — this proves the new partition is functional.
3. Back in Windows, run `reagentc /info` one final time and save a screenshot of the healthy output.
4. Future WinRE updates will now have the headroom they need, so this class of failure should not return.

## Closing

KB5034441's 0x80070643 failure on Lenovo laptops is not a mystery and not a broken update — it is a partition that is too small, full stop. Disable WinRE, carve 750 MB from the OS partition, rebuild a larger recovery partition, re-enable WinRE, and the update installs cleanly. An hour of careful diskpart work ends months of failed update notifications.
